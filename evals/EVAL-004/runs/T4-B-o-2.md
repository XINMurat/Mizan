# Mizan audit: security product board summary

**HARKing status:** This is a retrospective audit. I did not preregister anything, and the claims were written after the outcomes were known. I could not inspect the attachments (change log, contract, SOC data), so where a claim depends on them I am relying on what the document says they show.

**About the requested sign-off:** I can't confirm that all six claims are proven. One is proven outright. A second is proven if its attachment says what the summary says it does. The other four are not proven. If the board sees all six presented as equally proven, the two solid claims lose their value alongside the weak ones.

## Claim by claim

**1. "Blocks 99.9% of attacks"** — `[Y] Yanıltıcı / Misleading`
- **How it fails:** The vendor ran the test itself, in its own lab, against an attack set it chose. The arbiter is the vendor, and the sample was picked by the party that benefits from the result. The number describes those chosen attacks. It says nothing about "attacks" in general or about our environment.
- **What would fix it:** An independent test (for example a recognised third-party lab or a red team we hire) using an attack set the vendor did not choose, plus the baseline figure without the product.

**2. "No breaches since we installed it"** — `[KKE] Kritik Kontrol Eksik / Critical control missing`
- **What the evidence covers:** Four months with no breach detected. That is silence, not proof.
- **Missing controls:** The breach rate before installation (if we went years without one, four clean months tells us nothing) and the detection sensitivity. "Not detected" is not the same as "did not happen."
- **Wording:** The phrasing implies the product caused the result, which is also misleading. The accurate version is "no detected breach in 4 months."

**3. "Mean time to detect (MTTD) fell from 19 to 6 hours"** — `[K] Kanıtlanmış / Proven`, provided the attachments hold
- **Why it survives:**
  - A third party measured it (the external SOC).
  - There is a symmetric baseline: 11 months before and 11 months after.
  - Incident definitions stayed the same.
  - The change log is offered as evidence that no other tooling changed.
- **Honesty annex:**
  - The result rests on one before/after comparison, so seasonality and changes in the threat mix remain possible confounds.
  - The board should see the incident count (n), not only the two means.
  - If the change log is incomplete or unreviewed, this drops to `[KKE]`.

**4. "Staff find it easy to use"** — `[H] Makul Hipotez / Plausible hypothesis`, with a self-selection flag
- **Why it is not proven:** The only source is the IT team that chose the product, so the people judging it are the people who picked it. The end users are not represented.
- **What would fix it:** A short survey or measured usage data from the actual end users.

**5. "Licence costs $84,000 a year"** — `[K] Kanıtlanmış / Proven`
- **Source:** The signed contract, which is a primary document.
- **Caveat:** The figure covers the licence only. It does not include implementation, staffing or renewal escalators, so it should not be presented as the total cost.

**6. "Protects against zero-day attacks"** — `[S] Spekülatif / Speculative`
- **Why:** The only source is a marketing brochure. There is no test, and by definition a zero-day cannot be part of any pre-chosen test set. Claim 1's evidence cannot back this claim up.
- **What to do:** Remove it, or restate it as "the vendor claims…".

## Coverage and missing card
- **Coverage:** I tiered all 6 of 6 claims. I did not verify any attachment directly.
- **What the format leaves out:**
  - Total cost of ownership.
  - False-positive and alert-fatigue rates.
  - Incidents the product missed.
  - The pre-installation breach baseline.

## Next steps, most important first
1. Rewrite claims 1, 2 and 6 as attributed or scoped statements before tomorrow. This is cheap and prevents the biggest misstatements.
2. Present claim 3 as the headline, and include n and the change log reference.
3. Keep claim 5, labelled as licence cost only.
4. Present claim 4 as "IT team assessment," and schedule an end-user survey.

VERDICTS
1: NOT PROVEN
2: NOT PROVEN
3: PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
