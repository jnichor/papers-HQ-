## Referee Report — Round 5

**Journal:** Empirical Economics (Third-party methodology review)
**Manuscript:** "COVID-19 and the Formality Recovery Path in Peru: A Worker-Level Panel DiD Using Sectoral Teleworkability"
**Review Round:** 5 (following Round 4 major revision)

---

### Summary of Methodology

The paper estimates differential COVID-19 effects on Peruvian labor informality using a DiD that exploits the Dingel-Neiman teleworkability index as pre-determined, continuous treatment intensity across five ENAHO panel waves (2020–2024, N = 262,733). The continuous specification yields 19–22 pp smaller informality increases for highly teleworkable occupations (significant at 5–10%), while the binary specification yields an insignificant 9 pp differential. The revision addressed some prior concerns—Table 2 structure, heterogeneity reporting, and abstract transparency—but three of seven must-address items from Round 4 remain unresolved.

---

### Progress Since Round 4

**Adequately resolved:**
- Table 2 now cleanly separates continuous and binary specifications with correct panel labels and note descriptions. *(Must-address 3: resolved.)*
- Section 5.4 now reports actual coefficients and p-values for all heterogeneity subgroups. *(Must-address 7: resolved.)*
- Abstract correctly identifies p = 0.153 insignificance for the binary specification. *(Should-address 1: resolved.)*
- Table 1 footnote provides income variable construction details and the median (S/.14,495). *(Must-address 5: partially resolved; see Major Concern 4 below.)*

**Inadequately resolved or unaddressed:** Must-address items 2, 4, and 6 remain open, along with the partial resolution on items 1 and 5. These constitute the basis for the continued major revision recommendation.

---

### Major Concerns

**1. Wild cluster bootstrap still absent — inference integrity unresolved (Must-address Item 2, unresolved)**

The paper continues to use conventional CRVE-clustered standard errors at the ISCO-08 2-digit level with 40 (or 43 — see Minor Concern 1) clusters. The Cameron-Miller threshold for reliable conventional cluster SEs is approximately 50. This is not a minor technical footnote: the headline continuous-specification results hinge on t-statistics of approximately 1.97 (2022: −0.220/0.112) and 2.00 (2024: −0.190/0.095). With t(39) critical values of ±2.023 at the 5% level, these coefficients are not significant at conventional levels under the correct reference distribution, let alone under wild bootstrap. The ** significance stars on γ₂₀₂₂ and γ₂₀₂₄ are therefore potentially mis-assigned.

**Required action:** Implement wild cluster bootstrap (Rademacher weights, 999 replications) as the primary inference procedure. If the headline results survive, confidence in the conclusions increases substantially. If they do not survive, the framing must change. The authors must report bootstrap p-values alongside or in place of conventional clustered SEs as the primary evidence standard throughout Tables 2–3 and Section 5. This was explicitly required in Round 4 and cannot be deferred again.

---

**2. Reactiva Perú omitted as alternative channel (Must-address Item 4, unresolved)**

The paper makes no mention of Reactiva Perú (S/. 60bn, 2020–2021) or FAE-MYPE, the payroll-conditioned emergency credit programs that disbursed credit conditional on payroll maintenance to over 500,000 firms. These programs differentially benefited firms in teleworkable sectors—service, professional, and financial occupations—which are the same sectors identified as the "control" group in this paper. If credit access under Reactiva Perú allowed teleworkable-sector employers to maintain formal employment relationships during 2020–2021, the observed formality differential reflects both teleworkability per se and the additional support received by teleworkable-sector firms. This is a first-order confounder that threatens the exclusive-restriction interpretation of the DiD.

**Required action:** At minimum, the paper must acknowledge this channel in the limitations/robustness section. More robustly, the authors should test whether the formality differential is larger for firm-size bins most likely to have accessed Reactiva Perú (5–100 workers, formal-sector firms), or compare sectors with differential program take-up rates using SUNAT/SBS published disbursement data.

---

**3. Pre-pandemic parallel trends test not performed (Must-address Item 6, unresolved)**

