# Research Ideation: ChatGPT Availability → Software Development (Unique Pushers)

---

## Data Reconnaissance

Before proposing anything, let me map the identifying variation available in your data:

| Variable | Role | Identification potential |
|---|---|---|
| `iso2_code` | Country unit | Cross-sectional dose variation |
| `language` | Programming language | Pre-determined ChatGPT code quality varies |
| `language_type` | Language category | Pre-determined susceptibility to AI assistance |
| `num_pushers` | Outcome | Growth in contributors |
| `year / quarter` | Time | Pre/post ChatGPT (Nov 30, 2022) |

**Critical observation:** ChatGPT is a near-universal shock — but your data has TWO pre-determined axes of differential exposure: (1) **country-level English proficiency** (you already have `ef_epi_2025.csv`) and (2) **programming language-level ChatGPT code quality**. These are your Level B workhorses. Additionally, country-level **ChatGPT access restrictions** (Italy temp ban, China, Russia) create a small Level A wedge.

---

## THE 10 IDEAS

---

### IDEA 1 — English Proficiency as Continuous Treatment Dose
**Sub-topic:** Language Barriers / Access Gradient
**RQ:** Do countries with higher pre-ChatGPT English proficiency experience larger increases in unique pushers after Nov 2022, consistent with ChatGPT's English-first advantage?

**Method:** Continuous-treatment DiD (Tier 2). Unit = country × language × quarter. Dose = EF EPI score (you already have this), measured pre-ChatGPT. Estimating equation:

> `log(num_pushers)_ict = α_ic + α_t + β (EF_EPI_i × Post_t) + ε`

Country × language FE absorbs all time-invariant composition. Time FE absorbs global shocks. The interaction β is identified off pre-determined English proficiency.

**Identification level:** B
- Source of variation: EF EPI (pre-determined, 2022 index predates ChatGPT)
- Pre-periods: ~10–11 quarters (Q1 2020–Q3 2022)
- Parallel trends: testable with full pre-period × EF EPI interactions
- Clusters: ~161 countries → adequate; cluster at country level
- Threat: English proficiency correlated with prior tech trajectory → include HDI, internet penetration as controls

**Data needs:** Your data + EF EPI (already have it) + optional: World Bank internet access for controls
**Novelty:** Prior work (Noy & Zhang 2023, Peng et al. 2023) focuses on individual productivity in English-speaking contexts. Country-level English gradient in open-source contribution is unstudied.
**Impact:** Quantifies the global inequality in AI-driven developer productivity growth.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 4 | 5 | 5 | 4 | **4.4** |

---

### IDEA 2 — ChatGPT Country Bans as Quasi-Experiment
**Sub-topic:** Regulatory Heterogeneity / Access Restrictions
**RQ:** Does temporary or permanent removal of ChatGPT access (Italy Q2 2023, China/Russia persistent restrictions) cause a measurable decline in unique pushers relative to comparable unrestricted countries?

**Method:** DiD / Synthetic Control (Tier 1). Treatment = countries with ChatGPT access restrictions (Italy: Q2 2023 ban; China/Russia: ongoing). Control = matched countries on pre-treatment trends. For Italy specifically: interrupted panel with narrow window to isolate the ban episode.

**Identification level:** A
- Source: Policy-imposed access restriction — plausibly exogenous to developer activity trends
- Pre-periods: ~10 quarters
- Parallel trends: testable for Italy (before ban); China/Russia require synthetic control (donor pool)
- Clusters: Small treated set → use SC or wild bootstrap
- Threats: Selection (banning countries differ structurally); VPN circumvention attenuates true effect toward zero (making estimates conservative lower bounds)

**Data needs:** Your data. Supplement with VPN usage proxies (APNIC or GlobalWebIndex) for attenuation correction.
**Novelty:** No study has used ChatGPT access bans as a natural experiment for open-source contribution. The "regulatory wedge" angle is novel and policy-relevant.
**Impact:** Directly speaks to AI governance debates — quantifies cost of restricting access.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 4 | 3 | 5 | 4 | **4.0** |

---

### IDEA 3 — Programming Language ChatGPT-Quality Index as Dose
**Sub-topic:** Language-Level AI Susceptibility
**RQ:** Do programming languages where ChatGPT generates higher-quality code (Python, JavaScript, TypeScript) attract disproportionately more unique pushers post-Nov 2022 relative to low-quality languages (Fortran, COBOL, niche DSLs)?

