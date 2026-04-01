## Senior Econometrics Review — ENAHO 2024 OOP Strategy Memo

---

### DIMENSION 1: IDENTIFICATION (30 points available)

**Score: 21/30**

**What is correct:** The causal scope partition (Section 5 table) is the strongest element of the memo. Explicitly labeling quintile coefficients as descriptive and insurance coefficients as conditional associations, then repeating this in every referee response, is exactly the right discipline. The formal identification assumptions for CQR and RIF-OLS are stated correctly: correct specification of the conditional quantile function and RIF regression respectively. The estimand is well-defined.

**Problem 1 — No health status controls (serious omission):** ENAHO Module 400 collects illness episodes (P401–P403), self-reported health status, and chronic condition indicators. None appear in the control vector X_h. This is a significant gap for any analysis of health expenditure. If Q3 households have higher morbidity burden than Q4/Q5 — which is plausible if Q4/Q5 households have better preventive access — then β_Q3(τ) absorbs a health-status gradient, not an insurance-architecture gradient. The paper's narrative ("uninsured Q3 households face higher OOP exposure because they lack coverage") could equally be read as "Q3 households are sicker." You must add at least one health status variable — illness episode in the past 3 months or self-reported health — or explicitly state that Module 400 contains no usable health status variable and note the omission as a threat.

**Problem 2 — Selection into Part 2 creates compositional differences:** The CQPE from Part 2 estimates Q_τ(OOP_share | X, OOP > 0). Part 1 shows the probability of positive OOP differs by quintile (this is the point of Part 1). This means the Part 2 analytic sample for Q1 represents a differently-selected fraction of Q1 households than the Q3 Part 2 sample represents of Q3 households. If Part 1 shows P(OOP > 0 | Q3) < P(OOP > 0 | Q1) — plausible if Q3 households have better access to formal care than Q1 — then Q3 Part 2 households are a more severely selected (high-need) subsample. The Section 5 identification statement does not address this compositional selection. You should state: "Part 2 estimates characterize the conditional distribution of OOP burden among households that incur any health expenditure. Income-group comparisons within Part 2 condition on this selection, meaning quantile differences reflect both the income gradient and potential differences in health-need composition of the OOP-incurring population across quintiles."

**Problem 3 — Misleading plain-language identification statement:** Section 5 states income quintile differences "reflect the differential OOP price exposure of uninsured middle-income households relative to insured higher-income households." This sounds causal. The formal statement above is correctly descriptive. The plain-language version should be revised to: "we observe higher conditional quantiles of OOP_share for Q3 households; we hypothesize but do not establish that insurance gaps are a contributing mechanism."

---

### DIMENSION 2: SPECIFICATION (25 points available)

**Score: 17/25**

**What is correct:** The two-part model structure is sound. Part 1 probit via svyglm with survey design is appropriate. Part 2 CQR with bootstrap-clustered SEs at the UBIGEO level is appropriate. The RIF formula (Section 4.3) is correctly stated. Table and equation numbering is consistent throughout.

**Problem 1 — N_members and log(N_members) in the same equation (critical):** Section 4.2 specifies X_h = {Age_hh, Age_hh², Female_hh, Educ_hh, Urban, N_members, log(N_members)}. Including both the level and the log of household size creates near-perfect multicollinearity, particularly at small N values (N=1: log=0; N=2: log=0.69; N=3: log=1.10). The bootstrap SEs will be inflated and potentially unstable. Pick one — log(N_members) is more defensible economically because the marginal OOP effect of an additional household member diminishes. Remove N_members level or provide an explicit justification for the double specification.

**Problem 2 — Wald test does not test the primary hypothesis:** The key finding is β_Q3(τ) > β_Q4(τ) at high τ — the non-linear "middle-income squeeze" ordering. The Wald test in Step 8 uses:
```r
R_mat <- matrix(c(1,-1,0,0,  1,0,-1,0,  1,0,0,-1), nrow=3, byrow=TRUE)
```
This tests H₀: Q2 = Q3 = Q4 = Q5 (joint equality). Rejecting this test does not establish the specific ordering β_Q3 > β_Q4 that drives the paper's central claim. You must add a direct test of H₀: β_Q3(0.90) − β_Q4(0.90) ≤ 0, computed from the bootstrap covariance between these two coefficients. The reported Wald test is a valid auxiliary check but cannot serve as evidence for the non-linear middle-income squeeze.

**Problem 3 — 500 bootstrap replications insufficient at τ = 0.95:** Bootstrap variance estimates at extreme quantiles are noisier than at the median. The field standard for extremal quantile inference is 999 replications minimum; 500 is borderline acceptable at τ = 0.75 but inadequate at τ = 0.95. Change R = 999 at minimal computational cost.

**Problem 4 — Education recoding is unjustified and potentially fragile:** The P301A → years mapping assigns 0 for "sin nivel," 2 for "inicial/primaria incompleta," 6 for "primaria completa," etc. The values 2, 11, 14, 16, 18 are undocumented choices. ENAHO 2024 may use different category codes than assumed. The character coercion `educ_map[as.character(P301A)]` will silently return NA for any unmapped code rather than error. Use `match()` with an explicit NA check, and add `stopifnot(!any(is.na(dt$Educ_hh)))` after construction.

