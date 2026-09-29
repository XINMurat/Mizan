#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mizan_calibration.py — what do our experiments actually return?

A registry records each result; nothing summed them. This reads any number of
registries and reports two things, in this order, because the second is
meaningless without the first:

1. DECISIVENESS — the share of results that returned a verdict at all
   (threshold_met yes/no) rather than precondition_failed / underpowered.
   An experiment programme that never decides is not testing anything, and
   that is visible here before any hit rate is.
2. HIT RATE — among decisive results, the share that met their support
   threshold. Printed only when n >= MIN_N; below it the tool says so
   instead of printing a percentage (the curated-anecdote failure).

Tier mix per registry is printed beside, since a registry full of H with no
results is the other way a programme can stall.

Usage:
    python tools/mizan_calibration.py evals/*/*.mizan-registry.yaml
    python tools/mizan_calibration.py --json a.yaml b.yaml

Exit 0 always for a report; 2 if a file is not a registry.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write("ERROR: PyYAML is required. pip install pyyaml\n")
    sys.exit(2)

MIN_N = 5
DECISIVE = {"yes": "supported", "no": "refuted"}


def outcome(r: dict) -> str:
    v = str(r.get("threshold_met", "")).strip().lower()
    return {"true": "yes", "y": "yes", "false": "no", "n": "no"}.get(v, v) or "unrecorded"


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="decisiveness and hit rate across registries")
    ap.add_argument("registries", nargs="+")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)

    rows, total = [], Counter()
    for path in a.registries:
        try:
            d = yaml.safe_load(open(path, encoding="utf-8"))
        except (OSError, yaml.YAMLError) as exc:
            sys.stderr.write(f"ERROR: {path}: {exc}\n")
            return 2
        if not isinstance(d, dict) or not isinstance(d.get("hypotheses"), list):
            sys.stderr.write(f"ERROR: {path} is not a Mizan registry (no hypotheses)\n")
            return 2
        res = Counter(outcome(r) for r in d.get("results") or [] if isinstance(r, dict))
        tiers = Counter(str(h.get("tier", "")) for h in d["hypotheses"] if isinstance(h, dict))
        total.update(res)
        rows.append({"registry": path, "results": dict(res), "tiers": dict(tiers)})

    n_all = sum(total.values())
    n_dec = total["yes"] + total["no"]
    summary = {
        "results": n_all,
        "decisive": n_dec,
        "decisiveness": (n_dec / n_all) if n_all else None,
        "hit_rate": (total["yes"] / n_dec) if n_dec >= MIN_N else None,
        "outcomes": dict(total),
    }
    if a.json:
        print(json.dumps({"registries": rows, "summary": summary}, indent=2))
        return 0

    for r in rows:
        print(f"{r['registry']}\n  results {r['results'] or '{}'}  tiers {r['tiers']}")
    print(f"\n{n_all} result(s) across {len(rows)} registr{'y' if len(rows) == 1 else 'ies'}")
    if not n_all:
        print("  no results recorded — nothing has been tested yet; that is the finding.")
        return 0
    print(f"  decisive (a verdict returned): {n_dec}/{n_all} = {n_dec / n_all:.0%}")
    other = {k: v for k, v in total.items() if k not in DECISIVE}
    if other:
        print(f"  no verdict: {other}")
    if n_dec >= MIN_N:
        print(f"  hit rate among decisive: {total['yes']}/{n_dec} = {total['yes'] / n_dec:.0%}")
    else:
        print(f"  hit rate: not reported (decisive n={n_dec} < {MIN_N})")
    if n_dec == 0:
        print("  [KKE] no experiment here has returned a verdict. Fix the design "
              "(power, preconditions) before adding more hypotheses.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
