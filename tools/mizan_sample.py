#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mizan_sample.py — a substance check the validator cannot make, made cheap.

The validator checks that `refutation` and `arbiter` are PRESENT; it cannot
tell whether they could actually refute anything. A registry whose fields are
all filled and all empty of content passes it most easily. This tool picks a
few entries for a person who is not the author to read, and records that the
reading happened.

WHY THE PICK CANNOT BE CHOSEN
-----------------------------
The seed is the sha256 of the registry's bytes. Nobody picks it; getting a
different sample means changing the registry, and that change is in git. The
sample file stores the digest, so `--check` can prove the entries reviewed are
the entries drawn, not a friendlier set.

Usage:
    python tools/mizan_sample.py draw registry.yaml -n 3 -o review-sample.yaml
    # a reviewer fills `reviewer`, and per entry `can_refute: yes|no` + `note`
    python tools/mizan_sample.py check registry.yaml review-sample.yaml

`check` exits 1 when the sample does not match the registry's draw, a verdict
is missing, or the reviewer is the registry's owner; 0 otherwise. Entries a
reviewer marked `can_refute: no` are printed: they are the finding.
"""
from __future__ import annotations

import argparse
import hashlib
import random
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write("ERROR: PyYAML is required. pip install pyyaml\n")
    sys.exit(2)

BLOCKS = ("hypotheses", "features", "bugs")


def load(path: str):
    raw = open(path, "rb").read()
    data = yaml.safe_load(raw.decode("utf-8"))
    if not isinstance(data, dict) or not any(isinstance(data.get(b), list) for b in BLOCKS):
        raise ValueError(f"{path} is not a Mizan registry")
    return data, hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def draw(data: dict, digest: str, n: int) -> list[dict]:
    pool = [e for b in BLOCKS for e in (data.get(b) or [])
            if isinstance(e, dict) and e.get("id")]
    pool.sort(key=lambda e: str(e["id"]))
    rng = random.Random(int(digest, 16))
    return rng.sample(pool, min(n, len(pool)))


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="seeded substance-review sample")
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("draw"); d.add_argument("registry"); d.add_argument("-n", type=int, default=3)
    d.add_argument("-o", "--out")
    c = sub.add_parser("check"); c.add_argument("registry"); c.add_argument("sample")
    a = ap.parse_args(argv)

    try:
        data, digest = load(a.registry)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        sys.stderr.write(f"ERROR: {exc}\n")
        return 2

    if a.cmd == "draw":
        picked = draw(data, digest, a.n)
        out = {"sample": {"registry_sha256": digest, "n": len(picked), "reviewer": ""},
               "entries": [{"id": e["id"],
                            "refutation": e.get("refutation") or e.get("kill_condition") or "",
                            "arbiter": e.get("arbiter") or {},
                            "question": "Could this refutation condition and arbiter "
                                        "actually return 'refuted'?",
                            "can_refute": "", "note": ""} for e in picked]}
        text = yaml.safe_dump(out, allow_unicode=True, sort_keys=False, width=88)
        if a.out:
            open(a.out, "w", encoding="utf-8").write(text)
            sys.stderr.write(f"{len(picked)} entr{'y' if len(picked) == 1 else 'ies'} drawn -> {a.out}\n")
        else:
            sys.stdout.write(text)
        return 0

    s = yaml.safe_load(open(a.sample, encoding="utf-8")) or {}
    meta, entries = s.get("sample") or {}, s.get("entries") or []
    problems = []
    if meta.get("registry_sha256") != digest:
        problems.append("the registry changed since the draw — draw again; a stale "
                        "sample reviews entries that may no longer exist")
    else:
        want = [e["id"] for e in draw(data, digest, int(meta.get("n") or 0))]
        got = [e.get("id") for e in entries]
        if want != got:
            problems.append(f"entries {got} are not the draw {want}")
    reviewer = str(meta.get("reviewer") or "").strip()
    owner = str((data.get("registry") or {}).get("owner") or "").strip()
    if not reviewer:
        problems.append("no reviewer named")
    elif owner and reviewer.lower() == owner.lower():
        problems.append(f"reviewer '{reviewer}' is the registry owner (R7: producer != auditor)")
    no = []
    for e in entries:
        v = str(e.get("can_refute") or "").strip().lower()
        if v not in ("yes", "no"):
            problems.append(f"{e.get('id')}: can_refute is '{v}', expected yes|no")
        elif v == "no":
            no.append(f"{e.get('id')}: {e.get('note') or '(no note)'}")
    for p in problems:
        print(f"  ✗ {p}")
    for x in no:
        print(f"  FINDING cannot refute — {x}")
    print(f"{'FAIL' if problems else 'ok'}  {len(entries)} sampled, {len(no)} cannot refute")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
