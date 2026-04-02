## Referee Report

**Manuscript:** "Did ChatGPT Concentrate or Diversify the Programming Language Ecosystem? A Country-Level Event Study"

---

### Summary of Methodology

The paper uses a country-level panel of GitHub push activity (177 countries, 23 quarters, Q1 2020–Q3 2025) to study whether ChatGPT's release in November 2022 altered the concentration of programming language ecosystems, as measured by normalized HHI and Shannon entropy. The authors implement a within-country event study centered on Q1 2023 with country fixed effects, supplement it with cross-sectional heterogeneity analysis using English proficiency scores, and subject the results to an extensive robustness battery. The headline finding is appropriately cautionary: the baseline result is not robust to country-specific trends, placebo timing tests yield similar magnitudes, and composition effects mechanically account for most of the raw HHI change.

---

### Main Methodological Assessment

The paper is admirably honest about its null conclusion and the limits of its design. The robustness analysis is thorough and credibly undermines the causal interpretation of the baseline result. However, several fundamental issues compromise the methodology: (1) the design is an interrupted time series (ITS), not a difference-in-differences or event study in the standard sense, yet the paper frames it in DiD language throughout; (2) there are internal numerical inconsistencies between the reported event study coefficients and the ATT estimates that appear irreconcilable and may indicate a computational error; and (3) the sign reversal in the composition-adjusted specification is understated and carries important substantive implications.

---

### Major Concerns

**1. The design is ITS, not DiD; the DiD/ATT framing is misleading throughout.**

The paper correctly acknowledges in Section 3.1 that "event-time dummies are equivalent to calendar-quarter dummies" when treatment is universal and simultaneous, and that they "cannot include both event-time dummies and quarter fixed effects." This admission effectively concedes that the estimator is an interrupted time series (ITS) with country fixed effects, not a difference-in-differences. However, the paper then repeatedly uses ATT notation, references "the treated" (who are all units?), calls the result a "DiD estimate" (Section 4.2), and frames the identification around the timing assumption as though there is a clean parallel-trends structure.

**Specific suggestion:** Reframe Section 3 to be explicit that this is ITS. Replace "ATT" with "ITS estimate" or "within-country pre-post change." Remove DiD language. The identification assumption should be stated as: "Absent ChatGPT, within-country HHI would have continued on its pre-treatment trend." This is weaker than a parallel trends assumption and the paper should treat it as such. The robustness results (placebo tests, country trends) already speak to this assumption—they should be framed in ITS terms.

**2. Internal inconsistency between event study coefficients and ATT estimates (potential computational error).**

Section 4.1 reports that post-treatment HHI coefficients "range from +0.039 to +0.079" and pre-treatment coefficients "range from +0.071 to +0.121," all described as statistically significant. These are reported as deviations from the reference period (Q3 2022, normalized to zero). Yet the reported ATT is −0.027, which would require the average post coefficient to be approximately 0.027 units *below* the average pre coefficient. Under the stated numbers, this is marginally consistent (avg post ≈ 0.059 minus avg pre ≈ 0.096 ≈ −0.037), but requires that the reference-period HHI is the *local minimum* of the entire series—that HHI was higher than the reference in every pre-treatment quarter AND in every post-treatment quarter. This is a remarkable claim that is nowhere discussed, and it implies that HHI *rose* through Q3 2022 and then *rose further* in the post-period, but by less. That would be a *re-acceleration* of concentration post-ChatGPT, not diversification.

The entropy figures are even more problematic. The text reports post-treatment entropy coefficients "ranging from +2.53 to +2.79." The mean entropy in the full sample is 2.49. For coefficients representing *deviations from a reference quarter* to reach +2.53, the reference quarter (Q3 2022) would require entropy near zero, which is impossible given the minimum observed value is approximately 1.10. This strongly suggests the code may be reporting level estimates (fitted values or quarterly means) rather than deviation-from-reference coefficients, which would be a fundamental computational error.

