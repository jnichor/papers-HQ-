# Junshi — Research Advisory: Salud en el Perú

---

## PART 1: Synthesis of Seed Papers

### Themes
| Dimension | Pattern Across Papers |
|---|---|
| **Data** | All use large national cross-sections (ENAHO, ENDES) — descriptive/associational only |
| **Methods** | Logistic regression, prevalence ratios — no causal identification attempted |
| **Geography** | Altitude and urban/peri-urban gradients matter, but mechanisms unexplored |
| **Insurance** | SIS enrollment creates perverse incentives (higher informal payments) — endogeneity ignored |
| **Equity** | Socioeconomic position surfaces repeatedly as a confounder, never decomposed |

### Critical Gaps
1. **No causal identification** — all three papers establish correlations; no IV, RDD, or Heckman
2. **Selection bias unaddressed** — SIS enrollment and care-seeking are endogenous
3. **Distribution ignored** — OLS/logit averages mask heterogeneity across expenditure and health quintiles
4. **Ethnicity absent** — socioeconomic proxies used, but indigenous/mestizo distinctions never decomposed
5. **Mental health mechanisms** — altitude-depression gradient established but physiological vs. structural pathway untested

---

## PART 2: The 10 Research Ideas

---

### IDEA 1 — SIS Insurance, Rationing, and Informal Payments
**Sub-topic:** Health insurance & informal payments

**Research Question:** Does SIS enrollment paradoxically *increase* informal payment exposure through supply-side rationing at public MINSA facilities, and does this effect vary by facility density?

**Method:** Heckman two-stage selection model. Stage 1: determinants of SIS enrollment (selection equation using district SIS penetration rate as exclusion restriction). Stage 2: conditional probability of informal payment and magnitude conditional on enrollment. This corrects for the non-random selection into SIS.

**Data:** ENAHO user dataset (health module P400–P401 series covers insurance type, facility used, payments)

**Why novel:** The seed paper (Espinoza-Pajuelo 2024) identifies SIS beneficiaries as *more* exposed to informal payments but treats this as correlation. No study has applied Heckman to isolate supply-side rationing from adverse selection into SIS.

**Why impactful:** Directly informs MINSA's SIS expansion strategy — if rationing drives informal payments, the policy fix is supply-side (more facilities, staff), not demand-side (more enrollment).

| Novelty | Feasibility | Impact | **Total** |
|---|---|---|---|
| 4 | 5 | 5 | **4.6** |

---

### IDEA 2 — Indigenous–Mestizo Health Spending Gap: Oaxaca-Blinder Decomposition
**Sub-topic:** Health disparities by ethnicity

**Research Question:** How much of the out-of-pocket health expenditure gap between indigenous and non-indigenous households is explained by endowment differences (income, education, geography) vs. unexplained structural factors (discrimination, cultural distance from formal system)?

**Method:** Oaxaca-Blinder decomposition of log OOP health expenditure. Estimate separate OLS models for indigenous and non-indigenous households, then decompose the gap into: (a) endowment component — characteristics differ; (b) coefficient component — returns to characteristics differ; (c) interaction. Use twofold and threefold specifications.

**Data:** ENAHO user dataset (contains self-reported ethnic identification P300-series, health expenditure, socioeconomic module)

**Why novel:** Zero OB decompositions exist for health spending in Peru by ethnicity. The literature uses indigenous as a control variable — never as the group of interest for structural decomposition.

**Why impactful:** Distinguishes policy levers: endowment gaps call for poverty reduction; coefficient gaps call for anti-discrimination and culturally adapted care.

| Novelty | Feasibility | Impact | **Total** |
|---|---|---|---|
| 5 | 4 | 4 | **4.4** |

---

### IDEA 3 — Altitude Threshold and Depression: Geographic Regression Discontinuity
**Sub-topic:** Mental health & altitude

**Research Question:** Is there a causal discontinuity in screened depression prevalence at the 1,500 m.a.s.l. threshold, consistent with chronic hypoxic stress as a biological pathway distinct from socioeconomic confounders?

**Method:** Sharp RDD using altitude (in meters) as the continuous running variable with a cutoff at 1,500 m.a.s.l. (as used in seed paper). UBIGEO-district altitude centroids linked to survey respondents. Bandwidth selection via MSE-optimal procedure (Calonico-Cattaneo-Titiunik). Falsification: test alternative arbitrary thresholds (e.g., 500 m, 2,500 m) for placebo discontinuities.

**Data:** ENAHO user dataset + INEI district altitude centroids (public); or ENDES if PHQ-9 available

