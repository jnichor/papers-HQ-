# =============================================================================
# 00_clean.py  --  Data Cleaning: ENAHO 2024 Module 400 + Sumaria
# Referee Checklist Compliant: survey weights, zero-OOP flags, cell sizes,
# weighted quintiles, head identification, chronic illness construction
# =============================================================================
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(42)

PROJECT = Path(__file__).resolve().parent.parent.parent
RAW_400 = Path("C:/Users/jesus/Documents/Enaho01A-2024-400.csv")
RAW_SUM = Path("C:/Users/jesus/Documents/Sumaria-2024.csv")
CLEAN_DIR = PROJECT / "data" / "clean"
TABLE_DIR = PROJECT / "paper" / "tables"
for d in [CLEAN_DIR, TABLE_DIR]:
    d.mkdir(parents=True, exist_ok=True)

SEP = "=" * 68
print(SEP)
print("00_clean.py -- Data Cleaning (Referee Checklist Compliant)")
print(SEP)

# -- Load Module 400 ----------------------------------------------------------
print("\n[1] Loading ENAHO 2024 Module 400...")
df = pd.read_csv(RAW_400, encoding="latin-1", low_memory=False)
print(f"  Raw: {len(df):,} individuals, {len(df.columns)} columns")

# -- Load Sumaria --------------------------------------------------------------
print("\n[2] Loading Sumaria 2024...")
df_sum = pd.read_csv(RAW_SUM, encoding="latin-1", low_memory=False)
print(f"  Sumaria: {len(df_sum):,} households")

# -- Insurance (individual level) ----------------------------------------------
print("\n[3] Insurance indicators...")
ins_cols = ["P4191", "P4192", "P4193", "P4194", "P4195", "P4196", "P4197"]
for col in ins_cols + ["P4198"]:
    df[col] = df[col].astype(str).str.strip()

df["has_sis_i"] = (df["P4191"] == "1").astype(int)  # SIS only (P4191), NOT P4195 (EPS)
df["has_essalud_i"] = (df["P4192"] == "1").astype(int)
df["has_private_i"] = ((df["P4194"] == "1") | (df["P4193"] == "1") | (df["P4195"] == "1")).astype(int)  # EPS goes here
df["uninsured_i"] = df[ins_cols].apply(lambda r: all(v == "2" for v in r), axis=1).astype(int)

print(f"  SIS (any): {df['has_sis_i'].sum():,}")
print(f"  EsSalud: {df['has_essalud_i'].sum():,}")
print(f"  Private/FFAA: {df['has_private_i'].sum():,}")
print(f"  Truly uninsured: {df['uninsured_i'].sum():,}")

# -- Demographics (individual level) ------------------------------------------
print("\n[4] Demographics...")
df["age"] = pd.to_numeric(df["P208A"], errors="coerce")
df["female"] = (df["P207"].astype(str).str.strip() == "2").astype(int)
educ_map = {"1": 0, "2": 0, "3": 3, "4": 6, "5": 11, "6": 11, "7": 14, "8": 16, "9": 18, "10": 20}
df["educ_years"] = df["P301A"].astype(str).str.strip().map(educ_map).fillna(0)

# Chronic illness
illness_cols = [c for c in df.columns if c.startswith("P401") and c not in
                ["P401", "P401C", "P401F", "P401G", "P401G1", "P401G2"]]
for c in illness_cols:
    df[c] = (df[c].astype(str).str.strip() == "1").astype(int)
df["has_chronic_i"] = (df[illness_cols].sum(axis=1) >= 1).astype(int)

# Hospitalization
df["hospitalized_i"] = (df.get("P4121", pd.Series(dtype=str)).astype(str).str.strip() == "1").astype(int)
df["child_u5_i"] = (df["age"] < 5).astype(int)
df["elderly_65_i"] = (df["age"] >= 65).astype(int)

# -- Health expenditure (individual, 4-week recall) ----------------------------
print("\n[5] Health expenditure...")
for col in ["P41601", "P41602", "P41603"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col].astype(str).str.strip(), errors="coerce").fillna(0)
    else:
        df[col] = 0
