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

## Result (2026-09-29): precondition failed again — ceiling

```
detection     A 0.958   B 1.000   C 1.000
false flags   A 0.167   B 0.167   C 0.042
mean words    A 664     B 1438    C 847
calibration   PASS in all six packets
```

The harder material moved arm A from 1.000 to 0.958 — one defect (T5: ROI is
200%, not 300%) missed by both arm-A runs — and no further. Above the
preregistered 0.85, so **no verdict**: both hypotheses stay `[H]`.

**The answer key was wrong twice, and the models found it.** The false-flag
guard reads "broken", but reading the flags by hand shows most are errors in
the key, not in the reviews:

- T4-S2: the alert threshold was validated by replaying the same incident it
  was tuned on — circular. Flagged in all three arms; 4 of the 9 flags.
- T1-S2: 0.5% prevalence in 41,200 people is about 206 cases, yet 312 are
  confirmed. A real contradiction the author never planted.

The key is left as it was and nothing is re-scored. Correcting the ruler
after reading the result is the move this whole registry exists to prevent;
the correction goes into the next preregistration instead.

**Across EVAL-001 and EVAL-002, measured and not in dispute:** on this model,
the skill more than doubles output length (1,370 and 1,438 words against 619
and 664) with no detection gain on either task set. Whether it buys anything
the rubric does not score — tier discipline, refusing an arbiter-less `[K]`,
behaviour over a long registry — is untested. Whether a smaller model, with
headroom, benefits from it is also untested.
