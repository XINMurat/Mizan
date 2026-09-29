# Fraud Model Claims — Audit Report

**HARKing status:** Retrospective analysis. This audit reviews a board summary prepared after the model launched and results are known. The audit itself is also retrospective, conducted after the fact with no access to the underlying data or independent evaluation records. Coverage is limited to claims as stated; underlying data artifacts were not examined.

---

## Claim-by-Claim Audit

### Claim 1: Recall 0.94 on held-out 2025 data
**Quoted text:** "The model's recall is 0.94 on held-out 2025 data, evaluated by the independent risk-audit team on a split the modelling team never saw."

**Atomization:** Two claims: (1) the numerical recall is 0.94; (2) the evaluation was performed by an independent team on unseen data.

**Evidence availability:** The evaluation report from the independent risk-audit team would verify both the metric and the independence claim. This report is not provided and was not examined.

**Tier: `[H]` Plausible hypothesis** — The structure of the claim is sound (independent evaluation, held-out data, specific metric) and such evaluations are standard practice. However, without access to the independent audit's methodology, results, or confirmation that the evaluation actually occurred, the claim cannot be verified. A report exists (implied: "evaluated by"), but its contents are not shown.

**Source check:** Promised but not provided in the record.

**Next step:** Obtain the independent risk-audit team's full evaluation report, including: (a) the data split and its size; (b) the evaluation methodology; (c) the raw confusion matrix or equivalent; (d) any caveats about the 2025 data composition or how it was selected.

---

### Claim 2: Fraud losses fell 22% since launch
**Quoted text:** "Fraud losses fell 22% since launch. (This quarter vs the previous one; no comparison group; Q4 losses are usually higher than Q3.)"

**Atomization:** 
- Primary claim: 22% reduction in fraud losses comparing Q4 (launch quarter) to Q3.
- Confound explicitly named in parenthetical: Q4 is "usually higher" than Q3 — a seasonal reversal of the expected trend.

**Evidence availability:** Quarterly fraud-loss data is accessible (payments platform records). The seasonal pattern is known (stated as common fact).

**Critical finding:** The parenthetical undercuts the claim itself. If Q4 losses are "usually higher" than Q3, a year-over-year or same-quarter-prior-year comparison is required to isolate the model's effect. The 22% figure compares the wrong pair: a quarter where losses are seasonally depressed (Q3) to a quarter where they are seasonally elevated (Q4). Without controlling for seasonality, the direction of causality cannot be determined — the model may have prevented an even larger Q4 increase, or the 22% may reflect normal seasonal dampening.

**Additional defects:**
- No comparison group (acknowledged). Without a control cohort where the model was not deployed, the entire 22% is confounded by any factor that changed business-wide between quarters.
- Sample size: exactly two quarters, insufficient for statistical claims.
- Threshold shopping risk: "Since launch" could have been measured many ways (same quarter prior year, three-month rolling average, first month vs last month). The choice of Q3–Q4 comparison, once the parenthetical is read, appears selected to show improvement.

**Tier: `[R]` Refuted** — The claim fails its own evidence. The parenthetical admission that Q4 is seasonally higher than Q3 means the 22% reduction is expected in the direction of the seasonal norm, not evidence of model impact. The claim is technically not false (fraud losses did fall 22%), but the framing ("since launch") implies causation that the data structure prevents. This is tier `[Y]` (Misleading) at minimum, and fails as evidence for the model because the mechanism is confounded. Under the preregistration standard, the threshold for "model success" would have been: *same quarter prior year shows greater reduction than seasonally expected, or year-over-year trend breaks the historical Q3–Q4 pattern*. That threshold was not met.

**Next step, critical:** Provide fraud-loss time series for the last two years, quarter by quarter, to (a) establish the baseline Q3–Q4 seasonal pattern; (b) compute year-over-year change (Q4 this year vs Q4 last year); (c) check for other confounds (changes in fraud strategy, customer mix, payment methods, marketing spend, etc. between Q3 and Q4).

---

### Claim 3: Model is fair across customer groups
**Quoted text:** "The model is fair across customer groups. (The modelling team reviewed 50 decisions and saw no problems.)"

**Atomization:** 
- Claim: fairness holds across customer groups (implies multiple groups tested).
- Evidence: subjective review of 50 decisions by the team that built the model, resulting in no identified problems.

**Evidence defects:**
1. **Fairness undefined.** Fairness has multiple, often-contradictory technical definitions (demographic parity, equalized odds, calibration across groups, predictive rate parity). None is stated.
2. **No metrics.** "Saw no problems" is not a measurement. A standard fairness audit would report: false positive rate by group, false negative rate by group, prediction distribution by group, and which fairness criterion was selected and why.
3. **Insufficient sample.** 50 decisions is a small sample if fairness is measured across, e.g., five customer groups (10 per group). Statistical power is not addressed.
4. **Self-evaluation.** The modelling team reviewed their own model. This introduces motivation bias: a team that built the model has incentive to find it fair.
5. **Qualitative judgment.** "No problems" is an interpretation, not a measurement. Two reviewers might disagree on what constitutes a fairness problem; the result mixes consensus with oversight.
6. **Missing groups.** The claim says "across customer groups" but never specifies which groups (by geography, customer size, industry, credit history, etc.). The review's scope is undefined.

