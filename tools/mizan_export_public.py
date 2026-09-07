#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mizan_export_public.py — private registry -> publishable excerpt.

WHY THIS EXISTS
---------------
`mizan-product-registry.yaml` is gitignored on purpose: it carries pricing
notes, market projections and an on-prem roadmap alongside entries that are
about nothing but the method. That is a reasonable thing to keep private and
an unreasonable thing to keep whole, because the public write-ups that cite
this registry -- the case study, the family page -- then rest on a file no
reader can open. Under R8 that leaves every one of those claims
author-reported: a permanent [KKE] bought by an accident of file layout.

This script publishes the part that can be published, and nothing else.

ALLOWLIST, NOT BLOCKLIST -- the one design decision here
-------------------------------------------------------
An entry is exported ONLY if it carries `visibility: "public"`. Absence is
not permission. The alternative (list what to strip) fails in the direction
that matters: a new entry written next month leaks by default, and nobody
notices, because a blocklist is silent about what it has never heard of.
This is the same commitment the schema makes elsewhere -- "no known
relatives" is an answer and an absent field is silence.

Two consequences worth stating:

  * The export is smaller than the registry, always, and the header says by
    how much. A reader who knows 4 of 15 entries are published knows the
    excerpt is an excerpt. An export that hid its own ratio would be the
    survivorship problem this method is named for, committed by the tool.

  * Redaction is per-ENTRY, not per-field. There is no partial entry: an
    entry whose threshold is public but whose cost is not stays private
    whole. Field-level redaction produces documents that look complete and
    are not, and a reader cannot tell which fields were removed.

USAGE
    python tools/mizan_export_public.py mizan-product-registry.yaml \\
        -o docs/registry-excerpt.yaml

The output passes mizan_validate.py -- an excerpt that could not survive the
project's own validator would not be worth publishing.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    print("PyYAML required: pip install -r tools/requirements.txt", file=sys.stderr)
    raise SystemExit(2)

# The blocks an entry can live in. `probes` is handled separately: it is a
# mapping of lists, not a list.
ENTRY_BLOCKS = ("hypotheses", "features", "design_constraints", "refuted_and_discarded")

HEADER = """\
# =====================================================================
# Mizan urun registry'si — YAYINLANABILIR ALINTI / PUBLIC EXCERPT
#
# Uretildi / generated: {date}
# Kaynak / source: {src} (gitignore'lu, yayinlanmiyor / private, unpublished)
# Uretici / generator: tools/mizan_export_public.py
#
# BU DOSYA BIR ALINTIDIR. Kaynak registry {total} girdi tasiyor; burada
# {kept} tanesi var. Disarida kalanlar silinmedi -- yalnizca
# `visibility: public` tasimadiklari icin export edilmediler. Izin
# yoklugu izin degildir: bir girdi acikca isaretlenmediyse ozel kalir.
#
# THIS FILE IS AN EXCERPT. The source registry holds {total} entries and
# {kept} of them are here. The rest were not deleted -- they simply do not
# carry `visibility: public`. Absence is not permission.
#
# Alintida OLMAYAN bir girdiye dayanan her iddia, okuyucu tarafindan
# denetlenemez ve R8 geregi kalici [KKE] tasir. Bunu soylemek bu dosyanin
# isinin yarisidir.
# =====================================================================

"""


def _public(entry: dict) -> bool:
    return isinstance(entry, dict) and entry.get("visibility") == "public"


def export(doc: dict) -> tuple[dict, int, int]:
    """Return (excerpt, kept, total). Counts every entry in every block."""
    out: dict = {}
    kept = total = 0

    reg = dict(doc.get("registry") or {})
    # `project` is preserved, not renamed. Downstream tools key on it --
    # mizan_export_refuted.py stamps it into every exported pattern as
    # `source_registry` -- and renaming it here produced a chain of empty
    # provenance fields two hops away. `excerpt: true` is the marker; the
    # identity stays what it was.
    reg["excerpt"] = True
    out["registry"] = reg

    for block in ENTRY_BLOCKS:
        entries = doc.get(block) or []
        if not isinstance(entries, list):
            continue
        total += len(entries)
        keep = [e for e in entries if _public(e)]
        kept += len(keep)
        if keep:
            out[block] = keep

    probes = doc.get("probes")
    if isinstance(probes, dict):
        kept_probes: dict = {}
        for name, rows in probes.items():
            if not isinstance(rows, list):
                continue
            total += len(rows)
            keep = [r for r in rows if _public(r)]
            kept += len(keep)
            if keep:
                kept_probes[name] = keep
        if kept_probes:
            out["probes"] = kept_probes

    return out, kept, total


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("registry", help="the private registry to read")
    ap.add_argument("-o", "--out", required=True, help="excerpt to write")
    args = ap.parse_args(argv)

    with open(args.registry, encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)
    if not isinstance(doc, dict):
        print("registry is not a mapping", file=sys.stderr)
        return 2

    excerpt, kept, total = export(doc)
    if kept == 0:
        # Not an error, and not something to write silently either: an empty
        # excerpt published next to a page that cites it is worse than no file.
        print(
            "no entry carries `visibility: public` — nothing to export.\n"
            "Mark the entries you intend to publish, one at a time.",
            file=sys.stderr,
        )
        return 1

    body = yaml.safe_dump(excerpt, allow_unicode=True, sort_keys=False, width=88)
    header = HEADER.format(
        date=_dt.date.today().isoformat(),
        src=args.registry.replace("\\", "/"),
        total=total,
        kept=kept,
    )
    with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(header + body)

    print(f"wrote {args.out} — {kept} of {total} entries ({total - kept} withheld)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