df["health_expend_i"] = df["P41601"] + df["P41602"] + df["P41603"]

# -- Aggregate to household ---------------------------------------------------
print("\n[6] Aggregating to household level...")
hh_key = ["CONGLOME", "VIVIENDA", "HOGAR"]

# Insurance (precedence: EsSalud > SIS > Private > Uninsured)
hh_ins = df.groupby(hh_key).agg(
    has_sis=("has_sis_i", "max"),
    has_essalud=("has_essalud_i", "max"),
    has_private=("has_private_i", "max"),
    all_uninsured=("uninsured_i", "min"),
).reset_index()

def assign_insurance(row):
    if row["has_essalud"] == 1: return "EsSalud"
    elif row["has_sis"] == 1: return "SIS"
    elif row["has_private"] == 1: return "Private"
    elif row["all_uninsured"] == 1: return "Uninsured"
    else: return "Other"

hh_ins["insurance_cat"] = hh_ins.apply(assign_insurance, axis=1)

# Health expenditure: annualize x13 (4-week recall)
hh_expend = df.groupby(hh_key)["health_expend_i"].sum().reset_index()
hh_expend.columns = hh_key + ["health_expend_4wk"]
hh_expend["health_expend"] = hh_expend["health_expend_4wk"] * 13
hh_expend["health_expend_x12"] = hh_expend["health_expend_4wk"] * 12  # robustness

# Head of household (CODPERSO==1)
head_mask = df["CODPERSO"] == 1
df_head = df[head_mask][hh_key + ["age", "female", "educ_years"]].copy()
df_head.columns = hh_key + ["age_head", "female_head", "educ_years"]
# Check head uniqueness
n_heads = df_head.groupby(hh_key).size()
multi_heads = (n_heads > 1).sum()
print(f"  Households with multiple heads: {multi_heads}")
df_head = df_head.drop_duplicates(subset=hh_key, keep="first")

# HH characteristics
hh_chars = df.groupby(hh_key).agg(
    hh_size=("age", "count"),
    children_u5=("child_u5_i", "sum"),
    elderly_65=("elderly_65_i", "sum"),
    chronic_any=("has_chronic_i", "max"),
    hospitalized=("hospitalized_i", "max"),
).reset_index()

# Geographic
hh_geo = df.groupby(hh_key).agg(
    UBIGEO=("UBIGEO", "first"),
    DOMINIO=("DOMINIO", "first"),
    ESTRATO=("ESTRATO", "first"),
).reset_index()

# Survey weight
hh_weight = df.groupby(hh_key)["FACTOR07"].first().reset_index()

# Merge all
df_hh = hh_ins.merge(hh_expend, on=hh_key, how="left")
df_hh = df_hh.merge(df_head, on=hh_key, how="left")
df_hh = df_hh.merge(hh_chars, on=hh_key, how="left")
df_hh = df_hh.merge(hh_geo, on=hh_key, how="left")
df_hh = df_hh.merge(hh_weight, on=hh_key, how="left")
print(f"  Households after merge: {len(df_hh):,}")

# -- Merge with Sumaria --------------------------------------------------------
print("\n[7] Merging with Sumaria...")
sum_key = hh_key + ["GASHOG2D"]
df_sum_hh = df_sum[sum_key].copy()
df_sum_hh.columns = hh_key + ["total_consumption"]

n_before = len(df_hh)
df_hh = df_hh.merge(df_sum_hh, on=hh_key, how="inner")
n_matched = len(df_hh)
n_unmatched = n_before - n_matched
print(f"  Matched: {n_matched:,} / {n_before:,} ({100*n_matched/n_before:.1f}%)")
print(f"  Unmatched (dropped): {n_unmatched:,}")

# -- OOP share construction ----------------------------------------------------
print("\n[8] Constructing OOP share...")
df_hh["total_consumption"] = pd.to_numeric(df_hh["total_consumption"], errors="coerce")
n_before = len(df_hh)
df_hh = df_hh[df_hh["total_consumption"].notna() & (df_hh["total_consumption"] > 0)].copy()
print(f"  Dropped {n_before - len(df_hh)} HH with zero/missing consumption")

