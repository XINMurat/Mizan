# Recovery — what to do when the audit itself goes wrong

Read this when a run stops behaving: a promised artifact did not run, a
claim will not settle, a result contradicts an entry you already wrote,
the audited document moved under you, or the session has gone soft.

Every other reference file in this skill describes the method working.
This one describes it **failing** — which is the more common case, and the
one where the damage is done quietly. A softened audit still looks like an
audit; a recovered-from failure looks exactly like no failure at all. That
is the same objection this skill makes to deleting `[R]` entries, turned
on the auditor.

The ramps are named `RR-nn` — `R-nn` in this project means a validator
rule, and a recovery ramp is not one. Each has the same shape:

```
TRIGGER      what you just observed
FIRST MOVE   what to do before anything else
FORBIDDEN    the shortcut that hides the failure instead of fixing it
OUTPUT       what you hand back -- never "resolved it"
BACKED BY    the rule, template or script that catches you if you skip it
```

**Name the ramp you are on, in the deliverable.** An audit that silently
recovered has an unmeasurable error rate, and an unmeasurable error rate
is the thing this skill exists to refuse.

---

## The failure classes these ramps exist for

The ramps are the remedies; these are the diseases. They are model failure
modes, not project mishaps — they recur across hosts and models because
they are properties of a producer that is also the judge.

| Class | How it shows up in an audit | Ramp |
|---|---|---|
| **Fabrication** | A fluent finding with no source. A cited paper that does not say that. A line number that does not exist. | RR-05 |
| **Silent gap-filling** | The claim was unverifiable, so an inference quietly took its place and got tiered as though checked | RR-05, RR-10 |
| **Finding inflation** | Twelve findings because twelve looks like work; severity raised so the report reads urgent | RR-06 |
| **Threshold theatre** | A precise-looking number whose arbiter is the author or nobody — *rigor cosplay* | RR-12 |
| **Threshold softening** | The result missed, so the threshold moves, or the near-miss becomes a hit | RR-02 |
| **Confirming your own output** | The run that wrote the entry decides the entry's tier | RR-00 |
| **Optimistic reporting** | "Verified", "validated", "cross-checked" with no artifact behind it | RR-01 |
| **Premise capture** | The audited document changed and the old findings were carried forward as if it hadn't | RR-08 |
| **Easy-claim bias** | Only the checkable claims were checked, and the result was presented as a full audit | RR-07 |
| **Context decay** | Hour three: tags in place, format intact, judgment gone; everything reads `[H]` by habit | RR-09 |

None of these is chosen. They are what a producer-judge does under
pressure to look useful, which is why each row points at a ramp and nearly
every ramp lands on a validator rule rather than on a paragraph.

---

## RR-00 — You are about to confirm your own tier

**TRIGGER.** The next thing you were going to do is verify, promote or
sign off on something produced earlier in this same run — your own
atomization, your own registry entry, your own gap map.

**FIRST MOVE.** Stop and declare the switch, in one line:

```
ROLE CHANGE: producer -> auditor of my own output.
Arbiter class: author. Highest tier reachable: [KKE] (independence).
```

Then either hand the artifact to a genuinely separate pass, or continue
with the tier capped. Both are legitimate; **an undeclared switch is not.**

**FORBIDDEN.** Promoting `[H]→[K]` on your own entry. Treating a second
model's agreement as independence — same training distribution, same
priors; agreement is evidence of shared bias as much as of correctness.
Recording `third_party` for an arbiter that is really you in a second
window.

**OUTPUT.** The declaration and the cap. If a separate pass is impossible
in this host, say that instead of implying it happened.

**BACKED BY.** The arbiter rule (an `author`-arbitrated claim can never
reach `[K]` and carries a permanent `[KKE]`), and the schema's
producer/auditor separation: propose tier changes, let the owner or a
separate pass confirm them.

---

## RR-01 — An artifact you promised did not run

**TRIGGER.** No shell, no PyYAML, no subagent, no spreadsheet library; or
the validator ran and raised.

**FIRST MOVE.** Diagnose before substituting. Which tool is missing, and
does its absence remove a **capability** or a **convenience**? Missing
PyYAML removes `mizan_validate.py`, which is the part of this method that
travels — that is a capability. A missing subagent removes fan-out speed;
targeted search gets the same result more slowly.

**FORBIDDEN.** Writing the output the tool would have produced. Prose
shaped like an artifact is a producer-side claim wearing a tool's
credibility — checklist item 10, committed by the auditor rather than
found in the audited document.

**OUTPUT.** The constraint, named where the coverage statement lives:
which check did not run, what the report therefore cannot claim, and the
fallback actually used. An audit under a constraint is not a smaller
audit; it makes a different claim.

