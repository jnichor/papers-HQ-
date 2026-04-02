"""Stage 4 automated validator.

Checks objective facts about generated scripts and their outputs:
script existence, execution success, output files, code patterns.
"""

import re
from pathlib import Path

from . import CheckLevel, ValidationResult


EXPECTED_SCRIPTS = ["00_clean.py", "01_main.py", "02_robustness.py", "03_output.py"]


def validate(
    scripts_dir: Path, project_dir: Path, all_results: dict
) -> ValidationResult:
    vr = ValidationResult()
    _check_scripts_exist(vr, scripts_dir)
    _check_scripts_ran(vr, all_results)
    _check_output_files(vr, scripts_dir, project_dir)
    _check_results_summary_content(vr, scripts_dir, project_dir)
    _check_code_patterns(vr, scripts_dir)
    _check_referee_checklist_coverage(vr, scripts_dir, project_dir)
    return vr


# ── HARD checks ──────────────────────────────────────────────────────────────

def _check_scripts_exist(vr: ValidationResult, scripts_dir: Path):
    for name in EXPECTED_SCRIPTS:
        exists = (scripts_dir / name).exists()
        vr.add(
            f"script_exists:{name}", CheckLevel.HARD, exists,
            f"{name} {'found' if exists else 'MISSING'}"
        )


def _check_scripts_ran(vr: ValidationResult, all_results: dict):
    for name in EXPECTED_SCRIPTS:
        result = all_results.get(name, {})
        ok = result.get("ok", False)
        if ok:
            detail = "ran OK"
        else:
            stderr = result.get("stderr", "unknown error")
            detail = f"FAILED: {stderr[:200]}"
        vr.add(f"script_ran:{name}", CheckLevel.HARD, ok, detail)


def _check_output_files(vr: ValidationResult, scripts_dir: Path, project_dir: Path):
    clean_dir = project_dir / "data" / "clean"
    tables_dir = project_dir / "paper" / "tables"
    figures_dir = project_dir / "paper" / "figures"

    # Clean data file
    clean_files = (
        list(clean_dir.glob("*.parquet"))
        + list(clean_dir.glob("*.csv"))
        if clean_dir.exists() else []
    )
    vr.add(
        "clean_data_exists", CheckLevel.HARD, len(clean_files) > 0,
        f"Found {len(clean_files)} data file(s) in data/clean/"
        if clean_files else "No .parquet or .csv in data/clean/"
    )

    # Tables — accept .tex files in tables/ OR tables embedded in main.tex
    tex_files = list(tables_dir.glob("*.tex")) if tables_dir.exists() else []
    # Also check for tables in main.tex or .md summary files
    other_table_files = (
        list(tables_dir.glob("*.md")) if tables_dir.exists() else []
    )
    main_tex = tables_dir.parent / "main.tex" if tables_dir.exists() else Path(".")
    has_inline_tables = False
    if main_tex.exists():
        main_content = main_tex.read_text(encoding="utf-8")
        has_inline_tables = r"\begin{table}" in main_content or r"\begin{tabular}" in main_content
    tables_found = len(tex_files) > 0 or len(other_table_files) > 0 or has_inline_tables
    vr.add(
        "tables_exist", CheckLevel.HARD, tables_found,
        f"Found {len(tex_files)} .tex table(s)" + (", inline tables in main.tex" if has_inline_tables else "")
        + (f", {len(other_table_files)} summary file(s)" if other_table_files else "")
        if tables_found else "No tables found in paper/tables/ or main.tex"
    )

    # Figures (SOFT — some papers are table-only)
    pdf_files = list(figures_dir.glob("*.pdf")) if figures_dir.exists() else []
    vr.add(
        "figures_exist", CheckLevel.SOFT, len(pdf_files) > 0,
        f"Found {len(pdf_files)} figure(s): {', '.join(f.name for f in pdf_files[:5])}"
        if pdf_files else "No .pdf files in paper/figures/"
    )

    # results_summary.md
    summary_path = _find_results_summary(scripts_dir, project_dir)
    vr.add(
        "results_summary_exists", CheckLevel.HARD, summary_path is not None,
        f"Found at {summary_path}" if summary_path else
        "results_summary.md not found in scripts/ or data/clean/"
    )

    # Non-empty check for all outputs
    all_outputs = tex_files + pdf_files + clean_files
    if summary_path:
        all_outputs.append(summary_path)
    empty_files = [f for f in all_outputs if f.stat().st_size == 0]
    vr.add(
        "outputs_non_empty", CheckLevel.HARD, len(empty_files) == 0,
        f"{len(empty_files)} empty file(s): {', '.join(f.name for f in empty_files)}"
        if empty_files else f"All {len(all_outputs)} output files are non-empty"
    )


# ── SOFT checks ──────────────────────────────────────────────────────────────