# Floor at 5th percentile
cons_floor = df_hh["total_consumption"].quantile(0.05)
cons_floor = max(cons_floor, 500)
n_floored = (df_hh["total_consumption"] < cons_floor).sum()
print(f"  Consumption floor (5th pct): {cons_floor:,.0f} soles ({n_floored} HH affected)")

df_hh["health_expend"] = df_hh["health_expend"].fillna(0).clip(lower=0)
df_hh["oop_share"] = df_hh["health_expend"] / df_hh["total_consumption"].clip(lower=cons_floor)
n_capped = (df_hh["oop_share"] > 1).sum()
df_hh["oop_share"] = df_hh["oop_share"].clip(0, 1)
print(f"  Capped at 1.0: {n_capped} HH ({100*n_capped/len(df_hh):.2f}%)")

# Alternative: x12 annualization
df_hh["oop_share_x12"] = df_hh["health_expend_x12"] / df_hh["total_consumption"].clip(lower=cons_floor)
df_hh["oop_share_x12"] = df_hh["oop_share_x12"].clip(0, 1)

# -- Zero OOP flag (referee requirement) ----------------------------------------
df_hh["zero_oop"] = (df_hh["health_expend"] == 0).astype(int)
zero_rate = df_hh["zero_oop"].mean()
print(f"\n  Zero OOP households: {df_hh['zero_oop'].sum():,} ({100*zero_rate:.1f}%)")
print(f"  Zero OOP by insurance:")
for g in ["SIS", "EsSalud", "Uninsured", "Private", "Other"]:
    mask = df_hh["insurance_cat"] == g
    if mask.sum() > 0:
        zr = df_hh.loc[mask, "zero_oop"].mean()
        print(f"    {g}: {100*zr:.1f}%")

# -- CHE indicators ------------------------------------------------------------
for thresh in [10, 25, 40]:
    df_hh[f"che_{thresh}pct"] = (df_hh["oop_share"] > thresh/100).astype(int)

# -- Consumption quintiles (WEIGHTED) ------------------------------------------
print("\n[9] Weighted consumption quintiles...")
df_hh["FACTOR07"] = df_hh["FACTOR07"].fillna(1)
# Weighted quintile using cumulative weight
df_hh = df_hh.sort_values("total_consumption").reset_index(drop=True)
cum_weight = df_hh["FACTOR07"].cumsum() / df_hh["FACTOR07"].sum()
df_hh["quintile"] = pd.cut(cum_weight, bins=[0, 0.2, 0.4, 0.6, 0.8, 1.0],
                            labels=[1, 2, 3, 4, 5], include_lowest=True).astype(int)
print(f"  Quintile distribution (weighted):")
for q in [1, 2, 3, 4, 5]:
    n = (df_hh["quintile"] == q).sum()
    print(f"    Q{q}: {n:,}")

# -- Region & controls ---------------------------------------------------------
print("\n[10] Final variables...")
df_hh["department"] = df_hh["UBIGEO"].astype(str).str[:2]
df_hh["rural"] = (df_hh["ESTRATO"].astype(float) >= 6).astype(int)
df_hh["age_head"] = pd.to_numeric(df_hh["age_head"], errors="coerce").fillna(40)
df_hh["age_head_sq"] = df_hh["age_head"] ** 2
df_hh["female_head"] = df_hh["female_head"].fillna(0).astype(int)
df_hh["educ_years"] = df_hh["educ_years"].fillna(0)
df_hh["hh_size"] = df_hh["hh_size"].fillna(1)
df_hh["children_u5"] = df_hh["children_u5"].fillna(0)
df_hh["elderly_65"] = df_hh["elderly_65"].fillna(0)
df_hh["chronic_any"] = df_hh["chronic_any"].fillna(0).astype(int)
df_hh["hospitalized"] = df_hh["hospitalized"].fillna(0).astype(int)

