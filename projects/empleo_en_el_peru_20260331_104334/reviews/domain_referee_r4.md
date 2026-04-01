## Referee Report — Round 4

**Journal:** [Development Economics / Labor Economics field journal]
**Paper:** "COVID-19 and the Formality Recovery Path in Peru: A Worker-Level Panel DiD Using Sectoral Teleworkability"
**Round:** 4 (evaluation of revised manuscript)

---

### Summary

This paper uses five waves of the ENAHO employment panel (2020–2024) and the Dingel-Neiman (2020) teleworkability index to estimate whether contact-intensive workers in Peru experienced a permanent increase in informality relative to teleworkable workers following COVID-19. The DiD design interacts year dummies with occupational teleworkability, and the main findings are interpreted as evidence of permanent informality scarring. The revised manuscript partially addresses earlier concerns but leaves several Round 3 "must address" requirements unresolved, and introduces a new, fundamental inconsistency between claimed evidence and statistical significance.

---

### Main Assessment

The revision has made targeted improvements: the SE methodology is now consistently described as clustered throughout, the Wald test p-value is internally consistent (0.937 in both abstract and body), and the attrition analysis is transparent. However, five of the seven Round 3 "must address" items remain unresolved. More critically, the headline result is now explicitly reported with p = 0.153—well above any conventional significance threshold—while the abstract and conclusion continue to assert "causal evidence that COVID-19 produced permanent informality scarring." This contradiction between the reported evidence and the causal language is the most urgent issue requiring correction.

---

### Major Comments

**1. Statistically insignificant headline result paired with causal language (unresolved, now more severe)**

The abstract states the 9 pp effect with "p = 0.153" and the conclusion states "This paper provides causal evidence that COVID-19 produced permanent informality scarring." A p-value of 0.153 is not statistically significant at the 10% level, let alone the 5% or 1% levels conventionally required to assert causal evidence. The appropriate language for a p = 0.153 result is "suggestive" or "imprecisely estimated." The authors must either (a) implement wild cluster bootstrap and report whether the result meets significance thresholds under that method, (b) substantially moderate all causal language to reflect the uncertainty, or (c) front the continuous specification (which yields * significance) as the primary result and relegate the binary to robustness. As drafted, the abstract reports a statistically insignificant effect but labels it causal evidence in the conclusion—these cannot simultaneously be correct.

**2. Wild cluster bootstrap still absent (Round 1 requirement, unresolved through Round 4)**

With 43 ISCO-08 clusters—below the Cameron and Miller (2015) threshold of ~50—conventional cluster-robust standard errors have known finite-sample over-rejection bias. Wild cluster bootstrap with Rademacher weights (≥999 replications) was required in Round 1 and remains unimplemented. Given that the headline coefficient is already insignificant at p = 0.153 under conventional clustering, WCB inference could only widen confidence intervals further. This is not a pro forma concern: it directly bears on whether any significance claim in this paper survives proper inference.

**3. Table 2 specification inconsistency (persists)**

Section 4.2 designates the continuous teleworkability score as the primary specification ("Our primary specification uses the continuous teleworkability score...avoiding the arbitrary binary classification"). Section 5 explicitly states "Table 2 presents the main results using the continuous teleworkability specification." Yet Table 2's interaction column is labeled "Interaction (TW$_\text{low}$)" and the table notes state "differential effect for contact-intensive workers (teleworkability < 0.20)"—the binary specification. The authors cannot simultaneously describe Table 2 as showing the continuous specification while labeling it with the binary indicator. The 9 pp figure in the abstract also corresponds to the binary specification but is attributed a p = 0.153, whereas Table 2's binary interaction for 2021 shows a * (p < 0.10). These are inconsistent. The authors must (a) label Table 2 correctly as the binary specification and present a separate table for the continuous specification, or (b) promote the continuous specification to Table 2 and present the binary as a robustness table, with full consistency across abstract, body, tables, and notes.

**4. Reactiva Perú confound: still unaddressed (Round 3 "must address")**

