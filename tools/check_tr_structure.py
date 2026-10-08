#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A translation that is meant to be one-to-one must keep the source's shape.

check_lang_parity.py asks whether a menu entry can deliver its language. It
never opens the two documents and compares them, and nothing else did either.
So when the adaptation recipe in domain-adaptation.md grew a question 0 -- the
arbiter, the question the recipe itself calls decisive -- the Turkish page kept
saying "answer five questions" and nothing failed. That was not a check that
missed; it was a check that did not exist.

This compares structure, not wording: per `###` section, the number of bullet
items and of numbered items, in the source and in its Turkish counterpart.
Translating a sentence changes neither count; dropping a recipe question or a
catalog line changes one of them.

It only runs on pages that declare `"tr_structure": "1:1"` in
docs/en-mirror.json. The other Turkish pages are adaptations, not line-for-line
translations, and their shapes differ from their sources on purpose -- forcing
the rule on them would fire on every run and teach people to ignore it.

Usage:
    python tools/check_tr_structure.py    # exit 1 if a 1:1 page drifted
"""
from __future__ import annotations

import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP_PATH = os.path.join(ROOT, "docs", "en-mirror.json")

SECTION = re.compile(r"^#{3,4} ")
BULLET = re.compile(r"^- ")
NUMBERED = re.compile(r"^\d+\. ")


def shape(path):
    """[(section index, bullets, numbered)] -- section 0 is the preamble."""
    with io.open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    out = [[0, 0]]
    for line in lines:
        if SECTION.match(line):
            out.append([0, 0])
        elif BULLET.match(line):
            out[-1][0] += 1
        elif NUMBERED.match(line):
            out[-1][1] += 1
    return out


def main():
    with io.open(MAP_PATH, encoding="utf-8") as fh:
        pages = json.load(fh)["pages"]

    checked, problems = 0, []
    for page in pages:
        if page.get("tr_structure") != "1:1":
            continue
        checked += 1
        sources, tr = page["sources"], page["tr"]
        if len(sources) != 1:
            problems.append("%s: 1:1 needs exactly one source, got %d"
                            % (tr, len(sources)))
            continue
        en_shape, tr_shape = shape(sources[0]), shape(tr)
        if len(en_shape) != len(tr_shape):
            problems.append("%s has %d sections, %s has %d"
                            % (sources[0], len(en_shape) - 1,
                               tr, len(tr_shape) - 1))
            continue
        for i, (a, b) in enumerate(zip(en_shape, tr_shape)):
            where = "preamble" if i == 0 else "section %d" % i
            if a[0] != b[0]:
                problems.append("%s %s: %d bullets in the source, %d here"
                                % (tr, where, a[0], b[0]))
            if a[1] != b[1]:
                problems.append("%s %s: %d numbered items in the source, %d here"
                                % (tr, where, a[1], b[1]))

    if problems:
        sys.stderr.write("FAIL: a one-to-one translation lost its shape:\n")
        for line in problems:
            sys.stderr.write("  " + line + "\n")
        return 1
    print("ok  %d one-to-one page(s) keep their source's shape" % checked)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
