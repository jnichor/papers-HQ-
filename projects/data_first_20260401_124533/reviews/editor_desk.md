## Desk Review Decision

**Assessment:**

The paper is technically competent and addresses a well-motivated question. The identification strategy (CTOT index as exogenous variation) is credible and well-established in the literature. The disaggregation of civil liberties and the asymmetric event study design are genuine innovations. Pre-trend tests are reported, clustering is appropriate, and the sample (80 countries, 7,330 obs.) is adequate for the design.

Several issues warrant referee scrutiny but do not warrant desk rejection: the sparse episode count (31 busts, 21 recoveries) for a 5-outcome event study; the oddity that the "recovery" coefficient for movement freedom is *negative* (-0.024) rather than near zero, which the paper does not discuss; and the selective reporting of the placebo test only for freedom of expression. The framing of "4 of 5 symmetry rejections" also sits in tension with the abstract's emphasis on movement as the headline finding.

These are substantive questions for referees, not fatal flaws.

```json
{
  "desk_decision": "PROCEED",
  "reason": "Clear research question, credible identification via CTOT index, appropriate data, and genuine methodological contribution in the asymmetric event study design. Core results are internally consistent. Issues—sparse episode counts, unexplained sign of recovery coefficient, selective placebo reporting—are within the scope of normal peer review.",
  "referee_1_type": "CREDIBILITY",
  "referee_2_type": "MEASUREMENT"
}
```

**Referee guidance:**

- **CREDIBILITY**: Scrutinize the episode definition (is the 20% threshold arbitrary and does it drive results?), staggered treatment timing and potential contamination across overlapping bust/recovery windows, and the adequacy of 80 clusters for the reported inference.
- **MEASUREMENT**: Evaluate whether the CLD ordinal scale (1–4) is appropriate for OLS event-study estimation, whether the five liberty dimensions are sufficiently distinct to support separate interpretation, and why the recovery coefficient for freedom of movement is negative rather than near zero.