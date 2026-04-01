"""01_main.py - Asymmetric event study: bust vs recovery effects on civil liberties."""

import numpy as np
import pandas as pd
import pyfixest as pf
from pathlib import Path
from scipy import stats
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

np.random.seed(42)

PROJECT = Path(r"C:\Users\jesus\Documents\paper-HQ-sin API\projects\data_first_20260401_124533")
DATA_CLEAN = PROJECT / "data" / "clean"

LIBERTIES = ["freexp", "freass", "frerel", "fremov", "fairtrial"]
LIBERTY_LABELS = {"freexp": "Expression", "freass": "Assembly", "frerel": "Religion",
                  "fremov": "Movement", "fairtrial": "Fair Trial"}

print("=" * 70)
print("01_main.py - Asymmetric Event Study")
print("=" * 70)

df = pd.read_csv(DATA_CLEAN / "clean_data.csv")
print(f"\n[1] Data: {len(df):,} rows, {df['ID'].nunique()} countries")

# ══════════════════════════════════════════════════════════════════════════════
# 2. TWFE BASELINE: bust effect on each liberty
# ══════════════════════════════════════════════════════════════════════════════
print("\n[2] TWFE baseline: bust effect on each civil liberty")
print(f"    {'Liberty':<15} {'Coef':>8} {'SE':>8} {'p-val':>8} {'N':>8}")
print(f"    {'-'*15} {'-'*8} {'-'*8} {'-'*8} {'-'*8}")

twfe_results = []
for lib in LIBERTIES:
    df_reg = df.dropna(subset=[lib]).copy()
    try:
        m = pf.feols(f"{lib} ~ bust | country_id + YEAR", data=df_reg,
                      vcov={"CRV1": "country_id"})
        c, s, p = m.coef().iloc[0], m.se().iloc[0], m.pvalue().iloc[0]
        ci_lo, ci_hi = c - 1.96 * s, c + 1.96 * s
        stars = "***" if p < 0.01 else "**" if p < 0.05 else "*" if p < 0.1 else ""
        print(f"    {lib:<15} {c:>8.4f} {s:>8.4f} {p:>8.4f} {len(df_reg):>8,} {stars}")
        twfe_results.append({"liberty": lib, "coef": c, "se": s, "pvalue": p,
                              "ci_lower": ci_lo, "ci_upper": ci_hi, "n": len(df_reg)})
    except Exception as e:
        print(f"    {lib:<15} FAILED: {e}")

pd.DataFrame(twfe_results).to_csv(DATA_CLEAN / "twfe_bust_results.csv", index=False)

# ══════════════════════════════════════════════════════════════════════════════
# 3. BUST EVENT STUDY
# ══════════════════════════════════════════════════════════════════════════════
print("\n[3] Bust event study (t-3 to t+5)...")

all_es_bust = []
for lib in LIBERTIES:
    df_es = df.dropna(subset=[lib, "bust_event_time"]).copy()
    df_es["bet_binned"] = df_es["bust_event_time"].clip(-3, 5)

    try:
        m = pf.feols(f"{lib} ~ i(bet_binned, ref=-1.0) | country_id + YEAR",
                      data=df_es, vcov={"CRV1": "country_id"})
        coefs = m.coef()
        ses = m.se()
        pvals = m.pvalue()

        for idx in coefs.index:
            t = float(idx.split("::")[-1])
            all_es_bust.append({
                "liberty": lib, "rel_time": t, "coef": coefs[idx],
                "se": ses[idx], "pvalue": pvals[idx],
                "ci_lower": coefs[idx] - 1.96 * ses[idx],
                "ci_upper": coefs[idx] + 1.96 * ses[idx],
                "phase": "bust",
            })
        # Add reference
        all_es_bust.append({"liberty": lib, "rel_time": -1, "coef": 0, "se": 0,
                             "pvalue": 1, "ci_lower": 0, "ci_upper": 0, "phase": "bust"})
        print(f"    {lib}: estimated ({len(coefs)} coefficients)")
    except Exception as e:
        print(f"    {lib}: FAILED - {e}")

# ══════════════════════════════════════════════════════════════════════════════
# 4. RECOVERY EVENT STUDY
# ══════════════════════════════════════════════════════════════════════════════
print("\n[4] Recovery event study (t-3 to t+5)...")

all_es_recovery = []
for lib in LIBERTIES:
    df_es = df.dropna(subset=[lib, "recovery_event_time"]).copy()
    df_es["ret_binned"] = df_es["recovery_event_time"].clip(-3, 5)

    try:
        m = pf.feols(f"{lib} ~ i(ret_binned, ref=-1.0) | country_id + YEAR",
                      data=df_es, vcov={"CRV1": "country_id"})
        coefs = m.coef()
        ses = m.se()
        pvals = m.pvalue()

        for idx in coefs.index:
            t = float(idx.split("::")[-1])
            all_es_recovery.append({
                "liberty": lib, "rel_time": t, "coef": coefs[idx],
                "se": ses[idx], "pvalue": pvals[idx],
                "ci_lower": coefs[idx] - 1.96 * ses[idx],
                "ci_upper": coefs[idx] + 1.96 * ses[idx],
                "phase": "recovery",
            })
        all_es_recovery.append({"liberty": lib, "rel_time": -1, "coef": 0, "se": 0,
                                 "pvalue": 1, "ci_lower": 0, "ci_upper": 0, "phase": "recovery"})
        print(f"    {lib}: estimated ({len(coefs)} coefficients)")
    except Exception as e:
        print(f"    {lib}: FAILED - {e}")

