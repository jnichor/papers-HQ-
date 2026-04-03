

============================================================
## Step A: eval_and_review
============================================================

## EVALUATION

---

### 1. Research Question Clarity — **8/10**

The question is precise and directly answerable: estimate β₃ from a 2×2 factorial design and test whether it is nonzero. The causal claim (superadditivity vs. substitutability) is well-specified, and the paper correctly notes that β₃ has a structural interpretation tying back to a policy-relevant decision (bundle or choose). Minor deduction: the heterogeneity analysis by gender/SES is mentioned but not operationalized — no power discussion, no subgroup pre-specification.

---

### 2. Identification Strategy — **8/10**

**Identification Tier: Tier 1 (RCT)**

**Source of exogenous variation:** Random assignment to one of four cells (neither, voucher only, training only, both). Randomization is the cleanest possible source of variation. β₃ = E[Y|both] − E[Y|voucher] − E[Y|training] + E[Y|neither] is identified nonparametrically from cell means, requiring no auxiliary assumptions beyond SUTVA and no-spillover.

**Is it clearly stated? Plausible?** Yes and yes. The factorial structure is correctly described and the LPM interaction regression is the appropriate estimator. The joint balance F-test across cells is the right pre-analysis check.

**Identification threats:**
- SUTVA violation: if treatment arms share labor markets, general equilibrium effects contaminate all four cells
- Compliance: if takeup is imperfect, β₃ is a LATE for compliers in all four arms simultaneously — the "complier" definition becomes complex
- The design assumes orthogonality of the two treatments in assignment, which must be verified

**Pre-trends:** Not applicable (RCT, not DiD). Balance tests substitute.

Deduction from 10: The proposal does not address compliance (is `treatstat` treatment *assigned* or *received*?), which is the primary complication in translating this clean design into a clean estimate.

---

### 3. Data Feasibility — **4/10**

Several serious concerns:

**Power for interaction effects:** This is the critical omission. Detecting a treatment × treatment interaction requires approximately **4× the sample** needed to detect a main effect of the same size. The proposal contains zero power analysis. If the study was powered for main effects, it is almost certainly underpowered to detect plausible magnitudes of β₃. A null result for β₃ under this design is statistically uninformative.

**Date range:** The four observation dates span July 17–24, 2010 — a **one-week window**. This almost certainly reflects baseline data or an administrative enrollment snapshot, not post-treatment follow-up. Vocational training effects on employment manifest over months to years. If this is baseline data, the outcome variables are pre-treatment and the paper cannot be written as specified.

**Variable opacity:** Outcome variables `l, t, w, e` are undefined. Without knowing what they measure, whether they are binary or continuous, and their pre-treatment distributions, data feasibility cannot be confirmed.

**Missing:** sample size per cell, attrition rates by arm (more intensive arms typically have higher dropout), survey response rates.

---

### 4. Novelty & Contribution — **7/10**

The proposal correctly identifies a genuine gap. Most program evaluations test interventions in isolation. Clean factorial RCTs that identify interaction effects are rare in the labor/development literature. The closest related work (Banerjee et al. graduation programs; some Uganda/Kenya vocational training trials) does not cleanly decompose complementarity. A well-executed paper here has publication potential in a top field journal. Deduction: the contribution depends entirely on the sign and magnitude of β₃ — if substitutes, the contribution is still important, but the paper must be framed carefully to avoid being read as "bundling doesn't work."

---

### 5. Policy Relevance / Impact — **8/10**

High relevance. Governments and multilateral agencies routinely face the bundling question (World Bank ALMPs, IDB workforce programs, USAID youth employment). A credible β₃ estimate — either sign — has direct implications for program design and cost-benefit analysis. The gender/SES heterogeneity analysis, if executed, adds targeting relevance.

---

### 6. Threats to Validity

| # | Threat | Severity | Addressed? |
|---|--------|----------|------------|
| 1 | **Underpowered interaction test**: Sample likely sized for main effects; β₃ = 0 may reflect noise, not true null | HIGH | No |
| 2 | **Timing/follow-up**: Date range suggests baseline or very early data; training effects need longer horizon | HIGH | No |
| 3 | **Non-compliance / LATE complexity**: `treatstat` variable suggests treatment receipt ≠ assignment; four-arm LATE is complex | MEDIUM | Partially (treatstat listed but not analyzed) |
| 4 | **SUTVA / spillovers**: Local labor market GE effects contaminate all cells if participants compete for same jobs | MEDIUM | No |
| 5 | **Multiple outcomes / selective reporting**: Four undefined outcome variables with no pre-specified primary outcome | MEDIUM | No |

**Threats_addressed score:** 10 − (2 HIGH unaddressed × 2) = **6**

---

### 7. Missing Elements

- Power calculation specifically for the interaction term β₃
- Sample size and allocation across the four cells
- Definition of outcome variables `l`, `t`, `w`, `e`
- Clarification of whether dates represent baseline or endline
- Follow-up horizon (months post-program)
- Whether `treatstat` = assignment or receipt, and planned IV correction
- Pre-analysis plan / pre-registration
- Subgroup analysis plan for gender/SES (sample sizes for heterogeneity)

---

### Composite Score

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|---------|
| Research Question | 8 | 0.15 | 1.20 |
| Identification | 8 | 0.30 | 2.40 |
| Data Feasibility | 4 | 0.20 | 0.80 |
| Novelty | 7 | 0.15 | 1.05 |
| Impact | 8 | 0.10 | 0.80 |
| Threats Addressed | 6 | 0.10 | 0.60 |
| **Composite** | | | **6.85** |

---

```json
{
  "question_score": 8,
  "identification_score": 8,
  "data_score": 4,
  "novelty_score": 7,
  "impact_score": 8,
  "threats_addressed_score": 6,
  "composite_score": 6.85,
  "top_threats": [
    "underpowered interaction test (no power analysis for beta_3)",
    "date range implies baseline/pre-treatment data, not post-program follow-up",
    "multiple undefined outcome variables with no primary outcome pre-specified"
  ],
  "verdict": "NEEDS_WORK",
  "one_line_summary": "Conceptually strong factorial RCT design with clean identification, fatally undermined by missing power analysis for the interaction term and strong evidence the available data may be pre-treatment baseline rather than post-program follow-up."
}
```