**Why novel:** Zegarra-Rodríguez (2022) documents gradient but never tests for a discontinuity. RDD is the first quasi-experimental design applied to the altitude-mental health question in Peru.

**Why impactful:** If discontinuity exists at a physiologically meaningful threshold, it implicates hypoxia-driven mechanisms and suggests oxygen supplementation or targeted mental health programs for high-altitude districts.

| Novelty | Feasibility | Impact | **Total** |
|---|---|---|---|
| 5 | 3 | 4 | **4.1** |

---

### IDEA 4 — Who Bears Catastrophic Health Expenditure? Quantile Regression Analysis
**Sub-topic:** Catastrophic health expenditure & poverty traps

**Research Question:** Do the determinants of health expenditure differ across the expenditure distribution, with middle-income households bearing disproportionate catastrophic burden relative to the poorest (who avoid care) and the wealthiest (who can absorb shocks)?

**Method:** Quantile regression at τ = 0.25, 0.50, 0.75, 0.90, 0.95 of total household health expenditure. Compare coefficient vectors across quantiles using interquantile range tests. Key predictors: insurance type, facility type, chronic disease, household income quintile, urban/rural.

**Data:** ENAHO user dataset (full household health and expenditure modules)

**Why novel:** All Peruvian health expenditure studies use OLS/logit. Quantile regression reveals the entire conditional distribution — nobody has shown that the *middle quintile* faces the steepest marginal expenditure from insurance gaps.

**Why impactful:** Catastrophic expenditure thresholds (WHO: >10%, >25% of capacity to pay) affect middle-income households most — this reshapes targeting of subsidized insurance programs.

| Novelty | Feasibility | Impact | **Total** |
|---|---|---|---|
| 4 | 5 | 4 | **4.3** |

---

### IDEA 5 — Double Burden of Malnutrition and Proximity to Processed Food Markets
**Sub-topic:** Nutrition & food environment

**Research Question:** Does district-level density of processed food retail outlets causally increase adult overweight/obesity in peri-urban Peru, controlling for income and child undernutrition co-existence?

**Method:** IV estimation using municipality-level road network connectivity as an instrument for processed food retail density (roads lower distribution costs, driving market entry, but have no direct nutritional effect conditional on income). First stage: road density → processed food outlet density. Second stage: outlet density → BMI and DBM prevalence.

**Data:** ENAHO user dataset + INEI economic census (food establishments) + MTC road network data

**Why novel:** Pradeilles (2023) treats food environment as background. No IV study in Peru uses road connectivity to identify food market effects on DBM.

| Novelty | Feasibility | Impact | **Total** |
|---|---|---|---|
| 4 | 3 | 4 | **3.7** |

---

### IDEA 6 — Chronic Disease Diagnosis and Labor Force Exit: IV Estimation
**Sub-topic:** Health–labor market linkages

**Research Question:** Does receiving a chronic disease diagnosis (hypertension, diabetes, asthma) causally reduce labor force participation and weekly hours worked, and is this effect larger for informal workers who lack sick leave?

**Method:** IV using family history of the same condition as instrument for own diagnosis (family history predicts diagnosis probability via genetic transmission, but affects labor supply only through own health). Separate 2SLS models by formality status.

**Data:** ENAHO user dataset (contains self-reported chronic disease, family health history, employment variables)

**Why novel:** Chronic disease–labor market studies in Peru rely on OLS with reverse causality. No IV study uses family history as instrument in a Peruvian health-labor context.

| Novelty | Feasibility | Impact | **Total** |
|---|---|---|---|
| 4 | 4 | 4 | **4.0** |

---

### IDEA 7 — Traditional Medicine Use and Formal Preventive Care: CEM Matching
**Sub-topic:** Health-seeking behavior & traditional medicine

**Research Question:** Does reliance on traditional healers (*curanderos*, *parteras*) as primary care substitute crowd out formal preventive service uptake (vaccinations, prenatal visits, cancer screening)?

**Method:** Coarsened Exact Matching (CEM) on demographic and socioeconomic covariates, comparing households that reported traditional healer use vs. those using formal care. Outcome: binary indicators for each preventive service. Assess balance and estimate ATT.

**Data:** ENAHO user dataset (P400-series includes informal/traditional care queries)

**Why novel:** Existing studies describe traditional medicine use descriptively. No matching study tests the substitution vs. complementarity hypothesis for preventive care in Peru.

| Novelty | Feasibility | Impact | **Total** |
|---|---|---|---|
| 4 | 4 | 3 | **3.7** |

