# Security Product Board Summary — Evidence Audit

**HARKing Status:** This audit is retrospective. The claims were selected and framed after the product was already in use; this is not preregistered. The team's confidence level ("all proven") was set after outcomes were observed.

**Coverage:** All 6 claims are directly checkable against supplied sources.

---

## Claim-by-Claim Tier Assessment

### 1. The product blocks 99.9% of attacks

**Claim:** Product blocks 99.9% of attacks.  
**Evidence:** Vendor's own lab test; attack set chosen by the vendor.  
**Assessment:** `[H]` — Plausible hypothesis. **Not Proven.**

**Justification:** The vendor both designed the product AND selected the test set. This creates a second-order selection bias: vendors have strong incentive to choose attacks their solution is known to handle well, and to exclude attacks it handles poorly. Even if the lab test is technically sound, the attack set is not representative of real-world attack distribution. This is vendor-curated evidence, not independent verification.

**Mechanism:** Vendor incentive alignment → test-set selection bias → inflated pass rate.

**Next step:** Obtain independent third-party penetration testing with a test set designed by the third party or drawn from a public standard (e.g., NIST attack taxonomy, OWASP Top 10). Current claim stays `[H]` until independent measurement.

---

### 2. We have had no breaches since we installed it

**Claim:** No breaches since installation (four months).  
**Evidence:** Four months; no breach detected.  
**Assessment:** `[H]` — Plausible hypothesis. **Not Proven.**

**Justification:** A four-month observation window is too short for a "proven no breaches" claim, and the absence of detected breaches is not evidence the product caused that absence. Confounds: (a) your organization may not have been targeted during those four months, (b) an attack may have succeeded but gone undetected, (c) other changes (firewalls, access controls, user behavior) may account for the difference. This is survivorship bias framed as a positive result.

**Mechanism:** Short observation window + correlation without causation + absence treated as evidence of causation.

**Next step:** Establish a longer baseline (12–24 months minimum) and document what changed operationally besides the product. Before promoting beyond `[H]`, run a symmetric control: compare breach rate against similar peer organizations that DID NOT install this product, controlling for size, industry, and attack surface. Current claim cannot reach `[K]`.

---

### 3. Mean time to detect fell from 19 to 6 hours

**Claim:** MTTD improved from 19 hours (11 months pre-install) to 6 hours (11 months post-install), measured by external SOC provider with same incident definitions and documented no other tooling change.

**Assessment:** `[KKE]` — Critical control missing. **Not Proven (without confound verification).**

**Justification:** This claim has the strongest methodology of the six: external measurer, same definitions, symmetric before/after window, and explicit statement that no other tooling changed. However, a critical confound control is missing—one that the data could potentially show but wasn't stated as checked:

- **Confound:** Did the *types* of incidents change? If post-installation attacks were lighter/simpler to detect, the improvement would reflect attack distribution, not product capability. The claim states "same incident definitions" (good), but not whether the incident *mix* remained constant.

- **Confound:** Did SOC staffing or expertise change? If the team improved, the product gets false credit.

**Mechanism:** Before → after measurement is sound; the gap is in whether competing hypotheses were ruled out.

**Next step:** Obtain the change log. Verify that (a) incident type distribution remained similar, (b) SOC staffing and procedures did not change, and (c) no other security tooling was added/upgraded during the window. If these are documented as unchanged in the attached change log, tier can be promoted to `[K]`. Current state: the methodology is sound but incomplete without confound checks.

**Note:** This claim should move to `[K]` if the change log verifies the confounds. It is the only claim here with credible methodology. Flag: confirm the change log was actually reviewed.

---

### 4. Staff find it easy to use

**Claim:** Staff find the product easy to use.  
**Evidence:** The IT team that chose it says so.  
**Assessment:** `[H]` — Plausible hypothesis. **Not Proven.**

**Justification:** The IT team that selected the product is exactly the wrong witness for usability. They are invested in the decision (sunk cost, commitment bias, motivated reasoning to believe they made a good choice). A post-purchase statement from the decision-makers is the highest-conflict-of-interest evidence source for product quality.

**Mechanism:** Post-hoc rationalization by invested decision-makers.

**Next step:** Obtain independent usability data: (a) System Usability Scale (SUS) score from frontline staff who did not choose the product, (b) time-to-productivity for new users, or (c) support ticket volume related to ease-of-use issues. Current claim stays `[H]` until independent measurement from non-invested stakeholders.

---

### 5. The licence costs $84,000 a year

**Claim:** Annual licensing cost is $84,000.  
**Evidence:** Signed contract.  
**Assessment:** `[K]` — Proven. **PROVEN.**

**Justification:** A signed contract is direct, authoritative evidence of the agreed price. This claim makes no causal assertion; it states a contractual fact. The evidence is both accessible and dispositive.

---

### 6. It protects against zero-day attacks

**Claim:** The product protects against zero-day attacks.  
**Evidence:** Marketing brochure.  
**Assessment:** `[S]` — Speculative. **Not Proven.**

**Justification:** A vendor marketing brochure is not evidence; it is an advertising claim. Marketing material is composed specifically to persuade, not to report. Vendors routinely claim "zero-day protection" to mean "detection," "mitigation," or "heuristic signatures" — terms that sound similar but are weaker than blocking an actual zero-day (by definition, zero-days are unknown, so no signature exists). The mechanism of protection is not stated, nor is any test that would distinguish this claim from marketing language.

**Mechanism:** Vendor marketing claim without technical definition or independent verification.

**Next step:** Obtain the vendor's technical documentation defining "zero-day protection" (what mechanism? signature-free detection? behavioral analysis?). Then obtain independent verification: zero-day vulnerability tests that the product either detected/blocked or failed to detect. Until then, the claim is aspirational language, not evidence.

---

## Summary

**The board should NOT sign off on an "all proven" statement.** Of six claims:

- **1 is proven:** Claim 5 (licensing cost).
- **5 are not proven:** Claims 1, 2, 4, 6.
- **1 is not proven pending verification:** Claim 3 (MTTD improvement). This one has credible methodology but requires confirmation that attached documentation actually verifies the confounds.

**Key pattern:** Vendor-curated or vendor-invested evidence (Claims 1, 4, 6) systematically fails the audit. Claim 3 is sound in structure but incomplete. Claim 2 suffers from short observation window and correlation/causation confusion.

**Recommendation:** Before presenting to the board, obtain:
1. Independent third-party penetration testing (for Claim 1).
2. Longer baseline (12+ months) plus peer comparison (for Claim 2).
3. Verification that the attached change log confirms confound absence (for Claim 3 — promote to `[K]` if confirmed).
4. Independent usability measurement from non-decision-makers (for Claim 4).
5. Technical specification and independent zero-day testing (for Claim 6).

**Cost if this audit is ignored:** The board will ratify claims the organization cannot defend to auditors, regulators, or in an incident post-mortem. The strongest of these claims (Claim 3) is the only one with a credible path to `[K]`. The others require structural changes to evidence collection, not just more data.

---

## VERDICTS

1: NOT PROVEN
2: NOT PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
