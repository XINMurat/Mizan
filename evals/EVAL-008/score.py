"""EVAL-008 scorer runner: one fresh API call per blinded packet.

    python evals/EVAL-008/score.py            # all packets without a score file

The scorer sees SCORER.md, the task's answer key and the blinded packet, never
scores/mapping.json. Raw replies are kept in scores/raw/; the parsed JSON goes
to scores/<task>.json. An existing score file is never overwritten.
"""
import json
import os
import re
import sys
import time

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = "claude-opus-5-5"
MAX_TOKENS = 32000
TASKS = [f"T{i}" for i in range(1, 7)]


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def main():
    import anthropic
    client = anthropic.Anthropic()
    key = yaml.safe_load(read(os.path.join(HERE, "..", "EVAL-003", "key.yaml")))
    os.makedirs(os.path.join(HERE, "scores", "raw"), exist_ok=True)
    for t in TASKS:
        out = os.path.join(HERE, "scores", f"{t}.json")
        if os.path.exists(out):
            continue
        prompt = (read(os.path.join(HERE, "SCORER.md")) + "\n\n# Answer key\n\n"
                  + yaml.safe_dump({t: key[t]}, allow_unicode=True, sort_keys=True)
                  + "\n\n# Packet\n\n" + read(os.path.join(HERE, "scores", "packets", f"{t}.md")))
        with client.messages.stream(model=MODEL, max_tokens=MAX_TOKENS,
                                    messages=[{"role": "user", "content": prompt}]) as st:
            r = st.get_final_message()
        text = "".join(b.text for b in r.content if b.type == "text")
        with open(os.path.join(HERE, "scores", "raw", f"{t}.txt"), "w", encoding="utf-8") as f:
            f.write(text)
        m = re.search(r"\{.*\}", text, re.S)
        data = json.loads(m.group(0))
        with open(out, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=0)
        print({"task": t, "model": r.model, "stop": r.stop_reason, "in": r.usage.input_tokens,
               "out": r.usage.output_tokens, "at": time.strftime("%H:%M:%S")}, file=sys.stderr)


if __name__ == "__main__":
    main()
