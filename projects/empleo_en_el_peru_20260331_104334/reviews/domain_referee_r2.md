## Referee Report

**Journal of Development Economics / World Development**

---

### Summary

This paper estimates the causal effect of COVID-19 on labor informality in Peru using a difference-in-differences design that exploits variation in occupational teleworkability from the Dingel-Neiman (2020) index. Drawing on five waves of the ENAHO employment panel (2020–2024), the authors find that contact-intensive workers experienced approximately 9 percentage points higher informality relative to teleworkable workers in 2021, with no measurable attenuation through 2024. The paper concludes that COVID-19 produced permanent population-level informality scarring and suggests portable social protection may be more effective than firm-based formalization strategies.

---

### Main Assessment

**Strengths.** The paper addresses a genuinely important question with a sensible identification strategy. The four-year horizon is the paper's main value-added over shorter-window COVID-informality studies, and the authors are commendably honest about the limitations of their design (no pre-trends test, rotating panel constraints, 2020 baseline contamination). The distinction between individual-level scarring and population-level differential—a distinction many event-study papers blur—is appropriately drawn.

**Weaknesses.** The paper has four problems of varying severity: (1) a verifiable inconsistency between the claimed main result (9 pp increase for contact-intensive workers) and what Table 2 actually displays; (2) the complete absence of pre-2020 ENAHO waves, which exist and would permit a parallel-trends test; (3) no discussion of Peru's severe political instability in 2021–2023 as an independent confound for the formality trajectory; and (4) omission of Reactiva Perú and other COVID-policy programs that differentially affected formal versus informal workers' incentives. Together these issues undermine confidence in the causal interpretation without sinking the core empirical exercise.

---

### Major Comments

**1. Table 2 sign inconsistency with abstract/text (critical).** The abstract and Section 5 state that contact-intensive workers experienced a 9 pp *increase* in informality relative to teleworkable workers. Table 2, however, reports interaction coefficients (labeled "Interaction (TW$_{\text{low}}$)") of −0.202, −0.220, −0.189, −0.190 across 2021–2024. If TW$_{\text{low}}$ = 1 for contact-intensive workers, a negative coefficient implies they experienced *lower* informality growth than the reference group—the opposite of the headline claim. Three resolutions are possible: (a) the table is displaying the continuous specification (with TW ∈ [0,1]) rather than the binary, in which case the label is wrong and the 9 pp figure must be derived from a marginal effect evaluated at group means; (b) the binary dummy is coded 1 for *teleworkable* workers (inverse of what the table note states), which would be a labeling error; or (c) the sign on the interaction term is reported incorrectly. The authors must reconcile this discrepancy explicitly. The 9 pp figure in the abstract appears to emerge from the binary specification, but that table is not presented as such.

**2. No pre-pandemic ENAHO waves.** ENAHO is fielded annually going back to at least 2001. Waves for 2017–2019 are publicly available from INEI. The paper's identification rests on parallel trends that, by the authors' own admission, "cannot be tested." This is an unnecessary weakness: including 2017–2019 waves would provide three pre-pandemic event-study coefficients (relative to a 2019 baseline), enabling the standard visual and statistical pre-trend validation. Peru experienced several sector-specific shocks pre-2020 (El Niño 2017, mining strikes) that could have generated non-parallel trends between contact-intensive and teleworkable workers. The omission of available pre-period data is the paper's most consequential shortcoming.

**3. Peru's political instability as confound.** The paper attributes the persistence of the informality differential to COVID-19 scarring, but Peru underwent extraordinary political disruption between 2021 and 2023: the election and subsequent impeachment of President Castillo (June 2021–December 2022), the Boluarte government's contested legitimacy, and sustained protest-related economic disruption concentrated in sectors like mining and transport that overlap heavily with contact-intensive occupations. This institutional instability constitutes an independent shock to formal employment relationships that is not orthogonal to the treatment variable. The zero-attenuation Wald test ($p = 0.994$) is equally consistent with (a) genuine COVID scarring or (b) a subsequent shock correlated with contact-intensity. The paper must discuss this confound explicitly and, if possible, attempt to decompose the post-2022 portion of the effect.

**4. Reactiva Perú and differential policy exposure.** The government's largest economic stabilization response—Reactiva Perú, which extended S/ 60 billion in credit guarantees to formal firms conditional on payroll maintenance—is nowhere discussed. Reactiva Perú created a formal–informal wedge in firm survival that could independently predict the trajectory of social security coverage among workers in affected sectors. Teleworkable occupations are disproportionately in services and professional sectors that accessed Reactiva Perú. If Reactiva artificially maintained formal contracts for teleworkable workers during 2020–2021, the DiD captures a policy-mediated wedge, not purely occupation-based teleworkability. Similarly, Bono Independiente transfers and AFP emergency withdrawals affected informal workers' behavior. The identification section should address how these programs interact with the identifying variation.