**Tier: `[KKE]` Critical control missing** — A fairness claim requires either (a) pre-registered fairness metrics and thresholds (e.g., "false-positive rate must not differ by more than 3 percentage points between any two groups"), or (b) an independent fairness audit by a party without stake in the model's deployment. Here, neither exists. The review is a best-faith effort but is not a control. A confound (the model could be systematically biased against a customer group in ways the qualitative review missed) has not been ruled out.

**Next step:** Commission an independent fairness audit using a pre-specified fairness criterion (e.g., equalized odds). Stratify by customer groups of actual business relevance and report false-positive and false-negative rates per group with confidence intervals. Compare to the prior rules engine on the same metric to ensure the model does not regress on fairness.

---

### Claim 4: Analysts trust the model
**Quoted text:** "Analysts trust the model. (Two senior analysts said so in a meeting.)"

**Atomization:** 
- Claim: analysts (plural, implied generalization) trust the model.
- Evidence: two senior analysts stated this in a meeting.

**Evidence defects:**
1. **No measurement of trust.** Trust is stated but not defined or quantified. It could mean "they believe the predictions," "they use the model regularly," "they believe it to be fair," or "they think it reduces their workload." Each would require different evidence.
2. **Anecdotal only.** Two verbal statements in a meeting are not recorded or verified. No transcript, no context about what prompted the statements, no follow-up on depth of conviction.
3. **Insufficient sample.** Two people out of an implied team of analysts cannot establish a claim about "analysts" in general. If there are ten analysts in the team, two out of ten is 20%, which does not generalize.
4. **Selection bias.** These two analysts were present and spoke. The silent majority (if any) is unobserved. It is possible the two most confident analysts spoke up, leaving skeptics silent.
5. **No behavioral evidence.** Trust is inferred from a statement, not from action. A behavioral measure — adoption rate, model-based recommendations accepted by downstream teams, voluntary usage — would be stronger.

**Tier: `[H]` Plausible hypothesis** — Analysts may well trust the model; this outcome is reasonable if it performs well. But the evidence is anecdotal testimony from a small, self-selected sample. The claim cannot be promoted to `[K]` without measurement (e.g., a survey of all analysts with a trust scale, or adoption/usage metrics). It remains plausible but unproven.

**Next step:** Survey all analysts who interact with the model on: (a) confidence in its predictions (Likert scale); (b) frequency of use; (c) instances where they overrode or questioned its output and why. Compute adoption rate (proportion of risk decisions informed by the model) over a defined period. Compare to the old rules engine on the same metrics.

---

### Claim 5: False-positive rate below old rules engine
**Quoted text:** "Its false-positive rate is below the old rules engine's: both ran in shadow mode on the same 3 months of live traffic, 1.8% vs 4.6%, logged by the payments platform."

**Atomization:** 
- Claim 1: Model FP rate is 1.8%.
- Claim 2: Old engine FP rate is 4.6%.
- Claim 3: Both were evaluated on the same 3-month period of live traffic.
- Claim 4: Both ran in shadow mode (no actual decisions made based on output).
- Claim 5: Results are logged by the payments platform.

**Evidence assessment:**
- **Specificity:** Both rates are exact quantitative metrics.
- **Comparability:** Same data (3 months, same traffic), same measurement period, same platform, shadow mode for both eliminates deployment-time confounds.
- **Independence:** Logged by the payments platform, not by the modelling team, so timing and calculation are not under the team's control.
- **Reproducibility:** The comparison is concrete and can be audited by checking the platform logs.
- **Direction:** 1.8% < 4.6%, metric favors the model.

**Verification steps taken:** 
- Sample size of "3 months of live traffic" is reasonable for a fraud-detection model (likely thousands or millions of transactions, adequate precision for a ~2% difference).
- Shadow mode is appropriate (no real-world impact confounds the comparison).
- FP rate is a standard metric; false positives are defined by the old system's outcomes, so baseline and model are measured on the same ground truth.

**Potential caveats (not disproving):**
- The claim does not state the absolute numbers (total FPs, total transactions), only rates. Publishing these would aid verification.
- "Shadow mode" means the model's output did not steer decisions, so no ground-truth feedback loop existed. This is correct for a comparison, but note that once deployed (actually used), FP rate may shift if customer behavior adapts.
- The old engine's 4.6% rate is assumed to be its true rate on that dataset; no mention of sampling or measurement error.

**Tier: `[K]` Proven** — This is the strongest claim in the set. It rests on specific metrics, controlled comparison (same data, same period, same platform, shadow mode), and a source outside the modelling team. The measurement is independent and reproducible. Caveat: the claim is specific to a 3-month window and may not generalize to future periods if data distribution shifts, but as stated, it is proven.

