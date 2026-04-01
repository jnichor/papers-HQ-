## Literature Review: "The Middle-Income Squeeze" — Quantile Regression of CHE Determinants in Peru

---

### Preliminary Note on Provided Closest Papers

The three papers supplied by the submitter (informal payments, malnutrition, altitude-depression) are **tangentially related at best** — they share the ENAHO/ENDES data context or the Peru setting but address entirely different outcomes and mechanisms. The actual closest literature sits in the health financing/catastrophic expenditure and quantile methods traditions. I reframe accordingly below.

---

## 1. Closest Existing Papers

**Paper 1: Xu, K., Evans, D.B., Kawabata, K., Zeramdini, R., Klavus, J., & Murray, C.J.L. (2003). "Household catastrophic health expenditure: a multicountry analysis." *The Lancet*, 362(9378), 111–117.**

- **Main result:** Across 59 countries, 150 million people annually face financial catastrophe from health payments; lack of prepayment coverage and out-of-pocket reliance are the primary structural drivers. Established the WHO "capacity-to-pay" denominator (total consumption minus food expenditure) and the 40% CHE threshold — the exact methodology this proposal adopts.
- **Difference:** Xu et al. use binary probit on CHE incidence as their estimand. There is no within-distribution heterogeneity analysis — a household either crosses the threshold or does not. The proposed study asks *how much* each covariate shifts the entire expenditure-share distribution, which the binary approach cannot answer. Xu et al. also cannot capture the "near-poor" squeeze because their aggregated cross-national design obscures intra-country distributional patterns.

---

**Paper 2: Wagstaff, A., & van Doorslaer, E. (2003). "Catastrophe and impoverishment in paying for health care: with applications to Vietnam 1993–98." *Health Economics*, 12(11), 921–934.**

- **Main result:** In Vietnam, OOP payments pushed 2.5% of households below the poverty line; catastrophic incidence was concentrated among the poor but not exclusively so. Introduced impoverishment-adjusted CHE measures and demonstrated that the poor *under-use* care while the non-poor face budget shocks — an early empirical hint of a distributional story.
- **Difference:** Still uses mean/threshold-based OLS and logit. Wagstaff & van Doorslaer acknowledge that their methods cannot recover heterogeneous covariate effects across the expenditure distribution. The Vietnamese context also lacks the specific SIS/EsSalud/uninsured segmentation that defines Peru's middle-income exposure mechanism.

---

**Paper 3: Knaul, F.M., Wong, R., Arreola-Ornelas, H., & Méndez, O. (2011). "Household catastrophic health expenditures: a comparative analysis of twelve Latin American and Caribbean countries." *Salud Pública de México*, 53(Suppl 4), S85–S95.**

- **Main result:** CHE prevalence in LAC ranges from 1.5% (Uruguay) to 6.5% (Mexico pre-Seguro Popular); the non-poor and partially insured carry disproportionate CHE burden in middle-income LAC countries — the closest existing empirical analog to the "middle-income squeeze" claim. Logistic regression shows insurance coverage is protective but the effect is non-linear across income deciles.
- **Difference:** Uses country-level means and logit; no within-country quantile analysis. Peru is not among the 12 countries. The proposed study operationalizes the distributional non-linearity that Knaul et al. describe qualitatively with a rigorous quantile regression design using nationally representative Peruvian microdata.

---

**Paper 4: Borah, B.J., & Basu, A. (2013). "Highlighting differences between conditional and unconditional quantile regression approaches through an application to assess medication adherence." *Health Economics*, 22(9), 1052–1070.**

- **Main result:** Conditional QR (CQR) and unconditional QR (UQR/RIF) diverge substantially at the tails of health expenditure distributions; UQR is more policy-relevant when the target is the marginal effect on the population distribution rather than individuals with specific covariate profiles. Insurance coverage had statistically larger effects at the upper tail of spending in their application.
- **Difference:** Applied to U.S. Medicare adherence data, not CHE in LMICs; outcome is medication cost rather than expenditure share relative to capacity-to-pay. The proposed study is the first to apply this CQR vs. RIF-UQR comparison explicitly to CHE threshold determinants in a lower-middle-income country.

---

**Paper 5: Limwattananon, S., Tangcharoensathien, V., & Prakongsai, P. (2007). "Catastrophic and poverty impacts of health payments: results from national household surveys in Thailand." *Bulletin of the World Health Organization*, 85(8), 600–606.**

