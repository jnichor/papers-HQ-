# EVALUATION

---

## 1. Research Question Clarity — 7/10

The question is reasonably specific: it identifies the outcome (informality), the treatment source (sectoral teleworkability/COVID exposure), the population (Peruvian workers), the time window (2020–2024), and heterogeneity dimensions (firm size, gender, region). The panel + event-study framing gives it a clear temporal structure.

Deductions:
- "More persistent" is undefined — persistent relative to what benchmark? Complete recovery by 2024? A pre-COVID informality rate?
- The question conflates two distinct causal claims: (a) COVID caused differential informality by sector, and (b) recovery paths vary by firm size/gender/region. These could and probably should be separate estimands.
- The counterfactual is implicit. Workers in high-teleworkability sectors are the control group, but this is never stated.

---

## 2. Identification Strategy — 5/10

**Design logic**: TWFE event study with individual and year fixed effects, using the Dingel-Neiman teleworkability score as a continuous measure of differential COVID exposure. Pre-trends are testable via year × teleworkability interaction coefficients.

**Strengths**:
- Individual FEs absorb time-invariant selection into high vs. low teleworkability sectors.
- Continuous treatment avoids the binary treatment heterogeneity critique of standard DiD.
- Pre-trend testability is a genuine virtue.

**Critical weaknesses**:

**Structural confounding in pre-trends (HIGH)**: Low-teleworkability sectors (hospitality, retail, construction, domestic services) in Peru were already structurally more informal before COVID. The parallel trends assumption requires that absent COVID, informality trends in low- and high-teleworkability sectors would have evolved identically. This is implausible: contact-intensive sectors have endogenously different formality dynamics tied to seasonality, enforcement access, and firm-size composition — all pre-existing conditions. The event study will show pre-trend divergence that may be secular, not COVID-induced.

**Teleworkability as treatment validity**: The Dingel-Neiman index was constructed from US O*NET task data. In Peru, occupational task content differs substantially, particularly in agriculture, informal services, and artisanal manufacturing. The mapping to CIIU 4-digit codes compounds measurement error. No Peru-specific validation is proposed.

**Sector-switching endogeneity**: Individual FEs absorb time-invariant sector assignment, but workers displaced from low-teleworkability jobs may have moved to different sectors post-shock. If sector switches are endogenous to the COVID treatment, the treatment variable becomes time-varying and the FE absorbs only the baseline sector — a specification mismatch.

**Clustering**: SE clustering at the individual level is unusual and potentially anti-conservative; variation in the teleworkability score comes from the sector level (CIIU 2-digit), so clustering at that level would be more appropriate and yields fewer clusters.

