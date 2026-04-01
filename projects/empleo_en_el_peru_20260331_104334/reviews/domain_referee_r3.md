## Referee Report — Round 2 Review

**Journal:** Development Economics / Labour Economics

**Paper:** "COVID-19 and the Formality Recovery Path in Peru: A Worker-Level Panel DiD Using Sectoral Teleworkability"

---

### Summary

This paper estimates the causal effect of COVID-19 on labor informality in Peru using a difference-in-differences design that exploits the Dingel-Neiman (2020) teleworkability index as pre-determined treatment intensity. Using ENAHO panel data from 2020–2024, the authors report that contact-intensive workers experienced a differential informality increase that persisted through 2024, interpreted as pandemic scarring. The revised version attempts to address four must-address items from Round 1: the sign/label inconsistency, the SE mislabeling, cross-definition divergence, and the absence of pre-pandemic data.

---

### Assessment of Revisions

The authors have made genuine progress on two of the four must-address items. The sign/label inconsistency is now resolved through a coherent restructuring: the main specification uses the continuous teleworkability score (negative γ_k = teleworkable workers were *protected*), and the 9 pp binary estimate is relegated to a robustness check. The cross-definition divergence (social security vs. contract vs. firm size) is now given a substantive interpretation — the shock operated through social security shedding — which is plausible and improves the paper. These are real improvements.

However, the two most identification-critical issues from Round 1 remain substantially unaddressed, and new inconsistencies introduced in revision further undermine confidence.

---

### Major Comments

**1. Pre-pandemic data: Must-address item unresolved (identification-critical)**

The previous round explicitly required incorporation of ENAHO waves 2017–2019 to test parallel pre-trends, citing their public availability from INEI. The revised paper acknowledges this limitation in one sentence each in Sections 6.4 and 7, deferring it to "future research." This is not acceptable. The treatment and control groups differ by 32 pp in rurality (44% vs. 12%) and 19 pp in gender composition (42% vs. 61% female). Rural workers in Peru had systematically higher pre-pandemic informality *growth* due to agricultural informalization and migration dynamics. Without pre-trend evidence, the identifying assumption is not merely untestable — it is *a priori* implausible given the documented compositional differences. The ENAHO 2017–2019 rotating panel data is publicly available at no cost. The authors must incorporate it.

**2. Wild cluster bootstrap: Must-address item unresolved (inference-critical)**

The revised Table 2 now correctly shows cluster-robust standard errors (progress from Round 1). However, the Cameron-Miller threshold of ≥50 clusters for reliable cluster inference has not been met: the paper reports 40 clusters in Table 2 and 43 clusters in the abstract — itself an inconsistency. More importantly, wild cluster bootstrap with Rademacher weights (≥999 replications) was explicitly required in Round 1 and has not been implemented. With 40 clusters, standard asymptotic cluster SEs are downward-biased, and the borderline significance of the 2021 interaction (10% level in the continuous spec) is sensitive to this. The inference conclusion about scarring rests on significance claims that cannot be verified without the bootstrap.

**3. Persistent internal inconsistency: HC1 vs. clustered SEs**

Section 3.5 (Data) still states: "Standard errors are heteroskedasticity-robust (HC1)." Table 2 now shows clustered SEs. These directly contradict. The abstract states 43 clusters; the table states 40. The paper appears to have been selectively revised without full internal reconciliation. These inconsistencies raise concerns about which SE type was actually used in the reported estimates.

**4. Headline claim disconnected from main table**

The abstract, introduction, and conclusion all lead with "9 percentage point increase in informality." Table 2 — the main results table — shows interaction coefficients of −0.20 to −0.22 from the continuous specification. The 9 pp figure derives from the binary specification, which is described as a robustness check and has no dedicated table in the paper. For a reader arriving via the abstract, the main table does not verify the headline result. Either: (a) present the binary specification as the primary table and the continuous as supplementary, or (b) derive the 9 pp explicitly from the continuous estimates in the text and show the binary table in the appendix. As currently structured, the paper's headline claim is not reproducible from its main display.

**5. Reactiva Perú remains absent**

