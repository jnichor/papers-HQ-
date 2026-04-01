"""Stage 2 — Ideation (research-junshi).

Generates 8-10 research ideas from seed papers, scores them, and selects the top 3.
"""

from datetime import datetime
from pathlib import Path

from ..config import get_profile
from ..claude_runner import run_claude
from ..json_utils import extract_json
from ..state import save_state


def run(project_dir: Path, state: dict) -> dict:
    """Execute Stage 2: idea generation."""
    stage1 = state["stages"].get("stage1", {})
    topic = stage1.get("topic", "academic research")

    # Include dataset context — prefer downloaded profiles (Stage 1.5) over recommendations
    stage1_5 = state["stages"].get("stage1_5", {})
    downloaded_datasets = stage1_5.get("downloaded_datasets", [])
    recommended_sources = stage1.get("recommended_data_sources", [])
    sources_context = ""

    if downloaded_datasets:
        # Stage 1.5 downloaded and profiled datasets — use REAL variables
        sources_context = "\n\n## DOWNLOADED DATASETS (with real variables)\n\n"
        sources_context += (
            "These datasets have been downloaded and profiled. "
            "Your ideas MUST use variables that ACTUALLY EXIST in these datasets. "
            "For each idea, specify WHICH dataset and WHICH variables it uses.\n\n"
        )
        for i, ds in enumerate(downloaded_datasets, 1):
            profile = ds.get("profile", {})
            sources_context += f"### Dataset {i}: {ds.get('name', '?')}\n"
            sources_context += f"- File: {Path(ds.get('local_path', '?')).name}\n"
            if profile:
                sources_context += f"- Rows: {profile.get('rows', '?'):,}\n"
                sources_context += f"- Columns: {profile.get('cols', '?')}\n"
                sources_context += f"- Structure: {profile.get('structure', '?')}\n"
                id_cols = profile.get("id_cols", [])
                if id_cols:
                    sources_context += f"- ID columns: {', '.join(id_cols[:5])}\n"
                time_cols = profile.get("time_cols", [])
                if time_cols:
                    sources_context += f"- Time columns: {', '.join(time_cols[:5])}\n"
                columns = profile.get("columns", [])
                if columns:
                    sources_context += f"- Variables: {', '.join(columns[:30])}\n"
                    if len(columns) > 30:
                        sources_context += f"  ... ({len(columns)} total)\n"
                data_summary = profile.get("data_summary", "")
                if data_summary:
                    sources_context += f"\n**Data summary:**\n{data_summary}\n"
            sources_context += "\n"

        # Also mention datasets that couldn't be downloaded
        not_downloaded = stage1_5.get("not_downloaded", [])
        if not_downloaded:
            sources_context += "### Datasets NOT downloaded (available for manual download):\n"
            for ds in not_downloaded:
                sources_context += f"- {ds.get('name', '?')} — {ds.get('url', 'N/A')}\n"
            sources_context += "\n"

    elif recommended_sources and not stage1.get("data_profile"):
        # Fallback: Stage 1 recommendations without download (no Stage 1.5)
        sources_context = "\n\n## AVAILABLE DATASETS (from Stage 1 Discovery)\n\n"
        sources_context += (
            "These datasets were identified as the best available for this topic. "
            "Your ideas MUST be designed to work with at least one of these datasets. "
            "For each idea, specify WHICH dataset(s) it uses.\n\n"
        )
        for i, ds in enumerate(recommended_sources[:3], 1):
            sources_context += f"### Dataset {i}: {ds.get('name', '?')}\n"
            sources_context += f"- Provider: {ds.get('provider', '?')}\n"
            sources_context += f"- URL: {ds.get('url', 'N/A')}\n"
            sources_context += f"- Structure: {ds.get('data_structure', '?')}\n"
            sources_context += f"- Time span: {ds.get('time_span', '?')}\n"
            nat_exp = ds.get("natural_experiment", "")
            if nat_exp:
                sources_context += f"- Natural experiment: {nat_exp}\n"
            methods = ds.get("causal_methods_enabled", [])
            if methods:
                sources_context += f"- Causal methods enabled: {', '.join(methods)}\n"
            sources_context += f"- Access: {ds.get('access', '?')}\n"
            sources_context += f"- Format: {ds.get('format', '?')}\n\n"

    # If Path B, include rich data context with structure constraints
    data_profile = stage1.get("data_profile")
    data_context = ""
    if data_profile:
        cols = ", ".join(data_profile.get("columns", [])[:25])
        if len(data_profile.get("columns", [])) > 25:
            cols += f", ... ({data_profile['cols']} total)"
        structure = data_profile.get("structure", "unknown")
        panel_details = data_profile.get("panel_details", {})

        # Build structure-specific constraints
        wide_panel = data_profile.get("wide_panel")
        if structure == "wide-panel" and wide_panel:
            core_sample = ", ".join(panel_details.get("core_vars_sample", [])[:10])
            suffixes = panel_details.get("year_suffixes", [])
            years = panel_details.get("time_values", [])
            unsuffixed = ", ".join(panel_details.get("unsuffixed_cols", [])[:15])
            vars_per = panel_details.get("vars_per_period", {})
            vars_per_str = ", ".join(f"{s}: {n} vars" for s, n in vars_per.items())
            structure_block = (
                f"DATA STRUCTURE: WIDE-FORMAT PANEL — time encoded in column name suffixes.\n"
                f"  Year suffixes: {', '.join(suffixes)}\n"
                f"  Corresponding years: {years}\n"
                f"  Time periods: {panel_details.get('n_time_periods', '?')}\n"
                f"  Variables per period: {vars_per_str}\n"
                f"  Core variables (shared across all periods): {panel_details.get('n_core_vars', '?')}\n"
                f"  Sample base vars: {core_sample}\n"
                f"  Time-invariant/ID columns: {unsuffixed}\n"
                f"\n"
                f"  IMPORTANT: Each variable appears once per year with a suffix "
                f"(e.g., variable_{suffixes[0]}, variable_{suffixes[-1]}).\n"
                f"  The data MUST be reshaped from wide to long format before panel analysis.\n"
                f"  After reshaping: one row per individual-year, with columns for year, ID, "
                f"and all base variables.\n"
                f"\n"
                f"  This IS panel data (same individuals tracked over {len(years)} years: {years}).\n"
                f"\n"
                f"  *** PRIORITY METHODS (exploit the panel dimension — use these first): ***\n"
                f"  DiD, event study, TWFE, individual fixed effects, dynamic panel (Arellano-Bond),\n"
                f"  correlated random effects, Markov transition matrices, survival models.\n"
                f"\n"
                f"  SECONDARY METHODS (cross-sectional, use sparingly — max 1 of 3 top ideas):\n"
                f"  IV, RDD, matching (PSM, CEM), Oaxaca-Blinder, quantile regression.\n"
                f"\n"
                f"  AT LEAST 2 of the top 3 ideas MUST use panel methods that exploit within-individual\n"
                f"  variation over time. The whole point of having panel data is to control for\n"
                f"  unobserved heterogeneity — do NOT waste it on purely cross-sectional designs.\n"
                f"  Scripts MUST include a wide-to-long reshape step before estimation.\n"
            )
        elif structure == "panel":
            pd_info = panel_details
            structure_block = (
                f"DATA STRUCTURE: TRUE PANEL — same individuals tracked over time.\n"
                f"  ID column: {pd_info.get('id_column', '?')}\n"
                f"  Time column: {pd_info.get('time_column', '?')}\n"
                f"  Unique individuals: {pd_info.get('n_unique_ids', '?')}\n"
                f"  Time periods: {pd_info.get('n_time_periods', '?')}\n"
                f"\n"
                f"  *** PRIORITY METHODS (exploit the panel dimension — use these first): ***\n"
                f"  DiD, event study, TWFE, individual fixed effects, dynamic panel (Arellano-Bond),\n"
                f"  correlated random effects, Markov transition matrices, survival models.\n"
                f"\n"
                f"  SECONDARY METHODS (cross-sectional, use sparingly — max 1 of 3 top ideas):\n"
                f"  IV, RDD, matching (PSM, CEM), Oaxaca-Blinder, quantile regression.\n"
                f"\n"
                f"  AT LEAST 2 of the top 3 ideas MUST use panel methods that exploit within-individual\n"
                f"  variation over time. The whole point of having panel data is to control for\n"
                f"  unobserved heterogeneity — do NOT waste it on purely cross-sectional designs.\n"
            )
        elif structure == "pooled-cross-sections":
            structure_block = (
                f"DATA STRUCTURE: POOLED CROSS-SECTIONS — different individuals each period.\n"
                f"  Time column: {panel_details.get('time_column', '?')}\n"
                f"  Time periods: {panel_details.get('n_time_periods', '?')}\n"
                f"  Time values: {panel_details.get('time_values', [])}\n"
                f"  IDs repeating across periods: ONLY {panel_details.get('pct_ids_multiple_periods', 0)}%\n"
                f"\n"
                f"  ALLOWED methods: group-level DiD, repeated cross-section DiD, IV, RDD,\n"
                f"    propensity score matching, Oaxaca-Blinder decomposition, cohort analysis.\n"
                f"  FORBIDDEN methods (require individual tracking): individual FE, individual\n"
                f"    event study, Markov transition matrices, survival/hazard models,\n"
                f"    Arellano-Bond, within-individual variation.\n"
            )
        elif structure == "repeated-cross-sections":
            structure_block = (
                f"DATA STRUCTURE: REPEATED CROSS-SECTIONS — multiple waves, no individual ID.\n"
                f"  Time column: {panel_details.get('time_column', '?')}\n"
                f"  Time periods: {panel_details.get('n_time_periods', '?')}\n"
                f"\n"
                f"  ALLOWED methods: group-level DiD, IV, RDD, decompositions, cohort/pseudo-panel.\n"
                f"  FORBIDDEN: individual FE, individual event study, transition matrices.\n"
            )
        else:
            structure_block = (
                f"DATA STRUCTURE: SINGLE CROSS-SECTION — one time snapshot.\n"
                f"\n"
                f"  ALLOWED methods: IV, RDD, matching (PSM, CEM), Oaxaca-Blinder,\n"
                f"    Heckman selection, quantile regression.\n"
                f"  FORBIDDEN: DiD, event study, FE, transition matrices, any method\n"
                f"    requiring time variation.\n"
            )

        data_context = f"""

## USER DATASET (Path B) — READ CAREFULLY

{structure_block}
- Rows: {data_profile.get('rows', '?'):,}
- Columns: {data_profile.get('cols', '?')}
- Variables: {cols}
- ID columns: {', '.join(data_profile.get('id_cols', [])[:5]) or 'None detected'}
- Time columns: {', '.join(data_profile.get('time_cols', [])[:5]) or 'None detected'}

## CRITICAL CONSTRAINTS

1. Every idea you propose MUST use ONLY methods compatible with the data structure above.
   If you propose an incompatible method, the idea will be automatically rejected in
   Stage 3 validation.
2. If the data has a panel or time dimension, you MUST exploit it. Panel data is rare
   and valuable — proposing only cross-sectional methods on panel data is a waste of
   the researcher's data advantage. Prioritize methods that use within-unit variation
   over time (FE, DiD, TWFE, event study, dynamic panel) over purely cross-sectional
   approaches (IV, RDD, matching).
3. Design your identification strategy around the STRONGEST feature of this data."""

    # Determine if panel methods should be enforced
    is_panel = data_profile and data_profile.get("structure") in ("panel", "wide-panel")

    panel_enforcement = ""
    if is_panel:
        panel_enforcement = f"""
## *** MANDATORY: PANEL DATA METHOD REQUIREMENT ***

You have PANEL DATA. This is the single most important fact about this dataset.
Panel data lets you track the SAME individuals over time and control for ALL
time-invariant unobserved heterogeneity (individual fixed effects).

HARD RULES — violation means automatic rejection:
- AT LEAST 6 of your 8-10 ideas MUST use a panel method as the PRIMARY method.
  Panel methods: individual FE, TWFE, DiD, event study, dynamic panel (Arellano-Bond),
  correlated random effects (CRE), Markov transition matrices, survival/hazard models.
- AT LEAST 2 of your TOP 3 ideas MUST use panel methods.
- Cross-sectional methods (IV, RDD, matching, Oaxaca-Blinder, quantile regression)
  are allowed for AT MOST 1 of the top 3. They do NOT exploit the panel dimension.

Think about what CHANGES over time in this data: do people gain education? switch
from informal to formal jobs? move regions? start/stop working? These transitions
are the gold mine of panel data. Design your ideas around TRANSITIONS and CHANGES,
not static snapshots.
"""

    # ── Read feasibility constraints from Stage 1.5 ─────────────────────
    feasibility = state["stages"].get("stage1_5", {}).get("feasibility", {})
    max_tier = feasibility.get("max_tier", 1)
    score_ceiling = feasibility.get("score_ceiling", 100)
    allowed_methods = feasibility.get("allowed_methods", [])
    forbidden_methods = feasibility.get("forbidden_methods", [])
    feasibility_warnings = feasibility.get("warnings", [])

    feasibility_block = ""
    if feasibility:
        self_contained = feasibility.get("self_contained", True)
        n_ordinal = feasibility.get("n_ordinal_vars", 0)
        n_continuous = feasibility.get("n_continuous_vars", 0)

        self_contained_warning = ""
        if not self_contained:
            self_contained_warning = """
  *** SELF-CONTAINMENT WARNING: This dataset does NOT contain both treatment
  and continuous outcome variables. Ideas that require merging with external
  datasets are RISKY — merge attrition, coding inconsistencies, and coverage
  gaps will reduce the effective sample and weaken identification.
  STRONGLY PREFER ideas that use ONLY variables already in this dataset.
  If external data is needed, it must be simple (1-2 variables, well-known source). ***
"""

        ordinal_warning = ""
        if n_ordinal > 0 and n_continuous == 0:
            ordinal_warning = f"""
  *** ORDINAL OUTCOME WARNING: All {n_ordinal} numeric variables are ordinal
  (<=7 unique values). Within-unit variation will be very low.
  PREFER methods that work well with ordinal outcomes:
  - Ordered probit/logit with FE
  - Linear probability model for binary recodings
  - Transition matrices (prob of moving between categories)
  DO NOT propose DiD/event study on ordinal variables with 3-4 values —
  the referee will reject on power grounds. ***
"""
        elif n_ordinal > n_continuous:
            ordinal_warning = f"""
  *** MOSTLY ORDINAL DATA: {n_ordinal} ordinal vs {n_continuous} continuous vars.
  Prefer ideas that use the continuous variables as outcomes. ***
"""

        feasibility_block = f"""
## *** DATA FEASIBILITY CONSTRAINTS (from Stage 1.5 assessment) ***

The data has been downloaded and profiled. Based on its structure, these are the
HARD CONSTRAINTS on what methods are feasible:

  Maximum method tier: {max_tier} ({feasibility.get('tier_label', 'unknown')})
  Score ceiling with this data: {score_ceiling}/100
  Allowed methods: {', '.join(allowed_methods) if allowed_methods else 'all'}
  FORBIDDEN methods: {', '.join(forbidden_methods) if forbidden_methods else 'none'}

{'Data limitations:' if feasibility_warnings else ''}
{chr(10).join('  - ' + w for w in feasibility_warnings)}
{self_contained_warning}
{ordinal_warning}

*** CRITICAL: Do NOT propose methods listed as FORBIDDEN above. ***
*** Ideas using forbidden methods will be AUTOMATICALLY REJECTED. ***
*** Only propose methods that the data can ACTUALLY support. ***
*** A realistic, well-identified Tier {max_tier} design scores higher than ***
*** an ambitious but flawed Tier 1 design that referees will destroy. ***
"""

    prompt = f"""You are a bold but REALISTIC research advisor (Junshi). Your task:

RESEARCH AREA: {topic}

## *** CAUSAL IDENTIFICATION PRIORITY ***

Top journals require CAUSAL identification strategies. Always prefer methods that
establish causality over purely descriptive or correlational approaches.
BUT: only propose methods that the available data can ACTUALLY SUPPORT.
An overambitious design that fails at peer review is worse than a modest but
credible design that survives.

METHOD HIERARCHY (strongest to weakest — aim for the highest FEASIBLE tier):
  Tier 1 (CAUSAL): DiD, event study, IV/2SLS, RDD, RCT, synthetic control
  Tier 2 (PANEL-CAUSAL): TWFE, individual FE + exogenous shock, Arellano-Bond GMM, CRE
  Tier 3 (PANEL-DESCRIPTIVE): individual FE without clear identification, within-estimator
  Tier 4 (CROSS-SECTION): OLS, matching (PSM/CEM), Oaxaca-Blinder, quantile regression,
          decompositions, probit/logit, Heckman selection

HARD RULES:
- Only propose methods up to Tier {max_tier}. Methods beyond this tier are FORBIDDEN.
- For EACH idea, you must explain WHY the data supports the proposed method:
  (a) What is the source of exogenous variation?
  (b) How many pre-treatment periods are available?
  (c) Can parallel trends be tested? With how many pre-periods?
  (d) Are there enough clusters for reliable inference?
  (e) Is the treatment plausibly exogenous? What threatens this?
- If you cannot answer ALL of (a)-(e) convincingly, downgrade to a lower tier.
- A Tier 2 design with strong identification beats a Tier 1 design with weak ID.

{feasibility_block}
{panel_enforcement}
{data_context}
{sources_context}

Based on the current state of research in {topic}:

1. Identify the key themes, methods, and gaps across these papers.
2. Generate 8-10 bold, specific research ideas. Each must be actionable — not "explore X"
   but "do Y to achieve Z, enabled by insight W."

   CRITICAL DIVERSITY RULE: The 8-10 ideas MUST span at least 5 DISTINCT sub-topics
   within "{topic}". Do NOT cluster ideas around a single theme (e.g., do not generate
   4 ideas about wage gaps). Use the seed papers as starting points but BRANCH OUT
   into other important sub-areas of the field. Adapt sub-areas to the specific topic.

   CRITICAL METHOD-DATA FIT RULE: Your method choices MUST match the strongest
   feature of the available data. If the data is panel, the majority of ideas MUST
   exploit within-individual variation over time. A reviewer will immediately ask
   "why didn't you use FE/DiD if you have panel data?" — your ideas must use those methods.

3. For each idea, specify:
   - A clear research question
   - Proposed empirical method — ALWAYS prefer Tier 1-2 causal methods. For each idea,
     state the TIER (1-4) and the SOURCE OF IDENTIFYING VARIATION.
   - Data sources needed
   - Why this is novel and impactful
   - Sub-topic category (to verify diversity)
4. Score each idea:
   - Novelty (1-5)
   - Feasibility (1-5)
   - Impact (1-5)
   - Total = Novelty * 0.4 + Feasibility * 0.3 + Impact * 0.3
   - Causal bonus: add +0.3 to the total score of any idea that uses a Tier 1-2 causal method.
   {"- Panel bonus: add +0.3 to the total score of any idea that uses a panel method as primary method." if is_panel else ""}
5. Select the TOP 3 ideas and elaborate on each. The top 3 MUST come from
   3 DIFFERENT sub-topics. Never select 2 ideas from the same sub-topic.
   AT LEAST 2 of the top 3 MUST use Tier 1 or Tier 2 causal methods.
   {"AT LEAST 2 of the top 3 MUST use panel methods (FE, DiD, TWFE, event study, dynamic panel)." if is_panel else ""}

IMPORTANT: At the end, output a JSON block:
```json
{{
  "top_ideas": [
    {{
      "rank": 1,
      "title": "...",
      "research_question": "...",
      "method": "DiD",
      "sub_topic": "informality",
      "data_sources": ["..."],
      "novelty": 4,
      "feasibility": 4,
      "impact": 5,
      "total_score": 4.3,
      "pitch": "2-3 sentence pitch",
      "first_experiment": "What you'd do in week 1"
    }}
  ]
}}
```
"""
    output_file = project_dir / "stage2_ideation.md"
    p = get_profile("stage2")
    response = run_claude(prompt, model=p["model"], effort=p["effort"], output_file=output_file)
    ideas_data = extract_json(response)

    state["stages"]["stage2"] = {
        "status": "completed",
        "output_file": str(output_file),
        "completed_at": datetime.now().isoformat(),
    }

    if ideas_data and "top_ideas" in ideas_data:
        state["stages"]["stage2"]["top_ideas"] = ideas_data["top_ideas"]
        print(f"  [ok] Generated {len(ideas_data['top_ideas'])} top ideas")
    else:
        print("  [warn] Could not parse structured JSON. Check stage2_ideation.md manually.")

    state["current_stage"] = 2
    save_state(project_dir, state)
    return state
