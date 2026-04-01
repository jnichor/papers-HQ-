## Referee Report

**Journal of Development Economics**
**Manuscript: "COVID-19 and the Formality Recovery Path in Peru: A Worker-Level Panel DiD Using Sectoral Teleworkability"**

---

### Summary of Methodology

The paper estimates the causal effect of COVID-19 on labor informality in Peru using a pooled WLS difference-in-differences design with year fixed effects. Treatment intensity is the Dingel-Neiman (2020) teleworkability index, mapped to ENAHO ISCO-08 occupation codes, with a binary treatment indicator at the 0.20 threshold (contact-intensive). The event study spans five waves (2020–2024) and tests for permanent scarring via a Wald test of coefficient stability. A secondary within-estimator (individual FEs) is estimated on the rotating panel subsample.

---

### Main Methodological Assessment

This paper addresses an important question with a credible quasi-experimental design, honest acknowledgment of its data limitations, and a well-structured event study. The core identifying variation—teleworkability as pre-determined treatment intensity—is sound in principle. However, the paper as submitted has four substantive methodological problems that require revision before publication: (1) standard errors are systematically understated due to incorrect clustering; (2) no pre-trend evidence is provided or approximated; (3) the divergence across informality definitions is underdiscussed; and (4) extreme survey weights are unaddressed. These are fixable, and the underlying findings are plausible, but the inferential claims currently rest on a weaker statistical foundation than the text suggests.

---

### Major Concerns

**1. Clustering at the wrong level (most critical)**

The paper uses HC1 heteroskedasticity-robust standard errors throughout. However, the treatment variable (teleworkability) is assigned at the ISCO-08 2-digit occupation level, aggregated to 43 sub-major groups. When treatment is constant within clusters, within-cluster residual correlation inflates apparent precision — the classic Moulton (1986) problem. With 43 occupation clusters, the error from ignoring within-occupation correlation is not trivial: Bertrand, Duflo, and Mullainathan (2004) show that DiD SEs can be understated by a factor of 2–3 in analogous settings.

*Suggested fix:* Report all main specifications with SEs clustered at the ISCO-08 2-digit occupation level (or sector × region level as the strategy memo indicates). With 43 clusters, wild cluster bootstrap (Cameron, Gelbach, and Miller 2008) is preferable to asymptotic clustering. The finding that $p < 0.001$ under HC1 may survive this correction, but the authors cannot credibly claim statistical significance without checking.

**2. No pre-pandemic baseline and unaddressed contamination of the 2020 reference period**

The paper correctly acknowledges (Section 6.4) that the ENAHO panel begins in 2020 and that parallel trends cannot be tested. But it does not attempt any approximation. More critically, if ENAHO 2020 fieldwork occurred both before and after the March lockdown, the reference category is partially treated. This has two consequences: (a) DiD coefficients are attenuated toward zero, so reported 9 pp effects are a lower bound; (b) "pre-trend tests" using 2020 variation would be invalid as a falsification.

*Suggested fix:* At minimum, the authors should (i) use any available metadata on ENAHO 2020 interview dates to split the 2020 sample into pre- and post-lockdown subwaves and estimate baseline informality from the pre-lockdown subsample only; (ii) explore whether the ENAHO 2017–2019 cross-sections (not panels) can support a between-survey parallel trends test across occupation groups, even without individual tracking; (iii) quantify the estimated attenuation bias under assumptions about the share of 2020 interviews conducted post-March.

**3. Near-zero contract coefficient demands structural explanation, not just tabulation**

The robustness table shows the social security definition yields $\hat{\gamma}_{2021} = 0.089$ while the written-contract definition yields $\approx 0.002$. This is a 45-fold difference in magnitude that the paper describes in one sentence ("the pandemic's informality shock operated primarily through the loss of employer-provided social security"). This explanation is substantively important and requires its own analysis.

*Suggested fix:* Estimate the joint dynamics of social security and contract coverage at the worker level. If workers lost social security while retaining written contracts, this implies a specific form of deformalization (employer cost-cutting while maintaining formal employment relationships) that has distinct policy implications and also constitutes evidence against the "structural trap" interpretation. Alternatively, if both social security and contracts declined but only the former shows a DiD effect, this points to selection issues in the contract variable. Either way, the paper currently understates a finding that is as important as the main result.

