# Strategy Memo

## Title
Program Complementarity: Is Voucher + Training Superadditive?

## Research Question
Does simultaneous access to both a wage voucher and vocational training produce
employment gains larger than the sum of each program's individual effect?

## Empirical Strategy
Factorial RCT with interaction term:

    Y_i = alpha + beta1 * Voucher_i + beta2 * Training_i + beta3 * (Voucher_i x Training_i) + X_i * gamma + epsilon_i

- **beta1**: marginal effect of voucher (V=1 vs V=0, holding T=0)
- **beta2**: marginal effect of training (T=1 vs T=0, holding V=0)
- **beta3**: superadditivity parameter -- tests whether the joint program exceeds the sum of parts
- **H0**: beta3 = 0 (additive effects); **H1**: beta3 > 0 (complementarity)

## Design
- 2x2 factorial randomized controlled trial, 4 arms:
  1. Control (V=0, T=0)
  2. Voucher only (V=1, T=0)
  3. Training only (V=0, T=1)
  4. Both (V=1, T=1)
- Sample: 2322 community college graduates in Jordan
- Outcomes: labor force participation (l), employment type (t), wages (w), employment (e)
- Covariates: age, gender, community college, exam result

## Identification
**Level A -- Randomized Controlled Trial**

Random assignment to the four arms ensures unconfounded estimation of beta1, beta2,
and crucially beta3. The factorial design is efficient: it estimates main effects
with the full sample and the interaction with the contrast between the "both" arm
and the sum of single-arm effects.

## Robustness
- Balance verification (F-tests across 4 arms)
- Attrition analysis by arm
- Lee bounds for wage equation (conditional on employment)
- LATE/2SLS using assignment as instrument for take-up
- Permutation inference for beta3
- Benjamini-Hochberg correction across 4 outcomes
- Placebo tests (pre-treatment outcome, random assignment)
- Sensitivity to covariate specification

## Key References
- Groh, McKenzie, Shammout, Vishwanath (2016). "Testing the importance of search
  frictions and matching through a randomized experiment in Jordan." IZA Journal
  of Labor Economics.
- Crépon, Duflo, Gurgand, Rathelot, Zamora (2013). "Do labor market policies have
  displacement effects? Evidence from a clustered randomized experiment." QJE.
