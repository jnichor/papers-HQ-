## Referee Report — Round 2 Review

**Paper:** "Wage Subsidies vs. Vocational Training for Young Men: Experimental Evidence from a Factorial Randomized Controlled Trial"

---

### Summary of Methodology

The paper evaluates a 2×2 factorial RCT cross-randomizing employment vouchers and vocational training among 1,347 young men, estimating main effects and their interaction via OLS with HC2 standard errors. Robustness checks include permutation inference, Lee bounds, logit re-estimation, and covariate sensitivity analysis. Relative to Round 2, the revision has corrected the education variable description and achieved broad numerical consistency with the underlying data evidence packet, resolving several prior editorial concerns.

---

### Overall Assessment

The revision demonstrates genuine responsiveness to editorial feedback on education variable labeling and numerical consistency. However, three of the six "must-address" concerns from Round 2 remain substantively unresolved: the unexplained increase in sample size from midline to endline; the complete absence of compliance rates and LATE estimates (pre-specified in the research strategy); and the dramatic, unexplained 29 percentage point decline in control-group LFP between waves—the very benchmark against which the paper's headline persistence finding is measured. Until these gaps are addressed, the endline causal interpretation rests on an uncertain foundation.

---

### Major Concerns

**1. Sample size increase from midline to endline remains unexplained.**

The effective regression sample rises from N=1,207 at midline to N=1,255 at endline—an *increase* of 48 observations. Standard panel attrition predicts monotone decline. The revision makes no attempt to account for this anomaly beyond noting that sample sizes "vary across outcomes due to differential item non-response." The authors must document: (a) the exact mechanism by which individuals appear at endline but not midline (re-contact, refreshment sample, administrative record linkage?); (b) whether these "late-appearing" observations are balanced across treatment arms; and (c) whether restricting endline estimates to the balanced subsample observed at both waves materially changes the coefficients. Without this, the endline and midline estimates are not measuring outcomes for the same underlying population, and the fade-out comparison is confounded.

**2. No compliance rates and no LATE estimates, despite pre-specification.**

The paper remains entirely intent-to-treat. The research strategy memo explicitly pre-specified LATE/TOT estimation via 2SLS using assignment as an instrument for program take-up, yet no first-stage statistics, take-up rates, or IV estimates appear anywhere in the revision. This is not a minor omission: ITT estimates mechanically understate per-complier effects, the discussion of fade-out mechanisms (Section 7.1) conflates subsidy expiration with behavioral responses that are only identifiable among compliers, and the cost-effectiveness framing in the conclusion is uninterpretable without per-complier scaling. The evidence packet confirms that `linearmodels` is working in the pipeline, so 2SLS is implementable. Authors should report: (a) take-up rates by arm with a first-stage table; (b) LATE estimates for at least employment and LFP at both horizons; and (c) revised welfare language conditioned on complier status.

**3. The 29 percentage point collapse in control-group LFP is never explained.**

Control-group LFP falls from 77.1% at midline to 48.0% at endline—a decline of 29.1 pp that is nearly three times the size of the persistent treatment effect the paper foregrounds. This collapse is the single most important threat to the endline LFP result (10.1 pp, p=0.008), which is the paper's primary persistence finding. A 10 pp effect relative to a collapsing control baseline may reflect differential compositional changes across arms, survey artifacts, seasonal factors, or differential attrition—not a lasting behavioral shift induced by vouchers. The revision acknowledges the 48.0% control mean without addressing its origin. Authors must provide: (a) evidence that the LFP question wording was unchanged across waves; (b) documentation of any seasonal or macroeconomic variation in the study period; (c) an attrition-by-arm table showing whether LFP declines are differentially concentrated among selective non-respondents; and (d) a sensitivity analysis restricting to balanced attritors. Until the control group's trajectory is explained, the headline endline LFP effect is not credibly interpretable.

**4. 975 excluded observations remain inadequately characterized.**

The revision adds a single sentence: "The remaining 975 individuals were excluded from randomization, *likely* due to eligibility screening or logistical constraints." The use of "likely" signals uncertainty that is inappropriate given the authors' direct access to implementation records. The authors must at minimum: (a) confirm whether baseline covariates exist for these individuals; (b) if so, compare their characteristics to the experimental sample and report an omnibus balance test; and (c) assess whether there is differential selection into the experimental sample on observables that correlates with the treatment assignment rule. The concern is not merely transparency—if the 975 were screened based on characteristics correlated with potential outcomes, the external validity of all effects is materially qualified.

---

### Minor Concerns

1. **Variable label for "education" remains ambiguous.** The evidence packet shows the balance table variable is `b_communitycollege`, which the paper relabels as "Education (1--8 scale)." A data appendix should clarify whether this variable encodes: (a) a community college institution identifier (i.e., a categorical fixed effect treated as numeric), (b) a constructed education-level index, or (c) something else. If it is a college code rather than an educational attainment measure, calling it "education" in the balance table remains misleading regardless of the scale description.

