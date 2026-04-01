"""Interactive human-in-the-loop checkpoints for Stages 2.5 and 3.5.

Each checkpoint saves state *before* prompting so that Ctrl-C never loses
progress.  The user can resume with ``--from-stage 2.5`` or ``3.5``.
"""

import textwrap
from typing import Optional


# -- Causal method classification ---------------------------------------------

CAUSAL_METHODS = {
    "did", "diff-in-diff", "difference-in-differences", "difference in differences",
    "twfe", "two-way fixed effects", "event study", "event-study",
    "iv", "instrumental variable", "instrumental variables", "2sls", "tsls",
    "rdd", "regression discontinuity", "regression-discontinuity",
    "rct", "randomized", "experiment",
    "arellano-bond", "arellano bond", "dynamic panel", "gmm",
    "synth", "synthetic control",
    "bunching", "bunching estimator",
}

PANEL_METHODS = {
    "individual fe", "individual fixed effects", "fixed effects", "panel fe",
    "twfe", "two-way fixed effects", "within-estimator", "within estimator",
    "correlated random effects", "cre", "mundlak",
    "arellano-bond", "arellano bond", "dynamic panel", "gmm",
    "markov", "transition matrix", "survival model", "hazard",
}

DESCRIPTIVE_METHODS = {
    "ols", "wls", "oaxaca", "oaxaca-blinder", "blinder-oaxaca",
    "quantile regression", "rif", "firpo",
    "decomposition", "fairlie",
    "psm", "propensity score", "matching", "cem",
    "heckman", "selection model",
    "probit", "logit", "bivariate probit",
    "descriptive", "correlational",
}


def _classify_method(method_str: str) -> str:
    """Classify a method string as CAUSAL, PANEL, or DESCRIPTIVE."""
    m = method_str.lower().strip()
    # Check causal first (strongest)
    for kw in CAUSAL_METHODS:
        if kw in m:
            return "CAUSAL"
    # Then panel (uses within-individual variation but not necessarily causal)
    for kw in PANEL_METHODS:
        if kw in m:
            return "PANEL"
    # Then descriptive
    for kw in DESCRIPTIVE_METHODS:
        if kw in m:
            return "DESCRIPTIVE"
    return "UNKNOWN"


def _method_tag(classification: str) -> str:
    """Return a colored tag for the method classification."""
    tags = {
        "CAUSAL": "[CAUSAL]",
        "PANEL": "[PANEL]",
        "DESCRIPTIVE": "[DESCRIPTIVE]",
        "UNKNOWN": "[?]",
    }
    return tags.get(classification, "[?]")


# -- Display helpers ----------------------------------------------------------

def _hr(char="-", width=60):
    print(char * width)


def _print_idea(idx: int, idea: dict):
    """Pretty-print one research idea with causal classification."""
    method = idea.get('method', 'N/A')
    classification = _classify_method(method)
    tag = _method_tag(classification)

    print(f"\n  [{idx}] {idea.get('title', 'Untitled')}")
    print(f"      Score: {idea.get('total_score', '?')}  "
          f"(N={idea.get('novelty','?')} F={idea.get('feasibility','?')} I={idea.get('impact','?')})")
    print(f"      Method: {method}  {tag}")
    print(f"      RQ: {idea.get('research_question', 'N/A')}")
    data = idea.get("data_sources", [])
    if data:
        print(f"      Data: {', '.join(data)}")
    pitch = idea.get("pitch", "")
    if pitch:
        wrapped = textwrap.fill(pitch, width=54, initial_indent="      ", subsequent_indent="      ")
        print(wrapped)


def _print_strategy(strategy: dict | str):
    """Pretty-print the proposed identification strategy."""
    if isinstance(strategy, str):
        for line in strategy.splitlines():
            print(f"  {line}")
        return
    print(f"  Method: {strategy.get('method', 'N/A')}")
    print(f"  Design: {strategy.get('design', 'N/A')}")
    print(f"  Data: {strategy.get('data_sources', 'N/A')}")
    pap = strategy.get("pre_analysis_plan", "")
    if pap:
        wrapped = textwrap.fill(pap, width=56, initial_indent="  PAP: ", subsequent_indent="       ")
        print(wrapped)


# -- Stage 2.5: Idea Selection -----------------------------------------------

