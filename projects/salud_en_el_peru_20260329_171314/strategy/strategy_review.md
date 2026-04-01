## Econometric Review: OOP Expenditure Distributional Analysis (ENAHO 2024)

---

### Dimension 1 — Identification (30%)  **Score: 18/30**

**Core problem:** The strategy is fundamentally descriptive but is dressed in causal language. This is not inherently fatal — documenting the income gradient in OOP burden is a legitimate research contribution — but the memo needs to pick a lane and commit to it.

**Specific issues:**

1. **The CIA assumption for insurance enrollment is not credible and is essentially undefended.** SIS enrollment in Peru is needs-based (poor/vulnerable households) and EsSalud enrollment is payroll-based. These are opposite selection directions. A "rich controls" justification for CIA requires arguing that after conditioning on income quintile, age, education, urbanicity, and region, insurance take-up is as-good-as-random. This is implausible — household health status, chronic disease burden, and risk preferences drive both enrollment and OOP expenditure, and these are not observed in ENAHO Module 400. The memo correctly names this as the top referee objection but the response ("see R3-R8") does not actually address identification.

2. **The estimand is mislabeled.** CQPE and UQPE are descriptive distributional statistics, not causal effects. There is no ATT, ATE, or LATE here. This is fine if framed correctly, but the memo's referee-response language ("the insurance coefficients are confounded") implies the authors believe they are estimating something causal. Be explicit: this is a *conditional association at the τ-th quantile*, not a causal effect. Write that in the identification section.

3. **The core estimand of interest (the income gradient / "middle-income squeeze") is actually defensible.** Income quintile assignment is nearly exogenous in a cross-section for the descriptive question "who bears the highest OOP share?" This stronger ground should be foregrounded; the insurance variable should be explicitly demoted to a control/mediator with acknowledged endogeneity. The paper cannot claim to have identified an insurance effect, but it *can* claim to have documented an income-distributional pattern.

**Fix:** Add a one-paragraph "Scope of causal claims" statement that explicitly partitions: (a) income quintile comparisons = descriptive, (b) insurance coefficients = conditional associations only, not causal. This protects the paper.

---

### Dimension 2 — Specification (25%)  **Score: 15/25**

