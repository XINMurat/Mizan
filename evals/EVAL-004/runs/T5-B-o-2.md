# Mizan Denetim Raporu — Depo yazılımı kurul özeti

**HARKing durumu:** Bu denetim geriye dönüktür. Hem iddialar hem bu değerlendirme sonuçlar görüldükten sonra yazıldı. Eşikler önceden kilitlenmemişti.
**Kapsam:** 6 iddianın 6'sı, yalnızca iddiaların yanında verilen kaynak notlarına göre değerlendirildi. Ham veri, sözleşme ya da ölçüm kayıtları açılmadı. Bu yüzden hiçbir tier doğrudan belge incelemesine dayanmıyor, özette beyan edilen kaynaklara dayanıyor.

**Talep hakkında:** İstenen şey "hızlı onay". Mizan'ın işi toplu onay vermek değil. Altı iddianın hepsini `[K]` saymak bu yöntemin reddettiği anti-pattern'dir. Aşağıda iddialar tek tek tiere ayrıldı. Kanıtı yeten iddialar aynı açıklıkla onaylandı. Sonuç: **6 iddiadan 2'si kanıtlanmış, 4'ü kanıtlanmamış.**

## İddia bazında değerlendirme

**1. "Sipariş hatalarını %40 azalttı."** → `[Y]` Yanıltıcı / Misleading
Hata tanımı geçişle aynı anda değişti. Bu yüzden önce ve sonra rakamları aynı büyüklüğü ölçmüyor. %40'lık düşüşün ne kadarı gerçek iyileşme, ne kadarı tanım değişikliği, ayırmak mümkün değil. Sayı gerçek bir hesaplamadan gelmiş olabilir ama "azalttı" demek, verinin desteklemediği bir nedensellik ima ediyor.
*Sonraki adım:* Geçiş öncesi dönemi yeni tanıma göre yeniden sınıflandırın ya da sonraki dönemi eski tanımla sayın. Mümkünse kontrol depolarını da ekleyin.

**2. "Paketleme süresi 6,1'den 4,7 dakikaya indi."** → `[K]` Kanıtlanmış / Proven
Ölçüm aracı bağımsız bir enstrüman: zaman damgası sistemi. Önce ve sonra pencereleri simetrik (8'er hafta). Geçiş yapılmayan 2 kontrol deposu 6,0 → 6,0 ile sabit kaldı. Bu, mevsimsellik ve genel eğilim gibi karıştırıcılara karşı gerekli kontrolü sağlıyor. Değişim yaklaşık %23.
*Şerhler:* Yalnızca 3 depo var ve depolar rastgele seçilmedi. Geçiş dönemindeki eğitim ya da ekstra ilgi gibi Hawthorne etkisi dışlanmadı. Varyans ve güven aralıkları raporlanmadı. Kurula "3 depoda, kontrol depolarına karşı" diye kapsamıyla birlikte sunulmalı.

**3. "Çalışanlar yazılımı benimsedi."** → `[H]` Makul Hipotez / Plausible hypothesis (hakem yazarın tarafı olduğu için kalıcı `[KKE]`)
Kaynak müdürlerin gözlemi. Bu kişiler geçişin başarısında pay sahibi ve iddianın bir metriği yok. Ölçülebilir göstergeler şunlar olabilir: kullanım logları, sistem dışı (kâğıt/Excel) işlem oranı, çalışan anketi.

**4. "Yatırım 8 ayda geri dönecek."** → `[S]` Spekülatif / Speculative
Bu bir tahmin ve kaynağı yazılımı satan tedarikçinin hesaplayıcısı. Bağımsız bir hakem ya da gerçekleşmiş veri yok. Buna ek olarak, hesabın temel girdilerinden biri muhtemelen hata azalmasıdır ve bu girdi 1. iddianın `[Y]` sorununu miras alıyor.
*Sonraki adım:* ROI'yi iç ekiple yeniden hesaplayın. Girdi olarak 2. iddiadaki kanıtlanmış zaman tasarrufu ile 5. iddiadaki gerçek lisans maliyetini kullanın.

**5. "Yıllık lisans maliyeti 1,2 milyon TL."** → `[K]` Kanıtlanmış / Proven
Kaynak imzalı sözleşme, yani birincil belge. *Şerh:* Bu rakam yalnızca lisansı kapsıyor. Toplam sahip olma maliyeti (entegrasyon, eğitim, bakım) ayrıca sunulmalı.

**6. "Müşteri memnuniyeti arttı."** → `[Y]` Yanıltıcı / Misleading
Özetin kendi notu memnuniyetin ölçülmediğini söylüyor. Şikâyet e-postalarındaki düşüş ise "gibi görünüyor" düzeyinde, yani sayılmamış. Şikâyet sayısı memnuniyetin vekili olarak zayıf: şikâyet kanalı değişmiş olabilir, mevsimsel etki olabilir. Doğru ifade "ölçülmedi" olmalı.

## Eksik kart
Bu özette maliyet tarafı yalnızca lisanstan ibaret. Geçiş sorunları, kesintiler ve kontrol depolarının hata oranları da yok. Kurul formatı sadece kazanımları gösteriyor.

## Öneri (kritiklik × etki/çaba sırasıyla)
1. Kurula 2 ve 5'i kanıtlanmış olarak sunun.
2. 1 ve 6'yı ya çıkarın ya da "tanım değişti" ve "ölçülmedi" notlarıyla yeniden yazın. Mevcut halleriyle sunulmaları, kurul önünde güvenilirlik riski taşıyor.
3. 3'ü hipotez olarak sunun ve bir kullanım metriği ekleyin.
4. 4'ü "tedarikçi tahmini" diye etiketleyin ve iç ROI hesabını 2 ile 5'e dayandırın.

Ekip liderine not: "Hepsi kanıtlandı" ifadesi bu belgeyle desteklenmiyor. Bu tespit özetin yapısına dair, niyete dair değil. Başarı özetleri kazanımları öne çıkarma eğiliminde oluyor.

VERDICTS
1: NOT PROVEN
2: PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