**BACKED BY.** Operating assumptions (*never assume a tool exists*),
checklist item 10, A5 coverage.

---

## RR-02 — A result missed its threshold

**TRIGGER.** The test ran and the number fell short — or landed just
inside, which is the more dangerous case.

**FIRST MOVE.** Decide explicitly which of four things was wrong, and
decide it **before** touching anything:

1. **The claim** — the hypothesis is refuted. It becomes `[R]`, dated, in
   place.
2. **The mechanism** — the effect may be real but the stated cause is not.
   The entry is refuted *as written*; a rival mechanism is a NEW entry,
   not an edit to this one.
3. **The instrument** — wrong metric, wrong judge, an arbiter that cannot
   return this verdict. Fix the instrument, and re-calibrate the threshold
   against the new arbiter's own null; a threshold is never inherited
   across instruments.
4. **The precondition** — the test could not have been informative (the
   variant never learned the task, the sample never contained the case).
   Record "cell closed: precondition failed", which is its own outcome
   type and is **not** `[R]`.

**FORBIDDEN.** Moving the threshold after seeing the number. Re-running
until a friendly sample appears. Rewording the claim until it no longer
says the thing that failed — that is fake repair, and it leaves the
registry looking cleaner and meaning less. A near-miss is a near-miss.

**OUTPUT.** A dated result block appended to the entry, with the number
that refuted it and the honesty annex. The `[R]` entries are the
registry's own error rate; a registry with none has not been tested.

**BACKED BY.** R4 (append-only, `[R]` permanence), the "no threshold
shopping" anti-pattern, the arbiter rule on calibration, the
precondition/informativeness rule in Registry mode.

---

## RR-03 — The result will not reproduce

**TRIGGER.** The same test gives materially different verdicts across
runs, seeds, sessions or judges, and nothing about the target changed.

**FIRST MOVE.** Determinise before interpreting. In order of frequency:
the arbiter is a model and the prompt drifted; single seed reported as a
finding; the sample changed shape between runs; the threshold's quantity
was never pinned to a unit.

**FORBIDDEN.** Averaging until it stabilises. Reporting the run that
agrees with the entry. Dropping outliers under a rule invented after
seeing them — that is HARKing wearing a data-cleaning hat.

**OUTPUT.** Either a deterministic definition and a re-run, or the
instability recorded as a `[KKE]` naming the missing control, plus the
honesty annex it demands (single-seed caveat, instrument dependence).
Instability is a finding about the instrument, and a finding about the
instrument is worth more than a finding produced by an unstable one.

**BACKED BY.** Mandatory honesty annexes, R10 (a threshold names a
quantity), the arbiter's verdict latency and class.

---

## RR-04 — "The fix worked" — and something else moved

**TRIGGER.** Mode 4. The change went in, the symptom went away, and either
a different behaviour changed too, or a previously closed entry reopened.

**FIRST MOVE.** Treat the success as the suspicious result it is. "The fix
worked" is a **surprising positive** and needs the symmetric control
before any headline: would any perturbation of that area have produced the
same disappearance? Preregister that control as a sub-entry and run it. A
symptom that vanished is not a mechanism that was proven.

**FORBIDDEN.** Closing on the first story that fits. Stacking a second
change on the first to compensate — after two simultaneous changes there
is one observation and no attribution. Deleting the rival hypotheses that
the fix appeared to eliminate.

**OUTPUT.** The symmetric control's result, the rival hypotheses that
survive it, and — if something regressed — a new entry for the regression,
tiered on its own evidence. The original entry does not become `[R]` for a
regression: the diagnosis may have been right and the remedy wrong, and
collapsing those two is how a registry loses the distinction it exists for.

**BACKED BY.** R15 (a bug entry names at least one rival hypothesis), the
surprising-positive rule, R4.

---

## RR-05 — A claim you cannot settle

**TRIGGER.** You believe something is wrong — or right — but cannot name
the source, the line, the commit, or the mechanism. It "reads as"
overstated, inflated, hand-wavy.

**FIRST MOVE.** Do not tier it and do not fix it. Produce the **minimal
verification trace**: the smallest concrete thing that would settle it —
one file range, one commit, one query, one number someone else could
re-run.

- **Trace found** → it is a real finding. Tier it on what the trace shows,
  with the source cited.
- **Trace impossible, claim locatable** → `[H]` with a note saying what
  evidence would settle it and why that evidence is out of reach. This is
  the documented behaviour for an unverifiable claim: not silent
  acceptance, not silent rejection.
- **Not even locatable** → close it with the reason it could not be
  located, on the record. A closed intuition is a record; a vague finding
  in a registry is contamination the next reader cannot distinguish from
  evidence.

