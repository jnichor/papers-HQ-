## Referee Report

**Journal:** [Anonymous Review]
**Paper:** "Apartheid or Persecution? A Randomized Experiment on the Effect of Legal Labels on Public Support for ICC Accountability"

---

### Summary of Methodology

The paper employs a two-arm randomized vignette experiment (N=784) to estimate the average treatment effect of legal label choice — "apartheid" versus "persecution" — on U.S. respondents' support for ICC accountability. Random assignment provides clean identification; the ATE is estimated across three specifications (raw difference-in-means with HC2 standard errors, OLS with baseline controls, and double LASSO), supplemented by Fisher permutation inference, ordered probit, binary logit, Lee attrition bounds, and CATE analysis across quintiles of a pre-treatment pro-Israel attitude index, with Benjamini–Hochberg correction for multiple comparisons.

---

### Main Methodological Assessment

The identification strategy is the paper's strongest feature: randomization renders the raw difference-in-means an unbiased estimator of the ATE under mild assumptions, and the balance checks broadly confirm covariate equivalence. The estimation suite is appropriate, the point estimates are remarkably stable across specifications (range: 0.008 SD), and the use of permutation inference alongside parametric testing is exemplary. However, four issues materially affect the interpretation of results and require revision before publication: (1) the Lee bounds are misinterpreted in a way that inverts the paper's own conclusion; (2) the composite outcome index is underspecified; (3) the balance table incorporates the pre-cleaned education outlier, undermining the balance claim; and (4) the absence of a manipulation check leaves the null ambiguous between a true null and an attention failure. The lack of pre-registration, combined with several post-hoc heterogeneity dimensions explored in the robustness section, is an acknowledged but insufficiently addressed concern.

---

### Major Concerns

**1. Critical misinterpretation of Lee attrition bounds.**
The paper reports Lee bounds of [−0.118, −0.053] and states that "both bounds are negative and the interval excludes zero, suggesting that even under differential attrition the treatment effect is weakly negative." This framing is internally inconsistent with the paper's own null-result claim. If the Lee bounds point estimates both lie strictly below zero, and if those estimates were statistically precise, this would constitute *evidence of a significant negative treatment effect* — not support for a null. The paper treats a tightly negative pair of bounds as consistent with its null conclusion, which is incorrect.

More fundamentally, the authors report only the *point estimates* of the trimming-based bounds, not their standard errors or confidence intervals. Lee (2009) bounds are themselves estimated quantities with sampling uncertainty. To assess whether the bounds exclude zero in a statistically meaningful sense, one must construct confidence intervals for each bound (e.g., via the delta method or bootstrap). Without these, the claim that the bounds "exclude zero" is unsubstantiated. Additionally, with reported attrition of only 3.1% that is described as balanced across arms, bounds this far from the main estimate warrant explanation — the trimming fractions implied should be reported.

*Required action:* Report standard errors and 95% CIs for both Lee bounds. Interpret the bounds correctly: if both CI endpoints are negative and exclude zero, this strengthens the case for a negative effect, not a null. If CI intervals for the bounds do overlap with zero, state that explicitly.

