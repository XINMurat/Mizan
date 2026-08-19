# Proza ↔ şema denetimi: hangi zorunluluk yazılı ama uygulanmıyor?

*Tarih: 2026-08-20. Kapsam: `skill/mizan/SKILL.md` (345 satır) **ve
`skill/mizan/references/` altındaki beş dosyanın tamamı** (checklist 208,
code-audit 190, domain-adaptation 201, feature-gate 127, templates 175 — toplam
901 satır); `skill/mizan/schemas/mizan-registry.yaml` (v1.2) ve
`tools/mizan_validate.py` (R1–R8) tarafından fiilen uygulananlarla
karşılaştırıldı.*

*Kardeş denetim: `Kiyas/PROSE-SCHEMA-AUDIT.md`. Aynı yöntem, aynı sorular.
Kural eklemek yöntem değişikliğidir ve karar bakımındır.*

---

## DURUM (2026-08-20) — hangileri kapatıldı

| # | Bulgu | Durum |
|---|---|---|
| 0 | R4 CI'da koşmuyor | **KAPATILDI** — `--against`, `fetch-depth: 0`, baseline adımı + self-test |
| 1 | `features`/`bugs` hiç denetlenmiyor (M5) | **KAPATILDI** — şema v1.3 + R13/R14/R15 + R8 kapsamı |
| 2 | `[K]` kanıtsız verilebiliyor | **KAPATILDI** — R9 (result VEYA `external_evidence`) |
| 3 | Uyarı kanalı yok | **KAPATILDI** — `warnings` + `--strict`; CI örneklerde strict, diğerlerinde tavsiye |
| 4 | Eşikler sayısal olmak zorunda değil | **KAPATILDI** — R10, `non_numeric_justification` kaçış kapısıyla |
| 5 | Tier'sız girdi geçiyor | **KAPATILDI** — R11 |
| 6 | "Her alan zorunlu" uygulanmıyor (M6) | **KAPATILDI** — R12 (`metric.instrument` dahil) |
| 7 | Prior art alanı okunmuyor (koşullu) | **KAPATILDI** — R12; "bilinen akraba yok" meşru, sessizlik değil |
| 8 | Coverage Ledger'ın veri biçimi yok (M9) | **AÇIK — tek kalan** |
| 9–11 | `two_sided`, eşiksiz hipotez, hepsi-`[K]` | **KAPATILDI** — W1 / W2 / W3 |

**Şema v1.4 notu:** R9–R12'nin göç maliyeti gerçek — her girdi artık
enstrümanı adlandırılmış bir `metric`, bir `cost`, bir `status` ve açık bir
`prior_art` ister. Bunu ödeyemeyen bir girdi önkayıt edilmemiş, taslak
çizilmiştir; R11 de onu etiketsiz bırakmak yerine söyler. 1.0–1.3 dosyaları
uygulanmadan geçerli kalır.

**Kanalın ilk koşusunda çıkan iki şey:** (a) kendi eklediğim FEAT-001/BUG-001
girdilerinde `two_sided` yoktu — W1 hemen yakaladı, şemaya ve örneğe eklendi.
(b) `mizan-product-registry.yaml`'daki FEAT-M001/M002, `value_metric` /
`success_threshold` adlarını kullanıyor; v1.3'ün `metric`/`threshold` eşlemesi
bunları görmez hâle getiriyordu. **Bu, benim önerdiğim tasarım kararının
sessizce mevcut girdileri geçersiz kılması olurdu.** Doğrulayıcı artık her iki
adı da kabul ediyor (`FIELD_ALIASES`); yeniden adlandırma hiçbir şey kazandırmaz.
Geriye kalan tek gerçek göç maliyeti: `alternatives` girdilerine `kind:`
eklemek — "null alternatif fiyatlandı" ifadesini iddia edilebilir olmaktan
çıkarıp denetlenebilir yapan şey o.

**Tasarım kararı (kullanıcı):** `features`/`bugs`, hipotez şeklinin **üzerine**
eklenir. Sonuç: `value metric` → `metric`, `success threshold` → `threshold`,
bug'ın mekanizması → `formal` (semptom kendi alanında yorumsuz kalır). Böylece
R1 ve R8 ikinci bir uygulama yazılmadan bu iki bloğa da geçerli oldu; yalnız
onlara özgü olan üç şey yeni kural gerektirdi (R13 kill_condition, R14
alternatives, R15 rival_hypotheses).

