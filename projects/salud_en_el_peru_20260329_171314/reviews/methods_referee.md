## Referee Report

**Journal**: [Health Economics / Journal of Development Economics / Journal of Health Economics]
**Paper**: "The Middle-Income Squeeze: Distributional Analysis of Health Expenditure Determinants in Peru"

---

### Summary of Methodology

The paper applies conditional quantile regression (CQR) at five quantiles (τ = 0.10, 0.25, 0.50, 0.75, 0.90) to OOP health expenditure share, interacting insurance status (SIS, EsSalud, uninsured) with consumption quintiles using Peru's 2024 ENAHO cross-section (N = 33,691 households). The authors frame the analysis explicitly as descriptive rather than causal, acknowledge three sources of endogeneity (insurance selection, quintile endogeneity, care avoidance/foregone care), and report cluster-bootstrapped standard errors at the PSU level with 200 replications. Twenty-five robustness checks cover alternative samples, CHE thresholds, floors, annualization, and placebo tests.

---

### Main Methodological Assessment

The paper makes a legitimate methodological contribution by moving beyond binary CHE threshold analysis to characterize the full conditional distribution of OOP burden. The honest, upfront descriptive framing is commendable and appropriate given the data. However, three substantive methodological concerns—zero-mass degeneracy at lower quantiles without a two-part or censored-quantile correction, inadequate bootstrap replications for publishable inference, and no multiple testing correction across a large family of tests—must be addressed before publication. Additionally, the use of OLS on a fractional bounded outcome as the "benchmark" without acknowledging the functional form implications is a minor but visible gap.

---

### Major Concerns

**1. Zero-inflation renders lower-quantile CQR estimates uninformative and the paper's response is insufficient.**

With 44.1% of households reporting zero OOP expenditure, the conditional quantile function is degenerate at any τ ≤ 0.44 (approximately). The paper acknowledges this in the results section ("all coefficients are at or near zero with negligible standard errors" at τ = 0.10) but treats it as an interpretive caveat rather than a methodological flaw. The appropriate response is one of:

- **Two-part model**: Probit/logit for P(OOP > 0) followed by OLS or QR on the positive-spending subsample, allowing separate analysis of the extensive and intensive margins.
- **Censored quantile regression** (Powell 1986, Chernozhukov & Hong 2002): Properly handles the boundary mass at zero and produces informative estimates at quantiles below the zero-mass proportion.
- **Tobit-based QR** or the Machado-Santos Silva (2005) quantile regression with fixed effects for the bounded outcome.

The current positive-OOP subsample analysis (robustness panel, N = 18,843) is not a substitute: conditioning on positive spending is a selected sample (Heckman selection problem), not a solution to the censoring. The paper should either adopt censored QR as the primary specification or explicitly position CQR as applying only to informative quantiles (τ ≥ 0.50) and reframe the paper accordingly.

**Suggestion**: Replace the τ = 0.10 and 0.25 specifications with censored quantile regression, or adopt a two-part model as the primary framework with CQR as a supplementary check on the intensive-margin sample.

---

**2. Two hundred bootstrap replications is insufficient for publishable inference, particularly at τ = 0.90.**

The paper explicitly acknowledges that 200 replications is "below the recommended 999 for publishable inference" (citing Cameron et al. 2008). At τ = 0.90, where effective cell sizes are small (top decile × quintile × insurance cells may contain O(50–100) observations), bootstrap standard errors with 200 replications have high Monte Carlo error. The reported p-values and significance stars at τ = 0.90—which underpin the paper's main claims—rest on noisy standard error estimates.

**Suggestion**: Increase bootstrap replications to at minimum 999 (1,999 preferred for tail quantiles). Report whether significance conclusions at τ = 0.75 and τ = 0.90 survive under the higher-replication standard errors. If computational constraints are binding, report wild cluster bootstrap or analytical Koenker–Bassett standard errors as the primary inference method, with 999-replication bootstrap as validation.

---

**3. No multiple testing correction across a large family of hypothesis tests.**

The paper reports coefficients from 5 quantile regressions × (2 insurance dummies + 8 interaction terms + controls), plus 25 robustness regressions. Across this family, some results will appear significant by chance under conventional α = 0.05 thresholds. The paper selectively highlights which insurance–quintile–quantile interactions are significant (e.g., SIS×Q3 at τ = 0.90 significant; SIS×Q2 not) without adjusting for the joint testing problem. This is a form of implicit specification searching even when the paper does not intend it.

