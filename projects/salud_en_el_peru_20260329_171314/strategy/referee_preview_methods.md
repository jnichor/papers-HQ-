```json
{
  "code_requirements": [
    {
      "category": "pitfall",
      "requirement": "Before running any QR, compute the exact fraction of households with zero OOP health expenditure. If this fraction exceeds τ (e.g., >10% zeros makes the τ=0.10 quantile degenerate — the conditional quantile is identically zero and coefficients are undefined or trivially zero). Report this fraction prominently. The two-part model is not optional if zero fraction ≥ 10%.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "Cluster bootstrap at PSU level (CONGLOME) using minimum 999 replications, not 200. At τ=0.90 and τ=0.95, the effective number of above-quantile observations per cluster is very small; 200 draws produce noisy quantiles of the bootstrap distribution. Use 999 as the floor for publishable work.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "At τ=0.90 and τ=0.95, additionally implement the Parente & Santos Silva (2016) wild score bootstrap for QR (or Hagemann 2017 score bootstrap). Cluster bootstrap validity requires enough clusters; wild bootstrap is more reliable when within-cluster sample sizes at the extreme tail are thin. Report both; flag disagreements.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "Apply ENAHO expansion weights (FACTOR07 or PONDERA) in all estimates. Standard qreg/quantreg do not automatically use survey weights — use weighted QR (rq with weights argument in R, or sqreg equivalent). Report both weighted and unweighted point estimates as a sensitivity check. Failure to weight will produce estimates unrepresentative of the Peruvian population.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "Report unweighted N (number of households, not individuals) at every model table. The analysis unit is the household — aggregate all individual-level variables to household level before estimation. Document the aggregation rule (head characteristics vs. household-level sums).",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Two-part model is a core specification, not a robustness check: (1) Probit for Pr(any OOP>0) with cluster-robust SEs; (2) QR on OOP_share conditional on positive spending. Compare coefficients from unconditional QR vs. two-part QR — meaningful divergence at low quantiles signals that unconditional QR at τ=0.10 is detecting participation margins, not spending intensity.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Implement inter-quantile range (IQR) Wald tests: test H0: β(τ_high) = β(τ_low) for each covariate across pairs (0.25 vs 0.75), (0.10 vs 0.90), (0.50 vs 0.90). Use the joint QR covariance matrix from the simultaneous quantile regression (sqreg in Stata / rq() with multiple tau in R). Do NOT simply compare separate bootstrap CIs — that approach has inflated Type I error.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Check for quantile crossing: verify that fitted conditional quantiles are monotone in τ across the covariate space. Non-crossing is not guaranteed in finite samples. If crossings occur at extreme quantiles, report their frequency and consider Chernozhukov, Fernandez-Val & Galichon (2010) rearrangement correction.",
      "priority": "SHOULD"
    },
    {
      "category": "specification",
      "requirement": "Report Koenker-Machado (1999) pseudo-R¹ (goodness of fit) at each quantile τ. This is analogous to R² and allows comparison of fit across quantiles. Do not use OLS R² for QR tables.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Clarify and consistently implement the denominator: the title says 'capacity-to-pay' (WHO/Xu et al. method = total consumption minus subsistence food expenditure), but the strategy memo uses GASHOG2D (total consumption). These are different measures. Pick one as primary, report the other as robustness, and explicitly label which definition is used in every table header.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "The 4-week recall annualization (×13) amplifies measurement error by √13 ≈ 3.6x in variance terms. Document this explicitly. As a robustness check, report results using the 4-week (non-annualized) share alongside the annualized version to verify qualitative stability.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Report CHE prevalence and QR results under all three threshold definitions: 10%, 25%, and 40% of total consumption (or capacity-to-pay). These must appear in a single summary table to allow direct comparison — not scattered across appendices.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Report weighted vs. unweighted estimates side-by-side for the main QR table. Large discrepancies signal that the unweighted sample over-represents specific strata and that the middle-income squeeze finding may be a sampling artifact.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Run urban-only and rural-only subsamples as separate QR estimations. The middle-income squeeze mechanism differs structurally between urban (EsSalud formal sector) and rural (SIS dominance) contexts. Pooling without an urban×quintile interaction may mask the heterogeneity the paper claims to find.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Alternative consumption floor sensitivity: run the main specification at the 1st, 5th, and 10th percentiles of Sumaria consumption as the denominator floor. The choice of floor mechanically affects the share distribution, particularly at the right tail where CHE is concentrated.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "RIF unconditional quantile regression (Firpo, Fortin & Lemieux 2009) must be estimated for the main specification. Report both conditional QR and RIF-QR coefficients for the key insurance and quintile variables. Conditional QR answers 'at what point in the conditional distribution does X matter?' while RIF-QR answers the population-level question implied by the research question. These can and do diverge — treat the divergence as a finding, not a problem.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Apply a multiple comparison correction (Holm-Bonferroni) to Wald test p-values when testing equality of coefficients across quantiles for all covariates simultaneously. Report both corrected and uncorrected p-values. With 6 quantiles and multiple regressors, uncorrected testing will produce spurious findings of quantile heterogeneity.",
      "priority": "SHOULD"
    },
    {
      "category": "presentation",
      "requirement": "Every QR results table must include: (1) point estimate, (2) bootstrap SE, (3) 95% CI, (4) Wald test p-value for equality with τ=0.50 or adjacent quantile, (5) pseudo-R¹, (6) unweighted N, (7) weighted N. Tables presenting only coefficients and stars are not acceptable.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "Produce a quantile process plot for each key covariate (SIS, EsSalud, quintile 2, quintile 3): coefficient on y-axis, τ on x-axis, with pointwise 95% bootstrap confidence bands. This is the primary visual evidence for or against quantile heterogeneity. Include OLS estimate as a horizontal reference line.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "Table notes must explicitly state: 'Coefficients represent changes in the conditional τ-quantile of OOP health expenditure share, not average marginal effects. Causal interpretation is not warranted given non-random insurance assignment.' This note is mandatory on every QR table.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "Report the distribution of OOP_share separately for zero-spenders and positive-spenders (histogram/density), and report the fraction of zeros by quintile and insurance group. This is prerequisite context for interpreting low-quantile QR results.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "For the two-part model, report the first-stage probit as marginal effects (AME), not log-odds. The second-stage QR table must be clearly labeled 'conditional on positive health spending' with the positive-spending N reported separately from the full-sample N.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "When presenting bootstrap SEs, report the bootstrap distribution percentile method (percentile, BC, or BCa) and the number of replications. Do not mix bootstrap-SE-based CIs (SE × 1.96) with direct percentile CIs — at extreme quantiles these diverge and the percentile method is more reliable.",
      "priority": "SHOULD"
    },
    {
      "category": "pitfall",
      "requirement": "Do not interpret QR coefficients at τ=0.10 as representing 'low-spending households.' The conditional quantile is the quantile of the spending distribution given covariates — a household at the 10th conditional quantile may have very different observable characteristics than a household at the 10th unconditional quantile. Conflating these is the most common misinterpretation in applied QR papers.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "Do not claim that negative QR coefficients for SIS at low quantiles mean SIS 'reduces' CHE. At τ=0.10 in a distribution with large zero mass, the negative coefficient may simply reflect that SIS beneficiaries are more likely to have zero spending (care avoidance or access barriers), not that SIS protects against high spending. The two-part model disentangles these.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "Quintile fixed effects and insurance categories are jointly endogenous — SIS is means-tested (targeting the poor) and EsSalud covers formal workers (higher income). Including both quintile dummies AND insurance dummies without interaction will partially absorb each other. The insurance × quintile interaction must be the primary specification, not an alternative.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "The ×13 annualization of the 4-week recall creates a share outcome that can mechanically exceed 1.0 for high-spending households (e.g., a catastrophic acute episode in one month). Verify the cap at 1.0 is applied AFTER annualization, and report what fraction of households are capped. Capping at 1.0 introduces censoring that QR does not automatically handle — consider Tobit-QR or report sensitivity excluding capped observations.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "Do not use ENAHO individual-level records without collapsing to household level first. Health module (Module 400) is individual-level; Sumaria consumption is household-level. Merging without aggregation produces a dataset where the same household consumption appears multiple times, inflating effective N and producing incorrect SEs.",
      "priority": "MUST"
    }
  ],
  "method_warnings": [
    "Zero mass dominance: ENAHO typically shows 40-60% of households reporting zero OOP health spending in any 4-week period. At τ=0.10 and potentially τ=0.25, the conditional quantile may be identically zero across all covariate values, rendering QR coefficients unidentified or trivially zero. Verify before interpreting.",
    "Survey design ignored by default QR estimators: rq() in R and qreg in Stata do not account for stratification (ESTRATO) or PSU clustering in point estimates — only in SEs if clustering is specified. This means even point estimates from unweighted QR may be inconsistent for population parameters.",
    "Bootstrap at extreme quantiles with small clusters: if CONGLOME clusters have fewer than ~15 observations each, cluster bootstrap standard errors are unreliable at τ=0.90–0.95 even with 999 replications. Check cluster size distribution and consider pairs bootstrap as an alternative.",
    "RIF density estimation sensitivity: RIF-QR requires a kernel density estimate of the unconditional quantile. The choice of bandwidth meaningfully affects RIF coefficients, especially in the right tail where the OOP share distribution is sparse. Report bandwidth selection method and sensitivity to ±50% bandwidth perturbation.",
    "Inter-quantile Wald tests require simultaneous estimation: if each quantile is estimated separately (even with the same bootstrap), the cross-quantile covariance is not captured. Must use simultaneous QR (e.g., R rq() with vector tau, or Stata sqreg) to obtain the joint covariance matrix needed for valid Wald tests.",
    "Consumption quintiles computed from the same GASHOG2D used as denominator: the quintile assignment and the outcome share are derived from the same variable, creating a mechanical negative correlation between being in higher quintiles and having a high share (denominator is larger). This is not a bias per se but must be explicitly acknowledged as a feature of the design, not an artifact."
  ],
  "must_not_claim": [
    "That insurance type (SIS, EsSalud, uninsured) causally reduces or increases catastrophic health expenditure — assignment is non-random and selection is severe (SIS targets the poor; EsSalud covers formal workers).",
    "That QR coefficients represent the effect of a covariate on a specific household's spending — they represent the covariate's association with the conditional quantile function, a population-level object.",
    "That the 'middle-income squeeze' is a causal mechanism — the paper documents a conditional distributional pattern, not a causal pathway. The phrase 'disproportionate exposure' must be operationalized as a conditional association, not a structural claim.",
    "That results from ENAHO 2024 alone generalize to trends over time — cross-sectional data support distributional snapshots, not dynamic or trend claims.",
    "That households at the 10th conditional quantile 'avoid care due to poverty' — care avoidance is a behavioral interpretation not identified by QR coefficients on spending conditional on having any spending.",
    "That the two-part model corrects for selection bias — the two-part model handles the zero mass mechanically but does not identify the causal effect of covariates on the participation or spending decision.",
    "That wild bootstrap standard errors are asymptotically valid under arbitrary within-cluster correlation at τ=0.95 — at extreme quantiles with very few observations above the quantile per cluster, bootstrap inference is approximate and should be labeled as such."
  ]
}
```

**Reviewer summary of the three highest-priority items:**

1. **Zero mass check first** — if ≥10% of households have zero OOP, τ=0.10 QR is fitting the zero boundary and every coefficient is uninterpretable. This single check could invalidate half the paper's results table.

2. **Simultaneous QR for Wald tests** — separate bootstrapped CIs cannot be compared to test quantile heterogeneity. The paper's central empirical claim (coefficients vary across quantiles) requires a joint test using the cross-quantile covariance from simultaneous estimation.

3. **Conditional vs. unconditional framing** — the RIF regression is not a robustness extension; it is the estimator that actually answers the stated research question about population-level distributional differences. Conditional QR answers a different (though related) question. Both must appear and their divergence must be discussed.