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

## Result (RES-EVAL-005)

**The repair worked on the locked threshold.** Arm O refused 5 of 24 earned
claims — exactly EVAL-004's rate, so the cost reproduces — and arm N refused 1.
N−O +0.167, 95% CI [+0.042, +0.333]; no unearned claim slipped through in N.
The length rule is within noise (N/O 0.81, CI [0.60, 1.08]). Not promoted to
[K]: the new rule's text cites EVAL-004 and was written after reading these
tasks; a fresh-task replication is the next step. T2-O-2's first attempt was
excluded (two Writes) and re-run; with it the verdict is the same.
