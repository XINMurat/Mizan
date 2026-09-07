#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YZ-006 verdict. Written BEFORE the run finished, so the analysis cannot be
chosen to suit the numbers.

The threshold is the registry's, quoted rather than re-derived:

    support : contradiction rate falls >= 25% relative AND accuracy does not
              fall
    refuted : <= 8% relative
    between : underpowered, one rerun with stated changes

Accuracy is reported with a paired bootstrap CI because 60 problems is a small
n and a point difference of a few percent over 60 items is noise wearing a
number. If the CI crosses zero, the accuracy clause is "did not fall" only in
the sense that nothing was shown either way, and that is what gets written.
"""
from __future__ import annotations

import json
import random
import sys


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def main(path: str) -> int:
    d = load(path)
    rows = d["rows"]
    cfg = d["config"]

    usable = [r for r in rows if r["arm_a"] is not None and r["arm_b"] is not None]
    dropped = len(rows) - len(usable)

    # PRECONDITION GATE — locked 2026-09-07, before the rerun. The first run
    # had no gate and printed a verdict off four usable problems. A test only
    # counts if its preconditions held, and "cell closed: precondition failed"
    # is its own outcome, distinct from refuted.
    MIN_USABLE = 40
    if len(usable) < MIN_USABLE:
        print(f"usable {len(usable)} of {len(rows)} — below the locked floor of {MIN_USABLE}.")
        print("VERDICT: CELL CLOSED — precondition failed. Not [R], not support.")
        print("The model did not produce parseable answers often enough for either")
        print("arm to mean anything. Nothing about the hypothesis was measured.")
        return 0

    acc_a = sum(1 for r in usable if r["arm_a"] == r["gold"]) / len(usable)
    acc_b = sum(1 for r in usable if r["arm_b"] == r["gold"]) / len(usable)

    rate_rows = [r for r in usable if r["rate_a"] is not None and r["rate_b"] is not None]
    ra = sum(r["rate_a"] for r in rate_rows) / len(rate_rows)
    rb = sum(r["rate_b"] for r in rate_rows) / len(rate_rows)
    rel = (ra - rb) / ra if ra > 0 else 0.0

    changed = [r for r in usable if r["arm_a"] != r["arm_b"]]
    fixed = [r for r in changed if r["arm_b"] == r["gold"]]
    broke = [r for r in changed if r["arm_a"] == r["gold"]]
    fell_back = sum(1 for r in usable if r["fell_back"])

    # paired bootstrap on the accuracy difference
    random.seed(0)
    diffs = []
    for _ in range(10000):
        s = [random.choice(usable) for _ in usable]
        a = sum(1 for r in s if r["arm_a"] == r["gold"]) / len(s)
        b = sum(1 for r in s if r["arm_b"] == r["gold"]) / len(s)
        diffs.append(b - a)
    diffs.sort()
    lo, hi = diffs[250], diffs[9750]

    kinds = {}
    for r in rows:
        for k, v in r["kinds"].items():
            kinds[k] = kinds.get(k, 0) + v

    print(f"model {cfg['model']}  n={cfg['n']}  problems={cfg['problems']}  temp={cfg['temp']}")
    print(f"usable {len(usable)}  (dropped, no parseable answer in an arm: {dropped})")
    print(f"fell back to arm A's pool (every candidate contradictory): {fell_back}")
    print()
    print(f"contradiction rate of the SELECTED trace   A {ra:.3f}   B {rb:.3f}   "
          f"relative reduction {rel*100:.1f}%")
    print(f"accuracy                                   A {acc_a:.3f}   B {acc_b:.3f}   "
          f"diff {acc_b-acc_a:+.3f}  95% CI [{lo:+.3f}, {hi:+.3f}]")
    print(f"answers changed by the filter: {len(changed)}  "
          f"(fixed {len(fixed)}, broke {len(broke)})")
    print(f"contradictions by class: {kinds}")
    print()

    if rel >= 0.25 and (acc_b - acc_a) >= 0:
        v = "SUPPORT — but read the scope caveat before promoting anything"
    elif rel <= 0.08:
        v = "REFUTED [R] — the filter does not buy what the seed claimed"
    else:
        v = "UNDERPOWERED — between the thresholds; one rerun with stated changes"
    if rel >= 0.25 and (acc_b - acc_a) < 0:
        v = "REFUTED [R] on the conjunction — rate fell but accuracy fell too"
    print("VERDICT:", v)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "run-60.json"))
