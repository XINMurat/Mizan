#!/usr/bin/env python3
"""EVAL-001 analysis, fixed before any run. Reads scores/<task>.json and
scores/mapping.json; prints per-arm rates, differences with a task-level
bootstrap 95% CI, calibration, and the verdict each preregistered rule gives."""
import json, os, random, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TASKS = [f"T{i}" for i in range(1, 7)]
B_SEED, B_N = 7, 10000


def load():
    mapping = json.load(open(os.path.join(HERE, "scores", "mapping.json")))
    det, ff, cal_ok = {}, {}, True
    for t in TASKS:
        sc = json.load(open(os.path.join(HERE, "scores", f"{t}.json")))
        for x, who in mapping[t].items():
            s = sc[x]
            d = sum(int(s[f"D{i}"]) for i in range(1, 5)) / 4
            f = (int(s["S1"]) + int(s["S2"])) / 2
            if who == "CAL+":
                cal_ok &= (d == 1.0 and f == 0.0)
            elif who == "CAL-":
                cal_ok &= (d == 0.0 and f == 0.0)
            else:
                det.setdefault(who[0], {}).setdefault(t, []).append(d)
                ff.setdefault(who[0], {}).setdefault(t, []).append(f)
    return det, ff, cal_ok


def arm_rate(tbl, arm, tasks):
    return statistics.mean(v for t in tasks for v in tbl[arm][t])


def diff_ci(tbl, a, b):
    point = arm_rate(tbl, a, TASKS) - arm_rate(tbl, b, TASKS)
    rng, boots = random.Random(B_SEED), []
    for _ in range(B_N):
        ts = [rng.choice(TASKS) for _ in TASKS]
        boots.append(arm_rate(tbl, a, ts) - arm_rate(tbl, b, ts))
    boots.sort()
    return point, boots[int(0.025 * B_N)], boots[int(0.975 * B_N) - 1]


def words():
    out = {}
    for arm in "ABC":
        n = [len(open(os.path.join(HERE, "runs", f"{t}-{arm}-{r}.md"), encoding="utf-8").read().split())
             for t in TASKS for r in (1, 2)]
        out[arm] = statistics.mean(n)
    return out


def verdict(point, lo, support, refute):
    if point >= support and lo > 0:
        return "SUPPORT"
    if point < refute:
        return "REFUTE"
    return "UNDERPOWERED"


def main():
    det, ff, cal_ok = load()
    print("calibration (known positive = 1.0/0.0, known negative = 0.0/0.0):",
          "PASS" if cal_ok else "FAIL -> precondition failed, no verdict")
    for arm in "ABC":
        print(f"arm {arm}: detection {arm_rate(det, arm, TASKS):.3f}  false-flag {arm_rate(ff, arm, TASKS):.3f}")
    w = words()
    print("mean words:", {k: round(v) for k, v in w.items()})
    res = {}
    for name, a, b, sup, ref in (("H1 B-A detection", "B", "A", 0.15, 0.05),
                                 ("H2 B-C detection", "B", "C", 0.10, 0.03)):
        p, lo, hi = diff_ci(det, a, b)
        res[name] = verdict(p, lo, sup, ref)
        print(f"{name}: {p:+.3f}  95% CI [{lo:+.3f}, {hi:+.3f}]  -> {res[name]}")
    p, lo, hi = diff_ci(ff, "B", "C")
    guard = p <= 0.10
    print(f"GUARD B-C false-flag: {p:+.3f}  95% CI [{lo:+.3f}, {hi:+.3f}]  -> {'holds' if guard else 'BROKEN: detection bought by over-flagging'}")
    ceiling = arm_rate(det, "A", TASKS) > 0.85
    if ceiling:
        print("PRECONDITION: arm A detection > 0.85 -> tasks too easy; no [R] can be read from this run")
    if not cal_ok:
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
