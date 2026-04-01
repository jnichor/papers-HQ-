# Referee Report: "COVID-19 and the Formality Recovery Path in Peru"

---

## Summary of Methodology

The paper employs a DiD event-study design using the Dingel-Neiman (2020) teleworkability index as pre-determined treatment intensity to estimate the differential informality response of contact-intensive Peruvian workers to the COVID-19 shock. The primary specification uses the continuous teleworkability score interacted with year dummies in a pooled WLS regression; a secondary within-estimator absorbs individual fixed effects. Because ENAHO's rotating panel replaces most households after two years, only 0.5% of individuals are observed in all five waves, making the event-study a hybrid between a true panel DiD and a repeated cross-section DiD that primarily identifies off cross-cohort variation within occupation groups.

---

## Main Methodological Assessment

The research question is well-motivated and the data infrastructure is suitable. The pre-determined treatment, the non-differential attrition result, and the honest acknowledgment of 2020 baseline contamination are genuine strengths. However, the paper suffers from three interlocking reporting failures that must be resolved before the results can be evaluated: (1) the main results table is mislabeled in a way that creates an apparent sign inconsistency with the narrative, (2) the headline "9 pp" result and the stated γ = 0.089 are not directly readable from Table 2, and (3) the standard-error type reported in Table 2 (HC1) is inconsistent with the abstract's claim of cluster-robust SEs. These are not trivial notation issues—they prevent independent verification of the central claim.

---

## Major Concerns

**1. Internal inconsistency between Table 2 coefficients and the headline result**

The paper's central claim is that contact-intensive workers experienced a 9 pp informality increase relative to teleworkable workers (γ = 0.089, p < 0.001, stable through 2024). Table 2, labeled as the *main* DiD results, shows interaction coefficients of –0.202 (2021) through –0.190 (2024) under the column header "Interaction (TW$_{\text{low}}$)."

These two representations are arithmetically inconsistent unless Table 2 is actually reporting the *continuous* TW specification (where a 1-unit increase in TW reduces informality by 0.20 pp, and the 9 pp aggregate is recovered by multiplying by the mean TW difference between groups ≈ 0.45), but the column header and table notes describe it as a binary TW$_{\text{low}}$ (contact-intensive = 1) result. If TW$_{\text{low}}$ truly equals 1 for contact-intensive workers, a *negative* interaction coefficient means contact-intensive workers had *less* informality increase than teleworkable workers—the opposite of the paper's narrative.

The p < 0.001 claim in the abstract does not appear in Table 2, which shows p < 0.05 at best. The γ = 0.089 value used in the scarring test appears to come from a separate binary specification that is not fully tabulated. The authors must: (a) decide unambiguously which specification is the main one (continuous or binary), (b) present that specification's full output—including the exact coefficients used for the Wald test—in the main table, and (c) correct the table header and notes. If the 9 pp figure requires multiplying a continuous coefficient by mean TW group differences, this calculation must be shown explicitly with the mean TW values for each group.

**2. Parallel trends: no validation possible and large compositional differences**

The panel begins in 2020, the shock year, making it impossible to test pre-trends. This is acknowledged. However, the paper does not provide the alternative supporting evidence that should accompany this limitation. Contact-intensive and teleworkable workers differ sharply on observables: 44% rural vs. 12% rural; 42% female vs. 61% female; informality rate gap of 16.6 pp *at baseline*. These pre-existing differences make parallel trends substantially less plausible than it would be for more comparable treatment and control groups, because the informality levels and their cyclical sensitivities are likely structurally different across these groups.

The main specification (Equation 1) includes no demographic or sector controls. The authors should: (a) estimate the primary specification with the full vector of observable controls (education, gender, age, region, sector) and show whether the interaction coefficients change materially; (b) provide any external corroborating evidence for parallel trends—e.g., pre-pandemic trends from ENAHO 2017-2019 cross-sections, or sector-level administrative data—even if these cannot be incorporated as a formal pre-trend test in the panel; (c) discuss why the large baseline composition differences do not threaten parallel trends.

**3. The near-zero contract-based informality result undermines the proposed mechanism**

