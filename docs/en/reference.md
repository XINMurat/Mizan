# Mizan — English Reference Index

The English canonical reference for the methodology lives inside the
portable skill package, so it stays in sync with what Claude actually
loads. This page is a map. The Turkish full-text mirrors are in
[`docs/tr/`](../tr/).

| Topic | English (canonical) | Turkish mirror |
|---|---|---|
| Methodology / core skill (Modes 1–2) | [`skill/mizan/SKILL.md`](../../skill/mizan/SKILL.md) | [`docs/tr/metodoloji.md`](../tr/metodoloji.md) |
| Templates (registry entry, result block, audit report) | [`skill/mizan/references/templates.md`](../../skill/mizan/references/templates.md) | [`docs/tr/metodoloji.md` §2](../tr/metodoloji.md) |
| Failure-mode checklist (HARKing, tier drift, …) | [`skill/mizan/references/checklist.md`](../../skill/mizan/references/checklist.md) | [`docs/tr/metodoloji.md` §3](../tr/metodoloji.md) |
| Software modes 3–4 (code audit, bug registry) | [`skill/mizan/references/code-audit.md`](../../skill/mizan/references/code-audit.md) | [`docs/tr/yazilim-modlari.md`](../tr/yazilim-modlari.md) |
| Software mode 5 (feature / PRD gate) | [`skill/mizan/references/feature-gate.md`](../../skill/mizan/references/feature-gate.md) | [`docs/tr/yazilim-modlari.md`](../tr/yazilim-modlari.md) |
| Domain adaptation (14 domains beyond software) | [`skill/mizan/references/domain-adaptation.md`](../../skill/mizan/references/domain-adaptation.md) | [`docs/tr/alan-uyarlama.md`](../tr/alan-uyarlama.md) |
| Machine-readable registry schema (R1–R8) | [`skill/mizan/schemas/mizan-registry.yaml`](../../skill/mizan/schemas/mizan-registry.yaml) | same file (comments EN) |

## English-only long-form docs

- [Usage guide](usage-guide.md) — install, workflows, hard rules.
- [Project instructions](project-instructions.md) — the block to paste
  into a Claude Project.

> **Maintenance note:** the skill references above are the single source of
> truth in English. The Turkish files in `docs/tr/` are hand-written
> mirrors — when a reference changes, update the matching Turkish file and
> record the change (append-only, per rule R4).
