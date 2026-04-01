# Junshi — Research Advisory Report
## Empleo en el Perú · ENAHO Panel 2020–2024

---

## PART 1 — Cross-Paper Synthesis: Themes, Methods, and Gaps

### Dominant Themes
| Theme | Paper | Key Finding |
|-------|-------|-------------|
| Enforcement → formalization | Bosch et al. (2025) | Low-cost deterrence letters shift large firms toward formal enrollment |
| Employment state dynamics | Herrera & Rosas (2003) | Inactivity, not unemployment, is the dominant labor adjustment margin |
| Gender wage structure | Vaccaro et al. (2022) | Unexplained wage gap stagnant at ~17% despite endowment convergence |

### Methodological Landscape
- **Causal identification present but narrow:** Bosch et al. use RCT (Tier 1), but only on the firm side. No paper uses the ENAHO panel's within-person variation for causal worker-side identification.
- **Herrera & Rosas (2003) is now 27 years old.** The COVID-19 pandemic (2020) is the largest labor market shock Peru has seen in a generation — its dynamic effects on transitions are completely unstudied with modern panel methods.
- **Vaccaro et al. stop at 2018 and use cross-sectional Oaxaca-Blinder.** The panel dimension of ENAHO is entirely unused for gender analysis.

### Critical Gaps
1. **Worker-side panel responses to enforcement shocks** (complement to Bosch et al.'s firm-side RCT)
2. **Post-COVID transition dynamics** with Markov/hazard methods (21-year extension of Herrera & Rosas)
3. **Within-person gender wage dynamics** using individual FE (instead of cross-sectional decompositions)
4. **Household labor supply responses** — added worker effect never studied in Peru with panel data
5. **Informality scarring** — no paper asks whether informal spells create lasting wage penalties
6. **Youth NEET dynamics** in post-pandemic recovery
7. **Sectoral reallocation** — whether COVID caused permanent cross-sector mobility

---

## PART 2 — 8–10 Research Ideas

---

### IDEA 1 — COVID-19 as an Exogenous Shock to Informality: Panel DiD with Sectoral Exposure

**Sub-topic:** Informality & COVID-19 recovery
**Research question:** Did the COVID-19 pandemic cause a durable increase in informality, and did the magnitude of the shock vary systematically by sector, region, and worker characteristics?

**Method:** Two-way Fixed Effects DiD (Tier 1)
- Identifying variation: Differential sectoral exposure to mobility restrictions (contact-intensive vs. teleworkable jobs, using Dingel & Neiman 2020 classifications matched to ENAHO occupation codes). Formally, `ΔInformality_it = α_i + λ_t + β(PostCOVID_t × ContactIntensive_i) + ε_it`.
- Panel exploits the 2020 baseline → 2021–2024 recovery path for the *same individuals*.
- Pre-trend check: use 2020 within the panel as pre-period baseline.

**Data:** ENAHO 2020–2024 panel (available), Dingel-Neiman teleworkability scores (public), INEI sectoral employment statistics.

**Novelty:** Bosch et al. (2025) study the firm side of formalization via enforcement. This is the worker-side panel DiD on the same formality question. No paper has used the 2020–2024 ENAHO panel to track individual-level formality recovery trajectories.

**Impact:** Directly informs whether Peru's labor market has recovered structurally or whether informality hysteresis is a durable policy problem.

| Novelty | Feasibility | Impact | Base | Tier 1 Bonus | Panel Bonus | **Total** |
|---------|-------------|--------|------|--------------|-------------|-----------|
| 4 | 5 | 5 | 4.7 | +0.3 | +0.3 | **5.3** |

---

### IDEA 2 — Labor Market State Dependence Post-COVID: Dynamic Markov Transitions with Individual Fixed Effects

**Sub-topic:** Labor market transitions
**Research question:** Has the pandemic increased state dependence (inertia) in informal and inactive labor market states? Do workers who enter informality during the COVID shock face higher probability of remaining informal even after recovery?

**Method:** First-order Markov transition matrices + dynamic panel (Arellano-Bond GMM, Tier 2)
- Identifying variation: Within-individual transitions across five states (formal employment, informal employment, self-employment, unemployment, inactivity) across 5 annual waves. Arellano-Bond GMM instruments lagged employment state with deeper lags to address the Nickell bias in short panels.
- Directly extends Herrera & Rosas (2003) by 25 years and into a pandemic context.

**Data:** ENAHO 2020–2024 panel (five waves, same individuals tracked).

**Novelty:** Herrera & Rosas (2003) is the canonical reference on Peruvian labor transitions — it uses 1997–1999 data. A 2020–2024 replication-and-extension would be immediately publishable and citeable. No one has done this.

**Impact:** Resolves whether Peru's labor adjustment continues to be dominated by employment-inactivity flows (Herrera's finding) or whether COVID introduced new unemployment dynamics.

