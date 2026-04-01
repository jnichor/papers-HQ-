## Referee Report

**Journal of Development Economics / Review of Economics and Statistics**

**Manuscript:** "COVID-19 and the Formality Recovery Path in Peru: A Worker-Level Panel DiD Using Sectoral Teleworkability"

---

### Summary

This paper estimates the causal effect of COVID-19 on labor informality in Peru using a difference-in-differences design that exploits differential occupational exposure via the Dingel-Neiman (2020) teleworkability index. Using five ENAHO waves (2020–2024), the authors find that contact-intensive workers experienced a roughly 9 percentage point increase in informality relative to teleworkable workers, a gap that persisted unchanged through 2024, which they interpret as evidence of permanent labor market scarring. The primary informality measure is absence of employer-provided social security; robustness checks using written contract and firm-size measures are included.

---

### Main Assessment

The paper addresses a genuinely important question for development economics: whether the occupational disruption from a severe aggregate shock produces permanent state-dependence in informality, or whether formality recovers as the shock dissipates. The setting (Peru, with >70% informality and an exceptionally strict lockdown) is well-chosen, the identification strategy is conceptually clean, and the four-year follow-up window is a genuine empirical contribution. The finding that the scarring channel operates through social security loss rather than firm-size transitions is substantively interesting and has direct policy implications.

However, the paper has several significant weaknesses that must be addressed before publication. The most serious is the failure to cluster standard errors at the treatment-assignment unit. The treatment variable is constant within ISCO-08 2-digit occupation groups, yet the paper reports only HC1 heteroskedasticity-robust SEs rather than cluster-robust SEs at the occupation (or occupation × region) level; this almost certainly overstates precision. Second, the "scarring" framing is econometrically stronger than the evidence warrants: the rotating panel design means most cross-year variation is cross-cohort rather than within-individual, the Wald test is silent on aggregate confounds, and the within-estimator actually shows modest attenuation (0.103 → 0.081) that the authors do not adequately reconcile with the scarring thesis. Third, the extremely unbalanced treatment/control split (75.7% treated) combined with large baseline differences in rural status, gender, and income raises questions about whether parallel trends is a credible assumption that the paper does not fully engage with.

---

### Major Comments

**1. Standard error clustering is misspecified (critical).** The teleworkability treatment is assigned at the 2-digit ISCO-08 occupation level: every worker in a given sub-major group receives the identical treatment value. This creates within-occupation error correlation that HC1 does not correct. The strategy memo explicitly specifies sector × region clustering, but the paper reports HC1 throughout. With only ~43 ISCO-08 sub-major groups, standard two-way cluster-robust inference may face few-cluster problems, but the paper must at minimum cluster at the occupation level and report results with occupation × region clustering as in the strategy memo. The current SE estimates—which are the basis for the paper's central $p < 0.001$ claims—should be treated as unreliable until this is resolved. The authors should report both specifications side by side in Table 2 and discuss whether significance survives.

**2. The "scarring" interpretation exceeds what the evidence can establish.** The paper uses "scarring" to describe group-level persistence of a DiD gap, but scarring in the literature (Arulampalam 2001, Cruces & Calvo 2012) refers to persistent *within-individual* effects on employment quality. Three sub-issues compound this:

- *Cross-cohort composition:* ENAHO's rotating design means most individuals are observed for only two consecutive years; the 2021-vs-2024 comparison is largely a comparison of different cohorts. The paper should clearly distinguish between "within-individual scarring" and "persistent cohort-level informality gap," and the scarring framing should be moderated accordingly.
- *Within-estimator attenuation:* Section 5.3 reports FE coefficients declining from 0.103 (2021) to 0.081 (2024). For individuals actually observed over time, this is partial within-individual recovery. This directly contradicts permanent scarring at the individual level but is buried in a few lines with no reconciliation.
- *The Wald test is necessary but not sufficient:* Failing to reject $\gamma_{2024} = \gamma_{2021}$ shows the DiD gap did not narrow relative to the 2021-level (itself potentially attenuated by the contaminated 2020 baseline). It does not rule out that the gap reflects ongoing differential occupation-level exposures (e.g., continued informalization pressure in contact-intensive sectors for structural reasons unrelated to pandemic scarring).

**3. No pre-pandemic parallel trends test and inadequate treatment of 2020 baseline contamination.** The paper acknowledges both problems but does not adequately address their joint severity. With 2020 as the baseline year and fieldwork spanning the pre- and post-lockdown period, the DiD coefficients estimate the shock relative to an already-partially-treated baseline. This produces coefficient attenuation in a direction that is hard to sign, and the magnitude of the 9 pp estimate should be interpreted with this caveat placed prominently in the results section rather than in limitations. The authors should: (i) examine whether ENAHO 2020 fieldwork metadata (quarter of interview) permits construction of a clean pre-lockdown subsample as a baseline robustness check; and (ii) provide a detailed argument—not just an assertion—for why parallel pre-trends are plausible given the large observable differences between the treatment and control groups.

