---
name: mizan
description: Evidence-tiered claim auditing and preregistered hypothesis registries for documents, codebases, bugs, and features. Use whenever the user asks to evaluate, audit, review, or fact-check any claim set (AI-generated summaries, project reports, self-assessments, research writeups, year-in-reviews), wants honest rigor instead of praise, or mentions evidence tiers, preregistration, refutation conditions, HARKing, confounds, or hit rates. Also use to start or maintain hypothesis registries for experiments, decisions, or predictions. Also use for software work — auditing an existing codebase or repo (what comments, names, docs, and tests claim vs. what code does; generating evidence-tiered docs from undocumented code), tracking bug hypotheses while debugging, and gating new features or PRDs (tiering PRD claims, preregistering success metrics and kill conditions, generating alternatives from gap maps). Triggers include "değerlendir", "denetle", "önkayıt", "audit this repo", "bug hipotezi", "PRD'yi süz".
---

# Mizan — Evidence-Tiered Auditing & Preregistration Registry

Mizan (Turkish/Arabic: "the scale") turns a rigorous experimental-science
discipline into a portable tool for evaluating *any* claim set and for
maintaining living hypothesis registries. Its core commitments:

1. **Every claim gets an evidence tier.** No untagged assertions.
2. **Thresholds are locked before results.** If that's impossible
   (retrospective analysis), the HARKing risk is stated explicitly — never
   silently absorbed.
3. **Every hypothesis carries a refutation condition.** A claim that cannot
   fail is not audited, it is decorated.
4. **Refuted entries are never deleted.** They are marked `[R]` and archived
   in place. Negative results are first-class results.
5. **Surprising positives get a symmetric control before a headline.**
   A result that flatters the hypothesis is the one most in need of a
   confound check.
6. **Hit rates over curated examples.** Three confirming anecdotes are
   selection bias; a scored prediction record is evidence.

## Evidence tiers (use these exact labels, bilingual)

| Tag | TR | EN | Meaning |
|---|---|---|---|
| `[K]` | Kanıtlanmış | Proven | Direct evidence supports it; source cited; threshold met |
| `[H]` | Makul Hipotez | Plausible hypothesis | Theoretical grounding exists; empirical support missing or below threshold |
| `[S]` | Spekülatif | Speculative | Interesting; not currently testable or no test designed |
| `[R]` | Reddedildi | Refuted | Tested and failed its own threshold — kept on record, never deleted |
| `[KKE]` | Kritik Kontrol Eksik | Critical control missing | Result exists but a confound/baseline check that could flip it has not run |
| `[Y]` | Yanıltıcı | Misleading | Technically containing truth but framed to imply more than the evidence supports |

Tier drift is itself a finding: when a claim silently moved from `[H]` to
`[K]` between two documents without new evidence, flag it.

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

## Software modes (3, 4, 5)

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

**Beyond software.** Modes 3/4/5 are domain-independent patterns
(claim-vs-evidence hop audit; anomaly → rival-hypothesis registry;
forward-commitment gate). When the user applies Mizan to marketing
campaigns, sales deals, analytics reports, incident response,
root-cause analysis, hiring, procurement, investment theses, content,
program evaluation, or personal experiments — or any domain not listed —
read `references/domain-adaptation.md`: it contains the five-question
adaptation recipe, per-domain hop maps and confound catalogs, and the
hard constraints that transfer unchanged (append-only, DC-001 on
individual hit rates, permanent [KKE] where symmetric controls are
impossible).

## Audit mode — procedure

Read `references/checklist.md` before your first audit in a conversation;
it lists the failure modes to hunt for and worked examples.

1. **Atomize.** Decompose the document into individual checkable claims.
   A sentence like "you flagged r=0.997 as suspicious, which led to the
   init bug" is TWO claims (the flagging happened; it caused the discovery).
2. **Source each claim.** For every claim, identify what evidence would
   verify it and whether that evidence is accessible (conversation history,
   files, commits, logs, web). Actually check what is checkable — open the
   file, search the history, run the number. A claim you cannot verify gets
   `[H]` with a note, not silent acceptance and not silent rejection.
3. **Tier each claim** with the table above. Quote the claim, then the tag,
   then a one-line justification with the source.
4. **Hunt counter-examples.** For every pattern-claim ("you always X",
   "the system consistently Y"), actively search for instances of the
   opposite before accepting it. Report the search even when it comes up
   empty — "no counter-example found in N sources checked" is information;
   silence is not.
5. **Compute hit rates where possible.** If the document praises someone's
   judgment/predictions/instincts, reconstruct the full prediction record,
   not just the wins. A ~50-60% hit rate honestly reported is worth more
   than a 100% curated one — and say so.
6. **Name the missing card.** Every summary format structurally omits
   something (failures, deferrals, abandoned lines, costs). State what this
   document's format cannot show, and sketch it from available evidence.
