"""
01_main.py - Main regression analysis for factorial RCT
========================================================
Factorial OLS, ANCOVA, superadditivity tests, permutation inference,
effect sizes, MDE, BH correction.
"""

import sys
import warnings
import numpy as np
import pandas as pd
import statsmodels.api as sm
from pathlib import Path
from itertools import product

warnings.filterwarnings("ignore")

# ── paths ───────────────────────────────────────────────────────────────────
PROJECT = Path(__file__).resolve().parents[2]
CLEAN = PROJECT / "data" / "clean"

print("=" * 70)
print("01_main.py  --  Main Regression Analysis")
print("=" * 70)

# ── Load data ───────────────────────────────────────────────────────────────
df = pd.read_csv(CLEAN / "clean_data.csv", low_memory=False)
print(f"Loaded clean data: {df.shape[0]} rows")

# Create interaction term
df["voucher_x_training"] = df["voucher"] * df["training"]

# ── Sanity check ────────────────────────────────────────────────────────────
print("\n[SANITY CHECK] Theory predicts:")
print("  - Voucher increases employment => positive coefficient for mid_x")
print("  - Effect is large at midline (~+39pp) and fades by endline")
print("  - Training has small effects throughout")
print("  - Interaction is near-zero (additive, not superadditive)")

expected_signs = {
    "mid_x": {"voucher": "+", "training": "+"},
    "mid_salary": {"voucher": "+", "training": "+"},
    "end_x": {"voucher": "+", "training": "+"},
    "end_lfp": {"voucher": "+", "training": "+"},
    "end_salary": {"voucher": "+", "training": "+"},
}

# ── Outcomes ────────────────────────────────────────────────────────────────
outcomes = ["mid_x", "mid_salary", "end_x", "end_lfp", "end_salary"]
baseline_controls = ["b_b1age", "b_communitycollege", "b_examresult"]
# Keep controls that exist
baseline_controls = [c for c in baseline_controls if c in df.columns]

results = []
ancova_results = []

# ── 2-3. Factorial OLS + ANCOVA ─────────────────────────────────────────────
print("\n[1-3] Factorial OLS and ANCOVA regressions")
print("-" * 70)

for outcome in outcomes:
    if outcome not in df.columns:
        print(f"  SKIPPING {outcome}: column not found")
        continue

    sub = df[["voucher", "training", "voucher_x_training", outcome] + baseline_controls].dropna()
    if len(sub) < 30:
        print(f"  SKIPPING {outcome}: only {len(sub)} obs")
        continue

    y = sub[outcome]
    # Simple factorial model
    X_simple = sm.add_constant(sub[["voucher", "training", "voucher_x_training"]])
    mod_simple = sm.OLS(y, X_simple).fit(cov_type="HC2")

    # ANCOVA model
    X_ancova = sm.add_constant(sub[["voucher", "training", "voucher_x_training"] + baseline_controls])
    mod_ancova = sm.OLS(y, X_ancova).fit(cov_type="HC2")

    print(f"\n  === {outcome} (n={len(sub)}) ===")
    for var in ["voucher", "training", "voucher_x_training"]:
        b = mod_simple.params[var]
        se = mod_simple.bse[var]
        p = mod_simple.pvalues[var]
        stars = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""
        print(f"    OLS    {var:25s}: b={b:+.4f}  se={se:.4f}  p={p:.4f} {stars}")

    for var in ["voucher", "training", "voucher_x_training"]:
        b = mod_ancova.params[var]
        se = mod_ancova.bse[var]
        p = mod_ancova.pvalues[var]
        stars = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""
        print(f"    ANCOVA {var:25s}: b={b:+.4f}  se={se:.4f}  p={p:.4f} {stars}")

    # Store simple results
    for var in ["voucher", "training", "voucher_x_training"]:
        results.append({
            "outcome": outcome,
            "model": "OLS",
            "variable": var,
            "coef": mod_simple.params[var],
            "se": mod_simple.bse[var],
            "pvalue": mod_simple.pvalues[var],
            "ci_low": mod_simple.conf_int().loc[var, 0],
            "ci_high": mod_simple.conf_int().loc[var, 1],
            "n": len(sub),
            "r2": mod_simple.rsquared,
        })
    for var in ["voucher", "training", "voucher_x_training"]:
        results.append({
            "outcome": outcome,
            "model": "ANCOVA",
            "variable": var,
            "coef": mod_ancova.params[var],
            "se": mod_ancova.bse[var],
            "pvalue": mod_ancova.pvalues[var],
            "ci_low": mod_ancova.conf_int().loc[var, 0],
            "ci_high": mod_ancova.conf_int().loc[var, 1],
            "n": len(sub),
            "r2": mod_ancova.rsquared,
        })