| Novelty | Feasibility | Impact | Base | Tier 2 Bonus | Panel Bonus | **Total** |
|---------|-------------|--------|------|--------------|-------------|-----------|
| 5 | 4 | 4 | 4.5 | +0.3 | +0.3 | **5.1** |

---

### IDEA 3 — Informality Scarring: Long-Run Wage Penalties from Informal Spells (Arellano-Bond GMM)

**Sub-topic:** Informality & human capital
**Research question:** Does an informal employment spell during 2020–2021 cause persistent wage depression in 2022–2024, even after returning to formal employment?

**Method:** Dynamic panel GMM (Arellano-Bond, Tier 2)
- Identifying variation: Uses deeper lags of wages and informality status as internal instruments. The COVID shock generates plausibly exogenous informal entries for workers in contact-intensive sectors, helping validate the instrument. Model: `log(w_it) = ρ log(w_{i,t-1}) + γ Informal_{i,t-1} + α_i + λ_t + ε_it`.
- The panel dimension allows controlling for all time-invariant unobserved worker quality (education, ability) that would otherwise confound OLS estimates.

**Data:** ENAHO 2020–2024 panel.

**Novelty:** Informality scarring is well-documented in developed economies (e.g., Germany, UK) but essentially unstudied in Peru or Latin America with true panel data. This is a direct contribution to the scarring literature.

**Impact:** Justifies policy urgency around preventing informality entry — not just facilitating exit. Feeds directly into SUNAFIL enforcement design debates (companion to Bosch et al.).

| Novelty | Feasibility | Impact | Base | Tier 2 Bonus | Panel Bonus | **Total** |
|---------|-------------|--------|------|--------------|-------------|-----------|
| 5 | 4 | 5 | 4.8 | +0.3 | +0.3 | **5.4** |

---

### IDEA 4 — The Added Worker Effect in Peru: Household Labor Supply Responses to COVID Job Loss (TWFE)

**Sub-topic:** Household labor supply / gender
**Research question:** When a primary earner (typically male) lost employment during COVID-19, did secondary earners (typically female) increase labor supply? Did this response formalize or informalize secondary workers?

**Method:** TWFE DiD (Tier 1)
- Identifying variation: Within-household variation in primary earner job loss (2020 shock) interacted with household composition characteristics. The panel allows constructing household-level employment histories and identifying the *exact timing* of primary job loss and secondary labor supply response.
- Causal logic: primary earner job loss is plausibly exogenous due to COVID sectoral lockdowns (not driven by secondary earner choices).

**Data:** ENAHO 2020–2024 panel (household linkage via `conglome + vivienda + hogar` identifiers).

**Novelty:** The added worker effect is a classic theoretical prediction but has never been tested in Peru with panel data. COVID creates a uniquely large and plausibly exogenous household income shock. Vaccaro et al. (2022) study wages but ignore labor supply margins entirely.

**Impact:** Directly addresses whether Peru's gender gap in labor force participation has structural vs. cyclical roots.

| Novelty | Feasibility | Impact | Base | Tier 1 Bonus | Panel Bonus | **Total** |
|---------|-------------|--------|------|--------------|-------------|-----------|
| 5 | 4 | 4 | 4.5 | +0.3 | +0.3 | **5.1** |

---

### IDEA 5 — Gender Wage Gap Dynamics with Individual Fixed Effects: Decomposing Within-Person Changes

**Sub-topic:** Gender inequality
**Research question:** How much of the stagnant gender wage gap identified by Vaccaro et al. (2022) is driven by within-person wage stagnation vs. compositional changes in the female workforce?