**Suggestion**: Apply Romano–Wolf (2005) stepdown corrections or Benjamini–Hochberg FDR corrections across the key hypothesis family (the insurance–quintile interaction terms at each quantile). At minimum, report joint F-tests for whether the full set of interactions is jointly significant at each quantile, as a complement to individual t-tests. For the robustness table, clarify which of the 25 checks were pre-specified and which were exploratory.

---

**4. Consumption quintile endogeneity is acknowledged but inadequately addressed.**

Total consumption (GASHOG2D) includes health expenditure, so the denominator of OOP_share and the variable defining quintile assignment share a common component. Households with high health spending have higher total consumption, are assigned to higher quintiles, and have mechanically higher OOP_share. The paper acknowledges this in a sentence but does not estimate a robust alternative. This circularity is particularly problematic for the paper's central claim about the quintile gradient.

**Suggestion**: Construct consumption quintiles from non-health consumption (GASHOG2D minus P41601 + P41602 + P41603 aggregated to household level). Re-estimate the main specifications with this alternative quintile assignment. If the main findings are robust to this correction, the mechanical relationship concern is largely resolved. This is the most direct available check and should be included as a primary robustness specification, not a footnote.

---

**5. OLS benchmark uses a linear model for a fractional bounded outcome without justification.**

OOP_share is bounded [0, 1]. Linear OLS can produce fitted values outside [0, 1] and the linear probability/share approximation is well-known to be inappropriate at extremes. For a paper positioning itself as a methodological contribution over the CHE binary-threshold literature, using a linear benchmark without acknowledgment of this limitation is conspicuous.

**Suggestion**: Estimate the OLS benchmark as a fractional logit (Papke & Wooldridge 1996) or beta regression as a robustness check. If these yield qualitatively similar conclusions, the current linear benchmark can be retained with a footnote citing the comparison. If they diverge, the fractional logit should be the primary benchmark.

---

### Minor Concerns

**1. Household head's insurance as the household insurance measure.** Module 400 provides individual-level insurance data. Assigning household insurance based on the household head excludes cases where the head is uninsured but dependents have SIS coverage, or vice versa. A household-level measure (e.g., any member insured, or majority coverage) may better characterize financial protection. Report sensitivity to alternative household insurance aggregation rules.

**2. The ×13 annualization amplifies point-in-time measurement error.** A single acute care visit in the 4-week recall window is multiplied by 13, dramatically overstating annual OOP for episodically ill households. The ×12 sensitivity is reported, but neither multiplier corrects for the fundamental recall problem. The paper should more prominently acknowledge that the annualization assumption is the dominant source of measurement error in the outcome variable, and consider reporting results in raw 4-week OOP share as an alternative.

**3. Weak placebo test.** The random treatment reassignment placebo is nearly trivially expected to yield a null result—random noise regressed on correlated covariates will not produce spurious associations in a large, well-controlled regression. A more informative falsification would be: (a) test whether insurance status predicts non-health expenditure shares (food, clothing) at the same quantiles; finding significant associations would indicate residual confounding. (b) Test whether future insurance status (if panel data from prior ENAHO waves are accessible) predicts current OOP share, which would detect selection effects.

**4. EsSalud interaction estimates from very small cells.** With N = 648 EsSalud households split across 5 quintiles, some quintile–EsSalud cells likely have fewer than 100 observations. The paper reports EsSalud interaction estimates but these are effectively unidentified. These should either be suppressed with a note on insufficient cell size, or aggregated (collapse Q3–Q5 into "upper quintiles" for the EsSalud interaction) to improve precision.

**5. Survey-weighted quantile regression implementation is non-standard.** Applying FACTOR07 as frequency weights rescaled to preserve sample size is not equivalent to properly propagating the stratified multistage survey design through the quantile regression estimator. The stratification and clustering structure affects both the point estimates (through probability-proportional-to-size weighting) and the variance. The paper should cite the specific QR-with-survey-weights estimator being used (e.g., the design-weighted estimator of Koenker & Bassett or the bootstrap-based approach of Chambers & Dunstan 1986) and confirm that the implementation matches.

