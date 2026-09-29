# EVAL-001 — does the skill change what an audit finds?

The family's central claim is that this discipline produces better audits.
Until this directory it had no control arm anywhere: the Kıyas ledger says so
about itself, and no skill had been run with and without its instructions.
This is the first attempt, and it is preregistered — everything here except
`runs/` and `scores/` was committed before a single arm ran.

## Design

| | |
|---|---|
| Tasks | 6 short claim sets (`tasks/`), 3 Turkish, 3 English. Each has **4 planted defects** and **2 sound claims** (`key.yaml`). |
| Arm A | the task alone |
| Arm B | the task + `skill/mizan/SKILL.md` (body) as instructions |
| Arm C | the task + a 45-word "be skeptical" instruction (`arms/C.md`) |
| Runs | 6 tasks × 3 arms × 2 repetitions = 36, each a fresh model instance with no tools but writing its answer |
| Scoring | blinded (`blind.py` strips tier tags and names, shuffles with a fixed seed), one scorer per task, rubric in `SCORER.md` |
| Calibration | every packet hides a known positive and a known negative; a miss voids the run |
| Analysis | `analyze.py`: detection and false-flag rates per arm, task-level bootstrap CI |

**B vs A** asks whether the skill does anything. **B vs C** asks the question
that matters: whether 486 lines of skill measurably beat one paragraph.

The hypotheses, thresholds, refutation conditions and the precondition that
voids a too-easy run are in `eval-001.mizan-registry.yaml`, validated by
Mizan's own validator.

## Stated limits, before the result

- The same model family writes and scores the reviews.
- The answer key was written by the evaluation's author; the scorer only matches against it.
- Blinding strips tags, not style or length. Length per arm is reported beside every rate.
- Six tasks give a wide confidence interval. *Underpowered* is a likely and legitimate outcome.
- Defects are always items 1-4. The position is identical across arms, so it cannot favour one.

## Re-running

```bash
python evals/EVAL-001/blind.py      # after runs/ holds all 36 outputs
# score each scores/packets/T*.md with SCORER.md -> scores/T*.json
python evals/EVAL-001/analyze.py
```

## Result of run 1 (2026-09-29): precondition failed — ceiling

```
detection     A 1.000   B 1.000   C 1.000
false flags   A 0.000   B 0.000   C 0.000
mean words    A 619     B 1370    C 760
calibration   PASS in all six packets
```

Every one of the 36 runs found all four planted defects and flagged neither
sound claim. The preregistered precondition — arm A detection at most 0.85 —
failed, so **no verdict is read**: not `[R]`, not `[K]`. Both hypotheses stay
`[H]`. `analyze.py` prints "REFUTE" for the differences; the precondition
overrides it, as the registry says it would.

The scorer was not being lenient. The two subtlest defects were checked by
hand in arm A's raw output: both repetitions computed that 12,400 → 15,100 is
about 1.22×, not 3× (T5), and both named the skipped tests as exactly the
legacy parser tests (T4). Arm A even invented evidence tiers of its own.

What this run does show, `[K]` on this task set: the skill roughly doubled
output length (1,370 vs 619 words) for no measurable detection gain. That is a
cost, measured. Whether a benefit exists on harder material is still open.

Why the ceiling happened is `[H]`, formed after seeing the result: the tasks
signposted their defects (the price cut sits in parentheses beside the churn
claim). EVAL-002 tests that with defects that are not signposted, longer
documents with distractors, and defects that need computation or
cross-referencing to find.
