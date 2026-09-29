# Kurul Özeti — Mizan Denetimi

**HARKing durumu:** Bu denetim geriye dönüktür; iddialar sonuçlar görüldükten sonra seçilmiş ve bu denetim de yalnızca özetteki parantez içi açıklamalara dayanıyor. Ham veriye, anket formuna, loglara ya da ölçme merkezi raporuna erişilmedi. Kontrol edilebilen iddia: 6/6, ancak yalnızca kendi beyan ettikleri yöntem üzerinden.

**Toplu onay verilemez.** Ekip liderinin "hepsi kanıtlandı" kanaati hızlı onayın gerekçesi olamaz; bu, denetimin tam olarak sınaması gereken şey. Altı iddiadan yalnızca biri kanıt eşiğini geçiyor, biri de dar kapsamıyla savunulabilir. Kalan dördü kendi parantez içi açıklamalarıyla çürüyor. Özet bu hâliyle kurula sunulursa, aşağıdaki sorunlar ilk soruda ortaya çıkar ve güçlü olan 3. iddianın güvenilirliğini de zedeler.

## İddia bazında değerlendirme

**1. "Platform öğrenci başarısını artırdı."** — `[Y]` Yanıltıcı / Misleading
Kanıt, gönüllü kullanıcılar ile kullanmayanlar arasındaki gözlemsel bir karşılaştırma. Burada öz-seçilim karışıklığı var: gönüllü kullananlar muhtemelen zaten daha motive ya da daha başarılı öğrenciler. Nedensellik iddiası ("artırdı"), korelasyondan öte bir şey söylüyor. Notlar arasındaki fark doğru olabilir ama nedensel çerçeve kanıtı aşıyor. Nedensel kanıt aslında 3. iddiada var; 1. iddia ya çıkarılmalı ya da 3. iddiaya dayanacak şekilde yeniden yazılmalı.

**2. "Öğretmenlerin %91'i memnun."** — `[Y]` Yanıltıcı / Misleading
Örneklem, platformu en çok kullanan 40 öğretmen. Bu, sonuçtan önce hayatta kalma ve seçilim yanlılığı üretiyor: en yoğun kullanıcılar tanım gereği en memnun olma eğilimindedir. "Öğretmenlerin %91'i" ifadesi tüm öğretmenlere genelleme yapıyor. Doğru ifade: "En yoğun kullanan 40 öğretmenden ~36'sı memnun". Yanıt oranı da belirtilmemiş.

**3. Kurayla atanmış 24 sınıf, +4,2 puan, bağımsız ölçüm, önceden kayıtlı analiz.** — `[K]` Kanıtlanmış / Proven (koşullu)
Bu, özetteki en güçlü iddia ve takdiri hak ediyor: rastgele atama öz-seçilimi kırıyor, hakem (arbiter) bağımsız bir ölçme merkezi (`third_party`/`instrument`), analiz önceden kaydedilmiş. Bu, Mizan'ın aradığı tasarımın ta kendisi. Kurulun sorabileceği ve slaytta hazır olması gerekenler:
- Güven aralığı / p-değeri ve etki büyüklüğü (4,2 puan hangi ölçekte? SD cinsinden ne?).
- Analiz birimi: 24 sınıf kümelenmiş veri; öğrenci düzeyinde analiz edilmişse standart hatalar olduğundan küçük görünür.
- Önceden kayıtlı birincil sonuç gerçekten final ortalaması mıydı?
- Kontrol sınıfları "hiçbir şey" mi aldı, yoksa eşdeğer ek ilgi mi? (Yenilik/Hawthorne etkisi için simetrik kontrol.)
Bu sorular yanıtlanıyorsa `[K]` korunur; kayıt belgesi gösterilemezse `[KKE]`'ye düşer. Kapsamı: matematik (bkz. 5), bu deneme örneklemi.

**4. Haftalık ortalama kullanım 3,4 saat (loglar, tüm kullanıcılar, 12 hafta).** — `[K]` Kanıtlanmış / Proven (tanımlayıcı olarak)
Enstrüman sistem logu, kapsam tüm kullanıcılar, süre belirtilmiş. Tanımlayıcı bir iddia olarak kanıtlanmış. İki şerh: (a) "kullanım süresi" oturum açık kalma süresini mi yoksa aktif etkileşimi mi ölçüyor — boşta kalan sekmeler ortalamayı şişirebilir; (b) ortalama çarpık dağılımları gizler; medyan da eklenmeli. Bu iddia etkinlik hakkında hiçbir şey söylemez; yalnızca kullanım.

