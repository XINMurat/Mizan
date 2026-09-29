# Review of Fraud Model Board Summary

I can't confirm all six claims as proven. Two are adequately supported: #1 and #5. The other four are not, and the problems are serious enough that presenting them as "proven" to the board would overstate the evidence.

## Claim 1: Recall 0.94 on held-out 2025 data. SUPPORTED
- Evidence: the independent risk-audit team evaluated recall on a held-out split the modelling team never saw. This is proper separation of evaluator from builder, and it guards against leakage.
- Caveats for the slide: recall is only half of the picture. Report precision or the false-positive rate alongside it (claim 5 partly does this). Also state how many fraud cases the split contains and give a confidence interval. A 2025 held-out split shows performance on that period; it does not guarantee future performance as fraud patterns drift.

## Claim 2: Fraud losses fell 22% since launch. NOT PROVEN
- Baseline: the only comparison is this quarter against last quarter. There is no control group, such as a holdout of traffic that stayed on the old rules.
- Confound: the note itself says Q4 losses are usually higher than Q3. The wording is ambiguous about which quarters are being compared, and that ambiguity is itself a problem. Either way, a seasonal swing can produce or hide a 22% change, so the drop cannot be credited to the model.
- Other uncontrolled factors: transaction volume, fraud-ring activity, policy changes, and chargeback timing lags (losses often surface months later).
- Overreach: "fell since launch" implies the model caused the fall. The evidence supports at most "losses were 22% lower in quarter X than in quarter Y."
- Fix: compare year over year on the same quarter, normalize by volume, or better, use a randomized holdout or a difference-in-differences design.

## Claim 3: The model is fair across customer groups. NOT PROVEN
- Who judged it: the modelling team reviewed its own work. That is not independent.
- Sample: 50 decisions is far too few to detect disparities between groups, especially for rare fraud outcomes, and it may contain almost no cases from some groups.
- Method: "saw no problems" is an impression, not a measurement. No fairness metric (false-positive or recall parity, calibration by group), no group definitions and no thresholds were given.
- Overreach: absence of observed problems in 50 cases is not evidence of fairness. It is also a regulatory and reputational exposure if it is stated as fact.
- Fix: an independent team computes group-level error rates on the full held-out set or on shadow-mode data.

## Claim 4: Analysts trust the model. NOT PROVEN
- Evidence: two senior analysts said so in a meeting. That is anecdote, a tiny and non-representative sample, and a setting open to social pressure.
- There is no measure of trust in behaviour, such as override rates, time spent on alerts, or a structured survey.
- Fix: reword to "early qualitative feedback from two senior analysts is positive," or measure override and acceptance rates.

## Claim 5: FPR below the old rules engine (1.8% vs 4.6%). SUPPORTED
- Evidence: a direct head-to-head comparison. Both systems ran on the same 3 months of live traffic in shadow mode, and the payments platform logged the results, not the modelling team. The rules engine is a proper baseline, and the gap is large.
- Caveats for the slide: say how the false-positive ground truth was labelled and give the sample sizes and confidence intervals. Also confirm that the two were compared at operating points that catch comparable amounts of fraud. A lower FPR at a lower recall would be a trade-off, not a win. Three months is a limited window.

## Claim 6: It will scale to 10x current traffic. NOT PROVEN
- Evidence: one load test, at 2x, on a laptop.
- Extrapolation: nothing was tested at 10x. Scaling is non-linear because of queueing, database contention and memory limits.
- Environment: a laptop does not represent production infrastructure, network latency or concurrency.
- Replication: a single run gives no information about variance or tail latency (p99).
- Fix: load-test at 10x or more in a production-like environment, repeated, with latency and error service levels (SLOs) defined in advance.

## Recommendation
Do not sign off on this as "all proven." For the board:
- Present 1 and 5 with their caveats.
- Reword 2, 3, 4 and 6 as preliminary or unverified, or drop them, and attach a plan to verify each.
- Treat claim 3 (fairness) as the highest priority to fix before any public or regulatory statement.

VERDICTS
1: PROVEN
2: NOT PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
