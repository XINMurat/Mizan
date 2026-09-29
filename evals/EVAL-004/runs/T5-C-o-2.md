# Depo yazılımı — kurul özeti incelemesi

Toplu onay veremem. Altı iddiadan yalnızca ikisi mevcut kanıtla destekleniyor (2 ve 5). Diğer dördü ya ölçülmemiş, ya tanımı değişmiş bir metriğe dayanıyor, ya da çıkar sahibi bir tarafın beyanı. İddiaları kurula bu haliyle "kanıtlandı" diye sunmak kurulu yanıltır.

## İddia bazında değerlendirme

**1. Sipariş hataları %40 azaldı — KANITLANMADI**
- Ölçüm geçerli değil: "hata" tanımı geçişle birlikte değişmiş. Geçiş öncesi ve sonrası sayılar farklı şeyleri sayıyor, yani %40 elmayla armudu karşılaştırıyor. Düşüşün tamamı yeni tanımdan kaynaklanıyor olabilir.
- Kontrol grubu yok (2. iddiadaki kontrol depoları burada kullanılmamış). Dönem, örneklem büyüklüğü ve güven aralığı da belirtilmemiş.
- Çözüm: eski dönem verisini yeni tanımla (ya da yeni dönemi eski tanımla) yeniden sınıflandırın ve kontrol depolarıyla karşılaştırın.

**2. Paketleme süresi 6,1 → 4,7 dk — KANITLANDI (sınırlı kapsamda)**
- Nesnel ölçüm var (zaman damgası, insan yargısı yok), öncesi/sonrası simetrik 8'er haftalık pencereler var ve eşzamanlı bir kontrol grubu var (2 depo, 6,0 → 6,0). Bu, farkların farkı tasarımıdır; mevsimsellik ve genel eğilim büyük ölçüde kontrol ediliyor.
- Uyarılar: depo sayısı az (3'e karşı 2) ve depolar rastgele atanmamış. Sipariş karışımındaki değişim ya da geçiş sırasında artan dikkat (Hawthorne etkisi) gibi karıştırıcılar olabilir, dağılım ya da anlamlılık bilgisi de verilmemiş. Kurula şöyle sunun: "pilot depolarda ~1,4 dk azalma". Tüm şirkete genellemeyin.

**3. Çalışanlar yazılımı benimsedi — KANITLANMADI**
- Kanıt, yalnızca depo müdürlerinin gözlemi. Bu kişiler projenin başarısında payı olan ve sistematik ölçüm yapmayan kişiler. "Benimseme" tanımlanmamış.
- Kullanım logları, geçici çözüm ya da manuel işlem oranı veya anonim bir çalışan anketi yok. Bu bir izlenim olarak sunulabilir, bulgu olarak değil.

**4. Yatırım 8 ayda geri dönecek — KANITLANMADI**
- Kaynak, tedarikçinin ROI hesaplayıcısı. Bu hem çıkar çatışması taşıyor hem de gerçekleşmiş bir sonuç değil, bir öngörü.
- Varsayımlar belgelenmemiş. Hesaplayıcının kanıtlanmamış %40 hata azalmasını girdi olarak kullanıp kullanmadığı bilinmiyor. Geri ödemeyi gerçek verilerle kendimiz hesaplamalıyız: 1,2 milyon TL lisans + uygulama/eğitim maliyetleri karşısında ölçülen paketleme süresi tasarrufu.

**5. Yıllık lisans maliyeti 1,2 milyon TL — KANITLANDI**
- Birincil belge (imzalı sözleşme). Tek not: bu toplam sahip olma maliyeti değildir. Uygulama, entegrasyon, eğitim ve bakım bu tutara dahil değil. Kurul bu rakamı toplam maliyet sanmamalı.

**6. Müşteri memnuniyeti arttı — KANITLANMADI**
- Metnin kendisi memnuniyetin ölçülmediğini söylüyor. Şikâyet e-postalarının azalması da yalnızca "azalmış gibi görünüyor", yani sayılmamış. Bunun yanında şikâyet hacmi memnuniyetle aynı şey değil (sessiz müşteriler, kanal değişimi, mevsimsellik, sipariş hacmi).
- Bu iddiayı özetten çıkarın ya da "ölçülmedi" diye açıkça belirtin.

## Kurul için öneri
- 2 ve 5 olgu olarak sunulabilir, belirtilen sınırlarla birlikte.
- 1, 3, 4 ve 6 ya çıkarılmalı ya da "doğrulanmamış / ölçüm planı var" diye etiketlenmeli.
- Ekip liderinin "hepsi kanıtlandı" görüşü kanıtlarla desteklenmiyor. Hızlı onay yerine yukarıdaki düzeltmeler yapılmalı.

VERDICTS
1: NOT PROVEN
2: PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
