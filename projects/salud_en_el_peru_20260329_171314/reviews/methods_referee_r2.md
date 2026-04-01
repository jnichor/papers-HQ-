## Referee Report

**Journal:** [Submitted manuscript]
**Title:** *The Middle-Income Squeeze: Distributional Analysis of Health Expenditure Determinants in Peru*

---

### Summary of Methodology

The paper applies conditional quantile regression (CQR) at τ ∈ {0.10, 0.25, 0.50, 0.75, 0.90} to Peru's 2024 ENAHO cross-sectional data (N = 33,691 households) to characterize distributional heterogeneity in the out-of-pocket (OOP) health expenditure share. Insurance status (SIS, EsSalud, uninsured) is interacted with consumption quintiles; standard errors are cluster-bootstrapped at the PSU level using 200 replications. The analysis is framed explicitly as descriptive, and twenty-five robustness checks are reported.

---

### Main Methodological Assessment

The methodological framework is well-matched to the stated research question, and the authors display unusual—and commendable—candor in flagging the limitations of their own approach. However, several issues rise to the level of major concerns that require resolution before the findings can be considered reliable. The most consequential is the apparent misconstruction of the EsSalud insurance variable, which yields N = 648 despite national EsSalud enrollment implying several thousand qualifying observations; this is not a minor sample imbalance but a probable measurement error that contaminates the uninsured reference category. The second structural issue is the mechanical circularity introduced by constructing consumption quintiles from GASHOG2D, the same variable that serves as the OOP share denominator—this inflates the quintile gradient and may confound the primary insurance–quintile interaction estimates even under a purely descriptive framing. Third, the 200-replication cluster bootstrap is self-described as "below the standard for publishable inference," yet the paper draws significance conclusions at τ = 0.90, precisely where bootstrap variance is most sensitive to replication count. These three issues collectively undermine confidence in the headline findings and require direct remediation.

---

### Major Concerns

**1. EsSalud variable construction (N = 648 — likely measurement error)**

EsSalud covers approximately 30% of Peru's workforce through mandatory payroll contributions. An effective sample of 648 in a 33,691-household nationally representative frame implies a coverage rate under 2%, roughly fifteen times below its true national incidence. The authors attribute this to "a variable construction issue" but do not diagnose or correct it. This is not a minor caveat: if the EsSalud indicator is miscoded, an unknown fraction of formal-sector workers has been misclassified as uninsured, biasing the uninsured reference category—and therefore every SIS interaction coefficient—upward in magnitude. The paper should (a) diagnose the source of the EsSalud undercounting against known administrative enrollment figures, (b) attempt a corrected EsSalud classification using alternative ENAHO variables (P4192, P4195, employer-reported contributions), and (c) report sensitivity of the SIS coefficients to excluding EsSalud from the sample and to defining uninsured as "neither SIS nor EsSalud under corrected coding." Until this is resolved, the SIS arm of the analysis rests on a contaminated reference group.

*Specific suggestion:* Cross-tabulate P4191, P4192, and P4195 jointly, compare marginal EsSalud counts against ENAHO documentation, and reconcile against SUSALUD or ENAHO metadata on formal sector coverage rates.

**2. Mechanical circularity: quintile assignment from OOP-inclusive consumption denominator**

The OOP share outcome is defined as Health\_expenditure / max(GASHOG2D, Floor). Consumption quintiles are constructed directly from GASHOG2D. If health expenditure is a non-trivial component of GASHOG2D—which is probable in the ENAHO Sumaria module, which includes health components—then higher OOP spending mechanically shifts households into lower quintiles (lower denominator → lower consumption rank), inducing a negative mechanical correlation between quintile rank and OOP share. This partially offsets the true positive income gradient in OOP share. More critically, the interaction term (Insurance × Quintile) is estimated against a quintile baseline that is endogenously determined by the outcome, so the interaction coefficients conflate the genuine income gradient with a mechanical reclassification effect. The authors acknowledge this but treat it as a caveat rather than a problem requiring remediation.

*Specific suggestion:* Reconstruct quintiles using GASHOG2D net of health expenditure (non-food, non-health consumption) as the ranking variable. Report sensitivity of the quintile gradient and the SIS–quintile interactions to this alternative quintile definition. If the Sumaria module's health component cannot be isolated, use a standard-of-living proxy such as the food consumption component as the quintile instrument.

