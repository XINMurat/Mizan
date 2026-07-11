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

## 10. The auditor's own blind spot
- **What:** the audit itself is a retrospective document with coverage
  limits and its own selection effects.
- **Rule:** every audit report opens with a coverage statement (N of M
  claims checkable, which sources were inaccessible) and treats the
  auditor's prior outputs as auditable claims. When later evidence
  contradicts an earlier tier you assigned, revise it visibly.