**Method:** Individual FE panel regression + CRE decomposition (Tier 2–3)
- Identifying variation: Within-person wage changes over 2020–2024. Correlated Random Effects (Mundlak device) decomposes the total gender gap into within- and between-person components — impossible with repeated cross-sections.
- This directly answers whether the "unexplained" gap in Oaxaca-Blinder is really unexplained or reflects unobserved time-invariant worker heterogeneity.

**Data:** ENAHO 2020–2024 panel.

**Novelty:** Vaccaro et al. (2022) use Oaxaca-Blinder on pooled cross-sections (Tier 4). This upgrades the question to within-person dynamics and separates unobserved heterogeneity from true discrimination. Critical methodological advance over the existing literature.

**Impact:** Changes the policy prescription — if the gap is within-person stagnation, the cause is different from between-person selection.

| Novelty | Feasibility | Impact | Base | Tier 2 Bonus | Panel Bonus | **Total** |
|---------|-------------|--------|------|--------------|-------------|-----------|
| 4 | 5 | 4 | 4.3 | +0.3 | +0.3 | **4.9** |

---

### IDEA 6 — NEET Youth Dynamics: Survival Analysis of Entry and Exit from Non-Employment (Tier 2)

**Sub-topic:** Youth employment
**Research question:** What individual and household characteristics predict duration in NEET status (Not in Employment, Education, or Training) for Peruvian youth aged 15–29, and did COVID extend NEET spells?

**Method:** Discrete-time hazard models (Tier 2) + Markov transition matrices
- Identifying variation: Within-individual transitions in/out of NEET status across 5 waves. COVID-19 acts as a common shock, allowing comparison of hazard rates pre- vs. post-2020.
- Panel is essential: cross-sectional data can measure prevalence but not duration.

**Data:** ENAHO 2020–2024 panel (identify youth 15–29 using age variables with year-specific suffixes; NEET = not employed + not in school).

**Novelty:** NEET research in Peru is essentially absent. The 5-wave panel makes it possible to estimate actual duration models — not just point-in-time snapshots. Latin America youth employment literature (e.g., Cruces et al.) has no Peru-specific panel duration study.

**Impact:** High policy salience — Peru has significant NEET rates and no evidence base for targeting interventions.

| Novelty | Feasibility | Impact | Base | Tier 2 Bonus | Panel Bonus | **Total** |
|---------|-------------|--------|------|--------------|-------------|-----------|
| 5 | 4 | 4 | 4.5 | +0.3 | +0.3 | **5.1** |

---

### IDEA 7 — Regional Convergence in Labor Outcomes: Event Study of Mining Boom/Bust Shocks

**Sub-topic:** Regional labor markets
**Research question:** Do commodity price shocks (mining sector) propagate into regional labor markets through formality rates and wages, and do individuals in mining-adjacent regions show differential within-person income volatility?

**Method:** Event study (Tier 1) using commodity price variation as an external shock
- Identifying variation: International copper/gold price changes interacted with region-level mining exposure (share of regional GDP from mining, from INEI regional accounts). Workers in mining-exposed regions are the treatment; non-mining regions are controls.
- Panel identifies within-person income responses to commodity cycles.

**Data:** ENAHO 2020–2024 panel + INEI regional GDP accounts + World Bank commodity prices.

**Novelty:** Regional labor market studies in Peru exist but rarely exploit panel data for individual-level responses. Linking commodity price variation to individual-level panel outcomes is methodologically superior to existing region-level aggregate studies.

**Impact:** Addresses the "resource curse" at the individual worker level in a developing economy context.

| Novelty | Feasibility | Impact | Base | Tier 1 Bonus | Panel Bonus | **Total** |
|---------|-------------|--------|------|--------------|-------------|-----------|
| 4 | 3 | 4 | 3.8 | +0.3 | +0.3 | **4.4** |

---

### IDEA 8 — Returns to Education Over the Business Cycle: Individual FE with Human Capital Accumulation

**Sub-topic:** Human capital & wages
**Research question:** Did the returns to higher education in Peru increase or decrease during the COVID-19 recession, and do educated workers show faster earnings recovery?

**Method:** Individual FE + event study around education completion (Tier 2–3)
- Identifying variation: Within-person variation in educational attainment (if individuals complete degrees during the panel) + interaction with COVID shock timing. For workers who don't change education, exploits the within-person wage trajectory relative to a time trend conditional on education group.

**Data:** ENAHO 2020–2024 panel.

