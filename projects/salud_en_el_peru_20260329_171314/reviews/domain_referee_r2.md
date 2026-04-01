## Referee Report

**Journal:** Health Economics / Journal of Development Economics (assumed)
**Manuscript:** "The Middle-Income Squeeze: Distributional Analysis of Health Expenditure Determinants in Peru"

---

### Summary

This paper applies conditional quantile regression to Peru's 2024 ENAHO to examine whether the correlates of out-of-pocket (OOP) health expenditure share vary across the conditional spending distribution, interacting insurance status (SIS, EsSalud, uninsured) with consumption quintiles. The authors find that OLS estimates of SIS effects are null at the mean, but SIS–quintile interactions become significant and negative at upper quantiles, with a monotonically increasing protection gradient from Q1 to Q5 rather than the U-shaped pattern the "middle-income squeeze" hypothesis predicts. The paper is accompanied by 25 robustness checks and an unusually candid limitations discussion.

---

### Main Assessment

The paper's chief virtues are its methodological transparency, comprehensive robustness analysis, and intellectual honesty in reporting a result that refutes its own title hypothesis. These are genuine strengths in an area where confirmatory bias is pervasive. However, several issues impede publication in its current form: a fundamental mismatch between the title framing and the findings, an inadequately investigated EsSalud measurement failure that invalidates one arm of the insurance analysis, an unaddressed mechanical endogeneity in the quintile assignment, and an insufficiently implemented primary methodology (censored quantile regression or two-part model are described but not adopted as the main specification despite the acknowledged 44.1% zero-mass problem). The institutional and literature coverage of the Peru-specific context has meaningful gaps.

---

### Major Comments

**1. Title–findings mismatch requires resolution**

The paper is titled "The Middle-Income Squeeze" and the abstract frames the analysis as testing whether middle-income households face *disproportionate* OOP burden relative to both the poorest and the wealthiest. The results section (§5) and conclusion (§7) acknowledge that this hypothesis is *rejected*: the protection gradient is monotonically increasing from Q1 to Q5, not U-shaped. This is a substantive finding in its own right, but the title, abstract framing, and introduction all continue to lead with the squeeze hypothesis as if it were supported. The paper needs either (a) a revised title and framing that leads with the monotonic regressive protection gradient as the primary finding, or (b) a more explicit structure that announces the hypothesis, reports its rejection, and reorients the paper around what the data actually show. A paper whose results contradict its framing signals to reviewers that the analysis was designed to confirm a prior hypothesis and then restructured after the fact.

**2. EsSalud measurement failure is insufficiently investigated**

The authors note in passing that the EsSalud cell has N=648 and caution against interpreting EsSalud coefficients. This is inadequate. EsSalud covers approximately 10–11 million Peruvians (roughly 30% of the population), the majority of formal-sector workers and their dependents. A nationally representative ENAHO sample of 33,691 households should yield several thousand EsSalud-affiliated households. The reported N=648 is off by an order of magnitude and suggests a variable construction error, not a sampling artifact.

The most likely source is the authors' decision to assign household insurance status from the *household head's* coverage alone (§3, variable construction). Many households in which the head is self-employed or informal will have EsSalud-affiliated dependents (spouses in formal employment, adult children) whose coverage is discarded. An alternative explanation is mis-specified variable logic in the SIS/EsSalud precedence rule (P4191/P4192). The authors must: (i) document the marginal frequency distributions of P4191 and P4192 before and after applying their coding rules; (ii) check whether the N=648 figure is at the individual or household level; (iii) consider reassigning household insurance to *any member* having EsSalud rather than only the head; and (iv) report the share of households with at least one EsSalud-affiliated member as a check against national administrative data. Until this is resolved, the insurance framework is one-armed, and the SIS vs. uninsured comparison cannot be cleanly interpreted without knowing which portion of the "uninsured" category actually has EsSalud coverage misclassified.

**3. Mechanical endogeneity in the quintile–OOP share relationship**

