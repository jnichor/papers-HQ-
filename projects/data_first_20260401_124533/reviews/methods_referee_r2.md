# Referee Report: "Commodity Busts and the Selective Erosion of Civil Liberties"

---

## Summary of Methodology

This paper estimates the effect of commodity terms-of-trade busts on five disaggregated civil liberty outcomes across 80 commodity-dependent countries from 1975–2018, exploiting exogenous price variation from the IMF's CTOT index. The identification strategy combines a TWFE estimator with separate event studies for bust and recovery episodes, and tests for dynamic asymmetry between the two. The paper is carefully written and its design—disaggregating political outcomes and testing for ratchet dynamics—is genuinely innovative.

---

## Main Methodological Assessment

The paper pursues a credible identification strategy and addresses several potential confounders responsibly (COVID exclusion, threshold robustness). However, three verified, inter-related problems collectively undermine the main result before revisions: (1) a sign reversal between the TWFE estimate and the event-study bust average that is inadequately explained; (2) a permutation placebo p-value (0.389) that directly contradicts the parametric p-value (0.020) on the same result; and (3) the absence of multiple-testing correction for five simultaneous hypothesis tests. Together these issues mean the central claim—that commodity busts selectively erode fair trial rights—rests on an internal contradiction. These problems are all visible in the evidence packet and are addressable with revisions.

---

## Major Concerns

**1. Sign reversal between TWFE and event-study estimate is unresolved**

The TWFE coefficient for fair trial is −0.199 (Table 1), implying busts *reduce* fair trial rights. The event-study bust average reported in Table 2 is +0.489, implying that during bust episodes fair trial rights *improve* relative to t = −1. The paper attributes this to sample-composition differences and reference-period normalization, but this is insufficient. A sign reversal—not merely a magnitude difference—requires explanation. The natural reading is that bust-experiencing countries were on positive institutional trajectories before the bust (hence the positive event-study average), while TWFE is picking up a level difference relative to non-bust countries. If this is correct, the TWFE estimate conflates the bust effect with pre-existing country differences that FEs do not fully absorb.

*Suggested fix*: Report a Goodman-Bacon decomposition to identify which comparison groups drive the TWFE estimate. Additionally, show the event-study path for fair trial in the text (not only the symmetry test aggregate), and explicitly plot the bust-period dynamic coefficients. If the event-study coefficients at k = 0,+1,+2 are uniformly positive, the TWFE and event-study findings are telling different stories about different estimands, and the paper should clearly label what each identifies.

**2. Permutation placebo test contradicts the parametric result**

The paper's main causal claim rests on the fair trial TWFE estimate (p = 0.020). The permutation test—which is, by design, robust to the distributional assumptions underlying the parametric test—yields p = 0.389. This means 38.9% of random permutations of bust timing produce a coefficient at least as extreme as the actual coefficient. The paper's explanation—that this is "consistent with a modest effect that does not dominate the null distribution"—is post-hoc rationalization: a result with p = 0.389 in a permutation test is not statistically distinguishable from noise by any conventional standard. The permutation test is more reliable than the asymptotic parametric test in a sample with N = 80 clusters, making this discrepancy the most serious inferential problem in the paper.

*Suggested fix*: The paper must either (a) reconcile the two tests by identifying why they diverge (e.g., show that asymptotic SEs are downward biased by running wild cluster bootstrap), or (b) honestly report that the permutation test does not support the parametric finding and downgrade the fair trial result from a robust finding to a suggestive one. Reporting wild cluster bootstrap p-values (Cameron, Gelbach & Miller 2008) would also be valuable for all five outcomes given N = 80 clusters, where asymptotic cluster inference may be unreliable.

**3. Multiple testing correction is absent**

The paper tests five simultaneous hypotheses and finds one significant at p = 0.020. The probability of finding at least one false positive across five independent tests at α = 0.05 is approximately 22.6%. A Bonferroni correction would require p < 0.010 for family-wise error rate control; the fair trial result (p = 0.020) does not survive this correction. The paper makes no mention of multiple testing, which is a standard concern in this design.

*Suggested fix*: Report Bonferroni-adjusted (or Holm-adjusted) p-values alongside unadjusted ones in Table 1. If the result does not survive correction, re-frame the finding as exploratory or use the language of a pre-specified primary outcome if the fair trial hypothesis was designated a priori.

**4. Staggered DiD concerns are underaddressed**

The paper's argument that non-absorbing treatment eliminates the negative-weighting problem (Goodman-Bacon 2021) is partially correct but overstated. Heterogeneous-treatment-robust estimators such as Callaway & Sant'Anna and Sun & Abraham can accommodate repeated treatments with appropriate modifications. With 31 heterogeneously-timed episodes and documented episode heterogeneity (average duration 3–4 years), negative weights from TWFE remain a plausible concern, particularly because some "clean controls" in the Bacon decomposition may themselves be future treated units.

*Suggested fix*: Report a Bacon decomposition to verify that negative-weighted comparisons do not drive the point estimate. Even a simplified version (how much of the TWFE weight comes from "treated vs. clean control" comparisons) would be informative.

**5. Symmetry test methodology needs explicit statement**

Table 2 reports z-statistics as large as 5.483 with only 50 combined episodes across 80 countries. The methodology for computing these z-statistics and the "asymmetry" column's standard error is not stated in the paper. If the z-statistic is computed from stacked regression coefficients with a joint Wald test, the large values are plausible but need verification. If it is computed from a simpler formula, it may be mechanically inflated.

