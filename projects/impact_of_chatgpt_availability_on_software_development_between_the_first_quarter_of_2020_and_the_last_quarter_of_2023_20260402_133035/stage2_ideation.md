# Research Ideation: ChatGPT's Impact on Software Development (2020–2023)
**Advisor: Junshi | Dataset: Language×Country×Quarter push counts**

---

## Step 1: Literature Landscape

**Key themes in existing work:**
- Productivity effects of AI coding assistants (GitHub Copilot RCTs; Peng et al. 2023)
- Aggregate labor market effects of LLMs on software workers (Brynjolfsson, Li & Raymond 2023)
- Stack Overflow traffic declines as proxy for ChatGPT substitution (various blog-level analyses)
- Language-model capability heterogeneity across programming languages
- Geographic and demographic heterogeneity in AI tool adoption

**Key gaps:**
1. No credibly causal study of *ecosystem-level* language popularity shifts induced by ChatGPT
2. No cross-country evidence exploiting differential English proficiency as treatment intensity
3. No analysis of whether ChatGPT homogenized or diversified the language ecosystem
4. No evidence on niche/legacy language revival vs. mainstream concentration
5. No study of new-entrant vs. incumbent developer effects at scale using observational OSS data
6. No RD evidence exploiting the sharp November 2022 launch date at fine temporal resolution

**Data asset:** 161,922 rows covering (language × country × quarter), 6 time periods (Q1 2020–Q4 2023, with ~11 pre-treatment quarters before Q4 2022 and ~5 post-treatment quarters). Unit: aggregate pushers per language-country-quarter cell. This is a **group-level repeated cross-section** — ideal for group-level DiD, event studies, RDD-in-time, and decompositions.

---

## Step 2: The 10 Ideas

---

### Idea 1 — ChatGPT Capability-Weighted DiD on Language Adoption
**Sub-topic: Programming Language Adoption**
**Research question:** Did programming languages for which ChatGPT has demonstrably stronger code generation (Python, JavaScript, TypeScript) gain a disproportionate share of active pushers after Q4 2022 relative to languages with weak LLM support (COBOL, Fortran, Ada)?

**Method:** Tier 1 — Difference-in-Differences with continuous treatment intensity
- Unit: language × country × quarter
- Treatment: post-Q4 2022 × ChatGPT capability score for each language (source: HumanEval/EvalPlus benchmarks, passable on a per-language basis)
- Identifying variation: Cross-language differential in ChatGPT generation quality, interacted with the sharp November 2022 launch date
- Pre-periods for parallel trends: ~11 quarters (Q1 2020–Q3 2022) ✓
- Clusters: ~50 countries × N languages ≫ 50 clusters ✓
- Threats: confounds from pre-existing Python/JS growth trends (testable with linear pre-trends)

**Data needed:** Existing dataset + HumanEval benchmark scores by language (public)
**Novelty:** 4 | **Feasibility:** 5 | **Impact:** 5
**Total:** 0.4×4 + 0.3×5 + 0.3×5 = 1.6+1.5+1.5 = **4.6 + 0.3 causal bonus = 4.9**

---

### Idea 2 — English Proficiency as Treatment Intensity: Geographic DiD
**Sub-topic: Geographic Diffusion of AI Tools**
**Research question:** Did countries with higher English proficiency experience faster growth in software developer activity after ChatGPT's (initially English-only) launch, and did this gap close after multilingual releases?

**Method:** Tier 1 — DiD with continuous treatment intensity (EF-EPI English proficiency score × post-Q4 2022)
- Unit: country × quarter (collapsing across languages, or interacting)
- Identifying variation: Pre-determined English proficiency (EF-EPI 2020, measured before treatment) creates plausibly exogenous differential exposure
- Pre-periods: 11 quarters ✓; parallel trends testable across the full pre-period
- Clusters: ~50 countries — borderline; use wild cluster bootstrap
- Threat: English-proficient countries also have higher baseline tech capacity; control for GDP/pc, broadband penetration

