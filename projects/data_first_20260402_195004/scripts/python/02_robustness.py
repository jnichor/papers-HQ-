"""
02_robustness.py
----------------
Ordered probit, logit, alternative moderators, Lee bounds,
covariate sensitivity, BH correction.
"""

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.miscmodels.ordinal_model import OrderedModel

# ── paths ──────────────────────────────────────────────────────────────
PROJECT = Path(__file__).resolve().parents[2]
CLEAN   = PROJECT / "data" / "clean"

# ── load ───────────────────────────────────────────────────────────────
df = pd.read_csv(CLEAN / "clean_data.csv")
TREAT = "apartheid_vs_persecution_treat"
OUTCOME = "ICC_referral"
print(f"Loaded {len(df)} rows")

results = []

# ── 1. Ordered probit ─────────────────────────────────────────────────
sub_op = df[[OUTCOME, TREAT]].dropna()
try:
    op_model = OrderedModel(
        sub_op[OUTCOME].astype(int),
        sub_op[[TREAT]],
        distr="probit"
    ).fit(method="bfgs", disp=False)
    coef = op_model.params[TREAT]
    se = op_model.bse[TREAT]
    p = op_model.pvalues[TREAT]
    results.append({
        "test": "Ordered probit",
        "outcome": OUTCOME,
        "coef": round(coef, 6),
        "se": round(se, 6),
        "p_value": round(p, 6),
        "n": int(op_model.nobs),
    })
    print(f"Ordered probit: coef={coef:.4f}, p={p:.4f}")
except Exception as e:
    print(f"Ordered probit failed: {e}")
    results.append({"test": "Ordered probit", "outcome": OUTCOME,
                     "coef": np.nan, "note": str(e)})

# ── 2. Logit on binary outcome ────────────────────────────────────────
OUTCOME_BIN = "ICC_referral_binary"
sub_log = df[[OUTCOME_BIN, TREAT]].dropna()
X_log = sm.add_constant(sub_log[[TREAT]])
logit_model = sm.Logit(sub_log[OUTCOME_BIN], X_log).fit(disp=False)
results.append({
    "test": "Logit (binary outcome)",
    "outcome": OUTCOME_BIN,
    "coef": round(logit_model.params[TREAT], 6),
    "se": round(logit_model.bse[TREAT], 6),
    "p_value": round(logit_model.pvalues[TREAT], 6),
    "n": int(logit_model.nobs),
    "note": "log-odds coefficient",
})
# Marginal effect
mfx = logit_model.get_margeff()
results.append({
    "test": "Logit marginal effect",
    "outcome": OUTCOME_BIN,
    "coef": round(mfx.margeff[0], 6),
    "se": round(mfx.margeff_se[0], 6),
    "p_value": round(mfx.pvalues[0], 6),
    "n": int(logit_model.nobs),
})
print(f"Logit: coef={logit_model.params[TREAT]:.4f}, p={logit_model.pvalues[TREAT]:.4f}")

# ── 3. Alternative moderators ─────────────────────────────────────────
# Hawkish aggregate quintiles
if "hawkish_aggregate" in df.columns:
    sub_h = df[[OUTCOME, TREAT, "hawkish_aggregate"]].dropna()
    sub_h["hawk_quintile"] = pd.qcut(sub_h["hawkish_aggregate"], q=5,
                                      labels=False, duplicates="drop") + 1
    for q in sorted(sub_h["hawk_quintile"].unique()):
        sq = sub_h[sub_h["hawk_quintile"] == q]
        if len(sq) > 10:
            X_ = sm.add_constant(sq[[TREAT]])
            m = sm.OLS(sq[OUTCOME], X_).fit(cov_type="HC2")
            results.append({
                "test": f"CATE hawkish Q{int(q)}",
                "outcome": OUTCOME,
                "coef": round(m.params[TREAT], 6),
                "se": round(m.bse[TREAT], 6),
                "p_value": round(m.pvalues[TREAT], 6),
                "n": int(m.nobs),
            })
    print("Hawkish quintile CATEs computed.")

# Hostile sexism terciles
if "hostile_sexism_agg" in df.columns:
    sub_hs = df[[OUTCOME, TREAT, "hostile_sexism_agg"]].dropna()
    sub_hs["hs_tercile"] = pd.qcut(sub_hs["hostile_sexism_agg"], q=3,
                                     labels=False, duplicates="drop") + 1
    for t in sorted(sub_hs["hs_tercile"].unique()):
        st = sub_hs[sub_hs["hs_tercile"] == t]
        if len(st) > 10:
            X_ = sm.add_constant(st[[TREAT]])
            m = sm.OLS(st[OUTCOME], X_).fit(cov_type="HC2")
            results.append({
                "test": f"CATE hostile_sexism T{int(t)}",
                "outcome": OUTCOME,
                "coef": round(m.params[TREAT], 6),
                "se": round(m.bse[TREAT], 6),
                "p_value": round(m.pvalues[TREAT], 6),
                "n": int(m.nobs),
            })
    print("Hostile sexism tercile CATEs computed.")

# ── 4. Lee bounds ─────────────────────────────────────────────────────
# Lee (2009) bounds for attrition: trim the "excess" group
sub_lee = df[[OUTCOME, TREAT]].copy()
n_treat_total = (df[TREAT] == 1).sum()
n_ctrl_total = (df[TREAT] == 0).sum()
n_treat_obs = sub_lee.loc[sub_lee[TREAT] == 1, OUTCOME].notna().sum()
n_ctrl_obs = sub_lee.loc[sub_lee[TREAT] == 0, OUTCOME].notna().sum()

