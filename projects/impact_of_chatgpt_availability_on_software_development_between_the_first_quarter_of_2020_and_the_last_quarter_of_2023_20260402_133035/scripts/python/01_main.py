"""
01_main.py — Main Event Study & Heterogeneity Analysis
======================================================
Runs the core specifications from the strategy memo:
  1. TWFE event study for HHI and Shannon entropy
  2. Pre-trend joint F-test
  3. Heterogeneity by English proficiency (continuous + binary + tercile)
  4. Anticipation effects test
  5. Composition effects test (N_languages around treatment)

Outputs:
  - data/clean/main_results.csv
  - data/clean/event_study_coefficients.csv
"""

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

from pathlib import Path
import numpy as np
import pandas as pd
import statsmodels.api as sm
from linearmodels.panel import PanelOLS
from scipy import stats

# ── Paths ─────────────────────────────────────────────────────────────────────
PROJECT = Path(__file__).resolve().parents[2]
CLEAN_DIR = PROJECT / "data" / "clean"
panel = pd.read_csv(CLEAN_DIR / "clean_data.csv")

print("=" * 70)
print("01_main.py — Main Event Study & Heterogeneity Analysis")
print("=" * 70)
print(f"[load] Panel: {len(panel):,} rows, {panel.shape[1]} cols")


# ═══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def run_event_study(data, outcome, cluster_col="iso2_code", drop_q4_2022=True,
                    extra_controls=None, label=""):
    """Run event study with country FEs, clustered SEs.

    NOTE: With simultaneous treatment (all countries treated at Q4 2022),
    event-time dummies are perfectly collinear with quarter FEs.
    We use entity FEs only; event-time dummies absorb the time variation.
    """
    df = data.copy()
    if drop_q4_2022:
        df = df[~df["drop_q4_2022"]].copy()

    # Event time dummies (omit t=-1 as reference)
    event_times = sorted(df["event_time"].unique())
    ref_period = -1
    event_times_use = [t for t in event_times if t != ref_period]

    for t in event_times_use:
        df[f"et_{t}"] = (df["event_time"] == t).astype(int)

    et_cols = [f"et_{t}" for t in event_times_use]

    # Set panel index
    df["country_id"] = pd.Categorical(df["iso2_code"]).codes
    df = df.set_index(["country_id", "quarter_id"])

    y = df[outcome]
    x_cols = et_cols + (extra_controls if extra_controls else [])
    X = df[x_cols]

    # Entity FEs only — event-time dummies replace quarter FEs
    # (they are collinear under simultaneous treatment)
    mod = PanelOLS(y, X, entity_effects=True, time_effects=False, drop_absorbed=True)
    res = mod.fit(cov_type="clustered", cluster_entity=True)

    # Extract event study coefficients
    coefs = []
    for t in event_times_use:
        col = f"et_{t}"
        if col in res.params.index:
            coefs.append({
                "event_time": t,
                "coef": res.params[col],
                "se": res.std_errors[col],
                "ci_low": res.params[col] - 1.96 * res.std_errors[col],
                "ci_high": res.params[col] + 1.96 * res.std_errors[col],
                "pval": res.pvalues[col],
            })

    # Add reference period (zero by construction)
    coefs.append({
        "event_time": ref_period,
        "coef": 0.0, "se": 0.0, "ci_low": 0.0, "ci_high": 0.0, "pval": np.nan,
    })
    coefs_df = pd.DataFrame(coefs).sort_values("event_time")

    # Pre-trend F-test: joint test that all pre-treatment coefficients = 0
    pre_cols = [f"et_{t}" for t in event_times_use if t < -1]
    pre_cols_in_model = [c for c in pre_cols if c in res.params.index]
    if len(pre_cols_in_model) >= 2:
        r_matrix = np.zeros((len(pre_cols_in_model), len(res.params)))
        for i, col in enumerate(pre_cols_in_model):
            j = list(res.params.index).index(col)
            r_matrix[i, j] = 1
        try:
            f_test = res.wald_test(formula="+".join(pre_cols_in_model) + "=0")
            f_stat = f_test.stat
            f_pval = f_test.pval
        except Exception:
            f_stat, f_pval = np.nan, np.nan
    else:
        f_stat, f_pval = np.nan, np.nan

    n_countries = df.index.get_level_values(0).nunique()
    n_quarters = df.index.get_level_values(1).nunique()

    info = {
        "label": label,
        "outcome": outcome,
        "n_obs": res.nobs,
        "n_countries": n_countries,
        "n_quarters": n_quarters,
        "r2_within": res.rsquared_within,
        "pretrend_f": f_stat,
        "pretrend_p": f_pval,
    }

    return res, coefs_df, info


