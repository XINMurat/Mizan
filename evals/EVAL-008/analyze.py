#!/usr/bin/env python3
"""EVAL-008 analysis, written before any scoring. load(), arm_rate() and
diff_ci() are EVAL-003's unchanged; arms, reps and the verdict rules are
H-EVAL-008a/b/c's as preregistered in eval-008.mizan-registry.yaml."""
import json, os, random, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TASKS = [f"T{i}" for i in range(1, 7)]
REPS = (1, 2, 3)
B_SEED, B_N = 7, 10000


def load():
    mapping = json.load(open(os.path.join(HERE, "scores", "mapping.json")))
    det, ff, cal_ok = {}, {}, True
    for t in TASKS:
        sc = json.load(open(os.path.join(HERE, "scores", f"{t}.json")))
        for x, who in mapping[t].items():
            s = sc[x]
            d = sum(int(s[f"D{i}"]) for i in range(1, 5)) / 4
            sk = [k for k in s if k.startswith("S")]
            f = sum(int(s[k]) for k in sk) / len(sk)
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


def word_table():
    return {arm: {t: [len(open(os.path.join(HERE, "runs", f"{t}-{arm}-{r}.md"),
                                encoding="utf-8").read().split()) for r in REPS]
                  for t in TASKS} for arm in "OPC"}


def ratio_ci(tbl, a, b):
    point = arm_rate(tbl, a, TASKS) / arm_rate(tbl, b, TASKS)
    rng, boots = random.Random(B_SEED), []
    for _ in range(B_N):
        ts = [rng.choice(TASKS) for _ in TASKS]
        boots.append(arm_rate(tbl, a, ts) / arm_rate(tbl, b, ts))
    boots.sort()
    return point, boots[int(0.025 * B_N)], boots[int(0.975 * B_N) - 1]


def main():
    det, ff, cal_ok = load()
    print("calibration:", "PASS" if cal_ok else "FAIL -> precondition failed, no verdict")
    for arm in "OPC":
        print(f"arm {arm}: detection {arm_rate(det, arm, TASKS):.3f}  false-flag {arm_rate(ff, arm, TASKS):.3f}")
    w = word_table()
    print("mean words:", {a: round(arm_rate(w, a, TASKS)) for a in "OPC"})

    ceiling = arm_rate(det, "O", TASKS) > 0.90
    if ceiling:
        print("PRECONDITION: arm O detection > 0.90 -> no verdict for a or b")

    # H-EVAL-008a
    p, lo, hi = diff_ci(det, "P", "O")
    fp, flo, fhi = diff_ci(ff, "P", "O")
    if p >= -0.05 and lo > -0.15 and fp <= 0:
        va = "SUPPORT"
    elif p <= -0.10 or fp >= 0.10:
        va = "REFUTE"
    else:
        va = "UNDERPOWERED"
    print(f"H-EVAL-008a P-O detection {p:+.3f} CI [{lo:+.3f}, {hi:+.3f}]; "
          f"false-flag {fp:+.3f} CI [{flo:+.3f}, {fhi:+.3f}] -> {va}")

    # H-EVAL-008b
    p, lo, hi = diff_ci(det, "C", "O")
    fp, flo, fhi = diff_ci(ff, "C", "O")
    if p >= 0 and fp <= 0:
        vb = "SUPPORT"
    elif p <= -0.08:
        vb = "REFUTE"
    else:
        vb = "UNDERPOWERED"
    print(f"H-EVAL-008b C-O detection {p:+.3f} CI [{lo:+.3f}, {hi:+.3f}]; "
          f"false-flag {fp:+.3f} CI [{flo:+.3f}, {fhi:+.3f}] -> {vb}")

    # H-EVAL-008c
    r, rlo, rhi = ratio_ci(w, "P", "O")
    vc = "SUPPORT" if (r <= 0.80 and rhi < 1) else "REFUTE" if r >= 0.95 else "UNDERPOWERED"
    print(f"H-EVAL-008c P/O words {r:.3f} CI [{rlo:.3f}, {rhi:.3f}] -> {vc}")
    return 3 if not cal_ok else 0


if __name__ == "__main__":
    sys.exit(main())