def _check_results_summary_content(
    vr: ValidationResult, scripts_dir: Path, project_dir: Path
):
    summary_path = _find_results_summary(scripts_dir, project_dir)
    if not summary_path:
        return  # already flagged by _check_output_files

    text = summary_path.read_text(encoding="utf-8")
    numbers = re.findall(r'-?\d+\.?\d*', text)
    has_numbers = len(numbers) >= 3
    vr.add(
        "results_summary_has_numbers", CheckLevel.SOFT, has_numbers,
        f"Found {len(numbers)} numeric values"
        if has_numbers else
        f"Only {len(numbers)} numbers found — likely placeholder text"
    )


def _check_code_patterns(vr: ValidationResult, scripts_dir: Path):
    # Seed setting
    for name in EXPECTED_SCRIPTS:
        path = scripts_dir / name
        if not path.exists():
            continue
        code = path.read_text(encoding="utf-8")

        if name == "00_clean.py":
            has_seed = bool(re.search(r'(np\.random\.seed|random\.seed|seed\s*=)', code))
            vr.add(
                f"seed_set:{name}", CheckLevel.SOFT, has_seed,
                "Random seed found" if has_seed else "No random seed set"
            )

    # SE clustering in regression scripts
    for name in ["01_main.py", "02_robustness.py"]:
        path = scripts_dir / name
        if not path.exists():
            continue
        code = path.read_text(encoding="utf-8")
        has_cluster = bool(re.search(
            r'(cov_type.*cluster|\.fit\(.*cluster|get_robustcov|ClusteredSE|cluster.*se)',
            code, re.IGNORECASE
        ))
        vr.add(
            f"se_clustering:{name}", CheckLevel.SOFT, has_cluster,
            "Clustering pattern found" if has_cluster else
            "No SE clustering detected — verify this is intentional"
        )

    # Imports in 01_main.py
    main_path = scripts_dir / "01_main.py"
    if main_path.exists():
        code = main_path.read_text(encoding="utf-8")
        has_stats = bool(re.search(
            r'(import statsmodels|import linearmodels|from statsmodels|from linearmodels'
            r'|import pyfixest|from pyfixest|import did|from csdid)',
            code
        ))
        vr.add(
            "stats_library_imported", CheckLevel.SOFT, has_stats,
            "Statistical library imported"
            if has_stats else
            "No statsmodels/linearmodels/pyfixest import found in 01_main.py"
        )

    # ── Causal method checks ──────────────────────────────────────────────
    # Check if scripts implement key causal inference requirements
    all_code = ""
    for name in ["01_main.py", "02_robustness.py"]:
        path = scripts_dir / name
        if path.exists():
            all_code += path.read_text(encoding="utf-8") + "\n"

    if all_code:
        # Detect if this is a DiD/event study design
        is_did = bool(re.search(
            r'(did|diff.*in.*diff|event.study|twfe|two.way.*fixed)',
            all_code, re.IGNORECASE
        ))

        if is_did:
            # Pre-trend test
            has_pretrend = bool(re.search(
                r'(pre.?trend|pre.?period|parallel.*trend|f.?test.*pre|joint.*test.*pre'
                r'|placebo.*test|false.*treatment)',
                all_code, re.IGNORECASE
            ))
            vr.add(
                "pretrend_test", CheckLevel.SOFT, has_pretrend,
                "Pre-trend or placebo test found"
                if has_pretrend else
                "No pre-trend/placebo test detected — required for DiD/event study"
            )

            # Wild cluster bootstrap
            has_wcb = bool(re.search(
                r'(wild.*cluster.*bootstrap|wildboottest|boottest|wcb|rademacher'
                r'|bootstrap.*cluster)',
                all_code, re.IGNORECASE
            ))
            vr.add(
                "wild_cluster_bootstrap", CheckLevel.SOFT, has_wcb,
                "Wild cluster bootstrap found"
                if has_wcb else
                "No wild cluster bootstrap detected — recommended for <50 clusters"
            )

            # Heterogeneity-robust estimator — only flag if staggered treatment
            is_staggered = bool(re.search(
                r'(stagger|cohort.*treat|treatment.*timing|adoption.*year'
                r'|treat.*year.*var|first.*treat)',
                all_code, re.IGNORECASE
            ))
            is_common_shock = bool(re.search(
                r'(common.*shock|simultaneous|all.*units.*treat|universal.*treat'
                r'|covid.*shock|pandemic.*shock)',
                all_code, re.IGNORECASE
            ))

            if is_staggered and not is_common_shock:
                # Staggered treatment: Sun-Abraham/CS is essential
                has_het_robust = bool(re.search(
                    r'(sun.*abraham|callaway.*sant|de.*chaisemartin|bacon.*decomp'
                    r'|interaction.weighted|SA.*estimator|CS.*estimator|DIDM)',
                    all_code, re.IGNORECASE
                ))
                vr.add(
                    "het_robust_estimator", CheckLevel.SOFT, has_het_robust,
                    "Heterogeneity-robust estimator found (Sun-Abraham/CS/DIDM)"
                    if has_het_robust else
                    "STAGGERED DiD detected but no Sun-Abraham/Callaway-Sant'Anna — "
                    "TWFE may produce biased estimates with negative weights"
                )
            elif not is_common_shock:
                # Unknown treatment structure: soft recommendation
                has_het_robust = bool(re.search(
                    r'(sun.*abraham|callaway.*sant|de.*chaisemartin|bacon.*decomp'
                    r'|interaction.weighted|SA.*estimator|CS.*estimator|DIDM)',
                    all_code, re.IGNORECASE
                ))
                if has_het_robust:
                    vr.add(
                        "het_robust_estimator", CheckLevel.SOFT, True,
                        "Heterogeneity-robust estimator found"
                    )