**4. Extreme survey weights must be addressed in robustness checks.** The data audit flags a max/median weight ratio of 3,394×. This is extreme. WLS estimation with such outlier weights can cause the estimates to be dominated by a small number of observations. The paper does not mention this anywhere in the text. A robustness check trimming or winsorizing weights at the 99th percentile should be added to Section 6, and the direction and magnitude of any change should be reported.

**5. Binary treatment with 75.7% treated creates overlap and parallel-trends concerns.** The contact-intensive group (score < 0.20) constitutes 75.7% of the sample, while the "teleworkable" comparison is 24.3% and differs substantially on key covariates: 61% female vs. 42%, 12% rural vs. 44% rural, income gap of ~65%. These are not minor imbalances—they reflect fundamentally different labor market segments. The paper should present the continuous teleworkability score as the primary treatment variable (as specified in the strategy memo) and treat the binary indicator as a secondary specification. The continuous specification is both more statistically efficient and less vulnerable to the comparison-group representativeness critique.

---

### Minor Comments

1. **Implausible income figures in Table 1.** Monthly income is reported as 15,440 soles for contact-intensive and 25,408 soles for teleworkable workers. Peru's median monthly labor income is approximately 1,200–1,800 soles; 15,440 soles/month would imply ~$4,000 USD/month, far above average. Please clarify the unit (monthly vs. annual? current soles vs. deflated?), note that ~40–60% of the sample has missing income data (likely explaining the upward bias), and verify these figures against published INEI wage statistics.

2. **Heterogeneity section is uninformative as written.** Section 5.4 describes what the figures "reveal" and "test" without reporting a single coefficient. The reader cannot evaluate these claims. Add a table with interaction coefficients and SEs for each subgroup, or at minimum report the key numbers in text.

3. **FE attenuation is inconsistently handled.** The within-estimator shows a decline from 0.103 to 0.081 but the paper attributes this to "compositional changes in the rotating panel or genuine within-individual partial recovery." This ambiguity is unsatisfying; the authors should be more precise about which interpretation is consistent with the attrition analysis results.

4. **The Saltiel (2020) adaptation should be implemented, not deferred.** The paper explicitly acknowledges that the D&N index was built on U.S. task content and may misclassify Peruvian occupations. Saltiel (2020) provides a direct remedy for exactly this setting. Recommending it for "future research" while using the potentially mis-measured instrument in the main analysis weakens the paper. This validation should be in Section 6, not the conclusion.

5. **Policy recommendation exceeds evidence.** The conclusion advocates for "portable social protection mechanisms, decoupled from the employer relationship" as more effective than traditional formalization strategies. This recommendation does not follow from the findings, which identify a scarring effect but provide no evidence on counterfactual interventions. This should be clearly flagged as speculative policy extrapolation.

6. **"Scarring" terminology throughout.** Given the evidence is group-level, not individual-level, the abstract, title, and conclusion should use more precise language: "persistent informality gap" or "permanent formality shock" better describes what the DiD estimates.

7. **Bosch (2025) citation context.** The paper cites Bosch (2025) for worker-side informality dynamics but that paper studies firm-level compliance via enforcement letters. The connection to this paper's findings should be made more explicit, particularly since the two papers point to different mechanisms (firm vs. worker side).

8. **Year effects indicate aggregate confounds.** Table 2 shows year effects of 0.064–0.077 for teleworkable workers—substantial informalization even among the "control" group. The paper does not discuss what drove this. Peru experienced severe political instability (2021–2023 presidential crises, Pedro Castillo impeachment) and economic deterioration that could plausibly affect all workers. This context should be acknowledged as a potential violation of the "no interference" assumption.

---

### Missing Literature

1. **Adams-Prassl, Boneva, Golin & Rauh (2020)**, "Inequality in the impact of the coronavirus shock: Evidence from real time surveys," *Economic Journal*. This is the canonical paper using teleworkability to measure COVID-19 occupational exposure inequality and should be in the literature review.

2. **Loayza & Rigolini (2011)**, "Informal employment: Safety net or growth engine?" *World Development*. Essential for contextualizing the informal sector as a cyclical absorber—the framing affects how to interpret a persistent DiD gap.

3. **Dix-Carneiro (2014) / Dix-Carneiro & Kovak (2017)** on trade shocks and formal-informal sector transitions in Brazil. The closest methodological antecedent for long-run labor market adjustment following an aggregate shock in a high-informality Latin American economy.

4. **Mongey, Pilossoph & Weinberg (2021)**, "Which workers bear the burden of social distancing policies?" *Journal of Economic Inequality*. Provides developed-country benchmarks for teleworkability-based heterogeneity analysis.

5. **ILO Panorama Laboral** annual reports on Latin American labor markets and COVID-19 impacts. Necessary institutional context, especially for establishing that Peru's lockdown was among the strictest in the region.

