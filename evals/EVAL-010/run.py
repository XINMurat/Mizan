"""EVAL-010 runner: one fresh conversation per run; the model may read its
arm's skill files through one tool, as an installed skill would.

    python evals/EVAL-010/run.py --task T1

Arm O = SKILL.md body and files at ca58307 (v2.9, unpruned); arm N = the
pruned body and files at d2cef6c. Files are served from those commits' git
objects, so later edits cannot reach a run. Every tool call is logged.
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MODEL = "claude-haiku-5-5"
MAX_TOKENS = 32000
MAX_TURNS = 10
ARMS = {"O": "ca58307", "N": "d2cef6c"}
REPS = (1, 2, 3)
TOOL = {
    "name": "read_skill_file",
    "description": "Read a file of the skill these instructions come from. "
                   "Path relative to the skill root, e.g. references/checklist.md "
                   "or schemas/mizan-registry.yaml.",
    "input_schema": {"type": "object", "properties": {"path": {"type": "string"}},
                     "required": ["path"]},
}


def git_file(commit, path):
    r = subprocess.run(["git", "show", f"{commit}:skill/mizan/{path}"], cwd=ROOT,
                       capture_output=True, text=True, encoding="utf-8")
    return r.stdout if r.returncode == 0 else None


def prompt(task, arm):
    body = git_file(ARMS[arm], "SKILL.md").split("\n---\n", 1)[1].lstrip("\n")
    p = open(os.path.join(ROOT, "evals", "EVAL-007", "runs", "prompts", f"{task}-O.md"),
             encoding="utf-8").read()
    return "# Instructions\n\n" + body.rstrip("\n") + "\n\n" + p[p.index("# Task"):]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True, choices=[f"T{i}" for i in range(1, 7)])
    a = ap.parse_args()
    import anthropic
    client = anthropic.Anthropic()
    os.makedirs(os.path.join(HERE, "runs", "prompts"), exist_ok=True)
    for arm in ARMS:
        p = prompt(a.task, arm)
        with open(os.path.join(HERE, "runs", "prompts", f"{a.task}-{arm}.md"), "w",
                  encoding="utf-8", newline="\n") as f:
            f.write(p)
        sha = hashlib.sha256(p.encode("utf-8")).hexdigest()[:12]
        for rep in REPS:
            out = os.path.join(HERE, "runs", f"{a.task}-{arm}-{rep}.md")
            if os.path.exists(out):
                continue
            msgs, reads, tin, tout, stop = [{"role": "user", "content": p}], [], 0, 0, None
            for _ in range(MAX_TURNS):
                with client.messages.stream(model=MODEL, max_tokens=MAX_TOKENS, tools=[TOOL],
                                            messages=msgs) as st:
                    r = st.get_final_message()
                tin += r.usage.input_tokens
                tout += r.usage.output_tokens
                stop = r.stop_reason
                if stop != "tool_use":
                    break
                msgs.append({"role": "assistant", "content": r.content})
                results = []
                for b in r.content:
                    if b.type == "tool_use":
                        path = str(b.input.get("path", "")).lstrip("/").replace("skill/mizan/", "")
                        text = git_file(ARMS[arm], path)
                        reads.append(path if text is not None else f"{path} (not found)")
                        results.append({"type": "tool_result", "tool_use_id": b.id,
                                        "content": text if text is not None else "File not found."})
                msgs.append({"role": "user", "content": results})
            text = "".join(b.text for b in r.content if b.type == "text")
            with open(out, "w", encoding="utf-8", newline="\n") as f:
                f.write(text)
            rec = {"run": f"{a.task}-{arm}-{rep}", "model": r.model, "prompt_sha": sha,
                   "stop": stop, "reads": reads, "in": tin, "out": tout,
                   "at": time.strftime("%Y-%m-%dT%H:%M:%S")}
            with open(os.path.join(HERE, "runs", "log.jsonl"), "a", encoding="utf-8") as f:
                f.write(json.dumps(rec) + "\n")
            print(rec, file=sys.stderr)


if __name__ == "__main__":
    main()
