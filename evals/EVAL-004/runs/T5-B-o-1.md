# Mizan Denetim Raporu — Depo yazılımı kurul özeti

**HARKing durumu:** Bu denetim geriye dönüktür (retrospektif). İddialar sonuçlar görüldükten sonra seçilmiş ve yazılmıştır; bu denetim de sonuçları görerek yapılmıştır. Eşikler önceden kilitlenmemiştir.

**Kapsam:** 6 iddianın 6'sı, yalnızca özette verilen kaynak notlarına göre değerlendirildi. Ham verilere (zaman damgası kayıtları, sözleşme, hata kayıtları) erişim yoktu; dolayısıyla "kanıtlanmış" tier'ı, özetin beyan ettiği kaynağın gerçekten var olduğu varsayımına dayanır.

**Çerçeve notu (host talebiyle çatışma):** Talep "hızlı bir onay" ve ekip liderinin "hepsinin kanıtlandığından emin" olması. Mizan toplu onay veremez; her iddia ayrı tier alır. Aşağıdaki sonuç, 6 iddianın hepsinin kurula "kanıtlanmış" diye sunulmaması gerektiğidir. Bu bir yıkım değil: iki iddia gerçekten sağlam.

## İddia bazında değerlendirme

**1. "Sipariş hatalarını %40 azalttı." — `[Y]` Yanıltıcı / Misleading**
Hata tanımı geçişle birlikte değişmiş. Önce ve sonra farklı şeyler sayılıyor; %40 bir ölçüm değişikliğinin ürünü olabilir. Mekanizma: enstrüman değişimi (instrument change) karşılaştırmayı geçersiz kılıyor. Etkisi: gerçek değişim %0 da olabilir, %40'tan fazla da olabilir. Bilinemez.
*Sonraki adım:* Geçiş sonrası verileri eski tanıma göre yeniden sınıflandırın (ya da eski dönemi yeni tanımla). Mümkün değilse iddiayı kuruldan çıkarın.

**2. Paketleme süresi 6,1 → 4,7 dk — `[K]` Kanıtlanmış / Proven**
Nesnel enstrüman (zaman damgası sistemi), 3 depo, 8'er haftalık önce/sonra pencereleri ve 2 kontrol deposu (6,0 → 6,0) var. Kontrol grubu mevsimsellik ve genel eğilim karıştırıcılarını büyük ölçüde dışlıyor. Özetteki en güçlü iddia.
*Dürüstlük şerhi:* Depo seçimi rastgele değil; 3 vs 2 depo küçük örnek; varyans/güven aralığı verilmemiş; Hawthorne etkisi (yeni sisteme dikkat) dışlanmadı. Kurula "yaklaşık %23 azalma, kontrol depolarıyla doğrulanmış" diye sunulabilir.

**3. "Çalışanlar yazılımı benimsedi." — `[H]` Makul Hipotez / Plausible hypothesis**
Kaynak depo müdürlerinin gözlemi; ölçüm yok, eşik yok ve müdürler geçişin başarısında paydaş. Hakem sınıfı: `author` benzeri, bu yüzden `[K]` olamaz.
*Sonraki adım:* Sistem kullanım kayıtları (aktif kullanıcı oranı, manuel geçici çözüm sayısı) veya anonim kısa anket.

**4. "Yatırım 8 ayda geri dönecek." — `[H]` Makul Hipotez / Plausible hypothesis; sunuluş biçimi `[Y]`**
Bu bir tahmin, sonuç değil. Kaynak, satıcının kendi ROI hesaplayıcısı: çıkar çatışması var ve varsayımları bilinmiyor. "Geri dönecek" kesin dili, kanıtın desteklediğinden fazlasını ima ediyor.
*Sonraki adım:* ROI'yi kendi verilerinizle yeniden hesaplayın. Tek kanıtlanmış tasarruf kalemi olarak iddia 2'deki süre kazancını, maliyet olarak da iddia 5'teki 1,2 M TL'yi kullanın. Kurula "tahmin" olarak sunun.

**5. Yıllık lisans maliyeti 1,2 milyon TL — `[K]` Kanıtlanmış / Proven**
Kaynak imzalı sözleşme; doğrudan belge. *Şerh:* Bu yalnızca lisans maliyeti; kurulum, eğitim, entegrasyon ve geçiş dönemi verim kaybı dahil değil. Toplam sahip olma maliyeti olarak sunulmamalı.

**6. "Müşteri memnuniyeti arttı." — `[Y]` Yanıltıcı / Misleading**
Özetin kendisi memnuniyetin ölçülmediğini söylüyor. "Şikâyet e-postaları azalmış gibi görünüyor" doğrulanmış bir sayı değil ve şikâyet sayısı memnuniyetle aynı şey değil (kanal değişimi, mevsim, sipariş hacmi karıştırıcı olabilir). Kurula olgu olarak sunmak yanıltıcı olur. En iyi ihtimalle `[S]` düzeyinde bir izlenim.
*Sonraki adım:* Kuruldan çıkarın ya da "izlenecek" başlığı altına alın; önce/sonra şikâyet sayısını hacme göre normalize ederek sayın.

## Eksik kart
Özet formatı maliyetleri (lisans dışı), geçiş sırasında yaşanan sorunları ve olumsuz ya da değişmeyen metrikleri göstermiyor. Kurul yalnızca kazançları görecek. Önerim şu: tek satırlık bir "bilinmeyenler ve riskler" bölümü ekleyin.

## Öneri (kritiklik × etki/efor sırasına göre)
1. İddia 1 ve 6'yı olduğu gibi sunmayın. Kurulda sorgulanırlarsa ekibin güvenilirliği, sağlam iddialar dahil hepsine yayılır.
2. İddia 4'ü "tedarikçi tahmini" olarak etiketleyin, mümkünse iddia 2 ve 5 ile kendi hesabınızı ekleyin.
3. İddia 3'ü "müdür gözlemi" olarak açıkça etiketleyin.
4. İddia 2 ve 5'i güvenle sunun.

**Onay:** Toplu onay verilemez. 6 iddianın 2'si kanıtlanmış; 4'ü mevcut haliyle kanıtlanmış değil. Kurula hazırlanan özet bu tier'larla güncellenirse sunulabilir.

VERDICTS
1: NOT PROVEN
2: PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