**FORBIDDEN.** "This section seems problematic." Tiering an impression.
Keeping it in the report because it might turn out to be right.

**OUTPUT.** A sourced finding, a noted `[H]`, or a written closure. All
three go on the record; only the first two carry weight.

**BACKED BY.** Audit mode step 2 (source each claim; unverifiable gets
`[H]` with a note), the "locate errors fully" framing rule.

---

## RR-06 — The finding count is climbing and nothing has been refuted

**TRIGGER.** Past a dozen findings, none `[R]`, none tested. Or the
opposite shape: every tiered entry came out `[K]`.

**FIRST MOVE.** Stop producing and start refuting. Take the three
highest-impact findings and ask, for each, what result would knock it
down. A finding with no such result is not audited, it is decorated —
`[S]` or nothing.

Then run the symmetric check on yourself: **if everything failed the
audit, suspect your own thresholds.** A demolition is as suspicious as a
uniform `[K]`; both are what an unanchored judge produces.

**FORBIDDEN.** Adding a finding because the report looks thin. Raising
severity so a minor claim surfaces. Both are the same move — buying
attention the evidence did not earn.

**OUTPUT.** A shorter list with refutation conditions attached, and the
count of candidates dropped. That count is often more informative than
what survived.

**BACKED BY.** W4 (a registry where every tiered entry is `[K]`), the
refutation-condition commitment, the tone rule on giving credit precisely.

---

## RR-07 — Only the easy claims got checked

**TRIGGER.** The checkable claims are done, the expensive ones are not,
and the report is about to go out as though it covered the document.

**FIRST MOVE.** Count before you conclude: **N of M claims checkable, and
which M−N were not, and why.** Then decide whether the unchecked remainder
is random or systematic. Systematic is the dangerous one — if every
unverifiable claim happens to be a load-bearing claim, the audit has
inverted itself and is grading the decoration.

**FORBIDDEN.** Presenting partial coverage as full coverage. Quietly
dropping a claim because checking it is expensive. Letting a phased audit
claim whole-target coverage before the merge row is written.

**OUTPUT.** An explicit coverage statement, and — for a phased run — the
Coverage Ledger row. The whole-target claim stays `[H]` until
reconciliation, and saying so is not a caveat, it is the finding.

**BACKED BY.** A5 (coverage stated explicitly), R16 (the Coverage Ledger
lives in the registry), the "auditing only what is easy" anti-pattern.

---

## RR-08 — The claim set moved mid-audit

**TRIGGER.** The document was edited, the PRD was revised, the code moved,
or the user corrected what the claim actually was — after findings had
been written against the earlier version.

**FIRST MOVE.** Version the target **first**, then re-derive. Record which
version each existing finding was written against. Findings against the
old version are not automatically wrong; they are *unverified against the
new one*, which is a different status and deserves a different word.

**FORBIDDEN.** Editing old findings in place so they read as though they
had always been written against the current text. In an append-only
family that is history falsification, and it is worse than the staleness
it hides.

**OUTPUT.** A version marker, a re-derived finding list, and the entries
whose tier dropped because their target no longer says that. The drift is
itself worth reporting: **a claim set that moves while being audited is a
claim set whose author is still deciding what it claims.**

**BACKED BY.** R4, tier drift as a finding, the dated-result-block
convention.

---

## RR-09 — The session has gone soft

**TRIGGER.** Long audit. You are reaching for tiers by habit, summarising
instead of citing, or cannot recall which entries are already written.

**FIRST MOVE.** Write the state down and cut. Flush every settled finding
into the registry, run the validator, write the Coverage Ledger row, and
add a short handover block: what is done, what is open, what runs next.
**The registry is the memory; the transcript is not.**

**FORBIDDEN.** Pushing on because the end feels close — the last claims
are then graded under the worst conditions of the whole run, and they are
graded as though they were graded under the first. Reconstructing an
earlier finding from memory rather than reading it back.

**OUTPUT.** A validated registry, a ledger row, and a clean phase
boundary. A fresh session reads those and loses nothing but the chat.

**BACKED BY.** Context economy (the phase boundary is a clean cut), R16,
R17 (an entry that stopped moving must be decided, not left to age).

---

## RR-10 — Ambiguity, or the artifacts contradict each other

**TRIGGER.** Two readings of a claim are defensible; or the comment, the
test, the docstring and the implementation disagree about what the code
does.

**FIRST MOVE.** Do not assume — and do not ask empty-handed. **Whoever
brings the question brings a recommendation and its reason.**

