"""00_clean.py - Reshape ENAHO 500 panel + merge teleworkability index.

Input:  ENAHO Module 500 parquet (wide, 2020-2024) + teleworkability crosswalk
Output: data/clean/clean_data.csv
"""

import os
import warnings
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = r"C:\Users\jesus\Documents\enaho01a-2020-2024-500-panel.parquet"
CROSSWALK_PATH = os.path.join(PROJECT_DIR, "data", "external", "isco2_telework_complete.csv")
CLEAN_DIR = os.path.join(PROJECT_DIR, "data", "clean")
os.makedirs(CLEAN_DIR, exist_ok=True)

YEAR_SUFFIXES = ["20", "21", "22", "23", "24"]
YEAR_MAP = {"20": 2020, "21": 2021, "22": 2022, "23": 2023, "24": 2024}

print("=" * 60)
print("00_clean.py - Reshape + Teleworkability Merge")
print("=" * 60)

# == Step 1: Load selective columns from parquet ==
print("\n[1/5] Loading selective columns from parquet...")

KEY_VARS = [
    "p505r4",    # occupation ISCO-08 4-digit
    "p507",      # industry CIIU broad
    "p510",      # firm size
    "p511a",     # social security
    "p517",      # contract type
    "ocu500",    # employment status
    "p208a",     # age
    "p207",      # gender
    "dominio",   # geographic domain
    "estrato",   # urban/rural
    "facpob07",  # survey weight
    "nconglome", # PSU
    "ubigeo",    # geographic code
    "i524a1",    # labor income
    "p506r4",    # occupation detail
    "codperso",  # person code
    "hogar",     # household
    "mes",       # survey month
]

# Build column list
load_cols = ["numper", "conglome", "vivienda"]
for sfx in YEAR_SUFFIXES:
    for v in KEY_VARS:
        load_cols.append(f"{v}_{sfx}")
# Panel linkage
all_cols = pd.read_parquet(DATA_PATH, columns=None).columns.tolist()
link_cols = [c for c in all_cols if c.startswith("perpanel") or c.startswith("hpan") or c.startswith("facpanel")]
load_cols.extend(link_cols)

# Filter to existing columns
existing = set(all_cols)
load_cols = [c for c in load_cols if c in existing]
load_cols = list(set(load_cols))

df_raw = pd.read_parquet(DATA_PATH, columns=load_cols)
print(f"  Loaded: {df_raw.shape[0]:,} x {df_raw.shape[1]:,}")

# == Step 2: Reshape to long ==
print("\n[2/5] Reshaping to long format...")
frames = []
for sfx in YEAR_SUFFIXES:
    yr = YEAR_MAP[sfx]
    row = {
        "conglome": df_raw["conglome"],
        "vivienda": df_raw["vivienda"],
        "numper": df_raw["numper"],
        "year": yr,
    }
    for v in KEY_VARS:
        col = f"{v}_{sfx}"
        row[v] = df_raw[col] if col in df_raw.columns else np.nan
    frames.append(pd.DataFrame(row))

df = pd.concat(frames, ignore_index=True)
del df_raw, frames
print(f"  Long: {df.shape[0]:,} x {df.shape[1]:,}")

# == Step 3: Convert types and build variables ==
print("\n[3/5] Building variables...")

num_vars = ["ocu500", "p208a", "p207", "dominio", "estrato", "facpob07",
            "p510", "p511a", "p517", "p507", "i524a1", "numper", "mes"]
for v in num_vars:
    if v in df.columns:
        df[v] = pd.to_numeric(df[v], errors="coerce")

# Panel ID
df["pid"] = (df["conglome"].astype(str).str.strip() + "_"
             + df["vivienda"].astype(str).str.strip() + "_"
             + df["numper"].astype(str).str.strip())

# Demographics
df["female"] = (df["p207"] == 2).astype(int)
df["rural"] = (df["estrato"] >= 6).astype(int)
# Winsorize survey weights at 1st and 99th percentile to reduce extreme weight influence
raw_weight = df["facpob07"].fillna(1)
w_lo = raw_weight.quantile(0.01)
w_hi = raw_weight.quantile(0.99)
df["weight"] = raw_weight.clip(lower=w_lo, upper=w_hi)
df["weight_raw"] = raw_weight

def dominio_to_region(d):
    if d in [1, 2, 3]: return "Costa"
    elif d in [4, 5, 6]: return "Sierra"
    elif d == 7: return "Selva"
    elif d == 8: return "Lima"
    return np.nan