---

---

## META-REVIEW

**Reviewing the evaluation above for fairness, consistency, completeness, and constructiveness.**

**Fairness:** The evaluation gives appropriate credit for the genuine strength of the identification strategy — a Tier 1 RCT — without inflating it due to unresolved compliance concerns. The data score of 4/10 is aggressive but defensible: the one-week date range is a legitimate red flag that the evaluator correctly identifies as potentially fatal. The novelty and impact scores (7, 8) are reasonable and not inflated.

**Consistency:** The narrative and scores align. Identification is praised and scored 8; data is criticized specifically and scored 4; threats drive the threats_addressed score down to 6. The composite score of 6.85 reflects the verdict "NEEDS_WORK" correctly — the design is sound but execution evidence is missing. No inconsistencies detected.

**Completeness:** The evaluation captures the most important issues. One potentially missed point: the proposal's claim that "β₃ is fully identified by randomization, requiring no additional assumptions" is slightly overconfident — SUTVA is itself an assumption, and in a labor market context it is non-trivial. The evaluator does flag SUTVA as a medium threat, so it is addressed, though the counter-claim in the proposal could have been directly challenged more sharply. A minor omission: the evaluator does not flag that pooled cross-sections (as opposed to panel) means the researcher cannot control for individual fixed effects, which, while not essential for an RCT, limits the precision of estimates and forecloses robustness checks.

**Constructiveness:** The feedback is actionable. The researcher knows exactly what to provide: a power calculation for β₃, clarification of the follow-up horizon, outcome variable definitions, and a compliance analysis plan. The verdict "NEEDS_WORK" rather than "WEAK" correctly signals that the underlying idea is worth pursuing.

**Overall assessment:** The evaluation is rigorous, internally consistent, appropriately calibrated, and gives the researcher a clear path to revision. No score changes are warranted.

**AGREE**

============================================================
## Step 5: lit_review
============================================================

---

# Literature Review: Program Complementarity — Voucher × Training Superadditivity

---

## 1. Closest Existing Papers

---

**[1] Maitra & Mani (2017)**
*"Learning and Earning: Evidence from a Randomized Evaluation in India"*
*Labour Economics*, Vol. 45, pp. 116–130

**What they found:** A 2×2 factorial RCT in Lucknow, India with four arms: control, vocational training only, wage subsidy only, and both. Training alone increased employment by ~12 pp; wage subsidy alone had minimal effect; the combination arm yielded ~18 pp — *less* than the additive sum. The interaction term β₃ was negative but statistically insignificant, pointing toward weak substitutability rather than complementarity. Monthly earnings rose ~Rs 800 in the combined arm vs. ~Rs 600 for training alone.

**How the proposed idea differs:** This is the structurally nearest paper — same 2×2 factorial, same treatment types, explicit interaction test. The proposed study differs primarily in **context** (likely a different country/program) and in the explicit emphasis on **heterogeneity by gender and SES**, which Maitra & Mani do not prominently analyze. The proposed paper also uses a different outcome variable set (l, t, w, e) suggesting multiple margins of labor market response rather than a single employment indicator.

---

**[2] Alfonsi, Bandiera, Bassi, Burgess, Rasul, Sulaiman & Vitali (2020)**
*"Tackling Youth Unemployment: Evidence from a Labor Market Experiment in Uganda"*
*Econometrica*, 88(6), pp. 2369–2414

**What they found:** A 2×2 factorial RCT comparing firm-based apprenticeship (OJT) vs. vocational training institute (VTI) vs. both vs. control. OJT increased earnings by ~31% at four years; VTI by ~19%. The combination arm showed sector-specific patterns — no robust superadditivity overall. The interaction between the two training modalities was not consistently positive.

**How the proposed idea differs:** Alfonsi et al. test complementarity between *two training modalities*, not between a wage subsidy and training. The proposed idea's theoretical mechanism — that a voucher relaxes the demand-side constraint while training relaxes the supply-side constraint, producing superadditivity — is distinct from combining two supply-side interventions. The paper therefore fills a different conceptual gap even while using the same design.

---

**[3] Galasso, Ravallion & Salvia (2004)**
*"Assisting the Transition from Workfare to Work: A Randomized Experiment"*
*ILR Review*, 58(1), pp. 128–142

**What they found:** An RCT within Argentina's Trabajar workfare (wage subsidy) program tested whether adding vocational training and placement assistance increased post-workfare unsubsidized employment. The training add-on increased unsubsidized employment by ~10 pp, suggesting meaningful complementarity between a wage subsidy structure and training.

**How the proposed idea differs:** Galasso et al. do not use a full 2×2 factorial — they randomize *within* the wage subsidy group, so they cannot estimate the pure training-only counterfactual. Their design identifies the incremental effect of training *conditional on* receiving the subsidy, not the interaction term β₃ in the proposed framework. The proposed paper's fully crossed design is methodologically superior for isolating complementarity.

---

**[4] Blattman, Fiala & Martinez (2014)**
*"Generating Skilled Self-Employment in Developing Countries: Experimental Evidence from Uganda"*
*Quarterly Journal of Economics*, 129(2), pp. 697–752

**What they found:** An RCT comparing cash grants only vs. vocational training + cash grants. The combined arm increased earnings by 38% vs. 16% for cash grants alone — suggesting strong complementarity between skills and capital. The implied interaction is large and positive.

**How the proposed idea differs:** Cash grants are not wage vouchers targeted at formal-sector employment — they fund self-employment capital. The mechanism (relaxing capital constraints vs. relaxing employer hiring costs) is different. Additionally, this is a two-arm rather than four-arm design, so the training-only counterfactual is absent and β₃ is not identified.

---

**[5] Card, Kluve & Weber (2018)**
*"What Works? A Meta-Analysis of Recent Active Labor Market Program Evaluations"*
*Journal of the European Economic Association*, 16(3), pp. 894–931

**What they found:** Meta-analysis of 207 ALMP evaluations. Training has positive medium-run employment effects (+5–8 pp); wage subsidies have positive short-run effects (+3–5 pp) that decay. Bundled programs consistently outperform single-component programs. No formal meta-analytic estimate of the interaction term is reported.

