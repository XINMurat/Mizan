# YZ-006 — the pair pass at decoding, not in the loss

The first hypothesis in this project to be preregistered, run, and scored.
It came back `[R]`, and this directory is here so that verdict can be
checked rather than believed.

## What was claimed

K-03, from the Kıyas batch of 2026-09-06: the compositional-consistency
check does not need to be a differentiable loss term. It needs a **judge**,
and a non-differentiable symbolic judge is available at inference time. So
run it as a candidate filter at decoding and measure.

## What was run

| | |
|---|---|
| Model | `qwen2.5:1.5b-instruct`, local (ollama, CPU-bound) |
| Data | GSM8K test, problems 0–59, in order, no selection |
| Candidates | 8 per problem, temperature 0.8 |
| Arm A (control) | majority vote over all parseable candidates |
| Arm B | drop self-contradictory candidates, then majority vote |
| Judge | deterministic; `ARITH`, `PAIR`, `FINAL`; never sees the gold answer |
| Wall clock | 297 minutes |

Both arms read the **same** 8 candidates. Nothing is generated twice; the
arms differ only in how they choose. The control is not greedy decoding — a
filter compared against greedy would measure the value of sampling eight
times, which is a known result and not this hypothesis.

## What happened

```
usable 60 of 60          (locked precondition floor: 40)
contradiction rate       A 0.485 → B 0.133      −72.5% relative
accuracy                 A 0.367 → B 0.333      −3.3 pts, 95% CI [−11.7, +5.0]
answers changed by the filter: 20   (fixed 2, broke 4)
contradiction classes:   ARITH 1664 · PAIR 554 · FINAL 77
```

The preregistered condition was a **conjunction**: the contradiction rate
falls at least 25% relative **and** accuracy does not fall. The first half
passed by a wide margin. The second did not — the point estimate moved the
wrong way, and because the interval crosses zero, "accuracy fell" is not
shown either. What is not shown is "it did not fall", and that is what the
rule asked for. Relaxing that afterwards would be moving the goalpost.

**Verdict: `[R]`, under this run's conditions.**

## The part worth more than the verdict

The filter fixed 2 answers and broke 4. Internal consistency is not
correctness. A trace that is wrong from beginning to end without ever
contradicting itself is exactly the trace a consistency filter *prefers* —
it optimises the thing it measures, which is contradiction, not error.

That is a small, measured instance of the mechanism K-05 predicts for the
reward scheme in YZ-002: a different seed, the same class of failure.

## What limits it

The judge was audited after the fact and its flags are technically correct:
`0 = 1` and `10 = 7` really are false equalities; it does not invent
contradictions. But most flags are **not reasoning errors — they are
degeneracy.** At 1.5B the model frequently collapses into loops that repeat
`1 = 7` for hundreds of lines, and a single trace can carry 100+ `ARITH`
flags. So at this scale the filter worked largely as a broken-output
detector, not on the "locally right, globally inconsistent" case K-03 is
actually about. The 72.5% reduction is therefore less informative than it
looks: throwing away garbage lowers a contradiction rate cheaply.

One model, one domain, n=60, one run. `[R]` here does not mean "the pair
pass is useless at inference". It means the preregistered threshold was not
met with this setup.

## Two rig failures, both on the record

**The first run closed on a failed precondition** — 56 of 60 problems
produced no parseable answer at all
(`run-60-precondition-failed.json`). Cause: the prompt originally taught
the step format with a worked example, the model copied that example into
unrelated traces, and the judge read it as a real claim. Removing the
example fixed the contamination and broke format compliance instead. The
fix was to show the shape with placeholders and no digit anywhere in the
prompt. The precondition gate in `analyze.py` was locked **after** that run
and **before** the second one, because the first analysis printed a verdict
off four usable problems.

**The traces were still not persisted.** The second run was supposed to
keep them so the judge could be audited; the field was added to the
candidate dict and never written into the per-problem summary, so it did
not survive. The audit was done by regenerating traces with the same seeds
instead. That is a recovery, not a substitute: seed determinism in ollama
was assumed and not verified, and the originals are gone.

## Files

| | |
|---|---|
| `pairfilter.py` | the rig: prompt, judge, both arms |
| `analyze.py` | the verdict, including the locked precondition gate |
| `run-60-v2.json` | the scored run |
| `run-60-precondition-failed.json` | the first run, kept because it is a result too |

Reproduce with `python pairfilter.py --n 8 --problems 60 --out run.json`
then `python analyze.py run.json`. Expect several hours without a GPU.

The registry entry, with the dated result blocks and the author's
prediction (which was wrong in both directions), is `YZ-006` in
`mizan-product-registry.yaml`; the published excerpt is
`docs/registry-excerpt.yaml`.