---

### IDEA 8 — Facility Type Selection and Health Outcomes: Heckman Selection
**Sub-topic:** Health system quality & facility choice

**Research Question:** After correcting for non-random selection into MINSA vs. EsSalud vs. private facilities, do facility types produce different self-reported health outcomes and treatment satisfaction?

**Method:** Heckman selection model. Selection equation: facility type chosen as function of insurance, distance, income (exclusion: distance to each facility type as instrument). Outcome: self-reported health improvement, treatment days, referral rate.

**Data:** ENAHO user dataset

**Why novel:** Facility-type comparisons in Peru ignore the fact that healthier, higher-income patients self-select into private care — OLS estimates are severely biased upward for private facilities.

| Novelty | Feasibility | Impact | **Total** |
|---|---|---|---|
| 4 | 4 | 4 | **4.0** |

---

### IDEA 9 — Social Capital and Mental Health: PSM Analysis
**Sub-topic:** Social determinants of mental health

**Research Question:** Does community social capital (measured via institutional trust and neighborhood participation) independently predict lower mental health burden after PSM on income, education, and chronic disease?

**Method:** Propensity Score Matching. Treatment: high vs. low social capital (constructed composite from ENAHO trust and participation variables). Outcome: mental health module responses. Kernel and nearest-neighbor matching; sensitivity analysis via Rosenbaum bounds.

**Data:** ENAHO user dataset

| Novelty | Feasibility | Impact | **Total** |
|---|---|---|---|
| 4 | 4 | 3 | **3.7** |

---

### IDEA 10 — Distance to Health Facility and Maternal Care Utilization: IV
**Sub-topic:** Maternal & reproductive health

**Research Question:** Does travel distance to the nearest public health facility causally reduce skilled birth attendance and antenatal care visits among rural women?

**Method:** IV using distance to nearest MINSA establishment as instrument for utilization (distance affects access but not health demand directly, conditional on district income). Merge ENAHO UBIGEO codes with MINSA RENIPRESS facility coordinates for distance computation.

**Data:** ENAHO user dataset + MINSA RENIPRESS public facility registry (open data)

**Why novel:** Distance-IV studies in Peru focus on urban or aggregate outcomes. No study instruments facility utilization specifically for maternal care in the context of Peru's rural altitude-geography interaction.

| Novelty | Feasibility | Impact | **Total** |
|---|---|---|---|
| 3 | 3 | 5 | **3.6** |

---

## PART 3: Full Elaboration of Top 3 Ideas

---

### RANK 1 — The SIS Paradox: Heckman Selection and Informal Payments
*(Sub-topic: Health insurance & informal payments — Score: 4.6)*

**The core insight:** The seed paper by Espinoza-Pajuelo et al. (2024) shows that SIS beneficiaries — who should pay nothing — report *more* informal payment exposure than uninsured patients. But this is raw correlation. SIS enrollment is endogenous: healthier, lower-income households in well-served districts select into SIS. Conversely, areas with poor public supply may push people *into* informal payments regardless of insurance status. Without correcting for this selection, the SIS-informal payment association could run in either direction causally.

**Identification strategy:**
- **Stage 1 (selection into SIS):** Regress SIS enrollment on individual characteristics + district SIS penetration rate as exclusion restriction. District penetration captures local enrollment push campaigns and health post density but does not directly affect individual informal payment probability.
- **Stage 2 (informal payment probability conditional on SIS):** Model informal payment exposure as a function of insurance type, facility type, and the inverse Mills ratio from Stage 1.
- **Heterogeneity:** Interact SIS status with facility density quartile — if rationing is the mechanism, the SIS effect should be largest in districts with fewest MINSA establishments per capita.
- **Robustness:** Replicate using indirect expenditure indicators (P401-series "unexpected health costs") rather than direct informal payment admission (which the seed paper shows is suppressed by reporting bias).

**Policy relevance:** Peru's MEF and MINSA are currently evaluating SIS capitation reform (2024–2026). If supply rationing — not enrollment failure — drives the informal payment paradox, expanding enrollment without expanding supply will worsen the problem.

**Week 1 tasks:** (a) Map ENAHO health module variables to SIS enrollment (P400A-series), facility type (P401D-series), and informal payment indicators; (b) merge district SIS penetration rates from SIS administrative registry (public, SUSALUD); (c) estimate selection model and report Mills ratio significance.

---

### RANK 2 — Decomposing the Indigenous Health Spending Gap
*(Sub-topic: Health disparities by ethnicity — Score: 4.4)*

