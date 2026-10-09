# Context economy

Moved verbatim from SKILL.md (v2.9, lines 344-373) when the body was pruned (EVAL-008/009). Nothing here was rewritten.

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

