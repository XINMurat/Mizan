#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mizan_export_results.py — decided tiers, for Kıyas' survival ledger.

The Kıyas ledger asks one question of a Mizan registry: what did each
registered seed end up as? Until now someone copied that by hand, which is
how a ledger drifts from its registry. This tool emits the answer:

    python tools/mizan_export_results.py registry.yaml -o mizan-results.yaml
    # in the Kıyas repo:
    python tools/kiyas_ledger.py --sync mizan-results.yaml ledger/kiyas-ledger.yaml

WHAT COUNTS AS DECIDED — the trap this avoids
---------------------------------------------
The ledger counts K and H as "survived". A hypothesis sits at H from the
moment it is written, so exporting every entry's current tier would count
every untested seed as a survivor. An entry is exported as decided only
when a result names it AND that result's `decision_confirmed_by` is filled
(R7: someone other than the producer). Everything else is listed under
`pending` with the reason, and carries no tier.

Exit code 0 on success, 2 when the file is not a registry.
"""
from __future__ import annotations

import argparse
import sys
from datetime import date

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write("ERROR: PyYAML is required. pip install pyyaml\n")
    sys.exit(2)

BLOCKS = ("hypotheses", "features", "bugs")


def _s(v) -> str:
    return "" if v is None else str(v).strip()


def confirmed(r: dict) -> bool:
    who = _s(r.get("decision_confirmed_by")).lower()
    return bool(who) and not who.startswith("pending")


def build(data: dict) -> dict:
    results = [r for r in (data.get("results") or []) if isinstance(r, dict)]
    by_hyp: dict[str, list[dict]] = {}
    for r in results:
        by_hyp.setdefault(_s(r.get("hypothesis")), []).append(r)

    decided, pending = [], []
    for block in BLOCKS:
        for e in data.get(block) or []:
            if not isinstance(e, dict) or not _s(e.get("id")):
                continue
            eid = _s(e["id"])
            rs = by_hyp.get(eid, [])
            ok = [r for r in rs if confirmed(r)]
            if ok:
                last = ok[-1]
                decided.append({"id": eid, "tier": _s(e.get("tier")).upper(),
                                "result": _s(last.get("id")),
                                "confirmed_by": _s(last.get("decision_confirmed_by"))})
            else:
                pending.append({"id": eid, "reason": (
                    "result exists, decision not confirmed (R7)" if rs
                    else "no result yet")})
    return {
        "mizan_results": {
            "project": _s((data.get("registry") or {}).get("project")),
            "exported": date.today().isoformat(),
            "rule": "tier only for entries with a confirmed result; pending carries none",
        },
        "decided": decided,
        "pending": pending,
    }


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("registry", help="path to mizan-registry.yaml")
    ap.add_argument("-o", "--out", help="write here instead of stdout")
    a = ap.parse_args(argv)
    try:
        data = yaml.safe_load(open(a.registry, encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        sys.stderr.write(f"ERROR: cannot read {a.registry}: {exc}\n")
        return 2
    if not isinstance(data, dict) or not any(isinstance(data.get(b), list) for b in BLOCKS):
        sys.stderr.write(f"ERROR: {a.registry} is not a Mizan registry "
                         f"(none of {', '.join(BLOCKS)})\n")
        return 2
    out = build(data)
    text = yaml.safe_dump(out, allow_unicode=True, sort_keys=False, width=88)
    if a.out:
        open(a.out, "w", encoding="utf-8").write(text)
        sys.stderr.write(f"{len(out['decided'])} decided, {len(out['pending'])} pending -> {a.out}\n")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
