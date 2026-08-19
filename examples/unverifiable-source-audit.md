<!-- =====================================================================
Worked example — auditing a document whose source you cannot reach
Çalışılmış örnek — kaynağına ulaşamadığın bir dokümanı denetlemek
===================================================================== -->

# When the source is out of reach

The audit procedure in `SKILL.md` assumes something it never states: that the
auditor can, in principle, **check the claim against the world**. Atomize,
source each claim, tier it, hunt counter-examples — each step quietly presumes
reachable ground truth.

A common case violates that assumption. A user brings a document summarizing
an external work the auditor cannot access: published after the model's
knowledge cutoff, behind a paywall, internal to another organization, or
simply not fetchable in the current session. The document is *about* the world;
the auditor can only reach the *document*.

This is not a rare edge case. It is the default shape of "here is a report
someone sent me, is it any good?" And it has a specific failure mode that
looks nothing like a refusal.

---

## 1. The failure mode: tier laundering

The dangerous document here is not a sloppy one. It is a **well-made** one:
claims already atomized, evidence tiers already applied, limitations already
declared, independent commentary already quoted and weighed.

Faced with that, the auditor's cheapest path is to **inherit the document's own
tags**. The output looks like a rigorous audit — tier tags in place, format
intact, findings enumerated — and every tag in it is really a restatement of
what the document asserted about itself. A `[K]` that entered as the author's
self-assessment leaves as the auditor's verdict. Nothing was checked; the
tags were laundered.

Note how this differs from the anti-pattern `rigor cosplay` already in
`SKILL.md`. There, judgment is *softened* by a host instruction. Here judgment
is **delegated**, invisibly, to the audited party — and the more competently the
document is written, the more inviting the delegation.

---

## 2. The two surfaces, separated

The move that prevents laundering is to split the audit target in two before
starting, and to say which surface every finding comes from.

| Surface | Reachable? | What can be audited |
|---|---|---|
| **Internal** — the document as a text | yes | Consistency, tier drift, arithmetic, does the stated evidence support the stated tag, does the framing match the numbers, what is structurally missing |
| **External** — the world the document describes | no | Nothing. Not the paper, not the code, not the replications, not the quoted commentators |

Everything below comes from the internal surface. Stating that first is not a
disclaimer; it is the finding that determines the ceiling of every other one.

---

## 3. Preregistration (written before reading closely)

**Prediction:** a document with this much visible methodological apparatus will
still contain at least one place where the framing outruns the numbers it
itself reports, and at least one tag that is inherited rather than earned.

**Refutation condition:** if every tier tag in the document is traceable to
evidence the document itself supplies, and no framing/number gap appears, the
prediction is wrong and the document passes as internally sound.

**Two-sided:** a pass is genuinely informative here. It would mean the
remaining risk is entirely external — i.e. the only way to be wrong is for the
source itself to be wrong — which is a very different report to give the user
than "the summary overstates its source".

---

## 4. What the internal surface actually yields

Four finding types are available without any access to the source. They are
listed in the order of how much they buy.

**(a) Tier drift inside one document.** A figure stated in the main text and
then materially revised by a later analysis in the same document, with the
original left standing. The revision is the finding, and so is the fact that
the earlier number was not retracted. A reader who stops at the main text
carries away a number the document itself no longer supports.

**(b) Showcase-versus-systematic gaps.** A flagship example presented as a
clean demonstration, alongside a systematic success rate reported elsewhere
that is above chance but below half. Neither statement is false. The framing is
still misleading, and this is exactly the `three confirming anecdotes are
selection bias, a scored prediction record is evidence` rule applied to someone
else's document.

**(c) The document's own criterion, applied consistently.** If a document
states that self-refereed results cap at `[KKE]`, that criterion can be run
against every tag it assigns — including the ones where it applied the rule
correctly, which is worth saying too. An audit that reports only failures of a
document's stated standard, and never its correct applications, is producing a
hit rate over curated examples.

**(d) The missing card.** What does this document's *format* structurally omit?
For a report on a detection or auditing method: sensitivity and specificity.
Case studies establish that the method *can* fire; they say nothing about how
often it fires when it should not. The absence of a false-positive rate is a
finding available from the shape of the document alone.

None of (a)–(d) requires the source. All four are real findings. This is the
positive claim of the example: **an unreachable source does not reduce the
audit to a shrug** — it relocates it.

---

## 5. The proposed rule (NOT silently applied)

The rule set has no entry for this, and the gap is not covered by the existing
arbiter rule. That rule asks *who returns the verdict* and caps a claim whose
judge is its own author. Source reachability is a different axis: a source can
have a perfectly independent arbiter and still be unreachable **by the
auditor**. An audit that leans on a verdict it cannot inspect is self-report at
one remove.