- **Main result:** After Thailand's universal health coverage (UC) scheme launch, CHE incidence among the poor fell sharply but the non-poor-non-insured (informal workers) saw no improvement; CHE concentration among the informal middle persisted. Provides the strongest prior evidence for the "squeeze" mechanism in a comparable LMIC health system.
- **Difference:** Pre/post UC design in Thailand; no quantile regression — still uses CHE incidence rates by quintile. Peru's SIS is explicitly means-tested (unlike Thailand's UC) creating a more pronounced coverage cliff at the near-poor boundary, making the mechanism stronger and the research gap sharper.

---

## 2. Methodological Precedents

**Precedent 1: Firpo, S., Fortin, N.M., & Lemieux, T. (2009). "Unconditional Quantile Regressions." *Econometrica*, 77(3), 953–973.**

- **Credibility:** This is the canonical identification paper for RIF regression. The core insight — that the influence function can be used to decompose unconditional distributional statistics — is well-established. Published critiques (e.g., Borgen 2016, *Sociological Methods & Research*) note that RIF coefficients are local approximations and can be sensitive to bandwidth choice in density estimation, but the method is accepted for policy-relevant distributional analysis.
- **Design lessons for the proposal:** (1) The density at each quantile of health expenditure share must be estimated carefully — kernel bandwidth choice matters at the tails where CHE is concentrated. (2) RIF results should be presented alongside CQR to show the difference is substantive, not artifactual. (3) The proposal's plan to run both CQR and RIF-UQR is methodologically sound and directly follows Firpo et al.'s recommendation.

---

**Precedent 2: Manning, W.G., Basu, A., & Mullahy, J. (2005). "Generalized modeling approaches to risk adjustment of skewed outcomes data." *Journal of Health Economics*, 24(3), 465–488.**

- **Credibility:** Well-cited; the core argument that health expenditure is heavily right-skewed and standard OLS produces biased estimates is robust. The paper compares GLM, two-part models, and quantile regression for OOP expenditure. Published debate with Buntin & Zaslavsky in the same journal; no fatal critiques.
- **Design lessons:** The proposal's OLS baseline will predictably show attenuated insurance coefficients relative to upper-tail QR — Manning et al.'s simulation results predict exactly this. The paper recommends reporting the full quantile path rather than selecting one focal quantile, which the proposal already does (τ = 0.10 through 0.95). Their finding that two-part models and QR converge in the middle quantiles but diverge at extremes validates the focus on τ = 0.90 and 0.95 for catastrophic exposure.

---

**Precedent 3: Flores, G., Krishnakumar, J., O'Donnell, O., & van Doorslaer, E. (2008). "Coping with health-care costs: implications for the measurement of catastrophic expenditures and poverty." *Health Economics*, 17(12), 1393–1412.**

- **Credibility:** This paper directly critiques the Xu et al. threshold methodology, arguing that the binary CHE indicator discards information and that households near the threshold are misclassified. The authors propose continuous measures of "excess" health expenditure as a superior estimand — exactly the continuous outcome the proposed quantile regression uses. Well-cited; no serious methodological rebuttals.
- **Design lessons:** The proposed study should acknowledge this paper's critique explicitly — the motivation for continuous QR over binary CHE logit is precisely the information loss identified here. Flores et al. also show that near-threshold households in their sample are disproportionately in the third and fourth income quintiles, providing prior evidence for the middle-income squeeze hypothesis the proposal seeks to test.

---

## 3. Gap Analysis

**What specific gap does this idea fill?**

The CHE literature in Peru and LAC has three dominant empirical forms: (1) binary logit/probit on CHE incidence using the Xu et al. threshold; (2) OLS on health expenditure share as a continuous outcome; (3) quintile or decile tabulations showing CHE rates by income group. None of these recover heterogeneous covariate effects across the *conditional* or *unconditional* distribution of health expenditure share. The question "does SIS protect the near-poor as effectively as the ultra-poor?" cannot be answered by any of these approaches — it requires examining whether the SIS coefficient changes sign or magnitude between τ = 0.25 and τ = 0.90. This paper fills that methodological gap for Peru specifically, where the three-tier insurance architecture (SIS for the poor, EsSalud for formal workers, out-of-pocket for the middle) creates a theoretically clean test case.

**Is the gap genuine or artificial?**