Section 6.1 reports that the no-written-contract informality measure yields a near-zero interaction coefficient (0.002), compared with 0.089 for the social-security measure and 0.047 for the small-firm measure. This finding is mentioned briefly but not explained. It is a direct challenge to the scarring narrative: if the pandemic induced durable displacement into informality, why did it leave written contract arrangements essentially unchanged while eliminating employer-provided social security contributions? Possible explanations—selective non-compliance with social security obligations while maintaining paper contracts, sectoral composition of the sample, or attenuation bias in the contract variable—have different implications for the policy conclusions. The authors should report the full event-study profiles for all three informality definitions side by side and provide a substantive discussion of what the divergence implies.

**4. Standard error specification inconsistency**

The abstract states SEs are "clustered at the ISCO-08 2-digit occupation level (43 clusters)." Table 2 reports "SE type: HC1"—a heteroskedasticity-only White correction, not a cluster-robust estimator. These are not equivalent; HC1 SEs under intra-cluster correlation will be downward biased, making inference anti-conservative. The authors must: (a) clarify which estimator was actually used (and fix one of the two to match); (b) if cluster-robust SEs are used, report them as CR-1 or CR-1S, not HC1; (c) with 43 clusters, implement wild cluster bootstrap (Roodman et al. 2019) as a check, since t-distribution approximations can be unreliable at this cluster count with highly unequal cluster sizes.

**5. Income variable plausibly mislabeled in Table 1**

Table 1 reports monthly income of 15,440 soles for contact-intensive workers and 25,408 soles for teleworkable workers. Peru's monthly minimum wage is approximately 1,025 soles and the average formal wage is approximately 2,000–3,000 soles/month; the table values are 10–15× higher than plausible averages and would imply average formal-sector monthly income exceeding USD 6,000. These figures are consistent with *annual* income denominated in soles (15,440 / 12 ≈ 1,287/month; 25,408 / 12 ≈ 2,117/month), or possibly with survey-weighted totals rather than weighted means. The authors must verify and correct the label, and explain why N for income (78,180 and 38,777) covers only about 40% of the analytic sample.

---

## Minor Concerns

1. **Confidence intervals absent**: Point estimates and p-values are reported throughout but confidence intervals are never shown. All tables and figures should include 95% CIs, which are more informative about precision and effect size uncertainty.

2. **Wald test precision**: The scarring test reports γ$_{2021}$ = γ$_{2024}$ = 0.089 (identical to 3 decimal places) with z = –0.007. When point estimates are rounded to the same value, the Wald statistic is trivially zero, providing no real information about persistence. Report the estimates to sufficient decimal places to make the Wald test non-degenerate, and state the variance-covariance of (γ$_{2021}$, γ$_{2024}$) so readers can assess the power of the test.

3. **Multiple testing in heterogeneity analysis**: Section 5.4 reports at least eight DiD specifications across four subgroup dimensions. No correction for multiple comparisons is applied or discussed. This is particularly important given the p < 0.10 significance levels in some subgroup results. A Bonferroni or Holm correction, or a joint hypothesis test across subgroups, should be reported.

4. **Saltiel (2020) adaptation not implemented**: The paper cites Saltiel (2020)'s developing-country adaptation of the teleworkability index as a recommended future validation. Given that the key identifying variable is a U.S.-task-based measure applied to Peruvian occupations, this validation should be done now, not deferred. The Saltiel crosswalk would provide a direct test of whether the U.S.-based teleworkability ranking applies to the Peruvian context.

5. **Survey weight extremity**: The data audit flags a max/median weight ratio of 3,394× even after the stated 1st/99th percentile winsorization. If these are post-winsorization values, the distribution is still severe enough to raise concerns about whether the WLS results are driven by a small number of influential observations. Report the sensitivity of the main coefficients to 95th-percentile (rather than 99th-percentile) winsorization.

6. **SUTVA with 75.7% treated**: With three-quarters of the employed sample in the "treated" (contact-intensive) group, general-equilibrium spillovers are plausible—e.g., labor supply shifts toward the formal sector by contact-intensive workers could affect informality rates among teleworkable workers. The authors should at minimum acknowledge this threat and, if feasible, test whether the DiD estimate is sensitive to geographic variation in the local share of contact-intensive workers (a standard test for market-level spillovers).

7. **No placebo/falsification test**: The paper has no placebo test (e.g., testing whether the informality differential between contact-intensive workers in sectors with and without early reopening follows the expected pattern, or a fictitious treatment year prior to 2020 in cross-sectional data). Given the absence of pre-trends, a placebo exercise using an alternative shock that should *not* generate differential informality by teleworkability would substantially strengthen identification.

