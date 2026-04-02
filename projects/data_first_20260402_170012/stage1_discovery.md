{
  "path": "C",
  "topic": "First Oil Production and the Long-Run Path of Political Institutions",
  "qualified_datasets": 1,
  "selected_dataset": "Oil, Gas and Political Institutions (Ross-Mahdavi 1932-2014)",
  "feasibility": {
    "max_tier": 1,
    "tier_label": "CAUSAL (all methods available)",
    "score_ceiling": 85,
    "allowed_methods": [
      "DiD",
      "staggered DiD",
      "event study",
      "IV/2SLS",
      "RDD",
      "synthetic control",
      "TWFE",
      "individual FE"
    ],
    "forbidden_methods": [],
    "warnings": [
      "High missingness: gas_prod55_14 (43%), gas_value_nom (43%), gas_value_2000 (43%), gas_value_2014 (43%), oil_exports (71%)",
      "Some variables have low within-unit variation: iso3numeric (within/total=0.00), gas_prod55_14 (within/total=0.12). Consider using these as controls, not outcomes."
    ],
    "best_structure": "panel",
    "best_rows": 15521,
    "best_cols": 41,
    "n_periods": 83,
    "n_ordinal_vars": 1,
    "n_continuous_vars": 36,
    "self_contained": true
  },
  "suggestions": [
    {
      "dataset_index": 1,
      "topic": "Oil Price Windfalls and Democratic Erosion",
      "research_question": "Do positive oil revenue windfalls cause political institutions to deteriorate (the 'resource curse'), using global price shocks as exogenous variation in windfall size?",
      "method": "DiD with event study around major price shocks (1973, 1979, 1986, 2008)",
      "identification_level": "B",
      "identification": "Global oil prices (oil_price_2000) are set on world markets and exogenous to any single country's politics. Countries with higher pre-shock oil production capacity (oil_prod32_14 measured in a pre-period window) receive larger revenue windfalls from the same price movement. Treatment intensity = pre-determined production × price shock, so selection into 'high exposure' is not driven by contemporaneous political choices.",
      "control_group": "Non-producing or very-low-producing countries face near-zero windfall from the same global price shock and serve as the dose-zero comparison group. Within the set of producers, low-production countries are the low-dose control for high-production countries.",
      "score_potential": "Level B dose variation + 80+ years of panel + multiple price shock events for stacking + country and year FE absorbs confounders = 88–93 potential. Weaknesses: oil production itself may be endogenous to regime type (partially addressed by lagging production measure to pre-shock window)."
    },
    {
      "dataset_index": 1,
      "topic": "First Oil Production and the Long-Run Path of Political Institutions",
      "research_question": "Does the onset of oil production permanently alter a country's political trajectory, estimated using the staggered timing of first production as quasi-random variation?",
      "method": "Staggered DiD / Callaway-Sant'Anna event study around each country's first production year",
      "identification_level": "A",
      "identification": "oil_prod32_14 spanning 1932–2014 captures countries that began production at very different historical moments — some in the 1930s–50s (Mexico, Venezuela, Iran), others in the 1970s–90s (Norway, Chad, Sudan), others never. The precise timing of a commercial oil discovery is largely geological and cannot be chosen by the regime in power. Staggered adoption DiD uses countries that have not yet begun production as the clean control group for countries that just started.",
      "control_group": "Countries with zero oil production in the current year (including future producers not yet treated and permanent non-producers) serve as the never/not-yet-treated control group — the cleanest possible counterfactual in a staggered design.",
      "score_potential": "Level A binary treatment + staggered timing + 80-year panel with many pre-treatment periods per cohort + modern heterogeneity-robust estimator (Callaway-Sant'Anna or Sun-Abraham) = 90–95 potential. Key threat to validity: oil discoveries may cluster in periods of geopolitical interest (colonial extraction), which is partially addressed by including cohort × calendar-year FE or restricting to post-WWII sample."
    }
  ]
}