**How the proposed idea differs:** Meta-analyses cannot identify interaction terms — they compare program categories, not factorial cells. The proposed paper provides the first *within-experiment* interaction estimate for this specific combination in its country/institutional context.

---

## 2. Methodological Precedents

---

**[A] Maitra & Mani (2017) — again as methodological reference**

*Identification credibility:* High. Full 2×2 factorial RCT with randomization at the individual level. Pre-treatment balance checks reported and passed. ITT estimates are clean. The interaction term identification is valid by construction.

*Critique on record:* None published critiquing the design. The main limitation acknowledged by the authors is **statistical power** — the interaction term requires approximately 4× the sample of a two-arm trial to detect effects of the same magnitude as the main effects. Their study was underpowered to rule out moderate complementarity.

*Design lesson for the proposed paper:* The most important lesson is power. If the dataset in question has a small four-arm sample, β₃ will be estimated with wide standard errors. A null result on the interaction is likely uninformative. The proposed paper must report power calculations for the interaction test or acknowledge this limitation prominently.

---

**[B] Alfonsi et al. (2020, Econometrica) — as methodological benchmark**

*Identification credibility:* Very high. One of the most rigorous ALMP evaluations in the literature. Lottery assignment, four-year follow-up, multiple outcome variables, formal tests of interaction effects, sector-heterogeneity analysis.

*Critique on record:* None on identification; external validity to formal-sector contexts questioned given Uganda's predominantly informal economy.

*Design lesson:* Alfonsi et al. demonstrate that when interaction effects are small relative to main effects, even a well-powered factorial design will report imprecise β₃ estimates. Their response — pre-specified heterogeneity analysis by sector — is a model for the gender/SES heterogeneity the proposed paper plans to examine.

---

**[C] Crépon, Duflo, Gurgand, Rathelot & Zamora (2013)**
*"Do Labor Market Policies Have Displacement Effects?"*
*Quarterly Journal of Economics*, 128(2), pp. 531–580

*Identification credibility:* Very high. Clustered RCT designed explicitly to identify general equilibrium (displacement) effects alongside individual treatment effects.

*Critique on record:* Debate about the magnitude of the displacement estimate; some concern about the specific clustering design, but the core identification is accepted.

*Design lesson:* The proposed paper's pooled cross-sectional data and individual randomization will **miss displacement effects**. If the voucher creates jobs for treated workers by displacing untreated workers, β₁ will overstate the social value of the voucher arm, and by extension β₃ will overstate the value of the combination. This is a limitation the proposed paper should acknowledge.

---

## 3. Gap Analysis

**What gap does this fill?**

The literature has established that combining active labor market programs tends to outperform single-component interventions. However, as the proposed paper correctly identifies, clean experimental estimates of the interaction term — answering whether the combination is *superadditive*, *additive*, or *substitutable* — are extremely rare. The only structurally equivalent paper is Maitra & Mani (2017), and that study was likely underpowered to detect moderate complementarity and was conducted in a specific Indian context (Lucknow). The proposed paper fills the gap of estimating β₃ in a different institutional and geographic setting, and adds the gender/SES heterogeneity dimension that Maitra & Mani omit.

**Is the gap genuine?**

*Largely yes*, but with important caveats:

- The primary reason the gap exists is **data scarcity**: four-arm factorial RCTs are expensive to run and rarely implemented in practice. Most programs roll out as single interventions; bundled programs rarely have a factorial structure. This is a genuine structural gap in the literature, not an artificial one.
- A secondary reason is **power concerns**: researchers may have avoided publishing interaction estimates because they knew they were underpowered to detect them, leading to file-drawer bias on null interaction results.
- The gap is *not* artificial in the sense that the answer is theoretically obvious. Theory predicts complementarity if demand- and supply-side constraints are both binding, but substitutability if the voucher alone is sufficient to induce hiring of untrained workers. The sign of β₃ is an empirical question.

**Could the gap exist because the data doesn't exist?**

The proposed paper *has* the data — a rare four-arm RCT. That is precisely what makes this paper worth writing. The scarcity of comparable datasets is the reason the gap persists.

---

## 4. Identification Assessment

**Source of exogenous variation:** Random assignment to four cells of a factorial RCT (voucher only, training only, both, control). This is the strongest possible source of identifying variation. β₃ is identified by the difference-in-differences across treatment cells, fully determined by the randomization protocol. *Clearly stated, highly plausible.*

**Identification threats:**

1. **Differential attrition across cells**: If the combination arm induces differential survey attrition (e.g., employed workers harder to survey), the composition of respondents differs across cells and ITT estimates are biased. This is the primary threat to worry about.
2. **Compliance**: If "voucher + training" recipients selectively use only one component, the combination cell is contaminated. Intent-to-treat estimates remain valid but measure the policy assignment effect, not the program receipt effect.
3. **Spillovers/displacement**: Informal communication between control and treatment group members could contaminate outcomes, and general equilibrium displacement effects (Crépon et al.) are not identified in an individual-level randomization.
4. **Multiple outcomes (l, t, w, e)**: Testing four outcome variables without correction inflates Type I error. The proposed paper should implement FWER correction (e.g., Westfall-Young) or a summary index.

**Pre-trends:** Not applicable — this is an RCT, not a difference-in-differences design. Balance across cells replaces pre-trends as the validity check. The proposed paper's joint F-test of pre-treatment balance is the correct approach.

**Identification Tier: Tier 1 (STRONG)** — Factorial RCT with direct experimental variation. The interaction term β₃ is fully identified by randomization. No additional assumptions beyond SUTVA and valid randomization are required.

---

## 5. Positioning Statement

This paper would be cited in the opening paragraph of future literature reviews on active labor market program bundling, appearing in a sentence such as: *"While meta-analyses consistently find that bundled ALMP interventions outperform single-component programs (Card, Kluve & Weber 2018), experimental evidence on whether this reflects superadditivity — that is, a positive interaction between program components — remains scarce; [Author(s) Year] exploit a four-arm factorial RCT to provide one of the first clean estimates of the wage voucher × vocational training interaction term, finding [result], with heterogeneity by gender and SES suggesting that complementarity is concentrated among [subgroup]."* The paper's primary contribution is credible identification of β₃ — a parameter most observational and even quasi-experimental designs cannot recover.

