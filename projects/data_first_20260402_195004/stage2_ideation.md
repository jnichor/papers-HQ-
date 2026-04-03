## Research Ideation: Civilian Casualty Framing & ICC Referral Support

### Dataset Reading

This is a **randomized survey experiment** — the treatment columns (`apartheid_treatment`, `apartheid_vs_persecution_treat`, `foreign_aid`, etc.) are randomly assigned conditions. This is critical: **identification is Level A (ID=5) for all treatment-based designs**. The "cross-section" limitation is by design, not a flaw. The allowed methods (IV, matching, quantile regression, OLS) are all appropriate — and OLS with random treatment assignment is Tier 1 (RCT).

---

## State of the Literature

**Key themes in civilian casualty framing research:**
- Moral distance and in-group/out-group framing affects war crime attribution (Sikkink 2011; Krain 2012)
- Legal frames (genocide, apartheid, ethnic cleansing) increase legitimacy of external intervention — but backfire with partisan audiences (Tomz & Weeks 2013; Chapman & Reiter 2004)
- ICC referral support is shaped by humanitarian vs. geopolitical priming (Kelley 2007; Bosco 2014)
- Framing civilian casualties as "collateral damage" vs. "targeted" shifts blame attribution (Gartner & Segura 1998)
- Pro-Israel predispositions act as a prior that is robust to weak frames but movable by strong legal ones (Tessler 2003)

**Key gaps:**
1. No study has experimentally compared *legally-specific* frames (apartheid vs. persecution) on ICC support
2. Partisan heterogeneity in legal frame receptivity is understudied
3. Sexism scales have never been used to moderate atrocity framing effects
4. Foreign aid conditionality as a mechanism for casualty salience — unexplored
5. Racial identity as moderator of conflict framing (Black Lives Matter analogy effects) — no experimental work

---

## 8-10 Research Ideas

---

### Idea 1 — **Apartheid vs. Persecution Frame: Legal Label Effects on ICC Referral Support**
**Sub-topic: Legal Framing Precision**
**RQ:** Does labeling Israeli actions as "apartheid" vs. "persecution" differentially increase support for ICC referral, holding casualty salience constant?

**Method:** OLS with treatment dummy `apartheid_vs_persecution_treat`, controls for demographics and `pro_israel_score`. LASSO for covariate selection. **Tier 1 (RCT). Level A.**
- Source of variation: Random assignment to apartheid vs. persecution label
- Pre-treatment periods: N/A (cross-section by design)
- Parallel trends: N/A
- Clusters: Randomization at individual level, 1,185 units
- Threats: Differential attrition by condition — check balance

**Data needed:** Survey already contains this.
**Novel:** "Apartheid" carries specific legal weight under international law; no prior experiment tests this specific contrast against "persecution."
**Impact:** Directly informs advocacy strategy for ICC referral campaigns.

| N | F | I | ID | Total |
|---|---|---|----|-------|
| 5 | 5 | 5 | 5  | **5.0** |

---

### Idea 2 — **Partisan Asymmetry in Legal Frame Receptivity**
**Sub-topic: Political Polarization & International Law**
**RQ:** Do Democrats and Republicans diverge in ICC referral support in response to apartheid framing, and does this gap widen with stronger legal frames?

**Method:** RCT with heterogeneous treatment effects (HTE): OLS with `apartheid_treatment × stronger_republican_8pt` interaction. Causal Forest (GRF) to estimate CATEs across partisan spectrum. **Tier 1 (RCT + HTE). Level A.**
- Source: Random assignment; partisan score is pre-determined
- N~1,185 with continuous 8-point partisan scale — adequate power for HTE
- Threats: Partisan identity may be endogenous to Israel attitudes — partial concern

**Data needed:** Already present.
**Novel:** Prior work uses observational data. This is the first clean experimental estimate of partisan framing asymmetry on ICC support.
**Impact:** High — informs whether bipartisan ICC support is achievable via frame choice.

