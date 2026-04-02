"""Stage 6 — Peer Review.

Editor desk-reviews the paper, then 2 referees (domain + methods) score it.
If Major Revisions → loop back to Stage 5 writing (max 3 R&R rounds).
"""

from datetime import datetime
from pathlib import Path

from ..config import (
    CLO_AUTHOR, MAX_RR_ROUNDS, ACCEPT_GATE, MINOR_REV_GATE, REJECT_FLOOR,
    get_profile,
)
from ..claude_runner import run_claude, run_claude_parallel
from ..json_utils import extract_json, smart_truncate
from ..state import save_state


def _read_agent(name: str) -> str:
    path = CLO_AUTHOR / ".claude" / "agents" / f"{name}.md"
    return path.read_text(encoding="utf-8") if path.exists() else f"(agent '{name}' not found)"


def _read_file_or(path: Path, default: str = "") -> str:
    return path.read_text(encoding="utf-8") if path.exists() else default


def _consistency_check(project_dir: Path) -> bool:
    """Run a full consistency check on the paper before re-review.

    Uses Claude to read ALL sections, tables, abstract, and result CSVs,
    then fix any internal contradictions (numbers, labels, SE methods,
    cluster counts, specification descriptions).

    Returns True if fixes were made, False if paper was already consistent.
    """
    paper_dir = project_dir / "paper"
    clean_dir = project_dir / "data" / "clean"

    # Gather paper content from main.tex
    sections = {}
    main_tex = paper_dir / "main.tex"
    if main_tex.exists():
        sections["main.tex"] = main_tex.read_text(encoding="utf-8")

    # Gather all tables
    tables = {}
    tables_dir = paper_dir / "tables"
    if tables_dir.exists():
        for f in sorted(tables_dir.glob("*.tex")):
            tables[f.name] = f.read_text(encoding="utf-8")

    # Gather result CSVs (ground truth)
    result_csvs = {}
    if clean_dir.exists():
        for f in ["main_event_study.csv", "scarring_test.csv", "panel_summary.csv",
                   "binary_event_study.csv", "fe_event_study.csv"]:
            fpath = clean_dir / f
            if fpath.exists():
                result_csvs[f] = fpath.read_text(encoding="utf-8")

    if not sections or not result_csvs:
        return False

    # Build the consistency check prompt
    paper_text = ""
    for name, content in sections.items():
        paper_text += f"\n### {name}\n```latex\n{smart_truncate(content, 5000)}\n```\n"
    for name, content in tables.items():
        paper_text += f"\n### TABLE: {name}\n```latex\n{content}\n```\n"

    csv_text = ""
    for name, content in result_csvs.items():
        csv_text += f"\n### {name}\n```csv\n{content}\n```\n"

    prompt = f"""You are a meticulous copy-editor for an academic economics paper.

Your task: find and fix ALL internal inconsistencies in this paper. The result CSV
files are the GROUND TRUTH — the paper text and tables must match them exactly.

## PAPER CONTENT
{paper_text}

## GROUND TRUTH (result CSVs from the analysis scripts)
{csv_text}

## CHECK EACH OF THESE:

1. NUMBERS: Do coefficients, SEs, p-values, and CIs in the text match the CSVs?
   Fix any that don't. The CSV is always correct.

2. SAMPLE SIZE: Is N consistent across abstract, data section, results, and tables?
   Check: n_obs, n_individuals, n_clusters.

3. SE METHOD: Is the standard error method described consistently across ALL sections?
   (e.g., "HC1" vs "clustered" — pick one and use it everywhere)

4. SPECIFICATION: Is the primary specification described the same way in intro,
   strategy, results, and table header? (e.g., "continuous" vs "binary" treatment)

5. CLUSTER COUNT: Is the number of clusters the same everywhere?

6. BASELINE STATISTICS: Do descriptive stats in text match panel_summary.csv?

7. SIGNIFICANCE STARS: Do stars in tables match the p-values in the CSVs?

For EACH inconsistency found, output the fix as:
- File: [filename]
- Old text: [exact text to replace]
- New text: [corrected text]

Output a JSON block:
```json
{{
  "consistent": false,
  "n_fixes": 5,
  "fixes": [
    {{
      "file": "05_results.tex",
      "description": "Coefficient 0.089 should be -0.202 (continuous spec)",
      "old_text": "exact old text here",
      "new_text": "exact new text here"
    }}
  ]
}}
```

If the paper is fully consistent, output:
```json
{{
  "consistent": true,
  "n_fixes": 0,
  "fixes": []
}}
```
"""
    p = get_profile("stage4_critic")
    print("  [consistency] Running full document consistency check...")
    response = run_claude(
        prompt, model=p["model"], effort=p["effort"],
        label="consistency check",
        allowed_tools=[],
    )
    result = extract_json(response) or {}

    if result.get("consistent", True):
        print("  [consistency] Paper is internally consistent. No fixes needed.")
        return False

    fixes = result.get("fixes", [])
    n_applied = 0
    for fix in fixes:
        fname = fix.get("file", "")
        old_text = fix.get("old_text", "")
        new_text = fix.get("new_text", "")
        desc = fix.get("description", "")

        if not fname or not old_text or not new_text or old_text == new_text:
            continue

        # Find the file — all paper content lives in main.tex
        fpath = None
        if fname == "main.tex" or (fname.endswith(".tex") and not fname.startswith("table")):
            fpath = paper_dir / "main.tex"
        elif fname.endswith(".tex"):
            fpath = tables_dir / fname

        if fpath and fpath.exists():
            content = fpath.read_text(encoding="utf-8")
            if old_text in content:
                content = content.replace(old_text, new_text, 1)
                fpath.write_text(content, encoding="utf-8")
                n_applied += 1
                print(f"  [fix] {fname}: {desc[:80]}")
            else:
                print(f"  [skip] {fname}: old text not found (may have been fixed already)")
        else:
            print(f"  [skip] {fname}: file not found")

    print(f"  [consistency] Applied {n_applied}/{len(fixes)} fixes.")
    return n_applied > 0


