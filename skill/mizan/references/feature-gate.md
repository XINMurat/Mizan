# Mizan Feature / PRD Gate (Mode 5)

## The frame

A PRD is a claim set about the future, usually presented one tier above
its evidence: user-problem claims ("users struggle with X" — often `[H]`
dressed as `[K]`), value claims ("this will increase Y"), cost claims,
and dependency claims ("the API supports this"). The gate does two
things: it tiers the PRD's claims BEFORE code is written, and it
preregisters how the feature will be judged AFTER it ships — including
the condition under which it gets removed.

## Gate procedure

### Step 1 — Atomize the PRD

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

### Step 2 — Preregister the feature entry

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

### Step 3 — Alternative-forcing (the suggestion mechanism)

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

### Step 4 — Post-ship verification (the confound control)

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

### Step 5 — Implementation-phase claims

While building, PRD claims meet reality. Rules:

- A dependency claim that fails mid-build flips to `[R]` in the entry —
  visibly, with the workaround's added cost recorded against the
  feature's cost claim.
- Scope drift is tier drift: each addition beyond the PRD gets its own
  micro-entry or an explicit "post-hoc scope, not preregistered" label.
- Acceptance tests are written from the refutation-phrased criteria
  BEFORE the demo, and they are subject to Mode 3's test-quality rule
  (a test that cannot fail is decoration).

## Step 6 — what it cost, and against what (R22)

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

### The arm, or the cap

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

## Large PRDs and feature portfolios — phase the gate

A single epic PRD or a whole roadmap of features is too large to atomize
and preregister in one pass. Reuse the phased protocol from
`code-audit.md` §A5.1: Phase 0 partitions the PRD into bounded feature
groups (or the roadmap into individual FEAT-X entries) and records them in
a Coverage Ledger (`templates.md` §5); each phase gates one group fully
and APPENDS its FEAT-X entries to the one registry; a final reconciliation
pass catches cross-feature dependency claims and shared kill conditions
(feature A's success metric that silently depends on feature B). Until
that pass runs, "the whole PRD is gated" is `[H]`, not `[K]`.
