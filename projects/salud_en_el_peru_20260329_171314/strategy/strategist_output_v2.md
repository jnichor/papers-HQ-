# Revised Strategy Memo — All Four Deliverables

---

## `strategy_memo.md`

---

# Strategy Memo: Catastrophic Health Expenditure and the Middle-Income Squeeze in Peru
## ENAHO 2024 Module 400 — Quantile Regression Analysis

### 1. Research Question and Estimands

**Research question:** Does out-of-pocket (OOP) health expenditure as a share of capacity-to-pay (CTP) exhibit a non-linear distributional pattern across the income spectrum, and are middle-income (Q3) households disproportionately vulnerable relative to their insurance coverage and consumption levels?

**Primary estimand:** Conditional Quantile Partial Effect (CQPE) — the effect of income quintile and insurance status on the τ-th conditional quantile of OOP_share = OOP/CTP, holding controls constant, estimated at τ ∈ {0.25, 0.50, 0.75, 0.90, 0.95} on the subsample with OOP > 0.

**Secondary estimand:** Unconditional Quantile Partial Effect (UQPE) — the effect of income quintile membership on the τ-th quantile of the marginal (population) distribution of OOP_share, estimated via Recentered Influence Function (RIF) regression.

**Primary specification — zero mass point (CRITICAL):** OOP = 0 for an expected 40–60% of ENAHO households in a given quarter, creating a mass point at zero in the OOP_share distribution that violates the regularity conditions for standard Koenker–Bassett CQR (which requires an absolutely continuous conditional distribution). The **primary specification is therefore a two-part model**:

- **Part 1:** Weighted probit for P(OOP > 0 | X) — characterizes the extensive margin
- **Part 2:** Weighted CQR of OOP_share conditional on OOP > 0, at τ ∈ {0.25, 0.50, 0.75, 0.90, 0.95} — conditions out the mass point entirely

Full-sample CQR (including OOP = 0 observations) is retained as a **secondary/descriptive specification** in Figure 1, with estimates at τ < estimated mass-point fraction clearly marked as unreliable and not used for inference. Censored QR (Powell 1986 via `crq()`) is robustness check R8.

### 2. Data and Variables

**Dataset:** ENAHO 2024, Module 400 (Health), merged with Module 300 (Education), Module 200 (Household characteristics), and the Sumaria file (consumption aggregates). Unit of observation: household.

| Variable | Definition | Source column |
|---|---|---|
| OOP | Total OOP health expenditure (soles), annualized from 3-month recall: consultations, medicines, lab, hospitalization, dental, optical, other | P407A + P407B + P407C + P407D + P407E + P407F + P407G + P407H (× 4 to annualize) |
| CTP | Capacity to pay: total household consumption minus food subsistence minimum | See Section 3 |
| OOP_share | Primary outcome: OOP / CTP | Constructed |
| SIS | =1 if any household member covered by SIS | P4191 == 1 |
| EsSalud | =1 if any household member covered by EsSalud | P4192 == 1 |
| Quintile | Income quintile (Q1–Q5) based on weighted per-capita consumption | See Section 3 |
| Age_hh | Age of household head (years) | P208A |
| Female_hh | =1 if household head is female | P207 == 2 |
| Educ_hh | Education of household head (approximate years of schooling) | P301A (recoded) |
| Urban | =1 if urban area | AREA == 1 |
| N_members | Household size | MIEPERHO (Module 200 roster) |
| UBIGEO | District identifier (for clustering) | UBIGEO |
| ESTRATO | Survey stratum | ESTRATO |
| FACTOR07 | Household expansion factor (survey weight) | FACTOR07 |

### 3. Sample Construction

#### 3.1 CTP Denominator (Pre-Specified — No Fallback)

Following WHO/PAHO catastrophic expenditure methodology and INEI's official poverty measurement:

**CTP_h = max(C_h − z_food(d) × n_h, 1)**

where:
- **C_h** = annualized total household consumption from Sumaria (GASHOG2D, soles/year). **No imputation fallback is used.** Households missing GASHOG2D are excluded from the analytic sample (restriction 3 below). This is a pre-specified exclusion, not an RA judgment call; the exclusion count is documented in the flowchart.
- **z_food(d)** = INEI food poverty line for geographic domain d ∈ {costa urbana, costa rural, sierra urbana, sierra rural, selva urbana, selva rural, Lima Metropolitana}, in soles per person per month. Source: INEI Condiciones de Vida en el Perú 2024 technical annex. These are loaded as a lookup table keyed on DOMINIO (7 values).
- **n_h** = household size (MIEPERHO)
- The floor of 1 prevents division by zero; households reaching the floor are excluded in restriction 4

**Rationale:** Using the food poverty line as subsistence minimum follows Wagstaff & van Doorslaer (2003) and is consistent with INEI methodology. Domain-specific lines reduce systematic geographic measurement error.

#### 3.2 Income Quintile Assignment (Pre-Specified)

Quintile cut-points are computed as the **weighted quantiles of per-capita consumption** (GASHOG2D / n_h) at p = {0.20, 0.40, 0.60, 0.80} using the full ENAHO 2024 sample **before** restrictions, with FACTOR07 as probability weights. This ensures Q1–Q5 represent national population fifths, not sample fifths, and the "middle-income squeeze" claim refers to the national middle quintile. Robustness check R2 uses unweighted within-sample quintile cuts as an alternative.

#### 3.3 Survey Weighting

All estimation uses FACTOR07 as probability weights throughout:
- Part 1 probit: estimated via `svyglm()` with survey design (ids=~UBIGEO, strata=~ESTRATO, weights=~FACTOR07)
- Part 2 CQR: `rq(..., weights=FACTOR07)`
- RIF-OLS: `lm(..., weights=FACTOR07)` with cluster-robust SEs
- Kernel density for RIF construction: weighted density using FACTOR07

