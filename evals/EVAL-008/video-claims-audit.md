# Denetim: "Anthropic ve OpenAI Uyardı. Skill'lerimi Tek Tek Baştan Yazıyorum."

Kaynak: YouTube `5LLLxHxkCnI`, kullanıcının yapıştırdığı transkript (2026-10-09).

**HARKing durumu:** Retrospektif denetim. Video, örneklerini sonuçları gördükten
sonra seçmiş. Bu denetim de iddiaları videoyu izledikten sonra seçti.
**Kapsam:** 12 iddia. Bunların 5'i dış kaynakla kontrol edildi (web araması,
yalnızca ikincil kaynaklar, birincil belgeler açılmadı). 1'i repodaki
ölçümlerle karşılaştırıldı. Kalan 6'sı yalnızca videonun kendi
gösterimine dayanıyor.

| # | İddia | Tier | Gerekçe |
|---|---|---|---|
| V1 | Kısa brif, uzun prompttan daha kaliteli sonuç veriyor | `[H]` / `[KKE]` | Görev başına 1–2 deneme yapılmış. "Kalite"yi yazar kendisi değerlendirmiş (hakem = yazar). Kör puanlama yok. Testlerin 5/6'sı yaratıcı görsel/metin işi. |
| V2 | Yeni modeller talimatı harfiyen uyguluyor | `[H]`, desteği güçlü | Anthropic'in Claude 4 sonrası prompt rehberi "daha kesin talimat takibi" diyor. Repodaki EVAL-004'te haiku, skill yüklüyken hak edilmiş iddiaların 5/24'ünü şablonu uygulayıp reddetti. Bu, aynı mekanizmanın bağımsız bir gözlemi. |
| V3 | Ayrıntılı talimat performansı düşürüyor | `[Y]` | Doğru olan kısım şu: talimat dışındaki işler yapılmıyor (V6). Ancak "düşürüyor" genellemesi, "istenen iş tam yapıldı ama istenmeyen yapılmadı" sonucunu kalite düşüşü gibi sunuyor. |
| V4 | Bu görüş OpenAI ve Anthropic'in resmi tavsiyesi | `[H]`, yönü doğru | OpenAI'nin yeni rehberi sonuç odaklı ve yalın promptları öneriyor. İkincil kaynaklar yalın sistem promptlarıyla %10–15 skor artışı ve %33–67 maliyet düşüşü bildiriyor; birincil belge açılmadı. "GPT-6 Astra" adı doğrulanamadı; aramada bulunan model adı GPT-5.6 Sol. |
| V5 | Anthropic: CLAUDE.md 200 satırın altında kalsın | `[H]` | Birçok ikincil kaynak bu rakamı Anthropic belgelerine atfediyor. Birincil belge bu oturumda açılmadı. |
| V6 | Kart ekstresi testi: ağır prompt 0/7 sorun, kısa prompt 7/7 sorun buldu | `[KKE]` | Tek görev, 2 deneme. Mekanizma makul: format dayatınca model yalnızca formatı doldurur. Bu, Mizan'ın kendi "eksik kart" kavramıyla aynı şey. Kontrol koşulu da eksik: "sorunları da belirt" diyen bir ağır prompt denenmemiş. |
| V7 | Martılar: model sorunu gördü ama listeye bağlı kaldığı için düzeltmedi | `[S]` | Tek bir anekdot. Davranışın açıklaması ilginç ama sınanmamış. |
| V8 | ETH Zürih: context dosyaları maliyeti %20'den fazla artırıyor, başarıyı artırmıyor | `[K]` yönü, `[H]` rakamları | arXiv 2602.11988. Otomatik üretilmiş dosyalar başarıyı biraz düşürüp maliyeti %20–23 artırıyor. Geliştiricinin yazdığı dosyalar yaklaşık %4 yarar ve %19 maliyet getiriyor. Video bu ikinci kısmı söylemiyor: insan eliyle yazılmış, az sayıda talimat yine de hafif yarar sağlıyor. Rakamlar ikincil kaynaklardan; makale okunmadı. |
| V9 | "Model kendi bilebilir mi? Bilebiliyorsa sil" ölçütü | `[H]`, iyi bir ölçüt | ETH makalesinin önerisiyle örtüşüyor: yalnızca çıkarılamayacak ayrıntılar yazılsın. Mizan'ın hem tarafındaki hem karşısındaki gözlem: EVAL-001/002'de talimatsız kol bile tavana ulaştı. |
| V10 | Çelişkili talimatlar modeli bozuyor | `[H]` | Makul ama videoda test edilmemiş. |
| V11 | İndirilen skill'lerin çoğunu silin | `[S]` | Görüş belirtiyor, ölçüm yok. |
| V12 | Prompt yazmak yerine modelle konuşun | `[S]` | İş akışı tavsiyesi, sınanmamış. |

## Repodaki ölçümler videoyla karşılaştırıldığında

Mizan bu soruyu kısmen zaten ölçmüş:

- **RES-EVAL-001 / 002:** Skill'siz kol dahil tüm kollar tavana ulaştı. Skill çıktıyı 2,2 kat uzattı ama bulunan hata sayısı artmadı (`[K]`, maliyet ölçüldü). Bu sonuç videonun yanında.
- **RES-EVAL-003:** Haiku'da tavan aşılmadı. Tam skill, 45 kelimelik kısa brife göre +0,062 daha fazla hata buldu (CI [0,000, +0,146]). Ama 2,5 kat daha fazla yanlış alarm verdi ve 3,6 kat daha uzun yazdı. Bu sonuç **videoya karşı** yönde, fakat anlamlı değil.
- **RES-EVAL-004 / 006 / 007:** Skill yüklüyken haiku hak edilmiş iddiaların %17–21'ini reddetti. Bunu düzeltmek için SKILL.md'ye eklenen kural iki kez çürütüldü. Bu, V2'nin mekanizmasının (harfiyen uygulama) bu repodaki gözlemi.

**Sonuç:** Videonun ana yönü (yalın yaz, modelin bilebileceğini silme, her
ayrıntı emir gibi okunur) iki üreticinin rehberiyle ve ETH çalışmasıyla
destekleniyor. Mizan'ın kendi ölçümleri de bununla çelişmiyor. Videonun kendi
kanıtı ise zayıf: anekdota dayalı, hakem yazarın kendisi, ve yaratıcı görevlerde
toplanmış. "Kısa brif denetimde de daha iyi" iddiası Mizan için açık bir
soru. EVAL-008'in H-EVAL-008b hipotezi bunu sınıyor.

## Eksik kart

Video maliyeti yalnızca bir kez anıyor ("maliyet de arttı"). Kısa promptlar
daha uzun sürdü ve daha pahalıya geldi. Bu, ETH bulgusunun tersi yönünde
bir maliyet ve videoda tartışılmıyor. Ayrıca başarısız kısa prompt denemeleri
gösterilmiyor.

## EVAL-008 sonrası (2026-10-09)

Tüm kollar tavana ulaştı (54/54 çalıştırmada tespit 1,000), bu yüzden V1 ve V3 için karar
okunamadı. Ölçülenler: 45 kelimelik kısa brif, 488 satırlık skill kadar hata buldu;
budanmış skill aynı tespitte %26 daha kısa cevap yazdı ve prompt token'ı 10,8 binden
2,7 bine indi; yanlış alarm yönü O 0,083 > C 0,056 > P 0,000 (tavan nedeniyle yalnızca ipucu).
Bu, V9'u ("modelin bilebileceğini sil") Mizan'ın hata tespiti işlevi için destekler yönde;
skill'in tespit dışındaki iddiaları ölçülmedi.