**Method:** Continuous-treatment DiD (Tier 2). Unit = country × language × quarter. Dose = pre-determined language-level ChatGPT code quality score (construct from HumanEval/MBPP benchmarks or language frequency in ChatGPT pre-training data). Both sources are measured before Nov 2022.

> `log(num_pushers)_ict = α_ic + α_t + β (ChatGPT_Quality_l × Post_t) + ε`

**Identification level:** B
- Source: Language-level ChatGPT quality is pre-determined by training corpus composition, not by Nov 2022 developer activity
- Pre-periods: ~10 quarters
- Parallel trends: testable across language quality quartiles
- Clusters: ~50+ distinct languages → cluster at language level or two-way

**Data needs:** Your data + HumanEval/MBPP pass@k rates by language (public benchmarks from Codex, GPT-4 papers, Chen et al. 2021)
**Novelty:** Uses a pre-determined language-level instrument that no existing open-source study exploits. Separates "ChatGPT-accessible" from "ChatGPT-resistant" programming ecosystems.
**Impact:** Shows which language ecosystems are structurally disrupted — actionable for language designers and CS educators.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 5 | 4 | 4 | 3 | **3.8** |

---

### IDEA 4 — Extensive Margin: Does ChatGPT Lower Barriers to Entry?
**Sub-topic:** Developer Entry / Human Capital Accumulation
**RQ:** Does ChatGPT increase the number of unique pushers (extensive margin entry) disproportionately in high-English-proficiency countries, consistent with lower cognitive barriers to coding?

**Method:** Continuous DiD (Tier 2) on the extensive margin outcome (num_pushers, not per-capita rates). Dose = EF EPI × language ChatGPT quality (two-dimensional dose). This allows testing whether the barrier-lowering effect operates through both the country and language channels simultaneously.

> `log(num_pushers)_ict = α_ic + α_t + β₁(EF_i × Post_t) + β₂(Quality_l × Post_t) + β₃(EF_i × Quality_l × Post_t) + ε`

Triple interaction β₃ identifies whether countries AND languages where ChatGPT works best see the biggest new-contributor surge.

**Identification level:** B
- Both doses pre-determined; triple interaction is powerful and novel
- Directly exploits panel structure across country × language × quarter
- Threat: Selection of languages into countries (e.g., Python-heavy Silicon Valley) — absorbed by country × language FE

**Data needs:** Your data + EF EPI + HumanEval benchmarks
**Novelty:** The "extensive margin entry" framing is new. Most productivity papers look at output quality per developer, not the number of people who start contributing.
**Impact:** If ChatGPT democratizes entry, it changes forecasts about global developer supply — huge policy implications.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 4 | 4 | 5 | 3 | **3.8** |

---

### IDEA 5 — Language Portfolio Diversification: Did ChatGPT Increase Specialization or Breadth?
**Sub-topic:** Developer Specialization / Language Concentration
**RQ:** Did ChatGPT cause countries' developer communities to concentrate in fewer "AI-boosted" languages (specialization) or spread into more languages (diversification)?

**Method:** Construct country-quarter HHI of language concentration from your data. Use this as outcome in a continuous DiD where dose = EF EPI. Test whether high-English countries show greater post-ChatGPT concentration shifts.

**Identification level:** B
- Clever use of derived outcome (HHI) to capture structural reallocation
- Dose = EF EPI, pre-determined

**Data needs:** Your data alone (HHI computable from num_pushers by language within country-quarter) + EF EPI for dose
**Novelty:** No paper looks at language portfolio concentration as an outcome of AI tools.
**Impact:** Speaks to whether AI is homogenizing the global software stack toward a few dominant languages.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 4 | 5 | 4 | 3 | **3.8** |

---

### IDEA 6 — Geographic Convergence: Does ChatGPT Compress the Developer Gap?
**Sub-topic:** Global Inequality in Software Development
**RQ:** Do initially developer-sparse countries experience faster growth in unique pushers post-ChatGPT, consistent with AI reducing the human-capital barrier to software contribution?