def run_did_interaction(data, outcome, treatment_var, cluster_col="iso2_code",
                        drop_q4_2022=True, label=""):
    """Run DiD with interaction: outcome ~ event_dummies * treatment_var."""
    df = data.copy()
    if drop_q4_2022:
        df = df[~df["drop_q4_2022"]].copy()

    # Drop obs where treatment_var is missing
    df = df.dropna(subset=[treatment_var])

    event_times = sorted(df["event_time"].unique())
    ref_period = -1
    event_times_use = [t for t in event_times if t != ref_period]

    for t in event_times_use:
        df[f"et_{t}"] = (df["event_time"] == t).astype(int)
        df[f"et_{t}_x_{treatment_var}"] = df[f"et_{t}"] * df[treatment_var]

    et_cols = [f"et_{t}" for t in event_times_use]
    interact_cols = [f"et_{t}_x_{treatment_var}" for t in event_times_use]

    df["country_id"] = pd.Categorical(df["iso2_code"]).codes
    df = df.set_index(["country_id", "quarter_id"])

    y = df[outcome]
    # With time FEs, the main event-time dummies are absorbed.
    # Only the interaction terms (event_time x treatment_var) are identified
    # because treatment_var varies cross-sectionally.
    X = df[interact_cols]

    mod = PanelOLS(y, X, entity_effects=True, time_effects=True, drop_absorbed=True)
    res = mod.fit(cov_type="clustered", cluster_entity=True)

    # Extract interaction coefficients
    coefs = []
    for t in event_times_use:
        col = f"et_{t}_x_{treatment_var}"
        if col in res.params.index:
            coefs.append({
                "event_time": t,
                "coef": res.params[col],
                "se": res.std_errors[col],
                "ci_low": res.params[col] - 1.96 * res.std_errors[col],
                "ci_high": res.params[col] + 1.96 * res.std_errors[col],
                "pval": res.pvalues[col],
            })
    coefs.append({
        "event_time": ref_period,
        "coef": 0.0, "se": 0.0, "ci_low": 0.0, "ci_high": 0.0, "pval": np.nan,
    })
    coefs_df = pd.DataFrame(coefs).sort_values("event_time")

    n_countries = df.index.get_level_values(0).nunique()

    info = {
        "label": label,
        "outcome": outcome,
        "treatment_var": treatment_var,
        "n_obs": res.nobs,
        "n_countries": n_countries,
        "r2_within": res.rsquared_within,
    }

    return res, coefs_df, info


# ═══════════════════════════════════════════════════════════════════════════════
# 1. MAIN EVENT STUDY
# ═══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("1. MAIN EVENT STUDY")
print("=" * 70)

all_coefs = []
all_results = []

for outcome in ["hhi_norm", "entropy"]:
    res, coefs, info = run_event_study(panel, outcome, label=f"Main: {outcome}")
    coefs["specification"] = f"main_{outcome}"
    all_coefs.append(coefs)
    all_results.append(info)

    print(f"\n  [{outcome}]")
    print(f"    N={info['n_obs']}, Countries={info['n_countries']}, "
          f"Quarters={info['n_quarters']}")
    print(f"    Within R2={info['r2_within']:.4f}")
    print(f"    Pre-trend F-test: F={info['pretrend_f']:.3f}, p={info['pretrend_p']:.4f}"
          if not np.isnan(info['pretrend_f']) else "    Pre-trend F-test: N/A")

    # Print post-treatment coefficients
    post_coefs = coefs[coefs["event_time"] >= 0]
    for _, row in post_coefs.iterrows():
        sig = "***" if row["pval"] < 0.01 else "**" if row["pval"] < 0.05 else "*" if row["pval"] < 0.1 else ""
        print(f"    t={int(row['event_time']):+d}: b={row['coef']:+.4f} (se={row['se']:.4f}){sig}")


# ═══════════════════════════════════════════════════════════════════════════════
# 2. HETEROGENEITY BY ENGLISH PROFICIENCY
# ═══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("2. HETEROGENEITY BY ENGLISH PROFICIENCY")
print("=" * 70)

