Here is a pull request description. Assess whether its claims are adequately supported before this is merged.

---
**PR #482 — faster config parser**

1. All tests pass. (CI summary: 214 passed, 3 skipped — the three skipped tests are the ones in `test_parser_legacy.py`.)
2. Parsing is 40% faster. Measured once on my laptop against the production latency numbers from last month's dashboard.
3. No behaviour change. (The diff also changes the default of `strict_mode` from `true` to `false`.)
4. Security reviewed — I went through the input handling myself and it looks fine.
5. Added 12 unit tests covering the new parser branches; the coverage report is attached (branch coverage 81% → 88%).
6. Backward compatible: ran client v3.2 against the new server in staging, 200 requests, 0 errors, logs attached.
