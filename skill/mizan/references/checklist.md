# Mizan Failure-Mode Checklist

Hunt for these in every audit. Each item: what it is, how to detect it,
and a compact worked example.

## 1. HARKing (Hypothesizing After the Results are Known)
- **What:** thresholds or hypotheses chosen after seeing outcomes,
  presented as if chosen before.
- **Detect:** ask "when was this success criterion written relative to the
  result?" If the document can't answer, assume after.
- **Example:** a review says "the pyramidal architecture was the key bet" —
  but contemporaneous records show five parallel bets; the winning one was
  retroactively promoted to "the" bet.
- **Note:** retrospective analysis cannot avoid HARKing; it can only
  DECLARE it. The sin is the silence, not the retrospection.

## 2. Selection bias / curated examples
- **What:** pattern-claims supported only by confirming instances.
- **Detect:** for every "always/consistently/reliably", demand the
  denominator. Search for disconfirming instances yourself.
- **Example:** "you flagged the suspicious number three times" — true; the
  full record also contains two flagged numbers that were fine and one
  unflagged number that was the real bug. Hit rate 3/6, not 3/3.

## 3. Missing confound / symmetric control
- **What:** a positive result attributed to the specific mechanism without
  ruling out a generic alternative that would produce the same number.
- **Detect:** ask "what boring explanation produces this result?" and
  check whether it was tested. Mark `[KKE]` if not.
- **Example:** adding input-dependent phase improved perplexity +6.75% →
  headline "geometry matters". Symmetric control (same extra projection
  routed to amplitude instead) improved +16.4% → the gain was generic
  input-conditioning capacity, not phase. The headline flips.

## 4. Survivorship in the format itself
- **What:** the document type structurally cannot represent failures
  (year-in-review cards, highlight reels, launch posts).
- **Detect:** ask what a maximally honest version of this format would
  contain that this instance doesn't. Name the missing card.
- **Example:** a four-card strengths summary has no card for deferred
  work, abandoned lines, or the incident that forced a reformat — yet
  those are equally characteristic patterns in the same evidence base.

## 5. Tier drift
- **What:** a claim's certainty silently escalating across retellings —
  `[S]` in the lab notebook, `[H]` in the report, `[K]` in the deck.
- **Detect:** when multiple documents exist, diff the modal verbs and
  hedges around the same claim.
- **Example:** "may correspond to GPT-2-level performance" (notebook) →
  "GPT-2-level performance" (summary). The vocabulary-size artifact that
  invalidated the comparison never made the summary.

## 6. Threshold shopping / moving goalposts
- **What:** a near-miss reinterpreted by adjusting the bar after the fact.
- **Detect:** compare the recorded threshold to the language around the
  result ("essentially met", "just under", "directionally correct").
- **Rule:** a near-miss is recorded as a near-miss. One preregistered
  rerun with stated changes is legitimate; silent reinterpretation is not.

## 7. Precondition failure disguised as evidence
- **What:** a null or positive result reported from a test whose
  informativeness precondition failed.
- **Detect:** check whether the test could have detected the effect at
  all (did the model learn the task? did the instrument have the
  sensitivity? was the sample non-degenerate?).
- **Example:** "no difference between variants" on a task NEITHER variant
  learned (both at chance) — the cell closes as "precondition failed",
  it does not count for or against the hypothesis.

## 8. Instrument-dependence unstated
- **What:** a measured quantity presented as a property of the subject
  when it is a property of subject × instrument × conditions.
- **Detect:** ask "would a different window/tokenizer/timeframe/sample
  change this number?" If plausibly yes, the honesty annex must say so.
- **Example:** a "selectivity demand" score changed from 0.139 to 0.378
  purely by changing the measurement window; the first number alone told
  a false story.