The paper does not mention Reactiva Perú, Peru's S/. 60 billion FAE-MYPE/Reactiva Perú credit guarantee program (2020–2021) that provided liquidity conditional on maintaining payroll. Firms in teleworkable sectors were disproportionately able to operate during lockdowns, maintain payroll, and access these guarantees—creating a plausible alternative mechanism for the observed formality differential that is independent of teleworkability per se. If teleworkable-sector firms retained workers on payroll to access credit guarantees, the measured formality gap would reflect a fiscal transfer channel, not a structural scarring mechanism. This confound is institutionally important and must be discussed in the identification section.

**5. Implausible income figures: still unexplained (Round 3 "must address")**

Table 1 reports mean monthly incomes of S/. 15,440 (contact-intensive) and S/. 25,408 (teleworkable). ENAHO aggregate statistics place mean monthly labor income in Peru at approximately S/. 1,500–1,800 during this period—making these figures 8–14× the national average. The evidence packet confirms these values appear in the actual output. No table note, section footnote, or data appendix provides any explanation (units conversion, sample restriction to high earners, or coding check). Until clarified, a reader cannot determine whether these figures reflect a data processing error in the pipeline affecting the entire analysis, or an unusual sample restriction. This must be explained.

**6. No pre-pandemic parallel trends validation (Round 1 requirement, unresolved)**

The paper now honestly acknowledges this limitation ("We cannot test parallel trends in the pre-period") and notes it as future research. However, the compositional imbalance between treatment groups—32 pp rurality gap and 19 pp gender gap (Table 1)—makes the parallel trends assumption structurally implausible without empirical validation. ENAHO 2017–2019 microdata is publicly available from INEI. Incorporating two pre-pandemic waves would directly address this concern and is feasible within a revision cycle. The honest acknowledgment in Section 6.4 is necessary but insufficient given how central this assumption is to all claims in the paper.

---

### Minor Comments

1. **Attrition rates and inference scope mismatch.** Section 6.3 reports 78.7% attrition by 2021 and 96.9% by 2024. The non-differential attrition result (p = 0.163 for teleworkability predicting attrition) is informative but does not imply the retained sample is representative. With only ~3% of the original cohort observed in 2024, any within-individual inference about scarring is implausible—the paper appropriately disclaims this in Section 4.4, but the introduction and abstract should more prominently flag that the "permanence" claim is a population cross-sectional finding, not individual tracking.

2. **Heterogeneous effects reported without numbers.** Section 5.4 discusses heterogeneity by gender, region, and firm size but provides only verbal placeholders ("the gender-specific interaction coefficients reveal whether the scarring burden fell disproportionately on one gender"). Figure 3 is cited but no numerical results are reported. Either tabulate these estimates or remove this subsection.

3. **Balanced panel results absent.** Section 6.2 states the balanced sub-panel (N = 1,154) is "extremely small" and cautions against relying on it—but provides no coefficients from this sub-panel. If the balanced panel is too small to be informative, the subsection should be omitted rather than retained as an empty placeholder.

4. **Abstract p-value for binary 2021 effect.** The abstract reports p = 0.153 for the 9 pp effect. If this comes from the binary specification, it conflicts with the * (p < 0.10) shown in Table 2 for the 2021 binary interaction. The authors must reconcile this arithmetic discrepancy or identify which table and specification corresponds to p = 0.153.

5. **"Causal evidence" framing throughout.** Given (a) no pre-trend test, (b) a statistically insignificant headline coefficient, and (c) an unaddressed fiscal confound, the repeated use of "causal evidence" and "causal interpretation" in the abstract, introduction, and conclusion overstates what this design can establish. The appropriate framing is "consistent with" or "suggestive of."

---

### Missing Literature

- **Campos and Ohnsorge (2020)** and **Ohnsorge and Yu (2021)**: World Bank multi-country analyses of COVID-19 and informality in emerging markets; directly relevant to the external validity discussion.
- **Contreras, Glave, and Yamada (2020)**: Peru-specific analysis of COVID-19 labor market impacts that likely documents the immediate formality shock the authors build upon.
- **Fairlie et al. (2020)**: U.S. context for occupation-based COVID exposure and employment; the comparison strengthens the teleworkability framing.
- **Neidhöfer, Serrano, and Gasparini (2018)** on intergenerational mobility and informality traps in Latin America—relevant to the scarring mechanism discussion.
- Any empirical work on **Reactiva Perú's** labor market effects is essential given the confound identified in Major Comment 4.