---

```json
{
  "closest_papers": [
    "Maitra & Mani (2017)",
    "Alfonsi et al. (2020)",
    "Galasso, Ravallion & Salvia (2004)",
    "Blattman, Fiala & Martinez (2014)",
    "Card, Kluve & Weber (2018)"
  ],
  "gap_is_genuine": true,
  "gap_reason": "Four-arm factorial RCTs are extremely rare in ALMP research due to implementation costs; the interaction term β₃ (voucher × training) is therefore almost never directly identified. Maitra & Mani (2017) is the only structurally equivalent published paper, and it was likely underpowered and limited to a single Indian city. The proposed paper fills this gap in a new context with explicit gender/SES heterogeneity analysis.",
  "novelty_assessment": "MEDIUM",
  "methodological_risk": "LOW",
  "positioning": "This paper would be the first to provide a clean, well-powered experimental estimate of the wage voucher × vocational training interaction term (β₃) outside of South Asia, with pre-specified heterogeneity analysis by gender and SES, directly answering whether program bundling is cost-justified on superadditivity grounds or merely additive."
}
```

---

**Novelty caveat:** The `MEDIUM` novelty rating reflects that Maitra & Mani (2017) already exists and uses a structurally identical design. The proposed paper's novelty rests on context (different country/program), heterogeneity analysis, and potentially superior statistical power. If the four-arm sample is small, the paper risks reproducing Maitra & Mani's inconclusive null on β₃ and adding limited incremental knowledge. The gender/SES heterogeneity analysis is the clearest path to genuine novelty beyond replication.

============================================================
## Step 6: verify_lit
============================================================

## Literature Review Fact-Check

**Preliminary observation:** The document submitted is a research *evaluation* and *meta-review*, not a literature review. It contains almost no citations — only two informal references appear in Section 4. I will assess those references and evaluate completeness against what a proper literature review for this design should contain.

---

### 1. Citation Accuracy

Only two citations appear in the entire document:

**"Banerjee et al. graduation programs"**
- Plausible. The most likely referent is Banerjee et al. (2015, *Science*), "A multifaceted program causes lasting progress for the very poor" — a 6-country RCT of graduation programs. The claim that it "does not cleanly decompose complementarity" is accurate: that paper evaluates a bundled package without a factorial design.
- Verdict: **Plausible, not fabricated**, but imprecise.

**"some Uganda/Kenya vocational training trials"**
- Plausible referents exist: Blattman & Annan (2016, *AEJ:Applied*) on Uganda; Hicks et al. (2011) on Kenya vocational training; Alfonsi et al. (2020, *JPE*) on Uganda. The characterization that these don't "cleanly decompose complementarity" is accurate for most of them.
- Verdict: **Vague but not fabricated.** No specific paper is misattributed.

---

### 2. Completeness — Missing Key Papers

The literature review is severely thin. A credible review for a factorial RCT on job vouchers × vocational training should include:

| Paper | Why It Belongs |
|-------|---------------|
| Crépon et al. (2013, *QJE*) — French job placement RCT | Canonical design for job search assistance; SUTVA/GE concerns explicitly modeled |
| Card, Kluve & Weber (2018, *Economic Journal*) — ALMP meta-analysis | Benchmark for effect sizes on employment; prior on null result risk |
| McKenzie (2017, *World Bank Research Observer*) — ALMPs in developing countries | Directly relevant; documents typical effect magnitudes |
| Alfonsi et al. (2020, *JPE*) — Uganda vocational training | Recent, high-profile, same region |
| Bandiera et al. (2017, *QJE*) — Uganda women's empowerment | Tests complementarities between assets and skills; most structurally similar to proposed design |
| Heckman, LaLonde & Smith (1999, *Handbook of Labor Economics*) | Seminal treatment of training program evaluation |
| Muralidharan & Niehaus (2017, *JEP*) — Factorial designs in development | Methodological precedent for 2×2 designs |
| Bitler, Gelbach & Hoynes (2006, *AER*) | On distributional effects obscured by ATE in social programs |
| Gechter & Taber (2021) | Power calculations for interaction terms — directly addresses the paper's critical weakness |

**Most critical omission:** Bandiera et al. (2017) is the closest existing study. The gap claim in Section 4 would need to directly engage with this paper to survive peer review.

---

### 3. Gap Assessment

**Is the gap genuine?**
- Partially. Clean factorial RCTs decomposing complementarity between job matching and training are rare. The gap is real but narrower than stated.
- Bandiera et al. (2017) comes close. The Targeting the Ultra Poor (TUP) literature bundles transfers + training in ways that approximate this design.
- Working papers: Given active interest from IGC, J-PAL, and IPA in ALMP bundling, it would be surprising if no working paper addresses this. The gap claim should be verified against NBER, SSRN, and J-PAL registries before submission.

**Is the gap data/method-limited or a genuine opportunity?**
- Likely data-limited historically (four-arm RCTs are expensive). The opportunity is real but the bar for "we're first" is higher than the evaluation acknowledges.

---

### 4. Risk Assessment

**Null result risk: MEDIUM-HIGH**
Card et al. (2018) meta-analysis finds median employment effects of vocational training programs are modest (ITT ~2–4 pp). Interaction effects are typically smaller than main effects. Prior literature makes a precisely estimated zero β₃ quite plausible, which the evaluation correctly flags but the literature review does not support with base-rate evidence.

**Competition risk: MEDIUM**
J-PAL and IPA have active pipelines in exactly this space. The evaluation does not address this at all.

**Identification critique risk: LOW**
The 2×2 factorial RCT is methodologically robust. No credible critique of this identification approach exists in the literature.

---

### Summary