The denominator of the OOP share outcome is total household consumption (GASHOG2D from Sumaria). The quintile assignment is also constructed from GASHOG2D. Health spending is a component of total consumption in ENAHO's Sumaria module. This creates a mechanical, negative-feedback relationship: higher OOP spending pushes households into higher quintiles, which then appears as a positive quintile gradient in the OOP share regression. The authors acknowledge this in one sentence (§5) but treat it as a caveat rather than addressing it. The standard correction in the CHE literature is to construct quintiles from *non-health* consumption or from permanent income proxies. The Xu et al. (2003) "capacity-to-pay" approach (consumption net of subsistence food spending) addresses the related but distinct subsistence problem; the quintile endogeneity problem requires a separate fix. At minimum, the authors should present quintile-assignment sensitivity using consumption net of health spending.

**4. Primary methodology inconsistency**

The paper describes the two-part model and censored quantile regression (CQR) as methodological solutions to the zero-mass problem, but implements neither as the primary specification. Instead, the authors use standard Koenker–Bassett CQR while restricting interpretation to τ ≥ 0.50 post-hoc. This is defensible as a practical choice but conflicts with the methodological framing in §2 (literature review) and §4 (strategy). If the zero-mass fraction is 44.1%, then the 50th conditional quantile is near zero for much of the covariate space, and the restriction to τ ≥ 0.50 does not fully resolve the degeneracy problem — it merely postpones it. The paper should either (a) implement CQR with Powell's (1986) censored estimator or the Chernozhukov-Hong (2002) approach as the main specification, with standard CQR as a robustness check; or (b) more explicitly defend why the two-part model at the intensive margin is a sufficient complement and report its estimates with at least comparable prominence to the quantile regressions. The current presentation leaves the reader uncertain whether the upper-quantile results survive proper treatment of the zero mass.

**5. Cluster bootstrap adequacy**

The authors themselves note (§7) that the 200-replication cluster bootstrap is below the standard for publishable inference, particularly for upper-tail quantile standard errors which require more replications due to higher variance in the estimating equations. This is not a minor caveat — inference at τ = 0.90 with 200 bootstraps is unreliable, and the paper's principal substantive claims (the SIS×Q5 coefficient at τ = 0.90 is −1.94 pp, p < 0.01) rest on this inference. The standard recommendation for quantile regression with cluster bootstrap is ≥ 500 replications at the median and ≥ 1,000 at tail quantiles. This should be corrected before submission to any peer-reviewed journal.

**6. SIS institutional characterization is outdated**

The paper describes SIS as a "subsidized public insurance scheme for the poor" with means-tested targeting. This characterization was accurate pre-2019 but is incomplete for 2024 data. Decreto Legislativo 1302 (2016) and subsequent reforms (particularly under the Decreto de Urgencia 017-2019 and the pandemic-era expansions) substantially broadened SIS coverage beyond the poor, and SISFOH (Sistema de Focalización de Hogares) scoring — the actual targeting instrument — has known leakage rates documented in MIDIS evaluations. The paper's discussion of "targeting leakage" as an explanation for the regressive SIS protection pattern (§7) is qualitatively correct but would be strengthened by engaging with the actual targeting mechanism and citing evaluations of SISFOH accuracy. Additionally, the paper does not mention FISSAL (Fondo Intangible Solidario de Salud), the SIS sub-fund for high-cost diseases, which is directly relevant to catastrophic spending at the upper tail. Households enrolled through FISSAL have qualitatively different coverage that could explain part of the upper-quantile SIS association.

---

### Minor Comments

1. **Abstract framing**: The abstract states the results "suggest that policies targeting average CHE rates may overlook the concentration of financial risk in the upper tail...where middle-income households without adequate insurance bear the greatest burden." This is not supported by the reported results, which show a monotonic Q1-to-Q5 gradient — the *highest*-quintile households, not middle-income ones, show the largest conditional OOP burden and the largest SIS interaction effects. This sentence should be revised.