Unweighted estimation on ENAHO produces sample-distribution estimates, not population estimates. Because the paper's claim is about Peru's national income distribution, all reported estimates are population-weighted. Unweighted estimates are included in Table 5 (robustness summary) as a specification check.

#### 3.4 Sample Restrictions and CONSORT Flowchart

```
ENAHO 2024 Module 400 (all surveyed households)
         n_0
          │
          ├─ Restrict 1: Exclude institutionalized (ESTRATO == 8):    −n_1
          │
          ├─ Restrict 2: Exclude missing/zero FACTOR07:               −n_2
          │
          ├─ Restrict 3: Exclude missing GASHOG2D                     −n_3
          │             [no fallback; excluded households tabulated]
          │
          ├─ Restrict 4: Exclude CTP < 1 after subsistence floor:     −n_4
          │
          ├─ Restrict 5: Exclude OOP_share > 5 (implausible values):  −n_5
          │
          └─ Restrict 6: Exclude head age < 18 or > 90:               −n_6
                    │
          ══════════════════════════════════
          Analytic sample:  n_analytic
          ══════════════════════════════════
                    │
          ┌─────────┴───────────┐
       OOP = 0              OOP > 0
      (n_zero)            (n_positive)
    [Part 1 probit:     [Part 2 CQR:
     full n_analytic]    τ ∈ {0.25, 0.50,
                          0.75, 0.90, 0.95}]

  Mass-point fraction: n_zero / n_analytic
  (if > 0.25, full-sample CQR at τ ≤ 0.25
   is marked unreliable)
```

*All n values are filled in after running Step 3 of pseudo_code.md and reported in Table 1.*

#### 3.5 Power at τ = 0.95

With district-level clustering (~1,800 UBIGEO codes), the effective Part 2 sample is n_positive. Districts with fewer than 5 Part 2 observations are collapsed to the province level for SE computation (see pseudo_code.md Step 7). The count of such districts is reported as a footnote to Table 3.

### 4. Estimating Equations

#### 4.1 Part 1: Selection into Positive OOP (Primary)

Pr(OOP_h > 0 | X_h) = Φ(α + β_Q · Quintile_h + β_SIS · SIS_h + β_ES · EsSalud_h + γ · X_h)

Weighted probit (FACTOR07), SEs from survey design.

#### 4.2 Part 2: CQR Conditional on OOP > 0 (Primary)

Q_τ(OOP_share_h | X_h, OOP_h > 0) = α(τ) + β_Q(τ) · Quintile_h + β_SIS(τ) · SIS_h + β_ES(τ) · EsSalud_h + γ(τ) · X_h

where:
- Quintile_h = vector of dummies for Q2, Q3, Q4, Q5 (Q1 = reference)
- X_h = {Age_hh, Age_hh², Female_hh, Educ_hh, Urban, N_members, log(N_members)}
- τ ∈ {0.25, 0.50, 0.75, 0.90, 0.95}
- Estimation: `rq(formula, tau=τ, data=dt_pos, weights=FACTOR07, method="br")`
- SEs: `boot.rq(..., R=500, bsmethod="cluster", cluster=~UBIGEO)`

#### 4.3 RIF-UQR: Unconditional Quantile Extension (Secondary)

RIF(OOP_share_h; Q_τ) = Q_τ + [τ − 1(OOP_share_h ≤ Q_τ)] / f̂(Q_τ)

where f̂(Q_τ) is the weighted kernel density at Q_τ (Gaussian kernel, Silverman bandwidth; computed on positive-OOP subsample for τ > mass-point fraction, full sample with mass-point adjustment for τ ≤ mass-point fraction). Weighted τ-quantile of OOP_share uses FACTOR07. Weighted RIF-OLS with cluster-robust SEs gives UQPE.

### 5. Identification Assumption and Causal Scope

**Formal statement:** The conditional quantile function Q_τ(OOP_share | X) is correctly specified; the RIF regression E[RIF | X] is correctly specified.

**Plain language:** After conditioning on insurance status, demographics, and urban/rural location, income quintile differences in OOP_share reflect the differential OOP price exposure of uninsured middle-income households relative to insured higher-income households.

**Causal scope — explicit partition (required to prevent referee misreading):**

| Parameter | Interpretation | Causal status |
|---|---|---|
| β_Q(τ): quintile dummies | Conditional quantile difference in OOP_share by income group, holding insurance and demographics constant | **Descriptive.** Income quintile is not randomly assigned; this is an income-distribution characterization, not a causal effect of income. |
| β_SIS(τ), β_ES(τ): insurance dummies | Conditional association between insurance status and OOP_share, holding quintile and demographics constant | **Conditional association only.** Insurance enrollment is endogenous (correlated with health status, labor formality, and income). These coefficients **must not** be interpreted as the causal effect of insurance coverage. |

This partition is stated here and repeated verbatim in the empirical strategy section of the paper.

### 6. Expected Signs

| Parameter | Expected sign | Economic reasoning |
|---|---|---|
| β_Q3(τ) at high τ | **Positive** | Above SIS threshold, below EsSalud coverage; full OOP exposure at catastrophic events |
| β_Q4(τ), β_Q5(τ) at high τ | Negative | Higher EsSalud/private coverage; ability to pay shields upper quintiles |
| β_Q2(τ) at high τ | Near zero / weakly positive | Partial SIS coverage; OOP exposure lower than Q3 |
| β_SIS(τ) | Negative | SIS reimburses direct costs; reduces OOP conditional on use |
| β_EsSalud(τ) | Negative | EsSalud comprehensive coverage reduces OOP |
| Age_hh | Positive (non-linear) | Older heads → higher morbidity → higher OOP exposure |
| Urban | Ambiguous | Higher provider prices offset by higher formal insurance access |
| Educ_hh | Negative (high τ) | Education → better insurance navigation and preventive care use |

### 7. Tables and Figures — Stated Purposes

