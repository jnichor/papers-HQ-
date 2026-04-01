Now I have sufficient information to write the full literature review. Let me synthesize.

---

# Literature Review: "The Ratchet Effect — Commodity Booms Don't Undo What Busts Destroy"

---

## 1. Closest Existing Papers

### Paper 1: Caselli & Tesei (2016)
**Citation:** Caselli, F. & Tesei, A. (2016). "Resource Windfalls, Political Regimes, and Political Stability." *Review of Economics and Statistics*, 98(3), 573–590.

**Main Result:** Commodity price windfalls make autocracies *more* autocratic and politically stable but have no significant effect on democracies. The political effect of windfall gains is regime-conditional and nonlinear. Effect sizes are economically meaningful — a one standard deviation commodity price increase strengthens autocratic institutions by roughly 0.1–0.2 Polity IV units.

**Difference from proposed idea:**
- Tests *booms* only, not bust-recovery cycles. There is no asymmetry test.
- Uses aggregate regime type (Polity IV), not disaggregated civil liberties from V-Dem.
- The mechanism studied is elite entrenchment during windfalls, not repression persistence after bust.
- Time period extends to 2007; no focus on 1975–1994 specifically.

---

### Paper 2: Arezki & Brückner (2012)
**Citation:** Arezki, R. & Brückner, M. (2012). "Commodity Windfalls, Democracy and External Debt." *Economic Journal*, 122(561), 848–866.

**Main Result:** Commodity price windfalls reduce democracy scores in autocracies (using Polity and Freedom House) and increase external debt. Effect is concentrated in oil exporters. No analogous effect in democracies. Panel of 134 countries, 1970–2007, country and year FE.

**Difference from proposed idea:**
- Same directional test (boom → repression), but no bust episode or recovery analysis.
- Freedom House civil liberties is a single aggregate index; proposed paper uses all five disaggregated V-Dem liberties separately.
- No formal test of whether windfall-induced repression is reversed when commodity prices fall.
- No ratchet hypothesis; the question of *reversibility* is entirely absent.

---

### Paper 3: Bazzi & Blattman (2014)
**Citation:** Bazzi, S. & Blattman, C. (2014). "Economic Shocks and Conflict: Evidence from Commodity Prices." *American Economic Journal: Macroeconomics*, 6(4), 1–38.

**Main Result:** Using country-commodity export share weights as instruments, they find commodity export price booms *reduce* conflict onset (opportunity cost channel), while price busts have mixed and mostly insignificant effects on conflict. Challenges simple "resource curse = conflict" narrative.

**Difference from proposed idea:**
- Outcome is armed conflict, not civil liberties or political repression — a fundamentally different dimension of political stability.
- The export-share IV is methodologically close to CTOT identification, but the research design does not distinguish bust from recovery.
- No V-Dem data; no disaggregation by type of political freedom.
- Implicit symmetry assumption is never tested.

---

### Paper 4: Conrad & Moore (2010)
**Citation:** Conrad, C.R. & Moore, W.H. (2010). "What Stops the Torture?" *American Journal of Political Science*, 54(2), 459–476.

**Main Result:** Independent judiciaries — particularly constitutional prohibitions on torture with enforcement — are the primary constraint on torture initiation and continuation. International pressure and civil society have weaker effects. The determinants of *stopping* repression differ from the determinants of *starting* it, making this the closest published analog to a repression-asymmetry test.

**Difference from proposed idea:**
- The asymmetry is institutional (what constraints stop torture), not economic (do price recoveries reverse repression).
- No commodity price variation; no panel identification from economic shocks.
- Narrowly focused on torture/physical integrity, not the full spectrum of civil liberties (assembly, expression, electoral, etc.).
- Does not construct bust-recovery pairs or test symmetric reversal.

---

### Paper 5: Davenport (2007)
**Citation:** Davenport, C. (2007). "State Repression and the Tyrannical Peace." *Journal of Peace Research*, 44(4), 485–504.

**Main Result:** Repression exhibits strong autoregressive persistence ("the peace of the grave") — past repression is the strongest predictor of current repression, stronger than most political or economic determinants. Establishes the empirical foundation for the ratchet hypothesis without testing it causally.

**Difference from proposed idea:**
- Descriptive persistence, not causal asymmetry. Shows repression is sticky but does not exploit exogenous economic variation.
- No commodity price shocks; identification is lagged-dependent-variable OLS, not event study.
- Cannot distinguish "repression is persistent" from "determinants of repression are persistent."
- Does not separate bust from recovery episodes.

---

## 2. Methodological Precedents