> **Proposed:** *Source reachability caps the tier.* A claim whose source the
> auditor cannot reach may not exceed `[KKE]` in the auditor's own output,
> regardless of how the source tiers it. The auditor's tags describe the
> auditor's evidence, never the source's. Where the source's tags are
> reported, they are quoted as the source's claims, not adopted.

**Illet:** a tier is a statement about the evidence *available to the person
assigning it*. Adopting a tag assembled from evidence you cannot see makes the
tag describe someone else's epistemic position while carrying your name.

**Breaking point:** the rule collapses degrees of unreachability that are not
equal. A source unreachable in this session but trivially fetchable in the
next, a paywalled paper with a public abstract, and a source that does not
exist all land in the same bucket. A finer rule would grade them; this one does
not, and would flatten a fetch-and-recheck into a permanent cap.

**Why it is written here and not patched into `SKILL.md`:** changing the rule
set is a method change, and this project's own contribution rules require a
method change to arrive with its illet and its breaking point rather than with
a plausible rationale. Both are above. The decision belongs to the maintainer,
in the open, as a proposal — which is also the honest way to handle the fact
that the rule was generated from a single encounter with a single document.

---

## 6. What this does NOT establish

- Nothing about the external document that triggered it. The source is left
  unnamed on purpose: a worked example that hard-codes unverified factual
  claims about a real paper rots when they turn out wrong, and nobody
  revisits an example.
- Not that the four finding types are exhaustive. They are what one pass
  produced.
- Not that the proposed rule improves audit quality. That is `[S]` — it has one
  motivating case and no comparison against auditing without it.
- The document that motivated this example was, on the internal surface, mostly
  sound: it caught its own showcase-versus-systematic gap and applied its own
  self-referee criterion correctly in the section where it mattered most. An
  example built only on a bad document would teach the wrong lesson, because
  the laundering risk is highest with a good one.

## 7. What would upgrade it

- Run the same pass on several unreachable-source documents of differing
  quality and record which of the four finding types fire, and how often. That
  turns "these findings are available" from an assertion into a rate.
- A control: the same document audited by someone *with* source access, to see
  which internal-surface findings survive contact with the external one — and,
  more usefully, which real problems the internal surface could never have
  caught.
- A graded version of the reachability rule, distinguishing
  not-in-this-session from not-in-principle.

---

## Türkçe özet

Bu örnek, `SKILL.md`'nin sessizce varsaydığı bir koşulun çiğnendiği durumu
işler: denetçinin iddiayı **dünyaya karşı** kontrol edebilmesi. Kullanıcı,
denetçinin erişemediği bir dış çalışmayı özetleyen bir doküman getirdiğinde
(kesim tarihi sonrası, ödeme duvarı ardında, başka bir kurumun içinde) bu
koşul yoktur.

**Asıl tehlike özensiz doküman değil, iyi yazılmış dokümandır.** İddiaları
ayrıştırılmış, katmanları atanmış, sınırları beyan edilmiş bir metin karşısında
en ucuz yol, dokümanın kendi etiketlerini devralmaktır. Çıktı denetim gibi
görünür, ama her etiket dokümanın kendisi hakkındaki beyanının tekrarıdır:
**katman aklama**. Bu, mevcut `rigor cosplay` anti-deseninden farklıdır — orada
yargı *yumuşatılır*, burada denetlenen tarafa *devredilir*, ve doküman ne kadar
iyi yazılmışsa devir o kadar davetkârdır.

Çözüm, başlamadan önce hedefi ikiye ayırmak: **içsel yüzey** (metnin kendisi —
tutarlılık, katman kayması, çerçeveleme-sayı uyumu, yapısal eksik) erişilebilir;
**dışsal yüzey** (makale, kod, replikasyonlar) erişilemez. İçsel yüzey dört
gerçek bulgu türü verir: (a) doküman içi katman kayması, (b) vitrin-örnek ile
sistematik oran arasındaki uçurum, (c) dokümanın kendi ölçütünün kendi
etiketlerine tutarlı uygulanması — doğru uyguladığı yerler dahil, (d) formatın
yapısal olarak atladığı kart (bir tespit yöntemi raporunda: yanlış-pozitif
oranı). Yani **erişilemeyen kaynak denetimi omuz silkmeye indirgemez; yerini
değiştirir.**

Önerilen kural — *kaynak erişilebilirliği katmanı tavanlar*: denetçinin
ulaşamadığı bir kaynağa dayanan iddia, kaynak onu nasıl etiketlerse etiketlesin,
denetçinin kendi çıktısında `[KKE]`'yi aşamaz. Bu, hakem kuralından farklı bir
eksendir: kaynağın hakemi tam bağımsız olabilir ve yine de denetçi için
erişilemez olabilir. Kural **sessizce uygulanmadı**, öneri olarak yazıldı —
illeti ve kırılma noktası yukarıda; yöntem değişikliği kararı bakımın işidir.