**2. Composite outcome index is underspecified.**
The primary outcome is described as a "standardized composite index" of three survey items (investigate, issue arrest warrants, support cooperation), but the paper provides no information on: (a) the response scale for each component; (b) whether items are equally weighted or combined via factor loadings; (c) the internal reliability (Cronbach's alpha or omega) of the composite; and (d) effects on individual components separately. An index with α < 0.70 would raise concerns about construct validity. Furthermore, if the three components have substantially different variances or distributional shapes, simple averaging is not neutral.

*Required action:* Report Cronbach's alpha and the correlation structure of the components. Report treatment effects on each component separately (perhaps in an appendix) to assess whether the null is uniform across index dimensions or averages out heterogeneous effects.

**3. Balance table uses pre-winsorized education data.**
The balance table (Table 1 equivalent) reports mean education of −11.035 in the treatment arm and +4.627 in the control arm — a difference of −15.662 that is clearly driven by the respondent with education = −3105, which the paper acknowledges as a data entry error and winsorizes in all analytic specifications. Presenting a balance check that relies on the raw, corrupted variable is misleading: it implies the treatment and control groups are unbalanced on education (SMD = −0.101), when the winsorized data would show balance. Separately, the `over_65` indicator shows p = 0.037 (SMD = −0.149) — the only marginally significant covariate. The paper claims all 126 covariates pass balance "after adjusting for multiple comparisons," but does not specify which adjustment procedure was applied to the balance check, nor whether `over_65` passes after adjustment.

*Required action:* Re-run the balance table using the winsorized/cleaned analytic sample. Explicitly state the multiple-testing procedure applied to the full set of 126 balance tests and confirm whether `over_65` passes after correction.

**4. Absence of a manipulation check.**
The paper reports a null ATE and interprets it as evidence that label choice does not move opinion. However, there is no evidence that respondents read the vignette carefully or noticed the label. In online survey experiments, inattentive respondents who skim or skip text would mechanically produce a null — not because labels don't matter, but because the manipulation was not processed. Without a manipulation check (e.g., "Which label was used to describe the policies?" or a comprehension question), the null is ambiguous between a true null and treatment non-receipt.

*Required action:* Report attention check or manipulation check pass rates. If no manipulation check was embedded in the survey, acknowledge this explicitly as a limitation and discuss what share of respondents were flagged as inattentive by any platform-side quality filters (e.g., speeder flags, response pattern checks). Analyze ATE restricted to high-attention subsamples if such filters are available.

**5. Multiple exploratory heterogeneity dimensions without pre-registration disclosure.**
The paper correctly states it was not pre-registered. However, the robustness section explores CATEs across three separate moderators: (a) pro-Israel attitude quintiles, (b) hawkishness quintiles, and (c) hostile sexism tertiles — yielding 15 subgroup estimates. BH correction is applied *within* each moderator's family of tests, but not *across* moderator families. The hawkishness Q2 estimate (−0.310, p = 0.031) that does not survive within-family BH correction is mentioned multiple times in the paper (Section 5, Discussion, and Conclusion) in ways that may leave readers with an impression of heterogeneity that the evidence does not support. With no pre-registration and 15 exploratory tests across three moderator dimensions, the family-wise error rate is materially elevated.

*Required action:* Either apply a single BH/Holm correction across all 15 subgroup estimates reported in the paper, or explicitly acknowledge that CATE analyses across moderators are purely exploratory and remove the repeated emphasis on the hawkishness Q2 finding. At minimum, a single footnote summarizing the joint null of homogeneity across all three moderators would improve transparency.

---

### Minor Concerns

1. **Sample size discrepancy in Table 1 note.** The table note states N=784 (398 treated, 386 control), but the analytic sample is N=760 (759 with controls). The table note should reflect the actual estimation sample and explain the 24-observation reduction.

2. **Ordered probit scale.** The ordered probit coefficient (−0.072) is not directly comparable to the OLS estimate in standard deviation units. The table caption or note should clarify this is a latent-scale coefficient, and ideally report a marginal effect or rescale to facilitate comparison.

3. **Double LASSO selected controls not reported.** The paper employs double LASSO selecting from 126 variables but does not report which controls were selected. This is a transparency gap, particularly given the lack of pre-registration. An appendix listing selected variables would allow readers to assess whether the selection is sensible.

4. **CI precision in abstract.** The abstract states "the 95% confidence interval rules out effects larger than 0.22 SD in magnitude," but the reported CI is [−0.217, +0.061]. The upper bound is +0.061, not 0.22. The 0.22 refers to the magnitude of the lower bound. The phrasing is technically defensible but imprecise — a reader could infer the paper rules out any effect above 0.22 SD in absolute value, when in fact it only rules out effects more positive than +0.06 and more negative than −0.22. Clarify that the CI is asymmetric and rules out a *positive* effect of 0.06 SD or larger.

5. **No survey weights.** The data audit flags the absence of survey weights. The paper recruits from an online platform; if the platform provides post-stratification weights (as most do), their omission should be acknowledged as a potential limitation for external validity. Results may not generalize to the U.S. adult population.

6. **Vignette pre-testing details absent.** The paper mentions the vignette "was pre-tested for comprehension" but provides no details. Who was pre-tested? What was the sample size? What did comprehension questions reveal? This information would strengthen the design section.

7. **Mechanism discussion could be strengthened.** The three mechanisms proposed (label redundancy, crystallized attitudes, limited public connotations) are plausible but untested. Even descriptive evidence on respondents' awareness of the South Africa–apartheid association would help discriminate among them.

---

### Recommendation

**Minor Revision**

The paper's identification strategy is sound, its null result is credibly estimated, and its approach to inference (permutation tests, multiple-testing corrections, equivalence framing) is largely exemplary. The major concerns — particularly the Lee bounds misinterpretation, the underspecified index, and the manipulation check gap — are addressable without new data collection. The multiple exploratory CATE dimensions require only more careful framing. I would expect to accept the revised version without further major review.

---

```json
{
  "score": 76,
  "decision": "MINOR_REVISIONS",
  "dimension_scores": {
    "identification_strategy": 86,
    "estimation_implementation": 70,
    "statistical_inference": 74,
    "robustness_sensitivity": 72,
    "replication_readiness": 68
  },
  "sanity_checks": {
    "sign": "PASS",
    "magnitude": "PASS",
    "dynamics": "NA",
    "consistency": "PASS"
  },
  "major_comments": [
    "Lee attrition bounds are presented as point estimates only (no SEs or CIs), and are misinterpreted: bounds of [-0.118, -0.053] that exclude zero would constitute evidence of a significant negative effect, not support for a null. CIs for the bounds must be constructed and correctly interpreted.",
    "Composite outcome index is underspecified: response scales, weighting scheme, and Cronbach's alpha are not reported; effects on individual components are not shown.",
    "Balance table uses pre-winsorized education data (Mean T = -11.035 vs Mean C = 4.627), making it invalid as a balance check. The over_65 imbalance (p=0.037) and the multiple-testing correction procedure applied to all 126 balance tests should be explicitly described.",
    "No manipulation check is reported. An online null result is ambiguous between a true null and treatment non-receipt from inattentive respondents.",
    "Multiple heterogeneity dimensions (pro-Israel quintiles, hawkishness quintiles, hostile sexism tertiles, yielding 15 subgroup estimates) are explored post-hoc without pre-registration, with BH correction applied only within moderator families. The hawkishness Q2 finding (-0.310, p=0.031) is mentioned repeatedly in a way that overstates its evidentiary weight."
  ],
  "minor_comments": [
    "Table 1 note reports N=784 but analytic sample is N=760; the discrepancy should be explained in the table note.",
    "Ordered probit coefficient is not comparable to OLS SD-unit estimates; report a marginal effect or note the scaling difference explicitly.",
    "Double LASSO selected controls should be listed in an appendix for transparency.",
    "Abstract CI phrasing ('rules out effects larger than 0.22 SD in magnitude') obscures asymmetry of the CI [-0.217, +0.061]; the positive bound is only +0.061.",
    "Absence of survey weights should be acknowledged as a limitation for external validity to the U.S. adult population.",
    "Vignette pre-testing details (sample, comprehension pass rate) are mentioned but not reported.",
    "Mechanism discussion (redundancy, crystallized priors, limited connotations) is plausible but untested; even descriptive evidence on respondent awareness of South Africa associations would help discriminate."
  ]
}
```