results_df = pd.DataFrame(results)

# ── 4. Superadditivity test ─────────────────────────────────────────────────
print("\n\n[4] Superadditivity test (H0: interaction = 0)")
print("-" * 70)
for outcome in outcomes:
    row = results_df[(results_df["outcome"] == outcome) &
                     (results_df["model"] == "OLS") &
                     (results_df["variable"] == "voucher_x_training")]
    if len(row) > 0:
        r = row.iloc[0]
        reject = "REJECT" if r["pvalue"] < 0.05 else "FAIL TO REJECT"
        print(f"  {outcome:15s}: interaction = {r['coef']:+.4f}, p = {r['pvalue']:.4f} => {reject}")

# ── 5. Cohen's d ────────────────────────────────────────────────────────────
print("\n[5] Cohen's d for main effects")
print("-" * 70)
cohen_rows = []
for outcome in outcomes:
    if outcome not in df.columns:
        continue
    for treat_var in ["voucher", "training"]:
        t1 = df.loc[df[treat_var] == 1, outcome].dropna()
        t0 = df.loc[df[treat_var] == 0, outcome].dropna()
        if len(t1) > 5 and len(t0) > 5:
            pooled_sd = np.sqrt(((len(t1)-1)*t1.std()**2 + (len(t0)-1)*t0.std()**2) / (len(t1)+len(t0)-2))
            d = (t1.mean() - t0.mean()) / pooled_sd if pooled_sd > 0 else np.nan
            cohen_rows.append({"outcome": outcome, "treatment": treat_var, "cohens_d": round(d, 4)})
            print(f"  {outcome:15s} x {treat_var:10s}: d = {d:+.4f}")

# ── 6. Permutation test for interaction ─────────────────────────────────────
print("\n[6] Permutation test for interaction (1000 reshuffles)")
print("-" * 70)
np.random.seed(42)
n_perm = 1000
perm_results = {}

for outcome in outcomes:
    if outcome not in df.columns:
        continue
    sub = df[["voucher", "training", "voucher_x_training", outcome]].dropna()
    if len(sub) < 30:
        continue

    y = sub[outcome].values
    X_base = sm.add_constant(sub[["voucher", "training", "voucher_x_training"]].values)

    # Observed interaction coefficient
    mod_obs = sm.OLS(y, X_base).fit()
    obs_coef = mod_obs.params[3]  # interaction is last

    perm_coefs = []
    for _ in range(n_perm):
        y_perm = np.random.permutation(y)
        mod_p = sm.OLS(y_perm, X_base).fit()
        perm_coefs.append(mod_p.params[3])

    perm_coefs = np.array(perm_coefs)
    perm_p = np.mean(np.abs(perm_coefs) >= np.abs(obs_coef))
    perm_results[outcome] = {"obs_coef": obs_coef, "perm_p": perm_p, "perm_coefs": perm_coefs}
    print(f"  {outcome:15s}: obs interaction = {obs_coef:+.4f}, permutation p = {perm_p:.4f}")

# Save permutation distribution for first outcome
if perm_results:
    first_outcome = list(perm_results.keys())[0]
    perm_dist_df = pd.DataFrame({
        "perm_coef": perm_results[first_outcome]["perm_coefs"],
        "outcome": first_outcome,
    })

