# EVAL-002 — the same question on material that does not give itself away

[EVAL-001](../EVAL-001/) asked whether the Mizan skill changes what an audit
finds, and could not answer: every arm found every planted defect (the
preregistered ceiling precondition failed). Its tasks signposted their
defects — the price cut sat in parentheses beside the churn claim.

EVAL-002 keeps the design (arms, scorer, blinding, calibration, analysis,
thresholds; files copied unchanged apart from the seed) and changes only the
material:

- **No defect is signposted in its own item.** Four need arithmetic
  (78% not 82%, +25% not +40%, 49 minutes not 47, ROI 200% not 300%); five
  need another item to see (prevalence, last year's November, the DNS
  incident, the service inventory, who was shown the ads).
- **Distractor items** carry no defect and are not scored; some hold the fact
  that exposes a defect elsewhere.
- **Sound claims that look suspicious**: a large effect measured against a
  proper control, so over-flagging has something to bite on.
- **Defect positions vary** across tasks.

Preregistration: `eval-002.mizan-registry.yaml`, committed with `key.yaml`,
`tasks/` and `runs/prompts/` before any run. The same limits as EVAL-001
apply (same model family writes and scores; the author wrote the key; blinding
strips tags, not style), stated in the registry.
