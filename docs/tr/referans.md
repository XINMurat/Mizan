# Mizan — Türkçe Referans Dizini

Metodolojinin **kanonik metni İngilizcedir** ve taşınabilir skill paketinin
içinde yaşar: Claude'un gerçekten yüklediği dosya odur. Bu sayfa bir haritadır
— hangi konunun kanonik karşılığı nerede, ve Türkçe aynası hangisi.

Kanonik İngilizce metinler artık bu sitede de yayımlanıyor; aşağıdaki
bağlantılar GitHub'a değil, sayfalara gidiyor. Başlıktaki **EN** düğmesi de
aynı yere götürür.

| Konu | İngilizce (kanonik) | Türkçe ayna |
|---|---|---|
| Metodoloji / çekirdek skill (Mod 1–2) | [Methodology](../en/methodology.md) | [Metodoloji](metodoloji.md) |
| Şablonlar (registry girdisi, sonuç bloğu, denetim raporu) | [Methodology](../en/methodology.md) içinde | [Metodoloji §2](metodoloji.md) |
| Hata-modu kontrol listesi (HARKing, katman kayması, …) | [`skill/mizan/references/checklist.md`](../../skill/mizan/references/checklist.md) | [Metodoloji §3](metodoloji.md) |
| Kurtarma rampaları (RR-00…RR-13), model hata sınıfları, kapanış skorkartı | [`skill/mizan/references/recovery.md`](../../skill/mizan/references/recovery.md) | [Metodoloji §4](metodoloji.md) — rampa tablosu ve hata sınıfları; rampa başına uzun form yalnızca İngilizce |
| Yazılım modları 3–5 (kod denetimi, bug registry, özellik kapısı) | [Software modes](../en/software-modes.md) | [Yazılım modları](yazilim-modlari.md) |
| Alan uyarlama (yazılım dışı 14 alan) | [Domain adaptation](../en/domain-adaptation.md) | [Alan uyarlama](alan-uyarlama.md) |
| Makine-okunur registry şeması (R1–R22) | [`skill/mizan/schemas/mizan-registry.yaml`](../../skill/mizan/schemas/mizan-registry.yaml) | aynı dosya (yorumlar İngilizce) |

## Yalnızca İngilizce uzun-form belgeler

- [Usage guide](../en/usage-guide.md) — kurulum, akışlar, sert kurallar.
- [Project instructions](../en/project-instructions.md) — bir Claude Projesine
  yapıştırılacak blok.

> **Bakım notu:** yukarıdaki kanonik metinler tek doğruluk kaynağıdır.
> `docs/tr/` altındaki Türkçe dosyalar **elle yazılmış aynalardır** — bir
> referans değiştiğinde eşleşen Türkçe dosya güncellenir ve değişiklik
> kaydedilir (yalnızca-eklenir, R4). `docs/en/` altındaki İngilizce sayfalar
> ise elle değil, `tools/sync_en_docs.py` ile üretilir; CI, kaynağından
> sapan bir sayfayı fark eder.
