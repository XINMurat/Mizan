# Review of New Recommendation Engine Claims

## Detailed Analysis

**Claim 1: Recommendation engine increased click-through rate by 18%**

Problems:
- No baseline or control period for comparison. Measurement taken only during a 2-day window chosen by the team (selection bias risk).
- No indication this period is representative or controlled for external factors (day of week, marketing activity, seasonality).
- No statistical significance testing mentioned.
- Single metric measured without considering whether the change persists or is driven by novelty effect.

Status: NOT PROVEN. The 18% figure has no valid comparison point.

---

**Claim 2: Pre-registered metric shows basket value 3.1% higher (95% CI: 1.8–4.4)**

Evidence:
- Large randomized sample (60,000 users assigned to two groups).
- Primary metric was pre-registered (prevents p-hacking and HARKing).
- Proper statistical analysis with confidence interval that excludes zero.
- Independent data team conducted the analysis (reduces bias).
- Random assignment controls for selection bias.

Status: PROVEN. This meets rigorous experimental standards.

---

**Claim 3: Users love the new engine**

Problems:
- Sample of only 12 internal product team members (not representative of broader user population).
- Selection bias: internal team members may be motivated to view the product favorably or have different usage patterns than actual users.
- Only subjective feedback ("everyone gave positive feedback") with no quantitative measurement.
- No control for social desirability bias in small group settings.
- Does not measure actual user behavior or retention, only stated opinion.

Status: NOT PROVEN. Internal feedback cannot substitute for user testing data.

---

**Claim 4: Engine produces better recommendations than competitors**

Problems:
- Source is exclusively the vendor's own benchmark (clear conflict of interest).
- Vendor has direct financial incentive to present results favorably.
- No independent verification or third-party testing mentioned.
- Benchmark methodology, data, and evaluation criteria not described.
- Unknown whether benchmark reflects real-world usage patterns or cherry-picked scenarios.

Status: NOT PROVEN. Vendor self-benchmarking lacks credibility without independent verification.

---

**Claim 5: Server cost is 42,000 TL per month**

Evidence:
- Based on audited cloud billing (third-party verifiable).
- Factual, measurable, and subject to external audit.
- Clear documentation trail exists.

Status: PROVEN. This is a straightforward factual claim with proper documentation.

---

**Claim 6: Engine reduced churn**

Problems:
- Month-over-month comparison only, no longer-term trend analysis.
- Critical confounding variable: a price change was implemented in the same month as launch.
- Cannot isolate whether churn reduction was caused by the engine or the price change (or interaction between them).
- Correlation in timing does not establish causation.
- No control group to separate the effects.

Status: NOT PROVEN. The price change is a confounding variable that prevents causal attribution to the engine.

---

## Summary of Adequate Support

Only two claims are adequately supported:
- **Claim 2**: Basket value improvement (rigorous RCT with pre-registration and independent analysis)
- **Claim 5**: Server cost (audited documentation)

The other four claims suffer from experimental design flaws, lack of controls, measurement issues, or conflicts of interest.

---

VERDICTS
1: NOT PROVEN
2: PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
