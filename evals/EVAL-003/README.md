# EVAL-003 — EVAL-002 on a smaller model

EVAL-001 and EVAL-002 hit the ceiling: on the default model even arm A found
nearly every planted defect, so no verdict could be read. EVAL-003 asks the
same question where there is headroom. Tasks, prompts, arms, scorer rubric,
blinding and analysis are EVAL-002's (prompts byte-identical); the review
runs use **haiku**, the blinded scoring stays on the default model so that
scoring quality does not change with the arm model.

The two answer-key errors found in EVAL-002 (T1-S2, T4-S2 — both "sound"
claims that were not) are removed from scoring here, before any run.
EVAL-002 itself was not re-scored. Preregistration:
`eval-003.mizan-registry.yaml`.

## Result (RES-EVAL-003)

Precondition met (arm A 0.771). Detection A 0.771 / B 0.875 / C 0.812; false
flags A 0.083 / B 0.208 / C 0.083; words A 385 / B 1803 / C 494. B−A +0.104,
95% CI [−0.062, +0.250] — **underpowered**, no verdict. The point estimate
favours the skill, but comes with 2.5× the false flags and 4.7× the length.
