# Review of fraud model board claims

I can't sign off on all six claims as proven. Two are well supported. The other four have specific gaps, and the board should hear them phrased more carefully.

## 1. Recall 0.94 on held-out 2025 data: supported
- **Evidence:** A held-out split from 2025 that the modelling team never saw. An independent risk-audit team ran the evaluation. That means the data wasn't touched during development and the people judging it aren't the people who built it.
- **Remaining caveats (not blockers):**
  - Recall should be shown with precision or the false-positive rate. A model can reach high recall by flagging lots of transactions.
  - Fraud labels arrive late (chargebacks can take months), so recent 2025 cases may be missing.
  - Give a confidence interval and the number of fraud cases in the test set.
- **Verdict:** Adequately supported as stated.

## 2. Fraud losses fell 22% since launch: not proven
- **Weak before/after comparison:** This is one quarter against the previous quarter, with no comparison group.
- **Seasonal confound:** Q4 losses are usually higher than Q3. That seasonality means the raw comparison could hide or distort the model's effect, depending on which quarters were compared. The team's own note flags it, so the number isn't interpretable as it stands.
- **Other possible causes:** Changes in fraud attacks, transaction volume, policy or other controls could explain the change. Nothing rules them out.
- **Overreach:** "Since launch" suggests the model caused the drop. The evidence only shows that losses changed at the same time.
- **What would fix it:** A year-over-year seasonal comparison, a holdout or control group, and losses normalised by volume.

## 3. The model is fair across customer groups: not proven
- **Not independent:** The modelling team reviewed its own model.
- **Sample too small:** 50 decisions can't support a claim about every customer group, and some groups probably appear only a few times or not at all.
- **No defined test:** No fairness measure was stated, such as false-positive or recall rates by group, and no threshold was set in advance.
- **Wrong conclusion drawn:** "Saw no problems" means no problems were found in 50 cases. It doesn't show the model is fair.
- **Possible legal and regulatory exposure:** The board shouldn't hear "fair" without a proper audit by group.

## 4. Analysts trust the model: not proven
- **Weak evidence:** Two senior analysts gave informal verbal statements in a meeting.
- **No survey or behavioural data:** Nobody was surveyed, and there are no measures of what analysts actually do, such as override rates or how many alerts they accept.
- **Likely bias:** Answers given in a meeting are prone to social-desirability bias.
- **Overreach:** The claim goes from two people to "analysts" in general.

## 5. False-positive rate 1.8% vs 4.6% for the old rules engine: supported
- **Evidence:** Both systems ran in shadow mode on the same 3 months of live traffic, so they're compared on identical data. The payments platform logged the results, which makes it a neutral source.
- **Minor caveats:**
  - Confirm that the false-positive rate is defined the same way for both systems.
  - Report it next to recall at matched operating points, because a lower false-positive rate could come from missing more fraud.
  - Add confidence intervals.
- **Verdict:** Adequately supported.

## 6. Will scale to 10x traffic: not proven
- **One test at a lower load:** The model was load-tested once, at 2x, so predicting 10x means assuming behaviour five times beyond anything tested.
- **Unrepresentative environment:** A laptop isn't the production environment.
- **No repeat runs:** A single run tells you nothing about variance, latency tails or failure modes.
- **What's needed:** Repeated tests at 10x or more in an environment like production, with latency and error budgets set in advance.

## Recommendation
Present claims 1 and 5 as evidence. Reword the other four for the board:
- **Claim 2:** "Losses fell 22% quarter over quarter; attribution is unverified, and seasonality is a confound."
- **Claim 3:** "Fairness audit pending."
- **Claim 4:** "Early qualitative feedback is positive."
- **Claim 6:** "Validated to 2x on a laptop; a 10x test is planned."

Presenting all six as proven would overstate the evidence to the board.

VERDICTS
1: PROVEN
2: NOT PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