# Insurance dummies
df_hh["ins_sis"] = (df_hh["insurance_cat"] == "SIS").astype(int)
df_hh["ins_essalud"] = (df_hh["insurance_cat"] == "EsSalud").astype(int)
df_hh["ins_uninsured"] = (df_hh["insurance_cat"] == "Uninsured").astype(int)

# -- Cell sizes (referee requirement) -------------------------------------------
print("\n[11] Cell sizes (quintile x insurance):")
cell_sizes = df_hh.groupby(["quintile", "insurance_cat"]).size().unstack(fill_value=0)
print(cell_sizes.to_string())
cell_sizes.to_csv(CLEAN_DIR / "cell_sizes.csv")

# -- Save clean data -----------------------------------------------------------
print("\n[12] Saving clean data...")
keep_cols = ["CONGLOME", "VIVIENDA", "HOGAR", "UBIGEO", "department",
             "DOMINIO", "ESTRATO", "FACTOR07",
             "insurance_cat", "ins_sis", "ins_essalud", "ins_uninsured",
             "has_sis", "has_essalud",
             "health_expend", "health_expend_x12", "total_consumption",
             "oop_share", "oop_share_x12", "zero_oop",
             "che_10pct", "che_25pct", "che_40pct", "quintile",
             "age_head", "age_head_sq", "female_head", "educ_years",
             "hh_size", "children_u5", "elderly_65", "rural",
             "chronic_any", "hospitalized"]
df_hh[keep_cols].to_csv(CLEAN_DIR / "clean_data.csv", index=False)
print(f"  Saved: {len(df_hh):,} rows, {len(keep_cols)} columns")

# -- Summary statistics (weighted) ---------------------------------------------
print("\n[13] Weighted summary statistics...")
stat_vars = ["oop_share", "health_expend", "total_consumption", "zero_oop",
             "che_10pct", "che_25pct", "che_40pct",
             "age_head", "female_head", "educ_years", "hh_size",
             "children_u5", "elderly_65", "rural", "chronic_any", "hospitalized"]

w = df_hh["FACTOR07"].values
stats_rows = []
for var in stat_vars:
    v = df_hh[var].values
    valid = np.isfinite(v)
    wv = w[valid]
    vv = v[valid]
    wmean = np.average(vv, weights=wv)
    wvar = np.average((vv - wmean)**2, weights=wv)
    stats_rows.append({
        "Variable": var, "N": int(valid.sum()),
        "Weighted_Mean": wmean, "Weighted_SD": np.sqrt(wvar),
        "Min": vv.min(), "Median": np.median(vv), "Max": vv.max()
    })
stats_df = pd.DataFrame(stats_rows)
stats_df.to_csv(CLEAN_DIR / "summary_stats.csv", index=False)

# LaTeX
tex = ["\\begin{table}[htbp]", "\\centering",
       "\\caption{Summary Statistics (Survey-Weighted)}", "\\label{tab:sumstats}", "\\small",
       "\\begin{tabular}{lrrrrrrr}", "\\toprule",
       "Variable & N & Mean & SD & Min & Median & Max \\\\", "\\midrule"]
for _, row in stats_df.iterrows():
    vname = str(row["Variable"]).replace("_", "\\_")
    tex.append(f"  {vname} & {int(row['N']):,} & {row['Weighted_Mean']:.3f} & "
               f"{row['Weighted_SD']:.3f} & {row['Min']:.3f} & {row['Median']:.3f} & {row['Max']:.3f} \\\\")
tex += ["\\bottomrule", "\\end{tabular}",
        "\\begin{minipage}{\\textwidth}\\footnotesize",
        "\\textit{Notes:} ENAHO 2024. Survey-weighted (FACTOR07). Unit: household.",
        "\\end{minipage}", "\\end{table}"]
(TABLE_DIR / "summary_stats.tex").write_text("\n".join(tex), encoding="utf-8")

# -- Balance table by insurance (weighted) -------------------------------------
print("\n[14] Weighted balance table...")
balance_vars = ["oop_share", "zero_oop", "health_expend", "age_head", "female_head",
                "educ_years", "hh_size", "children_u5", "elderly_65",
                "rural", "chronic_any", "hospitalized"]
