# EVAL-008 — does a pruned SKILL.md audit as well as the full one?

A video argued that current models apply every written detail literally, so
long skills and CLAUDE.md files now lower quality, and should be cut to what
the model cannot know by itself. The claims are audited in
[video-claims-audit.md](video-claims-audit.md). This eval tests the part that
matters for Mizan, on EVAL-003's task set (the only one where a no-instruction
arm stayed below the ceiling on haiku).

## Design

| | |
|---|---|
| Tasks / key | EVAL-002's six tasks, EVAL-003's key, unchanged |
| Arm O | `skill/mizan/SKILL.md` at `ca58307` (488 lines) |
| Arm P | the same file pruned by the recipe below, ≤ 200 lines |
| Arm C | EVAL-001's 45-word brief (`arms/C.md`, byte-identical): the video's "short brief" |
| Runs | 6 tasks × 3 arms × 3 reps = 54, haiku, one fresh instance per run |
| Scoring | EVAL-003's `blind.py` + `SCORER.md` + `analyze.py`, unchanged |

Hypotheses, thresholds, decision rules: `eval-008.mizan-registry.yaml`
(validator: no R1–R28 violations).

## Recipe for arm P (fixed before P is written)

P is written after this file is committed and committed itself before any
run. The recipe allows only **moving** and **deleting**, never new rule text:

1. Keep verbatim: the six core commitments, the tier table, the mode-choice
   paragraph, one line per mode 3–7 pointing to its reference file.
2. Move to `references/`: the audit-mode and registry-mode procedures, the
   schema-version rule history (R9–R25 narrative), context economy.
3. Keep, shortened by deletion only: tone rules, operating assumptions,
   anti-patterns — one line each, reason kept.
4. Fix the "Two modes" / "Modes 3–7" heading conflict by renaming only.
5. Stop at ≤ 200 lines; if it cannot be reached by 1–4, stop at the shortest
   result and record the line count as a deviation.

## Stated limits, before the result

- Whoever writes P has seen these tasks and earlier runs (named confound).
- Six tasks: a 0.05 difference is below what this n resolves; *underpowered* is
  the most likely verdict for H-EVAL-008a.
- Same model family writes and scores; calibration packets bound, not remove, this.

## Result (2026-10-09): precondition failed — ceiling

```
calibration   PASS in all six packets
detection     O 1.000   P 1.000   C 1.000
false flags   O 0.083   P 0.000   C 0.056
mean words    O 1588    P 1167    C 1311
P/O words     0.735, CI [0.648, 0.826]  -> H-EVAL-008c met
```

claude-haiku-5-5 found all 24 planted defects under every arm, where EVAL-003's
haiku with no instruction found 77%. No verdict is read for 008a or 008b, and
SKILL.md is not changed by this eval. What the run does show: the pruned body
cuts answer length by about a quarter and prompt tokens by three quarters with
no detection loss on this set — and that a 45-word brief does as well on
detection. Whether the skill earns its length must be measured on something
detection cannot see (registry discipline, earned vs unearned [K]).