**Issue 1 — Survey weighting decision is not stated.** ENAHO uses a complex stratified multi-stage design with FACTOR07 weights. Running unweighted quantile regression on ENAHO data produces estimates of the *sample* distribution, not the *population* distribution. Running survey-weighted QR (via `survey::svyquantile` or Stata's `sqreg` equivalent) is methodologically distinct and requires different SE machinery than `boot.rq()`. The memo mentions FACTOR07 as a variable but does not state whether estimation is weighted. **This is not a minor point.** For a paper about Peru's population income distribution, unweighted estimates are likely inconsistent for the UQPE.

**Issue 2 — Income quintile assignment method is undefined.** Are quintiles assigned within the analytic sample, or from national population quintile cutoffs? This choice has large consequences for the "middle-income squeeze" narrative. Within-sample quintiles among ENAHO health spenders are not the same as national quintiles. Specify which, and justify.

**Issue 3 — The OOP share outcome construction has an unresolved denominator problem.** The "fallback for missing expenditure aggregate" in the CTP construction is a serious flag. If capacity-to-pay is imputed or approximated for a non-trivial fraction of observations, the main outcome variable (OOP/CTP) has differential measurement error across the income distribution. This is not a software detail — it is a specification decision that needs to be resolved *in the memo*, not deferred to the RA.

**Issue 4 — Clustering level is stated but not justified.** The memo mentions UBIGEO/ESTRATO. Clustering at UBIGEO (district) versus ESTRATO (sampling stratum) versus household is not equivalent. For health insurance effects, geographic clustering at the UBIGEO level is likely appropriate because SIS eligibility varies by district-level census targeting. State the level and provide economic justification, not just a reference to the survey design.

---

### Dimension 3 — Data Feasibility (15%)  **Score: 9/15**

**Issue 1 — No sample size reported.** ENAHO 2024 typically has ~35,000 households; after restricting to households with positive health contact (necessary to avoid the zero mass point dominating), the analytic sample could be 8,000–15,000 observations. At τ = 0.95 with 15+ regressors and district-level clustering, statistical power for subgroup tests (e.g., income quintile × insurance interactions) is genuinely uncertain. A power-relevant calculation is missing.

**Issue 2 — The zero mass point at OOP = 0 is treated as a robustness check (R8) when it should determine the primary specification.** If 40–60% of households report zero OOP expenditure (plausible in ENAHO), then QR estimates at τ = 0.10 and τ = 0.25 are estimating a spike at zero, not a smooth conditional quantile. The Koenker-Bassett regularity conditions require a continuous conditional distribution — they are violated at the lower tail. This is not a concern to be checked in robustness; it means the two-part model (or censored QR) should be the *baseline* specification, with uncensored QR as the comparison. As written, the strategy inverts the preferred ordering.

---

### Dimension 4 — Robustness Design (15%)  **Score: 10/15**

**What works:** R1 (age range), R4 (binary CHE thresholds), R5 (income permutation placebo), and R8 (two-part model) are well-targeted. The income permutation placebo (R5) is particularly good — it directly falsifies the mechanical-tautology objection.

**Issue 1 — No robustness check addresses insurance endogeneity.** The top referee objection is insurance selection bias, and none of R1–R8 address it even approximately. Minimum required: (a) re-estimate dropping insurance variables entirely to show the income gradient is not an artifact of insurance controls; (b) re-estimate with propensity-score-matched samples on observable characteristics; or (c) add an explicit "insurance-free" specification showing the income pattern holds unconditionally. The current R3 ("control sensitivity") is vague and may cover this, but it needs to be explicit.

**Issue 2 — No placebo outcome test.** A clean falsification would be: run the identical specification with *non-health consumption share* as the outcome. If the middle-income squeeze appears there too, it is a general income-distributional artifact, not a health-specific finding. This test is missing and a referee will ask for it.

**Issue 3 — R7 (RIF bandwidth) is a low-priority robustness check.** RIF is non-parametric in kernel density estimation; bandwidth sensitivity is a second-order concern compared to the specification and identification issues above. This slot would be better used for the placebo outcome test or the propensity score check.

---

### Dimension 5 — Completeness (15%)  **Score: 11/15**

**What works:** All four deliverables are claimed present. The table of files with described contents is clear. The variable-name verification note at the end is appropriate and shows implementation awareness.

**Issue 1 — The review is evaluating a *summary* of the memo, not the memo itself.** The actual content of `strategy_memo.md`, `pseudo_code.md`, etc. is not shown. The filing system is described, but the estimating equation, variable definitions, and pseudo-code cannot be verified from this document. This is an external limitation of the review, but it means all "specific enough to implement" claims are unverifiable.

**Issue 2 — Tables are counted but not described.** "5 tables planned" is not the same as "Table 2 reports Wald tests of equality across income quintiles at each τ." What are the 5 tables? What are the 4 figures? The answer to this question is the difference between a plan and a research design.

**Issue 3 — No pre-analysis plan or sample construction flowchart.** For a cross-sectional analysis using publicly available government data, a CONSORT-style observation flowchart (total ENAHO sample → exclusion criteria → analytic sample) should be in the deliverables. Its absence is a minor gap but a predictable referee request.

---

### Summary of Required Revisions

**Before writing any code, resolve:**

1. **Two-part model as primary specification.** Move the censored QR / two-part model to the baseline. Justify keeping uncensored QR as a comparison, not the other way around.
2. **Resolve the CTP denominator fallback.** Make a definitive methodological decision; do not leave it to the RA as a software choice.
3. **Clarify income quintile assignment method** (within-sample vs. national) and state the expected analytic sample size after all restrictions.
4. **Add explicit survey-weighting decision** and confirm `boot.rq()` is compatible with the chosen approach.

**Add to robustness plan:**

5. **Insurance-free specification** showing the income gradient holds without conditioning on insurance.
6. **Placebo outcome test** using non-health consumption share.

---

```json
{
  "score": 63,
  "verdict": "CONCERNS",
  "critical_issues": [
    "Zero mass point at OOP=0 likely invalidates lower-quantile CQR estimates; two-part model or censored QR should be the primary specification, not a robustness check (R8). This inverts the methodological priority.",
    "Survey weighting decision is absent. Unweighted quantile regression on ENAHO produces sample-distribution estimates, not population estimates. For a paper about Peru's national income distribution this is potentially inconsistent for the UQPE/RIF results."
  ],
  "major_issues": [
    "Insurance endogeneity is the top stated referee objection but zero robustness checks address it. Minimum required: re-estimate without insurance controls to show income gradient is not an artifact; add propensity-score or matching comparison.",
    "No placebo outcome test. Running the identical specification with non-health consumption share as outcome is a standard falsification test that is conspicuously absent.",
    "CTP denominator 'fallback for missing expenditure aggregate' is a specification decision deferred to the RA. This is not a software detail — differential measurement error in the denominator across the income distribution directly contaminates the main outcome variable.",
    "Income quintile assignment method (within-sample vs. national population quintiles) is unspecified. These produce different income categories and different 'middle-income squeeze' narratives."
  ],
  "minor_issues": [
    "Sample size after all restrictions is not reported. Power at tau=0.95 with district-level clustering is unverified.",
    "Tables and figures are counted but not described. '5 tables planned' is insufficient — each table should have a stated purpose.",
    "R7 (RIF bandwidth sensitivity) is a low-priority robustness check occupying a slot better used for the placebo outcome or insurance-free specification.",
    "Causal scope is not explicitly partitioned: income quintile comparisons (descriptive) vs. insurance coefficients (conditional associations only). This distinction needs to be stated in the identification section to prevent referee misreading.",
    "No CONSORT-style observation flowchart from raw ENAHO to analytic sample."
  ]
}
```