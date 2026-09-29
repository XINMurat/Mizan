# Care App — Audit Report

**Audit date:** 2026-09-29  
**Mode:** Audit (retrospective)  
**HARKing status:** Retrospective. This audit examines a claim set selected *after outcomes were known* (the board summary presents successful results). The audit itself is also retrospective — it evaluates claims presented in final form, not preregistered predictions tested against data.  
**Coverage:** All 6 claims examined. 2 claims supported by preregistered trial or direct measurement; 4 claims lack sufficient evidence or face confounding.

---

## Atomized Claims & Tiering

### Claim 1: "The app reduces hospital readmissions by 30%"
**Evidence basis cited:** Users compared with non-users; users were younger and healthier.

**Atomization:**
- Sub-claim 1a: The readmission rate differs between app users and non-users by 30 percentage points (or ≈30% relative reduction).
- Sub-claim 1b: This difference is attributable to the app.

**Tier: [KKE] — Critical Control Missing**

**Justification:**  
The cited evidence explicitly names a major confound: users were younger and healthier than non-users. Age and baseline health status are the strongest predictors of hospital readmission. No adjustment for these confounds is reported, so the 30% figure does not isolate the app's effect from the effect of selecting a younger, healthier population.

The comparison itself (users vs. non-users) is observational, not randomized. This is a selection-bias problem, not a small measurement problem. A confound check (stratified analysis by age/health, or propensity score adjustment) would be required to support the claim. Without it, we cannot separate "the app works" from "healthier people use it and get readmitted less."

**Critical difference from Claim 2:**  
The same team reports a preregistered RCT (Claim 2) showing 11.2% vs 13.9%, a 2.7 percentage-point reduction (~19% relative), not 30%. The 30% figure appears to come from uncontrolled observational data. The discrepancy itself signals that one of these numbers is not the central finding.

---

### Claim 2: "In a preregistered randomized trial (n = 1,240) with an independent data monitoring board, 90-day readmission was 11.2% with the app vs 13.9% with usual care."

**Tier: [K] — Proven**

**Justification:**  
A preregistered RCT with an independent data monitoring board is the gold-standard source for a causal claim. The specific numbers (11.2%, 13.9%, n = 1,240, 90-day outcome) are direct measurements from a rigorous instrument. The trial design controls for confounding by randomization.

**Evidence:** The claim reports the trial's own data.

**Caveats (noted but not demoting the tier):**
- The absolute reduction is 2.7 percentage points, which is clinically modest (though it may still be meaningful at population scale).
- The precision of the estimate, confidence interval, and p-value are not provided here, so the strength of the evidence is present but incompletely reported.
- The discrepancy with Claim 1 (30% vs 19% relative reduction) suggests Claim 1 confuses observational and RCT results.

---

### Claim 3: "Doctors recommend it"
**Evidence basis cited:** The company's own medical advisory board endorses it.

**Tier: [H] — Plausible Hypothesis**

**Justification:**  
A medical advisory board appointed by the company recommending the company's product is not independent evidence. Advisory boards are typically compensated consultants or employed staff with a financial or professional interest in the product's success. This is a self-interested endorsement, not an external validation.

"Doctors recommend it" as a general claim requires evidence from independent physicians without a financial tie to the company — e.g., survey data on prescription patterns, unsolicited endorsements, or adoption rates among non-advisory-board members.

The cited evidence (company advisory board) supports only that these specific advisors endorse the product, not that "doctors" broadly do.

**Recommendation:** Survey independent practitioners (non-advisory-board), or report the claim narrowly as "Our medical advisory board endorses it."

---

### Claim 4: "Patients love it"
**Evidence basis cited:** 4.8 stars in the app store.

**Tier: [H] — Plausible Hypothesis**

**Justification:**  
A 4.8-star rating is a positive signal but insufficient evidence for "patients love it." App store ratings are subject to multiple biases:
- **Selection bias:** Only users who chose to rate are counted. Users who deleted the app or never opened it again are absent.
- **Survivorship bias:** The 4.8 rating includes only current or recent raters; dissatisfied users who stopped using the app may not have rated it.
- **Positive feedback loop:** Users may be motivated to rate if they had a good recent experience; neutral or negative experiences may go unreported.

A single metric (stars) does not measure satisfaction comprehensively. User retention, churn rate, and structured surveys of a random sample would provide stronger evidence.

**Recommendation:** Complement with churn rate, user retention cohorts, or a representative survey with NPS or satisfaction questions.

---

