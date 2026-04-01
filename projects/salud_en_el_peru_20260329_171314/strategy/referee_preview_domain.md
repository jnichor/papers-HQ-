```json
{
  "code_requirements": [
    {
      "category": "data_construction",
      "requirement": "Merge Module 400 (health) with Sumaria at household level using the triple key CONGLOME+VIVIENDA+HOGAR. Verify merge is 1:1 at household level; flag unmatched records and report counts.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Annualize 4-week recall health spending (P41601+P41602+P41603) by multiplying by 13 (52 weeks / 4 weeks). Document this assumption explicitly; add robustness with ×12 (calendar-month interpretation) as a sensitivity check.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Aggregate individual-level health spending to household level (sum within CONGLOME+VIVIENDA+HOGAR) before constructing the OOP share. Do NOT use individual-level OOP shares averaged to HH level — this gives wrong denominator.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Construct consumption floor as the 5th percentile of GASHOG2D (Sumaria) among households with positive consumption. Apply floor BEFORE dividing; never divide by raw GASHOG2D directly. Report count of households affected by the floor.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Cap OOP share at 1.0 after floor-adjusted division. Report the number and share of observations capped. Test sensitivity with no cap as robustness.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Construct mutually exclusive insurance categories: (1) SIS only (P4191=1, P4192≠1), (2) EsSalud (P4192=1, possibly with SIS), (3) EPS/private (P4195=1, no SIS or EsSalud), (4) Uninsured (none). Handle overlaps explicitly; document precedence rule (EsSalud > SIS for overlap).",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Flag zero-OOP households explicitly before any estimation. Report: (a) share with zero OOP by insurance type, (b) share with zero OOP by consumption quintile. These numbers motivate the two-part model.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Construct consumption quintiles from GASHOG2D using survey-weighted quintile breaks (FACTOR07). Do NOT use unweighted quantile cuts — ENAHO oversamples rural areas and this will distort quintile composition.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Identify the household head from Module 200 (PARENTESCO=1). Attach head-level characteristics (age, sex, education) to the household record. Verify uniqueness — each household should have exactly one head; log households with zero or multiple heads.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Construct chronic illness indicator from Module 400 (any household member reporting chronic condition, e.g., P4031). Aggregate to HH level as 'any chronic member' dummy.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "OLS benchmark: regress OOP_share on insurance dummies, quintile dummies, insurance×quintile interactions, and controls (age_head, female_head, education, HH_size, children_under5, elderly_65plus, rural, chronic, region FE). Use survey-weighted OLS with cluster-robust SEs at PSU level (CONGLOME). This is the baseline for QR comparison.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Quantile regression at τ = {0.10, 0.25, 0.50, 0.75, 0.90, 0.95} using statsmodels QuantReg. Use survey weights as frequency weights (FACTOR07, rescaled to mean=1 to preserve sample size in inference). Same regressors as OLS benchmark.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Standard errors: cluster bootstrap at PSU level (CONGLOME) with B=500 replications for τ = {0.10, 0.25, 0.50, 0.75}. For τ = {0.90, 0.95}, use wild cluster bootstrap (boottest or manual implementation) because cluster count may be low in the upper tail subsample. Report both and note any divergence.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Wald test for coefficient equality across quantile pairs: test H0: β(τ_j) = β(τ_k) for each coefficient, using joint QR estimation across quantile pairs and bootstrapped covariance. At minimum test: (0.25 vs 0.75) and (0.50 vs 0.90) for insurance and quintile coefficients.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Two-part model: (Part 1) survey-weighted probit for Pr(OOP>0) on same regressors; (Part 2) QR at τ = {0.25, 0.50, 0.75, 0.90} on the positive-OOP subsample only. Report both parts in separate tables. This addresses the zero mass point directly.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "RIF unconditional quantile regression (Firpo, Fortin & Lemieux 2009) at τ = {0.25, 0.50, 0.75, 0.90}: compute the RIF of OOP_share at each quantile (using kernel density estimate of the marginal distribution), then regress RIF on covariates via WLS with survey weights. Report unconditional marginal effects for insurance and quintile variables.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "For RIF-QR, use Gaussian kernel with bandwidth selected by Silverman's rule-of-thumb on the full (weighted) OOP_share distribution. Report sensitivity to bandwidth (×0.5 and ×2) in a footnote or appendix table.",
      "priority": "SHOULD"
    },
    {
      "category": "estimation",
      "requirement": "Fractional logit / fractional probit (Papke & Wooldridge 1996) as an additional robustness model for the bounded [0,1] outcome. Report APEs for insurance and quintile variables alongside OLS and median QR. This directly addresses referee concern about the bounded nature of the outcome.",
      "priority": "SHOULD"
    },
    {
      "category": "estimation",
      "requirement": "CHE binary outcome regressions: run survey-weighted probit and linear probability model for CHE_10, CHE_25, CHE_40 binary indicators. Report marginal effects at means. These complement the continuous QR analysis and link to the CHE literature frame.",
      "priority": "SHOULD"
    },
    {
      "category": "estimation",
      "requirement": "Test for quantile crossing: after fitting the QR models, verify that predicted quantile functions are monotone for representative covariate profiles (e.g., median covariates by insurance group). If crossing occurs, report it and note it as a limitation.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "CHE threshold robustness: re-compute all CHE binary indicators at thresholds 10%, 25%, and 40% of total consumption. Report CHE rates by quintile and insurance group under all three definitions in a single comparison table.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Consumption floor sensitivity: re-run main QR at three floor choices — 1st percentile, 5th percentile (baseline), 10th percentile of GASHOG2D. Report change in key coefficients for insurance and quintile 2/3 (the 'middle-income squeeze' test).",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Urban/rural subsample analysis: re-run main QR specification separately for urban (AREA=1) and rural (AREA=2) subsamples. Report coefficient plots side-by-side. Rural households have very different care-seeking patterns and SIS coverage.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Trim extreme OOP shares: re-run excluding households with OOP_share > 0.99 (post-cap) AND with OOP_share in [0, 0.001) (near-zero but positive). Compare coefficients at τ=0.75 and τ=0.90.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Weighted vs. unweighted QR: report main table coefficients both with and without FACTOR07 survey weights. If weights change substantive conclusions, discuss why (likely rural oversampling).",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Stepwise control addition: run QR at τ=0.50 and τ=0.90 adding controls in blocks — (1) insurance only, (2) +quintile, (3) +demographics, (4) +chronic+rural, (5) +region FE. Track stability of insurance and quintile coefficients. This demonstrates that middle-income squeeze is not explained away by demographic confounders.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Annualization sensitivity: re-run with ×12 multiplier (monthly interpretation) instead of ×13. Report side-by-side with baseline. Difference is ~8%; if it changes key comparisons, flag as data limitation.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Alternative outcome definition: replace GASHOG2D as denominator with 'capacity-to-pay' = GASHOG2D minus food subsistence expenditure (bottom-quintile food spending per capita × HH size). Run QR with this denominator as additional outcome. Cite Xu et al. (2003) WHO methodology.",
      "priority": "SHOULD"
    },
    {
      "category": "inference",
      "requirement": "Report effective cluster count at each quantile subsample — particularly for τ=0.90 and τ=0.95 where the regression is effectively run on the top decile/5% of observations. If fewer than 30 PSUs contribute, flag SE reliability and switch to wild bootstrap exclusively.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "Apply multiple testing correction (Benjamini-Hochberg FDR at q=0.10) to the set of insurance and quintile p-values across all quantiles and outcomes. Report both corrected and uncorrected p-values in supplementary table. Do NOT correct Wald tests for quantile equality — those are pre-specified.",
      "priority": "SHOULD"
    },
    {
      "category": "survey_design",
      "requirement": "Use ENAHO survey weights (FACTOR07 from Sumaria) throughout ALL descriptive statistics and regression models. Verify FACTOR07 sums to approximate Peru population in survey year. Never report unweighted means as primary estimates.",
      "priority": "MUST"
    },
    {
      "category": "survey_design",
      "requirement": "Document the survey design variables used: PSU = CONGLOME, stratum = ESTRATO (or NOM_UBIGEO + AREA interaction if ESTRATO is unavailable). For variance estimation, cluster at PSU; do NOT attempt Taylor linearization unless using a dedicated survey package — cluster bootstrap is sufficient.",
      "priority": "MUST"
    },
    {
      "category": "tables_and_figures",
      "requirement": "Table 1: Weighted summary statistics — means/proportions for all analysis variables, separately by insurance group (SIS / EsSalud / EPS / Uninsured), with p-values from F-test of equality. Include N (unweighted) and weighted population share per group.",
      "priority": "MUST"
    },
    {
      "category": "tables_and_figures",
      "requirement": "Table 2: Distributional profile by consumption quintile — OOP_share mean, median, 75th and 90th percentile; CHE rates at 10%/25%/40%; share with zero OOP; insurance coverage rates. All weighted.",
      "priority": "MUST"
    },
    {
      "category": "tables_and_figures",
      "requirement": "Table 3: Main QR results — coefficient table with columns for OLS, τ=0.10, 0.25, 0.50, 0.75, 0.90, 0.95. Rows: insurance dummies, quintile dummies, interaction terms, controls. Bootstrap SEs in parentheses. Stars at 1%/5%/10%. Bottom rows: Wald test p-values for equality of insurance coefficients (Q1 vs Q5).",
      "priority": "MUST"
    },
    {
      "category": "tables_and_figures",
      "requirement": "Table 4: Two-part model — Panel A: probit marginal effects for Pr(OOP>0); Panel B: QR coefficients on positive-OOP subsample at τ=0.25, 0.50, 0.75, 0.90. Same regressors as Table 3.",
      "priority": "MUST"
    },
    {
      "category": "tables_and_figures",
      "requirement": "Table 5: RIF-QR results at τ=0.25, 0.50, 0.75, 0.90 — unconditional marginal effects for insurance and quintile variables. Compare with conditional QR (Table 3) in a side-by-side column layout.",
      "priority": "MUST"
    },
    {
      "category": "tables_and_figures",
      "requirement": "Table 6: Robustness summary — for key insurance and quintile 3 coefficients at τ=0.50 and τ=0.90, report point estimates across: (a) baseline, (b) floor=1st pct, (c) floor=10th pct, (d) ×12 annualization, (e) no cap, (f) urban only, (g) rural only, (h) unweighted.",
      "priority": "MUST"
    },
    {
      "category": "tables_and_figures",
      "requirement": "Figure 1: Kernel density plot of OOP_share (weighted) for each insurance group on the same axes. Use log scale or truncate at 0.5 for readability. Annotate zero-mass share per group.",
      "priority": "MUST"
    },
    {
      "category": "tables_and_figures",
      "requirement": "Figure 2: QR coefficient plots — for each key variable (SIS dummy, EsSalud dummy, quintile 3 dummy), plot the point estimate + 95% CI band across τ = {0.10, 0.25, 0.50, 0.75, 0.90, 0.95} with the OLS estimate as a horizontal reference line. This is the primary visual for the 'squeeze' narrative.",
      "priority": "MUST"
    },
    {
      "category": "tables_and_figures",
      "requirement": "Figure 3: CHE rate heatmap — rows = consumption quintile (Q1–Q5), columns = insurance group, cells = CHE rate at 25% threshold. Repeat for 10% and 40% thresholds in appendix. This is the clearest visual for the middle-income squeeze hypothesis.",
      "priority": "MUST"
    },
    {
      "category": "tables_and_figures",
      "requirement": "Figure 4: Insurance × quintile interaction plot — for τ=0.50 and τ=0.90, plot predicted OOP_share (at covariate means) against quintile, separately for each insurance group. Show that SIS breaks the gradient at low quintiles and EsSalud breaks it at high quintiles, leaving middle uninsured at highest risk.",
      "priority": "MUST"
    },
    {
      "category": "tables_and_figures",
      "requirement": "Appendix Figure A1: Map of CHE rates by region (24 INEI regions) at 25% threshold, weighted. Requires shapefile merging; use geopandas. This addresses geographic heterogeneity without inflating the main text.",
      "priority": "SHOULD"
    },
    {
      "category": "tables_and_figures",
      "requirement": "Appendix Table A1: Zero-OOP decomposition — for each insurance × quintile cell, report: (1) share with zero OOP, (2) conditional mean OOP_share given positive, (3) overall mean OOP_share. Decomposes the two-part model motivation.",
      "priority": "SHOULD"
    }
  ],
  "data_warnings": [
    "ZERO MASS POINT (critical): Expect 40–65% of households to report zero OOP in a given 4-week window. QR at τ=0.10 and τ=0.25 will likely estimate zero or near-zero coefficients and be uninformative for the distributional question. The two-part model is not optional — it is the primary estimator for identifying who participates in the market at all.",
    "ANNUALIZATION MISMATCH: GASHOG2D in Sumaria is already annualized. P416 variables cover the last 4 weeks only. Multiplying by 13 produces an unbiased annual estimate only if expenditure is evenly distributed across months — a strong assumption for acute illness. Flag this as a limitation; the paper is measuring 'annualized 4-week recall' not true annual OOP.",
    "INSURANCE OVERLAP: P4191 (SIS), P4192 (EsSalud), P4195 (EPS) are not mutually exclusive in raw data. Households can report multiple. Document the overlap frequency. Apply an explicit precedence rule (suggest: EPS > EsSalud > SIS > Uninsured) and report sensitivity to alternative rules.",
    "QUINTILE ENDOGENEITY TO HEALTH SPENDING: GASHOG2D likely includes health spending, so the quintile rank is partially determined by the outcome variable. Consider using a consumption measure that excludes health spending (GASHOG2D minus OOP) for quintile construction as the primary specification; report standard GASHOG2D quintile as robustness.",
    "ENAHO SAMPLE DESIGN: CONGLOME is the PSU but is not unique across years if pooling. For single-year use, CONGLOME is the correct cluster. Verify that CONGLOME does not repeat across strata in the 2024 wave. Report number of PSUs after merging to main analysis sample.",
    "SPARSE CELLS AT EXTREME QUANTILES: At τ=0.90 and τ=0.95, the effective estimation sample is the top 10%/5% of OOP_share. The insurance×quintile interaction model has many cells; expect collinearity or empty cells especially for EPS (rare insurance type). Consider dropping EPS×Q1 and EPS×Q2 interactions or collapsing EPS with EsSalud for extreme-quantile models.",
    "REGIONAL FIXED EFFECTS COLLINEARITY: With 24 region FEs and some insurance types (EPS) concentrated in Lima, collinearity between region FE and insurance may inflate SEs. Test VIF post-OLS. If VIF > 10 for any insurance dummy, consider region groups (coast/sierra/selva + Lima) instead of full FEs.",
    "FACTOR07 WEIGHT DISTRIBUTION: ENAHO oversamples rural and small-domain areas. FACTOR07 values can be very large for small-PSU observations. Check for extreme weight values (>50× median); consider winsorizing weights at 99th percentile for robustness. Report unweighted sample size vs. weighted population estimate.",
    "CHILDREN AND ELDERLY HEALTH SPENDING: Households with children <5 or elderly 65+ will have systematically higher OOP via pediatric and geriatric care. Confirm these are included as controls, NOT as subgroups of interest (unless explicitly motivated). Misspecification here inflates quintile 2/3 coefficients if correlated with age structure.",
    "P41603 'OTHER HEALTH COSTS' DEFINITION: This variable can capture very heterogeneous items (hospitalization, transport, dental, optical). If its variance is high, it may dominate the outcome. Check its distribution separately; flag whether it disproportionately affects upper-quantile estimates.",
    "MISSING CONSUMPTION DATA: Some households in Module 400 may not appear in Sumaria (module non-response). Report match rate. If match rate < 95%, investigate systematically whether non-matches are urban/rural, insured/uninsured, etc. Do NOT silently drop unmatched records.",
    "CAPACITY-TO-PAY DENOMINATOR: The strategy memo proposes using a food-subsistence floor for a 'capacity-to-pay' variant. Implementing this requires computing minimum food spending at household-size-specific equivalence scale. Use the Xu et al. (2003) WHO definition exactly: CTP = total expenditure − (food spending of households in the 45th–55th percentile of food-share distribution × HH size). Do NOT approximate with an arbitrary fraction of consumption.",
    "CHRONIC ILLNESS ENDOGENEITY: Chronic illness is a strong predictor of both insurance take-up (SIS targets chronic patients) and OOP. In a conditional QR this is a confounder, but it may mediate the insurance effect. Run one specification with and one without chronic illness to show it is a control, not a collider."
  ],
  "tables_required": [
    "Table 1: Weighted descriptive statistics by insurance group (SIS / EsSalud / EPS / Uninsured) — all key variables, p-value for equality, unweighted N and weighted population share",
    "Table 2: Distributional profile by consumption quintile — OOP_share at mean/median/p75/p90, CHE rates at 10%/25%/40%, zero-OOP share, insurance coverage rates",
    "Table 3: Main QR results — OLS + τ={0.10, 0.25, 0.50, 0.75, 0.90, 0.95}, cluster-bootstrap SEs, Wald test p-values for coefficient equality across quantile pairs",
    "Table 4: Two-part model — Panel A probit APEs for participation; Panel B conditional QR at τ={0.25, 0.50, 0.75, 0.90} on positive-OOP subsample",
    "Table 5: RIF unconditional QR results — unconditional marginal effects at τ={0.25, 0.50, 0.75, 0.90} side-by-side with conditional QR from Table 3",
    "Table 6: Robustness sensitivity — key coefficients (insurance, quintile 2, quintile 3) at τ=0.50 and τ=0.90 across 8 robustness specifications",
    "Table 7: CHE probit and LPM results — APEs for CHE_10, CHE_25, CHE_40 binary outcomes with same regressors",
    "Appendix Table A1: Zero-OOP decomposition by insurance × quintile cell",
    "Appendix Table A2: OLS with stepwise control addition (5 nested models) for τ=0.50 and τ=0.90",
    "Appendix Table A3: QR results with alternative annualization (×12 vs ×13 multiplier)",
    "Appendix Table A4: Fractional logit / fractional probit APEs as bounded-outcome robustness"
  ],
  "figures_required": [
    "Figure 1: Weighted kernel density of OOP_share by insurance group (overlaid, truncated at 0.6 or log-scaled); annotate zero-mass fraction per group",
    "Figure 2: QR coefficient plots — point estimate + 95% CI band across τ={0.10, 0.25, 0.50, 0.75, 0.90, 0.95} for (a) SIS dummy, (b) EsSalud dummy, (c) quintile 3 dummy; OLS horizontal reference line on each",
    "Figure 3: CHE rate heatmap — quintile (rows) × insurance group (columns), CHE-25% threshold; separate panel for CHE-10% and CHE-40% in appendix",
    "Figure 4: Predicted OOP_share vs. consumption quintile by insurance group at τ=0.50 and τ=0.90 (two panels), covariates at means — the core 'middle-income squeeze' visualization",
    "Figure 5: Two-part model decomposition — bar chart of zero-OOP probability and conditional mean OOP_share by quintile × insurance group, illustrating participation vs. intensity margins separately",
    "Appendix Figure A1: Choropleth map of CHE-25% rate by INEI region (24 regions), survey-weighted",
    "Appendix Figure A2: QR coefficient stability across control blocks (stepwise addition) for quintile 3 at τ=0.50 and τ=0.90"
  ]
}
```

**Key judgment calls embedded above:**

- **τ=0.10 should be reported but de-emphasized in text** — at this quantile you are almost certainly estimating the zero-mass boundary, not a genuine distributional difference. The two-part model is the real workhorse.
- **RIF-QR is MUST, not NICE** — conditional QR answers "given you are at the 90th conditional percentile," but policy relevance requires the unconditional statement "a household that moves from uninsured to SIS shifts the population 90th percentile by X." Referees who know FFL 2009 will ask for this.
- **No IV/RDD required** — this is correctly framed as descriptive. The Wald tests for quantile equality are the inferential core, not a causal claim.
- **Quintile construction must exclude own-OOP** — this is the single most likely data error that would invalidate the middle-income squeeze finding, and it is not mentioned in the strategy memo.