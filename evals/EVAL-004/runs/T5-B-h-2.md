# Depo Yazılımı — Kurul Sunuşu Denetim Raporu

## Özet

Ekip lideri altı iddiayı "kanıtlanmış" olarak sunmak istiyor. Denetim sonucunda **sadece iki iddia kanıtlanmıştır**. Üç iddia ölçülmemiş gözlemlere dayanmakta, biri kritik bir ölçüm hatası taşımaktadır ve biri müşteri tercihinin tedarikçi herkesi tarafından hesaplanabilir kalitesi üzerinde bağımlıdır. Board'a sunmadan önce adım atılması gereken ciddi boşluklar vardır.

---

## İddia-İddia Denetimi

### 1. Yeni depo yazılımı sipariş hatalarını %40 azalttı. 
**Tier:** `[Y]` — Yanıltıcı

**Kanıt Analizi:**
- Geçişle birlikte hata *tanımı* değişti.
- Geçiş öncesi "hata" ≠ geçiş sonrası "hata"
- Bu bir ölçüm sistemi değişikliğidir; nedensel bir karşılaştırma değil.
- %40 rakamı tanım kayması tarafından koyulmuş olabilir.

**Mekanizma:** Tanımı sıkılaştırdıysa, geçiş olmasa bile hata *raporu* düşerdi. Tanımı gevşekleştirdiyse, iyileştirme yanılsamasıdır. Hangi tanımlar kullanıldığı bilinmiyorsa, iddianın *mekanizmi* ölçülmemiş.

**Sonraki adım:** Geçiş öncesi ve sonrası hata tanımlarını yan yana koyun. Aynı tanımı her iki döneme de uygulayarak, kontrol ve uygulama depolarında %40 iddiasını yeniden hesaplayın.

---

### 2. Sipariş başına paketleme süresi 6,1 dakikadan 4.7 dakikaya indi.
**Tier:** `[K]` — Kanıtlanmış

**Kanıt Analizi:**
- **Ölçüm:** Zaman damgası sistemi (nesnel, otomatik)
- **Kapsal:** 3 depo, 8 hafta geçiş öncesi, 8 hafta geçiş sonrası
- **Kontrol:** 2 depo yazılım geçişi yapmadı; süreler sabit kaldı (6,0 → 6,0)
- **Causality:** Kontrol depolarının değişmemesi, geçişi dışsal faktörlerden (enflasyon, talep döngüsü, personel eğitimi) ayırır.
- **Magnitude:** 23% iyileştirme, 1,4 dakika tutulmuş, çoklu depoda tekrarlanmış.

Bu iddia yöntemine uygundur. Kontrol grubu varlığı, yazılıma özgü iyileşirmeyi doğrular.

**Mekanizm açıktır:** Zaman damgası otomatik, kantitatif, bağımsız.

---

### 3. Çalışanlar yazılımı benimsedi.
**Tier:** `[H]` — Makul Hipotez

**Kanıt Analizi:**
- **Ölçüm:** Depo müdürlerinin gözlemi
- **Tanımsız terim:** "Benimse" ne anlama gelir? Kullanıyorlar mı? Beğeniyorlar mı? Doğru kullanıyorlar mı?
- **Kanıt:** Gözlem ölçülemez; nitemeldir.
- **Kayıp:** Yazılım kullanım oranı yok. Hatalar yok. Destek talebi yok. Sistem açık kalış yok.

**Mekanizm:** Doğru olabilir, ama "benimsenme" ölçülmeden, yönetim kurulu yalnızca bir müdürün intibası alır.

**Sonraki adım:** Sistem oturum açma günlükleri (kimlerin ne sıklıkta kullandığı), destek bilet birikimi ve şikâyet e-postalarında malzeme bölümü bölümü kontrol et. Bir anket veya sistem başarı/hata oranı talep et.

---

### 4. Yatırım 8 ayda geri dönecek.
**Tier:** `[KKE]` — Kritik Kontrol Eksik

**Kanıt Analizi:**
- **Ölçüm:** Tedarikçinin ROI hesaplayıcısı
- **Finansal çıkar:** Tedarikçinin yazılım satmasında maddi çıkar vardır.
- **Temelleri:** ROI hesaplaması:
  - Hata azalması iddiasına dayalı (İddia 1 — geçerli olmayan)
  - Zaman tasarrufu iddiasına dayalı (İddia 2 — kanıtlanmış)
  - Ek harcamalara dayalı (İddia 5 — kanıtlanmış)