**Data needed:** EF-EPI 2020 English Proficiency Index (public), World Bank GDP/internet data
**Novelty:** 5 | **Feasibility:** 4 | **Impact:** 5
**Total:** 0.4×5 + 0.3×4 + 0.3×5 = 2.0+1.2+1.5 = **4.7 + 0.3 = 5.0**

---

### Idea 3 — RDD-in-Time Around the November 2022 Launch
**Sub-topic: Causal Aggregate Impact**
**Research question:** Is there a statistically significant discontinuity in total active pushers or language diversity at the Q4 2022 threshold, consistent with a ChatGPT-driven demand shock?

**Method:** Tier 1 — Regression Discontinuity in Time (RDiT)
- Running variable: quarter index, cutoff at Q4 2022
- Outcome: log(num_pushers) aggregated by country or globally; or HHI of language shares
- Identifying variation: The sharp, externally determined launch date — developers cannot self-select into treatment timing
- Bandwidth selection: IK-optimal; robustness to triangular/rectangular kernel
- Pre-periods: 11 points left of cutoff; enough for McCrary density test analog
- Threat: Contemporaneous shocks (mass tech layoffs late 2022); use placebo cutoffs

**Data needed:** Existing dataset only
**Novelty:** 3 | **Feasibility:** 5 | **Impact:** 4
**Total:** 0.4×3 + 0.3×5 + 0.3×4 = 1.2+1.5+1.2 = **3.9 + 0.3 = 4.2**

---

### Idea 4 — Language Ecosystem Diversity: Did ChatGPT Homogenize or Diversify?
**Sub-topic: Ecosystem Concentration**
**Research question:** Did ChatGPT's release shift the distribution of pushers toward mainstream languages (concentration) or enable growth in niche languages (diversification), as measured by within-country Herfindahl indices?

**Method:** Tier 1 — Event study
- Unit: country × quarter; outcome = HHI of language shares within country
- Treatment: Post-Q4 2022 indicator; country-quarter panel
- Identification: sharp launch date; distributed lag specification with leads and lags
- Pre-periods: 11 quarters ✓
- Test: F-test of joint significance of pre-period leads

**Data needed:** Existing dataset only (compute HHI from num_pushers shares)
**Novelty:** 4 | **Feasibility:** 5 | **Impact:** 4
**Total:** 0.4×4 + 0.3×5 + 0.3×4 = 1.6+1.5+1.2 = **4.3 + 0.3 = 4.6**

---

### Idea 5 — New Entrant Proxy: Growth in Low-Barrier Scripted Languages
**Sub-topic: Developer Onboarding / Entry**
**Research question:** Did ChatGPT lower barriers to entry into software development, as proxied by disproportionate growth in scripted/interpreted "beginner-friendly" languages (Python, Ruby) relative to compiled/typed languages requiring deeper expertise?

**Method:** Tier 1 — DiD
- Unit: language × quarter; treatment = language_type ∈ {scripted} × post-Q4 2022
- Identification: Pre-determined language type classification (immutable property); interacted with sharp launch
- Pre-periods: 11 ✓; parallel trends testable
- Heterogeneity: interact with country income level — do low-income countries see larger entry effects?

**Data needed:** Existing dataset (language_type variable already present)
**Novelty:** 4 | **Feasibility:** 5 | **Impact:** 5
**Total:** 0.4×4 + 0.3×5 + 0.3×5 = 1.6+1.5+1.5 = **4.6 + 0.3 = 4.9**

---

### Idea 6 — Legacy Language Revival: Did ChatGPT Rescue COBOL and Fortran?
**Sub-topic: Legacy/Niche Language Dynamics**
**Research question:** Did legacy languages (COBOL, Fortran, Pascal) — known for scarce documentation and limited community — experience a disproportionate *relative* boost post-ChatGPT, as LLMs compensate for thin Stack Overflow coverage?

