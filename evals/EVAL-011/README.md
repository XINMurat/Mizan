# EVAL-011 — schema-pointer fix, and does the audit procedure cause over-refusal?

Both arms are v3.0 as merged (`e9d842b`) with `read_skill_file`. Arm N is the body only; arm Q has `references/audit-procedure.md` in the prompt, as if read first. 36 runs on claude-haiku-5-5; every read logged. Hypotheses: `eval-011.mizan-registry.yaml`.

```bash
python evals/EVAL-011/run.py --task T1   # ... T6
PYTHONUTF8=1 python evals/EVAL-011/score.py
```