---

### DIMENSION 3: DATA FEASIBILITY (15 points available)

**Score: 10/15**

**What is correct:** ENAHO is a publicly available survey with known structure. OOP components (P407A–P407H) are standard ENAHO health module fields. GASHOG2D is the standard Sumaria consumption aggregate. Survey weights and cluster identifiers are correctly specified. The annualization (×4 for 3-month recall) is methodologically appropriate.

**Problem 1 — Effective cluster count for bootstrap at τ = 0.95:** ENAHO covers approximately 30,000–35,000 households. With 40–60% zero OOP, the Part 2 sample is roughly 12,000–18,000 observations across approximately 1,800 UBIGEO districts. Average cluster size is approximately 7–10 in the Part 2 sample. At τ = 0.95, the upper 5% of the Part 2 sample is ~600–900 observations — fewer than one observation per cluster on average. The province-level collapse protocol is pre-specified but may affect a large fraction of districts. Report ex ante the expected fraction of UBIGEO codes that will require collapse; if it exceeds 30%, province-level clustering should be the primary specification, not a fallback.

**Problem 2 — OOP_share > 5 threshold interacts with CTP floor:** The floor `max(C_h − z_food × n_h, 1)` means households near the poverty line have CTP approaching 1 sol. For such households, even modest OOP can generate OOP_share > 5 and trigger exclusion. The restriction 5 (OOP_share > 5) will disproportionately exclude poor households near the subsistence minimum — potentially the most policy-relevant group. Document the quintile distribution of exclusions in Table 1. If Q1 is disproportionately excluded by restriction 5, the analytic sample is biased against the group the policy is meant to help.

**Problem 3 — DOMINIO coding assumption:** The z_lines lookup table hardcodes DOMINIO = 1:7. ENAHO uses various domain coding schemes across years; 2024 module documentation may differ. Step 0 checks variable names but not the DOMINIO values. Add `stopifnot(all(dt$DOMINIO %in% 1:7))` before the merge, with a contingency note for what to do if DOMINIO values differ.

---

### DIMENSION 4: ROBUSTNESS DESIGN (15 points available)

**Score: 11/15**

**What is correct:** R5 (insurance-free specification) and R7 (placebo outcome) are well-designed and directly address the two most important threats. R4 (binary CHE thresholds) is underrated — it converts the result to a policy-legible format and is substantially less sensitive to denominator measurement error than the continuous share. R8 (censored QR) is appropriately positioned as a primary-specification sensitivity.

**Problem 1 — No geographic heterogeneity check:** The "middle-income squeeze" has a plausible geographic confound: Lima Metropolitan households are more likely to be Q3 (urban, formal-sector adjacent) and also face higher provider prices. If the Q3 spike is entirely a Lima Metropolitan phenomenon, the national policy interpretation is weakened. Add R9: re-estimate Part 2 CQR separately for Lima Metropolitan vs. non-Lima, or include DOMINIO fixed effects as an alternative specification.

**Problem 2 — R6 (PS matching) is under-specified and likely uninformative:** The spec restricts to Q3 households and matches on P(SIS=1). The resulting comparison is of matched insured vs. uninsured Q3 households. But the memo then says "Re-estimate the Part 2 CQR OOP_share comparison between insured and uninsured Q3 households on matched sample" without specifying: at which τ? On what sample size? With what cluster structure? More fundamentally, the matched comparison cannot address unobservable health status selection (the key concern), and within Q3 the sample for matching is small enough that balance may be poor. This check will consume RA time but is unlikely to persuade a skeptical referee. Replace R6 with a more tractable check: within-quintile heterogeneity in OOP_share by formal employment status (a proxy for EsSalud eligibility independent of actual enrollment), which is available in ENAHO.

**Problem 3 — Placebo specification has a mechanical anti-correlation:** The placebo outcome is (GASHOG2D − OOP) / CTP. Since OOP appears in both the main outcome numerator and the placebo denominator's superset, high OOP mechanically reduces the placebo numerator. For households with very high OOP, the placebo will be mechanically low. This means even a null placebo could be partly mechanical rather than a genuine falsification. A cleaner placebo would be (food expenditure) / CTP, or a non-health durable expenditure share, where the numerator has no mechanical relationship to OOP.

---

### DIMENSION 5: COMPLETENESS (15 points available)

**Score: 11/15**

**What is correct:** All four deliverables are present. Tables 1–5 have stated purposes and the purposes are informative (not just "reports estimates"). Referee responses directly address the objections with specific evidence. The CONSORT flowchart with fill-in-later n values is good practice.

**Problem 1 — Missing code for Figures 2 and 3:** Step 11 codes only Figures 1 and 4. Figure 2 (predicted OOP_share distributions by quintile) and Figure 3 (Part 1 probit marginal effects bar chart) are described in the deliverables plan but have no corresponding pseudo-code. An RA reading this document cannot implement them. Add code.