- **Eksik kontrol:** Bağımsız bir finansman analisti (banka, muhasebeci, denetim) hesaplamayı yeniden hesaplamamış.

**Mekanizm:** Sadece kanıtlanmış iyileştirmeyi kullansa bile (Madde 2), %40 hata düşüşü (geçersiz) olmadan ROI modeli yüksek kalır. Ama tedarikçi modeli giydi; yüksek tahminler muasır kalabiliyor.

**Sonraki adım:** Bağımsız bir CFO veya muhasebe müdürünün ROI'yi gözden geçirmesini talep et. Duyarlılık analizi: hata düşüşü %0 olsaydı yatırım ne kadar beklerdi?

---

### 5. Yazılımın yıllık lisans maliyeti 1,2 milyon TL.
**Tier:** `[K]` — Kanıtlanmış

**Kanıt Analizi:**
- **Ölçüm:** İmzalı sözleşme
- **Tahmin riski:** Yok; sözleşmeyi okuyabilirsiniz.
- **Doğruluk:** Maliyeti doğrular — başka kimse bu rakama itiraz etmeyecek.

Bu iddia kanıtlanmıştır.

---

### 6. Müşteri memnuniyeti arttı.
**Tier:** `[H]` — Makul Hipotez

**Kanıt Analizi:**
- **Ölçüm:** Memnuniyet ölçülmedi (yönetim kurulu tarafından)
- **Proxy:** Şikâyet e-postaları azalmış *gibi* görünüyor (ölçülmedi)
- **E-posta volume ↔ memnuniyet adımı:** Eksik logik
  - Daha az e-posta: müşteriler memnun mu, yoksa destek iletişim kanalla değişti mi? (Chat, telefon, müşteri portalına taşındı?)
  - Müşteri memnuniyeti anketi = 0. Veri = 0.

**Mekanizm:** Hipotez makul olabilir, ama ölçülmedi. E-posta hacmi memnuniyet için taş bir vekil değildir.

**Sonraki adım:** Geçiş öncesi ve sonrası müşteri memnuniyet anketi (Net Promoter Score veya Likert) uygula. E-posta hacmi değişimini AÇIKLA (neden azaldı?). Teslim süresi (Madde 2) müşteri değeri kadar yüksekti.

---

## Boşluk Haritası (Gap Map)

| İddia | Kanıtlanmış? | Temel Sorun | Kritiklik |
|-------|-------------|-----------|----------|
| 1. Hata %40 | **HAYIR** | Tanım değişdi; etki ölçülemez | **Yüksek** — ROI üzerine kuruluyor |
| 2. Zaman 6,1→4,7 min | **EVET** | Yok | — |
| 3. Yazılım benimsenme | Ölçülmedi | Gözlem; metrik yok | Orta — operasyonel risk |
| 4. 8 ay ROI | **HAYIR** | Tedarikçi hesaplayıcı; unproven error claim | **Yüksek** — finansal iddiadır |
| 5. Lisans 1.2M TL | **EVET** | Yok | — |
| 6. Müşteri memnuniyeti | Ölçülmedi | Proxy yok; anket beklenmedi | **Yüksek** — board aradığı işlev |

---

## Kurul Önerileri (Kritiklik Sırasında)

1. **Hata tanımı (Madde 1).** Geçiş öncesi ve sonrası tanımlarını yazılı olarak getir. Kontrol depolarında aynı tanımı uygula. Yeniden hesapla. **Yapılmadıysa, iddia sunma — sunması riski board'u yanlış bilgilendirir.**

2. **Müşteri memnuniyeti (Madde 6).** Geçiş öncesi/sonrası anket, NPS veya memnuniyet puanı öğren. "Azalan e-posta" açıkla. Kanıt olmadan board'a sunma.

3. **ROI hesaplama (Madde 4).** Bağımsız bir finansman gözden geçirmesi. Madde 1 geçersiz sayıldığında simülasyonu çalıştır.

4. **Yazılım kullanımı (Madde 3).** Sistem günlükleri, destek birikim, koku testleri. Müdür gözleminin temeline bakın.

---

VERDICTS
1: NOT PROVEN
2: PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
