# Yazılım Benimseme Kurulu Sunuşu — Kanıt Denetimi

**Denetçi:** Claude Haiku 4.5  
**Tarih:** 2026-09-29  
**Mod:** Denetim (retrospektif)  
**HARKing Riski:** Yüksek — örnekler seçilmiş sonuçları göstermektedir. Kontrol deposu verilerinin varlığı kısmi risk azaltır; ancak diğer iddiaların çoğu sonuç elde edildikten sonra sunulmuştur.

---

## Denetlenen İddiaların Atomizasyonu

1. Sipariş hataları yeni yazılım nedeniyle %40 azaldı.
2. Ambalajlama süresi ölçülebilir şekilde iyileşti (6,1 → 4,7 dakika) ve kontrol grubu bu iyileşmeyi göstermedi.
3. Depo müdürleri yazılımın benimsendiğini gözlemlediler.
4. Yatırım tedarikçinin hesaplamasına göre 8 ayda geri dönecektir.
5. Yazılım lisansı yıllık 1,2 milyon TL maliyetlidir.
6. Müşteri memnuniyeti arttı.

---

## Kanıt Denetimi ve Tierleme

### İddia 1: Sipariş Hatalarında %40 Azalma
**Alıntı:** "Yeni depo yazılımı sipariş hatalarını %40 azalttı. (Hata tanımı, yazılım geçişiyle birlikte değişti.)"

**Kanıt Durumu:** Hata tanımı değiştirilmiştir. Bu değişiklik, yazılımla eş zamanlı olduğundan, iyileştirme gerçek mi yoksa tanımlama kayması mı olduğunu belirlemek imkansız hale getirir. Kontrol deposu verisi yoktur. Tanımlama değişikliği, kanıt değerlendirmesini yapılamaz kılar.

**Tier:** `[KKE]` — Kritik Kontrol Eksik. Hata tanımının yazılım öncesi ve sonrasında aynı kalması gerekir; değilse, herhangi bir nicel iyileşme tanımlama artefaktı olabilir.

**Sonuç:** Onaylanamaz.

---

### İddia 2: Ambalajlama Süresi (6,1 → 4,7 dakika)
**Alıntı:** "Sipariş başına paketleme süresi 6,1 dakikadan 4,7 dakikaya indi: zaman damgası sistemi, 3 depo, geçişten önce ve sonra 8'er hafta; geçiş yapılmayan 2 kontrol deposunda süre değişmedi (6,0 → 6,0)."

**Kanıt Durumu:**
- Ölçüm yöntemi açıkça tanımlanmış (zaman damgası sistemi).
- Örneklem boyutu makul (3 depo × 8 hafta × 2 dönem).
- **Kontrol grubu mevcuttur:** 2 depo geçiş yapmadı ve değişim göstermedi (6,0 → 6,0).
- Kontrol grubunun değişmezliği, gözlemlenen iyileşmenin yazılımdan kaynaklandığını destekler (mevsimsel, operasyonel değişiklikler kontrolü).

**Tier:** `[K]` — Kanıtlanmış. Ölçülebilir, kontrol edilmiş veri, eşik karşılanmış. Bu iddianın tek zayıflığı süre sınırlanmasıdır (8 hafta) — uzun vadeli etkiyi göstermez; ancak kısa vadeli iyileşme için yeterlidir.

**Sonuç:** Onaylanır.

---

### İddia 3: Çalışan Benimsemesi
**Alıntı:** "Çalışanlar yazılımı benimsedi. (Depo müdürlerinin gözlemi.)"

**Kanıt Durumu:** Kanıt sadece üç depo müdürünün gözlem yorumudur. "Benimseme" nicel olarak tanımlanmamıştır. Ölçüm seçeneği:
- Kullanım istatistikleri (sistem logları)
- Eğitim tamamlama oranları
- İş arkadaşları anketleri (yapılmamış)

**Tier:** `[H]` — Makul Hipotez. Temel gözlem mevcuttur; kanıt ölçüm eşiğinin altında veya doğrudan olmayan kanıtlardır.

**Sonuç:** Onaylanamaz.

---

### İddia 4: 8 Aylık Yatırım Geri Dönüş Süresi
**Alıntı:** "Yatırım 8 ayda geri dönecek. (Tedarikçinin ROI hesaplayıcısı.)"

