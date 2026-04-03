## Diagnosis: 3 Critical Weaknesses

**1. Threats Unaddressed (5/10 → pulling composite down 0.5 pts vs. initial)**
Two HIGH-severity threats are completely unaddressed: social desirability bias on a politically toxic topic, and the pre-registration absence that makes LASSO selection HARK-adjacent. Combined, these reduce the threats score to 5/10 under the formula.

**2. Novelty Eroded by Competition Risk (5/10)**
The mechanism is asserted ("historical weight") but never unpacked or tested. Without knowing *why* apartheid moves people differently from persecution, the paper is atheoretical advocacy research. In an active research space (Israel/ICC, November 2024 arrest warrants), a paper without a mechanism claim is easily scooped by a more theoretically ambitious competitor.

**3. Impact Ceiling Capped by Null-Result Risk (6/10)**
Equivalence framing effects are notoriously small (Chong & Druckman 2007: 4–8 pp realistic MDE). High-prior respondents — the policy-relevant group — are the least movable. Without knowing who is movable and *why*, the CATE analysis is descriptive rather than actionable.

---

## Pivot Strategy

### Fix 1: Pre-Registration + Specification Curve (addresses Threats score)

**Problem:** LASSO covariate selection without pre-registration is HARK-adjacent; referees will demand specification robustness.

**Concrete fix:**
- Post a pre-analysis plan to OSF **today** with honest disclosure language: *"This analysis plan is filed post-data-collection but pre-analysis. All specifications below were determined before examining treatment-outcome relationships."*
- Run a **specification curve** across four estimators: (a) raw OLS, no covariates; (b) OLS + demographic controls; (c) OLS + LASSO-selected controls; (d) IPW with propensity score. Report all four ATEs in a single figure. If they converge within ±1.5 pp, the LASSO concern is neutralized.
- Expected score impact: Threats Addressed +2 pts (eliminates one HIGH threat).

### Fix 2: Mechanism Test Using Existing Covariates (addresses Novelty)

**Problem:** "Historical weight" is the mechanism but it's never operationalized. This makes the paper a framing-effects application, not a theoretical contribution.

**Concrete fix — testable with data already in hand:**
- Identify whether the survey contains: (a) any South Africa / apartheid knowledge item, (b) racial justice attitudes (BLM support, systemic racism beliefs), or (c) familiarity with the ICC. If any exist, pre-specify a **mechanism moderation test**: does the apartheid > persecution gap widen for respondents with higher apartheid prototype knowledge? Narrowing it to:

  > H_mech: The apartheid label effect on ICC support is larger among respondents with higher prior knowledge of South African apartheid, consistent with a historical-resonance mechanism (not a generic negativity-labeling or racial-justice-priming mechanism).

- If racial justice attitudes are available, add a **competing mechanism test**: H_rival: the effect is larger among respondents high on racial justice attitudes, consistent with moral priming rather than legal precision.
- This 2×2 mechanism decomposition (Historical Knowledge × Racial Justice Attitudes, both continuous, interacted with treatment) turns a simple A/B test into a genuine theoretical contribution.
- Expected score impact: Novelty +2 pts; Impact +1 pt.

### Fix 3: Address Demand Effects Directly (addresses Threats score)

**Problem:** Apartheid is politically charged; respondents may moderate toward perceived social norms, compressing true effects.

**Concrete fix — requires a small supplemental data collection (N ≈ 400, ~$800 on Prolific):**
- Add a **list experiment** on the ICC support item: embed the ICC referral item in a list of 3 innocuous items (control) vs. 4 items including ICC referral (treatment). Compare means to recover a demand-effect-free prevalence estimate.
- Alternatively (no new data needed): stratify existing sample by **Crowne-Marlowe Social Desirability** scores if the survey included such a scale — or proxy with a self-report "I care about what others think" item. Show that the label effect holds (or strengthens) among low-social-desirability respondents.
- If neither is available: add a **falsification test** using a politically neutral outcome (e.g., support for ICC referral regarding a third-party conflict with no Israel framing) to show that the label effect is specific to the Israel context, not a generic demand artifact.
- Expected score impact: Threats Addressed +1 pt (partially addresses second HIGH threat).

---

## Revised Proposal

