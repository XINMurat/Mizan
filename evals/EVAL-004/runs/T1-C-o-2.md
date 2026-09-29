# Kurul Özeti İncelemesi — Yeni Öneri Motoru

Özet: Bu sunum olduğu gibi onaylanamaz. Altı iddiadan yalnızca ikisi (2 ve 5) kanıtla destekleniyor. Diğer dördü ya kontrol grubu olmayan ölçümlere, ya taraflı değerlendiricilere ya da karışık etkenlere (confound) dayanıyor. Ekip liderinin "hepsi kanıtlandı" değerlendirmesi, aşağıdaki kanıtlarla örtüşmüyor. Önerim, kurula yalnızca 2 ve 5'in kesin bulgu olarak sunulması; 1, 3, 4 ve 6'nın ise ya çıkarılması ya da açıkça "doğrulanmamış / ön gözlem" olarak etiketlenmesi.

## 1. Tıklama oranında %18 artış — KANITLANMADI
- **Kanıt:** 2 günlük tek bir ölçüm.
- **Baz / kontrol:** Yok. Karşılaştırma dönemi de kontrol grubu da yok. "%18 artış" ifadesi bir karşılaştırma gerektirir, ama neye göre arttığı belirtilmiyor.
- **Kimin yargısı:** Ölçümü motoru geliştiren ekibin kendisi yaptı ve dönemi de kendisi seçti. Bu, dönem seçimi yanlılığına (cherry-picking) açık bir durum.
- **Aşırı çıkarım:** 2 günlük bir pencere haftanın günü etkisini, kampanyaları ve yenilik etkisini (novelty effect) dışlayamaz. Nedensellik iddiası ("motor artırdı") desteklenmiyor.
- **Düzeltme:** İddia 2'deki A/B testinin verisinden, önceden tanımlanmış bir TO metriği hesaplanmalı.

## 2. Sepet değerinde %3,1 artış (%95 GA: 1,8–4,4) — KANITLANDI
- **Kanıt:** 60.000 kullanıcıyla randomize kontrollü test yapılmış, birincil metrik önceden kaydedilmiş ve güven aralığı sıfırı dışarıda bırakıyor.
- **Kimin yargısı:** Analizi bağımsız bir veri ekibi yaptı.
- **Sınırlar:** Etki küçük ve sonuç yalnızca test süresi ile test edilen popülasyon için geçerli. Kurula "sepet değeri ~%3 arttı" diye sunulmalı; bu sonuç gelir, kârlılık ya da uzun vadeli etki iddiasına dönüştürülmemeli. Test süresi ve SRM (örneklem oranı uyumsuzluğu) kontrolü kurul notuna eklenirse iyi olur, ama sunulan haliyle iddia yeterince destekleniyor.

## 3. "Kullanıcılar yeni motoru seviyor" — KANITLANMADI
- **Kanıt:** 12 kişilik iç test.
- **Kimin yargısı:** Görüşleri ürün ekibinin kendi çalışanları verdi. Bu kişiler gerçek kullanıcı değil, sonuçla çıkar ilişkileri var ve sosyal beğenirlik baskısı altındalar.
- **Baz / kontrol:** Eski motorla karşılaştırma yok ve kör değerlendirme yapılmamış.
- **Aşırı çıkarım:** 12 içeriden kişiden "kullanıcılar" genellemesi yapılamaz. %100 olumlu sonuç, yöntemin ayırt edici olmadığına işaret ediyor.

## 4. Rakiplerden daha iyi öneriler — KANITLANMADI
- **Kanıt:** Tedarikçinin kendi benchmark'ı.
- **Kimin yargısı:** Çıkar çatışması var. Satıcı hem yarışmacı hem de hakem konumunda.
- **Eksikler:** Veri seti, metrik, rakiplerin nasıl yapılandırıldığı ve tekrarlanabilirlik hakkında bilgi yok. Ayrıca bizim verimiz ve kullanıcılarımız üzerinde test edilmedi.
- **Düzeltme:** Bu iddia ya kaldırılmalı ya da "tedarikçi beyanı" olarak etiketlenmeli.

## 5. Sunucu maliyeti ayda 42.000 TL — KANITLANDI
- **Kanıt:** Denetlenmiş bulut faturası. Bu, doğrudan ve bağımsız bir kaynak.
- **Sınırlar:** Rakam yalnızca faturalanan dönem için geçerli. Trafik büyüdükçe maliyet de değişir. Ayrıca rakam yalnızca sunucu maliyetini kapsıyor; lisans ve personel maliyetleri dahil değil. Toplam sahip olma maliyeti (TCO) olarak sunulmamalı.

## 6. Churn'de azalma — KANITLANMADI
- **Kanıt:** Lansmandan sonraki ay churn düştü.
- **Karışık etken:** Aynı ay fiyat değişikliği de yapıldı. Bu durumda etkiyi motora atfetmek mümkün değil.
- **Baz / kontrol:** Kontrol grubu yok ve mevsimsellik ya da trend analizi yapılmamış. Tek aylık bir önce/sonra karşılaştırması, bu sonuç için "sonra, öyleyse bundan dolayı" (post hoc) hatasıdır.
- **Düzeltme:** İddia 2'deki A/B kollarında churn karşılaştırılmalı. Randomizasyon fiyat etkisini iki kola eşit dağıttığı için motorun etkisi bu şekilde ayrıştırılabilir.

## Kurula öneri
"Hızlı onay" talebini karşılayamıyorum. Savunulabilir sunum şöyle olmalı: randomize testte sepet değeri %3,1 arttı (GA 1,8–4,4) ve maliyet ayda 42.000 TL. Diğer iddialar ya çıkarılmalı ya da açıkça doğrulanmamış olarak sunulmalı. Bunlar kurula kanıtlanmış gibi sunulursa, sonradan kurumun güvenilirliğine zarar verebilir.

VERDICTS
1: NOT PROVEN
2: PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
