# Mizan Tooling — R1–R8 Validator

*(Türkçe aşağıda / Turkish below)*

## English

`mizan_validate.py` is a **judgment-free, LLM-free** static validator for
`mizan-registry.yaml` files. It enforces only the mechanical hard rules
R1–R8 from the schema — it does **not** evaluate whether a hypothesis is
good, only whether the registry is structurally honest.

> This is the cheapest, gate-approved slice of feature **FEAT-M001** in the
> project's private roadmap registry: "a simple pre-commit hook + schema
> validator (LLM-free, R1–R8 static checks only)".
> The semantic auditor (a human or a frontier model) stays separate — that
> separation is rule **R7** itself. The rest of FEAT-M001 (agentic
> auto-fix, CI/CD gate) remains **gated**, pending the preregistered
> success/kill evidence.

### What each rule checks

| Rule | Check |
|---|---|
| R1 | A hypothesis referenced by a result has a locked `threshold` (support+refute) and a `refutation`. |
| R2 | Every experiment has a `baseline` (or a written justification for "none"); a baseline-less experiment cannot propose `H->K`. |
| R3 | Every confound named in a hypothesis is either controlled or explicitly accepted in the experiment. |
| R4 | Append-only: with `--against <gitref>`, history may only grow and no entry may vanish. |
| R5 | Every result has a non-empty `honesty_annexes`. |
| R6 | A `surprising_positive` proposing `H->K` must carry a `confound_control_result`. |
| R7 | A result that *proposes* a tier change must have `decision_confirmed_by` set (producer ≠ sole auditor). |
| R8 | Every hypothesis names its `arbiter` — the judge returning the verdict on its threshold. Class `author` cannot reach K (permanent KKE); class `none` leaves the entry at S. Enforced from `schema_version` 1.2. |

### Usage

```bash
pip install -r tools/requirements.txt

python tools/mizan_validate.py path/to/mizan-registry.yaml
python tools/mizan_validate.py --lang tr registry.yaml      # Turkish messages
python tools/mizan_validate.py --against HEAD registry.yaml  # append-only check
```

Exit codes: `0` clean · `1` violations · `2` usage/parse error.

### Pre-commit hook

```bash
git config core.hooksPath tools/hooks
# or copy tools/hooks/pre-commit into .git/hooks/ and chmod +x it
```

The hook validates any staged `*mizan-registry*.yaml` file, including the
append-only check against `HEAD`. Set `MIZAN_LANG=tr` for Turkish output.

---

## Türkçe

`mizan_validate.py`, `mizan-registry.yaml` dosyaları için **yargısız,
LLM'siz** statik bir doğrulayıcıdır. Yalnızca şemadaki mekanik sert
kuralları (R1–R8) uygular — bir hipotezin *iyi* olup olmadığını değil,
registry'nin yapısal olarak dürüst olup olmadığını denetler.

> Bu, projenin özel yol haritası registry'sindeki **FEAT-M001**
> özelliğinin kapıdan onaylı en ucuz dilimidir:
> "basit pre-commit hook + şema doğrulayıcı (LLM'siz, yalnız R1–R8 statik
> kontrolü)". Anlamsal denetçi (insan veya frontier model) ayrı kalır — bu
> ayrım zaten **R7** kuralıdır. FEAT-M001'in gerisi (ajan otomatik-düzeltme,
> CI/CD gate) önkayıtlı başarı/kill kanıtı gelene dek **kapılı** kalır.

### Kullanım

```bash
pip install -r tools/requirements.txt
python tools/mizan_validate.py --lang tr registry.yaml
python tools/mizan_validate.py --lang tr --against HEAD registry.yaml
```

Çıkış kodları: `0` temiz · `1` ihlal · `2` kullanım/ayrıştırma hatası.

### Pre-commit kancası

```bash
git config core.hooksPath tools/hooks
export MIZAN_LANG=tr   # Türkçe çıktı için
```


---

## `mizan_export_refuted.py` — the Kıyas feedback loop

Mizan's half of the generator↔auditor loop. It reads a registry and emits
`refuted-patterns.yaml`: every entry at tier R or Y, plus permanent KKEs,
turned into negative constraints a generator can consult before proposing a
relative of something already killed.

```bash
python tools/mizan_export_refuted.py registry.yaml -o refuted-patterns.yaml
# then, in the Kıyas repo:
python tools/kiyas_validate.py --refuted refuted-patterns.yaml seeds.yaml
```

It walks `hypotheses`, `bugs`, `features` and `refuted_and_discarded`, since
refuted material does not live in one block and those blocks disagree about
field names. Keyword extraction is deliberately crude: a match is a prompt to
check relatedness, never an automatic rejection. A false positive costs one
glance; a missed refuted relative costs a repeated experiment.

## `mizan_export_refuted.py` — Kıyas geri-besleme döngüsü

Üretici↔denetçi döngüsünün Mizan yarısı. Bir registry'yi okur ve
`refuted-patterns.yaml` üretir: R veya Y katmanındaki her girdi, artı kalıcı
KKE'ler, bir üreticinin çürütülmüş bir şeyin akrabasını önermeden önce
bakabileceği negatif-kısıtlara çevrilir.

`hypotheses`, `bugs`, `features` ve `refuted_and_discarded` bloklarını gezer;
çünkü çürütülmüş malzeme tek blokta yaşamaz ve bu bloklar alan isimlerinde
anlaşamaz. Anahtar-kelime çıkarımı bilerek kabadır: eşleşme, bakmak için bir
uyarıdır, otomatik ret değil. Yanlış pozitifin bedeli bir bakış; kaçırılmış
çürütülmüş akrabanın bedeli tekrarlanmış bir deney.
