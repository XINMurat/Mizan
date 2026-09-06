# Mizan Documentation / Dokümantasyon

**⚡ New here? / Yeni misiniz?** → [QUICKSTART.md](QUICKSTART.md) — concrete
"say this → get this" examples in both languages / iki dilde somut örnekler.

Choose a language / Bir dil seçin:

## 🇬🇧 English

| Doc | What it covers |
|---|---|
| [usage-guide.md](en/usage-guide.md) | Install, daily workflows, hard rules |
| [project-instructions.md](en/project-instructions.md) | Block to paste into a Claude Project |
| [methodology.md](en/methodology.md) | Modes 1–2, the core skill in full |
| [software-modes.md](en/software-modes.md) | Modes 3–5: code audit, bug registry, feature gate |
| [domain-adaptation.md](en/domain-adaptation.md) | Modes 3/4/5 across 14 domains beyond software |
| [reference.md](en/reference.md) | Index → methodology, templates, checklist, software modes, domain adaptation |

The English methodology reference is the skill itself
([`../skill/mizan/`](../skill/mizan/)), so it never drifts from what Claude
loads. The three pages above are **generated** from those files by
`tools/sync_en_docs.py` and checked in CI — read them here, edit them there.

## 🇹🇷 Türkçe

| Belge | İçerik |
|---|---|
| [kullanim-kilavuzu.md](tr/kullanim-kilavuzu.md) | Kurulum, günlük akışlar, sert kurallar |
| [metodoloji.md](tr/metodoloji.md) | Mod 1–2 tam referans (SKILL + şablonlar + kontrol listesi) |
| [yazilim-modlari.md](tr/yazilim-modlari.md) | Mod 3–5: kod denetimi, bug registry, özellik kapısı |
| [alan-uyarlama.md](tr/alan-uyarlama.md) | Mod 3/4/5'in yazılım ötesi 14 alana uyarlanması |
| [proje-talimati.md](tr/proje-talimati.md) | Claude Project'e yapıştırılacak talimat bloğu |
| [referans.md](tr/referans.md) | Dizin → metodoloji, şablonlar, kontrol listesi, yazılım modları, alan uyarlama |

---

**Parity note / Parite notu:** both sides now list the same documents. The
Turkish files are hand-written full-text mirrors — when a reference changes,
update the Turkish side and record it (append-only, R4). The English pages
under `en/` that mirror the skill are generated, not hand-written: run
`python tools/sync_en_docs.py`; CI fails if they drift. /
İki taraf artık aynı belgeleri listeliyor. Türkçe dosyalar elle yazılmış
tam-metin aynalardır — bir referans değişince Türkçe tarafı güncelleyin ve
kaydedin (append-only, R4). `en/` altındaki skill aynası sayfalar ise elle
değil `python tools/sync_en_docs.py` ile üretilir; saparlarsa CI patlar.