### Tarama sırasında çıkan ek bulgu — örnek registry'nin kendi hakkındaki iddiası yanlıştı

`examples/mizan-registry.example.yaml` başlığında *"passes tools/mizan_validate.py
(R1–R8 clean)"* yazıyordu ve `schema_version: "1.1"` beyan ediyordu. R8 ise
1.2'ye kapılı. Yani **R8 o dosyada hiç koşmamıştı** — ve H-001'in hakem bloğu
hiç yoktu. 1.2'ye çıkarıp koşunca tek ihlalle düşüyor. Başlıktaki iddia, ancak
kontrol kapalı olduğu için doğruydu: reponun kendi terimleriyle bir `[Y]`,
kendi örnek dosyasında.

Düzeltildi: dosya 1.3 beyan ediyor, H-001 hak ettiği `instrument` hakemini aldı,
ve 1.3'ün tanımladığı FEAT/BUG girdileri çalışılmış hâlleriyle eklendi. Bu,
§0'daki sorunun üçüncü bir cevabı: proza–şema farkı yalnızca kuralların değil,
**örneklerin kendi hakkındaki iddialarının** da altını oyabiliyor.

---

## 0. Neden bu tarama yapıldı

Kıyas'ta aynı tarama, prozanın açıkça yasakladığı iki şeye şemanın izin verdiğini
buldu (G8/G9 ile kapatıldı). Soru: bu Kıyas'a özgü müydü, yoksa "prozayı yaz,
şemayı sonra yetiştir" ikisinde de aynı biçimde mi işliyor?

Cevap: aynı biçimde işliyor, **ama farklı bir yerde**. Mizan'ın hakem katmanı
(R8) Kıyas'ınkinden **daha eksiksiz** — Kıyas'ta hâlâ açık olan bir bulguyu
(`class` ↔ `independent_of_author` çelişkisi) Mizan zaten yakalıyor. Buna karşılık
Mizan'ın **kendi altı temel taahhüdünden üçü** hiç uygulanmıyor.

---

## 1. Kanıt-A: R1–R8'den temiz geçen içi boş registry

```yaml
registry: {project: "Probe", schema_version: "1.2"}
hypotheses:
  - id: "H-001"
    # tier: HİÇ YOK — taahhüt 1 "no untagged assertions"
    status: "open"
    formal: "The new approach is better."
    # threshold yok, refutation yok, prior_art yok, two_sided yok
    arbiter: {class: "runtime", who: "pytest"}
  - id: "H-002"
    tier: "K"
    threshold: {support: "improves things", refute: "does not improve things"}
    refutation: "if it does not improve"
    two_sided: ""
    prior_art: []
    arbiter: {class: "runtime", who: "pytest"}
experiments: []
results: []
```

→ `OK — 2 entries checked, no R1–R8 violations.`

`"improves things"`, prozanın **eşik olmayan şeye örnek olarak verdiği ifadenin
kendisi**: *"'Improves things' is not a threshold; 'ΔPPL ≤ −3%' ... is."*

## 2. Kanıt-B: kanıtsız `[K]`

```yaml
registry: {project: "P", schema_version: "1.2"}
hypotheses:
  - id: "H-001"
    tier: "K"                       # deney yok, sonuç yok, onay yok
    threshold: {support: ">= 5%", refute: "< 1%"}
    refutation: "below 1%"
    arbiter: {class: "third_party", who: "external reviewer", calibration: "reviewer null"}
experiments: []
results: []
```

→ `OK — 1 entries checked, no R1–R8 violations.`