# ── 7. MDE calculation ─────────────────────────────────────────────────────
print("\n[7] Minimum Detectable Effects (alpha=0.05, power=0.80)")
print("-" * 70)
from scipy.stats import norm
z_alpha = norm.ppf(0.975)
z_beta = norm.ppf(0.80)

mde_rows = []
for outcome in outcomes:
    if outcome not in df.columns:
        continue
    sub = df[[outcome, "voucher"]].dropna()
    n_treat = (sub["voucher"] == 1).sum()
    n_control = (sub["voucher"] == 0).sum()
    sd = sub[outcome].std()
    mde = (z_alpha + z_beta) * sd * np.sqrt(1/n_treat + 1/n_control)
    mde_rows.append({"outcome": outcome, "sd": round(sd, 4), "mde": round(mde, 4),
                      "n_treat": n_treat, "n_control": n_control})
    print(f"  {outcome:15s}: SD={sd:.4f}, MDE={mde:.4f} (n_t={n_treat}, n_c={n_control})")

# ── 8. BH correction ───────────────────────────────────────────────────────
print("\n[8] Benjamini-Hochberg correction across outcomes")
print("-" * 70)
# Get OLS voucher p-values
ols_voucher = results_df[(results_df["model"] == "OLS") & (results_df["variable"] == "voucher")].copy()
ols_voucher = ols_voucher.sort_values("pvalue").reset_index(drop=True)
m = len(ols_voucher)
ols_voucher["rank"] = range(1, m + 1)
ols_voucher["bh_threshold"] = 0.05 * ols_voucher["rank"] / m
ols_voucher["bh_reject"] = ols_voucher["pvalue"] <= ols_voucher["bh_threshold"]

for _, row in ols_voucher.iterrows():
    status = "SIGNIFICANT" if row["bh_reject"] else "not significant"
    print(f"  {row['outcome']:15s}: p={row['pvalue']:.4f}, BH threshold={row['bh_threshold']:.4f} => {status}")

# Add BH-adjusted p-values to main results
results_df["bh_pvalue"] = np.nan
for i, row in results_df.iterrows():
    match = ols_voucher[ols_voucher["outcome"] == row["outcome"]]
    if len(match) > 0 and row["model"] == "OLS" and row["variable"] == "voucher":
        # Simple BH adjustment
        results_df.loc[i, "bh_pvalue"] = min(row["pvalue"] * m / match.iloc[0]["rank"], 1.0)

# ── 9. Sanity check: compare signs ─────────────────────────────────────────
print("\n[9] SANITY CHECK: Sign verification")
print("-" * 70)
all_ok = True
for outcome, signs in expected_signs.items():
    for var, expected in signs.items():
        row = results_df[(results_df["outcome"] == outcome) &
                         (results_df["model"] == "OLS") &
                         (results_df["variable"] == var)]
        if len(row) > 0:
            actual = "+" if row.iloc[0]["coef"] > 0 else "-"
            match = "OK" if actual == expected else "MISMATCH"
            if match == "MISMATCH":
                all_ok = False
            print(f"  {outcome:15s} x {var:10s}: expected={expected}, actual={actual} => {match}")

if all_ok:
    print("\n  ALL SIGNS MATCH THEORETICAL PREDICTIONS")
else:
    print("\n  WARNING: Some signs do not match predictions!")

# ── 10. Save ────────────────────────────────────────────────────────────────
print("\n[10] Saving outputs...")
results_df.to_csv(CLEAN / "main_results.csv", index=False)
print(f"  Saved: main_results.csv ({len(results_df)} rows)")

if perm_results:
    perm_dist_df.to_csv(CLEAN / "permutation_distribution.csv", index=False)
    print(f"  Saved: permutation_distribution.csv")

print("\n" + "=" * 70)
print("01_main.py COMPLETE")
print("=" * 70)