## 9. Motive smuggled into mechanism
- **What:** explaining a skewed document by intent ("designed to
  manipulate") when structure suffices (selection pressure, incentives).
- **Detect:** can the skew be produced by an optimization process with no
  flattering intent anywhere? Then say that; reserve intent claims for
  evidenced cases.

## 10. Producer-side claim (the unreachable capability)
- **What:** a claim verified entirely on the PRODUCING side — the system
  writes the row, emits the event, computes the value — while the
  CONSUMING side (can a user actually reach it?) was never checked. The
  claim is true and the capability is absent.
- **Detect:** for every "X is produced / recorded / stored / emitted",
  ask "through which surface does someone read X, and was that surface
  exercised?" In software, diff the endpoint list against the calls the
  client actually makes, and the table list against the read paths.
  Anything produced but unreachable is `[Y]`, not `[K]` — the acceptance
  criterion passed, the promise did not.
- **Example:** a task closed as "notifications (in-app + email) done" on
  the criterion *"the relevant event produces a notification"*. Endpoints
  and twelve tests existed; the frontend contained zero notification
  calls. One test was even named `read_all_clears_the_badge` — guarding a
  badge that was never built. Same class had already recurred three times
  in that project (audit log written but never displayed; delete endpoint
  with no UI; password-change endpoint with no UI) and none of the four
  was found by the plan — each surfaced by accident.
- **Why it survives review:** the acceptance criterion is written by the
  layer that owns the producing side, and it is *correct for that layer*.
  The gap lives between tasks, so no single task's checklist can see it.
  Cutting a backlog by layer (BE/FE) makes this the default failure.

## 11. The auditor's own blind spot
- **What:** the audit itself is a retrospective document with coverage
  limits and its own selection effects.
- **Rule:** every audit report opens with a coverage statement (N of M
  claims checkable, which sources were inaccessible) and treats the
  auditor's prior outputs as auditable claims. When later evidence
  contradicts an earlier tier you assigned, revise it visibly.

## 12. The never-claimed capability (model–reality gap)
- **What:** the audit finds nothing wrong because there is nothing to
  find *in the document*. Every claim checks out, every tier is honest —
  and a situation that routinely happens in the domain cannot be
  expressed by the system at all. **An absent capability makes no claim,
  so claim-auditing is structurally blind to it.** Item 10 is its
  near neighbour and is NOT the same: there, a promise was made and only
  half-delivered; here, the promise was never made, so no amount of
  atomizing the document will surface it.
- **Detect:** the input for this probe is **the domain, not the
  document**. List the situations that actually occur in this field, then
  ask of each: can the model express it? Three outcomes —
  (a) expressible → fine; (b) inexpressible **and written down as a
  deliberate boundary** → fine, that is a decision; (c) inexpressible
  **and nowhere recorded** → finding. An undocumented gap is always worse
  than a decided limit, because no one chose it.
- **Honest constraint — you cannot generate this list alone.** The
  auditor knows the artifact; only someone who knows the field knows what
  happens in it. **Ask.** An audit that skips the asking and invents
  plausible-sounding scenarios is producing fiction with an evidence tag
  on it. Record who supplied the scenarios; that provenance is part of
  the coverage statement.
- **Example:** a process-memory application passed a full claim audit
  (61 endpoints, 20 tables, producer/consumer diff, item-10 sweep). Ten
  design gaps were found *afterwards*, none by that audit, all by the
  domain owner asking ordinary questions: *"can two people work the same
  step?"* (no lock existed; the second writer silently overwrote the
  first one's signature), *"how does work move between two departments?"*
  (the model had one unit per process and the concept was neither built
  nor rejected), *"what happens when a process is retired?"* (an
  `archived` status was defined and written by no endpoint — while the UI
  actively told users to archive). The audit had even declared its own
  limit correctly: *"I could not find the classes I do not know about,
  and I cannot count what I did not find."* That declaration was right,
  and it was not a method.
- **Why it survives review:** every other checklist item starts from a
  sentence someone wrote. This one has no sentence to start from. It is
  the only item whose evidence is an **absence**, which is why it must be
  driven by an external list prepared in advance (see SKILL.md audit
  step 7) rather than by reading harder.
- **Seed list — how to ask, when the domain owner is in the room.** The
  constraint above stands: you cannot write the scenarios. You *can* write
  the prompts that make someone else's knowledge surface, and asking "what
  situations occur in your field?" cold reliably produces nothing. These
  eight classes are domain-independent because they are properties of any
  system with state, people and time in it — every one of them has produced a
  real finding in this checklist's own examples. Turn each into a question in
  the owner's vocabulary, ask it, and record the answer as a scenario:
  1. **Two at once** — can two people do this to the same thing at the same
     time? (The concurrent-signature overwrite.)
  2. **End of life** — what happens when this thing is finished, retired,
     cancelled, archived? (The `archived` status no endpoint ever wrote.)
  3. **Crossing a boundary** — how does work move between two units, teams,
     departments, tenants? (The handoff the model had no concept for.)
  4. **The person leaves** — who holds this when its owner is gone, on leave,
     deactivated? (The task claimed by someone who will never return.)
  5. **Zero, one, very many** — the empty case, the single case, and ten
     thousand. Which of the three did nobody try?
  6. **Undo and exit** — reversing it, deleting it, taking the data out.
     Exits are designed last and used first when things go wrong.
  7. **Out of order, half-done** — the step done twice, done backwards, or
     interrupted midway. What state does that leave?
  8. **Who may see it** — the same object seen by a different role, an
     outside party, an auditor, a bulk export.
  The list is a **prompt for the asking, never a substitute for it**: the
  answers are the evidence, and an auditor who fills these in alone has
  written eight plausible fictions instead of one. Record the answers as
  `probes.domain.scenarios` with `supplied_by` naming who actually spoke, and
  add each phase's scenarios before that phase begins (below).
- **Preregistration rule:** scenarios written *after* a gap is found are
  HARKing (item 1) and prove nothing about coverage. Their value is
  entirely in the gaps not yet known, so each new phase must add its
  scenarios **before** the phase's work begins, and the report must state
  plainly which scenarios were retrospective.

## 13. The unaudited conjunction (each feature correct, the pair broken)
- **What:** every feature is individually correct, individually tested,
  individually tiered `[K]` — and two of them held **at the same time**
  break a guarantee that neither one owns. Items 10 and 12 are about a
  single thing (half-delivered, or never built). This one is about a
  **pair**, and it is invisible to any procedure that atomizes: atomizing
  is precisely the act of taking claims apart, so a defect that exists
  *only in the conjunction* is destroyed by step 1 of the audit.
- **Detect:** do not ask "is this feature correct?" — ask **"which
  existing guarantee can this feature touch, and does that guarantee
  still hold while this feature is active?"** Build the pair list
  deliberately: new feature × every guarantee it can reach. Two classes
  are especially fragile:
  - **Derived signals.** Anything computed from an absence ("no one has
    touched this in 3 days", "unassigned", "not yet read") silently
    changes meaning when a new state is introduced.
  - **Guarantees enforced in one place.** A privacy rule proven across
    five call sites is voided by a sixth surface that bypasses them —
    bulk export being the classic one.
- **Ordering counts.** Some conjunctions are not symmetric: the pair is
  safe in one order and broken in the other. State the required order as
  part of the finding, not as an implementation detail.
- **Examples (one session, five findings, none from claim-auditing):**
  *pause × staleness signal* — pausing work is correct, flagging
  untouched work is correct; together, pausing becomes the cheap way to
  hide stuck work and the flag dies of noise. *mute × handoff
  notification* — notification preferences are correct, cross-team
  handoff alerts are correct; together the handoff can be silenced and
  the system reports success while no one is told. *claim × departure* —
  claiming a task is correct, deactivating a leaver is correct; together
  the task is held by someone who will never return, and a timeout that
  assumes "busy" cannot tell that from "gone". *export × private notes* —
  a report generator is correct, per-note privacy is correct; one button
  voids the other. *anonymisation × open work* — both correct, but only
  in one order: anonymise first and the owner of the work to be
  reassigned is no longer readable.
- **Why it survives review:** each feature's acceptance criteria are
  written by whoever owns that feature, and are *correct for it*. The
  defect lives between two owners, so no single criterion can see it —
  the same structural reason item 10 survives, one level up. Tests
  inherit the flaw: they are written per feature, so a green suite is
  evidence about the parts and says nothing about the pair.
- **Where it is recorded:** `probes.conjunction.pairs` in the registry
  schema (R20). A pass that leaves no row is indistinguishable from a
  pass that was skipped, and this one is skipped by default.
- **Cost of finding it late:** cheap on paper, expensive in code. These
  are model-level conflicts; discovered during design they are one
  decision, discovered after shipping they are a migration.
