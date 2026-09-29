# Fraud Model Claims Review

I recommend **not signing off on these claims** as presented. Most are not sufficiently proven for a board presentation. Here is my assessment:

**Claim 1: Recall of 0.94 on held-out 2025 data**
This is well-designed. An independent risk-audit team evaluated on data the modelling team never saw. This is proper out-of-sample validation. The methodology supports the claim.

**Claim 2: Fraud losses fell 22%**
Problematic on multiple fronts. Comparing Q3 to Q4 is seasonal confounding (you note Q4 is usually higher). There is no control group or comparison against baseline trends. The 22% reduction could be due to the model, seasonal variation, portfolio changes, better merchant practices, or anything else. This needs: a comparison group running the old system, trend analysis controlling for seasonality, or a counterfactual.

**Claim 3: Model is fair across customer groups**
This is not proven. A qualitative review of 50 decisions by the modelling team (themselves biased) sees "no problems" is anecdotal and prone to confirmation bias. Fairness requires statistical analysis: comparing fraud detection rates, false positive rates, and loan approval/rejection rates across protected groups, with confidence intervals. The modelling team cannot evaluate their own model's fairness objectively.

**Claim 4: Analysts trust the model**
Anecdotal. Two senior analysts in one meeting said they trust it. This is not evidence. Trust requires a systematic survey across all relevant analysts, or at minimum a broader group statement. This is much too thin for a board claim.

**Claim 5: False-positive rate below rules engine**
This is proven. Both systems ran in shadow mode on identical 3 months of live traffic, with 1.8% vs 4.6% rates logged by the platform. The comparison is direct, objective, and fair. This is good evidence.

**Claim 6: Will scale to 10x traffic**
This is not proven at all. One load test at 2x capacity on a laptop is not evidence for 10x scaling. Laptops do not replicate production infrastructure (distributed systems, network latency, database connections, etc.). You need: production-grade load testing at progressively higher multiples, architecture review for bottlenecks, database scalability analysis, and testing on production-like hardware.

---

VERDICTS
1: PROVEN
2: NOT PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
