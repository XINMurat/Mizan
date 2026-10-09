# Reference index — full text

Moved verbatim from SKILL.md (v2.9, lines 457-488) when the body was pruned (EVAL-008/009). Nothing here was rewritten.

## References

- `references/recovery.md` — the recovery ramps (`RR-00`…`RR-13`) for when
  the audit itself goes wrong: a promised artifact that did not run, a
  claim that will not settle, a target that moved mid-audit, a tier you
  have to demote. Also the model failure classes they exist for and the
  closing process scorecard. Read when a run stops behaving.
- `references/templates.md` — Registry Entry template, Audit Report
  template, result-block format (TR + EN). Read when producing either
  deliverable.
- `references/checklist.md` — failure-mode checklist (HARKing, selection
  bias, confounds, survivorship, tier drift, threshold shopping) with
  compact worked examples. Read before the first audit in a conversation.
- `references/code-audit.md` — Mode 3 (code audit) and Mode 4
  (bug-hypothesis registry) procedures.
- `references/feature-gate.md` — Mode 5 (feature/PRD gate) procedure and
  the suggestion mechanism.
- Mode 6 needs no reference file — it reads the registry itself.
- `references/security-probe.md` — Mode 7: the trust-boundary map,
  the inverted tier table, and what the pass cannot see.
- `references/domain-adaptation.md` — Modes 3/4/5 beyond software:
  adaptation recipe + 14 domain modules (analytics, marketing, sales,
  research, finance, ops/RCA, security/IR, hiring, procurement, legal,
  UX research, content, policy, personal experiments).
- `schemas/mizan-registry.yaml` — the machine-readable registry format.
  When the user keeps a registry file (in project knowledge, a repo, or
  uploads one), read it at session start, APPEND rather than overwrite,
  propose new entries in this schema, and enforce its hard rules R1–R28
  (mandatory baseline, mandatory confound controls, append-only history,
  no K-promotion without controls on surprising positives, and
  producer/auditor separation: propose tier changes, let the owner or a
  separate audit pass confirm them).
