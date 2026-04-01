## Referee Report — Round 2

**Journal of Development Economics / Health Economics (submitted)**
**Manuscript:** "Regressive Financial Protection? Quantile Regression Analysis of Out-of-Pocket Health Expenditure in Peru"
**Round:** 2 (Revised Manuscript)

---

### Summary

This paper applies conditional quantile regression to Peru's 2024 ENAHO to examine whether the association between SIS insurance membership and out-of-pocket health expenditure share varies across the conditional spending distribution and across consumption quintiles. The revised version corrects the title framing (from "middle-income squeeze" to "regressive protection gradient"), adds explicit caveats about methodological limitations throughout the text, and acknowledges the zero-mass problem at lower quantiles. The core data construction problems flagged in Round 1, however, remain structurally unresolved.

---

### Main Assessment

I commend the authors for substantially increasing transparency: the limitations section now contains unusually candid self-assessments, the abstract discloses the bootstrap deficiency directly, and the framing correctly describes a monotonic rather than a squeeze-shaped gradient. These are genuine improvements.

Nevertheless, the three issues classified as conditionally fatal in Round 1 have been *acknowledged but not corrected*. The paper's own conclusion states that two issues "require resolution before the findings can be considered reliable." I take that characterization seriously. A manuscript that self-identifies its results as unreliable pending specific corrections should not advance to publication in that state—it should implement the corrections. Transparency about unfixed problems is epistemically commendable but is not a substitute for fixing them.

---

### Major Comments