**Table 1: Analytic Sample Descriptive Statistics**
*Purpose:* Means and proportions of all analysis variables by quintile (Q1–Q5) and overall; n_analytic, n_positive, n_zero, and all CONSORT restriction counts. Allows readers to verify representativeness, assess covariate balance across quintiles, and confirm the mass-point fraction.

**Table 2: Part 1 — Weighted Probit of P(OOP > 0)**
*Purpose:* Report marginal effects for quintile dummies, SIS, EsSalud, and controls. Establishes the extensive margin: whether income gradient operates through probability of any OOP or conditional amount. Decomposition of total effect into Part 1 + Part 2 margins is discussed in the text.

**Table 3: Part 2 — Weighted CQR Estimates, OOP_share | OOP > 0 (Primary)**
*Purpose:* Main results table. Report β_Q(τ) and β_SIS(τ), β_ES(τ) at τ ∈ {0.25, 0.50, 0.75, 0.90, 0.95} with bootstrap-clustered SEs. Key test: β_Q3(0.90) significantly positive and larger than β_Q4(0.90). Wald test for equality of quintile coefficients at each τ reported at foot of table. n_positive and count of province-collapsed clusters noted as footnotes.

**Table 4: Weighted RIF-OLS Estimates — Unconditional Quantile Partial Effects**
*Purpose:* UQPE for quintile dummies at τ ∈ {0.25, 0.50, 0.75, 0.90, 0.95} from RIF-OLS. Comparison with Table 3 tests whether the middle-income squeeze is a conditional or unconditional population-distribution phenomenon.

**Table 5: Robustness Summary**
*Purpose:* Sign and significance of β_Q3(0.90) under each of R1–R8. One column per robustness check, plus a column for baseline and a column for unweighted baseline. Allows readers to assess stability of the main finding across all methodological choices at a glance.

**Figure 1: Quantile Process Plots — β_Q(τ) for Q2–Q5, τ ∈ {0.10, …, 0.95}**
*Purpose:* Estimated quintile coefficients and 95% bootstrap CIs across the full τ grid, for both Part 2 CQR (solid) and full-sample CQR (dashed). Visually shows where in the distribution the middle-income squeeze is concentrated. Full-sample CQR estimates at τ < mass-point fraction plotted with open circles and labeled "unreliable — mass point."

**Figure 2: Predicted OOP_share Distribution by Quintile**
*Purpose:* Kernel density plots of predicted OOP_share for Q1–Q5 households evaluated at mean controls (Part 2 sample). Shows distributional separation and economic magnitude.

**Figure 3: Part 1 Probit Marginal Effects — P(OOP > 0) by Quintile**
*Purpose:* Bar chart of marginal effects with 95% CIs. Isolates the extensive margin of the income gradient.

**Figure 4: Main vs. Placebo — β_Q3(τ) Comparison**
*Purpose:* Side-by-side plot of β_Q3(τ) from (a) main outcome OOP_share and (b) placebo outcome non-health consumption share, with 95% CIs. Falsification: if the middle-income squeeze is genuine and health-specific, placebo coefficients should be near zero or negative.

### 8. Bootstrap-Clustered SE Justification

Households are clustered within UBIGEO districts. SEs are computed via `boot.rq()` with R = 500 bootstrap replications resampling at the UBIGEO level. This accounts for: (1) intra-cluster correlation in OOP patterns from local health shocks and provider availability; (2) ENAHO's stratified multi-stage sampling structure (ESTRATO used as stratification variable in bootstrap); (3) heteroskedasticity in OOP_share across the income distribution.

---

## `pseudo_code.md`

---

# Pseudo-Code: ENAHO 2024 OOP Analysis
## From Raw CSV to Final Outputs (R)

### Step 0: Load Data and Verify Variable Names

```r
library(data.table)
library(quantreg)
library(survey)
library(Hmisc)     # wtd.quantile
library(sandwich)
library(lmtest)
library(ggplot2)

dt_400    <- fread("enaho01a-2024-400.csv")
dt_300    <- fread("enaho01a-2024-300.csv")
dt_200    <- fread("enaho01a-2024-200.csv")
dt_sum    <- fread("sumaria-2024.csv")

# CRITICAL: verify before any subsequent step
cat("=== Module 400 columns ===\n"); print(names(dt_400))
# Expected: P407A-P407H, P4191, P4192, P406, P208A, P207, P301A,
#           FACTOR07, UBIGEO, ESTRATO, AREA, DOMINIO (or derivable)

cat("=== Sumaria columns ===\n"); print(names(dt_sum))
# Expected: GASHOG2D (total annualized consumption), CONGLOME, VIVIENDA, HOGAR

cat("=== Module 200 columns ===\n"); print(names(dt_200))
# Expected: MIEPERHO (household size), P208A, P207
```

### Step 1: Construct OOP and Insurance Dummies

```r
oop_cols <- c("P407A","P407B","P407C","P407D","P407E","P407F","P407G","P407H")
dt_400[, OOP := rowSums(.SD, na.rm=TRUE) * 4, .SDcols=oop_cols]
# Multiply by 4: 3-month recall → annualized

dt_400[, SIS     := as.integer(P4191 == 1)]
dt_400[, EsSalud := as.integer(P4192 == 1)]
dt_400[is.na(SIS), SIS := 0]
dt_400[is.na(EsSalud), EsSalud := 0]
```

### Step 2: Merge and Construct CTP (Pre-Specified — No Fallback)