### Precedent 1: The Export-Weighted Commodity Price Instrument
The identification strategy belongs to a well-established tradition originating with **Deaton & Miller (1996)** and refined by **Bazzi & Blattman (2014)** and **Caselli & Tesei (2016)**. The core insight: construct country-specific commodity price indices as a weighted average of world prices, using predetermined export shares as weights. Because world prices are set in global markets, this variation is plausibly exogenous to any single small economy's political outcomes.

**Credibility assessment:** High for the first stage. Commodity price movements are large, persistent, and driven by supply shocks (weather, geological discoveries) and demand from third-country economies — all plausibly orthogonal to country-specific political institutions. The main published critique (Bazzi & Blattman themselves discuss this) is that **global demand shocks** — particularly China's commodity supercycle — may simultaneously affect commodity prices *and* political institutions through growth channels, violating exclusion. This is especially acute for the 1975–1994 window, which overlaps with the oil shocks (1973, 1979, 1986), Cold War geopolitics, and the Third Wave of democratization — all confounded global forces. **Takeaway for this design:** The proposed paper must grapple explicitly with whether 1975–1994 confounders (Soviet collapse, debt crisis, Cold War patronage) are absorbed by the TWFE country and year fixed effects.

### Precedent 2: State-Dependent / Asymmetric Local Projections
**Ramey & Zubairy (2018)** ("Government Spending Multipliers in Good Times and in Bad," *Journal of Political Economy*) and **Jordà (2005)** ("Estimation and Inference of Impulse Responses by Local Projections," *AER*) establish the methodological template for asymmetric event studies with state-dependent responses. Ramey & Zubairy formally test whether fiscal multipliers differ in booms vs. recessions using the same LP-OLS approach that this paper would apply to bust vs. recovery episodes.

**Credibility assessment:** High methodological credibility — LP event studies are now standard and relatively assumption-free compared to VARs. The key design lesson: **the symmetry test must specify the null precisely**. Ramey & Zubairy use F-tests on the equality of impulse responses across states; this paper would analogously test whether the IRF for liberty during recovery equals (in absolute value) the IRF during bust. Without this formal test, the paper just produces two event-study plots and eyeballs them.

### Precedent 3: Staggered TWFE and Heterogeneity-Robust Estimators
**Callaway & Sant'Anna (2021)** (*Journal of Econometrics*) and **Sun & Abraham (2021)** (*Journal of Econometrics*) document that staggered-adoption TWFE estimators can produce sign-reversed estimates when treatment effects are heterogeneous across cohorts and time. Given that bust episodes occur at different times for different countries across 1975–1994, and that the political effects of busts almost certainly vary by pre-bust regime type, this heterogeneity problem is directly applicable.

**Credibility assessment:** The literature has a clear solution — use Callaway-Sant'Anna or Sun-Abraham estimators, or Borusyak et al. (2024) imputation estimator. A paper that applies standard TWFE without addressing this critique will face referee pushback. **Design lesson:** The paper should treat bust onset as staggered treatment and explicitly implement a heterogeneity-robust estimator, separating the response by pre-bust regime type as an effect modifier.

---

## 3. Gap Analysis

**What gap does this idea fill?**

The existing literature has established three things in isolation: (1) commodity booms entrench autocracies and erode civil liberties *during* booms (Caselli & Tesei; Arezki & Brückner); (2) repression is highly persistent in panel data (Davenport); and (3) the determinants of stopping repression differ from those of starting it (Conrad & Moore). What nobody has done is close the loop by exploiting *exogenous commodity bust-recovery pairs* to test whether the civil liberty losses induced by busts are reversed when prices recover. This is a genuine and consequential gap: it has direct bearing on whether commodity-exporting autocracies face any natural "democratic reset" when their fiscal crisis eases.

**Is the gap genuine or artificial?**

The gap is **genuine**, but partially explained by data availability timing:
- V-Dem was released publicly beginning in 2014–2016 and has only recently achieved sufficient coverage and disaggregation for this exercise. Researchers working on political economy of commodities before ~2015 had only Freedom House and Polity IV, both of which are coarse annual aggregates that obscure the within-regime variation across specific liberties.
- The CTOT dataset (Gruss & Kebhaj 2019) is itself recent, providing clean bust/recovery identification. Pre-2019, researchers would have had to construct comparable indices manually, discouraging exactly this design.
- The formal asymmetry test requires enough bust-recovery *pairs* to have statistical power. If a country's commodity price never recovered within the panel window (which is plausible for 1975–1994 given the depth of the 1986 oil price collapse), those pairs don't exist.

**Could the gap exist because the data doesn't support the test?**