**Method:** Tier 1 — DiD
- Treatment intensity: inverse of Stack Overflow question count per language (pre-ChatGPT, from SOTorrent), interacted with post-Q4 2022
- Identification: Pre-determined community size is a fixed language attribute; ChatGPT creates differential value precisely where human documentation is sparse
- Pre-periods: 11 ✓; falsification: use inverse of GitHub repo count as alternative intensity

**Data needed:** Stack Overflow data dump (pre-2022 question counts by language tag, public)
**Novelty:** 5 | **Feasibility:** 3 | **Impact:** 4
**Total:** 0.4×5 + 0.3×3 + 0.3×4 = 2.0+0.9+1.2 = **4.1 + 0.3 = 4.4**

---

### Idea 7 — IV: Broadband Penetration as Instrument for ChatGPT Adoption
**Sub-topic: Mechanisms of Adoption**
**Research question:** What is the causal effect of ChatGPT adoption (instrumented by pre-existing broadband/mobile internet penetration) on country-level software developer participation?

**Method:** Tier 1 — IV/2SLS
- First stage: country-level broadband penetration (2021, pre-determined) × post-Q4 2022 predicts ChatGPT adoption proxied by Google Trends index for "ChatGPT" by country
- Second stage: log(num_pushers) on instrumented ChatGPT adoption
- Exclusion restriction: infrastructure affects pushers only through ChatGPT access (debatable — control for pre-trend in developer activity)
- Clusters: ~50 countries; use Conley spatial SEs

**Data needed:** ITU broadband penetration data (public), Google Trends by country (public)
**Novelty:** 4 | **Feasibility:** 3 | **Impact:** 4
**Total:** 0.4×4 + 0.3×3 + 0.3×4 = 1.6+0.9+1.2 = **3.7 + 0.3 = 4.0**

---

### Idea 8 — Synthetic Control: Counterfactual for High-Adoption Countries
**Sub-topic: Country-Level Macro Impact**
**Research question:** What would developer activity in high-ChatGPT-adoption countries (US, UK, Canada) have looked like absent the tool, using a synthetic control built from countries with delayed/restricted access (China, Russia)?

**Method:** Tier 1 — Synthetic Control
- Donor pool: countries with access restrictions or very low English proficiency
- Pre-fit period: Q1 2020–Q3 2022 (11 quarters) ✓
- Outcome: log(num_pushers) aggregated to country-quarter
- Placebo: apply to each donor country, compute rank of RMSPE

**Data needed:** Existing dataset + freedom-of-internet index for donor pool selection
**Novelty:** 3 | **Feasibility:** 4 | **Impact:** 4
**Total:** 0.4×3 + 0.3×4 + 0.3×4 = 1.2+1.2+1.2 = **3.6 + 0.3 = 3.9**

---

### Idea 9 — Cross-Language Spillovers: Polyglot Complementarity
**Sub-topic: Cross-Language Spillovers**
**Research question:** Did ChatGPT increase polyglot development (pushers active in multiple languages), using growth in multi-language country-quarter cells as a proxy for lower switching costs?

**Method:** Tier 2 — TWFE panel model
- Unit: country × quarter; outcome = number of distinct languages with positive pushers / Shannon entropy of language distribution
- Identification: within-country variation over time, leveraging the launch shock
- Fixed effects: country FE + quarter FE; cluster at country level
- Limitation: no individual tracking, so this is country-level language breadth, not individual polyglotism

**Data needed:** Existing dataset only
**Novelty:** 4 | **Feasibility:** 5 | **Impact:** 3
**Total:** 0.4×4 + 0.3×5 + 0.3×3 = 1.6+1.5+0.9 = **4.0 + 0.3 = 4.3**

---

### Idea 10 — Oaxaca-Blinder Decomposition of Pre/Post Language Mix
**Sub-topic: Compositional Change**
**Research question:** How much of the change in the developer ecosystem composition between pre- and post-ChatGPT periods is explained by shifts in language characteristics (type, documentation density) vs. changes in returns to those characteristics?

