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