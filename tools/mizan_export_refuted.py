#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Export refuted patterns from a Mizan registry as negative constraints.

This is the Mizan half of the Kıyas <-> Mizan loop. Kıyas generates,
Mizan audits and refutes, and refuted patterns are supposed to come BACK
to Kıyas as negative constraints ([GB] / AD4). That return path was prose
in both skills and a file (`refuted_and_open.md`) whose format was never
specified — which meant the AD4 sweep could not actually be performed.

This tool makes the handoff typed: it reads a mizan-registry.yaml and
emits refuted-patterns.yaml, which `kiyas_validate.py --refuted` consumes.

What it exports: every hypothesis at tier R (refuted) or Y (misleading),
plus — deliberately — every permanent KKE, because "we could never run
the control" is also a constraint a generator should know about.

Keyword extraction is crude on purpose: the consumer treats a match as a
prompt to look, not a verdict. A false positive costs one glance; a missed
refuted relative costs a repeated experiment.

Usage:
    python tools/mizan_export_refuted.py registry.yaml > refuted-patterns.yaml
    python tools/mizan_export_refuted.py -o refuted-patterns.yaml registry.yaml

Dependency: PyYAML  (pip install pyyaml)
"""
from __future__ import annotations

import argparse
import re
import sys
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write("ERROR: PyYAML is required. Install it with: pip install pyyaml\n")
    sys.exit(2)

EXPORT_TIERS = {"R", "Y", "KKE"}

# Words that carry no discriminating signal in a keyword match.
STOP = {
    "the", "and", "for", "with", "that", "this", "from", "into", "than",
    "has", "have", "was", "were", "will", "can", "not", "but", "its",
    "bir", "bu", "ile", "için", "olan", "daha", "gibi", "veya", "ama",
    "input", "model", "test", "result", "effect", "value", "using",
}


def keywords(text: str, limit: int = 8) -> list[str]:
    """Content words long enough to discriminate, in first-appearance order."""
    seen: list[str] = []
    for w in re.findall(r"[A-Za-zÇĞİÖŞÜçğıöşü_-]{4,}", text.lower()):
        if w in STOP or w in seen:
            continue
        seen.append(w)
        if len(seen) >= limit:
            break
    return seen


def _s(v: Any) -> str:
    return (v or "").strip() if isinstance(v, str) else ("" if v is None else str(v).strip())


# Refuted material does not live in one place. Real registries carry it as
# hypotheses, bug hypotheses, killed features, and a free-form discard list —
# and those blocks disagree about field names (formal/claim,
# refutation/reason). A generator that only reads `hypotheses` would consult
# an export that is silently empty, which is worse than no export at all.
SOURCE_KEYS = ("hypotheses", "bugs", "features", "refuted_and_discarded")
CLAIM_FIELDS = ("formal", "claim", "problem_claim", "symptom", "mechanism")
REASON_FIELDS = ("refutation", "reason", "why_closed", "kill_condition")


def _first(e: dict, fields: tuple[str, ...]) -> str:
    for f in fields:
        v = _s(e.get(f))
        if v:
            return v
    return ""


def build(data: dict) -> dict:
    reg = data.get("registry") or {}
    out: list[dict] = []
    for key in SOURCE_KEYS:
        for h in (data.get(key) or []):
            if not isinstance(h, dict):
                continue
            tier = _s(h.get("tier")).upper()
            # Entries in an explicit discard list are refuted by placement,
            # even when nobody bothered to tag them.
            if tier not in EXPORT_TIERS and key != "refuted_and_discarded":
                continue
            claim = _first(h, CLAIM_FIELDS)
            body = " ".join([_s(h.get("title")), claim, _first(h, REASON_FIELDS)])
            out.append({
                "id": h.get("id"),
                "title": _s(h.get("title")),
                "tier": tier or "R",
                "block": key,
                "claim": claim,
                "why_closed": _first(h, REASON_FIELDS) or "see registry history",
                # A refuted hypothesis constrains its relatives, not just
                # itself: the generator needs the mechanism, not the verdict.
                "keywords": keywords(body),
                "source_registry": reg.get("project") or "",
            })
    return {
        "refuted_patterns": out,
        "exported_from": reg.get("project") or "",
        "note": (
            "Negative constraints for Kıyas generation (AD4/[GB]). A match is "
            "a prompt to check relatedness, never an automatic rejection."
        ),
    }


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Export refuted patterns for Kıyas")
    ap.add_argument("registry", help="path to mizan-registry.yaml")
    ap.add_argument("-o", "--out", help="write here instead of stdout")
    args = ap.parse_args(argv)

    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")  # type: ignore[union-attr]
        except (AttributeError, ValueError):
            pass

    try:
        data = yaml.safe_load(open(args.registry, "r", encoding="utf-8")) or {}
    except Exception as exc:
        sys.stderr.write(f"parse error: {exc}\n")
        return 2

    text = yaml.safe_dump(build(data), allow_unicode=True, sort_keys=False)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