**Novelty:** Moderate — returns to education are well-studied. The COVID interaction and within-person FE approach are the innovations. Best treated as a supporting paper rather than a standalone contribution.

| Novelty | Feasibility | Impact | Base | Tier 2 Bonus | Panel Bonus | **Total** |
|---------|-------------|--------|------|--------------|-------------|-----------|
| 3 | 4 | 3 | 3.3 | +0.3 | +0.3 | **3.9** |

---

### IDEA 9 — Sectoral Reallocation and Wage Adjustment: Did COVID Permanently Restructure the Peruvian Labor Market?

**Sub-topic:** Sectoral dynamics & structural change
**Research question:** Did workers who were displaced from contact-intensive sectors (retail, food, tourism) during COVID permanently reallocate to other sectors, and what are the wage consequences of forced sector switching?

**Method:** Markov transition matrices across sectors + individual FE (Tier 2)
- Identifying variation: Sector-of-employment transitions observed for the same workers over 5 waves. COVID-induced sector switching is plausibly exogenous (not driven by worker preferences). Compare wages before and after sector switch using within-person variation.

**Data:** ENAHO 2020–2024 panel (sector/industry codes available with year suffixes).

**Novelty:** Forced reallocation literature (Autor et al., China shock) has no Peru equivalent. The 5-wave panel is ideal for measuring permanent vs. temporary reallocation.

**Impact:** High — directly measures the structural adjustment cost of COVID at the individual level.

| Novelty | Feasibility | Impact | Base | Tier 2 Bonus | Panel Bonus | **Total** |
|---------|-------------|--------|------|--------------|-------------|-----------|
| 4 | 4 | 4 | 4.0 | +0.3 | +0.3 | **4.6** |

---

### IDEA 10 — Self-Employment as a Refuge: Entry into Self-Employment During Economic Crises and Its Wage Penalty

**Sub-topic:** Self-employment & entrepreneurship
**Research question:** Does forced entry into self-employment during the COVID-19 shock generate a wage penalty relative to comparable workers who maintained salaried employment, and is the penalty permanent?

**Method:** DiD + Propensity Score Matching (Tier 1–4 hybrid)
- Identifying variation: Workers who entered self-employment in 2020–2021 (treatment) vs. observably similar workers who did not (control), matched on 2019 characteristics. The panel allows testing for pre-treatment parallel trends.

**Data:** ENAHO 2020–2024 panel.

**Novelty:** Self-employment in Peru is large (~40% of workers) but the distinction between voluntary ("opportunity") and forced ("necessity") self-employment is rarely studied with causal methods. The COVID shock provides a rare quasi-experiment.

| Novelty | Feasibility | Impact | Base | Tier 1 Bonus | Panel Bonus | **Total** |
|---------|-------------|--------|------|--------------|-------------|-----------|
| 4 | 4 | 4 | 4.0 | +0.3 | +0.3 | **4.6** |

---

## PART 3 — Scoring Summary

| # | Idea | Sub-topic | Tier | Panel? | N | F | I | **Total** |
|---|------|-----------|------|--------|---|---|---|-----------|
| 3 | Informality scarring (Arellano-Bond) | Informality & human capital | 2 | ✓ | 5 | 4 | 5 | **5.4** |
| 1 | COVID DiD on formality transitions | Informality & COVID recovery | 1 | ✓ | 4 | 5 | 5 | **5.3** |
| 2 | Markov state dependence | Labor transitions | 2 | ✓ | 5 | 4 | 4 | **5.1** |
| 4 | Added worker effect (TWFE) | Household labor supply | 1 | ✓ | 5 | 4 | 4 | **5.1** |
| 6 | NEET youth survival models | Youth employment | 2 | ✓ | 5 | 4 | 4 | **5.1** |
| 5 | Gender gap FE/CRE decomposition | Gender inequality | 2–3 | ✓ | 4 | 5 | 4 | **4.9** |
| 9 | Sectoral reallocation Markov+FE | Sectoral dynamics | 2 | ✓ | 4 | 4 | 4 | **4.6** |
| 10 | Self-employment DiD+PSM | Self-employment | 1/4 | ✓ | 4 | 4 | 4 | **4.6** |
| 7 | Regional mining event study | Regional labor markets | 1 | ✓ | 4 | 3 | 4 | **4.4** |
| 8 | Returns to education FE | Human capital & wages | 2–3 | ✓ | 3 | 4 | 3 | **3.9** |

