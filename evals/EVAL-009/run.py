"""EVAL-009 runner: one fresh API call per run, no tools, no system prompt.

    python evals/EVAL-009/run.py --task T1          # 9 runs: 3 arms x 3 reps
    python evals/EVAL-009/run.py --task T1 --dry    # write prompts only

Prompts are rebuilt from committed files every time and written to
runs/prompts/ so the exact text each run saw is on record. An existing run file
is never overwritten: re-running a task only fills gaps (the exclusion rule's
single re-run is done by moving the excluded file to runs/excluded/ first).
Reads ANTHROPIC_API_KEY from the environment.
"""
import argparse
import hashlib
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MODEL = "claude-haiku-5-5"
MAX_TOKENS = 32000
ARMS = ("O", "P", "C")
REPS = (1, 2, 3)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def arm_body(arm):
    if arm == "O":
        # SKILL.md body without front matter, as EVAL-003 arm B used it
        text = read(os.path.join(ROOT, "skill", "mizan", "SKILL.md"))
        return text.split("\n---\n", 1)[1].lstrip("\n")
    return read(os.path.join(ROOT, "evals", "EVAL-008", "arms", f"{arm}.md"))


def task_text(task):
    # the "# Task" section of EVAL-007's prompt (EVAL-006's tasks), byte-identical
    p = read(os.path.join(ROOT, "evals", "EVAL-007", "runs", "prompts", f"{task}-O.md"))
    return p[p.index("# Task"):]


def prompt(task, arm):
    return "# Instructions\n\n" + arm_body(arm).rstrip("\n") + "\n\n" + task_text(task)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True, choices=[f"T{i}" for i in range(1, 7)])
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()

    os.makedirs(os.path.join(HERE, "runs", "prompts"), exist_ok=True)
    log_path = os.path.join(HERE, "runs", "log.jsonl")
    client = None
    if not a.dry:
        import anthropic
        client = anthropic.Anthropic()

    for arm in ARMS:
        p = prompt(a.task, arm)
        pp = os.path.join(HERE, "runs", "prompts", f"{a.task}-{arm}.md")
        with open(pp, "w", encoding="utf-8", newline="\n") as f:
            f.write(p)
        sha = hashlib.sha256(p.encode("utf-8")).hexdigest()[:12]
        for rep in REPS:
            out = os.path.join(HERE, "runs", f"{a.task}-{arm}-{rep}.md")
            if a.dry or os.path.exists(out):
                continue
            with client.messages.stream(model=MODEL, max_tokens=MAX_TOKENS,
                                        messages=[{"role": "user", "content": p}]) as st:
                r = st.get_final_message()
            text = "".join(b.text for b in r.content if b.type == "text")
            with open(out, "w", encoding="utf-8", newline="\n") as f:
                f.write(text)
            rec = {"run": f"{a.task}-{arm}-{rep}", "model": r.model, "prompt_sha": sha,
                   "stop": r.stop_reason, "in": r.usage.input_tokens,
                   "out": r.usage.output_tokens, "at": time.strftime("%Y-%m-%dT%H:%M:%S")}
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(rec) + "\n")
            print(rec, file=sys.stderr)


if __name__ == "__main__":
    main()
