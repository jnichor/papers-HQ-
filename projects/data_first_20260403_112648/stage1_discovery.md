{
  "path": "C",
  "topic": "Voucher vs. Training: Differential Employment Effects",
  "qualified_datasets": 3,
  "selected_dataset": "Wage Subsidies RCT Jordan (REStat)",
  "feasibility": {
    "max_tier": 2,
    "tier_label": "GROUP-LEVEL CAUSAL (no individual tracking)",
    "score_ceiling": 70,
    "allowed_methods": [
      "group-level DiD",
      "repeated cross-section DiD",
      "IV/2SLS",
      "RDD",
      "synthetic control",
      "cohort analysis",
      "Oaxaca-Blinder",
      "quantile regression"
    ],
    "forbidden_methods": [
      "individual FE",
      "individual event study",
      "Arellano-Bond",
      "Markov transitions"
    ],
    "warnings": [
      "Structure is pooled-cross-sections — individual FE not feasible.",
      "4 time periods — limited event study dynamics.",
      "High missingness: treatstat (42%), voucher (42%), training (42%), both (42%), b_d2sector (93%)",
      "Majority ordinal variables (750 ordinal vs 453 continuous). Power for FE/DiD may be limited.",
      "Only 16 clusters — below 30 threshold. Cluster-robust SEs unreliable. Wild bootstrap required but may lack power."
    ],
    "best_structure": "pooled-cross-sections",
    "best_rows": 2322,
    "best_cols": 1420,
    "n_periods": 4,
    "n_ordinal_vars": 750,
    "n_continuous_vars": 453,
    "self_contained": true
  },
  "suggestions": [
    {
      "dataset_index": 1,
      "topic": "Voucher vs. Training: Differential Employment Effects",
      "research_question": "Do wage vouchers produce larger short-run employment gains than employer-sponsored training among young Jordanian women, and does the combined arm (both) yield complementary or redundant returns?",
      "method": "ITT comparison across RCT arms (OLS with randomization-based SEs); LATE via IV using arm assignment as instrument for actual take-up",
      "identification_level": "A",
      "identification": "Random assignment to three treatment arms (voucher, training, both) vs. pure control via `treatstat`, `voucher`, `training`, `both` — lottery-based allocation is the source of exogenous variation. This is a published REStat RCT, so randomization is verified.",
      "control_group": "Pure-control participants (treatstat=0) serve as the counterfactual; pairwise arm comparisons exploit cross-arm randomization",
      "score_potential": "Level A identification (RCT) + 1,420-variable baseline balance checks + multiple treatment arms for dose-response = 90+ potential"
    },
    {
      "dataset_index": 1,
      "topic": "Tawjihi Score Threshold and Training Returns",
      "research_question": "Is the return to the wage-subsidy program heterogeneous around the Tawjihi pass/fail cutoff — do barely-passing graduates benefit more than barely-failing ones, conditional on treatment arm?",
      "method": "RDD on `b_c2avtawjihi` (continuous Tawjihi average) at the `b_passfail` cutoff; interacted with treatment arm indicators for CATE",
      "identification_level": "A",
      "identification": "The Jordanian Tawjihi exam imposes a sharp administrative pass/fail threshold that determines post-secondary eligibility for reasons entirely outside individual control at the margin. `b_tawjihirecord` and `b_passfail` identify the running variable and cutoff.",
      "control_group": "Individuals just below the Tawjihi pass threshold serve as the counterfactual for individuals just above it — bandwidth around cutoff enforces local comparability",
      "score_potential": "RDD on a hard institutional threshold within an RCT = double identification; bandwidth sensitivity and McCrary density test straightforward = 88–92 potential"
    },
    {
      "dataset_index": 2,
      "topic": "Political Congruence and Selective News Avoidance",
      "research_question": "Does partisan congruence between a citizen and their representative causally reduce motivated news avoidance, or does it merely reflect prior political engagement?",
      "method": "IV/2SLS: instrument `congruence` with close-election margins in the respondent's district (forces congruence to be as-good-as-random near 50% vote shares); outcome is `avoidance` / `W2_news_switchaway`",
      "identification_level": "A",
      "identification": "`congruence` and `congruence_EU` measure ideological alignment between the respondent and elected representative — alignment near district-level electoral thresholds is quasi-random. Marginal voters in nearly-tied races experience exogenous congruence shifts. The `region` variable enables district-level merge with electoral records.",
      "control_group": "Residents of districts where the 'wrong' party barely won serve as controls for otherwise identical residents of districts where the 'right' party barely won",
      "score_potential": "IV with well-motivated instrument + W1 baseline controls to absorb prior avoidance + attrition correction via `W2_WeightSocDemTurnAttrition` = 82–87 potential"
    },
    {
      "dataset_index": 2,
      "topic": "Wave-1 News Habits as Instrument for Wave-2 Social-Media Reliance",
      "research_question": "Does habitual social-media news consumption (`W2_news_socmed`) causally erode political knowledge and internal efficacy, or do low-efficacy individuals self-select into passive feeds?",
      "method": "IV/2SLS: use `W1_news_socmed` (pre-determined baseline habit) as instrument for endogenous `W2_news_socmed`; outcomes are `knowledge`, `internal_efficacy`, `external_efficacy`",
      "identification_level": "B",
      "identification": "Wave-1 social-media news habit predates the outcome measurement period and is correlated with Wave-2 behavior, but affects Wave-2 outcomes only through the channel of continued use — satisfying exclusion under the assumption that W1 habits don't directly shift W2 knowledge except via consumption. `sample` flag controls for panel composition.",
      "control_group": "Low-W1-socmed users serve as the dose-variation control group for high-W1-socmed users",
      "score_potential": "Lagged instrument IV + two-wave structure + rich W1 covariates for over-identification test = 80–84 potential"
    },
    {
      "dataset_index": 3,
      "topic": "Afghanistan Conflict Framing and Elite Support for ICC Referrals",
      "research_question": "Does randomly assigning elite respondents to an 'Afghanistan accountability' frame causally increase support for ICC referrals, and does this effect vary by hawkishness and cosmopolitanism?",
      "method": "ITT (OLS) of `Afghanistan_treatment` on `ICC_referral`; CATE estimation interacting treatment with `hawkish_aggregate`, `cosmopolitan`, and `pro_israel_score`",
      "identification_level": "A",
      "identification": "`Afghanistan_treatment` is a binary randomized vignette assignment (mean=0.52, near-equal split confirming randomization). Framing is assigned before outcome elicitation — this is a clean survey experiment with no selection into treatment.",
      "control_group": "Respondents assigned to the control vignette (Afghanistan_treatment=0) are the direct counterfactual; randomization guarantees balance on `rank_*`, `hhi`, `education`, ideology",
      "score_potential": "Level A identification (randomized survey experiment) + elite sample with `_within_bin` RDD variables available as robustness = 88–93 potential"
    },
    {
      "dataset_index": 3,
      "topic": "RDD on Implicit Score Bins: Hawkishness Threshold and UNSC Condemnation",
      "research_question": "Is there a discontinuous jump in support for UNSC condemnation at the threshold that separates 'hawk' from 'non-hawk' elites, identifying an attitude-to-policy gap that ideological self-report cannot reveal?",
      "method": "RDD using `hawkish_aggregate` as the running variable at a theoretically motivated cutoff; outcome is `UNSC_condemn`; validate with `UNSC_condemn_within_bin` as the pre-binned check variable already embedded in the data",
      "identification_level": "A",
      "identification": "The presence of `airstrikes_within_bin`, `ICC_referral_within_bin`, `UNSC_condemn_within_bin` variables signals the original study already constructed RDD bins — the running variable and cutoff are structurally embedded. Respondents near the hawkishness threshold are locally as-good-as-randomly assigned to hawk vs. non-hawk status.",
      "control_group": "Respondents just below the hawkishness threshold serve as controls for those just above it; the `_within_bin` variable enables the standard Calonico-Cattaneo-Titiunik bandwidth procedure",
      "score_potential": "RDD with pre-validated bins already in data + elite policy outcomes + heterogeneity by `pro_israel_score` and `cosmopolitan` = 85–90 potential"
    }
  ]
}