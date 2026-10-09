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

## Result (2026-10-09)

```
parse rate        1.000, 54/54 end_turn
earned-PROVEN     O 0.667   P 0.806   C 0.917
unearned-PROVEN   O 0.014   P 0.000   C 0.042
mean words        O 813     P 780     C 712
H-EVAL-009a  P vs O non-inferior            -> SUPPORT (threshold met)
H-EVAL-009b  P reduces over-refusal          -> UNDERPOWERED (+0.139, CI [-0.056, +0.444])
H-EVAL-009c  45-word brief vs O non-inferior -> threshold met, NOT promoted (surprising positive, control pending)
```

The full skill made haiku-5-5 refuse a third of earned claims. The pruned body
refused fewer and let no unearned claim through. By the preregistered rule, P
replaces SKILL.md's body — held for owner confirmation before the change is made.
