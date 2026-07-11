# Mizan — Ek Bölümler: Yazılım Modları (Mod 3–5)
## Türkçe Dokümantasyon Eki (code-audit.md + feature-gate.md karşılığı)

> Bu ek, ana Türkçe dokümantasyonun (Mizan_TR_Dokumantasyon.md) devamıdır.
> Skill'in v2 paketine eklenen iki referans dosyasının birebir karşılığı.

**Yapısal fark:** Kod tabanında iddia ile kanıtı FARKLI artefaktlarda
yaşar (ad / yorum / docstring / test / implementasyon) ve aralarındaki
her sıçrama ayrı doğrulanmak zorundadır. Yorumun var olduğunu doğrulamak,
iddiasının doğru olduğunu doğrulamak değildir.

---

# BÖLÜM 4 — Kod Denetimi ve Bug-Hipotez Registry'si (Mod 3–4)

## A Kısmı — Kod denetimi (Mod 3)

### A1. İddia envanteri — kodda iddialar nerede yaşar

Kanıt ağırlığı sırasıyla:

1. **Testler** — en güçlü iddia kaynağı. Her assert, (genellikle) sonuç
   görülmeden kilitlenmiş bir eşiktir: zaten var olan bir önkayıt
   registry'si. Dokümantasyon yoksa İLK okunacak şey test paketidir.
2. **İmplementasyona bitişik metin** — yorumlar, docstring'ler. Bunlar
   davranış iddia eder; kanıt implementasyondur. Sıçramayı doğrula.
3. **Adlar** — fonksiyon/sınıf/değişken adları birer vaattir
   (`validate_input`, `sanitize`, `cache`, `thread_safe`).
4. **Dış dokümanlar** — README, wiki, PRD'ler, commit mesajları. Koddan
   en uzak; sapma riski en yüksek.
5. **Yapı** — config değerleri, type hint'ler, hata mesajları, bağımlılık
   pinleri (bir pin, uyumluluk iddia eder).

### A2. Kod iddiaları için katman eşlemesi

| Katman | Koddaki anlamı |
|---|---|
| `[K]` | İddiayı, gerçekten başarısız olabilen geçer bir test destekliyor (bkz. A4) veya implementasyon/çalıştırmayla doğrudan doğrulandı |
| `[H]` | İddia ad/yorum/dokümanda var; kapsayan test yok; implementasyon çelişmiyor ama doğrulamıyor da |
| `[KKE]` | Test var ama iddiayı çürütebilecek kenarı kapsamıyor (derinliği hiç test etmeyen bir "deep discovery" testi) |
| `[Y]` | Ad/doküman, kodun teslim ettiğinden fazlasını vaat ediyor (yalnız whitespace kırpan bir `sanitize`) |
| `[R]` | İmplementasyon iddiayla doğrudan çelişiyor (sınırsız `rglob` üzerindeki "2 seviye derinlik" yorumu) |

**Sıçrama kuralı:** Yorumun varlığı ≠ davranışın varlığı. Docstring ≠
test. Test adı ≠ test içeriği. Her sıçramayı ayrı katmanla; bir iddianın
katmanı, doğrulanmış EN ZAYIF sıçramasının katmanıdır.

### A3. Sapma kataloğu (kontrol listesi maddelerinin kod versiyonları)

- **Yorum–kod sapması** = tier drift: yorum eski veya niyetlenilen
  implementasyonu anlatıyordu; kod değişti, yorum kalmadı. Tespit:
  yorumun ve altındaki kodun `git log -L` geçmişini karşılaştır — kod,
  yorumun son dokunuşundan sonra değiştiyse işaretle.
- **TODO/FIXME envanteri** = kayıtsız ertelemeler. Hepsini çıkar,
  `git blame` ile tarihle, Boşluk Haritası'na koy. İki yaşındaki TODO
  plan değil, erteleme örüntüsüdür.
- **Ölü kod** = terk edilmiş `[S]` girdileri. Referanssız fonksiyonlar,
  ulaşılamaz dallar, hiç açılmamış feature flag'ler.
- **Doküman–kod sapması:** README iddiaları vs gerçek CLI bayrakları /
  API yüzeyi.

### A4. Test-kalite denetimi — `[K]`'nın confound-kontrolü

