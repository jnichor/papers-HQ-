{
  "path": "C",
  "topic": "Commodity Price Shocks and the Sequencing of Civil Liberty Erosion",
  "qualified_datasets": 2,
  "selected_dataset": "Civil Liberty Dataset",
  "feasibility": {
    "max_tier": 1,
    "tier_label": "CAUSAL (all methods available)",
    "score_ceiling": 100,
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
    "warnings": [],
    "best_structure": "panel",
    "best_rows": 9292,
    "best_cols": 11,
    "n_periods": 51
  },
  "suggestions": [
    {
      "dataset_index": 1,
      "topic": "Two-Turnover Consolidation Threshold and Breakdown Risk",
      "research_question": "Does crossing Huntington's two-turnover consolidation threshold causally reduce the probability of subsequent democratic breakdown?",
      "method": "RDD",
      "identification": "The discrete threshold of achieving exactly two consecutive democratic power turnovers (two_turnover_period) creates a discontinuity: countries just above vs. just below the threshold are comparable on pre-existing trends, but those above face structurally different institutional expectations. The running variable is turnover count, and breakdown_type is the outcome.",
      "score_potential": "Directly tests a foundational claim in democratization theory (Huntington 1991) with a credible causal design rather than correlation. The RDD is clean because the threshold is definitional, not policy-chosen. The LIED data has global coverage and multiple waves of transitions, giving sufficient bandwidth observations. Publishable in APSR, JOP, or BJPS — reviewers will recognize the theoretical stakes and the identification is difficult to dispute."
    },
    {
      "dataset_index": 1,
      "topic": "Sovereignty Shocks and Democratic Trajectory (Post-Soviet vs. Decolonization Waves)",
      "research_question": "Do newly sovereign states inherit systematically different democratic trajectories depending on the wave of independence (decolonization 1960s vs. post-Soviet 1991), and what explains the divergence?",
      "method": "synthetic control",
      "identification": "The sovereign variable marks sovereignty onset, which is exogenous to the nascent state's own institutions (driven by colonial metropole collapse or Soviet dissolution — external shocks). Staggered synthetic controls build a counterfactual for each newly sovereign country using donor pool of already-sovereign states matched on pre-sovereignty lexical_index and region. The two waves provide a quasi-experimental contrast of institution-transfer regimes.",
      "score_potential": "Exploits a natural experiment that spans ~80 countries across two historically distinct exogenous shocks. Synthetic control is the gold standard for comparative case inference. The wave comparison (decolonization vs. post-Soviet) adds a second layer of identification that rules out generic 'new state' explanations. Directly speaks to debates on institutional transplantation and path dependence — publishable in AJPS, World Politics, or Comparative Political Studies."
    },
    {
      "dataset_index": 2,
      "topic": "Commodity Price Shocks and the Sequencing of Civil Liberty Erosion",
      "research_question": "When commodity-dependent states experience exogenous terms-of-trade collapses, which civil liberty dimension (freexp, freass, fremov, fairtrial) erodes first, and does the sequence predict eventual recovery?",
      "method": "event study",
      "identification": "Global commodity price indices (oil, metals, agricultural) interacted with each country's export composition at baseline provide plausibly exogenous variation in fiscal stress for commodity-dependent states — identification borrowed from Bazzi & Blattman (2014). The event is a large negative terms-of-trade shock (>1.5 SD). The panel (204 countries × 51 years) supports staggered event study with country and year FE, using the five civil liberty outcomes as a vector of dependent variables.",
      "score_potential": "Uses a well-validated IV strategy (commodity prices as instruments for fiscal/political stress) applied to a novel outcome — the within-erosion ordering of specific rights. The five distinct civil liberty dimensions allow falsification tests (e.g., frerel should respond less than freexp during political crackdowns). Clean panel structure supports Callaway-Sant'Anna or Sun-Abraham heterogeneity-robust estimators. Speaks to mechanisms of democratic backsliding — high relevance to JCR, IO, or the Journal of Human Rights."
    },
    {
      "dataset_index": 2,
      "topic": "Regional Civil Liberty Contagion via Authoritarian Diffusion",
      "research_question": "Does a major regional neighbor's deterioration in freedom of expression causally reduce freedom of assembly and fair trial rights in neighboring states, consistent with authoritarian diffusion?",
      "method": "IV/2SLS",
      "identification": "Instrument for neighbor freexp shocks using the neighbor's distance-weighted exposure to global autocratization pressure (e.g., share of the neighbor's own neighbors that are autocratizing) — a standard spatial-IV exclusion restriction. This isolates the contagion channel from common regional shocks. The panel allows country FE to absorb time-invariant confounders, and year FE to absorb global trends. freass and fairtrial are the endogenous outcomes of interest.",
      "score_potential": "Addresses an open debate — whether authoritarian diffusion operates through information, legitimation, or security cooperation — by examining which rights cluster together under regional contagion. The IV exclusion restriction is defensible and testable (placebo: freedom of religion should not respond to political expression shocks in autocratic neighbors). Panel depth (51 years, 204 countries) gives strong first-stage power. Publishable in IO, World Politics, or AJPS given the diffusion literature's prominence."
    }
  ]
}