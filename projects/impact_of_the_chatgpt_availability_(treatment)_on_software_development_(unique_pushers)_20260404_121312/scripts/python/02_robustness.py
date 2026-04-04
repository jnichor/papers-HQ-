"""
02_robustness.py
Robustness checks for the ChatGPT ban DiD analysis.
"""

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
import numpy as np
import pandas as pd
from linearmodels.panel import PanelOLS
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
print("02_robustness.py -- Robustness Checks")
print("LOADED: %d rows, %d columns" % (df.shape[0], df.shape[1]))
print("=" * 70)

results = []

# ------------------------------------------------------------------ #
# Helper: run a DiD regression, return dict
# ------------------------------------------------------------------ #
def run_did(data, dep_var, treat_var, label):
    """Run a two-way FE DiD and return results dict."""
    tmp = data.copy()
    tmp["_cid"] = pd.Categorical(tmp["iso2_code"]).codes
    panel = tmp.set_index(["_cid", "quarter_id"])
    mod = PanelOLS(
        dependent=panel[dep_var],
        exog=panel[[treat_var]],
        entity_effects=True,
        time_effects=True,
        check_rank=False,
    )
    res = mod.fit(cov_type="clustered", cluster_entity=True)
    coef = res.params[treat_var]
    se   = res.std_errors[treat_var]
    pval = res.pvalues[treat_var]
    nobs = int(res.nobs)
    r2   = res.rsquared
    out = {
        "model": label,
        "coefficient": round(coef, 6),
        "std_error": round(se, 6),
        "p_value": round(pval, 6),
        "n_obs": nobs,
        "r_squared": round(r2, 6),
    }
    return out


# ================================================================== #
# 1. FALSIFICATION -- Placebo outcome: n_languages
# ================================================================== #
print("\n### 1. Placebo Outcome: n_languages ###")
print("  n_languages should NOT be affected by a ChatGPT ban.")

df["log_n_languages"] = np.log(df["n_languages"] + 1)
r1 = run_did(df, "log_n_languages", "treat_did", "placebo_outcome_n_languages")
results.append(r1)

print("  coefficient : %.4f" % r1["coefficient"])
print("  p-value     : %.4f" % r1["p_value"])
if r1["p_value"] > 0.10:
    print("  --> NOT significant (good: placebo outcome unaffected).")
else:
    print("  --> Significant -- potential concern.")

# ================================================================== #
# 2. FALSIFICATION -- Placebo timing: shift treatment to Q2 2021
# ================================================================== #
print("\n### 2. Placebo Timing: Treatment shifted to Q2 2021 ###")
print("  Restrict to pre-ChatGPT period only (quarter_id < 20224).")
print("  Fake post = quarter_id >= 20212.")

pre_df = df[df["quarter_id"] < 20224].copy()
pre_df["fake_post"] = (pre_df["quarter_id"] >= 20212).astype(int)
pre_df["fake_treat_did"] = pre_df["banned_persistent"] * pre_df["fake_post"]

r2 = run_did(pre_df, "log_pushers", "fake_treat_did", "placebo_timing_Q2_2021")
results.append(r2)

print("  coefficient : %.4f" % r2["coefficient"])
print("  p-value     : %.4f" % r2["p_value"])
if r2["p_value"] > 0.10:
    print("  --> NOT significant (good: no effect at placebo date).")
else:
    print("  --> Significant -- potential concern for parallel trends.")

# ================================================================== #
# 3. SEPARATE COUNTRY DiD: China only, Russia only
# ================================================================== #
print("\n### 3. Separate Country DiD ###")

for code, name in [("CN", "China"), ("RU", "Russia")]:
    sub = df[(df["iso2_code"] == code) | (df["banned_persistent"] == 0)].copy()
    sub["_banned"] = (sub["iso2_code"] == code).astype(int)
    sub["_treat"] = sub["_banned"] * sub["post_chatgpt"]
    r = run_did(sub, "log_pushers", "_treat", "did_%s_only" % code)
    results.append(r)
    print("  %s: coef=%.4f  se=%.4f  p=%.4f" % (name, r["coefficient"], r["std_error"], r["p_value"]))

# ================================================================== #
# 4. EXCLUDE COVID PERIOD (drop 2020)
# ================================================================== #
print("\n### 4. Exclude COVID Period (drop 2020) ###")

no_covid = df[df["year"] != 2020].copy()
r4 = run_did(no_covid, "log_pushers", "treat_did", "exclude_covid_2020")
results.append(r4)

print("  coefficient : %.4f" % r4["coefficient"])
print("  p-value     : %.4f" % r4["p_value"])
print("  N           : %d" % r4["n_obs"])

# ================================================================== #
# 5. OECD-ONLY CONTROL GROUP
# ================================================================== #
print("\n### 5. OECD-only Control Group ###")