def idea_selection(top_ideas: list[dict]) -> dict:
    """Present the top 3 ideas and let the researcher choose.

    Returns
    -------
    dict
        ``{"action": "SELECT"|"COMBINE"|"REJECT", "selected_idea": {...} | None}``
    """
    _hr("=")
    print("STAGE 2.5 - IDEA SELECTION (human checkpoint)")
    _hr("=")
    print("\nThe pipeline generated the following top ideas:\n")

    for i, idea in enumerate(top_ideas[:3], 1):
        _print_idea(i, idea)

    # ── Causal method audit ──────────────────────────────────────────────
    top3 = top_ideas[:3]
    classifications = [_classify_method(idea.get("method", "")) for idea in top3]
    n_causal = sum(1 for c in classifications if c == "CAUSAL")
    n_panel = sum(1 for c in classifications if c == "PANEL")
    n_descriptive = sum(1 for c in classifications if c in ("DESCRIPTIVE", "UNKNOWN"))

    print()
    _hr("-")
    print("CAUSAL DESIGN AUDIT")
    _hr("-")
    print(f"  Causal methods (DiD, IV, RDD, event study, etc.): {n_causal} of 3")
    print(f"  Panel methods (FE, TWFE, dynamic panel, CRE):     {n_panel} of 3")
    print(f"  Descriptive methods (OLS, matching, decomp.):     {n_descriptive} of 3")

    if n_causal >= 2:
        print(f"\n  [ok] {n_causal} of 3 ideas use causal identification.")
        print(f"       These designs are competitive for top field journals.")
    elif n_causal == 1:
        print(f"\n  [!] WARNING: Only 1 of 3 ideas uses a causal design.")
        print(f"      Papers without causal identification face a score ceiling")
        print(f"      of ~70/100 and are limited to regional/applied journals.")
        print(f"      Consider REJECT ALL to regenerate with more causal designs,")
        print(f"      or select the causal idea (marked [CAUSAL]).")
    else:
        if n_panel >= 1:
            print(f"\n  [!!] WARNING: No ideas use a causal design.")
            print(f"       {n_panel} idea(s) use panel methods, which exploit within-individual")
            print(f"       variation but do NOT provide causal identification without")
            print(f"       a pre-treatment baseline or exogenous variation.")
            print(f"\n       To reach 80+/100, you need causal designs (DiD, IV, RDD).")
            print(f"       This typically requires pre-treatment data or a natural experiment.")
            print(f"       Consider REJECT ALL if you have data that supports causal designs.")
        else:
            print(f"\n  [!!] WARNING: No ideas use causal or panel methods.")
            print(f"       All 3 ideas are purely descriptive/correlational.")
            print(f"       Score ceiling: ~65/100 (regional journals only).")
            print(f"\n       Strongly consider REJECT ALL to regenerate, or provide")
            print(f"       additional data that enables causal identification.")

    print()
    _hr()
    print("Options:")
    print("  SELECT  <number>   - proceed with that idea  (e.g. SELECT 1)")
    print("  COMBINE <n> <m>    - merge two ideas          (e.g. COMBINE 1 2)")
    print("  REJECT ALL         - discard all, re-run Stage 2")
    _hr()
    print("\a", end="", flush=True)  # Terminal bell — user input needed

    while True:
        choice = input("\n>> ").strip().upper()

        if choice.startswith("SELECT"):
            parts = choice.split()
            if len(parts) == 2 and parts[1].isdigit():
                idx = int(parts[1])
                if 1 <= idx <= len(top_ideas[:3]):
                    selected = top_ideas[idx - 1]
                    print(f"\n  [ok] Selected idea {idx}: {selected.get('title')}")
                    return {"action": "SELECT", "selected_idea": selected}
            print("  Usage: SELECT <1|2|3>")

        elif choice.startswith("COMBINE"):
            parts = choice.split()
            if len(parts) == 3 and parts[1].isdigit() and parts[2].isdigit():
                a, b = int(parts[1]), int(parts[2])
                limit = len(top_ideas[:3])
                if 1 <= a <= limit and 1 <= b <= limit and a != b:
                    idea_a = top_ideas[a - 1]
                    idea_b = top_ideas[b - 1]
                    combined = {
                        "title": f"{idea_a.get('title', '')} + {idea_b.get('title', '')}",
                        "research_question": f"Combined: {idea_a.get('research_question','')} | {idea_b.get('research_question','')}",
                        "method": f"{idea_a.get('method','')}/{idea_b.get('method','')}",
                        "data_sources": list(set(idea_a.get("data_sources", []) + idea_b.get("data_sources", []))),
                        "novelty": max(idea_a.get("novelty", 0), idea_b.get("novelty", 0)),
                        "feasibility": min(idea_a.get("feasibility", 0), idea_b.get("feasibility", 0)),
                        "impact": max(idea_a.get("impact", 0), idea_b.get("impact", 0)),
                        "pitch": f"{idea_a.get('pitch','')} - merged with - {idea_b.get('pitch','')}",
                        "first_experiment": idea_a.get("first_experiment", idea_b.get("first_experiment", "")),
                    }
                    print(f"\n  [ok] Combined ideas {a} & {b}")
                    return {"action": "COMBINE", "selected_idea": combined}
            print("  Usage: COMBINE <n> <m>  (e.g. COMBINE 1 3)")

        elif choice == "REJECT ALL":
            print("\n  [x] All ideas rejected. Pipeline will re-run Stage 2.")
            return {"action": "REJECT", "selected_idea": None}

        else:
            print("  Unrecognised command. Type SELECT <n>, COMBINE <n> <m>, or REJECT ALL.")