**Bir hipotez, tek bir deney veya sonuç olmadan doğrudan `[K]` yazılabiliyor.**
R7 yalnızca bir *sonucun* terfi önerdiği durumda devreye giriyor; hiç sonuç
üretmeyip `tier: K` yazmak denetimsiz. Bu, anti-desen listesinin ilk maddesinin
(*"a tiered report where every claim lands in `[K]` without checking sources —
the flattery problem wearing a lab coat"*) tam olarak açık hâli.

---

## 3. Bulgular

Kıyas denetimindeki sınıflandırmanın aynısı.

### ÇELİŞKİ-M1 — `[K]` kanıtsız verilebiliyor **(en ağır bulgu)**

**Proza:** taahhüt 1 ve anti-desen 1. Ayrıca tier tablosu `[K]` = *"Direct
evidence supports it; source cited; threshold met"* — üçü de bir sonucun varlığını
gerektirir.

**Şema:** `tier: K` serbest bir alan. R7 yalnızca `decision: propose H->K` taşıyan
bir sonuç varsa bakıyor; sonuç hiç yoksa kontrol yok.

**Uygulanabilir mi:** evet. `tier == "K"` ⇒ bu hipoteze atıfta bulunan, eşiği
karşılamış bir `result` var. **Kırılma noktası:** dışarıdan gelen, registry'de
deneyi olmayan bir kanıt (yayımlanmış literatür) meşru olarak `[K]` olabilir —
o durumda `prior_art` + kaynak alanı kanıt yerine geçmeli. Yani kural
"result VEYA yazılı dış kaynak" biçiminde olmalı, yalnız result değil.

### ÇELİŞKİ-M2 — eşikler sayısal olmak zorunda değil

**Proza:** registry adımı 2, birebir: *"Lock thresholds numerically. 'Improves
things' is not a threshold; 'ΔPPL ≤ −3%' or 'counter-example rate < 1 per 10
sources' is."*

**Şema:** R1 yalnızca `support` ve `refute` alanlarının **boş olmadığına** bakıyor.
İçerik serbest.

**Uygulanabilir mi:** evet — Kıyas'ta W1 için yazılan sayı/karşılaştırma regex'inin
tersi. Orada "sayı VAR mı" aranıyordu, burada "sayı YOK mu". Aynı enstrüman.
**Not:** Kıyas'ta bu regex zaten yazılı ve test edilmiş durumda; taşınabilir.

### ÇELİŞKİ-M3 — prior art hiç kontrol edilmiyor *(references taramasıyla yumuşatıldı)*

**Proza:** registry adımı 8: *"Prior art is declared, not discovered by reviewers.
If the hypothesis has known relatives, name them in the entry and state where the
originality claim actually lives."*

**Şema:** `prior_art` alanı var, doğrulayıcı **hiç okumuyor.** Boş liste veya
alanın tamamen yokluğu sessizce geçiyor.

**DÜZELTME (references taraması sonrası):** İlk turda bunu "prior_art boş olamaz"
biçiminde bir kural adayı olarak yazmıştım; **yanlıştı.** `templates.md` §1 açıkça
diyor ki *"Every field is mandatory except 'Prior art' (mandatory only when
relatives are known or suspected)."* Yani koşullu zorunlu. Doğru kural, Kıyas'ın
"not searched dürüst bir cevaptır" mantığının aynısı: **alan mevcut olmalı ve
açık bir şey söylemeli** — "bilinen akraba yok" meşru bir değer, sessizlik değil.
Bu, G7'nin boş-liste-artı-not kuralıyla birebir aynı biçim.

**Karşılaştırma:** Kıyas'ta bunun karşılığı G9 olarak kapatıldı, ama orada
koşulsuz (`searched: true`). Mizan'da koşullu olmalı — iki repoyu körü körüne
hizalamak burada hata olurdu.

### ÇELİŞKİ-M4 — tier'sız girdi geçiyor

**Proza:** taahhüt 1: *"Every claim gets an evidence tier. **No untagged
assertions.**"*

**Şema:** `if t and t not in VALID_TIERS` — yani tier **varsa** geçerliliğine
bakılıyor, **yoksa** hiç ses çıkmıyor. Etiketsiz iddia tam olarak yasaklanan şey.

**Uygulanabilir mi:** evet, tartışmasız, tek satır.

### ÇELİŞKİ-M5 — `features` ve `bugs` blokları hiç denetlenmiyor **(kapsam olarak en büyük)**

Bu, `references/` taramasının çıkardığı asıl bulgu, ve tek başına ilk turdaki
her şeyden geniş: **Mod 4 (bug) ve Mod 5 (feature/PRD) için şema tarafında
sıfır uygulama var.**

Kanıt-C:

