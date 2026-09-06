# Mizan Tooling — R1–R21 Validator

*(Türkçe aşağıda / Turkish below)*

## English

`mizan_validate.py` is a **judgment-free, LLM-free** static validator for
`mizan-registry.yaml` files. It enforces only the mechanical hard rules
R1–R21 from the schema — it does **not** evaluate whether a hypothesis is
good, only whether the registry is structurally honest.

> This is the cheapest, gate-approved slice of feature **FEAT-M001** in the
> project's private roadmap registry: "a simple pre-commit hook + schema
> validator (LLM-free, R1–R21 static checks only)".
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
kuralları (R1–R21) uygular — bir hipotezin *iyi* olup olmadığını değil,
registry'nin yapısal olarak dürüst olup olmadığını denetler.

> Bu, projenin özel yol haritası registry'sindeki **FEAT-M001**
> özelliğinin kapıdan onaylı en ucuz dilimidir:
> "basit pre-commit hook + şema doğrulayıcı (LLM'siz, yalnız R1–R21 statik
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

## `token_budget.py` — the context budget, checked

A skill costs tokens the way a dependency costs bytes: to everyone who installs
it, on every cold start, forever. This one was designed to be cheap and that
intention lived only in prose — so between two releases the SKILL.md body grew
and the per-run load grew with it, and nothing failed, because **a budget nobody
checks is a preference**.

```bash
python tools/token_budget.py              # measure and compare to the ceilings
python tools/token_budget.py --json       # machine-readable
python tools/token_budget.py --update     # rewrite the ceilings AS THEY ARE NOW
```

Three tiers, because they are not paid at the same rate:

| tier | what it is | when it is paid |
|---|---|---|
| **T0** | the frontmatter `description` | every session where the skill is installed, used or not |
| **T1** | the SKILL.md body | whenever the skill triggers, and again on every cold start |
| **T2** | references and schemas | only when the procedure sends the model to that file |

Scripts and assets are not counted: they are executed or handed over as files,
not read into context. Counting tokens nobody pays is the fastest way to get a
budget ignored.

`runs` in `tools/token-budget.json` names what ONE mode actually loads —
SKILL.md plus whatever the procedure mandates — and gives that set its own
ceiling. That is the operational number; the tier totals are the structural one.

**The ceilings are preregistered.** Raising one is a deliberate commit with a
reason in the message, exactly as this skill demands of every other threshold.
`--update` exists for that commit and for no other purpose: running it to turn a
red build green, without reading the diff, is threshold shopping.

**The instrument, stated:** no tokenizer vocabulary is reachable offline, so
tokens are estimated from characters at the ratio in the config. The absolute
numbers are `[H]`; the drift the gate catches is `[K]`, because both sides are
measured with one instrument.

---

## `token_budget.py` — bağlam bütçesi, kontrol edilerek

Bir skill, bir bağımlılığın bayt harcadığı gibi token harcar: kuran herkese,
her soğuk başlangıçta, sürekli. Bu skill ucuz olacak şekilde tasarlandı ve o
niyet yalnızca düzyazıda yaşadı — iki release arasında SKILL.md gövdesi büyüdü,
koşu başına yük onunla büyüdü ve hiçbir şey kırılmadı, çünkü **kimsenin kontrol
etmediği bütçe, bütçe değil tercihtir.**

```bash
python tools/token_budget.py              # ölç, tavanlarla karşılaştır
python tools/token_budget.py --json       # makine okunur
python tools/token_budget.py --update     # tavanları ŞU ANKİ hâliyle yaz
```

Üç katman, çünkü aynı fiyattan ödenmiyorlar:

| katman | nedir | ne zaman ödenir |
|---|---|---|
| **T0** | frontmatter'daki `description` | skill kurulu olan her oturumda, kullanılsa da kullanılmasa da |
| **T1** | SKILL.md gövdesi | skill tetiklendiğinde ve her soğuk başlangıçta yeniden |
| **T2** | referanslar ve şemalar | yalnız prosedür modeli o dosyaya gönderdiğinde |

Script'ler ve varlıklar sayılmaz: onlar çalıştırılır ya da dosya olarak
devredilir, bağlama okunmaz. Kimsenin ödemediği token'ı saymak, bir bütçeyi
görmezden getirtmenin en hızlı yoludur.

`tools/token-budget.json` içindeki `runs`, TEK bir modun fiilen ne yüklediğini
adlandırır — SKILL.md artı prosedürün zorunlu kıldıkları — ve o kümeye kendi
tavanını verir. Operasyonel sayı budur; katman toplamları yapısal olandır.

**Tavanlar önkayıtlıdır.** Bir tavanı yükseltmek, mesajında gerekçesi olan
bilinçli bir commit'tir — bu skill'in diğer her eşikten istediğinin aynısı.
`--update` o commit için vardır, başka hiçbir şey için değil: kırmızı bir
build'i diff'i okumadan yeşile çevirmek için koşturmak, eşik alışverişidir.

**Alet, beyanıyla:** çevrimdışı erişilebilir bir tokenizer sözlüğü yok, bu yüzden
token sayısı config'teki orandan karakterle tahmin edilir. Mutlak sayılar `[H]`;
kapının yakaladığı kayma `[K]`, çünkü iki taraf da tek aletle ölçülür.
