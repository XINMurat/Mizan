#!/usr/bin/env python3
"""EVAL-009 scoring, fixed before any run. Arbiter class: runtime.

EVAL-007's scorer (verdicts/load/rate/ci unchanged in logic) with arms O/P/C
and reps 1-3; verdict rules are H-EVAL-009a/b/c's from the registry.
"""
import os, random, re, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
TASKS = [f"T{i}" for i in range(1, 7)]
ARMS, REPS = "OPC", (1, 2, 3)
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
    key = yaml.safe_load(open(os.path.join(HERE, "key.yaml"), encoding="utf-8"))
    U, E, W, parsed, total = {}, {}, {}, 0, 0
    for t in TASKS:
        for arm in ARMS:
            for rep in REPS:
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


def noninferior(E, U, a):
    d, lo, hi = ci(E, lambda t, ts: rate(t, a, ts) - rate(t, "O", ts))
    g, glo, ghi = ci(U, lambda t, ts: rate(t, a, ts) - rate(t, "O", ts))
    if d >= -0.05 and lo > -0.15 and g <= 0.05:
        v = "SUPPORT"
    elif d <= -0.10 or g >= 0.10:
        v = "REFUTE"
    else:
        v = "UNDERPOWERED"
    return d, lo, hi, g, glo, ghi, v


def main():
    U, E, W, pr = load()
    print(f"haiku-5-5: parse rate {pr:.3f}")
    for arm in ARMS:
        print(f"  arm {arm}: earned-PROVEN {rate(E, arm, TASKS):.3f}  "
              f"unearned-PROVEN {rate(U, arm, TASKS):.3f}  mean words {rate(W, arm, TASKS):.0f}")
    if pr < 0.90:
        print("PRECONDITION FAILED: parse rate < 0.90 -- no verdict"); return 0
    moves = max(1 - rate(E, a, TASKS) for a in ARMS) >= 0.10 or max(rate(U, a, TASKS) for a in ARMS) >= 0.10
    if not moves:
        print("PRECONDITION FAILED (a, c): every arm within 10% of the key on both classes -- "
              "the tasks do not separate arms, no verdict")
    for name, a in (("H9a P vs O", "P"), ("H9c C vs O", "C")):
        d, lo, hi, g, glo, ghi, v = noninferior(E, U, a)
        print(f"{name}: earned {d:+.3f} CI [{lo:+.3f}, {hi:+.3f}]; unearned {g:+.3f} "
              f"CI [{glo:+.3f}, {ghi:+.3f}] -> {v if moves else 'no verdict'}")
    if rate(E, "O", TASKS) > 0.90:
        print("PRECONDITION FAILED (b): arm O refused < 10% of earned claims -- no verdict")
    else:
        d, lo, hi = ci(E, lambda t, ts: rate(t, "P", ts) - rate(t, "O", ts))
        v = "SUPPORT" if d >= 0.10 and lo > 0 else ("REFUTE" if d < 0.03 else "UNDERPOWERED")
        print(f"H9b earned P-O: {d:+.3f}  95% CI [{lo:+.3f}, {hi:+.3f}] -> {v}")
    no3 = [t for t in TASKS if t != "T3"]
    print("secondary, without T3: earned " + "  ".join(f"{a} {rate(E, a, no3):.3f}" for a in ARMS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
