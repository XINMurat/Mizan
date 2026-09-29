# Mizan Tooling — R1–R28 Validator

*(Türkçe aşağıda / Turkish below)*

## English

`mizan_validate.py` is a **judgment-free, LLM-free** static validator for
`mizan-registry.yaml` files. It enforces only the mechanical hard rules
R1–R28 from the schema — it does **not** evaluate whether a hypothesis is
good, only whether the registry is structurally honest.

> This is the cheapest, gate-approved slice of feature **FEAT-M001** in the
> project's private roadmap registry: "a simple pre-commit hook + schema
> validator (LLM-free, R1–R28 static checks only)".
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
python tools/mizan_validate.py --format github registry.yaml  # PR annotations (json also)
```

Exit codes: `0` clean · `1` violations · `2` usage/parse error. A file that
is not a registry — none of the known top-level sections, a section of the
wrong type, an entry that is not a mapping, a sibling family's file (ux-mizan
`flows`/`findings`, Kıyas `seeds`/`batch`) with none of Mizan's sections — is
a parse error (`2`), never a
clean `0 entries`: an empty verdict computed from missing input is not a pass.

`--format json` gives machine-readable output and `--format github` emits
workflow annotations that show on the PR diff; the exit code never depends on
the format.

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
kuralları (R1–R28) uygular — bir hipotezin *iyi* olup olmadığını değil,
registry'nin yapısal olarak dürüst olup olmadığını denetler.

> Bu, projenin özel yol haritası registry'sindeki **FEAT-M001**
> özelliğinin kapıdan onaylı en ucuz dilimidir:
> "basit pre-commit hook + şema doğrulayıcı (LLM'siz, yalnız R1–R28 statik
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
Registry olmayan bir dosya — bilinen üst düzey bölümlerin hiçbiri yok, bir
bölüm yanlış tipte, bir girdi mapping değil, Mizan bölümü olmayan bir kardeş
aile dosyası (ux-mizan `flows`/`findings`, Kıyas `seeds`/`batch`) — ayrıştırma hatasıdır (`2`), asla
temiz bir `0 girdi` değil: eksik girdiden hesaplanan boş hüküm geçiş değildir.

`--format json` makinece okunur çıktı, `--format github` PR diff'inde görünen
annotation'lar üretir; çıkış kodu biçimden bağımsızdır.

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

## `mizan_export_results.py` — decided tiers for the Kıyas ledger

```bash
python tools/mizan_export_results.py registry.yaml -o mizan-results.yaml
# then, in the Kıyas repo:
python tools/kiyas_ledger.py --sync mizan-results.yaml ledger/kiyas-ledger.yaml
```

The ledger counts K and H as survival, and every hypothesis starts at H. So a
tier is exported only for an entry with a result whose `decision_confirmed_by`
is filled (R7); everything else is listed as `pending` with its reason and no
tier. `--sync` fills only EMPTY ledger tiers and reports any disagreement
instead of overwriting.

Kıyas sağ-kalım defteri için karara bağlanmış tier'lar. Defter K ve H'yi
sağ-kalım sayar ve her hipotez H'de başlar; bu yüzden tier yalnız
`decision_confirmed_by` dolu bir sonucu olan girdi için çıkar, gerisi
gerekçesiyle `pending` listelenir. `--sync` yalnız BOŞ tier'ları doldurur,
çelişkiyi üzerine yazmaz, raporlar.

## `--profile lite`, `mizan_calibration.py`, `mizan_sample.py`

```bash
python tools/mizan_validate.py --profile lite registry.yaml   # R1-R8 block; R9+ shown as warnings
python tools/mizan_calibration.py evals/*/*.mizan-registry.yaml
python tools/mizan_sample.py draw registry.yaml -n 3 -o review-sample.yaml
python tools/mizan_sample.py check registry.yaml review-sample.yaml
```

- **lite** is a first-week profile: R1–R8 block, everything above is still
  printed as `(lite: deferred)`. It demotes, never hides. CI runs full.
- **calibration** reports first how many results returned a verdict at all,
  then a hit rate only when at least 5 did. On this repository's four evals it
  reads 0/4 decisive — the finding is the design, not the skill.
- **sample** draws entries for a non-author to read, seeded by the registry's
  own sha256 so the draw cannot be chosen; `check` refuses a stale, reordered
  or owner-reviewed sample. The validator checks that a refutation exists;
  this records that someone checked it could refute.

/ **lite** ilk hafta profilidir: R1–R8 engeller, üstü `(lite: deferred)` olarak
görünür kalır; gizlemez, düşürür. **calibration** önce kaç sonucun hüküm
döndürdüğünü, ancak en az 5 hüküm varsa isabet oranını basar. **sample**,
registry'nin kendi sha256'sıyla tohumlanmış, seçilemez bir örneklemi yazar
olmayan birine okutur ve bunu kayda geçirir.

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

---

## `build_skill.py` — the package, byte for byte

```bash
python tools/build_skill.py           # writes mizan.skill from skill/mizan/
python tools/build_skill.py --check   # CI: fails on any byte difference
```

Same file in all four repositories; it packages the one directory under
`skill/`. LF line endings, a fixed timestamp and a sorted file list, so the
same source always gives the same archive. `--check` compares the package as
packaged: the check it replaced normalised CRLF on both sides, and a package
zipped on Windows passed as in sync with `#!/usr/bin/env python3\r` inside.

## `build_skill.py` — paket, bayt bayt

`python tools/build_skill.py` paketi üretir, `--check` (CI) her bayt farkında
düşer. Dört repoda aynı dosyadır ve `skill/` altındaki tek dizini paketler. LF,
sabit zaman damgası, sıralı dosya listesi: aynı kaynak her zaman aynı arşivi
verir. Yerine geçtiği kontrol CRLF'yi iki tarafta da normalleştiriyordu; içinde
`#!/usr/bin/env python3\r` olan, Windows'ta sıkıştırılmış bir paket senkron
göründü.
