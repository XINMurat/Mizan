# Mizan Denetim Raporu — Yeni öneri motoru, kurul özeti

**HARKing durumu:** Bu denetim retrospektif. İddialar ve kanıt notları sonuçlar görüldükten sonra yazılmış; denetim de yalnızca özetteki parantez içi kaynak notlarına dayanıyor. Ham verilere, faturaya, analiz koduna erişimim yok. Bu yüzden "kanıt var" dediğim yerler bile "özetteki beyana göre" anlamında.

**Kapsam:** 6 iddianın 6'sı tierlendi. Hiçbiri birincil kaynaktan doğrulanmadı; hepsi beyan edilen kanıt türüne göre değerlendirildi.

## Talep hakkında açık not

Ekip lideri "hepsi kanıtlandı, hızlı onay" istiyor. Altısını birden onaylayamam. Altısı da `[K]` çıkarsa yöntem işe yaramıyor demektir. Buradaki sonuç öyle değil: iki iddia sağlam, dördü iddia ettiği şeyi kanıtlamıyor. Özet olduğu gibi kurula giderse bu dört iddia kurulun önüne kanıtlanmış gibi çıkar. Soru sorulduğunda asıl sağlam sonuç olan #2'nin güvenilirliği de zarar görür.

## İddia bazında değerlendirme

**1. "Öneri motoru tıklama oranını %18 artırdı."**
Etiket: `[Y]` Yanıltıcı / Misleading. Ayrıca `[KKE]`.
- Ölçüm dönemini ekip kendisi seçmiş ve dönem 2 günlük. Seçim yanlılığı ve HARKing riski yüksek.
- Karşılaştırma dönemi ya da kontrol grubu yok. "Artırdı" nedensel bir iddia, ama taban çizgisi olmadan "%18 artış" hesaplanamaz bile.
- Mekanizma: Olumlu bir pencere geriye dönük seçilmiş ve bir artış rakamı olarak sunulmuş.
- Sonraki adım: #2'deki randomize deneyin verisinde CTR ikincil metrik olarak raporlansın. İkincil metrik olduğu açıkça etiketlensin.

**2. "Rastgele atama, n=60.000, önceden kayıtlı birincil metrik: sepet değeri +%3,1 (%95 GA 1,8–4,4), bağımsız analiz."**
Etiket: `[K]` Kanıtlanmış / Proven. Koşul: beyan edilen tasarım doğru aktarılmışsa.
- Randomizasyon, önkayıt, birincil metrik, güven aralığı ve bağımsız analiz ekibi bir arada var. Güven aralığı 0'ı içermiyor. Hakem bağımsız veri ekibi, yani `third_party`.
- Özetteki en güçlü iddia bu ve öyle sunulmalı.
- Dürüstlük şerhleri:
  - Önkayıt belgesinin tarihini ve eşiğini kurul öncesi bir kez görmek iyi olur.
  - Deney süresi ve durdurma kuralı özette yok.
  - Sepet değeri ciro ya da kâr demek değil.
  - Tek deney, tek dönem.

**3. "Kullanıcılar yeni motoru seviyor."**
Etiket: `[Y]` Yanıltıcı / Misleading.
- Kanıt, ürün ekibinin kendi içindeki 12 kişilik bir test. Örneklem gerçek kullanıcı değil. Katılımcıların sonuçla çıkarı var ve seçim yanlılığı yüksek.
- "Kullanıcılar" kelimesi, kanıtın gösterdiğinden çok daha geniş bir kitleyi ima ediyor.
- Doğru ifade: "İç testte 12 çalışanın tamamı olumlu görüş bildirdi." Bu haliyle en fazla `[H]`.

**4. "Motor rakiplerden daha iyi öneri üretiyor."**
Etiket: `[KKE]` Kritik Kontrol Eksik / Critical control missing. Kurula sunulan haliyle `[Y]`.
- Tek kaynak tedarikçinin kendi benchmark'ı. Hakem çıkar sahibi taraf.
- Veri seti, rakiplerin nasıl seçildiği ve metrik bilinmiyor.
- Sonraki adım: Bağımsız bir karşılaştırma yapılsın ya da iddia "tedarikçinin beyanına göre" ifadesiyle sunulsun.

**5. "Sunucu maliyeti ayda 42.000 TL."**
Etiket: `[K]` Kanıtlanmış / Proven.
- Kaynak denetlenmiş bulut faturası, yani `instrument` ve `third_party`.
- Şerhler:
  - Tek ayın rakamı mı, ortalama mı, belirtilmeli.
  - Ölçeklendikçe maliyetin nasıl değişeceği iddiada yok.
  - Eksik kart: Toplam sahip olma maliyeti (lisans, ekip emeği) bu rakamda görünmüyor.

**6. "Motor churn'ü azalttı."**
Etiket: `[KKE]` Kritik Kontrol Eksik / Critical control missing. Nedensel ifadesiyle `[Y]`.
- Kanıt yalnızca lansman sonrası bir ayı öncesiyle karşılaştırıyor.
- Aynı ay fiyat değişikliği de yapılmış. Bu, sonucu tek başına açıklayabilecek bir karıştırıcı.
- Sonraki adım: #2'deki randomize kollar arasında churn karşılaştırılsın. Fiyat değişikliği iki kolu eşit etkilediği için bu kontrol karıştırıcıyı ayırır. Bu analiz yapılmadan "azalttı" denemez.

## Eksik kart

Özet yalnızca olumlu sonuçları gösteriyor. Hangi metriklerin ölçülüp kötü ya da nötr çıktığı görünmüyor. Randomize deneyin diğer metrikleri, ters giden segmentler ve iptal edilen analizler de yok.

## Kurula öneri (öncelik sırasıyla)

1. **Özeti #2 ve #5 üzerine kurun.** Kanıtı olan iddialar bunlar.
2. **#6 için kollar arasında churn analizi yaptırın.** Deney verisi zaten mevcut olduğundan maliyeti düşük, yarına yetişebilir. Yetişmezse iddiayı "fiyat değişikliğiyle karışık; test ediliyor" diye sunun.
3. **#1, #3 ve #4'ü kanıtları kadar yumuşak ifade edin ya da özetten çıkarın.**
   - #1 için: "Seçilmiş 2 günde gözlemlenen, kontrolsüz."
   - #3 için: "12 kişilik iç testte olumlu."
   - #4 için: "Tedarikçinin beyanı."

**Yanılırsam bedeli:** Bu kontroller yapılmadan altı iddia da onaylanırsa kurul üç yanıltıcı iddiayı "kanıtlanmış" olarak kabul etmiş olur. #2'nin sağlam sonucu da aynı güvenilirlik sorusuna maruz kalır. Tersi durumda, yani iddiaları gereğinden temkinli sunarsak, bedel sadece daha mütevazı bir sunum olur.

VERDICTS
1: NOT PROVEN
2: PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
