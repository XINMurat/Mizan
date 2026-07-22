# Contributing to Mizan / Mizan'a Katkı

*(English first — Türkçe aşağıda.)*

Mizan is a methodology project, so it holds itself to its own discipline.
Contributions are welcome, but they must respect the hard rules the tool
enforces on everyone else.

---

## English

### Ground rules (the same R1–R8 the tool enforces)

1. **Preregister before you measure.** If a change claims an improvement,
   state the threshold and the refutation condition *before* showing the
   result. No HARKing.
2. **Append-only history.** Never delete or rewrite a refuted claim, a
   `[R]` entry, or a past result — mark it and keep it. (The one exception
   to git-history rewriting is removing genuinely private or personal data;
   that is done deliberately, not for tidiness.)
3. **Tier every claim.** In docs, PRs, and issues, tag non-obvious factual
   claims with `[K]/[H]/[S]/[R]/[KKE]/[Y]`. An untagged strong claim is a
   review comment waiting to happen.
4. **Name the arbiter.** Any claim with a numeric threshold states who
   returns the verdict on it. If the answer is "the person making the
   claim", the claim is capped at `[KKE]`; if there is no judge at all,
   drop the number rather than let it imply an oracle that does not exist.
5. **Bilingual parity is required.** Every user-facing doc change must land
   in **both** `docs/en/` and `docs/tr/` (and both halves of `README.md`,
   `CONTRIBUTING.md`, `docs/QUICKSTART.md`). A PR that updates only one
   language is incomplete. Keep the tier tags identical across languages.

### Before opening a PR

```bash
pip install -r tools/requirements.txt
# 1. registries must pass R1–R8 (English or Turkish messages):
python tools/mizan_validate.py examples/mizan-registry.example.yaml
# 2. enable the gate so bad registries can't be committed:
git config core.hooksPath tools/hooks
```

### Continuous integration (CI)

The badge at the top of the README —
`[![CI](…/actions/workflows/mizan.yml/badge.svg)](…)` — is **green when
`main` passes** two jobs, which run on every push and pull request
([`.github/workflows/mizan.yml`](.github/workflows/mizan.yml)):

- **validate-registries** — runs the R1–R8 validator on every
  `*mizan-registry*.yaml`, plus a self-test asserting the validator
  *rejects* a deliberately broken registry (so it can never silently pass
  everything).
- **skill-package-in-sync** — fails if `mizan.skill` drifts from
  `skill/mizan/`; rebuild the package after editing the skill.

**Reproduce CI locally before pushing** (same checks, no waiting):

```bash
# job 1: validate every registry
find . -path ./.git -prune -o -name '*mizan-registry*.y*ml' -print \
  | xargs -I{} python tools/mizan_validate.py {}
# job 2: skill package in sync with source
python - <<'PY'
import zipfile, os, sys
n = lambda b: b.replace(b"\r\n", b"\n"); z = zipfile.ZipFile("mizan.skill")
bad = [k for k in z.namelist()
       if not os.path.exists(os.path.join("skill", k))
       or n(z.read(k)) != n(open(os.path.join("skill", k), "rb").read())]
print("skill in sync" if not bad else "OUT OF SYNC: " + ", ".join(bad))
sys.exit(1 if bad else 0)
PY
```

**Check a run's status:** the **Actions** tab on GitHub, the README badge,
or the GitHub CLI:

```bash
gh run list --workflow mizan.yml     # recent runs + their conclusion
gh run watch                         # live-follow the current run
```

A PR is not done while CI is red.

If you change **any** file under `skill/mizan/`, rebuild the one-file
package so it stays in sync (the shipped `mizan.skill` embeds those files):

```bash
python - <<'PY'
import zipfile, os
with zipfile.ZipFile("mizan.skill", "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk("skill/mizan"):
        for f in files:
            p = os.path.join(root, f)
            z.write(p, os.path.relpath(p, "skill"))
print("rebuilt mizan.skill")
PY
```

### What lives where

- `skill/mizan/` — the portable skill (English canonical). Editing here is
  editing the product; rebuild `mizan.skill` after.
- `docs/en/`, `docs/tr/` — long-form docs, kept at parity.
- `tools/` — the R1–R8 validator and git hook (MIT).
- `examples/` — worked registries that MUST stay R1–R8-clean.

### Licensing of contributions

By contributing you agree your changes are licensed as the repo is: **MIT**
for code/schema, **CC-BY-4.0** for prose/methodology (see `LICENSE` and
`LICENSE-docs.md`). Do not add code under an incompatible license.

### Scope discipline

New features are gated (Mode 5). Before proposing one, state the problem
claim with its tier and source, a success metric AND a kill condition, and
at least one cheaper alternative plus the null alternative. "It would be
nice" is not a gate.

---

## Türkçe

Mizan bir metodoloji projesidir; bu yüzden kendi disiplinine kendisi de
uyar. Katkılar memnuniyetle karşılanır ama aracın herkese uyguladığı sert
kurallara saygı göstermek zorundadır.

