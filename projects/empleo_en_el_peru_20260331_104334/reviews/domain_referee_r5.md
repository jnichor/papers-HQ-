## Referee Report — Round 5 Review
**COVID-19 and the Formality Recovery Path in Peru: A Worker-Level Panel DiD Using Sectoral Teleworkability**

---

### Summary

This paper estimates the effect of COVID-19 on persistent labor informality in Peru using a difference-in-differences design that exploits differential occupational exposure through the Dingel-Neiman (2020) teleworkability index, applied to five waves of the ENAHO employment panel (2020–2024, N = 262,733). The continuous treatment specification yields interaction coefficients of −19 to −22 pp (p < 0.05 in 2022 and 2024), while the binary specification yields an insignificant 9 pp differential (p = 0.153); neither attenuates through 2024. The revised paper represents meaningful progress over the previous round but leaves two of the seven must-address items from Round 4 unresolved.

---

### Main Assessment

**Progress since Round 4.** The authors have addressed several substantive concerns credibly: (1) causal language has been substantially softened throughout, with the abstract now correctly framing both the continuous and binary results in associational language; (2) Table 2 is now clearly structured with separate, correctly labeled panels for the continuous and binary specifications, resolving the earlier conflation; (3) Section 5.4 now reports numerical coefficients and p-values for all heterogeneity subgroups; and (4) the abstract now transparently states the binary result's insignificance at the 5% level. These are genuine improvements that address real concerns.

**Remaining deficiencies.** Two must-address items from Round 4 remain unresolved: (a) wild cluster bootstrap inference has not been implemented despite 40 clusters falling below the Cameron-Miller threshold; and (b) Reactiva Perú—a plausible alternative channel flagged explicitly in Round 4—is not mentioned anywhere in the paper. The pre-2020 parallel trends test has been deferred to future research rather than executed, despite the availability of ENAHO 2017–2019 data and a 32 pp rurality gap between treatment groups that makes common trends structurally implausible without empirical validation. These are not minor editorial matters; they are conditions for credible causal identification and adequate alternative-channel discussion.

---

### Major Comments

**1. Wild cluster bootstrap remains unimplemented (Round 4 must-address, unresolved).**

The revised paper continues to report only conventional ISCO-clustered standard errors as the headline inference procedure, despite 40 clusters falling below the Cameron-Miller (2008) threshold at which asymptotic cluster-robust SEs exhibit well-documented over-rejection bias. This matters differentially across specifications: the continuous results (p < 0.05 in 2022 and 2024) might survive bootstrap inference, but the binary 2021 result at p = 0.153 could move in either direction. The authors must implement wild cluster bootstrap with Rademacher weights (Roodman et al. 2019, `boottest` in Stata or `wildclusterboot` in R) and report wild bootstrap p-values as the primary inferential standard, with conventional clustered SEs as a secondary comparison. The current Table 2 note that results use "40 clusters" is not a substitute for this; it simply documents the known problem without resolving it.

**2. Reactiva Perú omitted (Round 4 must-address, unresolved).**

The paper makes no mention of Reactiva Perú (S/. 60 billion, 2020–2021), Peru's primary COVID-era credit support program for formal firms that conditioned access on maintaining payroll and social security obligations. This is a directly relevant institutional feature for two reasons. First, the paper's headline mechanism—the differential *retention* of social security coverage in teleworkable vs. contact-intensive sectors—is precisely the condition firms needed to satisfy to access Reactiva funds. Teleworkable-sector firms (disproportionately larger, formal, urban) were structurally better positioned to maintain payrolls and access credit. Second, contact-intensive firms (agriculture, construction, personal services) were both less able to telework *and* less likely to be formal Reactiva beneficiaries, making the two channels observationally indistinguishable in this design. The authors cannot establish that their estimated differential reflects teleworkability per se rather than differential exposure to the largest economic policy intervention of the period. At minimum, Section 6 must discuss Reactiva as an alternative channel and explain why the teleworkability mechanism is more plausible or how the two might be disentangled.

**3. Pre-2020 parallel trends: deferral to future research is insufficient given compositional imbalances.**

