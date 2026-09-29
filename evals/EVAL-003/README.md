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
