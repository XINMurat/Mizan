---
name: mizan
description: Evidence-tiered claim auditing and preregistered hypothesis registries for documents, codebases, bugs, and features. Use whenever the user asks to evaluate, audit, review, or fact-check any claim set (AI-generated summaries, project reports, self-assessments, research writeups, year-in-reviews), wants honest rigor instead of praise, or mentions evidence tiers, preregistration, refutation conditions, HARKing, confounds, or hit rates. Also use to start or maintain hypothesis registries for experiments, decisions, or predictions. Also use for software work — auditing an existing codebase or repo (what comments, names, docs, and tests claim vs. what code does; generating evidence-tiered docs from undocumented code), tracking bug hypotheses while debugging, and gating new features or PRDs (tiering PRD claims, preregistering success metrics and kill conditions, generating alternatives from gap maps). Triggers include "değerlendir", "denetle", "önkayıt", "audit this repo", "bug hipotezi", "PRD'yi süz".
license: MIT
metadata:
  author: XINMurat
  schema_version: "1.7"   # pinned to the schema banner by CI
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
7. **Probe the domain, not just the document.** Every step above starts
   from a sentence someone wrote, so none of them can find a capability
   that was never claimed — an absence produces no claim to tier. Obtain
   a list of situations that actually occur in this field and test each
   against the model: expressible (fine), inexpressible **and recorded as
   a deliberate boundary** (fine — that is a decision), inexpressible and
   **nowhere recorded** (finding). **You cannot write this list alone and
   must not pretend to:** ask the domain owner, and record who supplied
   the scenarios as part of the coverage statement. Invented
   plausible-sounding scenarios are fiction wearing an evidence tag.
   Scenarios written after a gap was found are HARKing and prove nothing
   about coverage — say which ones were retrospective.
   (Checklist item 12.)
8. **Re-assemble — audit the conjunctions, not only the claims.**
   Step 1 took the document apart; a defect that exists **only when two
   features hold at once** was destroyed by that very act and cannot
   reappear in any later step. So put things back together deliberately:
   for each feature, list the existing guarantees it can touch, and for
   each pair ask **"does that guarantee still hold while this feature is
   active?"** Prioritise (a) **derived signals** — anything computed from
   an absence changes meaning the moment a new state exists — and
   (b) **guarantees enforced call-site by call-site**, which any new bulk
   surface can bypass wholesale. Check ordering too: some pairs are safe
   in one direction only, and the required order is part of the finding.
   A green test suite is not counter-evidence here: tests are written per
   feature, so they attest to the parts and are silent about the pair.
   (Checklist item 13.)
9. **Close the loop — for an ongoing target, CREATE the registry, do not
   offer it.** When the audited thing is a living project (a repo, a
   backlog, a program) rather than a finished document, a one-shot audit
   cannot see gaps born after it ran. The audit's final act is therefore
   to WRITE the registry file (Registry mode, seeded with the surviving
   `[H]` claims and every recurring failure class found) and to name the
   trigger that re-runs the audit — a phase boundary, a release, a
   fixed cadence. Ending with "shall I set up tracking?" is a known
   failure of this skill: the offer gets deferred, the project keeps
   closing tasks, and the next audit arrives only after a user stumbles
   on a gap. If the user declines the registry, record the refusal in the
   report so the absence of continuity is itself on the record.
10. **Declare the HARKing status.** Retrospective analysis selected its
   examples after seeing outcomes. Say this plainly in the report header —
   including about your own audit, which is also retrospective.
11. **Separate mechanism from motive.** When explaining why a document is
   skewed, prefer structural explanations (selection pressure, format
   incentives) over intent attribution ("they designed it to flatter") —
   unless intent is itself evidenced.

## Registry mode — procedure

1. **One entry per hypothesis**, using the Registry Entry template
   (`references/templates.md`). The entry is written BEFORE the test runs.
2. **Lock thresholds numerically.** "Improves things" is not a threshold;
   "ΔPPL ≤ −3%" or "counter-example rate < 1 per 10 sources" is. A threshold
   alone does not survive contact with a determined author, so three companion
   fields are locked with it and checked by R18: **data status** (does the data
   already exist, and have you seen it — registration against seen data is
   postdiction, not preregistration), **stopping rule** (the n or the condition
   that ends collection, without which "collect until it crosses" is always
   available), and **exclusion rule** (which observations get dropped, decided
   before seeing them; `none` is an answer, silence is not). The
   open-science preregistration templates ask all three before anything else,
   and each closes a door this file already argued should be shut.
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

**From schema 1.4, four rules close the gaps between this file and the
data.** A `[K]` entry needs a threshold-meeting result or a cited external
source (R9) — prior art is not evidence for the claim, only context for its
originality. Thresholds name a quantity (R10), with a written justification
as the escape hatch for a genuinely categorical verdict. Every entry carries
a tier (R11), since "no untagged assertions" was never checked. And the
mandatory fields of the entry template are present (R12): `formal`, a
`metric` with a **named instrument**, `cost`, `status`, and `prior_art` —
where "no known relatives" is an answer and an absent field is silence.

**Bug entries and feature gates are hypotheses, not a different species.**
From schema 1.3 they carry the same fields and the same rules 1–9 above: a
bug's `formal` holds the MECHANISM (the symptom stays interpretation-free in
its own field), a feature's value metric IS `metric` and its success
threshold IS `threshold`. Three rules are specific to them, and each was
mandatory in `references/` long before anything checked it: a feature names
its **kill condition** (R13) and its **alternatives** including the null
option (R14); a bug names at least one **rival hypothesis** (R15). The point
of R15 is Mode 4's whole point — never close on the first story that fits.