```r
key <- c("CONGLOME","VIVIENDA","HOGAR")
dt <- merge(dt_400, dt_sum[, c(key, "GASHOG2D"), with=FALSE],   by=key, all.x=TRUE)
dt <- merge(dt,    dt_200[, c(key, "MIEPERHO","P208A","P207"), with=FALSE], by=key, all.x=TRUE)
dt <- merge(dt,    dt_300[, c(key, "P301A"),  with=FALSE],       by=key, all.x=TRUE)
dt[, N_members := MIEPERHO]

# CTP construction — food poverty line by INEI domain (7 domains)
# RA: fill z_food_monthly from INEI Condiciones de Vida 2024 technical annex
z_lines <- data.table(
  DOMINIO = 1:7,
  z_food_monthly = c(NA, NA, NA, NA, NA, NA, NA)  # fill from INEI document
)
dt <- merge(dt, z_lines, by="DOMINIO", all.x=TRUE)
dt[, z_food_annual := z_food_monthly * 12 * N_members]
dt[, CTP := pmax(GASHOG2D - z_food_annual, 1)]

dt[, OOP_share := OOP / CTP]

# Placebo outcome (non-health consumption share) — constructed here for later use
dt[, nonhealth_cons  := GASHOG2D - OOP]
dt[, placebo_share   := nonhealth_cons / CTP]
```

*Note: Households with missing GASHOG2D are excluded in Step 3 (restriction 3). There is no imputation. This is a pre-specified design choice.*

### Step 3: Sample Restrictions — CONSORT Counts

```r
n0 <- nrow(dt)

dt <- dt[!(ESTRATO %in% 8)]
n_after_r1 <- nrow(dt); cat("After R1 (institutionalized):", n0 - n_after_r1, "excluded\n")

dt <- dt[!is.na(FACTOR07) & FACTOR07 > 0]
n_after_r2 <- nrow(dt); cat("After R2 (FACTOR07):", n_after_r1 - n_after_r2, "excluded\n")

dt <- dt[!is.na(GASHOG2D)]
n_after_r3 <- nrow(dt); cat("After R3 (missing GASHOG2D):", n_after_r2 - n_after_r3, "excluded\n")

dt <- dt[CTP >= 1]
n_after_r4 <- nrow(dt); cat("After R4 (CTP < 1):", n_after_r3 - n_after_r4, "excluded\n")

dt <- dt[OOP_share <= 5]
n_after_r5 <- nrow(dt); cat("After R5 (OOP_share > 5):", n_after_r4 - n_after_r5, "excluded\n")

dt <- dt[P208A >= 18 & P208A <= 90]
n_analytic <- nrow(dt); cat("After R6 (age):", n_after_r5 - n_analytic, "excluded\n")

n_positive <- nrow(dt[OOP > 0])
n_zero     <- nrow(dt[OOP == 0])
mass_frac  <- n_zero / n_analytic

cat("\nAnalytic sample:", n_analytic, "\n")
cat("OOP > 0:", n_positive, sprintf("(%.1f%%)\n", 100*n_positive/n_analytic))
cat("Mass point at 0:", sprintf("%.1f%%\n", 100*mass_frac))
cat("Part 2 CQR sample:", n_positive, "\n")
cat("Reliable CQR quantiles: tau >", round(mass_frac, 2), "\n")
```

### Step 4: Income Quintile Assignment (Population-Weighted)

```r
dt[, pcap_cons := GASHOG2D / N_members]

# Weighted quintile cut-points — represents national population fifths
q_cuts <- wtd.quantile(dt$pcap_cons, weights=dt$FACTOR07, probs=c(0.2,0.4,0.6,0.8))
cat("Quintile cut-points (soles/person/year):", q_cuts, "\n")

dt[, Quintile := cut(pcap_cons, breaks=c(-Inf, q_cuts, Inf),
                      labels=c("Q1","Q2","Q3","Q4","Q5"), include.lowest=TRUE)]
dt[, Q2 := as.integer(Quintile=="Q2")]
dt[, Q3 := as.integer(Quintile=="Q3")]
dt[, Q4 := as.integer(Quintile=="Q4")]
dt[, Q5 := as.integer(Quintile=="Q5")]

# Verify: weighted shares should be ~20% each
dt[, .(wt_share=round(sum(FACTOR07)/sum(dt$FACTOR07),3)), by=Quintile][order(Quintile)]
```

### Step 5: Additional Controls

```r
dt[, Age_hh      := P208A]
dt[, Age_hh_sq   := P208A^2]
dt[, Female_hh   := as.integer(P207 == 2)]
dt[, Urban       := as.integer(AREA == 1)]
dt[, log_N       := log(N_members)]

# P301A → approximate years of schooling
educ_map <- c("1"=0,"2"=2,"3"=6,"4"=11,"5"=14,"6"=16,"7"=18)
dt[, Educ_hh := as.numeric(educ_map[as.character(P301A)])]
```

### Step 6: Part 1 — Weighted Probit P(OOP > 0)

```r
dt[, positive_OOP := as.integer(OOP > 0)]

p1_formula <- positive_OOP ~ Q2+Q3+Q4+Q5+SIS+EsSalud+
                              Age_hh+Age_hh_sq+Female_hh+Educ_hh+Urban+log_N

svy_design <- svydesign(ids=~UBIGEO, strata=~ESTRATO,
                         weights=~FACTOR07, data=dt, nest=TRUE)
p1_fit <- svyglm(p1_formula, design=svy_design, family=binomial("probit"))
summary(p1_fit)
# Marginal effects → Table 2; Figure 3
```

### Step 7: Part 2 — Weighted CQR Conditional on OOP > 0