8. **Individual fixed effects identification**: Section 4.3 notes the within-estimator requires within-individual variation, which is "limited by ENAHO's rotating panel design." With most individuals observed for only 2 consecutive years, the event-study identification in the FE specification relies almost entirely on variation between 2020 and 2021, with later years identified mainly from fresh cohorts. The slight coefficient attenuation from the within-estimator (0.103 to 0.081 between 2021 and 2024) should be reported more precisely and its source discussed.

---

## Recommendation

**Major Revision**

The paper addresses an important policy question using a credible quasi-experimental design, but cannot be accepted without resolving the internal reporting inconsistencies (concerns 1 and 4), providing a richer defense of parallel trends given the large baseline compositional differences (concern 2), and explaining the divergent results across informality definitions (concern 3). The income variable labeling error in Table 1 must also be corrected. None of these require new data collection; they require careful rewriting, additional tables, and expanded robustness analysis.

---

```json
{
  "score": 62,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "identification_strategy": 63,
    "estimation_implementation": 56,
    "statistical_inference": 63,
    "robustness_sensitivity": 64,
    "replication_readiness": 56
  },
  "sanity_checks": {
    "sign": "FAIL",
    "magnitude": "PASS",
    "dynamics": "PASS",
    "consistency": "FAIL"
  },
  "major_comments": [
    "Table 2 labels the interaction as 'TW_low' (binary contact-intensive indicator) but shows negative coefficients (–0.202 in 2021); if TW_low=1 for contact-intensive workers a negative sign means they became MORE formal, contradicting the narrative. The coefficients are internally consistent only if the table actually reports the continuous TW specification, making the label wrong. The headline γ=0.089 and p<0.001 are not derivable from Table 2 without knowing mean TW group differences, and the binary spec yielding 0.089 is never fully tabulated. Authors must resolve which specification is primary, display its complete output, and fix all labeling.",
    "No pre-pandemic data precludes formal pre-trend testing; contact-intensive and teleworkable groups differ by 32pp on rurality and 19pp on gender share, making parallel trends less credible. The main regression includes no demographic controls. Authors should (a) add controls to the main specification, (b) show robustness to controls, and (c) provide any external corroborating evidence for pre-trend similarity.",
    "The no-written-contract informality measure yields γ≈0.002 (near zero) while the social-security measure yields γ=0.089 and the small-firm measure yields γ=0.047. This cross-definition divergence directly challenges the scarring mechanism claim and is not adequately explained. Authors must present full event-study profiles for all three definitions and discuss the mechanistic implications of the divergence.",
    "Abstract and text claim cluster-robust SEs (43 ISCO-08 clusters); Table 2 reports 'SE type: HC1' which is heteroskedasticity-only (not cluster-robust). HC1 under intra-cluster correlation is downward-biased. Authors must reconcile, implement cluster-robust SEs throughout, and report wild cluster bootstrap as a robustness check given 43 clusters.",
    "Table 1 reports monthly income of 15,440 and 25,408 soles for the two groups, roughly 10–15× Peru's average formal wage and 5× consistent with annual rather than monthly figures. Authors must verify and correct the label and explain the ~40% income missingness rate."
  ],
  "minor_comments": [
    "Confidence intervals are never reported; all tables and figures should show 95% CIs alongside point estimates.",
    "Wald test reports γ_2021=γ_2024=0.089 to identical 3 decimal places making z=–0.007 trivially zero; report sufficient decimal places and report the covariance between the two estimates so readers can assess test power.",
    "Eight or more subgroup DiD specifications are reported with no multiple-testing correction; apply Bonferroni/Holm correction or joint hypothesis test.",
    "Saltiel (2020) developing-country teleworkability adaptation is deferred to future work but is directly relevant to the external validity of the identifying variable; this validation should be implemented in the current paper.",
    "Post-winsorization weight ratio remains 3,394× (max/median per data audit); test sensitivity of main estimates to 95th-percentile winsorization.",
    "With 75.7% of workers in the treated group, GE spillovers to the control group are plausible; discuss and, if feasible, test using geographic variation in the local share of contact-intensive workers.",
    "No placebo or falsification test is included; a fictitious treatment year or cross-sectional placebo using a shock orthogonal to teleworkability would strengthen identification given the absence of pre-trends.",
    "FE specification attenuation from 0.103 (2021) to 0.081 (2024) is inconsistent with the claimed zero-attenuation result; authors should report this discrepancy precisely and discuss whether it reflects compositional change in the rotating panel or genuine within-person recovery."
  ]
}
```