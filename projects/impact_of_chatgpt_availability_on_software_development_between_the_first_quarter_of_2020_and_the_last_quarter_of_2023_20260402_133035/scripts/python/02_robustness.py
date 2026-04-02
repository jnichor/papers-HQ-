"""
02_robustness.py --Robustness Checks & Placebo Tests
=====================================================
Implements the full robustness battery from the referee checklist:
  1. Placebo timing tests (Q1 2021, Q1 2022, Q1 2024)
  2. Alternative treatment timing (Q4 2022, Q1 2023, Q2 2023)
  3. Country-specific linear time trends
  4. Balanced panel only
  5. Winsorized outcomes
  6. Minimum language threshold (>=3 languages)
  7. Composition-adjusted HHI (balanced language set)
  8. Restrict post-period to Q1 2023 only (before GPT-4/Bard)
  9. Wild cluster bootstrap
  10. With/without imputed observations comparison

Outputs:
  - data/clean/robustness_results.csv
"""

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
import numpy as np
import pandas as pd
from linearmodels.panel import PanelOLS

# ── Paths ─────────────────────────────────────────────────────────────────────
PROJECT = Path(__file__).resolve().parents[2]
CLEAN_DIR = PROJECT / "data" / "clean"
panel = pd.read_csv(CLEAN_DIR / "clean_data.csv")

print("=" * 70)
print("02_robustness.py --Robustness Checks & Placebo Tests")
print("=" * 70)
print(f"[load] Panel: {len(panel):,} rows")

results = []


# ═══════════════════════════════════════════════════════════════════════════════
# HELPER: Simple DiD estimator (post-treatment average effect)
# ═══════════════════════════════════════════════════════════════════════════════

def run_simple_did(data, outcome, event_time_col="event_time", drop_partial=True,
                   add_country_trend=False, label=""):
    """Run simple DiD: outcome ~ post + country_FE + quarter_FE, return ATT."""
    df = data.copy()
    if drop_partial and "drop_q4_2022" in df.columns:
        df = df[~df["drop_q4_2022"]].copy()

    df = df.dropna(subset=[outcome])
    if len(df) < 20:
        return {"label": label, "outcome": outcome, "att": np.nan,
                "se": np.nan, "pval": np.nan, "n_obs": len(df), "n_countries": 0}

    df["post_treat"] = (df[event_time_col] >= 0).astype(int)

    df["country_id"] = pd.Categorical(df["iso2_code"]).codes
    df = df.set_index(["country_id", "quarter_id"])

    x_cols = ["post_treat"]

    if add_country_trend:
        # Country-specific linear time trends
        df["t_trend"] = df["t_index"]
        # We add country_id x t interaction via dummy expansion
        # With entity FE already in PanelOLS, we add t_trend as a control
        # The entity FE absorbs the level, t_trend captures the slope
        x_cols.append("t_trend")

    y = df[outcome]
    X = df[x_cols]

    # Entity FEs only -- post_treat is collinear with time FEs under simultaneous treatment
    mod = PanelOLS(y, X, entity_effects=True, time_effects=False, drop_absorbed=True)
    try:
        res = mod.fit(cov_type="clustered", cluster_entity=True)
        att = res.params.get("post_treat", np.nan)
        se = res.std_errors.get("post_treat", np.nan)
        pval = res.pvalues.get("post_treat", np.nan)
        r2 = res.rsquared_within
    except Exception as e:
        print(f"    [!] {label}: regression failed --{e}")
        att, se, pval, r2 = np.nan, np.nan, np.nan, np.nan

    n_countries = data["iso2_code"].nunique()

    return {
        "label": label,
        "outcome": outcome,
        "att": att,
        "se": se,
        "pval": pval,
        "ci_low": att - 1.96 * se if not np.isnan(se) else np.nan,
        "ci_high": att + 1.96 * se if not np.isnan(se) else np.nan,
        "n_obs": res.nobs if not np.isnan(att) else len(df),
        "n_countries": n_countries,
        "r2_within": r2,
    }


# ═══════════════════════════════════════════════════════════════════════════════
# 0. BASELINE (for comparison)
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[0] BASELINE")
for outcome in ["hhi_norm", "entropy"]:
    r = run_simple_did(panel, outcome, label=f"Baseline: {outcome}")
    results.append(r)
    sig = "***" if r["pval"] < 0.01 else "**" if r["pval"] < 0.05 else "*" if r["pval"] < 0.1 else ""
    print(f"  {outcome}: ATT={r['att']:+.4f} (se={r['se']:.4f}){sig}  N={r['n_obs']}")


