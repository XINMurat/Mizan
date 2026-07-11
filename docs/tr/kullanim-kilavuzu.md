# Mizan Sistemi — Kullanım Kılavuzu (v1.0)
### Kanıt-katmanlı araştırma ve mühendislik disiplini: kurulum, akışlar, kurallar

Bu kılavuz kalıcı referanstır. Sistemin üç katmanı, ChatGPT önerisinin
denetiminden ayakta kalan mimariye dayanır — gerisi atılmıştır:

| Katman | Bileşen | Sorumluluğu | Nerede yaşar |
|---|---|---|---|
| Davranış | userPreferences + Mizan Proje Talimatı | AI nasıl davranır | Claude ayarları + Project instructions |
| Denetim | Mizan skill (v2.1) | Bir iddia nasıl değerlendirilir | Skill olarak yüklü |
| Veri | mizan-registry.yaml | Araştırma bilgisi nasıl saklanır | Proje bilgisi / repo |

Üç katman bağımsız çalışır: skill'siz şema da okunur, şemasız skill de
denetler. Birlikte tam sistemdir.

---

## 1. Kurulum (bir kez)

1. **Skill:** `mizan.skill` dosyasını Claude'a yükleyin (Ayarlar →
   Capabilities → Skills). Güncellemelerde eski sürümün üzerine yenisini
   yükleyin — otomatik güncellenmez. Şu anki sürüm: v2.1 (5 mod + şema).
2. **Proje talimatı:** `Mizan_Proje_Talimati.md` içindeki bloğu, Mizan
   ile çalışacağınız her Claude Project'in "Project instructions"
   alanına yapıştırın.
3. **Şema:** `mizan-registry.yaml` şablonunu kopyalayıp proje adınızla
   doldurun; Project knowledge'a dosya olarak ekleyin VEYA repo'nuzda
   tutun (önerilen: repo'da — git diff'i şemanın tasarım gerekçesidir).
4. **Diğer AI'lar için:** şema ve Türkçe dokümantasyon model-bağımsızdır.
   ChatGPT/Gemini'ye şema dosyası + Mizan_TR_Dokumantasyon.md verilirse
   aynı disiplinle (daha zayıf tetiklenme garantisiyle) çalışırlar.

## 2. Günlük akışlar

### 2.1 Yeni hipotez (önkayıt)
Test edilebilir bir iddia doğduğunda: "Bunu registry'ye önkaydet" deyin
veya Claude'un önerisini onaylayın. Claude şema formatında H-girdisi
üretir — eşik ve çürütme koşulu SONUÇ GÖRÜLMEDEN kilitlenir. Girdiyi
registry dosyanıza ekleyin (Claude proje bilgisindeki dosyayı doğrudan
değiştiremez; güncel bloğu üretir, siz yapıştırırsınız — repo'da
çalışıyorsanız Claude Code doğrudan yazabilir).

### 2.2 Deney ve sonuç
Deney girdisinde iki alan pazarlıksızdır: `baseline` (yoksa yazılı
gerekçe; baseline'sız deney hiçbir hipotezi [K]'ya taşıyamaz) ve
`confound_controls` (hipotezin confound listesindeki her madde ya
kontrol edilir ya açıkça risk olarak kabul edilir). Sonuç bloğu
append-only'dir; `honesty_annexes` boş olamaz.

### 2.3 Sürpriz pozitif protokolü
Sonuç beklenenden iyiyse `surprising_positive: true` işaretlenir ve
[K]-terfisi simetrik kontrolü bekler ("bu spesifik mekanizma mı, jenerik
alternatif mi?"). Manşet, kontrolden sonra atılır.

### 2.4 Denetim istekleri (Mod 1)
Herhangi bir iddia setini — AI özeti, rapor, öz-değerlendirme —
"Mizan'la denetle" diyerek verin. Çıktı: kapsam beyanı, katmanlı iddia
tablosu, karşı-örnek taraması, isabet oranı, eksik kart, sonraki adımlar.

### 2.5 Kod denetimi (Mod 3)
"Bu repoyu/modülü Mizan'la denetle." Claude iddia envanteri çıkarır
(testler → yorumlar → adlar → dokümanlar), her sıçramayı ayrı doğrular
(yorumun varlığı ≠ davranışın varlığı), kanıt-katmanlı davranış raporu +
Boşluk Haritası üretir. Dokümansız projede bu rapor dokümantasyonun
kendisidir. Büyük kod tabanında kapsam beyanı zorunludur — örneklenmiş
denetim tam denetim gibi sunulmaz.

### 2.6 Bug avı (Mod 4)
Debug'a başlarken: "Bug hipotezi olarak kaydet." Semptom (yorumsuz),
mekanizma hipotezi (yanlış çıkabilecek kadar spesifik), rakip hipotez ve
çürütme testi kaydedilir. "Düzeltme çalıştı" sürpriz pozitiftir:
geri-al-kontrolü yapılmadan mekanizma [K] olmaz. 10-15 girdiden sonra
gerçek bug-sezgisi isabet oranınız çıkar.

### 2.7 Özellik kapısı (Mod 5)
Yeni özellik/PRD'de: "Bunu kapıdan geçir." PRD atomize edilir (problem/
değer/maliyet/bağımlılık/kapsam iddiaları katmanlanır — bağımlılık
iddiaları sprint ortasında değil ŞİMDİ doğrulanır), başarı eşiği VE
kaldırma koşulu önkaydedilir, alternatif-zorlama uygulanır (≥1 ucuz
alternatif + null alternatif, aynı metrikte). Kabul kriterleri çürütme
dilinde yazılır. Boşluk Haritası'ndan gelen adaylar kanıt taşıyan hazır
backlog'dur.