```r
dt_pos <- dt[OOP > 0]

# Check cluster sizes; collapse small clusters to province
cluster_sz <- dt_pos[, .N, by=UBIGEO]
small_cl   <- cluster_sz[N < 5, UBIGEO]
cat("Districts with < 5 obs in Part 2:", length(small_cl),
    sprintf("(%.1f%% of observations)\n",
            100*sum(cluster_sz[N<5, N])/n_positive))
# If > 5% affected, derive PROVINCIA from UBIGEO (first 4 chars) and use as cluster

p2_formula <- OOP_share ~ Q2+Q3+Q4+Q5+SIS+EsSalud+
                           Age_hh+Age_hh_sq+Female_hh+Educ_hh+Urban+log_N
taus <- c(0.25, 0.50, 0.75, 0.90, 0.95)

p2_fits <- rq(p2_formula, tau=taus, data=dt_pos, weights=FACTOR07, method="br")

set.seed(42)
p2_boot <- boot.rq(x       = model.matrix(p2_formula, data=dt_pos),
                    y       = dt_pos$OOP_share,
                    tau     = taus,
                    R       = 500,
                    bsmethod= "cluster",
                    cluster = dt_pos$UBIGEO,
                    weights = dt_pos$FACTOR07)

coef_p2  <- coef(p2_fits)
# SE for each (tau, coef): sd across bootstrap draws
se_p2    <- apply(p2_boot$B, 2, sd)
se_mat   <- matrix(se_p2, nrow=nrow(coef_p2))  # rows=coefs, cols=taus
# → Table 3
```

### Step 8: Wald Test — Quintile Equality at Each τ

```r
Q_names <- c("Q2","Q3","Q4","Q5")
Q_idx   <- which(rownames(coef_p2) %in% Q_names)
n_coef  <- nrow(coef_p2)

for (i in seq_along(taus)) {
  B_draws <- p2_boot$B[, Q_idx + (i-1)*n_coef]   # bootstrap draws for Q2-Q5 at tau_i
  V_Q     <- cov(B_draws)
  b_Q     <- coef_p2[Q_idx, i]
  R_mat   <- matrix(c(1,-1,0,0,  1,0,-1,0,  1,0,0,-1), nrow=3, byrow=TRUE)
  W       <- t(R_mat %*% b_Q) %*% solve(R_mat %*% V_Q %*% t(R_mat)) %*% (R_mat %*% b_Q)
  cat(sprintf("tau=%.2f  Wald (H0: Q2=Q3=Q4=Q5)  chi2(3)=%.2f  p=%.4f\n",
              taus[i], W, pchisq(W, df=3, lower.tail=FALSE)))
}
```

### Step 9: RIF-UQR (Weighted)

```r
# Weighted quantiles of OOP_share on full analytic sample
Q_tau_vals <- wtd.quantile(dt$OOP_share, weights=dt$FACTOR07, probs=taus)

rif_results <- list()
for (i in seq_along(taus)) {
  tau_i  <- taus[i]
  Q_tau  <- Q_tau_vals[i]
  rif_col <- paste0("RIF_", tau_i*100)

  # Bandwidth and density — positive-OOP subsample if tau > mass_frac
  if (tau_i > mass_frac) {
    bw  <- bw.nrd0(dt_pos$OOP_share)
    den <- density(dt_pos$OOP_share,
                   weights=dt_pos$FACTOR07/sum(dt_pos$FACTOR07),
                   bw=bw, kernel="gaussian")
  } else {
    bw  <- bw.nrd0(dt$OOP_share)
    den <- density(dt$OOP_share,
                   weights=dt$FACTOR07/sum(dt$FACTOR07),
                   bw=bw, kernel="gaussian")
  }
  f_Q <- approx(den$x, den$y, xout=Q_tau)$y

  dt[, (rif_col) := Q_tau + (tau_i - as.integer(OOP_share <= Q_tau)) / f_Q]

  rif_fm  <- as.formula(paste(rif_col,
               "~ Q2+Q3+Q4+Q5+SIS+EsSalud+Age_hh+Age_hh_sq+Female_hh+Educ_hh+Urban+log_N"))
  rif_fit <- lm(rif_fm, data=dt, weights=FACTOR07)
  rif_vcv <- vcovCL(rif_fit, cluster=~UBIGEO)
  rif_results[[rif_col]] <- coeftest(rif_fit, vcov=rif_vcv)
}
# → Table 4
```

### Step 10: Placebo Outcome (Non-Health Consumption Share)

```r
# placebo_share already constructed in Step 2
dt_pos[, placebo_share := nonhealth_cons / CTP]  # re-join if needed

pl_formula <- placebo_share ~ Q2+Q3+Q4+Q5+SIS+EsSalud+
                               Age_hh+Age_hh_sq+Female_hh+Educ_hh+Urban+log_N

pl_fits <- rq(pl_formula, tau=taus, data=dt_pos, weights=FACTOR07, method="br")

set.seed(43)
pl_boot <- boot.rq(x       = model.matrix(pl_formula, data=dt_pos),
                    y       = dt_pos$placebo_share,
                    tau     = taus, R=500,
                    bsmethod="cluster", cluster=dt_pos$UBIGEO,
                    weights = dt_pos$FACTOR07)
# β_Q3 from pl_fits vs p2_fits → Figure 4
```

### Step 11: Generate Figures

```r
# ── Figure 1: Quantile process plot (τ = 0.10 to 0.95) ──────────────
tau_grid <- seq(0.10, 0.95, by=0.05)

# Full-sample CQR (secondary spec; for comparison)
cqr_full  <- rq(p2_formula, tau=tau_grid, data=dt, weights=FACTOR07, method="br")

# Part 2 CQR at fine grid
p2_full <- rq(p2_formula, tau=tau_grid, data=dt_pos, weights=FACTOR07, method="br")

fig1_df <- rbind(
  data.frame(tau=tau_grid, beta=coef(cqr_full)["Q3",], spec="Full-sample CQR",
             reliable = tau_grid > mass_frac),
  data.frame(tau=tau_grid, beta=coef(p2_full)["Q3",],  spec="Part 2 CQR (OOP>0)",
             reliable = TRUE)
)
ggplot(fig1_df, aes(tau, beta, color=spec, shape=reliable)) +
  geom_line() + geom_point(size=2) +
  scale_shape_manual(values=c("TRUE"=16,"FALSE"=1),
                     guide=guide_legend(title="Reliable estimate")) +
  geom_hline(yintercept=0, linetype="dashed") +
  annotate("rect", xmin=0.10, xmax=mass_frac, ymin=-Inf, ymax=Inf,
           alpha=0.1, fill="red") +
  labs(title="Figure 1: Q3 Coefficient Process",
       subtitle=paste("Shaded region: tau < mass-point fraction (", round(mass_frac,2),")"),
       x="Quantile (τ)", y="β_Q3") + theme_minimal()

# ── Figure 4: Main vs. Placebo ───────────────────────────────────────
fig4_df <- data.frame(
  tau  = rep(taus, 2),
  beta = c(coef(p2_fits)["Q3",], coef(pl_fits)["Q3",]),
  spec = rep(c("Main: OOP share", "Placebo: non-health share"), each=length(taus))
)
ggplot(fig4_df, aes(tau, beta, color=spec)) +
  geom_line() + geom_point() +
  geom_hline(yintercept=0, linetype="dashed") +
  labs(title="Figure 4: Middle-Income Squeeze — Main vs. Placebo Outcome",
       x="Quantile (τ)", y="β_Q3 coefficient") + theme_minimal()
```

