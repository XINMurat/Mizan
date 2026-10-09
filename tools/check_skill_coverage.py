#!/usr/bin/env python3
"""Nothing the skill said was lost when its body was pruned.

Every sentence of SKILL.md's body at a baseline git ref must appear, verbatim
after whitespace is collapsed, in the current SKILL.md or one of its
references/*.md. The prune (EVAL-008/009) moved text out of the always-loaded
body; this check is what lets "moved, not deleted" be a [K] claim rather than
the author's word.

    python tools/check_skill_coverage.py            # baseline = v2.9 body
    python tools/check_skill_coverage.py --against <ref>
"""
import argparse
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = "skill/mizan/SKILL.md"
BASELINE = "ca58307"  # last commit with the unpruned v2.9 body


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def body(text):
    return text.split("\n---\n", 1)[1] if text.startswith("---") else text


def sentences(text):
    parts = re.split(r"(?<=[.!?:])\s+|\n\s*\n|\n(?=\s*[-|#*\d])", body(text))
    return [norm(p) for p in parts if len(norm(p)) >= 12]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--against", default=BASELINE)
    a = ap.parse_args()
    old = subprocess.run(["git", "show", f"{a.against}:{SKILL}"], cwd=ROOT,
                         capture_output=True, text=True, encoding="utf-8", check=True).stdout
    haystack = norm("\n".join(open(p, encoding="utf-8").read() for p in
                             [os.path.join(ROOT, SKILL)] +
                             sorted(glob.glob(os.path.join(ROOT, "skill/mizan/references/*.md")))))
    sents = sentences(old)
    missing = [s for s in sents if s not in haystack]
    for s in missing:
        print(f"MISSING: {s[:120]}", file=sys.stderr)
    print(f"{len(sents) - len(missing)}/{len(sents)} sentences of {SKILL}@{a.against} found verbatim")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