Başarısız olamayan test dekorasyondur (iki-yönlü bilgilendiriciliğin
test paketlerine uygulanışı). Bir iddiayı bir teste dayanarak `[K]`'ya
terfi ettirmeden önce:

- Assert'ün iddia edilen davranışı gerçekten çalıştırdığını kontrol et
  ("fonksiyon exception atmadan koştu" yetmez).
- Mümkünse **mutation testing** kullan (mutmut, cosmic-ray, Stryker) —
  sistematik kontrol budur: implementasyonu mutasyona uğratmak testi
  öldürmüyorsa, test o iddiayı korumuyormuş.
- Ucuz manuel versiyon: iddia edilen davranışı yerelde bilerek boz;
  paket yeşil kalıyorsa `[K]` sahteymiş — `[KKE]` işaretle.

### A5. Ölçek, örnekleme ve kapsam beyanı

Küçük kod tabanları dışında tam atomizasyon imkânsızdır. Zorunlu pratik:

- Kapsamı baştan beyan et: hangi modüller/yollar, hangi seçim kuralıyla
  (risk-ağırlıklı: giriş noktaları, güvenlik yüzeyleri, para yolları,
  `git log --stat` ile yakın-zamanda-çalkalanmış dosyalar).
- Kapsamı raporla: "M modülden N'i, L public fonksiyondan K'sı."
- Örneklenmiş denetimi asla tam denetim gibi sunma.

### A6. Çıktılar

1. **Kanıt-katmanlı davranış raporu** — her cümle bir katman ve kaynak
   taşır (dosya:satır, test adı veya koşum çıktısı). Projenin
   dokümantasyonu yoksa bu rapor dokümantasyonun KENDİSİ olur — her
   cümlesi temenni yerine `[K]`/`[H]` etiketi taşıyan üretilmiş doküman.
2. **Boşluk Haritası (Gap Map)** — kodun eksik-kart analizi:
   - `[R]` bulguları → bozulmuş vaatler (kodu düzelt veya iddiayı düzelt)
   - `[KKE]` bulguları → test edilmemiş yüzeyler (sağlamlaştırma adayları)
   - `[Y]` bulguları → vaat–teslimat boşlukları (yerine getir veya
     yeniden adlandır)
   - TODO/ölü-kod envanteri → erteleme kaydı
   Boşluk Haritası, Mod 5'in özellik önerilerini besler.

## B Kısmı — Bug-hipotez registry'si (Mod 4)

### B1. Çerçeve

Debug'ın çoğu kayıtsız HARKing'dir: teori kur → yamala → yeşil →
teoriyi doğrulanmış ilan et. Registry her adımı açık hale getirir ve
zamanla debug yapanın sezgilerini puanlar.

### B2. Girdi şablonu (standart registry girdisini genişletir)

```markdown
### BUG-HX — <semptom, tek satır> `[H]` `[önkayıt GG-AA-YYYY]`
- **Semptom:** gözlemlenen davranış, aynen (log, trace, tekrar-üretme
  adımları). Bu alanda yorum yok.
- **Mekanizma hipotezi:** NEDEN oluyor — yanlış çıkabilecek kadar
  spesifik (dosya:satır, state, sıralama).
- **Çürütme testi:** bu mekanizmayı rakiplerinden ayıran deney (bir
  breakpoint, bir log satırı, minimal repro, property testi). Hangi
  sonuç BU hipotezi öldürür?
- **Rakip hipotezler:** aynı semptomu üreten en az bir alternatif
  mekanizma.
- **DURUM:** ⏳
```

### B3. "Düzeltme çalıştı" bir sürpriz pozitiftir

Bir bug'ı `[K]` (mekanizma doğrulandı) olarak kapatmadan önce:

- **Simetrik kontrol:** nötr bir perturbasyon da "düzeltir" miydi?
  (Timing değişimleri, cache temizliği, restart etkileri, heisenbug'lar.)
  Ucuz versiyon: düzeltmeyi geri al — bug tekrar üretiliyor mu? Sonra
  yeniden uygula. Geri almada repro yoksa → düzeltme `[K]` değil `[KKE]`.
- **Mekanizma kontrolü:** düzeltmenin konumu, hipotezlenen mekanizmayla
  eşleşiyor mu? Alakasız bir konumdan çalışan düzeltme, semptomu
  iyileştirirken mekanizmayı çürütür — iki olguyu da kaydet.

### B4. Şüphe envanteri → sezgi isabet oranı

Statik sinyaller (kontrolsüz dönüş değerleri, sınır aritmetiği,
paylaşılan mutable state, TOCTOU örüntüleri, yutulan exception'lar) her
biri temizleme-testli bir `[H]` girdisi olur. 10–15 girdiden sonra
gerçek bug-sezgisi isabet oranı çıkar — "uymuyan sayıyı yakalarsın"
örüntüsünün kod versiyonunun puanlanması. Dürüstçe kaydedilmiş ~%50,
seçilmiş %100'den değerlidir.

### B5. Değişmeden devralınan kurallar

Çürüyen hipotezler registry'de `[R]` olarak kalır. Yakın-kaçırma
yakın-kaçırmadır. Sonradan kurulan mekanizma hikâyeleri "sonradan" diye
etiketlenir. Önkoşul başarısızlıkları ("hiç tekrar-üretilemedi") hücreyi
lehte/aleyhte sayılmadan kapatır.

---

# BÖLÜM 5 — Özellik / PRD Kapısı (Mod 5)

## Çerçeve

Bir PRD, gelecek hakkında bir iddia setidir ve genellikle kanıtından bir
katman yukarıda sunulur: kullanıcı-problemi iddiaları ("kullanıcılar
X'te zorlanıyor" — çoğu zaman `[K]` kılığında `[H]`), değer iddiaları
("bu, Y'yi artıracak"), maliyet iddiaları ve bağımlılık iddiaları
("API bunu destekliyor"). Kapı iki şey yapar: PRD'nin iddialarını kod
yazılmadan ÖNCE katmanlar, ve özelliğin yayından SONRA nasıl
yargılanacağını — kaldırılma koşulu dahil — önkaydeder.

## Kapı prosedürü

### Adım 1 — PRD'yi atomize et

İddia türlerine ayır, her birini kaynağıyla katmanla:

- **Problem iddiaları:** bu problemi kim yaşıyor, nereden biliyoruz?
  Destek kayıtları, telemetri, kullanıcı alıntıları = `[K]`; kurucu
  sezgisi = `[H]` (meşru! ama etiketli); "kullanıcılar besbelli ister" =
  `[S]`.
- **Değer iddiaları:** öngörülen etki, sayı olarak.
- **Maliyet iddiaları:** emek, bakım yükü, eklenen karmaşıklık.
- **Bağımlılık iddiaları:** "kütüphane/API/platform X'i destekliyor" —
  ŞİMDİ doğrula, sprint ortasında değil. Yanlış bağımlılık iddiası erken
  yakalanması en ucuz, geç yakalanması en pahalı `[R]`'dir.
- **Kapsam iddiaları:** PRD'nin DIŞARIDA dediği şeyler. Kapsam-dışı
  bölümü olmayan PRD = gerçekleşmesi önkaydedilmiş scope drift.

### Adım 2 — Özellik girdisini önkaydet

```markdown
### FEAT-X — <ad> `[H]` `[önkayıt GG-AA-YYYY]`
- **Problem iddiası:** katmanı ve kaynağıyla.
- **Değer metriği:** ne iyileşiyor, nasıl ölçülüyor (enstrüman adıyla:
  telemetri olayı, sorgu, destek-kaydı sayısı).
- **Başarı eşiği:** şimdi kilitlenir. "T haftada hedef kullanıcıların
  ≥%N'i benimser" — "kullanıcılar beğenir" değil.
- **Kill condition / Kaldırma koşulu:** özelliğin KALDIRILMASINI haklı
  çıkaracak yayın-sonrası ölçüm. Kaldırma koşulu olmayan özellikler
  kalıcı bakım borcu olarak birikir.
- **Bilgilendiricilik önkoşulu:** başarı ölçülebilir mi ki? Telemetri /
  kullanıcı sinyali yoksa ya önce ölçümü kur ya da özelliğin `[S]`
  olarak yayınlandığını kabul et ve bunu söyle.
- **Alternatifler:** ZORUNLU, bkz. Adım 3.
- **Kabul kriterleri:** çürütme koşulu olarak ifade edilir ("özellik şu
  durumda kabulden KALIR...") — demo'da iyi görünüp çalışmayan "mış
  gibi" özelliklerin doğrudan panzehiri.
- **Maliyet:** yapım + bakım tahmini.
- **DURUM:** ⏳ kapıda / 🔨 yapımda / 🚢 yayında, ölçülüyor.
```

### Adım 3 — Alternatif-zorlama (öneri mekanizması)

Her özellik girdisi, AYNI değer metriği üzerinde katmanlanmış olarak
şunları listelemek ZORUNDA:

1. **Önerilen özellik**, belirtildiği haliyle.
2. **Aynı problem iddiasına saldıran en az bir daha ucuz alternatif**
   (UI yerine config bayrağı, sihirbaz yerine doküman sayfası, realtime
   yerine batch iş).
3. **Null alternatif** — hiçbir şey yapma, veya %10'luk versiyon.
   Problem çözülmezse maliyeti ne? Bazen dürüst cevap "bakım yükünden
   az"dır.

"Kullanıcının aklına gelmeyen özellikler" meşru olarak buradan çıkar.
İki yapılandırılmış kaynak:

- **Boşluk Haritası** (Mod 3'ten): `[R]` bulguları düzelt-veya-adlandır
  özellikleri önerir; `[KKE]` bulguları sağlamlaştırma işleri;
  `[Y]` bulguları vaat-yerine-getirme özellikleri; TODO envanteri ise
  kullanıcının zaten yazıp unuttuğu hazır bir backlog'dur. Bu adaylar
  yapıları gereği kanıt taşır — beyin fırtınasından değil, doğrulanmış
  boşluklardan türetilmişlerdir.
- **Registry madenciliği:** bug girdilerinde tekrarlayan `[R]`
  örüntüleri sistematik zayıflıkları açığa çıkarır (üç kez çürüyen
  "cache tutarlıdır" hipotezi → invalidation-yeniden-tasarımı özellik
  adayı).

**Dürüstlük maddesi — bunun vaat edemeyeceği şey:** Mizan bir denetim
disiplinidir, yaratıcılık motoru değil. Adayları yalnız kayıtlı
kanıttan üretir (boşluklar, çürütmeler, ertelemeler) ve herhangi bir
kaynaktan gelen fikirleri SIRALAR ve KISITLAR; saf icadın yenilik
tavanı hâlâ icat eden insanlara ve modellere aittir. Fikir üretimine
gerçek katkısı negatif uzaydır: gözde-özellikleri erken öldürmek (null
alternatif), unutulmuş backlog'u yüzeye çıkarmak (TODO/Boşluk Haritası)
ve her fikri aynı metrikte yarıştırmaya zorlamak. Bunu abartma.

### Adım 4 — Yayın-sonrası doğrulama (confound-kontrolü)

- Önkayıtlı eşiğe, önkayıtlı zamanda ölç. Kısmi veriyle erken kutlama =
  eşik alışverişi.
- **Benimseme sıçramaları sürpriz pozitiftir:** yenilik etkisini kontrol
  et (yenilik penceresi geçince yeniden ölç), mevsimselliği ve
  yamyamlaştırmayı (metrik, kardeş özellikten çalarak mı iyileşti?).
- Lansmandan SONRA seçilen metriklerle başarı ilan eden retrospektifler
  HARKing'dir; "sonradan" etiketle ve sonradan-kurulan hikâye daha güzel
  olsa bile önkayıtlı metriğin ne dediğini kaydet.
- Kaldırma koşulu tutarsa → özellik `[R]`'ye düşer ve kaldırma ya da
  yeni girdiyle açık yenileme planlanır. `[R]` özellikler registry'de
  kalır: "X'i sidebar'da göstermeyi denedik; öldü" kurumsal hafızadır —
  aynı fikrin seneye yeniden pazarlanmasını engeller.

### Adım 5 — İmplementasyon-fazı iddiaları

Yapım sırasında PRD iddiaları gerçekle buluşur. Kurallar:

- Yapım ortasında çöken bağımlılık iddiası girdide görünür biçimde
  `[R]`'ye döner — workaround'un ek maliyeti, özelliğin maliyet
  iddiasının karşısına kaydedilir.
- Scope drift, tier drift'tir: PRD ötesindeki her ekleme ya kendi
  mikro-girdisini ya da açık bir "sonradan kapsam, önkayıtlı değil"
  etiketini alır.
- Kabul testleri, çürütme-dilli kriterlerden demo'dan ÖNCE yazılır ve
  Mod 3'ün test-kalite kuralına tabidir (başarısız olamayan test
  dekorasyondur).