# Combine and save
all_es = pd.DataFrame(all_es_bust + all_es_recovery)
all_es.to_csv(DATA_CLEAN / "event_study_coefficients.csv", index=False)
print(f"    Saved event_study_coefficients.csv ({len(all_es)} rows)")

# ══════════════════════════════════════════════════════════════════════════════
# 5. JOINT SYMMETRY TEST
# ══════════════════════════════════════════════════════════════════════════════
print("\n[5] Joint symmetry test: H0: bust effect = -recovery effect")

symmetry_results = []
for lib in LIBERTIES:
    bust_post = all_es[(all_es["liberty"] == lib) & (all_es["phase"] == "bust") & (all_es["rel_time"] >= 0)]
    rec_post = all_es[(all_es["liberty"] == lib) & (all_es["phase"] == "recovery") & (all_es["rel_time"] >= 0)]

    if len(bust_post) > 0 and len(rec_post) > 0:
        # Average post-treatment effect for bust and recovery
        bust_avg = bust_post["coef"].mean()
        rec_avg = rec_post["coef"].mean()
        bust_se = np.sqrt(np.sum(bust_post["se"] ** 2)) / len(bust_post)
        rec_se = np.sqrt(np.sum(rec_post["se"] ** 2)) / len(rec_post)

        # Test H0: bust_avg + rec_avg = 0 (symmetry: bust = -recovery)
        diff = bust_avg + rec_avg  # should be 0 under symmetry
        diff_se = np.sqrt(bust_se ** 2 + rec_se ** 2)
        if diff_se > 0:
            z = diff / diff_se
            p_sym = 2 * (1 - stats.norm.cdf(abs(z)))
        else:
            z, p_sym = np.nan, np.nan

        ratchet = "YES" if (bust_avg < 0 and rec_avg < abs(bust_avg) * 0.5 and p_sym < 0.1) else "NO"

        print(f"    {lib}: bust_avg={bust_avg:+.4f}, rec_avg={rec_avg:+.4f}, "
              f"diff={diff:+.4f}, z={z:.3f}, p={p_sym:.4f} | Ratchet: {ratchet}")

        symmetry_results.append({
            "liberty": lib, "bust_avg": bust_avg, "recovery_avg": rec_avg,
            "asymmetry": diff, "z_stat": z, "p_symmetry": p_sym, "ratchet": ratchet,
        })

sym_df = pd.DataFrame(symmetry_results)
sym_df.to_csv(DATA_CLEAN / "symmetry_test.csv", index=False)

# ══════════════════════════════════════════════════════════════════════════════
# 6. PRE-TREND F-TEST
# ══════════════════════════════════════════════════════════════════════════════
print("\n[6] Pre-trend tests (bust event study)")
for lib in LIBERTIES:
    pre = all_es[(all_es["liberty"] == lib) & (all_es["phase"] == "bust") &
                  (all_es["rel_time"] < -1)]
    if len(pre) > 0 and pre["se"].sum() > 0:
        f_stat = np.sum((pre["coef"] / pre["se"]) ** 2) / len(pre)
        p_val = 1 - stats.f.cdf(f_stat, len(pre), 1000)
        status = "REJECT" if p_val < 0.05 else "OK"
        print(f"    {lib}: F={f_stat:.3f}, p={p_val:.4f} [{status}]")

# ══════════════════════════════════════════════════════════════════════════════
# 7. RESULTS SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
summary_lines = [
    "# Results Summary: The Ratchet Effect",
    "",
    "## TWFE Bust Effects:",
]
for r in twfe_results:
    stars = "***" if r["pvalue"] < 0.01 else "**" if r["pvalue"] < 0.05 else "*" if r["pvalue"] < 0.1 else ""
    summary_lines.append(f"- {r['liberty']}: {r['coef']:.4f}{stars} (SE={r['se']:.4f})")

summary_lines.append("\n## Symmetry Test (Ratchet):")
for _, r in sym_df.iterrows():
    summary_lines.append(
        f"- {r['liberty']}: bust={r['bust_avg']:+.4f}, recovery={r['recovery_avg']:+.4f}, "
        f"p_symmetry={r['p_symmetry']:.4f}, ratchet={r['ratchet']}"
    )

with open(DATA_CLEAN / "results_summary.md", "w", encoding="utf-8") as f:
    f.write("\n".join(summary_lines))

pd.DataFrame(twfe_results).to_csv(DATA_CLEAN / "main_results.csv", index=False)
print(f"\n    Saved results_summary.md, main_results.csv")
print("\n" + "=" * 70)
print("01_main.py completed successfully")
print("=" * 70)
