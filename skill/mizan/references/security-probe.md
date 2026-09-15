# Mizan Security Probe (Mode 7)

Mode 6 is meta-review. This is Mode 7.

## 0. Why this is a mode and not a checklist

Modes 3–5 all run the same engine: someone made a claim, find the evidence,
tier the gap. That engine has a known blind spot, and SKILL.md audit step 7
states it outright — *an absence produces no claim to tier*. Security lives
almost entirely in that blind spot. Nobody writes "this endpoint trusts the
`role` field from the client"; the defect IS the sentence nobody wrote.

Step 7's answer was to stop inventing scenarios and go ask the domain owner.
Mode 7 keeps that shape and changes the supplier: the scenario list comes
from a **trust-boundary map plus an adversary model**, not from the people
who built the thing. They are the wrong witnesses here — not dishonest, but
structurally unable to name the assumption they never knew they made.

So the mode is not "Mode 3 with security words in the risk ranking"
(`code-audit.md` §A5 already does that, and that is all it does). It is a
different scenario source, an inverted tier rule, and one new probe block.

## 1. The inverted tier rule — read this before anything else

In Modes 3–5 a passing test is evidence toward `[K]`. Here it is not.

| Observation | Tier | Why |
|---|---|---|
| Exploit attempt run, failed | `[KKE]` | An attack you thought of and could execute is a sample of one adversary. Not finding it is not absence. |
| Scanner clean | `[KKE]` | The scanner's rule set is its scenario list, and you did not write it, cannot enumerate it, and it was not written for this system. |
| Control present AND reached on every path into the asset | `[K]` | The claim is now about code structure, which the runtime can arbitrate (R8). |
| Control present, path coverage unverified | `[H]` | The usual claim-vs-evidence hop; call-site enforcement is the fragile class (see §4). |
| "We follow OWASP / we are SOC2" | `[Y]` until mapped | A compliance answer is a claim about a process, framed to imply a claim about a system. |

**The one rule that separates this mode from every scanner:** *not exploited*
never promotes. Only a **named boundary with a control on every path to it**
promotes. Security tooling almost universally scores silence as a pass; the
entire value of running this inside Mizan is that the schema refuses to.

Corollary for the report: a Mode 7 pass that finds nothing produces a
`[KKE]` coverage statement, never a clean bill. Say what was probed and what
that leaves untouched, or you have written reassurance.

## 2. Procedure

### S1. Map the trust boundaries — before reading any code for bugs
A boundary is any point where data or control crosses from one authority to
another: network ingress, authn/authz check, deserialization, subprocess and
shell, file path construction, SQL/template/HTML interpolation, secret load,
inter-service call, CI/build input, dependency resolution, admin surface.

For each, record three things — and if you cannot fill all three, that gap is
itself the first finding:
- **who** is on the far side (anonymous / authenticated user / another
  tenant / an internal service / a package registry / a CI runner),
- **what** they control (which bytes, which fields, which ordering),
- **what the near side assumes** about it.

The third one is the money column. It is the sentence nobody wrote.

### S2. Derive the adversary scenarios from the map, not from a vibe
One scenario per boundary, phrased as an action, not a category:
"a logged-in tenant A user changes the id in the URL to a tenant B record" —
not "IDOR". The category names a bug class; the action names a test.

`supplied_by` here is `threat_model`, and it is honest only if the map in S1
came first. **A scenario you wrote after finding the bug is HARKing** and R19
already refuses it via `written_before_work` — the same rule, same reason.

### S3. Run each scenario to an outcome
`reachable` (the action works — a finding), `blocked_by` (a named control
stops it, and you cite it), `boundary_recorded` (it works and that is a
written, deliberate decision — an internal admin tool with a documented trust
assumption is not a vulnerability), `unchecked`.

`blocked_by` requires naming the control **and** showing it is on every path,
not the one path you tried. One reached call site is not a guarantee.

### S4. Conjunction pass — where the real ones are
SKILL.md audit step 8 transfers here with more force than anywhere else,
because atomizing is exactly how security reviews lose findings. Two features
each correct alone:
- a feature that **widens what an actor controls** (bulk import, a new filter
  parameter, file upload, a webhook), and
- a guarantee **enforced call site by call site** (every handler calls
  `check_access` — the new bulk path calls it once for the batch), or a
  **signal derived from an absence** (rate limiting keyed on a field the new
  surface lets the caller omit).

Every pair goes in `probes.conjunction` as usual. Order matters here too:
"revoke then read" and "read then revoke" are different systems.

### S5. Dependency and supply surface
Treat the lockfile as a claim set: pinned ≠ verified, and a transitive
dependency's maintainer is on the far side of a boundary nobody mapped.
Record it as a boundary in S1 with `who = the package registry` rather than
as a separate exercise.

### S6. Close the loop
Mode 7's output is a registry, not a PDF. The escape mechanism (`probes.escaped`,
R21) is the whole point and the thing a one-shot scan structurally cannot do:
when something surfaces later on ground this pass covered, it becomes a
**class** — `class_ref` if a probe should have caught it, `class_new` if the
probe now exists because of it. A CVE report is a count. A class is learning.

## 3. Relationship to `/security-review` and scanners

They are instruments, not rivals, and under R8 they are good ones — a scanner
is an `instrument` arbiter, which beats `author`. Use them, cite them by name
and version as the evidence for a scenario outcome, and then apply §1: their
silence is `[KKE]`, their hit is `[K]` on that one scenario and says nothing
about the boundary it did not model.

`/security-review` is diff-scoped and has no memory. Mode 7 is
boundary-scoped and append-only. Running it inside a diff review is fine and
cheap; treat the result as one phase in the coverage ledger (`code-audit.md`
§A5.1), never as the pass.

## 4. Rules inherited unchanged

R1 (threshold before result), R2 (baseline), R8 (arbiter — a self-run exploit
attempt is `author` unless a tool or a third party adjudicates), R19
(`written_before_work`, `supplied_by`), R20 (conjunction pairs), R21
(escapes become classes), append-only, and DC-001: a finding is a property of
the system, never of the person who wrote the line.

## 5. What this mode cannot do — state it in every report

- It is bounded by the boundary map. An unmapped boundary produces no
  scenario and therefore no finding, and nothing in this procedure detects
  its own omission. This is the same limit as step 7's and it does not go
  away by being named.
- It does not model a resourced adversary chaining three low findings. A
  pairwise conjunction pass finds pairs; it is silent about triples, and
  saying "we checked combinations" over a pairwise pass is `[Y]`.
- Cryptographic and protocol-level review is not in scope here and must be
  waived explicitly (`coverage.domain_probe_waived` is the existing
  mechanism) rather than left as an implied pass.
