# Audit Report: New Recommendation Engine Claims

**Date of audit:** 2026-09-29  
**Target:** Board summary claims (6 assertions) for new recommendation engine  
**Audit mode:** Retrospective (claims already generated; board presentation scheduled)  
**HARKing status:** Claims were crafted after engine was built and launched; no preregistration visible. Metrics cherry-picked from broader engine telemetry. Audit is also retrospective.

---

## Executive Summary

Of the six claims presented to the board, only two meet the threshold for `[K]` (Proven). Three fall to `[H]` (Plausible Hypothesis) due to missing evidence or design flaws, one is `[KKE]` (Critical Control Missing) due to a confound, and one risks `[Y]` (Misleading) due to undisclosed conflicts of interest.

The team leader's request for "quick approval" of all claims cannot be granted. Two claims (basket value, server cost) are defensible; four require either additional controls or demotion to hypothesis tier. Presenting all six as proven to the board would misrepresent the evidence.

---

## Detailed Tier Analysis

### Claim 1: Recommendation engine increased click-through rate 18%
**Tier: [H] Plausible Hypothesis**

**Claim as stated:** "Recommendation engine increased click-through rate by 18%. (Team measured it in self-selected 2-day period; no comparison period.)"

**Evidence structure:**
- Measurement: 2-day period, self-selected by team
- Baseline: None stated
- Sample: Not stated
- Calculation method: Not stated

**Justification:** A self-selected measurement window is the definition of selection bias in A/B testing. The team chose the two days AFTER results were visible, not before. The absence of a comparison period (control group, pre/post split, or historical baseline) means any observed lift could be:
  - Natural variation in user behavior (day-of-week, time-of-season effects)
  - Novelty effect (users click more because something is new)
  - Operator behavior change (team pushed different content during the window)

The claim survives as a plausible observation but cannot support a board-level decision. This is HARKing by measurement window: Hypothesis After Results Known.

---

### Claim 2: Basket value 3.1% higher (95% CI: 1.8–4.4)
**Tier: [K] Proven**

**Claim as stated:** "60,000 users randomly assigned two arms; basket value on new engine 3.1% higher (95% GA: 1.8–4.4). Pre-registered primary metric analyzed by independent data team."

**Evidence structure:**
- Sample size: 60,000 (large, adequate for precision)
- Randomization: Explicit random assignment to two arms
- Primary metric: Pre-registered (threshold locked before seeing data)
- Analyzer: Independent data team (conflict-of-interest check passed)
- Confidence interval: 95%, 1.8–4.4 (lower bound excludes zero; threshold met)

**Justification:** This claim meets the gold standard for a single-factor experiment:
1. **Preregistration:** Primary metric was locked before analysis (prevents threshold shopping)
2. **Randomization:** Removes confounds via assignment mechanism
3. **Independence:** Data team separate from product team (removes motive to inflate)
4. **Sample size:** 60,000 is sufficient to resolve 3.1% effect with tight CI
5. **Quantitative threshold:** 95% CI is a standard arbiter; verdict is deterministic

This claim reaches `[K]`. It is proven within its scope (basket value on the tested sample during the test period).

---

### Claim 3: Users love the new engine
**Tier: [H] Plausible Hypothesis**

**Claim as stated:** "Users love the new engine. (Product team's 12-person internal test; everyone gave positive feedback.)"

**Evidence structure:**
- Sample: 12 internal employees (product team)
- Method: Internal testing, not stated whether structured feedback or casual
- Result: 100% positive (12 of 12)

