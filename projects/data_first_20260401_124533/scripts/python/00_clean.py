"""00_clean.py - Merge CLD civil liberties + IMF CTOT, identify bust/recovery episodes."""

import numpy as np
import pandas as pd
from pathlib import Path
from scipy import stats

np.random.seed(42)

PROJECT = Path(r"C:\Users\jesus\Documents\paper-HQ-sin API\projects\data_first_20260401_124533")
DATA_EXT = PROJECT / "data" / "external"
DATA_CLEAN = PROJECT / "data" / "clean"
DATA_CLEAN.mkdir(parents=True, exist_ok=True)

print("=" * 70)
print("00_clean.py - Data Cleaning")
print("=" * 70)

# ══════════════════════════════════════════════════════════════════════════════
# 1. LOAD CLD (Civil Liberty Dataset)
# ══════════════════════════════════════════════════════════════════════════════
print("\n[1] Loading CLD...")
cld = pd.read_excel(DATA_EXT / "CLD_2.10.xlsx")
print(f"    CLD: {cld.shape[0]:,} rows x {cld.shape[1]} cols")
print(f"    Countries: {cld['ID'].nunique()}")
print(f"    Years: {cld['YEAR'].min()}-{cld['YEAR'].max()}")
print(f"    Columns: {list(cld.columns)}")

LIBERTIES = ["freexp", "freass", "frerel", "fremov", "fairtrial"]

# ══════════════════════════════════════════════════════════════════════════════
# 2. MISSINGNESS - CLD
# ══════════════════════════════════════════════════════════════════════════════
print("\n[2] Missingness - CLD")
print(f"    {'Variable':<20} {'% Missing':>10} {'N Missing':>10}")
print(f"    {'-'*20} {'-'*10} {'-'*10}")
for col in cld.columns:
    n_miss = cld[col].isnull().sum()
    if n_miss > 0:
        pct = n_miss / len(cld) * 100
        print(f"    {col:<20} {pct:>9.1f}% {n_miss:>10,}")
if cld.isnull().sum().sum() == 0:
    print("    No missing values in CLD")

# MCAR test
print("\n    MCAR assessment:")
any_miss = cld[LIBERTIES].isnull().any(axis=1)
n_miss = any_miss.sum()
print(f"    Rows with missing liberties: {n_miss} ({n_miss/len(cld)*100:.1f}%)")
if n_miss > 5:
    for var in LIBERTIES:
        complete = cld.loc[~any_miss, "YEAR"]
        incomplete = cld.loc[any_miss, "YEAR"]
        if len(complete) > 2 and len(incomplete) > 2:
            t, p = stats.ttest_ind(complete, incomplete, equal_var=False)
            flag = " ***" if p < 0.05 else ""
            print(f"    YEAR: mean(complete)={complete.mean():.0f}, mean(miss)={incomplete.mean():.0f}, p={p:.3f}{flag}")
            break
else:
    print("    Insufficient missing for MCAR test — data is complete")

# ══════════════════════════════════════════════════════════════════════════════
# 3. LOAD CTOT (Commodity Terms of Trade)
# ══════════════════════════════════════════════════════════════════════════════
print("\n[3] Loading CTOT...")
ctot_raw = pd.read_csv(DATA_EXT / "dataset_2026-04-01T18_13_32.219913504Z_DEFAULT_INTEGRATION_IMF.RES_CTOT_5.0.1.csv",
                        low_memory=False)
print(f"    CTOT raw: {ctot_raw.shape[0]:,} rows x {ctot_raw.shape[1]} cols")

# Filter to annual net export CTOT index (GDP-weighted)
# SERIES_CODE format: ISO3.INDICATOR_CODE.other.A (A=annual)
ctot_filtered = ctot_raw[
    ctot_raw["SERIES_CODE"].str.contains("CNEPI_CTOT_GDP", na=False) &
    ctot_raw["SERIES_CODE"].str.endswith(".A", na=False)
].copy()

if len(ctot_filtered) == 0:
    # Try alternative indicator
    print("    [warn] CNEPI_CTOT_GDP not found, trying CEPI_CTOTX_GDP...")
    ctot_filtered = ctot_raw[
        ctot_raw["SERIES_CODE"].str.contains("CEPI_CTOTX_GDP", na=False) &
        ctot_raw["SERIES_CODE"].str.endswith(".A", na=False)
    ].copy()

if len(ctot_filtered) == 0:
    # Fallback: use any annual CTOT series
    print("    [warn] Specific series not found, using first annual series per country...")
    ctot_filtered = ctot_raw[
        ctot_raw["FREQUENCY"].str.upper().eq("A") if "FREQUENCY" in ctot_raw.columns
        else ctot_raw["SERIES_CODE"].str.endswith(".A", na=False)
    ].copy()
    # Keep only one series per country
    ctot_filtered = ctot_filtered.drop_duplicates(subset=["COUNTRY"], keep="first")

print(f"    CTOT filtered: {len(ctot_filtered):,} rows (one per country)")

# Extract ISO3 from SERIES_CODE (first 3 chars)
ctot_filtered["iso3"] = ctot_filtered["SERIES_CODE"].str[:3]

# Reshape: extract annual columns (4-digit year columns)
year_cols = [c for c in ctot_filtered.columns if len(c) == 4 and c.isdigit()]
print(f"    Year columns found: {len(year_cols)} ({year_cols[0]}-{year_cols[-1]})")

ctot_long = ctot_filtered.melt(
    id_vars=["iso3", "COUNTRY"],
    value_vars=year_cols,
    var_name="year",
    value_name="ctot_index",
)
ctot_long["year"] = ctot_long["year"].astype(int)
ctot_long["ctot_index"] = pd.to_numeric(ctot_long["ctot_index"], errors="coerce")
ctot_long = ctot_long.dropna(subset=["ctot_index"])
print(f"    CTOT long: {len(ctot_long):,} rows, {ctot_long['iso3'].nunique()} countries")