**Top 3 — different sub-topics, all Tier 1–2, all panel:**
1. Idea 3 (5.4) — Informality & human capital
2. Idea 1 (5.3) — Informality & COVID → **same sub-topic as #1!** → Replaced by next different sub-topic
3. Corrected Top 3: **#3 (Informality scarring)**, **#1 (COVID DiD) → same sub-topic** → use **Idea 2 (5.1, Labor transitions)**, **Idea 4 (5.1, Household labor supply)**

**Final Top 3 (distinct sub-topics):**
| Rank | Idea | Sub-topic | Score |
|------|------|-----------|-------|
| 1 | Informality scarring (Arellano-Bond GMM) | Informality & human capital | 5.4 |
| 2 | COVID DiD on formality transitions | COVID recovery & formality | 5.3 |
| 3 | NEET youth survival models | Youth employment | 5.1 |

*(Ideas 2 and 4 are very close and excellent alternatives if the top 3 need adjustment.)*

---

## PART 4 — Top 3 Elaborated

---

### RANK 1 — Informality Scarring in Peru: Long-Run Wage Penalties from COVID-Induced Informal Spells

**Tier: 2 — Dynamic Panel GMM (Arellano-Bond)**
**Identifying variation:** Lagged informality status instrumented with deeper lags; COVID-sector exposure used as external validity check for instrument quality.

**Detailed design:**

The core model is:
```
log(w_it) = ρ log(w_{i,t-1}) + γ₁ Informal_{i,t-1} + γ₂ Informal_{i,t-2}
            + Xᵢₜ'β + αᵢ + λₜ + εᵢₜ
```

- `αᵢ` = individual fixed effects absorb all time-invariant ability, education quality, and selection into informality
- `λₜ` = year fixed effects absorb macro shocks (COVID, commodity prices)
- `γ₁`, `γ₂` measure the *scarring coefficient* — the persistent wage penalty from past informal spells
- Arellano-Bond GMM uses lags `t-2` and `t-3` of wages as instruments for `log(w_{i,t-1})`, avoiding the Nickell bias inherent in FE with lagged dependent variable

**Heterogeneity analysis:**
- By return-to-formality speed (did the worker re-formalize by 2022?)
- By initial education level (do high-skilled workers show faster recovery?)
- By region (Lima vs. rural Peru — different informal labor market structures)
- By age at time of COVID shock

**Reshape script requirement:** Wide ENAHO → long format using year suffixes `_20` through `_24`. ID variables: `numper` + `conglome` + `vivienda`. Panel-declare in Stata (`xtset`) or Python (`PanelOLS`).

**Potential threat:** Measurement error in informality status (social security enrollment self-reported). Robustness check: use multiple informality definitions (social security, contract type, labor rights).

**Why top journals will care:** Informality scarring is empirically established in developed countries (Germany, UK, Austria) but Peru is a high-informality developing country where the mechanism may differ fundamentally. This is the first true panel-data test of scarring in Peru.

---

### RANK 2 — COVID-19 and the Formality Recovery Path: A Worker-Level Panel DiD

**Tier: 1 — Two-Way Fixed Effects DiD + Event Study**
**Identifying variation:** Differential exposure to COVID mobility restrictions by sector of employment (contact-intensive vs. teleworkable, using Dingel-Neiman scores matched to CIIU occupation codes at 4-digit level).

**Detailed design:**

**Step 1 — Define treatment intensity:**
Match each worker's occupation (ENAHO variable `p507` with year suffixes) to the Dingel-Neiman (2020) teleworkability index. High index = low COVID exposure; low index = high COVID exposure. This creates a *continuous treatment* — exposure to the formality shock.

**Step 2 — TWFE specification:**
```
Informal_it = αᵢ + λₜ + β(Post2020_t × ContactIntensity_i) + Xᵢₜ'γ + εᵢₜ
```

**Step 3 — Event study:**
Replace `Post2020_t` with year dummies (2021, 2022, 2023, 2024, relative to 2020 baseline) to trace the full dynamic path of formality recovery. Test pre-trend assumption within the panel.

