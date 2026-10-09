# EVAL-010 — the pruned skill with its references readable

EVAL-009 ran the pruned body with no way to read `references/`. Installed, it can. Both arms here get one tool, `read_skill_file`, over their own skill files at pinned commits (O = v2.9 at `ca58307`, N = pruned at `d2cef6c`), on EVAL-006's tasks; every read is logged. Hypotheses and the merge decision rule: `eval-010.mizan-registry.yaml`.

```bash
python evals/EVAL-010/run.py --task T1   # ... T6
PYTHONUTF8=1 python evals/EVAL-010/score.py
```

## Result (2026-10-09)

```
earned-PROVEN    O 0.583   N 0.750   (N-O +0.167, CI [-0.056, +0.333])
unearned-PROVEN  O 0.000   N 0.000
H-EVAL-010a non-inferior -> SUPPORT;  H-EVAL-010b -> UNDERPOWERED
reads  O: checklist 18, templates 6   N: checklist 18, templates 18, schema 15, audit-procedure 0
```

The prune holds with references readable. N read the full schema on most runs because the pruned reference line had lost v2.9's condition ("when the user keeps a registry file"); restored after the run, post-hoc. Merge (v3.0) awaits owner confirmation.