---

### Recommendation

**MAJOR REVISIONS** (third consecutive major revision request)

The paper addresses a genuinely important question with an appropriate dataset. However, across four rounds, the following requirements remain unresolved: (1) wild cluster bootstrap inference, (2) pre-pandemic parallel trends validation, (3) Reactiva Perú confound, and (4) implausible income figures. A fifth issue—the disconnect between p = 0.153 and causal language—has worsened relative to prior rounds rather than improved. The editor should consider whether a further major revision round is warranted or whether the paper should be redirected to a venue with a working paper standard. Acceptance conditional on the items listed above being addressed in a timely revision is the recommended path if the editor judges the contribution sufficient.

---

```json
{
  "score": 52,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "contribution_novelty": 62,
    "literature_positioning": 52,
    "substantive_arguments": 44,
    "external_validity": 53,
    "journal_fit": 50
  },
  "major_comments": [
    "Statistically insignificant headline result (p=0.153) paired with repeated 'causal evidence' language in abstract and conclusion — these are logically incompatible; all causal claims must be moderated to match the evidential standard actually achieved.",
    "Wild cluster bootstrap with Rademacher weights still absent after four rounds; with 43 clusters below the Cameron-Miller threshold, conventional clustered SEs have known over-rejection bias and WCB remains the required primary inference method.",
    "Table 2 specification inconsistency: Section 4 and Section 5 both assert Table 2 displays the continuous teleworkability specification, but the interaction column is labeled TW_low with notes describing the binary cutoff — the continuous and binary results are conflated across the text, table, and abstract.",
    "Reactiva Perú (S/. 60 bn FAE-MYPE/Reactiva Perú program, 2020–2021) remains unaddressed despite being a Round 3 must-address item; payroll-conditioned credit access by teleworkable-sector firms constitutes a plausible alternative channel for the observed formality differential.",
    "Monthly income figures of S/. 15,440 and S/. 25,408 in Table 1 remain 8–14x Peru's national average with no clarifying note; the evidence packet confirms these values appear in the actual pipeline output, and without explanation they undermine confidence in the data processing.",
    "No pre-pandemic parallel trends test despite ENAHO 2017–2019 data being publicly available from INEI; the 32 pp rurality and 19 pp gender compositional gaps between treatment groups make parallel trends structurally implausible without empirical validation."
  ],
  "minor_comments": [
    "Attrition of 96.9% by 2024 means the 'permanence' finding rests almost entirely on cross-sectional population comparisons, not within-individual tracking; this distinction should be stated prominently in the abstract, not only in Section 4.4.",
    "Section 5.4 heterogeneous effects contains only verbal placeholders with no numerical results; tabulate the estimates or remove the subsection.",
    "Section 6.2 balanced panel analysis contains no coefficients and acknowledges the sub-sample is too small to be informative — this subsection should be removed or replaced with actual estimates.",
    "Abstract p=0.153 for the 9 pp binary effect conflicts arithmetically with the * (p<0.10) shown for the 2021 binary interaction in Table 2; one of these must be wrong.",
    "The Wald test for scarring (p=0.937) correctly tests coefficient stability, but stability of an imprecisely estimated coefficient does not constitute evidence of scarring — this distinction should be stated clearly when the test result is interpreted."
  ],
  "missing_literature": [
    "Ohnsorge and Yu (2021), World Bank research on COVID-19 and informality in emerging markets — directly relevant to external validity framing.",
    "Peru-specific COVID-19 labor impact studies (Contreras, Glave, Yamada 2020 or equivalent) that document the immediate formality shock this paper builds upon.",
    "Empirical work evaluating Reactiva Perú's labor market effects — essential given the unaddressed confound in the identification strategy.",
    "Neidhöfer, Serrano, and Gasparini (2018) on informality traps and intergenerational mobility in Latin America — relevant to the scarring mechanism."
  ]
}
```