### Temel kurallar (aracın uyguladığı R1–R8'nin aynısı)

1. **Ölçmeden önce önkaydet.** Bir değişiklik iyileştirme iddia ediyorsa,
   eşiği ve çürütme koşulunu sonucu göstermeden *önce* yaz. HARKing yok.
2. **Append-only geçmiş.** Çürüyen bir iddiayı, `[R]` girdisini veya geçmiş
   bir sonucu asla silme/yeniden yazma — işaretle ve tut. (Git geçmişini
   yeniden yazmanın tek istisnası, gerçekten özel/kişisel veriyi kaldırmak;
   bu "temizlik" için değil, bilinçli yapılır.)
3. **Her iddiayı katmanla.** Dokümanlarda, PR'larda, issue'larda apaçık
   olmayan olgusal iddiaları `[K]/[H]/[S]/[R]/[KKE]/[Y]` ile etiketle.
   Etiketsiz güçlü iddia, gelmeyi bekleyen bir inceleme yorumudur.
4. **Hakemi isimlendir.** Sayısal eşiği olan her iddia, o eşik üzerinde
   hükmü kimin verdiğini yazar. Cevap "iddiayı yapan kişi" ise iddia
   `[KKE]` tavanındadır; hiç hakem yoksa, var olmayan bir oracle'ı ima
   etmesin diye sayıyı tamamen kaldır.
5. **İki dillilik zorunlu.** Kullanıcıya dönük her doküman değişikliği
   **hem** `docs/en/` **hem** `docs/tr/` içine (ve `README.md`,
   `CONTRIBUTING.md`, `docs/QUICKSTART.md`'in her iki yarısına) girmeli.
   Tek dili güncelleyen PR eksiktir. Katman etiketlerini iki dilde birebir
   aynı tut.

### PR açmadan önce

```bash
pip install -r tools/requirements.txt
python tools/mizan_validate.py --lang tr examples/mizan-registry.example.yaml
git config core.hooksPath tools/hooks
export MIZAN_LANG=tr
```

### Sürekli entegrasyon (CI)

README'nin başındaki rozet —
`[![CI](…/actions/workflows/mizan.yml/badge.svg)](…)` — her push ve pull
request'te çalışan iki iş geçtiğinde **`main` için yeşildir**
([`.github/workflows/mizan.yml`](.github/workflows/mizan.yml)):

- **validate-registries** — R1–R8 validator'ını her `*mizan-registry*.yaml`
  üzerinde çalıştırır; ayrıca validator'ın **kasıtlı bozuk** bir registry'yi
  *reddettiğini* doğrulayan bir öz-test (yani hiçbir zaman sessizce her şeyi
  geçiremez).
- **skill-package-in-sync** — `mizan.skill`, `skill/mizan/` ile ayrışırsa
  başarısız olur; skill'i düzenledikten sonra paketi yeniden derle.

**Push'tan önce CI'ı yerelde tekrarla** (aynı kontroller, beklemesiz):

```bash
# 1. iş: her registry'yi doğrula
find . -path ./.git -prune -o -name '*mizan-registry*.y*ml' -print \
  | xargs -I{} python tools/mizan_validate.py --lang tr {}
# 2. iş: skill paketi kaynakla senkron mu — yukarıdaki İngilizce bölümdeki
#    tek-satırlık Python bloğunun aynısı.
```

**Bir koşunun durumunu kontrol et:** GitHub'daki **Actions** sekmesi, README
rozeti veya GitHub CLI:

```bash
gh run list --workflow mizan.yml     # son koşular + sonuçları
gh run watch                         # mevcut koşuyu canlı izle
```

CI kırmızıyken PR "bitti" sayılmaz.

`skill/mizan/` altında **herhangi** bir dosyayı değiştirirsen, tek-dosya
paketini yeniden derle (yayınlanan `mizan.skill` o dosyaları içinde
gömülü tutar) — komut yukarıdaki İngilizce bölümde.

### Ne nerede yaşar

- `skill/mizan/` — taşınabilir skill (İngilizce kanonik). Burayı düzenlemek
  ürünü düzenlemektir; sonra `mizan.skill`'i yeniden derle.
- `docs/en/`, `docs/tr/` — uzun-metin dokümanlar, paritede tutulur.
- `tools/` — R1–R8 doğrulayıcı ve git hook (MIT).
- `examples/` — R1–R8'den temiz kalması ZORUNLU çalışan registry'ler.

### Katkıların lisansı

Katkı vererek, değişikliklerinin repo ile aynı lisansta olduğunu kabul
edersin: kod/şema için **MIT**, metin/metodoloji için **CC-BY-4.0** (bkz.
`LICENSE` ve `LICENSE-docs.md`). Uyumsuz lisanslı kod ekleme.

### Kapsam disiplini

Yeni özellikler kapılıdır (Mod 5). Önermeden önce: problem iddiasını
katmanı ve kaynağıyla, bir başarı metriği VE bir kaldırma koşulu, en az bir
ucuz alternatif artı null alternatifi yaz. "Güzel olurdu" bir kapı değildir.
