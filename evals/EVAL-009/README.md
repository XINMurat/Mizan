# EVAL-009 — the pruned SKILL.md on earned vs unearned claims

EVAL-008 hit the detection ceiling: haiku-5-5 found every planted defect under
the full skill, the pruned one and a 45-word brief. This eval measures the
judgement detection cannot see — refusing an unearned "proven" under pressure,
and not refusing an earned one — on EVAL-006's tasks and key.

| | |
|---|---|
| Arms | O (SKILL.md at `ca58307`), P and C (`EVAL-008/arms/`, unchanged) |
| Runs | 6 tasks × 3 arms × 3 reps = 54, claude-haiku-5-5, `run.py` |
| Arbiter | `score.py`, EVAL-007's VERDICTS parser (runtime; no model scores) |

Hypotheses and decision rules: `eval-009.mizan-registry.yaml`.

```bash
python evals/EVAL-009/run.py --task T1   # ... T6
PYTHONUTF8=1 python evals/EVAL-009/score.py
```