Table 1 documents a 32 pp rurality gap (44% rural vs. 12%) and a 19 pp gender gap (42% vs. 61% female) between contact-intensive and teleworkable workers. These are not minor imbalances—they represent structural differences correlated with distinct pre-pandemic labor market trajectories. Rural Peru has substantially different informality dynamics than urban Peru (agricultural informality rates exceed 95%), and female labor force participation responds differently to aggregate shocks. The paper's conclusion frames a pre-trend test as a recommendation for future work using ENAHO 2017–2019 data (publicly available from INEI). This framing is inadequate given that (a) the data are accessible, (b) the compositional gaps make common trends structurally implausible, and (c) the pre-trend test was explicitly required in Round 4. The authors should execute the pre-trend test in the current revision or provide a direct empirical argument—for example, showing that within-region or within-gender comparisons narrow the compositional gap without eliminating the informality differential.

**4. Income variable explanation partially addresses but does not resolve the anomaly.**

The Table 1 note now explains that S/. 15,440 (contact-intensive) and S/. 25,408 (teleworkable) represent gross income from all jobs including in-kind payments. However, the contact-intensive *median* of S/. 14,495—disclosed in the note—remains 14× the national minimum wage for a sample that is 44% rural and concentrated in agriculture, construction, and personal services. The explanation that professional/managerial concentration drives the teleworkable mean is plausible, but it does not explain why the modal contact-intensive worker (agricultural laborer, rural, informal) reports median income 14× the minimum wage. The authors should report the 25th and 75th percentiles of the income distribution by group, confirm whether the variable is in nominal or real (deflated) terms, and state the reference year for the minimum wage comparison. If the variable is in fact annual income mislabeled as monthly, this must be corrected.

---

### Minor Comments

**1. Cluster count discrepancy.** Section 3.4 states the crosswalk aggregates to "43 ISCO-08 sub-major groups," while the abstract, Section 3.5, and Table 2 report "40 clusters." The discrepancy is unexplained. If three groups are dropped from the regression due to empty cells or collinearity, this should be documented in the table notes.

**2. "Strengthens the causal interpretation" language.** Sections 6.3 and 7 retain the phrase "strengthens the causal interpretation" to describe non-differential attrition and the within-estimator. While standard in the DiD literature, this framing is overstated in a design with no pre-trend test and large compositional imbalances between groups. Replace with "is consistent with a causal interpretation" throughout.

**3. Within-estimator results not tabulated.** Section 5.3 reports within-estimator coefficients (−0.256 in 2021, −0.237 in 2024) only in text. As a "secondary specification" described in Section 4.2, these warrant a dedicated column in Table 2 or an appendix table for reproducibility.

