"""Stage 7 — Submission (integration test).

Three phases:
  7a: Replication audit — re-run all scripts, compare outputs.
  7b: Integration validation — cross-stage consistency checks.
  7c: Final quality gate — validators + component scores must all pass.
  7d: Journal targeting (only if gate passes).
"""

import hashlib
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

from ..config import (
    CLO_AUTHOR, SUBMISSION_GATE, COMPONENT_MIN, QUALITY_WEIGHTS,
    MAX_STAGE7_IMPROVE, get_profile,
)
from ..claude_runner import run_claude
from ..json_utils import extract_json
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
                str(project_dir / "paper" / "sections"),
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
        stage3 = state["stages"].get("stage3", {})
        idea_result = stage3.get("result", {})

        targeting_prompt = f"""You are an academic journal targeting advisor.

Paper title: {idea_result.get('title', 'Untitled')}
Method: {idea_result.get('method', 'N/A')}
Field: Economics (empirical)

Referee scores:
- Domain referee: {stage6.get('domain_score', '?')}/100
- Methods referee: {stage6.get('methods_score', '?')}/100
- Editorial decision: {stage6.get('decision', '?')}

Quality gate: PASSED (aggregate {aggregate:.1f}/100)

Recommend:
1. Primary target journal (name, why it fits, typical turnaround)
2. Backup journal (name, why it's a realistic fallback)
3. Conference presentation targets (2-3 conferences)

Output a JSON block:
```json
{{
  "primary_journal": {{"name": "...", "fit_reason": "...", "turnaround_months": 6}},
  "backup_journal": {{"name": "...", "fit_reason": "..."}},
  "conferences": ["..."]
}}
```
"""
        p = get_profile("stage7_targeting")
        resp = run_claude(
            targeting_prompt, model=p["model"], effort=p["effort"],
            output_file=project_dir / "quality_reports" / "journal_targeting.md",
            allowed_tools=[],
        )
        targeting_result = extract_json(resp) or {}
        journal = targeting_result.get("primary_journal", {}).get("name", "?")
        print(f"  [7d] Target journal: {journal}")
    else:
        print("\n  [7d] Skipping journal targeting — gate not passed.")

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
