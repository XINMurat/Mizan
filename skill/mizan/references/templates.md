# Mizan Templates

Contents:
1. Registry Entry template (prospective)
2. Result block format (appended to entries)
3. Audit Report template (retrospective)
4. Compact claim-line format (for inline audits)

All templates are bilingual-friendly: keep the tier tags as-is
(`[K]/[H]/[S]/[R]/[KKE]/[Y]`), write prose in the user's language.

---

## 1. Registry Entry template

Write the entry BEFORE the test runs. Every field is mandatory except
"Prior art" (mandatory only when relatives are known or suspected).

```markdown
### HX — <short hypothesis name> `[H]` `[önkayıt / preregistered YYYY-MM-DD]`
*(Köken / Origin: where this hypothesis came from — user intuition,
prior result, external suggestion. One or two lines.)*

- **Formel / Formal:** the claim as a precise, testable statement.
- **Metrik / Metric:** what will be measured, and with what instrument
  (file, script, query, data source).
- **Eşik / Threshold:** the numeric decision rule, LOCKED now.
  "X ≥ N → supported; X < M → refuted; between → underpowered, one rerun."
- **Çürütme / Refutation:** what result kills the hypothesis. Check
  two-sided informativeness: state what EACH outcome would teach.
- **Bilgilendiricilik önkoşulu / Informativeness precondition:** (when
  relevant) what must hold for the test to count at all.
- **Önkayıtlı öngörü / Preregistered prediction:** (optional but valuable)
  what the author expects, written before the result. A wrong prediction
  honestly recorded is a feature.
- **Prior art:** known relatives; where the originality claim lives.
- **Maliyet / Cost:** rough effort so priorities can be ordered.
- **DURUM / STATUS:** ⏳ preregistered, not run.
```

## 2. Result block format

Append to the entry; never overwrite earlier blocks.

```markdown
- **SONUÇ / RESULT (YYYY-MM-DD):** measured values, verbatim.
  Threshold met? YES/NO/PRECONDITION FAILED.
  Decision: `[H]→[K]` / `[H]→[R]` / cell closed (precondition) /
  underpowered (one rerun allowed, say what changes).
- **Dürüstlük şerhleri / Honesty annexes:** scope limits, n, seeds,
  instrument dependence, anything a hostile reviewer would find.
- **Sonradan akıl yürütme / Post-hoc reasoning:** (if any) clearly labeled
  as not preregistered.
- **Confound-kontrolü / Confound control:** (mandatory before promoting a
  SURPRISING positive to `[K]`) the symmetric control run and its result,
  or a sub-entry preregistering it. The headline waits for this.
- Ham çıktı / Raw output: <path or link>.
```

## 3. Audit Report template

```markdown
# Mizan Denetimi / Mizan Audit — <document name> (YYYY-MM-DD)

## 0. Denetim beyanı / Audit declaration
- Scope: N atomic claims extracted; M were checkable with available
  sources (list source types: conversation history, files, commits, web).
- HARKing status: this audit is retrospective; examples in the source
  document were selected after outcomes were known, and this audit's own
  coverage is limited to accessible evidence.

## 1. İddia tablosu / Claim table
| # | Claim (quoted or tightly paraphrased) | Tier | Source / justification (one line) |
|---|---|---|---|

## 2. Karşı-örnek taraması / Counter-example sweep
For each pattern-claim: what was searched, what was found, including
empty results ("no counter-example in N sources").

## 3. İsabet oranı / Hit rate
Where the document praises judgment or predictions: the reconstructed
full record — wins AND losses — with the honest rate.

## 4. Eksik kart / The missing card
What this document's format structurally cannot show, sketched from
available evidence (failures, deferrals, abandoned lines, costs).

## 5. Yapısal teşhis / Structural diagnosis
Why the document is skewed the way it is — mechanism over motive
(selection pressure, format incentives), unless intent is evidenced.

## 6. Ayakta kalanlar / What survives
The claims that passed, stated with the same specificity as the
failures. If nothing survives, question the audit's own thresholds.

## 7. Sonraki adımlar / Next steps
Ordered by criticality × (impact / effort). If the user wants ongoing
tracking, seed a registry from the surviving [H] claims.
```

## 4. Compact claim-line format

For quick inline audits (chat replies, not documents):

```
"<claim>" → [TIER] — one-line justification (source).
```

Example:

```
"Each fix got its own descriptive commit" → [K] — verified in repo
history, 14/14 fixes have dedicated commits (github.com/.../commits).
"You catch bad numbers before you can say why" → [H] — 3 confirming
instances found, prediction record incomplete; full hit rate needs the
project-scoped conversations (inaccessible from here).
```
