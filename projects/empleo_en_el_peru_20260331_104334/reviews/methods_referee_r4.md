## Referee Report — Round 4
**COVID-19 and the Formality Recovery Path in Peru: A Worker-Level Panel DiD Using Sectoral Teleworkability**

---

### Summary of Methodology

The authors estimate the effect of COVID-19 on labor informality in Peru using a pooled weighted least squares DiD event study that exploits differential occupational exposure via the Dingel-Neiman (2020) teleworkability index mapped to ISCO-08 2-digit codes. The primary specification uses a continuous treatment variable (teleworkability score) interacted with year dummies, with standard errors clustered at the 43 ISCO-08 2-digit occupation groups. The panel is drawn from ENAHO 2020–2024 (262,733 observations), though 96.9% of baseline individuals exit by 2024.

---

### Main Methodological Assessment

The authors resolved several bookkeeping inconsistencies from prior rounds: the SE type is now stated consistently as clustered (no longer contradicted by an HC1 reference), the Wald test p-value is now internally consistent (0.937 throughout), and the cluster count is now uniformly stated as 43. These are genuine improvements.

However, four "must-address" items from the Round 3 editorial letter remain unresolved after two full revision cycles. Three are empirically addressable and carry material consequences for the paper's validity. The persistence of these gaps—particularly the absence of wild cluster bootstrap inference and the unaddressed Reactiva Perú confound—is increasingly difficult to defend. Additionally, the revised abstract introduces a new inferential problem: the headline effect is now reported with p = 0.153, a result that is not significant at any conventional threshold, yet is presented in the abstract without qualification as a principal finding. This is a step backward from the prior draft.

---

### Major Concerns

**1. Wild cluster bootstrap inference remains unimplemented (third carry-over from Round 1)**

With 43 clusters and a headline coefficient significant at only the 10% level in 2021 (and insignificant under the binary specification reported in the abstract, p = 0.153), the distributional properties of the conventional cluster-robust t-statistic matter critically. The Cameron-Miller (2015) threshold of approximately 50 clusters is well below the current cluster count. Finite-sample over-rejection bias under conventional asymptotics means the reported significance levels are unreliable. The authors must implement wild cluster bootstrap with Rademacher weights (≥999 replications) as the primary inference method and re-state all significance claims accordingly. If the 2021 coefficient does not survive WCB, the characterization of "immediate and large increase in informality" in the conclusion must be substantially qualified.

*Concrete fix*: Replace Table 2 SEs/p-values with WCB-based p-values. If the result is borderline, report both and discuss.

**2. The headline abstract result is statistically insignificant and presented without qualification**

The abstract states "contact-intensive workers experienced a 9 percentage point increase in informality relative to teleworkable workers (p = 0.153)." A p-value of 0.153 does not permit the unqualified causal language used throughout the abstract and conclusion ("causal evidence that COVID-19 produced permanent informality scarring," Section 7). This is not a rounding issue or minor infelicity—the binary specification on which the 9 pp headline is based fails to reject the null of no effect at any standard significance level. The continuous specification in Table 2 achieves 10% significance in some years, but that is a distinct result with a different economic interpretation (marginal effect of a full unit change in TW, which is largely out-of-sample). The authors must either: (a) present the binary specification as the primary table with correct inference, or (b) scale back the abstract's causal claims to match the actual significance level. A result significant at p = 0.153 can be reported but not as unqualified causal evidence.

*Concrete fix*: Revise the abstract to read "suggestive" or "marginally significant" or move to a specification that achieves conventional significance, and adjust all downstream causal language accordingly.

**3. Reactiva Perú confound remains unaddressed (second carry-over from Round 2)**

The S/ 60 billion Reactiva Perú payroll-conditioned credit guarantee program provided subsidized credit to firms that retained workers on formal payrolls. Access was strongly tilted toward firms in teleworkable sectors (services, finance, formal manufacturing) since eligibility required prior tax compliance and formal worker registration. This creates a direct alternative mechanism: the observed formality differential may partly reflect the *preservation* of formality in teleworkable sectors via subsidized firm credit, not purely a *loss* of formality in contact-intensive sectors due to the nature of the occupations. The current paper offers no discussion of this program anywhere in its six substantive sections. At a minimum, the identification discussion must acknowledge that Reactiva Perú was contemporaneous with the period of maximum treatment effect (2021) and explain why it does not invalidate the teleworkability interpretation.

*Concrete fix*: Add a paragraph in Section 4 (Identification) discussing Reactiva Perú as a potential confound, and either (a) provide evidence that program take-up was not differentially concentrated in teleworkable occupations conditional on the outcome, or (b) acknowledge this as a binding limitation on causal claims.

**4. Monthly income figures remain implausible without explanation (second carry-over)**

Table 1 reports mean monthly incomes of 15,440 soles (contact-intensive) and 25,408 soles (teleworkable) for the 2020–2024 period. Peru's national average monthly earnings during this period were approximately 1,500–1,800 soles. These figures are 8–14× the national average, far outside the plausible range even for upper-income workers. This discrepancy appears across two revision cycles without any clarifying note. Possible explanations include: the variable capturing annual income mislabeled as monthly, the sample restricted to formal workers with unusually high earnings, a unit or scaling error in the variable construction, or a coding bug. Any of these explanations is resolvable. The failure to address this after two rounds undermines confidence in the data processing pipeline.

*Concrete fix*: Add a table note explaining the income variable construction (unit, trimming, sample restriction) and verify that the figures are consistent with ENAHO documentation.

**5. Heterogeneity section (Section 5.4) contains no results**

