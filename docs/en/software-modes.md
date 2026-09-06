<!-- GENERATED PAGE - do not edit here.
     Source of truth: skill/mizan/references/code-audit.md, skill/mizan/references/feature-gate.md
     Regenerate:      python tools/sync_en_docs.py
     CI (`--check`) fails if this page drifts from its source. -->

# Software modes 3–5 — code audit, bug registry, feature gate

> **Mirrored from the skill package.** This is the canonical English text that
> Claude actually loads, published here so it can be read next to its Turkish
> mirror instead of only on GitHub. Edit the sources above, not this
> page; the Turkish mirror is `docs/tr/yazilim-modlari.md`.

## Mizan Code Audit & Bug-Hypothesis Registry (Modes 3–4)

### Part A — Code audit (Mode 3)

#### A1. Claim inventory — where claims live in code

Extract claims from, in order of evidential weight:

1. **Tests** — the strongest claim source. Every assertion is a threshold
   that was (usually) locked before results: an existing preregistration
   registry. Read the test suite FIRST when documentation is absent.
2. **Implementation-adjacent text** — comments, docstrings. These claim
   behavior; the implementation is the evidence. Verify the hop.
3. **Names** — function/class/variable names are promises
   (`validate_input`, `sanitize`, `cache`, `thread_safe`).
4. **External docs** — README, wiki, PRDs, commit messages. Furthest from
   the code; highest drift risk.
5. **Structure** — config values, type hints, error messages, dependency
   pins (a pin claims compatibility).

#### A2. Tier mapping for code claims

| Tier | Meaning in code |
|---|---|
| `[K]` | Claim backed by a passing test that could actually fail (see A4) or verified directly against the implementation/execution |
| `[H]` | Claim exists in name/comment/doc; no covering test; implementation not contradicting but not confirming |
| `[KKE]` | A test exists but does not cover the edge that would falsify the claim (e.g., a "deep discovery" test that never tests depth) |
| `[Y]` | Name/doc promises more than the code delivers (a `sanitize` that only trims whitespace) |
| `[R]` | Implementation directly contradicts the claim (a "2 levels deep" comment above an unlimited `rglob`) |

**The hop rule:** comment existence ≠ behavior existence. Docstring ≠
test. Test name ≠ test content. Tier each hop separately; a claim's tier
is the tier of its WEAKEST verified hop.

**The reachability hop (mandatory, run it explicitly).** Production ≠
availability. A value written to a table, an event emitted, a row logged
— none of it is a delivered capability until something a user operates
can read it. This hop is invisible to per-unit review because it lives
BETWEEN units, so audit it as its own pass with two cheap diffs:

- **Endpoint → client:** enumerate server routes; enumerate the calls the
  client actually issues; the difference is unreachable surface.
- **Store → read path:** enumerate tables/collections; for each, find the
  code path that reads it for a user. Zero read paths = dead surface
  (either an unregistered deferral or a broken promise).