### Revised Research Question
> Does labeling Israeli actions as 'apartheid' vs. 'persecution' increase support for ICC referral, and is this effect driven by historical-resonance activation (knowledge of South African apartheid) or by racial-justice moral priming — or are both mechanisms operative for distinct subgroups?

The original question is preserved but extended to include a mechanism test that distinguishes two theoretically competing explanations for the expected effect.

### Revised Identification Strategy
**Core:** Random assignment to apartheid vs. persecution label (Tier 1 RCT, unchanged). Internal validity is not at issue.

**Added layers:**
1. **Specification curve** (4 estimators) reported alongside the primary ATE. Pre-registered post-collection with disclosure.
2. **Mechanism moderation regressions** (pre-specified):
   - `ICC_support ~ treat × apartheid_knowledge + controls` — tests historical-resonance mechanism
   - `ICC_support ~ treat × racial_justice_attitudes + controls` — tests moral-priming mechanism
   - Both interacted simultaneously: `treat × apartheid_knowledge × racial_justice_attitudes` — identifies which mechanism dominates
3. **Demand effects robustness**: If list experiment data collected, report alongside direct measure. If not, report demand-effects-stratified CATE.

### Revised Data Plan
| Source | Purpose | Already collected? |
|--------|---------|-------------------|
| Original N=1,185 survey | Primary ATE + CATE | Yes |
| OSF post-analysis pre-registration | Credibility | File immediately |
| CPS benchmarks | Sample representativeness table | No cost — public data |
| Prolific supplemental wave (N=400) | List experiment for demand-effects robustness | Optional, ~$800 |

**Minimum viable paper:** Original data + OSF registration + specification curve + mechanism test using existing covariates. The supplemental wave is a strength-add, not a requirement.

### Revised Sample Documentation
Document the following in Table 1 or appendix:
- Recruitment platform (Prolific/Lucid/MTurk — name it)
- Demographic comparison to CPS: age, gender, education, race
- Attention check pass rate and robustness of ATE excluding failures
- Power analysis retrospectively: at N=1,185, the study is powered at 80% to detect effects ≥ 4.5 pp (assuming σ=0.4 on a 0-1 outcome) — confirm this is above the realistic MDE for equivalence framing

### New Robustness Checks
1. **Specification curve** (4 estimators as above)
2. **Attention-filter robustness**: Drop respondents failing ≥1 attention check; report ATE change
3. **Mechanism moderation test** (pre-specified, see above)
4. **Demand-effects stratification** (low vs. high social desirability scores)
5. **Outcome operationalization robustness**: If multiple ICC-support items exist, report ATE on each separately and on an index; if only one item, flag as limitation

---

## Expected Score Impact Summary

| Fix | Dimension affected | Score change |
|-----|--------------------|-------------|
| OSF pre-registration + specification curve | Threats Addressed | +2 |
| Mechanism test (historical resonance vs. racial justice) | Novelty | +2 |
| Mechanism test (actionable CATE implications) | Impact | +1 |
| Demand effects robustness (stratification or list exp.) | Threats Addressed | +1 |
| Sample documentation + power analysis | Data Feasibility | ±0 (confirms existing score) |

---

## Post-Pivot Re-Evaluation

### 1. Research Question Clarity — **9/10**

The revised question is specific, causal, and now theoretically grounded. The mechanism decomposition (historical resonance vs. racial justice priming) transforms a two-cell A/B test into a test of competing theoretical accounts. Minor deduction: the mechanism hypotheses require additional covariates whose availability is not yet confirmed.

---

### 2. Identification Strategy — **8/10**

**Source of exogenous variation:** Random assignment to label condition. Tier 1 (RCT). Unchanged and credible.

The specification curve and pre-registration disclosure address the most significant execution concern. The mechanism moderation tests are observational (non-randomized moderators), but this is standard in heterogeneous treatment effects analysis — the RCT randomizes treatment, moderation is descriptive not causal. Reviewers will accept this framing if stated honestly.

**Identification Tier: Tier 1.** Internal validity remains strong.

**Remaining concern:** The mechanism moderators (apartheid knowledge, racial justice attitudes) are post-treatment covariates if measured *after* treatment exposure — this would make the mechanism test uninterpretable. They must be measured in a pre-treatment block or identified as pre-treatment demographics. This is a real risk that cannot be resolved without knowing the survey instrument.

---

### 3. Data Feasibility — **8/10**