**Method:** Conditional convergence DiD (Tier 2). Dose = initial (pre-2022) developer density (low density = high "potential gain"). Interact with Post × EF EPI to separate convergence driven by AI access quality.

**Identification level:** B (initial developer density is pre-determined)
**Data needs:** Your data (compute baseline pushers from pre-2022 quarters) + World Bank population data for per-capita normalization
**Novelty:** Standard convergence model applied to AI-driven human capital in open-source — connects development economics to AI literature.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 3 | 4 | 4 | 3 | **3.4** |

---

### IDEA 7 — Language-Type Reallocation: Scripting vs. Compiled Languages
**Sub-topic:** Language Type Composition Shift
**RQ:** Did ChatGPT cause a reallocation of pushers from low-level/compiled languages (C, C++, Rust) toward high-level/scripting languages (Python, JavaScript, Ruby) where AI assistance is most effective?

**Method:** Share DiD (Tier 2). Outcome = share of country-quarter pushers working in "AI-favored" language_type. Dose = EF EPI or internet access. Use your existing `language_type` variable as a pre-determined classifier.

**Identification level:** B
**Data needs:** Your data (language_type already exists!) + EF EPI
**Novelty:** Directly uses the `language_type` variable already in your dataset — lowest marginal data cost of any idea here.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 3 | 5 | 4 | 3 | **3.6** |

---

### IDEA 8 — Complementarity Between English Access and Internet Infrastructure
**Sub-topic:** Infrastructure Complementarities
**RQ:** Is the ChatGPT effect on unique pushers supermodular in English proficiency AND internet penetration? Do you need both conditions to see gains?

**Method:** Bartik shift-share / continuous DiD with two-dimensional dose (EF EPI × internet penetration index, both pre-determined). Identify the interaction term.

**Identification level:** B (both doses pre-determined)
**Data needs:** Your data + EF EPI + ITU internet access statistics
**Novelty:** Tests whether AI tools require infrastructure complements — relevant for policy sequencing.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 3 | 3 | 4 | 3 | **3.2** |

---

### IDEA 9 — Skill Downgrading: Does ChatGPT Reduce Complexity of Contributed Code?
**Sub-topic:** Code Quality / Skill Composition
**RQ:** Post-ChatGPT, do repositories in AI-susceptible languages show an influx of low-complexity commits (proxied by new contributor share), consistent with AI lowering the skill floor?

**Method:** Continuous DiD with new-entrant share outcome. Requires augmenting with GitHub API data to classify contributors as new vs. experienced. Dose = language ChatGPT quality.

**Identification level:** B
**Data needs:** Your data + GitHub API (contributor tenure data) — external data requirement reduces feasibility
**Novelty:** The "skill downgrading" channel is theoretically predicted but empirically untested.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 4 | 2 | 4 | 3 | **3.2** |

---

### IDEA 10 — Temporal Dynamics: Was the ChatGPT Effect Front-Loaded or Sustained?
**Sub-topic:** Dynamic Treatment Effects / Anticipation
**RQ:** Did the increase in unique pushers concentrate in Q1 2023 (immediate adoption wave) or did it build gradually, and does this pattern vary by EF EPI dose?