**1. EsSalud household-head assignment remains uncorrected (Round 1: Conditionally Fatal #1)**

The variable construction still reads: *"The household-level insurance variable is assigned based on the household head's coverage"* (Section 3). The EsSalud cell remains at N=648 (~2% vs. ~30% nationally), and the authors correctly diagnose the cause in the conclusion. The proposed fix—restricting the primary comparison to SIS vs. uninsured—does not resolve the problem: if EsSalud members in households where the head lacks EsSalud coverage are reassigned to the uninsured category, the uninsured reference group is contaminated by high-income formal workers who do have coverage. Every SIS coefficient in the paper is estimated against this polluted baseline. Restricting *interpretation* to the SIS–uninsured comparison does not undo the contamination in the regression coefficients themselves. This issue must be corrected in the data, not in the discussion section.

**2. Mechanical quintile circularity remains uncorrected (Round 1: Conditionally Fatal #2)**

Quintiles are still constructed from GASHOG2D, which includes health expenditure. The abstract discloses this ("partly mechanical"), and the conclusion calls reconstruction "required." The disclosure does not eliminate the problem: the entire quintile gradient—the paper's primary finding—is inflated by this construction. At τ=0.90, the Q5 coefficient (5.16 pp) and the SIS×Q5 interaction (−1.94 pp) are both contaminated by the mechanical component. These are the headline numbers. Until quintiles are reconstructed from non-health consumption, the paper's central finding cannot be separated from an artifact of variable construction.

**3. Bootstrap at 200 replications (Round 1: Conditionally Fatal #3)**

The manuscript still uses 200 cluster-bootstrap replications and still describes this in the abstract as "below the 999 standard." The SIS×Q5 estimate at τ=0.90 (−1.94 pp, p<0.01) anchors the paper's main policy-relevant claim. Bootstrap inference on upper-tail quantile estimates with 200 replications is known to be unstable; the p<0.01 designation is unreliable. Re-estimation with ≥999 replications is computationally straightforward and was required in Round 1. Its continued absence is unexplained.

**4. Primary specification: zero-mass treatment unresolved (Round 1: Must Address #4)**

The abstract and introduction describe the two-part model as a "complement" to CQR, and CQR at τ≥0.50 remains the primary specification. The Round 1 editorial requirement was to either (a) implement censored quantile regression or (b) elevate the two-part model to primary status. Neither has occurred. The 44.1% zero mass means that CQR at τ=0.50 is estimating a conditional quantile that lies exactly at zero for a substantial fraction of the covariate space; the paper acknowledges this creates uninformative estimates at lower quantiles but does not extend the logic to question τ=0.50 more carefully. The two-part model should be the primary vehicle for inference, with CQR reported as sensitivity.

**5. Non-health expenditure falsification test deferred**

The paper acknowledges in Section 6 that the random-reassignment placebo is "weak" and that a non-health expenditure share falsification "would better rule out residual confounding." It then defers this test to future work. A test that takes thirty minutes to run should not be deferred. If the insurance×quintile interactions predict non-health expenditure shares at the same quantiles, the pattern is likely attributable to omitted household characteristics rather than insurance effects. The absence of this test leaves open a straightforward alternative explanation for the headline results.

**6. Multiple testing: acknowledgment without correction**

Section 6 correctly notes that no familywise correction has been applied and that 4/25 significant results is within the chance range. This acknowledgment is not a substitute for the Holm-Bonferroni or Benjamini-Hochberg adjustment required in Round 1. The claim that SIS×Q5 is significant at p<0.01 at τ=0.90 cannot stand without adjustment for testing across five quantiles and multiple interaction terms simultaneously.

---

### Minor Comments

1. **Annualization factor**: The ×13 factor (noted as dominant source of measurement error) warrants a brief discussion of whether ENAHO's 4-week health recall systematically over- or under-represents acute vs. chronic spending households differently across quintiles. Higher-quintile households may be more likely to have chronic, regular expenditure well-captured by 4-week recall; lower-quintile households may have more acute, episodic spending that is poorly annualized.

2. **P41603 heterogeneity**: The paper notes that "other health costs" captures hospitalization, transport, dental, and optical expenses with high within-category variance. For the upper-quantile estimates (τ=0.90), it would be informative to report what share of households at or above the 90th conditional quantile have nonzero P41603—if this category dominates the tail, the headline results are partly an artifact of category heterogeneity.

3. **Targeting leakage mechanism**: The conclusion raises the possibility that the regressive protection pattern reflects SIS enrollment among higher-income households via targeting leakage. This is the most policy-relevant mechanism and deserves more development: administrative data from SUSALUD or regional SIS enrollment audits could be cited to establish whether such leakage is empirically documented in Peru.

4. **Firpo et al. (2009) RIF extension**: The paper correctly notes that RIF regression would provide the population-level complement to the conditional quantile results. Given that the conditional vs. unconditional distinction matters for the policy question (how does SIS shift the population OOP distribution?), this extension is more than a curiosity. It should either be estimated or the distinction should be drawn more sharply when discussing policy implications.

5. **Post-pandemic caveat**: The 2024 post-pandemic caveat is appropriately included but could note specific mechanisms: deferred care during 2020-2022 generating a backlog of high-cost utilization, and changes in health-seeking behavior affecting the zero-mass fraction. The 44.1% zero-OOP rate should be compared to pre-pandemic ENAHO waves to assess whether it reflects steady-state behavior.

---

### Missing Literature

- **Lavado & Valdivia (2010)** — "Intermediación y cobertura del SIS": documents SIS targeting errors in Peru; directly relevant to the leakage mechanism hypothesized in the conclusion.
- **Bernal, Carpio & Klein (2017)** — *Health Economics*: evaluates SIS impact on health care utilization and OOP in Peru using RD design; the most directly comparable causal estimate and a key comparator for the magnitudes reported here.
- **Seinfeld & Besich (2014)** — GRADE working paper on EsSalud's informal coverage measurement issues; directly relevant to the EsSalud N=648 problem.
- **Wagstaff et al. (2018)** — *Lancet*: global CHE decomposition provides benchmarks for Peru's OOP share distribution and enables comparison of the reported 44.1% zero-mass against regional norms.
- **Chernozhukov & Hong (2002)** — cited in Section 2 for censored QR but not implemented; the gap between citation and implementation should be acknowledged or closed.

---

### Recommendation

**Major Revision (Second Round)**

The revised manuscript demonstrates improved transparency and correct framing, both of which are genuine contributions relative to Round 1. However, all three conditionally fatal issues remain structurally unresolved. The paper's own conclusion characterizes the results as unreliable pending correction—a characterization I endorse and which precludes acceptance. The authors should be informed that a third round will be expected to demonstrate: (1) EsSalud variable reconstructed using any-household-member coverage; (2) consumption quintiles reconstructed from non-health consumption; (3) bootstrap replications ≥999; and (4) the non-health expenditure falsification test implemented. If the authors are unable to resolve issues (1) or (2)—for instance, due to variable constraints in the public ENAHO release—they should explain that constraint explicitly and demonstrate that the bias direction and magnitude are bounded in a way that does not overturn the substantive conclusions.

---

```json
{
  "score": 60,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "contribution_novelty": 65,
    "literature_positioning": 68,
    "substantive_arguments": 50,
    "external_validity": 63,
    "journal_fit": 60
  },
  "major_comments": [
    "EsSalud household-head assignment remains uncorrected: N=648 contaminates the uninsured reference group for all insurance comparisons; restricting interpretation to SIS-uninsured does not undo coefficient contamination in estimation.",
    "Mechanical quintile circularity unresolved: quintiles constructed from GASHOG2D inclusive of health spending inflate all quintile gradients and insurance×quintile interactions including the headline SIS×Q5 = -1.94pp estimate.",
    "Bootstrap at 200 replications: upper-tail significance claims (p<0.01 at τ=0.90) remain unstable; re-estimation at ≥999 replications was required in Round 1 and is still absent.",
    "Primary specification not corrected: CQR at τ≥0.50 remains primary without censored QR or two-part model elevation; the 44.1% zero mass continues to undermine the primary inferential vehicle.",
    "Non-health expenditure falsification test deferred to future work despite being a straightforward implementation; deference is not an acceptable substitute for execution when the test is required to rule out omitted variable confounding.",
    "Multiple testing acknowledgment substituted for correction: Holm-Bonferroni or Benjamini-Hochberg adjustment was required in Round 1 and is not implemented; noting that 4/25 is within the chance range does not adjust the significance claims in the main tables."
  ],
  "minor_comments": [
    "Annualization ×13 interacts with spending type: chronic vs. acute expenditure households may be differentially mis-annualized across quintiles; brief discussion warranted.",
    "P41603 heterogeneity may dominate upper-quantile estimates; report share of τ=0.90 households with nonzero other-health-costs.",
    "Targeting leakage mechanism—the most policy-relevant implication of the regressive gradient—deserves empirical anchoring via SUSALUD administrative records or prior audit literature.",
    "Conditional vs. unconditional quantile distinction matters for policy interpretation; RIF extension should be implemented or the distinction drawn more sharply when discussing population-level implications.",
    "44.1% zero-OOP mass should be benchmarked against pre-pandemic ENAHO waves to assess whether it represents steady-state behavior or post-pandemic anomaly."
  ],
  "missing_literature": [
    "Bernal, Carpio & Klein (2017, Health Economics) — SIS impact evaluation using RD; key comparator for reported magnitudes",
    "Lavado & Valdivia (2010, GRADE) — SIS targeting errors in Peru; directly relevant to leakage mechanism",
    "Seinfeld & Besich (2014) — EsSalud informal coverage measurement; relevant to N=648 construction problem",
    "Wagstaff et al. (2018, Lancet) — global CHE decomposition; provides regional benchmarks for zero-mass and OOP share distribution"
  ]
}
```