**4. Extreme survey weights unaddressed**

The data audit flags a max/median weight ratio of 3,394×. In WLS, such extreme weights give a single observation the inferential weight of 3,394 average observations. This is not a minor data issue: it can dominate point estimates and standard errors. The paper does not report or discuss this.

*Suggested fix:* (a) Report results with weights winsorized at the 99th percentile as a robustness check; (b) compare unweighted and weighted estimates—if they diverge substantially, investigate which observations have extreme weights (likely rural, small strata) and whether they are driving the DiD result.

---

### Minor Concerns

**5. Binary treatment threshold sensitivity**

The 0.20 cutoff that defines "contact-intensive" is not justified beyond its mechanical properties (captures 75.7% of workers). The authors should show that results are stable across alternative thresholds (0.10, 0.30, 0.40) and/or estimate using the continuous teleworkability score as treatment intensity. The continuous specification also avoids the loss of within-group variation from discretization.

**6. Very asymmetric treatment/control split**

With 196,069 treated and 66,664 control observations (a 3:1 ratio), the comparison group is substantially smaller. The "teleworkable" comparison group (score ≥ 0.20) includes workers with highly heterogeneous characteristics—only 8.2% are highly teleworkable (score ≥ 0.50). The paper should show that results are not sensitive to restricting the control group to high-teleworkability workers (score ≥ 0.50), which provides a sharper contrast.

**7. Large year effects for the control group require discussion**

The year effects for teleworkable workers are substantial: +7.4 pp in 2021, +7.7 pp in 2022. If teleworkable workers are the "unexposed" group, why did their informality also rise by more than 7 percentage points? This suggests either (a) macroeconomic channels affected all workers regardless of teleworkability, or (b) the parallel trends assumption is violated in levels (both groups trended up, but at different rates). The paper should address this—ideally by showing the parallel trends assumption holds in the (unobserved) pre-period, or by discussing what drove the control group's rise.

**8. FE vs. pooled specification inconsistency**

The strategy memo specifies individual fixed effects ($\alpha_i$) as the primary specification. Equation (1) in the paper does not include individual FEs—it is pooled OLS with year dummies and TW$^{low}$ as a level variable. The within-estimator (Eq. 2) is demoted to "secondary." Given that contact-intensive and teleworkable workers differ substantially on baseline characteristics (rural share: 44% vs. 12%, income: 15,440 vs. 25,408 soles), time-invariant confounders in the pooled specification are a concern. The authors should clarify whether the individual FE specification is primary or secondary, and if secondary, explain why pooled OLS is preferred given the panel structure.

**9. Income data documentation**

Table 1 reports monthly income of 15,440 soles for contact-intensive workers and 25,408 soles for teleworkable workers. At current exchange rates, 15,440 soles/month (~$4,000 USD) is implausibly high for a sample dominated by agricultural, construction, and service workers. These may be annual figures, total household income rather than individual labor income, or subject to extreme outlier inflation. Additionally, the income sample is 78,180 out of 196,069 contact-intensive observations (~60% missing), raising selection concerns. The paper should clarify the income variable definition and report median income alongside means.

**10. Multiple testing not discussed**

The paper reports DiD coefficients across 4 post-treatment years, 3 informality definitions, and 4 heterogeneity dimensions. No multiple testing correction is applied or discussed. While the primary interaction effects are large and consistent enough that Bonferroni corrections would not change the conclusion, the authors should at minimum acknowledge this and note which results are pre-specified versus exploratory.

**11. Confidence intervals**

The text reports point estimates and p-values but rarely explicit confidence intervals. Standard practice in development economics is to report 95% CIs alongside estimates. This is especially important for the scarring interpretation: the Wald test p = 0.994 means $\hat{\gamma}_{2024} - \hat{\gamma}_{2021} \approx 0$, but the 95% CI for this difference would reveal whether economically meaningful recovery can be ruled out.

---

### Recommendation

**Major Revision**