| N | F | I | ID | Total |
|---|---|---|----|-------|
| 4 | 5 | 5 | 5  | **4.8** |

---

### Idea 3 — **Hostile Sexism and Civilian Casualty Desensitization**
**Sub-topic: Psychological Predispositions & Atrocity Response**
**RQ:** Do respondents high in hostile sexism discount civilian casualties involving women, and does apartheid framing moderate this discounting?

**Method:** OLS with `hostile_sexism_agg × apartheid_treatment` interaction on ICC support / casualty concern outcomes. Quantile regression to check if effects concentrate at tails of sexism distribution. **Tier 1 (RCT). Level A.**
- Source: Random assignment; `hostile_sexism_agg` is pre-measured
- Novel design: Sexism scale as moderator, not outcome
- Threats: Measurement error in self-reported sexism (likely attenuates, won't confound)

**Data needed:** Already present.
**Novel:** No prior paper has linked ambivalent sexism theory to international humanitarian law opinion. Bridges social psychology and IR.
**Impact:** Moderate-high — explains variation in public support for protection-of-civilians norms.

| N | F | I | ID | Total |
|---|---|---|----|-------|
| 5 | 5 | 4 | 5  | **4.8** |

---

### Idea 4 — **Foreign Aid Conditionality as a Casualty Salience Mechanism**
**Sub-topic: Foreign Policy Linkage & Public Opinion**
**RQ:** Does framing civilian casualties in terms of US foreign aid conditionality increase support for ICC referral more than a pure humanitarian frame?

**Method:** OLS comparing `foreign_aid` treatment arm vs. control on ICC support and rank outcomes. Mediation analysis: does `pro_israel_score` mediate the foreign aid effect? **Tier 1 (RCT). Level A.**
- Source: Random assignment to foreign aid frame
- Mechanism test: Causal mediation (Imai et al. 2010)
- Threats: Mediation assumptions (sequential ignorability) — flag clearly

**Data needed:** Present.
**Novel:** Foreign aid conditionality frames are used by legislators but untested on public opinion formation for ICC.
**Impact:** High policy relevance — this is the actual Senate debate happening now.

| N | F | I | ID | Total |
|---|---|---|----|-------|
| 4 | 5 | 5 | 5  | **4.8** |

---

### Idea 5 — **Pro-Israel Prior as Bayesian Resistance to Legal Frames**
**Sub-topic: Prior Beliefs & Frame Persuasion**
**RQ:** Is the apartheid framing effect on ICC support attenuated by pre-existing pro-Israel attitudes, and is there a threshold beyond which frames cannot move opinion?

**Method:** OLS with `apartheid_treatment × pro_israel_score` interaction. Quantile treatment effects to identify whether effects are null only at the top of the pro-Israel distribution. RDD on `pro_israel_score` if there's a natural break. **Tier 1 (RCT). Level A.**
- Source: Random assignment; `pro_israel_score` pre-determined
- Threats: `pro_israel_score` may be correlated with partisanship — partial collinearity, not confounding

**Data needed:** Present.
**Novel:** Bayesian updating models of persuasion rarely tested with legal/atrocity frames.
**Impact:** Important for understanding who is genuinely reachable.

| N | F | I | ID | Total |
|---|---|---|----|-------|
| 4 | 5 | 4 | 5  | **4.6** |

---

### Idea 6 — **Race, Solidarity, and Cross-Conflict Identification**
**Sub-topic: Racial Identity & International Conflict Framing**
**RQ:** Do Black respondents show greater ICC referral support after civilian casualty framing (via cross-racial solidarity mechanism), and does apartheid framing amplify this gap?

**Method:** Oaxaca-Blinder decomposition of Black-white gap in ICC support, plus RCT interaction `apartheid_treatment × black`. **Tier 1 (RCT). Level A** for treatment effect; **Tier 4** for Oaxaca component — report both clearly.
- Source: Random assignment for interaction; race is pre-determined
- Threats: Small N for Black subsample — report power

**Data needed:** Present (`black`, `white` dummies).
**Novel:** "Apartheid" label carries specific historical resonance for Black Americans — no paper has tested this differential framing effect.
**Impact:** High — explains demographic variation in BDS/ICC public support.

| N | F | I | ID | Total |
|---|---|---|----|-------|
| 5 | 4 | 5 | 5  | **4.8** |

---

### Idea 7 — **Ranking Experiments: Which Attributes of Civilian Harm Drive ICC Support Most?**
**Sub-topic: Conjoint/Attribute Weighting in Atrocity Response**
**RQ:** Among attributes of civilian harm narratives (scale, intentionality, legal label, perpetrator identity), which has the largest effect on ICC referral support?

**Method:** If `rank_1–rank_4` are from a ranking/conjoint task, estimate Average Marginal Component Effects (AMCEs) using OLS on forced-choice outcomes. If not conjoint, treat as ordered outcome and use ordered logit with treatment assignment. **Tier 1 (RCT). Level A.**
- Source: Random assignment of ranked vignettes
- Key uncertainty: Need to verify rank variables are from conjoint design

**Data needed:** Present, but need codebook to confirm rank structure.
**Novel:** Conjoint decomposition of ICC support attributes — no prior work.
**Impact:** Directly actionable for framing strategy.

| N | F | I | ID | Total |
|---|---|---|----|-------|
| 4 | 3 | 4 | 5  | **4.2** |

---

### Idea 8 — **Gender and Civilian Protection Norms: Who Supports ICC and Why?**
**Sub-topic: Gender & Humanitarian Intervention Support**
**RQ:** Do female respondents show higher baseline ICC referral support, and does benevolent sexism (paternalism toward female victims) predict casualty framing effects among men?

**Method:** OLS with `female × apartheid_treatment` interaction. Benevolent sexism (`benevolent_sexism_agg`) as moderator among male respondents. **Tier 1 (RCT). Level A.**
- Source: Random assignment; gender pre-determined
- Novel: Distinguishes female respondent effect from female victim salience effect

**Data needed:** Present.
**Novel:** Gender gap in humanitarian intervention support typically explained by risk aversion — this proposes a sexism-mechanism for men.
**Impact:** Moderate — theoretical contribution to gender and IR.

| N | F | I | ID | Total |
|---|---|---|----|-------|
| 4 | 5 | 3 | 5  | **4.2** |

---

### Idea 9 — **Education and Receptivity to International Legal Frames**
**Sub-topic: Information Processing & Legal Sophistication**
**RQ:** Does higher education amplify the effect of apartheid framing on ICC support, consistent with a legal-sophistication mechanism?

**Method:** OLS with `education × apartheid_treatment` interaction. Heckman correction if higher-educated respondents are differentially selected into the survey. **Tier 1 (RCT). Level A.**
- Source: Random assignment; education pre-determined
- Threats: Education correlated with partisan identity — partial, include both

**Data needed:** Present.
**Novel:** "Conceptual sophistication" literature (Zaller 1992) applied to ICC framing.
**Impact:** Moderate — speaks to elite/mass opinion gaps on international law.

| N | F | I | ID | Total |
|---|---|---|----|-------|
| 3 | 5 | 3 | 5  | **4.0** |

---

### Idea 10 — **Regional Variation in ICC Support: Heckman-Corrected Differential Framing Response**
**Sub-topic: Geographic Polarization & International Institutions**
**RQ:** Do Southern/rural respondents respond differently to civilian casualty frames, and does this explain regional variation in ICC legitimacy perceptions?

**Method:** OLS with `region × apartheid_treatment` interaction. Heckman selection if regional sampling is non-random. **Tier 1 (RCT). Level A.**
- Source: Random assignment; region pre-determined
- Note: Smaller cells per region — watch power

**Data needed:** Present.
**Novel:** Regional variation in ICC support attitudes is completely unstudied.
**Impact:** Moderate — more descriptive than theoretical.

| N | F | I | ID | Total |
|---|---|---|----|-------|
| 3 | 4 | 3 | 5  | **3.8** |

---

## Ranking Summary

| # | Idea | N | F | I | ID | Total |
|---|------|---|---|---|----|-------|
| 1 | Apartheid vs. Persecution Label | 5 | 5 | 5 | 5 | **5.0** |
| 2 | Partisan Asymmetry in Legal Frame | 4 | 5 | 5 | 5 | **4.8** |
| 3 | Hostile Sexism × Framing | 5 | 5 | 4 | 5 | **4.8** |
| 4 | Foreign Aid Conditionality | 4 | 5 | 5 | 5 | **4.8** |
| 5 | Race × Apartheid Framing | 5 | 4 | 5 | 5 | **4.8** |
| 6 | Pro-Israel Prior as Resistance | 4 | 5 | 4 | 5 | **4.6** |
| 7 | Conjoint Attribute Weighting | 4 | 3 | 4 | 5 | **4.2** |
| 8 | Gender & Benevolent Sexism | 4 | 5 | 3 | 5 | **4.2** |
| 9 | Education × Legal Sophistication | 3 | 5 | 3 | 5 | **4.0** |
| 10 | Regional Variation + Heckman | 3 | 4 | 3 | 5 | **3.8** |

---

## TOP 3 ELABORATIONS

### #1: Apartheid vs. Persecution Label Effects on ICC Referral
**Sub-topic: Legal Framing Precision**

"Apartheid" and "persecution" are both ICC Rome Statute crimes but carry vastly different political valences. "Apartheid" invokes South African history and systemic racial oppression; "persecution" is vaguer and less politically loaded. This experiment can identify whether the *legal specificity* of the label, or its *historical resonance*, drives ICC support — a distinction no prior work makes.

**Week 1 plan:** Run balance check across `apartheid_vs_persecution_treat` arms on all demographics. Run OLS of treatment on primary ICC support outcome. Estimate CATEs by `pro_israel_score` quintile to identify persuadable subgroups.

---

### #2: Partisan Asymmetry in Legal Frame Receptivity
**Sub-topic: Political Polarization & International Law**

The apartheid framing may work well on Democrats but backfire among Republicans via reactance — consistent with "boomerang effect" theory (Nyhan & Reifler 2010). This paper would provide the first clean causal estimate of partisan frame asymmetry for ICC support, with direct implications for whether universal vs. targeted communication strategies work.

**Week 1 plan:** Estimate `apartheid_treatment × stronger_republican_8pt` interaction via OLS. Then run causal forest (GRF package in R) on full treatment-covariate space to generate CATE map. Visualize treatment effects across the 8-point partisan scale.

---

### #3: Hostile Sexism and Civilian Casualty Desensitization
**Sub-topic: Psychological Predispositions & Atrocity Response**

Hostile sexism predicts viewing women as manipulative rather than vulnerable — which may translate into discounting civilian casualties that include women and children. Apartheid framing shifts from victim-centered to structural/legal framing, potentially bypassing this desensitization. No prior work bridges ambivalent sexism theory (Glick & Fiske 1996) to international humanitarian law opinion. This is a genuinely novel cross-disciplinary finding if confirmed.

**Week 1 plan:** Check distribution of `hostile_sexism_agg`. Regress ICC support on `hostile_sexism_agg` × `apartheid_treatment`. Run quantile regression to check whether effects are concentrated among high-sexism respondents. Test whether `benevolent_sexism_agg` has opposite-sign interaction (paternalistic protection motive).

---

```json
{
  "top_ideas": [
    {
      "rank": 1,
      "title": "Apartheid vs. Persecution Label Effects on ICC Referral Support",
      "research_question": "Does labeling Israeli actions as 'apartheid' vs. 'persecution' differentially increase support for ICC referral, holding casualty salience constant?",
      "method": "OLS with treatment dummy (apartheid_vs_persecution_treat), LASSO covariate selection, CATE estimation by pro_israel_score quintile",
      "identification_level": "A",
      "identification_source": "Random assignment to apartheid vs. persecution legal label in survey experiment",
      "sub_topic": "Legal Framing Precision",
      "data_sources": ["Survey experiment already collected (N=1,185)"],
      "novelty": 5,
      "feasibility": 5,
      "impact": 5,
      "identification": 5,
      "total_score": 5.0,
      "pitch": "Apartheid and persecution are both Rome Statute crimes, but 'apartheid' carries unique historical weight that may shift ICC support independently of casualty information. This experiment provides the first clean causal estimate of legal label precision on international justice preferences — directly actionable for advocacy organizations deciding which frames to deploy.",
      "first_experiment": "Balance check on apartheid_vs_persecution_treat arms → OLS on primary ICC support outcome → CATE estimation by pro_israel_score quintile to identify who is movable"
    },
    {
      "rank": 2,
      "title": "Partisan Asymmetry in Legal Frame Receptivity for ICC Referral",
      "research_question": "Do Democrats and Republicans diverge in ICC referral support in response to apartheid framing, and does the partisan gap widen with stronger legal frames?",
      "method": "OLS with apartheid_treatment × stronger_republican_8pt interaction; Causal Forest (GRF) for full CATE map across partisan spectrum",
      "identification_level": "A",
      "identification_source": "Random assignment to apartheid framing; partisan identity is pre-determined and exogenous to treatment",
      "sub_topic": "Political Polarization and International Law",
      "data_sources": ["Survey experiment already collected (N=1,185)", "stronger_republican_8pt continuous scale"],
      "novelty": 4,
      "feasibility": 5,
      "impact": 5,
      "identification": 5,
      "total_score": 4.8,
      "pitch": "If apartheid framing backfires among Republicans via reactance while activating Democrats, universal communication strategies are counterproductive — advocates should micro-target frames. This paper provides the first experimental evidence on partisan frame asymmetry for ICC referral, with immediate practical implications.",
      "first_experiment": "OLS with treatment × republican_8pt interaction → Causal Forest estimation → visualize treatment effect as function of partisan score"
    },
    {
      "rank": 3,
      "title": "Hostile Sexism as a Moderator of Civilian Casualty Framing Effects",
      "research_question": "Do respondents high in hostile sexism discount civilian casualties involving women, and does apartheid (structural) framing bypass this psychological desensitization?",
      "method": "OLS with hostile_sexism_agg × apartheid_treatment interaction; quantile regression to detect tail effects; benevolent_sexism_agg as opposite-sign check",
      "identification_level": "A",
      "identification_source": "Random assignment to apartheid framing; hostile_sexism_agg measured pre-treatment and exogenous",
      "sub_topic": "Psychological Predispositions and Atrocity Response",
      "data_sources": ["Survey experiment already collected (N=1,185)", "hostile_sexism_1-3/agg", "benevolent_sexism_1-3/agg"],
      "novelty": 5,
      "feasibility": 5,
      "impact": 4,
      "identification": 5,
      "total_score": 4.8,
      "pitch": "Ambivalent sexism theory predicts that hostile sexists view female suffering as less credible — which may cause them to discount civilian casualty frames featuring women and children. Structural/legal frames like apartheid may circumvent this by shifting from victim-centered to systemic framing. No prior work connects Glick & Fiske's sexism scales to international humanitarian law opinion, making this a genuine cross-disciplinary contribution.",
      "first_experiment": "Distribution check on hostile_sexism_agg → OLS with interaction term → quantile regression at 75th and 90th percentile of sexism distribution → repeat with benevolent_sexism_agg for mechanism test"
    }
  ],
  "identification_warning": "No warning needed — all top 3 ideas have Identification = 5 (Level A). This dataset is a randomized survey experiment with pre-assigned treatment conditions, providing clean causal identification without requiring DiD or panel variation. The cross-sectional structure is by design, not a limitation."
}
```