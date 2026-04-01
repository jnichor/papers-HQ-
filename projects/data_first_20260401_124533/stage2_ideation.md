# Research Advisory: Commodity Price Shocks and the Sequencing of Civil Liberty Erosion

---

## I. Literature Landscape: Themes, Methods, and Gaps

### Core Themes in the Literature

**Commodity shocks → political outcomes:** The foundational work (Brückner & Ciccone 2010; Bazzi & Blattman 2014) establishes that commodity price busts increase the risk of civil conflict in Sub-Saharan Africa, identifying variation via global price indices weighted by pre-determined export shares. The mechanism runs through fiscal stress: revenue collapse → austerity → grievance → state repression or insurgency.

**Resource curse and institutions:** Tsui (2011), Andersen & Aslaksen (2013), and the broader resource curse literature show that oil windfalls undermine democratic institutions, but the *channel* is typically studied at slow-moving institutional aggregates (Polity, Freedom House), not at the level of specific civil liberties.

**Repression as a political tool:** Davenport (2007) and Ritter (2014) demonstrate that repression is *strategic* — governments choose which rights to violate based on threat environments. But this work lacks exogenous economic shocks as a trigger.

**V-Dem disaggregated rights:** Coppedge et al. use V-Dem to study individual freedoms, but almost no paper has exploited V-Dem's multi-dimensional civil liberty data to study *sequencing* — the ordering in which freedoms collapse.

### Methodological Gaps

1. **No causal sequencing analysis.** Literature treats civil liberties as a scalar index; V-Dem's five-dimensional structure (`freexp`, `freass`, `frerel`, `fremov`, `fairtrial`) is nearly unexploited for ordering analysis.
2. **Asymmetry neglected.** Virtually no paper tests whether boom-era liberty gains are symmetric with bust-era losses (ratchet effect hypothesis).
3. **Duration ignored.** No paper models how the *length* of a price slump, not just its magnitude, determines irreversibility of liberty erosion.
4. **Mechanism black box.** The path from price shock → repression typically skips the political economy of which freedoms governments *strategically target first*.
5. **Reversal dynamics absent.** What happens when prices recover? The literature assumes the question is symmetric; almost no paper tests this.

---

## II. 8–10 Research Ideas

---

### Idea 1 — The Domino Sequence: Which Freedom Falls First?
**Sub-topic: Sequencing dynamics**

**Research Question:** Do commodity price collapses trigger civil liberty erosion in a statistically predictable sequence, and does freedom of assembly consistently precede erosion of expression, movement, religion, and fair trial?

**Method — Tier 1 (TWFE Event Study + Markov Transition Matrices):**
- Construct a country-year commodity price shock variable using the Gruss-Kebhaj (2019) terms-of-trade shock: global price index weighted by initial export basket shares (predetermined), generating exogenous within-country year-to-year variation.
- **Primary:** TWFE event study on each of the 5 liberty outcomes, with event = commodity price shock exceeding −1.5 SD. Include country FE (absorbs all time-invariant heterogeneity) and year FE (absorbs global shocks). Estimate leads/lags k = −5 to +10.
- **Secondary:** Discretize each liberty into quartile states. Construct Markov transition matrices conditional on shock timing. Test whether `freass` states deteriorate with shorter lag than `freexp`, `fairtrial`, etc. using non-parametric rank tests on first-passage times.