**5. Survey weight extremity.** The data audit flags a max/median weight ratio of 3,394:1, indicating at least one observation receives weight nearly 3,400 times the median. The paper states weights are winsorized at the 1st/99th percentiles, yet the data audit reports this ratio as if the winsorization is insufficient or applied post-winsorization. Given that the outcome is a binary indicator and the estimator is WLS, a single extreme observation can have catastrophic leverage. The authors should report the effective sample size before and after winsorization, and verify that the main coefficient is not driven by a handful of high-weight observations (e.g., via leave-one-out diagnostics on the highest-weight cluster).

**6. Wild cluster bootstrap for 43-cluster inference.** The paper clusters at the ISCO-08 2-digit level (43 clusters). Cameron and Miller (2015) and MacKinnon et al. (2022) demonstrate that cluster-robust variance estimators are unreliable below approximately 50 clusters, with over-rejection rates that increase sharply as cluster count falls. With 43 clusters, the $p < 0.001$ claim in the abstract should be treated cautiously. The authors should implement the wild cluster bootstrap (Rademacher weights, 999 replications) as the primary inference method, with standard CRVE as the secondary.

---

### Minor Comments

**1. Income descriptive statistics.** Table 1 reports mean monthly income of 15,440 soles for contact-intensive workers and 25,408 for teleworkable workers. Peru's median monthly labor income is approximately 1,000–1,500 soles in this period; the values reported appear implausibly high even accounting for the smaller income sample (N = 78,180 vs. 196,069 total). The footnote should explain whether these are (a) annual figures erroneously labeled monthly, (b) weighted means with un-winsorized weights, or (c) conditional on positive earnings among wage workers only. If the latter, the sample selection should be noted as a caveat on income comparisons.

**2. The 0.20 teleworkability threshold.** The binary treatment threshold (TW < 0.20) is not justified beyond the observation that it places 75.7% of workers in the treated group. The paper should show that the 9 pp result is not sensitive to alternative thresholds (e.g., 0.15, 0.25, 0.30), particularly because the continuous specification is described as the "main" one while the binary is "robustness," but the headline number comes from the binary specification.

**3. bosch2025 citation.** The reference to "Bosch (2025)" in the introduction and literature review is unusual—if this is a working paper, it should include its provenance (NBER, IZA, SSRN). If it refers to a published paper, the date should be confirmed. This citation underpins a key claim about Peru's formalization policies and deserves a complete reference.

**4. Contract-based informality near zero.** Section 6.1 notes that the contract-based informality measure yields a coefficient of "near zero (0.002)." This is important because it implies that the pandemic's formalization shock operated almost entirely through social security removal without corresponding changes in written contract status. However, in Peru's labor law, a worker can be formally contracted but still lose social security if the employer fails to register with EsSalud. The divergence between definitions may reflect this institutional feature—employer-side noncompliance rather than worker-side transition—and deserves a paragraph of institutional discussion rather than a one-sentence observation.

**5. Saltiel (2020) not implemented.** The paper acknowledges that Saltiel (2020) provides a developing-country adaptation of the Dingel-Neiman index and recommends it "for future validation," but the existing Peru-specific teleworkability values in Saltiel's data are directly usable for a robustness check. Given that this is Peru-specific data (Saltiel reports country-level work-from-home shares), it is a natural and easy validation exercise that should be included rather than deferred.

**6. "Permanent scarring" language.** The paper is careful in Section 4.4 to distinguish population-level differentials from individual-level scarring. The abstract and conclusion use "permanent informality scarring" and "structurally trapped in informality" without this qualification. The language should be consistent throughout: what the data show is a stable population-level differential, not demonstrated individual permanence.

**7. Age heterogeneity results.** Section 5.4 describes heterogeneity by age group (youth 15–29, prime, senior) but Table references no corresponding table; Figure 3 covers gender, region, and firm size only. The age results appear to be described but not reported. The authors should either include the age estimates in Figure 3 or add a supplementary table.

---

### Missing Literature

- Maloney (2004), "Informality Revisited," *World Development*: the foundational debate on whether informality is involuntary—directly relevant to the "trapped in informality" claim.
- Levy (2018), *Under-Rewarded Efforts*, IDB: comprehensive treatment of informality in Latin America, including the firm-level incentives created by dual social insurance systems.
- Bosch and Maloney (2010), "Comparative analysis of labor market dynamics using Markov processes," *Journal of Development Economics*: on informality transitions and persistence in developing countries.
- Adams-Prassl et al. (2020), "Inequality in the Impact of the Coronavirus Shock," *Economic Policy*: the key cross-country COVID-inequality paper using a task-based index structurally similar to this design.
- Loayza and Rigolini (2011), "Informal Employment: Safety Net or Growth Engine?" *World Development*: on informality as buffer during aggregate shocks, relevant to interpreting the crisis response.
- Engbom et al. (2021) or Dix-Carneiro and Kovak (2017) on persistence of location- and sector-specific shocks as a theoretical underpinning for the scarring mechanism.
- Peru-specific COVID labor market literature (INEI, ILO Peru, BCRP): the paper cites no Peru-specific labor market studies other than the ENAHO data source.