The paper makes a credible and important empirical contribution, and the core findings are plausible and well-motivated. However, the clustering issue (Major Concern 1) undermines all inferential claims as currently reported, and addressing it may change the precision of results substantially. The near-zero contract coefficient (Major Concern 3) is itself a substantive finding that the current draft undersells. These revisions are tractable and would substantially strengthen the paper.

---

```json
{
  "score": 66,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "identification_strategy": 64,
    "estimation_implementation": 62,
    "statistical_inference": 65,
    "robustness_sensitivity": 63,
    "replication_readiness": 74
  },
  "sanity_checks": {
    "sign": "PASS",
    "magnitude": "PASS",
    "dynamics": "PASS",
    "consistency": "FAIL"
  },
  "major_comments": [
    "Standard errors use HC1 (heteroskedasticity-robust) despite treatment being assigned at the ISCO-08 2-digit occupation level (~43 clusters). This ignores within-occupation residual correlation (Moulton problem) and likely understates SEs by a factor of 2-3. Must re-estimate with occupation-level clustered SEs and wild cluster bootstrap given only 43 clusters.",
    "ENAHO 2020 is the reference period but fieldwork occurred both pre- and post-March lockdown, making the baseline partially treated. This attenuates DiD estimates (stated) but the paper does not attempt to quantify the attenuation or use pre-lockdown subwave interviews as a cleaner baseline. Additionally, no pre-trend evidence of any form is provided — the paper should explore whether ENAHO 2017-2019 cross-sections can provide supporting (non-panel) parallel trends evidence.",
    "The social security definition yields gamma_2021 = 0.089 while the written-contract definition yields ~0.002 (a 45x difference). This is not a robustness check failure — it is a substantive finding about the mechanism of deformalization. The paper dispatches it in one sentence. A worker-level joint analysis of whether the two margins moved independently or jointly is necessary to support the 'permanent scarring' interpretation.",
    "Data audit flags max/median survey weight ratio of 3,394x. WLS estimates with such extreme weights can be dominated by a handful of high-weight observations. No winsorized-weight robustness check is reported or discussed."
  ],
  "minor_comments": [
    "Binary treatment cutoff at 0.20 is arbitrary. Show sensitivity to alternative thresholds (0.10, 0.30, 0.40) and estimate using the continuous teleworkability score.",
    "Control group (teleworkable, score >= 0.20) experienced +7.4 pp informality increase in 2021 — nearly as large as the main DiD effect. This is unexplained and should be discussed: what drove informality increases among workers the design assumes were unaffected?",
    "Table 1 reports monthly income of 15,440 soles for contact-intensive workers. This is implausibly high (~$4k USD/month) for this population and likely reflects annual income, household income, or extreme outlier inflation. Clarify variable definition and report medians.",
    "Income data is missing for ~60% of contact-intensive observations (78,180 of 196,069) and ~42% of teleworkable observations. Selection into income non-response should be discussed.",
    "Equation (1) does not include individual fixed effects, but the strategy memo specifies them as primary. The within-estimator is demoted to secondary without justification, despite substantial pre-existing differences between treatment and control groups on observable characteristics.",
    "Multiple testing across 3 informality definitions, 4 post-treatment years, and 4 heterogeneity dimensions is not discussed. At minimum acknowledge which results are pre-specified.",
    "Confidence intervals should accompany all point estimates. For the scarring test, the 95% CI for gamma_2024 - gamma_2021 should be reported to show what magnitudes of recovery can be ruled out.",
    "Heterogeneity results in Section 5.4 describe analyses that 'reveal' effects but report no actual coefficients — these are placeholders in the current draft. Actual estimates must be populated.",
    "With only 1,154 individuals observed in all five waves (0.5% of sample), the 'balanced panel' comparison is uninformative. The within-estimator results (attenuation from 0.103 to 0.081) deserve more careful interpretation given the rotating panel structure.",
    "The Saltiel (2020) developing-country teleworkability adaptation is mentioned as a recommended future validation but not implemented. Given that the entire identification strategy rests on the validity of this crosswalk for Peru, at least a partial validation (comparing task distributions for a subset of occupations) would strengthen the paper."
  ]
}
```