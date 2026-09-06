# Mizan — English Reference Index

The English canonical reference for the methodology lives inside the
portable skill package, so it stays in sync with what Claude actually
loads — and it is now published on this site too, generated from those
files by `tools/sync_en_docs.py` and checked in CI, so the English menu
offers the same documents the Turkish one does. This page is a map. The
Turkish full-text mirrors are in
[Kullanım kılavuzu](../tr/kullanim-kilavuzu.md), [Metodoloji](../tr/metodoloji.md),
[Yazılım modları](../tr/yazilim-modlari.md) and [Alan uyarlama](../tr/alan-uyarlama.md)
— or press **TR** in the header.

| Topic | English (canonical) | Turkish mirror |
|---|---|---|
| Methodology / core skill (Modes 1–2) | [Methodology](methodology.md) | [`docs/tr/metodoloji.md`](../tr/metodoloji.md) |
| Templates (registry entry, result block, audit report) | [`skill/mizan/references/templates.md`](../../skill/mizan/references/templates.md) | [`docs/tr/metodoloji.md` §2](../tr/metodoloji.md) |
| Failure-mode checklist (HARKing, tier drift, …) | [`skill/mizan/references/checklist.md`](../../skill/mizan/references/checklist.md) | [`docs/tr/metodoloji.md` §3](../tr/metodoloji.md) |
| Recovery ramps (RR-00…RR-13), model failure classes, closing scorecard | [`skill/mizan/references/recovery.md`](../../skill/mizan/references/recovery.md) | [`docs/tr/metodoloji.md` §4](../tr/metodoloji.md) — ramp table and failure classes; the per-ramp long form stays English-only |
| Software modes 3–4 (code audit, bug registry) | [Software modes](software-modes.md) | [`docs/tr/yazilim-modlari.md`](../tr/yazilim-modlari.md) |
| Software mode 5 (feature / PRD gate) | [Software modes](software-modes.md) | [`docs/tr/yazilim-modlari.md`](../tr/yazilim-modlari.md) |
| Domain adaptation (14 domains beyond software) | [Domain adaptation](domain-adaptation.md) | [`docs/tr/alan-uyarlama.md`](../tr/alan-uyarlama.md) |
| Machine-readable registry schema (R1–R22) | [`skill/mizan/schemas/mizan-registry.yaml`](../../skill/mizan/schemas/mizan-registry.yaml) | same file (comments EN) |

## English-only long-form docs

- [Usage guide](usage-guide.md) — install, workflows, hard rules.
- [Project instructions](project-instructions.md) — the block to paste
  into a Claude Project.

> **Maintenance note:** the skill package is the single source of truth in
> English. The pages linked above under `docs/en/` are generated from it —
> do not edit them; run `python tools/sync_en_docs.py`. The Turkish files in
> `docs/tr/` are hand-written mirrors — when a reference changes, update the
> matching Turkish file and record the change (append-only, per rule R4).