**Kanıt Durumu:** Hesaplama, tedarikçi tarafından yapılmıştır — tedarikçinin yazılımı satması konusunda mali çıkar vardır. Bağımsız doğrulama yoktur. Hesaplamaya giren varsayımlar (örneğin hata azalması elbette maliyete dönüşüyor mü?) açıklanmamıştır. Geriye dönük veri (8 haftalık sonuçlar) bütün yıl performans prometine uzatılmıştır.

**Tier:** `[H]` — Makul Hipotez. Tedarikçi girişimi; objektif araç ya da bağımsız gözlem değil. ROI'yi destekleyen ölçülebilir veri henüz yoktur.

**Sonuç:** Onaylanamaz.

---

### İddia 5: Yıllık Lisans Maliyeti 1,2 Milyon TL
**Alıntı:** "Yazılımın yıllık lisans maliyeti 1,2 milyon TL. (İmzalı sözleşme.)"

**Kanıt Durumu:** İmzalı sözleşme, kesin ve doğrulanabilir dokumenter kanıttır. Bu bilgi tartışmaya açık değildir.

**Tier:** `[K]` — Kanıtlanmış. Hukuki sözleşme, kaynak yapıyor.

**Sonuç:** Onaylanır.

---

### İddia 6: Müşteri Memnuniyeti Artışı
**Alıntı:** "Müşteri memnuniyeti arttı. (Memnuniyet ölçülmedi; şikâyet e-postaları azalmış gibi görünüyor.)"

**Kanıt Durumu:** Kendi başında söyledi: "Memnuniyet ölçülmedi." Şikâyet e-postalarında görülen azalma dolaylı göstergedir — başka nedenlerle azalabilir (örn., müşteri tabanı değişti, şikâyet kanalları değişti, çalışanlar şikâyetleri belki başka yönerge veya kanal altında alıyor). Ölçülenmiş memnuniyet verisinin eksikliği, bu iddiayı destekleyen kanıt yoktur demektir.

**Tier:** `[H]` — Makul Hipotez. Ancak tanımlayıcı ipucu (şikâyet e-postalarındaki azalma) başlı başına veri değildir ve kafa karıştırıcı değişkenlerle açıklanabilir.

**Sonuç:** Onaylanamaz.

---

## Özet Bulgular

| İddia | Tier | Durum | Sonuç |
|-------|------|-------|-------|
| 1. Hata azalması | `[KKE]` | Kritik kontrol eksik | NOT PROVEN |
| 2. Ambalajlama süresi | `[K]` | Kontrol grubu destekli, ölçülmüş | PROVEN |
| 3. Yazılım benimsemesi | `[H]` | Gözlem yalnızca; ölçüm yok | NOT PROVEN |
| 4. 8 aylık ROI | `[H]` | Tedarikçi tarafından hesaplanmış; bağımsız doğrulama yok | NOT PROVEN |
| 5. Lisans maliyeti | `[K]` | İmzalı sözleşme | PROVEN |
| 6. Müşteri memnuniyeti | `[H]` | Ölçülmemiş; dolaylı göstergeler sadece | NOT PROVEN |

---

## Öneriler (Kritiklik × Etki/Çaba)

1. **Hata Tanımı (İddia 1) — ACIL:** Yazılım öncesi ve sonrasında hata tanımını tekdüze hale getirin ve eski tanım altında geçişten sonraki hataları yeniden sayın. Tanımlama değişikliği nedeniyle iddia desteklenmiş görünemez.

2. **Müşteri Memnuniyeti Anketi (İddia 6) — ORTA:** Hedefli müşteri memnuniyeti anketi yapın. Şikâyet e-postaları ölçüm için yetersiz.

3. **Yazılım Benimsemesi (İddia 3) — ORTA:** Sistem loglarından aktif kullanım oranını ve eğitim tamamlama oranlarını toplayın. Müdür gözlemi bağlamsal ama ölçülmüş kanıt değildir.

4. **ROI Modeli (İddia 4) — DÜŞÜK:** Tedarikçi hesaplamasının yerine bağımsız ROI analizi yapın. Yapılan 8 haftalık veri, tam yıl tahmini için uygulanabilir yeterli veridir; ancak tahmin tedarikçi olmayan bir denetçi tarafından yapılmalıdır.

---

VERDICTS
1: NOT PROVEN
2: PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
