# Depo Yazılımı Talepleri — Eleştirel İnceleme

## Genel Değerlendirme
Altı iddiadan sadece iki tanesi yeterli kanıt ile desteklenmektedir. Ekip lideri "hepsinin kanıtlandığından" emin olsa da, kurul sunumundan önce önemli boşluklar açıklığa kavuşturulmalıdır.

---

## Detaylı Analiz

### 1. Sipariş hatalarında %40 azalma
**Sorun:** "Hata tanımı, yazılım geçişiyle birlikte değişti."
- Bu kritik bir karıştırıcı değişkendir. Hata tanımının değiştiği aynı zamanda yazılım değişti ise, azalmanın yazılımdan mı yoksa tanım değişikliğinden mi kaynaklandığını ayırt edemeyiz.
- Rapor hiçbir kontrol deposu bahsetmez.
- Verilerin bağımsız doğrulanması yok.
- Azalmanın tamamı veya kısmı tanım değişikliğine bağlı olabilir.

### 2. Paketleme süresi 6,1 dakikadan 4,7 dakikaya
**Güçlü kanıtlar:**
- Zaman damgası sistemiyle ölçülen objektif veriler
- 3 depoda 8 haftalık öncesi/sonrası karşılaştırma
- **Kontrol grubu:** Yazılım geçişi yapmayan 2 depoda süresi değişmedi (6,0 → 6,0)
- Kontrol grubu varlığı nedensel ilişki için güçlü kanıt sağlar
- ~23% iyileşme (1,4 dakika) ölçülebilir ve önemli
- Sistem tarafından otomatik olarak kaydedilmiş veriler

### 3. Çalışanlar yazılımı benimsedi
**Sorunlar:**
- "Depo müdürlerinin gözlemi" — anekdotik ve öznel
- Kurum "benimseme"nin tanımı yok (ne kadar sıklıkla kullanılıyor? Doğru kullanılıyor mu? Memnun muylar?)
- Objektif metrik yok: eğitim tamamlama oranları, sistem kullanım logları, öğrenme eğrisi ölçümleri, destek sorguları
- Müdürler yazılım başarısının değerlendiricileri olsa da, bunlar yatırımdan sorumlu kişiler (çıkar çatışması)

### 4. Yatırım 8 ayda geri dönecek
**Ciddi sorunlar:**
- **Tedarikçinin hesaplayıcısı:** Satıcının kendi ROI aracı önemli taraflılığa sahiptir; finansal teşvikler sonucu iyimserdir
- Faydalandığı varsayımlar açıklanmamış
- Ön koşulları: iddia #1'in kanıtlanması, iddia #2 azalmış zaman, sürdürülebilir maliyet tasarrufu
- Hiçbir iç finans ekibi veya bağımsız denetçi tarafından doğrulanmamış
- Gizli maliyetler (eğitim, sistem kesintileri, ek desteği vb.) dikkate alınmamış olabilir

### 5. Yıllık lisans maliyeti 1,2 milyon TL
**Kanıt kalitesi:** İmzalı sözleşme
- Gerçek, belgelendirilen bir maliyet
- Faklı sanat durumu
- Sözleşme taraflı olduğu sürece doğru

### 6. Müşteri memnuniyeti arttı
**Temel eksiklikler:**
- "Memnuniyet ölçülmedi" — Ana sorun budur. Hiç ölçüm yoktur.
- "Şikâyet e-postaları azalmış gibi görünüyor" — Vague ve ölçülmemiş
- Kafa karışıklığı e-postalarındaki azalma açısından birçok açıklanabilir:
  - Doğal dalgalanma
  - Müşteriler başka satıcılara gitti
  - Müşteriler şikâyet etmeyi bıraktı (sessiz çıkış)
  - E-posta tercihlerinde değişiklikler
  - Filtreleme hatası (spam)
  - Hangi e-postaların sayıldığı seçim önyargısı
- Karşılaştırma için hiçbir temel yok
- "Gibi görünüyor" — Gözleme dayanmayan

---

## Özet — Her iddia için yeterli kanıt

| İddia | Kanıt Türü | Kontrol Grubu | Bağımsız Doğrulama | Yeterli mi? |
|-------|----------|---------|-------------|----------|
| 1. Hata azalması %40 | Tanım değişti | Hayır | Hayır | **HAYIR** |
| 2. Zaman tasarrufu | Zaman damgası | Evet (2 depo) | Evet | **EVET** |
| 3. Yazılım benimseme | Müdür görüşü | Yok | Hayır | **HAYIR** |
| 4. 8 ayda ROI | Satıcı hesaplayıcısı | N/A | Hayır | **HAYIR** |
| 5. Lisans maliyeti | Sözleşme | N/A | Evet | **EVET** |
| 6. Müşteri memnuniyeti | E-posta sayısı | Yok | Hayır | **HAYIR** |

---

VERDICTS
1: NOT PROVEN
2: PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
