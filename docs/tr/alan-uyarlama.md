# Mizan — Alan Uyarlama: Mod 3/4/5 Yazılımın Ötesinde
## Türkçe Dokümantasyon Eki (references/domain-adaptation.md karşılığı, v2.2)

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

Beş soruyu cevapla; cevaplar alan-modülünün kendisidir:

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

### 4. Akademik / Bilimsel Araştırma
- Doğal habitat — Mod 1/2 buradan geldi. Gerçekten yeni transfer,
  Mod 3'ün literatüre uygulanması: abstract iddiaları ↔ methods/results
  kanıtı (abstract-şişmesi belgelenmiş tier drift'tir), atıf iddiaları ↔
  atıf verilen makalenin gerçekte gösterdiği.
- Prior art: önkayıt, registered reports, PRISMA.

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

### 7. Güvenlik ve Olay Müdahalesi
- Mod 4 olay müdahalesiyle neredeyse izomorf: semptom (alarm/IOC) →
  sızma hipotezi → rakipler (yanlış yapılandırma? tarayıcı gürültüsü?
  gerçek ihlal?) → ayırt edici kanıt. Olay-sonrası raporlar HARKing
  mıknatısıdır — zaman çizelgesi iddiaları artefakt atfı ister.
- Mod 3: güvenlik-duruşu iddiaları (dokümanlar, uyumluluk cevapları) ↔
  gerçek config'ler ve kontroller.
- Prior art: blameless postmortem (= DC-001'in atası), ATT&CK hipotez avı.

### 8. İşe Alım ve İnsan Kararları
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

### 9. Tedarik ve Satıcı Seçimi
- Mod 3: satıcı iddiaları (SLA, benchmark sunumları, "enterprise-ready")
  ↔ sözleşme maddeleri ↔ POC'de ölçülen davranış. Satıcı benchmark'ları
  yeniden-üretilene kadar [Y]'dir.
- Mod 5 = RFP kapısı: gereksinimler katmanlı iddialar olarak;
  bağımlılık iddiaları ("stack'imizle entegre olur") imzadan ÖNCE
  doğrulanır; çıkış/geçiş maliyeti kaldırma-koşulu ekonomisi olarak
  kaydedilir.
- Confound'lar: demo-ortamı vs üretim, referans-müşteri seçim yanlılığı.

### 10. Hukuk / Sözleşmeler / Uyumluluk
- Mod 3: politika/uyumluluk iddiaları ("GDPR-uyumluyuz") ↔ gerçek
  maddeler, gerçek veri akışları; pazarlama vaatleri ↔ sözleşmesel
  yükümlülükler (sözleşmede olmayan vaat en iyi ihtimalle [H]'dir).
- Mod 4: uyuşmazlık analizi — tarafların anlatıları, belge kaydına
  karşı rakip hipotezler olarak.
- Not: kanıtı yapılandırır; hukuki tavsiye değildir.

### 11. Ürün / UX Araştırması
- Mod 3: "kullanıcılar X istiyor" iddiaları ↔ görüşme transkriptleri
  (gerçekte söylenen vs özet — özetleme sapması tier drift'tir);
  kullanılabilirlik-raporu iddiaları ↔ oturum kayıtları.
- Confound'lar: yönlendirici sorular, sesli-azınlığa kayan örneklem,
  söylem-eylem boşluğu (beyan edilen tercih vs davranış).
- Prior art: continuous discovery pratikleri, kanıta dayalı tasarım.

### 12. İçerik / Gazetecilik / Teknik Yazarlık
- Mod 3: başlık ↔ gövde ↔ kaynak (başlık şişmesi = tier drift); her
  olgu iddiasının birincil kaynağa sıçraması.
- Mod 5 = içerik kapısı: kitle-değeri iddiası, dağıtım bağımlılık
  iddiaları, kalıcı-mı-söner-mi beklentisi önkayıtlı öngörü olarak.
- Prior art: doğrulama masaları; [Y] ve [KKE] editoryal standartlara
  doğrudan oturur.

### 13. Politika / Program Değerlendirme (kamu, STK)
- Mod 5 = program kapısı: değişim-teorisi katmanlı iddia zinciri
  olarak; sunset maddesi = kaldırma koşulu (pratikte nadir,
  önkaydedildiğinde dönüştürücü).
- Confound'lar: programa seçilim, seküler eğilimler, hedeflenmiş
  gruplarda ortalamaya dönüş.
- Zemin-gerçek gecikmesi: yıllar — yetersiz-güçlü normdur; her girdide
  bunu söyle.
- Prior art: RCT değerlendirme kültürü, mantık modelleri.

### 14. Kişisel Deneyler (sağlık, fitness, üretkenlik)
- Mod 4, n=1 üzerinde: semptom → mekanizma hipotezi → en ucuz ayırt
  edici değişiklik, TEK seferde tek değişken; washout dönemleri kişisel
  simetrik kontrol olarak.
- Confound'lar: plasebo/beklenti, ortalamaya dönüş (müdahaleye en kötü
  anında başlarsın), mevsim/uyku/stres birlikte-hareketi.
- Kalıcı dürüstlük etiketi: n=1, çoğu kapanışı [H]'de tavanlar — bu
  başarısızlık değil, dürüst tavandır.
- Not: öz-gözlemi yapılandırır; tıbbi kararlar klinisyenlere aittir.

## Bu dosyanın anti-örüntüsü

Beş kapı-alanını, kendilerini parodiye çevirdikleri alanlara zorla
giydirme. Bir girdinin kaldırma koşulu veya metriği tiyatral
duruyorsa dürüst versiyonu kaydet: "güvenilir enstrüman yok → iddia
[S]'de kalır" meşru ve yararlı bir sonuçtur.
