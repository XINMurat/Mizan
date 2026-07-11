# Mizan Quickstart / Hızlı Başlangıç

Concrete "say this → get this" examples. / Somut "şunu de → şunu al" örnekleri.
*(English first, Türkçe aşağıda.)*

---

## English

### 0. Install (30 seconds)
Upload [`mizan.skill`](../mizan.skill) in Claude.ai (Settings → Skills), **or**
copy `skill/mizan/` into `~/.claude/skills/` for Claude Code. Full install
options: [usage-guide.md](en/usage-guide.md).

### 1. Audit a claim set (Mode 1)
You paste an AI-written summary / a self-review / a report and say:

> **"Audit this with Mizan."**

You get back: a coverage line (N claims, M checkable), a tiered claim table
(`[K]/[H]/[S]/[R]/[KKE]/[Y]`), a counter-example sweep, a hit rate where
judgment is praised, the "missing card", and next steps. Nothing lands in
`[K]` without a checked source.

### 2. Preregister a hypothesis (Mode 2)
A testable idea comes up. You say:

> **"Preregister this hypothesis."**

Mizan writes a registry entry **before** the test — with a numeric threshold
(`support`/`refute`) and a refutation condition **locked now**. Copy the
[registry template](../templates/mizan-registry.yaml) into your repo first;
the entry appends to it. A worked, rule-passing registry is in
[`examples/`](../examples/mizan-registry.example.yaml).

### 3. Audit a repo (Mode 3)
> **"Audit this repo with Mizan."**

Every function name, comment, docstring, and test is treated as a claim;
each hop (comment → behavior, test-name → test-content) is verified
separately. Output: an evidence-tiered behavior report + a Gap Map (broken
promises `[R]`, untested surfaces `[KKE]`, promise-gaps `[Y]`).

### 4. Gate a feature/PRD (Mode 5)
> **"Gate this PRD."**

The PRD is atomized and tiered; the success metric AND the kill condition
are preregistered; you are forced to name ≥1 cheaper alternative + the null
alternative before committing.

### 5. Enforce the rules locally (this repo's tooling)
```bash
pip install -r tools/requirements.txt
python tools/mizan_validate.py examples/mizan-registry.example.yaml   # -> OK
git config core.hooksPath tools/hooks                                 # block bad commits
```
The validator checks R1–R7 mechanically (no LLM). See
[`tools/README.md`](../tools/README.md).

---

## Türkçe

### 0. Kurulum (30 saniye)
Claude.ai'de [`mizan.skill`](../mizan.skill) yükleyin (Ayarlar → Skills),
**veya** Claude Code için `skill/mizan/`'ı `~/.claude/skills/` altına
kopyalayın. Tüm seçenekler: [kullanim-kilavuzu.md](tr/kullanim-kilavuzu.md).

### 1. Bir iddia setini denetle (Mod 1)
AI-üretimi bir özet / öz-değerlendirme / rapor yapıştırıp dersiniz ki:

> **"Bunu Mizan'la denetle."**

Şunu alırsınız: kapsam satırı (N iddia, M'i kontrol edilebilir), katmanlı
iddia tablosu (`[K]/[H]/[S]/[R]/[KKE]/[Y]`), karşı-örnek taraması, yargının
övüldüğü yerde isabet oranı, "eksik kart" ve sonraki adımlar. Kaynağı
kontrol edilmeden hiçbir iddia `[K]`'ya düşmez.

### 2. Bir hipotezi önkaydet (Mod 2)
Test edilebilir bir fikir doğar. Dersiniz ki:

> **"Bu hipotezi önkaydet."**

Mizan, testten **önce** bir registry girdisi yazar — sayısal eşik
(`support`/`refute`) ve çürütme koşulu **şimdi kilitlenir**. Önce
[registry şablonunu](../templates/mizan-registry.yaml) repo'nuza kopyalayın;
girdi ona eklenir. Kuralları geçen çalışan örnek:
[`examples/`](../examples/mizan-registry.example.yaml).

### 3. Bir repoyu denetle (Mod 3)
> **"Bu repoyu Mizan'la denetle."**

Her fonksiyon adı, yorum, docstring ve test bir iddia sayılır; her sıçrama
(yorum → davranış, test-adı → test-içeriği) ayrı doğrulanır. Çıktı:
kanıt-katmanlı davranış raporu + Boşluk Haritası (kırık sözler `[R]`,
test edilmemiş yüzeyler `[KKE]`, söz-boşlukları `[Y]`).

### 4. Bir özellik/PRD'yi kapıdan geçir (Mod 5)
> **"Bu PRD'yi kapıdan geçir."**

PRD atomize edilip katmanlanır; başarı metriği VE kaldırma koşulu
önkaydedilir; taahhütten önce ≥1 ucuz alternatif + null alternatifi
adlandırmaya zorlanırsınız.

### 5. Kuralları yerelde uygula (bu reponun araçları)
```bash
pip install -r tools/requirements.txt
python tools/mizan_validate.py --lang tr examples/mizan-registry.example.yaml
git config core.hooksPath tools/hooks
export MIZAN_LANG=tr
```
Doğrulayıcı R1–R7'yi mekanik kontrol eder (LLM yok). Bkz.
[`tools/README.md`](../tools/README.md).
