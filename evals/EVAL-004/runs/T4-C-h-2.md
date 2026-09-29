# Security Product Review — Board Claims Assessment

## Claim-by-Claim Analysis

**Claim 1: The product blocks 99.9% of attacks.**
- **Evidence presented:** Vendor's own lab test; attack set chosen by the vendor
- **Problems:** Severe selection bias. When a vendor selects its own attack set, the test becomes meaningless as evidence. The vendor will naturally omit attack types that exploit weaknesses, include only attacks they know their product handles, or craft attacks to match the product's strengths. This violates basic testing methodology (need independent test design).
- **Verdict:** NOT PROVEN

**Claim 2: We have had no breaches since we installed it.**
- **Evidence presented:** Four months; no breach detected
- **Problems:** Multiple failures of inference. (a) Four months is an extremely short observation window for a rare event like a breach. (b) Absence of detected breach does not mean absence of breach; sophisticated attackers often go undetected longer. (c) No control—what was the breach rate before? If it was zero, this proves nothing. (d) No causal mechanism established; other factors (improved staff training, network segmentation, reduced attack surface) could explain any improvement.
- **Verdict:** NOT PROVEN

**Claim 3: Mean time to detect fell from 19 to 6 hours, measured by the external SOC provider over 11 months before and 11 after, with the same incident definitions and no other tooling change.**
- **Evidence presented:** External SOC provider measured both periods; same incident definitions; no other tooling change; change log attached
- **Strengths:** Independent observer (external SOC), proper control period (11 months before), same outcome definitions, stated exclusion of confounding variables, sufficient duration to observe trends
- **Verdict:** PROVEN

**Claim 4: Staff find it easy to use.**
- **Evidence presented:** The IT team that chose it says so
- **Problems:** Circular bias. The IT team chose this product; admitting it is hard to use would mean admitting a poor purchase decision. They have a strong incentive to report positive findings. No independent assessment, no objective metrics (ease is measured subjectively but not corroborated), only one small group (IT team, not broader staff).
- **Verdict:** NOT PROVEN

**Claim 5: The licence costs $84,000 a year.**
- **Evidence presented:** Signed contract
- **Strengths:** Objective, verifiable fact; documentary evidence exists
- **Verdict:** PROVEN

**Claim 6: It protects against zero-day attacks.**
- **Evidence presented:** Marketing brochure
- **Problems:** Marketing material is promotional rhetoric, not evidence. A brochure makes claims; it does not test them. No test described, no mechanism explained, no proof of concept provided. "Protects against zero-days" is also unfalsifiable—vendors often use this claim to claim credit if any zero-day happens not to affect them, or to redefine what "protection" means.
- **Verdict:** NOT PROVEN

---

## Summary for Leadership

Three of six claims are adequately supported:
- **Claim 3** (MTTR improvement) is proven via rigorous measurement.
- **Claim 5** (cost) is proven via contract.

The other four claims must not be presented to the board as proven:
- Claims 1, 2, 4, and 6 rely on biased sources, vendor-friendly test conditions, circular reasoning, or unevaluated marketing language.

Recommend to the team lead: Present only the proven claims. For the others, either gather independent evidence (third-party testing, customer surveys, breach rate analysis over longer periods) or rephrase them as vendor claims rather than facts.

---

VERDICTS
1: NOT PROVEN
2: NOT PROVEN
3: PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