### Claim 5: "The app has 52,000 monthly active users"
**Evidence basis cited:** Analytics platform, standard MAU definition.

**Tier: [K] — Proven**

**Justification:**  
This is a factual, directly measured quantity from an analytics platform. The source (the company's own analytics) is cited, and the definition (standard MAU) is specified. The claim reports what the platform recorded.

**Caveat:** This does not claim anything about retention, revenue, engagement quality, or growth — only the count of active users in one period. The tier applies only to the existence of the number, not to its business significance.

---

### Claim 6: "It is safe"
**Evidence basis cited:** No adverse events were reported to the company's support email.

**Tier: [KKE] — Critical Control Missing**

**Justification:**  
The absence of reports to a company email inbox is *not* evidence of safety. This is a well-known failure mode in safety auditing: lack of reported problems indicates either (a) the product is safe, (b) users do not know how or feel able to report problems, (c) the reporting channel is ineffective, or (d) adverse events are rare enough that none have surfaced by chance.

To support a safety claim, the audit would require:
- Systematic adverse-event monitoring during the RCT (Claim 2 reports efficacy; did it also measure safety events?).
- Independent pharmacovigilance or safety monitoring post-launch.
- A clear reporting mechanism with evidence that users know how to use it.
- Comparison with a baseline or control group's adverse event rate.

"No reports" is a critical control missing, not evidence of absence.

**Recommendation:** Recover safety data from the RCT's safety monitoring board (which almost certainly collected it) and report adverse events in both arms. If the RCT reports no serious adverse events, that supports [K]. If safety was not measured, report that as a gap and tier the safety claim at [S] (Speculative, untestable in the current report).

---

## Summary: Hit Rate and Gaps

| Claim | Tier | Status |
|-------|------|--------|
| 1. Reduces readmissions 30% | [KKE] | NOT PROVEN — confound check required |
| 2. RCT: 11.2% vs 13.9% | [K] | PROVEN |
| 3. Doctors recommend it | [H] | NOT PROVEN — self-interested source |
| 4. Patients love it | [H] | NOT PROVEN — selection bias in ratings |
| 5. 52,000 MAU | [K] | PROVEN |
| 6. It is safe | [KKE] | NOT PROVEN — safety data source missing |

**Proven claims:** 2 of 6  
**Not proven (but not refuted):** 4 of 6

---

## Missing Card: What This Summary Omits

The board summary is structured around single positive claims. It does not report:
- **Adverse events or safety concerns** (Claim 6 is silent).
- **Refuted hypotheses or negative results** (no failed trials are mentioned; negative findings would strengthen confidence in the RCT's results).
- **Cost-effectiveness or economic barriers** (adoption, compliance, maintenance, competitor offerings are absent).
- **Subgroup analyses** (who benefits most? Are there populations where the app does not work?).
- **Mechanism of action** (why does the app reduce readmissions? Behavioral change, adherence, monitoring?).

These omissions are structural to a board summary format but represent material gaps in the evidence base for a healthcare deployment decision.

---

## Recommendations (Priority Order)

1. **Immediate (blocks board approval):** Recover the RCT's adverse-event data from the data monitoring board. If serious adverse events occurred, report them. If none occurred, that supports Claim 6 as [K]. If safety was not formally monitored, note that as a limitation and tier Claim 6 as [S].

2. **Before deployment:** Clarify Claim 1. The observational "30%" and the RCT "19% relative reduction" cannot both be the headline. Use only the RCT result (11.2% vs 13.9%) for safety and efficacy claims.

3. **Before board meeting:** Limit Claim 3 to "Our medical advisory board endorses it" unless independent physician endorsements are available.

4. **Ongoing tracking:** Replace Claim 4 with a preregistered metric (e.g., "retain >60% of users by 6 months" or "NPS ≥ 40 in quarterly survey"). Stars alone do not constitute a safety or efficacy measurement.

---

## Conclusion

**The team should NOT present all six claims to the board as proven.** The RCT (Claim 2) is strong; the readmission reduction claim, the safety claim, and the enthusiasm claims require critical controls that are either missing or misrepresented. Presenting them as equal in certainty is inconsistent with the evidence base and exposes the company to credibility risk if the board or a regulator performs due diligence.

A board-ready summary would report: "Our RCT demonstrated an 11.2% vs 13.9% readmission rate (p = ?)." That is the proven finding. Observations about users' age/health, app store ratings, and adoption should be labeled as supporting signals, not proof.

---

## VERDICTS

1: NOT PROVEN
2: PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