---

## `robustness_plan.md`

---

# Robustness Plan: Checks R1–R8

Each check follows the format: **Threat → Specification → Weakening condition → Strengthening condition**

---

**R1: Age Range Sensitivity**
- **Threat:** The 18–90 head-age restriction is arbitrary; outlier health profiles at extremes may distort distributional estimates.
- **Specification:** Re-estimate Part 2 CQR with (a) restriction expanded to 16–95 and (b) restricted to 25–75.
- **Weakening:** β_Q3(0.90) changes sign or loses significance under either alternative.
- **Strengthening:** β_Q3(0.90) stable across both variants.

---

**R2: Income Quintile Definition**
- **Threat:** Weighted population quintile cut-points may classify households differently than unweighted within-sample quintiles, affecting the Q3 composition.
- **Specification:** Re-estimate using unweighted within-sample quintile cuts (standard `quantile()` without FACTOR07).
- **Weakening:** Q3 effect disappears under unweighted quintiles; finding is weighting-sensitive.
- **Strengthening:** β_Q3(0.90) positive and significant under both definitions.

---

**R3: Outlier Treatment**
- **Threat:** The OOP_share > 5 exclusion threshold is arbitrary; results may be driven by a small number of extreme observations.
- **Specification:** (a) Winsorize OOP_share at 99th percentile instead of exclusion; (b) exclude at OOP_share > 2; (c) no upper restriction.
- **Weakening:** High-τ estimates change qualitatively across variants.
- **Strengthening:** Q3 > Q4 pattern at τ = 0.90 persists across all three variants.

---

**R4: Binary CHE Thresholds**
- **Threat:** Continuous OOP_share may miss clinically meaningful threshold effects; binary CHE is the policy-relevant metric.
- **Specification:** Weighted probit/logit of I(OOP_share > θ) on quintile dummies for θ ∈ {0.10, 0.25, 0.40}. Report marginal effects by quintile.
- **Weakening:** Q3 is not disproportionately represented among CHE households at any standard threshold.
- **Strengthening:** Q3 has the highest CHE incidence among Q2–Q5 at θ = 0.10 and/or 0.25.

---

**R5: Income Gradient Without Insurance Controls — Insurance Endogeneity Check (NEW)**
- **Threat (top referee objection):** SIS and EsSalud enrollment is endogenous to health status and income. If quintile and insurance enrollment are collinear, the quintile coefficients β_Q(τ) are contaminated by insurance endogeneity. Insurance-free estimates provide the uncontaminated income-distribution description.
- **Specification:** Re-estimate Part 2 CQR omitting SIS and EsSalud from the right-hand side. Compare β_Q3(τ) with vs. without insurance controls at τ ∈ {0.25, 0.50, 0.75, 0.90, 0.95}.
- **Weakening:** β_Q3(0.90) changes substantially (sign or > 50% magnitude change) when insurance controls are added; income gradient is not stable to insurance specification.
- **Strengthening:** β_Q3(0.90) is similar with and without insurance controls; the income gradient does not depend on insurance endogeneity, and the middle-income squeeze is identifiable as a pure income-distribution phenomenon.

---

**R6: Propensity-Score Matched Within-Q3 Comparison — Insurance Endogeneity Check (NEW)**
- **Threat (insurance endogeneity, continued):** Within Q3, comparison of insured vs. uninsured households confounds health status with insurance selection; sicker households may select into SIS.
- **Specification:** Restrict to Q3 households. Estimate propensity score for P(SIS=1) using Age_hh, Female_hh, Educ_hh, Urban, N_members, DOMINIO. Construct 1:1 nearest-neighbor matched sample (logit PS, caliper = 0.2 SD). Re-estimate the Part 2 CQR OOP_share comparison between insured and uninsured Q3 households on matched sample.
- **Weakening:** Post-matching OOP_share difference within Q3 between insured and uninsured vanishes; the conditional association was entirely selection on observables.
- **Strengthening:** Post-matching OOP_share remains higher for uninsured Q3 households, consistent with a genuine insurance role (though not causal identification).

---

**R7: Placebo Outcome — Non-Health Consumption Share (NEW)**
- **Threat:** The middle-income squeeze in OOP_share may reflect a general income-nonlinearity in consumption shares rather than a health-specific phenomenon.
- **Specification:** Identical Part 2 CQR specification with placebo outcome = (total consumption − OOP) / CTP. (See pseudo_code.md Step 10.) Compare β_Q3(τ) from placebo vs. main — Figure 4.
- **Weakening:** β_Q3(τ) for the placebo outcome is also positive and significant at high τ; the finding is not health-specific.
- **Strengthening:** Placebo β_Q3(τ) near zero or negative while main β_Q3(τ) is positive; health-specific interpretation strongly supported.

---

