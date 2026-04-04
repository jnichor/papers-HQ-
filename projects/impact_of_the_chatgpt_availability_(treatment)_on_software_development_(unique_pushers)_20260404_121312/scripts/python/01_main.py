"""
01_main.py
DiD, Event Study, and Synthetic Control for the impact of ChatGPT
availability on software development (unique pushers).
"""

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
import numpy as np
import pandas as pd
from linearmodels.panel import PanelOLS
import cvxpy as cp
from scipy import stats

# ------------------------------------------------------------------ #
# PATHS
# ------------------------------------------------------------------ #
PROJECT = Path(__file__).resolve().parents[2]
DATA    = PROJECT / "data" / "clean" / "clean_data.csv"
OUTPUT  = PROJECT / "output"
OUTPUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA)
print("=" * 70)
print("LOADED: %d rows, %d columns" % (df.shape[0], df.shape[1]))
print("Columns: %s" % ", ".join(df.columns.tolist()))
print("=" * 70)

# ------------------------------------------------------------------ #
# 1. SANITY CHECK
# ------------------------------------------------------------------ #
print("\n### 1. SANITY CHECK ###")
print(
    "Theory predicts NEGATIVE: restricted countries should have FEWER "
    "pushers growth post-ChatGPT relative to unrestricted"
)

# ------------------------------------------------------------------ #
# 2. DiD  --  Persistent bans (CN/RU/IR/SY/CU vs rest)
# ------------------------------------------------------------------ #
print("\n### 2. DiD -- Persistent Bans ###")

df["country_id"] = pd.Categorical(df["iso2_code"]).codes
panel = df.set_index(["country_id", "quarter_id"])

mod_did = PanelOLS(
    dependent=panel["log_pushers"],
    exog=panel[["treat_did"]],
    entity_effects=True,
    time_effects=True,
    check_rank=False,
)
res_did = mod_did.fit(cov_type="clustered", cluster_entity=True)

coef  = res_did.params["treat_did"]
se    = res_did.std_errors["treat_did"]
pval  = res_did.pvalues["treat_did"]
nobs  = int(res_did.nobs)
r2    = res_did.rsquared

print("  treat_did coefficient : %.4f" % coef)
print("  Std. error            : %.4f" % se)
print("  p-value               : %.4f" % pval)
print("  N                     : %d" % nobs)
print("  R-squared (within)    : %.4f" % r2)
if coef < 0:
    print("  --> Coefficient is NEGATIVE, consistent with theory.")
else:
    print("  --> Coefficient is POSITIVE, inconsistent with theory.")

main_results = pd.DataFrame([{
    "model": "DiD_persistent_bans",
    "coefficient": round(coef, 6),
    "std_error": round(se, 6),
    "p_value": round(pval, 6),
    "n_obs": nobs,
    "r_squared": round(r2, 6),
}])

# ------------------------------------------------------------------ #
# 3. EVENT STUDY
# ------------------------------------------------------------------ #
print("\n### 3. Event Study ###")

# ChatGPT launch ~ Q4 2022 (quarter_id 20224).  Reference = Q3 2022.
all_quarters = sorted(df["quarter_id"].unique())
ref_quarter = 20223  # Q3 2022

# Create interaction dummies: banned_persistent x I(quarter == q)
event_cols = []
for q in all_quarters:
    if q == ref_quarter:
        continue
    col = "banned_x_q%d" % q
    df[col] = (df["banned_persistent"] * (df["quarter_id"] == q)).astype(int)
    event_cols.append(col)

df["country_id"] = pd.Categorical(df["iso2_code"]).codes
panel_es = df.set_index(["country_id", "quarter_id"])

mod_es = PanelOLS(
    dependent=panel_es["log_pushers"],
    exog=panel_es[event_cols],
    entity_effects=True,
    time_effects=True,
)
res_es = mod_es.fit(cov_type="clustered", cluster_entity=True)

