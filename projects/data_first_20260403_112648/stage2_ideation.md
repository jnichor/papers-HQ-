# Junshi Research Advisor — Voucher vs. Training: Differential Employment Effects

## Dataset Diagnosis

Before generating ideas, one critical observation: **all four survey dates fall within the same week (July 17–24, 2010)**. This is not meaningful panel data — it is a single cross-section surveyed over one week. The 0% ID overlap confirms this.

**The real identification asset is the treatment assignment itself.** Variables `treatstat`, `voucher`, `training`, `both` indicate this is almost certainly a **multi-arm RCT** (control / voucher-only / training-only / both). This is Level A identification — the cleanest possible. Every idea should exploit this randomization.

Secondary identification asset: `b_c2avtawjihi` (Tawjihi score — Jordan's matriculation exam) and `b_b3socialstatus` are **pre-determined characteristics** that can credibly moderate treatment effects.

---

## Literature Themes & Gaps

| Theme | What exists | Gap |
|---|---|---|
| Average treatment effects | Groh et al. 2016 (Jordan), Card et al. (training reviews) | Heterogeneous effects by pre-treatment characteristics |
| Gender × program | Maitra & Mani, Hirshleifer et al. | Mechanism: does it work through job search or skill? |
| Program complementarity | Sparse — most studies single-arm | Is voucher + training superadditive? |
| Social mobility | Alfonsi et al. (Uganda) | SES heterogeneity in Middle East context |
| Non-labor outcomes | Almost none for Jordan | Marriage timing, women's autonomy |
| Information frictions | Limited | Do vouchers work because they reveal market wages? |
| Institution quality | Card et al. suggest this matters | Provider quality moderating training returns |

---

## 8–10 Research Ideas

---

### Idea 1 — Gender Differential in Voucher vs. Training Returns
**Sub-topic: Gender**
**Question:** Does the relative advantage of vouchers over training differ by gender, and if so, through which mechanism?
**Method:** **Tier 1 — OLS/IV on RCT arms with gender interaction.** Regress employment/wage outcomes on `voucher × female`, `training × female`, `both × female` dummies. Source of identifying variation: **random treatment assignment**. No pre-treatment periods needed — the RCT cross-section is sufficient. Threats: gender imbalance across treatment cells (check randomization balance).
**Data:** Available — `b_b2gender`, treatment dummies, employment outcomes.
**Novelty:** Existing Jordan studies report average effects; this explicitly tests mechanism heterogeneity by gender in a Jordanian labor market context (one of the lowest female LFPR globally).
**Why novel:** Most HTE analyses on vouchers vs. training focus on age, not gender × program type interaction in MENA.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 4 | 5 | 5 | 5 | **4.8** |

ID = 5: Level A. Randomized assignment of treatment arms.

---

### Idea 2 — Tawjihi Score as Dose Moderator: Human Capital × Program Complementarity
**Sub-topic: Human capital heterogeneity**
**Question:** Does pre-existing academic achievement (Tawjihi score) determine whether vouchers or job training is the more effective intervention?
**Method:** **Tier 1 — RCT HTE with continuous moderator.** Interact `voucher`, `training`, `both` dummies with `b_c2avtawjihi` (continuous, pre-determined). Estimate: `Y = α + β₁·Voucher + β₂·Training + β₃·Voucher×Tawjihi + β₄·Training×Tawjihi + X'γ + ε`. Identifying variation: treatment is randomly assigned; Tawjihi is pre-determined (taken years before the program). Credibility: cannot manipulate a score earned years prior.
**Data:** Available — `b_c2avtawjihi`, `b_tawjihirecord`, treatment dummies.
**Why novel:** Theory predicts training requires absorptive capacity (higher Tawjihi → bigger training returns) while vouchers may work regardless of academic baseline. This directly tests that hypothesis.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 4 | 5 | 4 | 5 | **4.6** |

ID = 5: Level A. RCT × pre-determined academic score.

---

### Idea 3 — RDD at Tawjihi Pass/Fail Cutoff for Program Eligibility
**Sub-topic: Academic selection & eligibility**
**Question:** If program eligibility required passing the Tawjihi, does the pass/fail discontinuity reveal the LATE of program access on employment?
**Method:** **Tier 1 — RDD on `b_c2avtawjihi` at the pass threshold.** Use `b_passfail` as the running variable indicator. Estimate local polynomial regression on each side of the cutoff. Source of variation: students just above/below the passing threshold are near-identical on unobservables. Threat: manipulation of scores around cutoff (test with McCrary density test). Pre-treatment periods: not needed for RDD.
**Data:** `b_c2avtawjihi`, `b_passfail`, `b_examresult` — all available.
**Why novel:** This provides a SECOND independent identification strategy orthogonal to the RCT arms, enabling a comparison of LATE (RDD) vs. ATE (RCT). If results align, external validity is dramatically strengthened.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 4 | 4 | 4 | 4 | **4.0** |

ID = 4: Level A with threat of score manipulation near threshold.

---

### Idea 4 — Social Status × Program Type: Do Vouchers Reinforce Inequality?
**Sub-topic: Distributional effects / inequality**
**Question:** Do vouchers disproportionately benefit higher-SES youth (who can navigate job markets better) while training is more equalizing?
**Method:** **Tier 1 — RCT HTE with `b_b3socialstatus`.** Interact treatment arms with pre-determined social status. Test for slope heterogeneity using endogenous stratification estimator (Abadie et al. 2018) to avoid specification-searching bias. Identifying variation: randomized treatment; SES is measured pre-program.
**Data:** `b_b3socialstatus`, treatment dummies, employment/wage outcomes.
**Why novel:** Policy-critical question: if vouchers benefit the already-advantaged, they exacerbate inequality. This directly informs program targeting.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 3 | 5 | 5 | 5 | **4.6** |

ID = 5: Level A. RCT × pre-determined SES.

---

### Idea 5 — Community College Quality as Moderator of Training Returns
**Sub-topic: Institution quality**
**Question:** Does the quality of the community college assigned to the training arm explain variation in training effectiveness, conditional on randomized assignment?
**Method:** **Tier 1/2 — RCT × institution quality interaction.** Within the training arm, use `b_communitycollege` identifiers to construct college-level quality proxies (average pass rates, specialization mix). Regress outcomes on training-arm indicator × college quality. Identifying variation: random assignment to training arm; college assignment is either randomized or conditionally exogenous given treatment.
**Data:** `b_communitycollege`, `b_examresult`, `b_passfail`, `b_c3specialization`.
**Why novel:** The "training doesn't work" finding in many LMICs may be an institution-quality story, not a training-vs-voucher story. This decomposes average training effects.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 4 | 4 | 4 | 4 | **4.0** |

ID = 4: Level A within training arm; slight threat if college assignment is non-random.

---

### Idea 6 — Program Complementarity: Is Voucher + Training Superadditive?
**Sub-topic: Program design / bundling**
**Question:** Does the combined arm produce employment gains larger than the sum of individual arms, and for whom?
**Method:** **Tier 1 — Factorial RCT decomposition.** Test H₀: `β_both = β_voucher + β_training` using a Wald test. If superadditive, decompose the complementarity by gender and SES. Identifying variation: random assignment to all four arms is the gold standard.
**Data:** All treatment dummies are in the dataset.
**Why novel:** Almost no published study has a clean 2×2 RCT design for this comparison. Most compare two arms only, making complementarity untestable. This is methodologically rare.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 5 | 5 | 5 | 5 | **5.0** |

ID = 5: Level A. Pure RCT factorial design.

---

### Idea 7 — Labor Supply Constraints vs. Demand Frictions: Desire vs. Ability
**Sub-topic: Labor supply heterogeneity**
**Question:** Do vouchers and training differentially resolve demand-side frictions vs. supply-side constraints (measured by `b_b6desiretowork` and `b_b7abilitytowork`)?
**Method:** **Tier 1 — RCT HTE stratified by pre-treatment constraint type.** If "desire to work" is low, demand-side interventions won't work regardless. If "ability to work" is the constraint, training may dominate. Estimate treatment effects within each stratum. Identifying variation: randomized treatment; desire/ability measured prior to treatment.
**Data:** `b_b6desiretowork`, `b_b7abilitytowork`, treatment dummies.
**Why novel:** This is a direct test of the theoretical mechanism — it moves from "which program works" to "WHY it works," with implications for targeting.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 5 | 4 | 5 | 5 | **4.8** |

ID = 5: Level A. RCT × pre-determined attitudinal constraints.

---

### Idea 8 — Marriage Timing and Women's Autonomy as Non-Labor Outcomes
**Sub-topic: Non-labor outcomes / women's empowerment**
**Question:** Do employment programs (especially vouchers that connect women to employers) reduce early marriage or change marriage age expectations?
**Method:** **Tier 1 — RCT on non-labor outcome `b_b4marriageage`.** Regress marriage age/plans on treatment dummies, with female subsample. Test whether training vs. voucher differentially affects autonomy measures. Identifying variation: randomized treatment assignment.
**Data:** `b_b4marriageage`, `b_b5selectiondecision`, gender variable.
**Why novel:** The employment-marriage nexus in MENA is understudied. If vouchers connect women to the formal sector (changing reservation marriage age), this has long-run demographic implications.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 5 | 4 | 4 | 5 | **4.6** |

ID = 5: Level A. Randomized treatment; marriage timing is post-treatment outcome.

---

### Idea 9 — Specialization-Job Match and Voucher vs. Training Effectiveness
**Sub-topic: Skill-job mismatch**
**Question:** Does the match between a youth's training specialization and local labor demand moderate whether vouchers (flexible) outperform training (rigid)?
**Method:** **Tier 2 — Bartik-style shift-share within RCT.** Construct a mismatch index from `b_c3specialization` and local job vacancy data (or census occupation shares). Interact mismatch with treatment arms. Identifying variation: randomized treatment; specialization pre-dates program.
**Data:** `b_c3specialization`, treatment dummies; may need external occupation data.
**Why novel:** The theory predicts vouchers should dominate ESPECIALLY when training produces the wrong skills. Testing this prediction directly is new.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 4 | 3 | 4 | 3 | **3.4** |

ID = 3: Level B. Pre-determined specialization creates dose variation, but external occupation data required.

---

### Idea 10 — Selection Decision and Program Take-Up: LATE vs. ATE
**Sub-topic: Compliance and selection**
**Question:** Does who selects into each program arm (using `b_b5selectiondecision`) affect outcomes, and can IV recover the LATE for compliers?
**Method:** **Tier 1 — IV/2SLS using randomized assignment as instrument for actual program take-up.** `b_b5selectiondecision` likely captures whether the assignment was accepted. IV recovers LATE. Compare LATE vs. ITT (intent-to-treat) to understand compliance effects.
**Data:** `b_b5selectiondecision`, treatment dummies, outcomes.
**Why novel:** Most RCT papers report ITT only. If there is non-compliance, the LATE (the effect on those who actually participate) can differ dramatically — and the policy-relevant parameter depends on whether the program is mandatory or voluntary.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 3 | 5 | 4 | 5 | **4.4** |

ID = 5: Level A. Randomized assignment instruments actual take-up.

---

## Ranked Summary

| Rank | Idea | N | F | I | ID | **Score** | Sub-topic |
|---|---|---|---|---|---|---|---|
| 1 | Program Complementarity (Idea 6) | 5 | 5 | 5 | 5 | **5.00** | Program design |
| 2 | Labor Supply Constraints (Idea 7) | 5 | 4 | 5 | 5 | **4.80** | Labor supply |
| 3 | Gender Differential (Idea 1) | 4 | 5 | 5 | 5 | **4.80** | Gender |
| 4 | Social Status (Idea 4) | 3 | 5 | 5 | 5 | **4.60** | Inequality |
| 5 | Tawjihi Moderator (Idea 2) | 4 | 5 | 4 | 5 | **4.60** | Human capital |
| 6 | Marriage Timing (Idea 8) | 5 | 4 | 4 | 5 | **4.60** | Non-labor |
| 7 | LATE vs. ATE (Idea 10) | 3 | 5 | 4 | 5 | **4.40** | Compliance |
| 8 | RDD Tawjihi (Idea 3) | 4 | 4 | 4 | 4 | **4.00** | Academic selection |
| 9 | College Quality (Idea 5) | 4 | 4 | 4 | 4 | **4.00** | Institution quality |
| 10 | Skill Mismatch (Idea 9) | 4 | 3 | 4 | 3 | **3.40** | Skill mismatch |

---

## Top 3 — Full Elaboration

---

### #1 — Program Complementarity: Is Voucher + Training Superadditive?

**Research question:** Does simultaneous access to both a wage voucher and vocational training produce employment gains larger than the sum of each program in isolation — and does this complementarity vary by gender or SES?

**Method (Tier 1 — Factorial RCT):**
The dataset's four-arm structure (control, voucher, training, both) is a rare 2×2 factorial design. The estimator is:

```
Y_i = α + β₁·Voucher_i + β₂·Training_i + β₃·(Voucher×Training)_i + X_i'γ + ε_i
```

where `β₃` directly identifies superadditivity. If `β₃ > 0`, the programs are complements. Test H₀: `β₃ = 0` using heteroskedasticity-robust SEs. Follow with HTE: interact `β₃` with gender and social status. No pre-treatment periods needed; the RCT cross-section is the design.

**Identification:** Level A (ID = 5). Pure random assignment to all four arms. No threats from parallel trends (irrelevant in cross-section RCT). Inference: with N ≈ 2,322 across 4 arms, each cell has ~580 observations — adequate power for interaction effects.

**What makes this novel:** The Groh et al. (2016) Jordan NOW paper reports arm-by-arm results but does not formally test for superadditivity using an interaction estimator. Virtually no published paper in the voucher/training literature has a clean factorial structure that makes `β₃` identified. The policy implication is concrete: if programs are superadditive, bundling is cost-effective; if they substitute, policymakers must choose.

**Week 1 action:** Construct the four treatment cells from `voucher`, `training`, `both`. Check randomization balance using a joint F-test of pre-treatment characteristics across cells. Estimate the main linear probability model with and without controls. Plot cell-mean outcomes with 95% CIs.

---

### #2 — Labor Supply Constraints vs. Demand Frictions: Desire vs. Ability to Work

**Research question:** Do vouchers and job training differentially resolve distinct pre-existing barriers to employment — specifically, do they work for youth who want to work but lack ability differently than for youth who have ability but lack desire?

**Method (Tier 1 — RCT HTE stratified by constraint type):**
Use `b_b6desiretowork` and `b_b7abilitytowork` to create a 2×2 constraint typology:
- High desire / high ability → market friction (vouchers should work — they connect)
- High desire / low ability → skill deficit (training should work — it builds skills)
- Low desire / high ability → preference/culture barrier (neither may work)
- Low desire / low ability → compound barrier (both required)

Estimate:
```
Y_i = α + Σ_k [β_k · Treat_i · Stratum_k] + δ·Stratum_k + X_i'γ + ε_i
```

Test whether treatment effect heterogeneity across strata is statistically significant using a joint Wald test. Identifying variation: treatment assignment is randomized; desire/ability measured on the survey (pre-determined relative to employment outcomes measured later in the questionnaire).

**Identification:** Level A (ID = 5). The stratification variables are attitudinal measures taken independently of outcomes. Even if there is measurement error in desire/ability, the treatment effect within each stratum is still identified by randomization.

**What makes this novel:** Existing heterogeneous effects analyses focus on observables like age, education, or gender — they do not test the underlying structural constraint. This paper operationalizes the theoretical distinction between demand-side (desire) and supply-side (ability) barriers directly, which is the mechanism most policy discussions assume but no paper directly tests in a multi-arm RCT.

**Week 1 action:** Cross-tabulate `b_b6desiretowork` × `b_b7abilitytowork` to check cell sizes. If the variables are Likert-scale, discretize at the median. Estimate treatment effects separately for each of the four constraint strata. Run a formal test for equal treatment effects across strata.

---

### #3 — Gender Differential in Voucher vs. Training Returns: Mechanism Decomposition

**Research question:** Does the voucher arm disproportionately benefit women relative to training — and if so, is this because vouchers provide information about market wages (breaking monopsony), reduce employer discrimination through subsidy, or connect women to formal sector jobs with better career paths?

**Method (Tier 1 — RCT interaction with gender + mechanism proxies):**
```
Y_i = α + β₁·Voucher_i·Female_i + β₂·Training_i·Female_i + β₃·Both_i·Female_i
      + β₄·Voucher_i + β₅·Training_i + β₆·Both_i + δ·Female_i + X_i'γ + ε_i
```

The gender-treatment interactions are the main parameters of interest. Then decompose: if `β₁ > β₂` for women (vouchers dominate), test whether this is mediated by formal-sector job placement, wage level, or job stability using available job characteristic variables (`w`, `e`, `l`, `t`). Use a Frisch-Waugh-Lovell mediation approach (not causal mediation, which requires additional assumptions, but descriptive channel analysis).

**Identification:** Level A (ID = 5). Randomized treatment; gender is obviously pre-determined. The interaction term `Voucher × Female` is identified by the joint randomization and the biological pre-determination of gender. No parallel trends assumption needed.

**What makes this novel:** Jordan has one of the world's lowest female labor force participation rates (~14%). The MENA-specific question is whether vouchers break employer-side discrimination (because the subsidy compensates for hiring risk) while training alone does not. This framing — vouchers as a discrimination tax instrument rather than just a job search tool — is theoretically new and policy-relevant beyond Jordan.

**Week 1 action:** Check randomization balance within gender cells (4 arms × 2 genders = 8 cells). Estimate the baseline regression above using LPM for employment as outcome. Plot the gender × treatment interaction graphically. Note whether `b_b2gender` is binary or has more categories.

---

```json
{
  "top_ideas": [
    {
      "rank": 1,
      "title": "Program Complementarity: Is Voucher + Training Superadditive?",
      "research_question": "Does simultaneous access to both a wage voucher and vocational training produce employment gains larger than the sum of each program in isolation, and does this complementarity vary by gender or SES?",
      "method": "Factorial RCT with interaction term (Voucher × Training)",
      "identification_level": "A",
      "identification_source": "Random assignment to four treatment arms (control, voucher, training, both) creates clean experimental variation for the β_complementarity interaction",
      "sub_topic": "Program design and bundling",
      "data_sources": ["voucher", "training", "both", "treatstat", "employment outcome variables l, t, w, e"],
      "novelty": 5,
      "feasibility": 5,
      "impact": 5,
      "identification": 5,
      "total_score": 5.0,
      "pitch": "The dataset's rare four-arm RCT structure allows direct identification of whether vouchers and training are complements or substitutes — a question virtually no published paper has answered cleanly. If superadditive, bundling is cost-effective; if substitutes, policymakers must choose. The interaction estimator β₃ is fully identified by randomization, requiring no additional assumptions.",
      "first_experiment": "Construct four treatment cells from voucher/training/both dummies. Run joint F-test of pre-treatment balance across cells. Estimate LPM with Y = α + β₁·Voucher + β₂·Training + β₃·(Voucher×Training) + controls. Test H₀: β₃ = 0. Plot cell-mean employment outcomes with 95% CIs."
    },
    {
      "rank": 2,
      "title": "Labor Supply Constraints vs. Demand Frictions: Desire vs. Ability to Work",
      "research_question": "Do vouchers and job training differentially resolve distinct pre-existing barriers — specifically, do they work for youth who want to work but lack ability differently than for youth who have ability but lack desire?",
      "method": "RCT HTE stratified by pre-determined constraint typology from b_b6desiretowork × b_b7abilitytowork",
      "identification_level": "A",
      "identification_source": "Random treatment assignment; desire and ability measured independently from employment outcomes, creating credible pre-determined interaction variables",
      "sub_topic": "Labor supply heterogeneity and mechanism",
      "data_sources": ["b_b6desiretowork", "b_b7abilitytowork", "treatstat", "voucher", "training", "both", "employment outcomes"],
      "novelty": 5,
      "feasibility": 4,
      "impact": 5,
      "identification": 5,
      "total_score": 4.8,
      "pitch": "No published study on employment programs directly tests whether vouchers resolve demand-side frictions while training resolves supply-side skill deficits — yet this is the core theoretical mechanism policymakers invoke. Using pre-measured desire and ability variables to stratify treatment effects within a clean RCT provides a direct structural test unavailable in any prior paper.",
      "first_experiment": "Cross-tabulate b_b6desiretowork × b_b7abilitytowork to verify cell sizes (target ≥50 per stratum-treatment cell). Discretize at median if Likert-scale. Estimate treatment effects separately for each of four constraint strata. Run Wald test for equal treatment effects across strata."
    },
    {
      "rank": 3,
      "title": "Gender Differential in Voucher vs. Training Returns: Mechanism Decomposition",
      "research_question": "Does the voucher arm disproportionately benefit women relative to training in Jordan's low-LFPR context, and is this driven by employer-side discrimination reduction rather than skill acquisition?",
      "method": "RCT with gender × treatment interaction terms, followed by descriptive mediation through formal-sector job placement and wage variables",
      "identification_level": "A",
      "identification_source": "Randomized treatment assignment; gender is biologically pre-determined; interaction Voucher×Female is jointly identified by both",
      "sub_topic": "Gender and women's labor force participation",
      "data_sources": ["b_b2gender", "voucher", "training", "both", "treatstat", "w", "e", "l", "t"],
      "novelty": 4,
      "feasibility": 5,
      "impact": 5,
      "identification": 5,
      "total_score": 4.8,
      "pitch": "Jordan's female LFPR of ~14% makes it the ideal context to test whether vouchers function as a discrimination tax instrument (compensating employers for hiring risk) rather than merely a job-search tool. The four-arm RCT cleanly identifies gender heterogeneity in program effects, and the mechanism decomposition — comparing formal-sector placement rates across arms by gender — advances theory beyond average treatment effect estimation.",
      "first_experiment": "Check randomization balance within 8 cells (4 arms × 2 genders). Estimate LPM: Y = α + β₁·Voucher·Female + β₂·Training·Female + β₃·Both·Female + β₄·Voucher + β₅·Training + β₆·Both + δ·Female + controls. Plot the six treatment-gender interaction means. Verify b_b2gender coding."
    }
  ],
  "identification_warning": null
}
```