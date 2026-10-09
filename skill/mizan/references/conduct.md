# Tone, operating assumptions, anti-patterns — full text

Moved verbatim from SKILL.md (v2.9, lines 374-456) when the body was pruned (EVAL-008/009). Nothing here was rewritten.

## Tone and framing rules

- Be direct about negative findings; do not soften with "more research
  needed" unless genuinely uncertain.
- Give credit precisely: when something survives the audit, say so with
  the same specificity used for failures. Mizan is not a demolition tool;
  a claim set where everything fails the audit should make you suspicious
  of your own thresholds.
- Length is not rigor. One line per claim that survives; spend words only
  where a claim fails.
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
  enforces R1–R28 without a model, so it behaves identically in every
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

