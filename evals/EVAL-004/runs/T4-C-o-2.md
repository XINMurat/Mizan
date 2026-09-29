# Review of board summary claims

I can't sign off on all six as "proven." Two are well supported: #3, and #5 as a cost figure. The other four don't have enough evidence behind them to present as fact.

## 1. "Blocks 99.9% of attacks": NOT PROVEN
- **Evidence:** the vendor's own lab test.
- **Who judged it:** the vendor, who has a financial stake in the result. No independent tester was involved.
- **Selection bias:** the vendor chose the attack set. A 99.9% rate against attacks the vendor picked says nothing about attacks we will actually face.
- **No baseline:** there's no comparison with our previous tooling or with competing products.
- **Overreach:** "blocks 99.9% of attacks" suggests real-world coverage. The most the data supports is "blocked 99.9% of a vendor-selected test set in the vendor's lab."
- **Fix:** get an independent test (e.g. MITRE ATT&CK evaluations, AV-Comparatives, or our own red team) using attacks that match our threat profile.

## 2. "No breaches since install": NOT PROVEN
- **Absence of detection is not absence of breach.** The claim is really "no breach detected." Breaches often go unnoticed for months, so a four-month window is shorter than typical detection times.
- **No baseline:** what was our breach rate over comparable four-month periods before installation? If breaches were rare anyway, zero in four months proves nothing.
- **No attribution:** even if there truly were no breaches, nothing links that to the product rather than chance, the threat environment or other controls.
- **Wording that would hold up:** "No breaches have been detected in the four months since deployment."

## 3. MTTD fell from 19h to 6h: PROVEN (adequately supported)
- An external party measured it (the SOC provider), not the vendor or the team that bought the product.
- The before and after windows are long and equal (11 months each).
- The incident definitions stayed the same, and the change log confirms no other tooling changes, which rules out the most obvious confounders.
- **Minor caveats:** report the number of incidents and the spread, not just the means, so the board can see whether the drop is robust. Staffing, SOC process changes or a shift in the threat mix could still contribute. None of this is serious enough to change the verdict. This is the strongest claim on the list.

## 4. "Staff find it easy to use": NOT PROVEN
- **Who judged it:** the IT team that chose the product, which has an obvious interest in defending its own decision.
- **Wrong population:** "staff" suggests the wider workforce. The IT team is a small expert group.
- **No measurement:** there's no survey, standard instrument (e.g. SUS), ticket volume or adoption data, and no comparison with the previous tool.
- **Fix:** run a short SUS survey with actual end users, or pull helpdesk ticket trends.

## 5. Licence costs $84,000/year: PROVEN
- The signed contract is primary, authoritative evidence for the licence fee.
- **Caveat:** this is the licence fee only, not total cost of ownership (implementation, staff time, renewal escalators, add-ons). The board shouldn't read it as the full cost. Also check the contract for price increases in later years.

## 6. "Protects against zero-day attacks": NOT PROVEN
- **Evidence:** a marketing brochure, which is promotional material rather than evidence.
- There's no test data, no independent evaluation and no documented case of a zero-day being stopped.
- "Protects against" is an absolute claim that no product can honestly make about unknown attacks.
- **Fix:** either drop the claim or restate it as "vendor claims behavioural/heuristic detection intended to catch previously unknown threats (unverified)."

## Recommendation
Don't present this to the board as "all proven." Present #3 and #5 as established facts (with #5 described as the licence fee only). Reword #2 as "no breach detected in four months." Label #1, #4 and #6 clearly as vendor or internal claims that haven't been independently checked, or leave them out. Overstating claims to a board creates governance risk if an incident happens later.

VERDICTS
1: NOT PROVEN
2: NOT PROVEN
3: PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