**Genuine, with caveats.** The gap exists for two real reasons:

1. *Data access*: ENAHO is publicly available but combining the health module and the consumption module to construct the capacity-to-pay denominator requires non-trivial data harmonization. Many researchers use only one module. This is a friction cost, not a fundamental barrier.

2. *Methodological tradition*: Health economists working on CHE in LMICs have been slower to adopt quantile methods than labor economists. The CHE field's attachment to the Xu et al. binary framework — which remains the WHO standard for cross-national comparisons — has created path dependence that discourages distributional analysis.

The gap is **not artificial** in the sense of "the answer being obvious." The direction of the middle-income squeeze — whether near-poor households with partial SIS coverage face *more* or *less* catastrophic exposure than the ultra-poor — is genuinely uncertain *a priori*. The ultra-poor may avoid care entirely (spending near zero), making their *conditional* health expenditure share misleadingly low while their *unconditional* welfare loss from foregone care is high. This selection problem makes the empirical answer non-obvious.

**Could the gap exist because the data doesn't exist?**

No. ENAHO has been publicly available since the early 2000s and includes the required consumption and health expenditure modules. The computational tools (Stata's `qreg`, `rifhdreg`) are standard. The gap is intellectual, not infrastructural.

---

## 4. Positioning Statement

This paper would be cited as the first study to apply unconditional quantile regression to catastrophic health expenditure determinants in Peru, establishing that the protective effect of SIS insurance is concentrated at lower quantiles of the health expenditure distribution and attenuates or reverses at the upper tail where catastrophic episodes occur — a finding that directly challenges the premise of binary CHE measurement and provides empirical grounding for the "missing middle" insurance design problem in Peru's Cobertura Universal de Salud framework. Future papers evaluating SIS expansion, CUS monitoring targets, or the near-poor subsidy boundary would cite this work as the distributional benchmark against which policy counterfactuals are assessed.

---

```json
{
  "closest_papers": [
    "Xu et al. (2003)",
    "Wagstaff & van Doorslaer (2003)",
    "Knaul et al. (2011)",
    "Borah & Basu (2013)",
    "Limwattananon et al. (2007)"
  ],
  "gap_is_genuine": true,
  "gap_reason": "The CHE literature in Peru and LAC uses binary logit or mean regression, neither of which recovers heterogeneous covariate effects across the expenditure distribution. ENAHO data is available; the gap is methodological and disciplinary, not data-constrained. The middle-income squeeze hypothesis is empirically non-obvious due to care-avoidance selection among the ultra-poor.",
  "novelty_assessment": "MEDIUM",
  "methodological_risk": "LOW",
  "positioning": "This paper would be the first to apply RIF unconditional quantile regression to the determinants of catastrophic health expenditure in Peru, demonstrating that insurance-type effects are quantile-dependent and that near-poor households with partial SIS coverage face disproportionate upper-tail expenditure risk — providing a distributional benchmark for CUS subsidy design that binary CHE incidence measures cannot supply."
}
```

---

### Critical Observations for the Author

1. **Novelty is MEDIUM, not HIGH.** The distributional heterogeneity of CHE determinants has been noted qualitatively (Knaul et al., Wagstaff & van Doorslaer) but not formally estimated. The quantile method is the contribution; the Peru context and SIS mechanism add applied relevance but do not constitute a fundamental theoretical advance.

2. **The three supplied "closest papers" are poor comparators.** Informal payments (Espinoza-Pajuelo), malnutrition (Pradeilles), and altitude-depression (Zegarra-Rodríguez) share the survey data context but are orthogonal in method and outcome. The submission would benefit from replacing them with papers from the CHE/health financing tradition listed above.

3. **The care-avoidance selection problem is the main threat to the middle-income squeeze narrative.** If the ultra-poor have near-zero health spending because they forgo care rather than because SIS protects them, the quantile regression at τ = 0.10 is not estimating "good insurance protection" — it is estimating the covariate profile of care-avoiders. The Wald test across quantiles is necessary but not sufficient to distinguish these mechanisms. A two-part model (probability of any spending × conditional level) run in parallel would strengthen the identification of the squeeze story.

4. **Methodological risk is LOW** because ENAHO is clean, QR is well-established, and the RIF extension is standard. The main execution risk is the capacity-to-pay denominator construction — the food expenditure deflation from the consumption module requires careful treatment of imputed values.