*Suggested fix*: Add a methods subsection or footnote explaining exactly how the asymmetry standard error is computed, what regression is estimated, and how sampling uncertainty in both the bust and recovery event studies is accounted for simultaneously.

---

## Minor Concerns

1. **Definition of "commodity-dependent" is not provided.** The 80-country sample is central to the identification argument, but the criterion for inclusion is never stated. If commodity dependence is defined using an endogenous variable (e.g., a commodity revenue share), sample selection could correlate with institutional quality in ways that affect the results.

2. **Fair trial has 506 missing observations (N = 6,824 vs. 7,330).** The source of these missing values is unexplained. If missingness correlates with bust episodes or institutional quality, estimates for fair trial are not identified from the same sample as the other four liberties.

3. **Dose-response is not monotonic.** The paper claims a dose-response pattern as evidence of robustness, but the coefficients are −0.154 (−15%), −0.199 (−20%), −0.290 (−25%), and −0.149 (−30%). The −30% coefficient drops substantially below −25%, breaking monotonicity. The paper should not characterize this as a clean dose-response relationship.

4. **No time-varying controls.** The TWFE specification includes only country and year FEs. Plausible within-country time-varying confounders—economic growth, conflict onset, political transitions—are absent. Even if CTOT shocks are exogenous, they may operate through channels correlated with these variables. Including at least GDP per capita growth as a control would strengthen the design.

5. **Recovery episode definition is ambiguous.** The paper defines 21 recovery episodes as "subsequent increases exceeding +20%," but does not specify whether recovery must follow a bust episode. If recovery episodes include countries that never experienced a bust, the symmetry test compares conceptually distinct episodes.

6. **Ordinal outcomes treated as continuous.** The 1–4 scale outcomes are analyzed with linear TWFE. While this is common practice and likely innocuous given the roughly symmetric distributions reported in Table 3, the paper should briefly acknowledge this as a modeling choice and note that ordered logit FE models (or rescaling) yield similar qualitative results if run.

7. **Wild cluster bootstrap not reported.** With N = 80 clusters and potentially unequal cluster sizes (some countries may contribute multiple episodes), asymptotic cluster-robust SEs may be unreliable in finite samples. Wild cluster bootstrap p-values (especially for the key fair trial result) should be reported or at minimum discussed.

---

## Recommendation

**Major Revision**

The paper addresses an important question with a well-motivated identification strategy and an honest assessment of many limitations. However, the internal inconsistency between the TWFE and event-study estimates for fair trial, the failure of the permutation test, and the absence of multiple-testing correction jointly prevent publication in the current form. All three issues are addressable with additional analysis rather than redesign.

---

```json
{
  "score": 63,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "identification_strategy": 70,
    "estimation_implementation": 57,
    "statistical_inference": 52,
    "robustness_sensitivity": 62,
    "replication_readiness": 73
  },
  "sanity_checks": {
    "sign": "FAIL",
    "magnitude": "PASS",
    "dynamics": "FAIL",
    "consistency": "FAIL"
  },
  "major_comments": [
    "Sign reversal between TWFE (β = −0.199) and event-study bust average (+0.489) for fair trial is inadequately explained. A sign reversal across estimands—not merely a magnitude difference—requires a Goodman-Bacon decomposition and explicit plotting of bust-period event-study coefficients to determine what each estimand identifies.",
    "Permutation placebo test (p = 0.389) directly contradicts the parametric result (p = 0.020) for the paper's main finding. In a sample with N = 80 clusters where asymptotic inference may be unreliable, the permutation test is arguably more credible. The paper's reconciliation is post-hoc rationalization; wild cluster bootstrap p-values should be reported and the finding should be downgraded if they are non-significant.",
    "Five simultaneous outcomes are tested with no multiple-testing correction. A Bonferroni adjustment requires p < 0.010 for FWER control at 5%; the fair trial result (p = 0.020) does not survive this standard. Bonferroni or Holm-adjusted p-values must be reported.",
    "Staggered DiD concerns are underaddressed. The claim that non-absorbing treatment eliminates negative-weighting is overstated. A Bacon decomposition should verify that clean-control comparisons dominate the TWFE estimate.",
    "Symmetry test z-statistics (up to 5.483 with ~50 episodes) are implausibly large. The standard error computation for the asymmetry statistic is never stated and must be made explicit."
  ],
  "minor_comments": [
    "Definition of 'commodity-dependent' (the 80-country selection criterion) is never stated; this affects the external validity and potentially the internal validity of the design.",
    "506 missing observations for fair trial (N = 6,824 vs. 7,330) are unexplained; if missingness correlates with bust episodes, the fair trial estimates have a different identifying population than the other four liberties.",
    "Dose-response pattern is non-monotonic: the −30% threshold coefficient (−0.149) falls well below the −25% estimate (−0.290), breaking the claimed monotonicity.",
    "No time-varying controls included in the TWFE specification; GDP per capita growth or conflict indicator should at minimum be discussed as potential within-country confounders.",
    "Recovery episode definition does not specify whether recovery must follow a bust episode; if not, the symmetry test compares conceptually distinct episode types.",
    "Ordinal outcomes (1–4 scale) are treated as continuous without acknowledgment; a brief robustness note on ordered logit results would address this.",
    "Wild cluster bootstrap SEs should be reported for all five liberties given the finite-sample reliability concerns with N = 80 asymptotic clusters."
  ]
}
```