2. **No multiple testing correction across outcomes.** The paper tests eight primary outcomes (four at midline, four at endline) plus interaction terms—at least 10 hypothesis tests. The only statistically significant endline result, end_lfp (p=0.008), is the paper's headline persistence finding and is therefore the test most vulnerable to Type I error inflation. The pre-specified strategy memo listed Benjamini-Hochberg correction, which is absent. The authors should report q-values for all outcomes and verify that the LFP result survives FDR adjustment.

3. **Inconsistency in fade-out figure caption.** The caption for Figure 3 states the employment effect declines "from +0.396 to +0.034" and salary "from +64.796 to +7.713." The main regression table (Table 3, full-controls specification) reports endline employment = 0.030 and endline salary = 6.954. If the figure uses the no-controls specification and the table uses full controls, this should be noted explicitly. As written, it creates an apparent numerical inconsistency in the paper's central dynamic finding.

4. **Placebo test uses only age.** The balance table contains seven variables; the falsification exercise tests only age. A joint F-test across all seven baseline characteristics, or a randomization test of the omnibus balance statistic, would be more informative. Single-variable placebo tests with selectively chosen covariates are subject to the criticism that the authors stopped after a convenient pass.

5. **SUTVA not discussed.** With approximately 600 treated individuals concentrated in local Jordanian labor markets, displacement effects are a plausible concern. The paper argues that the demand-side constraint is binding (consistent with the large voucher effect), but does not consider whether voucher-induced employment partially displaces non-participants or other workers in the same market. One paragraph in Section 7 acknowledging this as a scope condition for the net welfare interpretation would appropriately bound the paper's policy conclusions.

6. **Interaction confidence interval reported as "approximately."** The paper states the 95% CI on β₃ is "approximately [−0.117, +0.087]." This is arithmetically correct (−0.015 ± 1.96 × 0.052) but should be stated as an exact figure, since this CI is the primary evidence for the null interaction result and the basis for the policy conclusion that bundling adds no value.

---

### Recommendation: **Major Revision**

Three of the six Round 2 "must-address" items remain substantively unresolved (sample size increase, LATE estimates, control LFP collapse). Each of these gaps is central to the paper's identification claims and to the interpretation of its headline endline results. The paper makes meaningful progress on variable documentation and numerical transparency, and the core midline voucher result is clean and credible. With targeted revision on the four major concerns above, the paper could be a solid contribution.

---

```json
{
  "score": 74,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "identification_strategy": 76,
    "estimation_implementation": 74,
    "statistical_inference": 69,
    "robustness_sensitivity": 73,
    "replication_readiness": 77
  },
  "sanity_checks": {
    "sign": "PASS",
    "magnitude": "PASS",
    "dynamics": "FAIL",
    "consistency": "PASS"
  },
  "major_comments": [
    "Sample size rises from N=1,207 at midline to N=1,255 at endline with no explanation of mechanism; the midline-to-endline fade-out comparison is therefore between potentially different populations. Authors must document the source of re-appearing observations, test arm balance among them, and provide sensitivity estimates restricted to balanced attritors.",
    "LATE/compliance estimates are absent despite being pre-specified in the research strategy. Take-up rates, first-stage statistics, and IV/2SLS LATE estimates are required for at minimum employment and LFP; linearmodels is confirmed working in the pipeline. All welfare and fade-out mechanism discussion is uninterpretable without per-complier scaling.",
    "Control-group LFP collapses 29.1 pp from midline (77.1%) to endline (48.0%), nearly three times the persistent treatment effect (10.1 pp). The revision never explains this. The headline persistence result is not credibly interpretable until: (a) survey instrument changes are ruled out, (b) seasonal/macroeconomic confounds are documented, (c) differential attrition by arm is examined, and (d) balanced-attritor sensitivity is reported.",
    "975 excluded observations (42% of the full baseline sample) are characterized only as 'likely due to eligibility screening.' This signals uncertainty incompatible with the authors' direct access to implementation records. Baseline comparisons and exogeneity tests for the excluded group are required."
  ],
  "minor_comments": [
    "Variable b_communitycollege is labeled 'Education (1-8 scale)' in the balance table; a data appendix should clarify whether this is a college identifier code or a constructed attainment index, as the distinction affects interpretation of balance and covariate adjustment.",
    "No multiple testing correction applied across 8+ primary outcomes; the key endline LFP result (p=0.008) should be evaluated against Benjamini-Hochberg q-values as pre-specified in the research strategy.",
    "Figure 3 caption reports endline employment effect as +0.034 and salary as +7.713, inconsistent with Table 3 values of 0.030 and 6.954; if the figure uses the no-controls specification, this must be stated explicitly.",
    "Placebo test uses only age from a seven-variable balance table; an omnibus joint F-test or randomization-based balance statistic would be more credible than a single selectively chosen variable.",
    "SUTVA and potential displacement effects are unaddressed despite the concentration of ~600 treated individuals in local Jordanian labor markets; a brief scope-condition acknowledgment in Section 7 is warranted.",
    "The 95% CI on the interaction term β₃ is described as 'approximately' [-0.117, +0.087]; this is the paper's key null result and should be stated precisely."
  ]
}
```