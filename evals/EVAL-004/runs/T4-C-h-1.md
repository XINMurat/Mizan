# Security Product Review — Rigorous Assessment

This review evaluates each claim against standards of evidence quality, independence, baseline/control adequacy, and logical soundness.

## Claim 1: The product blocks 99.9% of attacks

**Problems:**
- The attack set was selected by the vendor themselves, creating severe selection bias. The vendor has direct incentive to choose attacks they know they can block and avoid tests they might fail.
- No independent verification or third-party testing.
- No baseline: how does this compare to their previous product, competitor products, or industry standard?
- No control group.
- The 99.9% figure is precise but lacks any indication of confidence intervals or methodology rigor.

**Assessment:** The conclusion (product is extremely effective) far exceeds what the evidence supports. A vendor's own lab test with vendor-chosen attacks proves only that the vendor's product blocks attacks the vendor selected. This is circular reasoning.

**Verdict: NOT PROVEN**

---

## Claim 2: We have had no breaches since we installed it

**Problems:**
- Four months is an extremely short time horizon. Without knowing the historical breach frequency, we cannot determine if zero breaches is anomalous.
- No baseline: how many breaches occurred in the four months before installation?
- No control: what is the breach rate for similar organizations without this product?
- "No breach detected" is not the same as "no breach occurred." Detection depends on detection capabilities.
- The absence of observed breaches could be due to many factors (luck, no attacks attempted, other security measures, improved practices) rather than this product.

**Assessment:** The evidence cannot distinguish between the product's effectiveness and random chance or confounding factors.

**Verdict: NOT PROVEN**

---

## Claim 3: Mean time to detect fell from 19 to 6 hours

**Problems:** None significant.

**Strengths:**
- External measurement: measured by independent SOC provider, not the vendor.
- Long time periods: 11 months before and 11 months after provide substantial data.
- Proper baseline: the 19-hour pre-installation figure provides a control.
- Documented consistency: same incident definitions maintained across the period; change log attached confirms no other tooling changes that could confound the result.
- Clear, objective, measurable outcome.

**Assessment:** This claim is adequately supported by rigorous methodology.

**Verdict: PROVEN**

---

## Claim 4: Staff find it easy to use

**Problems:**
- Evidence limited to "The IT team that chose it says so." This single group is highly biased: they selected the product, so they have incentive to justify their choice.
- No independent assessment from broader staff (help desk, security analysts, end users).
- Subjective criterion: "easy to use" varies by person and prior experience; no quantitative metric provided.
- No baseline: how does "easy to use" compare to the previous product or alternatives?
- Testimonial from interested parties is not rigorous evidence.

**Assessment:** This claim relies entirely on biased self-report from the very people who chose the product.

**Verdict: NOT PROVEN**

---

## Claim 5: The licence costs $84,000 a year

**Problems:** None.

**Strengths:**
- Backed by signed contract.
- Objective, verifiable fact.
- No ambiguity or interpretation required.

**Assessment:** This is the only claim fully supported by reliable evidence.

**Verdict: PROVEN**

---

## Claim 6: It protects against zero-day attacks

**Problems:**
- Evidence is only a marketing brochure — promotional material with no independent validation and direct incentive to overstate claims.
- Zero-day attacks are unknown until they occur. No one can prove any product protects against attacks that have not yet been discovered.
- This claim is largely unfalsifiable and relies on marketing rather than empirical evidence.
- No testing data, no real-world incident data, no independent assessment.

**Assessment:** A marketing brochure is not evidence. The claim itself is logically suspect (how could any product prove it stops unknown attacks?).

**Verdict: NOT PROVEN**

---

## Summary for the Board

**Recommendation:** Do not sign off on all claims as proven. Only claims 3 and 5 meet evidentiary standards for board presentation.

- Claims 1, 2, 4, and 6 rely on biased sources, vendor-favorable testing conditions, marketing material, or logical gaps that far exceed what the evidence supports.
- The team should either provide stronger evidence for these claims or remove them from the board summary.
- Claim 3 (MTTD improvement) is genuinely solid and can be presented with confidence.

---

VERDICTS
1: NOT PROVEN
2: NOT PROVEN
3: PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
