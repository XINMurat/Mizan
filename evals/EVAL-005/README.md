# EVAL-005 — did the two new SKILL.md rules repair EVAL-004's cost?

EVAL-004 measured one behavioural effect of the skill on haiku, and it was a
cost: arm B refused 5 of 24 **earned** claims (A and C: none), and wrote
~1440 words against A's 272. Two rules were added to SKILL.md in response
("an earned claim is reported as earned"; "length is not rigor").

This is the ablation of exactly that change: EVAL-004's six tasks, key,
pressure sentence and VERDICTS parser, on haiku, two arms run side by side:

- **O** — the SKILL.md EVAL-004 used (commit 4177aca)
- **N** — current SKILL.md; the diff between the two prompts is only the two rules

6 tasks × 2 arms × 2 repetitions = 24 runs. Arms A and C are not re-run: the
question is the change, and running O now controls for date and sampling
better than reusing EVAL-004's B. Preregistration: `eval-005.mizan-registry.yaml`.
