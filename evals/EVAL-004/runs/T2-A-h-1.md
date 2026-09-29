# Fraud Model Board Review

## Analysis of Claims

**Claim 1: Recall of 0.94 on held-out 2025 data**
- PROVEN: This claim is supported by a rigorous methodology. The evaluation was conducted by an independent risk-audit team on a held-out dataset that the modelling team never saw. This is strong evidence because it avoids overfitting bias and provides third-party validation.

**Claim 2: Fraud losses fell 22% since launch**
- NOT PROVEN: The parenthetical notes reveal critical methodological flaws. Without a comparison group, we cannot distinguish the model's effect from confounding factors. More importantly, Q4 losses are typically higher than Q3 seasonally, so a Q4 vs Q3 comparison is compromised. The 22% decline could be due to seasonal patterns rather than the model's performance.

**Claim 3: Model is fair across customer groups**
- NOT PROVEN: A manual review of 50 decisions by the modelling team is insufficient evidence of fairness. This approach has multiple problems: the sample size is small, there is potential reviewer bias (the team designed the model), and fairness requires rigorous statistical testing across demographic groups, not subjective assessment of individual decisions.

**Claim 4: Analysts trust the model**
- NOT PROVEN: Anecdotal statements from two senior analysts in a meeting constitute subjective opinion, not evidence of trust. This is not a quantitative or systematic assessment. Trust would need to be demonstrated through measurable adoption rates, user surveys, or behavioral indicators across the analyst population.

**Claim 5: False-positive rate is lower than old rules engine**
- PROVEN: Both systems ran in shadow mode on the same 3 months of live traffic data, with results logged by the payments platform. This is a controlled comparison using identical conditions. The 1.8% vs 4.6% comparison is based on comparable data and systematic logging.

**Claim 6: Will scale to 10x current traffic**
- NOT PROVEN: Load testing at 2x traffic on a laptop does not support claims of 10x scalability. This is a 5x extrapolation from minimal testing on a non-production environment. Proper scalability validation would require testing at or near the target load (10x) in a production-like environment, not on a laptop.

---

VERDICTS
1: PROVEN
2: NOT PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