---

### Recommendation

**Major Revision**

The core research question is important, the data are appropriate, and the design is reasonable given constraints. However, the paper requires substantial revision before acceptance: the Table 2 sign inconsistency must be resolved, the available pre-2020 ENAHO waves should be incorporated for parallel-trends validation, the political instability confound must be discussed, and the Reactiva Perú omission must be addressed. These are revisions that substantially change the evidentiary basis of the causal claims, not cosmetic corrections.

---

```json
{
  "score": 68,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "contribution_novelty": 76,
    "literature_positioning": 63,
    "substantive_arguments": 62,
    "external_validity": 65,
    "journal_fit": 72
  },
  "major_comments": [
    "Table 2 sign inconsistency: interaction coefficients (TW_low) are reported as negative (−0.20 to −0.22), implying contact-intensive workers became *less* informal than teleworkable workers — the opposite of the abstract's 9 pp claim. Authors must reconcile whether Table 2 reports the continuous specification (with a labeling error) or a coding error in the binary dummy.",
    "Pre-2020 ENAHO waves exist (2017–2019) and are publicly available from INEI. Omitting them precludes the standard parallel-trends test. Including them converts an untestable assumption into a testable one, which is the paper's most straightforward improvement.",
    "Peru's political instability (Castillo election 2021, impeachment December 2022, Boluarte protests 2022–2023) represents an independent shock correlated with contact-intensive sectors (transport, mining, agriculture). The zero-attenuation Wald test (p = 0.994) cannot distinguish COVID scarring from a continued policy-regime shock. This confound must be discussed and, if possible, decomposed.",
    "Reactiva Perú (S/ 60bn credit guarantees requiring payroll maintenance by formal firms) is entirely absent from the paper. This program created a formal–informal wedge that is mechanically correlated with the teleworkability treatment. Its omission from the identification discussion is a significant oversight.",
    "Extreme survey weight ratio (3,394:1 max/median) raises concerns about whether winsorization at 1st/99th percentiles is adequate. Authors should report effective sample size, verify leverage diagnostics, and confirm that the main result is not driven by a handful of extreme-weight observations.",
    "With 43 clusters, standard CRVE inference is unreliable (Cameron-Miller 2015 recommend ≥50). Wild cluster bootstrap with Rademacher weights and 999 replications should replace HC1 as the primary inference method."
  ],
  "minor_comments": [
    "Monthly income figures (15,440 soles for contact-intensive, 25,408 for teleworkable) are implausible relative to Peru's median wage of ~1,000–1,500 soles. Authors should clarify whether these are annual figures, conditional on wage workers only, or affected by un-winsorized weights.",
    "The 0.20 teleworkability threshold is arbitrary; sensitivity analysis at 0.15, 0.25, and 0.30 should be reported since the binary specification drives the headline 9 pp result.",
    "The 'bosch2025' citation lacks full provenance; if it is a working paper, the repository/institution should be cited.",
    "The near-zero coefficient on the contract-based informality measure (0.002) likely reflects Peru-specific employer noncompliance behavior (failing to register with EsSalud while maintaining written contracts); this institutional interpretation deserves a paragraph, not a parenthetical.",
    "Saltiel (2020) provides Peru-specific work-from-home shares and should be implemented as a crosswalk robustness check rather than deferred to future work.",
    "Age heterogeneity results (youth 15–29, prime, senior) are described in Section 5.4 but appear absent from Figure 3 and tables; either include or remove the description.",
    "The terms 'permanent scarring' and 'structurally trapped' in the abstract and conclusion should be qualified consistently with the paper's own caveat that ENAHO's rotating panel identifies population-level differentials, not individual-level permanence."
  ],
  "missing_literature": [
    "Maloney (2004), 'Informality Revisited,' World Development — foundational paper on whether informality is involuntary; directly relevant to the scarring-as-trap claim.",
    "Levy (2018), Under-Rewarded Efforts, IDB — comprehensive treatment of dual social insurance and informality incentives in Latin America.",
    "Bosch and Maloney (2010), 'Comparative analysis of labor market dynamics using Markov processes,' Journal of Development Economics — on informality transition persistence.",
    "Adams-Prassl et al. (2020), 'Inequality in the Impact of the Coronavirus Shock,' Economic Policy — key cross-country COVID task-based analysis structurally similar to this design.",
    "Loayza and Rigolini (2011), 'Informal Employment: Safety Net or Growth Engine?' World Development — on informality as aggregate-shock buffer.",
    "Dix-Carneiro and Kovak (2017), 'Trade Liberalization and Regional Dynamics,' American Economic Review — model of permanent regional labor market effects of sector shocks; provides theoretical grounding for scarring.",
    "Peru-specific COVID labor market studies from INEI, ILO Peru country office, or BCRP — the paper currently cites no Peru-specific empirical labor market literature."
  ]
}
```