# -- Stage 3.5: Data Source Selection ----------------------------------------

def data_source_selection(
    main_data_name: str,
    external_sources: list[str],
    external_justifications: list[dict] | None = None,
) -> dict:
    """Ask the user whether to work with only the main dataset or also external data.

    Parameters
    ----------
    main_data_name : str
        Name of the main dataset file.
    external_sources : list[str]
        Names/descriptions of proposed external data sources.
    external_justifications : list[dict] | None
        For each external source: {"source", "role", "impact_without"}.

    Returns
    -------
    dict
        ``{"choice": 1|2, "use_external": bool}``
    """
    _hr("=")
    print("STAGE 3.5 - DATA SOURCE SELECTION")
    _hr("=")

    print(f"\n  Main dataset: {main_data_name}")
    if external_sources:
        print(f"\n  External sources proposed by the strategy:")
        if external_justifications:
            for j in external_justifications:
                print(f"\n    * {j.get('source', '?')}")
                print(f"      Role: {j.get('role', 'N/A')}")
                print(f"      Without it: {j.get('impact_without', 'N/A')}")
        else:
            for i, src in enumerate(external_sources, 1):
                print(f"    {i}. {src}")

        # Show recommendation
        if external_justifications:
            critical = [j for j in external_justifications if j.get("critical", False)]
            if critical:
                print(f"\n  [!] {len(critical)} source(s) are CRITICAL for the identification strategy.")
                print(f"      Without them, the strategy will need to be adapted.")
            else:
                print(f"\n  [i] External sources are optional — they strengthen the study")
                print(f"      but the main analysis can proceed without them.")
    else:
        print(f"\n  No external datasets are needed for this strategy.")

    print()
    _hr()
    print("Options:")
    print(f"  1  -  Work ONLY with the main dataset ({main_data_name})")
    if external_sources:
        print(f"  2  -  Work with the main dataset + external datasets")
    _hr()
    print("\a", end="", flush=True)  # Terminal bell — user input needed

    while True:
        choice = input("\n>> ").strip()
        if choice == "1":
            print(f"\n  [ok] Dataset fixed: {main_data_name}")
            print(f"  The strategy will use ONLY this dataset.")
            return {"choice": 1, "use_external": False}
        elif choice == "2":
            if not external_sources:
                print("  [warn] No external sources were proposed. Defaulting to option 1.")
                print(f"\n  [ok] Dataset fixed: {main_data_name}")
                return {"choice": 1, "use_external": False}
            print(f"\n  [ok] Will attempt to download and merge external datasets.")
            return {"choice": 2, "use_external": True}
        else:
            print("  Please enter 1 or 2.")


# -- Stage 3.5: Strategy Review ----------------------------------------------