# ── Referee checklist coverage ────────────────────────────────────────────────

# Keywords that indicate a MUST requirement is addressed in the code.
# Each tuple: (checklist keyword pattern, code keyword patterns)
_CHECKLIST_CODE_MAP = [
    # Estimation
    (r"event.study|distributed.lag", [r"event.?time|event.?study|distributed.?lag"]),
    (r"cluster.*standard.*error", [r"cluster|cov_type.*cluster"]),
    (r"wild.*cluster.*bootstrap", [r"wildboot|wild.*cluster.*bootstrap|boottest|rademacher"]),
    (r"pre.?trend.*test|joint.*f.?test", [r"pre.?trend|f.?test|wald.*test|joint.*test"]),
    (r"heterogeneity.*interact", [r"interact|_x_|epi.*post|treatment.*var"]),
    (r"placebo.*test", [r"placebo|fake.*treat|false.*treatment"]),
    (r"country.*specific.*trend", [r"country.*trend|t_trend|linear.*trend"]),
    (r"balanced.*panel", [r"balanced|balance"]),
    (r"winsoriz", [r"winsoriz|clip|percentile.*trim"]),
    (r"composition.*effect|language.*entry", [r"composition|n_language|balanced.*lang"]),
    (r"hhi.*shannon|both.*outcome", [r"hhi.*entropy|entropy.*hhi|for.*outcome"]),
    (r"summary.*statistic", [r"summary.*stat|describe|mean.*sd"]),
    (r"normalized.*hhi", [r"hhi_norm|normalized"]),
    (r"data.*provenance", [r"provenance|source.*log"]),
    (r"missingness|missing.*data", [r"miss|isnull|dropna|MCAR|MAR"]),
]


def _check_referee_checklist_coverage(
    vr: ValidationResult, scripts_dir: Path, project_dir: Path
):
    """Cross-check referee MUST requirements against generated code."""
    checklist_path = project_dir / "strategy" / "referee_checklist.md"
    if not checklist_path.exists():
        return

    cl_text = checklist_path.read_text(encoding="utf-8")

    # Extract MUST requirements
    musts = []
    in_must = False
    for line in cl_text.splitlines():
        if "MUST-HAVE" in line or "MUST" in line and "##" in line:
            in_must = True
            continue
        if in_must and line.startswith("## "):
            break
        if in_must and line.strip().startswith("- "):
            musts.append(line.strip("- ").strip())

    if not musts:
        return

    # Read all script code
    all_code = ""
    for name in EXPECTED_SCRIPTS:
        path = scripts_dir / name
        if path.exists():
            all_code += path.read_text(encoding="utf-8") + "\n"

    if not all_code:
        return

    all_code_lower = all_code.lower()

    # Check each MUST against code
    implemented = 0
    not_implemented = []
    for must in musts:
        must_lower = must.lower()
        found = False
        for checklist_pat, code_pats in _CHECKLIST_CODE_MAP:
            if re.search(checklist_pat, must_lower):
                if any(re.search(cp, all_code_lower) for cp in code_pats):
                    found = True
                    break
        if found:
            implemented += 1
        else:
            not_implemented.append(must[:80])

    total = len(musts)
    coverage_pct = (implemented / total * 100) if total > 0 else 0

    vr.add(
        "referee_checklist_coverage", CheckLevel.SOFT,
        coverage_pct >= 60,
        f"Referee checklist: {implemented}/{total} MUST requirements detected in code "
        f"({coverage_pct:.0f}%)"
    )

    if not_implemented:
        # Log first few missing for the report
        missing_preview = "; ".join(not_implemented[:5])
        if len(not_implemented) > 5:
            missing_preview += f" ... and {len(not_implemented) - 5} more"
        vr.add(
            "referee_checklist_missing", CheckLevel.SOFT,
            len(not_implemented) <= total * 0.4,
            f"Possibly unimplemented: {missing_preview}"
        )


# ── Helpers ──────────────────────────────────────────────────────────────────

def _find_results_summary(scripts_dir: Path, project_dir: Path):
    for candidate in [
        scripts_dir / "results_summary.md",
        project_dir / "data" / "clean" / "results_summary.md",
        project_dir / "paper" / "results_summary.md",
        project_dir / "paper" / "tables" / "results_summary.md",
        project_dir / "results_summary.md",
    ]:
        if candidate.exists():
            return candidate
    return None