def _gather_paper(paper_dir: Path) -> str:
    """Read the full paper content for review.

    The paper MUST be sent in full to referees — truncating to only the
    abstract causes referees to request changes that are already present
    in the body text.  We allow up to 50,000 chars for main.tex (covers
    most single-file papers) and 8,000 per section file.
    """
    parts = []
    main_tex = paper_dir / "main.tex"
    if main_tex.exists():
        full_text = main_tex.read_text(encoding="utf-8")
        parts.append(f"## main.tex\n```latex\n{smart_truncate(full_text, 50000)}\n```\n")

    return "\n".join(parts) or "(no paper content found)"


def _gather_evidence_packet(project_dir: Path) -> str:
    """Gather code outputs, data summaries, and audit results for referees.

    This gives referees access to actual evidence so they can verify their
    hypotheses instead of guessing about what the data/code look like.
    """
    parts = []

    # Data audit report (from Stage 4.5)
    audit = project_dir / "quality_reports" / "data_audit.md"
    if audit.exists():
        parts.append(f"## Data Audit Report (Stage 4.5)\n{smart_truncate(audit.read_text(encoding='utf-8'), 3000)}\n")

    # Results summary
    for loc in [
        project_dir / "paper" / "tables" / "results_summary.md",
        project_dir / "scripts" / "python" / "results_summary.md",
    ]:
        if loc.exists():
            parts.append(f"## Results Summary\n{smart_truncate(loc.read_text(encoding='utf-8'), 2000)}\n")
            break

    # Cell sizes
    cell_sizes = project_dir / "data" / "clean" / "cell_sizes.csv"
    if cell_sizes.exists():
        parts.append(f"## Cell Sizes (quintile x insurance)\n```\n{smart_truncate(cell_sizes.read_text(encoding='utf-8'), 1000)}\n```\n")

    # Code validator output
    code_review = project_dir / "quality_reports" / "code_review.md"
    if code_review.exists():
        parts.append(f"## Code Validator Report\n{smart_truncate(code_review.read_text(encoding='utf-8'), 2000)}\n")

    # Table content (actual .tex files)
    tables_dir = project_dir / "paper" / "tables"
    if tables_dir.exists():
        for t in sorted(tables_dir.glob("*.tex"))[:6]:
            content = t.read_text(encoding="utf-8")
            parts.append(f"## Table: {t.name}\n```latex\n{smart_truncate(content, 1500)}\n```\n")

    # Figure list
    figs_dir = project_dir / "paper" / "figures"
    if figs_dir.exists():
        figs = []
        for ext in ["*.pdf", "*.png", "*.jpg", "*.svg"]:
            figs.extend(sorted(figs_dir.glob(ext)))
        if figs:
            parts.append(f"## Figures Available\n" + "\n".join(f"- {f.name}" for f in figs) + "\n")

    return "\n".join(parts) if parts else "(no evidence packet available)"