resp_treat = n_treat_obs / n_treat_total
resp_ctrl = n_ctrl_obs / n_ctrl_total

if resp_treat != resp_ctrl:
    # Trim from the group with higher response rate
    if resp_treat > resp_ctrl:
        trim_frac = 1 - resp_ctrl / resp_treat
        trim_group = 1
    else:
        trim_frac = 1 - resp_treat / resp_ctrl
        trim_group = 0

    obs = sub_lee.dropna()
    trim_data = obs[obs[TREAT] == trim_group][OUTCOME].sort_values()
    n_trim = int(np.ceil(len(trim_data) * trim_frac))

    # Lower bound: trim top
    lower_trim = trim_data.iloc[:len(trim_data) - n_trim]
    other = obs[obs[TREAT] != trim_group][OUTCOME]
    if trim_group == 1:
        lb = lower_trim.mean() - other.mean()
    else:
        lb = obs[obs[TREAT] == 1][OUTCOME].mean() - lower_trim.mean()

    # Upper bound: trim bottom
    upper_trim = trim_data.iloc[n_trim:]
    if trim_group == 1:
        ub = upper_trim.mean() - other.mean()
    else:
        ub = obs[obs[TREAT] == 1][OUTCOME].mean() - upper_trim.mean()

    lee_lower = min(lb, ub)
    lee_upper = max(lb, ub)
else:
    lee_lower = lee_upper = np.nan

results.append({
    "test": "Lee bounds",
    "outcome": OUTCOME,
    "coef": np.nan,
    "note": f"[{lee_lower:.4f}, {lee_upper:.4f}]" if not np.isnan(lee_lower) else "No differential attrition",
    "n": n_treat_obs + n_ctrl_obs,
})
print(f"Lee bounds: [{lee_lower:.4f}, {lee_upper:.4f}]" if not np.isnan(lee_lower) else "Lee bounds: No differential attrition")

# ── 5. Sensitivity to covariate set ──────────────────────────────────
# No controls (same as spec 1)
sub_s = df[[OUTCOME, TREAT]].dropna()
# HC2 robust SEs (heteroskedasticity-consistent, no clustering needed for individual-level RCT)
m0 = sm.OLS(sub_s[OUTCOME], sm.add_constant(sub_s[[TREAT]])).fit(cov_type="HC2")
results.append({
    "test": "Sensitivity: no controls",
    "outcome": OUTCOME,
    "coef": round(m0.params[TREAT], 6),
    "se": round(m0.bse[TREAT], 6),
    "p_value": round(m0.pvalues[TREAT], 6),
    "n": int(m0.nobs),
})

# Baseline controls
base_covs = ["respondent_age", "female", "education", "stronger_republican_8pt"]
base_covs = [c for c in base_covs if c in df.columns]
sub_b = df[[OUTCOME, TREAT] + base_covs].dropna()
m1 = sm.OLS(sub_b[OUTCOME], sm.add_constant(sub_b[[TREAT] + base_covs])).fit(cov_type="HC2")
results.append({
    "test": "Sensitivity: baseline controls",
    "outcome": OUTCOME,
    "coef": round(m1.params[TREAT], 6),
    "se": round(m1.bse[TREAT], 6),
    "p_value": round(m1.pvalues[TREAT], 6),
    "n": int(m1.nobs),
})

# Full controls
all_covs = ["respondent_age", "female", "white", "black", "education",
            "stronger_republican_8pt", "hawkish_aggregate",
            "hostile_sexism_agg", "benevolent_sexism_agg",
            "cosmopolitan", "knowledge_ir_agg", "pro_israel_score",
            "hhi", "over_65"]
all_covs = [c for c in all_covs if c in df.columns]
sub_f = df[[OUTCOME, TREAT] + all_covs].dropna()
m2 = sm.OLS(sub_f[OUTCOME], sm.add_constant(sub_f[[TREAT] + all_covs])).fit(cov_type="HC2")
results.append({
    "test": "Sensitivity: full controls",
    "outcome": OUTCOME,
    "coef": round(m2.params[TREAT], 6),
    "se": round(m2.bse[TREAT], 6),
    "p_value": round(m2.pvalues[TREAT], 6),
    "n": int(m2.nobs),
})
print("Covariate sensitivity computed.")

# ── 6. Benjamini-Hochberg on CATE quintile p-values ──────────────────
cate_df = pd.read_csv(CLEAN / "cate_results.csv")
pvals = cate_df["p_value"].values
m_tests = len(pvals)
ranks = stats.rankdata(pvals)
bh_adjusted = np.minimum(1.0, pvals * m_tests / ranks)
# Enforce monotonicity
sorted_idx = np.argsort(pvals)
bh_sorted = bh_adjusted[sorted_idx]
for i in range(1, len(bh_sorted)):
    bh_sorted[i] = max(bh_sorted[i], bh_sorted[i-1])
bh_adjusted[sorted_idx] = bh_sorted

cate_df["p_bh_adjusted"] = np.round(bh_adjusted, 6)
cate_df.to_csv(CLEAN / "cate_results.csv", index=False)
print("BH-adjusted p-values added to CATE results.")

# ── save ──────────────────────────────────────────────────────────────
rob_df = pd.DataFrame(results)
rob_df.to_csv(CLEAN / "robustness_results.csv", index=False)
print("02_robustness.py complete.")
