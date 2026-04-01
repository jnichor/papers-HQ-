"""02_robustness.py - Robustness checks for ratchet effect."""

import numpy as np
import pandas as pd
import pyfixest as pf
from pathlib import Path
from scipy import stats  # noqa: F401
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

np.random.seed(42)

PROJECT = Path(r"C:\Users\jesus\Documents\paper-HQ-sin API\projects\data_first_20260401_124533")
DATA_CLEAN = PROJECT / "data" / "clean"

LIBERTIES = ["freexp", "freass", "frerel", "fremov", "fairtrial"]

print("=" * 70)
print("02_robustness.py - Robustness Checks")
print("=" * 70)

df = pd.read_csv(DATA_CLEAN / "clean_data.csv")
print(f"\n[1] Data: {len(df):,} rows")

results = []

# ══════════════════════════════════════════════════════════════════════════════
# 2. PLACEBO BUST DATES
# ══════════════════════════════════════════════════════════════════════════════
print("\n[2] Placebo bust dates (permutation test)...")
LIB = "fairtrial"  # primary outcome (significant in TWFE)
df_reg = df.dropna(subset=[LIB]).copy()

try:
    actual = pf.feols(f"{LIB} ~ bust | country_id + YEAR", data=df_reg,
                       vcov={"CRV1": "country_id"})
    actual_coef = actual.coef().iloc[0]

    N_PERMS = 999
    placebo_coefs = []
    countries = df_reg["ID"].unique()
    bust_status = df_reg.groupby("ID")["bust"].apply(lambda x: x.values).to_dict()

    for i in range(N_PERMS):
        df_p = df_reg.copy()
        # Shuffle bust indicators within each country's time series
        for c in countries:
            mask = df_p["ID"] == c
            vals = df_p.loc[mask, "bust"].values.copy()
            np.random.shuffle(vals)
            df_p.loc[mask, "bust"] = vals
        try:
            m = pf.feols(f"{LIB} ~ bust | country_id + YEAR", data=df_p,
                          vcov={"CRV1": "country_id"})
            placebo_coefs.append(m.coef().iloc[0])
        except:
            pass
        if (i + 1) % 200 == 0:
            print(f"      Permutation {i+1}/{N_PERMS}")

    placebo_coefs = np.array(placebo_coefs)
    p_placebo = np.mean(np.abs(placebo_coefs) >= np.abs(actual_coef))
    print(f"    Actual: {actual_coef:.4f}, Placebo p-value: {p_placebo:.4f}")
    results.append({"test": "Placebo bust dates", "coef": actual_coef,
                     "placebo_pval": p_placebo, "n_perms": len(placebo_coefs)})
except Exception as e:
    print(f"    [error] {e}")

# ══════════════════════════════════════════════════════════════════════════════
# 3. ALTERNATIVE BUST THRESHOLDS
# ══════════════════════════════════════════════════════════════════════════════
print("\n[3] Alternative bust thresholds...")
for thresh in [-15, -25, -30]:
    df_t = df.copy()
    df_t["bust_alt"] = (df_t["ctot_cum3"] <= thresh).astype(int)
    df_t_reg = df_t.dropna(subset=[LIB]).copy()
    n_busts = df_t_reg["bust_alt"].sum()
    try:
        m = pf.feols(f"{LIB} ~ bust_alt | country_id + YEAR", data=df_t_reg,
                      vcov={"CRV1": "country_id"})
        c, s, p = m.coef().iloc[0], m.se().iloc[0], m.pvalue().iloc[0]
        print(f"    Threshold {thresh}%: coef={c:.4f} (SE={s:.4f}, p={p:.4f}), N_bust={n_busts}")
        results.append({"test": f"Bust threshold {thresh}%", "coef": c, "se": s,
                         "pvalue": p, "n_busts": n_busts})
    except Exception as e:
        print(f"    Threshold {thresh}%: FAILED - {e}")

# ══════════════════════════════════════════════════════════════════════════════
# 4. ALL 5 LIBERTIES BUST EFFECT
# ══════════════════════════════════════════════════════════════════════════════
print("\n[4] Bust effect across all liberties...")
for lib in LIBERTIES:
    df_lib = df.dropna(subset=[lib]).copy()
    try:
        m = pf.feols(f"{lib} ~ bust | country_id + YEAR", data=df_lib,
                      vcov={"CRV1": "country_id"})
        c, s, p = m.coef().iloc[0], m.se().iloc[0], m.pvalue().iloc[0]
        print(f"    {lib}: coef={c:.4f} (SE={s:.4f}, p={p:.4f})")
        results.append({"test": f"Bust effect: {lib}", "coef": c, "se": s, "pvalue": p})
    except Exception as e:
        print(f"    {lib}: FAILED - {e}")

