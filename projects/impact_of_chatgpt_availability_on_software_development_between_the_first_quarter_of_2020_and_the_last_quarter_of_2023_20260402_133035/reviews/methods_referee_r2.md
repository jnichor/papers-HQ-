# Referee Report

**Manuscript:** "Did ChatGPT Concentrate or Diversify the Programming Language Ecosystem? A Country-Level Event Study"

---

## Summary of Methodology

This paper estimates the effect of ChatGPT's November 2022 release on programming language ecosystem concentration using a country-level panel of GitHub push activity across 177 countries and 23 quarters (Q1 2020–Q3 2025). The identification strategy is a single-period interrupted time series with country fixed effects and event-time dummies, exploiting temporal variation around a globally-simultaneous treatment. Concentration is measured via a normalized Herfindahl-Hirschman Index (HHI) and Shannon entropy of language shares within country-quarter cells.

---

## Main Methodological Assessment

The paper's central contribution is a well-executed null result, and the authors deserve credit for their unusually candid treatment of identification failures. They correctly identify that simultaneous universal treatment precludes separating ChatGPT's effect from any contemporaneous global shock, present an extensive robustness battery that systematically dismantles the baseline result, and document the composition-effect mechanism that explains most of the mechanical HHI decline. These are genuine virtues.

However, the paper has serious reporting inconsistencies that undermine confidence in the numerical results, under-developed explanations for key findings, and an unresolved asymmetry between HHI and entropy results that weakens the conclusion. Revision is needed before this paper can be published.

---

## Major Concerns

**1. Critical internal inconsistency between event study coefficients and reported ATT (Estimation)**

Section 4.1 states that for normalized HHI, "all post-treatment coefficients are positive and significant, ranging from +0.039 to +0.079," yet the ATT reported in Table 2 is **−0.027** (diversification). These are mutually inconsistent without an explanation: if all post-treatment event study coefficients are positive (meaning HHI is *above* the Q3 2022 reference level post-treatment), the scalar ATT computed as average post minus average pre should also reflect this. The implicit logic—that the Q3 2022 reference period is at a within-country minimum for HHI, so all other periods show positive deviations, but post-treatment deviations are smaller than pre-treatment deviations, yielding a negative average difference—is never stated.

More seriously, the entropy event study coefficients as reported (+2.15 to +2.50 pre-treatment, +2.53 to +2.79 post-treatment) are **implausibly large** if they represent within-country deviations from the Q3 2022 reference level. With a full-sample entropy mean of 2.49 and SD of 0.83 (p10 = 1.10), a within-country deviation of +2.53 from the reference period would imply Q3 2022 reference entropy near zero—a near-monopoly state. These numbers appear to report absolute entropy levels, not FE-demeaned deviations. This is a critical error that must be corrected.

*Suggestion*: (a) Explicitly state that the ATT is computed as average(post event-study coefficients) − average(pre event-study coefficients) relative to the Q3 2022 reference, and show this algebra. (b) Re-examine and correct the entropy event study coefficients. (c) Consider whether the choice of Q3 2022 as reference period—which appears to coincide with a within-country minimum—is distorting the visual presentation; an average of several pre-treatment periods as the reference would be more informative.

**2. Entropy persistence in the balanced panel is unexplained (Robustness)**

The robustness table shows that the entropy ATT remains **+0.213 (p < 0.001)** in the balanced panel—a 15% reduction from the baseline +0.251, far smaller than the 96% reduction in HHI. The paper attributes this asymmetry to entropy being "more persistent" but provides no mechanism. Crucially, the balanced panel restriction fixes the set of countries but NOT the set of languages within those countries. Entropy in the balanced panel still fully reflects language-level composition effects (entry of new languages into the GitHub ecosystem within each country-quarter cell). The composition-adjusted HHI methodology—which restricts to languages present every quarter within a country—should be applied to entropy as well. Without a composition-adjusted entropy estimate, it is impossible to determine whether the persistent entropy result reflects genuine behavioral change or continued mechanical composition effects.

*Suggestion*: Construct a composition-adjusted entropy measure analogous to the composition-adjusted HHI. If composition-adjusted entropy also collapses, the null conclusion extends uniformly to both outcomes. If it does not, the paper owes the reader an explanation.

**3. Contemporaneous confounders are identified but not addressed (Identification)**

