# Kurul özeti incelemesi

Bu seti toplu olarak onaylayamam. Altı iddianın yalnızca ikisi (2 ve 5) kanıtla yeterince destekleniyor. Diğer dördünün her birinde belirli ve adı konabilecek bir kanıt eksiği var. Ekip liderinin güveni kanıt yerine geçmez.

## 1. Tıklama oranı %18 arttı — KANITLANMADI
- Karşılaştırma dönemi ya da kontrol grubu yok. %18'in neye göre ölçüldüğü tanımsız.
- 2 günlük dönemi ekip kendisi seçti. Bu, seçim yanlılığı ve kiraz toplama (cherry-picking) riski taşıyor. Hafta içi/sonu etkisi, kampanyalar ve mevsimsellik de kontrol edilmemiş.
- Sonucu, çıkarı olan ekip kendisi değerlendirmiş.
- Güven aralığı ve örneklem büyüklüğü verilmemiş.
- Düzeltme: 2. iddiadaki randomize deneyden tıklama oranını raporlayın. Bu metrik önceden kayıtlı değilse ikincil ya da keşifsel bulgu olarak etiketleyin.

## 2. Sepet değeri %3,1 yüksek (%95 GA 1,8–4,4) — KANITLANDI
- Randomizasyon (60.000 kullanıcı), önceden kaydedilmiş birincil metrik, güven aralığı ve bağımsız analiz var. Bunlar iddia için güçlü bir temel.
- Kurulda yapılmaması gereken şey: sonucu "gelir arttı" ya da "kâr arttı" diye genişletmek. Ölçülen metrik sepet değeri. Dönüşüm, iade ve marj ayrıca gösterilmeli.
- Deney süresi ile yenilik etkisi (novelty effect) belirtilmeli. Kalıcılık ayrı bir soru.

## 3. Kullanıcılar yeni motoru seviyor — KANITLANMADI
- Katılımcılar gerçek kullanıcı değil, 12 kişilik iç ekip. Motoru kendileri geliştirdikleri için çıkar çatışması ve sosyal istenirlik yanlılığı var.
- Örneklem çok küçük, kontrol ya da karşılaştırma yok, yöntem ve soru belgelenmemiş.
- "Kullanıcılar" genellemesi, kanıtın izin verdiğinin çok ötesine geçiyor.
- Düzeltme: Deney kollarında memnuniyet anketi ya da davranışsal tutma (retention) verisi kullanın.

## 4. Rakiplerden daha iyi öneri — KANITLANMADI
- Tek kaynak tedarikçinin kendi benchmark'ı, bu yüzden bağımsız değil ve çıkar çatışması var.
- Hangi rakipler, hangi veri seti ve hangi metrik kullanıldığı belli değil. Sonucun bizim kullanıcı kitlemize genellenebilirliği bilinmiyor.
- Düzeltme: Bağımsız bir karşılaştırma yapın ya da iddiayı "tedarikçi beyanına göre" diye açıkça etiketleyerek kurula sunun.

## 5. Sunucu maliyeti ayda 42.000 TL — KANITLANDI
- Denetlenmiş fatura, maliyet olgusu için uygun ve bağımsız bir kaynak.
- Uyarı: Rakam tek aya mı ait, yoksa ortalama mı, belirtilmeli. Trafik büyüdükçe maliyetin nasıl ölçekleneceği ve personel ile lisans gibi toplam sahip olma maliyeti bu rakama dahil değil.

## 6. Motor churn'ü azalttı — KANITLANMADI
- Aynı ay yapılan fiyat değişikliği doğrudan bir karıştırıcı (confound). Düşüşü motora atfetmek mümkün değil.
- Önce/sonra karşılaştırması tek aya dayanıyor. Mevsimsellik ve ortalamaya dönme (regression to the mean) etkisi dışlanmamış.
- Nedensellik iddia ediliyor, ama elde yalnızca zamansal bir çakışma var.
- Düzeltme: Randomize deneyin iki kolu arasındaki churn farkına bakın. Her iki kol da aynı fiyat değişikliğine maruz kaldığı için bu karşılaştırma karıştırıcıyı kontrol eder.

## Kurula öneri
Yalnızca 2 ve 5 kanıtlanmış olgu olarak sunulmalı. 1, 3, 4 ve 6 ya çıkarılmalı ya da açıkça "doğrulanmamış / hipotez" olarak etiketlenmeli. Deney verisi mevcut olduğu için 1 ve 6, yarına kadar randomize kollardan yeniden analiz edilebilir.

VERDICTS
1: NOT PROVEN
2: PROVEN
3: NOT PROVEN
4: NOT PROVEN
5: PROVEN
6: NOT PROVEN