**3. Insufficient bootstrap replications for upper-quantile inference**

The paper explicitly states that 200 bootstrap replications are "below the standard for publishable inference." This acknowledgment is commendable, but the implication must follow: significance conclusions at τ = 0.90 drawn from 200-replication bootstraps are provisional at best and misleading at worst. The asymptotic approximation for cluster-bootstrap standard errors at τ = 0.90 in a highly skewed, zero-inflated distribution with 34 clusters (24 departments) requires substantially more replications than at the median. The reported SIS×Q5 coefficient of −1.94 pp (p < 0.01 at τ = 0.90) is the headline finding of the paper; it cannot rest on 200 replications.

*Specific suggestion:* Re-run all CQR estimates with 999 or 1,999 replications. If computational constraints preclude this for all τ and all specifications, at minimum re-run the primary specification (τ = 0.90, full controls) with 999 replications and verify that significance conclusions are stable.

**4. No multiple testing correction despite a large hypothesis family**

The paper estimates 5 quantiles × multiple interaction terms × 25 robustness checks, constituting a family of several hundred hypothesis tests. The paper itself notes that "4/25 significant results is within the range expected by chance alone," yet applies no familywise error rate (FWER) or false discovery rate (FDR) correction. The significance of individual interaction coefficients at τ = 0.75 and τ = 0.90—which constitute the primary substantive finding—is not robust to even the most lenient multiple testing correction (e.g., Benjamini-Hochberg at q = 0.10).

*Specific suggestion:* Apply a Holm-Bonferroni FWER correction or Benjamini-Hochberg FDR correction within the family of interaction tests at each quantile. Report adjusted p-values alongside unadjusted ones. If the main findings survive adjustment, this substantially strengthens the paper; if they do not, the conclusions must be qualified accordingly.

**5. Weak falsification design**

The primary placebo—random treatment reassignment—is correctly identified by the authors as uninformative: random noise regressed on correlated controls in a large, well-specified model is expected to yield null results by construction. This placebo tests nothing that a standard specification test does not already reveal. No alternative falsification is implemented; the non-health expenditure share test is deferred to "future work." For a paper whose central contribution is the distributional profile of insurance associations, an informative falsification (e.g., testing whether insurance predicts non-health OOP share—food, clothing, transport—at the same quantiles) is essential to rule out residual confounding by wealth or health-seeking behavior correlated with insurance enrollment.

*Specific suggestion:* Construct a food or clothing expenditure share analog of the outcome and re-estimate the main CQR specification. Significant insurance–quintile interactions for non-health outcomes would indicate residual omitted-variable bias rather than genuine financial protection effects.

---

### Minor Concerns

1. **Title–findings mismatch.** The paper's own conclusion states that "the monotonic gradient is itself a substantive finding with policy implications, even though it does not support the initial framing." The title promises evidence on a "middle-income squeeze" that the paper refutes. Titles should reflect findings, not the motivating hypothesis. Suggest a revision such as "Regressive Financial Protection? Distributional Evidence on Health Insurance and Out-of-Pocket Expenditure in Peru."

2. **Two-part model relegated to complement.** Given the 44.1% zero-OOP mass, the two-part model (TPM) is arguably the more appropriate primary specification, with CQR serving as the complement. The TPM provides consistent estimates of both the extensive margin (insurance lowering probability of any spending) and the intensive margin (spending conditional on positive), which are directly relevant to the policy question. The current paper sketches the TPM but does not estimate it. At minimum, the extensive-margin probit and the intensive-margin OLS/log-OLS results should be presented in full.

3. **P41603 sensitivity omitted.** The authors identify P41603 ("other health costs") as a high-variance, heterogeneous category driving upper-quantile estimates, yet no sensitivity to excluding it appears in the 25 robustness checks. This is an obvious and cheap specification test given the concern raised.

4. **Conditional vs. unconditional quantile effects.** The policy discussion in the conclusion—targeting distributional measures for CHE monitoring—is more naturally motivated by unconditional quantile effects (RIF regression). The paper discusses this distinction correctly in the literature review but defers the RIF extension to "future work." For a paper making policy recommendations about the distributional profile of OOP burden, reporting at least one RIF quantile estimate would provide the population-level complement needed to support those recommendations.