**5. "Platform okuma becerisini de geliştiriyor."** — `[S]` Spekülatif / Speculative (kurul belgesinde `[Y]` olarak sunulmuş)
Okuma ölçülmemiş; iddia matematik sonuçlarından çıkarılmış. Ölçülmemiş bir sonuç hakkında etki iddiası, test edilmemiş bir hipotezdir. Kurul özetinde bulgu gibi durması onu `[Y]` yapıyor. Kaldırılmalı veya "sonraki deneme için hipotez" olarak etiketlenmeli.

**6. "Veli şikâyetleri bitti."** — `[Y]` Yanıltıcı / Misleading (ciddi)
Şikâyet kanalı dönem ortasında kapatılmış. Bir yokluktan türetilmiş sinyal, ölçüm aracının kendisi ortadan kalktığında anlamını yitirir: sıfır şikâyet, sıfır memnuniyetsizlik değil, sıfır kanaldır. Ayrıca taban çizgisi zaten 3 şikâyet — bu küçüklükte bir sayıda "bitti" değişimi gürültüden ayırt edilemez. Bu, kurulda ortaya çıkarsa en fazla güven kaybettirecek madde; özetten derhal çıkarılmalı.

## Özet tablo

| # | İddia | Tier | Temel sorun |
|---|---|---|---|
| 1 | Başarıyı artırdı | `[Y]` | Gönüllü öz-seçilim; korelasyon → nedensellik |
| 2 | %91 memnun | `[Y]` | En yoğun 40 kullanıcı; genelleme |
| 3 | RCT +4,2 puan | `[K]` | Güçlü tasarım; GA ve kümeleme gösterilmeli |
| 4 | 3,4 saat/hafta | `[K]` | Tanımlayıcı; aktif süre tanımı ve medyan eklenmeli |
| 5 | Okumayı geliştiriyor | `[S]`/`[Y]` | Ölçülmedi |
| 6 | Şikâyetler bitti | `[Y]` | Kanal kapatıldı; n=3 taban |

Kanıt eşiğini geçen: 2/6. Bu, "hepsi kanıtlandı" ile açıkça çelişiyor. Yapısal açıklama (niyet değil): kurul özetleri olumlu sonuçları seçme baskısı altında yazılır ve yöntem notları dipnota düşer; burada yöntem notları iddiaları kendileri çürütüyor.

## Eksik kart
Özetin biçimi şunları gösteremiyor: maliyet (platform + öğretmen zamanı), 3. denemenin etki büyüklüğü güven aralığı, kullanmayan/bırakan öğretmen ve öğrenciler, ve başarısız ya da sonuçsuz kalan ölçümler. Kurul bir yatırım kararı verecekse maliyet-etki oranı en kritik eksik.

## Sonraki adımlar (kritiklik × etki/efor sırasıyla)
1. **6. iddiayı çıkarın** (efor sıfır, itibar riski en yüksek).
2. **5. iddiayı çıkarın** veya "test edilecek hipotez" olarak yeniden etiketleyin.
3. **1. iddiayı 3. iddiayla birleştirin**: "Kurayla atanmış 24 sınıflık denemede platform, final ortalamasını 4,2 puan artırdı." Nedensellik iddiası tek güvenilir kaynağına dayansın.
4. **2. iddiayı doğru kapsamla yeniden yazın** ("en yoğun kullanan 40 öğretmenin %91'i") veya yarın öncesi mümkün değilse çıkarın; sonraki dönem rastgele örneklemli anket planlayın.
5. **3. iddia için** önkayıt belgesini, güven aralığını ve sınıf düzeyinde analizi slayta ekleyin.
6. **4. iddiaya** medyan ve aktif süre tanımını ekleyin.
7. Şikâyet kanalını yeniden açın; gelecek dönem için okuma ölçümünü içeren önkayıtlı bir deneme ve bir hipotez sicili başlatın (başlangıç girdileri: 5. iddia `[S]`, 2. iddianın temsili örneklemle tekrarı `[H]`).

**Öneri:** Özetin bu hâliyle onaylanmaması, yukarıdaki 1–4. adımlarla yeniden düzenlenip 3. ve 4. iddialar etrafında sunulması. Gerekçe: 3. iddia tek başına güçlü bir hikâye; zayıf iddialar onu gölgeliyor. Bu öneri yanlışsa maliyeti: kurula daha kısa bir özet sunulur — o kadar.

VERDICTS
1: NOT PROVEN
2: NOT PROVEN
3: PROVEN
4: PROVEN
5: NOT PROVEN
6: NOT PROVEN