**Method:** Event-study with continuous dose (Callaway-Sant'Anna style adapted for repeated cross-sections). Plot β_τ × EF_EPI coefficients across leads and lags. Tests anticipation, immediate effects, and persistence.

**Identification level:** B (uses EF EPI dose to generate heterogeneous event-study)
**Data needs:** Your data + EF EPI
**Novelty:** The dynamic heterogeneity angle — "who adjusted fastest" — is unstudied.

| N | F | I | ID | **Total** |
|---|---|---|---|---|
| 3 | 4 | 3 | 3 | **3.0** |

---

## RANKED SUMMARY TABLE

| Rank | Idea | Sub-topic | N | F | I | ID | **Score** |
|---|---|---|---|---|---|---|---|
| 1 | English Proficiency Dose | Language barriers | 4 | 5 | 5 | 4 | **4.4** |
| 2 | ChatGPT Country Bans | Regulatory heterogeneity | 4 | 3 | 5 | 4 | **4.0** |
| 3 | Extensive Margin Entry (triple interaction) | Developer entry | 4 | 4 | 5 | 3 | **3.8** |
| 4 | Language ChatGPT Quality Dose | Language AI susceptibility | 5 | 4 | 4 | 3 | **3.8** |
| 5 | HHI Diversification | Specialization | 4 | 5 | 4 | 3 | **3.8** |
| 6 | Scripting vs Compiled Reallocation | Language type shift | 3 | 5 | 4 | 3 | **3.6** |
| 7 | Geographic Convergence | Global inequality | 3 | 4 | 4 | 3 | **3.4** |
| 8 | Infrastructure Complementarity | Infra complements | 3 | 3 | 4 | 3 | **3.2** |
| 9 | Skill Downgrading | Code quality | 4 | 2 | 4 | 3 | **3.2** |
| 10 | Dynamic Effects | Temporal dynamics | 3 | 4 | 3 | 3 | **3.0** |

---

## TOP 3 ELABORATED IDEAS

---

### #1 — English Proficiency as ChatGPT Adoption Dose (ID Level B, Score 4.4)

**The core insight:** ChatGPT was trained predominantly on English text. Its code assistance quality degrades for users who (a) read English documentation less fluently and (b) interact with it in non-English. This creates a pre-determined, continuous dose of "effective treatment intensity" that varies across countries based on their English proficiency (EF EPI) — measured before ChatGPT existed.

**Estimating equation:**
```
log(num_pushers_ict) = α_ic + α_t + β(EF_EPI_i × Post_t) + X_i'γ × Post_t + ε_ict
```
where `i` = country, `c` = language, `t` = quarter, `Post_t` = 1 for quarters after Q3 2022.

**Parallel trends test:** Interact EF EPI quartiles with quarter dummies in the pre-period. If high- and low-EF countries had parallel pusher trends before Q4 2022, this validates the design. With 10+ pre-quarters, you have statistical power to formally reject pre-trends.

**Robustness:**
- Control for GDP per capita × Post, HDI × Post (absorb correlated country characteristics)
- Drop top 5 English-speaking countries (US, UK, CA, AU, NZ) and verify results hold
- Placebo: use a fake treatment date (Q4 2021) — β should be zero
- Heterogeneity: estimate separately for `language_type` — stronger effects in high-level languages where English documentation is critical

**What's novel:** Every existing paper (Noy & Zhang, Brynjolfsson et al.) studies English-speaking subjects in lab/firm settings. This is the first country-level test of the English access gradient in open-source software, using the full global distribution.

**Week 1:** Merge `iso2_code` to EF EPI file (already in your repo at `data/external/ef_epi_2025.csv`). Compute `log(num_pushers)` by country × language × quarter. Run the baseline regression with country × language FE and time FE. Plot binscatter of β by EF EPI quartile. If the pattern shows a positive gradient post-Q4 2022, you have your paper.

---

### #2 — ChatGPT Country Bans as Quasi-Experiment (ID Level A, Score 4.0)

**The core insight:** Several countries imposed access restrictions on ChatGPT:
- **Italy:** Full ban March 31–April 28, 2023 (one quarter-ish)
- **China:** Persistent block (OpenAI not operating; Baidu's ERNIE Bot launched March 2023)
- **Russia:** Access increasingly restricted post-2022

This creates a Level A design — the assignment to "restricted access" is driven by political/regulatory decisions largely exogenous to developer activity trends. The key assumption: Italy/China/Russia's developer communities were not on a structurally different trajectory from comparable unrestricted countries before the bans.

**Strategy:**
- **Italy (event study):** Narrow window around Q2 2023. Compare Italy's unique pushers to a synthetic control (weighted combination of similar EU countries: Spain, Portugal, Greece). Test whether pusher growth dipped during the ban quarter and rebounded immediately after — the "notch" pattern is convincing.
- **China/Russia (long DiD):** Classify as persistently restricted. Compare to BRICS/emerging markets with unrestricted access. Use EF EPI to match control units.

**VPN correction:** Estimates will be attenuated if developers circumvent bans via VPN. This makes your estimates **lower bounds** on the true effect — a conservative framing referees accept. You can augment with APNIC or Freedom House internet freedom scores to discuss likely attenuation magnitude.

**Threats and responses:**
- *Italy is small in GitHub activity* → supplement with total pushers aggregated across all languages; also strengthens the China/Russia arm
- *China had domestic substitutes (ERNIE Bot, Copilot alternatives)* → label this as "net effect of ChatGPT loss + imperfect substitution"
- *Simultaneous confounders (EU AI Act discussion in Italy)* → narrow event window helps; placebo dates in 2020-2021

**Week 1:** Filter data to Italy (IT), China (CN), Russia (RU) + candidate controls. Compute quarterly growth rates in `num_pushers` per language. Visually inspect whether ban-period quarters show a dip relative to pre-trend. If the Italy "notch" is visible in the raw data, proceed to synthetic control.

---

### #3 — Extensive Margin Entry: ChatGPT as a Developer Pipeline Amplifier (ID Level B, Score 3.8)

**The core insight:** The most transformative claim about ChatGPT is not that it makes existing developers faster — it's that it enables people who previously couldn't code to contribute. This "extensive margin" effect shows up as growth in `num_pushers` (your exact outcome variable). The twist: this effect should be strongest where ChatGPT works best, operationalized by a **two-dimensional dose**: English proficiency (determines interaction quality) × language-level ChatGPT code quality (determines output quality).

**Estimating equation:**
```
log(num_pushers_ict) = α_ic + α_t 
    + β₁(EF_i × Post_t) 
    + β₂(Quality_l × Post_t) 
    + β₃(EF_i × Quality_l × Post_t) + ε_ict
```

β₃ is the key coefficient: it tests whether the barrier-lowering effect is *supermodular* — you need both access quality (EF) and tool quality (code benchmark performance) to see new contributor growth.

**Constructing `Quality_l`:** Use pass@k rates from HumanEval/MBPP by language (Chen et al. 2021; these are pre-ChatGPT benchmarks, so pre-determined). Languages like Python (pass@1 ≈ 0.67), JavaScript, TypeScript score high. COBOL, Fortran, assembly score near zero.

**Why this is empirically powerful:**
- Triple interaction generates rich heterogeneity — you can plot a 2×2: high/low English × high/low language quality
- The "new entrant" interpretation is supported if the effect is concentrated in beginner-friendly languages (Python, JavaScript) and absent in expert-only languages (C, Rust)
- Country × language FE eliminates all time-invariant composition differences

**Robustness:** Decompose `num_pushers` growth into: (a) growth within existing language-country cells (intensive margin) vs. (b) appearance of new country × language combinations in the data (extensive margin). The latter is a clean test of barrier reduction.

**Week 1:** Collect HumanEval/MBPP pass@k by language from Chen et al. (2021) Table 3 and related papers. Build a 50-row crosswalk: `language → Quality_score`. Merge to your panel. Run the triple interaction. The 2×2 heterogeneity plot is your Figure 3.

---

```json
{
  "top_ideas": [
    {
      "rank": 1,
      "title": "English Proficiency as ChatGPT Treatment Dose: Country-Level Evidence from Open-Source Development",
      "research_question": "Do countries with higher pre-ChatGPT English proficiency experience larger increases in unique GitHub pushers after November 2022, consistent with ChatGPT's English-first design creating a continuous gradient of effective treatment intensity?",
      "method": "Continuous-treatment DiD with pre-determined country-level dose (EF EPI score)",
      "identification_level": "B",
      "identification_source": "EF English Proficiency Index, measured pre-ChatGPT, creates differential treatment intensity across countries. Cross-country variation in English access to AI tools is exogenous to developer activity trends.",
      "sub_topic": "language_barriers_english_gradient",
      "data_sources": ["Your panel (iso2_code × language × quarter)", "EF EPI data (already in repo: ef_epi_2025.csv)", "World Bank GDP/HDI for controls"],
      "novelty": 4,
      "feasibility": 5,
      "impact": 5,
      "identification": 4,
      "total_score": 4.4,
      "pitch": "ChatGPT's English-first architecture means its productivity benefits are unevenly distributed globally. Using pre-determined EF EPI scores as a continuous dose in a DiD design — with the data you already have — we test whether the global open-source developer community expanded most where English proficiency was highest, providing the first country-level evidence on AI's role in widening vs. narrowing the global software development gap.",
      "first_experiment": "Merge iso2_code to ef_epi_2025.csv. Compute log(num_pushers) by country × language × quarter. Run: log(pushers) = country×language FE + quarter FE + β(EF_EPI × Post_Q42022). Plot binscatter of quarterly pusher growth rates by EF EPI quartile, pre vs. post. If gradient visible, estimate full model with HDI × Post controls and test for pre-trend parallel-ness."
    },
    {
      "rank": 2,
      "title": "Regulatory Wedge: ChatGPT Access Bans as a Natural Experiment for Open-Source Contribution",
      "research_question": "Does restricting ChatGPT access (Italy's temporary ban; China/Russia's persistent restrictions) cause a measurable decline in unique pushers relative to comparable unrestricted countries, providing a causal estimate of ChatGPT's contribution to software development?",
      "method": "DiD with synthetic control for Italy event study; TWFE DiD for China/Russia vs. matched emerging markets",
      "identification_level": "A",
      "identification_source": "Country-level ChatGPT access bans are driven by political/regulatory decisions exogenous to developer activity trends. Italy's Q2 2023 ban creates a credible treated unit with a clean event window and reversal.",
      "sub_topic": "regulatory_heterogeneity_access_restrictions",
      "data_sources": ["Your panel", "Official OpenAI country availability announcements", "APNIC VPN usage data (for attenuation correction)", "Freedom House internet freedom scores"],
      "novelty": 4,
      "feasibility": 3,
      "impact": 5,
      "identification": 4,
      "total_score": 4.0,
      "pitch": "While most studies measure ChatGPT's average effect, policy-imposed access restrictions create a rare Level A experiment: treated units (Italy, China, Russia) vs. comparable controls. Italy's narrow ban window enables a high-frequency event study with clean entry/exit, while China/Russia's persistent restrictions enable long-run estimates. Attenuation from VPN use makes estimates conservative lower bounds — a refereeacceptable framing that also quantifies the regulatory cost of AI governance.",
      "first_experiment": "Filter panel to Italy (IT) + EU control countries (ES, PT, GR, PL). Compute quarterly num_pushers per language. Visually test whether Q2 2023 shows a dip in Italy vs. controls. If the 'notch' pattern is visible in raw data, proceed to synthetic control (donor pool = all EU non-ban countries weighted to match Italy's pre-2022 trend)."
    },
    {
      "rank": 3,
      "title": "Supermodular Entry: ChatGPT Lowers Coding Barriers Only Where Both English Access and Language Quality Are High",
      "research_question": "Does ChatGPT increase the number of unique pushers disproportionately in country × language cells where both English proficiency (interaction quality) and language-level ChatGPT code performance (output quality) are high, consistent with supermodular complementarity in AI-assisted entry?",
      "method": "Continuous DiD with triple interaction: EF_EPI × ChatGPT_Language_Quality × Post; outcome is log(num_pushers) at country × language × quarter level",
      "identification_level": "B",
      "identification_source": "Two pre-determined doses: (1) EF EPI measured before ChatGPT launch; (2) HumanEval/MBPP pass@k scores from pre-ChatGPT Codex benchmarks (Chen et al. 2021). Both are exogenous to post-2022 developer activity.",
      "sub_topic": "developer_entry_barriers_extensive_margin",
      "data_sources": ["Your panel", "EF EPI (in repo)", "HumanEval/MBPP pass@k by language (Chen et al. 2021, public benchmark tables)"],
      "novelty": 4,
      "feasibility": 4,
      "impact": 5,
      "identification": 3,
      "total_score": 3.8,
      "pitch": "The most consequential claim about AI coding tools is that they democratize software development — enabling new contributors, not just accelerating existing ones. Using unique pushers as the outcome (pure extensive margin), we test whether new-developer entry is supermodular: you need BOTH a country that can interact with ChatGPT in English AND a programming language where ChatGPT generates usable code. The triple interaction design generates rich 2×2 heterogeneity directly testable with existing data and publicly available benchmarks.",
      "first_experiment": "Download HumanEval pass@1 rates by programming language from Chen et al. (2021) supplementary tables. Build a language → quality_score crosswalk for the top 30 languages in your data. Merge to panel. Run triple interaction regression with country×language FE + quarter FE. Plot 2×2 binscatter: high/low EF × high/low quality, post-minus-pre growth rates. Check whether the high×high cell dominates."
    }
  ],
  "identification_warning": null
}
```