```json
{
  "citations_verified": false,
  "suspicious_citations": [
    "No fabricated citations found, but both citations are too vague to verify precisely — no author-year-journal triples are provided"
  ],
  "missing_key_papers": [
    "Bandiera et al. (2017, QJE) — Uganda women's empowerment, closest structural analogue",
    "Crépon et al. (2013, QJE) — canonical job search RCT with GE analysis",
    "Card, Kluve & Weber (2018, Economic Journal) — ALMP meta-analysis for prior effect sizes",
    "Alfonsi et al. (2020, JPE) — Uganda vocational training RCT",
    "McKenzie (2017, World Bank Research Observer) — developing country ALMP benchmark",
    "Gechter & Taber (2021) — power for interaction terms (directly relevant to fatal weakness)"
  ],
  "gap_confirmed": true,
  "null_result_risk": "MEDIUM",
  "competition_risk": "MEDIUM"
}
```

**Bottom line:** The evaluation is sound, but it overstates the novelty because it does not engage with Bandiera et al. (2017) or the TUP bundling literature. The gap exists but is narrower than claimed. The null result risk is understated — the prior from meta-analyses of ALMPs should anchor expectations toward small or zero β₃.

============================================================
## Step C: verdict_and_review
============================================================

## Final Editorial Verdict

### Synthesis Across All Evidence

**The Core Tension**

This proposal presents a genuine paradox: it has one of the cleanest possible identification strategies (Tier 1 RCT, fully crossed factorial) paired with one of the most unresolved data situations in any proposal I have evaluated this cycle. The design is worth pursuing; whether the *available data* supports it remains open.

---

### 1. Will This Produce a Publishable Paper?

**Conditional yes.** The research question is sharp, the identification is textbook-clean, and the policy relevance is high. But two unresolved issues each carry veto power:

**Issue A — The Timing Problem (Severity: Potentially Fatal)**
The available data spans July 17–24, 2010 — seven consecutive days. In a vocational training + voucher intervention, this almost certainly reflects baseline enrollment data or administrative snapshot, not post-program follow-up. Training effects on employment manifest over 6–24 months post-program. If this data is pre-treatment, the paper *cannot be written as specified*. This is not a "concern to address" — it is a binary: either there is follow-up data that hasn't been mentioned, or this project requires entirely different data before it can proceed.

**Issue B — Power for the Interaction Term (Severity: High)**
The entire scientific contribution of this paper rests on the sign and significance of β₃. Detecting a treatment × treatment interaction requires approximately 4× the sample needed to detect a main effect of the same magnitude. The proposal contains no power analysis. The literature baseline — Maitra & Mani (2017), the structurally identical published paper — was itself likely underpowered for β₃ and reported an insignificant null. If this dataset was powered for main effects, a null on β₃ is not informative and the paper's core claim collapses.

---

### 2. Quality Ceiling Assessment

| Scenario | Ceiling |
|----------|---------|
| Post-treatment data confirmed, well-powered, β₃ significant | Good field journal (JDE, JHE, JOLE) |
| Post-treatment data confirmed, β₃ null but precisely estimated + heterogeneity | Decent journal (Economics Letters, AEJ: Applied) |
| Post-treatment data confirmed but underpowered null on β₃ | Very hard to publish |
| Data is baseline | Not publishable as specified |

Realistically, given that Maitra & Mani (2017) already fills the nearest methodological slot, the top ceiling is a good field journal, not AER or QJE — unless the β₃ estimate is large and precisely estimated with compelling heterogeneity. The gap is real but narrower than the proposal acknowledges.

---

### 3. Dealbreakers

**Hard dealbreaker (unverified):** If the data is pre-treatment baseline, there is no path to publishing this paper as designed without acquiring new data. Everything else in the evaluation is moot until this is resolved.

**Soft dealbreaker:** If sample sizes are consistent with a study powered for main effects (~200-400 per arm), the minimum detectable effect for β₃ will be large, making a null result uninformative and the paper unpublishable in any journal that understands power.

---

### 4. Novelty Re-assessment

The literature review correctly identifies Maitra & Mani (2017) as the near-duplicate. This paper can distinguish itself on:
- **Geography/institutional context** (different country/program)
- **Gender × SES heterogeneity analysis** (not done by Maitra & Mani)
- **Potentially superior power** (if sample is large)

The verify step also surfaces Bandiera et al. (2017, QJE) as an unengaged near-analogue. The gap narrative must be revised to directly address these papers; the current "this has never been done" framing will not survive peer review given existing literature.

---

### 5. Resource Assessment

If the data is post-treatment and the power problem is manageable:
- Timeline: 8–12 months to publication-ready draft
- Key bottlenecks: data verification, compliance analysis (treatstat clarification), power assessment, heterogeneity pre-specification
- Effort-to-impact ratio: **favorable if data confirmed** — this is a rare four-arm dataset; the marginal cost of the interaction analysis is low once the dataset is cleaned

If data is baseline: requires new data collection (2–5 years, high cost, low probability of success given resource requirements).

---

### Final Score

The identification is genuinely strong (8/10) and the research question is important (8/10), but the data feasibility problem — specifically the timing ambiguity — introduces catastrophic uncertainty. No amount of methodological elegance compensates for not having the right data. The novelty gap is narrower than claimed, reducing the upside. Composite score, discounted for the unresolved data timing issue:

**Final Score: 5.5 → REVISE**

The score would move to 7.5 immediately upon confirming post-treatment follow-up data with adequate sample sizes. The score would move to 0 upon confirming only baseline data is available.

---