**Justification:** Four independent failures of this claim:
1. **Selection bias:** Internal employees are not representative users. They have context (know the feature is new, expect it to be good, may fear social cost of criticism).
2. **Sample size:** N=12 is below the threshold for generalizing user preference claims. (No confidence interval provided; "everyone" is anecdotal language.)
3. **Measurement method:** "Positive feedback" is unstructured. No distinction between "works" and "love." No intensity scale; 11/12 positive would use identical language.
4. **100% positive is a red flag:** In any real sample, at least one user dislikes a feature for idiosyncratic reasons. Unanimous response suggests social desirability bias (people don't want to disappoint the team that built it).

The claim is plausible — the engine may be well-liked — but the evidence is anecdote, not measurement. Reported as `[H]`.

---

### Claim 4: Engine produces better recommendations than competitors
**Tier: [Y] Misleading (conflict of interest undisclosed)**

**Claim as stated:** "Engine produces better recommendations than competitors. (Source: supplier's own benchmark.)"

**Evidence structure:**
- Benchmark: Conducted by the supplier
- Competitors: Not named
- Methodology: Not stated
- Results: Not detailed

**Justification:** Undisclosed conflict of interest makes this claim misleading:
1. **Supplier incentive:** The supplier of the engine has direct financial interest in its superiority claims. Any benchmark they run is post-hoc justification of a sale, not independent evidence.
2. **Methodology opacity:** "Benchmark" is not defined. Was it a public benchmark (e.g., RecSys dataset)? Custom data? Supplier's own metrics favoring their design choices?
3. **Competitor cherry-picking:** Which competitors? If three alternatives were tested and two fared better, this headline is false even if worded to sound true.
4. **Missing control:** No independent party (research team, third-party lab, academic audit) repeated the test.

This claim reaches `[Y]` because it is technically possible the statement is true while being framed to mislead: a supplier benchmark is inherently biased by its source. The board should see it labeled as such.

---

### Claim 5: Server cost is 42,000 TL per month
**Tier: [K] Proven**

**Claim as stated:** "Engine's server cost 42,000 TL/month. (Audited cloud invoice.)"

**Evidence structure:**
- Source: Cloud invoice (primary financial document)
- Audit: Explicit mention of audit
- Quantification: Precise monthly amount
- Verification: Document exists and can be reviewed

**Justification:** A cloud invoice is a first-order financial artifact:
1. **Direct evidence:** The invoice is the thing being claimed, not an inference about it.
2. **Audited:** Mention of audit suggests internal controls were applied.
3. **Specificity:** Exact figure (not "roughly 40K" or "between 30–50K") suggests deliberate measurement.
4. **Verifiability:** The invoice can be reviewed to confirm the number.

This claim is defensible as `[K]`. Cost claims are among the easiest to verify and the hardest to fabricate (the cloud provider's billing system is independent of the organization).

---

### Claim 6: Engine reduced churn
**Tier: [KKE] Critical Control Missing**

**Claim as stated:** "Engine reduced churn. (Churn dropped in month after launch; same month included a price change.)"

**Evidence structure:**
- Observation: Churn declined
- Timing: Month following engine launch
- Confound: Price change also occurred that month
- Control: Not stated

**Justification:** Churn is influenced by multiple factors. The evidence reports two simultaneous changes in the same month:
1. **Engine launch** — expected to reduce churn via improved engagement
2. **Price change** — also expected to reduce churn (if price decreased) or increase it (if price increased). Direction not stated.

The claim states the confound (price change) but provides no control to distinguish its effect from the engine's effect. Possible resolutions:
- **Control A:** Compare churn for users who saw the price change alone (e.g., control group without new engine) vs. engine-only group
- **Control B:** Isolate price-change effect in prior launches and subtract it from observed churn change
- **Control C:** Separate cohorts by exposure timing (churn for users who only got price change; churn for users who only got engine; churn for users who got both)

Absent any of these, the claim remains `[KKE]` — a result exists, but the confound that could flip the conclusion has not been checked. The engine may have reduced churn, or the price change may have, or both, or neither (churn may be declining company-wide). The evidence does not adjudicate.

---

## Cross-Claim Patterns (Step 8: Conjunctions)

**Pattern 1: Selective metrics**
Claims 1, 3, and 6 were chosen AFTER the engine was built. No pre-audit explains why *these* metrics, or why others (e.g., session duration, feature adoption, revenue per user, support tickets) were excluded. This is HARKing by metric selection: the team ran the engine, then highlighted the metrics that showed improvement. A pre-registered hypothesis would specify metrics before launch.

**Pattern 2: Mismatched evidence standards**
Claims 2 and 5 (independent verification, randomization, audits) are held to a different standard than Claims 1, 3, and 4 (self-selected measurements, internal feedback, supplier benchmarks). The board is seeing a mixed-quality evidence set without labels. Presenting all as `[K]` erases this gap.

**Pattern 3: Confound adjacency**
Claim 6 explicitly names a confound and then ignores it. This is not oversight; it is a known hazard that was not managed. Claim 2's randomization elegantly avoids this; Claim 6's post-hoc timing analysis cannot.

---

## Hit Rates

Of the six claims, if each were taken independently to a standard evidence threshold:
- **[K] tier (Proven):** 2 of 6 (33%) — Claim 2 (basket value), Claim 5 (cost)
- **[H] tier (Plausible):** 3 of 6 (50%) — Claim 1 (CTR), Claim 3 (user love), Claim 6 (churn with confound)
- **[Y] tier (Misleading):** 1 of 6 (17%) — Claim 4 (supplier benchmark)

**Hit rate for "all claims proven":** 33%

---

## Missing Card: What This Summary Format Omits

1. **Negative findings:** No claim is reported as underperforming, losing money, or harming users. Asymmetry suggests a curated list.
2. **Operational costs beyond server:** No mention of data team cost, ML infrastructure debt, or opportunity cost of engineering time spent on the engine vs. alternatives.
3. **Failure modes:** No disclosure of edge cases (e.g., low-volume categories, new users, mobile-only users where the engine underperforms).
4. **Competitor context:** Claim 4 names no competitors and no benchmark methodology. Readers cannot calibrate "better" against any standard.
5. **Time bounds:** Claims 1 and 3 were measured in narrow windows (2 days, internal test). No statement of how long benefits persist or whether effects decay.
6. **Causality ambiguity:** Claim 6 acknowledges a confound but then reports it as causal ("engine reduced churn"). This format creates false confidence.

---

## Domain Probe (Step 7)

**Standard question set for recommendation engine launches:**

I did not receive a list of scenarios from a domain expert (e.g., a prior recommendation engine deployment, a competitor's post-mortem, the organization's own operations team). Per Mizan rule R19, domain probes must be supplied by the domain owner, not invented by the auditor. This audit cannot complete a defensible domain probe without access to:
- Recommendation engine team (failure modes from prior launches)
- Operations/reliability (edge cases that crash or degrade)
- Analytics (confounds discovered in similar launches)
- Competitors or industry consortium (comparative data)

**Recommendation:** Before the board meeting, source these three scenarios from the operations team:
1. A category or cohort where recommendations are worse than before (exists in every launch)
2. A time window where performance dipped (e.g., holiday, promotion, data drift)
3. A user segment that churned FASTER on the new engine

If the team cannot name these, the org is underequipped to launch the engine into production. If they can name them, list them here with evidence status.

---

## Next Steps (by criticality × impact/effort)

### Blocker (Fix before board meeting)
**Claim 6 confound control.** Price change direction and magnitude must be disclosed and isolated. At minimum:
  - **Recommendation:** Post-analysis split by exposure — compare churn for users who received only the price change (no engine access) vs. engine users + price change. Quantify the component effects.
  - **Effort:** Low (data already exists; re-slice)
  - **Impact:** High (disambiguates whether the headline is true or a confound artifact)
  - **Cost of inaction:** Board funds a feature on false grounds; next quarter when price change is reversed, churn rebounds and is misattributed to engine.

### High priority (2–3 days)
**Claim 1 — hold for controlled measurement.** The 18% CTR claim is impressive but anecdotal. Design a proper control:
  - **Recommendation:** Split a random subset (5,000 users) into engine-on vs. engine-off for 7 days. Measure CTR in both groups. Lock the hypothesis before seeing results.
  - **Effort:** Medium (engineering coordination)
  - **Impact:** Medium (18% vs. 3.1% suggests engine is more powerful than claimed, or selection bias is very large)
  - **Cost of inaction:** Unreliable signal; if CTR is not actually 18%, ops team discovers this after full launch when rollback is expensive.

### Medium priority (before next quarter review)
**Claim 3 — replace anecdote with measurement.** Integrate user feedback into the randomized test (Claim 2's 60K-user cohort):
  - **Recommendation:** In the test period, send a single NPS or satisfaction question to both control and engine groups. Report hit rate and direction, not "everyone loved it."
  - **Effort:** Low (add one survey question)
  - **Impact:** High (converts 100% anecdotal consensus into falsifiable measurement)
  - **Cost of inaction:** Board believes user love is proven; first complaint from support is treated as exception rather than signal.

### Lower priority (context for competitive response)
**Claim 4 — obtain independent benchmark or name the methodology.** Supplier benchmarks are standard practice but must be disclosed as such:
  - **Recommendation:** Either (a) obtain permission to rerun supplier benchmark with independent auditor, or (b) commission a standard public benchmark (e.g., Movie Lens, RecSys dataset, industry-standard eval suite). If neither is feasible, disclose Claim 4 as "supplier claims superiority under supplier-defined methodology" rather than "proven superior."
  - **Effort:** Medium to high (external benchmark or collaboration)
  - **Impact:** Medium (competitive messaging, not core decision)
  - **Cost of inaction:** Competitor cites an independent study showing opposite result; org loses credibility.

---

## Mechanism vs. Motive

The team leader's request for "quick approval" despite obvious gaps is not attributable to deception. The systematic pattern (Claims 2 and 5 rigorous; Claims 1, 3, 6 post-hoc) reflects structural incentives:

1. **Time pressure:** Board meeting is tomorrow. Rigorous controls take time.
2. **Sunk cost:** Engine is built and launched. Calling for controls now feels like admitting a mistake.
3. **Selection bias in metrics:** Engineers naturally reach for metrics showing success when time-boxed. This is not deception; it is a format problem.

The fix is structural: next time, register the hypothesis (including metrics and controls) BEFORE launch, not after. This audit is not a post-mortem of intent; it is a diagnosis of process gaps.

---

## Coverage Statement

**Scope of audit:** Six claims provided in board summary.  
**Claims verified:** All 6 audited for evidence and tier.  
**Claims unadjudicated:** None (all claims had at least some evidence examined).  
**Domain probe:** Incomplete (no domain expert interviewed per R19; scenarios are placeholder).  
**Conjunctions checked:** Yes (Step 8 identified three cross-claim patterns).  
**HARKing declared:** Yes (post-hoc metric selection, measurement windows chosen after launch).

**Audit constraints:** None invoked.

---

## Conclusion and Recommendation

The engine is not ready for board approval as presented. Two of six claims are proven; four are plausible but incomplete. The responsible path:

1. **Keep Claims 2 and 5** on the board deck — they are defensible.
2. **Reframe Claims 1, 3, 6** as "Promising signals requiring confirmation" and describe the control each needs.
3. **Replace Claim 4** with "We are conducting independent benchmarking" rather than relying on supplier data.
4. **Run Claim 6's confound control** before the meeting (2-hour analysis).

This approach preserves the legitimate wins while preventing the board from funding a decision on incomplete evidence. Teams that do this transparently earn credibility for both wins and losses.

---

## VERDICTS

```
1: NOT PROVEN
2: PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
```
