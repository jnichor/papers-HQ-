"""
02_robustness.py - Robustness checks for factorial RCT
=======================================================
Falsification tests, Lee bounds, logit, sensitivity to covariates,
time dynamics comparison.
"""

import sys
import warnings
import numpy as np
import pandas as pd
import statsmodels.api as sm
from pathlib import Path
from scipy.stats import norm

warnings.filterwarnings("ignore")

# ── paths ───────────────────────────────────────────────────────────────────
PROJECT = Path(__file__).resolve().parents[2]
CLEAN = PROJECT / "data" / "clean"

print("=" * 70)
print("02_robustness.py  --  Robustness Checks")
print("=" * 70)

df = pd.read_csv(CLEAN / "clean_data.csv", low_memory=False)
df["voucher_x_training"] = df["voucher"] * df["training"]
print(f"Loaded clean data: {df.shape[0]} rows")

robustness_rows = []

# ── 1. Falsification: placebo outcome ───────────────────────────────────────
print("\n[1] FALSIFICATION: b_b1age as placebo outcome")
print("-" * 70)
print("  If treatment is random, voucher should NOT predict baseline age.")

sub = df[["voucher", "training", "voucher_x_training", "b_b1age"]].dropna()
y = sub["b_b1age"]
X = sm.add_constant(sub[["voucher", "training", "voucher_x_training"]])
mod = sm.OLS(y, X).fit(cov_type="HC2")

for var in ["voucher", "training", "voucher_x_training"]:
    b = mod.params[var]
    p = mod.pvalues[var]
    status = "FAIL (significant!)" if p < 0.05 else "PASS (not significant)"
    print(f"  {var:25s}: b={b:+.4f}, p={p:.4f} => {status}")
    robustness_rows.append({
        "test": "placebo_age", "variable": var,
        "coef": b, "se": mod.bse[var], "pvalue": p,
        "note": status,
    })

# ── 2. Falsification: permuted treatment arms ──────────────────────────────
print("\n[2] FALSIFICATION: Permuted treatment (1000 reshuffles on mid_x)")
print("-" * 70)
np.random.seed(123)
if "mid_x" in df.columns:
    sub = df[["voucher", "training", "mid_x"]].dropna()
    y = sub["mid_x"].values
    true_X = sm.add_constant(sub[["voucher", "training"]].values)
    true_mod = sm.OLS(y, true_X).fit()
    true_b_voucher = true_mod.params[1]

    perm_bs = []
    for _ in range(1000):
        perm_voucher = np.random.permutation(sub["voucher"].values)
        perm_training = np.random.permutation(sub["training"].values)
        perm_X = sm.add_constant(np.column_stack([perm_voucher, perm_training]))
        perm_mod = sm.OLS(y, perm_X).fit()
        perm_bs.append(perm_mod.params[1])

    perm_bs = np.array(perm_bs)
    perm_p = np.mean(np.abs(perm_bs) >= np.abs(true_b_voucher))
    print(f"  True voucher effect on mid_x: {true_b_voucher:+.4f}")
    print(f"  Permutation p-value: {perm_p:.4f}")
    print(f"  Mean of permuted coefficients: {np.mean(perm_bs):+.4f}")
    status = "PASS (true effect is extreme)" if perm_p < 0.05 else "FAIL"
    robustness_rows.append({
        "test": "permutation_falsification", "variable": "voucher->mid_x",
        "coef": true_b_voucher, "se": np.nan, "pvalue": perm_p,
        "note": status,
    })

# ── 3. Lee bounds for salary conditional on employment ──────────────────────
print("\n[3] Lee bounds for salary (conditional on employment)")
print("-" * 70)

for prefix, emp_var, sal_var in [("midline", "mid_x", "mid_salary"),
                                   ("endline", "end_x", "end_salary")]:
    if emp_var not in df.columns or sal_var not in df.columns:
        print(f"  SKIP {prefix}: missing columns")
        continue

    sub = df[["voucher", emp_var, sal_var]].dropna(subset=["voucher", emp_var])

    # Employment rates by treatment
    emp_treat = sub.loc[sub["voucher"] == 1, emp_var].mean()
    emp_ctrl = sub.loc[sub["voucher"] == 0, emp_var].mean()
    excess = emp_treat - emp_ctrl

    print(f"  {prefix}: emp_treat={emp_treat:.3f}, emp_ctrl={emp_ctrl:.3f}, excess={excess:+.3f}")

    # Among employed in each group
    sal_treat = sub.loc[(sub["voucher"] == 1) & (sub[emp_var] == 1), sal_var].dropna()
    sal_ctrl = sub.loc[(sub["voucher"] == 0) & (sub[emp_var] == 1), sal_var].dropna()

    if len(sal_treat) < 5 or len(sal_ctrl) < 5:
        print(f"    Too few employed observations for Lee bounds")
        continue

    # Proportion to trim from treatment group
    if excess > 0 and emp_treat > 0:
        trim_pct = excess / emp_treat
        trim_n = int(np.floor(trim_pct * len(sal_treat)))
        if trim_n > 0 and trim_n < len(sal_treat):
            sal_sorted = np.sort(sal_treat.values)
            # Lower bound: trim from top
            lower_mean = sal_sorted[:len(sal_treat) - trim_n].mean()
            # Upper bound: trim from bottom
            upper_mean = sal_sorted[trim_n:].mean()

            lb = lower_mean - sal_ctrl.mean()
            ub = upper_mean - sal_ctrl.mean()
            print(f"    Lee bounds: [{lb:+.2f}, {ub:+.2f}]")
            print(f"    Trimmed {trim_n} obs ({100*trim_pct:.1f}%) from treatment group")
            robustness_rows.append({
                "test": f"lee_bounds_{prefix}", "variable": sal_var,
                "coef": (lb + ub) / 2, "se": np.nan, "pvalue": np.nan,
                "note": f"Lee bounds: [{lb:+.2f}, {ub:+.2f}]",
            })
        else:
            naive = sal_treat.mean() - sal_ctrl.mean()
            print(f"    Trim too small; naive diff = {naive:+.2f}")
    else:
        naive = sal_treat.mean() - sal_ctrl.mean() if len(sal_treat) > 0 else np.nan
        print(f"    No excess employment; naive diff = {naive:+.2f}")