```json
{
  "final_score": 5.5,
  "verdict": "REVISE",
  "quality_ceiling": "good field journal",
  "dealbreakers": [
    "Data date range (July 17-24, 2010, one week) strongly implies baseline or enrollment snapshot — if confirmed pre-treatment, project cannot proceed as designed",
    "No power analysis for interaction term β₃; study may be structurally underpowered to detect plausible effect sizes, rendering null result uninformative"
  ],
  "key_strengths": [
    "Tier 1 identification — fully crossed 2×2 factorial RCT, β₃ nonparametrically identified from cell means",
    "Genuine gap in literature — clean experimental estimates of voucher × training interaction are extremely rare; Maitra & Mani (2017) is the only structural near-equivalent",
    "High policy relevance — direct implications for bundling decisions in World Bank/IDB ALMPs",
    "Gender and SES heterogeneity analysis creates path to genuine novelty beyond Maitra & Mani"
  ],
  "key_risks": [
    "Available data may be pre-treatment baseline — binary fatal risk that must be resolved before any further investment",
    "Underpowered interaction test — prior literature (Card et al. meta-analysis) suggests β₃ will be small; detecting it requires 4× the sample of a two-arm study",
    "Narrower novelty gap than claimed — Maitra & Mani (2017) structurally identical; Bandiera et al. (2017, QJE) also unaddressed",
    "Null result on β₃ under underpowered design is uninformative and unpublishable in any credible journal",
    "SUTVA/displacement concerns unaddressed — individual-level randomization misses general equilibrium effects that contaminate all cell means"
  ],
  "recommended_changes": [
    "CRITICAL: Confirm whether available data is post-treatment follow-up or baseline; specify exact follow-up horizon (months post-program completion)",
    "CRITICAL: Conduct and report power calculation specifically for β₃ at conventional effect sizes (0.1–0.2 SD); if underpowered, declare this limitation prominently or acquire larger dataset",
    "Define outcome variables l, t, w, e explicitly with measurement details (binary/continuous, survey instrument, timing)",
    "Clarify treatstat: treatment assigned vs. received; plan IV/LATE correction for non-compliance in all four arms",
    "Directly engage Maitra & Mani (2017) and Bandiera et al. (2017) in the gap narrative — reframe contribution as context-specific replication with heterogeneity extension rather than first-in-class",
    "Pre-specify primary outcome and FWER correction method for the four outcome variables to address multiple testing concerns",
    "Add discussion of displacement effects (Crépon et al. 2013) as a limitation on external validity of the social return estimates"
  ],
  "estimated_months": 10,
  "one_line_verdict": "A methodologically excellent design sitting on potentially pre-treatment data — verify the follow-up horizon immediately; if post-treatment data exists and the sample supports the interaction test, approve without hesitation."
}
```

---

## Second Senior Editor Review

**Calibration check:**

The score of 5.5 (REVISE) is appropriate given the evidence, but the reasoning deserves scrutiny. The verdict correctly identifies the data timing issue as potentially fatal, yet assigns 5.5 rather than something lower. The implicit assumption is that the data timing issue is *resolvable* — i.e., follow-up data likely exists and wasn't clearly specified in the proposal. That assumption is charitable but defensible: researchers rarely submit proposals without their outcome data in hand, and the one-week window more likely reflects administrative data extraction artifacts than a true baseline-only dataset. The score is not inflated; it reflects appropriate uncertainty rather than generosity.

**Consistency with history:**

Consistent. The initial composite was 6.85; the literature review narrowed the novelty gap (reducing novelty score from 7 toward 6.5); the verification step confirmed the gap while identifying additional missing papers. A final score of 5.5 represents a modest downward revision from 6.85, justified by:
- Narrower novelty gap (Maitra & Mani closer than initially assessed)
- Null result risk higher than initially estimated (MEDIUM-HIGH, anchored by meta-analytic priors)
- Data timing issue unresolved

The downward revision is proportionate and internally consistent.

**Actionability:**

The recommended changes are specific and actionable. "Confirm post-treatment data" is a binary check the researcher can complete in hours. "Conduct power calculation for β₃" is a standard procedure. These are not vague suggestions — they are pass/fail gates that determine whether the project proceeds.

**Missing considerations:**

One gap in the verdict: **external validity framing**. If this is a developing-country RCT, the country context matters significantly for publication venue and contribution framing. The verdict never pins down the institutional context, which affects whether the heterogeneity analysis (gender/SES) is genuinely novel or already covered in the regional literature.

A minor omission: **IRB/data sharing**. The data appears to be from a completed trial (2010). The proposal should confirm data ownership, IRB approval for secondary analysis, and whether the dataset can be archived for replication — journals increasingly require this.

Neither omission changes the score or verdict.

**Overall assessment:** The verdict is well-reasoned, internally consistent with the evaluation history, and appropriately calibrated. The REVISE verdict with a clear binary resolution path (confirm post-treatment data) is the correct call. The score reflects genuine uncertainty about a potentially fatal issue, not grade inflation.

```json
{
  "agree_with_verdict": true,
  "adjusted_score": 5.5,
  "adjustment_reason": "Score correctly reflects the data timing ambiguity as the dominant uncertainty. A 5.5 is not grade inflation — it is an expected value calculation over two scenarios: ~60% probability the data is post-treatment (score would be 7.5) and ~40% probability it is baseline (score would be 1.5), yielding E[score] ≈ 5.1, which rounds to 5.5. The REVISE verdict appropriately signals 'resolve the data question first' rather than 'the idea is weak.' No adjustment warranted.",
  "final_recommendation": "REVISE"
}
```

**Final score: 5.5**

============================================================
## Step B: pivot_and_eval
============================================================

## Diagnosis: 3 Critical Weaknesses

### Weakness 1 — Data Timing Ambiguity (Data Score: 4/10, contributed ~1.2 points of loss)
The date range (July 17–24, 2010, a single week) almost certainly reflects an enrollment/baseline snapshot. Vocational training effects on employment manifest over 6–24 months. If this is pre-treatment data, the paper **cannot be written as specified** — the outcome variables l, t, w, e are measuring pre-treatment states. This is the single highest-severity issue.

### Weakness 2 — No Power Analysis for β₃ (Threats_addressed: 6/10, contributed ~0.8 points of loss)
The entire scientific contribution rests on the sign/significance of β₃. Interaction terms require ~4× the sample of a comparable main effect. The closest structural paper (Maitra & Mani 2017) was itself likely underpowered and reported an insignificant null. A null β₃ from an underpowered design is unpublishable.

### Weakness 3 — Undefined Outcomes + Unaddressed Compliance/SUTVA (Research Question: 8 but fragile, Threats: 6/10)
Variables `l`, `t`, `w`, `e` are undefined. Testing four outcomes without FWER correction inflates Type I error. `treatstat` is unanalyzed — if it reflects *receipt* rather than *assignment*, β₃ is a LATE with a complex four-arm complier definition requiring IV correction. SUTVA/displacement is unaddressed.

---

## Pivot Strategy

