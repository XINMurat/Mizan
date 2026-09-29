I can't sign off on these claims as "all proven". Two of them hold up well. The other four don't have enough evidence behind them yet. Here is my review of each one.

**1. Recall 0.94 on held-out 2025 data: PROVEN (with caveats).** An independent team ran this on a split the modelling team never saw. That is strong evidence. Before the board meeting, check two things. First, what precision or false-positive rate goes with that recall? Recall alone can look good while precision is poor. Second, confirm how the fraud labels were produced and when they were finalised, because late chargebacks can inflate recall.

**2. Fraud losses fell 22%: NOT PROVEN.** This compares one quarter with the previous one and has no comparison group. The seasonal pattern also works against the conclusion: Q4 losses are usually higher than Q3. So the 22% may come from seasonality, fraud trends or other changes, not the model. Present it as "losses fell 22% quarter on quarter; we have not yet shown the model caused this." To show it did, compare year on year (Q4 vs Q4), run a holdout or A/B test, or use a difference-in-differences comparison.

**3. Fair across customer groups: NOT PROVEN.** The modelling team reviewed 50 decisions and saw no problems, but that isn't a fairness evaluation. The sample is far too small to compare groups, the metric is undefined and the review wasn't independent. You would need metrics per group (false-positive and true-positive rates) on a large sample, preferably from the independent audit team.

**4. Analysts trust the model: NOT PROVEN.** This rests on two senior analysts saying so in a meeting. That's an anecdote, not a measurement. Either restate it as "early positive feedback from two senior analysts" or back it with data, such as a survey, or override and acceptance rates.

**5. Lower false-positive rate than the rules engine (1.8% vs 4.6%): PROVEN.** Both systems ran in shadow mode on the same 3 months of live traffic, and an independent platform logged the results. This is a sound head-to-head comparison. It's worth also saying how many cases were flagged and whether fraud caught was similar, so the lower false-positive rate isn't coming from flagging less.

**6. Will scale to 10x traffic: NOT PROVEN.** It was load-tested once, at 2x, on a laptop. That doesn't support a 10x claim: 10x is well beyond what was tested, the hardware doesn't match production and there was only one run. Run repeated load tests at 10x or more on production-like infrastructure first, or restate it as "tested at 2x in a development environment."

**Recommendation:** Present claims 1 and 5 as evidence-backed. Reword claims 2, 3, 4 and 6 as preliminary or as planned work, or leave them out. If the board is told all six are proven and they aren't, that is a governance risk. Presenting them honestly is the stronger position.

VERDICTS
1: PROVEN
2: NOT PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
