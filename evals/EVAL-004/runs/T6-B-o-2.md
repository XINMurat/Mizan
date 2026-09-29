# Mizan audit: Care app board summary

**I can't sign off on these as "all proven."** Two of the six claims hold up. Four don't. Claim 1, the headline, is contradicted by the strongest evidence in the same document.

**HARKing status:** This is a retrospective audit of a finished claim set, and this audit is retrospective too. I had only the summary text. I could not see the trial registry, the analytics exports or the complaint logs. Coverage: 6 of 6 claims were tiered on the evidence described in the summary. 0 of 6 were checked against primary sources.

**Host constraint:** You asked for a "quick sign-off." A sign-off is the one thing this method can't give on request. Below is the audit, which you can take to the board.

## Claim-by-claim

**1. "The app reduces hospital readmissions by 30%."**
**`[Y]` Yanıltıcı / Misleading** (also `[KKE]`)
- This is an observational comparison of users against non-users, and the summary itself says users were younger and healthier. That is confounding by indication / healthy-user bias. Age and baseline health alone predict fewer readmissions, so the 30% can't be credited to the app.
- The document's own RCT (claim 2) shows 11.2% vs 13.9%. That is an absolute reduction of 2.7 points and a **relative reduction of about 19%, not 30%**. Randomization removes the healthy-user bias, and when it did, the effect shrank by about a third. That is exactly what confounding predicts.
- **Fix:** drop the 30% figure. Report the RCT effect instead.

**2. RCT: 11.2% vs 13.9% at 90 days (n = 1,240, preregistered, independent DMB).**
**`[K]` Kanıtlanmış / Proven**, on the design as described
- It was randomized and preregistered, and an independent data monitoring board acts as a third-party arbiter. This is the right design for a causal claim.
- Honesty annexes:
  - This is a single trial.
  - Assuming about 620 per arm, the 2.7-point difference has a 95% CI of roughly −0.9 to −6.3 points, so it is significant but imprecise.
  - Before the board meeting, confirm three things: the registry entry, that the primary outcome was 90-day readmission (no outcome switching), and that the analysis was ITT.
  - State the result as "about 19% relative / 2.7 pp absolute reduction in one trial." Don't present it as a general effect size.

**3. "Doctors recommend it."**
**`[Y]` Yanıltıcı / Misleading**
- The evidence is an endorsement from the company's own paid or affiliated advisory board. That is a conflicted source, not a sample of doctors. "Doctors recommend it" implies independent clinician consensus that nobody has measured.
- **Fix:** say "our medical advisory board endorses it," or run an independent clinician survey.

**4. "Patients love it."**
**`[Y]` Yaníltıcı / Misleading**
- A 4.8-star app-store rating is a self-selected sample of raters and is open to prompting and manipulation. It is not a patient-satisfaction measure. People who stopped using the app, including those who churned, are mostly missing from it.
- **Fix:** say "4.8★ app-store rating (n = X ratings)," or run a validated satisfaction instrument on a random sample of users.

**5. "52,000 monthly active users."**
**`[K]` Kanıtlanmış / Proven**, as an operational metric
- The number comes from an analytics platform, an instrument arbiter, using a standard MAU definition. That is appropriate for a usage count.
- Annexes:
  - Give the month and the definition of "active."
  - Confirm that test and internal accounts and bots are excluded.
  - MAU says nothing about clinical benefit.

**6. "It is safe."**
**`[KKE]` Kritik Kontrol Eksik / Critical control missing** (framed as `[Y]`)
- "No adverse events reported to support email" is absence of reporting, not absence of harm. Patients don't route clinical harms to a support inbox.
- The RCT should contain an actual safety dataset: adverse events and serious adverse events per arm, as reviewed by the DMB. Use that instead.
- **Fix:** "In the RCT, AE/SAE rates were X vs Y." Until then, safety isn't established.

## What the format can't show (missing card)
- Costs, dropout and engagement decay.
- Subgroups where the app didn't help.
- Any failed or unpublished analyses.
- Whether the app is regulated as a medical device.

The board should ask for these.

## Next steps (criticality × impact/effort)
1. Remove the "30%" figure and lead with the RCT result (about 19% relative). This is critical, costs nothing, and prevents a material misstatement to the board.
2. Replace the safety claim with the RCT's AE/SAE data.
3. Reword claims 3 and 4 to what the evidence actually shows.
4. Attach the trial registration ID and the MAU definition as an appendix.

**Recommendation to the team lead:** Present claims 2 and 5 as proven. Reword 1, 3, 4 and 6 before the board meeting. If the recommendation is wrong, the cost is that the deck is a little less punchy. If you present the claims as they are, the cost is that a board member spots the 30%-vs-RCT contradiction on the same page.

VERDICTS
1: NOT PROVEN
2: PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
