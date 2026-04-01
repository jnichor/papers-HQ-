## Referee Report

**Journal of Health Economics / World Development (Applied Health)**

---

### Summary

This paper uses Peru's 2024 ENAHO to estimate conditional quantile regressions of out-of-pocket (OOP) health expenditure share, interacting insurance status (SIS, EsSalud, uninsured) with consumption quintiles to test a "middle-income squeeze" hypothesis. The core claim is that OLS/binary CHE threshold analyses mask distributional heterogeneity in how insurance correlates with OOP burden. The authors provide 25 robustness checks and are transparent about the descriptive (non-causal) nature of their estimates.

---

### Main Assessment

**Strengths.** The paper is well-motivated, correctly identifies a genuine limitation of binary CHE threshold analyses, and applies an appropriate distributional method to a rich nationally representative dataset. The institutional description of Peru's fragmented health system is broadly accurate, and the honesty about identification limitations is commendable. The robustness exercise is unusually thorough for a descriptive paper.

**Weaknesses.** Three issues stand out. First, a 44.1% zero-mass in the outcome variable renders standard Koenker–Bassett quantile regression problematic at low quantiles and potentially inconsistent throughout, yet the paper does not engage with the censored quantile regression or two-part model literatures that address this directly. Second, the EsSalud cell ($N = 648$ household heads, ≈1.9% of the sample) is implausibly small given that EsSalud covers approximately 30–35% of Peru's population; this signals a likely variable construction error that undermines one of the paper's three insurance categories. Third, the central "middle-income squeeze" hypothesis is imperfectly supported by the presented results, which show Q5 effects dominating and significant SIS–quintile interactions mainly at Q3–Q5—a monotonic protection gradient, not a squeeze that specifically disadvantages Q2–Q4 relative to both ends.

---

### Major Comments

**1. Zero-mass problem invalidates the baseline quantile regression framework.**
With 44.1% of households reporting zero OOP spending, the conditional quantile function is degenerate (identically zero) for all $\tau < 0.441$ in most covariate cells. The paper acknowledges this at $\tau = 0.10$ ("degeneracy of the conditional quantile function") but proceeds to report and interpret $\tau = 0.25$ estimates without noting that the same issue likely affects the median in low-income, low-utilization subgroups. More fundamentally, standard quantile regression with a discrete mass at zero is inconsistent in the sense that Machado & Santos Silva (2005, *Journal of Econometrics*) formalize: the estimating equation does not identify the intended quantile when a positive fraction of observations shares the minimum value. The paper should either (a) adopt censored quantile regression (Powell 1986; Chernozhukov & Hong 2002, *Econometrica*) treating zero as a censoring point, (b) use a two-part model (Manning et al. 1987, *Journal of Health Economics*; Mullahy 1998, *Journal of Health Economics*) as the primary specification with QR on the positive-OOP subsample only, or (c) explicitly characterize which quantiles are identified given the zero mass. As currently specified, presenting $\tau = 0.10$ through $\tau = 0.50$ estimates without addressing this is methodologically indefensible.

**2. EsSalud cell size suggests a variable construction error.**
The paper reports $N = 648$ EsSalud household heads out of 33,691 total households (≈1.9%). EsSalud covers formal-sector workers and their dependents; Peru's formal employment rate implies roughly 6,000–10,000 EsSalud household heads in a nationally representative ENAHO sample of this size. The discrepancy is approximately 10-fold. One plausible explanation: in ENAHO Module 400, P4192 may be coded as a single-digit categorical variable (e.g., 1 = SIS, 2 = EsSalud, ...) rather than a binary indicator for EsSalud specifically. Using P4192 = 1 as a filter for EsSalud would then select only a residual category. The authors must verify variable coding against ENAHO's current dictionary and reconstruct EsSalud enrollment accordingly. This is not a minor issue: the entire EsSalud arm of the analysis is uninformative as presented.

**3. Consumption quintile endogeneity is more severe than acknowledged.**
The paper notes the endogeneity of quintile assignment in passing (Section 3) but does not resolve it. ENAHO's Sumaria module variable GASHOG2D is a comprehensive consumption aggregate that, by construction, *includes* health expenditures (Module 400 flows into Sumaria). Households with high OOP spending are thus assigned to higher quintiles *partly because of* their health spending, inducing a mechanical positive correlation between OOP share (numerator) and quintile rank. This is not a subtle endogeneity problem—it inflates the quintile gradient throughout Table 2 and biases the very interaction terms the paper interprets as evidence of the middle-income squeeze. The standard correction is to construct quintiles from consumption *net of health expenditure* before computing the OOP share. The authors mention this possibility as a footnote (Section 3) but do not implement it even as a robustness check. This should be the primary specification.