**Specific suggestion:** The authors must verify whether Figure 2 and the coefficient values cited in Section 4.1 represent (a) deviations from the reference period (the correct interpretation for equation 1) or (b) fitted values / quarterly means. If the latter, this is a critical bug. The ATT calculation method (is it the average of the post event-study coefficients minus the average of the pre coefficients? Or a separate pooled regression?) must be explicitly stated and verified to be consistent with the reported coefficient values.

**3. The composition-adjusted sign reversal is unexplained and substantively important.**

Table 2 shows that the composition-adjusted HHI ATT is +0.002 (p = 0.021), a 93% reduction *and a sign reversal* from the baseline ATT of −0.027. The text characterizes this as "a 93% reduction" but buries the sign flip in a parenthetical. Similarly, the "Min 3 languages" specification yields ATT = +0.007 (p < 0.001) for HHI—again positive (concentration), opposite to the baseline.

This sign reversal has a direct substantive interpretation: once you hold the composition of languages constant, the behavioral effect is *concentration*, not diversification. That is, when new languages enter the observed set post-ChatGPT (inflating the denominator of HHI), the mechanical effect dominates and creates apparent diversification. Conditional on a fixed language set, developers concentrated further in dominant languages. This is arguably the paper's most interesting finding and it is currently understated.

**Specific suggestion:** Devote a dedicated subsection to the composition-adjusted results. Clearly state that the sign reversal implies behavioral concentration once composition effects are netted out. Discuss whether this is consistent with the hypothesis that ChatGPT, by lowering barriers in mainstream languages, *increased* dominance of high-quality languages in developer activity—the opposite of the headline claim.

**4. Pre-treatment trend violation is treated as a "diagnostic" but it invalidates the design.**

The paper correctly notes that pre-treatment event study coefficients are "uniformly positive and significant, with magnitudes comparable to the post-treatment estimates." This is not merely a caution—it is a direct violation of the key ITS/pre-trend assumption. If the pre-treatment deviation pattern looks identical to the post-treatment pattern, the design provides zero identification of a ChatGPT-specific effect, regardless of what the post-treatment coefficients show. The paper partially addresses this through placebo tests and country trends, but does not sufficiently emphasize that the pre-trend failure means the baseline result should carry *no evidential weight* for causality—not merely "reduced confidence."

**Specific suggestion:** Restructure the results section to lead with the pre-trend violation and explicitly state that the baseline result is therefore uninformative about causality. The contribution of the paper lies in the robustness checks, not the baseline estimate.

---

### Minor Concerns

1. **ATT computation formula is never stated.** The paper reports ATT estimates throughout but never defines the aggregation formula. Is this the average of post-period event study coefficients, a separate pooled DiD regression, or the weighted average of quarterly contrasts? This must be stated for replication.

2. **EPI sample exclusions bias the heterogeneity analysis.** The 54 countries excluded from the EPI merge include the US, UK, Australia, Canada, and New Zealand—likely the highest-volume GitHub users in the sample. Excluding native English speakers from an English-proficiency heterogeneity test biases the comparison toward non-English countries and severely limits the external validity of the null heterogeneity finding.

3. **COVID pre-period contamination is understated.** The entire pre-treatment window (Q1 2020–Q3 2022) coincides with COVID-19. The paper lists this as a threat but does not show whether the country-specific trend results are sensitive to dropping 2020 from the pre-trend window. An additional robustness check using only Q1 2021–Q3 2022 as the "clean" pre-period would be informative.

4. **Sample loss between full panel and event study figures is unexplained.** The full panel has 3,586 observations; the event study figure caption reports 3,428. The difference (158 observations) cannot be explained solely by dropping Q4 2022 (which would remove approximately 177 observations if balanced). The missing observations should be accounted for.