es_df = pd.DataFrame({
    "quarter_id": [int(c.replace("banned_x_q", "")) for c in event_cols],
    "coefficient": [res_es.params[c] for c in event_cols],
    "std_error":   [res_es.std_errors[c] for c in event_cols],
    "p_value":     [res_es.pvalues[c] for c in event_cols],
})
es_df["ci_lower"] = es_df["coefficient"] - 1.96 * es_df["std_error"]
es_df["ci_upper"] = es_df["coefficient"] + 1.96 * es_df["std_error"]
es_df = es_df.sort_values("quarter_id").reset_index(drop=True)

# Label pre / post
es_df["period"] = np.where(es_df["quarter_id"] < 20224, "pre", "post")

print("  Event-study coefficients (ref = Q3-2022):")
for _, row in es_df.iterrows():
    flag = "*" if row["p_value"] < 0.05 else ""
    print(
        "    q%d  coef=%.4f  se=%.4f  p=%.4f  [%.4f, %.4f] %s"
        % (
            row["quarter_id"],
            row["coefficient"],
            row["std_error"],
            row["p_value"],
            row["ci_lower"],
            row["ci_upper"],
            flag,
        )
    )

# ------------------------------------------------------------------ #
# 5. PRE-TREND TEST  (joint F-test on pre-treatment dummies)
# ------------------------------------------------------------------ #
print("\n### 5. Pre-trend Test (Joint F-test) ###")

pre_cols = [c for c, q in zip(event_cols, [int(x.replace("banned_x_q","")) for x in event_cols]) if q < 20224]

if len(pre_cols) > 0:
    # Build restriction matrix: R * beta = 0 for pre-treatment coefficients
    pre_indices = [event_cols.index(c) for c in pre_cols]
    R = np.zeros((len(pre_cols), len(event_cols)))
    for i, idx in enumerate(pre_indices):
        R[i, idx] = 1.0

    beta_hat = res_es.params.values
    V = res_es.cov.values  # variance-covariance matrix

    r = R @ beta_hat
    meat = R @ V @ R.T
    try:
        F_stat = float(r.T @ np.linalg.inv(meat) @ r) / len(pre_cols)
        df1 = len(pre_cols)
        df2 = int(res_es.nobs) - len(event_cols)
        p_F = 1.0 - stats.f.cdf(F_stat, df1, df2)
        print("  F(%d, %d) = %.4f,  p = %.4f" % (df1, df2, F_stat, p_F))
        if p_F > 0.05:
            print("  --> Cannot reject null of parallel pre-trends (good).")
        else:
            print("  --> Pre-trends may be violated (p < 0.05).")
    except np.linalg.LinAlgError:
        F_stat, p_F = np.nan, np.nan
        print("  Singular matrix -- could not compute F-test.")
else:
    F_stat, p_F = np.nan, np.nan
    print("  No pre-treatment dummies found.")

main_results = pd.concat([main_results, pd.DataFrame([{
    "model": "pre_trend_F_test",
    "coefficient": round(F_stat, 6) if not np.isnan(F_stat) else np.nan,
    "std_error": np.nan,
    "p_value": round(p_F, 6) if not np.isnan(p_F) else np.nan,
    "n_obs": int(res_es.nobs),
    "r_squared": round(res_es.rsquared, 6),
}])], ignore_index=True)

# ------------------------------------------------------------------ #
# 4. SYNTHETIC CONTROL FOR ITALY  (cvxpy)
# ------------------------------------------------------------------ #
print("\n### 4. Synthetic Control -- Italy ###")

EU_CODES = [
    "DE", "FR", "ES", "PT", "NL", "BE", "AT", "SE", "DK", "FI",
    "PL", "CZ", "RO", "HU", "BG", "HR", "SK", "SI", "LT", "LV",
    "EE", "IE", "GR", "CY", "MT", "LU",
]

# Filter to EU countries present in data (exclude IT from donors)
eu_in_data = [c for c in EU_CODES if c in df["iso2_code"].values]
it_df = df[df["iso2_code"] == "IT"].sort_values("quarter_id")

