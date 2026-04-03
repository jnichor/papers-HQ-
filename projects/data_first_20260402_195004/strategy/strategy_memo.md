# Strategy Memo

## Title
Apartheid vs. Persecution Label Effects on ICC Referral Support

## Research Question
Does labeling Israeli actions as 'apartheid' vs 'persecution' differentially increase support for ICC referral?

## Method
- OLS with randomized treatment assignment, HC2 robust standard errors
- Conditional Average Treatment Effects (CATE) by pro_israel_score quintile
- Double LASSO covariate selection (Belloni et al., 2014)
- Robustness: ordered probit, logit on binary outcome, permutation inference, Lee bounds

## Identification Strategy
**Level A -- Randomized Experiment**

The dataset comes from a survey experiment with random assignment to vignette conditions.
The treatment variable `apartheid_vs_persecution_treat` is binary (1 = apartheid label,
0 = persecution label) and was randomly assigned within the relevant experimental arm.

Because assignment is randomized, the raw difference-in-means is an unbiased estimator
of the Average Treatment Effect (ATE). We include pre-treatment covariates to improve
precision but not for identification.

## Key Variables
- **Treatment**: `apartheid_vs_persecution_treat` (binary, 0 = persecution, 1 = apartheid)
- **Primary outcome**: `ICC_referral` (ordinal 1-5)
- **Secondary outcome**: `ICC_referral_binary` (binary)
- **Moderator**: `pro_israel_score` (continuous, split into quintiles for CATE)
- **Pre-treatment covariates**: respondent_age, female, white, black, education,
  stronger_republican_8pt, hawkish_aggregate, hostile_sexism_agg,
  benevolent_sexism_agg, cosmopolitan, knowledge_ir_agg

## Analysis Pipeline
1. `00_clean.py` -- Data cleaning, missingness audit, balance checks
2. `01_main.py` -- ATE estimation (3 specs), CATE, permutation test
3. `02_robustness.py` -- Ordered probit, logit, alternative moderators, Lee bounds, BH correction
4. `03_output.py` -- Figures (PDF), LaTeX tables, results summary
