# Mizan Code Audit & Bug-Hypothesis Registry (Modes 3–4)

## Part A — Code audit (Mode 3)

### A1. Claim inventory — where claims live in code

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

### A2. Tier mapping for code claims

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

### A3. Drift catalog (code versions of checklist items)

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

### A4. Test-quality audit — the confound control for `[K]`

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

### A5. Scale, sampling, and the coverage statement

Full atomization is impossible beyond small codebases. Mandatory
practice:

- Declare scope up front: which modules/paths audited, by what selection
  rule (risk-weighted: entry points, security surfaces, money paths,
  recently-churned files via `git log --stat`).
- Report coverage: "N of M modules, K of L public functions."
- Never present a sampled audit as a full one.

### A6. Deliverables

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

## Part B — Bug-hypothesis registry (Mode 4)

### B1. The frame

Most debugging is unrecorded HARKing: theorize → patch → green → declare
the theory confirmed. The registry makes each step explicit and scores
the debugger's instincts over time.

### B2. Entry template (extends the standard registry entry)

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

### B3. "The fix worked" is a surprising positive

Before closing a bug as `[K]` (mechanism confirmed):

- **Symmetric control:** would a neutral perturbation also have "fixed"
  it? (Timing changes, cache invalidation, restart effects, heisenbugs.)
  Cheap version: revert the fix — does the bug reproduce? Then re-apply.
  No repro on revert → the fix is `[KKE]`, not `[K]`.
- **Mechanism check:** does the fix's location match the hypothesized
  mechanism? A fix that works from an unrelated location refutes the
  mechanism even while curing the symptom — record both facts.

### B4. Suspicion inventory → instinct hit rate

Static signals (unchecked return values, boundary arithmetic, shared
mutable state, TOCTOU patterns, swallowed exceptions) each become an
`[H]` entry with a clearing test. Over 10–15 entries this produces the
auditor's/developer's real bug-instinct hit rate — the code version of
scoring "you catch the number that doesn't fit." A ~50% rate honestly
recorded beats a curated 100%.

### B5. Rules inherited unchanged

Refuted hypotheses stay in the registry `[R]`. Near-misses are
near-misses. Post-hoc mechanism stories are labeled post-hoc. Precondition
failures ("couldn't reproduce at all") close the cell without counting
for or against.