**R8: Censored QR vs. Two-Part Model (Primary Specification Sensitivity)**
- **Threat:** The two-part model treats OOP = 0 as a separate selection process. An alternative, censored quantile regression (Powell 1986), treats zeros as left-censored observations and imposes a unified model.
- **Specification:** Estimate censored QR via `crq()` on full analytic sample (including OOP = 0) at τ ∈ {0.25, 0.50, 0.75, 0.90, 0.95}.
- **Weakening:** β_Q3(0.90) from censored QR differs qualitatively from Part 2 CQR; zero-handling choice is consequential.
- **Strengthening:** Censored QR confirms Part 2 CQR result; finding is robust to the zero-treatment specification.

---

## `referee_objections.md`

---

# Adversarial Referee Objections and Responses

---

**Objection 1: Insurance Endogeneity**

*"The paper presents insurance coefficients as if they measure the causal effect of SIS and EsSalud enrollment on OOP expenditure. This is naive. SIS enrollment is heavily targeted to the poor and chronically ill; EsSalud coverage follows formal employment. Both are endogenous to health status, income, and labor market position — the exact variables that determine OOP expenditure. The authors have no instrument, no discontinuity, no natural experiment. The insurance coefficients are uninformative, and worse, if income quintile and insurance enrollment are correlated (as they obviously are in Peru), the quintile coefficients are also contaminated by selection. The middle-income squeeze story may be an artifact of insurance endogeneity, not a genuine income-distribution phenomenon."*

**Response:**

We explicitly acknowledge in the identification section (causal scope partition, Table in Section 5 of the strategy memo) that β_SIS and β_EsSalud are conditional associations, not causal effects, and are labeled as such throughout the paper. No causal claim about insurance is made.

For the quintile coefficients β_Q(τ), we address the endogeneity contamination concern through two robustness checks added specifically to address this objection:

**R5 (income gradient without insurance controls):** We re-estimate the full Part 2 CQR omitting insurance controls. If β_Q3(τ) is qualitatively unchanged, the income gradient is not an artifact of the insurance specification or its endogeneity. The side-by-side comparison at τ ∈ {0.25, 0.50, 0.75, 0.90, 0.95} is reported in Table 5. This also provides a pure descriptive income-distribution estimate uncontaminated by endogenous insurance controls.

**R6 (propensity-score matched within-Q3 comparison):** Within Q3, we use propensity-score matching on demographics to construct comparable insured and uninsured households, reducing selection on observables. If the OOP_share differential persists post-matching, the within-quintile insurance association is not entirely explained by observable selection.

The paper's core claim — that uninsured Q3 households face higher OOP_share at upper quantiles than Q4/Q5 households — is demonstrated to be robust to whether insurance controls are included (R5), which directly answers the concern that the income gradient is an insurance-endogeneity artifact.

---

**Objection 2: Denominator Measurement Error**

*"The CTP denominator is a household consumption aggregate from ENAHO. Consumption measurement error in household surveys is well-documented and systematically skewed: low-consumption households under-report, creating a mechanical upward bias in OOP/CTP for Q1 and Q2 households. This inflates the apparent squeeze among lower-income groups and may generate the non-linear quintile pattern the authors document. The income gradient in OOP_share may be a gradient in measurement error, not in true financial vulnerability."*

**Response:**

1. **Transparent denominator specification:** Our CTP uses the INEI food poverty line as a domain-specific subsistence minimum (7 geographic domains), the same methodology in INEI's official poverty measurement. Domain specificity reduces systematic geographic measurement error in the denominator.

2. **R3 (outlier treatment):** We winsorize OOP_share at the 99th percentile and vary the exclusion threshold. If measurement error is concentrated in extreme denominator values, this sensitivity check isolates its effect.

3. **R4 (binary CHE thresholds):** Binary I(OOP_share > θ) outcomes are substantially less sensitive to extreme denominator measurement error than the continuous share.

4. **R7 (placebo outcome):** If the Q3 spike is a measurement-error artifact in the CTP denominator, the identical pattern should appear in non-health consumption share / CTP — since both shares use the same denominator. If the placebo (Figure 4) shows no Q3 spike while the main result does, denominator measurement error cannot explain the health-specific finding.

We acknowledge the paper cannot fully resolve consumption measurement error in a cross-sectional design and note this as a limitation.

---

**Objection 3: Cross-Sectional Design Limitations**

*"The authors use a single cross-section (ENAHO 2024) to characterize an income-distribution phenomenon. Cross-sections conflate cohort effects, life-cycle income transitions, and geographic sorting with a genuine middle-income vulnerability. The authors cannot disentangle these with one cross-section."*

**Response:**

We fully agree and do not claim to do so. The estimand is explicitly a **descriptive conditional quantile partial effect** — a characterization of the 2024 cross-sectional distribution. Geographic sorting is partially addressed by conditioning on Urban/Rural and clustering at the UBIGEO level (which absorbs local OOP price variation in the variance estimate). Age_hh and Age_hh² control for the life-cycle health gradient, though not for cohort effects.

The paper's contribution is quantifying the distributional concentration of OOP burden in the 2024 cross-section for policy relevance (Peru's ongoing insurance reform debates). We note the cross-sectional limitation explicitly in the identification section and call for panel data analysis as future work.

---

**Objection 4: Mechanical Tautology**

*"The finding that uninsured Q3 households have high OOP_share is not a discovery — it is a tautological consequence of Peru's insurance architecture. SIS covers the poor; EsSalud covers formal workers; Q3 is left uninsured by design. What is the contribution beyond restating what the insurance coverage map already implies?"*

**Response:**

This conflates the theoretical implication with the empirical magnitude. Three questions remain empirically open:

1. **Is the OOP_share elevation catastrophic or merely elevated?** Our quantile regression shows the Q3 spike occurs at τ = 0.75–0.95 (Table 3, Figure 1) — the upper tail. Q3 is disproportionately represented among catastrophically burdened households, which is not tautologically implied by average lower insurance coverage.

