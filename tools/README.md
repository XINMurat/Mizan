# Mizan Tooling — R1–R7 Validator

*(Türkçe aşağıda / Turkish below)*

## English

`mizan_validate.py` is a **judgment-free, LLM-free** static validator for
`mizan-registry.yaml` files. It enforces only the mechanical hard rules
R1–R7 from the schema — it does **not** evaluate whether a hypothesis is
good, only whether the registry is structurally honest.

> This is the cheapest, gate-approved slice of feature **FEAT-M001** in the
> project's private roadmap registry: "a simple pre-commit hook + schema
> validator (LLM-free, R1–R7 static checks only)".
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
kuralları (R1–R7) uygular — bir hipotezin *iyi* olup olmadığını değil,
registry'nin yapısal olarak dürüst olup olmadığını denetler.

> Bu, projenin özel yol haritası registry'sindeki **FEAT-M001**
> özelliğinin kapıdan onaylı en ucuz dilimidir:
> "basit pre-commit hook + şema doğrulayıcı (LLM'siz, yalnız R1–R7 statik
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