7. **Declare the HARKing status.** Retrospective analysis selected its
   examples after seeing outcomes. Say this plainly in the report header —
   including about your own audit, which is also retrospective.
8. **Separate mechanism from motive.** When explaining why a document is
   skewed, prefer structural explanations (selection pressure, format
   incentives) over intent attribution ("they designed it to flatter") —
   unless intent is itself evidenced.

## Registry mode — procedure

1. **One entry per hypothesis**, using the Registry Entry template
   (`references/templates.md`). The entry is written BEFORE the test runs.
2. **Lock thresholds numerically.** "Improves things" is not a threshold;
   "ΔPPL ≤ −3%" or "counter-example rate < 1 per 10 sources" is.
3. **Write the refutation condition first**, and check the *two-sided
   informativeness* requirement: both possible outcomes must teach
   something. If only success is informative, redesign the test.
4. **State the informativeness precondition** where relevant: a test only
   counts if its preconditions held (e.g., a task-difference metric is
   meaningless if neither variant learned the task). Record "cell closed:
   precondition failed" as its own outcome type — distinct from `[R]`.
5. **On surprising positive results:** before promoting `[H]→[K]`, ask
   what symmetric/confound control would distinguish "the specific claim"
   from "a generic alternative", preregister that control as a sub-entry,
   and run it. The headline waits for the control.
6. **Status updates append, never overwrite.** Each result gets a dated
   result block. Post-hoc reasoning is allowed but must be labeled
   "sonradan akıl yürütme / post-hoc, not preregistered".
7. **Honesty annexes (dürüstlük şerhleri) are mandatory** on every result:
   scope limits, sample size, single-seed caveats, instrument dependence.
8. **Prior art is declared, not discovered by reviewers.** If the
   hypothesis has known relatives, name them in the entry and state where
   the originality claim actually lives.
9. **Name the arbiter of every threshold.** A locked numeric threshold is
   only as strong as the judge that returns its verdict, and that judge is
   what quietly disappears when this discipline moves off code: in a test
   suite the runtime decides, in a strategy memo the author decides while
   the paperwork looks identical. Record the arbiter's class — `runtime`
   (deterministic executor) / `instrument` (measurement independent of the
   author's opinion) / `third_party` (a judge other than the author) /
   `author` (self-judged) / `none` — plus the concrete judge and the
   verdict latency. Two hard consequences: an `author`-arbitrated claim
   can never reach `[K]`, it carries a permanent `[KKE]`; and with `none`
   the threshold is decorative, so say that and leave the entry at `[S]`
   rather than dressing an opinion in a number. Thresholds are calibrated
   against the arbiter's own null and are never inherited across
   instruments.

## Tone and framing rules

- Be direct about negative findings; do not soften with "more research
  needed" unless genuinely uncertain.
- Give credit precisely: when something survives the audit, say so with
  the same specificity used for failures. Mizan is not a demolition tool;
  a claim set where everything fails the audit should make you suspicious
  of your own thresholds.
- Locate errors fully: which claim, which source, what the mechanism of
  the error is, and what its quantitative impact is — not "this part may
  be problematic".
- After every diagnosis, give the next step, ordered by
  criticality × (impact / effort).
- When new evidence contradicts your own earlier audit output, acknowledge
  the contradiction explicitly and revise the tier. Your prior outputs are
  auditable claims too.
- Write in the user's language; keep the tier tags bilingual as in the
  table.

## Anti-patterns (refuse these politely)

- Producing a tiered report where every claim lands in `[K]` without
  checking sources — that is the flattery problem wearing a lab coat.
- Letting the user (or yourself) quietly raise a threshold after seeing a
  near-miss result. A near-miss is a near-miss; record it.
- Deleting or rewriting `[R]` entries "for cleanliness".
- Threshold theatre: attaching a precise-looking number to a claim whose
  arbiter is the author or nonexistent. The form of the code-verification
  loop without its judge is not rigor, it is rigor cosplay — and it is the
  single most likely way this methodology fails outside software.
- Auditing only the claims that are easy to check and presenting the
  result as a full audit — state coverage explicitly (N of M claims
  checkable).

## References

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
- `references/domain-adaptation.md` — Modes 3/4/5 beyond software:
  adaptation recipe + 14 domain modules (analytics, marketing, sales,
  research, finance, ops/RCA, security/IR, hiring, procurement, legal,
  UX research, content, policy, personal experiments).
- `schemas/mizan-registry.yaml` — the machine-readable registry format.
  When the user keeps a registry file (in project knowledge, a repo, or
  uploads one), read it at session start, APPEND rather than overwrite,
  propose new entries in this schema, and enforce its hard rules R1–R8
  (mandatory baseline, mandatory confound controls, append-only history,
  no K-promotion without controls on surprising positives, and
  producer/auditor separation: propose tier changes, let the owner or a
  separate audit pass confirm them).