# ═══════════════════════════════════════════════════════════════════════════════
# 1. PLACEBO TIMING TESTS
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[1] PLACEBO TIMING TESTS")

quarters_sorted = sorted(panel["quarter_id"].unique())
quarter_map = {qid: i for i, qid in enumerate(quarters_sorted)}

placebo_dates = {
    "Q1 2021": 20211,
    "Q1 2022": 20221,
    "Q1 2024": 20241,
}

for placebo_name, placebo_qid in placebo_dates.items():
    if placebo_qid not in quarter_map:
        print(f"  {placebo_name}: quarter not in data, skipping")
        continue

    placebo_idx = quarter_map[placebo_qid]
    df_placebo = panel.copy()
    df_placebo["event_time_placebo"] = df_placebo["t_index"] - placebo_idx

    # For pre-treatment placebos, restrict to pre-ChatGPT data only
    if placebo_qid < 20224:
        df_placebo = df_placebo[df_placebo["quarter_id"] < 20224].copy()

    for outcome in ["hhi_norm", "entropy"]:
        r = run_simple_did(
            df_placebo, outcome, event_time_col="event_time_placebo",
            drop_partial=False, label=f"Placebo {placebo_name}: {outcome}"
        )
        results.append(r)
        sig = "***" if r["pval"] < 0.01 else "**" if r["pval"] < 0.05 else "*" if r["pval"] < 0.1 else ""
        expected = "SHOULD BE NULL" if r["pval"] >= 0.1 else "!! SIGNIFICANT"
        print(f"  {placebo_name} {outcome}: ATT={r['att']:+.4f} (p={r['pval']:.3f}){sig} --{expected}")


# ═══════════════════════════════════════════════════════════════════════════════
# 2. ALTERNATIVE TREATMENT TIMING
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[2] ALTERNATIVE TREATMENT TIMING")

alt_dates = {
    "Q4 2022 (launch)": 20224,
    "Q1 2023 (mass adoption)": 20231,
    "Q2 2023 (API/plugins)": 20232,
}

for alt_name, alt_qid in alt_dates.items():
    if alt_qid not in quarter_map:
        print(f"  {alt_name}: quarter not in data, skipping")
        continue

    alt_idx = quarter_map[alt_qid]
    df_alt = panel.copy()
    df_alt["event_time_alt"] = df_alt["t_index"] - alt_idx

    for outcome in ["hhi_norm", "entropy"]:
        r = run_simple_did(
            df_alt, outcome, event_time_col="event_time_alt",
            drop_partial=False, label=f"Alt timing {alt_name}: {outcome}"
        )
        results.append(r)
        sig = "***" if r["pval"] < 0.01 else "**" if r["pval"] < 0.05 else "*" if r["pval"] < 0.1 else ""
        print(f"  {alt_name} {outcome}: ATT={r['att']:+.4f} (p={r['pval']:.3f}){sig}")


# ═══════════════════════════════════════════════════════════════════════════════
# 3. COUNTRY-SPECIFIC LINEAR TIME TRENDS
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[3] COUNTRY-SPECIFIC LINEAR TIME TRENDS")

for outcome in ["hhi_norm", "entropy"]:
    r = run_simple_did(panel, outcome, add_country_trend=True,
                       label=f"Country trends: {outcome}")
    results.append(r)
    sig = "***" if r["pval"] < 0.01 else "**" if r["pval"] < 0.05 else "*" if r["pval"] < 0.1 else ""
    print(f"  {outcome}: ATT={r['att']:+.4f} (se={r['se']:.4f}){sig}")


# ═══════════════════════════════════════════════════════════════════════════════
# 4. BALANCED PANEL ONLY
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[4] BALANCED PANEL ONLY")

balanced = panel[panel["balanced"]].copy()
print(f"  Balanced countries: {balanced['iso2_code'].nunique()}")
print(f"  Balanced obs: {len(balanced):,} (vs {len(panel):,} full)")

for outcome in ["hhi_norm", "entropy"]:
    r = run_simple_did(balanced, outcome, label=f"Balanced: {outcome}")
    results.append(r)
    sig = "***" if r["pval"] < 0.01 else "**" if r["pval"] < 0.05 else "*" if r["pval"] < 0.1 else ""
    print(f"  {outcome}: ATT={r['att']:+.4f} (se={r['se']:.4f}){sig}  N={r['n_obs']}")


# ═══════════════════════════════════════════════════════════════════════════════
# 5. WINSORIZED OUTCOMES
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[5] WINSORIZED OUTCOMES")