# ── 4. Logit for binary outcomes ────────────────────────────────────────────
print("\n[4] Logit for binary outcomes")
print("-" * 70)
binary_outcomes = ["mid_x", "end_x", "end_lfp", "mid_lfp"]

for outcome in binary_outcomes:
    if outcome not in df.columns:
        continue
    sub = df[["voucher", "training", "voucher_x_training", outcome]].dropna()
    y = sub[outcome]
    if y.nunique() < 2:
        print(f"  SKIP {outcome}: no variation")
        continue

    X = sm.add_constant(sub[["voucher", "training", "voucher_x_training"]])
    try:
        mod = sm.Logit(y, X).fit(disp=0, maxiter=100)
        print(f"\n  {outcome} (Logit, n={len(sub)}):")
        for var in ["voucher", "training", "voucher_x_training"]:
            b = mod.params[var]
            p = mod.pvalues[var]
            odds = np.exp(b)
            stars = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""
            print(f"    {var:25s}: log-OR={b:+.4f}, OR={odds:.3f}, p={p:.4f} {stars}")
            robustness_rows.append({
                "test": "logit", "variable": f"{outcome}_{var}",
                "coef": b, "se": mod.bse[var], "pvalue": p,
                "note": f"OR={odds:.3f}",
            })
    except Exception as ex:
        print(f"  Logit failed for {outcome}: {ex}")

# ── 5. Sensitivity to covariates ────────────────────────────────────────────
print("\n[5] Sensitivity to covariates (voucher effect on mid_x)")
print("-" * 70)
if "mid_x" in df.columns:
    covariate_sets = {
        "no_controls": [],
        "age_only": ["b_b1age"],
        "age_edu": ["b_b1age", "b_communitycollege"],
        "full": ["b_b1age", "b_communitycollege", "b_examresult"],
    }

    for label, covs in covariate_sets.items():
        all_vars = ["voucher", "training", "voucher_x_training", "mid_x"] + covs
        all_vars = [v for v in all_vars if v in df.columns]
        sub = df[all_vars].dropna()
        y = sub["mid_x"]
        x_vars = ["voucher", "training", "voucher_x_training"] + [c for c in covs if c in df.columns]
        X = sm.add_constant(sub[x_vars])
        mod = sm.OLS(y, X).fit(cov_type="HC2")
        b = mod.params["voucher"]
        se = mod.bse["voucher"]
        p = mod.pvalues["voucher"]
        print(f"  {label:20s}: voucher coef = {b:+.4f} (se={se:.4f}, p={p:.4f})")
        robustness_rows.append({
            "test": f"sensitivity_{label}", "variable": "voucher->mid_x",
            "coef": b, "se": se, "pvalue": p,
            "note": f"controls: {label}",
        })

# ── 6. Time dynamics: midline vs endline ────────────────────────────────────
print("\n[6] Time dynamics: voucher effect at midline vs endline")
print("-" * 70)
time_pairs = [
    ("mid_x", "end_x", "employment"),
    ("mid_salary", "end_salary", "salary"),
    ("mid_lfp", "end_lfp", "labor force participation"),
]

for mid_var, end_var, label in time_pairs:
    if mid_var not in df.columns or end_var not in df.columns:
        continue

    effects = {}
    for var, timepoint in [(mid_var, "midline"), (end_var, "endline")]:
        sub = df[["voucher", "training", "voucher_x_training", var]].dropna()
        y = sub[var]
        X = sm.add_constant(sub[["voucher", "training", "voucher_x_training"]])
        mod = sm.OLS(y, X).fit(cov_type="HC2")
        effects[timepoint] = {
            "coef": mod.params["voucher"],
            "se": mod.bse["voucher"],
            "p": mod.pvalues["voucher"],
        }

    mid_e = effects["midline"]
    end_e = effects["endline"]
    fade = mid_e["coef"] - end_e["coef"]
    # Z-test for difference
    se_diff = np.sqrt(mid_e["se"]**2 + end_e["se"]**2)
    z = fade / se_diff if se_diff > 0 else 0
    p_diff = 2 * (1 - norm.cdf(abs(z)))

    print(f"  {label}:")
    print(f"    Midline:  {mid_e['coef']:+.4f} (se={mid_e['se']:.4f}, p={mid_e['p']:.4f})")
    print(f"    Endline:  {end_e['coef']:+.4f} (se={end_e['se']:.4f}, p={end_e['p']:.4f})")
    print(f"    Fade-out: {fade:+.4f} (z={z:.2f}, p={p_diff:.4f})")

    robustness_rows.append({
        "test": f"time_dynamics_{label.replace(' ', '_')}",
        "variable": "voucher_fade",
        "coef": fade, "se": se_diff, "pvalue": p_diff,
        "note": f"mid={mid_e['coef']:+.4f}, end={end_e['coef']:+.4f}",
    })

# ── Save ────────────────────────────────────────────────────────────────────
print("\n[7] Saving outputs...")
rob_df = pd.DataFrame(robustness_rows)
rob_df.to_csv(CLEAN / "robustness_results.csv", index=False)
print(f"  Saved: robustness_results.csv ({len(rob_df)} rows)")

print("\n" + "=" * 70)
print("02_robustness.py COMPLETE")
print("=" * 70)