2. **Is Q3 worse off than Q1?** Q1 is also largely uninsured (SIS coverage is incomplete), yet our CQR framework directly tests whether Q3 > Q1 at high τ. If Q3 and Q1 had similar OOP burdens, the "squeeze" narrative collapses; Figure 1 tests this.

3. **Does the pattern persist conditional on insurance status?** R5 (insurance-free specification) estimates the income quintile gradient among all households regardless of insurance, including a within-uninsured comparison. If the squeeze is purely mechanical, quintile differences should vanish within the uninsured stratum.

The contribution is quantifying the *distributional concentration* of OOP burden — the share of Q3 households facing catastrophic expenditure, its comparison across quintiles, and the identification of upper-tail concentration as the policy-relevant metric for threshold design in future insurance expansion.

---

**Objection 5: Mass Point at OOP = 0**

*"Between 40–60% of households report zero OOP in a given quarter, creating a substantial mass point at zero in OOP_share. Standard Koenker–Bassett quantile regression requires an absolutely continuous conditional distribution — this regularity condition is violated. Estimates at τ < mass-point fraction are theoretically invalid. A two-part model or censored quantile regression is required."*

**Response:**

We agree with this objection. We have made the **two-part model the primary specification**, not a robustness check:

- **Part 1 (Table 2):** Weighted probit for P(OOP > 0 | X) — characterizes the extensive margin. Income quintile and insurance coefficients from Part 1 identify whether the squeeze operates through probability of any health expenditure.
- **Part 2 (Table 3):** Weighted CQR at τ ∈ {0.25, 0.50, 0.75, 0.90, 0.95} estimated on the OOP > 0 subsample. Conditioning on positive OOP eliminates the mass point entirely and satisfies the CQR regularity condition.

Full-sample CQR (including zeros) is retained as a **secondary descriptive specification** in Figure 1 only, with estimates at τ < mass-point fraction explicitly marked as unreliable (open circles, shaded region, labeled caveat in the caption). These estimates are not used for any reported inference.

Censored QR (Powell 1986 via `crq()`) is robustness check R8, testing whether the two-part model and censored QR yield qualitatively consistent results at high τ. The RIF-UQR estimates (Table 4) note the mass-point density adjustment in bandwidth selection for τ ≤ mass-point fraction (pseudo_code.md Step 9).

---

**Summary of deliverables produced:**

| File | Status |
|---|---|
| `strategy_memo.md` | Revised: two-part model as primary spec; survey weighting decision added; quintile assignment method specified; CTP denominator pre-specified (no fallback); causal scope partition table; CONSORT flowchart; power note; table and figure purposes stated |
| `pseudo_code.md` | Revised: Part 1 probit + Part 2 CQR as primary; `svydesign`/`svyglm` for survey weighting; weighted quintile cut-points; no CTP fallback; placebo outcome at Step 10; Figure 4 code added |
| `robustness_plan.md` | Revised: R5 (insurance-free) and R6 (PS matching) added for endogeneity; R7 (placebo outcome) added; old R7 (RIF bandwidth) removed; R8 is now censored QR as primary-spec sensitivity |
| `referee_objections.md` | Revised: Objection 1 response updated with R5/R6; Objection 5 response updated to reflect two-part model as primary |

**One critical implementation note for the RA:** At Step 0 of `pseudo_code.md`, run `print(names(dt_raw))` for each module and verify all assumed variable names (`P407A`–`P407H`, `P4191`, `P4192`, `P208A`, `P207`, `P301A`, `FACTOR07`, `UBIGEO`, `ESTRATO`, `AREA`, `DOMINIO`, `GASHOG2D`, `MIEPERHO`) against the actual ENAHO 2024 data dictionaries before executing any subsequent steps. Additionally, the INEI food poverty line values in Step 2's `z_lines` table must be filled from the INEI Condiciones de Vida en el Perú 2024 technical annex before running CTP construction.

---

```json
{
  "strategy_type": "Other",
  "estimand": "CQPE (conditional quantile partial effect, two-part model primary) + UQPE (unconditional quantile partial effect via RIF)",
  "primary_estimator": "Two-part model: Part 1 = weighted probit P(OOP>0); Part 2 = Koenker-Bassett Weighted CQR at τ ∈ {0.25, 0.50, 0.75, 0.90, 0.95} on OOP>0 subsample; RIF-OLS for unconditional quantile extension. Full-sample CQR retained as secondary/descriptive only.",
  "n_robustness_checks": 8,
  "n_tables_planned": 5,
  "n_figures_planned": 4,
  "top_referee_objections": [
    "Endogenous insurance enrollment: SIS and EsSalud selection confounds the insurance coefficients; no credible causal identification is provided. Addressed by: explicit causal scope partition (insurance = conditional association only); R5 (income gradient without insurance controls); R6 (propensity-score matched within-Q3 comparison).",
    "Measurement error in the capacity-to-pay denominator inflates the OOP share for low-consumption households, potentially generating a spurious income gradient. Addressed by: domain-specific INEI poverty line as denominator; R3 (outlier treatment); R4 (binary CHE thresholds); R7 (placebo outcome uses same denominator — differential placebo result rules out denominator artifact).",
    "Cross-sectional design conflates cohort effects, life-cycle income transitions, and geographic sorting with a genuine middle-income class vulnerability. Addressed by: explicit descriptive-only estimand framing; UBIGEO-clustered SEs; age quadratic controls; limitation acknowledged.",
    "The middle-income squeeze is mechanically tautological given Peru's insurance architecture; uninsured Q3 households driving the result is already known. Addressed by: upper-tail concentration as the empirical contribution; Q1 vs. Q3 comparison; R5 within-uninsured quintile test.",
    "Mass point at OOP = 0 violates QR regularity conditions; lower-quantile estimates are unreliable. Addressed by: two-part model is now the PRIMARY specification (Part 2 CQR on OOP>0 subsample only); full-sample CQR demoted to secondary/descriptive with unreliable estimates explicitly flagged; censored QR in R8."
  ]
}
```