**Missing TWFE staggered correction discussion**: While the treatment here is not staggered in the conventional DiD sense (it's a continuous score × year interaction), the proposal should acknowledge whether Callaway-Sant'Anna or Roth-Sant'Anna heterogeneous effects corrections apply and argue why they do or do not.

---

## 3. Data Feasibility — 6/10

**Strengths**:
- ENAHO panel component exists and covers 2020–2024 in principle.
- Dingel-Neiman teleworkability scores are open-access.
- CIIU occupation codes in ENAHO (p507 variants) are well-documented.

**Weaknesses**:
- **Panel retention**: ENAHO uses a rotating panel design, not a full longitudinal cohort. The fraction of individuals tracked across all five annual waves (2020–2024) is substantially smaller than the cross-sectional sample. The proposal states "5-wave structure" as though the full sample is tracked — this needs verification. With rotating panels, individual FEs are identified only for the sub-sample with ≥2 observations, reducing power sharply for event studies requiring 5+ periods.
- **Attrition non-randomness**: Informal workers, migrants, and workers who changed housing due to COVID are systematically harder to re-contact. This attrition is correlated with the outcome, biasing panel estimates downward in measured informality.
- **Dingel-Neiman → Peru CIIU mapping**: US SOC → CIIU 4-digit crosswalk requires intermediate steps and introduces classification error. The proposal says "4-digit CIIU" but then describes running regressions at "2-digit CIIU" — this inconsistency suggests the matching has not yet been attempted.
- No power calculation is presented for the heterogeneity analysis (firm size × gender × region cells will be small).

---

## 4. Novelty & Contribution — 5/10

The framing as the "worker-side complement" to Bosch et al. (2025) is a reasonable positioning strategy but overstates uniqueness. The COVID + teleworkability + informality combination has been applied to other Latin American contexts (Brazil, Mexico, Colombia) and several working papers exist on Peru's COVID labor market. The novelty claim rests on:

1. The 5-year recovery arc (genuine value if ENAHO panel retention allows it).
2. Hysteresis framing (interesting but needs a formal definition).
3. The Bosch et al. complementarity (enforcement supply-side ↔ this paper's demand/worker-side).

However, the methodology is standard TWFE event study applied to a well-known teleworkability instrument on a frequently used dataset. The heterogeneity analysis (gender, region, firm size) is descriptively valuable but not methodologically novel. The contribution is primarily empirical-contextual (Peru-specific evidence on a documented phenomenon), which has real value but is incremental rather than transformative.

---

## 5. Policy Relevance / Impact — 7/10

High relevance: Peru's informality rate (~70%) and active SUNAFIL enforcement context make this directly actionable. Documenting hysteresis would motivate targeted reintegration programs; documenting full recovery would validate current policy trajectories. The gender and regional dimensions connect to MIDIS social protection targeting. The Bosch et al. linkage gives a natural policy audience (SUNAFIL, MTPE). Effect sizes likely to be large enough to be economically meaningful given the scale of the COVID shock.

Minor deductions: The paper does not frame a specific policy decision it would inform, and hysteresis findings in labor markets are well-known outside Peru — the policy contribution depends on generating Peru-specific magnitudes, not on establishing the phenomenon.

---

## 6. Threats to Validity

| # | Threat | Severity | Addressed? |
|---|--------|----------|------------|
| 1 | **Pre-existing differential informality trends by sector**: Low-teleworkability sectors were already on distinct formality trajectories pre-COVID, violating parallel trends. | **HIGH** | No — pre-trend tests are planned but will not distinguish COVID-induced divergence from secular sectoral trends beginning before 2020. Need 2017–2019 ENAHO waves. |
| 2 | **Panel attrition correlated with informality**: Informal, mobile, and COVID-displaced workers are systematically lost from the panel, biasing measured informality downward and formality recovery upward. | **HIGH** | Not addressed. No attrition analysis or inverse-probability weighting proposed. |
| 3 | **Dingel-Neiman index measurement error for Peru**: US task-based teleworkability may misclassify Peruvian occupations, particularly in agriculture, informal trade, and artisanal work. Random measurement error attenuates estimates toward zero; systematic error could bias direction. | **MEDIUM** | Not addressed. No Peru-specific validation or robustness to alternative classification proposed. |
| 4 | **Endogenous sector switching post-shock**: Workers who lost formal employment may switch sectors, making the baseline teleworkability score an increasingly noisy measure of actual exposure over 2021–2024. | **MEDIUM** | Partially — individual FEs absorb baseline, but not the dynamic selection problem. |
| 5 | **SUTVA violation via informal sector absorption**: Workers displaced from formal contact-intensive jobs may crowd informal employment in high-teleworkability sectors, creating general equilibrium spillovers that contaminate the control group. | **LOW** | Not discussed. |

**Threats_addressed** = 10 − (2 HIGH unaddressed × 2) = **6**

---

## 7. Missing Elements

- **Pre-2020 ENAHO waves**: Without 2017–2019 data, pre-trend tests only cover the COVID window and cannot distinguish secular from shock-induced divergence.
- **Informality definition**: INEI uses at least three definitions (contributory social security, labor code compliance, firm-size proxy). The choice matters substantially for results and is unspecified.
- **Panel retention statistics**: What fraction of 2020 respondents are observed in 2021, 2022, 2023, 2024? This determines feasibility of the entire design.
- **Regional variation in mobility restrictions**: Peru's mobility restrictions varied by region and were re-imposed multiple times through 2021. This within-country variation could serve as an alternative or complementary identification source but is not exploited.
- **Hysteresis definition**: What functional form or test operationalizes "informality hysteresis"? A state-dependence test (Markov transition) would be more precise than a simple non-recovery reading.
- **Power for heterogeneity analysis**: Firm size × gender × region cells will be small in a rotating panel; no minimum detectable effect analysis.

---

## Composite Score Calculation

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|---------|
| Research Question | 7 | 0.15 | 1.05 |
| Identification | 5 | 0.30 | 1.50 |
| Data Feasibility | 6 | 0.20 | 1.20 |
| Novelty | 5 | 0.15 | 0.75 |
| Impact | 7 | 0.10 | 0.70 |
| Threats Addressed | 6 | 0.10 | 0.60 |
| **Composite** | | | **5.80** |

---

```json
{
  "question_score": 7,
  "identification_score": 5,
  "data_score": 6,
  "novelty_score": 5,
  "impact_score": 7,
  "threats_addressed_score": 6,
  "composite_score": 5.80,
  "top_threats": [
    "pre-existing differential informality trends by sector (parallel trends violation)",
    "panel attrition correlated with informality outcomes",
    "Dingel-Neiman teleworkability index validity for Peru"
  ],
  "verdict": "NEEDS_WORK",
  "one_line_summary": "A policy-relevant and well-framed question undermined by an undefended parallel trends assumption, likely panel attrition bias, and an instrument whose validity for Peru is unverified — all fixable with pre-2020 waves, attrition analysis, and Peru-specific teleworkability validation."
}
```

---

---

# META-REVIEW

## Fairness

The evaluation gives genuine credit where deserved: the event-study pre-trend testability is acknowledged, the policy relevance score (7/10) is not punished for identification problems, and the research question score (7/10) is not penalized for data concerns. The identification score (5/10) is the sharpest deduction, which is appropriate given that parallel trends is load-bearing for the entire design and the proposal provides no defense of it.

The score could be viewed as slightly harsh on novelty (5/10), given that the Bosch et al. complementarity framing is genuinely clever and the 5-year recovery arc is not standard in this literature. A 6/10 would also be defensible. However, 5/10 is within the reasonable range.

## Consistency

Narrative and scores align:
- Identification narrative highlights two high-severity unaddressed threats → 5/10 is consistent.
- Data narrative identifies ENAHO panel retention, attrition, and matching concerns → 6/10 is consistent (not a fatal flaw but non-trivial).
- Novelty narrative describes incremental, contextually valuable contribution → 5/10 is consistent.
- No inflation: the evaluator does not praise the design effusively and then score it 8/10.

## Completeness

The evaluation identifies the five most important threats. One modest gap: the evaluation does not explicitly flag the **composition effect** — if COVID caused worker transitions from formal employment to inactivity (not informality), the informality indicator may understate total labor market damage and the recovery metric may conflate return-to-formality with return-to-employment. This is related to the Herrera & Rosas (2003) cited paper, which specifically documents employment-inactivity flows as dominant in Peru, making this omission somewhat notable given that the proposal itself cites that paper. This is a medium-severity miss but not a fatal one.

The evaluation also does not mention that the **Bosch et al. (2025)** enforcement-letter RCT covers the same 2020–2024 window and same SUNAFIL context, which could create spillover contamination if treated firms also employed workers who appear in the ENAHO panel — though this is admittedly speculative.

## Constructiveness

The criticisms are specific and actionable:
- "Add 2017–2019 ENAHO waves" is concrete.
- "Conduct attrition analysis / IPW" is standard and implementable.
- "Peru-specific teleworkability validation" is a clear task.
- "Define informality measure" is a minimal fix.

The researcher can address at least three of the five threats without a fundamental redesign.

---

**AGREE**

The evaluation is internally consistent, appropriately calibrated (neither a rubber stamp nor an unreasonably harsh rejection), correctly identifies the structural weakness in the identification strategy as the dominant concern, and provides actionable guidance. The minor gaps (composition/inactivity flows, potential Bosch et al. spillover) are not severe enough to change any score materially.