Partially yes. The proposed 1975–1994 window is problematic for two reasons:
1. The CTOT dataset starts in 1980 per Gruss & Kebhaj (2019), meaning the first five years (1975–1979) may require alternative commodity price data and different weighting methodology.
2. The 1989–1994 period is dominated by the Soviet collapse and Third Wave democratization — a massive confound in which dozens of countries simultaneously experienced democratic transitions *and* commodity price disruptions for reasons unrelated to each other. Country-year fixed effects cannot fully absorb this if the timing of democratic transition correlates with bust depth.

---

## 4. Identification Assessment

**Source of exogenous variation:** World commodity prices, interacted with predetermined country-level export composition (the CTOT construction). This is a well-validated source of exogeneity. The key small-country assumption is defensible for most countries in the panel.

**Identification threats:**
1. **Global demand confounds:** The 1973–1982 oil shocks and 1986 oil price collapse were driven by OPEC decisions and global demand — not purely exogenous supply shocks. OPEC member countries (which are disproportionately in the sample) have endogenous production responses. This is a non-trivial violation.
2. **Third Wave democratization (1989–1994):** The political transitions of the early 1990s are not plausibly absorbed by year fixed effects alone, because their timing varied by country in ways correlated with economic conditions.
3. **Selection into bust episodes:** Countries that experienced deep busts (>1.5 SD) in 1975–1994 are not randomly selected — they tend to be commodity-dependent low-income autocracies, which is exactly the population where repression is already high and potentially on a different trend.
4. **Recovery definition endogeneity:** Defining recovery as "price returning above pre-bust level" means recovery timing depends on global commodity markets — plausibly exogenous — but the *duration* to recovery is correlated with country characteristics (import vs. export composition), introducing selection into the recovery group.

**Pre-trends:** Can be tested within the event study framework, but the 1975–1994 window is short enough that pre-bust windows for early busts may be very small, limiting power.

**Identification Tier: Tier 2–3.** The commodity price shock is a well-established instrument, pushing toward Tier 2. However, the asymmetric event study design stacks two treatments (bust onset, then recovery), introduces a non-trivial recovery selection problem, and operates across a historically turbulent period with multiple confounds that are not cleanly absorbed by TWFE. Realistically this is **Tier 3** unless the authors explicitly address the OPEC endogeneity and Cold War confounds with robustness tests.

---

## 5. Positioning Statement

This paper would be cited in future work on democratic backsliding, political economy of commodity exporters, and political persistence as the first study to formally test the asymmetry between repression installation and removal using exogenous commodity price variation. A future paper would write: *"Using bust-recovery pairs from the Gruss-Kebhaj commodity terms of trade dataset and disaggregated V-Dem civil liberty indicators, [Author] et al. show that freedom of assembly and expression are not restored when commodity prices recover, while personal integrity rights exhibit partial reversal — establishing causal evidence for the ratchet hypothesis in political repression that prior cross-sectional and time-series work (Davenport 2007; Conrad & Moore 2010) could only document descriptively."*

---

```json
{
  "closest_papers": [
    "Caselli & Tesei (2016)",
    "Arezki & Brückner (2012)",
    "Bazzi & Blattman (2014)",
    "Conrad & Moore (2010)",
    "Davenport (2007)"
  ],
  "gap_is_genuine": true,
  "gap_reason": "No existing paper tests the bust-vs-recovery symmetry of civil liberty effects using exogenous commodity price variation and disaggregated V-Dem indicators. The gap is partly explained by the recent availability of both V-Dem (post-2014) and the Gruss-Kebhaj CTOT dataset (2019), making this design only recently feasible.",
  "novelty_assessment": "HIGH",
  "methodological_risk": "HIGH",
  "positioning": "This paper would be the first to causally test the ratchet hypothesis in political repression — showing that specific civil liberties (assembly, expression) lost during commodity busts are not symmetrically restored during recoveries, while providing causal identification via exogenous commodity terms of trade shocks across a 50-80 country bust-recovery panel."
}
```

---

**Additional evaluator notes not captured in the JSON:**

- The HIGH methodological risk reflects three compounding concerns: (1) staggered TWFE heterogeneity bias, which requires Callaway-Sant'Anna or Borusyak imputation fixes; (2) the 1975–1994 window's overlap with Third Wave democratization and Cold War patronage structures as unabsorbed confounds; and (3) the recovery selection problem — if recovery is defined as prices exceeding pre-bust levels, and some countries never recover within the window, the "recovery treatment" is not randomly assigned. A referee at a top-5 journal will flag all three immediately.
- The HIGH novelty reflects that the combination of (a) formal symmetry test, (b) disaggregated V-Dem liberties, and (c) causal identification from CTOT shock pairs appears to be genuinely unoccupied in the literature, based on all available evidence through August 2025.