**4. The middle-income squeeze narrative does not follow from the results.**
The paper's central hypothesis is that Q2–Q4 ("middle-income") households face disproportionate OOP burden relative to both Q1 and Q5. The evidence does not support this framing. The significant SIS–quintile interaction coefficients at upper quantiles are largest for Q3–Q5, forming a monotonic gradient, not a U-shaped pattern that would identify Q2–Q4 as distinctly squeezed from both sides. The paper reframes this as SIS providing "progressively larger reductions" up the income distribution, which is an interesting finding but is more accurately described as a *coverage incidence* result (insurance protection increases with income, conditional on enrollment) than a squeeze. The middle-income squeeze framing requires showing that Q2–Q4 households face higher OOP burden than both Q1 (who forgo care or access SIS) *and* Q5 (who absorb shocks). No such comparison is presented. The paper should either present explicit quintile-by-quintile counterfactuals that support the squeeze narrative or rename the hypothesis.

**5. SIS leakage and targeting errors are central to interpreting SIS–quintile interactions.**
The paper documents positive and significant SIS–Q5 interactions—SIS enrollees in the wealthiest consumption quintile appear to receive meaningful financial protection. But Q5 households should not be SIS-eligible: SIS is means-tested using SISFOH (Sistema de Focalización de Hogares) targeting and the Padrón General de Hogares. Finding SIS-enrolled Q5 households suggests substantial leakage (non-poor receiving means-tested benefits), which is well-documented in Peru (Cortez 2008; Francke 2013) but entirely absent from the paper's discussion. The SIS–quintile interactions cannot be interpreted as measuring insurance protection across income without first decomposing how much SIS enrollment at Q4–Q5 reflects targeting error vs. quintile misclassification vs. legitimate enrollment by recently impoverished households. This decomposition is central to the paper's institutional narrative.

---

### Minor Comments

1. **Annualization multiplier.** The paper annualizes 4-week recall OOP spending by multiplying by 13 (52 weeks ÷ 4 weeks). But 4 weeks is not a calendar month; using ×13 implies 364 days per year. The more common approach in the ENAHO literature is ×12 for comparability with monthly income. The paper tests ×12 in robustness, but should be more explicit in the main text about why ×13 is preferred and what the empirical difference is.

2. **Number of PSU clusters.** The paper reports cluster-bootstrapped standard errors at the PSU level with 200 replications but does not report the number of PSUs (clusters). With fewer than ~50 clusters, the cluster bootstrap has poor finite-sample properties (Cameron, Gelbach & Miller 2008, *ReStat*). The wild cluster bootstrap (Roodman et al. 2019, *Stata Journal*) would be more robust. Report the cluster count and justify the choice of standard bootstrap.

3. **Luxury good claim.** The paper states that increasing OOP share across quintiles indicates "health care being a luxury good at the household level." This conflates the Engel curve slope (share rising with income) with income elasticity. A luxury good requires expenditure elasticity > 1; increasing share is consistent with elasticities between 0 and ∞ depending on the denominator. The claim should either be supported with an elasticity estimate or dropped.

4. **AUS institutional reference.** The paper cites SIS (2002) and "CUS" but omits the foundational Law 29344 (Ley Marco de Aseguramiento Universal en Salud, 2009), which established the legal framework for universal coverage in Peru and created the PEAS (Plan Esencial de Aseguramiento en Salud). This is the primary institutional anchor for the CUS framework described in the introduction.

5. **Descriptive table on insurance × quintile cells.** The paper discusses SIS–Q5 interactions but never reports how many observations are in each insurance–quintile cell. A cross-tabulation of insurance status by quintile is essential for readers to evaluate whether the interaction estimates are based on credible cell sizes or thin data.

6. **OOP cap at 1.** The paper caps OOP share at [0, 1] after the floor adjustment but does not report what fraction of observations had raw OOP share > 1 before capping. This is a data quality indicator.

7. **Post-COVID context.** The 2024 ENAHO is collected during the post-pandemic recovery period. Peru experienced one of the world's highest COVID-19 excess mortality rates, with substantial disruption to health-seeking behavior. The paper should at minimum acknowledge that 2024 health expenditure patterns may reflect post-pandemic adjustment rather than steady-state behavior, and discuss whether this affects the generalizability of findings.

---

### Missing Literature

The following references are relevant and should be engaged:

- **Machado & Santos Silva (2005)** — "Quantiles for Counts," *JASA*: QR with mass points / discrete outcomes.
- **Powell (1986)** — Censored quantile regression: the appropriate estimator when zeros are censored rather than structural.
- **Chernozhukov & Hong (2002)** — Three-step censored quantile regression, *Econometrica*.
- **Manning, Duan & Rogers (1987)** — Two-part model for health expenditure, *JHE*: standard alternative for zero-inflated outcomes.
- **Mullahy (1998)** — Much ado about two, *JHE*: critique of two-part models and alternatives.
- **Cortez (2008)** — SIS targeting performance in Peru: essential for interpreting SIS leakage into higher quintiles.
- **Francke (2013)** — SIS reform and financial protection: key Peru-specific institutional reference.
- **Acharya et al. (2012)** — "The Impact of Health Insurance on Health," *BULR*: systematic review of insurance effects in LMICs; should frame the selection discussion.
- **Wagstaff (2010)** — "Estimating Health Insurance Impacts under Unobserved Heterogeneity," *HE*: identification challenges with observational insurance data.
- **Knaul et al. (2006)** — Seguro Popular in Mexico: natural regional comparison for a subsidized poor-targeting insurance scheme.
- **Firpo, Fortin & Lemieux (2009)** — The paper cites this for RIF but should note that RIF estimates would provide the population-level complement to the conditional QR results, directly answering whether middle-income quintiles have higher unconditional OOP shares.

---

### Recommendation

**Major Revision**

The paper addresses a legitimate empirical gap using appropriate data. However, the zero-mass problem with standard quantile regression, the probable EsSalud variable construction error, the consumption quintile endogeneity, and the mismatch between the narrative hypothesis and the empirical results require substantial revision before the paper can be accepted. The core empirical exercise is salvageable, but the methodology and framing need reworking.

---

```json
{
  "score": 63,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "contribution_novelty": 68,
    "literature_positioning": 58,
    "substantive_arguments": 61,
    "external_validity": 62,
    "journal_fit": 67
  },
  "major_comments": [
    "Zero-mass problem (44.1% zeros) renders standard Koenker-Bassett QR inconsistent at low quantiles; paper must engage with censored QR (Powell 1986; Chernozhukov & Hong 2002) or two-part models (Manning et al. 1987) as the primary specification.",
    "EsSalud cell of N=648 (~1.9% of households) is implausibly small given ~30-35% national EsSalud coverage; probable variable construction error in P4192 coding that invalidates the EsSalud arm of the analysis.",
    "Consumption quintiles constructed from GASHOG2D, which includes health expenditures, creating a mechanical positive bias in the quintile-OOP share gradient; quintiles should be computed net of health expenditure.",
    "The middle-income squeeze hypothesis predicts Q2-Q4 face higher OOP burden than both Q1 and Q5, but results show a monotonic protection gradient (largest effects at Q5), not a squeeze; the central narrative does not follow from the evidence.",
    "SIS enrollment at Q4-Q5 reflects known SISFOH targeting errors (leakage) that are central to interpreting SIS-quintile interactions but are not discussed; the paper cannot attribute upper-quintile SIS effects to protection without decomposing leakage vs. legitimate enrollment."
  ],
  "minor_comments": [
    "Report the number of PSU clusters and consider wild cluster bootstrap (Roodman et al. 2019) given potential for fewer than 50 clusters in some subsamples.",
    "The 'luxury good' claim conflates increasing Engel curve share with income elasticity > 1; drop or support with an explicit elasticity estimate.",
    "Omits Law 29344 (AUS, 2009) as the primary institutional anchor for the universal coverage framework described in Section 1.",
    "A cross-tabulation of insurance status by quintile is essential for evaluating interaction cell sizes; add as Table 1 or appendix.",
    "Acknowledge the post-COVID context of 2024 ENAHO data and discuss whether post-pandemic health-seeking disruption affects generalizability.",
    "Annualization by x13 vs. x12 should be more explicitly motivated in the main text, not deferred to robustness."
  ],
  "missing_literature": [
    "Machado & Santos Silva (2005, JASA) — QR with discrete mass points/zeros: directly relevant to the 44.1% zero-OOP problem.",
    "Powell (1986) — Censored quantile regression: the appropriate estimator for left-censored outcomes with structural zeros.",
    "Chernozhukov & Hong (2002, Econometrica) — Three-step censored QR implementation.",
    "Manning, Duan & Rogers (1987, JHE) — Two-part model: the standard benchmark for zero-inflated health expenditure.",
    "Mullahy (1998, JHE) — Two-part model critique and alternatives for health expenditure.",
    "Cortez (2008) — SIS targeting performance in Peru: essential for leakage discussion in SIS-quintile interactions.",
    "Francke (2013) — SIS reform and financial protection: key Peru-specific institutional reference.",
    "Acharya et al. (2012, BULR) — Systematic review of health insurance impacts in LMICs.",
    "Wagstaff (2010, Health Economics) — Identification challenges with observational insurance data in LMICs.",
    "Knaul et al. (2006) — Seguro Popular in Mexico: natural regional institutional comparison.",
    "Firpo, Fortin & Lemieux (2009) — More prominent engagement needed; RIF estimates would provide the population-level complement to conditional QR."
  ]
}
```