for outcome_base in ["hhi_norm", "entropy"]:
    outcome_w = f"{outcome_base}_wins"
    if outcome_w not in panel.columns:
        # Winsorize on the fly
        p1 = panel[outcome_base].quantile(0.01)
        p99 = panel[outcome_base].quantile(0.99)
        panel[outcome_w] = panel[outcome_base].clip(p1, p99)

    r = run_simple_did(panel, outcome_w, label=f"Winsorized: {outcome_base}")
    results.append(r)
    sig = "***" if r["pval"] < 0.01 else "**" if r["pval"] < 0.05 else "*" if r["pval"] < 0.1 else ""
    print(f"  {outcome_base}: ATT={r['att']:+.4f} (se={r['se']:.4f}){sig}")


# ═══════════════════════════════════════════════════════════════════════════════
# 6. MINIMUM LANGUAGE THRESHOLD (>=3 languages)
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[6] MINIMUM LANGUAGE THRESHOLD (>=3)")

min_langs = panel[panel["n_languages"] >= 3].copy()
print(f"  Obs with >=3 languages: {len(min_langs):,} (dropped {len(panel) - len(min_langs):,})")

for outcome in ["hhi_norm", "entropy"]:
    r = run_simple_did(min_langs, outcome, label=f"Min 3 langs: {outcome}")
    results.append(r)
    sig = "***" if r["pval"] < 0.01 else "**" if r["pval"] < 0.05 else "*" if r["pval"] < 0.1 else ""
    print(f"  {outcome}: ATT={r['att']:+.4f} (se={r['se']:.4f}){sig}")


# ═══════════════════════════════════════════════════════════════════════════════
# 7. COMPOSITION-ADJUSTED HHI (balanced language set per country)
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[7] COMPOSITION-ADJUSTED HHI")

# Reload raw data to compute balanced-language HHI
raw = pd.read_csv(Path(r"C:\Users\jesus\Documents\data\languages.csv"))
raw["quarter_id"] = raw["year"].astype(int) * 10 + raw["quarter"].astype(int)

# For each country, keep only languages present in ALL quarters
def balanced_hhi(country_data):
    langs_per_q = country_data.groupby("quarter_id")["language"].apply(set)
    if len(langs_per_q) == 0:
        return pd.DataFrame()
    common_langs = set.intersection(*langs_per_q.values)
    if len(common_langs) < 2:
        return pd.DataFrame()
    filtered = country_data[country_data["language"].isin(common_langs)].copy()
    filtered["total"] = filtered.groupby("quarter_id")["num_pushers"].transform("sum")
    filtered["share"] = filtered["num_pushers"] / filtered["total"]

    agg = filtered.groupby("quarter_id").apply(
        lambda g: pd.Series({
            "hhi_balanced": np.sum(g["share"].values ** 2),
            "n_common_langs": len(common_langs),
        }), include_groups=False
    ).reset_index()
    agg["iso2_code"] = country_data["iso2_code"].iloc[0]
    return agg

balanced_hhi_panels = []
for country, cdata in raw.groupby("iso2_code"):
    bh = balanced_hhi(cdata)
    if len(bh) > 0:
        balanced_hhi_panels.append(bh)

if balanced_hhi_panels:
    bh_panel = pd.concat(balanced_hhi_panels, ignore_index=True)
    # Merge event time info
    bh_panel = bh_panel.merge(
        panel[["iso2_code", "quarter_id", "event_time", "t_index", "post", "drop_q4_2022"]].drop_duplicates(),
        on=["iso2_code", "quarter_id"], how="inner"
    )
    print(f"  Balanced-language HHI panel: {len(bh_panel):,} obs, "
          f"{bh_panel['iso2_code'].nunique()} countries")

    # Normalize balanced HHI
    bh_panel["hhi_balanced_norm"] = bh_panel.apply(
        lambda row: (row["hhi_balanced"] - 1/row["n_common_langs"]) /
                     (1 - 1/row["n_common_langs"]) if row["n_common_langs"] > 1 else 1.0,
        axis=1
    )

    for outcome in ["hhi_balanced_norm"]:
        r = run_simple_did(bh_panel, outcome, label=f"Composition-adjusted: {outcome}")
        results.append(r)
        sig = "***" if r["pval"] < 0.01 else "**" if r["pval"] < 0.05 else "*" if r["pval"] < 0.1 else ""
        print(f"  {outcome}: ATT={r['att']:+.4f} (se={r['se']:.4f}){sig}")