The conclusion again defers pre-trend validation to "future research." ENAHO 2017–2019 data is publicly available from INEI and the identifying variation (ISCO-08 occupational teleworkability) is by construction available for all years. The 32 pp rurality gap and 19 pp gender gap between contact-intensive and teleworkable workers documented in Table 1 make parallel trends structurally fragile: rural workers experienced differential trends across many economic dimensions in 2017–2019 (agricultural price shocks, infrastructure investment, drought cycles) unrelated to the pandemic. Without a pre-trend test, the baseline common-trends assumption is implausible on observable grounds alone.

**Required action:** Add ENAHO 2017 and 2019 waves and estimate the pre-period event study coefficients. If pre-trends are flat, this validates the design and substantially strengthens the paper. If they are non-flat, the authors must condition on occupation-year-level trends or abandon causal language entirely. This is not a future-research suggestion; it is a necessary validity check for the identification strategy.

---

**4. Causal language persists without adequate warrant (Must-address Item 1, partially resolved)**

The abstract and body now appropriately distinguish between the significant continuous-specification results and the insignificant binary results. However, the conclusion (Section 7) states: "Three features strengthen the causal interpretation... the effect is robust to within-individual (fixed effects) estimation, confirming that the result is not driven by compositional changes in the workforce." This overstates what fixed effects can establish. With ENAHO's rotating design (most individuals observed for only two consecutive years), the "individual FE" estimator absorbs time-invariant heterogeneity within short spells only; it does not address time-varying confounders, Reactiva Perú exposure, or the absence of pre-trend validation. Pre-determined treatment and non-differential attrition are necessary but not sufficient for causal identification.

**Required action:** Revise the conclusion to replace "causal interpretation" with "interpretive consistency with a causal mechanism, subject to the limitations documented in Section 6." Enumerate specifically what the three cited features do and do not establish.

---

**5. Income variable unit ambiguity not fully resolved (Must-address Item 5, partially resolved)**

The Table 1 footnote now states that i524a1 captures "total gross labor income from all jobs, including overtime, bonuses, and in-kind payments, before taxes" with a median of S/.14,495. This note does not resolve whether S/.14,495/month or S/.14,495/year. If monthly, the median formal-sector worker in this sample earns S/.173,940 per year — approximately 12× Peru's median household income, which is implausible. If annual, the median of S/.14,495/year corresponds to ~S/.1,208/month, which is just above the minimum wage and economically credible. The paper labels the variable as "Monthly income" in Table 1 while simultaneously reporting a value that is only plausible as annual income.

**Required action:** Clarify explicitly whether S/.14,495 (median) and S/.15,440/S/.25,408 (group means) are monthly or annual figures. If annual, relabel the table row. If monthly and correct, provide a verifiable source confirming that mean monthly earnings in the teleworkable sample exceed S/.25,000 in this period.

---

### Minor Concerns

1. **Cluster count inconsistency.** The abstract states "40 clusters," the data section refers to "43 ISCO-08 sub-major groups," and Table 2 notes "40 clusters." The discrepancy of 3 clusters should be explained (e.g., are 3 ISCO groups merged due to thin cells?). This affects reproducibility.

2. **Within-estimator SEs not reported.** Section 5.3 reports FE interaction coefficients (−0.256 in 2021, −0.237 in 2024) and claims significance at 5% without providing standard errors, cluster levels, or a reference table. These claims cannot be evaluated by readers. A table with SE and N for the FE specification is needed.

3. **Post-hoc rationalization of insignificant heterogeneity results.** Section 5.4 interprets the female coefficient (11.4 pp, p = 0.114) as "consistent with women facing greater barriers to re-formalization" despite non-significance at conventional levels, and the insignificant Lima result as reflecting "more homogeneous labor market." These interpretations may be substantively correct, but presenting them as findings without acknowledging their inferential status — all subgroup estimates are insignificant except Lima — conflates description with inference. Authors should explicitly note that the heterogeneity analysis is exploratory and underpowered.

