{
  "path": "C",
  "topic": "Oil Price Windfalls and Autocratic Regime Survival",
  "qualified_datasets": 2,
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
      "topic": "Oil Price Windfalls and Autocratic Regime Survival",
      "research_question": "Do positive oil price shocks extend autocratic regime survival, and does the effect depend on whether the country is a net oil exporter?",
      "method": "IV/2SLS with TWFE",
      "identification": "Global oil price variation (oil_price_2000) is exogenous to any single country. Interacting it with a country's pre-sample oil production capacity (oil_prod32_14 baseline) creates a Bartik-style instrument for oil revenue windfalls that is orthogonal to domestic political conditions. Net-exporter status (net_oil_exports > 0) sharpens the first stage.",
      "score_potential": "Combines the cleanest instrument in political economy (global price × pre-existing capacity) with an 82-year panel spanning decolonization, oil shocks, and the Cold War. Addresses a first-order question in the resource curse literature with a design that survives the Acemoglu-Robinson critique of endogenous production. Publishable at AER, JPE, or APSR."
    },
    {
      "dataset_index": 1,
      "topic": "Gas vs. Oil Revenue Composition and Fiscal Institutions",
      "research_question": "Does the shift from oil to natural gas as the dominant hydrocarbon revenue source produce different effects on state fiscal capacity and accountability than oil alone?",
      "method": "Staggered DiD / event study",
      "identification": "The timing of when countries transition to significant natural gas production (gas_prod55_14 begins 1955, with staggered entry across countries) is driven by geology and mid-20th-century infrastructure investment cycles, not by contemporaneous political conditions. Comparing institutional trajectories around the gas production onset date across adopting and non-adopting countries, controlling for oil revenue levels, isolates the gas-specific channel.",
      "score_potential": "Gas is systematically underexplored relative to oil in the resource curse literature despite requiring more infrastructure and longer-term contracts—creating distinct political economy. Staggered DiD with Callaway-Sant'Anna or Borusyak estimator addresses heterogeneous treatment timing. Long panel ensures sufficient pre-trends testing. Novel contribution to JDE, JEEA, or Journal of Politics."
    },
    {
      "dataset_index": 2,
      "topic": "Distance to Fertilizer Markets and Nitrogen Adoption",
      "research_question": "Does access to fertilizer markets—measured by distance to the nearest fertilizer outlet—causally raise nitrogen application rates and crop yields among smallholder farmers?",
      "method": "IV/2SLS",
      "identification": "median_dist_fert is determined by road network history and market geography, not by plot-level productivity. It predicts N_price_market (strong first stage) but is plausibly excludable from yields conditional on plot soil characteristics (clay, soil type), household FE, and crop FE. The instrument varies at the household level while outcomes vary at the plot level, enabling plot-level controls.",
      "score_potential": "Distance-based instruments for input market access have well-established validity in the agricultural economics literature. Plot-level data with detailed soil covariates (clay content, soil nutrient variables) allows unusually rich control for confounders. Policy-relevant for fertilizer subsidy targeting. Publishable at AJAE, JDE, or World Development."
    },
    {
      "dataset_index": 2,
      "topic": "Soil Clay Content and Returns to Improved Seeds",
      "research_question": "Does soil clay content—a geologically determined characteristic—moderate the productivity returns to improved seed adoption on smallholder plots?",
      "method": "Individual FE with IV/2SLS",
      "identification": "Clay content is determined by parent geology and is strictly exogenous to farmer decisions or plot investment. Within-household variation across plots in clay content (holding household characteristics, extension access, and prices constant) isolates the soil-technology complementarity. Household FE removes all household-level selection into improved seed adoption, leaving only plot-level soil variation to identify the interaction.",
      "score_potential": "Within-household plot design is the gold standard for separating technology returns from selection in smallholder agriculture. Soil heterogeneity as a moderator of returns is theoretically grounded (nutrient retention, water holding) but causally underidentified in existing work. Addresses why adoption of improved varieties remains low in some agroecological zones. Strong fit for AJAE, Economic Development and Cultural Change, or JDE."
    }
  ]
}