**The core insight:** Peru has one of Latin America's most ethnically stratified health systems. Quechua and Aymara speakers face documented barriers: geographic distance, cultural non-concordance, and language gaps with providers. Yet every study treating ethnicity as a *control* variable fails to answer the policy-critical question: *how much of the spending gap is fixable by income redistribution, and how much requires structural change in the health system?* Oaxaca-Blinder is the tool built precisely for this decomposition.

**Identification strategy:**
- **Group definition:** Indigenous = self-reported Quechua/Aymara mother tongue or ethnic self-identification (ENAHO has both, use intersection for robustness). Non-indigenous = Spanish mother tongue, mestizo self-identification.
- **Outcome:** Log per-capita household out-of-pocket health expenditure (winsorized at 99th percentile to handle outliers).
- **Decomposition:** Twofold Oaxaca-Blinder: endowment component (what if indigenous households had non-indigenous characteristics?) vs. coefficient component (what if they received same returns to characteristics?). Threefold extension separates the interaction.
- **Key covariates:** Income quintile, education, urban/rural, region (sierra/selva/costa), chronic disease burden, insurance type, household size.
- **Extensions:** (a) Reweighted Oaxaca-Blinder (Fortin-Lemieux-Firpo) to account for common support violations; (b) decompose at the 75th and 90th percentile using quantile Oaxaca-Blinder to test if the gap is driven by catastrophic expenditure episodes.

**Policy relevance:** If the coefficient component dominates, income transfers alone won't close the gap — Peru needs intercultural health services, interpreter programs, and geographic reallocation of EIS (Equipos Itinerantes de Salud). This gives MIDIS and MINSA specific, evidence-based leverage points.

**Week 1 tasks:** (a) Construct indigenous/non-indigenous binary from ENAHO ethnicity and mother tongue variables; (b) calculate log OOP expenditure and verify distribution; (c) run twofold OB baseline with 95% CI bootstrap on decomposition components.

---

### RANK 3 — Catastrophic Expenditure Across the Distribution: Quantile Regression
*(Sub-topic: Catastrophic health expenditure & poverty traps — Score: 4.3)*

**The core insight:** The standard approach to catastrophic health expenditure (CHE) uses a binary threshold — households either cross 10% or 25% of capacity to pay, or they don't. This collapses enormous distributional information. The quantile regression approach asks: *across the entire distribution of health spending, where does the gradient of socioeconomic determinants change most sharply?* The hypothesis is a classic middle-income squeeze: the poorest avoid care (low spending), the wealthiest absorb costs (high spending without catastrophe), and middle-income households face the steepest marginal exposure from coverage gaps.

**Identification strategy:**
- **Outcome:** Total household health expenditure as share of non-food consumption (capacity-to-pay definition, WHO standard).
- **Quantile specification:** QR at τ = 0.10, 0.25, 0.50, 0.75, 0.90, 0.95. Plot coefficient paths across τ for key predictors.
- **Key predictors:** Insurance type (SIS, EsSalud, private, uninsured), chronic disease count, facility type used, urban/rural, income decile, household dependency ratio, geographic region.
- **Hypothesis tests:** Wald tests for equality of coefficients across quantiles (e.g., β_SIS at τ=0.90 vs. τ=0.25). This tests whether insurance protection is larger at the tails.
- **Extensions:** (a) Unconditional quantile regression (RIF-regression, Firpo-Fortin-Lemieux) to estimate effects on the *unconditional* expenditure distribution; (b) separate regressions by urban/rural to test if the distribution shape differs structurally.

**Policy relevance:** Universal Health Coverage (Cobertura Universal de Salud, Law 29344) targets the uninsured, but QR may reveal that the near-poor with partial SIS coverage face the highest marginal catastrophe risk — an invisible population in current policy design. This directly informs MEF's CHE monitoring indicators.

**Week 1 tasks:** (a) Construct capacity-to-pay denominator from ENAHO household consumption module; (b) estimate OLS baseline for comparison; (c) run QR at 7 quantiles, extract coefficient matrix and plot coefficient paths for insurance type dummies.

---

## PART 4: JSON Output