Report both denominators ("57 of 61 routes reachable, 17 of 20 tables
read") — the ratio is what tells you whether you found an exception or a
pattern. See checklist §10.

#### A3. Drift catalog (code versions of checklist items)

- **Comment–code drift** = tier drift: the comment described an old or
  intended implementation; code moved, comment didn't. Detect with
  `git log -L` on the comment vs. the code below it — if the code changed
  after the comment was last touched, flag.
- **TODO/FIXME inventory** = unregistered deferrals. Extract all, date
  them via `git blame`, list in the Gap Map. A 2-year-old TODO is a
  deferral pattern, not a plan.
- **Dead code** = abandoned `[S]` entries. Unreferenced functions,
  unreachable branches, feature flags never flipped.
- **Doc–code drift**: README claims vs. actual CLI flags/API surface.

#### A4. Test-quality audit — the confound control for `[K]`

A test that cannot fail is decoration (two-sided informativeness applied
to test suites). Before promoting a claim to `[K]` on the strength of a
test:

- Check the assertion actually exercises the claimed behavior (not just
  "function runs without exception").
- Where available, use **mutation testing** (mutmut, cosmic-ray, Stryker)
  as the systematic control: if mutating the implementation doesn't kill
  the test, the test wasn't guarding the claim.
- Cheap manual version: deliberately break the claimed behavior locally;
  if the suite stays green, the claim's `[K]` was false — mark `[KKE]`.

#### A5. Scale, sampling, and the coverage statement

Full atomization is impossible beyond small codebases. Mandatory
practice:

- Declare scope up front: which modules/paths audited, by what selection
  rule (risk-weighted: entry points, security surfaces, money paths,
  recently-churned files via `git log --stat`).
- Report coverage: "N of M modules, K of L public functions."
- Never present a sampled audit as a full one.

#### A5.1. Phased audit for large codebases (full coverage without one-pass blow-up)

Sampling (A5) trades coverage for feasibility. When the user wants *full*
coverage on a repo too large to atomize in one pass, partition the work
into sequential phases instead — each phase small enough to audit
completely, all phases sharing one append-only registry as their memory.
This is not a new mechanism: it is the append-only registry (rule 4) used
as the cross-phase carrier, exactly as an existing registry file already
persists across sessions.

Procedure:

1. **Phase 0 — scoping only (cheap).** Do NOT atomize yet. Build the
   module/path map and risk-rank it (A5 selection rule: entry points,
   security/money surfaces, recently-churned files). Emit a **partition
   plan**: phases P1..Pn, each a bounded slice (by module, path, or
   surface) that fits one pass. Write the plan into the Coverage Ledger
   (template in `templates.md` §5) with every phase marked `⏳ planned`.
2. **Phase k — one slice, fully.** Run Mode 3 (or 4) completely on slice
   Pk only. APPEND findings to the single registry / behavior report;
   never rewrite prior phases' entries. Update the Coverage Ledger row:
   `✅ done`, with the "K of L functions" for that slice. Each phase can
   run in a fresh session — it reads the ledger + registry, sees what is
   done, continues.
3. **Merge — cross-phase reconciliation (mandatory, do not skip).**
   A final pass reconciles claims that cross slice boundaries: tier drift
   between modules, duplicate findings, and — the real risk — hops where
   a claim in slice A is verified only by evidence in slice E. Naive
   partitioning MISSES these; reconciliation is where phased audit is
   weakest, so name it explicitly. Until this pass runs, the audit's
   coverage claim is `[H]`, not `[K]`: "each slice fully audited" ≠ "the
   repo fully audited", and presenting it as the latter is itself a `[Y]`.

The Coverage Ledger IS the deliverable's scope statement (A5): it shows
at any moment which slices are `[K]`-covered, which are pending, and
whether reconciliation has run.

#### A6. Deliverables

1. **Evidence-tiered behavior report** — every statement carries a tier
   and a source (file:line, test name, or run output). When the project
   has no documentation, this report IS the documentation — generated
   docs where each sentence is tagged `[K]`/`[H]` instead of aspirational
   prose.
2. **Gap Map** — the missing-card analysis for code:
   - `[R]` findings → broken promises (fix the code or fix the claim)
   - `[KKE]` findings → untested surfaces (hardening candidates)
   - `[Y]` findings → promise–delivery gaps (fulfill or rename)
   - TODO/dead-code inventory → deferral record
   The Gap Map feeds Mode 5's feature suggestions.

### Part B — Bug-hypothesis registry (Mode 4)

#### B1. The frame

Most debugging is unrecorded HARKing: theorize → patch → green → declare
the theory confirmed. The registry makes each step explicit and scores
the debugger's instincts over time.

#### B2. Entry template (extends the standard registry entry)

```markdown
### BUG-HX — <symptom, one line> `[H]` `[önkayıt YYYY-MM-DD]`
- **Semptom / Symptom:** observable behavior, verbatim (log, trace, repro
  steps). No interpretation in this field.
- **Mekanizma hipotezi / Mechanism hypothesis:** WHY it happens —
  specific enough to be wrong (file:line, state, ordering).
- **Çürütme testi / Refutation test:** the experiment that distinguishes
  this mechanism from rivals (a breakpoint, a log line, a minimal repro,
  a property test). What result kills THIS hypothesis?
- **Rakip hipotezler / Rival hypotheses:** at least one alternative
  mechanism that produces the same symptom.
- **DURUM:** ⏳
```

#### B3. "The fix worked" is a surprising positive

Before closing a bug as `[K]` (mechanism confirmed):

- **Symmetric control:** would a neutral perturbation also have "fixed"
  it? (Timing changes, cache invalidation, restart effects, heisenbugs.)
  Cheap version: revert the fix — does the bug reproduce? Then re-apply.
  No repro on revert → the fix is `[KKE]`, not `[K]`.
- **Mechanism check:** does the fix's location match the hypothesized
  mechanism? A fix that works from an unrelated location refutes the
  mechanism even while curing the symptom — record both facts.

#### B4. Suspicion inventory → instinct hit rate

Static signals (unchecked return values, boundary arithmetic, shared
mutable state, TOCTOU patterns, swallowed exceptions) each become an
`[H]` entry with a clearing test. Over 10–15 entries this produces the
auditor's/developer's real bug-instinct hit rate — the code version of
scoring "you catch the number that doesn't fit." A ~50% rate honestly
recorded beats a curated 100%.

#### B5. Rules inherited unchanged

Refuted hypotheses stay in the registry `[R]`. Near-misses are
near-misses. Post-hoc mechanism stories are labeled post-hoc. Precondition
failures ("couldn't reproduce at all") close the cell without counting
for or against.

## Mizan Feature / PRD Gate (Mode 5)

### The frame

A PRD is a claim set about the future, usually presented one tier above
its evidence: user-problem claims ("users struggle with X" — often `[H]`
dressed as `[K]`), value claims ("this will increase Y"), cost claims,
and dependency claims ("the API supports this"). The gate does two
things: it tiers the PRD's claims BEFORE code is written, and it
preregisters how the feature will be judged AFTER it ships — including
the condition under which it gets removed.

### Gate procedure

#### Step 1 — Atomize the PRD

Decompose into claim types and tier each with sources:

- **Problem claims:** who has this problem, how do we know? Support
  tickets, telemetry, user quotes = `[K]`; founder intuition = `[H]`
  (legitimate! but labeled); "obviously users want" = `[S]`.
- **Value claims:** the predicted effect, as a number.
- **Cost claims:** effort, maintenance burden, complexity added.
- **Dependency claims:** "library/API/platform supports X" — verify NOW,
  not mid-sprint. A wrong dependency claim is the cheapest `[R]` to catch
  early and the most expensive to catch late.
- **Scope claims:** what the PRD says is OUT. Missing out-of-scope
  section = scope drift preregistered to happen.

#### Step 2 — Preregister the feature entry

```markdown
### FEAT-X — <name> `[H]` `[önkayıt YYYY-MM-DD]`
- **Problem iddiası / Problem claim:** with its tier and source.
- **Değer metriği / Value metric:** what improves, measured how
  (instrument named: telemetry event, query, support-ticket count).
- **Başarı eşiği / Success threshold:** locked now. "Adoption ≥ N% of
  target users in T weeks" — not "users like it".
- **Kill condition / Kaldırma koşulu:** the post-ship measurement that
  justifies REMOVING the feature. Features without kill conditions
  accumulate as permanent maintenance debt.
- **Bilgilendiricilik önkoşulu:** can success even be measured? If no
  telemetry/user signal exists, either build the measurement first or
  accept the feature ships as `[S]` and say so.
- **Alternatifler / Alternatives:** MANDATORY, see Step 3.
- **Kabul kriterleri / Acceptance criteria:** phrased as refutation
  conditions ("the feature FAILS acceptance if...") — this is the direct
  antidote to demo-driven "mış gibi" features that present well and
  don't function.
- **Maliyet / Cost:** build + maintenance estimate.
- **DURUM:** ⏳ gated, not started / 🔨 building / 🚢 shipped, measuring.
```

#### Step 3 — Alternative-forcing (the suggestion mechanism)

Every feature entry MUST list, tiered on the SAME value metric:

1. **The proposed feature** as specified.
2. **At least one cheaper alternative** that attacks the same problem
   claim (a config flag instead of a UI, a doc page instead of a wizard,
   a batch job instead of realtime).
3. **The null alternative** — do nothing, or the 10% version. What does
   the problem cost if unsolved? Sometimes the honest answer is "less
   than the maintenance burden."

This is where "features the user didn't think of" legitimately come
from. Two structured sources:

- **The Gap Map** (from Mode 3): `[R]` findings propose fix-or-rename
  features; `[KKE]` findings propose hardening work; `[Y]` findings
  propose promise-fulfillment features; the TODO inventory is a
  ready-made backlog the user already wrote and forgot. These candidates
  carry evidence by construction — they were derived from verified gaps,
  not brainstorming.
- **Registry mining:** recurring `[R]` patterns across bug entries
  reveal systematic weaknesses (e.g., three refuted "the cache is
  consistent" hypotheses → an invalidation-redesign feature candidate).

**Honesty clause — what this cannot promise:** Mizan is an auditing
discipline, not a creativity engine. It generates candidates only from
recorded evidence (gaps, refutations, deferrals) and it RANKS and
CONSTRAINS ideas from any source; the novelty ceiling of pure invention
still belongs to the humans and models doing the inventing. Its real
contribution to ideation is negative space: killing pet features early
(null alternative), surfacing the forgotten backlog (TODO/Gap Map), and
forcing every idea to compete on the same metric. Do not oversell this.

#### Step 4 — Post-ship verification (the confound control)

- Measure against the preregistered threshold at the preregistered time.
  Early celebration on partial data = threshold shopping.
- **Adoption spikes are surprising positives:** control for novelty
  effect (re-measure after the novelty window), seasonality, and
  cannibalization (did the metric improve by stealing from a sibling
  feature?).
- Retrospectives that declare success with metrics chosen AFTER launch
  are HARKing; label them post-hoc, and record what the preregistered
  metric said even when the post-hoc story is nicer.
- Kill condition met → the feature goes to `[R]` and gets scheduled for
  removal or explicit renewal with a new entry. `[R]` features stay in
  the registry: "we tried surfacing X in the sidebar; it died" is
  institutional memory that prevents the same pitch next year.

#### Step 5 — Implementation-phase claims

While building, PRD claims meet reality. Rules:

- A dependency claim that fails mid-build flips to `[R]` in the entry —
  visibly, with the workaround's added cost recorded against the
  feature's cost claim.
- Scope drift is tier drift: each addition beyond the PRD gets its own
  micro-entry or an explicit "post-hoc scope, not preregistered" label.
- Acceptance tests are written from the refutation-phrased criteria
  BEFORE the demo, and they are subject to Mode 3's test-quality rule
  (a test that cannot fail is decoration).

### Step 6 — what it cost, and against what (R22)

`cost` is an estimate written before the work. `cost_actual` is the
measurement taken after it, and the gate asks for it because "we cannot
measure the return on our tooling" is two problems wearing one sentence, only
one of which is hard.

**The cost side is measurable and usually already on disk.** Token usage per
session is written by the tool that spent it; invoices exist; hours are
tracked. Nobody totals them, which is not the same as nobody being able to.
Name the **instrument** that produced the number — a script, an invoice, a
dashboard. "The model estimated it" is not an instrument.

**The attribution is a judgement, and saying so is the point.** Which sessions
advanced which feature is decided by a person, not counted by a system. The
`attribution` field exists so a number cannot read as though it had been
counted when it was assigned.

**The return side needs the value metric you already named** in `metric`, and
one more thing the schema cannot supply for you:

#### The arm, or the cap

`baseline.kind` is mandatory and blunt:

| kind | what it is | what it costs you |
|---|---|---|
| `none` | no comparison exists | legal, honest, and it **caps the entry below `[K]`** |
| `internal-phase` | an earlier phase of the same project | cheap; confounded by everything else that changed |
| `parallel-arm` | the same work done both ways at once | expensive; the only one that isolates the tool |
| `historical` | a comparable past project | confounded by the years in between |

What the work cost is a measurement. That **the tool caused the difference**
is a claim, and with no arm nothing separates it from the boring explanations
that produce the same number: a codebase the team now knows, a backlog that
shrank, a second attempt at a problem already solved once. This is R2 —
a baseline-less experiment never promotes to `[K]` — pointed at the claim
teams most often make without a control.

The honest majority case is `internal-phase` with a `note` that lists what it
does not control for. That is worth more than a `parallel-arm` nobody ran and
far more than a `none` presented as a result.

---

### Large PRDs and feature portfolios — phase the gate

A single epic PRD or a whole roadmap of features is too large to atomize
and preregister in one pass. Reuse the phased protocol from
`code-audit.md` §A5.1: Phase 0 partitions the PRD into bounded feature
groups (or the roadmap into individual FEAT-X entries) and records them in
a Coverage Ledger (`templates.md` §5); each phase gates one group fully
and APPENDS its FEAT-X entries to the one registry; a final reconciliation
pass catches cross-feature dependency claims and shared kill conditions
(feature A's success metric that silently depends on feature B). Until
that pass runs, "the whole PRD is gated" is `[H]`, not `[K]`.