5. **The "first full treatment quarter" Q1 2023 is chosen without robustness.** ChatGPT was released on November 30, 2022 (essentially Q4 2022). Designating Q1 2023 as "t=0" is reasonable but arbitrary. A check treating Q4 2022 as the first treatment quarter (or using the paper's proposed 1/3 fractional indicator) should be included in the robustness table and appears to be missing despite being proposed in the strategy memo.

6. **Shannon entropy units are inconsistent with ATT scale.** Mean entropy is 2.49; the reported baseline ATT is +0.251. This represents a 10% increase in entropy units, which may or may not be economically meaningful—but the paper provides no benchmark for interpreting entropy changes. A comparison to the inter-quartile range of entropy (approximately 3.46 − 1.10 = 2.36) would help readers calibrate the magnitude.

7. **No power calculation for null heterogeneity finding.** The EPI heterogeneity analysis is the paper's only source of cross-sectional identification. With 78.2% sample coverage and the most GitHub-active countries excluded, the analysis may be substantially underpowered to detect differential effects of realistic magnitude. The paper should report minimum detectable effects.

---

### Recommendation: **Major Revision**

The paper makes a genuine contribution by demonstrating that apparent post-ChatGPT diversification is spurious, driven by pre-existing trends and composition effects. The honest null conclusion is credible and well-supported by the robustness battery. However, the methodological framing requires substantial revision: the DiD/event study language misrepresents an ITS design; the internally inconsistent coefficient values require verification and likely correction; and the substantively important sign reversal in composition-adjusted results must be properly analyzed rather than downplayed. These are addressable concerns that do not require new data collection, but they require careful re-estimation, re-writing of the empirical strategy section, and reorientation of the main findings around the composition-adjusted results.

---

```json
{
  "score": 66,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "identification_strategy": 60,
    "estimation_implementation": 58,
    "statistical_inference": 68,
    "robustness_sensitivity": 74,
    "replication_readiness": 68
  },
  "sanity_checks": {
    "sign": "PASS",
    "magnitude": "PASS",
    "dynamics": "FAIL",
    "consistency": "FAIL"
  },
  "major_comments": [
    "Design is ITS not DiD: simultaneous universal treatment with no control group means event-time dummies are collinear with quarter FEs; the 'ATT' framing and DiD language are misleading throughout and must be replaced with ITS terminology.",
    "Internal inconsistency between event study coefficients and ATT estimates: entropy coefficients of +2.53 to +2.79 are impossible as deviations from a reference quarter given mean entropy of 2.49; HHI coefficient pattern implies reference period is a local minimum yet the paper describes this as diversification — likely a computational error reporting level estimates instead of deviation-from-reference coefficients.",
    "Sign reversal in composition-adjusted HHI (baseline ATT = -0.027 vs. composition-adjusted ATT = +0.002) and in 'Min 3 languages' (+0.007) implies behavioral concentration once mechanical language-entry effects are removed; this reversal is understated and carries the paper's most important substantive implication.",
    "Pre-treatment trend violation is severe: pre-treatment event study coefficients are uniformly significant with magnitudes comparable to post-treatment, directly invalidating the timing assumption; the baseline result carries no evidential weight for causality and should be presented as such rather than as the lead finding."
  ],
  "minor_comments": [
    "ATT aggregation formula is never stated; must define whether this is average of post-period event study coefficients, a pooled DiD regression, or another estimator.",
    "EPI sample exclusion of native English-speaking countries (US, UK, AU, CA, NZ) biases the heterogeneity analysis toward non-English countries, limiting interpretation of the null result.",
    "No robustness check dropping 2020 (COVID onset) from the pre-trend window; the COVID-contaminated baseline makes it impossible to establish a stable counterfactual trend.",
    "Sample loss of 158 observations between full panel (3,586) and event study figure (3,428) is unexplained and cannot be accounted for solely by dropping Q4 2022.",
    "Q4 2022 fractional treatment indicator (proposed in strategy memo) is absent from the robustness table despite being a natural sensitivity check.",
    "No power calculation for the EPI heterogeneity analysis; with key high-GitHub-activity countries excluded, the null differential result may reflect insufficient power rather than absence of heterogeneity."
  ]
}
```