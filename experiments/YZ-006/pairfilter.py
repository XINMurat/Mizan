#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
YZ-006 / K-03 rig — does a pair-consistency filter at DECODING beat
equal-compute sampling?

WHAT IS BEING TESTED
--------------------
K-03's claim: the compositional-consistency check ("pair pass") does not need
to be a differentiable loss term. It needs a JUDGE, and a non-differentiable
symbolic judge is available at inference time. So run it as a candidate filter
and measure.

THE TWO ARMS — equal compute, and that is the whole point
--------------------------------------------------------
Both arms draw the SAME n candidates for a problem. Nothing is generated
twice; the arms differ only in how they choose among what was drawn.

  A (control): majority vote over all n candidate answers.
  B (filter):  drop every candidate whose trace contradicts itself, then
               majority vote over the survivors.

The control is NOT greedy decoding. A pair filter compared against greedy
would be measuring the value of sampling n times, which is a known result and
not this hypothesis. K-03 says so explicitly, and this is the line where it
would have been easiest to cheat.

Where no external verifier exists at selection time, majority vote IS the
equal-compute best-of-n. That substitution is recorded in the registry as a
dated clarification rather than made silently here.

THE JUDGE — deterministic, no model, and it never sees the gold answer
---------------------------------------------------------------------
Three contradiction classes, all mechanical:

  ARITH  a stated equality whose arithmetic is false: "12 * 3 = 34".
  PAIR   the same expression stated twice with different values. Each line is
         locally fine and the two cannot both hold. This is the pair check.
  FINAL  the declared final answer differs from the last value derived.

A candidate is contradictory if it trips any of the three. The checker is
deliberately narrow: it may MISS a contradiction, and it must never INVENT
one. A false positive discards a good candidate and flatters arm B, so the
asymmetry is built in on purpose.

USAGE
    python pairfilter.py --n 8 --problems 60 --out run.json
