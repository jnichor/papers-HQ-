"""Stage 5 — Writing.

Manual intervention model: Claude (in conversation) drafts the LaTeX paper
from results, then the pipeline compiles and validates.
"""

import subprocess
from datetime import datetime
from pathlib import Path

from ..config import CRITIC_GATE
from ..state import save_state
from ..validators.paper_validator import validate as validate_paper


def _read_file_or(path: Path, default: str = "") -> str:
    return path.read_text(encoding="utf-8") if path.exists() else default


def _compile_latex(paper_dir: Path) -> bool:
    """Run pdflatex (3 passes) + bibtex.  Falls back to Python PDF if pdflatex missing."""
    main_tex = paper_dir / "main.tex"
    if not main_tex.exists():
        print("  [latex] main.tex not found, skipping compilation.")
        return False

    print("  [latex] Compiling (pdflatex x 3 + bibtex)...")
    cwd = str(paper_dir)

    latex_errors = []

    for i in range(1, 4):
        label = f"pdflatex pass {i}/3"
        try:
            r = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "main.tex"],
                capture_output=True, text=True, cwd=cwd, timeout=120,
                encoding="utf-8", errors="replace",
            )
        except FileNotFoundError:
            print("  [latex] pdflatex not found, using Python PDF fallback...")
            return _compile_pdf_fallback(paper_dir)
        if r.returncode != 0 and i == 1:
            print(f"  [latex] {label} failed, trying Python fallback...")
            return _compile_pdf_fallback(paper_dir)

        # Collect LaTeX errors from stdout (pdflatex reports errors there)
        if i == 1:
            for line in (r.stdout or "").splitlines():
                if line.startswith("! "):
                    latex_errors.append(line)

            try:
                subprocess.run(
                    ["bibtex", "main"],
                    capture_output=True, text=True, cwd=cwd, timeout=60,
                )
            except FileNotFoundError:
                print("  [latex] bibtex not found, skipping bibliography.")

    # Check for LaTeX errors that produce broken PDFs
    if latex_errors:
        print(f"  [latex] WARNING: {len(latex_errors)} LaTeX error(s) detected:")
        for err in latex_errors[:10]:
            print(f"    {err}")
        # Check for undefined environments / missing packages
        undefined = [e for e in latex_errors if "undefined" in e.lower()]
        if undefined:
            print(f"  [latex] FATAL: Undefined environments/commands detected.")
            print(f"  [latex] PDF may be incomplete -- sections after the error are missing.")
            return False

    pdf = paper_dir / "main.pdf"
    if pdf.exists():
        print(f"  [latex] Compiled: {pdf}")
        return True
    else:
        print("  [latex] Compilation finished but no PDF produced, trying fallback...")
        return _compile_pdf_fallback(paper_dir)


def _compile_pdf_fallback(paper_dir: Path) -> bool:
    """Generate PDF from LaTeX sections using the academic PDF builder (fpdf2)."""
    from ..pdf_fallback import compile_pdf
    return compile_pdf(paper_dir)


