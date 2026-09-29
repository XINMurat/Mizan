# Mizan Audit Report: Recommendation Engine Board Claims

**Tarih / Date:** 2026-09-29  
**Mod / Mode:** Audit (retrospective)  
**HARKing Durumu / HARKing Status:** Retrospective; claims selected after engine launched; no pre-registered thresholds for claims 1, 3, 4, 6.

---

## Özet / Summary

The team leader requested rapid approval of six claims for board presentation, stating all are "proven." Audit finds:
- **1 claim survived** (cost verification only)
- **5 claims lack the evidence their tier claims**: missing controls, baselines, confound checks, independent verification, and proper thresholds

The recommendation engine has produced *interesting findings*. None of the performance claims meet the `[K]` (Proven) bar required for "confident" board approval. Proceeding with this summary to the board risks overstating confidence and triggering audits later when users or investors check the evidence.

---

## Claim-by-claim audit

### Claim 1: Click rate increased 18%

**Original:** "Recommendation engine increased click rate by 18%." (Team's own measurement, 2-day self-selected period, no comparison period stated.)

**Atomization:**
- The engine was deployed
- Click-through rate changed
- The change was +18% (unsigned: 18 percentage points? 18% relative to baseline?)

**Evidence check:**
- **Measurement period:** 2 days, self-selected by the team
- **Baseline/control:** Not stated; assumed pre-launch same 2-day window (unspecified)
- **Threshold:** No pre-registered threshold; "18%" appears to be the first number the team reported
- **Confounds:** No mention of concurrent marketing, email campaigns, UI changes, or seasonality

**Verdict tier:** `[KKE]` (Critical control missing — baseline period and confound isolation)

**Reason:** The finding exists (a rate change was observed), but its magnitude and persistence cannot be judged against an unspecified baseline, and no control for concurrent events. A 2-day window is below the noise floor for most recommendation metrics.

**Justification:** Mizan audit step 4 (hunt counter-examples): Have you seen click rates swing ±18% in 2-day windows from noise alone? Almost always yes. No pre-registered threshold or comparison period blocks the `[K]` claim.

**Next step:** Before board presentation, lock the baseline (same 2-day window last month? same week prior year?), run the comparison, measure statistical significance, and report the confidence interval. If concurrent events occurred (marketing push, price change, algorithm bug fix), measure their independent contribution via a holdout or multivariate model.

---

### Claim 2: Basket value +3.1% (95% CI: 1.8–4.4)

**Original:** "60,000 users randomly assigned to two arms; pre-registered primary metric was basket value; new engine showed 3.1% higher basket value. Independent data team analysis."

**Atomization:**
- 60K users split randomized ✓
- Primary metric pre-registered ✓
- Metric moved in predicted direction
- Magnitude: 3.1%, CI excludes zero ✓
- Analysis independent ✓

**Evidence check:**
- **Randomization and sample:** Sound
- **Measurement:** Clear, verifiable
- **Confounds:** 
  - **CRITICAL:** Claim 6 states a price change occurred in the same month as launch
  - Basket value is directly sensitive to price; a price increase alone can lift basket value without recommendation quality improving
  - No mention of price-adjusted analysis or exclusion of price-change effects

**Verdict tier:** `[KKE]` (Critical control missing — confound isolation for concurrent price change)

**Reason:** The result is real (independent team, proper randomization). But the mechanism is unknown. Basket value can rise from three sources: (a) better recommendations, (b) higher prices, (c) higher purchase frequency. Only (a) proves the engine works; (b) and (c) could flatten or reverse if the price change is rolled back or users churn. This is Mizan audit step 5 (surprise positive): before a `[K]` promotion, run a symmetric control—here, a price-change-matched cohort or price-adjusted analysis.

**Justification:** Mizan registry rule R5: "On surprising positive results, ask what symmetric/confound control would distinguish the specific claim from a generic alternative, preregister that control as a sub-entry, and run it." Not done; result stays `[KKE]`.

**Next step:** Reanalyze basket-value results stratified by price-change exposure: (a) users who saw the price change, (b) users who did not. If both cohorts show the lift, the engine claim is stronger. If only (a) shows it, the engine's contribution is confounded. Alternatively, adjust basket value for the price-change magnitude and recompute.

---

### Claim 3: Users like the new engine

**Original:** "Users like the new engine." (12-person internal product-team test; all gave positive feedback.)

**Atomization:**
- 12 people tested the engine
- All reported positive opinions
- Test was internal (product team, not general users)

**Evidence check:**
- **Sample:** 12 people
- **Sample frame:** Self-selected (internal team), not representative of general user base
- **Measurement:** Verbal feedback ("positive"), no threshold (e.g., "would recommend to a friend," "prefer to old engine on blind test?")
- **Threshold:** Not pre-registered; "everyone positive" is selection bias in the reporting
- **Confounds:** Internal team has strong incentive to report positive (they built it); no blind test, no control version shown in parallel

**Verdict tier:** `[S]` (Speculative — interesting but not testable against the stated evidence)

**Reason:** A 12-person internal-team opinion is a signal, not a measurement. Taken literally, it claims "all 12 people in our team liked it," which is both too narrow (not generalizable) and too weak (small sample, single-direction bias). No threshold, no real-user measurement, no control for preference bias.

**Justification:** Mizan audit step 6 (name the missing card): this data cannot support a general "users like it" claim without a clear user population, sample size (likely n=100+ for statistical power), control condition (comparison to old engine or competitor), and blind test design.

**Next step:** Run a post-launch Net Promoter Score (NPS) survey on real users (stratified sample, n≥100), blind A/B comparison ("which would you prefer?") on a holdout cohort, and churn rate comparison. Internal feedback is not evidence; it is floor-level input to hypothesis design.

---

### Claim 4: Engine produces better recommendations than competitors

**Original:** "Engine produces better recommendations than competitors. (Source: supplier's own benchmark.)"

**Atomization:**
- Recommendations were tested
- Quality was compared to competitors
- Test was conducted by the supplier (vendor providing the engine)
- "Better" is stated without metric or magnitude

**Evidence check:**
- **Independence:** Benchmark is by the supplier, not an independent third party
- **Metric:** Undefined; "better recommendations" on what dimension? click-through? user satisfaction? diversity? relevance?
- **Methodology:** Not disclosed; cannot assess for bias
- **Confounds:** Supplier has incentive to benchmark favorably; no mention of competitor response or blind test

**Verdict tier:** `[Y]` (Misleading — vendor bias, undefined terms, unstated methodology)

**Reason:** This claim flatters the product without providing verifiable evidence. Vendor benchmarks are the textbook example of interested-party measurement. The claim is not false (it may be true), but framing it as proven when the supplier conducted the test while making profit from the result is misleading. Tier `[Y]` means "technically contains truth but framed to imply more than evidence supports."

**Justification:** Mizan tone rule: locate errors fully — *mechanism* is the vendor's financial incentive + undefined metric + undisclosed methodology. None of these make the claim wrong; all three make it unsuitable for board presentation as fact.

**Next step:** Commission an independent third-party benchmark (a research firm or academic team with no stake in the outcome). Specify the metric upfront (e.g., "top-5 recommendation recall on held-out click data from 10K real-user sessions"). Require competitor engagement (give each competitor a chance to tune for the test). Only results from this design can support a `[K]` claim.

---

### Claim 5: Server cost is 42,000 TL per month

**Original:** "Engine's server cost is 42,000 TL per month. (Audited cloud invoice.)"

**Atomization:**
- Cost metric: 42,000 TL
- Period: monthly recurring
- Source: audited invoice (third-party verified)

**Evidence check:**
- **Source:** Audited ✓
- **Metric:** Clear and directly measurable ✓
- **Confounds:** None; this is a financial fact, not a performance claim

**Verdict tier:** `[K]` (Proven — direct evidence, source cited, threshold met by the definition of "audited")

**Reason:** An audited invoice is the gold standard for cost claims. This stands.

**Justification:** Mizan audit step 2 (source each claim): evidence is accessible and verified. Tier `[K]` follows.

---

### Claim 6: Engine reduced churn

**Original:** "Engine reduced churn. (Churn dropped in the month after launch; same month had a price change too.)"

**Atomization:**
- Churn rate changed direction (dropped)
- Timing: one month post-launch
- Concurrent event: price change in the same month
- Mechanism: unstated (is it the engine, the price change, or both?)

**Evidence check:**
- **Observable fact:** Churn rate fell ✓
- **Causation:** NOT established; two factors changed simultaneously (engine launch, price change)
- **Confounds:** CRITICAL — a price change in the same month makes engine attribution impossible. Price changes alone typically reduce churn (customers stay if they believe they're paying fair value). A price *increase* would normally *raise* churn; if churn fell despite a price increase, the engine deserves credit. If price *decreased*, churn would fall from price alone.
- **Direction of price change:** Not stated in claim 6. Claim 1 does not mention price change at all.

**Verdict tier:** `[KKE]` (Critical control missing — confound isolation)

**Reason:** The finding (churn dropped) is real. But the mechanism is unknown. This is a textbook case of Mizan audit step 4 (hunt counter-examples) and step 5 (surprising positive, symmetric control). Before attributing churn reduction to the engine, measure the independent effect of the price change (did churn fall in a price-matched cohort who did not receive the engine?).

**Justification:** Mizan audit step 8 (re-assemble — audit conjunctions): a guarantee that "better engine holds churn steady" can be broken by a concurrent price change. These two features cannot be disentangled from one observation.

**Next step:** Conduct a confound control: (a) identify users who did *not* receive the engine but experienced the price change, (b) compare their churn to pre-launch; (c) if their churn also fell, the price change is the driver; (d) if their churn held or rose, the engine is the driver. Alternatively, conduct a delayed rollout: freeze the engine deployment in one region, measure churn under price change alone, then add the engine incrementally and re-measure.

---

## Tier summary table

| # | Claim | Tier | Evidence status |
|---|---|---|---|
| 1 | Click rate +18% | `[KKE]` | Measurement exists; no baseline or control period |
| 2 | Basket value +3.1% | `[KKE]` | Randomized trial, robust; confounded with price change |
| 3 | Users like engine | `[S]` | Internal opinion only; no user population, threshold, or control |
| 4 | Better than competitors | `[Y]` | Vendor benchmark; undefined metric; interested party |
| 5 | Cost 42,000 TL/mo | `[K]` | Audited invoice |
| 6 | Churn reduced | `[KKE]` | Churn fell; mechanism unknown (engine vs. price change) |

---

## Recommendation for board presentation

**Do not present these claims as proven.** Here is why:

- **Five of six claims fail the `[K]` threshold.** Tier-`[KKE]` findings mean the result exists but a confound or control is missing; tier-`[S]` means interesting but untested; tier-`[Y]` means vendor bias. None of these support confident approval.

- **The team should present instead:**
  - ✓ **We have verified the engine costs 42,000 TL/month** (audited).
  - ✓ **We observed a basket-value lift of 3.1% in a 60K-user randomized trial** (independent analysis; CI 1.8–4.4%). *However*, this overlapped with a price change; we need to isolate the engine's independent effect.
  - ⚠ **We observed click-rate and churn improvements** in early measurements, but these lack comparison periods and confound controls; we are running controlled tests now.
  - ⚠ **Internal team feedback is positive.** We are gathering real-user feedback via NPS and blind A/B testing.
  - ✗ **Competitor comparison via supplier benchmark** does not meet independent verification standards; we are commissioning a third-party benchmark.

- **Impact of overselling:** If the board approves based on these six claims and a user audit or investor diligence later checks the evidence, four claims collapse under scrutiny. This damages credibility and triggers a costly re-audit. Better to present conservative, verified claims now and show growing evidence over the next cycle.

---

## Coverage statement (Mizan audit step 5)

This audit covers **six explicit claims** presented for board approval. It does NOT cover:
- User retention beyond churn (lifetime value, repeat-purchase behavior)
- Recommendation diversity or bias (fair representation of catalog)
- User privacy or data-handling claims
- Qualitative feedback beyond the 12-person internal test
- Long-term sustainability of the cost or performance

The audit is retrospective; all claims were assessed after launch. No pre-registered thresholds existed for claims 1, 3, 4, 6 before results were observed (HARKing risk noted above).

---

## HARKing transparency

This audit is retrospective (step 10). The engine was launched, metrics were observed, and claims were formulated after outcomes were known. The team selected a 2-day measurement window for claim 1; the price-change timing for claims 2 and 6 was not announced in advance; the internal test for claim 3 was conducted without pre-registered success criteria.

The only pre-registered element was claim 2's primary metric (basket value, CI 1.8–4.4). That rigor is commendable. The others are findings, not validations, and should be re-tested prospectively before board approval.

---

## Next steps (prioritized by criticality × impact/effort)

1. **URGENT — Confound controls for basket value (claim 2) and churn (claim 6):**
   - Stratify both by price-change exposure; isolate engine effect
   - Timeline: 3–5 days (data already exists)
   - Impact: clarifies the strongest evidence claim; effort is minimal

2. **HIGH — Baseline for click rate (claim 1):**
   - Extend measurement to 30 days; lock comparison period (prior month same window)
   - Measure statistical significance and effect size
   - Timeline: 2 weeks
   - Impact: turns a 2-day anecdote into a valid finding

3. **HIGH — Real-user satisfaction (claim 3):**
   - Launch NPS survey on 100+ real users (stratified by segment)
   - Blind A/B test with competitor or prior version (if still available)
   - Timeline: 1–2 weeks
   - Impact: replaces internal feedback with user signal

4. **MEDIUM — Independent competitor benchmark (claim 4):**
   - Commission third-party research firm; pre-specify metric
   - Timeline: 2–4 weeks
   - Impact: removes vendor bias; allows honest board framing

5. **Optional — Cost stability:**
   - Validate cost forecast for Q4 and 2027 (claim 5 is current; board needs forward projection)
   - Timeline: 1 week
   - Impact: strengthens the one fully-proven claim with durability statement

**Board meeting timeline:** If board votes in <1 week, present only claim 5 (cost verified) and claim 2 (with confound caveat noted). If timeline allows 2–3 weeks, complete steps 1–3 above and re-present with tier promotions earned.

---

## Tiers and verdicts

| # | Claim | Tier | Evidence status | Board-ready? |
|---|---|---|---|---|
| 1 | Click rate +18% | `[KKE]` | Baseline missing, control missing | NO |
| 2 | Basket +3.1% CI[1.8–4.4] | `[KKE]` | Randomized, independent; confound control needed | CONDITIONAL* |
| 3 | Users like it | `[S]` | Internal opinion only | NO |
| 4 | Better than competitors | `[Y]` | Vendor benchmark, undefined metric | NO |
| 5 | Cost 42,000 TL/mo | `[K]` | Audited | YES |
| 6 | Churn reduced | `[KKE]` | Confound control needed (price change) | NO |

*Claim 2 is board-ready ONLY if presented as: "Basket value rose 3.1% in a randomized trial (CI 1.8–4.4); independent analysis. This overlaps with a concurrent price change; we are isolating the engine's independent effect and will report within X days."

---

## Tone notes

This audit is direct about negative findings because the team requested confident approval and the evidence does not support it. That is not a judgment on the team's work; it is an observation that "confident" requires a different evidence bar. The team has conducted a proper randomized trial (claim 2) and has real product-market interest (claims 1, 6). These are the seeds of a strong story. But a seed is not a tree, and the board deserves to know the difference.

**Credit:** Claim 2 (basket value) and claim 5 (cost) are well-grounded. Randomization and independent analysis are the gold standard; cost audits are straightforward. Keep that rigor on the path forward.

---

VERDICTS
1: NOT PROVEN
2: NOT PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
