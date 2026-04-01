## Referee Report — Round 2
**Paper:** "COVID-19 and the Formality Recovery Path in Peru: A Worker-Level Panel DiD Using Sectoral Teleworkability"
**Round:** Second review following major-revision decision

---

### Summary of Methodology

The authors estimate the effect of COVID-19 on labor informality in Peru using a difference-in-differences design that exploits the pre-determined Dingel-Neiman (2020) teleworkability index as differential sectoral exposure. The primary specification interacts year dummies with the continuous teleworkability score in a pooled WLS regression with survey weights, using ENAHO employment panels from 2020–2024. The revised paper introduces clustered standard errors (ISCO-08 2-digit, 40 clusters) and clarifies the sign and interpretation of the continuous interaction coefficients.

---

### Main Methodological Assessment

The revision makes genuine progress on the sign/labeling confusion that plagued Round 1. The authors now correctly explain in the text that negative interaction coefficients on the teleworkability score indicate that more teleworkable workers experienced *smaller* informality increases — consistent with the headline claim that contact-intensive workers were differentially harmed. This is a meaningful clarification. The cross-definition divergence is also handled with a substantive narrative: the near-zero written-contract coefficient is reframed as indicating that the shock operated through the social-security channel rather than formal/informal contract transitions.

However, three of the four "must address" items from Round 1 remain either fully unresolved or only partially resolved, and new internal inconsistencies have been introduced in the revision process. The paper is not yet ready for acceptance.

---

### Major Concerns