This was a "should address" item in Round 1. The S/ 60 billion Reactiva Perú credit guarantee program, which conditioned support on payroll maintenance by formal firms and was disproportionately used by firms in teleworkable sectors, creates a mechanical wedge correlated with treatment. The program is not mentioned anywhere in the revised paper. This omission is particularly important given the paper's strong scarring interpretation: if formal firms in teleworkable sectors were differentially supported in maintaining payroll, the "protection" of teleworkable workers may reflect the program rather than teleworkability per se.

**6. Income data appears implausible**

Table 1 reports mean monthly income of 15,440 soles for contact-intensive workers and 25,408 soles for teleworkable workers. Peru's national average monthly earnings are approximately 1,500–2,000 soles. Even for a selected subsample of income reporters (78,180 of 196,069 observations have income data), figures 8–12x the national average are unexplained. The paper provides no note on income units or sample restrictions. This raises a data quality concern — whether the variable is annual income, income in a different unit, or represents a coding issue — that should be explicitly addressed.

---

### Minor Comments

1. The FE within-estimator results (Section 5.3) report positive coefficients (0.103 in 2021) while Table 2 shows negative γ_k. The text explains this by noting the FE spec uses the binary TW_low indicator (contact-intensive = 1), while the main spec uses the continuous score. This sign reversal should be flagged explicitly with a note in the table or a clarifying sentence, as the sign switch is easy to misread.

2. Section 5.2 reports the scarring Wald test as p = 0.937 while the abstract states p = 0.994. The two values are inconsistent. One appears to be a transcription error.

3. Event-study figures for all three informality definitions (social security, written contract, small firm) are not shown. Given that the cross-definition divergence is now claimed as a "substantive finding" central to the mechanism, visual evidence of the three event-study profiles is necessary, not merely the tabulated scalars in Section 6.1.

4. The paper does not control for sector-year trends, which is standard in DiD designs where treatment varies at the sector level. Agricultural commodity price shocks, construction cycles, and tourism collapses during 2020–2022 would generate sector-level informality variation that could bias the event-study coefficients.

5. The data audit notes a weight max/median ratio of 3,394, which implies the winsorizing at the 1st–99th percentile still leaves extreme weights in the distribution. The paper should report the effective sample size (ESS = (Σw)² / Σw²) under the winsorized weights to assess the practical influence of high-weight observations.

---

### Missing Literature

