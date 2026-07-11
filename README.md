# Mizan

**Evidence-tiered auditing & preregistration methodology, packaged as a Claude skill.**
**Kanıt-katmanlı denetim ve önkayıt metodolojisi — bir Claude skill'i olarak paketlenmiş.**

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
not the sole auditor who promotes it (R1–R7).

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

### Documentation

- **⚡ Quickstart:** [`docs/QUICKSTART.md`](docs/QUICKSTART.md) — concrete
  "say this → get this" examples (bilingual).
- **Start here:** [`docs/en/usage-guide.md`](docs/en/usage-guide.md) —
  install, workflows, hard rules.
- **Reference index:** [`docs/en/reference.md`](docs/en/reference.md) —
  methodology, templates, checklist, software modes, domain adaptation.
- **Turkish docs:** [`docs/tr/`](docs/tr/).
- **Contributing:** [`CONTRIBUTING.md`](CONTRIBUTING.md) — the R1–R7
  discipline for PRs, bilingual-parity rule (bilingual).

### Tooling (`tools/`)

A **judgment-free, LLM-free** validator enforces the mechanical hard rules
R1–R7 on any `mizan-registry.yaml`:

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
examples/                       worked registry that passes R1–R7
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
denetçi olamaz (R1–R7).

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
- **Katkı:** [`CONTRIBUTING.md`](CONTRIBUTING.md) — PR'lar için R1–R7
  disiplini ve iki-dillilik kuralı (iki dilli).

### Araçlar (`tools/`)

**Yargısız, LLM'siz** bir doğrulayıcı, herhangi bir `mizan-registry.yaml`
üzerinde mekanik sert kuralları (R1–R7) uygular:

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

**v2.2** — 5 modes + domain-adaptation module (14 domains) + R1–R7 registry
schema + bilingual docs (TR/EN) + R1–R7 validator & pre-commit hook.