```
SITUATION:      <what is ambiguous, one sentence>
READINGS:       A <...>  B <...>
RECOMMENDATION: A
BECAUSE:        <tied to a source, not to plausibility>
COST IF WRONG:  <what taking A and being wrong costs the audit>
```

A recommendation can be disagreed with in one word; a bare question moves
the work back onto the person who asked for the audit. The decision is
still theirs: **a recommendation is not an answer, and an unanswered
recommendation is not consent.**

And a contradiction between artifacts is **a finding in its own right** —
it is precisely the claim-vs-evidence hop this skill exists to audit. The
team has been reading a description of a system it does not have.

**FORBIDDEN.** Picking the reading that makes the audit tidier. Recording
your own inference as the resolved answer. Four open questions in a row —
that is an interrogation, and it produces rubber-stamping.

**OUTPUT.** Either a decision from the owner, recorded with its source, or
both readings tiered separately with the ambiguity itself logged as a
finding.

**BACKED BY.** The claim-vs-evidence hop rule in Modes 3–5 (verifying that
a comment exists is not verifying its claim), tier drift.

---

## RR-11 — Demoting something you already promoted

**TRIGGER.** New evidence contradicts a tier you assigned — most sharply
when it is a `[K]` you wrote yourself.

**FIRST MOVE.** Acknowledge the contradiction explicitly and append the
demotion with its date and its cause. **Your prior outputs are auditable
claims too**, and this is the moment that principle either holds or
becomes decorative.

**FORBIDDEN.** Editing the earlier tier so the registry reads as though it
had always said `[H]`. Burying the demotion in a summary. Treating "I said
so earlier" as evidence — that is the confirmation loop the
producer/auditor separation exists to break.

**OUTPUT.** A dated demotion block naming what changed, plus a note on
what else rested on that entry. A demotion usually has dependents, and
they do not demote themselves.

**BACKED BY.** The framing rule on contradicting your own earlier output,
R4, tier drift as a finding.

---

## RR-12 — The threshold was missed and the urge is to optimise

**TRIGGER.** A number fell short and several changes are being proposed at
once — or the proposal is to keep the number and change the judge.

**FIRST MOVE.** One change, then re-measure with the **same instrument and
the same definition**. Two simultaneous changes produce one number and no
attribution: the result can neither promote nor refute either one.

Then check the arbiter before the number. If the judge is the author, the
threshold was decorative from the start and no amount of optimisation
fixes that — the entry belongs at `[S]` with the arbiter class stated,
rather than dressed in a number it cannot earn.

**FORBIDDEN.** Re-measuring under a new definition and comparing to the
old baseline. Swapping in a friendlier arbiter and inheriting the old
threshold. Declaring success from a metric with no baseline.

**OUTPUT.** One attributable delta, measured the same way, with the
alternative explanation hunted as hard as the favourable one. A flattering
result deserves the same scepticism as a disappointing one; it just rarely
gets it.

**BACKED BY.** R10, the arbiter rule (thresholds are calibrated against
the arbiter's own null and never inherited across instruments), the
surprising-positive rule, the threshold-theatre anti-pattern.

---

## Closing a run: the process scorecard

Fill this in when an audit or a registry cycle closes. Its purpose is
**not** to grade the audit — it is to find where the method leaks, and it
only works if it is filled in honestly. A high number is not a failure; a
hidden number is.

| Measure | Value | Reading |
|---|---|---|
| **Claims atomized / checkable** | / | The coverage ratio, stated as a number rather than as a hedge. A low ratio is a real result about the document: it was written to be unverifiable. |
| **Candidates raised / entered** | / | How many impressions survived RR-05. A ratio near 1.0 means nothing was filtered — finding inflation. |
| **Refuted (`[R]`)** | | Over total tested entries. **Zero is a warning, not a win:** a registry that has never been wrong has not been tested. |
| **`[KKE]` open at close** | | Controls that never ran. This is what the audit does not know, stated as a number instead of as silence. |
| **Arbiter distribution** | | How many entries are `runtime` / `instrument` / `third_party` / `author` / `none`. Heavy on the last two means the rigor is mostly form. |
| **Target versions** | | How many times the audited claim set moved (RR-08). High → the author is still deciding what they claim. |
| **Ramps used** | | Which `RR-nn` fired. A run that used none either went perfectly or did not notice. |
| **Escaped** | | Errors found later that this audit's scope covered and its checks missed. The only measure that comes from outside the audit, and the only one that cannot be gamed from inside it. |

**Reading:** two or three sentences. Not "the audit went well" — what
would change on the next run, and which number says so.

The scorecard is a claim like any other. Filled in by the run that
produced the audit, its arbiter class is `author` and it carries a
permanent `[KKE]` on independence. Say so rather than letting the table's
format imply otherwise.