4. **Borderline headline significance under correct t-distribution.** Even setting aside the bootstrap issue, the two starred (**)  coefficients (γ₂₀₂₂ = −0.220, SE = 0.112; γ₂₀₂₄ = −0.190, SE = 0.095) yield t-ratios of 1.97 and 2.00, respectively. Under a t(39) reference distribution, the 5% two-tailed critical value is 2.023. These coefficients are not significant at 5% under the correct reference distribution. The ** notation is incorrect and must be revised to * (10%) or re-evaluated with bootstrap.

5. **Compositional imbalance discussion insufficient.** Table 1 shows a 32 pp rurality gap and 19 pp gender gap between treatment groups. Section 6 (robustness) notes these imbalances only in the context of attrition, not as a threat to the parallel trends assumption itself. A brief discussion of whether conditioning on rural/urban or gender-by-year interactions changes the headline results would strengthen the paper.

---

### Recommendation

**Major Revision**

The revision demonstrates meaningful improvement in presentation transparency (Table 2 structure, heterogeneity reporting, abstract clarity) and the authors' acknowledgment of limitations has strengthened. However, three of seven must-address items from Round 4 remain unresolved, including the two most critical for the paper's inferential validity: wild cluster bootstrap and the Reactiva Perú confounder. Additionally, the headline continuous-specification significance is not robust to the correct t(39) reference distribution, making the bootstrap implementation more urgent, not less. The paper cannot be accepted with conventional CRVE inference on 40 clusters when the headline t-statistics straddle the 5% boundary.

---

```json
{
  "score": 57,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "identification_strategy": 54,
    "estimation_implementation": 48,
    "statistical_inference": 46,
    "robustness_sensitivity": 55,
    "replication_readiness": 68
  },
  "sanity_checks": {
    "sign": "PASS",
    "magnitude": "PASS",
    "dynamics": "PASS",
    "consistency": "FAIL"
  },
  "major_comments": [
    "Wild cluster bootstrap (Rademacher, 999 reps) still absent with 40 clusters; headline t-statistics of 1.97 and 2.00 are below the t(39) 5% critical value of 2.023, making the ** significance notation incorrect and the inference procedure invalid as primary evidence.",
    "Reactiva Perú (S/. 60bn payroll-conditioned credit program, 2020-2021) not mentioned anywhere in the paper; teleworkable-sector firms were disproportionate beneficiaries and this constitutes a first-order alternative channel for the observed formality differential that must be addressed.",
    "Pre-pandemic parallel trends test using ENAHO 2017-2019 (publicly available from INEI) still not implemented; deferred again to 'future research' despite being explicitly required in Round 4; the 32 pp rurality and 19 pp gender gap between groups make parallel trends implausible without empirical validation.",
    "Causal language ('causal interpretation... confirmed by fixed effects') persists in the conclusion despite the absence of a pre-trend test, unaddressed Reactiva Perú channel, and inference concerns; must be revised to interpretive consistency language with explicit caveats.",
    "Income variable unit ambiguity unresolved: footnote adds context but does not state whether S/. 14,495 median is monthly or annual; if monthly, implied annual income of S/. 173,940 is 12x Peru's median household income and implausible."
  ],
  "minor_comments": [
    "Cluster count inconsistency between abstract/tables (40) and data section (43 ISCO sub-major groups); explain which is correct and how the discrepancy arises.",
    "FE within-estimator coefficients in Section 5.3 (-0.256 to -0.237) are reported with claimed 5% significance but no standard errors or reference table; a table with SEs and N is required for these to be evaluable.",
    "Heterogeneity estimates in Section 5.4 are uniformly insignificant (except Lima at p=0.001) yet are interpreted substantively; must be explicitly labelled as exploratory/underpowered rather than presented as findings.",
    "Two ** stars on gamma_2022 and gamma_2024 are mis-assigned: t-ratios of 1.97 and 2.00 fall below t(39)=2.023; correct to * (10%) pending bootstrap results.",
    "Compositional imbalance (rurality, gender) should be discussed as a parallel-trends threat in Section 4, not only in attrition analysis; a brief sensitivity test conditioning on rural-by-year interactions would help."
  ]
}
```