# Modes — full text

Moved verbatim from SKILL.md (v2.9, lines 45-123) when the body was pruned (EVAL-008/009). Nothing here was rewritten.

## Two modes — decide which one applies

**Audit mode (retrospective).** The user hands you an existing claim set —
a summary, a review, a report, an AI-generated assessment — and wants to
know how much of it survives scrutiny. Deliver the Audit Report
(template in `references/templates.md`).

**Registry mode (prospective).** The user wants to track hypotheses going
forward — experiments, predictions, work-pattern claims, product bets.
Create or update a registry file using the Registry Entry template. The
registry is a living Markdown document the user keeps in their project.

If the user's request contains elements of both ("audit this, then set up
tracking so it doesn't happen again"), do the audit first, then seed the
registry with the surviving `[H]` claims as its first entries.

## Modes 3–7

The same discipline applies to code, with one structural difference: in a
codebase, the claim and its evidence live in DIFFERENT artifacts (name /
comment / docstring / test / implementation), and every hop between them
must be verified separately. Verifying that a comment exists is not
verifying that its claim is true.

**Mode 3 — Code audit.** The user wants an existing codebase or repo
analyzed. Code is a claim set even without documentation: every function
name, comment, docstring, test, type hint, config value, and commit
message makes a verifiable claim. Read `references/code-audit.md` before
the first code audit. Deliverable: an evidence-tiered behavior report
(which doubles as generated documentation when none exists) plus a Gap
Map of broken promises, untested surfaces, and deferrals. For a repo too
large to audit in one pass, do NOT force it — partition into sequential
phases sharing one append-only registry (procedure in `code-audit.md`
§A5.1; Coverage Ledger template in `templates.md` §5); this applies to
Modes 4 and 5 too.

**Mode 4 — Bug-hypothesis registry.** Debugging is hypothesis testing
usually performed as unrecorded HARKing. Each suspicion becomes a
preregistered entry: mechanism, refutation test, threshold — run, record,
never delete. "The fix worked" is a surprising positive: it needs the
symmetric control (did THIS mechanism fix it, or would any perturbation
have?). Covered in `references/code-audit.md`.

**Mode 5 — Feature / PRD gate.** A PRD is a claim set about the future:
user-problem claims, value claims, cost claims, dependency claims —
usually presented one tier above their evidence. Atomize and tier the PRD
BEFORE building; preregister the success metric AND the kill condition;
force alternatives (including the null alternative) before committing.
Read `references/feature-gate.md` before gating a feature or PRD. This
mode also generates feature candidates the user didn't ask for, via the
Gap Map and alternative-forcing — see that file's "suggestion mechanism"
section for what this can and cannot promise.

**Mode 6 — Meta-review.** Every ~10 entries, or on request: which
hypothesis TYPES hit, which instruments proved reliable, where bias is
accumulating. Not a summary — a hit rate ACROSS entries, the one thing a
per-entry discipline cannot see from inside any entry. Its output revises
the methodology: these instructions and the schema are claim sets too,
subject to their own rules, so a change is justified and the old version
is never deleted.

**Mode 7 — Security probe.** Modes 3–5 all start from a sentence someone
wrote; a vulnerability is the sentence nobody wrote, so the engine that
powers them cannot reach it (audit step 7 says why). Mode 7 changes the
scenario source to a trust-boundary map plus an adversary model, and
inverts what counts as evidence: **not exploited is not a pass** — a failed
attempt and a clean scanner are silence and cap at `[KKE]` (R26); only a
named control on every path to the asset promotes. R27 is R19 with the
supplier changed. Read `references/security-probe.md` before the first
security pass.

**Beyond software.** Modes 3/4/5 are domain-independent patterns
(claim-vs-evidence hop audit; anomaly → rival-hypothesis registry;
forward-commitment gate). For ANY domain outside software, read
`references/domain-adaptation.md` — the five-question adaptation recipe,
14 per-domain hop maps and confound catalogs, and the constraints that
transfer unchanged (append-only, DC-001 on individual hit rates,
permanent [KKE] where symmetric controls are impossible).

