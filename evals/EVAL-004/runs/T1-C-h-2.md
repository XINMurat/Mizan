# Rigorous Review of Recommendation Engine Claims

This review examines each claim against standards for evidence, controls, bias, and causal inference.

## Claim 1: 18% increase in click-through rate
**Problem: Cherry-picked measurement period, no control group**
- The team selected their own 2-day measurement window, creating strong selection bias
- No comparison baseline, historical control, or concurrent control group
- No statistical significance testing or confidence intervals reported
- Dates could have been chosen specifically because they showed high performance
- This fails basic requirements for causal inference

**Verdict: NOT PROVEN**

## Claim 2: 3.1% higher basket value (95% CI: 1.8–4.4)
**Adequate evidence**
- Randomized controlled experiment with 60,000 users (large sample)
- Pre-registered primary metric reduces selective reporting bias
- Confidence interval excludes zero, indicating statistical significance
- Independent data team conducted analysis (reduces conflicts of interest)
- Methodology is methodologically sound

**Verdict: PROVEN**

## Claim 3: Users love the new engine
**Problems: Internal bias, no control, tiny sample**
- Only 12 people, all internal product team members
- No control group or comparison (no test of "old engine")
- Internal testers have conflicts of interest (they built it, want it to succeed)
- No control for confirmation bias or social desirability bias
- Favorable feedback from insiders does not constitute evidence of user satisfaction
- External user testing would be required for credibility

**Verdict: NOT PROVEN**

## Claim 4: Better recommendations than competitors
**Problem: Self-serving source with obvious conflict of interest**
- Benchmark comes from the supplier/vendor themselves
- Suppliers have financial incentive to claim superiority
- No independent third-party verification
- No peer review or external validation
- This is marketing material, not evidence

**Verdict: NOT PROVEN**

## Claim 5: Server cost 42,000 TL per month
**Adequate evidence**
- Audited cloud billing statement
- Concrete, verifiable financial fact
- No interpretation required; numbers don't lie when properly audited
- Clear documentation trail

**Verdict: PROVEN**

## Claim 6: Engine reduced churn
**Problem: Confounding variable makes causal claim impossible**
- Churn dropped in the month after launch
- But a price change was also made that same month
- Cannot isolate which factor caused churn reduction (or both, or neither)
- Price changes typically have direct, immediate impact on churn
- Without a control group or holding price constant, causality cannot be established
- The evidence supports "something changed," not "the engine reduced churn"

**Verdict: NOT PROVEN**

## Summary

Only 2 of 6 claims are adequately supported. Claims 1, 3, 4, and 6 should not be presented to the board as proven. Claim 2 (basket value increase) and Claim 5 (cost) are defensible.

---

VERDICTS
1: NOT PROVEN
2: PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