def run(project_dir: Path, state: dict) -> dict:
    """Execute Stage 6: editorial desk review + 2 referee reports."""
    paper_dir = project_dir / "paper"
    review_dir = project_dir / "reviews"
    review_dir.mkdir(exist_ok=True)
    (project_dir / "quality_reports").mkdir(exist_ok=True)

    # ── Run consistency check before every review round ──────────────
    _consistency_check(project_dir)

    paper_content = _gather_paper(paper_dir)
    strategy_memo = _read_file_or(project_dir / "strategy" / "strategy_memo.md")
    evidence_packet = _gather_evidence_packet(project_dir)

    # Track R&R round
    rr_round = state["stages"].get("stage6", {}).get("rr_round", 0) + 1
    round_suffix = f"_r{rr_round}" if rr_round > 1 else ""

    print(f"  [6] Peer review round {rr_round}/{MAX_RR_ROUNDS}")

    # Build revision context: what changed since last round
    revision_context = ""
    if rr_round > 1:
        # Read previous editorial decision
        prev_suffix = f"_r{rr_round - 1}" if rr_round > 1 else ""
        prev_decision_file = review_dir / f"editorial_decision{prev_suffix}.md"
        if prev_decision_file.exists():
            prev_decision = prev_decision_file.read_text(encoding="utf-8")
            revision_context = f"""
--- PREVIOUS ROUND FEEDBACK (Round {rr_round - 1}) ---
The authors received the following editorial decision and revised the paper.
You are reviewing the REVISED version. Evaluate whether the authors adequately
addressed the previous concerns. Do NOT re-raise issues that have been
satisfactorily resolved.

{smart_truncate(prev_decision, 3000)}

--- END PREVIOUS FEEDBACK ---
"""
        print(f"  [6] Including Round {rr_round - 1} feedback for referee context")

    # ── Editor desk review ───────────────────────────────────────────────
    editor_prompt_text = _read_agent("editor")

    editor_prompt = f"""{editor_prompt_text}

--- PAPER ---
{paper_content}

--- TASK ---
Phase 1: Desk review. Read title, abstract, introduction (first 3 pages).
Decide: proceed to referees, or desk reject?

If proceeding, select 2 referee types (from: STRUCTURAL, CREDIBILITY,
MEASUREMENT, POLICY, THEORY, SKEPTIC) with different dispositions.

Output a JSON block:
```json
{{
  "desk_decision": "PROCEED|DESK_REJECT",
  "reason": "...",
  "referee_1_type": "CREDIBILITY",
  "referee_2_type": "STRUCTURAL"
}}
```
"""

    print("  [6] Editor desk review...")
    pe = get_profile("stage6_editor")
    editor_response = run_claude(
        editor_prompt, model=pe["model"], effort=pe["effort"],
        output_file=review_dir / f"editor_desk{round_suffix}.md",
        allowed_tools=[],
    )
    editor_result = extract_json(editor_response) or {}

    if editor_result.get("desk_decision") == "DESK_REJECT":
        print(f"  [6] DESK REJECT: {editor_result.get('reason', '?')}")
        state["stages"]["stage6"] = {
            "status": "completed",
            "decision": "DESK_REJECT",
            "editor_result": editor_result,
            "rr_round": rr_round,
            "completed_at": datetime.now().isoformat(),
        }
        state["current_stage"] = 6
        save_state(project_dir, state)
        return state

    # ── Domain referee ───────────────────────────────────────────────────
    domain_prompt_text = _read_agent("domain-referee")

    # ── Field-specific calibration context ─────────────────────────────
    field_calibration = """
FIELD-SPECIFIC CALIBRATION (IMPORTANT — read before scoring):

1. STANDARD PRACTICES — Do NOT flag these as errors:
   - Consumption quintiles from total consumption (including health spending)
     is standard in the CHE literature (Xu et al. 2003, Wagstaff 2003).
     It is a known limitation, not a methodological error. Flag as MINOR
     only if the paper fails to acknowledge it.
   - Bootstrap replications of 200 are acceptable for a working paper.
     Flag as MINOR suggestion to increase to 999, not as MAJOR flaw.
   - OLS on fractional [0,1] outcomes is common as a benchmark alongside
     QR. Flag only if no alternative (fractional logit) is discussed.
   - Survey weights applied as frequency weights (rescaled) is standard
     for quantile regression when design-based QR estimators are unavailable.

2. EVIDENCE-BASED REVIEW — Use the data evidence packet below:
   - Before claiming a variable is miscoded, CHECK the cell sizes and
     distribution data provided. If the data confirms the paper's numbers,
     do not speculate about coding errors.
   - Before claiming results are implausible, CHECK the actual regression
     tables and results summary provided.
   - Distinguish between: (a) errors you can VERIFY from the evidence,
     (b) concerns you can only HYPOTHESIZE about. Label hypotheses as
     "possible concern" not "must fix".

3. SCORING GUIDANCE:
   - 70-85: Solid descriptive/observational paper with honest limitations
   - 60-69: Paper with real issues but salvageable with targeted revisions
   - Below 60: Only for fundamental errors VERIFIED in the evidence packet
   - Do NOT score below 60 based on hypothesized errors you cannot verify
"""

    domain_prompt = f"""{domain_prompt_text}

{revision_context}

--- PAPER ---
{paper_content}

--- STRATEGY MEMO (for reference) ---
{smart_truncate(strategy_memo, 2000)}

--- EVIDENCE PACKET (actual data/code outputs — use to verify claims) ---
{evidence_packet}

{field_calibration}

Score the paper from 0-100 across your 5 dimensions.

Output a JSON block:
```json
{{
  "score": 78,
  "decision": "MINOR_REVISIONS|MAJOR_REVISIONS|ACCEPT|REJECT",
  "dimension_scores": {{
    "contribution_novelty": 80,
    "literature_positioning": 75,
    "substantive_arguments": 78,
    "external_validity": 72,
    "journal_fit": 80
  }},
  "major_comments": ["..."],
  "minor_comments": ["..."],
  "missing_literature": ["..."]
}}
```
"""

    # ── Methods referee (build prompt before parallel launch) ───────────
    methods_prompt_text = _read_agent("methods-referee")

    methods_prompt = f"""{methods_prompt_text}

{revision_context}

--- PAPER ---
{paper_content}

--- STRATEGY MEMO (for reference) ---
{smart_truncate(strategy_memo, 2000)}

--- EVIDENCE PACKET (actual data/code outputs — use to verify claims) ---
{evidence_packet}

{field_calibration}

Score the paper from 0-100 across your 5 dimensions.

Output a JSON block:
```json
{{
  "score": 75,
  "decision": "MINOR_REVISIONS|MAJOR_REVISIONS|ACCEPT|REJECT",
  "dimension_scores": {{
    "identification_strategy": 78,
    "estimation_implementation": 72,
    "statistical_inference": 75,
    "robustness_sensitivity": 70,
    "replication_readiness": 80
  }},
  "sanity_checks": {{
    "sign": "PASS|FAIL",
    "magnitude": "PASS|FAIL",
    "dynamics": "PASS|FAIL|NA",
    "consistency": "PASS|FAIL"
  }},
  "major_comments": ["..."],
  "minor_comments": ["..."]
}}
```
"""

    # ── Run both referees in parallel ─────────────────────────────────────
    print("  [6] Domain + Methods referees reviewing in parallel...")
    pr = get_profile("stage6_referee")
    referee_responses = run_claude_parallel([
        {
            "prompt": domain_prompt, "model": pr["model"], "effort": pr["effort"],
            "output_file": review_dir / f"domain_referee{round_suffix}.md",
            "label": "domain-referee",
            "allowed_tools": [],
        },
        {
            "prompt": methods_prompt, "model": pr["model"], "effort": pr["effort"],
            "output_file": review_dir / f"methods_referee{round_suffix}.md",
            "label": "methods-referee",
            "allowed_tools": [],
        },
    ], max_workers=2)

    domain_result = extract_json(referee_responses[0]) or {}
    methods_result = extract_json(referee_responses[1]) or {}

    # ── Editorial decision ───────────────────────────────────────────────
    domain_score = domain_result.get("score", 0)
    methods_score = methods_result.get("score", 0)
    avg_score = (domain_score + methods_score) / 2 if (domain_score and methods_score) else 0

    domain_dec = domain_result.get("decision", "?")
    methods_dec = methods_result.get("decision", "?")

    # Editor synthesizes issues (but does NOT decide — thresholds do)
    decision_prompt = f"""{_read_agent('editor')}

--- REFEREE REPORTS ---

## Domain Referee (score: {domain_score})
Decision: {domain_dec}
Major comments: {domain_result.get('major_comments', [])}

## Methods Referee (score: {methods_score})
Decision: {methods_dec}
Major comments: {methods_result.get('major_comments', [])}

--- TASK ---
Phase 2: Synthesize referee reports. Classify each concern as
FATAL, ADDRESSABLE, or TASTE. List must_address / should_address /
may_address issues.

IMPORTANT: Do NOT output a "decision" field. The decision is computed
automatically from the average score and fatal issues. Just classify
the issues.

Output a JSON block:
```json
{{
  "avg_referee_score": {avg_score},
  "must_address": ["..."],
  "should_address": ["..."],
  "may_address": ["..."],
  "fatal_issues": []
}}
```
"""

    print("  [6] Editor synthesizing issues...")
    pd_ = get_profile("stage6_decision")
    decision_response = run_claude(
        decision_prompt, model=pd_["model"], effort=pd_["effort"],
        output_file=review_dir / f"editorial_decision{round_suffix}.md",
        allowed_tools=[],
    )
    decision_result = extract_json(decision_response) or {}

    # ── Deterministic decision based on thresholds ──────────────────────
    has_fatal = len(decision_result.get("fatal_issues", [])) > 0

    if avg_score >= ACCEPT_GATE and not has_fatal:
        decision = "ACCEPT"
    elif avg_score >= ACCEPT_GATE and has_fatal:
        decision = "MINOR_REVISIONS"
    elif avg_score >= MINOR_REV_GATE and not has_fatal:
        decision = "MINOR_REVISIONS"
    elif avg_score >= MINOR_REV_GATE and has_fatal:
        decision = "MAJOR_REVISIONS"
    elif avg_score >= REJECT_FLOOR:
        decision = "MAJOR_REVISIONS"
    else:  # avg < REJECT_FLOOR
        decision = "MAJOR_REVISIONS" if not has_fatal else "REJECT"

    decision_result["decision"] = decision

    print(f"  [6] Decision: {decision} (avg score: {avg_score:.0f}, "
          f"fatal: {has_fatal}, thresholds: ACCEPT>={ACCEPT_GATE}, "
          f"MINOR>={MINOR_REV_GATE}, REJECT<{REJECT_FLOOR})")

    state["stages"]["stage6"] = {
        "status": "completed",
        "decision": decision,
        "rr_round": rr_round,
        "domain_score": domain_score,
        "methods_score": methods_score,
        "avg_score": avg_score,
        "editor_result": editor_result,
        "domain_result": domain_result,
        "methods_result": methods_result,
        "decision_result": decision_result,
        "completed_at": datetime.now().isoformat(),
    }

    state["current_stage"] = 6
    save_state(project_dir, state)

    # ── R&R loop ─────────────────────────────────────────────────────────
    if decision == "MAJOR_REVISIONS" and rr_round < MAX_RR_ROUNDS:
        print(f"  [6] Major revisions requested -> looping back to Stage 5 "
              f"(round {rr_round + 1}/{MAX_RR_ROUNDS})")
        # The orchestrator in run_pipeline.py will re-run stages 5-6
        return state

    # ── End of R&R rounds: ALWAYS present options to user ────────────────
    # Reached when: (a) all R&R rounds exhausted, OR (b) decision is
    # ACCEPT/MINOR_REVISIONS/REJECT (no more automatic loops).
    # The user always gets to decide the next step.
    must_address = decision_result.get("must_address", [])
    should_address = decision_result.get("should_address", [])
    may_address = decision_result.get("may_address", [])

    print(f"\n  {'=' * 60}")
    print(f"  PEER REVIEW COMPLETE — {decision} (avg score: {avg_score:.0f})")
    if rr_round > 1:
        print(f"  After {rr_round} R&R rounds")
    print(f"  {'=' * 60}")

    issue_num = 0
    if must_address:
        print(f"\n  MUST-ADDRESS ({len(must_address)} issues):")
        for issue in must_address:
            issue_num += 1
            print(f"    {issue_num}. {issue[:120]}...")

    if should_address:
        print(f"\n  SHOULD-ADDRESS ({len(should_address)} issues):")
        for issue in should_address:
            issue_num += 1
            print(f"    {issue_num}. {issue[:120]}...")

    if may_address:
        print(f"\n  MAY-ADDRESS ({len(may_address)} issues):")
        for issue in may_address:
            issue_num += 1
            print(f"    {issue_num}. {issue[:120]}...")

    total_issues = len(must_address) + len(should_address) + len(may_address)
    if total_issues > 0:
        print(f"\n  Total: {total_issues} issues "
              f"({len(must_address)} must, {len(should_address)} should, {len(may_address)} may)")

    # ── Score ceiling diagnosis ──────────────────────────────────
    # Help user understand WHY the score is what it is and what
    # would be needed to reach higher tiers.
    print(f"\n  {'─' * 60}")
    print(f"  SCORE DIAGNOSIS")
    print(f"  {'─' * 60}")

    if avg_score >= 85:
        print(f"  Score {avg_score:.0f}/100 — EXCELLENT")
        print(f"  Paper is near publication-ready for top field journals.")
    elif avg_score >= 75:
        print(f"  Score {avg_score:.0f}/100 — GOOD")
        print(f"  Publishable in solid applied journals. Minor revisions needed.")
    elif avg_score >= 65:
        print(f"  Score {avg_score:.0f}/100 — ACCEPTABLE")
        print(f"  Publishable in regional/applied journals with revisions.")
    else:
        print(f"  Score {avg_score:.0f}/100 — NEEDS WORK")

    # Detect structural limitations from strategy/methodology
    strategy = state["stages"].get("stage3_5", {}).get("approved_strategy", {})
    method_text = str(strategy.get("method", "")).lower()
    design_text = str(strategy.get("design", "")).lower()
    all_issues_text = " ".join(str(m) for m in must_address).lower()

    ceiling_reasons = []

    # Cross-sectional design
    if "cross" in design_text or "cross-section" in method_text or "cross-section" in all_issues_text:
        ceiling_reasons.append(
            "Cross-sectional design (no causal identification) — "
            "panel data or quasi-experimental design needed for 80+"
        )

    # Weak instrument
    if "weak" in all_issues_text or "exclusion restriction" in all_issues_text or "instrument" in all_issues_text:
        ceiling_reasons.append(
            "Weak/missing instrument for selection correction — "
            "credible exclusion restriction needed for 80+"
        )

    # IIA issues
    if "iia" in all_issues_text or "hausman" in all_issues_text or "nested logit" in all_issues_text:
        ceiling_reasons.append(
            "MNL IIA assumption unverified — "
            "nested logit or mixed logit implementation needed for 75+"
        )

    # Small sample
    if "small sample" in all_issues_text or "n=" in all_issues_text or "sample size" in all_issues_text:
        ceiling_reasons.append(
            "Small effective sample for key estimates — "
            "more data or alternative estimator needed"
        )

    # PSM without actual treatment history
    if "psm" in method_text and ("cross" in design_text or "propensity" in all_issues_text):
        ceiling_reasons.append(
            "PSM on cross-section identifies associations, not causal effects — "
            "panel data with actual NEET history needed for causal claims (85+)"
        )

    if ceiling_reasons:
        print(f"\n  Why the score can't go higher with text edits alone:")
        for i, reason in enumerate(ceiling_reasons, 1):
            print(f"    {i}. {reason}")
        print(f"\n  These are design limitations, not writing issues.")
        print(f"  Reaching 80+ requires changes to data or methodology,")
        print(f"  not additional R&R rounds on the same paper.")

        # ── Recommended strategy + data for ~95/100 ──
        import re as _re
        main_data = state["stages"].get("stage1", {}).get("data_path", "")
        year_match = _re.search(r"20\d{2}", main_data)
        year = year_match.group() if year_match else "YYYY"

        print(f"\n  {'=' * 60}")
        print(f"  RECOMMENDED STRATEGY FOR ~95/100")
        print(f"  {'=' * 60}")
        print()
        print(f"  If you want the highest possible score, the optimal")
        print(f"  identification strategy would be:")
        print()

        rec_lines = []
        if "cross" in design_text:
            rec_lines.append(("Design", f"Panel (ENAHO rotating panel {int(year)-2}-{year}, DiD/event-study)"))
            rec_lines.append(("Primary", "Diff-in-Differences on NEET->employment transitions"))
        if "psm" in method_text or "matching" in method_text:
            rec_lines.append(("Wage", "Panel wage equation with individual fixed effects"))
        if "multinomial" in method_text or "mnl" in method_text:
            rec_lines.append(("Secondary", "Nested logit for multinomial NEET determinants"))
        if "heckman" in method_text or "selection" in method_text:
            rec_lines.append(("Selection", "Heckman with credible instrument (local labor demand shock)"))
        if "fairlie" in method_text or "decomposition" in method_text:
            rec_lines.append(("Decomp", "Fairlie with caregiving variables (Module 200)"))

        for label, desc in rec_lines:
            print(f"  {label:12s}: {desc}")

        # Build data list
        recommended_data = []
        if "cross" in design_text:
            for y in range(int(year) - 2, int(year) + 1):
                have = f"{y}-500" in main_data.lower()
                recommended_data.append({
                    "module": f"Module 500 (Employment) - {y}",
                    "file": f"Enaho01a-{y}-500.csv",
                    "purpose": "Build rotating panel via CONGLOME+VIVIENDA+HOGAR+CODPERSO",
                    "have": have,
                })
            for y in range(int(year) - 2, int(year) + 1):
                recommended_data.append({
                    "module": f"Module 300 (Education) - {y}",
                    "file": f"Enaho01a-{y}-300.csv",
                    "purpose": "P306 enrollment for NEET classification",
                    "have": False,
                })
        if "fairlie" in method_text or "decomposition" in method_text:
            recommended_data.append({
                "module": f"Module 200 (Household) - {year}",
                "file": f"Enaho01-{year}-200.csv",
                "purpose": "Children under 5, dependency ratio for Fairlie decomposition",
                "have": False,
            })

        if recommended_data:
            print(f"\n  Data you would need to provide:")
            border = "  +" + "-" * 62 + "+"
            print(border)
            for d in recommended_data:
                have_tag = " (already have)" if d["have"] else ""
                print(f"  |  {d['module']}{have_tag}")
                print(f"  |    File: {d['file']}")
                print(f"  |    Purpose: {d['purpose']}")
                print(f"  |")
            print(f"  |  Download: https://proyectos.inei.gob.pe/microdatos/")
            print(f"  |  Select ENAHO -> year -> module")
            print(border)

    else:
        # Generic guidance
        if avg_score < 80:
            print(f"\n  Review the must-address issues above.")
            print(f"  Some may require methodological changes, not just text edits.")

    print(f"  {'─' * 60}")

    print(f"  {'=' * 60}")
    print(f"  Options:")
    print(f"  [1] Accept score ({avg_score:.0f}) and proceed to Stage 7")
    print(f"  [2] Manual intervention — Claude fixes paper, then re-review")
    print(f"  [3] Add new data — provide additional dataset(s), re-run code + paper")
    print(f"  {'=' * 60}")
    print("\a", end="", flush=True)  # Terminal bell — user input needed

    user_choice = ""
    while user_choice not in ("1", "2", "3"):
        user_choice = input("\n  Enter your choice (1, 2, or 3): ").strip()
        if user_choice not in ("1", "2", "3"):
            print("  Please enter 1, 2, or 3.")

    if user_choice == "1":
        # Accept and proceed
        print(f"\n  [6] Score {avg_score:.0f} accepted. Proceeding to Stage 7.")

    elif user_choice == "2":
        # Manual intervention
        from ..claude_runner import request_manual_intervention

        issue_summary = (
            f"Stage 6 peer review: {decision} after {rr_round} "
            f"round(s). Avg referee score: {avg_score:.0f}. "
            f"Must-address issues: {len(must_address)}."
        )
        paper_files = [str(paper_dir / "main.tex")] if (paper_dir / "main.tex").exists() else []
        review_files = [str(f) for f in sorted(review_dir.glob("*.md"))]

        request_manual_intervention(
            stage="stage6_review",
            issue=issue_summary,
            files=paper_files + review_files,
            project_dir=project_dir,
        )

        # After intervention: run consistency check before re-review
        print(f"\n  [6] Post-intervention consistency check...")
        _consistency_check(project_dir)

        # Re-run peer review ONE more time
        print(f"\n  [6] Re-running peer review after manual intervention...")
        state = run(project_dir, state)
        return state

    elif user_choice == "3":
        # Add new data: user provides path(s) to additional dataset(s)
        print(f"\n  {'=' * 60}")
        print(f"  ADD NEW DATA")
        print(f"  {'=' * 60}")

        # Show what referees asked for so user knows exactly what to get
        all_referee_issues = must_address + should_address + may_address
        if all_referee_issues:
            print(f"\n  Referees requested the following changes:")
            for i, issue in enumerate(all_referee_issues, 1):
                tag = "MUST" if i <= len(must_address) else "SHOULD" if i <= len(must_address) + len(should_address) else "MAY"
                print(f"    {i}. [{tag}] {str(issue)[:120]}")

        # Detect specific data needs from ALL referee comments (not just must-address)
        all_issues = " ".join(str(m) for m in must_address + should_address + may_address).lower()
        print(f"\n  Based on referee feedback, you may need:")
        if "module 300" in all_issues or "p306" in all_issues or "enrollment" in all_issues:
            print(f"    - ENAHO Module 300 (Education): file Enaho01a-YYYY-300.csv")
            print(f"      Contains: P306 (current enrollment status)")
            print(f"      Purpose: Fix NEET classification using enrollment vs reference-week activity")
        if "module 200" in all_issues or "children" in all_issues or "household" in all_issues or "caregiving" in all_issues:
            print(f"    - ENAHO Module 200 (Household): file Enaho01-YYYY-200.csv")
            print(f"      Contains: household composition, children under 5, dependency ratio")
            print(f"      Purpose: Improve Fairlie decomposition with caregiving variables")
        if "panel" in all_issues or "rotating" in all_issues or "longitudinal" in all_issues:
            print(f"    - ENAHO quarterly panel files (multiple years)")
            print(f"      Purpose: Enable longitudinal analysis for causal identification")
        if not any(k in all_issues for k in ["module 300", "p306", "enrollment", "module 200", "children", "panel"]):
            print(f"    (Could not auto-detect specific modules from referee comments)")
            print(f"    Review the issues above and provide the relevant ENAHO modules.")

        print(f"\n  Where to download:")
        print(f"    INEI microdatos: https://proyectos.inei.gob.pe/microdatos/")
        print(f"    Select 'ENAHO' -> year matching your main dataset -> module")
        print(f"\n  The pipeline will re-run from Stage 4 (code) through")
        print(f"  Stage 5 (writing) with the new data.")
        print(f"  {'=' * 60}")

        data_dir = project_dir / "data" / "external"
        data_dir.mkdir(parents=True, exist_ok=True)

        added_files = []
        while True:
            path_input = input("\n  Data file path (or 'done' to finish): ").strip()
            if path_input.lower() == "done":
                break
            src = Path(path_input)
            if not src.exists():
                print(f"  [!] File not found: {src}")
                continue

            # ── Validate the file before accepting ──
            import shutil
            print(f"  [check] Validating {src.name} ...")
            try:
                import pandas as _pd
                _df_check = _pd.read_csv(src, nrows=5, encoding="latin-1", low_memory=False)
                file_cols = set(_df_check.columns)

                # Check merge keys
                merge_keys = {"CONGLOME", "VIVIENDA", "HOGAR", "CODPERSO"}
                has_merge_keys = merge_keys.issubset(file_cols)

                # Detect ENAHO module
                module_detected = "unknown"
                if any(c.startswith("P3") for c in file_cols):
                    module_detected = "Module 300 (Education)"
                elif any(c.startswith("P2") for c in file_cols):
                    module_detected = "Module 200 (Household characteristics)"
                elif any(c.startswith("P1") for c in file_cols):
                    module_detected = "Module 100 (Housing)"
                elif any(c.startswith("P4") for c in file_cols):
                    module_detected = "Module 400 (Health)"
                elif any(c.startswith("P5") for c in file_cols):
                    module_detected = "Module 500 (Employment)"

                full_df = _pd.read_csv(src, encoding="latin-1", low_memory=False)
                n_rows = len(full_df)
                n_cols = len(full_df.columns)
                del full_df

                print(f"    Detected: {module_detected}")
                print(f"    Rows: {n_rows:,}, Columns: {n_cols}")
                print(f"    Merge keys: {'YES' if has_merge_keys else 'NO'}")

                if not has_merge_keys:
                    print(f"\n  [!] This data ({src.name}) does not contain ENAHO")
                    print(f"      merge keys (CONGLOME, VIVIENDA, HOGAR, CODPERSO).")
                    print(f"      It cannot be merged with the main dataset.")
                    print(f"      This data is NOT what was requested.")
                    confirm = input("      Add anyway? (y/n): ").strip().lower()
                    if confirm != "y":
                        print(f"  [skip] {src.name} not added.")
                        continue

                # Check relevance against referee issues
                all_issues_text = " ".join(str(m) for m in must_address).lower()
                is_relevant = False
                if ("module 300" in all_issues_text or "p306" in all_issues_text or "enrollment" in all_issues_text) and "300" in module_detected:
                    is_relevant = True
                elif ("household" in all_issues_text or "children" in all_issues_text) and "200" in module_detected:
                    is_relevant = True
                elif "500" in module_detected:
                    # Same module as main — probably a duplicate
                    print(f"\n  [!] This data ({src.name}) appears to be {module_detected},")
                    print(f"      which is the same module as the main dataset.")
                    print(f"      This data is NOT what was requested.")
                    confirm = input("      Add anyway? (y/n): ").strip().lower()
                    if confirm != "y":
                        print(f"  [skip] {src.name} not added.")
                        continue

                if not is_relevant and module_detected != "unknown":
                    print(f"\n  [!] This data ({src.name}) appears to be {module_detected},")
                    print(f"      which may not match what the referees requested.")
                    confirm = input("      Add anyway? (y/n): ").strip().lower()
                    if confirm != "y":
                        print(f"  [skip] {src.name} not added.")
                        continue

                print(f"  [ok] {src.name} validated as {module_detected}")

            except Exception as val_err:
                print(f"  [!] Could not validate {src.name}: {val_err}")
                print(f"      The file may not be a valid CSV.")
                confirm = input("      Add anyway? (y/n): ").strip().lower()
                if confirm != "y":
                    print(f"  [skip] {src.name} not added.")
                    continue

            # ── Test merge with main dataset before accepting ──
            main_data_path = state["stages"].get("stage1", {}).get("data_path", "")
            if main_data_path and Path(main_data_path).exists():
                print(f"\n  [merge-test] Testing merge with main dataset ...")
                try:
                    merge_keys = ["CONGLOME", "VIVIENDA", "HOGAR", "CODPERSO"]
                    main_sample = _pd.read_csv(main_data_path, usecols=merge_keys,
                                               nrows=1000, encoding="latin-1", low_memory=False)
                    new_sample = _pd.read_csv(src, usecols=merge_keys,
                                              nrows=1000, encoding="latin-1", low_memory=False)
                    test_merge = main_sample.merge(new_sample, on=merge_keys, how="inner")
                    match_rate = len(test_merge) / len(main_sample) * 100

                    if match_rate < 5:
                        print(f"  [!] Merge test FAILED: only {match_rate:.1f}% of rows matched.")
                        print(f"      The main dataset and {src.name} do not share")
                        print(f"      enough common identifiers to merge.")
                        print(f"      This data ({src.name}) is NOT compatible.")
                        confirm = input("      Add anyway? (y/n): ").strip().lower()
                        if confirm != "y":
                            print(f"  [skip] {src.name} not added.")
                            continue
                    else:
                        print(f"  [ok] Merge test passed: {match_rate:.1f}% match rate (sample of 1,000 rows)")
                except Exception as merge_err:
                    print(f"  [warn] Could not test merge: {merge_err}")
                    print(f"         Proceeding without merge verification.")

            dst = data_dir / src.name
            shutil.copy2(src, dst)
            added_files.append(str(dst))
            print(f"  [ok] Copied: {src.name} -> {dst}")

        if added_files:
            # Store new data info in state for Stage 4 to use
            state["stages"].setdefault("stage6", {})
            state["stages"]["stage6"]["added_data"] = added_files
            state["stages"]["stage6"]["added_data_reason"] = (
                f"Referee requested additional data (R&R round {rr_round}). "
                f"Must-address issues: {'; '.join(str(m)[:80] for m in must_address[:3])}"
            )

            # Reset stages 4-5 for rebuild with new data
            for key in ["stage4a", "stage4bc", "stage4_5", "stage5"]:
                if key in state["stages"]:
                    del state["stages"][key]
            state["current_stage"] = 3.7
            state["stages"]["stage6"]["restart_from"] = 4

            # Delete old scripts and outputs so Stage 4 regenerates them
            scripts_dir = project_dir / "scripts" / "python"
            clean_dir = project_dir / "data" / "clean"
            if scripts_dir.exists():
                for old_script in scripts_dir.glob("*.py"):
                    old_script.unlink()
                print(f"  [clean] Deleted old scripts from {scripts_dir}")
            if clean_dir.exists():
                for old_output in clean_dir.glob("*.csv"):
                    old_output.unlink()
                print(f"  [clean] Deleted old outputs from {clean_dir}")

            save_state(project_dir, state)

            print(f"\n  [6] Added {len(added_files)} dataset(s).")
            print(f"  Pipeline will restart from Stage 4 with new data.")
            print(f"  Tell Claude: 'revisa el pipeline' when intervention is needed.")
        else:
            print(f"\n  [6] No files added. Returning to options.")
            # Re-display options
            state = run(project_dir, state)
            return state

    return state
