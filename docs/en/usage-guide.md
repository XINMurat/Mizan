# Mizan System — Usage Guide (v1.0)
### Evidence-tiered research & engineering discipline: install, workflows, rules

> Turkish original: [`docs/tr/kullanim-kilavuzu.md`](../tr/kullanim-kilavuzu.md)

This guide is the permanent reference. The system has three layers, based
on the architecture that survived the audit of the original proposal — the
rest was discarded:

| Layer | Component | Responsibility | Where it lives |
|---|---|---|---|
| Behavior | userPreferences + Mizan Project Instructions | How the AI behaves | Claude settings + Project instructions |
| Audit | Mizan skill (v2.1) | How a claim is evaluated | Installed as a skill |
| Data | mizan-registry.yaml | How research knowledge is stored | Project knowledge / repo |

The three layers work independently: the schema is readable without the
skill, and the skill audits without the schema. Together they are the full
system.

---

## 1. Install (once)

1. **Skill:** upload `mizan.skill` to Claude (Settings → Capabilities →
   Skills). On updates, upload the new version over the old one — it does
   not auto-update. Current version: v2.1 (5 modes + schema).
2. **Project instructions:** paste the block from
   [`project-instructions.md`](project-instructions.md) into the
   "Project instructions" field of every Claude Project you run with Mizan.
3. **Schema:** copy the `mizan-registry.yaml` template, fill in your
   project name, and add it as a file to Project knowledge OR keep it in
   your repo (recommended: in the repo — the git diff IS the schema's
   design rationale).
4. **For other AIs:** the schema and documentation are model-independent.
   If you give ChatGPT/Gemini the schema file + this documentation, they
   work with the same discipline (with a weaker triggering guarantee).

## 2. Daily workflows

### 2.1 New hypothesis (preregistration)
When a testable claim arises: say "preregister this in the registry" or
approve Claude's suggestion. Claude produces an H-entry in schema format —
the threshold and refutation condition are LOCKED BEFORE ANY RESULT IS
SEEN. Add the entry to your registry file (Claude cannot directly edit the
file in project knowledge; it produces the up-to-date block and you paste
it — if you work in a repo, Claude Code can write it directly).

### 2.2 Experiment and result
Two fields are non-negotiable in an experiment entry: `baseline` (if none,
a written justification; a baseline-less experiment can never promote a
hypothesis to `[K]`) and `confound_controls` (each item in the
hypothesis's confound list is either controlled or explicitly accepted as
a risk). The result block is append-only; `honesty_annexes` cannot be
empty.

### 2.3 Surprising-positive protocol
If a result is better than expected, mark `surprising_positive: true` and
the `[K]`-promotion waits for the symmetric control ("is it this specific
mechanism, or a generic alternative?"). The headline is published after
the control.

### 2.4 Audit requests (Mode 1)
Hand over any claim set — an AI summary, report, or self-assessment — by
saying "audit this with Mizan". Output: a coverage declaration, a tiered
claim table, a counter-example sweep, a hit rate, the missing card, and
next steps.

### 2.5 Code audit (Mode 3)
"Audit this repo/module with Mizan." Claude extracts a claim inventory
(tests → comments → names → docs), verifies each hop separately (a
comment's existence ≠ a behavior's existence), and produces an
evidence-tiered behavior report + a Gap Map. In an undocumented project,
that report IS the documentation. A coverage declaration is mandatory on a
large codebase — a sampled audit is never presented as a full one. When you
want *full* coverage on a repo too big for one pass, ask Claude to phase it:
sequential slices sharing one append-only registry plus a Coverage Ledger
(procedure in `code-audit.md` §A5.1) — no need to hold the whole repo in
one session.

### 2.6 Bug hunt (Mode 4)
When starting to debug: "register this as a bug hypothesis." The symptom
(no interpretation), the mechanism hypothesis (specific enough to be
wrong), a rival hypothesis, and a refutation test are recorded. "The fix
worked" is a surprising positive: no mechanism becomes `[K]` without a
revert-check. After 10–15 entries you get your real bug-instinct hit rate.

### 2.7 Feature gate (Mode 5)
For a new feature/PRD: "gate this." The PRD is atomized (problem / value /
cost / dependency / scope claims are tiered — dependency claims are
verified NOW, not mid-sprint), the success threshold AND the kill
condition are preregistered, and alternative-forcing is applied (≥1
cheaper alternative + the null alternative, on the same metric).
Acceptance criteria are written as refutation conditions. Candidates from
the Gap Map are an evidence-carrying, ready-made backlog.

### 2.8 Meta-review (Mode 6 behavior)
Every ~10 entries or on request: which hypothesis types hit, which
instruments are reliable, where bias is accumulating. The output feeds the
methodology — the instructions and schema are themselves subject to
revision (following their own discipline: changes are justified, history
is never deleted).

## 3. Hard rules (summary — R1–R7 in the schema)

1. Threshold + refutation condition before any result (HARKing structurally closed).
2. Baseline mandatory; a baseline-less result cannot produce `[K]`.
3. Every confound is either controlled or an explicitly accepted risk.
4. History is append-only; `[R]` is never deleted.
5. Honesty annexes cannot be empty.
6. Surprising positive → symmetric control before promotion.
7. Producer ≠ sole auditor: a tier change is proposed, then the owner /
   a separate audit confirms it. (RSI safety: the agent that writes its
   own result cannot promote its own hypothesis.)

## 4. Common mistakes

- **Turning the schema into a form:** not every chat idea needs
  preregistration; exploratory conversation is free. Preregistration kicks
  in the moment you decide a claim goes to a resource-consuming test.
- **Threshold shopping:** "essentially met" is forbidden; a near-miss is a
  near-miss, with a single justified rerun allowed.
- **Counting comment-existence as behavior-evidence** (in code audit):
  each hop is verified separately — this was the system's first live
  finding (discovery.py:105, a "2 levels" comment vs. an unbounded rglob).
- **Treating audit output as final:** an audit is also a retrospective
  document; read its coverage declaration, note the inaccessible sources.
- **Bloating the registry into one file:** one registry per project; at
  100+ entries, split by area (registry-bugs.yaml, registry-feat.yaml).

## 5. First real task (preregistered)

Migrating your SpectralLM experiment registry
(experiment_registry_and_metrics.md) to the mizan-registry.yaml schema —
with the threshold locked last session: the schema carries ≥20 real
entries without requiring a structural rewrite AND is read and updated at
least once by a tool/model other than you → then the standardization
discussion opens. Otherwise the ORP idea is `[R]` and the schema stays a
personal tool — which is also a valid outcome.

## 6. File inventory

| File | Contents |
|---|---|
| mizan.skill | Skill package v2.1 (5 modes + embedded schema) |
| mizan-registry.yaml | Schema template (standalone copy) |
| docs/en/project-instructions.md | Project instructions block + diff analysis |
| skill/mizan/SKILL.md + references/ | Mode 1–5 English reference |
| docs/tr/ | Full Turkish documentation |
| This guide | Install, workflows, rules |
