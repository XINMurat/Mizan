# Mizan Audit: Fraud Model Board Summary

**Mode:** Audit (retrospective). **HARKing status:** This is a retrospective review. The claims were written after the results were known, and this audit is retrospective too. **Coverage:** I tiered all 6 of 6 claims, but only as they are described in the summary. I did not open any of the source artifacts (the risk-audit report, the payments-platform logs, the load-test output). So "PROVEN" below means that the described evidence meets the bar, as long as the cited artifact exists and says what the summary says. Attach it to the board pack.

**Bottom line:** I can't sign off on all six as proven. Two hold up (1 and 5). The other four are at most plausible hypotheses, and one of them (2) is framed in a way that will mislead the board. Presenting all six as "proven" would put the two strong results next to weak ones and cost them credibility.

## Claim-by-claim

**1. "Recall 0.94 on held-out 2025 data, evaluated by the independent risk-audit team on a split the modelling team never saw."**
`[K] Kanıtlanmış / Proven`, provided the risk-audit report is attached. The arbiter is a third party, the data was held out, and the modelling team was blind to the split. That is the right design.
Honesty annex: recall alone does not describe operating cost. Report precision or FPR at the same threshold, plus the fraud base rate. Also state which decision threshold was used and whether it was fixed before the evaluation.

**2. "Fraud losses fell 22% since launch." (QoQ, no comparison group, Q4 usually higher than Q3)**
`[Y] Yanıltıcı / Misleading` + `[KKE] Kritik Kontrol Eksik / Critical control missing`. The 22% figure is probably arithmetically true, but "since launch" implies the model caused it. This is a single before/after comparison with no control, and seasonality, fraud-actor drift, volume changes or other interventions could each explain it. The note says Q4 losses are usually higher than Q3. If the comparison runs in the Q3→Q4 direction, the true effect could be larger than 22%. If it runs in any other direction, seasonality could be producing the whole drop. The board cannot tell which case this is.
Missing control: a year-over-year same-quarter comparison, losses normalised by transaction volume, or a holdout or staggered-rollout comparison group. Until one of these exists, restate the claim as "losses were 22% lower QoQ; attribution to the model is not established."

**3. "The model is fair across customer groups." (modelling team reviewed 50 decisions)**
`[H] Makul Hipotez / Plausible hypothesis`, and closer to `[S]` as currently evidenced. The arbiter here is the author: the team that built the model reviewed its own decisions, so the claim carries a permanent `[KKE]` until someone independent checks it. There is no metric, no threshold and no group definition. Fifty decisions is far too few to detect disparities, especially in a fraud setting where each group contains only a handful of positives. "Saw no problems" is an absence of findings, not evidence of fairness.
Needed: predefined groups and metrics (for example, FPR and recall parity per group, with a tolerance locked in advance), computed on the full held-out set by an independent team such as the risk-audit team.

**4. "Analysts trust the model." (two senior analysts in a meeting)**
`[H] Makul Hipotez / Plausible hypothesis`, weakly supported. Two self-selected people spoke in a group setting, so the claim rests on selection bias and social pressure. There is no instrument and no counter-example search: did anyone who distrusts the model get asked?
Needed: an anonymous survey of all analysts, or better, a behavioural measure such as the override rate on model alerts. Otherwise drop the claim from the board deck.

**5. "FPR below old rules engine: shadow mode, same 3 months of live traffic, 1.8% vs 4.6%, logged by the payments platform."**
`[K] Kanıtlanmış / Proven`, provided the platform logs are cited. Both systems ran on the same traffic over the same period, which is a proper paired comparison, and the platform logged the results as an instrument arbiter, not the modelling team.
Honesty annex: also report the recall of both systems on that traffic, because an FPR reduction is only meaningful if detection is at least comparable. Also state how fraud labels were resolved in shadow mode, since label lag could affect the result.

**6. "It will scale to 10x current traffic." (load-tested once at 2x on a laptop)**
`[S] Spekülatif / Speculative` (at best `[H]`). The evidence does not reach the claim. The claim is about 10x, the test ran at 2x, a single run cannot show variance, and a laptop does not reproduce the production environment. Linear extrapolation from 2x to 10x is exactly where saturation points (database, queue, network, memory) go unobserved.
Needed: a load test on production-like infrastructure, ramped to at least 10x, repeated, with locked latency and error-rate thresholds (for example, p99 < X ms and errors < Y% at 10x). Until then, the board wording should be "tested to 2x; 10x not yet tested."

## Missing card
A board summary format has no place for costs, failures or open risks. This deck does not show precision or alert volume, model drift monitoring, what happens when the model is down, or the losses from fraud the model missed. The board should see at least one line on each of these.

## Mechanism, not motive
The skew is structural. Board summaries reward confident one-liners, so strong evidence (1, 5) and anecdote (3, 4) get the same formatting. Nothing here suggests intent.

## Next steps (criticality × impact/effort)
1. **Reword claim 2** today. The cost is zero, and it removes the one statement a sharp board member can attack.
2. **Reword claims 4 and 6** to state what was actually done ("two analysts reported…", "tested to 2x"), or drop them. The effort is low.
3. **Attach the sources for 1 and 5**, and add precision (1) and recall (5) alongside them. This takes low-to-medium effort and makes both results airtight.
4. **Commission an independent fairness evaluation (3)** with locked metrics. This is medium effort and matters most for regulatory risk. Present it as "in progress", not "fair".
5. **Schedule a production-grade 10x load test (6)** before any scaling commitment.

## Recommendation on the sign-off
I recommend presenting 1 and 5 as established results and presenting 2, 3, 4 and 6 honestly as preliminary, with the rewording above. If this recommendation is wrong, the cost is small: the deck gets a little less punchy. If we sign off on all six as proven and the board or a regulator later probes claim 2 or claim 3, the cost is the credibility of the whole model, including its two genuinely strong results. The decision is the team lead's, but I can't confirm all six as proven.

VERDICTS
1: PROVEN
2: NOT PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