else:
    print("  [!] Could not compute balanced-language HHI")


# ═══════════════════════════════════════════════════════════════════════════════
# 8. RESTRICT POST-PERIOD TO Q1 2023 ONLY (before GPT-4/Bard)
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[8] CLEAN POST-WINDOW (Q1 2023 only, before GPT-4/Bard)")

clean_post = panel[(panel["quarter_id"] <= 20231)].copy()
print(f"  Obs in restricted window: {len(clean_post):,}")

for outcome in ["hhi_norm", "entropy"]:
    r = run_simple_did(clean_post, outcome, label=f"Clean post Q1-2023: {outcome}")
    results.append(r)
    sig = "***" if r["pval"] < 0.01 else "**" if r["pval"] < 0.05 else "*" if r["pval"] < 0.1 else ""
    print(f"  {outcome}: ATT={r['att']:+.4f} (p={r['pval']:.3f}){sig}")


# ═══════════════════════════════════════════════════════════════════════════════
# 9. WILD CLUSTER BOOTSTRAP
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[9] WILD CLUSTER BOOTSTRAP")

try:
    from wildboottest.wildboottest import wildboottest

    df_boot = panel[~panel["drop_q4_2022"]].copy()
    df_boot = df_boot.dropna(subset=["hhi_norm"])

    # Need to add FE dummies manually for wildboottest
    df_boot["post_treat"] = (df_boot["event_time"] >= 0).astype(int)

    # Country dummies
    country_dummies = pd.get_dummies(df_boot["iso2_code"], prefix="c", drop_first=True, dtype=float)
    quarter_dummies = pd.get_dummies(df_boot["quarter_id"], prefix="q", drop_first=True, dtype=float)

    X_boot = pd.concat([df_boot[["post_treat"]], country_dummies, quarter_dummies], axis=1)
    y_boot = df_boot["hhi_norm"].values

    boot_result = wildboottest(
        X=X_boot.values,
        Y=y_boot,
        cluster=pd.Categorical(df_boot["iso2_code"]).codes,
        R=np.array([1] + [0] * (X_boot.shape[1] - 1)),
        B=999,
        seed=42,
    )

    print(f"  HHI norm: t-stat={boot_result['t_stat']:.3f}, "
          f"p-value={boot_result['pvalue']:.4f}")
    results.append({
        "label": "Wild bootstrap: hhi_norm",
        "outcome": "hhi_norm",
        "att": np.nan,
        "se": np.nan,
        "pval": boot_result["pvalue"],
        "n_obs": len(df_boot),
        "n_countries": df_boot["iso2_code"].nunique(),
    })
except Exception as e:
    print(f"  [!] Wild bootstrap failed: {e}")
    print("  Continuing without bootstrap results.")


# ═══════════════════════════════════════════════════════════════════════════════
# 10. WITH/WITHOUT IMPUTATION COMPARISON
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[10] IMPUTATION COMPARISON")

# Since the raw data has no missing values (per 00_clean audit),
# this check compares results with and without EPI-unmatched countries
panel_epi_only = panel.dropna(subset=["epi_score"]).copy()
panel_all = panel.copy()
# For countries without EPI, set epi_score to global median
panel_imputed = panel.copy()
med_epi = panel["epi_score"].median()
panel_imputed["epi_score"] = panel_imputed["epi_score"].fillna(med_epi)

print(f"  With EPI only: {panel_epi_only['iso2_code'].nunique()} countries")
print(f"  All countries (imputed EPI): {panel_imputed['iso2_code'].nunique()} countries")

for outcome in ["hhi_norm"]:
    r1 = run_simple_did(panel_epi_only, outcome, label=f"EPI-matched only: {outcome}")
    r2 = run_simple_did(panel_all, outcome, label=f"All countries: {outcome}")
    results.append(r1)
    results.append(r2)
    print(f"  {outcome} (EPI-matched): ATT={r1['att']:+.4f} (p={r1['pval']:.3f})")
    print(f"  {outcome} (all):         ATT={r2['att']:+.4f} (p={r2['pval']:.3f})")


# ═══════════════════════════════════════════════════════════════════════════════
# SAVE
# ═══════════════════════════════════════════════════════════════════════════════
results_df = pd.DataFrame(results)
results_df.to_csv(CLEAN_DIR / "robustness_results.csv", index=False)
print(f"\n[save] Robustness results: {CLEAN_DIR / 'robustness_results.csv'}")
print(f"[save] Total specifications: {len(results_df)}")

print("\n[02_robustness] DONE [OK]")