```yaml
registry: {project: "P", schema_version: "1.2"}
hypotheses: []
experiments: []
results: []
features:
  - id: "FEAT-001"
    tier: "K"
    title: "Ship the wizard"
    # problem_claim yok, value_metric yok, success_threshold yok,
    # kill_condition yok, alternatives yok, kabul kriteri yok, arbiter yok
bugs:
  - id: "BUG-001"
    tier: "K"
    symptom: "it crashes"
    # mechanism yok, refutation_test yok, rival_hypotheses yok, arbiter yok
```

→ `OK — 2 entries checked, no R1–R8 violations.`

`check()` bu iki koleksiyonu yalnızca **tier geçerliliği** ve **girdi sayımı**
için okuyor. Başka hiçbir şey. Oysa referans dosyaları burada üç ayrı şeyi
büyük harfle zorunlu kılıyor:

- **`alternatives` — `feature-gate.md` Adım 3:** *"Every feature entry **MUST**
  list, tiered on the SAME value metric: 1. the proposed feature, 2. **at least
  one cheaper alternative**, 3. **the null alternative**."* Şemada alan yok
  (yalnızca dosya sonundaki yorumda geçiyor), kontrol yok.
- **`kill_condition` — `feature-gate.md` Adım 2:** *"Features without kill
  conditions accumulate as permanent maintenance debt."* Şemada alan yok,
  kontrol yok.
- **`rival_hypotheses` — `code-audit.md` §B2:** *"**at least one** alternative
  mechanism that produces the same symptom."* Bu, Mod 4'ün tamamının varlık
  sebebi (*"Never close on the first story that fits"*). Şemada alan yok,
  kontrol yok.

Ayrıca **R8 feature/bug'lara hiç uygulanmıyor**: `_check_arbiters(hyps.values())`
yalnızca hipotezleri geziyor. Oysa şemanın kendi yorumu diyor ki *"The
success_threshold carries its own arbiter block; a value metric whose only judge
is the feature's own proposer is class: author and cannot reach K."* — yazılmış,
uygulanmamış. Yukarıdaki `FEAT-001` hakemsiz olarak `[K]`'da duruyor.

**Uygulanabilir mi:** evet, ama önce **şema işi**. Bu alanların şemada tanımı
yok; kural yazmadan önce `features`/`bugs` girdilerinin alan yapısı yazılmalı.
Bu, Kıyas'ta G7 öncesi `discards`'ın durumunun aynısı: proza zorunlu kılıyor,
veri biçimi taşımıyor, dolayısıyla CI göremiyor.

### ÇELİŞKİ-M6 — "her alan zorunlu" hiç kontrol edilmiyor

`templates.md` §1 birinci cümlesi: *"Write the entry BEFORE the test runs.
**Every field is mandatory** except 'Prior art'."* Zorunlu alanlar: Formal,
Metric (+ **instrument**), Arbiter, Threshold, Refutation, Cost, Status.

Doğrulayıcı bunlardan yalnızca **Arbiter**'a (R8, ≥1.2) ve
**Threshold+Refutation**'a (R1, sadece bir sonuç atıfta bulunuyorsa) bakıyor.
`formal`, `metric`, `metric.instrument`, `cost`, `status` hiç okunmuyor.

Kanıt-D: `formal`, `metric`, `cost`, `status` alanlarının hiçbiri olmayan bir
hipotez temiz geçiyor.

`metric.instrument` özellikle önemli, çünkü `domain-adaptation.md` soru 2'nin
(*"what produces the numbers, and what are its known distortions?"*) kayıt
karşılığı o. Enstrümanı adlandırılmamış bir eşik, R8'in tam olarak engellemeye
çalıştığı şeyin ölçüm tarafındaki hâli.

### MODELLENMEMİŞ-M1 — `two_sided` alanı hiç okunmuyor

Registry adımı 3: *"check the two-sided informativeness requirement: both possible
outcomes must teach something. If only success is informative, redesign the test."*
Şemada alan var, doğrulayıcı bakmıyor. İçeriğin gerçekten iki yönlü olduğu
denetlenemez ama **varlığı** denetlenebilir — G6/G7'nin "sessizlik temiz tarama
değildir" mantığının aynısı.

### MODELLENMEMİŞ-M2 — henüz sonucu olmayan hipotez eşiksiz durabiliyor