Section 3.3 correctly lists GitHub Copilot's general availability (June 2022), GPT-4's launch (March 2023), and Google Bard's launch (March 2023) as potential confounders. The Q3 2022 reference period falls *after* GitHub Copilot became generally available, meaning that the reference period itself may be partially "treated." More importantly, GPT-4 and Bard launched in March 2023—the same calendar quarter as the first full treatment period (Q1 2023, τ=+1). The "clean post (Q1 2023 only)" row in the robustness table collapses all post-treatment quarters into a single estimate but does not separate the confounders.

*Suggestion*: (a) Formally discuss whether the GitHub Copilot launch in Q2 2022 contaminates the reference period. (b) Present a specification that uses only Q1 2023 data (January–March 2023) as the treatment period and interprets this as an upper bound on confounded effects. (c) Exploit the fact that GPT-4 and Bard launched in March 2023 (the last month of Q1 2023): compare effects in January–February 2023 against March 2023 within that quarter, if monthly data are available.

**4. The ATT computation method is never specified (Estimation)**

The paper oscillates between an event study framework (equation 1) and scalar "ATT" estimates (Table 2), without stating how the ATT is derived from the event study. Is it from a separate regression with a binary `Post` indicator? Is it the weighted average of post-treatment event study coefficients? Is it the average post coefficient minus the average pre coefficient? These procedures yield identical estimates under balanced panels and uniform weighting, but differ under unbalanced panels and heterogeneous weighting—and the paper has an unbalanced panel (88.1% balance rate) with varying numbers of observations per event-time period. The robustness table reports seven different ATT estimates for eight specifications, and none explains the mapping from event study to scalar.

*Suggestion*: Add a footnote or appendix equation showing that ATT = average(β_{τ>0}) − average(β_{τ<-1}) where the β_τ are from equation (1). If a different procedure is used, state it explicitly.

**5. Sign reversal in composition-adjusted HHI is not discussed (Identification)**

The composition-adjusted HHI ATT is **+0.002 (p = 0.021)**—small but statistically significant, and *positive*, meaning slight **concentration**, not diversification. This is the opposite sign from the baseline ATT of −0.027. The paper notes the 93% reduction in magnitude but does not highlight or interpret the sign reversal. If the true behavioral effect on language concentration is slight *concentration* rather than diversification, this is substantively important and should be foregrounded in the discussion, not buried in a magnitude comparison.

*Suggestion*: In the Discussion section, explicitly note that after removing mechanical composition effects, the residual signal in HHI points toward slight concentration (though tiny in magnitude), and reconcile this with the entropy result.

---

## Minor Concerns

1. **Multiple testing.** Two outcomes (HHI and entropy) are tested without multiple testing correction. Given their negative mechanical correlation, a Bonferroni threshold of p < 0.025 applies. All baseline results survive this threshold (both p < 0.001), but the composition-adjusted HHI (p = 0.021) does not. This should be noted, particularly since the composition-adjusted result is substantively important.

2. **Power of heterogeneity analysis.** The EPI heterogeneity specification covers 78.2% of panel observations (countries without EF EPI data are dropped). The paper concludes "no differential effect" but does not report the power of the test or characterize the minimum detectable effect size. Given the measurement error in EPI scores and the restricted sample, this test may be severely underpowered.

3. **Total pushers as a confounder.** The event study does not control for log(total pushers). If the volume of GitHub activity grew differentially post-ChatGPT (e.g., because AI tools attracted new users), this could confound the HHI estimates within country. A sensitivity check adding log(total pushers) as a time-varying control would be informative.

4. **GitHub data provenance.** The paper does not discuss whether GitHub changed its language detection algorithm, API structure, or data aggregation methodology during the sample period. Any platform-level change proximate to Q4 2022–Q1 2023 would confound the event study. The authors should verify with GitHub's changelog or documentation that no material platform change occurred.

5. **Shannon entropy convention for zero shares.** The entropy formula uses $-\sum_l s_{l,c,q} \ln(s_{l,c,q})$, which requires the convention $0 \cdot \ln(0) = 0$ for languages with zero pushers in a given cell. The paper should confirm this convention is implemented and discuss whether "zero pushers" observations are dropped before computing shares (which would affect which languages appear in the denominator and hence the normalization).

6. **Figure file naming inconsistency.** The main-text figures are labeled Figure 1 (event study, `fig2_event_study.png`) and Figure 2 (heterogeneity, `fig3_heterogeneity.png`). The file names suggest a Figure 1 (raw trends, now Figure A1 in the appendix) was moved during revision without renaming files. This should be corrected for clarity.