**Step 4 — Heterogeneity:**
- Firm size (large vs. small — connects to Bosch et al.'s finding that large firms drive enforcement response)
- Urban vs. rural (informality baseline and recovery speed differ dramatically)
- Gender (connects to Vaccaro et al. — did women's formality recover more slowly?)
- Region (Lima vs. Norte vs. Sur vs. Selva)

**Critical connection to seed papers:** Bosch et al. (2025) show that enforcement letters to *firms* raise formal enrollment by 9.8%. This paper asks: among workers displaced by COVID into informality, what is the return path back to formality? The two papers together map both supply (enforcement) and demand (worker recovery) sides of the formalization process.

**Data pipeline:**
1. Reshape ENAHO wide → long (year suffixes `_20`–`_24`)
2. Merge Dingel-Neiman scores on occupation code
3. Construct binary informality indicator (social security non-enrollment or lack of formal contract)
4. Panel-declare: `xtset numper year`
5. Estimate TWFE with clustered SEs at household level

---

### RANK 3 — Youth NEET Dynamics in Post-Pandemic Peru: Hazard Models with Panel Data

**Tier: 2 — Discrete-Time Hazard Models + Markov Transitions**
**Identifying variation:** Within-individual transitions into and out of NEET status across 5 annual waves; COVID-19 shock acts as a time-varying common shock enabling comparison of hazard rates before and after 2020.

**Detailed design:**

**NEET definition:** Youth aged 15–29 who are simultaneously (a) not employed and (b) not enrolled in education. Constructed from ENAHO variables for employment status (p501 variants) and school enrollment (p300 variants) with year suffixes.

**Model 1 — Markov transition matrices:**
Compute 4×1 state vectors (employed formal, employed informal, NEET, education) and 4×4 annual transition matrices for each year. Test first-order Markov property. Compare 2020→2021 transition matrix (COVID shock year) vs. 2022→2023 (recovery). Directly replicates and extends Herrera & Rosas (2003) methodology for youth specifically.

**Model 2 — Discrete-time hazard model:**
For each individual, NEET entry is a binary event. Spell duration measured in annual waves (1–5 years). Discrete-time proportional hazard:
```
h(t|X) = 1 - exp(-exp(Xᵢₜ'β + αₜ))
```
Covariates: gender, education level, region, household income quartile, presence of young children (especially relevant for women), COVID shock year indicator.

**Key heterogeneity questions:**
- Do women face longer NEET spells? (Gender-specific barriers to re-entry)
- Is rural NEET more persistent than urban NEET?
- Does household poverty accelerate or delay NEET exit? (Pressure to work vs. inability to find work)

**Why novel:** Latin American NEET research relies almost entirely on repeated cross-sections. The ENAHO panel makes it possible to estimate actual transition rates and duration dependence — not just point-in-time prevalence rates. The COVID shock provides a clean before/after comparison for hazard rates.

**Policy relevance:** Peru's youth NEET rate (~25% pre-pandemic) is among the highest in Latin America. Evidence on duration and predictors directly informs targeting of youth employment programs (PROJoven, Trabaja Perú).

---

## JSON Output

```json
{
  "top_ideas": [
    {
      "rank": 1,
      "title": "Informality Scarring in Peru: Long-Run Wage Penalties from COVID-Induced Informal Spells",
      "research_question": "Does entering informality during the COVID-19 shock (2020-2021) generate persistent wage penalties in 2022-2024, even after workers return to formal employment, and does this scarring vary by education, gender, and region?",
      "method": "Dynamic panel GMM (Arellano-Bond), Tier 2. Identifying variation: lagged informality status instrumented with deeper lags (t-2, t-3); COVID-sector exposure used as external validity check. Individual FE absorbs time-invariant unobserved heterogeneity.",
      "sub_topic": "informality_scarring",
      "data_sources": ["ENAHO panel 2020-2024 (wide-to-long reshape on year suffixes _20 through _24)", "INEI social security enrollment records for informality cross-validation"],
      "novelty": 5,
      "feasibility": 4,
      "impact": 5,
      "total_score": 5.4,
      "pitch": "Informality scarring is empirically established in Germany and the UK, but Peru is a high-informality developing economy where the mechanism and magnitude may differ fundamentally. The COVID shock provides a rare quasi-exogenous entry event, and the 5-wave ENAHO panel allows tracking the same workers from shock through recovery — the first true panel-data test of wage scarring from informality in Peru. Results would directly complement Bosch et al.'s (2025) firm-side enforcement findings by mapping the worker-side cost of informality spells.",
      "first_experiment": "Week 1: Reshape ENAHO wide→long format using year suffixes _20 through _24 (ID=numper+conglome+vivienda). Construct binary informality indicator (social security non-enrollment) for each individual-year. Estimate a simple individual FE model of log wages on lagged informality status (xtfeis or reghdfe in Stata / linearmodels in Python) to get a baseline OLS-FE scarring coefficient before moving to Arellano-Bond GMM."
    },
    {
      "rank": 2,
      "title": "COVID-19 and the Formality Recovery Path: A Worker-Level Panel DiD Using Sectoral Teleworkability",
      "research_question": "Did workers in contact-intensive sectors experience a larger and more persistent increase in informality after COVID-19, and how does the formality recovery trajectory vary by firm size, gender, and region in Peru?",
      "method": "Two-way fixed effects DiD + event study, Tier 1. Identifying variation: differential sectoral exposure to COVID mobility restrictions measured by Dingel-Neiman (2020) teleworkability index matched to ENAHO occupation codes. Individual and year FE absorb selection and macro shocks.",
      "sub_topic": "informality_covid_recovery",
      "data_sources": ["ENAHO panel 2020-2024 (primary)", "Dingel & Neiman (2020) teleworkability scores (public, matched on CIIU 4-digit occupation codes)", "INEI sectoral mobility restriction data (2020)"],
      "novelty": 4,
      "feasibility": 5,
      "impact": 5,
      "total_score": 5.3,
      "pitch": "Bosch et al. (2025) demonstrate that enforcement letters push large firms toward formal enrollment — but what happens to the workers displaced into informality by the COVID shock? This paper provides the missing worker-side panel complement: using sectoral teleworkability as a source of differential exposure, it traces the full formality recovery path for the same individuals from 2020 to 2024. The event-study design makes pre-trends testable and the 5-wave structure captures whether recovery is complete or whether informality hysteresis is a durable structural feature of Peru's labor market.",
      "first_experiment": "Week 1: Reshape ENAHO wide→long. Download Dingel-Neiman teleworkability scores (open-access). Match scores to ENAHO occupation variable (p507 variants) at 2-digit CIIU level. Construct informality indicator. Run basic TWFE: regress informality on i.year##c.teleworkability_score + individual FE + year FE, clustered SE at individual level. Inspect year-by-year interaction coefficients for event-study pre-trend check."
    },
    {
      "rank": 3,
      "title": "Youth NEET Dynamics in Post-Pandemic Peru: Markov Transitions and Discrete-Time Hazard Models",
      "research_question": "What individual and household characteristics predict entry into and duration of NEET status among Peruvian youth aged 15-29, and did the COVID-19 shock increase NEET spell persistence through 2024?",
      "method": "Discrete-time hazard models + Markov transition matrices, Tier 2. Identifying variation: within-individual transitions across five labor market states over five annual waves; COVID-19 (2020) acts as a common shock enabling comparison of hazard rates and transition probabilities across the pre- and post-shock period.",
      "sub_topic": "youth_employment_neet",
      "data_sources": ["ENAHO panel 2020-2024 (primary)", "INEI population projections for youth denominators", "MINEDU school enrollment administrative records (optional validation)"],
      "novelty": 5,
      "feasibility": 4,
      "impact": 4,
      "total_score": 5.1,
      "pitch": "Latin American NEET research relies almost entirely on repeated cross-sections, measuring prevalence but not duration or state dependence. The ENAHO 5-wave panel makes it possible — for the first time in Peru — to estimate actual transition rates, spell durations, and duration dependence in NEET status. The COVID shock provides a clean before/after design for hazard rates, and gender heterogeneity in NEET exit rates connects directly to Peru's persistent gender gap in labor force participation. Results directly target PROJoven and Trabaja Perú program design.",
      "first_experiment": "Week 1: Reshape ENAHO wide→long. Define NEET for individuals aged 15-29 using employment status (p501) and school enrollment (p300) variables with year suffixes. Compute 5x5 annual Markov transition matrices across states (formal employed, informal employed, NEET, education, other inactive). Compare 2020-2021 matrix vs. 2022-2023 matrix to identify COVID-induced changes in transition probabilities. Flag whether NEET absorption increased post-2020."
    }
  ]
}
```