6. **Maloney (2004)**, "Informality Revisited," *World Development*. The voluntary vs. involuntary informality debate is directly relevant to interpreting whether displaced workers returned to formal employment willingly or involuntarily remained informal.

7. **Egger, Hambel, Haushofer, Jessoe, Rao & Shapiro (2022)** or equivalent systematic evidence on COVID-19 economic impacts in low/middle-income countries for positioning relative to the broader developing-country COVID literature.

---

### Recommendation

**Major Revision**

The core research question is valuable and the setting is appropriate, but the paper requires substantive revisions on econometric specification (clustering), causal interpretation (scarring vs. compositional vs. aggregate effects), and engagement with the informality literature before it is ready for publication.

---

```json
{
  "score": 72,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "contribution_novelty": 78,
    "literature_positioning": 66,
    "substantive_arguments": 68,
    "external_validity": 68,
    "journal_fit": 75
  },
  "major_comments": [
    "Standard errors are misspecified: treatment is assigned at the 2-digit ISCO-08 level, creating within-occupation error correlation. HC1 SEs (not cluster-robust) overstate precision. Errors must be clustered at occupation × region level as specified in the strategy memo; statistical significance of p<0.001 claims should be re-verified.",
    "The 'scarring' interpretation exceeds what the evidence establishes. The rotating panel forces most cross-year comparisons to be cross-cohort, not within-individual. The within-estimator shows attenuation from 0.103 to 0.081 (partial within-individual recovery) that directly contradicts permanent scarring and is not reconciled in the text. The Wald test is necessary but not sufficient—it is silent on aggregate confounds and the contaminated 2020 baseline.",
    "The 2020 baseline is partially treated (fieldwork spans pre/post lockdown) and no pre-pandemic parallel trends test is possible. The authors must provide a more substantive defense of the parallel trends assumption, given large observable differences between treatment and control groups (44% vs. 12% rural; 42% vs. 61% female), or use within-2020 fieldwork timing to construct a cleaner pre-period baseline.",
    "Extreme survey weights (max/median = 3,394×) are flagged in the data audit but not addressed anywhere in the paper. WLS estimates dominated by extreme-weight observations can be unreliable; winsorized-weight robustness checks are required.",
    "Binary treatment with 75.7% of workers classified as 'treated' leaves only 24.3% as comparison, with large baseline imbalances. The continuous teleworkability score should be the primary specification; the binary indicator should be secondary. The current design risks violating overlap assumptions."
  ],
  "minor_comments": [
    "Monthly income figures in Table 1 (15,440 and 25,408 soles/month) appear implausibly high relative to Peru's median wages (~1,200–1,800 soles/month). Clarify units, note ~40–60% missing income data, and verify against INEI wage statistics.",
    "Section 5.4 (Heterogeneity) reports no numerical results—only descriptions of what the figures 'reveal.' Add a supplementary table with interaction coefficients and SEs for all subgroups.",
    "The Saltiel (2020) developing-country teleworkability adaptation should be implemented as a robustness check in Section 6, not deferred to future research, given the acknowledged limitation that D&N was constructed for U.S. occupations.",
    "The policy recommendation for 'portable social protection mechanisms' is speculative extrapolation from the findings and should be flagged explicitly as such; the paper provides no evidence on the effectiveness of this specific intervention.",
    "Table 2 year effects (0.064–0.077) show substantial informalization among teleworkable (control) workers throughout 2021–2024. Peru's severe political instability and economic deterioration during this period should be acknowledged as potential aggregate confounds not absorbed by the DiD design.",
    "The term 'scarring' throughout the abstract, title, and conclusion should be replaced with 'persistent informality gap' or 'permanent formality shock' to more accurately describe what group-level DiD estimates identify.",
    "The Bosch (2025) citation is for firm-level compliance with enforcement letters, not worker-side informality transitions. The connection to this paper's findings should be made explicit or the citation reconsidered."
  ],
  "missing_literature": [
    "Adams-Prassl, Boneva, Golin & Rauh (2020), 'Inequality in the impact of the coronavirus shock,' Economic Journal — canonical teleworkability-based COVID impact paper, conspicuously absent.",
    "Loayza & Rigolini (2011), 'Informal employment: Safety net or growth engine?' World Development — essential for framing whether informality is a cyclical absorber or trap.",
    "Dix-Carneiro (2014) / Dix-Carneiro & Kovak (2017) on trade shocks and formal-informal transitions in Brazil — closest methodological antecedent for long-run adjustment after aggregate shock in high-informality Latin America.",
    "Mongey, Pilossoph & Weinberg (2021), 'Which workers bear the burden of social distancing policies?' Journal of Economic Inequality — developed-country benchmark for teleworkability heterogeneity.",
    "Maloney (2004), 'Informality Revisited,' World Development — voluntary vs. involuntary informality framing directly relevant to interpreting the persistence of the informality gap.",
    "ILO Panorama Laboral and/or CEPAL COVID-19 labor market analyses — needed for institutional context establishing Peru's lockdown severity relative to regional peers."
  ]
}
```