def _diagnose_strategy(strategy: dict | str, main_data_name: str = "") -> None:
    """Analyze the strategy and print a quality ceiling diagnosis.

    Detects structural limitations in the identification strategy that
    will cap the final paper score, BEFORE the user commits to code and
    writing. Also recommends the optimal strategy for ~95/100 and lists
    exactly which data files the user would need to provide.
    """
    if isinstance(strategy, str):
        text = strategy.lower()
        method = ""
        design = ""
        title = ""
    else:
        text = " ".join(str(v) for v in strategy.values()).lower()
        method = str(strategy.get("method", "")).lower()
        design = str(strategy.get("design", "")).lower()
        title = str(strategy.get("title", ""))

    warnings = []
    ceiling = 100
    recommended_design = []
    recommended_data = []

    # Detect which ENAHO year from main dataset name
    import re
    year_match = re.search(r"20\d{2}", main_data_name or text)
    year = year_match.group() if year_match else "YYYY"

    # ── Cross-sectional design ──
    is_cross_section = "cross-section" in text or "cross section" in text
    has_panel = "panel" in text or "diff-in-diff" in text or "rdd" in text
    if is_cross_section and not has_panel:
        warnings.append({
            "issue": "Cross-sectional design — no causal identification",
            "impact": "Score ceiling ~70. Referees will flag all causal language.",
            "fix": "Use panel data (ENAHO rotating panel) or quasi-experimental design",
        })
        ceiling -= 30
        recommended_design.append("Panel (ENAHO rotating panel, DiD/event-study)")
        # Need multiple years of Module 500
        for y in range(int(year) - 2, int(year) + 1):
            fname = f"Enaho01a-{y}-500.csv"
            recommended_data.append({
                "file": fname,
                "module": f"Module 500 (Employment) — {y}",
                "purpose": "Build rotating panel via CONGLOME+VIVIENDA+HOGAR+CODPERSO",
                "have": fname.lower() in main_data_name.lower() if main_data_name else False,
            })

    # ── PSM without actual treatment history ──
    if ("psm" in method or "propensity score" in method or "matching" in method):
        if not has_panel:
            warnings.append({
                "issue": "PSM on cross-section — identifies associations, not causal effects",
                "impact": "Referees will require reframing as 'risk-profile gap', not 'penalty'",
                "fix": "Panel data to observe actual NEET->employment transitions",
            })
            ceiling -= 15
            if not recommended_design:
                recommended_design.append("Diff-in-Differences on NEET->employment transitions")

    # ── Heckman without clear instrument ──
    if "heckman" in method or "selection" in method:
        if "instrument" not in text and "exclusion restriction" not in text:
            warnings.append({
                "issue": "Heckman selection model without specified exclusion restriction",
                "impact": "Weak instrument -> Heckman demoted to robustness check",
                "fix": "Identify credible instrument (e.g. local labor demand shock)",
            })
            ceiling -= 10
            recommended_design.append("Heckman with credible instrument (local labor demand shock)")

    # ── Multinomial logit IIA concern ──
    if "multinomial logit" in method or "mnl" in method or "mlogit" in method:
        if "nested" not in method and "mixed logit" not in method:
            warnings.append({
                "issue": "Multinomial logit assumes IIA — may not hold for close substitutes",
                "impact": "If IIA test fails, referees will require nested logit",
                "fix": "Include nested logit as primary or robustness specification",
            })
            ceiling -= 5
            recommended_design.append("Nested logit for multinomial NEET determinants")

    # ── Small wage sample ──
    if "wage" in text and ("module 500" in text or "p524" in text):
        if "module 600" not in text and "ingresos" not in text:
            warnings.append({
                "issue": "Wage data from Module 500 only — likely small effective sample",
                "impact": "Module 500 has wages only for dependent workers (~5% of youth)",
                "fix": "Merge with Module 500 income variables or use total income",
            })
            ceiling -= 5
            recommended_design.append("Panel wage equation with individual fixed effects")

    # ── Missing education module ──
    if "p50410" in text and "p306" not in text:
        warnings.append({
            "issue": "Student classification via P50410 (reference-week) instead of P306 (enrollment)",
            "impact": "NEET rate will be ~42% instead of ~20%. Referees will flag immediately.",
            "fix": "Merge Module 300 (Education) for P306 enrollment status",
        })
        ceiling -= 10
        recommended_data.append({
            "file": f"Enaho01a-{year}-300.csv",
            "module": f"Module 300 (Education) — {year}",
            "purpose": "P306 enrollment status for accurate NEET classification",
            "have": False,
        })

    # ── Missing household composition for Fairlie ──
    if "fairlie" in method or "fairlie" in text or ("decomposition" in method and "gender" in text):
        if "module 200" not in text and "children" not in text and "caregiving" not in text:
            warnings.append({
                "issue": "Fairlie decomposition without caregiving/children variables",
                "impact": "Large 'unexplained' component may be due to omitted variables, not discrimination",
                "fix": "Merge Module 200 (Household) for children under 5, dependency ratio",
            })
            ceiling -= 5
            recommended_data.append({
                "file": f"Enaho01-{year}-200.csv",
                "module": f"Module 200 (Household) — {year}",
                "purpose": "Children under 5, dependency ratio for Fairlie decomposition",
                "have": False,
            })

    # Recommend Module 300 only if not already in main dataset or recommendations
    mod300_in_data = any("300" in d.get("module", "") for d in recommended_data)
    mod300_in_main = "300" in (main_data_name or "")
    if not mod300_in_data and not mod300_in_main:
        recommended_data.append({
            "file": f"Enaho01a-{year}-300.csv",
            "module": f"Module 300 (Education) — {year}",
            "purpose": "P306 enrollment for accurate NEET classification",
            "have": False,
        })

    # ── Print diagnosis ──
    print()
    _hr("-")
    print("STRATEGY QUALITY DIAGNOSIS")
    _hr("-")

    ceiling = max(ceiling, 0)
    if ceiling >= 85:
        tier = "STRONG — publishable in top field journals"
    elif ceiling >= 75:
        tier = "GOOD — publishable in solid applied journals"
    elif ceiling >= 65:
        tier = "ACCEPTABLE — publishable in regional/applied journals"
    else:
        tier = "LIMITED — significant methodological constraints"

    print(f"\n  Estimated score ceiling: ~{ceiling}/100 ({tier})")

    if warnings:
        print(f"\n  Structural limitations detected ({len(warnings)}):\n")
        for i, w in enumerate(warnings, 1):
            print(f"  {i}. {w['issue']}")
            print(f"     Impact: {w['impact']}")
            print(f"     To improve: {w['fix']}")
            print()
        print(f"  These limitations are inherent to the research design.")
        print(f"  They CANNOT be fixed by editing text — only by changing")
        print(f"  the data or methodology.")
    else:
        print(f"\n  No major structural limitations detected.")
        print(f"  Strategy has strong identification potential.")

    # ── Recommended strategy for ~95/100 ──
    if warnings:
        print(f"\n  {'=' * 60}")
        print(f"  RECOMMENDED STRATEGY FOR ~95/100")
        print(f"  {'=' * 60}")
        print()
        print(f"  If you want the highest possible score, the optimal")
        print(f"  identification strategy would be:")
        print()
        if recommended_design:
            for i, d in enumerate(recommended_design):
                label = ["Design", "Primary", "Secondary", "Wage", "Selection", "Decomp"][min(i, 5)]
                print(f"  {label:12s}: {d}")
        print()

        # ── Data needed ──
        # Deduplicate by file name
        seen_files = set()
        unique_data = []
        for d in recommended_data:
            if d["file"] not in seen_files:
                seen_files.add(d["file"])
                unique_data.append(d)

        if unique_data:
            print(f"  Data you would need to provide:")
            border = "+" + "-" * 62 + "+"
            print(f"  {border}")
            for d in unique_data:
                have_tag = " (already have)" if d["have"] else ""
                print(f"  |  {d['module']}{have_tag}")
                print(f"  |    File: {d['file']}")
                print(f"  |    Purpose: {d['purpose']}")
                print(f"  |")
            print(f"  |  Download: https://proyectos.inei.gob.pe/microdatos/")
            print(f"  |  Select ENAHO -> year -> module")
            print(f"  {border}")

    _hr("-")