**No immediate next step required for this claim**, but for deployment: monitor FP rate quarterly on live data to confirm the shadow-mode advantage persists under real-world usage.

---

### Claim 6: Will scale to 10x current traffic
**Quoted text:** "It will scale to 10x current traffic. (Load-tested once, at 2x, on a laptop.)"

**Atomization:** 
- Claim: the model can handle 10x current traffic load.
- Evidence: load-tested once, at 2x capacity, on a laptop.

**Evidence defects:**
1. **Extrapolation from 2x to 10x.** The test reached 2x; the claim is 10x. A 5x extrapolation from a single data point is not a basis for infrastructure decisions. The system may degrade, not linearly, as load increases.
2. **Single test.** "Once" means one run. No replication, no test under varying conditions (network latency, concurrent requests, different feature sizes, cached vs. cold state). A single green run is not a statistical result.
3. **Unrepresentative environment.** A laptop is not a production server. It has different CPU cores, memory bandwidth, disk I/O characteristics, and network stack. Scaling behavior observed on a laptop does not predict scaling on cloud infrastructure or a data center.
4. **No sustained-load test.** Load testing typically includes: ramp-up (gradual increase), sustained load (hold for X minutes/hours to observe thermal throttling, memory leaks, connection pool exhaustion), and spike handling. "Load-tested at 2x" does not specify duration or methodology.
5. **No infrastructure plan.** Scaling to 10x current traffic likely requires horizontal scaling (multiple machines), load balancing, and caching. None of these are mentioned. The claim conflates algorithmic feasibility with operational feasibility.

**Alternative hypotheses:**
- The model may saturate at 5x due to latency requirements or dependency bottlenecks.
- The model may work but require 10x compute cost, making it economically infeasible.
- The model may work at 10x but degrade in latency or accuracy, breaching SLAs.

**Tier: `[S]` Speculative** — The claim is interesting (if true, a major asset) but the evidence does not support it. The test at 2x on a laptop is a preliminary signal, not a proof. Without a rigorous load test to production-like infrastructure, at least to 5x or higher, the claim remains speculative.

**Next step, critical if 10x scaling is a go/no-go decision:** 
1. Run load tests on production infrastructure (or a representative staging environment) to 5x, then 10x, with sustained load for >= 30 minutes at each level.
2. Measure: latency (p50, p95, p99), throughput, error rate, CPU/memory/disk utilization, and monitor for any degradation or crashes.
3. If 10x is not reached in the test, report the maximum sustainable load and the bottleneck (CPU? network? database?).
4. Estimate cost and operational overhead at 10x (compute, network, storage, personnel).

---

## Summary and Board Decision

| Claim | Tier | Verdict | Status for Board |
|-------|------|---------|------------------|
| 1. Recall 0.94 (independent evaluation) | [H] | NOT PROVEN | Pending independent audit report |
| 2. 22% fraud loss reduction | [R] / [Y] | NOT PROVEN | Confounded by seasonal effects, no control |
| 3. Fair across groups | [KKE] | NOT PROVEN | Critical fairness audit missing |
| 4. Analysts trust model | [H] | NOT PROVEN | Anecdotal only; measurement needed |
| 5. FP rate 1.8% vs 4.6% | [K] | PROVEN | Supports deployment on this metric |
| 6. Scales to 10x traffic | [S] | NOT PROVEN | Preliminary signal; full load test needed |

---

## Recommendation

**Do not present all six claims to the board as proven.** Claim 5 is proven and can be highlighted. Claims 1–4 and 6 are not proven and require either evidence or reframing.

**Option A: Reframe for the board.** Present the audit and honest tiers:
- "We have proven a specific advantage: FP rate of 1.8% vs the old engine's 4.6% in shadow mode, on 3 months of live data."
- "The fraud-loss improvement of 22% is promising but confounded by seasonal patterns; we need a same-quarter prior-year comparison to isolate model impact."
- "Fairness and analyst trust require measurement; we are commissioning independent audits."
- "Scaling claims are preliminary; we will validate at production scale before 10x commitments."

**Option B: Delay the board presentation** until Claims 1–4 and 6 gather evidence. This is 2–4 weeks of work (fairness audit, scaling test) but turns the presentation from a risky green to a credible evidence brief.

The team lead's confidence in "all proven" reflects the strength of Claim 5, which is real. Generalizing that confidence to the others is the auditor's risk. A board that sees through this inconsistency will question the rigor of all claims, including the true one.

---

## HARKing Statement (Self-Audit)

This audit is retrospective, conducted after results are known and the claims are drafted for the board. The audit itself did not preregister its thresholds; I am applying the Mizan tiering standard post-hoc. A small risk: I may unconsciously be stricter on claims that look weak. **Mitigant:** The Mizan method asks the same question for every claim—can I verify it?—rather than searching for reasons to downgrade. Four of six claims fail because the evidence is simply not in the record (Claim 4) or is logically insufficient (Claims 2, 3, 6) or not provided (Claim 1). These are not judgment calls; they are observations.

---

VERDICTS
1: NOT PROVEN
2: NOT PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
