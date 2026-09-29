# Fraud Model Claims Review

## Detailed Assessment

**Claim 1: Recall is 0.94 on held-out 2025 data, evaluated by independent risk-audit team on split modelling team never saw**

*Status: Adequately supported*

The claim meets the evidence standard: (1) the evaluation was conducted by an independent party (not the modelling team), (2) the data was held-out and unknown to the model developers, (3) a specific metric is provided (recall = 0.94), and (4) the rigorous evaluation design prevents overfitting bias. This is sound.

---

**Claim 2: Fraud losses fell 22% since launch (Q4 vs Q3; no comparison group; Q4 losses usually higher than Q3)**

*Status: Not adequately supported*

Problems:
- **No control group**: Without a comparison group that didn't receive the model, causation cannot be established. The 22% reduction cannot be attributed to the model itself.
- **Confounding seasonality**: Q4 losses are typically higher than Q3—the comparison admits this. A Q4-to-Q3 drop is the opposite of the expected seasonal pattern and may reflect other factors (market conditions, customer behavior, holidays). The baseline expectation is actually for higher Q4 losses, making this comparison fundamentally misleading.
- **Temporal confounding**: Other changes (staffing, rules, external factors) during the same period are unaccounted for.

The claim overstates evidence by attributing causation without a control.

---

**Claim 3: Model is fair across customer groups (modelling team reviewed 50 decisions and saw no problems)**

*Status: Not adequately supported*

Problems:
- **Biased evaluators**: The modelling team has incentive to find their model fair; this is not independent review.
- **Inadequate sample size**: 50 decisions is a very small sample for claiming fairness across multiple customer groups. Statistical power is unclear.
- **No formal metrics**: Fairness requires quantitative measurement—disparate impact ratios, demographic parity, equalized odds, etc. "Saw no problems" is subjective impression, not evidence.
- **Vague scope**: "Customer groups" is undefined. How many groups? What are the group sizes? Are disaggregated metrics available for each?

The claim lacks both rigor and independence.

---

**Claim 4: Analysts trust the model (Two senior analysts said so in a meeting)**

*Status: Not adequately supported*

Problems:
- **Anecdotal only**: Two opinions in a meeting is not a systematic measure of trust.
- **Not representative**: Two people cannot represent analyst sentiment across the organization.
- **No measurable standard**: What does "trust" mean operationally? Is this based on documentation, past performance, explainability, or something else?
- **Selection bias**: Were these analysts chosen because they already favored the model? How many analysts were asked?

This is a vague, unquantifiable claim based on minimal evidence.

---

**Claim 5: False-positive rate below old rules engine (1.8% vs 4.6%, shadow mode, same 3 months of live traffic, logged by payments platform)**

*Status: Adequately supported*

Strengths:
- **Fair comparison**: Both systems ran in shadow mode on identical data (same 3 months, same traffic), eliminating environmental confounds.
- **Independent logging**: The payments platform logged both results, reducing measurement bias.
- **Objective metrics**: False-positive rates are clearly defined and measurable.
- **Clear outcome**: 1.8% vs 4.6% is a substantial, unambiguous difference in the model's favor.

The evidence is solid for this specific comparison. However, note that shadow mode means neither system was in production, so real-world performance may differ.

---

**Claim 6: Will scale to 10x current traffic (Load-tested once at 2x on a laptop)**

*Status: Not adequately supported*

Problems:
- **Extrapolation far beyond evidence**: The claim jumps from 2x to 10x—a 5-fold extrapolation beyond tested conditions.
- **Only tested once**: A single load test is insufficient; results should be replicated.
- **Wrong environment**: A laptop is not a production environment. Database, network, dependencies, concurrent users, and hardware differ fundamentally.
- **No saturation data**: At 2x load, was the system approaching capacity? Was there headroom? Without understanding the curve, 10x scaling is pure speculation.

The claim goes far beyond what evidence supports.

---

VERDICTS
1: PROVEN
2: NOT PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