R1 yalnızca bir sonucun atıfta bulunduğu hipotezlere bakıyor. Registry prosedürü
ise girdinin **test koşulmadan önce** yazıldığını ve eşiği o anda taşıdığını
söylüyor. Taslak hâlindeki girdiler için mevcut hoşgörü savunulabilir; bu yüzden
**uyarı**, kural değil.

### MODELLENMEMİŞ-M3 — hepsi `[K]` olan registry

Anti-desen 1'in registry-düzeyi hâli. Kıyas'taki W2'nin birebir kardeşi.
**Uyarı** olmalı — tek hipotezli veya gerçekten kanıtlanmış bir registry meşru.

### YAPISAL-M1 — uyarı kanalı yok (Kıyas ile aynı)

Doğrulayıcı ikili: ihlal listesi + exit 1, ya da OK. M1/M2/M3'ün üçü de bloke
etmemeli. Kıyas'ta bu kanal dün eklendi (`warnings` + `--strict`, CI strict koşar)
ve **doğrudan taşınabilir** — mesaj kataloğu, iki kanallı `check()` dönüşü ve
`--strict` bayrağı aynı biçimde çalışır.

### YAPISAL-M2 — R4 (append-only) CI'da hiç koşmuyor

`_append_only` yalnızca `--against GITREF` verilirse çalışıyor.
`.github/workflows/mizan.yml` doğrulayıcıyı **bayraksız** çağırıyor. Yani
reponun *"Refuted entries are never deleted"* taahhüdünü uygulayan kod var,
yazılmış, test edilmiş — ve hiçbir otomatik koşuda devreye girmiyor.

Bu, denetimin en ucuz düzeltmesi: PR'larda `--against origin/main` eklemek.
**Kırılma noktası:** yeni bir registry dosyası baseline'da yok; `load_git_baseline`
zaten `None` dönüp sessizce atlıyor, yani güvenli.

---

### YAPISAL-M3 — Coverage Ledger'ın veri biçimi yok

`code-audit.md` §A5.1 ve `templates.md` §5, fazlı denetimlerde Coverage
Ledger'ı **zorunlu** kılıyor ve ona bir hüküm bağlıyor: *"the whole-repo `[K]`
coverage claim stays `[H]` until the MERGE row is `✅ done`"* — yani **tier'ı
belirleyen bir kural**, ve bir Markdown tablosunda yaşıyor. Registry şemasında
karşılığı yok; hiçbir doğrulayıcı "MERGE koşmadan kapsam `[K]` olamaz"ı
denetleyemez.

Aynı sınıftan ikinci bir örnek: `checklist.md` §12'nin önkayıt kuralı — *"each
new phase must add its scenarios **before** the phase's work begins, and the
report must state plainly which scenarios were retrospective."* Senaryo listesi
için de şemada alan yok.

Bu, Kıyas'taki `discards` boşluğunun birebir aynısı: prozanın zorunlu kıldığı,
tier'ı etkileyen bir kayıt, yalnızca serbest metinde yaşıyor — yani sessizce
kaybolabilir ve kaybolduğu fark edilmez.

## 4. Mekanikleştirilemeyecek olanlar (kapsam dürüstlüğü)

- Tier drift'in **iki doküman arası** tespiti — registry içi değil.
- `two_sided` metninin gerçekten iki yönlü olması.
- `honesty_annexes` içeriğinin gerçekten ilgili sınırları sayması.
- Eşiğin sonucu gördükten sonra yükseltilip yükseltilmediği — ancak
  `--against` ile git tarihçesinden görülebilir, ki bu R4'ün alanı.
- `post_hoc_reasoning` etiketinin dürüst olması.
- Denetim kapsamının beyanı (*"N of M claims checkable"*) — rapor biçimine ait,
  registry şemasına değil.

---

## 5. Sıralama

Sıralama, `references/` taramasından sonra **değişti**: en büyük boşluk artık
tek bir kural değil, denetimsiz iki mod.

