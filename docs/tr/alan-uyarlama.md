# Mizan — Alan Uyarlama: Mod 3/4/5 Yazılımın Ötesinde
## Türkçe Dokümantasyon Eki (references/domain-adaptation.md karşılığı)

Mod 3, 4 ve 5 üç evrensel örüntünün yazılım kılığıdır:

- **Mod 3 (denetim):** iddia taşıyan artefakt asla davranış taşıyan
  artefakt değildir — aradaki her sıçramayı doğrula.
- **Mod 4 (anomali registry'si):** anomali → mekanizma hipotezi →
  rakip hipotezler → ayırt edici test. Uyan ilk hikâyede kapanma.
- **Mod 5 (taahhüt kapısı):** ileriye dönük her kaynak taahhüdü
  değer/maliyet/bağımlılık iddiaları taşır — katmanla, eşiği ve
  kaldırma koşulunu taahhütten ÖNCE kilitle, alternatifleri (null
  dahil) zorla.

## Uyarlama reçetesi (listede olmayan her alan için)

Altı soruyu cevapla; cevaplar alan-modülünün kendisidir. 0. soru,
yazılımdaki doğrulama döngüsünün ne kadarının taşınmadan sağ çıktığını
belirleyen sorudur:

0. **Hakem:** bu alanda kilitli bir eşiğin hükmünü kim veriyor —
   deterministik bir yürütücü, bağımsız bir enstrüman, üçüncü bir taraf,
   yoksa iddianın kendi yazarı mı? Yazılımın titizliği artefaktın kod
   olmasından değil, runtime'dan ödünç alınmıştır; çoğu alan protokolü
   devralır ve hakemi kaybeder. Her girdi için dürüstçe cevapla (şema
   alanı `hypothesis.arbiter`, kural R8): `author` iddiayı kalıcı
   [KKE]'de tavanlar, `none` eşiğin dekoratif olduğu ve girdinin [S]'de
   kaldığı anlamına gelir. Bütün hakemleri `author` olan bir alan bu
   yüzden denetlenemez değildir — yalnızca [K] üretemez, ve bunu söylemek
   işin ta kendisidir.

1. **Sıçrama haritası:** iddialar nerede, kanıt nerede yaşıyor?
   (Kodda: yorum vs implementasyon. Satışta: CRM alanı vs aktivite logu.)
2. **Enstrümanlar:** sayıları ne üretiyor, bilinen çarpıtmaları ne?
3. **Confound kataloğu:** bu alanda aynı sonucu hangi sıkıcı açıklama üretir?
4. **Zemin-gerçek gecikmesi:** bir iddia ne hızda ve ne ucuza çürütülür?
   (Kodda saniyeler; pazarlamada çeyrekler.) Yavaş alanlarda
   "yetersiz-güçlü" istisna değil NORMDUR — beklentiyi buna göre kur.
5. **Prior art:** bu alanda hangi mevcut disiplin zaten bunun gevşek
   versiyonu? (Girdilerde adlandır; Mizan formalize eder, nadiren icat eder.)

Değişmeden taşınan evrensel kurallar: append-only geçmiş; çürüyen
girdiler silinmez; sürpriz pozitifler simetrik kontrolü bekler; simetrik
kontrolün etik/pratik olarak kurulamadığı (insan-özneli) alanlarda iddia
KALICI [KKE] etiketi taşır — bu kusur değil, dürüstlük etiketidir.
**DC-001, bireysel isabet oranının silaha dönüşebileceği her yerde
geçerlidir** (satış forecast'i, analist tahminleri, işe-alım kararları):
bireysel skor kişide kalır, yönetim yalnız agregayı görür.

## Alan kataloğu

Her girdi 0. ve 4. soruyu tek satırda cevaplar, **Hakem / gecikme**;
çünkü bu ikisi, daha hiçbir eşik yazılmadan girdinin tavanını belirler:
`author` hakemi kalıcı [KKE]'de tavanlar (R8), çeyrekler ya da yıllar
süren bir gecikme "yetersiz-güçlü"yü beklenen sonuç yapar. Bir alanda iki
tür iddia için iki ayrı hakem varsa ikisi de adlandırılır — o ayrım
genellikle satırın söylediği en yararlı şeydir.

### 1. Veri ve Analitik
- Sıçrama: metrik etiketi / dashboard başlığı / rapor anlatısı ↔ gerçek
  sorgu (SQL/pipeline) ↔ ham veri. Grafikteki "aktif kullanıcı" vs
  WHERE koşulunun gerçekte saydığı.
- Mod 4 = metrik-anomali soruşturması: her düşüş/sıçrama için rakip
  hipotezler — tracking değişikliği, mevsimsellik, karışım kayması
  (Simpson paradoksu), gerçek etki.
- Confound'lar: enstrümantasyon değişimleri, backfill'ler, zaman
  dilimi/pencere tanımları, kohortlarda survivorship.
- Prior art: veri-kalite testleri (dbt testleri ≈ iddia assert'leri).
- Hakem / gecikme: "sorgu etiketin dediğini mi sayıyor" için `runtime` —
  yeniden çalıştır, [K] erişilebilir; bir anomalinin nedeni için
  `instrument`. Dakikalar ile günler arası.

### 2. Pazarlama ve Büyüme
- Sıçrama: kampanya brief'i / landing-page vaadi ↔ ürünün gerçek
  davranışı; kitle iddiaları ↔ anket/telemetri kanıtı.
- Mod 5 = kampanya kapısı: CAC/dönüşüm eşiği lansman öncesi kilitli;
  harcama tavanı = kaldırma koşulu; null alternatif ("hiç yapmasak")
  fiyatlanır.
- Confound'lar: yenilik etkisi, mevsimsellik, kardeş kanalların
  yamyamlaştırılması, erken bakma/peeking (erken durdurma = R1 ihlali).
- Prior art: düzgün A/B metodolojisi ZATEN önkayıttır; [Y] etiketi
  pazarlama metni için icat edilmiş gibidir.
- Hakem / gecikme: dönüşüm iddiaları için `instrument` (deney
  platformu, analitik); konumlandırma ve marka iddiaları için `author`,
  bu yüzden kalıcı [KKE] taşırlar. Haftalar ile çeyrekler arası —
  atıf pencereleri çoğu kapanışı yetersiz-güçlü kılar.

### 3. Satış ve CRM
- Sıçrama: pipeline-aşaması alanı / "champion belirlendi" iddiası ↔
  aktivite logu, alıcı-tarafı artefaktları (e-postalar, toplantılar).
- Mod 5 = deal-kalifikasyon kapısı (MEDDIC/BANT = gevşek prior art);
  diskalifikasyon kriterleri = kaldırma koşulu; kapanış olasılığı =
  önkayıtlı öngörü.
- Mod 4 = kayıp analizi: satıcının sonradan-hikâyesi vs alıcının
  beyan ettiği sebepler vs rakip mekanizmalar.
- Confound'lar: çeyrek-sonu baskısı, iskonto etkileri, tek-kişiye-bağlı
  temasın konsensüs gibi görünmesi. DC-001 kültürel olarak en zor burada.
- Hakem / gecikme: bir forecast için `instrument` (CRM'de kazanıldı /
  kaybedildi); satıcının kendi kayıp hikâyesi `author`'dır ve onu yalnız
  alıcı-tarafı kanıt (`third_party`) yükseltir. Bir satış döngüsü —
  haftalar ile aylar arası.

### 4. Akademik / Bilimsel Araştırma
- Doğal habitat — Mod 1/2 buradan geldi. Gerçekten yeni transfer,
  Mod 3'ün literatüre uygulanması: abstract iddiaları ↔ methods/results
  kanıtı (abstract-şişmesi belgelenmiş tier drift'tir), atıf iddiaları ↔
  atıf verilen makalenin gerçekte gösterdiği.
- Confound'lar: yayın yanlılığı, çatallanan yollar bahçesi (garden of
  forking paths), tekrarlamada ortalamaya dönen küçük-örneklem etkileri,
  birincil çalışma yerine onu özetleyen derlemeye atıf.
- Prior art: önkayıt, registered reports, PRISMA.
- Hakem / gecikme: bir atıf sıçraması için enstrüman, atıf verilen
  makaleyi okumaktır — herkes yapabilir, [K] saatler içinde
  erişilebilir; bir bulgu için `third_party` tekrarlama, yıllar içinde.

### 5. Finans ve Yatırım Kararları
- Sıçrama: yatırım tezi ↔ pozisyon; "X'e inanıyoruz çünkü Y" ↔ Y
  verisinin gerçekte gösterdiği.
- Mod 5 = pozisyon kapısı: çürütme koşullu giriş tezi
  (tez-geçersizleşmesi ≠ fiyat stop-loss'u — ikisi de kaydedilir),
  pozisyon büyüklüğü = maliyet iddiası.
- Confound'lar: alfa kılığında piyasa betası, rejim şansı,
  backtest'lerde survivorship, geçmişe aşırı-uyum.
- Prior art: yatırım memoları + pre-mortem'ler; trade günlükleri
  gayriresmî Mod 4 registry'leridir.
- Not: Mizan akıl yürütmeyi yapılandırır; finansal tavsiye makinesi
  değildir, işlem seçmez.
- Hakem / gecikme: tezin operasyonel kilometre taşları için
  `instrument` (açıklanan finansallar). Fiyat tezin hakemi DEĞİLDİR:
  tezin iddia etmediği sebeplerle hareket eder, bu yüzden tek başına bir
  fiyat hareketi tezi ne doğrular ne çürütür. Kilometre taşları için
  çeyrekler; bir strateji iddiası için tam bir rejim.

### 6. Operasyon / İmalat / Lojistik
- Mod 4 = kök-neden analizinin formalize hali: 5-Neden zincirleri,
  rakip hipotezleri ve ayırt edici testleri genelde atlayan mekanizma
  hipotezleridir — Mizan tam o eksikleri ekler. Süreç değişikliği
  sonrası "düzeltme çalıştı", uygulanabildiği yerde geri-al-kontrolüne
  tabidir.
- Mod 3: SOP/iş-talimatı iddiaları ↔ sahada gerçekten yapılan.
- Confound'lar: Hawthorne etkisi (gözlem davranışı değiştirir),
  eşzamanlı değişiklikler, talep karışımı.
- Prior art: A3/8D raporları, Six Sigma DMAIC.
- Hakem / gecikme: `instrument` (hata sayıları, çevrim süreleri);
  uygulanabilir bir geri-al-kontrolü hükmü neredeyse `runtime` yapar.
  Bir vardiya ile birkaç hafta arası.

### 7. Güvenlik ve Olay Müdahalesi
- Mod 4 olay müdahalesiyle neredeyse izomorf: semptom (alarm/IOC) →
  sızma hipotezi → rakipler (yanlış yapılandırma? tarayıcı gürültüsü?
  gerçek ihlal?) → ayırt edici kanıt. Olay-sonrası raporlar HARKing
  mıknatısıdır — zaman çizelgesi iddiaları artefakt atfı ister.
- Mod 3: güvenlik-duruşu iddiaları (dokümanlar, uyumluluk cevapları) ↔
  gerçek config'ler ve kontroller.
- Prior art: blameless postmortem (= DC-001'in atası), ATT&CK hipotez avı.
- Hakem / gecikme: bir yapılandırma iddiası için `runtime` — config'i
  oku, kontrolü çalıştır. "İhlal yok" için geçti hükmü verebilecek bir
  hakem yoktur: sessizlik [KKE]'de tavanlanır (R26). Bir olay yerine
  varlık-merkezli bir tarama için Mod 7'yi kullan
  (`security-probe.md`). Config için dakikalar; sızmanın içeride kalma
  süresi aylarla ölçülür.

### 8. İşe Alım ve İnsan Kararları
- Sıçrama: iş tanımı ve değerlendirme formu iddiaları ("güçlü sistem
  düşünürü") ↔ onları üreten kanıt (iş örneği, mülakat cevabının
  kendisi, referanslar).
- Mod 5 = işe-alım kapısı: rolün problem iddiası, 90-gün başarı
  metriği teklif öncesi kilitli, öncüller çökerse ROL için (kişi için
  değil) kaldırma koşulu.
- Mülakat sinyalleri = hipotezler; mülakatçı-başına önkayıtlı
  öngörüler, çok sayıda işe alım üzerinden kalibrasyonu ölçülebilir kılar.
- Confound'lar: halo etkisi, piyasa koşulları, onboarding kalitesinin
  seçim kalitesiyle karışması.
- SERT kısıt: DC-001 tam geçerli; mülakatçı-başına isabet oranı asla
  performans silahı olmaz. İnsan-özneli simetrik kontrol çoğunlukla
  imkânsız → kalıcı [KKE] etiketleri burada normaldir.
- Prior art: yapılandırılmış mülakat, iş-örneği testleri.
- Hakem / gecikme: neredeyse her zaman `author` ya da `third_party`
  olarak bir yönetici; 90 günlük bir metrik nadiren enstrümandır → [K]
  neredeyse erişilemez, bunu söyle. 90 gün ile bir yıl arası, küçük n
  ile.

### 9. Tedarik ve Satıcı Seçimi
- Mod 3: satıcı iddiaları (SLA, benchmark sunumları, "enterprise-ready")
  ↔ sözleşme maddeleri ↔ POC'de ölçülen davranış. Satıcı benchmark'ları
  yeniden-üretilene kadar [Y]'dir.
- Mod 5 = RFP kapısı: gereksinimler katmanlı iddialar olarak;
  bağımlılık iddiaları ("stack'imizle entegre olur") imzadan ÖNCE
  doğrulanır; çıkış/geçiş maliyeti kaldırma-koşulu ekonomisi olarak
  kaydedilir.
- Confound'lar: demo-ortamı vs üretim, referans-müşteri seçim yanlılığı.
- Prior art: POC karşılaştırmaları (bake-off), ağırlıklı puanlama
  matrisleri.
- Hakem / gecikme: `instrument` (POC ölçümü), ancak POC imzadan önce
  tasarlandıysa; satıcının kendi benchmark'ı `author` olarak satıcının
  kendisidir. POC için haftalar; gerçek SLA davranışı için aylar.

### 10. Hukuk / Sözleşmeler / Uyumluluk
- Mod 3: politika/uyumluluk iddiaları ("GDPR-uyumluyuz") ↔ gerçek
  maddeler, gerçek veri akışları; pazarlama vaatleri ↔ sözleşmesel
  yükümlülükler (sözleşmede olmayan vaat en iyi ihtimalle [H]'dir).
- Mod 4: uyuşmazlık analizi — tarafların anlatıları, belge kaydına
  karşı rakip hipotezler olarak.
- Confound'lar: seçici belge sunumu, her tarafın anlatısını biçimlendiren
  geriye dönük bakış, bağlı olduğu tanımlar olmadan okunan bir madde.
- Prior art: hukuki durum tespiti (due diligence); uyumluluk
  denetimlerinde kontrol testi (SOC 2, ISO 27001).
- Hakem / gecikme: maddeleri gerçek veri akışlarına karşı okumak Mod 3
  için enstrüman benzeridir; gerçek `third_party` (mahkeme, düzenleyici,
  denetçi) genellikle ancak bir uyuşmazlıkla gelir. Belge kontrolü için
  günler; uyuşmazlık için yıllar.
- Not: kanıtı yapılandırır; hukuki tavsiye değildir.

### 11. Ürün / UX Araştırması
- Mod 3: "kullanıcılar X istiyor" iddiaları ↔ görüşme transkriptleri
  (gerçekte söylenen vs özet — özetleme sapması tier drift'tir);
  kullanılabilirlik-raporu iddiaları ↔ oturum kayıtları.
- Confound'lar: yönlendirici sorular, sesli-azınlığa kayan örneklem,
  söylem-eylem boşluğu (beyan edilen tercih vs davranış).
- Prior art: continuous discovery pratikleri, kanıta dayalı tasarım.
- Hakem / gecikme: `instrument` (görev başarısı, davranışsal telemetri)
  ya da `third_party` olarak moderasyonlu oturumlar; araştırmacının
  sentezi `author`'dır. Oturumlar için günler; telemetri için haftalar.
  Araştırma iddialarını değil bir uygulamanın UX'ini denetlemek için
  tam prosedürü kardeş skill ux-mizan taşır.

### 12. İçerik / Gazetecilik / Teknik Yazarlık
- Mod 3: başlık ↔ gövde ↔ kaynak (başlık şişmesi = tier drift); her
  olgu iddiasının birincil kaynağa sıçraması.
- Mod 5 = içerik kapısı: kitle-değeri iddiası, dağıtım bağımlılık
  iddiaları, kalıcı-mı-söner-mi beklentisi önkayıtlı öngörü olarak.
- Confound'lar: aynı ajans haberini aktaran iki yayının iki kaynak
  sayılması, "ne iyi performans gösterdi"de survivorship, kitle tercihi
  sanılan bir platform algoritması değişikliği.
- Prior art: doğrulama masaları; [Y] ve [KKE] editoryal standartlara
  doğrudan oturur.
- Hakem / gecikme: bir olgu iddiası için `third_party` olarak birincil
  kaynak — [K] saatler içinde erişilebilir; bir içerik-değeri öngörüsü
  için `instrument` (analitik), haftalar boyunca.

### 13. Politika / Program Değerlendirme (kamu, STK)
- Sıçrama: program raporları (yürütülen faaliyetler — çıktılar) ↔ o
  faaliyetlerin hareket ettirmesi beklenen sonuç verisi. Çıktı sonuç
  değildir; birincisini sayan bir rapor ikincisi hakkında sessizdir.
- Mod 5 = program kapısı: değişim-teorisi katmanlı iddia zinciri
  olarak; sunset maddesi = kaldırma koşulu (pratikte nadir,
  önkaydedildiğinde dönüştürücü).
- Confound'lar: programa seçilim, seküler eğilimler, hedeflenmiş
  gruplarda ortalamaya dönüş.
- Hakem / gecikme: `third_party` olarak bağımsız bir değerlendirici,
  idari veri olan yerde `instrument`; uygulayıcı kurumun kendini
  değerlendirmesi `author`'dır. Yıllar — yetersiz-güçlü normdur; her
  girdide bunu söyle.
- Prior art: RCT değerlendirme kültürü, mantık modelleri.

### 14. Kişisel Deneyler (sağlık, fitness, üretkenlik)
- Sıçrama: hissedilen iyileşme ya da günlük kaydı ↔ ölçülen değer
  (giyilebilir cihaz, laboratuvar sonucu, kaydedilmiş çıktı) — aradaki
  fark, görünür hale gelmiş beklenti confound'udur.
- Mod 4, n=1 üzerinde: semptom → mekanizma hipotezi → en ucuz ayırt
  edici değişiklik, TEK seferde tek değişken; washout dönemleri kişisel
  simetrik kontrol olarak.
- Confound'lar: plasebo/beklenti, ortalamaya dönüş (müdahaleye en kötü
  anında başlarsın), mevsim/uyku/stres birlikte-hareketi.
- Kalıcı dürüstlük etiketi: n=1, çoğu kapanışı [H]'de tavanlar — bu
  başarısızlık değil, dürüst tavandır.
- Prior art: quantified-self pratiği, klinik araştırmada n-of-1
  denemeleri.
- Hakem / gecikme: özne aynı zamanda `author`'dır, bu yüzden kapanışlar
  [H] ya da [KKE]'de kalır; bir `instrument` (giyilebilir cihaz,
  laboratuvar testi) ölçtüğü şeyi yükseltir, hissedilen iddiayı değil.
  Döngü başına günler ile haftalar, washout dahil.
- Not: öz-gözlemi yapılandırır; tıbbi kararlar klinisyenlere aittir.

## Bu dosyanın anti-örüntüsü

Beş kapı-alanını, kendilerini parodiye çevirdikleri alanlara zorla
giydirme. Bir girdinin kaldırma koşulu veya metriği tiyatral
duruyorsa dürüst versiyonu kaydet: "güvenilir enstrüman yok → iddia
[S]'de kalır" meşru ve yararlı bir sonuçtur.
