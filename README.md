# Mizan

**Evidence-tiered auditing & preregistration methodology, packaged as a Claude skill.**
**Kanıt-katmanlı denetim ve önkayıt metodolojisi — bir Claude skill'i olarak paketlenmiş.**

[![CI](https://github.com/XINMurat/Mizan/actions/workflows/mizan.yml/badge.svg)](https://github.com/XINMurat/Mizan/actions/workflows/mizan.yml)

🌐 **Languages / Diller:** [English](#english) · [Türkçe](#türkçe)

Tiers / Katmanlar: **[K]** proven/kanıtlanmış · **[H]** plausible hypothesis/makul hipotez ·
**[S]** speculative/spekülatif · **[R]** refuted/reddedildi (never deleted / silinmez) ·
**[KKE]** critical control missing/kritik kontrol eksik · **[Y]** misleading/yanıltıcı.

---

## English

Mizan (Turkish/Arabic: *"the scale"*) turns a rigorous experimental-science
discipline into a portable tool for evaluating **any** claim set and for
maintaining living hypothesis registries.

**Hard rules:** thresholds are locked *before* results (no HARKing); every
hypothesis carries a refutation condition; surprising positives require a
symmetric confound control before promotion; history is append-only;
refuted entries are kept `[R]`, never deleted; the producer of a result is
not the sole auditor who promotes it (R1–R18).

### Install

- **Claude.ai / desktop / mobile:** upload [`mizan.skill`](mizan.skill)
  (Settings → Capabilities → Skills). Re-upload to update.
- **Claude Code / Desktop (raw skill):** copy `skill/mizan/` into
  `~/.claude/skills/` (personal) or `.claude/skills/` inside a repo
  (project-scoped). Verify with `/skills`. Common mistake: a doubly-nested
  folder — the path must be `~/.claude/skills/mizan/SKILL.md`.
- **Claude Project (full methodology):** paste
  [`docs/en/project-instructions.md`](docs/en/project-instructions.md) into
  the Project instructions field, and add a filled
  [`templates/mizan-registry.yaml`](templates/mizan-registry.yaml) to
  project knowledge or your repo.
- **Other AIs (ChatGPT, Gemini, local):** the format is model-independent —
  give them the schema + docs; discipline transfers, auto-triggering is
  weaker.

Then ask Claude to *"audit these claims with Mizan"*, *"preregister this
hypothesis"*, *"audit this repo"*, or *"gate this PRD"*.

**You do not need to configure your assistant for this to work.** No custom
instructions, no system prompt, no house style. If the skill only behaves
when your `CLAUDE.md` is set up a particular way, that is a **defect in the
skill**, not a missing step in your setup — please open an issue. This is a
tested claim, not a courtesy: `[K]` for the harnesses in
[`examples/portability-across-hosts.md`](examples/portability-across-hosts.md),
where the skill was run under a `CLAUDE.md` written to fight it and again
under none at all. That file also discloses why the author's own setup makes
their experience unrepresentative.

A second worked example covers the case the procedure quietly assumes away —
**a document whose source the auditor cannot reach** (published after a
knowledge cutoff, paywalled, internal to someone else). The failure mode there
is not refusal but **tier laundering**: inheriting a well-made document's own
tags and presenting them as a verdict. See
[`examples/unverifiable-source-audit.md`](examples/unverifiable-source-audit.md),
which also proposes — as a proposal, not a silent patch — a reachability cap on
tiers, with its illet and its breaking point.

### Companion skill — Kıyas

Mizan weighs and refutes; it does not generate what gets weighed. That is the
job of its upstream partner **[Kıyas](https://github.com/XINMurat/Kiyas)** —
disciplined ideation and analogical inference. Kıyas produces candidates
already shaped for a Mizan registry (illet, breaking point, cheapest
refutation, named prior art, and an **arbiter** block that mirrors Mizan's
R8), and the loop closes both ways: `tools/mizan_export_refuted.py` turns this
registry's `[R]`/`[Y]` entries into negative constraints Kıyas consults before
proposing a relative of something already killed.

```bash
python tools/mizan_export_refuted.py registry.yaml -o refuted-patterns.yaml
# then, in the Kıyas repo:
python tools/kiyas_validate.py --refuted refuted-patterns.yaml seeds.yaml
```

### Companion skill — İskele

Kıyas supplies what Mizan weighs; **[İskele](https://github.com/XINMurat/Iskele)**
supplies the structure both of them operate on — a domain model, a phased
roadmap with go/no-go gates, an atomic backlog with executable acceptance
criteria, and a progress report computed from a tracker rather than estimated
by hand. The three verbs are deliberately kept in three tools:

> **İskele builds · Mizan weighs · Kıyas generates**

The handoff runs in both directions: when İskele finishes a kit, Mizan audits
the kit's own claims — every "verified" sentence goes through a counter-example
sweep, and every estimate carries a tier instead of the false precision a
spreadsheet invites. What the audit turns up re-enters the kit as backlog tasks.

### Companion skill — ux-mizan

**[ux-mizan](https://github.com/XINMurat/ux-mizan)** carries this
methodology into a domain where the evidence is behavioural rather than
documentary — "users get lost", "this screen is confusing". Its own
restatement of R7: **if the referee writes it, there is no `[K]`.**

What concerns *this* repo: its design hypotheses live in a **Mizan**
registry, validated by this repo's validator in its own CI — including one
that is already `[R]`. The tools audit each other rather than only
describing each other.

The four verbs and how they hand off: **[the family page](https://xinmurat.github.io/)**.

### Case study — the skills used on a real problem

[**sieve-to-spectrum**](https://github.com/XINMurat/sieve-to-spectrum) is a
number-theory project that ran on Mizan: a multiplication table re-derives
three centuries of results, and along the way 14 claims are audited with
evidence tiers, with four self-corrections appended.

It is worth reading because it is not a demonstration. The hypotheses were
preregistered before they were run, **three of the four came back negative**,
and the negatives are still in the repository — which is the outcome this
methodology is built to survive and the one a self-made example never
produces.

### Documentation

- **⚡ Quickstart:** [`docs/QUICKSTART.md`](docs/QUICKSTART.md) — concrete
  "say this → get this" examples (bilingual).
- **Start here:** [`docs/en/usage-guide.md`](docs/en/usage-guide.md) —
  install, workflows, hard rules.
- **Reference index:** [`docs/en/reference.md`](docs/en/reference.md) —
  methodology, templates, checklist, software modes, domain adaptation.
- **Turkish docs:** [`docs/tr/`](docs/tr/).
- **Contributing:** [`CONTRIBUTING.md`](CONTRIBUTING.md) — the R1–R18
  discipline for PRs, bilingual-parity rule (bilingual).

### Tooling (`tools/`)

A **judgment-free, LLM-free** validator enforces the mechanical hard rules
R1–R18 on any `mizan-registry.yaml`:

```bash
pip install -r tools/requirements.txt
python tools/mizan_validate.py examples/mizan-registry.example.yaml
git config core.hooksPath tools/hooks    # enable the pre-commit gate
```

See [`tools/README.md`](tools/README.md). This is the gate-approved slice
of **FEAT-M001**; the agentic/CI parts stay preregistered-but-gated in the
project's private roadmap registry.

### Repository layout

```
mizan.skill                     one-file skill package (Claude.ai)
skill/mizan/                    raw skill: SKILL.md, references/, schemas/  (EN canonical)
docs/en/                        English long-form docs
docs/tr/                        Türkçe uzun-metin dokümanlar
templates/                      copy-and-fill templates (registry schema)
examples/                       worked registry that passes R1–R18;
                                portability tests across hostile + neutral hosts;
                                auditing a document whose source you cannot reach
tools/                          mizan_validate.py + pre-commit hook
```

### License

Suggested split (see [`LICENSE`](LICENSE) and
[`LICENSE-docs.md`](LICENSE-docs.md)): **code & schema → MIT**,
**text & methodology (docs, skill prose) → CC-BY-4.0**. Adjust to taste.

---

## Türkçe

Mizan (terazi/ölçü), titiz bir deneysel-bilim disiplinini **herhangi bir**
iddia setini değerlendirmek ve canlı hipotez registry'leri sürdürmek için
taşınabilir bir araca dönüştürür.

**Sert kurallar:** eşikler sonuç görülmeden *önce* kilitlenir (HARKing yok);
her hipotez bir çürütme koşulu taşır; sürpriz pozitifler terfiden önce
simetrik confound kontrolü ister; geçmiş append-only'dir; çürüyen girdiler
`[R]` olarak tutulur, silinmez; bir sonucun üreticisi onu terfi ettiren tek
denetçi olamaz (R1–R18).

### Kurulum

- **Claude.ai / masaüstü / mobil:** [`mizan.skill`](mizan.skill) dosyasını
  yükleyin (Ayarlar → Capabilities → Skills). Güncellemede üzerine yükleyin.
- **Claude Code / Desktop (ham skill):** `skill/mizan/` klasörünü
  `~/.claude/skills/` (kişisel) veya repo içi `.claude/skills/`
  (proje-kapsamlı) altına kopyalayın. `/skills` ile doğrulayın. Sık hata:
  çift iç-içe klasör — doğru yol `~/.claude/skills/mizan/SKILL.md`.
- **Claude Project (tam metodoloji):**
  [`docs/tr/proje-talimati.md`](docs/tr/proje-talimati.md) bloğunu Project
  instructions alanına yapıştırın; doldurulmuş
  [`templates/mizan-registry.yaml`](templates/mizan-registry.yaml)'ı proje
  bilgisine veya repo'nuza ekleyin.
- **Diğer AI'lar (ChatGPT, Gemini, yerel):** format model-bağımsızdır —
  şema + dokümanları verin; disiplin taşınır, otomatik tetiklenme zayıftır.

Sonra Claude'a *"bu iddiaları Mizan'la denetle"*, *"bu hipotezi önkaydet"*,
*"bu repoyu denetle"* veya *"bu PRD'yi kapıdan geçir"* deyin.

### Kardeş skill — Kıyas

Mizan tartar ve çürütür; tartılacak olanı üretmez. O, üretici üst-kolu
**[Kıyas](https://github.com/XINMurat/Kiyas)**'ın işidir — ilkeli fikir
üretimi ve analojik çıkarım. Kıyas, adayları Mizan registry'sine hazır
biçimde üretir (illet, kırılma noktası, en ucuz çürütme, isimli prior-art ve
Mizan'ın R8'ini aynalayan bir **hakem** bloğu); döngü iki yönde de kapanır:
`tools/mizan_export_refuted.py`, bu registry'nin `[R]`/`[Y]` girdilerini,
Kıyas'ın çürütülmüş bir şeyin akrabasını önermeden önce baktığı
negatif-kısıtlara çevirir.

```bash
python tools/mizan_export_refuted.py registry.yaml -o refuted-patterns.yaml
# sonra Kıyas deposunda:
python tools/kiyas_validate.py --refuted refuted-patterns.yaml tohumlar.yaml
```

### Kardeş skill — İskele

Kıyas, Mizan'ın tartacağını üretir; **[İskele](https://github.com/XINMurat/Iskele)**
ise ikisinin üzerinde çalıştığı yapıyı kurar — alan modeli, go/no-go kapılı
fazlı yol haritası, çalıştırılabilir kabul kriterli atomik backlog ve el
yordamıyla tahmin edilmek yerine çizelgeden **hesaplanan** ilerleme raporu. Üç
fiil bilinçli olarak üç araçta tutulur:

> **İskele kurar · Mizan tartar · Kıyas üretir**

Devir iki yönlüdür: İskele bir kiti bitirdiğinde Mizan kitin kendi iddialarını
denetler — "doğrulandı" diyen her cümle karşı-örnek taramasına girer, her tahmin
çizelgenin davet ettiği sahte kesinlik yerine bir katman taşır. Denetimin
bulduğu şey kite backlog görevi olarak geri girer.

### Kardeş skill — ux-mizan

**[ux-mizan](https://github.com/XINMurat/ux-mizan)**, bu metodolojiyi
kanıtın belgesel değil **davranışsal** olduğu bir alana taşır —
"kullanıcılar kayboluyor", "bu ekran karışık". R7'yi kendi cümlesiyle
söyler: **hakem yazarsa `[K]` yoktur.**

*Bu* depoyu ilgilendiren kısım: ux-mizan'ın kendi tasarım hipotezleri bir
**Mizan** registry'sinde tutulur ve bu deponun doğrulayıcısıyla, kendi
CI'ında denetlenir — biri şimdiden `[R]`. Araçlar birbirini yalnızca
anlatmıyor, denetliyor.

Dört fiil ve aralarındaki devir: **[aile sayfası](https://xinmurat.github.io/)**.

### Vaka çalışması — skill'lerin gerçek bir problemde kullanımı

[**sieve-to-spectrum**](https://github.com/XINMurat/sieve-to-spectrum), Mizan
üzerinde koşan bir sayı-teorisi projesi: bir çarpım tablosundan üç yüzyıllık
sonuçlar yeniden türetiliyor ve yol boyunca 14 iddia kanıt katmanlarıyla
denetleniyor, dört öz-düzeltme append edilmiş.

Okumaya değer, çünkü bir gösteri değil. Hipotezler koşulmadan önce önkayıt
edildi, **dördün üçü negatif döndü**, ve negatifler hâlâ depoda duruyor — bu
metodolojinin ayakta kalmak için kurulduğu sonuç, ve kendi yaptığın bir
örneğin asla üretmediği sonuç.

### Dokümantasyon

- **⚡ Hızlı başlangıç:** [`docs/QUICKSTART.md`](docs/QUICKSTART.md) — somut
  "şunu de → şunu al" örnekleri (iki dilli).
- **Buradan başlayın:**
  [`docs/tr/kullanim-kilavuzu.md`](docs/tr/kullanim-kilavuzu.md) — kurulum,
  akışlar, sert kurallar.
- **Tam metodoloji:** [`docs/tr/metodoloji.md`](docs/tr/metodoloji.md)
  (Mod 1–2), [`docs/tr/yazilim-modlari.md`](docs/tr/yazilim-modlari.md)
  (Mod 3–5), [`docs/tr/alan-uyarlama.md`](docs/tr/alan-uyarlama.md)
  (14 alan).
- **İngilizce dokümanlar:** [`docs/en/`](docs/en/).
- **Katkı:** [`CONTRIBUTING.md`](CONTRIBUTING.md) — PR'lar için R1–R18
  disiplini ve iki-dillilik kuralı (iki dilli).

### Araçlar (`tools/`)

**Yargısız, LLM'siz** bir doğrulayıcı, herhangi bir `mizan-registry.yaml`
üzerinde mekanik sert kuralları (R1–R18) uygular:

```bash
pip install -r tools/requirements.txt
python tools/mizan_validate.py --lang tr examples/mizan-registry.example.yaml
git config core.hooksPath tools/hooks    # pre-commit kapısını aç
```

Ayrıntı: [`tools/README.md`](tools/README.md). Bu, **FEAT-M001**'in kapıdan
onaylı dilimidir; ajan/CI parçaları projenin özel yol haritası
registry'sinde önkayıtlı-ama-kapılı kalır.

### Lisans

Önerilen ayrım (bkz. [`LICENSE`](LICENSE) ve
[`LICENSE-docs.md`](LICENSE-docs.md)): **kod & şema → MIT**,
**metin & metodoloji (dokümanlar, skill metni) → CC-BY-4.0**. Kararı siz
verirsiniz.

---

### Version / Sürüm

**v2.4** — closes every finding of [`PROSE-SCHEMA-AUDIT.md`](PROSE-SCHEMA-AUDIT.md),
the systematic diff between what SKILL.md and `references/` require and what
the schema enforced. Adds R9–R12 (evidence behind `[K]`, numeric thresholds, a
tier on every entry, the mandatory entry fields), R13–R15 (features and bugs
stop being free-form and become hypotheses with kill conditions, alternatives
and rival mechanisms), R16 and the `coverage` block (the Coverage Ledger moves
into the registry, so R4 protects its rows), and a non-blocking warning channel
(W1–W4, `--strict` in CI). R4 (append-only) now actually runs in CI — it never
had a baseline to compare against before. Registry schema 1.5; files at 1.0–1.4
stay valid and unenforced.

**v2.3** — adds R8 (arbiter) and registry schema 1.2: every threshold names
the judge that returns its verdict, so a self-judged claim is capped at
`[KKE]` and an unjudged one stays `[S]`. Schema 1.0/1.1 registries remain
valid and unenforced; migrate by bumping `schema_version` to `"1.2"`. Also
adds `tools/mizan_export_refuted.py` and wires the loop to the companion
skill [Kıyas](https://github.com/XINMurat/Kiyas): refuted entries become
negative constraints the generator consults.

**v2.2** — 5 modes + domain-adaptation module (14 domains) + R1–R7 registry
schema + bilingual docs (TR/EN) + R1–R7 validator & pre-commit hook.
