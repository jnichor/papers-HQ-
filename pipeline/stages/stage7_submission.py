"""Stage 7 — Submission (integration test).

Five phases:
  7a: Replication audit — re-run all scripts, compare outputs.
  7b: Integration validation — cross-stage consistency checks.
  7c: Final quality gate — validators + component scores must all pass.
  7d: Journal targeting (only if gate passes).
  7e: Feedback PDF — detailed diagnostics and improvement recommendations.
"""

import hashlib
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

from ..config import (
    CLO_AUTHOR, SUBMISSION_GATE, COMPONENT_MIN, QUALITY_WEIGHTS,
    MAX_STAGE7_IMPROVE,
)
from ..python_runner import run_python_script
from ..state import save_state
from ..validators.code_validator import validate as validate_code
from ..validators.paper_validator import validate as validate_paper
from ..validators.integration_validator import validate as validate_integration


def _read_file_or(path: Path, default: str = "") -> str:
    return path.read_text(encoding="utf-8") if path.exists() else default


def _hash_file(path: Path) -> str:
    """MD5 hash of a file for output comparison."""
    if not path.exists():
        return ""
    return hashlib.md5(path.read_bytes()).hexdigest()


def run(project_dir: Path, state: dict) -> dict:
    """Execute Stage 7: replication + integration test + final gate."""
    paper_dir = project_dir / "paper"
    scripts_dir = project_dir / "scripts" / "python"
    tables_dir = paper_dir / "tables"
    figures_dir = paper_dir / "figures"
    (project_dir / "quality_reports").mkdir(exist_ok=True)

    # ══════════════════════════════════════════════════════════════════════
    # 7a: REPLICATION AUDIT
    # ══════════════════════════════════════════════════════════════════════
    print("\n  [7a] Replication audit — re-running all scripts...")

    # Snapshot output files BEFORE replication
    pre_hashes = {}
    for d in [tables_dir, figures_dir]:
        if d.exists():
            for f in d.iterdir():
                pre_hashes[str(f.relative_to(project_dir))] = _hash_file(f)

    # Re-execute all scripts in order
    replication_ok = True
    replication_results = {}
    if scripts_dir.exists():
        py_scripts = sorted(scripts_dir.resolve().glob("[0-9]*.py"))
        for script in py_scripts:
            print(f"  [7a] Running {script.name}...")
            result = run_python_script(script, cwd=scripts_dir.resolve())
            replication_results[script.name] = {
                "ok": result["ok"],
                "returncode": result["returncode"],
            }
            if not result["ok"]:
                replication_ok = False
                print(f"  [7a] FAIL: {script.name}")
                stderr = result.get("stderr", "")
                if stderr:
                    print(f"        {stderr[:200]}")
    else:
        print("  [7a] No scripts directory found.")
        replication_ok = False

    # Snapshot output files AFTER replication and compare
    post_hashes = {}
    for d in [tables_dir, figures_dir]:
        if d.exists():
            for f in d.iterdir():
                post_hashes[str(f.relative_to(project_dir))] = _hash_file(f)

    changed_outputs = []
    for path, pre_hash in pre_hashes.items():
        post_hash = post_hashes.get(path, "")
        # Skip PDF figures — matplotlib PDFs have non-deterministic internal
        # metadata (font hashes, UUIDs) even with identical visual content.
        if path.endswith(".pdf") and "figures" in path:
            continue
        if pre_hash != post_hash:
            changed_outputs.append(path)

    disappeared = set(pre_hashes.keys()) - set(post_hashes.keys())
    new_files = set(post_hashes.keys()) - set(pre_hashes.keys())

    print(f"  [7a] Replication: {'PASS' if replication_ok else 'FAIL'}")
    if changed_outputs:
        print(f"  [7a] WARNING: {len(changed_outputs)} output(s) changed on re-run:")
        for c in changed_outputs[:5]:
            print(f"        - {c}")
    if disappeared:
        print(f"  [7a] WARNING: {len(disappeared)} output(s) disappeared on re-run")
    if not changed_outputs and not disappeared and replication_ok:
        print(f"  [7a] All outputs are reproducible (identical hashes).")

    # ══════════════════════════════════════════════════════════════════════
    # 7b: INTEGRATION VALIDATION
    # ══════════════════════════════════════════════════════════════════════
    print("\n  [7b] Running 3 validators in parallel...")

    # Run all three validators concurrently (pure Python, no Claude calls)
    with ThreadPoolExecutor(max_workers=3) as pool:
        f_code = pool.submit(
            validate_code, scripts_dir, project_dir,
            {name: res for name, res in replication_results.items()},
        )
        f_paper = pool.submit(
            validate_paper, paper_dir, project_dir,
            compiled=(paper_dir / "main.pdf").exists(),
        )
        f_integration = pool.submit(validate_integration, project_dir)

    code_val = f_code.result()
    paper_val = f_paper.result()
    integration_val = f_integration.result()

    print(f"  [7b] Code validator:        {code_val.format_for_log()}")
    print(f"  [7b] Paper validator:       {paper_val.format_for_log()}")
    print(f"  [7b] Integration validator: {integration_val.format_for_log()}")

    # Collect all hard failures across validators
    all_hard_failures = (
        code_val.hard_failures
        + paper_val.hard_failures
        + integration_val.hard_failures
    )
    all_validators_pass = len(all_hard_failures) == 0

    if all_hard_failures:
        print(f"\n  [7b] HARD FAILURES ({len(all_hard_failures)}):")
        for fail in all_hard_failures:
            print(f"        - {fail.name}: {fail.detail}")

    # ══════════════════════════════════════════════════════════════════════
    # 7c: FINAL QUALITY GATE
    # ══════════════════════════════════════════════════════════════════════
    print("\n  [7c] Final quality gate...")

    # Gather component scores from previous stages
    stage4a = state["stages"].get("stage4a", {})
    stage4bc = state["stages"].get("stage4bc", {})
    stage5 = state["stages"].get("stage5", {})
    stage6 = state["stages"].get("stage6", {})

    code_score = stage4bc.get("critic_score", 0)
    if code_score == 0 and replication_ok:
        code_score = 75

    # Identification score: use stage4a critic_score if available,
    # otherwise derive from the method's causal design tier
    ident_score = stage4a.get("critic_score", 0)
    if ident_score == 0:
        # Fallback: score based on method keywords in strategy
        from .stage4_strategy import _score_identification
        ident_score = _score_identification(state)

    # Adjust identification score based on peer review feedback:
    # If referees gave a very different assessment, blend the scores
    polish_score = stage6.get("avg_score", 0)
    if polish_score > 0 and ident_score > 0:
        # If referees score is much lower than identification score,
        # they likely disagree with the identification credibility.
        # Blend: 80% identification + 20% peer review signal
        if polish_score < ident_score - 15:
            ident_score = int(ident_score * 0.8 + polish_score * 0.2)

    components = {
        "identification": ident_score,
        "code": code_score,
        "paper": stage5.get("critic_score", 0),
        "polish": stage6.get("avg_score", 0),
        "replication": 100 if (replication_ok and not changed_outputs) else
                       50 if replication_ok else 0,
    }

    # Weighted aggregate
    aggregate = sum(
        components.get(k, 0) * w
        for k, w in QUALITY_WEIGHTS.items()
    )

    # Component minimums
    below_min = {k: v for k, v in components.items() if v < COMPONENT_MIN}

    # Gate decision: ALL must pass
    gate_passed = (
        aggregate >= SUBMISSION_GATE
        and not below_min
        and all_validators_pass
        and replication_ok
        and not changed_outputs
    )

    # Print report
    print(f"\n  {'=' * 60}")
    print(f"  FINAL QUALITY REPORT")
    print(f"  {'=' * 60}")
    print(f"  Aggregate score:    {aggregate:.1f}/100 (gate: {SUBMISSION_GATE})")
    print(f"  Validators:         {'PASS' if all_validators_pass else 'FAIL'}"
          f" ({len(all_hard_failures)} hard failures)")
    print(f"  Replication:        {'PASS' if replication_ok else 'FAIL'}")
    print(f"  Reproducibility:    "
          f"{'PASS' if not changed_outputs else 'FAIL'}"
          f" ({len(changed_outputs)} changed outputs)")
    print(f"  {'-' * 60}")
    for k, v in components.items():
        weight = QUALITY_WEIGHTS.get(k, 0)
        status = "PASS" if v >= COMPONENT_MIN else "FAIL"
        print(f"  [{status}] {k:20s}: {v:5.1f}/100 (weight: {weight:.0%})")
    print(f"  {'-' * 60}")
    print(f"  GATE: {'PASSED' if gate_passed else 'FAILED'}")
    print(f"  {'=' * 60}")

    if not gate_passed:
        reasons = []
        if aggregate < SUBMISSION_GATE:
            reasons.append(f"aggregate {aggregate:.1f} < {SUBMISSION_GATE}")
        if below_min:
            reasons.append(
                f"below component minimum: "
                + ", ".join(f"{k}={v}" for k, v in below_min.items())
            )
        if not all_validators_pass:
            reasons.append(f"{len(all_hard_failures)} hard validation failure(s)")
        if not replication_ok:
            reasons.append("replication failed")
        if changed_outputs:
            reasons.append(f"{len(changed_outputs)} non-reproducible output(s)")
        print(f"\n  Reasons: {'; '.join(reasons)}")

    # Save detailed validation report
    report_lines = [
        "# Stage 7 — Integration Test Report",
        f"\nDate: {datetime.now().isoformat()}",
        f"\n## Gate: {'PASSED' if gate_passed else 'FAILED'}",
        f"Aggregate: {aggregate:.1f}/{SUBMISSION_GATE}",
        f"\n## Component Scores",
    ]
    for k, v in components.items():
        report_lines.append(f"- {k}: {v}/100")
    report_lines.append(f"\n## Replication")
    report_lines.append(f"- Scripts ran: {'Yes' if replication_ok else 'No'}")
    report_lines.append(f"- Outputs reproducible: {'Yes' if not changed_outputs else 'No'}")
    if changed_outputs:
        report_lines.append(f"- Changed: {', '.join(changed_outputs)}")
    report_lines.append(f"\n## Code Validation\n{code_val.format_for_critic()}")
    report_lines.append(f"\n## Paper Validation\n{paper_val.format_for_critic()}")
    report_lines.append(
        f"\n## Integration Validation\n{integration_val.format_for_critic()}"
    )

    report_path = project_dir / "quality_reports" / "integration_test_report.md"
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"\n  [7] Full report: {report_path}")

    # ══════════════════════════════════════════════════════════════════════
    # 7e: USER DECISION — accept or improve
    # ══════════════════════════════════════════════════════════════════════
    print(f"\n  {'=' * 60}")
    print(f"  What would you like to do?")
    print(f"  {'=' * 60}")
    print(f"  [1] Accept aggregate score ({aggregate:.1f}/100) — paper finished")
    print(f"  [2] Improve paper — manual intervention to raise score")
    print(f"  {'=' * 60}")
    print("\a", end="", flush=True)  # Terminal bell — user input needed

    user_choice = ""
    while user_choice not in ("1", "2"):
        user_choice = input("\n  Enter your choice (1 or 2): ").strip()
        if user_choice not in ("1", "2"):
            print("  Please enter 1 or 2.")

    if user_choice == "2":
        # Save improvement request for manual intervention
        improvement_file = project_dir / "quality_reports" / "improvement_request.md"
        improvement_lines = [
            "# Improvement Request",
            f"\nDate: {datetime.now().isoformat()}",
            f"Current aggregate: {aggregate:.1f}/100",
            f"\n## Current Component Scores",
        ]
        for k, v in components.items():
            improvement_lines.append(f"- {k}: {v}/100")
        improvement_lines.append(f"\n## Areas for Improvement")
        improvement_lines.append(
            "Review the issues in the following files and address them manually:"
        )
        improvement_lines.append(
            f"- Identification: quality_reports/identification_review.md"
        )
        improvement_lines.append(f"- Code: quality_reports/code_review.md")
        improvement_lines.append(f"- Paper: quality_reports/paper_review.md")
        improvement_lines.append(f"- Polish: quality_reports/peer_review.md")
        improvement_lines.append(
            f"\n## Instructions"
        )
        improvement_lines.append(
            "1. Claude (in conversation) will read the review files and make "
            "improvements to the paper sections, scripts, and tables."
        )
        improvement_lines.append(
            "2. After improvements, update the review files with new scores."
        )
        improvement_lines.append(
            "3. Re-run Stage 7 to get the updated Final Quality Report."
        )
        improvement_file.write_text(
            "\n".join(improvement_lines), encoding="utf-8"
        )

        # Signal manual intervention and WAIT
        from ..claude_runner import request_manual_intervention
        request_manual_intervention(
            stage="stage7_improvement",
            issue=(
                f"Stage 7: User chose to improve paper. Aggregate={aggregate:.1f}/100. "
                f"Tell Claude: 'revisa el pipeline'. Claude will read the review files, "
                f"improve the paper/scripts, update scores, and signal completion."
            ),
            files=[
                str(project_dir / "quality_reports" / "integration_test_report.md"),
                str(project_dir / "quality_reports"),
                str(project_dir / "paper" / "main.tex"),
                str(project_dir / "scripts" / "python"),
            ],
            project_dir=project_dir,
        )

        # After intervention: re-run Stage 7 (with depth limit)
        improve_count = state["stages"].get("stage7", {}).get("improve_count", 0) + 1
        state.setdefault("stages", {}).setdefault("stage7", {})["improve_count"] = improve_count

        if improve_count > MAX_STAGE7_IMPROVE:
            print(f"\n  [7] Maximum improvement rounds ({MAX_STAGE7_IMPROVE}) reached. Proceeding as-is.")
        else:
            print(f"\n  [7] Re-running Stage 7 after improvements (round {improve_count}/{MAX_STAGE7_IMPROVE})...")
            state = run(project_dir, state)
            return state

    # ══════════════════════════════════════════════════════════════════════
    # User chose [1] — Accept score, proceed to journal targeting
    # ══════════════════════════════════════════════════════════════════════
    print(f"\n  Score accepted. Proceeding to finalize...")

    # ══════════════════════════════════════════════════════════════════════
    # 7d: JOURNAL TARGETING (only if gate passes)
    # ══════════════════════════════════════════════════════════════════════
    targeting_result = {}
    if gate_passed:
        print("\n  [7d] Journal targeting...")

        # Deterministic journal targeting based on score tiers
        # No Claude call needed — this is a simple lookup
        if aggregate >= 85:
            primary = {"name": "Journal of Political Economy", "fit_reason": "Top-5 general interest, strong empirical work", "turnaround_months": 6}
            backup = {"name": "Review of Economics and Statistics", "fit_reason": "Top field journal for empirical methods", "turnaround_months": 5}
            conferences = ["NBER Summer Institute", "AEA Annual Meeting", "ASSA"]
        elif aggregate >= 75:
            primary = {"name": "Journal of Economic Behavior & Organization", "fit_reason": "Strong fit for empirical tech/labor papers", "turnaround_months": 4}
            backup = {"name": "Information Economics and Policy", "fit_reason": "Specialized in technology and economics", "turnaround_months": 3}
            conferences = ["AEA Annual Meeting", "WEAI", "European Economic Association"]
        elif aggregate >= 70:
            primary = {"name": "Economics Letters", "fit_reason": "Fast turnaround, accepts concise empirical contributions", "turnaround_months": 2}
            backup = {"name": "Applied Economics Letters", "fit_reason": "Regional/applied journal, good for null results", "turnaround_months": 2}
            conferences = ["WEAI", "Southern Economic Association", "Midwest Economics Association"]
        else:
            primary = {"name": "Working Paper Series", "fit_reason": "Paper needs more work before journal submission", "turnaround_months": 0}
            backup = {"name": "SSRN / arXiv", "fit_reason": "Preprint to establish priority while revising", "turnaround_months": 0}
            conferences = ["Departmental seminar", "Brown bag lunch series"]

        targeting_result = {
            "primary_journal": primary,
            "backup_journal": backup,
            "conferences": conferences,
        }

        # Save to file
        targeting_file = project_dir / "quality_reports" / "journal_targeting.md"
        targeting_text = (
            f"# Journal Targeting\n\n"
            f"Aggregate score: {aggregate:.1f}/100\n\n"
            f"## Primary Target\n"
            f"**{primary['name']}** — {primary['fit_reason']} "
            f"(~{primary['turnaround_months']} months turnaround)\n\n"
            f"## Backup Target\n"
            f"**{backup['name']}** — {backup['fit_reason']}\n\n"
            f"## Conference Targets\n"
            + "\n".join(f"- {c}" for c in conferences)
        )
        targeting_file.write_text(targeting_text, encoding="utf-8")

        print(f"  [7d] Target journal: {primary['name']}")
    else:
        print("\n  [7d] Skipping journal targeting — gate not passed.")

    # ══════════════════════════════════════════════════════════════════════
    # 7e: FEEDBACK PDF
    # ══════════════════════════════════════════════════════════════════════
    print("\n  [7e] Generating feedback.pdf...")
    try:
        _generate_feedback_pdf(
            project_dir, state, components, aggregate, gate_passed,
            all_hard_failures, replication_ok, changed_outputs,
            code_val, paper_val, integration_val,
        )
    except Exception as e:
        print(f"  [7e] WARNING: feedback.pdf generation failed: {e}")

    # ══════════════════════════════════════════════════════════════════════
    # SAVE STATE
    # ══════════════════════════════════════════════════════════════════════
    state["stages"]["stage7"] = {
        "status": "completed",
        "replication_ok": replication_ok,
        "replication_results": replication_results,
        "outputs_reproducible": len(changed_outputs) == 0,
        "changed_outputs": changed_outputs,
        "validation": {
            "code": code_val.summary_counts,
            "paper": paper_val.summary_counts,
            "integration": integration_val.summary_counts,
            "all_hard_pass": all_validators_pass,
            "total_hard_failures": len(all_hard_failures),
        },
        "components": components,
        "aggregate_score": round(aggregate, 1),
        "gate_passed": gate_passed,
        "below_minimum": below_min,
        "targeting": targeting_result,
        "user_choice": "accept",
        "completed_at": datetime.now().isoformat(),
    }

    state["current_stage"] = 7
    save_state(project_dir, state)

    # Final summary
    final_pdf = paper_dir / "main.pdf"
    if gate_passed:
        print(f"\n  Paper is submission-ready.")
        print(f"  PDF: {final_pdf}")
    else:
        print(f"\n  Paper needs more work before submission.")
        print(f"  Review: {report_path}")

    return state