The heterogeneity subsection, which the paper identifies as a substantive finding (gender, region, firm size, age), contains no coefficients, no standard errors, and no conclusions. Each paragraph ends with a statement of what the analysis "tests" or "reveals" without reporting what it actually found. For example: "The gender-specific interaction coefficients reveal whether the scarring burden fell disproportionately on one gender." Figure 3 presumably contains the results, but a figure without textual interpretation of magnitudes, significance, and direction is not a scientific finding. This section should either report the results or be removed.

*Concrete fix*: Add the numerical results (at minimum the 2021 and 2024 interaction coefficients by subgroup with SEs) and provide a substantive interpretation.

---

### Minor Concerns

1. **Attrition severity under-weighted in the causal framing.** Section 6.3 acknowledges 96.9% attrition by 2024 but characterizes the result as not problematic because teleworkability does not predict attrition. Non-differential attrition prevents selection bias in the *level* of treatment but does not rescue the interpretation: with 96.9% of the 2020 baseline absent by 2024, the 2024 estimates are drawn almost entirely from a new cohort of workers. The conclusion's language about "permanent informality scarring" implies individual-level persistence, which cannot be established when fewer than 1 in 30 baseline individuals is observed in the final year. The paper already notes this in Section 4.4, but the conclusion restates the strong causal language without the qualification.

2. **Within-estimator results (Section 5.3) lack standard errors.** The FE coefficients (-0.256 and -0.237) are stated in the text with no SEs, no significance indicators, and no table reference. If these results are offered to "confirm that the result is not driven by compositional changes" (Section 7), they need proper inference.

3. **Parallel trends limitation lacks specificity.** Section 6.4 acknowledges the absence of pre-pandemic data but does not engage with the empirical severity of the problem. Table 1 shows a 31.9 pp rurality gap and a 19.4 pp gender composition gap between treatment groups. These are large structural differences. The bare statement "the identifying assumption rests on plausibility" does not acknowledge that these observable baseline differences make differential pre-trends more rather than less likely. The paper should discuss which structural factors most threaten parallel trends and whether sector-specific controls could partially address them.

4. **Specification label confusion in Table 2.** The table header references "TW$_\text{low}$" (binary indicator), while the main text and Section 4.2 state that the primary specification uses the *continuous* teleworkability score. The column label in Table 2 and the method described in the table notes must be reconciled.

5. **Abstract framing of the Wald test (p=0.937) is potentially misleading.** "Zero attenuation through 2024" is one interpretation of failing to reject H₀ for a test with p=0.937. But this result is also entirely consistent with the null being true (no effect in any year), which cannot be ruled out given the non-significant binary specification. The "scarring" interpretation requires that the effect exists and persists; the Wald test only addresses the second condition conditional on the first.

---

### Recommendation

**Major Revision**

The authors made genuine progress in Round 3 on internal consistency, and the acknowledged limitations (2020 contamination, rotating panel, pre-trend absence) reflect honest engagement with the design's constraints. However, four items that were explicitly labeled "must-address" in the editorial letter—wild cluster bootstrap, Reactiva Perú confound, income implausibility, and the headline-result traceability—remain open after two revision cycles, and a new inferential problem (abstract leading with p = 0.153 as an unqualified causal finding) was introduced in the revision. The paper cannot be recommended for acceptance until (at minimum) items 1–3 of the major concerns are resolved.

---

```json
{
  "score": 57,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "identification_strategy": 52,
    "estimation_implementation": 60,
    "statistical_inference": 48,
    "robustness_sensitivity": 58,
    "replication_readiness": 62
  },
  "sanity_checks": {
    "sign": "PASS",
    "magnitude": "FAIL",
    "dynamics": "PASS",
    "consistency": "FAIL"
  },
  "major_comments": [
    "Wild cluster bootstrap not implemented despite two consecutive rounds of editorial requirement; 43-cluster conventional inference is unreliable for a headline coefficient at borderline 10% significance.",
    "Abstract reports p=0.153 as a headline causal finding without flagging statistical insignificance; the conclusion uses unqualified causal language ('causal evidence of permanent informality scarring') inconsistent with this p-value.",
    "Reactiva Peru payroll-conditioned credit program (S/ 60bn) unaddressed for second consecutive round; creates a plausible alternative mechanism for the observed formality differential in teleworkable sectors.",
    "Monthly income figures (15,440 and 25,408 soles) are 8-14x Peru's national average and remain without any clarifying note after two rounds; data pipeline reliability cannot be assessed.",
    "Heterogeneity section (Section 5.4) contains no numerical results — only statements of what the analysis 'tests'; every paragraph must report actual coefficients, SEs, and direction of effects."
  ],
  "minor_comments": [
    "96.9% attrition by 2024 means the final-year estimates are drawn almost entirely from a new cohort; 'permanent scarring' language in the conclusion requires individual-level tracking that the rotating panel cannot provide.",
    "Within-estimator coefficients (-0.256, -0.237) are cited as corroborating evidence in the conclusion but appear in the text without standard errors or significance levels.",
    "Table 2 column label reads 'TW_low' (binary indicator) while Section 4.2 states the primary specification uses the continuous score; label and method description must match.",
    "Non-rejection of the Wald test (p=0.937) is presented as evidence of zero attenuation, but this framing is only valid conditional on the effect existing; the non-significant binary specification makes this conditional interpretation fragile.",
    "The identification section acknowledges parallel trends but does not engage with the 31.9 pp rurality gap and 19.4 pp gender gap between groups, which are observable signals that differential pre-trends are plausible."
  ]
}
```