**Method:** Tier 4 — Oaxaca-Blinder decomposition
- Decompose: Δ(share of pushers in language l) = endowment effect + coefficient effect
- Endowment: did the mix of language types change? Coefficient: did the "return" to being a scripted/documented language change?
- Descriptive but valuable for heterogeneity characterization

**Data needed:** Existing dataset + language attribute data (type, documentation proxies)
**Novelty:** 3 | **Feasibility:** 5 | **Impact:** 3
**Total:** 0.4×3 + 0.3×5 + 0.3×3 = 1.2+1.5+0.9 = **3.6** (no causal bonus)

---

## Step 3: Summary Scoreboard

| # | Idea | Sub-topic | Tier | Score |
|---|------|-----------|------|-------|
| 2 | English Proficiency DiD | Geographic Diffusion | 1 | **5.0** |
| 1 | Capability-Weighted DiD | Language Adoption | 1 | **4.9** |
| 5 | Scripted vs Compiled DiD | Developer Onboarding | 1 | **4.9** |
| 4 | Ecosystem HHI Event Study | Concentration | 1 | **4.6** |
| 6 | Legacy Language Revival | Niche Dynamics | 1 | **4.4** |
| 3 | RDiT at Launch Date | Causal Aggregate | 1 | **4.2** |
| 9 | Cross-Language Spillovers | Polyglot | 2 | **4.3** |
| 7 | IV Broadband | Mechanisms | 1 | **4.0** |
| 10 | Oaxaca Decomposition | Compositional | 4 | **3.6** |
| 8 | Synthetic Control | Macro Impact | 1 | **3.9** |

**Top 3 (distinct sub-topics, ≥2 Tier 1):** Ideas 2, 1, 5 → but 1 and 5 are adjacent (both language-side). Substitute Idea 5 with Idea 4 (Concentration sub-topic) for maximal sub-topic diversity.

**Final Top 3: Idea 2 (Geographic), Idea 1 (Language Adoption), Idea 4 (Concentration)**

---

## Step 4: Elaboration of Top 3

---

### RANK 1 — English Proficiency as Treatment Intensity

**The core insight:** ChatGPT launched in English only. Countries where developers already read/write English fluently could immediately extract full value; countries with low English proficiency faced a friction that attenuated the treatment. This is a pre-determined, immutable characteristic that creates *exogenous* variation in treatment intensity — the gold standard for identification without an RCT.

**Specification:**
```
log(num_pushers_{c,q}) = α_c + α_q + β (EPI_c × Post_q) + γ X_{c,q} + ε_{c,q}
```
where EPI_c is EF English Proficiency Index for country c (2020 vintage, pre-treatment), Post_q = 1 for Q4 2022 onward, α_c are country fixed effects absorbing all time-invariant country characteristics, α_q are quarter fixed effects absorbing global trends.

**Parallel trends test:** With 11 pre-periods, estimate leads fully: the coefficient on EPI_c × quarter_t for t < Q4 2022 should be jointly zero. Plot the event-study graph.