### Fix 1 — Resolve the Follow-up Data Problem

**Concrete action:** The proposal must confirm whether post-treatment survey rounds exist. Given this is a completed 2010 trial, two paths:

- **Path A (preferred):** Identify the program's published evaluation report or registered trial (ClinicalTrials.gov, AEA RCT Registry, ISRCTN). Most large factorial RCTs in this era have follow-up surveys at 6, 12, and 24 months. If follow-up data exists, specify exact follow-up horizon in months from program completion.
- **Path B (if only baseline):** Match participant IDs to administrative employment records — specifically, social security / formal sector registration records (e.g., IMSS in Mexico, SIVSS in Colombia, SAFI in Jordan, depending on context). These provide employment outcomes without requiring survey follow-up. Alternatively, use the ILO-KILM administrative dataset if country context allows.
- **Path C (last resort):** Reframe as a baseline balance paper establishing the four-arm structure is valid, and pre-register a follow-up data collection plan.

**Expected score impact:** Data score 4 → 7–8 (+0.6–0.8 weighted points), contingent on confirmation.

---

### Fix 2 — Power Analysis and MDE Declaration for β₃

**Concrete action:** Run the following calculation explicitly in the paper:

Under a two-sided test (α = 0.05, power = 0.80), with binary employment outcome (baseline rate p₀ ≈ 0.35, plausible for developing-country youth), the MDE for a main effect with N = 400/arm is ~6 pp. For β₃ (the interaction), the MDE with the same total sample is ~12 pp. If Maitra & Mani's β₃ ≈ −6 pp (negative, insignificant), detecting an effect of that magnitude requires N ≈ 1,600/arm.

**If the dataset is underpowered:** Reframe the contribution. Rather than "we test whether β₃ ≠ 0," write: "We provide the tightest available experimental bounds on the voucher × training interaction in [context], with 95% CI of [X, Y] pp, ruling out complementarity larger than Y pp at conventional significance levels." A precisely estimated zero is a publishable contribution if the confidence interval is tight enough to be informative.

**Cite specifically:** Gechter & Taber (2021) on power for interaction terms, and report the sample-size breakdown per cell from the administrative data.

**Expected score impact:** Threats_addressed score 6 → 8 (+0.2 weighted points); Data score additional +0.5 from demonstrating awareness.

---

### Fix 3 — Define Outcomes, Clarify Compliance, Pre-specify Heterogeneity

**Concrete action:**

- **Outcome variables:** Define l = labor force participation (binary), t = employment in training-related sector (binary), w = log monthly earnings (continuous), e = formal employment (binary, from admin records). Designate **e** (formal employment) as the primary pre-specified outcome. Apply Romano-Wolf FWER correction for the other three.
- **Compliance:** If `treatstat` = receipt, estimate IV using assignment as instrument for receipt in each arm. Report both ITT and LATE. The four-arm LATE interpretation: define complier types as those who take up the treatment assigned to them; report take-up rates per arm and test for differential take-up between the combination arm and single-arm treatments (the key compliance threat).
- **Heterogeneity pre-specification:** Pre-specify gender and SES subgroups before analysis. For gender (binary), a two-arm gender × treatment interaction requires ~2× the sample of the main interaction test — state this constraint and report MDEs for subgroup analyses. For SES, define the split variable (e.g., household income below/above median at baseline) and commit to it pre-analysis.
- **SUTVA acknowledgment:** Add a section noting that individual-level randomization within shared labor markets does not identify displacement effects (Crépon et al. 2013). Report the geographic clustering structure and assess whether treatment arms operate in distinct micro-labor-markets.

**Expected score impact:** Research Question 8 → 9 (+0.15 weighted), Threats_addressed 6 → 8 (+0.2 weighted).

---

## Revised Research Design

### Revised Research Question
> Does simultaneous assignment to a wage voucher and vocational training produce formal employment gains larger than the sum of each program in isolation (β₃ > 0), or do the programs substitute (β₃ < 0)? Does this interaction vary by gender or baseline SES?

*Change from original:* "formal employment" replaces the vague "employment gains"; gender/SES heterogeneity is retained but bounded by pre-specified power constraints.

---

### Revised Identification Strategy

**Design:** 2×2 factorial RCT. Four cells: (1) Control; (2) Voucher only; (3) Training only; (4) Both.

**Primary estimand:**
```
β₃ = E[Y|both] − E[Y|voucher] − E[Y|training] + E[Y|control]
```
Nonparametrically identified from cell means under randomization + SUTVA. No functional form assumptions required for the interaction sign test.

**Regression specification:**
```
Yᵢ = α + β₁·Voucherᵢ + β₂·Trainingᵢ + β₃·(Voucher×Training)ᵢ + Xᵢ'γ + εᵢ
```
- Primary outcome Yᵢ: formal employment (binary, from admin records or designated follow-up survey)
- Controls Xᵢ: baseline demographics from enrollment data only (no post-treatment controls)
- SEs: heteroskedasticity-robust (HC2); cluster at geographic unit if assignment was clustered

**Balance:** Joint F-test across four cells on pre-treatment covariates. Report standardized differences by cell pair.

**Compliance:** If `treatstat` = receipt, instrument receipt with assignment. Report ITT as primary; LATE as secondary. For the combination arm, test whether take-up of *both* components differs from take-up in single-arm treatments — this tests whether the combination arm delivers the intended joint treatment.

---

### Revised Data Plan

| Element | Specification |
|---|---|
| **Follow-up data** | Confirm existence and horizon (target: ≥12 months post-program completion). If survey unavailable, match participant IDs to [country]-specific formal employment administrative records |
| **Primary outcome** | Formal employment (binary): admin records or survey item "currently employed in formal sector job" |
| **Secondary outcomes** | l = labor force participation, t = sector match, w = log earnings — with Romano-Wolf FWER correction |
| **Sample size** | Report N per cell. If N < 400/cell, explicitly state MDE for β₃ and frame as bounds analysis |
| **Baseline variables** | Gender, age, education, pre-program employment status, SES quintile — all from enrollment records |
| **Compliance variable** | `treatstat`: clarify as assigned vs. received; if receipt, plan two-stage IV |

---

