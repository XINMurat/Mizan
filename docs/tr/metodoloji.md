# Mizan — Kanıt-Katmanlı Denetim ve Önkayıt Registry'si
## Türkçe Tam Dokümantasyon (SKILL.md + Şablonlar + Kontrol Listesi)

> Bu belge, `mizan.skill` paketinin içindeki dört dosyanın birebir Türkçe
> karşılığıdır (`SKILL.md`, `references/templates.md`, `references/checklist.md`,
> `references/recovery.md`). Skill'in kendisi İngilizce çalışır (taşınabilirlik için)
> ama Claude ile her zaman Türkçe konuşabilirsiniz — skill, kullanıcının
> dilinde yanıt vermeyi zaten kural olarak içerir.

---

# BÖLÜM 1 — Skill'in Ana Tanımı (SKILL.md karşılığı)

## Ne zaman devreye girer?

Mizan şu durumlarda tetiklenir:

- Bir iddia setini **değerlendirmek, denetlemek, doğrulamak** istediğinizde
  (AI'ın ürettiği bir özet, proje raporu, öz-değerlendirme, pazarlama
  belgesi, araştırma yazısı, "yıl özeti" vb.)
- Övgü yerine **dürüst ve titiz değerlendirme** istediğinizde
- Kanıt katmanları, önkayıt, çürütme koşulları, HARKing, confound
  (karıştırıcı etken), isabet oranı gibi kavramlardan bahsettiğinizde
- Deneyler, çalışma örüntüleri, kararlar veya tahminler için bir
  **hipotez registry'si başlatmak veya sürdürmek** istediğinizde
- "Değerlendir", "denetle", "bu iddialar ne kadar sağlam?" dediğinizde
  veya pohpohlayıcı bir özet paylaşıp "buna ne demeli?" diye sorduğunuzda

Skill aktifken Claude asla salt kutlayıcı bir değerlendirme üretmez.

## Çekirdek taahhütler

Mizan (terazi/ölçü), titiz deneysel-bilim disiplinini herhangi bir iddia
setinin değerlendirilmesine ve canlı hipotez registry'lerine taşır:

1. **Her iddia bir kanıt katmanı alır.** Etiketsiz iddia yok.
2. **Eşikler sonuç görülmeden kilitlenir.** Bu imkânsızsa (retrospektif
   analiz), HARKing riski açıkça beyan edilir — asla sessizce yutulmaz.
3. **Her hipotez bir çürütme koşulu taşır.** Başarısız olamayacak bir
   iddia denetlenmiş değil, süslenmiş demektir.
4. **Çürütülen girdiler asla silinmez.** `[R]` işaretlenir ve yerinde
   arşivlenir. Negatif sonuçlar birinci sınıf sonuçtur.
5. **Sürpriz pozitifler manşetten önce simetrik kontrol ister.** Hipotezi
   pohpohlayan sonuç, confound denetimine en çok muhtaç olandır.
6. **Seçilmiş örnekler yerine isabet oranı.** Üç onaylayıcı anekdot seçim
   yanlılığıdır; puanlanmış bir tahmin sicili kanıttır.

## Kanıt katmanları (bu etiketler aynen kullanılır)

| Etiket | Türkçe | Anlamı |
|---|---|---|
| `[K]` | Kanıtlanmış | Doğrudan kanıt destekliyor; kaynak gösterilmiş; eşik karşılanmış |
| `[H]` | Makul Hipotez | Teorik gerekçe var; ampirik destek eksik veya eşik altında |
| `[S]` | Spekülatif | İlginç; şu an test edilemez veya test tasarlanmamış |
| `[R]` | Reddedildi | Test edildi ve kendi eşiğini geçemedi — kayıtta tutulur, silinmez |
| `[KKE]` | Kritik Kontrol Eksik | Sonuç var ama sonucu tersine çevirebilecek bir confound/baseline kontrolü koşulmamış |
| `[Y]` | Yanıltıcı | Teknik olarak doğruluk payı taşıyor ama kanıtın desteklediğinden fazlasını ima edecek şekilde çerçevelenmiş |

**Katman kayması (tier drift) kendisi bir bulgudur:** bir iddia iki belge
arasında yeni kanıt olmadan sessizce `[H]`'den `[K]`'ya taşınmışsa, bu
işaretlenir.

## İki mod — hangisi geçerli, önce karar ver

**Denetim modu (retrospektif).** Kullanıcı mevcut bir iddia seti veriyor —
özet, inceleme, rapor, AI-üretimi değerlendirme — ve ne kadarının
incelemeye dayanacağını soruyor. Çıktı: Denetim Raporu (Bölüm 2'deki
şablon).

**Registry modu (prospektif).** Kullanıcı hipotezleri ileriye dönük takip
etmek istiyor — deneyler, tahminler, çalışma-örüntüsü iddiaları, ürün
bahisleri. Registry Girdisi şablonuyla canlı bir Markdown belgesi
oluşturulur veya güncellenir.