# ══════════════════════════════════════════════════════════════════════════════
# 4. MERGE CLD + CTOT
# ══════════════════════════════════════════════════════════════════════════════
print("\n[4] Merging CLD + CTOT...")

# CLD uses 'ID' as ISO3 code
merged = cld.merge(
    ctot_long[["iso3", "year", "ctot_index"]],
    left_on=["ID", "YEAR"],
    right_on=["iso3", "year"],
    how="inner",
)
merged = merged.drop(columns=["iso3", "year"])
print(f"    Merged: {len(merged):,} rows, {merged['ID'].nunique()} countries")
print(f"    Years: {merged['YEAR'].min()}-{merged['YEAR'].max()}")
n_lost = len(cld) - len(merged)
print(f"    Lost in merge: {n_lost:,} rows (countries without CTOT data)")

# ══════════════════════════════════════════════════════════════════════════════
# 5. IDENTIFY BUST AND RECOVERY EPISODES
# ══════════════════════════════════════════════════════════════════════════════
print("\n[5] Identifying bust/recovery episodes...")

# Compute 3-year cumulative CTOT change
merged = merged.sort_values(["ID", "YEAR"])
merged["ctot_pct_change"] = merged.groupby("ID")["ctot_index"].pct_change() * 100
merged["ctot_cum3"] = merged.groupby("ID")["ctot_pct_change"].transform(
    lambda x: x.rolling(3, min_periods=1).sum()
)

# Bust: cumulative 3-year decline >= 20%
BUST_THRESHOLD = -20
merged["bust"] = (merged["ctot_cum3"] <= BUST_THRESHOLD).astype(int)

# Bust onset: first year of each bust episode
merged["bust_onset"] = 0
for country in merged["ID"].unique():
    mask = merged["ID"] == country
    country_data = merged.loc[mask, "bust"].values
    onset = np.zeros_like(country_data)
    in_bust = False
    for i in range(len(country_data)):
        if country_data[i] == 1 and not in_bust:
            onset[i] = 1
            in_bust = True
        elif country_data[i] == 0:
            in_bust = False
    merged.loc[mask, "bust_onset"] = onset

# Recovery: cumulative 3-year increase >= 20% after a bust
RECOVERY_THRESHOLD = 20
merged["recovery"] = (merged["ctot_cum3"] >= RECOVERY_THRESHOLD).astype(int)

# Recovery onset after bust
merged["recovery_onset"] = 0
for country in merged["ID"].unique():
    mask = merged["ID"] == country
    cd = merged.loc[mask].copy()
    had_bust = False
    onsets = np.zeros(len(cd))
    for i, (_, row) in enumerate(cd.iterrows()):
        if row["bust_onset"] == 1:
            had_bust = True
        if had_bust and row["recovery"] == 1:
            onsets[i] = 1
            had_bust = False  # reset after recovery
    merged.loc[mask, "recovery_onset"] = onsets

n_busts = merged["bust_onset"].sum()
n_recoveries = merged["recovery_onset"].sum()
print(f"    Bust episodes: {n_busts}")
print(f"    Recovery episodes: {n_recoveries}")

# Event time relative to bust onset
merged["bust_event_time"] = np.nan
for country in merged["ID"].unique():
    mask = merged["ID"] == country
    cd = merged.loc[mask]
    onset_years = cd.loc[cd["bust_onset"] == 1, "YEAR"].values
    if len(onset_years) > 0:
        # Use first bust onset
        t0 = onset_years[0]
        merged.loc[mask, "bust_event_time"] = cd["YEAR"] - t0

# Event time relative to recovery onset
merged["recovery_event_time"] = np.nan
for country in merged["ID"].unique():
    mask = merged["ID"] == country
    cd = merged.loc[mask]
    onset_years = cd.loc[cd["recovery_onset"] == 1, "YEAR"].values
    if len(onset_years) > 0:
        t0 = onset_years[0]
        merged.loc[mask, "recovery_event_time"] = cd["YEAR"] - t0

# Country numeric ID
merged["country_id"] = pd.Categorical(merged["ID"]).codes

# ══════════════════════════════════════════════════════════════════════════════
# 6. SAVE
# ══════════════════════════════════════════════════════════════════════════════
print("\n[6] Saving clean_data.csv...")
merged.to_csv(DATA_CLEAN / "clean_data.csv", index=False)
print(f"    Saved: {merged.shape[0]:,} rows x {merged.shape[1]} cols")

# Summary stats
print("\n[7] Summary statistics")
print(f"    Countries: {merged['ID'].nunique()}")
print(f"    Years: {merged['YEAR'].min()}-{merged['YEAR'].max()}")
print(f"    Bust episodes: {n_busts}")
print(f"    Recovery episodes: {n_recoveries}")
for lib in LIBERTIES:
    s = merged[lib].dropna()
    print(f"    {lib}: mean={s.mean():.2f}, sd={s.std():.2f}, min={s.min()}, max={s.max()}")

summary = merged[LIBERTIES + ["ctot_index", "ctot_pct_change"]].describe().T
summary.to_csv(DATA_CLEAN / "summary_stats.csv")
print(f"\n    Saved summary_stats.csv")

# Missing data strategy
print("\n    Missing data strategy: LISTWISE DELETION per regression")
print("    Justification: CLD has no missing values. CTOT missingness is")
print("    structural (country not in commodity exporter sample). Countries")
print("    without CTOT data are excluded from analysis by construction.")
print("    This is sample restriction, not imputation choice.")

print("\n" + "=" * 70)
print("00_clean.py completed successfully")
print("=" * 70)