**The Coverage Ledger lives in the registry (schema 1.5, rule R16).** For a
phased audit it is the one deliverable that DECIDES a tier — the whole-target
coverage claim stays `[H]` until the MERGE row is done — and it used to live
in a Markdown table no check could read. Keeping it in the registry follows
`code-audit.md`'s own description of it as "the append-only registry used as
the cross-phase carrier", and it means R4 protects its rows for free: a
re-scoped slice gets a new row, never an edit that erases the old one.

The validator also has a **non-blocking warning channel** (W1–W4): a missing
two-sided statement, an entry written with no threshold or refutation and no
result yet, and a registry where every tiered entry is `[K]`. These advise
rather than stop, for the same reason R8's flag classes differ in force — a
checker that can only block teaches people to write around it, which is a
different skill from writing honestly.

## Context economy (long audits, long sessions)

An audit's cost grows with the transcript, not with the finding. Every
turn re-sends the whole conversation, so a large one-pass audit gets
slower and more expensive with each exchange — and the last claims are
graded under the worst conditions. The mechanism already exists in this
skill: **A5.1's phased audit with an append-only registry as the carrier**
(`references/code-audit.md`). That is not a large-codebase special case;
it is the general shape. Apply it whenever an audit will not finish in a
few exchanges:

- **The registry is the memory, the transcript is not.** Append each
  finding to the file as it is confirmed, never batch them for a summary
  at the end. A finding that lives only in the conversation is lost at
  the next context reset — and paid for on every turn until then.
- **Read ranges, not files.** Locate with search, then open the lines you
  need. Whole-file reads of large artifacts are the single largest
  avoidable cost, and they persist for the rest of the session.
- **Fan-out searching belongs in a subagent — where one exists.** A sweep
  over many files should return its conclusion, not its raw material. If
  the host has no subagent, get the same effect with targeted search
  (locate, then open only the matching ranges); never let the method
  depend on a tool that may be absent.
- **A phase boundary is a clean cut.** Once the ledger and registry are
  written, the next phase can start in a fresh session: it reads the
  files, sees what is done, continues. Say so explicitly at the boundary
  instead of carrying the whole history forward out of habit.
- **State the cost honestly.** If coverage was reduced because the audit
  ran long, that is a coverage statement (A5), not an aside.

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
  auditable claims too. The procedure for the demotion — dated, appended,
  never edited in place — is `references/recovery.md` RR-11.
- **Never bring a question empty-handed.** Whoever raises an ambiguity, an
  open option or a blocked step brings their recommendation and its
  reason with it: situation, options, recommendation, why, and what it
  costs if the recommendation is wrong. A recommendation can be disagreed
  with in one word; a bare question hands the work back to the person who
  asked for the audit. The decision stays theirs — a recommendation is not
  an answer, and an unanswered recommendation is not consent.
- Write in the user's language; keep the tier tags bilingual as in the
  table.

## Operating assumptions (this skill runs inside someone else's setup)

This skill is loaded into a host that already has its own instructions —
a project's `CLAUDE.md`, org policy, other skills. Those instructions
take precedence over this file. That is correct, and it is also the most
likely way Mizan fails: **it degrades quietly.** A short, softened audit
still looks like an audit — tier tags in place, format intact, judgment
gone. That is this skill's own `rigor cosplay` anti-pattern, arrived at
from the outside.

- **Name the conflict; do not silently comply.** When a host instruction
  is incompatible with the method, say which instruction, which step it
  disables, and what the report can no longer claim — then let the user
  decide. Three collisions are common enough to watch for by name:
  a **brevity cap** (Mizan's value is the specificity — "which claim,
  which source, what mechanism"; capped output drops exactly that),
  an instruction to be **encouraging or positive** (this skill exists to
  refuse a uniform `[K]`), and a **pinned output language** (which
  overrides "write in the user's language" — keep the tier tags
  bilingual regardless, they are labels, not prose).
- **An audit run under a constraint states the constraint.** If the
  method was reduced, that belongs in the coverage statement (A5)
  alongside sampling — a constrained audit is not a smaller audit, it is
  an audit with a different claim.
- **Never assume a tool exists.** Subagents, spreadsheet libraries and
  shell access vary by host. Check before promising an artifact, and if
  it is missing say so and offer the explicit fallback. **Prose
  substituted silently for an artifact is a producer-side claim**
  (checklist item 10) committed by the auditor.
- **Load references on demand, not upfront.** `checklist.md` before the
  first audit, `code-audit.md` for software modes, `templates.md` when
  writing entries, `recovery.md` the moment a run stops behaving. Reading
  everything at the start spends the context the audit itself needs.
- **The scripted part is the part that travels.** `mizan_validate.py`
  enforces R1–R18 without a model, so it behaves identically in every
  host. Whatever is enforced only by this prose is negotiable by the
  host's prose. When rigor must survive an unknown setup, put it in the
  validator, not in a paragraph.

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

- `references/recovery.md` — the recovery ramps (`RR-00`…`RR-12`) for when
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
- `references/domain-adaptation.md` — Modes 3/4/5 beyond software:
  adaptation recipe + 14 domain modules (analytics, marketing, sales,
  research, finance, ops/RCA, security/IR, hiring, procurement, legal,
  UX research, content, policy, personal experiments).
- `schemas/mizan-registry.yaml` — the machine-readable registry format.
  When the user keeps a registry file (in project knowledge, a repo, or
  uploads one), read it at session start, APPEND rather than overwrite,
  propose new entries in this schema, and enforce its hard rules R1–R18
  (mandatory baseline, mandatory confound controls, append-only history,
  no K-promotion without controls on surprising positives, and
  producer/auditor separation: propose tier changes, let the owner or a
  separate audit pass confirm them).