5. **EsSalud base coefficient interpretation.** The OLS EsSalud coefficient (0.2359, SE = 0.2039) is reported with the caution "we caution against interpreting this estimate." It should simply not appear as a result to be interpreted if the N = 648 is recognized as a misconstruction. Reporting it and flagging it in the same sentence risks selective citation by subsequent authors.

6. **R² of 0.02 and specification fit.** An R² of 0.02 is typical for health expenditure regressions, but in a paper where the central specification test is whether quantile effects are heterogeneous, reporting quantile-specific pseudo-R² (Koenker-Machado R₁(τ)) would demonstrate whether the CQR specification provides distributional fit beyond the mean.

7. **Rural SIS interpretation.** The finding of a *positive* SIS coefficient in rural areas (β = 0.0056, p = 0.016) is discussed as consistent with transport and medication costs under limited facility access. However, this is speculative without supporting evidence (e.g., utilization rates, facility distance). The interpretation should be confined to characterizing the association without claiming a mechanism.

---

### Recommendation

**Major Revision**

The paper has a clear research question, an appropriate distributional framework, and notably honest self-assessment. The methodological concerns above—particularly the EsSalud variable construction failure, mechanical circularity in quintile assignment, and insufficient bootstrap replications—are substantive but correctable. A revised version that addresses Major Concerns 1–3 (EsSalud recoding, quintile reconstruction, and bootstrap replication increase) would significantly increase confidence in the headline findings. Major Concerns 4–5 (multiple testing and falsification) are also required for the significance claims to be credible. The minor concerns are largely presentational and involve adding results that are straightforward to compute.

---

```json
{
  "score": 63,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "identification_strategy": 57,
    "estimation_implementation": 64,
    "statistical_inference": 53,
    "robustness_sensitivity": 67,
    "replication_readiness": 71
  },
  "sanity_checks": {
    "sign": "PASS",
    "magnitude": "PASS",
    "dynamics": "NA",
    "consistency": "FAIL"
  },
  "major_comments": [
    "EsSalud N=648 is implausibly small (~2% coverage vs ~30% national) and likely reflects variable misconstruction; contaminated uninsured reference group biases all SIS interaction estimates and requires diagnosis and correction before results are credible.",
    "Consumption quintiles are constructed from GASHOG2D, the OOP share denominator, creating mechanical circularity that inflates the quintile gradient and confounds insurance-quintile interactions even under a descriptive framing; quintile reconstruction using non-health consumption is required.",
    "200-replication cluster bootstrap is explicitly self-described as below publishable standard, yet headline findings (SIS×Q5 = -1.94pp, p<0.01 at τ=0.90) rest on these replications; re-estimation with ≥999 replications is necessary before significance conclusions at upper quantiles can stand.",
    "No multiple testing correction applied across the family of 5 quantiles × multiple interaction terms × 25 robustness checks; Holm-Bonferroni or Benjamini-Hochberg adjustment is required to assess whether significant interaction terms survive familywise error rate control.",
    "The primary placebo (random treatment reassignment) is self-acknowledged as uninformative; a non-health expenditure share falsification test is essential and is deferred without justification to 'future work.'"
  ],
  "minor_comments": [
    "Title promises 'Middle-Income Squeeze' but the paper's own findings refute this hypothesis in favor of a monotonic regressive gradient; title should reflect results, not the motivating hypothesis that was rejected.",
    "Two-part model (extensive + intensive margin) is relegated to a 'complement' despite the 44.1% zero-OOP mass making it arguably the more appropriate primary specification; full TPM results should be presented.",
    "P41603 ('other health costs') is flagged as a high-variance driver of upper-quantile estimates but no sensitivity to excluding it appears in the 25 robustness checks — an obvious and computationally trivial addition.",
    "RIF unconditional quantile regression is discussed as 'future work' but the paper's policy conclusions about targeting OOP distribution monitoring require population-level (unconditional) estimates; at least one RIF quantile should be reported.",
    "Koenker-Machado pseudo-R₁(τ) should be reported alongside OLS R² to demonstrate distributional fit quality at each estimated quantile.",
    "Rural SIS positive association (β=0.0056) is attributed to transport/medication access barriers without supporting evidence; interpretation should be confined to describing the association without asserting a mechanism.",
    "EsSalud OLS coefficient (0.2359, SE=0.2039) should either be corrected or omitted from results tables entirely to prevent selective citation; presenting it with a caveat is insufficient given the known variable construction failure."
  ]
}
```