def strategy_review(strategy: dict | str, main_data_name: str = "") -> dict:
    """Present the proposed identification strategy for human approval.

    Parameters
    ----------
    strategy : dict or str
        The proposed identification strategy.
    main_data_name : str
        Name of the main dataset file (used for year detection in diagnosis).

    Returns
    -------
    dict
        ``{"action": "APPROVE"|"REFORMULATE"|"REJECT", "notes": str}``
    """
    _hr("=")
    print("STAGE 3.5 - STRATEGY REVIEW (human checkpoint)")
    _hr("=")
    print("\nProposed identification strategy:\n")
    _print_strategy(strategy)

    # Show quality diagnosis BEFORE asking for decision
    _diagnose_strategy(strategy, main_data_name=main_data_name)

    print()
    _hr()
    print("Options:")
    print("  APPROVE                - accept the strategy as-is")
    print("  REFORMULATE            - upgrade to recommended strategy (provide data listed above)")
    print("  REJECT                 - discard and go back to Stage 2.5")
    _hr()
    print("\a", end="", flush=True)  # Terminal bell — user input needed

    while True:
        choice = input("\n>> ").strip().upper()

        if choice == "APPROVE":
            print("\n  [ok] Strategy approved. Proceeding to Stage 4.")
            return {"action": "APPROVE", "notes": ""}

        elif choice == "REFORMULATE":
            print("\n  Enter your revised strategy (end with an empty line):")
            lines = []
            while True:
                line = input("  | ")
                if not line:
                    break
                lines.append(line)
            notes = "\n".join(lines)
            print("\n  [ok] Strategy reformulated. Pipeline will use your version.")
            return {"action": "REFORMULATE", "notes": notes}

        elif choice == "REJECT":
            print("\n  [x] Strategy rejected. Pipeline will return to Stage 2.5.")
            return {"action": "REJECT", "notes": ""}

        else:
            print("  Unrecognised command. Type APPROVE, REFORMULATE, or REJECT.")
