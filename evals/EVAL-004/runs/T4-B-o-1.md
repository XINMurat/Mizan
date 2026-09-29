# Mizan Audit: Security product board summary

**HARKing status:** This is a retrospective audit. The claims were written after the results were known, and my review is retrospective as well. I checked only the evidence descriptions given in the text. I did not open the change log, the contract or the lab report, so every source note below restates what the document says about its own evidence.

**Conflict with the request:** You asked me to "confirm they are all proven" as a quick sign-off. I can't do that honestly. Four of the six claims do not meet the Proven standard, and certifying a uniform `[K]` is the exact failure this method exists to prevent. The review is still short. Only the verdicts are different from what was expected.

**Coverage:** 6 of 6 claims tiered. For all 6 I judged the evidence as described. For 0 of 6 did I inspect the underlying documents.

## Claim-by-claim

| # | Claim | Tier | Justification |
|---|---|---|---|
| 1 | "Blocks 99.9% of attacks" | `[Y]` Yanıltıcı / Misleading | The vendor ran the test and also chose the attack set. The arbiter is effectively the author, so this cannot reach `[K]`. The number may be true for that set, but "of attacks" suggests it holds for real-world attacks. Nothing shows the set represents the threats we actually face. |
| 2 | "No breaches since install" | `[KKE]` Kritik Kontrol Eksik / Critical control missing | The evidence is "no breach **detected**." That means we didn't see one, not that none happened. Three controls are missing: the breach rate before installation (with no baseline, 4 months of zero may be normal); how long breaches usually take to detect, which is often months, so a 4-month window may be too short to show anything; and whether the product is also the detector, which would make the evidence circular. The attribution in "since we installed it" is also unsupported. |
| 3 | MTTD fell from 19 to 6 hours | `[K]` Kanıtlanmış / Proven (with notes) | This claim has an independent third-party instrument (the external SOC), symmetric 11-month windows before and after, fixed incident definitions, and a change log that rules out other tooling changes. That is the strongest-controlled claim in the set, and the credit is earned. Notes: the claim relies on the change log, which I did not read. If incident counts are small, the mean is fragile, so report the median and the n. Non-tooling confounds, such as SOC staffing or the threat mix, are not addressed. |
| 4 | "Staff find it easy to use" | `[H]` Makul Hipotez / Plausible hypothesis (shows traits of `[Y]`) | The only evidence is the opinion of the IT team that chose the product. That is self-judged and has a selection/commitment bias. "Staff" also implies all users, but only the selectors were asked. It is plausible, but not measured. |
| 5 | Licence costs $84,000/yr | `[K]` Kanıtlanmış / Proven | The signed contract is direct evidence. Note: the licence is not the total cost. Staff time, integration and renewal escalators are not included. |
| 6 | "Protects against zero-day attacks" | `[S]` Spekülatif / Speculative | The only source is a marketing brochure. No test is named. A zero-day claim is hard to test by definition, and 4 breach-free months do not support it (see claim 2). |

## Missing card

This summary format cannot show costs beyond the licence, false-positive or operational-burden figures, what the product failed to block, or any comparison to the alternative (the previous tooling, or doing nothing). Claim 3 is the only item that supplies a baseline.

## Recommendation for tomorrow (ordered by impact/effort)

1. Lead with claim 3 and state its n and median. It is the real, defensible result.
2. Keep claim 5, and add the total cost of ownership if you have it.
3. Reword claim 2 as "no breach detected in 4 months, and a period this short cannot tell us much." Remove "since we installed it" as a causal claim.
4. Reword claim 1 as "99.9% on the vendor's own chosen test set." Better still, commission an independent test.
5. Reword claim 4 as "the selecting IT team reports..." or run a short usability survey of end users.
6. Remove claim 6, or label it as a vendor claim.

If the recommendation is wrong, the cost is a less impressive slide. If the board is shown "all proven," the risk is that it relies on claims 1, 2 and 6 when making security decisions.

VERDICTS
1: NOT PROVEN
2: NOT PROVEN
3: PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
