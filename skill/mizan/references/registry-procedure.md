# Registry mode — full procedure and schema rule history

Moved verbatim from SKILL.md (v2.9, lines 215-343) when the body was pruned (EVAL-008/009). Nothing here was rewritten.

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

**From schema 1.10, three rules close gaps the method itself had.** All three
came from one audit that MISSED four defects a user found by hand the same
day — every one of them lying BETWEEN slices, and none reachable by the
twenty-two rules that existed before them.
Each closes a place the method trusted without checking:

- **R23 — MERGE reconciles the pairs NOBODY LOOKED AT.** A `MERGE` row marked
  done carries `cross_slice`. A5.1's partition axes are all CONTAINERS while
  the escapes were RELATIONS, and MERGE's own description sent it after
  *findings already written down*. A defect living only in a seam appears in
  neither slice's findings, so reconciling them can never surface it.
- **R24 — the auditor's own instruments get calibrated too.** Every earlier
  measurement rule points outward; none asks whether the thing measuring
  works. That audit's ad-hoc scanners gave three different answers to one
  question on unchanged code. A scanner written during an audit is not a
  lesser instrument, it is an **uncalibrated** one.
- **R25 — a runtime verdict names the artifact it ran against.** `runtime` is
  the strongest arbiter class because a machine returns the verdict — which
  assumes it ran THE AUDITED CODE. A guard was measured three times (green,
  two-sided red, full suite passing) against a build that did not contain it.
  Not a weaker measurement: a **false assurance**.

- **R28 — the audit reads what was WRITTEN, not what gets PRODUCED.** The first
  rule here that doubts the INVENTORY rather than the reading. Slices are cut
  out of the source tree, which holds exactly what a human typed — so a
  generated config sits in no slice at all. Six phases, a MERGE, a bug registry
  and a security probe closed green while a packaging script wrote a BEL
  character into a shipped `web.config`: source correct, output corrupt,
  difference visible only in the generated file. `coverage.produced_artifacts`
  names them; **running the producer and reading its output** is what catches
  things.
- **W8 (warning) — can the arbiter return a verdict AT ALL?** Two-sidedness
  asks whether it can come out red; not whether it can come out. A hung run
  says nothing while looking exactly like patience — a suite sat twenty-five
  minutes at zero CPU, neither failing nor passing, and was about to be
  reported as verified. `failure_is_loud` is one line on how it fails.

The escapes, the numbers and what each rule would have caught are in
`references/code-audit.md` and `checklist.md` items 14–16.

The validator also has a **non-blocking warning channel** (W1–W8): a missing
two-sided statement, an entry written with no threshold or refutation and no
result yet, a registry where every tiered entry is `[K]`, and — from 1.10 —
**W6: every coverage phase done while the domain probe was never answered.**
R19 already blocks a tier-K claim over an unanswered probe, which is correct
but narrow: an audit settling for `[H]` never meets it. In the run that
produced W6 the probe was created on day one with `supplied_by: none` and
seven phases closed around it. Waiving is a decision; silence is not. These advise
rather than stop, for the same reason R8's flag classes differ in force — a
checker that can only block teaches people to write around it, which is a
different skill from writing honestly.

