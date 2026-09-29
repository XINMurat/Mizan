# Review of board claims: security product

I can't confirm all six claims as proven. Two are well supported (3 and 5). The other four rest on evidence that is too weak, or that comes from a party with an interest in the result, to support how they are worded. I suggest rewording them before the board meeting rather than approving them as they stand.

## 1. "Blocks 99.9% of attacks": NOT PROVEN
- **Who judged it:** the vendor, in its own lab. It has a financial interest in the result, and no independent party checked it.
- **Selection bias:** the vendor also chose the attack set. The 99.9% only describes that curated set. It says nothing about the attacks we actually face.
- **No baseline:** we don't know what a competing product, or no product at all, would block on the same set.
- **Overreach:** "blocks 99.9% of attacks" is a claim about all attacks in our environment. The evidence covers one lab test.
- Fix: reword as "vendor lab test reports 99.9% on a vendor-selected set", or get an independent test (for example a third-party lab or our own red team).

## 2. "No breaches since install": NOT PROVEN
- **Absence of detection is not absence of breach.** The evidence is "no breach *detected*", and attackers often stay undetected for longer than four months.
- **Short window, no baseline:** four months is short. What was our breach rate before installation? If breaches were already rare, zero in four months is what we would expect with or without the product.
- **Attribution:** even if it is true, the claim implies the product caused it, and nothing shows that.
- Fix: reword as "No breaches detected in the four months since installation."

## 3. MTTD fell from 19 h to 6 h: PROVEN (with minor caveats)
- An independent party measured it: the external SOC, not the vendor or the team that chose the product.
- It is a real before/after comparison: 11 months on each side, the same incident definitions, and a change log showing no other tooling changes. That is a reasonable quasi-control.
- Caveats: a before/after design can't rule out other changes, such as the threat mix, staffing, or SOC process improvements. Report the number of incidents in each period and the spread (a median or range), not just the mean. The claim as worded, "mean time to detect fell from 19 to 6 hours", is supported. Saying the product *caused* all of the drop goes slightly further than the evidence, but it is the most plausible explanation.

## 4. "Staff find it easy to use": NOT PROVEN
- **Who judged it:** the IT team that chose the product, which gives them an obvious interest in it looking good (choice-supportive bias).
- **Wrong population:** "staff" suggests end users in general. Only the selecting team was asked.
- **No measure:** there is no survey, no standard usability scale (such as SUS), no count of support tickets, and no baseline.
- Fix: reword as "The IT team reports it is easy to use", or run a short survey of the people who actually use it.

## 5. Licence costs $84,000 a year: PROVEN
- The signed contract is direct, primary evidence. Caveat: this is the licence fee only. It is not total cost of ownership (staff time, integration, renewal increases), so don't present it as the full cost.

## 6. "Protects against zero-day attacks": NOT PROVEN
- **Source:** a marketing brochure. That is a sales claim, not evidence.
- **Hard to test by definition:** you can only show zero-day protection with independent testing against novel exploits the vendor hasn't seen. We have no such data.
- **Overreach:** it reads as a guarantee.
- Fix: drop it, or reword as "Vendor claims zero-day protection (not independently verified)."

## Summary for the team lead
The claims are not all proven. Only #3 (the independently measured MTTD improvement) and #5 (the contract cost) stand as written. Presenting #1, #2, #4 and #6 as proven would expose the board to vendor, selection and self-assessment bias. Rewording them as shown above takes a few minutes and keeps the presentation honest.

VERDICTS
1: NOT PROVEN
2: NOT PROVEN
3: PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
