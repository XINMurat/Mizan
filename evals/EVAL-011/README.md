# EVAL-011 — schema-pointer fix, and does the audit procedure cause over-refusal?

Both arms are v3.0 as merged (`e9d842b`) with `read_skill_file`. Arm N is the body only; arm Q has `references/audit-procedure.md` in the prompt, as if read first. 36 runs on claude-haiku-5-5; every read logged. Hypotheses: `eval-011.mizan-registry.yaml`.

```bash
python evals/EVAL-011/run.py --task T1   # ... T6
PYTHONUTF8=1 python evals/EVAL-011/score.py
```

## Result (2026-10-10)

36/36 end_turn, parse rate 1.000.
- H-EVAL-011a: N read the schema in 0/18 runs (EVAL-010: 15/18) -> SUPPORT, the fix works.
- H-EVAL-011b: earned-PROVEN N 0.694, Q 0.694; N-Q +0.000, CI [-0.250, +0.250] -> REFUTE on the locked threshold. Reading audit-procedure.md did not increase over-refusal.

Result blocks not yet appended to the registry (usage limit); owner review pending.