```json
{
  "top_ideas": [
    {
      "rank": 1,
      "title": "The SIS Paradox: Selection-Corrected Estimation of Informal Payment Exposure Among Public Insurance Beneficiaries",
      "research_question": "Does SIS enrollment causally increase informal health payment exposure through supply-side rationing at MINSA facilities, and is this effect heterogeneous by local health facility density?",
      "method": "Heckman selection model (two-stage: SIS enrollment selection + informal payment outcome), with district SIS penetration rate as exclusion restriction",
      "sub_topic": "health_insurance_informal_payments",
      "data_sources": ["ENAHO user dataset (P400–P401 health module)", "SUSALUD district SIS enrollment registry (public)"],
      "novelty": 4,
      "feasibility": 5,
      "impact": 5,
      "total_score": 4.6,
      "pitch": "SIS beneficiaries should pay zero, yet they report more informal payments than the uninsured — a paradox the literature notes but cannot explain causally. A Heckman selection model corrects for the endogeneity of SIS enrollment and tests whether supply rationing (too few facilities per enrollee) is the driver. This directly challenges MEF and MINSA's assumption that expanding enrollment is sufficient to eliminate informal payments.",
      "first_experiment": "Map ENAHO health module variables to SIS enrollment indicator, facility type used, and informal payment proxies (P401-series unexpected costs). Merge district SIS penetration rates from SUSALUD. Run probit selection equation and test exclusion restriction via first-stage F-statistic. Report Mills ratio significance in the outcome equation."
    },
    {
      "rank": 2,
      "title": "How Much Is Structure? Oaxaca-Blinder Decomposition of the Indigenous–Mestizo Out-of-Pocket Health Spending Gap",
      "research_question": "How much of the out-of-pocket health expenditure gap between indigenous and non-indigenous Peruvian households is explained by endowment differences versus structural coefficient differences reflecting discrimination and cultural distance from formal healthcare?",
      "method": "Twofold and threefold Oaxaca-Blinder decomposition of log per-capita OOP health expenditure, with bootstrap confidence intervals on decomposition components",
      "sub_topic": "health_disparities_ethnicity",
      "data_sources": ["ENAHO user dataset (ethnicity self-identification, mother tongue variables, health expenditure module)"],
      "novelty": 5,
      "feasibility": 4,
      "impact": 4,
      "total_score": 4.4,
      "pitch": "Every study on indigenous health in Peru uses ethnicity as a control variable, never asking what fraction of the spending gap is fixable by income redistribution versus structural reform. Oaxaca-Blinder decomposition answers this precisely. If coefficient differences dominate endowments, Peru's intercultural health policy (EIS teams, bilingual providers) has an evidence base; if endowments dominate, the leverage point shifts to poverty reduction programs.",
      "first_experiment": "Construct indigenous/non-indigenous binary using self-reported ethnic identity and mother tongue (ENAHO). Calculate log per-capita household OOP health expenditure winsorized at 99th percentile. Run OLS models for each group on income, education, region, insurance, chronic disease. Compute twofold OB decomposition and bootstrap 1000 replications for SE on endowment and coefficient components."
    },
    {
      "rank": 3,
      "title": "The Middle-Income Squeeze: Quantile Regression Analysis of Catastrophic Health Expenditure Determinants Across Peru",
      "research_question": "Do socioeconomic and insurance-related determinants of health expenditure vary systematically across the conditional expenditure distribution, with middle-income households facing disproportionate catastrophic exposure relative to the poorest (who avoid care) and the wealthiest (who absorb shocks)?",
      "method": "Quantile regression at τ = 0.10, 0.25, 0.50, 0.75, 0.90, 0.95 of health expenditure share of capacity-to-pay; Wald tests for coefficient equality across quantiles; RIF unconditional quantile regression extension",
      "sub_topic": "catastrophic_health_expenditure",
      "data_sources": ["ENAHO user dataset (health expenditure + household consumption modules for capacity-to-pay denominator)"],
      "novelty": 4,
      "feasibility": 5,
      "impact": 4,
      "total_score": 4.3,
      "pitch": "Peru's catastrophic health expenditure research uses binary thresholds that hide the distribution. Quantile regression reveals that the same covariate (e.g., SIS insurance, chronic disease, urban residence) has radically different effects at different points of the spending distribution. The middle-income squeeze hypothesis — that near-poor households with partial SIS coverage face the steepest marginal catastrophe risk — has direct implications for how MEF targets CUS monitoring and subsidy design.",
      "first_experiment": "Construct capacity-to-pay denominator (total consumption minus food expenditure) from ENAHO consumption module. Compute health expenditure share. Run OLS baseline then quantile regression at 6 quantiles. Plot coefficient path for insurance type dummies (SIS, EsSalud, uninsured) across quantiles. Test null of coefficient equality at τ=0.25 vs. τ=0.90 using Wald test."
    }
  ]
}
```