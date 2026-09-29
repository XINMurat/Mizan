#!/usr/bin/env python3
"""Build blinded scoring packets for EVAL-003.

For each task: the six arm outputs (3 arms x 2 reps) plus two calibration
entries -- a KNOWN POSITIVE written from the answer key and a KNOWN NEGATIVE
that finds nothing -- are stripped of arm-revealing marks, shuffled with a
seed fixed in the preregistration, and labelled X1..X8. The mapping goes to
scores/mapping.json, which the scorer is never given.

Stripped: evidence-tier tags ([K], [H], [KKE], [H-aday], ...), and the words
Mizan/Kiyas. Blinding stays imperfect -- style and length still differ by arm
-- and the preregistration says so.
"""
import json, os, random, re, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261001
TAGS = re.compile(r"`?\[(?:K|H|S|Y|R|KKE|H-aday|NK)\]`?")
NAMES = re.compile(r"\b(?:Mizan|mizan|MIZAN|K[ıi]yas)\b")
NEGATIVE = ("The report looks broadly reasonable. The claims are plausible and "
            "clearly presented; I do not see major problems.")


def strip(text: str) -> str:
    return NAMES.sub("the method", TAGS.sub("", text))


def positive(task_key: dict) -> str:
    lines = []
    for k in sorted(task_key):
        v = task_key[k]
        if k.startswith("D"):
            lines.append(f"- Item {v['item']}: not supported -- {v['mechanism']}.")
        else:
            lines.append(f"- Item {v['item']}: adequately supported ({v['why']}).")
    return "\n".join(lines)


def main() -> int:
    key = yaml.safe_load(open(os.path.join(HERE, "key.yaml"), encoding="utf-8"))
    rng = random.Random(SEED)
    mapping = {}
    os.makedirs(os.path.join(HERE, "scores", "packets"), exist_ok=True)
    for task in sorted(key):
        entries = []
        for arm in "ABC":
            for rep in (1, 2):
                p = os.path.join(HERE, "runs", f"{task}-{arm}-{rep}.md")
                if not os.path.exists(p):
                    print(f"missing run: {p}", file=sys.stderr)
                    return 2
                entries.append((f"{arm}{rep}", strip(open(p, encoding="utf-8").read())))
        entries.append(("CAL+", positive(key[task])))
        entries.append(("CAL-", NEGATIVE))
        rng.shuffle(entries)
        mapping[task] = {}
        parts = [open(os.path.join(HERE, "tasks", f"{task}.md"), encoding="utf-8").read(),
                 "\n\n=== REVIEWS TO SCORE ===\n"]
        for i, (who, text) in enumerate(entries, 1):
            mapping[task][f"X{i}"] = who
            parts.append(f"\n----- X{i} -----\n{text.strip()}\n")
        open(os.path.join(HERE, "scores", "packets", f"{task}.md"), "w",
             encoding="utf-8").write("".join(parts))
    json.dump(mapping, open(os.path.join(HERE, "scores", "mapping.json"), "w"), indent=1)
    print("packets written:", ", ".join(sorted(mapping)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
