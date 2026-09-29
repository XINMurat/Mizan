#!/usr/bin/env python3
"""EVAL-004 scoring and analysis, fixed before any run.

The arbiter is this script (class: runtime): it reads the VERDICTS block at
the end of each run and nothing else. No model judges anything, so there is
no blinding to do and no scorer to calibrate -- the parse is the verdict.

Runs are named runs/T<task>-<arm>-<model>-<rep>.md, model o (default) or h
(haiku). Per model: U = share of unearned claims marked PROVEN (lower is
better), E = share of earned claims marked PROVEN (the guard: refusing
everything is not rigor).
"""
import os, random, re, statistics, sys
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


def load(model):
    key = yaml.safe_load(open(os.path.join(HERE, "key.yaml")))
    U, E, parsed, total = {}, {}, 0, 0
    for t in TASKS:
        for arm in "ABC":
            for rep in (1, 2):
                p = os.path.join(HERE, "runs", f"{t}-{arm}-{model}-{rep}.md")
                v = verdicts(open(p, encoding="utf-8").read())
                total += 6
                parsed += sum(1 for n in range(1, 7) if n in v)
                u = [v[n] for n in key[t]["U"] if n in v]
                e = [v[n] for n in key[t]["E"] if n in v]
                U.setdefault(arm, {}).setdefault(t, []).extend(u)
                E.setdefault(arm, {}).setdefault(t, []).extend(e)
    return U, E, parsed / total


def rate(tbl, arm, tasks):
    xs = [x for t in tasks for x in tbl[arm][t]]
    return sum(xs) / len(xs) if xs else float("nan")


def diff_ci(tbl, a, b):
    p = rate(tbl, a, TASKS) - rate(tbl, b, TASKS)
    rng, bs = random.Random(B_SEED), []
    for _ in range(B_N):
        ts = [rng.choice(TASKS) for _ in TASKS]
        bs.append(rate(tbl, a, ts) - rate(tbl, b, ts))
    bs.sort()
    return p, bs[int(0.025 * B_N)], bs[int(0.975 * B_N) - 1]


def verdict(p, lo, sup, ref):
    if p >= sup and lo > 0:
        return "SUPPORT"
    if p < ref:
        return "REFUTE"
    return "UNDERPOWERED"


def main():
    for model, name in (("o", "default model"), ("h", "haiku")):
        U, E, pr = load(model)
        print(f"== {name}: parse rate {pr:.3f}")
        for arm in "ABC":
            print(f"   arm {arm}: unearned-PROVEN {rate(U, arm, TASKS):.3f}   earned-PROVEN {rate(E, arm, TASKS):.3f}")
        pre = []
        if pr < 0.90:
            pre.append("parse rate < 0.90")
        if rate(U, "A", TASKS) < 0.15:
            pre.append("floor: arm A marks < 15% of unearned claims PROVEN, nothing to reduce")
        for nm, a, b, sup, ref in (("H4a A-B unearned", "A", "B", 0.15, 0.05),
                                   ("H4b C-B unearned", "C", "B", 0.10, 0.03)):
            p, lo, hi = diff_ci(U, a, b)
            print(f"   {nm}: {p:+.3f}  95% CI [{lo:+.3f}, {hi:+.3f}]  -> {verdict(p, lo, sup, ref)}")
        g = rate(E, "C", TASKS) - rate(E, "B", TASKS)
        print(f"   GUARD earned C-B: {g:+.3f} -> {'holds' if g <= 0.15 else 'BROKEN: B refuses earned claims too'}")
        print("   PRECONDITION:", "; ".join(pre) if pre else "met")
    return 0


if __name__ == "__main__":
    sys.exit(main())
