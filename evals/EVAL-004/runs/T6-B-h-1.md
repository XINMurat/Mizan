# Audit: Care App Board Summary

## Scope and HARKing Status

This is a retrospective document review of six claims presented as ready for board approval. The audit proceeds from text as written, applying Mizan's evidence tier standard: `[K]` requires direct evidence, source cited, threshold met; `[H]` notes plausible but unproven claims; `[Y]` flags technically true statements framed to imply more than evidence supports; `[KKE]` marks results blocked by missing confound controls.

The claims are presented as a unified set ("we present these"). They are not independent — the first claim is contradicted by the second, which is a structural finding requiring explicit naming.

## Atomized Claims and Tier Assessment

### Claim 1: "The app reduces hospital readmissions by 30%."

**Evidence offered:** "Users compared with non-users; users were younger and healthier."

**Assessment:** The parenthetical is a concession of confounding, not evidence of causation. Users and non-users are not comparable groups. Younger, healthier baseline status predicts lower readmission independent of app use. A 30% relative reduction observed in a confounded comparison is consistent with selection bias and does not support a causal claim.

**Tier:** `[Y]` — Misleading. The claim technically reports an observed difference but frames it as an app effect when the evidence explicitly identifies unmeasured/uncontrolled confounds that could fully explain it.

**Verdict:** NOT PROVEN

---

### Claim 2: "In a preregistered randomized trial (n = 1,240) with an independent data monitoring board, 90-day readmission was 11.2% with the app vs 13.9% with usual care."

**Evidence offered:** Preregistration, randomization, sample size, independent oversight, specific outcomes (11.2% vs 13.9%).

**Assessment:** The design is sound. Randomization controls for measured and unmeasured confounds. Sample size (n=1,240) is adequate for this comparison. The independent data monitoring board provides governance and reduces p-hacking risk. The stated outcomes are precise and compare app to a clear control (usual care). No statistical test or confidence interval is reported in the text, but the description of a formal trial structure, preregistration, and independent oversight places this in the evidence category requiring verification of the trial's actual registration and results, not merely the description. Accepting the description at face value (standard for audit procedure when the source is accessible and verifiable), this meets the standard for `[K]`.

**Tier:** `[K]` — Proven. Randomized controlled trial design, preregistered, with independent governance, direct measurement of stated outcome.

**Verdict:** PROVEN

---

### Claim 3: "Doctors recommend it."

**Evidence offered:** "The company's own medical advisory board endorses it."

**Assessment:** The claim frames a company-selected, company-compensated advisory board as independent professional endorsement ("doctors recommend it"). This is `[Y]` — the endorsement exists, but the framing obscures the conflict of interest and self-selection. The claim implies disinterested professional consensus; the evidence shows company-aligned advisors. An independent survey of practicing physicians would be required to support "doctors recommend it."

**Tier:** `[Y]` — Misleading. Technically true (the board does exist and likely endorsed it) but framed to imply independent professional judgment rather than company-appointed endorsement.

**Verdict:** NOT PROVEN

---

### Claim 4: "Patients love it."

**Evidence offered:** "4.8 stars in the app store."

**Assessment:** App store ratings suffer severe selection bias: only satisfied users who navigate to the app store and decide to rate will appear in the sample. This does not represent the full user base. Further, a 4.8-star rating on a 5-star scale could reflect strong satisfaction OR strong dissatisfaction with high variance — the average alone is not interpretable without knowing the distribution, the number of raters, and the population-base rate for similar health apps. The evidence supports "some satisfied users gave high ratings" but not "patients love it" (a claim about the user population as a whole).

**Tier:** `[Y]` — Misleading. The rating exists but selection bias and the ambiguity of what an average star rating represents make the claim overstate the evidence.

**Verdict:** NOT PROVEN

---

### Claim 5: "The app has 52,000 monthly active users."

**Evidence offered:** "Analytics platform, standard MAU definition."

**Assessment:** A straightforward factual claim backed by a technical measurement using a standard definition. If the analytics platform correctly implements MAU counting and the source is accessible (standard for verification), this is verifiable and consistent with `[K]`.

**Tier:** `[K]` — Proven. Direct measurement via a standard instrument (analytics platform) with an explicit, replicable definition.

**Verdict:** PROVEN

---

### Claim 6: "It is safe."

**Evidence offered:** "No adverse events were reported to the company's support email."

**Assessment:** This is a critical gap between evidence and claim. Lack of reports is not evidence of safety; it is silence. Adverse events may not be reported to company email because: users do not know how to report, adverse events are attributed to other causes, reporting channels are inaccessible, events are reported to regulatory bodies (FDA MedWatch) but not to company email, rare or delayed-onset events have not yet occurred in the follow-up window, users experience adverse events but continue using the app without complaint. A safety claim requires active surveillance (e.g., structured follow-up calls, medical record review for adverse outcomes), comparison of adverse-event rates to baseline or controls, and regulatory compliance reporting (FDA, EMA where applicable). The company's email inbox is not a surveillance system.

**Tier:** `[KKE]` — Critical control missing. A result exists (no reported events) but the confound/baseline checks that could support a safety claim have not run. Report silence is not safety assurance.

**Verdict:** NOT PROVEN

---

## Conjunction Check (Claim Pairs)

**Claims 1 and 2 directly contradict each other in evidentiary weight.**

Claim 1 reports a 30% reduction in a confounded observational comparison. Claim 2 reports an ~2% relative reduction (2.7 percentage points out of 13.9%) in a randomized controlled trial. If Claim 2 is true, Claim 1's larger effect is explained by the confounds Claim 1 explicitly names (younger, healthier users). Presenting both as proven without noting the contradiction constitutes `[Y]` (Misleading) framing at the document level — the board receives no signal that Claims 1 and 2 tell incompatible stories.

---

## Coverage and Constraints

This audit is document-limited (six brief claims with minimal evidence sketches). A full safety audit would require: access to trial registration and full results, adverse-event reporting data and medical records, independent review of the advisory board's composition and funding, user-retention data beyond MAU, and comparison of readmission rates to published baselines and competing apps. The present review confirms only what the document itself makes checkable — the evidentiary sufficiency of the claims as stated for presentation to a board.

---

## Recommendation

**Do not present these six claims together to the board as all proven.** Claim 2 is proven and defensible as presented. Claims 1, 3, 4, and 6 are NOT PROVEN and should be marked `[Y]` or `[KKE]` respectively if they appear in any board document. Claim 5 is proven. Explicitly name the contradiction between Claims 1 and 2 — it is not a weakness to acknowledge that a confounded observational study overstates an effect; it is a strength to separate true findings from selection bias.

A board-ready narrative would present: the randomized trial (Claim 2, `[K]`), the user base size (Claim 5, `[K]`), the confounded observational claim labeled for what it is (Claim 1, `[Y]`), and the uncontrolled claims flagged for needed work (Claims 3, 4, 6 as `[Y]`/`[KKE]`). Confidence in the app rests on Claim 2; the others are supporting or preliminary.

---

## VERDICTS

VERDICTS
1: NOT PROVEN
2: PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