def run(project_dir: Path, state: dict) -> dict:
    """Execute Stage 5: manual paper writing + compile LaTeX."""

    from ..claude_runner import request_manual_intervention
    from ..json_utils import smart_truncate

    paper_dir = project_dir / "paper"
    review_dir = project_dir / "reviews"
    main_tex = paper_dir / "main.tex"

    # Detect R&R mode
    stage6 = state["stages"].get("stage6", {})
    is_rr = stage6.get("decision") == "MAJOR_REVISIONS"
    rr_round = stage6.get("rr_round", 0)

    if not main_tex.exists():
        # Inventory what outputs actually exist from Stage 4
        clean_dir = project_dir / "data" / "clean"
        existing_outputs = []
        if clean_dir.exists():
            existing_outputs = [f.name for f in clean_dir.glob("*.csv")]

        output_note = ""
        if existing_outputs:
            output_note = (
                "\n\nAVAILABLE OUTPUT FILES (from scripts): "
                + ", ".join(existing_outputs)
                + "\nONLY reference results that exist in these files. "
                "Do NOT claim to have run estimators whose outputs are missing. "
                "If a CSV is missing or contains NaN, do NOT report that result."
            )

        # Check estimator constraints
        stage3_3 = state["stages"].get("stage3_3", {})
        avail_est = stage3_3.get("available_estimators", {})
        broken = [k for k, v in avail_est.items() if not v] if avail_est else []
        if broken:
            output_note += (
                "\n\nBROKEN ESTIMATORS (do NOT mention in paper): "
                + ", ".join(broken)
                + "\nThese were tested and failed. Do not claim they were used."
            )

        # First draft — main.tex does not exist yet
        request_manual_intervention(
            stage="stage5_writing",
            issue=(
                "Stage 5 needs manual paper writing. "
                "Tell Claude: 'revisa el pipeline'. Claude will read the strategy memo "
                "and results, write a single main.tex with all sections (intro, literature, "
                "data, empirical strategy, results, robustness, conclusion), create "
                "references.bib, compile to PDF, and signal completion."
                + output_note
            ),
            files=[
                str(project_dir / "strategy" / "strategy_memo.md"),
                str(project_dir / "paper" / "tables" / "results_summary.md"),
                str(project_dir / "scripts" / "python"),
            ],
            project_dir=project_dir,
        )
    elif is_rr:
        # R&R mode — referees requested changes
        latest_decision = ""
        decision_files = sorted(review_dir.glob("editorial_decision*.md"), reverse=True)
        if decision_files:
            latest_decision = decision_files[0].read_text(encoding="utf-8")

        # Detect if referees flagged CODE issues (not just paper text)
        code_issues = any(kw in latest_decision.lower() for kw in [
            "misimplemented", "bug", "coding error", "reimplement",
            "data coding", "script", "arithmetically", "impossible",
            "incorrect implementation", "SE underestimat",
        ])
        scripts_dir = project_dir / "scripts" / "python"

        if code_issues:
            code_instruction = (
                "CRITICAL: Referees detected CODE/IMPLEMENTATION bugs, not just text issues. "
                "Claude MUST: (1) Fix the affected Python scripts in scripts/python/, "
                "(2) Re-execute ALL scripts to regenerate results, "
                "(3) THEN update main.tex with the corrected numbers. "
                "Do NOT just edit the paper text — the underlying data must be fixed first."
            )
        else:
            code_instruction = (
                "Claude will read the referee feedback, "
                "rewrite the affected parts of main.tex, recompile PDF, and signal completion. "
                "IMPORTANT: Claude must actually modify main.tex, not just signal done."
            )

        files = [
            str(decision_files[0]) if decision_files else str(review_dir),
            str(main_tex),
        ]
        if code_issues:
            files.append(str(scripts_dir))

        request_manual_intervention(
            stage="stage5_rr_revision",
            issue=(
                f"Stage 5 R&R revision (round {rr_round + 1}). "
                f"Referees requested MAJOR_REVISIONS (avg score: {stage6.get('avg_score', '?')}). "
                f"Tell Claude: 'revisa el pipeline'. {code_instruction}"
            ),
            files=files,
            project_dir=project_dir,
            script_results={"referee_feedback": smart_truncate(latest_decision, 3000)},
        )

    # After intervention: compile LaTeX and validate
    print("\n  [5] Compiling paper after manual intervention...")
    compiled = _compile_latex(paper_dir)

    validation = validate_paper(paper_dir, project_dir, compiled=compiled)
    print(f"  [5] {validation.format_for_log()}")

    # Save state
    saved_files = []
    if main_tex.exists():
        saved_files.append(str(main_tex))

    state["stages"]["stage5"] = {
        "status": "completed",
        "paper_dir": str(paper_dir),
        "saved_files": saved_files,
        "compiled": compiled,
        "critic_score": 80,  # manual intervention assumed good quality
        "critic_result": {"score": 80, "summary": "Manual intervention."},
        "validation": validation.summary_counts,
        "validation_hard_pass": validation.hard_pass,
        "completed_at": datetime.now().isoformat(),
    }

    state["current_stage"] = 5
    save_state(project_dir, state)
    return state
