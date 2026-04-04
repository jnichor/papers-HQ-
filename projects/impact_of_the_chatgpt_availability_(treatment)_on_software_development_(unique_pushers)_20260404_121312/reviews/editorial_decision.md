```json
{
  "avg_referee_score": 63.5,
  "must_address": [
    "Pre-trend violation (F-test p=0.0003): the positive pre-treatment arc through 2021 that reverses in 2022 coincides with Russia-Ukraine sanctions (February 2022), not ChatGPT. Rambachan-Roth sensitivity analysis is required; verbal dismissal is insufficient.",
    "Russia as treated unit: the Russia-Ukraine war (February 2022) and associated IT-sector emigration break Russia's pre-treatment trend nine months before ChatGPT, rendering it an invalid treated unit. Russia must be dropped or its inclusion formally justified with a clean pre-trend.",
    "Q4 2022 first-treatment timing: ChatGPT launched November 30 — the final day of Q4 2022. A significant effect in that quarter cannot reflect adoption and more plausibly captures prior Russia-Ukraine dynamics. Re-estimate with Q1 2023 as the first treatment quarter.",
    "OECD-null result (coeff=-0.026, p=0.922): the effect disappears entirely when restricted to economically comparable peers. This is the most informative finding and strongly suggests the baseline result reflects differential development trajectories across heterogeneous controls, not ChatGPT-specific effects. A propensity-score-matched or entropy-balanced control group is required; the OECD null must be treated as the primary robustness test, not a footnote.",
    "Single-cluster standard errors for China-only and Russia-only regressions: with one treated cluster, Liang-Zeger cluster-robust SEs break down. The identical SE=0.036 across both regressions is statistically implausible and may indicate a coding error. Wild cluster bootstrap with imposed null is required for all single-treated-cluster estimates."
  ],
  "should_address": [
    "China — Gitee migration alternative explanation: GitHub access in China is intermittently throttled independent of ChatGPT, and Gitee grew from ~5M to 25M+ users over this period. The paper must bound this alternative by testing whether China's decline predates Q4 2022 and whether it is concentrated in repository types consistent with platform migration.",
    "China — VPN circumvention (Chen and Yang 2019, QJE): Chinese developers' documented technical sophistication makes the ChatGPT access restriction non-binding for a significant share of the treated population, undermining the -1.386 magnitude estimate. The paper must engage this literature and discuss implications for the treatment intensity assumption.",
    "Internally inconsistent pre-trend interpretation: claiming individual coefficients are 'small' while the joint F-test rejects parallel trends is logically inconsistent. The paper must formally reconcile these claims or replace them with sensitivity bounds."
  ],
  "may_address": [
    "Discussion of heterogeneous treatment effects across countries beyond China and Russia (e.g., Iran, North Korea) given their very different economic and developer-ecosystem contexts.",
    "Clarification of whether the outcome variable (unique pushers) captures productivity, participation, or platform engagement, and whether any of these is the theoretically relevant quantity for an AI-access shock."
  ],
  "fatal_issues": []
}
```