# Mizan — Kanıt-Katmanlı Denetim ve Önkayıt Registry'si
## Türkçe Tam Dokümantasyon (SKILL.md + Şablonlar + Kontrol Listesi)

> Bu belge, `mizan.skill` paketinin içindeki üç dosyanın birebir Türkçe
> karşılığıdır. Skill'in kendisi İngilizce çalışır (taşınabilirlik için)
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
7. **HARKing durumunu beyan et.** Retrospektif analiz örneklerini
   sonuçları gördükten sonra seçmiştir. Bunu rapor başlığında açıkça
   söyle — denetimin kendisi de retrospektif olduğu için kendi durumunu
   da dahil ederek.
8. **Mekanizmayı niyetten ayır.** Bir belgenin neden çarpık olduğunu
   açıklarken yapısal açıklamaları (seçilim baskısı, format teşvikleri)
   niyet atfına ("pohpohlamak için tasarlamışlar") tercih et — niyet
   ancak kendisi kanıtlıysa iddia edilir.

## Registry modu — prosedür

1. **Her hipoteze bir girdi** (Bölüm 2'deki şablonla). Girdi test
   koşulmadan ÖNCE yazılır.
2. **Eşikleri sayısal kilitle.** "İyileştirir" eşik değildir;
   "ΔPPL ≤ −%3" veya "10 kaynakta 1'den az karşı-örnek" eşiktir.
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
  denetlenebilir iddialardır.
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

---

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
