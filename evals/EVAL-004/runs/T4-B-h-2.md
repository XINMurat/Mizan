# Security Product Claims — Audit Report

**Date:** 2026-09-29  
**Target:** Board summary — six claims about internal security product  
**Audit mode:** Retrospective  
**HARKing status:** This review is retrospective; all examples and counter-examples are drawn after the outcomes were known.

---

## Summary

Of the six claims presented for board sign-off, **one survives scrutiny as proven, and five do not.** The team lead's confidence reflects standard selection effects in vendor-supplied claims and uncontrolled timelines. Claim 3 (MTTR measurement) would be proven if its supporting evidence were provided; the others face structural barriers to verification.

---

## Claim-by-claim audit

### Claim 1: The product blocks 99.9% of attacks.

**Evidence cited:** Vendor's own lab test; the attack set was chosen by the vendor.

**Tier:** `[Y]` — Misleading

**Justification:** This exemplifies the Mizan anti-pattern (rule 6): curated examples trump measurement records. The vendor chose both the tool being tested and the test set itself, eliminating any selection pressure that would penalize undisclosed failure modes. A 99.9% figure in a vendor-controlled lab tells us only that the vendor can construct a test the vendor's own product passes; it tells us nothing about real-world performance. No scored prediction record exists here—only a marketing result. The claim should be demoted from any tier suggesting confidence.

**Next step:** Request attack records from your own SOC or an independent penetration test against the same product using attacks drawn from *your* actual threat landscape, not a vendor-chosen set.

---

### Claim 2: We have had no breaches since we installed it (four months; no breach detected).

**Evidence cited:** Four-month timeline without detected breach.

**Tier:** `[KKE]` — Critical control missing

**Justification:** This is a surprising positive (no breach when one might have occurred), and rule 5 of the Mizan methodology requires a symmetric control before promotion. The claim conflates "no breach detected" with "no breach occurred," which are not the same. More critically, it lacks the confound check: *would we have had zero breaches in the same four-month period under the old system, or with any other product?* Without a control comparing breach rates before the product to breach rates after, the absence of events is information-free. Four months is also a short observation window for a rare event; absence alone cannot settle the claim at `[K]`.

**Next step:** Reconstruct breach rates (per unit time) for the 12 months before installation and the 4 months after. Compare them formally, accounting for seasonal and organizational changes. If the prior rate was already near zero, the four-month window proves nothing.

---

### Claim 3: Mean time to detect fell from 19 to 6 hours, measured by the external SOC provider over 11 months before and 11 after, with the same incident definitions and no other tooling change.

**Evidence cited:** Change log (attached, not provided to auditor).

**Tier:** `[H]` — Plausible hypothesis (cannot be elevated to `[K]` without the attached evidence)

**Justification:** The structure of this claim is sound. External measurement (not vendor-supplied), long observation windows (11 months each), consistent definitions, and a documented assumption about confounds (no other tooling change). If the attached change log is verified, this claim is provable. However, the critical supporting evidence—the change log itself—was not provided to this audit. Without it, the claim "no other tooling change" is an assertion, not a verified fact. Mizan rule 9 on thresholds requires that the arbiter (here, the change log as documentation) be named and accessible. The claim is well-formed and plausible, but incomplete.

**Next step:** Produce the change log. Verify that no other security tooling was added, upgraded, or reconfigured in the 11-month baseline or deployment window. If that check passes, this claim moves to `[K]`.

---

### Claim 4: Staff find it easy to use.

**Evidence cited:** The IT team that chose it says so.

**Tier:** `[Y]` — Misleading

**Justification:** The claim implies broad staff satisfaction, but the evidence is from a single group with clear incentive to justify their own choice (sunk cost bias, confirmation bias). This is survivorship bias: you heard only from people who kept the product, not from any who abandoned it or felt burdened by it. No metric exists—no help desk call volume, no adoption rate, no task-completion time, no voluntary-use measure. A subjective sentiment from the decision-makers is not evidence for the organization.

**Next step:** If "easy to use" is material to the board decision, measure it: track help desk tickets before and after, run a blind usability test with a control group using the old workflow, or survey all staff (not just IT) who interact with it.

---

### Claim 5: The licence costs $84,000 a year.

**Evidence cited:** Signed contract.

**Tier:** `[K]` — Proven

**Justification:** A signed contract is a first-order factual record. This claim is verifiable and, if the contract exists, true as stated. No ambiguity in the measurement or confounds that could hide a cost.

---

### Claim 6: It protects against zero-day attacks.

**Evidence cited:** Marketing brochure.

**Tier:** `[S]` — Speculative

**Justification:** A zero-day is, by definition, an attack unknown at the time of testing. No vendor can test against unknown attacks. This claim is unanchored—there is no refutation condition and no conceivable way to verify it before a zero-day is publicly disclosed (at which point it is no longer a zero-day). A marketing brochure stating an unfalsifiable claim is not evidence; it is marketing. The claim belongs at `[S]` because it cannot be meaningfully tested in the present.

**Next step:** Ask what the vendor means: Do they use a zero-day *emulation* (simulated attacks that resemble unknown ones)? If so, name that test. Otherwise, treat this as an aspirational claim ("our product is designed against unknown attacks") rather than one that meets a threshold.

---

## Missing card

This summary format cannot show:
- The *mechanism* by which each claim fails (selection bias vs. uncontrolled timeline vs. missing evidence).
- Whether the product is actually *bad*, or only *unproven* — a claim marked `[H]` or `[Y]` may be true, but the evidence does not yet settle it.
- The organizational context: What was the prior system? What breach rate or MTTR was tolerable? Against what threat model are these claims being judged?

---

## VERDICTS

```
1: NOT PROVEN
2: NOT PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
```

---

## Recommendation

**Do not sign off these claims to the board.** Of six statements, five either lack evidence or are structured to mislead. One (claim 5, cost) is verified. The board needs:

1. **Claim 3** — provide the change log to settle MTTR, or demote to `[H]`.
2. **Claims 1, 2** — reframe from "proven" to "plausible; further measurement needed."
3. **Claim 4** — replace with actual usability data, or remove from the board deck.
4. **Claim 6** — remove, or reframe as "the vendor claims zero-day protection" (let the board decide whether vendor claims count as evidence).

The team lead's confidence is understandable — all six claims *could* be true — but confidence is not evidence, and three of them actively invite board members to rely on curated vendor tests and uncontrolled timelines. Mizan exists to catch exactly this pattern.