**(a) Exogenous variation:** Global commodity price movements (supply-driven, exogenous to any single country's political decisions) × initial export composition (predetermined). This is the Bazzi-Blattman instrument.
**(b) Pre-treatment periods:** With T=51, shocks scattered across the sample give 5–15 pre-event periods per episode.
**(c) Parallel trends:** Testable across k=−5 to −1; 200 countries × multiple episodes gives ~300–400 country-event pairs after restricting to non-overlapping episodes.
**(d) Clusters:** 200 countries — sufficient for cluster-robust SE and wild-bootstrap.
**(e) Exogeneity threats:** Global prices are exogenous; the only threat is if initial export shares correlate with unobserved political trends. Mitigate by using shares lagged 10 years and testing robustness with Bartik-style overidentification.

**Data:** V-Dem (in hand) + IMF Primary Commodity Prices + Gruss-Kebhaj CTOT dataset.

**Novelty:** No paper has studied the *ordering* of civil liberty deterioration using causal identification. This reframes the resource curse from "do rights fall?" to "which rights fall first, and why?"

**Impact:** Direct policy implication — monitors can use early-warning indicators (e.g., assembly restrictions) as leading indicators of broader repression.

| Novelty | Feasibility | Impact | Base Score | +Causal | +Panel | **Total** |
|---------|-------------|--------|------------|---------|--------|-----------|
| 5 | 4 | 5 | 4.7 | +0.3 | +0.3 | **5.3** |

---

### Idea 2 — Oil vs. Grain: Does Commodity Type Determine the Repression Menu?
**Sub-topic: Commodity type heterogeneity**

**Research Question:** Do oil exporters sequence civil liberty erosion differently than agricultural commodity exporters following equivalent price shocks, reflecting differences in state capacity, rent distribution, and protest ecology?

**Method — Tier 2 (TWFE with Interaction Terms):**
- Classify countries by primary commodity export type (oil/gas vs. metals vs. agriculture) using UNCTAD TRAINS data.
- Estimate TWFE with commodity-type × shock interaction: `liberty_it = α_i + γ_t + β₁·shock_it + β₂·shock_it×OilExporter_i + ε_it`.
- Test joint significance of type interactions across all 5 liberty outcomes. Use Holm-Bonferroni for multiple comparisons.

**(a)-(e):** Same shock identification as Idea 1. Type classification is predetermined (time-invariant initial export structure). 200 countries with ~80 oil/gas, ~40 metals, ~80 agricultural exporters provides sufficient within-type variation.

**Data:** V-Dem + Gruss-Kebhaj + UNCTAD TRAINS commodity classification.

**Novelty:** Resource curse literature treats all commodity shocks symmetrically. Oil's rent-based patronage vs. agriculture's labor-intensive structure suggests qualitatively different repression logics.

| Novelty | Feasibility | Impact | Base Score | +Causal | +Panel | **Total** |
|---------|-------------|--------|------------|---------|--------|-----------|
| 4 | 4 | 4 | 4.0 | +0.3 | +0.3 | **4.6** |

---

### Idea 3 — Regime as Amplifier: Do Autocracies Suppress Strategically, Democracies Randomly?
**Sub-topic: Political regime interaction**

**Research Question:** Does regime type (V-Dem electoral democracy index) moderate both the magnitude and the *ordering* of civil liberty erosion following commodity shocks?

**Method — Tier 1 (DiD with Heterogeneous Treatment Effects):**
- Define a binary "severe shock" treatment (−2SD in commodity price index).
- Split sample into pre-classified regime groups (democratic / hybrid / autocratic) using V-Dem Liberal Democracy Index at t-5 (predetermined).
- Estimate heterogeneous DiD: `liberty_it = α_i + γ_t + β·shock_it×RegimeType_i + ε_it`.
- Test whether the *cross-liberty* sequence differs by regime type using seemingly unrelated regressions (SUR) and Chi-squared tests on coefficient vectors.

**(a)-(e):** Shock is exogenous; regime type classified at t-5 reduces reverse causality. Pre-periods allow parallel trends test within each regime group. Cluster at country level; ~65 countries per group in each category.

**Data:** V-Dem (all variables in hand).

**Novelty:** Medium — regime moderation is studied in conflict literature but not for civil liberty sequencing. Main contribution is the SUR-based ordering test.

| Novelty | Feasibility | Impact | Base Score | +Causal | +Panel | **Total** |
|---------|-------------|--------|------------|---------|--------|-----------|
| 3 | 5 | 4 | 3.9 | +0.3 | +0.3 | **4.5** |

---

### Idea 4 — The Ratchet: Are Commodity Booms Symmetric with Busts?
**Sub-topic: Boom-bust asymmetry and restoration**

**Research Question:** Do civil liberties that erode during commodity busts recover symmetrically during subsequent booms, or does repression exhibit a ratchet — easy to install, hard to remove?

**Method — Tier 1 (Event Study with Asymmetric Treatment, Panel):**
- Define two event types: (A) bust episodes (−1.5SD shock), (B) recovery episodes (price returning above pre-bust level).
- Estimate separate event study impulse response functions for each liberty under bust and boom treatments.
- Formally test symmetry: H₀: β_bust(k) = −β_boom(k) for each k. Reject with joint F-test.
- Add interaction: `freass_it = α_i + γ_t + Σ_k δ_k·bust(k)_it + Σ_k φ_k·boom(k)_it + ε_it`

**(a)-(e):** Both bust and boom are defined via the exogenous commodity price shock index. With T=51 and 200 countries, can identify ~50–80 bust-recovery pairs. Pre-trends testable for 5 pre-periods. Country FE removes baseline differences.

**Data:** V-Dem (in hand) + Gruss-Kebhaj CTOT.

**Novelty:** Nearly no paper tests asymmetry in civil liberties. The ratchet hypothesis is theorized (Davenport 2007) but never causally tested at this level of disaggregation.

**Impact:** If confirmed, the ratchet implies permanent democratic backsliding from temporary economic shocks — a fundamentally different policy message than the "reversible" view.

| Novelty | Feasibility | Impact | Base Score | +Causal | +Panel | **Total** |
|---------|-------------|--------|------------|---------|--------|-----------|
| 5 | 4 | 5 | 4.7 | +0.3 | +0.3 | **5.3** |

---

### Idea 5 — How Long Until Permanent Damage? Duration and Irreversibility
**Sub-topic: Persistence and duration dependence**

**Research Question:** Does the duration of a commodity price depression (not just its magnitude) predict the permanent collapse of a specific civil liberty, suggesting a "tipping point" in repression dynamics?

**Method — Tier 2 (Discrete-Time Hazard Model with Country FE):**
- Define "liberty collapse event" as a 3-year-sustained drop of ≥0.5 SD in a given liberty index.
- Model: complementary log-log hazard with country FE, time-varying covariate = duration of ongoing price depression (years below shock threshold).
- Include duration-squared to test non-linearity. Separate models for each liberty.
- Use correlated random effects (Mundlak device) as robustness if FE incidental parameters cause issues.

**(a)-(e):** Duration of price shock is a function of global prices (exogenous). With T=51 and variation in shock start/end dates across 200 countries, adequate variation in duration. Survival framework exploits full panel time dimension.

**Data:** V-Dem (in hand) + Gruss-Kebhaj CTOT.

**Novelty:** Hazard models for civil liberty collapse are rare; combining them with exogenous commodity shock duration is novel. Tests whether there is a "point of no return" for specific freedoms.

| Novelty | Feasibility | Impact | Base Score | +Causal | +Panel | **Total** |
|---------|-------------|--------|------------|---------|--------|-----------|
| 4 | 4 | 4 | 4.0 | +0.3 | +0.3 | **4.6** |

---

### Idea 6 — Strategic Assembly Suppression: Governments' First Move
**Sub-topic: Strategic repression mechanisms**

**Research Question:** Do governments *strategically target* freedom of assembly before other civil liberties following commodity shocks, because assembly is the most direct threat to fiscal austerity protests?

**Method — Tier 2 (TWFE with Granger-causal ordering + Mediation):**
- Estimate TWFE impulse responses for all 5 liberties.
- Formally test temporal ordering: does `freass` deteriorate at lag k=1 while `freexp`, `frerel`, `fremov`, `fairtrial` deteriorate at k=2,3? Use Granger-non-causality tests in the panel VAR (Holtz-Eakin, Newey, Rosen 1988 approach for panel VAR).
- Add protest data (ACLED or Mass Mobilization Project) as mediator to test the mechanism: shock → anticipated protest → assembly restriction → broader erosion.
- Panel VAR with 4 lags, country and year FE, Cholesky ordering tested via restrictions.

**(a)-(e):** The exogenous shock instrument applies. Panel VAR with 200 countries and T=51 gives adequate degrees of freedom. Protest data available from ACLED for most of the sample period.

**Data:** V-Dem (in hand) + ACLED/MMD protest data + Gruss-Kebhaj CTOT.

**Novelty:** Mechanism identification — *why* assembly is targeted first — is completely absent from the literature. This connects the political economy of protest to the repression sequence.

| Novelty | Feasibility | Impact | Base Score | +Causal | +Panel | **Total** |
|---------|-------------|--------|------------|---------|--------|-----------|
| 5 | 4 | 5 | 4.7 | +0.3 | +0.3 | **5.3** |

---

### Idea 7 — Pre-emptive Repression: Do Governments Act Before Prices Fall?
**Sub-topic: Anticipatory repression**

**Research Question:** Do commodity-dependent governments erode civil liberties *before* price collapses materialize, using futures market price signals as early warning of fiscal stress?

**Method — Tier 1 (Event Study with Lead Structure):**
- Use commodity futures prices (available from Bloomberg/CME for major commodities since ~1980) as a forward-looking shock indicator. Separate the *anticipated* shock (futures-implied price path) from the *realized* shock.
- Event study: `liberty_it = α_i + γ_t + Σ_{k=-5}^{+5} β_k·anticipated_shock_it(k) + ε_it`
- Test whether β_{k<0} significantly negative (pre-emptive repression) vs. β_{k>0} (reactive repression).

**(a)-(e):** Futures prices are exogenous to domestic political decisions. Pre-period tests span k=−5 to −1. Availability of futures data limits sample to post-1980, ~40 years, but still ~8,000 obs. Key threat: governments may have private information about commodity prices — but futures markets aggregate this.

**Data:** V-Dem (in hand) + Bloomberg futures prices + Gruss-Kebhaj CTOT.

**Novelty:** Very high — anticipatory repression using futures market signals is a genuinely new identification angle. Tests whether repression is forward-looking, not just reactive.

| Novelty | Feasibility | Impact | Base Score | +Causal | +Panel | **Total** |
|---------|-------------|--------|------------|---------|--------|-----------|
| 5 | 3 | 5 | 4.4 | +0.3 | +0.3 | **5.0** |

---

### Idea 8 — Spatial Contagion: Does My Neighbor's Repression Spread to Me?
**Sub-topic: International spillovers**

**Research Question:** Does civil liberty erosion in one commodity-exporting country, triggered by a shared price shock, spread to neighboring exporters via demonstration effects or competitive repression?

**Method — Tier 2 (Spatial TWFE):**
- Construct spatial weight matrix based on geographic proximity + commodity type similarity.
- Estimate: `liberty_it = α_i + γ_t + ρ·W·liberty_t + β·shock_it + ε_it`
- Test spatial autocorrelation conditional on common year shocks (Moran's I after TWFE residuals). Use Driscoll-Kraay SE for cross-sectional dependence.

**(a)-(e):** Spatial lag instrumented with neighbors' commodity shocks (standard Spatial IV). Cross-sectional dependence is a real concern with 200 countries but year FE absorbs global component. Residual spatial clustering after TWFE is the object of interest.

**Data:** V-Dem (in hand) + Gruss-Kebhaj CTOT + CEPII gravity data for distance matrix.

**Novelty:** Spatial diffusion of civil liberty erosion via commodity shocks has not been studied. Connects "authoritarian diffusion" literature to economic shocks.

| Novelty | Feasibility | Impact | Base Score | +Causal | +Panel | **Total** |
|---------|-------------|--------|------------|---------|--------|-----------|
| 4 | 3 | 4 | 3.7 | +0.3 | +0.3 | **4.3** |

---

### Idea 9 — The Fair Trial Last Bastion: Is Judicial Independence the Most Durable Freedom?
**Sub-topic: Institutional durability of specific rights**

**Research Question:** Is `fairtrial` systematically the *last* civil liberty to erode under commodity shocks (relative to assembly, expression, movement, religion), reflecting judicial independence as a structural constraint on executive repression?

**Method — Tier 2 (TWFE + SUR Cross-Equation Test):**
- Estimate TWFE for each liberty simultaneously in a SUR system.
- Test the null that the impulse response for `fairtrial` declines at the same rate as `freass` (the hypothesized "first mover") using Wald tests across equations.
- Construct a "repression sequence index" using the timing of each liberty's first statistically significant negative response, and regress this index on judicial independence measures (V-Dem `v2juncind`).

**(a)-(e):** Standard shock identification. SUR exploits cross-equation restrictions from the joint system. Judicial independence is predetermined if measured before shock.

**Data:** V-Dem (all variables in hand).

**Novelty:** Framing judicial independence as a *speed bump* in the repression sequence is new and theoretically grounded in separation of powers literature.

| Novelty | Feasibility | Impact | Base Score | +Causal | +Panel | **Total** |
|---------|-------------|--------|------------|---------|--------|-----------|
| 4 | 5 | 4 | 4.3 | +0.3 | +0.3 | **4.9** |

---

### Idea 10 — Threshold Effects: Non-Linear Collapse Below a Price Floor
**Sub-topic: Non-linear repression dynamics**

**Research Question:** Is there a price decline threshold beyond which civil liberty erosion accelerates non-linearly — a fiscal "cliff edge" where multiple liberties collapse simultaneously?

**Method — Tier 2 (Arellano-Bond GMM + Threshold Panel):**
- Estimate dynamic panel: `liberty_it = α·liberty_{it-1} + β·shock_it + δ·shock_it·𝟙(shock>τ) + α_i + ε_it`
- Use Arellano-Bond (1991) GMM to instrument for lagged dependent variable.
- Estimate threshold τ endogenously using Hansen (1999) panel threshold regression.
- Test whether the threshold coincides across all 5 civil liberties (simultaneous collapse) or is liberty-specific.

**(a)-(e):** Arellano-Bond instruments are internal (lagged levels). With N=200 and T=51, instrument proliferation is manageable with instrument collapse (Roodman 2009). The shock remains exogenous. Key threat: instrument validity requires no serial correlation in ε_it beyond AR(1); test with Arellano-Bond AR(2) test.

**Data:** V-Dem (in hand) + Gruss-Kebhaj CTOT.

**Novelty:** Non-linear threshold models for repression under economic shocks are rare. Tests the "tipping point" narrative with rigorous econometrics.

| Novelty | Feasibility | Impact | Base Score | +Causal | +Panel | **Total** |
|---------|-------------|--------|------------|---------|--------|-----------|
| 4 | 3 | 4 | 3.7 | +0.3 | +0.3 | **4.3** |

---

## III. Idea Ranking Summary

| Rank | Idea | Sub-topic | Method | Tier | Total Score |
|------|------|-----------|--------|------|-------------|
| 1 | Domino Sequence (Idea 1) | Sequencing dynamics | TWFE Event Study + Markov | 1–2 | **5.3** |
| 1 | Strategic Assembly Suppression (Idea 6) | Strategic repression mechanisms | TWFE + Panel VAR | 1–2 | **5.3** |
| 1 | Ratchet / Restoration Asymmetry (Idea 4) | Boom-bust asymmetry | Event Study (asymmetric) | 1 | **5.3** |
| 4 | Anticipatory Repression (Idea 7) | Anticipatory repression | Event Study with leads | 1 | **5.0** |
| 5 | Fair Trial Last Bastion (Idea 9) | Institutional durability | TWFE + SUR | 2 | **4.9** |
| 6 | Commodity Type Heterogeneity (Idea 2) | Commodity type | TWFE interaction | 2 | **4.6** |
| 6 | Duration/Hazard (Idea 5) | Persistence | Hazard model + FE | 2 | **4.6** |
| 6 | Boom-Bust Asymmetry (Idea 10) | Non-linear dynamics | A-B GMM + Threshold | 2 | **4.3** |
| 9 | Spatial Contagion (Idea 8) | International spillovers | Spatial TWFE | 2 | **4.3** |
| 10 | Regime Moderation (Idea 3) | Political institutions | DiD heterogeneous | 1 | **4.5** |

**Tie-breaking rule:** Among the three ideas tied at 5.3, I differentiate by *distinctiveness of contribution*:
- Idea 1 is the *headline finding* (what is the sequence?)
- Idea 6 is the *mechanism paper* (why does assembly fall first?)
- Idea 4 is the *policy-critical asymmetry paper* (is repression permanent?)

All three are from different sub-topics ✓. All three use panel methods ✓. All three use Tier 1–2 methods ✓.

---

## IV. Top 3 Ideas — Elaborated

---

### TOP IDEA #1: The Domino Sequence
**"Do Commodity Price Collapses Trigger Predictable Sequences of Civil Liberty Erosion? Evidence from 200 Countries, 1970–2020"**

**Research Question:** When a commodity price collapse hits an export-dependent country, which civil liberty erodes first — and does this sequence follow a predictable political-economic logic?

**Full Identification Strategy:**

*Step 1 — Construct exogenous commodity price shock:*
Use the Gruss-Kebhaj (2019) Commodity Terms of Trade (CTOT) shock, defined as the change in the log commodity export price index weighted by initial export shares from the UN Comtrade database (shares measured at t-10 to ensure they are predetermined). This generates a country-year variable that moves with global supply and demand (exogenous) but is scaled by each country's initial commodity dependence (time-invariant).

*Step 2 — TWFE event study:*
Define a "bust episode" as CTOT falling more than 1.5 standard deviations below its country-specific trend for at least 2 consecutive years. Estimate:

```
Y_{i,t} = α_i + γ_t + Σ_{k=-5}^{+10} β_k · D_{i,t+k} + X_{it}Γ + ε_{it}
```

where D_{i,t+k} is an indicator for being k years from episode start, for each of the 5 civil liberty outcomes separately. Plot impulse response functions with 95% confidence intervals (clustered at country level). Pre-trend test: joint F-test on k = −5 to −1.

*Step 3 — First-passage time analysis (Markov):*
Discretize each liberty into 4 ordered states. For each country-episode pair, record the year in which each liberty first transitions from state S to S−1. Compute non-parametric distributions of first-passage times for each liberty. Rank liberties by median first-passage time. Test pairwise rank differences using Mann-Whitney U tests, Holm-Bonferroni corrected.

*Step 4 — SUR confirmation:*
Estimate all 5 liberty equations jointly (SUR) and test whether the coefficient vectors are ordered as predicted by the Markov analysis. This provides cross-equation identification.

**Threats and Mitigations:**

| Threat | Mitigation |
|--------|-----------|
| Initial export shares endogenous | Use t-10 shares; Bartik overidentification test |
| Parallel trends violated | Plot pre-trends; add country-specific trends as robustness |
| Serial correlation | Driscoll-Kraay SE; AR(1) correction |
| "Commodity shocks" pick up other shocks | Saturate with GDP growth, political controls; test robustness to excluding oil shocks |

**Data requirements:**
- V-Dem civil liberty indices (all 5 in hand)
- Gruss-Kebhaj CTOT dataset (World Bank, freely available)
- UN Comtrade for export share construction (alternative: Bazzi-Blattman replication data, publicly available)

**Timeline for first 3 months:**
- Month 1: Clean and merge V-Dem + CTOT; identify bust episodes (est. ~250 country-episodes); run baseline TWFE
- Month 2: Markov transition matrices; first-passage time ranking
- Month 3: SUR system; robustness checks; draft introduction

**Why this will be published:** The paper answers a question no one has addressed with causal identification — not "do rights fall?" but "in what order?" — using the richest civil liberty panel data available. The combination of event study + Markov transition analysis is methodologically clean and narrative-ready. A clear answer (e.g., "assembly always falls first, fair trial last") is the kind of finding that lands in APSR or JDE.

---

### TOP IDEA #2: Strategic Assembly Suppression as Governments' First Move
**"Protest Preemption: Why Freedom of Assembly Is the Targeted First When Commodity Revenues Fall"**

**Research Question:** Do governments strategically target freedom of assembly before other civil liberties following commodity price shocks, because preempting collective action is the most cost-effective response to anticipated fiscal protests?

**Full Identification Strategy:**

*Core empirical design — Panel VAR with external instrument:*
Estimate a 5-variable panel VAR in first differences of all civil liberty indices, instrumented by the Gruss-Kebhaj CTOT shock:

```
ΔY_{it} = A(L)·ΔY_{it} + B·shock_{it} + α_i + γ_t + ε_{it}
```

where Y_{it} = (freass, freexp, fremov, frerel, fairtrial)'. Use the Holtz-Eakin, Newey, Rosen (1988) panel VAR estimator with forward orthogonal deviations to eliminate fixed effects without introducing MA bias.

*Causal ordering test:*
Estimate Cholesky decomposition with freass first; test whether this ordering is consistent with the data using likelihood ratio tests on structural restrictions. Compare with reverse ordering (fairtrial first).

*Mediation analysis — protest threat:*
Add protest incidence (ACLED, Mass Mobilization Project) as intermediate variable. Estimate:
1. shock → protest_probability (Probit with country FE)  
2. protest_probability → freass_deterioration (TWFE, IV: lagged shock)
3. Test partial mediation: does controlling for protest_probability reduce the direct shock → freass coefficient?

*Mechanism cross-check:*
Compare the assembly-first finding across two sub-samples: countries with high social movement capacity (V-Dem `v2csrlgrp`) vs. low. If the mechanism is protest preemption, the assembly-first pattern should be *stronger* in high-capacity countries.

**(a) Exogenous variation:** CTOT shock (global prices × initial shares). In the mediation chain, the CTOT shock instruments for fiscal pressure, which drives both protest and repression.

**(b) Pre-treatment periods:** 5–15 per episode; ample for pre-trend tests.

**(c) Parallel trends:** With N=200 and T=51, and given that CTOT shocks affect countries at different times, parallel trends is testable across multiple windows.

**(d) Clusters:** 200 country-level clusters; panel VAR inference uses block bootstrap.

**(e) Exogeneity:** Main threat is that CTOT shocks also trigger other governance changes correlated with assembly restrictions (e.g., state capacity decline). Test: does the assembly-first result hold when controlling for GDP, state capacity, and political turnover?

**Data requirements:**
- V-Dem (in hand)
- Gruss-Kebhaj CTOT
- ACLED protest event database (2000–present) or Mass Mobilization Project (1990–2019)

**Why this will be published:** The paper connects three literatures that have never been formally linked: commodity shocks, protest cycles, and targeted repression. The mediation design with an external instrument is methodologically sophisticated without being unapproachable. If the protest-preemption mechanism holds empirically, this has immediate implications for human rights monitoring — assembly restrictions are the *early warning signal*, not a lagging indicator.

---

### TOP IDEA #3: The Ratchet Effect — Liberty Losses Outlast Price Recoveries
**"Asymmetric Repression: Commodity Booms Don't Undo What Busts Destroy"**

**Research Question:** When commodity prices recover after a bust, do civil liberties restore symmetrically? Or does repression exhibit a ratchet — easily installed during crises, resistant to reversal during recoveries?

**Full Identification Strategy:**

*Asymmetric event study design:*
Identify two event types from the CTOT series:
- Type A (Bust): CTOT falls >1.5 SD below trend for ≥2 years
- Type B (Recovery): CTOT rises back above pre-bust level within 10 years of a Type A episode

Estimate separate but jointly identified event study:

```
Y_{it} = α_i + γ_t + Σ_{k=-5}^{+10} δ_k·Bust_{it+k} + Σ_{k=-5}^{+10} φ_k·Recovery_{it+k} + ε_{it}
```

Note: Bust and Recovery events are non-overlapping by construction.

*Symmetry test:*
Test H₀: δ_k = −φ_k for k = 1, 2, ..., 10 jointly. Rejection implies asymmetry.

*Liberty-specific asymmetry:*
Run the above for each of 5 civil liberties. Construct asymmetry index: A_j = |β_bust(10)| − |β_recovery(10)| for liberty j. Rank liberties by asymmetry. Test whether the liberty that falls first (from Idea 1) also exhibits the greatest asymmetry.

*Mechanism — Bureaucratic lock-in:*
Test whether asymmetry is larger in countries with weaker rule of law (`v2juncind`, V-Dem), consistent with a "bureaucratic capture" model where repressive institutions become self-reinforcing.

*Pre-registration plan:*
Pre-register the symmetry test and the liberty ranking as primary hypotheses; the mechanism test as exploratory.

**(a) Exogenous variation:** Both bust and recovery are driven by global commodity prices (exogenous). Recovery is identified as a positive price reversal after an exogenously-caused bust — the recovery itself need not be exogenous if we condition on the prior bust.

**(b)-(c):** With T=51 and ~50–80 bust-recovery pairs across 200 countries, adequate pre-periods per episode. Parallel trends testable for bust events; recovery parallel trends conditional on experiencing a bust.

**(d)-(e):** 200 clusters; key threat is selective exit (countries that experience state collapse may drop out). Address with inverse probability weighting for attrition.

**Data requirements:**
- V-Dem (in hand)
- Gruss-Kebhaj CTOT

**Why this will be published:** The ratchet hypothesis — widely cited in political science theory — has never been tested with causal identification on disaggregated civil liberty data. A clear finding that some liberties are permanent losses while others recover would be a landmark result. The paper is feasible with data already in hand, and the symmetry test is clean enough for a single-table main result.

---

## V. JSON Output

```json
{
  "top_ideas": [
    {
      "rank": 1,
      "title": "The Domino Sequence: Commodity Price Collapses and the Predictable Ordering of Civil Liberty Erosion",
      "research_question": "When a commodity price collapse hits an export-dependent country, which civil liberty erodes first — and does this sequence follow a predictable political-economic logic across 200 countries?",
      "method": "TWFE Event Study + Markov Transition Matrices (Panel VAR robustness)",
      "tier": 1,
      "identifying_variation": "Global commodity price index weighted by predetermined country export shares (Gruss-Kebhaj CTOT shock)",
      "sub_topic": "Sequencing dynamics",
      "data_sources": ["V-Dem (freexp, freass, frerel, fremov, fairtrial)", "Gruss-Kebhaj Commodity Terms of Trade dataset (World Bank)", "UN Comtrade for export share construction"],
      "novelty": 5,
      "feasibility": 4,
      "impact": 5,
      "total_score": 5.3,
      "pitch": "No paper has studied the ordering of civil liberty deterioration under commodity shocks using causal identification. Using V-Dem's unique five-dimensional civil liberty data and exogenous CTOT shocks, this paper answers 'which freedom falls first?' — reframing the resource curse from a scalar outcome to a temporal sequence with early-warning implications for human rights monitors.",
      "first_experiment": "Week 1: Merge V-Dem with Gruss-Kebhaj CTOT data; identify ~250 country-level bust episodes (CTOT > 1.5 SD decline for ≥2 years); estimate TWFE event study for all 5 civil liberties and plot impulse response functions with pre-trend tests to verify identification."
    },
    {
      "rank": 2,
      "title": "Protest Preemption: Why Freedom of Assembly Is Targeted First When Commodity Revenues Fall",
      "research_question": "Do governments strategically target freedom of assembly before other civil liberties following commodity price shocks because preempting collective action is the most cost-effective response to anticipated fiscal protests?",
      "method": "Panel VAR (Holtz-Eakin-Newey-Rosen) with CTOT instrument + Mediation via protest incidence",
      "tier": 2,
      "identifying_variation": "CTOT shock instruments for fiscal stress; protest data mediates the assembly-first mechanism",
      "sub_topic": "Strategic repression mechanisms",
      "data_sources": ["V-Dem (all 5 liberties + civil society capacity index)", "Gruss-Kebhaj CTOT dataset", "ACLED protest event database or Mass Mobilization Project"],
      "novelty": 5,
      "feasibility": 4,
      "impact": 5,
      "total_score": 5.3,
      "pitch": "This paper provides the first causal test of why, not just whether, governments sequence repression after commodity shocks. Using panel VAR with an external instrument and protest-incidence mediation, it shows that assembly is preemptively restricted before other liberties specifically in countries with higher protest capacity — turning assembly restrictions into a leading indicator of broader democratic backsliding.",
      "first_experiment": "Week 1: Download ACLED country-year protest event counts (or Mass Mobilization Project); merge with V-Dem and CTOT data; run reduced-form TWFE regressions of freass on CTOT shock and compare lag structure to freexp/fremov/frerel to establish the raw timing differential before formal panel VAR estimation."
    },
    {
      "rank": 3,
      "title": "The Ratchet Effect: Commodity Booms Don't Undo What Busts Destroy",
      "research_question": "When commodity prices recover after a bust, do civil liberties restore symmetrically, or does repression exhibit a ratchet — easily installed during crises but resistant to reversal during recoveries?",
      "method": "Asymmetric Event Study (TWFE) with bust and recovery episodes; joint symmetry test",
      "tier": 1,
      "identifying_variation": "Both bust and recovery events driven by exogenous global commodity price movements (CTOT); recovery identified conditional on prior exogenous bust",
      "sub_topic": "Boom-bust asymmetry and restoration",
      "data_sources": ["V-Dem (all 5 liberties + judicial independence v2juncind)", "Gruss-Kebhaj CTOT dataset"],
      "novelty": 5,
      "feasibility": 4,
      "impact": 5,
      "total_score": 5.3,
      "pitch": "The ratchet hypothesis — that repression is easy to install but hard to remove — is widely theorized but never causally tested on disaggregated civil liberty data. Using ~50-80 bust-recovery pairs across 200 countries, this paper formally rejects or confirms symmetry for each civil liberty, with the finding that specific freedoms (likely assembly, expression) are permanently lost while others partially recover constituting a landmark result for democratic backsliding theory.",
      "first_experiment": "Week 1: Using CTOT data, identify all bust episodes (>1.5 SD decline, ≥2 years) and their recovery dates (price returning above pre-bust level) within the 51-year panel; plot raw V-Dem liberty time series for a sample of 10-15 countries around bust-recovery pairs to visually inspect asymmetry before estimating the formal event study."
    }
  ]
}
```

---

**A note on data self-sufficiency:** All three top ideas are largely executable with data already in hand (V-Dem panel) plus one freely downloadable dataset (Gruss-Kebhaj CTOT, World Bank). The only optional add-on is ACLED for Idea 2's mediation analysis — but even without it, the core panel VAR result stands. This is a rare configuration where the most ambitious causal designs are also the most feasible.