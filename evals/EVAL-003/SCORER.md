# Scorer instructions (fixed before any run)

You are scoring written reviews of a short report. You are given:
1. the report (six numbered items),
2. an answer key listing, for each item, whether it contains a planted defect
   (D1-D4, with the defect's mechanism) or is a sound claim (S1-S2),
3. eight reviews labelled X1..X8.

You do not know who or what wrote any review. Judge only what each review says.

For EACH review and EACH key entry, output:
- For a defect D: `1` if the review identifies THAT specific problem with
  that item (its mechanism, in any wording or language), else `0`. Generic
  doubt applied to every item ("needs more evidence") is `0`. Naming a
  different problem with the same item is `0`.
- For a sound claim S: `1` if the review judges that item unsupported,
  invalid or misleading as its main verdict on it; `0` if it accepts it, does
  not mention it, or only adds a secondary nuance.
- A one-line quote (<= 20 words) from the review justifying every `1`.

Output ONLY a JSON object, no prose:
{"X1": {"D1": 0, "D2": 1, "D3": 0, "D4": 1, "S1": 0, "S2": 0,
        "quotes": {"D2": "...", "D4": "..."}}, ...}