groups = ["SIS", "EsSalud", "Uninsured"]
bal_rows = []
for var in balance_vars:
    row = {"Variable": var}
    for g in groups:
        mask = df_hh["insurance_cat"] == g
        vals = df_hh.loc[mask, var].values
        wts = df_hh.loc[mask, "FACTOR07"].values
        valid = np.isfinite(vals)
        if valid.sum() > 0:
            wmean = np.average(vals[valid], weights=wts[valid])
            wvar = np.average((vals[valid] - wmean)**2, weights=wts[valid])
            row[f"{g}_mean"] = wmean
            row[f"{g}_sd"] = np.sqrt(wvar)
            row[f"{g}_n"] = int(valid.sum())
    bal_rows.append(row)

bal_df = pd.DataFrame(bal_rows)
bal_df.to_csv(CLEAN_DIR / "balance_table.csv", index=False)

# LaTeX
tex_b = ["\\begin{table}[htbp]", "\\centering",
         "\\caption{Descriptive Statistics by Insurance Group (Survey-Weighted)}",
         "\\label{tab:balance}", "\\small",
         f"\\begin{{tabular}}{{l{'c' * len(groups) * 2}}}", "\\toprule"]
header1 = "& " + " & ".join(f"\\multicolumn{{2}}{{c}}{{{g}}}" for g in groups) + " \\\\"
header2 = "Variable & " + " & ".join(["Mean & SD"] * len(groups)) + " \\\\"
tex_b += [header1, "\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}", header2, "\\midrule"]
for _, row in bal_df.iterrows():
    vname = str(row["Variable"]).replace("_", "\\_")
    cells = []
    for g in groups:
        m = row.get(f"{g}_mean", np.nan)
        s = row.get(f"{g}_sd", np.nan)
        cells.append(f"{m:.3f} & {s:.3f}" if np.isfinite(m) else "-- & --")
    tex_b.append(f"  {vname} & " + " & ".join(cells) + " \\\\")
n_row = "  N & " + " & ".join(
    f"\\multicolumn{{2}}{{c}}{{{(df_hh['insurance_cat']==g).sum():,}}}" for g in groups
) + " \\\\"
tex_b += ["\\midrule", n_row, "\\bottomrule", "\\end{tabular}",
          "\\begin{minipage}{\\textwidth}\\footnotesize",
          "\\textit{Notes:} ENAHO 2024. Survey-weighted means (FACTOR07).",
          "\\end{minipage}", "\\end{table}"]
(TABLE_DIR / "balance_table.tex").write_text("\n".join(tex_b), encoding="utf-8")

# -- Zero OOP by quintile x insurance (referee requirement) --------------------
print("\n[15] Zero OOP rates by quintile x insurance:")
zero_table = df_hh.groupby(["quintile", "insurance_cat"])["zero_oop"].mean().unstack(fill_value=0)
print((zero_table * 100).round(1).to_string())
zero_table.to_csv(CLEAN_DIR / "zero_oop_rates.csv")

# -- Final summary -------------------------------------------------------------
print(f"\n{SEP}")
print(f"Sample: {len(df_hh):,} households")
for g in ["SIS", "EsSalud", "Uninsured", "Private", "Other"]:
    n = (df_hh["insurance_cat"] == g).sum()
    pct = 100 * n / len(df_hh)
    print(f"  {g}: {n:,} ({pct:.1f}%)")
print(f"OOP share: mean={df_hh['oop_share'].mean():.4f}, SD={df_hh['oop_share'].std():.4f}")
print(f"Zero OOP: {100*df_hh['zero_oop'].mean():.1f}%")
print(f"CHE: 10%={100*df_hh['che_10pct'].mean():.2f}%, "
      f"25%={100*df_hh['che_25pct'].mean():.2f}%, "
      f"40%={100*df_hh['che_40pct'].mean():.2f}%")
print(f"Survey weight sum: {df_hh['FACTOR07'].sum():,.0f}")
print(f"\nCLEAN_COLUMNS: {', '.join(keep_cols)}")
print(f"{SEP}\n00_clean.py complete.\n{SEP}")