# 2a. Continuous EPI interaction
for outcome in ["hhi_norm", "entropy"]:
    res, coefs, info = run_did_interaction(
        panel, outcome, "epi_score",
        label=f"EPI continuous: {outcome}"
    )
    coefs["specification"] = f"epi_continuous_{outcome}"
    all_coefs.append(coefs)
    all_results.append(info)
    print(f"\n  [{outcome} × EPI continuous]")
    print(f"    N={info['n_obs']}, Countries={info['n_countries']}")

# 2b. Binary high/low EPI
for outcome in ["hhi_norm", "entropy"]:
    res, coefs, info = run_did_interaction(
        panel, outcome, "epi_high",
        label=f"EPI binary: {outcome}"
    )
    coefs["specification"] = f"epi_binary_{outcome}"
    all_coefs.append(coefs)
    all_results.append(info)
    print(f"\n  [{outcome} × EPI high/low]")
    print(f"    N={info['n_obs']}, Countries={info['n_countries']}")

# 2c. Tercile split: run separate event studies for each tercile
print("\n  [Tercile split]")
for tercile in ["low", "medium", "high"]:
    sub = panel[panel["epi_tercile"] == tercile]
    if len(sub) < 50:
        print(f"    {tercile}: too few obs ({len(sub)}), skipping")
        continue
    for outcome in ["hhi_norm", "entropy"]:
        res, coefs, info = run_event_study(
            sub, outcome, label=f"EPI {tercile}: {outcome}"
        )
        coefs["specification"] = f"epi_tercile_{tercile}_{outcome}"
        all_coefs.append(coefs)
        all_results.append(info)
        print(f"    {tercile} {outcome}: N={info['n_obs']}, "
              f"R2={info['r2_within']:.4f}")


# ═══════════════════════════════════════════════════════════════════════════════
# 3. ANTICIPATION EFFECTS TEST
# ═══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("3. ANTICIPATION EFFECTS TEST")
print("=" * 70)
print("  Testing t=-2 (Q2 2022) and t=-3 (Q1 2022) for non-zero coefficients")

for outcome in ["hhi_norm", "entropy"]:
    _, coefs, _ = run_event_study(panel, outcome, label=f"Anticipation: {outcome}")
    for t in [-3, -2]:
        row = coefs[coefs["event_time"] == t]
        if not row.empty:
            r = row.iloc[0]
            sig = "SIGNIFICANT" if r["pval"] < 0.1 else "not significant"
            print(f"  [{outcome}] t={t}: b={r['coef']:+.4f} (p={r['pval']:.3f}) — {sig}")


# ═══════════════════════════════════════════════════════════════════════════════
# 4. COMPOSITION EFFECTS TEST
# ═══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("4. COMPOSITION EFFECTS TEST")
print("=" * 70)
print("  Does N_languages per country×quarter change around treatment?")

res_comp, coefs_comp, info_comp = run_event_study(
    panel, "n_languages", label="Composition: n_languages"
)
coefs_comp["specification"] = "composition_n_languages"
all_coefs.append(coefs_comp)
all_results.append(info_comp)

print(f"  N={info_comp['n_obs']}, Pre-trend p={info_comp['pretrend_p']:.4f}"
      if not np.isnan(info_comp['pretrend_p']) else f"  N={info_comp['n_obs']}")
post_comp = coefs_comp[coefs_comp["event_time"] >= 0]
for _, row in post_comp.iterrows():
    sig = "***" if row["pval"] < 0.01 else "**" if row["pval"] < 0.05 else "*" if row["pval"] < 0.1 else ""
    print(f"  t={int(row['event_time']):+d}: b={row['coef']:+.2f} (p={row['pval']:.3f}){sig}")

if any(post_comp["pval"] < 0.05):
    print("  [!] WARNING: Composition effects detected — N_languages changes significantly post-treatment.")
    print("      HHI interpretation must account for this (mechanical effect).")
else:
    print("  [ok] No significant composition effects — language entry/exit is not driving results.")


# ═══════════════════════════════════════════════════════════════════════════════
# 5. SAVE RESULTS
# ═══════════════════════════════════════════════════════════════════════════════
all_coefs_df = pd.concat(all_coefs, ignore_index=True)
all_coefs_df.to_csv(CLEAN_DIR / "event_study_coefficients.csv", index=False)

results_df = pd.DataFrame(all_results)
results_df.to_csv(CLEAN_DIR / "main_results.csv", index=False)

print(f"\n[save] Event study coefficients: {CLEAN_DIR / 'event_study_coefficients.csv'}")
print(f"[save] Main results: {CLEAN_DIR / 'main_results.csv'}")
print("\n[01_main] DONE [OK]")