df["region"] = df["dominio"].apply(dominio_to_region)
df["lima"] = (df["dominio"] == 8).astype(int)

# Employment status
df["employed"] = (df["ocu500"] == 1).astype(int)

# Informality indicators (for employed workers only)
# Definition 1: No social security (p511a = 7)
df["informal_noseg"] = np.where(df["employed"] == 1, (df["p511a"] == 7).astype(int), np.nan)
# Definition 2: No written contract (p517 in {5,6} = sin contrato/locacion)
df["informal_nocontract"] = np.where(df["employed"] == 1, df["p517"].isin([5, 6]).astype(int), np.nan)
# Definition 3: Small firm (p510 in {1,2} = <5 workers)
df["informal_smallfirm"] = np.where(df["employed"] == 1, df["p510"].isin([1, 2]).astype(int), np.nan)
# Primary: no social security
df["informal"] = df["informal_noseg"]

# Firm size categories
df["large_firm"] = np.where(df["employed"] == 1, df["p510"].isin([5, 6]).astype(int), np.nan)

# PSU for clustering
df["psu"] = df["nconglome"].astype(str).str.strip() if "nconglome" in df.columns else df["conglome"].astype(str)

# == Step 4: Merge teleworkability ==
print("\n[4/5] Merging teleworkability index...")

cw = pd.read_csv(CROSSWALK_PATH, dtype={"isco_2d": str})
print(f"  Crosswalk: {len(cw)} ISCO-08 2-digit codes")

# Extract ISCO 2-digit from p505r4
df["p505r4"] = df["p505r4"].astype(str).str.strip()
df["isco_2d"] = df["p505r4"].str[:2]
df.loc[df["isco_2d"].str.len() < 2, "isco_2d"] = np.nan

df = df.merge(cw, on="isco_2d", how="left")

# Treatment indicators
df["telework_low"] = (df["telework_score"] < 0.20).astype(int)  # contact-intensive
df["telework_high"] = (df["telework_score"] >= 0.50).astype(int)

# Terciles
df["telework_tercile"] = pd.qcut(
    df["telework_score"].rank(method="first", na_option="keep"),
    q=3, labels=["low_contact", "mid_contact", "high_contact"]
)

# Match rate
employed = df[df["employed"] == 1]
matched = employed["telework_score"].notna().mean() * 100
print(f"  Match rate (employed): {matched:.1f}%")
print(f"  Telework score distribution (employed):")
print(f"    Mean: {employed['telework_score'].mean():.3f}")
print(f"    Low telework (<0.20): {(employed['telework_score'] < 0.20).mean()*100:.1f}%")
print(f"    High telework (>=0.50): {(employed['telework_score'] >= 0.50).mean()*100:.1f}%")

# == Step 5: Save ==
print("\n[5/5] Saving clean data...")

# Restrict to employed working-age (15-65)
df["working_age"] = (df["p208a"] >= 15) & (df["p208a"] <= 65)
print(f"  Working-age employed obs: {(df['working_age'] & (df['employed']==1)).sum():,}")

# Panel summary
summary = []
for y in sorted(df["year"].unique()):
    yr = df[(df["year"] == y) & (df["employed"] == 1) & df["working_age"]]
    summary.append({
        "year": int(y),
        "n_employed": len(yr),
        "n_individuals": yr["pid"].nunique(),
        "pct_informal": yr["informal"].mean() * 100 if len(yr) > 0 else np.nan,
        "pct_telework_low": yr["telework_low"].mean() * 100 if len(yr) > 0 else np.nan,
        "pct_female": yr["female"].mean() * 100 if len(yr) > 0 else np.nan,
        "pct_rural": yr["rural"].mean() * 100 if len(yr) > 0 else np.nan,
        "mean_telework": yr["telework_score"].mean() if len(yr) > 0 else np.nan,
    })
summary_df = pd.DataFrame(summary)
summary_df.to_csv(os.path.join(CLEAN_DIR, "panel_summary.csv"), index=False)
print(summary_df.to_string(index=False))

df.to_csv(os.path.join(CLEAN_DIR, "clean_data.csv"), index=False)
print(f"\n  Saved: clean_data.csv ({df.shape[0]:,} x {df.shape[1]:,})")

print("\n" + "=" * 60)
print("00_clean.py DONE")
print("=" * 60)
