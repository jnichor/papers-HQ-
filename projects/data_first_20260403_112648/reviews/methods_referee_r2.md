## Referee Report

**Journal: [Development Economics / Labor Economics]**
**Manuscript: "Wage Subsidies, Vocational Training, and Their Interaction: A Factorial Randomized Experiment among Young Men in Jordan"**

---

### Summary of Methodology

This paper exploits a 2×2 factorial RCT among approximately 1,260 young Jordanian men to estimate the main effects of a 6-month wage voucher (~200 JD/month) and a short vocational training course, and their interaction. The primary estimating equation is a linear probability model with OLS, HC2 standard errors, and an ANCOVA variant controlling for baseline covariates. Asymptotic inference is complemented by permutation tests (10,000 draws) and Benjamini-Hochberg FDR correction; Lee bounds are reported for attrition robustness.

---

### Main Methodological Assessment

The identification strategy is the strongest possible for this research question: random assignment in a factorial design yields unbiased estimates of both main effects and the interaction term without reliance on any selection-on-observables assumptions. The core findings—a massive midline voucher effect (β = 0.399, d = 0.88) that fades to near zero by endline, persistent null training effects, and additive rather than superadditive combined effects—are internally coherent and confirmed by the independently verified code output. The inference toolkit (permutation p-values, BH correction, Lee bounds) is well-matched to the research design and the multiple-testing environment.

However, I have identified **multiple verifiable numerical discrepancies** between the estimates reported in the paper's tables and the estimates produced by the verified analysis code. These are not rounding differences; in several cases they affect the sign, magnitude, or significance of reported coefficients. Additional omissions—most importantly the absence of a compliance/take-up analysis and LATE estimation—limit the interpretive content of the ITT results. These issues require major revision before the paper can be published.

---

### Major Concerns

**1. Numerical discrepancies between paper tables and verified code output (Critical)**

Cross-referencing the paper's regression tables against the independently verified evidence packet reveals discrepancies in multiple cells. The most significant:

| Location | Paper reports | Evidence packet shows |
|---|---|---|
| Table 3, end_lfp, V×T | −0.048 (SE = 0.054, p = 0.377) | −0.058 (SE = 0.057, p = 0.305) |
| Table 3, end_salary, Training | 2.15 (p not shown) | 0.490 (SE = 6.105, p = 0.936) |
| Table 3, end_salary, V×T | −5.41 (SE = 9.14, p = 0.554) | −2.871 (SE = 9.362, p = 0.759) |
| Table 2, midline emp., N | 1,243 | 1,207 |
| Table 3, endline emp., N | 1,207 | 1,255 |

These discrepancies suggest the paper's tables reflect an earlier or alternative analysis run than the code that produced the evidence packet. **The authors must reconcile all reported estimates with their final analysis code, provide a version-controlled replication package, and explain any legitimate reason for differences (e.g., different specification, sample restriction).** Discrepancies in interaction terms and training coefficients are particularly consequential given the paper's central claim about additivity.

**2. Balance table statistics conflict with the actual data**

The paper's Table 1 reports mean age as 23.1–23.6 across arms and control-group N ≈ 400. The verified balance table from the code shows mean age ≈ 21.1–21.3 and control-group N ≈ 440–449. Similarly, the paper labels the education covariate as "years of education" with means of ~11.7–11.9, but the actual variable (`b_communitycollege`) is an ordinal 1–8 scale with means of ~4.4–4.6. **The authors must either correct Table 1 to reflect the actual data or provide a detailed crosswalk explaining which underlying variables map to each reported summary statistic.** Discrepancies in age means of ~2 years and in education variable definitions are not labeling issues—they represent substantively different information.

**3. Missing compliance and take-up analysis; no LATE estimation**

The paper reports intent-to-treat (ITT) effects throughout but never reports take-up rates: What fraction of voucher-arm participants redeemed the voucher? What fraction of training-arm participants completed training? These figures are essential for two reasons. First, they determine the scaling factor between ITT and LATE/TOT, which governs the implied per-complier cost-effectiveness. Second, differential take-up across the factorial arms could itself be informative about barriers to program adoption. The strategy memo explicitly planned a "LATE/2SLS using assignment as instrument for take-up," but this analysis does not appear in the paper. **The authors should report take-up rates by arm, compute TOT estimates via 2SLS, and reconcile why the planned LATE analysis was omitted.** If compliance was near 100%, this should be stated explicitly—it would itself be a notable finding.

