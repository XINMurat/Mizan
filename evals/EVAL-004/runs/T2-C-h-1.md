# Fraud Model Review: Evidence Assessment

## Claim-by-Claim Analysis

**Claim 1: Recall of 0.94 on held-out 2025 data**
This is adequately supported. The evaluation was conducted by an independent risk-audit team on data the modelling team never saw, establishing proper independence and no information leakage. The specific metric (0.94) is reported. A minor gap is the absence of a baseline (how did the previous model perform?), which limits context for judging whether 0.94 is a meaningful improvement, but the claim itself—that this is the measured recall—is proven.

**Claim 2: Fraud losses fell 22% since launch**
This is not proven. The team lead's own notes reveal critical flaws: no comparison group and acknowledged seasonality (Q4 losses are usually higher than Q3). Without either (1) a control group that did not use the model, or (2) seasonal adjustment, we cannot separate the model's effect from natural variation. A 22% drop could reflect better fraud conditions that quarter, not model performance. This conclusion goes far beyond what the data supports.

**Claim 3: Model is fair across customer groups**
This is not proven. The justification—a subjective 50-decision review by the modelling team—is inadequate. Problems: (a) the reviewers have vested interest in a positive verdict, (b) no systematic fairness metric (e.g., equal false-positive rates across groups) is defined or measured, (c) 50 decisions is a tiny sample for detecting fairness issues, (d) "saw no problems" is not a measurable outcome. This requires independent statistical testing on larger samples.

**Claim 4: Analysts trust the model**
This is not proven. Two senior analysts expressing approval in a meeting is anecdotal evidence at best. This is not systematic measurement of trust. Problems: (a) sample size of 2, (b) no structured survey or interview protocol, (c) informal setting allows social desirability bias (saying yes in a room with leadership), (d) trust is unquantified. A real finding would require formal surveys across the analyst team.

**Claim 5: False-positive rate below old rules engine (1.8% vs 4.6%)**
This is proven. The comparison is well-controlled: both systems ran in shadow mode on identical 3-month live traffic, results logged by an objective platform. This is a proper head-to-head test with clear, measurable outcome. The difference is substantial (4.6% → 1.8%) and the methodology is sound.

**Claim 6: Will scale to 10x current traffic**
This is not proven. Load-testing at 2x on a laptop does not support a 10x conclusion. Problems: (a) extrapolating from 2x to 10x (5× beyond tested capacity) is a large leap, (b) a laptop is not representative of production hardware and infrastructure, (c) only one test run provides no statistical confidence, (d) bottlenecks (database, API rate limits, memory) that appear at 5-10x scale are often different from those at 2x, so the test may miss critical failure modes. Real evidence requires load testing on production-equivalent hardware at or near target scale, and multiple runs.

## Summary

**Adequately supported:**
- Claim 1 (recall metric)
- Claim 5 (false-positive rate comparison)

**Not adequately supported:**
- Claim 2 (no control for seasonality)
- Claim 3 (subjective, small sample, no fairness metric)
- Claim 4 (anecdotal, tiny sample, no systematic measurement)
- Claim 6 (insufficient load testing, extrapolation beyond evidence)

The team lead's confidence is not warranted for the board. Claims 2, 3, 4, and 6 require substantially more evidence before presentation to oversight.

---
VERDICTS
1: PROVEN
2: NOT PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
