# Audit mode — full procedure

Moved verbatim from SKILL.md (v2.9, lines 124-214) when the body was pruned (EVAL-008/009). Nothing here was rewritten.

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
   **Record it:** `probes.domain` in the registry schema — the scenarios,
   `supplied_by` (auditor or none = self-report, and R19 refuses a tier-K
   coverage claim over it), and `written_before_work`. `checklist.md` item 12
   carries an eight-class seed list for the *asking* — two at once, end of
   life, crossing a boundary, the person leaves, zero/one/many, undo and
   exit, out of order, who may see it. It is a prompt for the interview, not
   a list you may fill in alone.
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
   **Record it:** `probes.conjunction.pairs` — feature, the guarantee it can
   reach, the order if the pair is asymmetric, and the outcome. A pair left
   `unchecked` blocks a tier-K coverage claim (R20); a pass that leaves no
   row cannot be told apart from one that never ran.
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
   The registry is also where escapes land: when a defect surfaces later on
   ground this audit covered, RR-13 turns it into a class — `probes.escaped`
   with `class_ref` (the check that should have fired) or `class_new` (the
   probe that now exists because of it), which R21 requires. The scorecard
   already counted escapes; counting is not learning, and items 12 and 13
   above were each born from an escape nobody recorded as one.
10. **Declare the HARKing status.** Retrospective analysis selected its
   examples after seeing outcomes. Say this plainly in the report header —
   including about your own audit, which is also retrospective.
11. **Separate mechanism from motive.** When explaining why a document is
   skewed, prefer structural explanations (selection pressure, format
   incentives) over intent attribution ("they designed it to flatter") —
   unless intent is itself evidenced.

