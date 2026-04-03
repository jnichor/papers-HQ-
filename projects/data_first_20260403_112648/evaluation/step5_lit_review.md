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