# Retired rules

A rule leaves SKILL.md only on a measured result, and the record of why stays
here. A refutation that is deleted gets rewritten: without this file, the
next person to meet the same over-refusal would add the same sentence back
and expect it to work.

Each entry gives the rule text as it shipped, why it was added, the evidence
that retired it, and what would justify bringing it back.

## "An earned claim is reported as earned" — retired 2026-09-29

**Text as shipped** (SKILL.md, *Tone and framing rules*):

> **An earned claim is reported as earned.** Before marking a claim `[KKE]`
> for a missing control, check the claim's own text: a comparison group, an
> independent measurement or a primary record stated there IS the control.
> Refusing an earned claim is an audit error of the same weight as passing an
> unearned one (EVAL-004: this skill made a small model refuse 5 of 24 earned
> claims; the bare model refused none).

**Why it was added.** EVAL-004 measured a real cost of the skill: under
sign-off pressure, haiku with SKILL.md refused 5 of 24 earned claims, the bare
model none.

**Evidence that retired it.**

| Eval | Tasks | Wording | Earned-PROVEN, rule − no rule | Verdict |
|---|---|---|---|---|
| EVAL-005 | the EVAL-004 tasks the rule was written after | cited | 5/24 → 1/24 refused | support, not promoted (seen tasks) |
| EVAL-006 | six fresh tasks | neutral (citation removed) | −0.083, CI [−0.167, 0.000] | refuted |
| EVAL-007 | the same six fresh tasks | cited, as shipped | −0.083, CI [−0.292, +0.083] | refuted |

The decision was preregistered in `evals/EVAL-007/eval-007.mizan-registry.yaml`
before any run: refute removes the rule. On unseen tasks neither wording
helped and both point estimates went the wrong way; EVAL-005's effect was fit
to the tasks the rule was written after.

**What is still true.** The over-refusal is real and reproduces (16.7% and
20.8% of earned claims refused without the rule). Retiring the rule removes a
remedy that did not work, not the problem. The principle survives in the rule
above it ("Give credit precisely"), which was there before and was not
measured on its own.

**What would bring it back.** A different remedy, not this sentence reworded:
preregistered on tasks written after the remedy, with the decision rule fixed
before the runs, as EVAL-007 did.
