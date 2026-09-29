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
