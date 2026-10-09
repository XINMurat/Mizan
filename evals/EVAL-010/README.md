# EVAL-010 — the pruned skill with its references readable

EVAL-009 ran the pruned body with no way to read `references/`. Installed, it can. Both arms here get one tool, `read_skill_file`, over their own skill files at pinned commits (O = v2.9 at `ca58307`, N = pruned at `d2cef6c`), on EVAL-006's tasks; every read is logged. Hypotheses and the merge decision rule: `eval-010.mizan-registry.yaml`.

```bash
python evals/EVAL-010/run.py --task T1   # ... T6
PYTHONUTF8=1 python evals/EVAL-010/score.py
```
