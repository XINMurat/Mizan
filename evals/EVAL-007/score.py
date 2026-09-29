#!/usr/bin/env python3
"""EVAL-007 scoring, fixed before any run. Arbiter class: runtime.

EVAL-006's scorer with the arms renamed. Runs are runs/T<task>-<arm>-<rep>.md
on haiku; arm O = the SKILL.md EVAL-004 used (EVAL-006's O prompt, byte for
byte), arm C = EVAL-006's N prompt with the rule's EVAL-004 citation put back,
i.e. the wording SKILL.md ships. C and N differ only in that parenthesis.
The secondary line (without T3) is preregistered here, because RES-EVAL-006
raised a possible key error on T3 #3 after the fact.
"""
import os, random, re, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
TASKS = [f"T{i}" for i in range(1, 7)]
LINE = re.compile(r"^\W*(\d)\W*\s*[:.)\-–]\s*\W*(NOT\s+PROVEN|PROVEN)\b", re.I | re.M)
B_SEED, B_N = 11, 10000


def verdicts(text):
    i = text.upper().rfind("VERDICTS")
    if i < 0:
        return {}
    out = {}
    for m in LINE.finditer(text[i:]):
        out.setdefault(int(m.group(1)), not m.group(2).upper().startswith("NOT"))
    return out


def load():
    key = yaml.safe_load(open(os.path.join(HERE, "key.yaml")))
    U, E, W, parsed, total = {}, {}, {}, 0, 0
    for t in TASKS:
        for arm in "OC":
            for rep in (1, 2):
                text = open(os.path.join(HERE, "runs", f"{t}-{arm}-{rep}.md"), encoding="utf-8").read()
                v = verdicts(text)
                total += 6
                parsed += sum(1 for n in range(1, 7) if n in v)
                U.setdefault(arm, {}).setdefault(t, []).extend(v[n] for n in key[t]["U"] if n in v)
                E.setdefault(arm, {}).setdefault(t, []).extend(v[n] for n in key[t]["E"] if n in v)
                W.setdefault(arm, {}).setdefault(t, []).append(len(text.split()))
    return U, E, W, parsed / total


def rate(tbl, arm, tasks):
    xs = [x for t in tasks for x in tbl[arm][t]]
    return sum(xs) / len(xs) if xs else float("nan")


def ci(tbl, f):
    rng, bs = random.Random(B_SEED), []
    for _ in range(B_N):
        ts = [rng.choice(TASKS) for _ in TASKS]
        bs.append(f(tbl, ts))
    bs.sort()
    return f(tbl, TASKS), bs[int(0.025 * B_N)], bs[int(0.975 * B_N) - 1]


def main():
    U, E, W, pr = load()
    print(f"haiku: parse rate {pr:.3f}")
    for arm in "OC":
        print(f"  arm {arm}: earned-PROVEN {rate(E, arm, TASKS):.3f}  "
              f"unearned-PROVEN {rate(U, arm, TASKS):.3f}  mean words {rate(W, arm, TASKS):.0f}")
    if pr < 0.90:
        print("PRECONDITION FAILED: parse rate < 0.90 -- no verdict"); return 0
    if rate(E, "O", TASKS) > 0.90:
        print("PRECONDITION FAILED: arm O refused < 10% of earned claims this time; "
              "the over-refusal did not reproduce on these tasks, nothing to repair -- no verdict")
        return 0
    d, lo, hi = ci(E, lambda t, ts: rate(t, "C", ts) - rate(t, "O", ts))
    v = "SUPPORT" if d >= 0.10 and lo > 0 else ("REFUTE" if d < 0.03 else "UNDERPOWERED")
    print(f"H7a earned C-O: {d:+.3f}  95% CI [{lo:+.3f}, {hi:+.3f}] -> {v}")
    g, glo, ghi = ci(U, lambda t, ts: rate(t, "C", ts) - rate(t, "O", ts))
    print(f"GUARD unearned C-O: {g:+.3f}  CI [{glo:+.3f}, {ghi:+.3f}] -> "
          f"{'holds' if g <= 0.05 else 'BROKEN: the new rule lets unearned claims through'}")
    r, rlo, rhi = ci(W, lambda t, ts: rate(t, "C", ts) / rate(t, "O", ts))
    v = "SUPPORT" if r <= 0.80 and rhi < 1 else ("REFUTE" if r >= 0.95 else "UNDERPOWERED")
    print(f"H7b words C/O: {r:.3f}  95% CI [{rlo:.3f}, {rhi:.3f}] -> {v}")
    no3 = [t for t in TASKS if t != "T3"]
    print(f"secondary, without T3: earned O {rate(E, 'O', no3):.3f}  C {rate(E, 'C', no3):.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