| # | Bulgu | Sınıf | Aksiyon |
|---|---|---|---|
| 0 | R4 CI'da koşmuyor | YAPISAL | Workflow'a `--against origin/main` — **kod gerektirmiyor** |
| 1 | `features`/`bugs` hiç denetlenmiyor (M5) | ÇELİŞKİ | Önce ŞEMA, sonra R13–R15 |
| 2 | `[K]` kanıtsız verilebiliyor | ÇELİŞKİ | R9, bloke eden (result VEYA dış kaynak) |
| 3 | Uyarı kanalı yok | YAPISAL | Kıyas'tan taşı; diğerlerini mümkün kılar |
| 4 | Eşikler sayısal olmak zorunda değil | ÇELİŞKİ | R10, bloke eden; regex Kıyas'ta hazır |
| 5 | Tier'sız girdi geçiyor | ÇELİŞKİ | R11, bloke eden, tek satır |
| 6 | "Her alan zorunlu" uygulanmıyor (M6) | ÇELİŞKİ | R12; `metric.instrument` dahil |
| 7 | Prior art alanı okunmuyor (koşullu) | ÇELİŞKİ | R12 ile birlikte; "yok" yazmak meşru, sessizlik değil |
| 8 | Coverage Ledger'ın veri biçimi yok (M9) | YAPISAL | Şema işi; G7'nin Mizan'daki karşılığı |
| 9 | `two_sided` okunmuyor | MODELLENMEMİŞ | Uyarı |
| 10 | Sonuçsuz hipotez eşiksiz | MODELLENMEMİŞ | Uyarı |
| 11 | Hepsi `[K]` registry | MODELLENMEMİŞ | Uyarı |

**0 numara kod yazmayı gerektirmiyor** — yazılmış ve test edilmiş bir kontrolün
çağrılmaması. Hâlâ en ucuz düzeltme.

**1 numara sıradaki büyük iş ve tek başına bir tur.** Kural yazmadan önce
şemanın `features`/`bugs` alan yapısını taşıması gerekiyor; aksi hâlde neyin
zorunlu olduğunu söyleyen bir veri biçimi olmadan kural yazmış oluruz.

---

## 6. Çapraz bulgu: iki repo birbirini tamamlıyor

Tarama, tek repoda görünmeyen bir şeyi gösterdi — aynı kural iki repoda farklı
olgunlukta:

| Kural | Kıyas | Mizan |
|---|---|---|
| hakem sınıfı zorunlu | G5 ✓ | R8 ✓ |
| yazar-hakem tavanı | G5 ✓ | R8 ✓ |
| `class` ↔ `independent_of_author` çelişkisi | **AÇIK** | R8 ✓ |
| prior art zorunlu | **G9 ✓** (dün) | **AÇIK** |
| sayısal eşik denetimi | W1 ✓ (ters yön) | **AÇIK** |
| uyarı kanalı | ✓ (dün) | **AÇIK** |
| append-only CI'da | yok (gerekmiyor) | kod var, **çağrılmıyor** |

Her iki repo da diğerinin çözdüğü bir şeyi çözmemiş. İki somut taşıma işi:
`independence_contradiction` → Kıyas'a, `warnings`/`--strict` + prior-art kapısı
→ Mizan'a.

---

## 7. Bu denetimin kurmadığı şeyler

- **Kapsam artık tam, ama yalnızca paketlenen dosyalar için.** `SKILL.md` + beş
  `references/` dosyası + şema + doğrulayıcı tarandı. `docs/` altındaki
  uzun-metinler (usage-guide, metodoloji, proje-talimati, yazilim-modlari,
  alan-uyarlama) **taranmadı**; onlar skill'e paketlenmiyor, ama kullanıcıya
  zorunluluk vaat ediyor olabilirler.
- **`domain-adaptation.md` bulgu üretmedi ve bu beklenen bir sonuç.** O dosya
  kural değil *uyarlama reçetesi* veriyor (altı soru + alan kataloğu); tek sert
  hükmü olan DC-001 (bireysel isabet oranları bireyde kalır, yönetim yalnız
  toplamı görür) bir yetkilendirme politikasıdır, registry şemasının
  denetleyebileceği bir şey değil. Taranmış ve temiz çıkmış olması da bir
  sonuçtur.
- **Kanıt fixture'ları sentetik.** Kuralın kapatmadığını gösterir, birinin
  istismar ettiğini değil. `examples/mizan-registry.example.yaml` bu boşlukların
  hiçbirine düşmüyor.
- **R9–R12 önerilmedi, sadece adlandırıldı.** Hiçbiri denetim kalitesini
  artırdığı gösterilmiş değil; tek gerekçeleri prozayla tutarlılık — `[S]`.
