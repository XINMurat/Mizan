# Mizan Denetim Raporu — Yeni öneri motoru kurul özeti

**HARKing durumu:** Bu denetim geriye dönüktür (retrospektif); iddialar sonuçlar görüldükten sonra seçilip yazılmış. Benim denetimim de geriye dönük — yalnızca özette verilen kaynak açıklamalarına dayanıyor, ham veriyi açmadım.

**Kapsam:** 6 iddianın 6'sı değerlendirildi; hiçbirinin ham verisi elimde değil. Değerlendirme, her iddianın yanında beyan edilen yöntem/kaynağa göre yapıldı.

**Talep çatışması (adı konarak):** "Hızlı onay" ve "hepsi kanıtlandı" beklentisi, bu yöntemin tek tip `[K]` vermeme kuralıyla çelişiyor. Toplu onay veremem; aşağıda iddia bazında hüküm var. Karar sizin — ama kurula altı iddianın dördünü kanıtlanmış diye sunmak, kurulda sorulacak ilk kontrol sorusunda çöker.

## İddia bazında tier

| # | İddia | Tier | Gerekçe |
|---|---|---|---|
| 1 | Tıklama oranı %18 arttı | `[Y]` Yanıltıcı / Misleading | Ekibin kendi seçtiği 2 günlük pencere, karşılaştırma dönemi yok. Pencere seçimi sonuç görüldükten sonra yapılabilir (cherry-picking); hafta içi/kampanya/mevsim etkisi ayrılamıyor. "%18" kesin bir sayı gibi sunuluyor ama taban çizgisi olmadan hiçbir şeyin artışı değil. |
| 2 | Sepet değeri %3,1 yüksek (GA %1,8–4,4), 60.000 kullanıcı, randomize, önkayıtlı, bağımsız analiz | `[K]` Kanıtlanmış / Proven | Randomizasyon, önkayıtlı birincil metrik, alt sınırı sıfırın üstünde güven aralığı, üçüncü taraf hakem (bağımsız veri ekibi). Setin en güçlü iddiası — kurul sunumunun omurgası bu olmalı. Dürüstlük şerhi: tek deney; süre ve yenilik etkisi (novelty) özette belirtilmemiş; sepet değeri ≠ kâr. |
| 3 | Kullanıcılar yeni motoru seviyor | `[Y]` Yanıltıcı / Misleading | Kanıt: ürün ekibinin 12 kişilik iç testi. Bunlar kullanıcı değil, motoru yapan/sahiplenen ekip — seçim yanlılığı ve çıkar çatışması. %100 olumlu, n=12, kontrol yok. "Kullanıcılar" genellemesi kanıtın bir kademe üstünde. |
| 4 | Motor rakiplerden daha iyi öneri üretiyor | `[H]` Makul Hipotez / Plausible hypothesis — `[KKE]` | Tek kaynak tedarikçinin kendi benchmark'ı: hakem sınıfı `author` (çıkarı olan taraf). Bağımsız karşılaştırma yok; bu haliyle `[K]` olamaz. İddia #2 kendi motorumuzun eski motorumuza üstünlüğünü gösterir, rakiplere değil. |
| 5 | Sunucu maliyeti ayda 42.000 TL | `[K]` Kanıtlanmış / Proven | Denetlenmiş bulut faturası — belgesel, üçüncü taraf doğrulamalı kaynak. Şerh: fatura dönemi ve trafik ölçeklendikçe maliyetin değişip değişmeyeceği belirtilmemiş; toplam sahip olma maliyeti (ekip, lisans) dahil değil. |
| 6 | Motor churn'ü azalttı | `[KKE]` Kritik Kontrol Eksik / Critical control missing | Lansman sonrası ayda churn düştü, ama aynı ay fiyat değişikliği de yapıldı — iki müdahale tamamen karışık (confounded). Nedensellik kurulamaz. #2'deki A/B deneyinin kolları churn açısından karşılaştırılırsa bu kontrol mümkün olabilir. |

**Özet:** 2 `[K]`, 1 `[H]/[KKE]`, 1 `[KKE]`, 2 `[Y]`. Kanıtlanmış iddialar (2 ve 5) gerçekten sağlam ve spesifik olarak takdiri hak ediyor: #2 iyi tasarlanmış bir deneyin örnek sonucu.

## Eksik kart (formatın gösteremediği)
Kurul özeti yalnızca kazanımları listeliyor: #2 deneyinde ikincil metrikler (tıklama, churn, dönüşüm, gecikme) ne gösterdi? Olumsuz ya da nötr çıkan metrik var mı? Maliyet (#5) ile getiri (#2) yan yana konmamış — %3,1 sepet artışının aylık TL karşılığı 42.000 TL'yi aşıyor mu, özette hesap yok.

## Mekanizma (motive değil)
Çarpıklık büyük ihtimalle yapısal: kurul formatı "başarı listesi" teşvik ediyor ve farklı kalitedeki kanıtlar aynı madde işaretiyle yan yana konunca en zayıfı en güçlüsünün itibarını ödünç alıyor. Kasıt iddia etmiyorum.

## Sonraki adımlar (kritiklik × etki/efor sırasıyla)
1. **Sunumu #2 ve #5 üzerine kurun** (efor: sıfır). Bunlar kurulun sorgusuna dayanır.
2. **#1'i çıkarın ya da #2'deki A/B deneyinin tıklama verisiyle değiştirin** (efor: düşük — veri muhtemelen zaten var). Randomize kollardaki CTR farkı %18'in yerini alır.
3. **#6 için A/B kollarında churn'ü karşılaştırın** (efor: düşük-orta). Fiyat değişikliği iki kola eşit uygulandıysa bu kontrol karışıklığı çözer. Yapılamıyorsa "fiyat değişikliğiyle aynı aya denk geldi, ayrıştırılamadı" diye sunun.
4. **#3'ü "iç test olumlu geri bildirim verdi (n=12, ekip içi)" olarak yeniden ifade edin**; gerçek kullanıcı memnuniyeti iddiası için A/B kollarında kısa anket.
5. **#4'ü "tedarikçi beyanı" olarak etiketleyin** ya da çıkarın; bağımsız benchmark yoksa kurula kanıt olarak sunulmamalı.
6. #2 × #5 maliyet-getiri hesabını ekleyin: kurulun soracağı asıl soru bu.

**Önerim:** Toplu onay yerine revize özetle gidin — #2 ve #5 "kanıtlanmış", diğerleri doğru etiketiyle. Neden: kurulda bir iddia çökerse sağlam olan #2'nin de güvenilirliği zedelenir. Önerim yanlışsa maliyeti: sunum biraz daha mütevazı görünür; başka kayıp yok.

VERDICTS
1: NOT PROVEN
2: PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