"""
from __future__ import annotations

import argparse
import ast
import json
import operator
import re
import sys
import time
import urllib.request
from collections import Counter

OLLAMA = "http://localhost:11434/api/generate"

# NOTE — the format is shown with PLACEHOLDERS, and the prompt contains no
# digit anywhere. Two failures produced that constraint, in order:
#   1. The first draft showed a worked example ("16 - 3 = 13"). The model
#      echoed it verbatim as its own first step on unrelated problems, and
#      the judge read it as a real claim: an instruction that plants a claim
#      inside the trace contaminates the thing being measured.
#   2. Removing the example and describing the format in words ("four hash
#      marks") made the model stop emitting the final line at all -- 56 of 60
#      problems produced no parseable answer and the run closed on a failed
#      precondition.
# Placeholders show the shape without supplying a number to copy. Six-sample
# pre-test: 4/6 parseable.
PROMPT = (
    "Solve the problem step by step.\n"
    "Write each arithmetic step on its own line in this form:\n"
    "  <expression> = <number>\n"
    "Use only digits and + - * / inside <expression>: no words, no units, "
    "no currency symbols, no LaTeX.\n"
    "Write the very last line in exactly this form:\n"
    "  #### <number>\n\n"
    "Problem: {q}\n"
)

# --------------------------------------------------------------------------
# the judge
# --------------------------------------------------------------------------

_OPS = {
    ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
    ast.Div: operator.truediv, ast.Pow: operator.pow, ast.USub: operator.neg,
    ast.UAdd: operator.pos, ast.Mod: operator.mod,
}

# "80,000 + 50,000 = 130,000". Commas are IN the expression class: leaving
# them out was the first draft's bug, and it silently truncated expressions
# into false arithmetic errors -- the judge inventing claims, exactly what it
# must not do.
STEP = re.compile(r"([0-9][0-9\s.,+\-*/()x×÷]*?)\s*=\s*\$?(-?[0-9,]+(?:\.[0-9]+)?)")
FINAL = re.compile(r"####\s*\$?(-?[0-9,]+(?:\.[0-9]+)?)")
BOXED = re.compile(r"boxed\s*\{?\s*\$?(-?[0-9,]+(?:\.[0-9]+)?)")

# LaTeX wrappers carry the same arithmetic in a form the parser cannot read.
# Strip the commands, never the numbers.
_TEX = re.compile(r"\\[A-Za-z]+|[{}$]|\\\[|\\\]|\\\(|\\\)")


def _clean(text: str) -> str:
    return _TEX.sub(" ", text)


def _num(s: str) -> float | None:
    try:
        return float(s.replace(",", "").replace("$", ""))
    except ValueError:
        return None


def _eval(expr: str) -> float | None:
    """Evaluate a pure-arithmetic expression, or return None. No names, no calls."""
    e = expr.replace("x", "*").replace("×", "*").replace("÷", "/").replace(",", "").strip()
    if not e or not re.fullmatch(r"[0-9\s.+\-*/()%]+", e):
        return None
    try:
        tree = ast.parse(e, mode="eval")
    except SyntaxError:
        return None

    def walk(node):
        if isinstance(node, ast.Expression):
            return walk(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
            a, b = walk(node.left), walk(node.right)
            if a is None or b is None:
                return None
            try:
                return _OPS[type(node.op)](a, b)
            except ZeroDivisionError:
                return None
        if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
            v = walk(node.operand)
            return None if v is None else _OPS[type(node.op)](v)
        return None

    try:
        return walk(tree)
    except Exception:
        return None


def answer_of(text: str) -> float | None:
    r"""The declared final answer, or None.

    Two accepted forms: the requested '#### n', and LaTeX \boxed{n}, which
    this model reaches for on its own often enough that refusing it would
    exclude traces for a formatting habit rather than for anything about the
    hypothesis. Nothing else counts -- in particular "the last number in the
    text" does NOT, because that is a guess dressed as a reading.
    """
    m = FINAL.search(text)
    if m:
        return _num(m.group(1))
    b = BOXED.findall(text)
    return _num(b[-1]) if b else None


def contradictions(text: str) -> list[dict]:
    """Every contradiction found. Never uses the gold answer."""
    fin = answer_of(text)
    text = _clean(text)
    found: list[dict] = []
    steps: list[tuple[str, float]] = []
    seen: dict[str, float] = {}

    for m in STEP.finditer(text):
        expr, rhs = m.group(1).strip(" ,"), _num(m.group(2))
        if rhs is None:
            continue
        val = _eval(expr)
        if val is None:
            continue
        steps.append((expr, rhs))

        if abs(val - rhs) > 1e-6 * max(1.0, abs(val)):
            found.append({"kind": "ARITH", "expr": expr, "stated": rhs, "actual": val})

        key = re.sub(r"\s+", "", expr)
        if key in seen and abs(seen[key] - rhs) > 1e-6 * max(1.0, abs(rhs)):
            found.append({"kind": "PAIR", "expr": expr, "first": seen[key], "second": rhs})
        seen.setdefault(key, rhs)

    if fin is not None and steps:
        last = steps[-1][1]
        if abs(fin - last) > 1e-6 * max(1.0, abs(last)):
            found.append({"kind": "FINAL", "final": fin, "last_step": last})
    return found


# --------------------------------------------------------------------------
# sampling
# --------------------------------------------------------------------------

def generate(model: str, prompt: str, temp: float, seed: int, timeout: int = 300) -> str:
    body = json.dumps({
        "model": model, "prompt": prompt, "stream": False,
        "options": {"temperature": temp, "seed": seed, "num_predict": 500},
    }).encode()
    req = urllib.request.Request(OLLAMA, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())["response"]


def vote(answers: list[float]) -> float | None:
    """Majority vote; ties broken by first appearance.

    Both arms see the candidates in the same order, so the tie-break cannot
    favour one of them.
    """
    if not answers:
        return None
    counts = Counter(answers)
    best = max(counts.values())
    for a in answers:
        if counts[a] == best:
            return a
    return None


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="qwen2.5:1.5b-instruct")
    ap.add_argument("--n", type=int, default=8)
    ap.add_argument("--problems", type=int, default=60)
    ap.add_argument("--temp", type=float, default=0.8)
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)

    from datasets import load_dataset
    ds = load_dataset("openai/gsm8k", "main", split="test")

    rows = []
    t0 = time.time()
    for i in range(args.problems):
        q = ds[i]["question"]
        gold = _num(ds[i]["answer"].split("####")[-1].strip())
        cands = []
        for k in range(args.n):
            try:
                txt = generate(args.model, PROMPT.format(q=q), args.temp, seed=1000 * i + k)
            except Exception as exc:
                txt = ""
                print(f"  gen error p{i} k{k}: {type(exc).__name__}", file=sys.stderr, flush=True)
            cands.append({
                "answer": answer_of(txt),
                "contradictions": contradictions(txt),
                # The judge has to be auditable after the fact. The first run
                # kept no traces, so 542 arithmetic flags could not be checked
                # for a second parser bug -- a judge whose verdicts cannot be
                # re-read is closer to author-report than to instrument.
                "text": txt,
            })

        parseable = [c for c in cands if c["answer"] is not None]
        clean = [c for c in parseable if not c["contradictions"]]

        arm_a = vote([c["answer"] for c in parseable])
        fell_back = not clean
        pool_b = parseable if fell_back else clean
        arm_b = vote([c["answer"] for c in pool_b])

        def sel_rate(pool, picked):
            same = [c for c in pool if c["answer"] == picked]
            return None if not same else sum(1 for c in same if c["contradictions"]) / len(same)

        rows.append({
            "i": i, "gold": gold,
            "n_parseable": len(parseable), "n_clean": len(clean),
            "arm_a": arm_a, "arm_b": arm_b, "fell_back": fell_back,
            "rate_a": sel_rate(parseable, arm_a),
            "rate_b": sel_rate(pool_b, arm_b),
            "kinds": dict(Counter(x["kind"] for c in cands for x in c["contradictions"])),
        })
        if (i + 1) % 5 == 0:
            el = time.time() - t0
            print(f"  {i+1}/{args.problems}  {el:.0f}s  ({el/(i+1):.1f}s/problem)", flush=True)

    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump({"config": vars(args), "rows": rows}, fh, ensure_ascii=False, indent=1)
    print(f"wrote {args.out}  ({time.time()-t0:.0f}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