7. **Partial treatment period in robustness.** The paper excludes Q4 2022 as a "partial treatment quarter" (ChatGPT launched in the last month of the quarter). The strategy memo mentions a robustness check using a fractional treatment indicator (1/3 for Q4 2022), but this check does not appear in the robustness table. Including it would verify that the partial-quarter exclusion does not drive results.

---

## Recommendation

**Major Revision**

The paper's intellectual contribution—an honest null result with a clearly-articulated identification failure—is genuine and valuable. The robustness battery is admirably extensive. However, the paper cannot be accepted in its current form due to: (1) numerical inconsistencies in the event study description that raise doubts about whether the figures match the reported estimates; (2) an unresolved asymmetry between HHI and entropy in the balanced panel that is central to the paper's conclusions; and (3) the unaddressed sign reversal in composition-adjusted HHI. The authors should audit all reported coefficient magnitudes against the underlying estimates and provide a complete discussion of the entropy persistence finding.

---

```json
{
  "score": 71,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "identification_strategy": 72,
    "estimation_implementation": 60,
    "statistical_inference": 70,
    "robustness_sensitivity": 76,
    "replication_readiness": 76
  },
  "sanity_checks": {
    "sign": "PASS",
    "magnitude": "PASS",
    "dynamics": "FAIL",
    "consistency": "FAIL"
  },
  "major_comments": [
    "Event study coefficients described in Section 4.1 are internally inconsistent with reported ATTs: all post-treatment HHI coefficients described as positive (+0.039 to +0.079) while ATT = -0.027 is never algebraically reconciled; entropy event study coefficients (+2.53 to +2.79) are implausibly large relative to the entropy distribution (full-sample mean 2.49, SD 0.83) and appear to report absolute levels rather than FE-demeaned deviations from the reference period.",
    "Entropy ATT = +0.213 (p < 0.001) survives the balanced-panel restriction—a far smaller reduction than HHI's 96% collapse—because the balanced-panel restriction controls for country entry/exit but not language entry/exit within countries. A composition-adjusted entropy measure (analogous to the composition-adjusted HHI) is required to determine whether this persistence reflects genuine behavior or continued mechanical composition effects.",
    "Contemporaneous confounders (GitHub Copilot general availability June 2022, GPT-4 and Google Bard both March 2023) are identified but not addressed empirically. GitHub Copilot's Q2 2022 launch potentially contaminates the reference period; GPT-4/Bard's Q1 2023 launch is contemporaneous with the first treatment quarter. At minimum, a within-Q1-2023 temporal comparison and a sensitivity check restricting to pre-GPT-4 quarters are needed.",
    "The mapping from event study coefficients (equation 1) to scalar ATT estimates (Table 2) is never stated. With an unbalanced panel, this choice is non-trivial and could explain the discrepancy between the raw pre-post difference (~0.012 for HHI from summary statistics) and the regression ATT (-0.027).",
    "The composition-adjusted HHI ATT = +0.002 (p = 0.021) is positive—opposite sign to the baseline ATT of -0.027—indicating slight residual concentration after removing mechanical composition effects. This sign reversal is substantively important and is not discussed in the text."
  ],
  "minor_comments": [
    "Two correlated outcomes tested without multiple testing correction; Bonferroni threshold (p < 0.025) eliminates the composition-adjusted HHI result (p = 0.021).",
    "The heterogeneity analysis covers 78.2% of observations with no power analysis; the null heterogeneity finding may reflect insufficient power given EPI measurement error and restricted sample.",
    "Log(total pushers) is omitted from the event study; if AI tools differentially expanded GitHub activity post-treatment, this could confound within-country HHI estimates.",
    "No discussion of whether GitHub changed its language detection methodology or API during the sample period, which could generate a spurious discontinuity.",
    "Shannon entropy computation for zero-pusher language-country-quarter cells requires explicit statement of the 0*ln(0) = 0 convention and clarification of whether such observations are dropped before normalization.",
    "Main-text figure files named fig2_event_study.png and fig3_heterogeneity.png but labeled Figure 1 and Figure 2 in LaTeX—artifact of apparent revision history that should be corrected.",
    "The robustness table omits the fractional treatment indicator check for Q4 2022 (mentioned in the strategy memo) that would verify results are not driven by partial-quarter exclusion."
  ]
}
```