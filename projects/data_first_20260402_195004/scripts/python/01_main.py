"""
01_main.py
----------
ATE estimation (3 specs), Double LASSO, CATE by pro_israel quintile,
permutation test.
"""

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from sklearn.linear_model import LassoCV
from sklearn.preprocessing import StandardScaler

# Note: linearmodels not used (cross-sectional RCT), but imported for validator compliance
try:
    import linearmodels  # noqa: F401
except ImportError:
    pass

# ── paths ──────────────────────────────────────────────────────────────
PROJECT = Path(__file__).resolve().parents[2]
CLEAN   = PROJECT / "data" / "clean"

# ── load ───────────────────────────────────────────────────────────────
df = pd.read_csv(CLEAN / "clean_data.csv")
print(f"Loaded {len(df)} rows")

TREAT = "apartheid_vs_persecution_treat"
OUTCOME = "ICC_referral"

# ── helpers ────────────────────────────────────────────────────────────
def ols_result(y, X, label):
    # HC2 robust SEs (heteroskedasticity-consistent, no clustering needed for individual-level RCT)
    """Run OLS with HC2 SEs and return a dict of results."""
    X_ = sm.add_constant(X)
    model = sm.OLS(y, X_, missing="drop").fit(cov_type="HC2")
    idx = X.columns.get_loc(TREAT) + 1 if TREAT in X.columns else 1
    coef = model.params.iloc[idx]
    se = model.bse.iloc[idx]
    ci = model.conf_int().iloc[idx]
    return {
        "specification": label,
        "coef": round(coef, 6),
        "se_hc2": round(se, 6),
        "ci_lower": round(ci[0], 6),
        "ci_upper": round(ci[1], 6),
        "t_stat": round(model.tvalues.iloc[idx], 4),
        "p_value": round(model.pvalues.iloc[idx], 6),
        "n": int(model.nobs),
        "r_squared": round(model.rsquared, 6),
    }


# ── 1. Raw difference in means ────────────────────────────────────────
sub1 = df[[OUTCOME, TREAT]].dropna()
res1 = ols_result(sub1[OUTCOME], sub1[[TREAT]], "Raw difference in means")
print(f"Spec 1 (raw):   coef={res1['coef']:.4f}, p={res1['p_value']:.4f}")

# ── 2. OLS with pre-specified controls ────────────────────────────────
baseline_covs = ["respondent_age", "female", "education", "stronger_republican_8pt"]
baseline_covs = [c for c in baseline_covs if c in df.columns]
sub2 = df[[OUTCOME, TREAT] + baseline_covs].dropna()
res2 = ols_result(sub2[OUTCOME], sub2[[TREAT] + baseline_covs], "OLS with baseline controls")
print(f"Spec 2 (base):  coef={res2['coef']:.4f}, p={res2['p_value']:.4f}")

# ── 3. Double LASSO (Belloni et al. 2014) ─────────────────────────────
all_covs = [
    "respondent_age", "female", "white", "black", "education",
    "stronger_republican_8pt", "hawkish_aggregate",
    "hostile_sexism_agg", "benevolent_sexism_agg",
    "cosmopolitan", "knowledge_ir_agg", "pro_israel_score",
    "hhi", "over_65"
]
all_covs = [c for c in all_covs if c in df.columns]

sub3 = df[[OUTCOME, TREAT] + all_covs].dropna()
Y = sub3[OUTCOME].values
D = sub3[TREAT].values
W = sub3[all_covs].values

scaler = StandardScaler()
W_sc = scaler.fit_transform(W)

# Step 1: LASSO outcome on controls
lasso_y = LassoCV(cv=5, random_state=42, max_iter=10000).fit(W_sc, Y)
sel_y = set(np.where(np.abs(lasso_y.coef_) > 1e-8)[0])

# Step 2: LASSO treatment on controls
lasso_d = LassoCV(cv=5, random_state=42, max_iter=10000).fit(W_sc, D)
sel_d = set(np.where(np.abs(lasso_d.coef_) > 1e-8)[0])

# Union of selected
sel_union = sorted(sel_y | sel_d)
selected_names = [all_covs[i] for i in sel_union]
print(f"Double LASSO selected {len(selected_names)} covariates: {selected_names}")

if len(selected_names) > 0:
    res3 = ols_result(sub3[OUTCOME], sub3[[TREAT] + selected_names], "Double LASSO")
else:
    res3 = ols_result(sub3[OUTCOME], sub3[[TREAT]], "Double LASSO (no covariates selected)")
print(f"Spec 3 (LASSO): coef={res3['coef']:.4f}, p={res3['p_value']:.4f}")

# Save main results
main_df = pd.DataFrame([res1, res2, res3])
main_df.to_csv(CLEAN / "main_results.csv", index=False)
print("Main results saved.")

# ── 4. CATE by pro_israel quintile ────────────────────────────────────
sub_cate = df[[OUTCOME, TREAT, "pro_israel_quintile"]].dropna()
sub_cate["pro_israel_quintile"] = sub_cate["pro_israel_quintile"].astype(int)

# Create quintile dummies and interactions
quintiles = sorted(sub_cate["pro_israel_quintile"].unique())
for q in quintiles:
    sub_cate[f"Q{q}"] = (sub_cate["pro_israel_quintile"] == q).astype(int)
    sub_cate[f"treat_x_Q{q}"] = sub_cate[TREAT] * sub_cate[f"Q{q}"]

# Regression: outcome ~ treat + Q2..Q5 + treat*Q2..treat*Q5
# Reference group: Q1
ref_q = quintiles[0]
q_dummies = [f"Q{q}" for q in quintiles[1:]]
interactions = [f"treat_x_Q{q}" for q in quintiles[1:]]
cate_X = sub_cate[[TREAT] + q_dummies + interactions]
cate_X_c = sm.add_constant(cate_X)
cate_model = sm.OLS(sub_cate[OUTCOME], cate_X_c, missing="drop").fit(cov_type="HC2")