**4. Unexplained reversal of sample size between midline and endline**

The evidence packet shows more observations at endline (N ≈ 1,255 for employment) than at midline (N ≈ 1,207). In a standard longitudinal panel, sample size monotonically decreases across waves due to attrition. The reversal here is unexplained and suggests either (a) participants who missed the midline survey were recovered at endline, (b) the midline and endline use different sampling frames, or (c) a data-processing error. **The authors must explain the wave-by-wave structure of the panel, the criteria for inclusion in each regression sample, and why attrition did not reduce the endline sample below the midline sample.** This is directly relevant to the paper's attrition analysis, which assumes moderate and non-differential attrition.

**5. The 975 excluded observations require justification**

The paper states "The full dataset contains 2,322 observations. Of these, 1,347 have valid treatment status...The remaining 975 observations lack treatment assignment and are excluded." This is a large share (42%) of the dataset with no treatment status. The authors offer no explanation for why nearly half the sample lacks treatment assignment. **The authors must describe who these 975 individuals are** (waitlisted, ineligible at screening, pre-randomization dropouts?), whether their exclusion is exogenous to potential outcomes, and whether the 1,347-observation analysis sample is representative of the enrolled population. An analysis of characteristics of excluded versus included individuals should be added to the appendix.

---

### Minor Concerns

1. **Cohen's d for binary outcomes.** The paper applies the standard Cohen's d formula (difference in proportions divided by pooled SD) to binary outcomes. For proportions, Cohen's h (the arcsine-transformed difference) is the appropriate effect size measure, as the SD of a binary variable is mechanically tied to its mean, making d misleadingly large when proportions are far from 0.5. At control-group employment of 0.178, the SD is ~0.383, inflating d relative to what it would be at a 50% baseline. The authors should either use Cohen's h or explicitly acknowledge this limitation.

2. **BH correction family not specified.** The authors invoke the Benjamini-Hochberg procedure but do not define the full test family over which it is applied. The evidence packet contains 15 tests (5 outcomes × 3 treatment indicators); it is not clear whether the BH correction is applied within outcomes, within time points, or globally. **Define the family of hypotheses explicitly** and provide the full ranked list of raw and adjusted p-values in an appendix.

3. **Unbalanced factorial design and OLS weighting.** The control arm (N ≈ 440) is substantially larger than the treatment arms (N ≈ 290–300). In an unbalanced 2×2 factorial, OLS estimates of β₁ and β₂ are not simple averages of the four cell contrasts—they are implicitly weighted by cell sizes. This is not an error, but the authors should acknowledge it and verify that results are robust to estimating arm-specific contrasts directly (e.g., "Both" minus "Control" as an unweighted measure of the combined effect).

4. **No pre-analysis plan cited.** The paper does not reference a pre-registered analysis plan. While the paper pre-specifies four moderators for heterogeneity analysis and applies BH correction, the reader has no way to assess whether the set of outcomes, the BH correction family, or the heterogeneity moderators were chosen before or after observing the data. A pre-analysis plan citation (or an honest statement of its absence) would strengthen the paper's credibility.

5. **Midline LFP not treated as a primary outcome.** The evidence packet shows midline LFP means (Control = 0.771, Voucher = 0.799, Both = 0.853), and the logit results indicate the voucher has OR = 1.18 on midline LFP (not significant). The paper discusses midline LFP only implicitly. Including it in the main tables would complete the picture of within-period substitution between employment and participation.

6. **b_examresult vs. Tawjihi pass indicator.** The balance table in the evidence packet shows `b_examresult` as a continuous variable with mean ≈ 62.4 and SD ≈ 3.2, but the paper's ANCOVA controls include "an indicator for having passed the Tawjihi exam." Clarify whether the regression uses a binary pass/fail indicator or the continuous score; these are substantively different variables.