2. **Annualization factor**: The paper multiplies 4-week recall spending by 13 to annualize (52 ÷ 4 = 13). However, ENAHO Module 400 uses a 4-week reference period, not one calendar month. The authors correctly note this introduces amplification error for acute episodes but do not note that the choice of 13 vs. 12 has different implications for seasonal health spending (e.g., respiratory illnesses in Andean winter). The ×12 robustness check is appropriate; the authors should clarify whether ×13 is standard practice in ENAHO-based health expenditure papers (it is — INEI documentation uses this factor) or a methodological choice.

3. **Urban–rural divergence finding**: The robustness section (§6) reports a significant *positive* SIS coefficient in the rural subsample (0.0056, p = 0.016), attributed to transport and medication costs for insured rural households that do seek care. This finding deserves more attention in the conclusion — it may represent a more important policy result than the urban-sample null. The SIS program's facility network in rural areas is critically underdeveloped relative to its enrollment coverage, and this is a known policy failure documented in ENAHO-based facility utilization studies.

4. **P41603 heterogeneity**: The authors note that the "other health costs" category captures heterogeneous items (hospitalization, transport, dental, optical). In the Peru context, dental and optical expenses are substantial and are frequently accessed at private facilities even by SIS enrollees who receive primary care publicly. Separating P41603 into hospitalization versus non-hospitalization components, even as a sensitivity, would help assess whether the upper-quantile findings are driven by catastrophic hospitalization costs or by the accumulation of small non-covered costs.

5. **RIF regression**: The paper correctly identifies RIF regression (Firpo et al., 2009) as providing the population-level complement to conditional quantile regression and defers it to future work. Given that much of the policy discussion concerns population-level CHE rates (the WHO/World Bank monitoring framework uses unconditional prevalence), adding at least a RIF-based table would significantly strengthen the policy relevance of the paper.

6. **Placebo test weakness**: The authors correctly note (§6) that the random treatment reassignment placebo is weak — regressing noise on correlated controls in a large sample is expected to yield a null. The more informative placebo of predicting *non-health* expenditure shares at upper quantiles is flagged as future work but would take limited additional effort given the data infrastructure already built.

7. **Multicollinearity in insurance–quintile cell sizes**: The paper does not report cell sizes for each SIS–quintile interaction cell. Given that SIS is means-tested (even with leakage), the SIS×Q5 cell likely has very few observations, and the upper-quantile coefficient for this interaction should be interpreted with caution regardless of bootstrap standard errors.

---

### Missing Literature

- **Wagstaff, A. (2010). Estimating health insurance impacts under unilateral enrollment: evidence from Peru's Seguro Integral de Salud.** *Journal of Development Economics*, 92(2), 267–276. This is the primary quasi-experimental study of SIS impact in Peru and must be cited. The authors' findings on null mean effects and potential selection bias are directly compared to Wagstaff's difference-in-differences estimates.

- **Seinfeld, J. & Montañez, C. (2007).** GRADE working paper on SIS financial protection. Provides Peru-specific baseline against which to benchmark.

- **Knaul, F. M., et al. (2011). The quest for universal health coverage: achieving social protection for all in Mexico.** *The Lancet*, 378(9808), 1259–1273. The Seguro Popular experience is the closest Latin American comparator to SIS and should be discussed.

- **McIntyre, D., et al. (2006). What are the economic consequences for households of illness and of paying for health care in low- and middle-income country contexts?** *Social Science & Medicine*, 62(4), 858–865. Conceptual framework for financial consequences.

- **Bernal, N., Carpio, M. A., & Klein, T. J. (2017). The effects of access to health insurance for informally employed individuals in Peru.** *Journal of Public Economics*, 154, 122–136. This paper uses discontinuities in SIS eligibility to estimate causal effects and is directly relevant to the selection concern.

- **Duan, N., et al. (1983). A comparison of alternative models for the demand for medical care.** *Journal of Business & Economic Statistics*, 1(2), 115–126. Standard reference for the two-part model that should be cited alongside Manning (1987).

- **Chernozhukov, V. & Hong, H. (2002). Three-step censored quantile regression.** *Journal of the American Statistical Association*, 97(459), 872–882. If censored QR is mentioned as an alternative, this is the implementation reference.

