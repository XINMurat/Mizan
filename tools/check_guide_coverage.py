#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The usage guides must teach every rule the validator enforces.

Both guides headed their rule section "R1–R28 in the schema" and stopped
explaining at rule 22 -- three schema versions (1.10, 1.11, 1.12) and six
rules behind, with the warnings at W1–W5 while the schema had reached W8. The
heading was pinned to nothing, so it stayed right while the content went stale
under it. Each guide also stated "the shipped schema" as a number, and the two
numbers disagreed with each other and with the schema (1.5, 1.8, actual 1.12).

So this checks two things against the schema file, which is the source:

  * every rule number R1..Rn and warning number W1..Wn defined in the schema
    appears in each guide (as `R23`, `W8`, or as the numbered item `23.`
    inside the hard-rules section -- the guides teach rules as a list);
  * no guide states a shipped/current schema version as a number. The
    sentence names the schema banner instead, so it cannot go stale.

Usage:
    python tools/check_guide_coverage.py    # exit 1 if a guide fell behind
"""
from __future__ import annotations

import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA = os.path.join(ROOT, "skill", "mizan", "schemas", "mizan-registry.yaml")
GUIDES = ["docs/en/usage-guide.md", "docs/tr/kullanim-kilavuzu.md"]

DEFINED = re.compile(r"^#\s+([RW])(\d+)\.\s", re.M)
SECTION = re.compile(r"^## 3\. .*?(?=^## 4\. )", re.M | re.S)
STALE_CLAIM = re.compile(
    r"(shipped schema is|current schema is|Dağıtılan şema|güncel şema)"
    r"\s+\d+\.\d+", re.I)


def read(path):
    with io.open(path, encoding="utf-8") as fh:
        return fh.read()


def mentioned(text, kind, num):
    """`R23` / `W8` anywhere, or a rule taught as list item `23.`."""
    if re.search(r"\b%s%d\b" % (kind, num), text):
        return True
    if kind == "W" and re.search(r"\bW1[–-]W(\d+)\b", text):
        top = max(int(m) for m in re.findall(r"\bW1[–-]W(\d+)\b", text))
        if num <= top:
            return True
    if kind == "R":
        section = SECTION.search(text)
        if section and re.search(r"^%d\. " % num, section.group(0), re.M):
            return True
    return False


def main():
    schema = read(SCHEMA)
    defined = sorted({(k, int(n)) for k, n in DEFINED.findall(schema)})
    if not defined:
        sys.stderr.write("FAIL: found no rule definitions in %s -- the "
                         "pattern no longer matches the schema\n" % SCHEMA)
        return 1

    problems = []
    for rel in GUIDES:
        text = read(os.path.join(ROOT, rel))
        missing = ["%s%d" % (k, n) for k, n in defined
                   if not mentioned(text, k, n)]
        if missing:
            problems.append("%s does not teach: %s" % (rel, " ".join(missing)))
        for m in STALE_CLAIM.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            problems.append("%s:%d states the schema version as a number "
                            "(%r) -- name the schema banner instead"
                            % (rel, line, m.group(0)))

    if problems:
        sys.stderr.write("FAIL: a usage guide fell behind the schema:\n")
        for line in problems:
            sys.stderr.write("  " + line + "\n")
        return 1
    r = max(n for k, n in defined if k == "R")
    w = max(n for k, n in defined if k == "W")
    print("ok  %d guide(s) teach R1-R%d and W1-W%d; no pinned schema number"
          % (len(GUIDES), r, w))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
