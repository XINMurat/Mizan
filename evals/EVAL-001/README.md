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