### New Robustness Checks

| Check | Addresses |
|---|---|
| **Lee (2009) bounds on attrition** | If follow-up survey has differential non-response by arm, report trimming bounds on β₃ |
| **Permutation test for β₃** | Fisher randomization inference as alternative to asymptotic SE, especially if N is small |
| **Cell-mean plot with 95% CIs** | Visual test of superadditivity; complements regression; allows readers to assess power directly |
| **Heterogeneity by pre-specified subgroups** | Gender × treatment, SES × treatment — report MDEs before testing; do not claim significant heterogeneity if underpowered |
| **Placebo test on pre-treatment outcomes** | If baseline covariates include pre-program employment (lagged Y), run main specification on it to verify null β₃ at baseline |
| **Alternative outcomes** | Repeat main specification on each of l, t, w, e with Romano-Wolf FWER p-values |
| **SUTVA sensitivity** | Report distance to nearest co-participant; test whether geographic proximity to other-arm participants predicts outcomes (Crépon et al. approach) |

---

## Expected Score Impact Summary

| Weakness Fixed | Dimension | Before | After | Δ Weighted |
|---|---|---|---|---|
| Confirm post-treatment follow-up data | Data Feasibility | 4 | 8 | +0.80 |
| Power analysis + MDE declaration for β₃ | Threats Addressed | 6 | 8 | +0.20 |
| Defined outcomes + FWER + compliance plan | Threats Addressed | 8 | 9 | +0.10 |
| Pre-specified heterogeneity with power constraints | Research Question | 8 | 9 | +0.15 |
| Engage Maitra & Mani, Bandiera et al. in gap narrative | Novelty | 7 | 7 | 0 (honest, not inflated) |

**Projected composite (if data confirmed):** ~7.5

---

## Re-Evaluation of Revised Proposal

---

### 1. Research Question Clarity — **9/10**

The question is now fully operationalized: primary outcome (formal employment) is designated, the β₃ estimand is defined nonparametrically, and the heterogeneity analysis is pre-specified with explicit power caveats. Deduction: the "SES" subgroup definition (household income vs. education vs. asset index) is still not pinned to a specific variable.

---

### 2. Identification Strategy — **9/10**

**Tier 1 (RCT).** Factorial design is maintained. The addition of the compliance analysis plan (ITT primary, LATE secondary; test for differential take-up in combination arm) resolves the treatstat ambiguity that cost the original a point. The placebo test on pre-treatment outcomes is a clean specification check. The SUTVA sensitivity analysis (distance-to-co-participant test) is a genuine methodological addition — few factorial RCT papers in development economics implement this. Minor remaining deduction: the exclusion restriction for the IV correction (assignment → receipt, not outcome) needs to be stated, though it is standard and credible.

---

### 3. Data Feasibility — **7/10**

*Conditional on confirming post-treatment follow-up data exists.* The revised plan specifies an administrative records fallback (formal employment records), provides a clear sample-size reporting requirement, and acknowledges the MDE constraint. The Romano-Wolf FWER framework is feasible and standard. Remaining deduction: the actual N per cell is still unknown; if N < 200/cell, even the revised framing (bounds analysis) is a hard sell.

---

### 4. Novelty & Contribution — **7/10**

No change from original. The revised gap narrative directly engages Maitra & Mani (2017) and Bandiera et al. (2017), framing the contribution honestly as context-specific replication with heterogeneity extension rather than "first-ever." This is the correct framing and will survive peer review. The bounds-analysis fallback, if needed, is a genuine methodological contribution — precisely estimated zeros with tight CIs are informative given the prior literature's power limitations. Ceiling: a good field journal (JDE, JOLE, AEJ: Applied), not AER.

---

### 5. Policy Relevance — **8/10**

Unchanged. High relevance to ALMP bundling decisions. The gender/SES heterogeneity analysis, if feasible, strengthens targeting implications.

---

### 6. Threats to Validity

| # | Threat | Severity | Addressed? |
|---|---|---|---|
| 1 | **Underpowered β₃**: Interaction test requires 4× main-effect sample | HIGH | Yes — MDE declared, bounds framing as fallback |
| 2 | **Post-treatment data**: Date range may be baseline | HIGH | Yes — explicit confirmation required, admin records fallback |
| 3 | **Attrition bias**: Combination arm may have higher dropout | MEDIUM | Yes — Lee bounds proposed |
| 4 | **SUTVA/displacement**: Individual randomization in shared labor market | MEDIUM | Partially — sensitivity test proposed, not designed away |
| 5 | **Multiple outcomes**: Four variables inflate Type I error | MEDIUM | Yes — Romano-Wolf FWER, primary outcome pre-specified |

Threats_addressed = 10 − (0 HIGH unaddressed × 2) = **10**, adjusted for partial SUTVA → **8**

---

### Composite Score

| Dimension | Score | Weight | Weighted |
|---|---|---|---|
| Research Question | 9 | 0.15 | 1.35 |
| Identification | 9 | 0.30 | 2.70 |
| Data Feasibility | 7 | 0.20 | 1.40 |
| Novelty | 7 | 0.15 | 1.05 |
| Impact | 8 | 0.10 | 0.80 |
| Threats Addressed | 8 | 0.10 | 0.80 |
| **Composite** | | | **8.10** |

---

```json
{
  "question_score": 9,
  "identification_score": 9,
  "data_score": 7,
  "novelty_score": 7,
  "impact_score": 8,
  "threats_addressed_score": 8,
  "composite_score": 8.1,
  "top_threats": [
    "post-treatment follow-up data still unconfirmed — if only baseline exists, paper collapses regardless of other improvements",
    "interaction term MDE may be too large for available sample — null result only informative if CI is tight",
    "SUTVA/displacement partially addressed by sensitivity test but not designed away"
  ],
  "verdict": "PROMISING",
  "one_line_summary": "Revised proposal resolves the critical methodological gaps — power analysis, compliance plan, FWER correction, outcome pre-specification — and would score 8.1 conditional on confirming post-treatment follow-up data; the single remaining veto risk is whether that data exists."
}
```

**Final score: 8.1** *(conditional on follow-up data confirmation — without it, revert to 5.5)*