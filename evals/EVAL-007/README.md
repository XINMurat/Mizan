# EVAL-007 — does the rule as shipped (with its citation) help on fresh tasks?

RES-EVAL-006 refuted the neutral-worded earned-claim rule on six fresh tasks,
but two things had changed at once: the tasks were new and the rule's
"(EVAL-004: … 5 of 24 …)" citation was gone. SKILL.md still ships the cited
wording. This eval runs that wording (arm C) against EVAL-004's SKILL.md
(arm O) on EVAL-006's tasks, in one batch, haiku, 2 repetitions: 24 runs.

Arm C is EVAL-006's N prompt with the citation put back and nothing else
changed; arm O is EVAL-006's O prompt byte for byte. What happens to
SKILL.md is fixed before the runs, in each hypothesis's `decision_rule`:
refute removes the rule and records it in `RETIRED-RULES.md`, support keeps
it, anything else changes nothing.

Preregistration: `eval-007.mizan-registry.yaml`, committed with `score.py`,
`tasks/`, `key.yaml` and `runs/prompts/` before any run.

## Result (RES-EVAL-007a) — refuted; the rule leaves SKILL.md

Parse rate 1.000. Arm O refused 20.8% of earned claims (the precondition
holds: the cost is real). Arm C, the wording SKILL.md shipped, did not reduce
it: earned-PROVEN O 0.792, C 0.708, C−O −0.083, 95% CI [−0.292, +0.083].
Unearned-PROVEN 0.000 in both arms, so the guard holds. Without T3
(preregistered secondary): O 0.900, C 0.850.

With EVAL-006, both wordings have now been run on unseen tasks and both point
estimates went the wrong way. EVAL-005's effect was fit to the tasks the rule
was written after. By the decision rule fixed before the runs, the rule is
removed from SKILL.md; the record is in `RETIRED-RULES.md`. The over-refusal
itself stays open.

**RES-EVAL-007b — underpowered.** Words C/O 0.949, CI [0.736, 1.177]: one
thousandth under the refute bar, so the length rule stays by the same
decision rule. Three batches (0.81, 0.81, 0.95), none resolving.

Two first attempts were excluded and re-run once (`runs/excluded/`, reasons
in the registry's deviations): one reported an Edit, one showed more tool
calls in the harness count than its own report admitted.
