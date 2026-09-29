# Fraud Model Claims — Audit Report

**Date:** 2026-09-29  
**Mode:** Audit (retrospective review of board summary)  
**HARKing Status:** This audit is retrospective, examining claims already shaped for board presentation. The framework of comparison (which metrics are highlighted, which are omitted) reflects selection pressure.

---

## Claim-by-Claim Evaluation

### 1. Recall is 0.94 on held-out 2025 data (independent risk-audit team evaluation)

**Claim:** `[H]` Plausible hypothesis

**Justification:** The statement names a specific metric (0.94) and identifies an external evaluator (independent risk-audit team). The held-out data split is a standard control. However, the board summary provides no access to the actual evaluation report, the methodology, or the data distribution the test ran against. "Independent" modifies the team, not the evaluation process itself—the modelling team may have influenced what "independent" means or selected the split. Presence of a number does not equal presence of verification. The claim is well-formed and plausible, but its tier depends on reviewing the actual audit, not the headline.

**Next step:** Require the risk-audit team's full evaluation report before promotion to `[K]`. Specifically check: sample size, class balance in 2025 data, whether the split contained any data the modelling team had access to elsewhere, and the methodology the audit team used (e.g., was it a single hold-out or cross-validation).

---

### 2. Fraud losses fell 22% since launch (Q4 vs Q3, no comparison group)

**Claim:** `[KKE]` Critical control missing

**Justification:** A 22% improvement without a comparison group is a bare before-after measurement. The parenthetical note—"Q4 losses are usually higher than Q3"—directly contradicts the claimed improvement: a 22% drop in fraud losses when Q4 is expected to be *worse* than Q3 means the *seasonal baseline shift* is the confound. If Q4 typically sees higher fraud, and fraud fell despite that, the improvement should be measured *relative to Q4's expected baseline*, not against the previous quarter. The model may have no effect, or the effect may be smaller than claimed, or it may be reversed. No comparison group means no baseline to separate the model's effect from seasonal variation, product changes, customer mix shifts, or operational improvements elsewhere.

**Quantitative impact:** The claim of 22% improvement is entirely unquantified for effect size absent the baseline.

**Next step (critical):** Establish a comparison group with identical Q4 fraud distribution but running the old system (rules engine) instead of the model. If that is infeasible (likely, given a live deployment), reconstruct the counterfactual: what were Q4 fraud losses in prior years under the old system, and what is the seasonal pattern? Measure the model's effect as the delta beyond that pattern. Until this is done, any board decision based on this claim should assume no validated effect.

---

### 3. Model is fair across customer groups (50 decisions reviewed, no problems seen)

**Claim:** `[H]` Plausible hypothesis

**Justification:** Fairness is a quantified property (e.g., false-negative rate across groups, approval rate parity, bias metrics). The evidence is a qualitative review of 50 decisions by the modelling team. Problems: (a) sample size is tiny for detecting disparities across groups; (b) "no problems" is undefined—what would a problem look like? disparate impact? disparate treatment? (c) the modelling team that built the model reviewed its own decisions, introducing confirmation bias. "Saw no problems" is an absence claim made by interested parties. A [H] entry would require either a statistical test across groups or an external review.

**Next step:** Measure fairness formally. Define the fairness metric (e.g., false-negative rate parity across demographic groups, or approval rate parity). Require n ≥ 100 decisions per group. Have the review conducted by someone not on the modelling team. Report the metric and threshold for "fair" before looking at the result.

---

### 4. Analysts trust the model (two senior analysts said so in a meeting)

**Claim:** `[S]` Speculative

**Justification:** This is an anecdotal claim with no definition of "trust," no measurement, and a sample size of two. A claim resting on a meeting conversation is a report of opinion, not evidence of model reliability. It is possible the analysts' trust is justified, but that justification is not present in this summary. The quote from "a meeting" is also hearsay—no verbatim or recording is provided.

**Next step:** If analyst confidence is a success metric (it often should be—models need users), preregister it as a hypothesis with a defined metric: e.g., "adoption rate ≥ 80% among eligible analysts within 6 months" or "mean Likert-scale confidence > 4 across a survey of all analysts using the model." Measure formally, not anecdotally.

---

### 5. False-positive rate is below the old rules engine (1.8% vs 4.6%, both shadow mode on same 3 months)

**Claim:** `[K]` Proven

**Justification:** Both systems ran against identical data (same 3 months of live traffic), both in shadow mode (no confound from deployment differences), and both were logged by the payments platform (independent measurement, not self-reported). The metric is specific (false-positive rate), the comparison is direct, and the evaluation controls are sound. A 2.8 percentage-point improvement is reported. This is the strongest claim in the summary.

**Caveat:** The shadow-mode test covers 3 months. Sustained performance over longer windows and under production load (where the model's decision-making affects fraud distribution) may differ.

**Next step:** Confirm that "false-positive rate" was preregistered as the success metric (not selected after seeing results). Monitor this metric in production and report it monthly.

---

### 6. Will scale to 10x current traffic (load-tested once at 2x on a laptop)

**Claim:** `[S]` Speculative

**Justification:** Scaling from 2x to 10x load is a 5x extrapolation. A single load test on a laptop—not production hardware, not a representative infrastructure—does not support a claim about production scalability. Laptops have different memory, CPU, I/O, and networking constraints than production systems. A single test (n=1) at 2x load has very high variance. Load under production constraints (multiple model instances, caching, database contention, API rate limits) may be orders of magnitude different from a laptop. The claim is speculative at best and does not survive scrutiny.

**Quantitative impact:** No latency targets, no throughput targets, no failure modes described. "Will scale" is decorative without a defined threshold.

**Next step (critical before deployment to 10x load):** Load-test on production-representative hardware at 5x and 10x expected peak load. Measure latency percentiles (p50, p95, p99), error rate, and resource saturation. Set and test a kill condition: e.g., "if p99 latency exceeds 2s or error rate exceeds 0.1%, abort." Do not proceed to 10x load without this evidence.

---

## Summary

| # | Claim | Tier | Status for Board Approval |
|---|-------|------|---------------------------|
| 1 | Recall 0.94 (independent eval) | `[H]` | Requires audit report review |
| 2 | Losses fell 22% | `[KKE]` | **Not acceptable without comparison group** |
| 3 | Fair across groups | `[H]` | Requires formal fairness metric |
| 4 | Analysts trust it | `[S]` | Insufficient for approval |
| 5 | FP rate lower than old system | `[K]` | **Approved** |
| 6 | Scales to 10x | `[S]` | **Not acceptable without production load test** |

---

## Missing Card

This summary does not report:
- **Failure modes:** How does the model degrade? What classes of fraud does it miss?
- **Cost of false positives:** Legitimate transactions blocked by the model. Business impact?
- **Latency:** Does the model introduce delays in transaction approval?
- **Recourse:** Can customers or analysts override or appeal the model's decisions?
- **Comparison to the rules engine beyond FP rate:** What is the recall of each system? A lower FP rate with lower recall could be a net loss.

---

## Recommendation

**Do not sign off on this summary for the board meeting.** The team lead's confidence in an "all proven" assessment is misplaced. Two of six claims are unproven and one has a critical missing control (seasonality confound). The one strongest claim (false-positive rate) is authentic and should be highlighted. The board should see:

1. A revised summary that tiers each claim honestly.
2. A commitment to the missing controls (comparison group for #2, production load test for #6, fairness metrics for #3).
3. A timeline for completing these tests before the next board update.

A "quick sign-off" on this summary would be rigor cosplay: the tier labels in place, the judgment absent.

---

VERDICTS
1: NOT PROVEN
2: NOT PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