OECD_CODES = [
    "US", "GB", "DE", "FR", "JP", "CA", "AU", "KR", "IT", "ES",
    "NL", "BE", "AT", "SE", "DK", "FI", "NO", "CH", "IE", "PL",
    "CZ", "HU", "SK", "SI", "PT", "GR", "LU", "EE", "LV", "LT",
    "IS", "NZ", "MX", "CL", "CO", "CR", "IL", "TR",
]

# Keep banned countries + OECD controls (excluding banned from OECD list)
banned_codes = {"CN", "RU", "IR", "SY", "CU"}
oecd_df = df[
    (df["iso2_code"].isin(banned_codes)) |
    ((df["banned_persistent"] == 0) & (df["iso2_code"].isin(OECD_CODES)))
].copy()

n_ctrl = oecd_df[oecd_df["banned_persistent"] == 0]["iso2_code"].nunique()
print("  OECD control countries in data: %d" % n_ctrl)

r5 = run_did(oecd_df, "log_pushers", "treat_did", "oecd_only_controls")
results.append(r5)

print("  coefficient : %.4f" % r5["coefficient"])
print("  p-value     : %.4f" % r5["p_value"])

# ================================================================== #
# 6. SENSITIVITY: Exclude small countries (< 500 avg pushers)
# ================================================================== #
print("\n### 6. Exclude Small Countries (< 500 avg pushers) ###")

avg_pushers = df.groupby("iso2_code")["total_pushers"].mean()
large_codes = avg_pushers[avg_pushers >= 500].index.tolist()
large_df = df[df["iso2_code"].isin(large_codes)].copy()

n_dropped = df["iso2_code"].nunique() - large_df["iso2_code"].nunique()
print("  Dropped %d countries with < 500 average pushers." % n_dropped)

r6 = run_did(large_df, "log_pushers", "treat_did", "exclude_small_countries")
results.append(r6)

print("  coefficient : %.4f" % r6["coefficient"])
print("  p-value     : %.4f" % r6["p_value"])

# ================================================================== #
# 7. PERMUTATION TEST
# ================================================================== #
print("\n### 7. Permutation Test (500 iterations) ###")

np.random.seed(42)
non_banned = df[df["banned_persistent"] == 0]["iso2_code"].unique()
n_banned = 5  # same number as actual banned countries
n_perms = 500

actual_coef_row = run_did(df, "log_pushers", "treat_did", "_actual")
actual_coef = actual_coef_row["coefficient"]

perm_coefs = []
for i in range(n_perms):
    if (i + 1) % 100 == 0:
        print("  Permutation %d / %d ..." % (i + 1, n_perms))
    fake_banned = set(np.random.choice(non_banned, size=n_banned, replace=False))
    tmp = df.copy()
    tmp["perm_banned"] = tmp["iso2_code"].isin(fake_banned).astype(int)
    tmp["perm_treat"] = tmp["perm_banned"] * tmp["post_chatgpt"]
    try:
        r = run_did(tmp, "log_pushers", "perm_treat", "_perm")
        perm_coefs.append(r["coefficient"])
    except Exception:
        perm_coefs.append(np.nan)

perm_coefs = np.array(perm_coefs)
perm_coefs_valid = perm_coefs[~np.isnan(perm_coefs)]

# p-value: share of permutation coefficients <= actual (one-sided, negative)
perm_p = np.mean(perm_coefs_valid <= actual_coef)
print("  Actual DiD coefficient   : %.4f" % actual_coef)
print("  Permutation mean         : %.4f" % np.nanmean(perm_coefs))
print("  Permutation std          : %.4f" % np.nanstd(perm_coefs))
print("  Permutation p-value      : %.4f  (share <= actual)" % perm_p)

results.append({
    "model": "permutation_test",
    "coefficient": round(actual_coef, 6),
    "std_error": round(float(np.nanstd(perm_coefs)), 6),
    "p_value": round(perm_p, 6),
    "n_obs": len(perm_coefs_valid),
    "r_squared": np.nan,
})

if perm_p < 0.05:
    print("  --> Actual effect is in the extreme tail (significant).")
else:
    print("  --> Actual effect is NOT extreme relative to random assignment.")

# ================================================================== #
# 8. SAVE
# ================================================================== #
print("\n### 8. Saving Results ###")

rob_df = pd.DataFrame(results)
rob_path = OUTPUT / "robustness_results.csv"
rob_df.to_csv(rob_path, index=False)
print("  Saved: %s" % rob_path)

perm_dist_df = pd.DataFrame({
    "iteration": range(1, n_perms + 1),
    "permutation_coefficient": perm_coefs,
})
perm_path = OUTPUT / "permutation_distribution.csv"
perm_dist_df.to_csv(perm_path, index=False)
print("  Saved: %s" % perm_path)

print("\n" + "=" * 70)
print("02_robustness.py DONE.")
print("=" * 70)