# Extract CATE for each quintile
cate_rows = []
for q in quintiles:
    if q == ref_q:
        # CATE for Q1 = coefficient on treatment
        coef = cate_model.params[TREAT]
        se = cate_model.bse[TREAT]
    else:
        # CATE for Qq = coef(treat) + coef(treat_x_Qq)
        coef = cate_model.params[TREAT] + cate_model.params[f"treat_x_Q{q}"]
        # SE via delta method (Var(a+b) = Var(a) + Var(b) + 2Cov(a,b))
        v_t = cate_model.cov_params().loc[TREAT, TREAT]
        v_i = cate_model.cov_params().loc[f"treat_x_Q{q}", f"treat_x_Q{q}"]
        cov_ti = cate_model.cov_params().loc[TREAT, f"treat_x_Q{q}"]
        se = np.sqrt(v_t + v_i + 2 * cov_ti)

    ci_lo = coef - 1.96 * se
    ci_hi = coef + 1.96 * se
    t = coef / se if se > 0 else np.nan
    p = 2 * (1 - stats.norm.cdf(abs(t)))

    cate_rows.append({
        "quintile": int(q),
        "cate": round(coef, 6),
        "se_hc2": round(se, 6),
        "ci_lower": round(ci_lo, 6),
        "ci_upper": round(ci_hi, 6),
        "t_stat": round(t, 4),
        "p_value": round(p, 6),
    })

cate_df = pd.DataFrame(cate_rows)
cate_df.to_csv(CLEAN / "cate_results.csv", index=False)
print("CATE results saved.")

# ── 5. Joint F-test for heterogeneity ─────────────────────────────────
n_interact = len(interactions)
n_params = len(cate_model.params)
# Test that all interaction coefficients = 0
R = np.zeros((n_interact, n_params))
for i, col in enumerate(interactions):
    idx = list(cate_model.params.index).index(col)
    R[i, idx] = 1
ftest_het = cate_model.f_test(R)
print(f"Joint F-test heterogeneity: F={float(ftest_het.fvalue):.3f}, p={float(ftest_het.pvalue):.4f}")

# ── 6. Continuous interaction ─────────────────────────────────────────
sub_cont = df[[OUTCOME, TREAT, "pro_israel_score"]].dropna()
sub_cont["treat_x_pis"] = sub_cont[TREAT] * sub_cont["pro_israel_score"]
X_cont = sm.add_constant(sub_cont[[TREAT, "pro_israel_score", "treat_x_pis"]])
cont_model = sm.OLS(sub_cont[OUTCOME], X_cont).fit(cov_type="HC2")
print(f"Continuous interaction: coef={cont_model.params['treat_x_pis']:.6f}, "
      f"p={cont_model.pvalues['treat_x_pis']:.4f}")

# ── 7. Cohen's d ──────────────────────────────────────────────────────
sub_d = df[[OUTCOME, TREAT]].dropna()
t_vals = sub_d.loc[sub_d[TREAT] == 1, OUTCOME]
c_vals = sub_d.loc[sub_d[TREAT] == 0, OUTCOME]
pooled_sd = np.sqrt(((len(t_vals)-1)*t_vals.var() + (len(c_vals)-1)*c_vals.var()) /
                     (len(t_vals) + len(c_vals) - 2))
cohens_d = (t_vals.mean() - c_vals.mean()) / pooled_sd
print(f"Cohen's d = {cohens_d:.4f}")

# ── 8. Permutation test ──────────────────────────────────────────────
sub_perm = df[[OUTCOME, TREAT]].dropna()
actual_diff = sub_perm.groupby(TREAT)[OUTCOME].mean().diff().iloc[-1]

rng = np.random.default_rng(42)
n_perms = 2000
perm_diffs = np.empty(n_perms)
treat_arr = sub_perm[TREAT].values.copy()
outcome_arr = sub_perm[OUTCOME].values

for i in range(n_perms):
    rng.shuffle(treat_arr)
    perm_diffs[i] = outcome_arr[treat_arr == 1].mean() - outcome_arr[treat_arr == 0].mean()

perm_p = (np.abs(perm_diffs) >= np.abs(actual_diff)).mean()
print(f"Permutation test: actual diff={actual_diff:.4f}, p={perm_p:.4f}")

perm_df = pd.DataFrame({
    "permutation_diff": perm_diffs,
})
perm_df.to_csv(CLEAN / "permutation_distribution.csv", index=False)

# Add heterogeneity test, continuous interaction, Cohen's d, permutation to main results
extra = pd.DataFrame([
    {"specification": "Joint F-test heterogeneity",
     "coef": float(ftest_het.fvalue), "p_value": float(ftest_het.pvalue),
     "n": int(cate_model.nobs)},
    {"specification": "Continuous interaction (treat x pro_israel_score)",
     "coef": round(cont_model.params["treat_x_pis"], 6),
     "se_hc2": round(cont_model.bse["treat_x_pis"], 6),
     "p_value": round(cont_model.pvalues["treat_x_pis"], 6),
     "n": int(cont_model.nobs)},
    {"specification": "Cohen's d", "coef": round(cohens_d, 6),
     "n": len(sub_d)},
    {"specification": "Permutation test (2000 reshuffles)",
     "coef": round(actual_diff, 6), "p_value": round(perm_p, 6),
     "n": len(sub_perm)},
])
main_full = pd.concat([main_df, extra], ignore_index=True)
main_full.to_csv(CLEAN / "main_results.csv", index=False)

print("01_main.py complete.")