**6. Region fixed effects specification is underdescribed.** How many regions are included (25 departments? 8 natural regions? ENAHO's 25 domains?)? With PSU-level clustering and region fixed effects, the within-region variation driving identification should be documented. If region effects absorb a large share of variance (relative to the very low R² = 0.0201), reporting within-R² would be informative.

**7. The RIF regression alternative is mentioned but not estimated.** The paper correctly notes that RIF regression (Firpo et al. 2009) answers the population-level unconditional quantile question, which is arguably more relevant for policy. Given that the paper's policy conclusions are about which households "bear the greatest burden" unconditionally, a brief RIF regression estimate would strengthen the link between the conditional CQR results and the policy claims.

---

### Recommendation: **Major Revision**

The paper makes a legitimate and honest descriptive contribution using an appropriate distributional method. The explicit non-causal framing, the transparent variable construction, and the breadth of robustness checks are commendable. However, the zero-inflation problem at lower quantiles is a structural methodological issue that the paper acknowledges but does not resolve; the 200-replication bootstrap is insufficient for the inference claims being made; and the absence of multiple testing correction over a large family of tests is a material concern. These are addressable with targeted additional analyses rather than a fundamental redesign of the paper.

---

```json
{
  "score": 67,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "identification_strategy": 70,
    "estimation_implementation": 62,
    "statistical_inference": 60,
    "robustness_sensitivity": 71,
    "replication_readiness": 75
  },
  "sanity_checks": {
    "sign": "PASS",
    "magnitude": "PASS",
    "dynamics": "NA",
    "consistency": "PASS"
  },
  "major_comments": [
    "Zero-inflation (44.1% zeros) renders CQR degenerate at tau=0.10 and tau=0.25; the paper acknowledges this but does not adopt censored QR (Powell 1986) or a two-part model, which are the appropriate methodological responses. The positive-OOP subsample robustness check does not resolve the issue because conditioning on positive spending introduces Heckman selection bias.",
    "200 bootstrap replications is self-admittedly below publishable standards (authors cite Cameron et al. 2008 threshold of 999). The main claims rest on upper-tail estimates (tau=0.75, tau=0.90) where effective cell sizes are smallest and bootstrap SEs are noisiest. Must increase to 999+ and re-confirm significance conclusions.",
    "No multiple testing correction across the family of 5 quantiles x 10 insurance/interaction coefficients, plus 25 robustness regressions. Selective reporting of which interactions are significant at which quantiles without familywise adjustment (Romano-Wolf or Benjamini-Hochberg) risks false discovery inflation.",
    "Consumption quintiles are constructed from total consumption that mechanically includes health expenditure (the numerator of the outcome), creating a circularity acknowledged but not resolved. The paper should estimate quintiles from non-health consumption as a primary robustness check, not merely a footnote acknowledgment.",
    "OLS benchmark uses linear regression on a fractional bounded outcome [0,1] without justification. Fractional logit (Papke-Wooldridge 1996) should be reported as the comparison benchmark given the paper's methodological positioning."
  ],
  "minor_comments": [
    "Household insurance defined by head's coverage excludes within-household coverage heterogeneity; report sensitivity to any-member insurance aggregation.",
    "Annualization multiplier x13 mechanically amplifies point-in-time measurement error for episodically ill households; this is the dominant source of outcome measurement error and deserves more prominent discussion than it currently receives.",
    "Random-reassignment placebo is too weak; falsification using non-health expenditure shares as outcomes at the same quantiles would be more informative for ruling out residual confounding.",
    "EsSalud quintile interaction cells likely have O(50-100) observations; these estimates are effectively unidentified and should be suppressed or aggregated to prevent readers from over-interpreting noisy coefficients.",
    "Survey-weighted QR implementation (frequency weights rescaled to preserve N) is non-standard and may not properly propagate the stratified multistage design; cite the specific estimator and validate against design-consistent alternatives.",
    "Region fixed effects specification is underdescribed (how many regions? which classification?); with PSU clustering and region FE, documenting the within-region variation driving identification is important.",
    "RIF regression (Firpo et al. 2009) is mentioned in the literature review but not estimated; given that policy conclusions concern unconditional quintile burdens, a brief RIF comparison would bridge the conditional CQR results to the policy framing more rigorously."
  ]
}
```