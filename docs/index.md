---
title: "Mizan — Evidence-Tiered Auditing & Preregistration"
description: "A Claude skill that turns an experimental-science discipline into a portable tool for evaluating any claim set and maintaining living hypothesis registries."
---

# Mizan

<div id="pane-en" markdown="1">

**Evidence-tiered auditing and preregistration methodology, packaged as a Claude skill.**

[Repository](https://github.com/XINMurat/Mizan) ·
[Latest release](https://github.com/XINMurat/Mizan/releases/latest) ·
[Kıyas](https://github.com/XINMurat/Kiyas) ·
[İskele](https://github.com/XINMurat/Iskele) ·
[ux-mizan](https://github.com/XINMurat/ux-mizan) ·
[**the family**](https://xinmurat.github.io/)

---

## English

Mizan (Turkish/Arabic: *the scale*) turns a rigorous experimental-science
discipline into a portable tool for evaluating **any** claim set — an
AI-generated summary, a project report, a year-in-review, a codebase, a PRD —
and for maintaining living hypothesis registries.

Its core commitments: every claim gets an evidence tier, with no untagged
assertions. Thresholds are locked before results, or the HARKing risk is
declared rather than silently absorbed. Every hypothesis carries a refutation
condition — a claim that cannot fail is not audited, it is decorated. Refuted
entries are never deleted. A surprising positive waits for its symmetric
control before it gets a headline. And three confirming anecdotes are selection
bias; a scored prediction record is evidence.

- [Quickstart](QUICKSTART.md) — install, create a registry, validate it
- [Usage guide](en/usage-guide.md) — the five modes, the hard rules, common mistakes
- [Reference](en/reference.md) — where every part of the methodology lives
- [Project instructions](en/project-instructions.md) — dropping Mizan into a project

**Worked examples** (in the repository): a
[registry that passes every rule](https://github.com/XINMurat/Mizan/blob/main/examples/mizan-registry.example.yaml),
the [portability runs](https://github.com/XINMurat/Mizan/blob/main/examples/portability-across-hosts.md)
that test whether the discipline survives a hostile setup, and
[auditing a document whose source you cannot reach](https://github.com/XINMurat/Mizan/blob/main/examples/unverifiable-source-audit.md) —
where the failure mode is not refusal but **tier laundering**.

The registry schema has an LLM-free validator (rules R1–R22, plus a
non-blocking warning channel). It enforces the mechanical invariants and
nothing else: semantic judgement stays with a human or a frontier model, which
is rule R7 itself.

</div>

<div id="pane-tr" markdown="1" class="pane-init">

**Kanıt-katmanlı denetim ve önkayıt metodolojisi — bir Claude skill'i olarak paketlenmiş.**

[Depo](https://github.com/XINMurat/Mizan) ·
[Son sürüm](https://github.com/XINMurat/Mizan/releases/latest) ·
[Kıyas](https://github.com/XINMurat/Kiyas) ·
[İskele](https://github.com/XINMurat/Iskele) ·
[ux-mizan](https://github.com/XINMurat/ux-mizan) ·
[**aile sayfası**](https://xinmurat.github.io/)

---

## Türkçe

Mizan (terazi/ölçü), titiz bir deneysel-bilim disiplinini **herhangi bir**
iddia setini değerlendirmek ve canlı hipotez registry'leri sürdürmek için
taşınabilir bir araca dönüştürür.

Temel taahhütler: her iddia bir kanıt katmanı alır, etiketsiz iddia olmaz.
Eşikler sonuç görülmeden önce kilitlenir; mümkün değilse HARKing riski
sessizce soğurulmaz, açıkça beyan edilir. Her hipotez bir çürütme koşulu
taşır — başarısız olamayan iddia denetlenmiş değil, süslenmiştir. Çürütülen
girdiler silinmez. Sürpriz pozitif, manşetten önce simetrik kontrolünü
bekler. Ve üç doğrulayıcı anekdot seçilim yanlılığıdır; puanlanmış bir tahmin
kaydı kanıttır.

- [Hızlı başlangıç](QUICKSTART.md) — kur, bir registry aç, doğrula
- [Kullanım kılavuzu](tr/kullanim-kilavuzu.md) — beş mod, sert kurallar, sık hatalar
- [Metodoloji](tr/metodoloji.md) — skill'in tam Türkçe karşılığı (Mod 1–2)
- [Yazılım modları](tr/yazilim-modlari.md) — kod denetimi, bug registry'si, PRD kapısı (Mod 3–5)
- [Alan uyarlama](tr/alan-uyarlama.md) — yazılım dışındaki 14 alan
- [Proje talimatı](tr/proje-talimati.md) — Claude Project alanına yapıştırılacak blok

</div>

---

## The family

**İskele kurar · Mizan tartar · Kıyas üretir.**
[İskele](https://github.com/XINMurat/Iskele) turns a vague project intent into
an executable delivery kit. Mizan audits claims and maintains preregistered
registries. [Kıyas](https://github.com/XINMurat/Kiyas) generates the candidates
Mizan weighs, and a Mizan registry's refuted entries flow back to Kıyas as
negative constraints — the loop closes.
