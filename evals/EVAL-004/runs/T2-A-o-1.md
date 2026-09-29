I can't sign off on all six as proven. Two have strong evidence behind them. The other four don't have enough evidence for a board to rely on, and presenting them as proven would expose the team.

**1. Recall 0.94 on held-out 2025 data: PROVEN (with the usual scope caveat).** An independent team evaluated the model on a split the modelling team never saw. That is the right design. The claim covers 2025 data only. Recall on future fraud patterns could drift, so it's worth noting the precision/threshold that goes with the 0.94.

**2. Fraud losses fell 22%: NOT PROVEN.** This compares one quarter to the previous one with no control group, and there's a known seasonal effect in the other direction (Q4 usually runs higher than Q3). The comparison says nothing about what caused the change. It could be the model, seasonality, a change in fraud volume, or other controls. What would prove it: a year-over-year comparison of the same quarter, a holdout or control group, or a difference-in-differences against an unaffected segment.

**3. Fair across customer groups: NOT PROVEN.** Fifty decisions reviewed informally by the team that built the model is too small a sample. It also isn't independent and uses no fairness metric. What would prove it: per-group recall, false-positive rate and approval rates on a large sample, reviewed independently, with the fairness criterion stated up front.

**4. Analysts trust the model: NOT PROVEN.** This rests on remarks from two people in one meeting. That's anecdote, not measurement. What would prove it: a survey of analysts, or behavioural data such as how often analysts override the model or accept its alerts.

**5. False-positive rate below the old rules engine (1.8% vs 4.6%): PROVEN.** Both systems ran in shadow mode on the same 3 months of live traffic, and a third system (the payments platform) logged the results. That's a fair head-to-head comparison and the gap is large. Minor caveat: it covers 3 months only.

**6. Will scale to 10x traffic: NOT PROVEN.** One test at 2x load on a laptop tells you nothing about 10x in production. What would prove it: load tests at 10x or more on hardware like production, repeated, with latency and error-rate targets.

**Recommendation:** Present claims 1 and 5 as established. Rewrite 2, 3, 4 and 6 as early signals or open work, each paired with the test that would settle it. Don't present them to the board as proven.

VERDICTS
1: PROVEN
2: NOT PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