**Problem 2 — No bootstrap confidence intervals for Figure 1 fine-grid:** Figure 1 is described as showing "95% bootstrap CIs across the full τ grid" but Step 11 only computes point estimates for the fine grid (`cqr_full` and `p2_full`). No bootstrap loop is specified for the fine τ grid. This is the most visually prominent figure in the paper — it needs implementable CI code.

**Problem 3 — RIF mass-point density adjustment stated but not implemented:** Section 4.3 states the density f̂(Q_τ) uses "mass-point adjustment for τ ≤ mass-point fraction." Step 9 code does NOT implement a mass-point adjustment — it switches the bandwidth estimation sample but uses the same `density()` call with Gaussian kernel, which will smooth over the mass point and underestimate f̂(Q_τ) near zero. The consequence is inflated RIF values for low τ. Either implement a proper point-mass adjustment (mix a discrete mass at 0 with the continuous kernel density) or remove the claim that a mass-point adjustment is performed.

**Problem 4 — boot.rq() cluster argument:** The `boot.rq()` function in the `quantreg` package uses `cluster` as a formula or factor, not a vector. The call `cluster = dt_pos$UBIGEO` may fail silently or error depending on package version. Verify against `?boot.rq` and replace with `cluster = ~UBIGEO` or convert to a factor with `cluster = as.factor(dt_pos$UBIGEO)`.

---

### SUMMARY TABLE

| Dimension | Weight | Raw Score | Weighted |
|---|---|---|---|
| Identification | 30% | 21/30 | 21.0 |
| Specification | 25% | 17/25 | 17.0 |
| Data Feasibility | 15% | 10/15 | 10.0 |
| Robustness Design | 15% | 11/15 | 11.0 |
| Completeness | 15% | 11/15 | 11.0 |
| **Total** | | | **70/100** |

---

### PRIORITY FIXES (before any code is written)

1. **Add health status control** — illness episode dummy or self-reported health from Module 400. Without it, the income gradient conflates insurance and morbidity gradients.
2. **Remove N_members from X_h** — keep only log(N_members). Fix the collinearity.
3. **Add direct test of β_Q3(0.90) > β_Q4(0.90)** — this is the paper's core claim and is not tested by the current Wald specification.
4. **Fix placebo outcome** — replace (GASHOG2D − OOP)/CTP with food expenditure share or non-health durable share to avoid mechanical anti-correlation.
5. **Add Figures 2 and 3 code** — both are in the deliverables plan but absent from pseudo_code.md.
6. **Add bootstrap CI loop for Figure 1 fine grid** — the paper's main visual requires it.

---

```json
{
  "score": 70,
  "verdict": "CONCERNS",
  "critical_issues": [
    "No health status controls (illness episodes, self-reported health) in a health expenditure regression — income gradient may partially reflect morbidity gradient rather than insurance architecture",
    "Wald test tests joint equality (Q2=Q3=Q4=Q5), not the paper's central hypothesis (β_Q3 > β_Q4 at high τ); the primary empirical claim has no direct formal test"
  ],
  "major_issues": [
    "N_members and log(N_members) both in the estimating equation — near-perfect multicollinearity, especially at small household sizes; remove N_members level",
    "Placebo outcome (GASHOG2D − OOP)/CTP has a mechanical anti-correlation with the main outcome because high OOP shrinks the placebo numerator; replace with food expenditure share or non-health durable share",
    "RIF mass-point density adjustment claimed in Section 4.3 but not implemented in Step 9 code — Gaussian kernel density() will underestimate f̂(Q_τ) at the mass point",
    "Code missing for Figures 2 and 3 entirely; no bootstrap CI loop for Figure 1 fine τ grid despite CIs being the figure's stated purpose",
    "Effective cluster size at τ = 0.95 may be below one observation per UBIGEO on average; quantify expected fraction requiring province collapse before declaring UBIGEO-level clustering as the primary SE method"
  ],
  "minor_issues": [
    "500 bootstrap replications insufficient for τ = 0.95 — use 999",
    "boot.rq() cluster argument likely requires formula (~UBIGEO) not vector; verify against package documentation",
    "Education P301A recoding uses undocumented year values; silent NA on unmapped codes needs a stopifnot() guard",
    "OOP_share > 5 exclusion will disproportionately exclude near-subsistence households (CTP near floor of 1); document quintile distribution of exclusions in Table 1",
    "R6 (propensity-score matching within Q3) is under-specified (no τ, no sample size estimate) and cannot address unobservable health status selection; replace with within-uninsured income gradient by formal employment status",
    "No geographic heterogeneity robustness check; Lima Metropolitan vs. non-Lima split needed to rule out the finding being geographically concentrated",
    "Plain-language identification statement in Section 5 sounds causal ('reflect the differential OOP price exposure'); revise to purely descriptive language consistent with formal statement above it"
  ]
}
```