# ══════════════════════════════════════════════════════════════════════════════
# FEEDBACK PDF GENERATOR
# ══════════════════════════════════════════════════════════════════════════════

def _generate_feedback_pdf(
    project_dir, state, components, aggregate, gate_passed,
    hard_failures, replication_ok, changed_outputs,
    code_val, paper_val, integration_val,
):
    """Generate feedback.pdf with detailed diagnostics and recommendations."""
    from fpdf import FPDF

    class FeedbackPDF(FPDF):
        def header(self):
            self.set_font("Helvetica", "B", 10)
            self.set_text_color(100, 100, 100)
            self.cell(0, 8, "Papers-HQ Feedback Report", align="R", new_x="LMARGIN", new_y="NEXT")
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(4)

        def footer(self):
            self.set_y(-15)
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(128, 128, 128)
            self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

        def section_title(self, title):
            self.set_font("Helvetica", "B", 14)
            self.set_text_color(0, 51, 102)
            self.ln(6)
            self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
            self.set_draw_color(0, 51, 102)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(4)

        def sub_title(self, title):
            self.set_font("Helvetica", "B", 11)
            self.set_text_color(51, 51, 51)
            self.ln(3)
            self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
            self.ln(1)

        def body_text(self, text):
            self.set_font("Helvetica", "", 10)
            self.set_text_color(0, 0, 0)
            safe = text.encode("latin-1", errors="replace").decode("latin-1")
            self.multi_cell(0, 5, safe)
            self.ln(2)

        def score_bar(self, label, score, weight=None):
            x = self.get_x()
            y = self.get_y()
            self.set_font("Helvetica", "", 10)
            label_text = f"{label}"
            if weight:
                label_text += f" ({int(weight*100)}%)"
            self.cell(55, 6, label_text)
            bar_x = x + 55
            bar_w = 100
            self.set_fill_color(230, 230, 230)
            self.rect(bar_x, y, bar_w, 6, "F")
            fill_w = max(0, min(bar_w, bar_w * score / 100))
            if score >= 80:
                self.set_fill_color(76, 175, 80)
            elif score >= 70:
                self.set_fill_color(255, 193, 7)
            else:
                self.set_fill_color(244, 67, 54)
            self.rect(bar_x, y, fill_w, 6, "F")
            self.set_xy(bar_x + bar_w + 2, y)
            self.set_font("Helvetica", "B", 10)
            self.cell(20, 6, f"{score:.0f}/100")
            self.ln(8)

    pdf = FeedbackPDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # Title
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(0, 51, 102)
    title = state["stages"].get("stage3", {}).get("result", {}).get("title", "Untitled")
    safe_title = title.encode("latin-1", errors="replace").decode("latin-1")
    pdf.multi_cell(0, 10, safe_title, align="C")
    pdf.ln(3)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, "Feedback & Improvement Report", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 6, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(8)

    # ── 1. SCORE BREAKDOWN ──
    pdf.section_title("1. Score Breakdown")
    pdf.body_text(
        f"Aggregate score: {aggregate:.1f}/100  |  "
        f"Gate: {'PASSED' if gate_passed else 'FAILED'}  |  "
        f"Threshold: {SUBMISSION_GATE}/100"
    )
    for comp_name, comp_score in components.items():
        weight = QUALITY_WEIGHTS.get(comp_name, 0)
        pdf.score_bar(comp_name.title(), comp_score, weight)

    pdf.ln(4)
    pdf.sub_title("What each score means")
    explanations = {
        "identification": (
            "Measures the credibility of the causal design. Depends on: valid control group, "
            "flat pre-trends, exogenous treatment, and addressed confounders. "
            "Simultaneous/universal treatments (no control group) cap this at ~85."
        ),
        "code": (
            "Code quality: scripts run without errors, outputs exist, SE clustering present, "
            "pre-trend tests implemented, and referee checklist requirements addressed."
        ),
        "paper": (
            "Paper completeness: all sections present, references resolve, tables and figures "
            "exist, word count in range, key numbers in abstract match results."
        ),
        "polish": (
            "Average referee score from peer review. Reflects identification credibility, "
            "result presentation, and robustness. Hardest to improve without better data."
        ),
        "replication": (
            "Whether all scripts reproduce identical outputs when re-run. "
            "100 = perfect replication."
        ),
    }
    for comp_name in components:
        exp = explanations.get(comp_name, "")
        if exp:
            pdf.set_font("Helvetica", "B", 10)
            pdf.cell(0, 5, f"{comp_name.title()} ({components[comp_name]:.0f}/100):", new_x="LMARGIN", new_y="NEXT")
            pdf.body_text(exp)

    # ── 2. RESULTS DIAGNOSTICS ──
    pdf.section_title("2. Why the Results Look Like This")

    # Read main results
    main_path = project_dir / "data" / "clean" / "main_results.csv"
    if main_path.exists():
        import csv
        with open(main_path, encoding="utf-8") as f:
            main_rows = list(csv.DictReader(f))
        if main_rows:
            pdf.sub_title("Main findings")
            for r in main_rows[:6]:
                spec = r.get("specification", r.get("estimator", r.get("label", "?")))
                # Find the coefficient column
                coef = None
                for col_name in ["coef", "att", "ATT", "estimate", "coefficient"]:
                    if col_name in r and r[col_name]:
                        try:
                            coef = float(r[col_name])
                            break
                        except (ValueError, TypeError):
                            pass
                p_val = None
                for col_name in ["p_value", "p", "pval", "Pr(>|t|)"]:
                    if col_name in r and r[col_name]:
                        try:
                            p_val = float(r[col_name])
                            break
                        except (ValueError, TypeError):
                            pass
                if coef is not None:
                    sig = ""
                    if p_val is not None:
                        sig = " (p=%.4f)%s" % (p_val, " ***" if p_val < 0.01 else " **" if p_val < 0.05 else " *" if p_val < 0.1 else "")
                    pdf.body_text("  %s: coef = %+.4f%s" % (spec[:60], coef, sig))

    # Read robustness results
    robustness_path = project_dir / "data" / "clean" / "robustness_results.csv"
    if robustness_path.exists():
        import csv
        with open(robustness_path, encoding="utf-8") as f:
            rob_rows = list(csv.DictReader(f))

        if rob_rows:
            pdf.sub_title("Robustness summary")

            # Count how many specs are significant vs not
            sig_count = 0
            insig_count = 0
            for r in rob_rows:
                p_val = None
                for col_name in ["p", "pval", "p_value"]:
                    if col_name in r and r[col_name]:
                        try:
                            p_val = float(r[col_name])
                            break
                        except (ValueError, TypeError):
                            pass
                if p_val is not None:
                    if p_val < 0.05:
                        sig_count += 1
                    else:
                        insig_count += 1

            total = sig_count + insig_count
            if total > 0:
                pdf.body_text(
                    "Of %d robustness specifications: %d significant (p<0.05), "
                    "%d insignificant." % (total, sig_count, insig_count)
                )
                if sig_count == 0:
                    pdf.body_text(
                        "No specification achieves statistical significance. "
                        "This is consistent with a genuine null result or an underpowered study."
                    )
                elif insig_count == 0:
                    pdf.body_text(
                        "All specifications are significant. The result is robust "
                        "across all tested variations."
                    )
                elif sig_count < insig_count:
                    pdf.body_text(
                        "Most specifications are insignificant. The significant results "
                        "may reflect specific subgroups or thresholds rather than a "
                        "general effect."
                    )

            # Show key robustness rows
            pdf.sub_title("Key robustness checks")
            for r in rob_rows[:10]:
                label = r.get("specification", r.get("label", "?"))
                att = None
                for col_name in ["ATT", "att", "coef", "estimate"]:
                    if col_name in r and r[col_name]:
                        try:
                            att = float(r[col_name])
                            break
                        except (ValueError, TypeError):
                            pass
                p_val = None
                for col_name in ["p", "pval", "p_value"]:
                    if col_name in r and r[col_name]:
                        try:
                            p_val = float(r[col_name])
                            break
                        except (ValueError, TypeError):
                            pass
                if att is not None:
                    p_str = " (p=%.3f)" % p_val if p_val is not None else ""
                    pdf.body_text("  %s: %+.4f%s" % (label[:55], att, p_str))

    elif not main_path.exists():
        pdf.body_text("No main_results.csv or robustness_results.csv found.")

    # ── 3. DATA LIMITATIONS ──
    pdf.section_title("3. Data Limitations")

    stage1 = state["stages"].get("stage1", {})
    data_profile = stage1.get("data_profile", {})
    structure = data_profile.get("structure", "unknown")

    pdf.sub_title("Current data")
    pdf.body_text(
        "Rows: %s  |  Columns: %s  |  Structure: %s" % (
            "{:,}".format(data_profile.get("rows", 0)) if data_profile.get("rows") else "?",
            data_profile.get("cols", "?"),
            structure,
        )
    )

    # Generate limitations based on actual data structure
    selected_idea = state["stages"].get("stage2_5", {}).get("selected_idea", {})
    id_level = selected_idea.get("identification_level", "")
    method = selected_idea.get("method", "").lower()

    limitations = []

    # Structure-specific limitations
    if structure == "cross-sectional":
        limitations.append((
            "Cross-sectional data",
            "Single time snapshot. Cannot control for time-invariant unobservables "
            "or track changes over time. Causal claims rely entirely on "
            "randomization or instrumental variable assumptions."
        ))
    elif structure in ("panel", "wide-panel"):
        limitations.append((
            "Panel attrition",
            "If units drop out of the panel over time, the remaining sample may be "
            "non-representative. Check attrition rates and Lee bounds."
        ))

    # Design-specific limitations
    if "rct" in method or "experiment" in method or "randomiz" in method or id_level == "A":
        limitations.append((
            "External validity",
            "Experimental results may not generalize beyond the study sample. "
            "The specific population, setting, and time period limit extrapolation."
        ))
        limitations.append((
            "Demand effects",
            "Survey/lab experiments may be subject to demand effects where "
            "respondents guess the hypothesis and adjust their responses."
        ))
    elif id_level == "C" or "simultaneous" in method:
        limitations.append((
            "No control group",
            "All units received the same treatment simultaneously. Cannot separate "
            "the treatment effect from other concurrent shocks."
        ))

    # Sample size limitations
    rows = data_profile.get("rows", 0)
    if rows and rows < 1000:
        limitations.append((
            "Small sample",
            "With N=%d, the study may be underpowered to detect small but "
            "meaningful effects. Report minimum detectable effect (MDE)." % rows
        ))

    # Referee feedback limitations
    stage6 = state["stages"].get("stage6", {})
    must_issues = []
    review_dir = project_dir / "reviews"
    if review_dir.exists():
        for dec_file in sorted(review_dir.glob("editorial_decision*.md"), reverse=True):
            try:
                import json as _json
                dec_text = dec_file.read_text(encoding="utf-8")
                dec_data = _json.loads(dec_text.strip().strip("`").strip("json").strip())
                must_issues = dec_data.get("must_address", [])[:3]
                break
            except Exception:
                pass

    if must_issues:
        limitations.append((
            "Unresolved referee concerns",
            "The following issues were flagged by referees and may limit the "
            "paper's publishability: " + "; ".join(m[:80] for m in must_issues)
        ))

    if not limitations:
        limitations.append((
            "General",
            "All empirical studies have limitations. Consult the referee feedback "
            "for specific concerns about this paper."
        ))

    for lim_title, lim_text in limitations:
        pdf.sub_title(lim_title)
        pdf.body_text(lim_text)

    # ── 4. VALIDATOR RESULTS ──
    pdf.section_title("4. Validator Results")
    for val_name, val_obj in [("Code", code_val), ("Paper", paper_val), ("Integration", integration_val)]:
        counts = val_obj.summary_counts
        pdf.sub_title(
            f"{val_name}: hard {counts.get('hard_pass', 0)}/{counts.get('hard_total', 0)}, "
            f"soft {counts.get('soft_pass', 0)}/{counts.get('soft_total', 0)}"
        )
        for check in val_obj.checks:
            if not check.passed:
                pdf.body_text(f"  [FAIL] {check.name}: {check.detail}")

    # ── 5. RECOMMENDATIONS ──
    pdf.section_title("5. Recommendations to Improve Score")

    # Read peer review must-address issues
    review_dir = project_dir / "reviews"
    must_issues = []
    if review_dir.exists():
        for dec_file in sorted(review_dir.glob("editorial_decision*.md"), reverse=True):
            try:
                import json as _json
                dec_text = dec_file.read_text(encoding="utf-8")
                dec_data = _json.loads(dec_text.strip().strip("`").strip("json").strip())
                must_issues = dec_data.get("must_address", [])
                break
            except Exception:
                pass

    # Show referee must-address issues first (most actionable)
    if must_issues:
        pdf.sub_title("[FROM REFEREES] Must-address issues from peer review")
        for i, issue in enumerate(must_issues[:8], 1):
            safe = issue.encode("latin-1", errors="replace").decode("latin-1")
            pdf.body_text("  %d. %s" % (i, safe[:200]))

    # Generic recommendations based on component scores
    recs = []
    if components.get("identification", 0) < 90:
        recs.append((
            "HIGH IMPACT", "Improve identification strategy",
            "Add exogenous variation: natural experiments, policy discontinuities, "
            "staggered rollout, or instrumental variables. RCTs score highest."
        ))
    if components.get("code", 0) < 90:
        recs.append((
            "MEDIUM IMPACT", "Improve code quality",
            "Address referee checklist gaps. Use validated packages (pyfixest, "
            "linearmodels) instead of manual implementations. Add missing "
            "robustness checks flagged by the code validator."
        ))
    if components.get("paper", 0) < 90:
        recs.append((
            "MEDIUM IMPACT", "Expand paper content",
            "Target 8,000-12,000 words. Ensure abstract contains exact key numbers "
            "matching results_summary. Add data appendix with variable definitions."
        ))
    if components.get("polish", 0) < 80:
        recs.append((
            "LOW IMPACT (depends on above)", "Address referee feedback",
            "Polish improves when identification and code improve. "
            "Focus on must-address issues listed above."
        ))

    for priority, rec_title, detail in recs:
        pdf.sub_title("[%s] %s" % (priority, rec_title))
        pdf.body_text(detail)

    # ── 6. SCORE IMPROVEMENT ESTIMATES ──
    pdf.section_title("6. Estimated Score Impact")

    improvements = []
    if components.get("identification", 0) < 90:
        improvements.append(("Stronger identification (RCT or natural experiment)", "+10 to +20 identification"))
    if components.get("code", 0) < 85:
        improvements.append(("Fix code validator soft failures", "+5 to +10 code"))
    if components.get("paper", 0) < 85:
        improvements.append(("Expand paper to 8,000+ words", "+5 paper"))
        improvements.append(("Ensure abstract numbers match results", "+3 paper, +3 integration"))
    if components.get("polish", 0) < 80:
        improvements.append(("Address all referee must-address issues", "+5 to +10 polish"))
    improvements.append(("Address all SHOULD-address issues", "+3 to +5 polish"))

    for improvement, impact in improvements:
        pdf.body_text("  %s:  %s" % (improvement, impact))

    # Estimate ceiling
    id_score = components.get("identification", 0)
    if id_score >= 90:
        ceiling = 92
    elif id_score >= 80:
        ceiling = 88
    elif id_score >= 70:
        ceiling = 82
    else:
        ceiling = 75

    pdf.ln(4)
    pdf.body_text(
        "Current aggregate: %.1f/100. "
        "Estimated ceiling with current data: ~%d. "
        "To reach 90+: need RCT or strong natural experiment data." % (aggregate, ceiling)
    )

    # Save
    output_path = project_dir / "feedback.pdf"
    pdf.output(str(output_path))
    print(f"  [7e] Saved: {output_path}")