7. **Reservation-wage mechanism is testable.** The paper discusses three fade-out mechanisms (employer learning, demand constraint, reservation wages) but treats them as observationally equivalent given the data. In fact, the reservation-wage mechanism predicts that workers who fail to find employment at endline should show higher reservation wages than control workers. If the survey collected any data on minimum acceptable wages or reasons for not working, even a simple descriptive test would help discipline the mechanism discussion.

8. **End_salary Lee bounds inconsistency with point estimate.** The paper argues that strictly positive endline salary Lee bounds [+1.26, +18.94] demonstrate a "robust salary gain at endline," but the OLS point estimate (6.95 JD, p = 0.273) is not statistically significant. The conjunction of a non-significant point estimate with strictly positive worst-case bounds is worth explaining carefully—Lee bounds and OLS are addressing different threats, so they need not agree—but the paper should clarify that the bounds are about attrition bias, not a substitute for statistical significance.

---

### Recommendation: **Major Revision**

The paper addresses an important policy question with an appropriate design and produces substantively interesting results. The identification strategy is the strongest available, and the core findings are supported by the verified data. However, the numerical discrepancies between reported tables and the verified code output are a non-negotiable issue that must be resolved. The missing take-up and LATE analysis, the unexplained exclusion of 975 observations, and the incorrect balance table statistics also require substantive revision. I am prepared to reconsider for publication once these issues are addressed.

---

```json
{
  "score": 72,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "identification_strategy": 88,
    "estimation_implementation": 68,
    "statistical_inference": 74,
    "robustness_sensitivity": 72,
    "replication_readiness": 58
  },
  "sanity_checks": {
    "sign": "PASS",
    "magnitude": "PASS",
    "dynamics": "PASS",
    "consistency": "FAIL"
  },
  "major_comments": [
    "Multiple verifiable numerical discrepancies between paper tables and evidence packet: end_lfp interaction (-0.048 paper vs -0.058 code), end_salary training coefficient (2.15 vs 0.490), end_salary interaction (-5.41 vs -2.871), and sample sizes (midline N=1,243 paper vs 1,207 code; endline employment N=1,207 paper vs 1,255 code). Requires reconciliation and versioned replication package.",
    "Balance table statistics conflict with actual data: paper reports mean age 23.1-23.6 and N=~300-400 per arm; evidence shows mean age ~21.1-21.3 and control N=~440-449. Education variable labeled 'years of education' (mean ~11.8) but actual variable is an ordinal 1-8 scale (mean ~4.4-4.6).",
    "No compliance/take-up rates reported and no LATE/TOT estimation, despite this being explicitly planned in the strategy memo. ITT estimates cannot be interpreted on a per-complier basis without these.",
    "Sample size increases from midline (N≈1,207) to endline (N≈1,255), which is inconsistent with standard panel attrition. The mechanism must be explained and validated.",
    "975 observations (42% of full dataset) are excluded for missing treatment assignment with no explanation of who these individuals are or whether their exclusion is exogenous."
  ],
  "minor_comments": [
    "Cohen's d applied to binary outcomes inflates effect size when proportions are far from 0.5; Cohen's h is the appropriate measure for proportions.",
    "BH correction family is not explicitly defined; the full ranked list of raw and adjusted p-values should appear in an appendix.",
    "Unbalanced factorial design (control N≈440 vs. treatment N≈290) means OLS β1 and β2 are implicitly cell-size-weighted; robustness to equal-weighted contrasts should be shown.",
    "No pre-analysis plan is cited; authors should either reference a registration or clearly state the analysis was not pre-registered.",
    "Midline LFP should be included as a primary outcome in Table 2 for completeness.",
    "ANCOVA specification description refers to 'an indicator for Tawjihi pass' but evidence packet shows b_examresult is a continuous score (mean ~62.4); clarify which variable is actually used.",
    "The reservation-wage fade-out mechanism could be partially tested if the survey collected data on minimum acceptable wages or job-search reasons; even a descriptive check would be informative.",
    "Strictly positive endline salary Lee bounds alongside a non-significant OLS estimate requires clearer exposition of what each addresses."
  ]
}
```