# Build donor matrix -- pivot to wide
donor_df = df[df["iso2_code"].isin(eu_in_data)].copy()
donor_wide = donor_df.pivot_table(
    index="quarter_id", columns="iso2_code", values="log_pushers"
)
# Keep only quarters present for Italy and donors
common_q = sorted(set(it_df["quarter_id"]) & set(donor_wide.index))
it_series = it_df.set_index("quarter_id").loc[common_q, "log_pushers"].values
donor_mat = donor_wide.loc[common_q].values  # (T x J)

# Handle missing values: drop quarters where any donor or Italy is NaN
valid = ~(np.isnan(it_series) | np.any(np.isnan(donor_mat), axis=1))
common_q_arr = np.array(common_q)
common_q_valid = common_q_arr[valid].tolist()
it_series = it_series[valid]
donor_mat = donor_mat[valid]

donor_names = donor_wide.columns.tolist()

# Pre-treatment: quarter_id < 20232 (before Q2 2023, Italy ban started Q2 2023)
pre_mask = np.array([q < 20232 for q in common_q_valid])
post_mask = ~pre_mask

Y_pre = it_series[pre_mask]
D_pre = donor_mat[pre_mask]

J = D_pre.shape[1]
w = cp.Variable(J)
objective = cp.Minimize(cp.sum_squares(D_pre @ w - Y_pre))
constraints = [w >= 0, cp.sum(w) == 1]
prob = cp.Problem(objective, constraints)
prob.solve(solver=cp.SCS, verbose=False)

w_vals = np.array(w.value).flatten()

# Synthetic Italy
synth_all = donor_mat @ w_vals
gap = it_series - synth_all

pre_rmspe = np.sqrt(np.mean((it_series[pre_mask] - synth_all[pre_mask]) ** 2))
post_gaps = gap[post_mask]

print("  Donor weights (top 5):")
top5 = np.argsort(-w_vals)[:5]
for idx in top5:
    if w_vals[idx] > 0.001:
        print("    %s : %.4f" % (donor_names[idx], w_vals[idx]))

print("  Pre-treatment RMSPE : %.4f" % pre_rmspe)
print("  Post-treatment gaps (Italy actual - synthetic):")

sc_results = []
for i, q in enumerate(common_q_valid):
    label = "PRE " if pre_mask[i] else "POST"
    sc_results.append({
        "quarter_id": q,
        "italy_actual": round(it_series[i], 4),
        "italy_synthetic": round(synth_all[i], 4),
        "gap": round(gap[i], 4),
        "period": "pre" if pre_mask[i] else "post",
    })
    if not pre_mask[i]:
        print(
            "    q%d  actual=%.4f  synth=%.4f  gap=%.4f"
            % (q, it_series[i], synth_all[i], gap[i])
        )

if len(post_gaps) > 0:
    avg_post_gap = np.mean(post_gaps)
    print("  Average post-treatment gap: %.4f" % avg_post_gap)
else:
    avg_post_gap = np.nan
    print("  No post-treatment periods found.")

main_results = pd.concat([main_results, pd.DataFrame([{
    "model": "synth_control_italy",
    "coefficient": round(avg_post_gap, 6) if not np.isnan(avg_post_gap) else np.nan,
    "std_error": round(pre_rmspe, 6),
    "p_value": np.nan,
    "n_obs": len(common_q_valid),
    "r_squared": np.nan,
}])], ignore_index=True)

# ------------------------------------------------------------------ #
# 6. SAVE RESULTS
# ------------------------------------------------------------------ #
print("\n### 6. Saving Results ###")

main_results.to_csv(OUTPUT / "main_results.csv", index=False)
print("  Saved: %s" % (OUTPUT / "main_results.csv"))

es_df.to_csv(OUTPUT / "event_study_coefficients.csv", index=False)
print("  Saved: %s" % (OUTPUT / "event_study_coefficients.csv"))

sc_df = pd.DataFrame(sc_results)
sc_df.to_csv(OUTPUT / "synthetic_control_results.csv", index=False)
print("  Saved: %s" % (OUTPUT / "synthetic_control_results.csv"))

print("\n" + "=" * 70)
print("DONE.")
print("=" * 70)