- **WHO & World Bank (2023). Tracking Universal Health Coverage: 2023 Global Monitoring Report.** Current benchmark for CHE monitoring methodology.

---

### Recommendation

**Major Revision**

The paper has a sound empirical core, commendable transparency, and a finding (the monotonic regressive protection gradient) that is genuinely policy-relevant for the CHE literature on Latin America. However, the EsSalud measurement failure, the title–findings mismatch, the mechanical endogeneity in quintile assignment, and the inadequate bootstrap implementation all require substantive revision before the paper can be published. The institutional characterization gaps are correctable. The decision to not implement CQR or the two-part model as the primary specification despite the known zero-mass problem is the most significant methodological weakness and should be addressed directly in the revision.

---

```json
{
  "score": 62,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "contribution_novelty": 65,
    "literature_positioning": 58,
    "substantive_arguments": 57,
    "external_validity": 65,
    "journal_fit": 63
  },
  "major_comments": [
    "Title–findings mismatch: the paper is framed around the middle-income squeeze hypothesis but reports a monotonic Q1-to-Q5 regressive gradient that rejects this hypothesis. The title, abstract, and introduction must be revised to lead with the actual finding.",
    "EsSalud N=648 is an order of magnitude below what a 30%-coverage scheme should yield in a nationally representative sample of 33,691 households. The household-head assignment rule likely discards thousands of EsSalud-affiliated non-head members. This must be investigated and documented before the insurance framework can be treated as valid.",
    "Mechanical endogeneity: total consumption (the quintile denominator) includes health spending in ENAHO Sumaria, creating a mechanical positive quintile–OOP share correlation. The paper acknowledges this in one sentence but does not correct it. Quintiles should be reconstructed from non-health consumption.",
    "The primary methodology is standard Koenker–Bassett CQR with post-hoc restriction to τ≥0.50, despite the acknowledged 44.1% zero mass. The two-part model and censored QR are described but not implemented as primary specifications. This inconsistency should be resolved — either implement CQR properly or elevate the two-part model.",
    "200-replication cluster bootstrap is below the minimum for credible inference at τ=0.90. The paper's main substantive claims rest on this inference. Replication count should be raised to ≥1,000 for upper-tail quantiles."
  ],
  "minor_comments": [
    "Abstract final sentence claims middle-income households bear the greatest burden, contradicting results that show a monotonic gradient peaking at Q5.",
    "The SIS positive coefficient in the rural subsample (robustness §6) deserves more prominence — it may be a more actionable finding than the urban null.",
    "P41603 heterogeneity (hospitalization vs. dental/optical) should be explored as a sensitivity given its likely role in driving upper-quantile estimates.",
    "Cell sizes for each SIS×quintile interaction should be reported — the SIS×Q5 cell is likely sparse and affects interpretation of the key coefficient.",
    "RIF regression would add meaningful policy relevance given that WHO/World Bank CHE monitoring uses unconditional prevalence rates; even one table would strengthen the paper.",
    "The random-treatment placebo (§6) is acknowledged as weak but the non-health expenditure falsification is deferred to future work; this would take minimal effort given existing data infrastructure."
  ],
  "missing_literature": [
    "Wagstaff (2010, JDE) — primary quasi-experimental SIS evaluation in Peru; must be cited and compared against.",
    "Bernal, Carpio & Klein (2017, JPubE) — causal effects of SIS access for informal workers using eligibility discontinuities.",
    "Knaul et al. (2011, Lancet) — Seguro Popular as closest Latin American comparator for SIS design and evaluation.",
    "Duan et al. (1983, JBES) — standard two-part model reference missing despite the model being discussed.",
    "Chernozhukov & Hong (2002, JASA) — implementation reference for censored QR mentioned but not cited.",
    "WHO & World Bank (2023) Global UHC Monitoring Report — current benchmark for CHE measurement methodology.",
    "McIntyre et al. (2006, SSM) — financial consequences of illness framework for LMICs."
  ]
}
```