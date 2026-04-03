## Referee Report

**Journal of Development Economics / American Economic Journal: Applied Economics**

---

### Summary

This paper reports a 2×2 factorial RCT among approximately 1,200–1,255 young Jordanian men, cross-randomizing a six-month wage voucher and a short vocational training course. The central findings are: (i) the wage voucher produced a massive short-run employment gain (Cohen's d = 0.88 at midline) that nearly completely faded by endline; (ii) vocational training had no significant effect at either horizon; and (iii) the interaction term is small and statistically indistinguishable from zero at both horizons, ruling out superadditivity. A single persistent effect survives: a 10.1 pp increase in labor-force participation at endline (p = 0.008).

---

### Main Assessment

The paper makes a genuine contribution. The factorial design is the correct tool for the research question, and the midline-to-endline fade-out is documented with unusual precision. The ALMP literature in MENA is thin on experimental evidence, and the null training result adds to a growing cross-country body of evidence. The empirical strategy—HC2 standard errors, BH correction, permutation inference, Lee bounds—is exemplary.

That said, I have several serious concerns, some involving verifiable numerical inconsistencies between the paper's tables and the underlying data evidence. These must be resolved before publication. I also flag a substantive interpretive gap—the dramatic control-group LFP decline from midline to endline—that the current draft treats almost in passing but that bears directly on the paper's headline persistence result.

---

### Major Comments

**1. Verifiable numerical discrepancies between paper tables and data outputs.**

Several numbers reported in the paper's tables do not match the data outputs provided in the evidence packet:

- **Age in balance table**: The paper's Table 1 reports mean ages of 23.1–23.6 years across arms, with the control mean at 23.4. The underlying data (variable `b_b1age`) shows means of 21.1–21.3 years—roughly 2.2 years lower across all arms. These cannot both be right. Either the paper's balance table is using a different or incorrectly-labeled age variable, or there is a coding error.

- **Control arm size**: The data show the control group contains 440–449 observations (depending on variable), while the paper's balance table reports "n ≈ 400." A 10 percent discrepancy in arm size is non-trivial and needs explanation.

- **Endline employment control mean**: The arm-means table reports a control mean of 0.212 for endline employment; the paper's Table 3 constant (which should equal the control mean in the unadjusted OLS) is 0.242. A 3 pp gap is substantial relative to an estimated treatment effect of 3.0 pp, and the source of the discrepancy (sample restriction, missingness pattern) must be explained.

- **Endline LFP interaction term**: The paper's Table 3 reports the endline LFP interaction as −0.048 (SE = 0.054, p = 0.377), but the data output shows −0.058 (SE = 0.057, p = 0.305). The authors should reconcile this and audit all tables against the final estimation code.

These discrepancies, taken together, undermine confidence in the accuracy of the reported results. The authors must provide a full audit of Table 1–4 numbers against the reproducible estimation output.

**2. The 29 percentage-point decline in control-group LFP demands a rigorous explanation.**

The control group's labor-force participation falls from 77.1% at midline to 48.0% at endline—a 29 pp drop over approximately 12 months. This is the baseline against which the voucher's persistent LFP effect (+10.1 pp) is measured. The paper flags this decline in Section 7.1 but disposes of it in two sentences, calling it "likely" due to "discouragement or return to education."

This explanation is insufficient for several reasons. First, a 29 pp decline in LFP among young men over one year is an extraordinary labor-market event, not a routine attrition pattern. Second, if the decline reflects survey-wave differences (e.g., different seasons, different enumerators, question reordering), it would be an artifact rather than a real behavioral change, and the voucher's persistent LFP advantage may not be interpretable as a genuine treatment effect. Third, if the decline reflects genuine discouragement concentrated in the control group—possibly as a direct consequence of not receiving the voucher—then the LFP persistence result should be interpreted as a despondency-prevention effect, not labor-market engagement, with correspondingly different policy implications.

The authors should: (a) document any differences in survey timing, mode, or question wording across waves; (b) check whether comparable cohort-level data (e.g., national LFS data for 18–30 year old men in Jordan during the study period) show similar trends; (c) test whether the control-group decline is driven by any observable subgroup; and (d) revisit the interpretation of the headline LFP persistence result in light of whatever they find.

**3. No compliance or take-up data reported anywhere in the paper.**

The paper reports intent-to-treat (ITT) estimates throughout. This is appropriate, but ITT interpretability depends critically on how many assigned participants actually received and used their treatment. For the wage voucher, the relevant question is: what fraction of the "voucher only" and "both" arm participants actually redeemed the voucher with an employer? For training, what fraction completed the course? These numbers are conspicuously absent.

The midline employment rate in the voucher arm is 57.4%—nearly tripling the control rate. If take-up of the voucher was, say, 70%, the LATE on employment would be roughly 57 pp among compliers, an even more extreme effect. If take-up was lower, the program may be less expensive to scale than the ITT effect implies. Compliance data are essential for interpreting effect magnitudes and for cost-effectiveness comparisons. The authors should report take-up rates by arm and offer LATE estimates via 2SLS (as contemplated in the strategy memo) at a minimum for the primary outcomes.

**4. No discussion of SUTVA / general-equilibrium displacement effects.**

With ~1,300 treated participants concentrated in a small labor market (registered at Jordanian employment offices, presumably in a limited number of governorates), the assumption of no interference between units is non-trivial. The wage voucher effectively made ~600 workers temporarily cost-free for private-sector employers in local markets. If labor demand is inelastic at the firm level, some voucher employment may have displaced non-participants or workers already employed without subsidy.

Crépon et al. (2013) is cited once to motivate the demand-constraint argument, but the paper does not engage with their key methodological point: positive ITT effects at the individual level can coexist with zero or negative aggregate employment effects if displacement is substantial. The paper's policy recommendation—that vouchers "generate massive short-run employment gains"—is only warranted if these are net employment gains, not redistributional. The authors should at minimum acknowledge this limitation; if spatial or employer-level variation allows any test of displacement, they should conduct it.

**5. The institutional description of the Tawjihi and the target population contains an inconsistency.**

The paper states the target population is "young men aged 18–30 who had completed or left secondary school and were not enrolled in tertiary education." The paper also correctly notes that `b_communitycollege` is an ordinal education scale 1–8, not a binary indicator. However, the strategy memo describes the sample as "2,322 community college graduates"—a characterization that is inaccurate per the paper's own clarification. More importantly, the paper's balance table labels this variable "Education (years): 11.7–11.9," suggesting it has been rescaled or relabeled. The authors should be transparent about how the raw ordinal variable (mean ~4.5 on 1–8 scale) maps to the "years of education" presentation in Table 1.

Similarly, the paper's balance table reports "Tawjihi pass (%): 42–44%" but the underlying data show an exam-score variable (`b_examresult`) with mean ~62.4. The threshold used to convert exam scores to a pass/fail indicator is never stated. Given that the Tawjihi pass threshold varies by stream and year in Jordan, this conversion is non-trivial and should be documented.

---

### Minor Comments

1. **Endline salary Lee bounds vs. point estimate**: The paper reports that endline salary Lee bounds are strictly positive [+1.26, +18.94] (lower bound = +1.26 JD), but the point estimate of 6.95 JD carries p = 0.273, implying the 95% CI for the point estimate includes zero. The Lee lower bound is a non-parametric worst-case estimate, not a confidence interval for the point estimate. The authors should clarify that the Lee bound is interpreted differently than the regression CI to avoid reader confusion.

2. **Voucher value relative to minimum wage and employer cost structure**: The paper states the voucher is "approximately 200 JD per month (roughly 70 percent of the prevailing entry-level wage)." In the relevant study period, Jordan's statutory minimum wage was 190 JD/month. If the 200 JD voucher exceeds the minimum wage, the employer's net cost could approach zero or go negative after accounting for social security contributions (~14.25% employer rate on formal payroll). The authors should clarify whether the subsidy covered gross wage cost inclusive of social security, or only the take-home wage. This affects interpretation of the near-complete employment gains at midline.

3. **Foreign labor displacement**: The paper correctly identifies foreign labor competition as a structural feature of the Jordanian labor market (Section 3.1) but does not examine whether the voucher-induced employment represents Jordanian workers replacing foreign workers at the firm level. This nationality-substitution channel is qualitatively different from net employment creation and is directly relevant to the displacement concern in Major Comment 4. Even a descriptive discussion would strengthen the mechanisms section.

4. **Heterogeneity on voucher take-up**: The paper explores heterogeneity by age, education, Tawjihi pass status, and baseline employment, but all results are heterogeneity in ITT effects. If take-up data are available, heterogeneity in LATE—whether the fade-out is sharper for lower-education or younger workers—would directly test the employer-learning mechanism against the demand-constraint mechanism.

5. **Missing citation — Groh, McKenzie, and Vishwanath (wage subsidies in Jordan)**: The paper cites Groh et al. (2016) for soft-skills training among Jordanian women but does not cite the closely related Groh, McKenzie, and Vishwanath work on wage subsidies and information asymmetries using a randomized experiment in Jordan. If this work exists in published or working-paper form at time of submission, it is essential to discuss given the near-identical context.

6. **Missing citation — Acemoglu and Pischke (1999)**: The discussion of why training fails would be strengthened by citing Acemoglu and Pischke's framework on employer-provided training and wage compression. Their prediction that competitive labor markets undersupply training is relevant to interpreting the null training result.

7. **Missing citation — Crépon, Duflo, Gurgand, Rathelot, and Zamora (2013)**: This paper is cited once in Section 2.3 but only for the demand-constraint argument. Its central methodological contribution—identifying displacement effects in a randomized job-search experiment—should be engaged more substantively in the SUTVA discussion called for in Major Comment 4.

8. **Control group LFP at midline (77.1%)**: This is quite high for a sample defined as not currently employed or enrolled. The authors should clarify the definition: is LFP at midline defined as employed or actively seeking, and if so, how is "actively seeking" measured? A 77.1% LFP rate with only 17.8% employment implies ~59% of the sample is actively job-seeking at midline—a plausible figure—but the denominator (does it exclude students who may have re-enrolled?) should be stated.

9. **Policy discussion on LFP persistence**: The paper correctly notes that the welfare interpretation of increased LFP is ambiguous—it could reflect genuine labor market engagement or frustrated job seekers who have not yet given up. The policy section would benefit from a brief discussion of what follow-on interventions (job-search assistance, employer matching programs) might convert the voucher-induced LFP persistence into actual employment.

10. **Male-only sample and policy generalizability**: Female youth unemployment in Jordan is equally policy-relevant and the barriers are qualitatively different (family norms, mobility constraints, social security gaps). The paper acknowledges the male-only restriction but does not discuss whether the voucher mechanism would operate differently for women. Given Jordan's active policy discussion on female employment, even a brief speculative paragraph would add value.

---

### Recommendation

**Major Revision**

The paper's research design is sound, the question is important, and the core findings are credible. However, the numerical discrepancies between the paper's tables and the underlying data (age, control arm size, endline employment control mean, LFP interaction term) must be audited and corrected before this paper can be published. The inadequate treatment of the dramatic control-group LFP decline and the complete absence of take-up/compliance data are substantive gaps that require new analysis or, at minimum, substantially revised discussion. The SUTVA concern is a known limitation of local labor market experiments that the paper cannot currently ignore given the scale of the midline effect.

---

```json
{
  "score": 72,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "contribution_novelty": 78,
    "literature_positioning": 73,
    "substantive_arguments": 65,
    "external_validity": 70,
    "journal_fit": 76
  },
  "major_comments": [
    "Verifiable numerical discrepancies between paper tables and data outputs: mean age in balance table (paper: 23.4 vs. data: 21.3), control arm size (~449 vs. ~400), endline employment control mean (0.242 vs. 0.212), and endline LFP interaction term (-0.048/p=0.377 vs. -0.058/p=0.305). Full audit required.",
    "The 29 pp decline in control-group LFP from midline (77.1%) to endline (48.0%) is under-explained. This baseline movement is larger than the persistent treatment effect it anchors; its cause (survey artifact, discouragement, seasonality) must be rigorously assessed before the headline LFP persistence result is interpretable.",
    "No compliance or take-up rates are reported. ITT interpretability and cost-effectiveness claims require LATE estimates; the strategy memo anticipates 2SLS but the paper omits it entirely.",
    "No discussion of SUTVA / general-equilibrium displacement effects despite a ~600-person treated sample concentrated in local Jordanian labor markets. A Cohen's d of 0.88 at midline raises the question of net vs. redistributive employment creation.",
    "Variable construction in Table 1 is opaque: the ordinal education variable (1-8 scale, mean ~4.5) is relabeled 'Education (years): 11.7-11.9' without explanation; the Tawjihi pass rate threshold from a continuous exam-score variable is never stated."
  ],
  "minor_comments": [
    "Endline salary Lee bounds [+1.26, +18.94] are presented as if consistent with the non-significant point estimate (p=0.273); clarify that Lee bounds and regression CIs answer different questions.",
    "Voucher value (200 JD) likely exceeds Jordan's statutory minimum wage (190 JD) in the study period; employer social security contributions (~14.25%) may have made net cost of hiring negative. This institutional detail matters for mechanism interpretation.",
    "Foreign-labor substitution as a channel of voucher employment gains is described as a structural feature in Section 3 but not tested or discussed in the mechanisms section.",
    "The 59% active-job-seeking rate implied by midline LFP (77.1%) minus employment (17.8%) requires the LFP definition and measurement instrument to be clearly stated.",
    "Policy discussion should address what follow-on interventions could convert the persistent LFP increase into actual employment.",
    "The male-only restriction warrants at least a speculative paragraph on whether the voucher mechanism would differ for women, given active policy debates on female employment in Jordan."
  ],
  "missing_literature": [
    "Groh, McKenzie, and Vishwanath — wage subsidies and information asymmetries, randomized experiment in Jordan (if available as working paper or publication at time of submission).",
    "Acemoglu and Pischke (1999) — employer-provided training and wage compression; directly relevant to interpreting null training result.",
    "Crépon, Duflo, Gurgand, Rathelot, and Zamora (2013) — cited once but not engaged for its central methodological contribution on displacement effects in local labor markets.",
    "Blattman and Ralston (2015) — review of ALMPs in poor and fragile states; relevant to MENA generalizability discussion.",
    "Bandiera, Burgess, Das, Gulesci, Rasul, and Sulaiman (2017) — labor markets and poverty, relevant to demand-constraint framing."
  ]
}
```