### 2.8 Meta-inceleme (Mod 6 davranışı)
Her ~10 girdide veya istekle: hangi hipotez türleri isabetli, hangi
enstrümanlar güvenilir, yanlılık nerede birikiyor. Çıktı metodolojiyi
besler — talimat ve şema da revizyona tabidir (kendi disiplinlerine
uyarak: değişiklik gerekçeli, geçmiş silinmez).

## 3. Sert kurallar (özet — şemadaki R1–R7)

1. Sonuçtan önce eşik + çürütme koşulu (HARKing yapısal olarak kapalı).
2. Baseline zorunlu; baseline'sız sonuç [K] üretemez.
3. Her confound ya kontrollü ya açıkça kabul edilmiş risk.
4. Geçmiş append-only; [R] silinmez.
5. Dürüstlük şerhleri boş olamaz.
6. Sürpriz pozitif → terfiden önce simetrik kontrol.
7. Üretici ≠ tek denetçi: tier değişikliği önerilir, sahip/ayrı denetim
   onaylar. (RSI-güvenliği: kendi sonucunu yazan ajan kendi hipotezini
   terfi ettiremez.)

## 4. Sık hatalar

- **Şemayı forma çevirmek:** her sohbet fikri önkayıt gerektirmez;
  keşifsel konuşma serbesttir. Önkayıt, iddianın kaynak tüketecek bir
  teste gitmesine karar verildiği anda devreye girer.
- **Eşik alışverişi:** "esasen karşılandı" yasak; yakın-kaçırma
  yakın-kaçırmadır, tek gerekçeli tekrar hakkı vardır.
- **Yorum-varlığını davranış-kanıtı saymak** (kod denetiminde): her
  sıçrama ayrı doğrulanır — bu sistemin ilk canlı bulgusu tam buydu
  (discovery.py:105, "2 seviye" yorumu vs sınırsız rglob).
- **Denetim çıktısını nihai saymak:** denetim de retrospektif bir
  belgedir; kapsam beyanını okuyun, erişilemeyen kaynakları not edin.
- **Registry'yi tek dosyada şişirmek:** proje başına bir registry;
  100+ girdide alan bazlı bölme (registry-bugs.yaml, registry-feat.yaml).

## 5. İlk gerçek görev (önkayıtlı)

SpectralLM deney registry'nizin (experiment_registry_and_metrics.md)
mizan-registry.yaml şemasına migrasyonu — geçen oturumda kilitlenen
eşikle: şema ≥20 gerçek girdiyi yapısal yeniden-yazım gerektirmeden
taşır VE en az bir kez sizin dışınızda bir araç/model tarafından okunup
güncellenirse → standartlaştırma tartışması açılır. Aksi halde ORP
fikri [R] ve şema kişisel araç olarak kalır — ki bu da geçerli bir
sonuçtur.

## 6. Dosya envanteri

| Dosya | İçerik |
|---|---|
| mizan.skill | Skill paketi v2.1 (5 mod + şema gömülü) |
| mizan-registry.yaml | Şema şablonu (bağımsız kopya) |
| Mizan_Proje_Talimati.md | Project instructions bloğu + fark analizi |
| Mizan_TR_Dokumantasyon.md | Mod 1–2 tam Türkçe referans |
| Mizan_TR_Ek_YazilimModlari.md | Mod 3–5 tam Türkçe referans |
| Bu kılavuz | Kurulum, akışlar, kurallar |