Data in hand. Sample size adequate for main effects. Slight deduction from 9 to 8: feasibility of the mechanism test depends on whether the survey includes the required pre-treatment moderator items (apartheid knowledge, racial justice attitudes). If these items are absent or post-treatment, Fix 2 cannot be executed without a new data collection wave.

---

### 4. Novelty & Contribution — **7/10**

The mechanism decomposition is the key upgrade. Testing *why* apartheid moves people (historical resonance vs. racial justice priming vs. legal precision signaling) is a genuine theoretical contribution to both the framing effects literature and the ICC public opinion literature. This fills the gap more completely than a pure A/B test — the result is citable regardless of whether the ATE is null (mechanism heterogeneity can coexist with zero ATE).

Competition risk remains HIGH but the mechanism angle reduces vulnerability: a competing paper that only estimates the ATE cannot scoop the mechanism findings.

---

### 5. Policy Relevance / Impact — **7/10**

The mechanism result is directly actionable: if the effect is driven by racial justice priming, advocacy organizations should target racial justice–engaged audiences; if by historical resonance, targeting should condition on apartheid knowledge. This specificity upgrades impact from 6 to 7.

---

### 6. Threats to Validity

| Threat | Severity | Addressed? |
|--------|----------|------------|
| Pre-registration / HARK-adjacent LASSO | HIGH | **Yes** — OSF post-collection registration + specification curve |
| Social desirability / demand effects | HIGH | **Partially** — demand-effects stratification; list experiment optional |
| Sample non-representativeness | HIGH | **Partially** — CPS comparison table documented; does not fix MTurk/Prolific limits |
| Label comprehension failure | MEDIUM | No — still no comprehension check mentioned |
| Mechanism moderators post-treatment | MEDIUM | No — depends on survey instrument; could invalidate Fix 2 |

**Threats_addressed** = 10 − (1 unaddressed HIGH × 2) = **8**

*(Two HIGH threats are now at least partially addressed; one residual HIGH remains for sample non-representativeness which cannot be fully fixed without a new nationally representative wave.)*

---

### Composite Score

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|---------|
| Research Question | 9 | 0.15 | 1.35 |
| Identification | 8 | 0.30 | 2.40 |
| Data Feasibility | 8 | 0.20 | 1.60 |
| Novelty | 7 | 0.15 | 1.05 |
| Impact | 7 | 0.10 | 0.70 |
| Threats Addressed | 8 | 0.10 | 0.80 |
| **Total** | | | **7.90** |

---

```json
{
  "question_score": 9,
  "identification_score": 8,
  "data_score": 8,
  "novelty_score": 7,
  "impact_score": 7,
  "threats_addressed_score": 8,
  "composite_score": 7.9,
  "top_threats": [
    "Sample non-representativeness: platform sample (Prolific/Lucid/MTurk) limits generalizability to general publics and policymakers — CPS comparison partially mitigates but does not resolve",
    "Mechanism moderators may be post-treatment: if apartheid knowledge and racial justice attitudes were measured after treatment exposure, the mechanism test is uninterpretable — instrument must be reviewed immediately",
    "Label comprehension failure still unaddressed: no manipulation check confirms respondents distinguish apartheid from persecution legally vs. rhetorically"
  ],
  "verdict": "PROMISING",
  "one_line_summary": "Upgraded from a clean A/B test to a mechanism-decomposing RCT; pre-registration + specification curve neutralize the HARK concern, and the historical-resonance vs. racial-justice-priming test is genuinely novel — but the mechanism test is only credible if moderators were measured pre-treatment, which must be verified immediately."
}
```

**Final score: 7.9 / 10**

---

### Net Score Change: +0.9 points (7.0 → 7.9)

The three fixes account for the gain as follows:

| Fix | Points added |
|-----|-------------|
| OSF pre-registration + specification curve | +0.30 (threats: 5→8, weighted at 0.10) |
| Mechanism test (novelty) | +0.30 (novelty: 5→7, weighted at 0.15) |
| Mechanism test (impact) + demand-effects work | +0.10 + 0.10 (impact 6→7; threats partial) |
| Research question upgrade | +0.15 (Q: 8→9, weighted at 0.15) |

The single highest-leverage action is filing the OSF pre-analysis plan *before* running any regressions. That single step removes the most damaging credibility threat and costs approximately one hour of work.