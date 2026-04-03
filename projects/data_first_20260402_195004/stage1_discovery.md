{
  "path": "C",
  "topic": "Civilian Casualty Framing and ICC Referral Support",
  "qualified_datasets": 3,
  "selected_dataset": "Elite Study Survey Data (Crime and Policing)",
  "feasibility": {
    "max_tier": 3,
    "tier_label": "CROSS-SECTIONAL CAUSAL (IV, RDD only)",
    "score_ceiling": 70,
    "allowed_methods": [
      "IV/2SLS",
      "RDD",
      "matching (PSM/CEM)",
      "Oaxaca-Blinder",
      "Heckman selection",
      "quantile regression"
    ],
    "forbidden_methods": [
      "DiD",
      "event study",
      "TWFE",
      "individual FE",
      "synthetic control",
      "Arellano-Bond"
    ],
    "warnings": [
      "Cross-sectional data — DiD, event study, FE not feasible.",
      "High missingness: make_illegal (67%), make_illegal_binary (67%)",
      "Majority ordinal variables (104 ordinal vs 22 continuous). Power for FE/DiD may be limited.",
      "Only 2 clusters — below 30 threshold. Cluster-robust SEs unreliable. Wild bootstrap required but may lack power."
    ],
    "best_structure": "cross-sectional",
    "best_rows": 1185,
    "best_cols": 126,
    "n_periods": 0,
    "n_ordinal_vars": 104,
    "n_continuous_vars": 22,
    "self_contained": true
  },
  "suggestions": [
    {
      "dataset_index": 1,
      "topic": "Civilian Casualty Framing and ICC Referral Support",
      "research_question": "Does framing a conflict (Afghanistan) in terms of civilian casualties increase elite support for ICC referrals, and does this effect vary by pre-existing hawkishness?",
      "method": "OLS / heterogeneous treatment effects (OLS + interaction terms); quantile regression on ICC_referral_within_bin",
      "identification_level": "A",
      "identification": "Afghanistan_treatment is a randomized binary vignette assignment (mean=0.52, near-perfect balance). Random assignment breaks any selection between respondent attitudes and treatment exposure. Within-bin outcomes confirm the design accounts for covariate balance.",
      "control_group": "Respondents assigned to the control vignette condition (Afghanistan_treatment=0) are the direct counterfactual — same population, different information frame, assignment outside their control.",
      "score_potential": "Level A identification (RCT in survey) + large N (1,185) + rich moderators (hawkish_aggregate, hostile_sexism_agg, partisan identifiers) + within-bin outcomes already constructed = 90–95 potential. Heterogeneous effects angle elevates contribution beyond a simple ATE paper."
    },
    {
      "dataset_index": 1,
      "topic": "Gender Attitudes as a Moderator of Hawkish Framing Effects on Airstrike Support",
      "research_question": "Do respondents high in hostile sexism respond differently to conflict framing (Afghanistan_treatment) when evaluating airstrike authorization, compared to low-sexism respondents?",
      "method": "OLS with interaction term (Afghanistan_treatment × hostile_sexism_agg); Oaxaca-Blinder decomposition across gender groups",
      "identification_level": "A",
      "identification": "Same randomized vignette assignment creates exogenous variation in framing. The moderator (hostile_sexism_agg) is a pre-treatment respondent characteristic — interacting it with the randomized treatment identifies a CATE without endogeneity concerns, since treatment assignment is independent of attitudes.",
      "control_group": "Within each tercile of hostile_sexism_agg, the control vignette group provides the baseline — variation in airstrike support across treatment arms within attitude subgroups is causal.",
      "score_potential": "Level A + novel moderator (gender attitudes in hawkishness literature is underexplored) + outcome directly relevant to security policy = 88–93 potential. Contribution is the CATE, not just the ATE."
    },
    {
      "dataset_index": 2,
      "topic": "Political Congruence as an Instrument for News Avoidance Effects on Political Efficacy",
      "research_question": "Does selective news avoidance reduce internal political efficacy, using political congruence (ideological alignment between voter and dominant news environment) as an instrument?",
      "method": "IV/2SLS: first stage regresses avoidance on congruence/congruence_EU; second stage estimates effect of instrumented avoidance on internal_efficacy and knowledge",
      "identification_level": "B",
      "identification": "Political congruence (congruence_EU) varies exogenously because it depends on the electoral outcome — the respondent did not choose which party won or which news outlets dominate. Misaligned respondents face a news environment that does not reflect their preferences, pushing avoidance upward for reasons outside their control. This satisfies exclusion: congruence affects efficacy only through news consumption patterns.",
      "control_group": "Respondents in high-congruence environments (news aligns with preferences) serve as the 'untreated' comparison — they face no exogenous push toward avoidance. The dose variation in congruence generates a continuous instrument.",
      "score_potential": "Level B IV + two-wave data (W1 baseline controls, W2 outcomes) + policy-relevant outcome (democratic efficacy) = 82–88 potential. Strength depends on first-stage F-stat; exclusion restriction is defensible but must be argued carefully."
    },
    {
      "dataset_index": 2,
      "topic": "Attrition-Corrected Estimates of News Diet Importance on Avoidance Behavior",
      "research_question": "Does perceiving news as important (W1_news_important) causally reduce avoidance by Wave 2, after correcting for the 31% selective attrition in W2 outcomes?",
      "method": "Heckman two-stage selection model: selection equation predicts W2 response using W1 sociodemographic predictors (age, education, interest) as exclusion restrictions; outcome equation estimates W1_news_important → W2 avoidance",
      "identification_level": "B",
      "identification": "W2 missingness (31%) is not random — older, lower-interest respondents selectively drop out, creating sample selection bias in naive cross-wave comparisons. Heckman uses W1 characteristics (age, interest, external_efficacy) that predict attrition but not news avoidance conditional on participation as exclusion restrictions.",
      "control_group": "Respondents who complete Wave 2 but have low W1 news importance scores serve as the comparison group for high-importance respondents, after correcting for differential attrition via the inverse Mills ratio.",
      "score_potential": "Level B + attrition correction is the methodological contribution + two-wave structure is ideal for Heckman = 80–85 potential. Value is the methodological correction to a pervasive problem in panel survey research."
    },
    {
      "dataset_index": 3,
      "topic": "Fertilizer Market Price Shocks and Smallholder Adoption: IV Evidence from Ethiopia",
      "research_question": "Do exogenous increases in nitrogen fertilizer market prices (N_price_market) reduce adoption of inorganic fertilizer, and by how much does this reduce plot-level yields?",
      "method": "IV/2SLS with household FE: instrument N_rate (nitrogen application) with N_price_market and median_dist_fert; panel allows controlling for time-invariant household unobservables",
      "identification_level": "A",
      "identification": "N_price_market varies across markets and time due to international commodity prices, import logistics, and supply chain shocks — all beyond the smallholder's control. median_dist_fert is a predetermined geographic characteristic (physical distance to input markets). Both shift the effective cost of fertilizer exogenously. The panel structure allows household FE to absorb selection on fixed characteristics.",
      "control_group": "Households in low-price or closer-to-market areas serve as the comparison group — they face the same agricultural conditions but exogenously lower fertilizer costs. Within-household price variation over time provides the cleanest identification.",
      "score_potential": "Level A (geographic + price IV) + panel FE + Ethiopia agricultural context (policy-relevant) + N_price_market directly observed (not constructed) = 90–95 potential. Two instruments allow overidentification test, strengthening credibility."
    },
    {
      "dataset_index": 3,
      "topic": "Agricultural Extension Services and Fertilizer Use Efficiency: Staggered DiD",
      "research_question": "Does receipt of agricultural extension services increase nitrogen use efficiency (crop output per unit of N_rate applied), exploiting the staggered geographic rollout of extension programs across woredas?",
      "method": "Staggered DiD / event study with TWFE and household FE; Callaway-Sant'Anna or Sun-Abraham estimator to handle treatment effect heterogeneity across cohorts",
      "identification_level": "A",
      "identification": "extension_received varies across villages and woredas based on program rollout timing determined by government agricultural bureaus — not by farmer demand or plot productivity. The geographic hierarchy (region → zone → woreda → kebele → village) allows clustering and testing whether rollout was correlated with pre-trends in fertilizer use or yields.",
      "control_group": "Households in woredas not yet reached by extension services at time t serve as the not-yet-treated control group for households newly receiving extension in that period — the staggered design avoids reliance on a never-treated group and enables event-study pre-trend tests.",
      "score_potential": "Level A (staggered policy rollout) + panel FE + modern staggered DiD estimators + rich soil/input controls (clay, P_rate, hired_labour) = 90–95 potential. Pre-trend falsification tests and heterogeneity by plot ownership (plot_owned) or soil type add robustness sections."
    }
  ]
}