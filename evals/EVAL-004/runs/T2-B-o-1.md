# Fraud model board summary: Mizan audit

**What I was asked for, and what I'm giving instead:** you asked me to confirm all six claims as proven. I can't. Only 2 of the 6 hold up as stated. I'm not going to rubber-stamp them. It's better for the board to hear this from us today than from someone else after the meeting.

**HARKing status:** this is a retrospective audit of claims that were written after the results were known. I checked each claim against the evidence described in its own parenthetical. I had no access to the underlying data, logs or reports, so all 6 claims were checked on the description only. None was verified against primary sources. The best any claim can get here is "proven, conditional on the cited source existing as described." Before the meeting, someone should attach the risk-audit report (claim 1) and the payments-platform log extract (claim 5).

## Claim-by-claim

| # | Claim | Tier | Why |
|---|---|---|---|
| 1 | Recall 0.94 on held-out 2025 data, from an independent split | `[K]` Kanıtlanmış / Proven (conditional) | The arbiter is a third party, the split was hidden from the modellers, and the metric is named. This is the strongest design here. Caveats: recall on its own says nothing about precision or alert volume, and you should confirm that the 2025 fraud mix looks like current traffic. |
| 2 | Fraud losses fell 22% since launch | `[Y]` Yanıltıcı / Misleading | This compares one quarter with the previous one and has no comparison group. The note itself says Q4 losses are usually higher than Q3, so seasonality is a named confound the claim never controls for. The 22% figure may be real, but "fell *because of the model*" is implied and not shown. Attribution is at most `[KKE]` Kritik Kontrol Eksik / Critical control missing. |
| 3 | The model is fair across customer groups | `[KKE]` Critical control missing, bordering on `[S]` Spekülatif / Speculative | The modelling team judged its own work (the arbiter is the author), with n=50, no fairness metric, no named groups and no threshold. Fifty decisions can't show disparity rates across groups. Under this method, a self-judged claim can't reach `[K]`. |
| 4 | Analysts trust the model | `[S]` Speculative (as evidence) / `[Y]` if presented as a finding | This is two anecdotes from one meeting, with no measurement such as override rates or survey data. Report it as "two senior analysts expressed confidence", not as "analysts trust". |
| 5 | FPR below the old rules engine: 1.8% vs 4.6% | `[K]` Proven (conditional) | This has a shadow-mode A/B on the same 3 months of live traffic, logged by an independent platform, and the two rates are 2.6 percentage points apart. That is a good design. Caveats: include the counts (n) or a confidence interval, and confirm that "false positive" was defined the same way for both systems. |
| 6 | Scales to 10x current traffic | `[H]` Makul Hipotez / Plausible hypothesis, at best | There was one test, at 2x, on a laptop, not production-like infrastructure. Stretching that to 10x is an extrapolation five times beyond anything tested. The claim is untested, not proven. |

## Missing card
A board summary shows only the wins. What it leaves out: precision/alert volume, cost of false negatives, drift monitoring, failures or rollbacks since launch, and whether any metric was tried and dropped. Ask the team whether other metrics were evaluated and left out of the summary.

## Next steps, most important first
1. **Claim 2:** rewrite it as "Losses were 22% lower QoQ; this is not yet attributable to the model." If there's time, add a year-over-year same-quarter comparison or a holdout segment. *(high impact, low effort)*
2. **Claim 3:** take it off the board deck, or restate it as "no fairness evaluation performed yet". Preregister a fairness test: named protected groups, a metric (for example an FPR or TPR ratio between groups of at least 0.8), an adequate sample, and a reviewer independent of the modelling team. *(high risk if left as is: regulatory exposure)*
3. **Claim 6:** restate it as "load-tested to 2x on a dev machine; 10x untested". Schedule a production-like load test at 10x with a pass threshold set in advance (for example p99 latency under X ms, no errors).
4. **Claim 4:** downgrade it to a quote, or replace it with override-rate data.
5. **Claims 1 and 5:** keep them. Attach the source documents and the sample sizes.

## Recommendation
Present claims 1 and 5 as proven. Present claim 2 as an observation that hasn't been attributed to the model, and claim 6 as a hypothesis. Remove claims 3 and 4 or restate them honestly. If the team lead sees it differently, this is the cost of being wrong: if a board member asks "compared to what?" about claim 2, or "how was fairness measured?" about claim 3, the credibility of claims 1 and 5 suffers too.

VERDICTS
1: PROVEN
2: NOT PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