**Heterogeneity:** Split by language_type — does English proficiency matter more for scripted languages (where ChatGPT's code quality is highest)?

**Threats and responses:**
- *English-proficient = high-income tech hub:* Control for GDP/pc × post, broadband × post
- *Simultaneous global tech layoffs (late 2022):* Include a layoff shock control (Layoffs.fyi data) or show the coefficient survives dropping US/FAANG-heavy countries
- *Multilingual ChatGPT update (March 2023):* Add a triple-diff: EPI × post-Q4 2022 × pre-March 2023 should be larger than EPI × post-March 2023, testing the specific English-friction channel

**Week 1 action:** Merge EF-EPI 2020 country scores into the dataset on iso2_code. Run the baseline DiD. Plot event study. Check cluster count and run wild-cluster bootstrap if N_clusters < 50.

---

### RANK 2 — ChatGPT Capability-Weighted DiD on Language Adoption

**The core insight:** ChatGPT's code generation quality is *not uniform across languages*. HumanEval benchmarks show pass@1 rates of ~70%+ for Python/JavaScript vs. <20% for COBOL/Ada/Prolog. This creates a continuous "treatment dose" that is determined entirely by the model's pre-existing training data composition — exogenous to any individual country or developer's choices.

**Specification:**
```
log(num_pushers_{l,c,q}) = α_{l,c} + α_q + β (Cap_l × Post_q) + δ (Cap_l × Trend_q) + ε_{l,c,q}
```
Cap_l = HumanEval pass@1 rate for language l (taken from published benchmarks, fixed pre-treatment). The language×country FE absorb all static differences. Quarter FE absorb global trends. The β coefficient captures whether high-capability languages gained relatively more pushers post-ChatGPT.

**Parallel trends:** 11 pre-period leads. Also run a Callaway-Sant'Anna style heterogeneity-robust estimator treating each language's capability tier discretely.

**Falsification:** Use a placebo treatment date (Q2 2021). β on the real date should be larger than all placebo dates.

**Week 1 action:** Download HumanEval/EvalPlus per-language pass@1 scores (available on GitHub). Map to language names in dataset. Run the baseline regression. Check whether Python and JS are visually diverging from COBOL/Fortran in the raw event-study plot.

---

### RANK 3 — Language Ecosystem Concentration Event Study

**The core insight:** If ChatGPT lowers the cost of *starting* in any language (documentation access, debugging help), we might expect *diversification* — the long tail of niche languages gains pushers. Conversely, if ChatGPT is a supercharger for already-popular languages, we expect *concentration*. Neither prediction is obvious, and the direction has first-order implications for the future of the language ecosystem and programming education.

**Specification:**
- Construct HHI_{c,q} = Σ_l (share_{l,c,q})² within each country-quarter
- Construct Shannon entropy H_{c,q} = -Σ_l (share_{l,c,q}) log(share_{l,c,q})
- Event study:
```
HHI_{c,q} = α_c + α_q + Σ_{τ≠-1} β_τ (Post_τ) + ε_{c,q}
```
- Each β_τ captures the deviation in HHI relative to the quarter before ChatGPT launch

**Heterogeneity:** Does the concentration effect differ between high-English and low-English countries? If ChatGPT primarily boosts Python (high-capability) in English-proficient countries but has smaller effects elsewhere, concentration should be higher in those countries — linking directly to the Rank 1 finding.

**Week 1 action:** Compute HHI and Shannon entropy from the raw dataset using pandas groupby. Plot raw trends by country income group. Run the event study TWFE regression. If pre-period β_τ are flat and post-period shows a level shift, you have a clean picture to build on.

---

```json
{
  "top_ideas": [
    {
      "rank": 1,
      "title": "English Proficiency as Exogenous Treatment Intensity: Geographic DiD of ChatGPT's Effect on Developer Activity",
      "research_question": "Did countries with higher pre-determined English proficiency experience disproportionate growth in software developer participation after ChatGPT's English-first launch in Q4 2022?",
      "method": "DiD with continuous treatment intensity (EF-EPI score × post-Q4 2022), country and quarter fixed effects, wild-cluster bootstrap inference",
      "sub_topic": "geographic_diffusion",
      "data_sources": [
        "Existing dataset (num_pushers, iso2_code, quarter)",
        "EF English Proficiency Index 2020 (ef.com, public)",
        "World Bank GDP per capita and broadband penetration (controls)",
        "Layoffs.fyi for tech layoff shock controls"
      ],
      "novelty": 5,
      "feasibility": 4,
      "impact": 5,
      "total_score": 5.0,
      "pitch": "ChatGPT launched in English, creating a natural experiment: countries whose developers already spoke English fluently received an immediate, full-intensity treatment, while low-proficiency countries faced an attenuated dose. English proficiency in 2020 is pre-determined and immutable, giving us a credibly exogenous source of variation. A triple-difference extending the design to the multilingual ChatGPT update (March 2023) can confirm the English-friction mechanism directly.",
      "first_experiment": "Merge EF-EPI 2020 country scores to the dataset on iso2_code. Compute a country×quarter panel of log(sum of num_pushers). Run the DiD regression with country and quarter FE, cluster SEs at country level, and plot a 12-quarter event study. Check whether pre-period coefficients on EPI×quarter are jointly zero (parallel trends), and whether the post-Q4 2022 coefficient is positive and significant."
    },
    {
      "rank": 2,
      "title": "ChatGPT Capability-Weighted DiD: Do Languages Where LLMs Excel Attract More Developers?",
      "research_question": "Did programming languages for which ChatGPT has demonstrably stronger code generation quality (measured by HumanEval pass@1 rates) gain disproportionately more active pushers after Q4 2022?",
      "method": "DiD with continuous treatment intensity (HumanEval pass@1 rate × post-Q4 2022), language×country and quarter fixed effects, pre-trend falsification",
      "sub_topic": "programming_language_adoption",
      "data_sources": [
        "Existing dataset (num_pushers, language, iso2_code, quarter)",
        "HumanEval/EvalPlus per-language pass@1 benchmarks (GitHub, public)",
        "Stack Overflow developer survey for baseline language popularity controls"
      ],
      "novelty": 4,
      "feasibility": 5,
      "impact": 5,
      "total_score": 4.9,
      "pitch": "LLMs are not equally capable across programming languages — their training data skews heavily toward Python and JavaScript, yielding pass@1 rates 3-4× higher than for legacy or domain-specific languages. This creates a continuous, pre-determined treatment intensity variable that is entirely exogenous to developer decisions. The 11-quarter pre-treatment period enables a rigorous parallel trends test, and a falsification using a placebo launch date can confirm the result is not driven by pre-existing Python growth.",
      "first_experiment": "Download HumanEval pass@1 scores by language from the EvalPlus GitHub repository and map to language names in the dataset. Compute language×quarter aggregates of log(num_pushers). Run the baseline DiD. Plot the raw time series for top-quintile vs. bottom-quintile capability languages — visual divergence post-Q4 2022 is the first sanity check before formal estimation."
    },
    {
      "rank": 3,
      "title": "Did ChatGPT Concentrate or Diversify the Language Ecosystem? A Country-Level Event Study of HHI",
      "research_question": "Did ChatGPT's release cause within-country language ecosystem concentration (fewer languages dominating) or diversification (long-tail growth), and does this vary by country English proficiency?",
      "method": "Event study (distributed lag model) on country×quarter Herfindahl-Hirschman Index and Shannon entropy, country and quarter fixed effects",
      "sub_topic": "ecosystem_concentration",
      "data_sources": [
        "Existing dataset only (num_pushers, language, iso2_code, quarter — sufficient to compute HHI and entropy)",
        "EF-EPI for heterogeneity analysis"
      ],
      "novelty": 4,
      "feasibility": 5,
      "impact": 4,
      "total_score": 4.6,
      "pitch": "Whether AI coding tools homogenize or diversify programming language use is a first-order question for software education and ecosystem resilience, yet no empirical evidence exists. The existing dataset directly enables computation of within-country HHI each quarter — no additional data needed. An event study design with 11 pre-periods can cleanly identify any structural break at Q4 2022, and a heterogeneity cut by English proficiency links this finding to the mechanism explored in Rank 1.",
      "first_experiment": "Use pandas to compute HHI_{c,q} = sum of squared language shares within each country-quarter. Plot average HHI over time, split by high vs. low English proficiency tercile. Run a TWFE event study with country and quarter FE, plotting 6 pre-period and 5 post-period coefficients. A flat pre-trend followed by a post-Q4 2022 level shift is the target pattern."
    }
  ]
}
```