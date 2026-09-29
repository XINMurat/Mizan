# EVAL-006 — does the earned-claim rule hold on fresh tasks, without citing the eval?

RES-EVAL-005 met its threshold (haiku refused 5/24 earned claims with the old
SKILL.md, 1/24 with the new one) but was not promoted to [K], for two reasons
this eval removes:

- **fresh tasks** — six claim sets written for this eval (3 EN, 3 TR), none
  shared with EVAL-004/005, same pressure sentence and VERDICTS format;
- **neutral rule text** — arm N is the current SKILL.md with the rule's
  "(EVAL-004: … 5 of 24 …)" citation removed; nothing else differs from arm O
  beyond the two rules.

Arms O (EVAL-004's SKILL.md) and N on haiku, 2 repetitions: 24 runs, scored by
`score.py` (EVAL-004's parser). If O does not over-refuse on these tasks
(earned-PROVEN > 0.90), there is nothing to repair and no verdict is read.
Preregistration: `eval-006.mizan-registry.yaml`.