- **Levy, S. (2008).** *Good Intentions, Bad Outcomes: Social Policy, Informality, and Economic Growth in Mexico.* Brookings. The argument that contributory social programs (like Peru's EsSalud) create informality traps is central to the policy discussion but unaddressed.
- **Loayza, N. (2007).** "The causes and consequences of informality in Peru." BCRP Working Paper. The Peru-specific informality literature is underrepresented; this paper establishes the structural baseline the authors build upon.
- **Fajnzylber, P., Maloney, W., & Montes-Rojas, G. (2011).** "Does formality improve micro-firm performance?" *Journal of Development Economics.* Directly relevant to the social security mechanism.
- **Fernández-Bastidas, R. (2023).** Recent work on Peruvian labor market recovery post-COVID exists and should be checked for overlap and positioning.
- **Cameron, A.C. & Miller, D.L. (2015).** "A practitioner's guide to cluster-robust inference." *Journal of Human Resources.* Should be cited when discussing the 40-cluster limitation.

---

### Recommendation

**Major Revision**

The paper addresses a genuinely important question with a reasonable design, and the revised presentation of the sign issue and cross-definition mechanism is improved. However, the failure to incorporate publicly available pre-pandemic ENAHO data (despite this being a Round 1 must-address requirement), the absence of wild cluster bootstrap for sub-threshold cluster counts, the unresolved internal SE inconsistencies, and the disconnection between the abstract's headline result and the main table collectively mean the paper's primary causal claim cannot yet be verified. These are not marginal issues — they are the identification core of the paper. A further revision that implements pre-trend testing on 2017–2019 ENAHO waves, wild bootstrap inference, full reconciliation of SE reporting, and discusses Reactiva Perú would substantially strengthen the submission.

---

```json
{
  "score": 60,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "contribution_novelty": 72,
    "literature_positioning": 62,
    "substantive_arguments": 55,
    "external_validity": 60,
    "journal_fit": 63
  },
  "major_comments": [
    "Pre-pandemic ENAHO 2017–2019 data publicly available from INEI and still not incorporated despite Round 1 must-address requirement. The 32 pp rurality gap and 19 pp gender composition gap between treatment groups make the parallel trends assumption a priori implausible without empirical pre-trend evidence. This is the single most critical unresolved issue.",
    "Wild cluster bootstrap with Rademacher weights not implemented despite Round 1 requirement. With 40–43 clusters (below Cameron-Miller ≥50 threshold), asymptotic cluster SEs are downward-biased. The 2021 coefficient is significant at only 10% in the main specification; this finding may not survive bootstrap inference.",
    "Internal SE inconsistency persists: Section 3.5 states HC1 robust SEs while Table 2 shows clustered SEs. Abstract reports 43 clusters; Table 2 reports 40. The paper was selectively revised without full reconciliation, and it is unclear which SE type underpins the reported results.",
    "Headline result (9 pp, abstract) is not reproducible from the main table (Table 2, continuous spec showing –0.20 to –0.22). The binary specification yielding 9 pp has no primary table in the paper. The disconnection between the abstract's headline claim and the main display must be resolved by either promoting the binary spec to primary or deriving the 9 pp explicitly from the continuous estimates in the text.",
    "Reactiva Perú (S/ 60 bn payroll-conditioned credit guarantee) remains entirely absent from identification discussion. Teleworkable-sector firms disproportionately accessed this program, potentially mechanically explaining teleworkable workers' relative formality protection independently of teleworkability per se.",
    "Income figures in Table 1 (15,440 and 25,408 soles/month) are 8–12x Peru's national average monthly earnings. No note explains the unit, sample restriction, or potential coding issue. This unexplained implausibility undermines confidence in the data processing pipeline."
  ],
  "minor_comments": [
    "Wald test p-value reported as 0.994 in abstract and 0.937 in Section 5.2. One is a transcription error; reconcile.",
    "FE within-estimator results show positive coefficients (0.103 in 2021) while main Table 2 shows negative γ_k. Sign reversal due to binary vs. continuous TW specification is explained in prose but should be flagged explicitly in the table notes to prevent misreading.",
    "Event-study plots for all three informality definitions (social security, contract, firm size) are not shown. Given that cross-definition divergence is now presented as the paper's mechanism claim, visual evidence of all three event-study profiles is necessary.",
    "No sector-year trend controls. Agricultural cycles, construction collapses, and tourism shocks during 2020–2022 generate sector-level informality variation that could confound the event-study coefficients.",
    "Effective sample size under winsorized weights should be reported alongside the weight max/median ratio of 3,394 cited in the audit, to assess influence of extreme observations.",
    "Saltiel (2020) developing-country teleworkability adaptation is cited but not implemented even as a robustness check. Given that the paper uses a U.S.-derived index applied to Peru, this validation gap should at minimum be quantified in terms of how different the Saltiel index would rank Peruvian occupations."
  ],
  "missing_literature": [
    "Levy, S. (2008). Good Intentions, Bad Outcomes: Social Policy, Informality, and Economic Growth in Mexico. Brookings. Central to the employer social security shedding mechanism claimed.",
    "Loayza, N. (2007). The causes and consequences of informality in Peru. BCRP Working Paper. Foundational Peru-specific baseline that is underrepresented.",
    "Fajnzylber, Maloney & Montes-Rojas (2011). Does formality improve micro-firm performance? Journal of Development Economics. Relevant to social security mechanism.",
    "Cameron & Miller (2015). A practitioner's guide to cluster-robust inference. Journal of Human Resources. Should be cited when motivating wild bootstrap with 40 clusters.",
    "Reactiva Perú program evaluation literature (BCRP working papers 2020–2022) needed to assess identification threat from payroll-conditioned credit guarantees."
  ]
}
```