**1. Pre-pandemic parallel trends test: still absent (Round 1 "must address" #4 — unresolved)**

The authors have explicitly acknowledged this limitation but have not incorporated the publicly available ENAHO waves from 2017–2019. The conclusion defers pre-trend testing to "future research." This is insufficient. The parallel-trends assumption is the load-bearing assumption of the entire identification strategy, and when pre-period data exists and is publicly available, reviewers — and ultimately readers — cannot accept an untested assumption as the foundation for a causal claim. Notably, Table 1 reveals a 32 pp rurality gap and a 19 pp gender gap between treatment and control groups, making prior trend equality substantially less credible on its face.

*Required action:* Incorporate ENAHO 2017–2019. Run the standard event-study pre-trend specification. If the pre-trends are flat, this dramatically strengthens the paper. If not, this motivates demographic controls or a reweighted estimator (e.g., entropy balancing on observables). Either outcome is publishable; the current state is not.

**2. Wild cluster bootstrap: not implemented despite below-threshold cluster count (Round 1 "must address" #2 — unresolved)**

Table 2 now correctly labels standard errors as clustered at the ISCO-08 2-digit level. However, the paper uses only 40 clusters (the abstract separately reports 43 — see inconsistency note below), well below the Cameron and Miller (2015) threshold of approximately 50. With fewer than 50 clusters, conventional cluster-robust variance estimators have non-trivial finite-sample bias toward over-rejection. The Round 1 decision explicitly required wild cluster bootstrap (WCB) with Rademacher weights (≥999 replications) as the primary inference method. This has not been done. It is possible that the WCB would widen confidence intervals enough to move some of the 5%- and 10%-significant coefficients to conventional insignificance — which would affect claims about the persistence of the effect in 2021 and 2023.

*Required action:* Implement WCB as the primary inference method for all regression tables. Report p-values from the bootstrap alongside conventional clustered SEs.

**3. Section 3 still states HC1 standard errors, contradicting Table 2 and Section 4**

Section 3 (Data, §3.5) reads: "Standard errors are heteroskedasticity-robust (HC1)." Table 2 and Section 4 now correctly state cluster-robust SEs. This internal contradiction makes it impossible for readers to know which standard errors are actually used. It also raises the concern that some tables or sub-specifications still use HC1 while others use clustered SEs, with the discrepancy concealed by inconsistent documentation.

*Required action:* Purge all HC1 references. Confirm that cluster-robust SEs (or WCB, once implemented) are used uniformly across all specifications.

**4. Abstract and text contain irreconcilable numerical inconsistencies**

The following discrepancies are present in the revised paper and undermine basic credibility:

- **Cluster count:** The abstract states "43 clusters"; Table 2 states "40 clusters." These cannot both be correct.
- **Wald test p-value:** The abstract reports "$p = 0.994$" for the scarring test; Section 5 reports "$p = 0.937$." These differ non-trivially and cannot both be correct.
- **Abstract significance claim:** The abstract states the 9 pp effect is at "$p < 0.001$." Table 2 (the primary specification, continuous TW) shows significance only at the 5% level in 2022 and 2024, and 10% in 2021 and 2023. The $p < 0.001$ figure likely derives from some other specification (possibly a pooled regression, not the event study) that is not tabulated.
- **The 9 pp headline is not derived from Table 2.** Table 2 is the continuous specification (coefficient ≈ −0.20). The 9 pp figure appears to come from the binary treatment specification, which is now labeled as a "robustness check." The within-estimator in Section 5.3 gives 0.103 (10.3 pp), not 9 pp. The paper must either (a) make the binary specification the main result and relegate the continuous to robustness, or (b) show explicitly how −0.20 × Δ(TW) ≈ 0.09 for the treated-vs-control gap, rounding and weighting considered.

*Required action:* Audit all numbers for consistency across abstract, body, and tables before resubmission. Provide a clear derivation of the 9 pp headline from the reported specification.

---

### Minor Concerns

**1. Reactiva Perú remains unmentioned**

The "should address" item from Round 1 — the S/ 60 bn Reactiva Perú credit guarantee program conditioned on payroll maintenance by formal firms — is absent from the revised paper. Because formal firms disproportionately employ teleworkable workers, this program creates a confound that could inflate the estimated teleworkability–formality differential. A paragraph in the identification discussion acknowledging this and a simple robustness check (e.g., excluding sectors with high Reactiva uptake) would substantially strengthen the paper's claim to a causal interpretation.

**2. Event-study profiles for alternative informality definitions not shown**

Section 6 discusses the cross-definition divergence narratively, which is an improvement. However, the Round 1 requirement was to "present full event-study profiles for all three definitions." A three-panel figure showing year-by-year interaction coefficients for social security, written contract, and firm-size measures simultaneously would allow readers to assess whether the near-zero contract estimate is consistent across all years or reflects cancellation of positive and negative year-specific effects.

**3. Heterogeneity results are qualitative, not quantitative**

Section 5 describes the gender, region, firm-size, and age heterogeneity results only qualitatively ("the magnitudes and dynamics differ by subgroup"). Figure 3 is referenced but no tabulated coefficients appear. Referee assessment of these claims is impossible without point estimates and standard errors.

**4. Saltiel (2020) adaptation not implemented**

The paper recommends this for "future validation" but does not perform it. Given that the entire identification strategy rests on the crosswalk from U.S. task descriptions to Peruvian occupations, a sensitivity check using the Saltiel developing-country scores — even for a subset of occupations — should be achievable within the current dataset.

---

### Recommendation: **Major Revision**

The revision demonstrates that the authors understand the main methodological concerns and have made good-faith progress on sign clarification and cross-definition interpretation. These are genuine contributions. However, the three issues that most directly threaten the credibility of the causal claim — the absence of pre-trend testing, the failure to implement wild cluster bootstrap, and pervasive internal numerical inconsistencies — were all flagged as mandatory in Round 1 and remain unaddressed. The paper cannot be accepted until these are resolved.

---

```json
{
  "score": 58,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "identification_strategy": 55,
    "estimation_implementation": 57,
    "statistical_inference": 54,
    "robustness_sensitivity": 62,
    "replication_readiness": 52
  },
  "sanity_checks": {
    "sign": "PASS",
    "magnitude": "PASS",
    "dynamics": "PASS",
    "consistency": "FAIL"
  },
  "major_comments": [
    "Pre-pandemic parallel trends test absent: ENAHO 2017-2019 publicly available, not incorporated; conclusion defers to 'future research' — insufficient for a causal claim given 32 pp rurality and 19 pp gender compositional gaps between groups (Round 1 must-address #4, unresolved).",
    "Wild cluster bootstrap not implemented: paper has 40 clusters (abstract claims 43 — internally inconsistent), below the Cameron-Miller ~50 threshold; conventional cluster-robust SEs have known finite-sample over-rejection bias; WCB with Rademacher weights ≥999 replications required as primary inference method (Round 1 must-address #2, unresolved).",
    "HC1 vs. clustered SE contradiction: Section 3 still states 'heteroskedasticity-robust (HC1)' while Table 2 and Section 4 state clustered SEs; this internal inconsistency makes it impossible to verify which SE type is actually used in any given specification.",
    "Irreconcilable numerical inconsistencies: (a) abstract says 43 clusters, Table 2 says 40; (b) abstract reports Wald test p=0.994, Section 5 reports p=0.937; (c) abstract claims p<0.001 for the headline effect, Table 2 shows 5-10% significance in the continuous specification; (d) the 9 pp headline is not derivable from Table 2 without an explicit calculation mapping the continuous coefficient (-0.20) to the binary group differential."
  ],
  "minor_comments": [
    "Reactiva Perú (S/60bn credit guarantee program conditioned on payroll maintenance) still absent from identification discussion; creates a mechanical formal-informal wedge correlated with treatment and should at minimum be acknowledged with a directional bias assessment.",
    "Event-study profiles for all three informality definitions (social security, written contract, small firm) are described narratively but not plotted; a three-panel event-study figure is needed to verify the cross-definition divergence is not driven by cancellation of year-specific effects.",
    "Heterogeneity results (gender, region, firm-size, age) are described only qualitatively in Section 5 with no tabulated coefficients; referee cannot assess these claims without point estimates and standard errors.",
    "Saltiel (2020) developing-country teleworkability adaptation punted entirely to future research; a sensitivity check using available Saltiel scores for even a subset of ISCO-08 codes would partially validate the crosswalk assumption that underlies the entire identification strategy."
  ]
}
```