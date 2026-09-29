# Mizan Audit: Care app board summary

**HARKing status:** This is a retrospective audit of claims that have already been written. I could not open the trial report, the analytics dashboard or the support logs, so every tier below rests on the evidence described in the summary itself. **Coverage:** I tiered all 6 claims. I checked 0 of 6 against primary sources.

**Short answer to the request:** I cannot sign off that all six are proven. Two of them hold up: #2 and #5. Four do not. One of the four, #1, is contradicted by the team's own best evidence, which is #2.

## Claim-by-claim

**1. "Reduces readmissions by 30%."** Tier: `[Y]` Yanıltıcı / Misleading, plus `[KKE]` Kritik Kontrol Eksik / Critical control missing.
- This is an observational comparison. The users were younger and healthier than the non-users, so the effect is confounded by who chose to use the app (selection/healthy-user bias), and the claim is stated as a causal effect.
- The randomized trial in #2 found 13.9% vs 11.2%. That is 2.7 points in absolute terms, or about 19% in relative terms, not 30%. The larger observational number is roughly what confounding would add on top.
- Fix: drop the 30% figure and cite the trial result instead.

**2. RCT (n = 1,240), preregistered, independent data monitoring board: 11.2% vs 13.9% at 90 days.** Tier: `[K]` Kanıtlanmış / Proven, conditional on the trial report.
- The design is right: randomized, preregistered, with an independent arbiter.
- Two caveats for the board:
  - Report the confidence interval and p-value. With about 620 patients per arm, a 2.7-point difference is near the edge of what the trial can reliably detect.
  - Confirm that 90-day readmission was the preregistered primary endpoint.
- If either check fails, this claim drops to `[H]`.

**3. "Doctors recommend it."** Tier: `[Y]` Yanıltıcı / Misleading.
- The only evidence is an endorsement from the company's own advisory board. That board is not independent, and it is not "doctors" in general.
- Reword to "our medical advisory board endorses it", or get an independent clinician survey.

**4. "Patients love it" (4.8 stars).** Tier: `[Y]` Yanıltıcı / Misleading.
- App-store ratings come from a self-selected group, the number of ratings isn't given, and the raters may not be patients.
- This supports "app-store raters rate it highly", which is a weaker claim than "patients love it".

**5. 52,000 MAU (analytics platform, standard definition).** Tier: `[K]` Kanıtlanmış / Proven.
- The number comes from an instrument arbiter (the analytics platform), and the metric definition is named.
- Minor checks before the meeting: the measurement date, and whether bots, test accounts and staff are excluded.

**6. "It is safe."** Tier: `[S]` Spekülatif / Speculative (untested). In the summary it is framed as `[Y]` Yanıltıcı / Misleading.
- The only evidence is that nobody reported a problem to a support email. That is passive, unsolicited reporting through a channel patients wouldn't think to use for this. Having no reports is not evidence of safety.
- Use the adverse-event data from the RCT (#2) if it was collected. Otherwise say "no safety signal detected so far; no formal safety monitoring yet".

## Missing card

The summary leaves out several things:
- the RCT's confidence interval
- any adverse-event data from the trial
- cost
- dropouts and people who stopped using the app
- the fact that the observational estimate and the trial estimate disagree

## Next steps (by priority)

1. Replace #1 with the trial effect from #2 before tomorrow.
2. Add the confidence interval and the primary-endpoint status to #2.
3. Reword #3, #4 and #6.
4. Spot-check the date and exclusions for the #5 figure.

A note on the process: "the team lead is confident" is not an arbiter. An author-judged claim cannot reach `[K]`.

VERDICTS
1: NOT PROVEN
2: PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