**4. Social security mechanism deserves fuller institutional elaboration.** Section 6.1's finding—that the informality effect operates through social security loss rather than firm-size changes—is the paper's most distinctive substantive contribution. The current three-sentence discussion is underweight. A brief elaboration connecting this to the specific institutional mechanics (employer social security obligations under Peru's health insurance framework, SUNAFIL enforcement capacity during lockdowns) and its interaction with Reactiva Perú's payroll-conditioning requirements would both strengthen the contribution and directly address the alternative-channel concern raised in Major Comment 2.

**5. Urban-only sensitivity as partial substitute for Saltiel (2020) validation.** The paper recommends in Section 6.4 that future work validate the teleworkability crosswalk against Saltiel's (2020) developing-country adaptation. A useful partial check—implementable within the existing data—is to restrict the main specification to urban workers, where the U.S.-derived task descriptions are more likely to translate. If results are stable, this partially addresses the index-validity concern without requiring the full Saltiel crosswalk.

---

### Missing Literature

- **Cameron, C., Gelbach, J., & Miller, D. (2008).** "Bootstrap-based improvements for inference with clustered errors." *Review of Economics and Statistics.* — Theoretical basis for the cluster-number concern; should be cited in the SE discussion.
- **Roodman, D., Nielsen, M.Ø., MacKinnon, J.G., & Webb, M.D. (2019).** "Fast and wild: Bootstrap inference in Stata using boottest." *The Stata Journal.* — Implementation reference for the required wild bootstrap.
- **Bosch, M. & Maloney, W.F. (2010).** "Comparative analysis of labor market dynamics using Markov processes: An application to informality." *Labour Economics.* — Standard reference on informality transition rates and the scarring mechanism in Latin America; relevant to Section 2.1 and the persistence discussion.
- **Neidhöfer, G., Lustig, N., & Morales, M. (2022).** "Intergenerational transmission of lockdown consequences." *Journal of Economic Inequality.* — Related scarring dynamics in LAC post-COVID.
- **Loayza, N.V. (2016).** "Informality in the process of development and growth." *The World Economy.* — Canonical framework for informality-development tradeoffs; relevant positioning for the Peru informality baseline.

---

### Recommendation

**Major Revision.** The paper has made genuine and substantive progress since Round 4, and the core empirical contribution—a five-year event study documenting persistent teleworkability-based informality differentials in Peru—remains valuable. However, two must-address items from the previous round (wild cluster bootstrap; Reactiva Perú) remain entirely unresolved, and the parallel trends concern is deferred rather than addressed despite available data. These are not cosmetic issues: they bear directly on whether the paper's inference is valid and whether the identified mechanism is correctly attributed. A targeted revision addressing Major Comments 1–3 specifically would substantially improve the paper's credibility.

---

```json
{
  "score": 63,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "contribution_novelty": 72,
    "literature_positioning": 65,
    "substantive_arguments": 58,
    "external_validity": 63,
    "journal_fit": 70
  },
  "major_comments": [
    "Wild cluster bootstrap remains unimplemented despite 40 clusters falling below the Cameron-Miller threshold; this is the primary required inference method for this design and was a must-address item in Round 4. Conventional clustered SEs should be demoted to secondary status.",
    "Reactiva Perú (S/. 60bn payroll-conditioned credit program, 2020-2021) is not mentioned anywhere in the revised paper despite being an explicitly flagged must-address confounder. The teleworkability mechanism and the Reactiva access channel are observationally indistinguishable in this design; the paper must discuss and attempt to rule out this alternative explanation.",
    "The pre-2020 parallel trends test has been deferred to future research rather than executed, despite (a) ENAHO 2017-2019 data being publicly available from INEI, (b) a 32 pp rurality and 19 pp gender gap between groups making common trends structurally implausible, and (c) this test being an explicit Round 4 must-address requirement. This must be implemented in the current revision.",
    "The Table 1 income figures (S/. 15,440 and S/. 25,408) remain unexplained at depth: the table note does not account for why the contact-intensive median (S/. 14,495) is 14x the minimum wage for a group that is 44% rural and concentrated in agriculture and manual services. The authors must report distributional statistics (25th/75th percentiles), confirm deflation status and reference year, and document the income variable construction pipeline."
  ],
  "minor_comments": [
    "Cluster count discrepancy: Section 3.4 states 43 ISCO-08 sub-major groups but all inference tables and the abstract report 40 clusters; the dropped groups should be identified and documented in table notes.",
    "The phrase 'strengthens the causal interpretation' in Sections 6.3 and 7 is overstated for a design with no pre-trend test and large compositional imbalances; replace with 'is consistent with a causal interpretation' throughout.",
    "Within-estimator results (-0.256 in 2021, -0.237 in 2024) are reported only in Section 5.3 prose; as a named secondary specification, these warrant a table column or appendix table.",
    "The social security mechanism finding (Section 6.1) is the paper's most institutionally novel contribution and deserves two additional paragraphs connecting to Peru's specific social security legal framework and the Reactiva payroll-conditioning requirement.",
    "A simple urban-only sensitivity check would partially substitute for the Saltiel (2020) crosswalk validation recommended for future work, is feasible with existing data, and would address index-validity concerns for the non-agricultural sample."
  ],
  "missing_literature": [
    "Cameron, Gelbach & Miller (2008) on bootstrap-based inference with clustered errors — required citation for the cluster-number concern",
    "Roodman, Nielsen, MacKinnon & Webb (2019) 'Fast and wild' boottest — required implementation reference for wild cluster bootstrap",
    "Bosch & Maloney (2010) on informality transition dynamics in Latin America — standard reference for the scarring mechanism",
    "Neidhöfer, Lustig & Morales (2022) on intergenerational transmission of COVID lockdown consequences in LAC",
    "Loayza (2016) on informality in the development process — canonical framework for Peru's informality baseline"
  ]
}
```