İstek ikisini de içeriyorsa ("bunu denetle, sonra bir daha olmasın diye
takip kur"), önce denetim yapılır, sonra hayatta kalan `[H]` iddiaları
registry'nin ilk girdileri olarak ekilir.

## Denetim modu — prosedür

İlk denetimden önce hata-modu kontrol listesi (Bölüm 3) okunur.

1. **Atomize et.** Belgeyi tek tek kontrol edilebilir iddialara ayır.
   "r=0.997'yi şüpheli buldun ve bu init bug'ını buldurdu" cümlesi İKİ
   iddiadır (işaretleme gerçekleşti; keşfe o sebep oldu).
2. **Her iddiayı kaynaklandır.** Her iddia için hangi kanıtın onu
   doğrulayacağını ve o kanıtın erişilebilir olup olmadığını belirle
   (konuşma geçmişi, dosyalar, commit'ler, loglar, web). Kontrol
   edilebilir olanı gerçekten kontrol et — dosyayı aç, geçmişi ara,
   sayıyı hesapla. Doğrulanamayan iddia notuyla birlikte `[H]` alır;
   ne sessizce kabul ne sessizce ret.
3. **Her iddiayı katmanla.** İddiayı alıntıla, etiketi ver, tek satırlık
   gerekçeyi kaynağıyla yaz.
4. **Karşı-örnek avla.** Her örüntü-iddiası için ("hep X yaparsın",
   "sistem tutarlı biçimde Y") kabul etmeden önce tersinin örneklerini
   aktif olarak ara. Arama boş dönse bile raporla — "N kaynakta
   karşı-örnek bulunamadı" bilgidir; sessizlik değildir.
5. **Mümkün olan yerde isabet oranı hesapla.** Belge birinin
   yargısını/tahminlerini/sezgilerini övüyorsa, yalnız kazançları değil
   tam tahmin sicilini yeniden kur. Dürüstçe raporlanmış ~%50-60 isabet,
   %100'lük seçilmiş bir listeden daha değerlidir — ve bunu söyle.
6. **Eksik kartı adlandır.** Her özet formatı yapısal olarak bir şeyi
   dışarıda bırakır (başarısızlıklar, ertelemeler, terk edilen hatlar,
   maliyetler). Bu belgenin formatının gösteremediğini belirt ve mevcut
   kanıttan taslağını çıkar.
7. **Belgeyi değil alanı probla.** Yukarıdaki her adım birinin yazdığı bir
   cümleden başlar; bu yüzden hiçbiri **hiç iddia edilmemiş** bir yeteneği
   bulamaz — yokluk, katmanlanacak iddia üretmez. Bu alanda gerçekten
   yaşanan durumların listesini **edin** ve her birini modele karşı sına:
   ifade edilebiliyor (sorun yok) · edilemiyor **ve bilinçli sınır olarak
   yazılmış** (sorun yok, bu bir karardır) · edilemiyor ve **hiçbir yerde
   yazılı değil** (bulgu). **Bu listeyi tek başına yazamazsın ve yazmış gibi
   yapmamalısın:** alan sahibine sor, senaryoları kimin verdiğini kapsam
   beyanının parçası olarak kaydet. Uydurulmuş makul senaryolar, kanıt
   etiketi takılmış kurgudur. Boşluk bulunduktan sonra yazılan senaryo
   HARKing'dir ve kapsam hakkında hiçbir şey kanıtlamaz — hangilerinin
   geriye dönük olduğunu söyle. Sormayı başlatacak sekiz sınıflık tohum
   listesi madde 3.12'dedir. **Kaydı:** `probes.domain` (R19).
8. **Yeniden birleştir — yalnız iddiaları değil bileşimleri de denetle.**
   1. adım belgeyi parçalarına ayırdı; **iki özellik aynı anda geçerliyken**
   var olan bir kusur tam da o eylemle yok edildi ve sonraki hiçbir adımda
   geri gelmez. O yüzden bilerek geri birleştir: her özellik için
   dokunabildiği mevcut garantileri listele ve her çift için sor —
   **"bu garanti, bu özellik etkinken hâlâ geçerli mi?"** Önceliklendir:
   (a) **türetilmiş sinyaller** — bir yokluktan hesaplanan her şey, yeni bir
   durum var olduğu anda anlam değiştirir; (b) **tek tek çağrı yerinde
   uygulanan garantiler** — yeni bir toplu yüzey bunları toptan baypas eder.
   Sırayı da kontrol et: bazı çiftler yalnız tek yönde güvenlidir ve gerekli
   sıra bulgunun parçasıdır. Yeşil test paketi burada karşı kanıt değildir:
   testler özellik başına yazılır, parçalara tanıklık eder, çift hakkında
   susar. **Kaydı:** `probes.conjunction` (R20).
9. **Döngüyü kapat — yaşayan bir hedef için registry'yi ÖNER değil KUR.**
   Denetlenen şey bitmiş bir belge değil de yaşayan bir proje ise (bir repo,
   bir backlog, bir program), tek seferlik denetim kendisinden sonra doğan
   boşlukları göremez. Denetimin son eylemi bu yüzden registry dosyasını
   **yazmaktır** (ayakta kalan `[H]` iddialar ve bulunan her tekrarlayan hata
   sınıfıyla tohumlanmış) ve denetimi yeniden tetikleyecek eşiği
   adlandırmaktır — bir faz sınırı, bir sürüm, sabit bir kadans. *"İstersen
   takip kurayım mı?"* diye bitirmek bu skill'in bilinen bir hatasıdır:
   öneri ertelenir, proje görev kapatmaya devam eder, sonraki denetim ancak
   bir kullanıcı boşluğa çarptığında gelir. Kullanıcı reddederse reddi
   rapora yaz; sürekliliğin yokluğu da kayda geçsin.
   Kaçaklar da buraya düşer: denetimin kapsadığı bir zeminde sonradan bir
   kusur çıktığında **RR-13** onu bir sınıfa çevirir — `probes.escaped`,
   `class_ref` (ateşlemesi gereken kontrol) ya da `class_new` (bu kaçak
   sayesinde artık var olan prob), ki R21 bunu şart koşar. Puan kartı
   kaçakları zaten sayıyordu; saymak öğrenmek değildir, ve madde 3.12 ile
   3.13'ün ikisi de kimsenin kaçak diye kaydetmediği birer kaçaktan doğdu.
10. **HARKing durumunu beyan et.** Retrospektif analiz örneklerini
   sonuçları gördükten sonra seçmiştir. Bunu rapor başlığında açıkça
   söyle — denetimin kendisi de retrospektif olduğu için kendi durumunu
   da dahil ederek.
11. **Mekanizmayı niyetten ayır.** Bir belgenin neden çarpık olduğunu
   açıklarken yapısal açıklamaları (seçilim baskısı, format teşvikleri)
   niyet atfına ("pohpohlamak için tasarlamışlar") tercih et — niyet
   ancak kendisi kanıtlıysa iddia edilir.

## Registry modu — prosedür

1. **Her hipoteze bir girdi** (Bölüm 2'deki şablonla). Girdi test
   koşulmadan ÖNCE yazılır.
2. **Eşikleri sayısal kilitle.** "İyileştirir" eşik değildir;
   "ΔPPL ≤ −%3" veya "10 kaynakta 1'den az karşı-örnek" eşiktir. Eşik tek
   başına, kararlı bir yazarla temasa dayanmaz; yanında üç alan daha kilitlenir
   ve **R18** bunları denetler: **veri durumu** (veri zaten var mı, gördün mü —
   görülmüş veriye karşı yazılan kayıt önkayıt değil sonradan-tahmindir),
   **durdurma kuralı** (n ya da toplamayı bitiren koşul; olmadan "geçene kadar
   topla" her zaman mümkündür) ve **dışlama kuralı** (hangi gözlemler düşer,
   görülmeden önce kararlaştırılmış; `yok` cevaptır, sessizlik değil). Açık
   bilim önkayıt şablonları bu üçünü her şeyden önce sorar.
3. **Önce çürütme koşulunu yaz** ve *iki-yönlü bilgilendiricilik*
   şartını kontrol et: her iki olası sonuç da bir şey öğretmeli. Yalnız
   başarı bilgilendiriciyse testi yeniden tasarla.
4. **Bilgilendiricilik önkoşulunu belirt** (gerektiğinde): bir test ancak
   önkoşulları tutmuşsa sayılır (örn. iki varyant da görevi
   öğrenememişse fark-metriği anlamsızdır). "Hücre kapandı: önkoşul
   sağlanmadı" kendi başına bir sonuç türü olarak kaydedilir — `[R]`'den
   farklıdır.
5. **Sürpriz pozitif sonuçlarda:** `[H]→[K]` terfisinden önce, "spesifik
   iddiayı" "jenerik alternatiften" ayıracak simetrik/confound kontrolün
   ne olduğunu sor, o kontrolü alt-girdi olarak önkaydet ve koştur.
   Manşet, kontrolü bekler.
6. **Durum güncellemeleri eklenir, asla üzerine yazılmaz.** Her sonuç
   tarihli bir sonuç bloğu alır. Sonradan akıl yürütmeye izin var ama
   "sonradan akıl yürütme — önkayıtlı değil" diye etiketlenmek zorunda.
7. **Dürüstlük şerhleri her sonuçta zorunludur:** kapsam sınırları,
   örneklem, tek-tohum uyarıları, enstrüman bağımlılığı.
8. **Prior art beyan edilir, hakem tarafından keşfedilmez.** Hipotezin
   bilinen akrabaları varsa girdide adlandırılır ve özgünlük iddiasının
   gerçekte nerede yaşadığı belirtilir.

## Ton ve çerçeveleme kuralları

- Negatif bulgularda doğrudan ol; gerçekten belirsiz değilse "daha fazla
  araştırma gerekiyor" ile yumuşatma.
- Hakkı tam teslim et: bir şey denetimden sağ çıktığında, bunu
  başarısızlıklarda kullanılan aynı özgüllükle söyle. Mizan bir yıkım
  aracı değildir; her iddianın çürüdüğü bir denetim, kendi eşiklerinden
  şüphelendirmelidir.
- Hataları tam konumlandır: hangi iddia, hangi kaynak, hatanın
  mekanizması ne, sayısal etkisi ne — "bu kısımda sorun olabilir" değil.
- Her teşhisin ardından sonraki adımı ver; sıralama:
  kritiklik × (etki / emek).
- Yeni kanıt kendi önceki denetim çıktınla çelişiyorsa, çelişkiyi açıkça
  kabul et ve katmanı revize et. Kendi önceki çıktıların da
  denetlenebilir iddialardır. Düşürmenin yordamı — tarihli, eklenen, yerinde
  düzenlenmeyen — BÖLÜM 4'te RR-11.
- **Boş elle soru sorma.** Belirsizliği, açık seçeneği veya tıkanan adımı
  getiren kendi önerisini ve gerekçesini de getirir: durum, seçenekler, öneri,
  gerekçe, yanılırsa bedeli. Öneriye bir kelimeyle itiraz edilebilir; çıplak
  soru işi, denetimi isteyen kişinin sırtına geri yükler. Karar yine onundur —
  **öneri cevap değildir, cevapsız öneri rıza değildir.**
- Kullanıcının dilinde yaz; katman etiketlerini tablodaki gibi koru.

## Anti-örüntüler (kibarca reddedilir)

- Kaynak kontrolü yapmadan her iddianın `[K]`'ya düştüğü katmanlı bir
  rapor üretmek — bu, laboratuvar önlüğü giymiş pohpohlama sorunudur.
- Sonuca-yakın bir kaçırmayı gördükten sonra eşiğin sessizce
  yükseltilmesine izin vermek. Yakın-kaçırma yakın-kaçırmadır; kaydedilir.
- "Temizlik için" `[R]` girdilerini silmek veya yeniden yazmak.
- Yalnız kontrolü kolay iddiaları denetleyip sonucu tam denetim gibi
  sunmak — kapsam açıkça belirtilir (M iddiadan N'i kontrol edilebilirdi).

---

# BÖLÜM 2 — Şablonlar (references/templates.md karşılığı)

## 2.1 Registry Girdisi şablonu

Girdi, test koşulmadan ÖNCE yazılır. "Prior art" dışında her alan
zorunludur (o da akrabalar biliniyor/şüpheleniliyorsa zorunlu olur).

```markdown
### HX — <kısa hipotez adı> `[H]` `[önkayıt GG-AA-YYYY]`
*(Köken: hipotez nereden geldi — kullanıcı sezgisi, önceki sonuç,
dış öneri. Bir-iki satır.)*

- **Formel:** iddianın kesin, test edilebilir ifadesi.
- **Metrik:** ne ölçülecek ve hangi enstrümanla (dosya, script,
  sorgu, veri kaynağı).
- **Veri durumu:** `not_collected` / `exists_unseen` / `exists_partially_seen`
  / `exists_seen`. **Önce bunu sor.** Veri zaten varsa ve ona baktıysan, kayıt
  önkayıt değildir — sonradan-tahmindir, ve `[önkayıt]` etiketinin iddiası tam
  olarak budur. Dürüst bir `exists_seen` kaydı değerlidir; yalnızca kendine
  önkayıtlı diyemez. (R18)
- **Durdurma kuralı:** n, ya da toplamanın biteceği koşul — şimdi yazılır.
  Olmadan "geçene kadar topla" hep mümkündür ve üstteki eşik hiçbir şeye karar
  vermez. (R18)
- **Dışlama kuralı:** hangi gözlemler hangi kuralla düşer, **görülmeden önce**
  kararlaştırılmış. `yok` geçerli cevaptır; sessizlik değildir. Sonradan icat
  edilmiş bir kuralla nokta atmak, veri temizliği kılığında HARKing'dir. (R18)
- **Eksik veri:** (ölçüm dönmeyebiliyorsa) eksik değer ne sayılır. Bunu
  boşluklar ortaya çıktıktan sonra kararlaştırmak, dışlama kuralının aynı
  hamlesidir, bir adım sonra.
- **Eşik:** sayısal karar kuralı, ŞİMDİ kilitlenir.
  "X ≥ N → destekli; X < M → çürüdü; arası → yetersiz-güçlü, bir tekrar."
- **Çürütme:** hangi sonuç hipotezi öldürür. İki-yönlü bilgilendiricilik
  kontrolü: HER sonucun ne öğreteceğini yaz.
- **Bilgilendiricilik önkoşulu:** (gerektiğinde) testin sayılması için
  neyin tutması gerektiği.
- **Önkayıtlı öngörü:** (opsiyonel ama değerli) yazarın beklentisi,
  sonuçtan önce yazılır. Dürüstçe kaydedilen yanlış tahmin bir
  meziyettir.
- **Prior art:** bilinen akrabalar; özgünlük iddiasının yaşadığı yer.
- **Maliyet:** öncelik sıralaması yapılabilsin diye kaba emek tahmini.
- **DURUM:** ⏳ önkayıtlı, koşulmadı.
```

## 2.2 Sonuç bloğu formatı

Girdiye eklenir; önceki bloklar asla üzerine yazılmaz.

```markdown
- **SONUÇ (GG-AA-YYYY):** ölçülen değerler, aynen.
  Eşik karşılandı mı? EVET/HAYIR/ÖNKOŞUL SAĞLANMADI.
  Karar: `[H]→[K]` / `[H]→[R]` / hücre kapandı (önkoşul) /
  yetersiz-güçlü (bir tekrar hakkı; neyin değişeceğini yaz).
- **Dürüstlük şerhleri:** kapsam sınırları, n, tohumlar, enstrüman
  bağımlılığı — düşman bir hakemin bulacağı her şey.
- **Sonradan akıl yürütme:** (varsa) "önkayıtlı değil" diye açıkça
  etiketlenir.
- **Confound-kontrolü:** (SÜRPRİZ pozitifin `[K]`'ya terfisinden önce
  zorunlu) koşulan simetrik kontrol ve sonucu, veya onu önkaydeden bir
  alt-girdi. Manşet bunu bekler.
- Ham çıktı: <yol veya bağlantı>.
```

## 2.3 Denetim Raporu şablonu

```markdown
# Mizan Denetimi — <belge adı> (GG-AA-YYYY)

## 0. Denetim beyanı
- Kapsam: N atomik iddia çıkarıldı; M'i mevcut kaynaklarla kontrol
  edilebilirdi (kaynak türlerini listele: konuşma geçmişi, dosyalar,
  commit'ler, web).
- HARKing durumu: bu denetim retrospektiftir; kaynak belgedeki örnekler
  sonuçlar bilindikten sonra seçilmiştir ve bu denetimin kendi kapsamı da
  erişilebilir kanıtla sınırlıdır.

## 1. İddia tablosu
| # | İddia (alıntı veya sıkı özet) | Katman | Kaynak / gerekçe (tek satır) |
|---|---|---|---|

## 2. Karşı-örnek taraması
Her örüntü-iddiası için: ne arandı, ne bulundu — boş sonuçlar dahil
("N kaynakta karşı-örnek yok").

## 3. İsabet oranı
Belge birinin yargısını/tahminlerini övdüğü yerlerde: yeniden kurulmuş
TAM sicil — kazançlar VE kayıplar — dürüst oranla.

## 4. Eksik kart
Bu belgenin formatının yapısal olarak gösteremediği şey, mevcut
kanıttan taslaklanmış hali (başarısızlıklar, ertelemeler, terk edilen
hatlar, maliyetler).

## 5. Yapısal teşhis
Belge neden bu yönde çarpık — niyet yerine mekanizma (seçilim baskısı,
format teşvikleri); niyet ancak kanıtlıysa.

## 6. Ayakta kalanlar
Geçen iddialar, başarısızlıklarla aynı özgüllükte. Hiçbir şey
kalmadıysa, denetimin kendi eşiklerini sorgula.

## 7. Sonraki adımlar
Kritiklik × (etki / emek) sırasıyla. Kullanıcı sürekli takip istiyorsa,
sağ kalan [H] iddialarından bir registry ek.
```

## 2.4 Kompakt iddia-satırı formatı

Hızlı satır-içi denetimler için (sohbet yanıtları, belge değil):

```
"<iddia>" → [KATMAN] — tek satır gerekçe (kaynak).
```

Örnek:

```
"Her düzeltme kendi açıklayıcı commit'ini aldı" → [K] — repo geçmişinde
doğrulandı, 14/14 düzeltmenin ayrı commit'i var (github.com/.../commits).
"Kötü sayıyı nedenini söyleyemeden yakalarsın" → [H] — 3 onaylayıcı
örnek bulundu, tahmin sicili eksik; tam isabet oranı proje-kapsamlı
konuşmaları gerektirir (buradan erişilemiyor).
```

## 2.5 Coverage Ledger (fazlı denetimler)

Sıralı fazlara bölünen büyük hedeflerde Mode 3/4/5 için
(`yazilim-modlari.md` §A5.1). Tüm fazlar ve oturumlar arasında paylaşılan
tek append-only tablo. Aynı zamanda denetimin kapsam beyanıdır (A5).

```markdown
# Mizan Coverage Ledger — <hedef> (başlangıç GG-AA-YYYY)

Seçim kuralı: <bölümlemede kullanılan risk-ağırlığı, örn. giriş noktaları
+ para yolları + çalkalanmış dosyalar önce>.
Registry / rapor dosyası: <fazların append ettiği yol>.

| Faz | Dilim (modül / yol / yüzey) | Durum | Kapsam (L'den K fn) | Eklenen bulgular | Tarih |
|---|---|---|---|---|---|
| P0 | yalnız kapsamlama — bölümleme planı | ✅ tamam | — | plan: P1..Pn | GG-AA-YYYY |
| P1 | <dilim> | ✅ tamam | 12/12 | 3×[R] 1×[Y] 5×[KKE] | GG-AA-YYYY |
| P2 | <dilim> | 🔨 sürüyor | 4/? | … | — |
| P3 | <dilim> | ⏳ planlandı | — | — | — |
| MERGE | fazlar-arası uzlaştırma | ⏳ bekliyor | — | tier-drift + dilim-aşan hop | — |

Kapsam iddiası durumu: MERGE koşana dek `[H]`; ancak sonra `[K]`.
```

Kurallar: satırlar eklenir/güncellenir, asla silinmez; yeniden-kapsamlanan
bir dilim düzenleme değil yeni satır alır. Tüm-repo `[K]` kapsam iddiası
MERGE satırı `✅ tamam` olana dek `[H]` kalır — bkz. §A5.1 adım 3.

---

## 2.6 Prob blokları (madde 3.12 ve 3.13'ün kaydı)

Bölüm 2'nin diğer her şablonu birinin **yazdığı** bir şeyi biçimlendirir.
Bu üçünün girdisi metin değildir — alanda yaşanan bir durum, iki özelliğin
kesişimi, ve dışarıda patlayan bir kusur — bu yüzden bir alan istemedikçe
geriye iz bırakmazlar ve koşuldukları, atlandıklarından ayırt edilemez.
Şema 1.8'de `probes` bloğu bunun içindir (R19–R21).

```yaml
probes:
  domain:                          # madde 3.12 — alan probu
    supplied_by: "domain_owner"    # domain_owner | user | third_party | auditor | none
                                   # auditor / none = kendi beyanı; R19 bunun
                                   # üstüne kurulan tier-K kapsam iddiasını reddeder
    supplier_note: "süreci her gün işleten operasyon sorumlusu"
    phase: "P1"
    written_before_work: true      # false = geriye dönük; sakla değil, söyle
    scenarios:
      - id: "DS-01"
        situation: "Aynı adımda iki kişi aynı anda çalışabilir mi?"
        outcome: "finding"         # expressible | boundary_recorded | finding | unchecked
        evidence: "src/steps/claim.py:88 — kilit yok; ikinci yazan eziyor"
        entry_ref: "BUG-H007"
        history:
          - { date: "2026-09-05", event: "senaryo alındı, P1 başlamadan önce" }

  conjunction:                     # madde 3.13 — bileşim pası
    phase: "P1"
    pairs:
      - id: "CJ-01"
        feature: "duraklatma"
        guarantee: "dokunulmamış iş için bayatlama bayrağı"
        order_sensitive: false     # true ise güvenli sırayı required_order'a yaz
        required_order: ""
        outcome: "breaks"          # holds | breaks | unchecked
        evidence: >
          İkisi de tek başına doğru; birlikte duraklatma, tıkanmış işi
          saklamanın ucuz yolu olur ve bayrak gürültüden ölür.
        entry_ref: ""
        history: []

  escaped:                         # RR-13 — kaçak, ve artık onu yakalayan sınıf
    - id: "ESC-01"
      found: "2026-09-05"
      found_by: "user"             # user | production | later_audit | third_party
      symptom: "ikinci imza birincinin üstüne sessizce yazıldı"
      in_scope: true               # denetimin beyan ettiği kapsamın içinde miydi?
      class_ref: "kontrol listesi madde 3.12"
      class_new: ""                # hiçbir sınıf kapsamıyorsa: bir sonraki koşuda
                                   # sorulabilecek soru olarak yazılmış yeni prob
      history:
        - { date: "2026-09-05", event: "kaçak kaydedildi" }
```

**Satırlar eklenir, yeniden yazılmaz (R4).** Yanlış çıkan bir senaryo bir
sonuç alır ve kalır. Tier-K bir kapsam iddiası bu blokları şart koşar; onsuz
yapılan kapsam iddiası alanı değil, dokümanı kapsar.

# BÖLÜM 3 — Hata-Modu Kontrol Listesi (references/checklist.md karşılığı)

Her denetimde bunlar avlanır. Her madde: nedir, nasıl tespit edilir,
kompakt çalışılmış örnek.

## 3.1 HARKing (Sonuçlar Bilindikten Sonra Hipotez Kurma)
- **Nedir:** eşiklerin veya hipotezlerin sonuçlar görüldükten sonra
  seçilip önceden seçilmiş gibi sunulması.
- **Tespit:** "bu başarı kriteri sonuca göre ne zaman yazıldı?" diye sor.
  Belge cevaplayamıyorsa, sonradan varsay.
- **Örnek:** bir inceleme "piramidal mimari kilit bahisti" diyor — ama
  eş-zamanlı kayıtlar beş paralel bahis gösteriyor; kazanan geriye dönük
  olarak "asıl" bahis ilan edilmiş.
- **Not:** retrospektif analiz HARKing'den kaçınamaz; yalnız BEYAN
  edebilir. Günah retrospektiflik değil, sessizliktir.

## 3.2 Seçim yanlılığı / seçilmiş örnekler
- **Nedir:** yalnız onaylayıcı örneklerle desteklenen örüntü-iddiaları.
- **Tespit:** her "hep/tutarlı/güvenilir biçimde" için paydayı iste.
  Çürütücü örnekleri kendin ara.
- **Örnek:** "şüpheli sayıyı üç kez işaretledin" — doğru; tam sicilde
  ayrıca işaretlenip temiz çıkan iki sayı ve işaretlenmeyip asıl bug
  olan bir sayı var. İsabet 3/6, 3/3 değil.

## 3.3 Eksik confound / simetrik kontrol
- **Nedir:** aynı sayıyı üretecek jenerik alternatifi elemeden pozitif
  sonucun spesifik mekanizmaya atfedilmesi.
- **Tespit:** "bu sonucu hangi sıkıcı açıklama üretir?" diye sor ve test
  edilip edilmediğine bak. Edilmediyse `[KKE]` işaretle.
- **Örnek:** girdiye-bağlı faz eklemek perpleksiteyi +%6.75 iyileştirdi →
  manşet "geometri önemli". Simetrik kontrol (aynı ek projeksiyon fazın
  yerine genliğe yönlendirildi) +%16.4 iyileştirdi → kazanç faz değil,
  jenerik girdi-koşullama kapasitesiymiş. Manşet tersine döner.

## 3.4 Formatın kendisindeki survivorship (sağ-kalan yanlılığı)
- **Nedir:** belge türünün başarısızlıkları yapısal olarak temsil
  edememesi (yıl-özeti kartları, öne-çıkanlar, lansman yazıları).
- **Tespit:** bu formatın azami dürüst versiyonu neyi içerirdi de bu
  örnek içermiyor, diye sor. Eksik kartı adlandır.
- **Örnek:** dört-kartlık bir güçlü-yönler özeti; ertelenmiş işler, terk
  edilen hatlar veya sistemi yeniden kurdurtan olay için kart yok — oysa
  bunlar aynı kanıt tabanında eşit derecede karakteristik örüntüler.

## 3.5 Katman kayması (tier drift)
- **Nedir:** bir iddianın kesinliğinin anlatımdan anlatıma sessizce
  tırmanması — laboratuvar defterinde `[S]`, raporda `[H]`, sunumda `[K]`.
- **Tespit:** birden fazla belge varsa aynı iddianın etrafındaki kipleri
  ve çekinceleri karşılaştır (diff'le).
- **Örnek:** "GPT-2 düzeyi performansa karşılık gelebilir" (defter) →
  "GPT-2 düzeyi performans" (özet). Karşılaştırmayı geçersiz kılan
  kelime-hazinesi artefaktı özete hiç girmemiş.

## 3.6 Eşik alışverişi / kale direğini oynatma
- **Nedir:** yakın-kaçırmanın çıta sonradan ayarlanarak yeniden
  yorumlanması.
- **Tespit:** kayıtlı eşiği sonucun etrafındaki dille karşılaştır
  ("esasen karşılandı", "hemen altında", "yön olarak doğru").
- **Kural:** yakın-kaçırma yakın-kaçırma olarak kaydedilir. Değişikliği
  belirtilmiş önkayıtlı BİR tekrar meşrudur; sessiz yeniden-yorum
  değildir.

## 3.7 Kanıt kılığındaki önkoşul-başarısızlığı
- **Nedir:** bilgilendiricilik önkoşulu tutmamış bir testten gelen boş
  veya pozitif sonucun raporlanması.
- **Tespit:** testin etkiyi hiç tespit edip edemeyeceğini kontrol et
  (model görevi öğrendi mi? enstrümanın hassasiyeti var mıydı? örneklem
  dejenere değil miydi?).
- **Örnek:** İKİSİ de görevi öğrenememiş (ikisi de şans düzeyinde) iki
  varyant arasında "fark yok" — hücre "önkoşul sağlanmadı" olarak
  kapanır; hipotez lehine de aleyhine de sayılmaz.

## 3.8 Belirtilmemiş enstrüman-bağımlılığı
- **Nedir:** özne × enstrüman × koşulların özelliği olan bir ölçümün
  öznenin özelliği gibi sunulması.
- **Tespit:** "farklı bir pencere/tokenizer/zaman aralığı/örneklem bu
  sayıyı değiştirir miydi?" diye sor. Makul biçimde evet ise, dürüstlük
  şerhi bunu söylemek zorunda.
- **Örnek:** bir "seçicilik talebi" skoru salt ölçüm penceresi
  değişince 0.139'dan 0.378'e çıktı; ilk sayı tek başına yanlış bir
  hikâye anlatıyordu.

## 3.9 Mekanizmaya kaçak niyet
- **Nedir:** çarpık bir belgeyi yapı yeterliyken (seçilim baskısı,
  teşvikler) niyetle ("manipüle etmek için tasarlanmış") açıklamak.
- **Tespit:** çarpıklık, hiçbir yerinde pohpohlama niyeti olmayan bir
  optimizasyon süreciyle üretilebilir mi? Öyleyse onu söyle; niyet
  iddialarını kanıtlı durumlara sakla.

## 3.10 Denetçinin kendi kör noktası
- **Nedir:** denetimin kendisi de kapsam sınırları ve kendi seçim
  etkileri olan retrospektif bir belgedir.
- **Kural:** her denetim raporu bir kapsam beyanıyla açılır (M iddiadan
  N'i kontrol edilebilirdi, hangi kaynaklar erişilemezdi) ve denetçinin
  önceki çıktılarını da denetlenebilir iddia sayar. Sonraki kanıt daha
  önce verdiğin bir katmanla çeliştiğinde, görünür biçimde revize et.


## 3.11 Üretici-tarafı iddia (erişilemeyen yetenek)
- **Nedir:** iddia doğrudur ve yetenek yoktur. Bir değer tabloya yazılır,
  bir olay yayılır, bir satır loglanır — kullanıcının işlettiği hiçbir yüzey
  onu okumuyorsa teslim edilmiş yetenek yoktur. `[K]` değil `[Y]`: kabul
  kriteri geçti, vaat geçmedi.
- **Tespit:** her "X üretiliyor / kaydediliyor / saklanıyor / yayılıyor"
  için sor: **X'i hangi yüzeyden biri okuyor ve o yüzey koşuldu mu?**
  Yazılımda iki ucuz diff: endpoint listesi ↔ istemcinin gerçekten yaptığı
  çağrılar; tablo listesi ↔ her tablonun okuma yolu. İki paydayı da raporla
  ("61 route'un 57'si erişilebilir, 20 tablonun 17'si okunuyor") — oran,
  istisna mı örüntü mü bulduğunu söyleyen şeydir.
- **Örnek:** *"bildirimler (uygulama içi + e-posta) tamam"* diye kapanan bir
  görev; kriter *"ilgili olay bir bildirim üretir"*. Endpoint'ler ve on iki
  test yerindeydi, ön yüzde tek bir bildirim çağrısı yoktu. Testlerden biri
  `read_all_clears_the_badge` adını taşıyordu — **var olmayan bir rozeti**
  koruyordu. Aynı sınıf o projede dört kez tekrarladı (denetim izi, silme
  ucu, parola değiştirme, bildirimler) ve **dördü de plandan çıkmadı**;
  hepsi tesadüfen fark edildi.
- **Neden incelemeden sağ çıkar:** kabul kriterini üreten katman yazar ve
  **o katman için doğrudur**. Boşluk görevlerin *arasında* yaşar; hiçbir tek
  görevin kendi listesi oraya bakamaz. Backlog'u katmana göre (BE/FE) kesmek
  bu hatayı varsayılan hâline getirir.

## 3.12 Hiç iddia edilmemiş yetenek (model–gerçeklik boşluğu)
- **Nedir:** denetim hiçbir şey bulamaz, çünkü **belgede** bulunacak bir şey
  yoktur. Her iddia tutar, her katman dürüsttür — ve alanda rutin olarak
  yaşanan bir durum sistemde hiç ifade edilemez. **Var olmayan yetenek iddia
  üretmez, iddia denetimi de bu yüzden ona yapısal olarak kördür.** Madde
  3.11 komşusudur ama aynısı değil: orada vaat verilmiş, yarısı teslim
  edilmiştir; burada vaat hiç verilmemiştir, dolayısıyla belgeyi ne kadar
  atomize edersen et yüzeye çıkmaz.
- **Tespit:** bu probun girdisi **alan**, belge değil. Bu alanda gerçekten
  yaşanan durumları listele, her birini modele sor. Üç sonuç: (a) ifade
  edilebiliyor → sorun yok; (b) edilemiyor **ve bilinçli bir sınır olarak
  yazılmış** → sorun yok, bu bir karardır; (c) edilemiyor **ve hiçbir yerde
  yazılı değil** → bulgu. Yazılmamış boşluk, kararlaştırılmış sınırdan her
  zaman kötüdür: kimse onu seçmemiştir.
- **Dürüst kısıt — bu listeyi tek başına üretemezsin.** Denetçi artefaktı
  bilir; alanda ne olduğunu yalnız o alanı bilen bilir. **Sor.** Sormayı
  atlayıp makul görünen senaryolar uyduran denetim, kanıt etiketi takılmış
  kurgu üretiyordur. Senaryoları kimin verdiğini kaydet; bu bilgi kapsam
  beyanının parçasıdır.
- **Sormanın aracı — sekiz sınıflık tohum listesi.** Yukarıdaki kısıt
  geçerli: senaryoları sen yazamazsın. Ama karşındakinin bilgisini yüzeye
  çıkaracak soruları yazabilirsin; "alanınızda hangi durumlar oluyor?" diye
  soğuk sormak güvenilir biçimde hiçbir şey üretmez. Bu sekiz sınıf
  alan-bağımsızdır, çünkü durumu, insanı ve zamanı olan her sistemin
  özelliğidir — ve her biri bu listenin kendi örneklerinde gerçek bir bulgu
  üretmiştir:
  1. **Aynı anda iki kişi** — ikisi aynı şeye aynı anda dokunabilir mi?
     (Sessizce üzerine yazılan ikinci imza.)
  2. **Yaşamın sonu** — bu şey bittiğinde, emekliye ayrıldığında, iptal
     edildiğinde, arşivlendiğinde ne olur? (Hiçbir endpoint'in yazmadığı
     `archived` durumu.)
  3. **Sınır geçişi** — iş iki birim, ekip, departman, kiracı arasında nasıl
     hareket eder? (Modelde karşılığı hiç olmayan devir.)
  4. **Kişi ayrılıyor** — sahibi gittiğinde, izne çıktığında, pasife
     alındığında bunu kim tutar? (Asla dönmeyecek birinin üstlendiği görev.)
  5. **Sıfır, bir, çok fazla** — boş hâl, tek hâl ve on bin. Üçünden
     hangisini kimse denemedi?
  6. **Geri alma ve çıkış** — iptal, silme, veriyi dışarı çıkarma. Çıkışlar
     en son tasarlanır ve işler kötüye gittiğinde ilk kullanılır.
  7. **Sırasız, yarım kalmış** — iki kez yapılan, ters sırada yapılan ya da
     ortasında kesilen adım. Geriye hangi durumu bırakır?
  8. **Kim görebilir** — aynı nesneyi başka bir rol, dışarıdan biri, bir
     denetçi, bir toplu dışa aktarım gördüğünde.
  Liste **sormanın aracıdır, sormanın yerine geçmez**: kanıt, alınan
  cevaplardır; bunları tek başına dolduran denetçi bir bulgu yerine sekiz
  makul kurgu yazmıştır.
- **Örnek:** bir süreç-hafızası uygulaması tam iddia denetiminden geçti (61
  endpoint, 20 tablo, üretici/tüketici diff'i, madde 3.11 taraması).
  On tasarım boşluğu *sonradan* bulundu; hiçbiri o denetimden çıkmadı,
  hepsi alan sahibinin sıradan sorularından: *"aynı adımda iki kişi
  çalışabilir mi?"* (kilit yoktu; ikinci yazan, birincinin imzasını sessizce
  eziyordu), *"iş iki departman arasında nasıl geçiyor?"* (modelde süreç
  başına tek birim vardı, kavram ne kuruldu ne reddedildi), *"süreç emekliye
  ayrılınca ne olur?"* (tanımlı ama hiçbir endpoint'in yazmadığı `archived`
  durumu — arayüz kullanıcıya aktif olarak arşivlemesini söylerken). Denetim
  kendi sınırını doğru da beyan etmişti: *"bilmediğim sınıfları bulamadım ve
  bulamadığımı sayamam."* O beyan doğruydu ve **bir yöntem değildi**.
- **Neden incelemeden sağ çıkar:** diğer her madde birinin yazdığı bir
  cümleden başlar. Bunun başlayacak cümlesi yoktur. Kanıtı bir **yokluk**
  olan tek maddedir; bu yüzden daha dikkatli okumakla değil, **önceden
  hazırlanmış dış bir listeyle** sürülmesi gerekir.
- **Önkayıt kuralı:** boşluk bulunduktan *sonra* yazılan senaryo HARKing'dir
  (madde 3.1) ve kapsam hakkında hiçbir şey kanıtlamaz. Değeri tamamen henüz
  bilinmeyen boşluklardadır; bu yüzden her yeni faz kendi senaryolarını
  **faz başlamadan önce** ekler ve rapor hangilerinin geriye dönük olduğunu
  açıkça söyler.
- **Nereye kaydedilir:** şemadaki `probes.domain` — senaryolar,
  `supplied_by` (denetçi ya da yoksa: kendi beyanı; R19 bunun üzerine
  kurulan tier-K kapsam iddiasını reddeder) ve `written_before_work`.

## 3.13 Denetlenmemiş bileşim (her özellik doğru, çift bozuk)
- **Nedir:** her özellik tek tek doğru, tek tek test edilmiş, tek tek `[K]`
  — ve ikisi **aynı anda** geçerliyken hiçbirinin sahibi olmadığı bir garanti
  kırılıyor. Madde 3.11 ve 3.12 tek bir şey hakkındadır (yarım teslim, ya da
  hiç kurulmamış). Bu ise bir **çift** hakkındadır ve atomize eden her
  prosedüre görünmezdir: atomize etmek tam olarak iddiaları parçalara ayırma
  eylemidir, dolayısıyla yalnızca bileşimde var olan kusur denetimin 1.
  adımında yok edilir.
- **Tespit:** "bu özellik doğru mu?" diye sorma — **"bu özellik hangi mevcut
  garantiye dokunabilir ve o garanti bu özellik etkinken hâlâ geçerli mi?"**
  diye sor. Çift listesini bilerek kur: yeni özellik × dokunabildiği her
  garanti. İki sınıf özellikle kırılgan:
  - **Türetilmiş sinyaller.** Bir yokluktan hesaplanan her şey ("3 gündür
    kimse dokunmadı", "atanmamış", "henüz okunmadı") yeni bir durum
    eklendiği anda sessizce anlam değiştirir.
  - **Tek tek çağrı yerinde uygulanan garantiler.** Beş çağrı yerinde
    doğru uygulanan bir gizlilik kuralı, onu baypas eden altıncı bir yüzeyle
    toptan geçersizleşir — klasiği toplu dışa aktarımdır.
- **Sıra önemlidir.** Bazı bileşimler simetrik değildir: çift bir sırada
  güvenli, diğerinde bozuktur. Gerekli sırayı uygulama detayı olarak değil,
  bulgunun parçası olarak yaz.
- **Örnekler (tek oturum, beş bulgu, hiçbiri iddia denetiminden çıkmadı):**
  *duraklatma × bayatlama sinyali* — işi duraklatmak doğru, dokunulmamış işi
  işaretlemek doğru; birlikte, duraklatma tıkanmış işi saklamanın ucuz yolu
  olur ve bayrak gürültüden ölür. *sessize alma × devir bildirimi* — bildirim
  tercihleri doğru, ekipler arası devir uyarısı doğru; birlikte devir
  susturulabilir ve sistem kimseye haber vermeden başarı raporlar.
  *üstlenme × ayrılma* — görevi üstlenmek doğru, ayrılanı pasife almak doğru;
  birlikte görev asla dönmeyecek birinde kalır ve "meşgul" varsayan bir
  zaman aşımı bunu "gitmiş"ten ayırt edemez. *dışa aktarım × özel notlar* —
  rapor üreteci doğru, not bazında gizlilik doğru; tek düğme diğerini
  geçersiz kılar. *anonimleştirme × açık işler* — ikisi de doğru, ama yalnız
  tek sırada: önce anonimleştir, yeniden atanacak işin sahibi artık
  okunamaz.
- **Neden incelemeden sağ çıkar:** her özelliğin kabul kriterini o özelliğin
  sahibi yazar ve **o özellik için doğrudur**. Kusur iki sahibin arasında
  yaşar; madde 3.11'in bir seviye üstündeki aynı yapısal sebep. Testler
  kusuru miras alır: özellik başına yazıldıkları için yeşil paket parçalar
  hakkında kanıttır ve çift hakkında sessizdir.
- **Geç bulmanın bedeli:** kâğıtta ucuz, kodda pahalı. Bunlar model
  düzeyinde çatışmalardır; tasarımda bulunursa tek karar, sevkten sonra
  bulunursa bir migrasyondur.
- **Nereye kaydedilir:** `probes.conjunction.pairs` (R20). Satır bırakmayan
  bir pas, hiç koşulmamış pastan ayırt edilemez — ve bu pas varsayılan
  olarak atlanır.

> **Numaralandırma notu.** İngilizce `checklist.md` dosyasında madde 10
> üretici-tarafı iddia, madde 11 denetçinin kör noktasıdır; buradaki 3.10 ve
> 3.11 bu ikisinin yeri değişmiş hâlidir. 12 ve 13 iki dilde aynı numarayı
> taşır — kurallar (R19/R20) ve rampalar onlara numarayla atıf yapar.

---

# BÖLÜM 4 — Kurtarma Rampaları (references/recovery.md karşılığı)

Diğer her bölüm yöntemin **çalışan** hâlini anlatır; bu bölüm **bozulan**
hâlini — daha sık olan ve zararın sessizce verildiği hâl. Yumuşatılmış bir
denetim hâlâ denetim gibi görünür; sessizce toparlanmış bir koşu ise hiç
bozulmamış bir koşudan ayırt edilemez. Bu, `[R]` kayıtlarını silmeye yapılan
itirazın denetçiye çevrilmiş hâlidir.

Rampalar `RR-nn` diye adlandırılır: bu projede `R-nn` zaten bir validator
kuralıdır, kurtarma rampası ise kural değildir.

Her rampa aynı biçimde: **DURUM · İLK HAMLE · YASAK · ÇIKTI · DAYANAK.** Son
satır her zaman var olan bir kurala düşer — yalnız düzyazıya yaslanan rampayı
uzun oturum unutur.

| Kod | Durum | Temel kural | Dayanak |
|---|---|---|---|
| **RR-00** | Kendi katmanını onaylamak üzeresin | Geçişi ilan et; hakem `author`, tavan `[KKE]` | Hakem kuralı, üretici/denetçi ayrımı |
| **RR-01** | Söz verilen artifact üretilemedi | Düzyazıyı artifact yerine koyma; kısıtı kapsam beyanına yaz | Kontrol listesi md. 3.11, A5 |
| **RR-02** | Sonuç eşiği tutturamadı | Dörtlü karar: iddia / mekanizma / **enstrüman** / önkoşul — eşiği oynatma | R4, R10, önkoşul kuralı |
| **RR-03** | Sonuç tekrar etmiyor | Deterministikleştir; uyan koşuyu raporlama | Dürüstlük şerhleri, hakem sınıfı |
| **RR-04** | "Düzeltme işe yaradı" ve başka şey de kıpırdadı | Sürpriz pozitif: simetrik kontrol; rakip hipotezleri silme | R15, sürpriz-pozitif kuralı |
| **RR-05** | Karara bağlanamayan iddia | Asgari doğrulama izi; iz yoksa notlu `[H]`, konumlanamıyorsa yazılı kapanış | Denetim adımı 2 |
| **RR-06** | Bulgu artıyor, hiçbiri çürütülmedi | Üretmeyi bırak çürütmeye başla; her şey düştüyse **kendi eşiğinden şüphelen** | W4, ton kuralları |
| **RR-07** | Yalnızca kolay iddialar kontrol edildi | M iddiadan N'i — ve kalan **rastgele mi sistematik mi** | A5, R16 |
| **RR-08** | İddia seti iş ortasında değişti | Hedefi sürümle, yeniden türet; eskiyi yerinde düzenleme | R4, katman kayması |
| **RR-09** | Oturum bulanıklaştı | Registry hafızadır; faz sınırı temiz kesittir | Bağlam ekonomisi, R16, R17 |
| **RR-10** | Belirsizlik / artifact'ler çelişiyor | Varsayma, boş elle sorma; çelişkinin kendisi **bulgudur** | İddia-kanıt sıçraması, katman kayması |
| **RR-11** | Kendi verdiğin katmanı düşürmek | Tarihli düşürme bloğu ekle; eskiyi silme, neyin ona dayandığını yaz | R4, ton kuralı |
| **RR-12** | Eşik tutmadı, optimize etme dürtüsü | Tek değişiklik, **aynı** enstrüman; önce hakeme bak | R10, hakem kuralı |
| **RR-13** | Bir şey kaçtı, yöntem kıpırdamadı | Kaçağı **kaydet**, sonra teşhis et; "hangi kontrol bunu yakalamalıydı?" — varsa `class_ref`, yoksa `class_new` | R21, puan kartındaki *Kaçan* satırı, md. 3.12-3.13 |

**Model hata sınıfları.** Rampalar çare, bunlar hastalık: uydurma · sessiz
boşluk doldurma · bulgu enflasyonu · **eşik tiyatrosu** (hakemi yazar olan ya da
hiç olmayan bir iddiaya kesin görünüşlü sayı iliştirmek — *rigor cosplay*) ·
eşik yumuşatma · kendi çıktısını onaylama · iyimser raporlama · premise esareti
· kolay-iddia yanlılığı · bağlam çürümesi · **sınıfsız kaçak** (hata çıktı, düzeltme girdi, bir sonraki denetimin neye baktığı değişmedi). Model bunları seçmez; hem üretip hem
yargılayan bir tarafın işe yarar görünme baskısı altındaki davranışıdır.

**Kapanış çizelgesi.** Bir denetim veya registry döngüsü kapanınca doldurulur.
Amaç denetimi notlamak değil, **yöntemin nereden sızdırdığını** bulmak:

| Ölçüt | Değer | Okuma |
|---|---|---|
| Atomize / kontrol edilebilir iddia | / | Kapsam oranı, çekince değil sayı olarak. Düşükse bu belge hakkında gerçek bir sonuçtur: doğrulanamayacak biçimde yazılmış. |
| Aday / kayda giren | / | RR-05'ten kaç izlenim geçti. 1.0'a yakınsa hiçbir şey elenmemiş — bulgu enflasyonu. |
| Çürütülen (`[R]`) | | Test edilen kayıtlara oran. **Sıfır uyarıdır, başarı değil:** hiç yanılmamış registry sınanmamış registry'dir. |
| Kapanışta açık `[KKE]` | | Hiç koşmamış kontroller. Denetimin **bilmediği** şey, sessizlik değil sayı olarak. |
| Hakem dağılımı | | `runtime` / `instrument` / `third_party` / `author` / `none`. Son ikisi ağırsa titizlik çoğunlukla biçimdir. |
| Hedef sürümü | | Denetlenen iddia seti kaç kez kıpırdadı (RR-08). Yüksekse yazar hâlâ ne iddia ettiğine karar veriyor. |
| Kullanılan rampalar | | Hangi `RR-nn`. Hiçbiri kullanılmadıysa ya kusursuzdu ya fark edilmedi. |
| **Kaçan** | | Sonradan bulunan, bu denetimin kapsamındaki hata. Dışarıdan gelen ve içeriden manipüle edilemeyen tek ölçü. |

Çizelge de bir iddiadır: denetimi üreten koşu doldurduysa hakem sınıfı `author`
olur ve kalıcı bir `[KKE]` taşır. Tablonun biçimi aksini ima etmesin diye bunu
yaz.