# ══════════════════════════════════════════════════════════════════════════════
# 5. COVID-19 EXCLUSION (movement restrictions confounder)
# ══════════════════════════════════════════════════════════════════════════════
print("\n[5] COVID-19 exclusion (2020-2021)...")
for lib in ["fremov", "fairtrial"]:
    df_nocovid = df[df["YEAR"] < 2020].dropna(subset=[lib]).copy()
    try:
        m = pf.feols(f"{lib} ~ bust | country_id + YEAR", data=df_nocovid,
                      vcov={"CRV1": "country_id"})
        c, s, p = m.coef().iloc[0], m.se().iloc[0], m.pvalue().iloc[0]
        print(f"    {lib} (excl COVID): coef={c:.4f} (SE={s:.4f}, p={p:.4f}), N={len(df_nocovid):,}")
        results.append({"test": f"Excl COVID 2020-21: {lib}", "coef": c, "se": s,
                         "pvalue": p, "n_obs": len(df_nocovid)})
    except Exception as e:
        print(f"    {lib}: FAILED - {e}")

# ══════════════════════════════════════════════════════════════════════════════
# 6. PLACEBO FOR MOVEMENT (the ratchet variable)
# ══════════════════════════════════════════════════════════════════════════════
print("\n[6] Placebo bust dates for fremov...")
df_mov = df.dropna(subset=["fremov"]).copy()
try:
    actual_mov = pf.feols("fremov ~ bust | country_id + YEAR", data=df_mov,
                           vcov={"CRV1": "country_id"})
    actual_mov_coef = actual_mov.coef().iloc[0]

    placebo_mov = []
    countries = df_mov["ID"].unique()
    for i in range(999):
        df_p = df_mov.copy()
        for c in countries:
            mask = df_p["ID"] == c
            vals = df_p.loc[mask, "bust"].values.copy()
            np.random.shuffle(vals)
            df_p.loc[mask, "bust"] = vals
        try:
            m = pf.feols("fremov ~ bust | country_id + YEAR", data=df_p,
                          vcov={"CRV1": "country_id"})
            placebo_mov.append(m.coef().iloc[0])
        except:
            pass
        if (i + 1) % 200 == 0:
            print(f"      Permutation {i+1}/999")

    placebo_mov = np.array(placebo_mov)
    p_mov = np.mean(np.abs(placebo_mov) >= np.abs(actual_mov_coef))
    print(f"    fremov actual: {actual_mov_coef:.4f}, placebo p: {p_mov:.4f}")
    results.append({"test": "Placebo: fremov", "coef": actual_mov_coef,
                     "placebo_pval": p_mov, "n_perms": len(placebo_mov)})
except Exception as e:
    print(f"    [error] {e}")

# ══════════════════════════════════════════════════════════════════════════════
# 7. POWER ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
print("\n[5] Power analysis...")
outcome_sd = df[LIB].std()
n_countries = df["ID"].nunique()
n_per_country = len(df) / n_countries
icc = 0.5  # high ICC for country-level political data
deff = 1 + (n_per_country - 1) * icc
mde = 2.8 * outcome_sd / np.sqrt(n_countries * n_per_country) * np.sqrt(deff)
mde_sd = mde / outcome_sd
print(f"    Outcome SD: {outcome_sd:.3f}")
print(f"    Countries: {n_countries}, Avg obs/country: {n_per_country:.1f}")
print(f"    MDE (80% power): {mde:.3f} ({mde_sd:.3f} SD)")
results.append({"test": "Power analysis", "mde": mde, "mde_sd": mde_sd})

# ══════════════════════════════════════════════════════════════════════════════
# 6. SAVE
# ══════════════════════════════════════════════════════════════════════════════
rob_df = pd.DataFrame(results)
rob_df.to_csv(DATA_CLEAN / "robustness_results.csv", index=False)
print(f"\n    Saved robustness_results.csv ({len(rob_df)} tests)")
print("\n" + "=" * 70)
print("02_robustness.py completed successfully")
print("=" * 70)
