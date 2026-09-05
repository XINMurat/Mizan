#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mizan registry validator — LLM-free static enforcement of hard rules R1–R21.

This is the cheap, judgment-free baseline of feature FEAT-M001 (in the
project's roadmap registry). It does NOT evaluate the *quality* of a
hypothesis; it only checks the mechanical, machine-checkable invariants of
the mizan-registry.yaml schema. Semantic judgment stays with a human or a
frontier model (that separation is rule R7 itself).

Bilingual: messages are emitted in the requested language (--lang tr|en).

TWO CHANNELS, and the reason there are two. Every rule here blocks, which
sounds like rigor and is not: a tool that can only stop you teaches authors
to write registries that do not trigger it, and that is a different skill
from writing honest ones. Some findings are usually-wrong-but-legitimately-
right-often-enough that stopping on them would be false precision. So:

  * VIOLATIONS (R1-R21) block. They mark a registry that is incomplete in a
    way the prose forbids outright.
  * WARNINGS (W1-W4) do not block by default. They mark shapes worth a
    second look. `--strict` promotes them to violations; CI runs strict,
    local runs do not.

Ported from the sibling Kiyas validator, where the same split exists for the
same reason (its G6 design note: if every flag blocked promotion, authors
would learn to leave the sweep silent).

Usage:
    python tools/mizan_validate.py path/to/mizan-registry.yaml
    python tools/mizan_validate.py --lang tr registry.yaml
    python tools/mizan_validate.py --against HEAD registry.yaml   # append-only check
    python tools/mizan_validate.py --strict registry.yaml         # warnings fail too

Exit code 0 = clean, 1 = violations found, 2 = usage/parse error.

Dependency: PyYAML  (pip install pyyaml)
"""
from __future__ import annotations

import argparse
import datetime
import re
import subprocess
import sys
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write(
        "ERROR: PyYAML is required. Install it with: pip install pyyaml\n"
        "HATA: PyYAML gerekli. Kurulum: pip install pyyaml\n"
    )
    sys.exit(2)

# R10 — "Lock thresholds numerically. 'Improves things' is not a threshold;
# 'ΔPPL ≤ −3%' or 'counter-example rate < 1 per 10 sources' is." Deliberately
# permissive: any digit counts. The rule is aimed at prose that names no
# quantity at all, not at policing how the quantity is expressed.
HAS_NUMBER = re.compile(r"\d")

VALID_TIERS = {"K", "H", "S", "R", "KKE", "Y"}

# R8 applies to hypotheses, and from schema 1.3 to features and bugs as well;
# the message has to say which, or a feature's missing arbiter reads as a
# hypothesis that does not exist.
KIND_LABEL = {
    "hypothesis": ("hypothesis", "hipotez"),
    "feature": ("feature", "feature"),
    "bug": ("bug", "bug"),
}
ARBITER_CLASSES = {"runtime", "instrument", "third_party", "author", "none"}

# Bilingual message catalog: key -> (en, tr)
MSG = {
    "R1_no_threshold": (
        "R1: hypothesis {id} is referenced by result {rid} but has no locked threshold (HARKing risk).",
        "R1: {id} hipotezine {rid} sonucu atıfta bulunuyor ama kilitli eşiği yok (HARKing riski).",
    ),
    "R1_no_refutation": (
        "R1: hypothesis {id} has no refutation condition — a claim that cannot fail is not audited.",
        "R1: {id} hipotezinin çürütme koşulu yok — başarısız olamayan iddia denetlenmiş değildir.",
    ),
    "R1_threshold_incomplete": (
        "R1: hypothesis {id} threshold must define both 'support' and 'refute'.",
        "R1: {id} hipotezinin eşiği hem 'support' hem 'refute' tanımlamalı.",
    ),
    "R2_no_baseline": (
        "R2: experiment {id} has no baseline and no written justification for its absence.",
        "R2: {id} deneyinin baseline'ı yok ve yokluğu için yazılı gerekçe de yok.",
    ),
    "R2_baseless_promotes_K": (
        "R2: result {id} rests on a baseline-less experiment ({eid}) yet proposes promotion to K — forbidden.",
        "R2: {id} sonucu baseline'sız bir deneye ({eid}) dayanıyor ama K'ya terfi öneriyor — yasak.",
    ),
    "R3_confound_uncontrolled": (
        "R3: confound '{c}' from hypothesis {hid} is neither controlled nor accepted in experiment {eid}.",
        "R3: {hid} hipotezindeki '{c}' confound'u, {eid} deneyinde ne kontrol edilmiş ne kabul edilmiş.",
    ),
    "R3_no_controls": (
        "R3: experiment {eid} lists confounds via its hypotheses but has no confound_controls block.",
        "R3: {eid} deneyi hipotezleri üzerinden confound taşıyor ama confound_controls bloğu yok.",
    ),
    "R4_history_shrank": (
        "R4: append-only violated — {kind} '{id}' history lost entries vs. baseline ({old} -> {new}).",
        "R4: append-only ihlali — {kind} '{id}' geçmişi baseline'a göre girdi kaybetti ({old} -> {new}).",
    ),
    "R4_entry_deleted": (
        "R4: append-only violated — {kind} '{id}' present in baseline is missing now (deletion of record).",
        "R4: append-only ihlali — baseline'da olan {kind} '{id}' şimdi yok (kayıt silinmiş).",
    ),
    "R5_empty_annexes": (
        "R5: result {id} has empty or missing honesty_annexes (mandatory, non-empty).",
        "R5: {id} sonucunun honesty_annexes'i boş veya eksik (zorunlu, boş olamaz).",
    ),
    "R6_surprising_no_control": (
        "R6: result {id} is a surprising_positive proposing K, but confound_control_result is empty.",
        "R6: {id} sonucu K öneren bir surprising_positive ama confound_control_result boş.",
    ),
    "R7_self_confirmed": (
        "R7: hypothesis {hid} is at tier {tier} but the driving result {id} has no decision_confirmed_by — promoted without independent confirmation (producer≠sole auditor).",
        "R7: {hid} hipotezi {tier} katmanında ama onu taşıyan {id} sonucunda decision_confirmed_by boş — bağımsız onay olmadan terfi (üretici≠tek denetçi).",
    ),
    "R8_no_arbiter": (
        "R8: {kind} {id} has no arbiter block — a locked threshold with no named judge is self-report.",
        "R8: {kind} {id} girdisinde hakem bloğu yok — hakemi isimlendirilmemiş kilitli eşik öz-beyandır.",
    ),
    "R8_bad_class": (
        "R8: {kind} {id} has invalid arbiter.class '{cls}' (allowed: runtime instrument third_party author none).",
        "R8: {kind} {id} girdisinde geçersiz arbiter.class '{cls}' (izinli: runtime instrument third_party author none).",
    ),
    "R8_no_who": (
        "R8: {kind} {id} names arbiter.class '{cls}' but not arbiter.who — the concrete judge is missing.",
        "R8: {kind} {id} arbiter.class '{cls}' diyor ama arbiter.who boş — somut hakem yok.",
    ),
    "R8_author_promotes_K": (
        "R8: {kind} {id} is at tier K but its arbiter is class '{cls}' — self-judged claims stay at KKE.",
        "R8: {kind} {id} K katmanında ama hakemi '{cls}' sınıfında — kendi kendini yargılayan iddia KKE'de kalır.",
    ),
    "R8_none_leaves_S": (
        "R8: {kind} {id} has arbiter.class 'none' but tier '{tier}' — with no arbiter the threshold is decorative; tier stays S.",
        "R8: {kind} {id} arbiter.class'ı 'none' ama tier '{tier}' — hakemsiz eşik dekoratiftir; tier S'de kalır.",
    ),
    "R8_no_calibration": (
        "R8: {kind} {id} uses arbiter.class '{cls}' without arbiter.calibration — thresholds are not inherited across instruments (write 'unknown' if that is the truth).",
        "R8: {kind} {id} '{cls}' hakem sınıfını arbiter.calibration olmadan kullanıyor — eşikler enstrümanlar arası miras alınmaz ('unknown' yazmak da geçerli cevaptır).",
    ),
    "R8_independence_contradiction": (
        "R8: {kind} {id} declares arbiter.class '{cls}' with independent_of_author: true — that class is by definition not independent.",
        "R8: {kind} {id} arbiter.class '{cls}' ile independent_of_author: true beyan ediyor — bu sınıf tanımı gereği bağımsız değil.",
    ),
    "R13_no_kill_condition": (
        "R13: feature {id} has no kill_condition — a feature with no defined end accumulates as "
        "permanent maintenance debt. Name the post-ship measurement that would justify removing it.",
        "R13: {id} feature'ında kill_condition yok — sonu tanımlanmamış bir özellik kalıcı bakım "
        "borcu olarak birikir. Onu kaldırmayı haklı çıkaracak yayın-sonrası ölçümü adlandır.",
    ),
    "R14_no_alternatives": (
        "R14: feature {id} lists no alternatives — every feature entry competes against at least "
        "one cheaper option and the null alternative, on the SAME value metric.",
        "R14: {id} feature'ı hiç alternatif listelemiyor — her feature girdisi, AYNI değer metriği "
        "üzerinde en az bir ucuz seçenek ve null alternatifle yarışır.",
    ),
    "R14_missing_kind": (
        "R14: feature {id} has no '{kind}' alternative — {why}",
        "R14: {id} feature'ında '{kind}' alternatifi yok — {why}",
    ),
    "R15_no_rivals": (
        "R15: bug {id} lists no rival_hypotheses — a mechanism with no rival is a story, not a "
        "hypothesis; nothing distinguishes it from the first explanation that came to mind.",
        "R15: {id} bug'ında rival_hypotheses yok — rakibi olmayan mekanizma hipotez değil hikâyedir; "
        "onu akla ilk gelen açıklamadan ayıran hiçbir şey yok.",
    ),
    "bad_tier": (
        "SCHEMA: {kind} '{id}' has invalid tier '{tier}' (allowed: K H S R KKE Y).",
        "ŞEMA: {kind} '{id}' geçersiz tier '{tier}' taşıyor (izinli: K H S R KKE Y).",
    ),
    "R9_K_without_evidence": (
        "R9: {kind} {id} sits at [K] with no supporting result and no external_evidence — "
        "[K] means direct evidence, source cited, threshold met. Writing the tier is not the same "
        "as earning it.",
        "R9: {kind} {id} [K] katmanında ama ne destekleyen bir sonuç ne external_evidence var — "
        "[K] doğrudan kanıt, kaynak gösterimi ve karşılanmış eşik demektir. Tier'ı yazmak, onu "
        "hak etmekle aynı şey değildir.",
    ),
    "R10_threshold_not_numeric": (
        "R10: {kind} {id} threshold.{side} names no quantity ('{text}') — 'improves things' is not "
        "a threshold. Add a number, or state threshold.non_numeric_justification.",
        "R10: {kind} {id} threshold.{side} hiçbir nicelik adlandırmıyor ('{text}') — 'iyileştirir' "
        "bir eşik değildir. Bir sayı ekle ya da threshold.non_numeric_justification yaz.",
    ),
    "R11_no_tier": (
        "R11: {kind} {id} carries no tier — every claim gets an evidence tier; no untagged "
        "assertions.",
        "R11: {kind} {id} hiçbir tier taşımıyor — her iddia bir kanıt katmanı alır; etiketsiz "
        "iddia olmaz.",
    ),
    "R12_missing_field": (
        "R12: {kind} {id} has no {field} — templates.md: every entry field is mandatory except "
        "prior art, which must still be PRESENT (\"no known relatives\" is an answer; silence is not).",
        "R12: {kind} {id} girdisinde {field} yok — templates.md: prior art dışında her alan "
        "zorunludur; prior art da MEVCUT olmalıdır (\"bilinen akraba yok\" bir cevaptır, sessizlik değil).",
    ),
    "R12_metric_no_instrument": (
        "R12: {kind} {id} metric names no instrument — a threshold whose number has no named "
        "producer is R8's problem on the measurement side.",
        "R12: {kind} {id} girdisinin metric'i enstrüman adlandırmıyor — sayısını üreten şeyi "
        "adlandırmamış eşik, R8'in ölçüm tarafındaki hâlidir.",
    ),
    "R18_no_data_status": (
        "R18: hypothesis {id} is marked preregistered but does not say whether the data already "
        "exists. Registration is not preregistration if the data exists and you have seen it -- "
        "that is postdiction, and the difference is the whole claim. Add data_status: "
        "not_collected / exists_unseen / exists_partially_seen / exists_seen.",
        "R18: {id} hipotezi önkayıtlı işaretli ama verinin zaten var olup olmadığını söylemiyor. "
        "Veri varsa ve görüldüyse bu önkayıt değil sonradan-tahmindir; iddianın tamamı bu farkta "
        "durur. data_status ekle: not_collected / exists_unseen / exists_partially_seen / "
        "exists_seen.",
    ),
    "R18_bad_data_status": (
        "R18: hypothesis {id} has data_status '{value}', which is not one of "
        "not_collected / exists_unseen / exists_partially_seen / exists_seen.",
        "R18: {id} hipotezinin data_status değeri '{value}' — şu dördünden biri olmalı: "
        "not_collected / exists_unseen / exists_partially_seen / exists_seen.",
    ),
    "R18_seen_data_preregistered": (
        "R18: hypothesis {id} declares data_status '{value}' AND claims to be preregistered. "
        "A hypothesis written against data its author has already seen cannot be preregistered; "
        "record it honestly as post-hoc and drop the preregistration claim.",
        "R18: {id} hipotezi data_status '{value}' diyor ve aynı anda önkayıtlı olduğunu iddia "
        "ediyor. Yazarının gördüğü veriye karşı yazılmış bir hipotez önkayıtlı olamaz; dürüstçe "
        "post-hoc olarak kaydet ve önkayıt iddiasını düşür.",
    ),
    "R18_no_stopping_rule": (
        "R18: hypothesis {id} is preregistered with a threshold but no stopping rule. Without one, "
        "'collect until it crosses' is available and the threshold stops deciding anything. State "
        "stopping_rule: the n, or the condition under which collection ends.",
        "R18: {id} hipotezi eşikli ve önkayıtlı ama durdurma kuralı yok. O olmadan 'geçene kadar "
        "topla' mümkündür ve eşik hiçbir şeye karar vermez. stopping_rule yaz: n, ya da toplamanın "
        "biteceği koşul.",
    ),
    "R18_no_exclusion_rule": (
        "R18: hypothesis {id} is preregistered with a threshold but names no exclusion rule. "
        "Dropping a point under a rule invented after seeing it is HARKing wearing a data-cleaning "
        "hat. Write exclusion_rule now -- 'none' is a valid answer, silence is not.",
        "R18: {id} hipotezi eşikli ve önkayıtlı ama dışlama kuralı yok. Bir noktayı, gördükten "
        "sonra icat edilmiş bir kuralla atmak, veri temizliği kılığında HARKing'dir. exclusion_rule "
        "şimdi yazılır — 'yok' geçerli bir cevaptır, sessizlik değildir.",
    ),
    "R17_no_review_by": (
        "R17: hypothesis {id} is open ({status}) with no review_by date — a preregistration with "
        "no deadline is not a commitment, it is an intention. Set review_by when you preregister.",
        "R17: {id} hipotezi açık ({status}) ama review_by tarihi yok — son tarihi olmayan bir "
        "önkayıt taahhüt değil niyettir. Önkayıt anında review_by yaz.",
    ),
    "R17_review_overdue": (
        "R17: hypothesis {id} passed its review_by ({due}) on {asof} and records no decision. An "
        "untested [H] that nobody closes becomes permanent by default — decide: extend with a "
        "reason and a new review_by, park it (status: dormant), or close it.",
        "R17: {id} hipotezi review_by tarihini ({due}) {asof} itibarıyla geçti ve hiçbir karar "
        "kaydetmiyor. Kimsenin kapatmadığı, test edilmemiş bir [H] varsayılan olarak kalıcılaşır — "
        "karar ver: gerekçe ve yeni bir review_by ile uzat, beklet (status: dormant), ya da kapat.",
    ),
    "R17_bad_date": (
        "R17: hypothesis {id} has review_by {due!r}, which is not an ISO date (YYYY-MM-DD). A "
        "deadline nobody can compare against is not a deadline.",
        "R17: {id} hipotezinin review_by değeri {due!r} — ISO tarih (YYYY-AA-GG) değil. "
        "Karşılaştırılamayan bir son tarih, son tarih değildir.",
    ),
    "R16_coverage_claim_unearned": (
        "R16: coverage claims tier K but {why} — \"each slice fully audited\" is not \"the target "
        "fully audited\", and presenting the second as the first is itself a [Y].",
        "R16: coverage tier K iddia ediyor ama {why} — \"her dilim tam denetlendi\", \"hedef tam "
        "denetlendi\" demek değildir; ikincisini birincisi gibi sunmak başlı başına [Y]'dir.",
    ),
    "R19_scenario_incomplete": (
        "R19: domain probe scenario {id} is missing {missing} — a scenario with no situation is not "
        "a probe, and one with no outcome was not run.",
        "R19: alan probu senaryosu {id} eksik: {missing} — durumu yazılmamış bir senaryo prob "
        "değildir; sonucu yazılmamış olan ise koşulmamıştır.",
    ),
    "R19_bad_outcome": (
        "R19: domain probe scenario {id} has outcome {got!r}; expected one of {allowed}.",
        "R19: alan probu senaryosu {id} sonucu {got!r}; beklenen: {allowed}.",
    ),
    "R19_coverage_unprobed": (
        "R19: coverage claims tier K but {why} — checklist item 12 is the only pass whose evidence "
        "is an ABSENCE: an unclaimed capability produces no claim to tier, so no amount of "
        "atomizing reaches it. A coverage claim made without it covers the document, not the domain.",
        "R19: coverage tier K iddia ediyor ama {why} — kontrol listesi madde 12, kanıtı bir YOKLUK "
        "olan tek pas: iddia edilmemiş bir yetenek katmanlanacak iddia üretmez, atomize etmek ona "
        "asla ulaşmaz. Bu pas olmadan yapılan kapsam iddiası alanı değil, dokümanı kapsar.",
    ),
    "R20_pair_incomplete": (
        "R20: conjunction pair {id} is missing {missing} — a pair is a feature AND the existing "
        "guarantee it can reach; either one alone is just a feature review.",
        "R20: bileşim çifti {id} eksik: {missing} — çift, bir özellik VE onun dokunabildiği mevcut "
        "garantidir; tek başına biri yalnızca özellik incelemesidir.",
    ),
    "R20_bad_outcome": (
        "R20: conjunction pair {id} has outcome {got!r}; expected one of {allowed}.",
        "R20: bileşim çifti {id} sonucu {got!r}; beklenen: {allowed}.",
    ),
    "R20_coverage_unpaired": (
        "R20: coverage claims tier K but {why} — atomizing is the act of taking claims apart, so a "
        "defect that exists only when two features hold AT ONCE was destroyed by step 1 of the "
        "audit and cannot reappear later. A green test suite is not counter-evidence: tests are "
        "written per feature and are silent about the pair.",
        "R20: coverage tier K iddia ediyor ama {why} — atomize etmek, iddiaları parçalara ayırma "
        "eylemidir; yalnızca iki özellik AYNI ANDA geçerliyken var olan kusur, denetimin 1. "
        "adımında yok edilir ve sonraki adımlarda geri gelmez. Yeşil test paketi karşı kanıt "
        "değildir: testler özellik başına yazılır ve çift hakkında sessizdir.",
    ),
    "R21_escape_unclassed": (
        "R21: escape {id} names neither class_ref nor class_new — the scorecard already counts "
        "escapes and calls that count the only measure that cannot be gamed from inside the audit. "
        "A count is not a loop: until the escape becomes a class, nothing catches the next one.",
        "R21: {id} kaçağı ne class_ref ne class_new belirtiyor — puan kartı kaçakları zaten sayıyor "
        "ve o sayıyı, denetimin içinden oynanamayacak tek ölçü diye adlandırıyor. Sayı, döngü "
        "değildir: kaçak bir sınıfa dönüşene kadar bir sonrakini hiçbir şey yakalamaz.",
    ),
    "R21_escape_incomplete": (
        "R21: escape {id} is missing {missing}.",
        "R21: {id} kaçağı eksik: {missing}.",
    ),
    "W5_no_probe": (
        "W5: the registry has a coverage block but no {which} probe — below a tier-K claim R19/R20 "
        "do not fire, and these are the two passes that find what tests cannot, so they are also "
        "the two easiest to skip in silence.",
        "W5: kayıt defterinde coverage bloğu var ama {which} probu yok — tier-K iddiası altında "
        "R19/R20 devreye girmez; bunlar testlerin göremediğini bulan iki pas olduğu için sessizce "
        "atlanması da en kolay olanlardır.",
    ),
    "W4_no_merge_row": (
        "W4: the coverage ledger has phase rows but no MERGE row — reconciliation is where a phased "
        "audit is weakest (a claim in one slice verified only by evidence in another), so it is "
        "planned up front or it is skipped.",
        "W4: coverage defterinde faz satırları var ama MERGE satırı yok — uzlaştırma, fazlı "
        "denetimin en zayıf yeridir (bir dilimdeki iddianın yalnızca başka bir dilimdeki kanıtla "
        "doğrulanması), o yüzden ya baştan planlanır ya atlanır.",
    ),
    "W1_no_two_sided": (
        "W1: {kind} {id} has no two_sided statement — if only one outcome teaches something, the "
        "test is worth redesigning before it runs.",
        "W1: {kind} {id} girdisinde two_sided beyanı yok — yalnızca tek sonuç bir şey öğretiyorsa, "
        "test koşmadan önce yeniden tasarlanmaya değer.",
    ),
    "W2_open_no_threshold": (
        "W2: {kind} {id} has no result yet and no {missing} — the entry is written BEFORE the test, "
        "and R1 only starts checking once a result references it.",
        "W2: {kind} {id} henüz sonuçsuz ve {missing} yok — girdi testten ÖNCE yazılır; R1 ise ancak "
        "bir sonuç ona atıfta bulununca devreye girer.",
    ),
    "W3_all_K": (
        "W3: all {n} tiered entries are at [K] — 'a tiered report where every claim lands in K' is "
        "the flattery problem wearing a lab coat. Legitimate, but worth checking the sources.",
        "W3: {n} etiketli girdinin hepsi [K] — 'her iddiası K'ya inen tierlı rapor', laboratuvar "
        "önlüğü giymiş iltifat problemidir. Meşru olabilir, ama kaynakları kontrol etmeye değer.",
    ),
    "clean": (
        "OK — {n} entries checked, no R1–R21 violations.",
        "OK — {n} girdi kontrol edildi, R1–R21 ihlali yok.",
    ),
    "found": (
        "{n} violation(s) found.",
        "{n} ihlal bulundu.",
    ),
    "warn_header": (
        "{n} warning(s) — not blocking; re-run with --strict to treat them as failures.",
        "{n} uyarı — bloke etmiyor; hata saymak için --strict ile yeniden koş.",
    ),
    "warn_strict": (
        "{n} warning(s) promoted to violations by --strict.",
        "{n} uyarı --strict ile ihlale yükseltildi.",
    ),
}


def m(key: str, lang: str, **kw: Any) -> str:
    en, tr = MSG[key]
    return (tr if lang == "tr" else en).format(**kw)


# Feature entries in the wild use references/feature-gate.md's vocabulary
# ("value metric", "success threshold"), while schema 1.3 maps those onto the
# hypothesis fields so R1/R8 apply without a second implementation. Both names
# are accepted: renaming a maintainer's existing entries would be a migration
# that buys nothing, and the mapping is the point, not the spelling.
FIELD_ALIASES = {
    "metric": ("metric", "value_metric"),
    "threshold": ("threshold", "success_threshold"),
    "acceptance_criteria": ("acceptance_criteria",
                            "acceptance_criteria_refutation_phrased"),
}


def _field(e: dict, canonical: str) -> Any:
    """Read a field by its canonical name, falling back to accepted aliases."""
    for name in FIELD_ALIASES.get(canonical, (canonical,)):
        if e.get(name) not in (None, "", [], {}):
            return e.get(name)
    return None


def _s(v: Any) -> str:
    return (v or "").strip() if isinstance(v, str) else ("" if v is None else str(v).strip())


def load(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise ValueError("top-level YAML is not a mapping")
    return data


def load_git_baseline(ref: str, path: str) -> dict | None:
    """Load the registry as it exists at a git ref, for the append-only check."""
    try:
        out = subprocess.run(
            ["git", "show", f"{ref}:{path}"],
            capture_output=True, text=True, check=True,
        ).stdout
    except Exception:
        return None
    try:
        data = yaml.safe_load(out)
        return data if isinstance(data, dict) else None
    except Exception:
        return None


OPEN_STATUSES = {"preregistered", "testing", "planned", "running", "open", "in_progress"}


DATA_STATUS = ("not_collected", "exists_unseen", "exists_partially_seen",
               "exists_seen")
# Seeing the data is what separates a prediction from a description of what
# already happened. OSF asks this first for the same reason.
SEEN_STATUS = ("exists_partially_seen", "exists_seen")


def _is_preregistered(h):
    """Does this entry CLAIM to be preregistered?

    The claim can live in an explicit boolean or in the prose tag the template
    uses. Both are read, because the rule has to bite on the entry as written
    rather than on the one field a careful author remembered to set.
    """
    pre = h.get("preregistered")
    if isinstance(pre, bool):
        return pre
    # The canonical field holds a DATE, not a boolean -- `preregistered:
    # "2026-07-11"` is how the worked example writes the claim, and an earlier
    # draft of this rule read only the boolean and so never fired on the very
    # entries it was written for. A truthy value here is the claim.
    if pre not in (None, "", False):
        return True
    blob = " ".join(_s(h.get(k)) for k in ("id", "name", "status", "origin", "note"))
    return "önkayıt" in blob.lower() or "prereg" in blob.lower()


def _check_preregistration(hyps, lang):
    """R18 — a preregistration that does not say what it locked, locked nothing.

    Three fields, each closing a door that the rest of this file already argues
    should be shut: data_status (is this a prediction or a description?),
    stopping_rule (can you collect until it crosses?), exclusion_rule (can you
    drop the inconvenient point afterwards?). Prose said all three long before
    anything checked them.
    """
    errs = []
    for hid, h in hyps.items():
        if not _is_preregistered(h):
            continue

        ds = _s(h.get("data_status"))
        if not ds:
            errs.append(m("R18_no_data_status", lang, id=hid))
        elif ds not in DATA_STATUS:
            errs.append(m("R18_bad_data_status", lang, id=hid, value=ds))
        elif ds in SEEN_STATUS:
            errs.append(m("R18_seen_data_preregistered", lang, id=hid, value=ds))

        # The stopping and exclusion rules only bite where a threshold exists:
        # an entry with no numeric decision rule has nothing to stop or clean
        # around, and firing there would train people to write "none" twice.
        if h.get("threshold"):
            if not _s(h.get("stopping_rule")):
                errs.append(m("R18_no_stopping_rule", lang, id=hid))
            if not _s(h.get("exclusion_rule")):
                errs.append(m("R18_no_exclusion_rule", lang, id=hid))
    return errs


def _check_review_deadlines(hyps: dict, lang: str, as_of: str) -> list[str]:
    """R17 — an open entry carries a deadline, and a passed deadline forces a decision.

    Two halves on purpose, because they fail for different reasons and at
    different times:

      * The STRUCTURAL half (a review_by must exist) is decided by the commit.
        It cannot start failing on its own.
      * The TEMPORAL half (the deadline has passed and nothing was decided) is
        decided by the calendar. It CAN turn a green main red with no commit
        in between -- and that is the rule working, not the build breaking. An
        untested [H] that nobody ever closes is how a registry fills with
        entries that look preregistered and were only ever sketched. A
        deadline that cannot interrupt you is a reminder, not a gate.

    Recording a decision clears it: a new review_by with a reason, status
    dormant, or a closed entry.
    """
    errs = []
    for hid, h in hyps.items():
        status = _s(h.get("status")).lower()
        if status and status not in OPEN_STATUSES:
            continue                       # closed / refuted / dormant: settled
        due = _s(h.get("review_by"))
        if not due:
            errs.append(m("R17_no_review_by", lang, id=hid, status=status or "open"))
            continue
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", due):
            errs.append(m("R17_bad_date", lang, id=hid, due=due))
            continue
        if due < as_of:                    # ISO dates compare as strings
            errs.append(m("R17_review_overdue", lang, id=hid, due=due, asof=as_of))
    return errs


def check(data: dict, lang: str,
          baseline: dict | None = None, as_of: str | None = None) -> tuple[list[str], list[str]]:
    """Return (violations, warnings). See the module docstring for why two."""
    errs: list[str] = []
    warns: list[str] = []
    hyps = {h.get("id"): h for h in (data.get("hypotheses") or []) if isinstance(h, dict)}
    exps = {e.get("id"): e for e in (data.get("experiments") or []) if isinstance(e, dict)}
    results = [r for r in (data.get("results") or []) if isinstance(r, dict)]
    features = [f for f in (data.get("features") or []) if isinstance(f, dict)]
    bugs = [b for b in (data.get("bugs") or []) if isinstance(b, dict)]

    n_entries = len(hyps) + len(exps) + len(results) + len(features) + len(bugs)

    # R17 — deadlines. Enforced only from schema_version 1.6, the same way R8
    # waited for 1.2 and R9-R12 for 1.4: a registry written before the field
    # existed migrates deliberately instead of failing on upgrade. Without
    # this gate the rule would also fire on every entry that simply omits
    # `status`, which is not the same as an entry that has stopped moving.
    # --as-of pins "today" so a run is reproducible; without it the calendar
    # decides, which is the point of the rule.
    if _schema_at_least(data, (1, 6)):
        errs += _check_review_deadlines(
            hyps, lang, as_of or datetime.date.today().isoformat())

    # R18 — preregistration completeness, gated at 1.7 the way R17 waited for
    # 1.6. An older registry migrates on purpose rather than failing the day
    # someone upgrades the skill.
    if _schema_at_least(data, (1, 7)):
        errs += _check_preregistration(hyps, lang)

    # R19-R21 — the probe block, gated at 1.8. Same migration shape as 1.6/1.7:
    # a registry written before the fields existed does not fail on upgrade.
    if _schema_at_least(data, (1, 8)):
        errs += _check_probes(data.get("probes"), data.get("coverage"), lang)
        warns += _probe_warnings(data.get("probes"), data.get("coverage"), lang)

    # tier sanity
    for kind, coll in (("hypothesis", hyps.values()), ("feature", features), ("bug", bugs)):
        for e in coll:
            t = _s(e.get("tier"))
            if t and t not in VALID_TIERS:
                errs.append(m("bad_tier", lang, kind=kind, id=e.get("id"), tier=t))
    # A feature's problem claim carries its own tier — "users struggle with X"
    # is usually [H] dressed as [K], and the gate exists to say which.
    for f in features:
        pc = f.get("problem_claim")
        if isinstance(pc, dict):
            t = _s(pc.get("tier"))
            if t and t not in VALID_TIERS:
                errs.append(m("bad_tier", lang, kind="feature problem_claim",
                              id=f.get("id"), tier=t))

    # R1 — threshold + refutation must exist on any hypothesis a result references
    referenced = {_s(r.get("hypothesis")) for r in results if _s(r.get("hypothesis"))}
    for hid in referenced:
        h = hyps.get(hid)
        if not h:
            continue
        thr = h.get("threshold") or {}
        rid = next((r.get("id") for r in results if _s(r.get("hypothesis")) == hid), "?")
        if not thr:
            errs.append(m("R1_no_threshold", lang, id=hid, rid=rid))
        elif not (_s(thr.get("support")) and _s(thr.get("refute"))):
            errs.append(m("R1_threshold_incomplete", lang, id=hid))
        if not _s(h.get("refutation")):
            errs.append(m("R1_no_refutation", lang, id=hid))

    # R2 — baseline mandatory; baseline-less experiment cannot promote to K
    for eid, e in exps.items():
        # A registry written by hand often puts a bare string here ("baseline: >").
        # Reading .get() off it used to raise AttributeError and abort the whole
        # run with a traceback — a validator that crashes on a malformed file
        # teaches nothing. Treat the string as the description and let R2 speak.
        bl = e.get("baseline") or {}
        if isinstance(bl, str):
            bl = {"description": bl}
        elif not isinstance(bl, dict):
            bl = {}
        desc = _s(bl.get("description"))
        just = _s(bl.get("justification"))
        if not desc:
            errs.append(m("R2_no_baseline", lang, id=eid))
        elif desc.lower() == "none" and not just:
            errs.append(m("R2_no_baseline", lang, id=eid))
    for r in results:
        eid = _s(r.get("experiment"))
        e = exps.get(eid)
        if e and str(r.get("decision", "")).lower().replace(" ", "") in {"proposeh->k", "h->k"}:
            bl = e.get("baseline") or {}
            if isinstance(bl, str):
                bl = {"description": bl}
            elif not isinstance(bl, dict):
                bl = {}
            desc = _s(bl.get("description"))
            if not desc or desc.lower() == "none":
                errs.append(m("R2_baseless_promotes_K", lang, id=r.get("id"), eid=eid))

    # R3 — every confound named in a hypothesis must be controlled or accepted
    for eid, e in exps.items():
        needed: set[str] = set()
        for hid in (e.get("hypotheses") or []):
            h = hyps.get(hid)
            if h:
                needed |= {str(c) for c in (h.get("confounds") or [])}
        if not needed:
            continue
        controls = e.get("confound_controls")
        if not controls:
            errs.append(m("R3_no_controls", lang, eid=eid))
            continue
        covered = {str(c.get("confound")) for c in controls if isinstance(c, dict)}
        for c in needed - covered:
            hid = next((hid for hid in (e.get("hypotheses") or [])
                        if c in {str(x) for x in (hyps.get(hid, {}).get("confounds") or [])}), "?")
            errs.append(m("R3_confound_uncontrolled", lang, c=c, hid=hid, eid=eid))

    # R5 — honesty annexes mandatory, non-empty
    for r in results:
        ann = r.get("honesty_annexes")
        if not ann or not (isinstance(ann, list) and any(_s(a) for a in ann)):
            errs.append(m("R5_empty_annexes", lang, id=r.get("id")))

    # R6 — surprising positive proposing K needs a completed confound control
    for r in results:
        proposes_k = str(r.get("decision", "")).lower().replace(" ", "") in {"proposeh->k", "h->k"}
        if r.get("surprising_positive") and proposes_k and not _s(r.get("confound_control_result")):
            errs.append(m("R6_surprising_no_control", lang, id=r.get("id")))

    # R7 — a REALIZED tier change (hypothesis now sits at the proposed tier)
    # must be confirmed by someone other than the writer. A still-pending
    # proposal (hypothesis not yet at the target tier) is a legitimate
    # intermediate state, not a violation.
    for r in results:
        dec = str(r.get("decision", "")).lower().replace(" ", "")
        if not dec.startswith("propose"):
            continue
        target = "K" if "->k" in dec else ("R" if "->r" in dec else "")
        hyp = hyps.get(_s(r.get("hypothesis")))
        if target and hyp and _s(hyp.get("tier")).upper() == target \
                and not _s(r.get("decision_confirmed_by")):
            errs.append(m("R7_self_confirmed", lang, id=r.get("id"),
                          hid=hyp.get("id"), tier=target))

    # R8 — every hypothesis names the arbiter that returns the verdict.
    # Enforced only for registries declaring schema_version >= 1.2, so that
    # 1.0/1.1 files migrate deliberately instead of failing on upgrade.
    if _schema_at_least(data, (1, 2)):
        errs += _check_arbiters(hyps.values(), lang)

    # From 1.3, R8 covers features and bugs too. Until now _check_arbiters
    # walked hypotheses only, so a feature could sit at [K] with no named
    # judge — while the schema's own comment already said that a value metric
    # judged solely by the feature's proposer is class: author.
    if _schema_at_least(data, (1, 3)):
        errs += _check_arbiters(features, lang, "feature")
        errs += _check_arbiters(bugs, lang, "bug")
        errs += _check_feature_gates(features, lang)
        errs += _check_bug_rivals(bugs, lang)

    # R9-R12 — the four places where the schema permitted what the prose
    # forbids outright (PROSE-SCHEMA-AUDIT.md). Gated on 1.4, the same
    # migration pattern R8 used for 1.2 and R13-R15 for 1.3.
    if _schema_at_least(data, (1, 4)):
        errs += _check_entry_discipline(hyps, features, bugs, results, lang)

    # R16 — no version gate needed: the coverage block is new, so a registry
    # without a phased audit has nothing to trip.
    errs += _check_coverage(data.get("coverage"), lang)

    # R4 — append-only vs. a git baseline (history may only grow; entries may not vanish)
    if baseline:
        errs += _append_only(data, baseline, lang)

    warns += _warnings(hyps, features, bugs, results, lang)
    warns += _coverage_warnings(data.get("coverage"), lang)

    check.n_entries = n_entries  # type: ignore[attr-defined]
    return errs, warns


def _warnings(hyps: dict, features: list[dict], bugs: list[dict],
              results: list[dict], lang: str) -> list[str]:
    """W1-W4 — findings that advise rather than block.

    Each has a legitimate exception, which is exactly why none of them is a
    rule: a draft entry may not have its threshold yet, a one-entry registry
    is trivially all-[K], and a test can be honestly one-sided in rare cases.
    Blocking on those would teach authors to shape registries around the
    checker instead of around the claim.
    """
    warns: list[str] = []
    referenced = {_s(r.get("hypothesis")) for r in results if _s(r.get("hypothesis"))}
    kinds = (("hypothesis", list(hyps.values())), ("feature", features), ("bug", bugs))

    for kind, coll in kinds:
        label = KIND_LABEL[kind][1 if lang == "tr" else 0]
        for e in coll:
            eid = e.get("id")
            if not _s(e.get("two_sided")):
                warns.append(m("W1_no_two_sided", lang, kind=label, id=eid))
            if _s(eid) in referenced:
                continue          # R1 already governs these, and it blocks
            thr = _field(e, "threshold")
            missing = []
            if isinstance(thr, dict):
                if not (_s(thr.get("support")) and _s(thr.get("refute"))):
                    missing.append("threshold")
            elif not _s(thr):
                # A prose threshold counts as PRESENT here. Whether it is
                # numeric is a separate finding, still open, and folding it
                # into W2 would hide two different problems behind one line.
                missing.append("threshold")
            if not _s(e.get("refutation")):
                missing.append("refutation")
            if missing:
                warns.append(m("W2_open_no_threshold", lang, kind=label, id=eid,
                               missing=" / ".join(missing)))

    tiered = [_s(e.get("tier")).upper()
              for _, coll in kinds for e in coll if _s(e.get("tier"))]
    if len(tiered) >= 2 and all(t == "K" for t in tiered):
        warns.append(m("W3_all_K", lang, n=len(tiered)))
    return warns


def _schema_at_least(data: dict, want: tuple[int, int]) -> bool:
    raw = _s((data.get("registry") or {}).get("schema_version"))
    parts = raw.split(".")
    try:
        got = (int(parts[0]), int(parts[1]) if len(parts) > 1 else 0)
    except ValueError:
        return False
    return got >= want


def _check_arbiters(entries: Any, lang: str, kind: str = "hypothesis") -> list[str]:
    """R8 — the judge behind the threshold, per entry."""
    errs: list[str] = []
    label = KIND_LABEL[kind][1 if lang == "tr" else 0]
    for h in entries:
        hid = h.get("id")
        arb = h.get("arbiter")
        if not isinstance(arb, dict) or not _s(arb.get("class")):
            errs.append(m("R8_no_arbiter", lang, kind=label, id=hid))
            continue
        cls = _s(arb.get("class")).lower()
        if cls not in ARBITER_CLASSES:
            errs.append(m("R8_bad_class", lang, kind=label, id=hid, cls=cls))
            continue
        if not _s(arb.get("who")):
            errs.append(m("R8_no_who", lang, kind=label, id=hid, cls=cls))

        tier = _s(h.get("tier")).upper()
        if cls == "author" and tier == "K":
            errs.append(m("R8_author_promotes_K", lang, kind=label, id=hid, cls=cls))
        if cls == "none" and tier not in {"", "S", "R"}:
            # R is reachable without an arbiter only by withdrawal, which the
            # history field records; S is the resting state.
            errs.append(m("R8_none_leaves_S", lang, kind=label, id=hid, tier=tier))
        if cls in {"instrument", "third_party"} and not _s(arb.get("calibration")):
            errs.append(m("R8_no_calibration", lang, kind=label, id=hid, cls=cls))
        if cls in {"author", "none"} and arb.get("independent_of_author") is True:
            errs.append(m("R8_independence_contradiction", lang, kind=label, id=hid, cls=cls))
    return errs


DOMAIN_OUTCOMES = ("expressible", "boundary_recorded", "finding", "unchecked")
PAIR_OUTCOMES = ("holds", "breaks", "unchecked")
# supplied_by classes that make the scenario list self-report. Same shape as
# R8's arbiter classes: a list the auditor invented is evidence about the
# auditor's imagination, not about the domain.
SELF_SUPPLIED = ("auditor", "none", "")


def _check_probes(probes: Any, cov: Any, lang: str) -> list[str]:
    """R19-R21 — the three passes whose input is not a sentence someone wrote.

    Structural checks run whenever a probe block exists; the gating half fires
    only on a coverage block CLAIMING tier K. Like every other rule here this
    checks completeness, never quality: that a scenario was supplied by someone
    who knows the field and got an outcome, not that it was a good scenario.
    """
    errs: list[str] = []
    if not isinstance(probes, dict):
        probes = {}

    dom = probes.get("domain") if isinstance(probes.get("domain"), dict) else {}
    scenarios = [x for x in (dom.get("scenarios") or []) if isinstance(x, dict)]
    for sc in scenarios:
        sid = _s(sc.get("id")) or "?"
        missing = [k for k in ("situation", "outcome") if not _s(sc.get(k))]
        if missing:
            errs.append(m("R19_scenario_incomplete", lang, id=sid,
                          missing=" / ".join(missing)))
        out = _s(sc.get("outcome")).lower()
        if out and out not in DOMAIN_OUTCOMES:
            errs.append(m("R19_bad_outcome", lang, id=sid, got=out,
                          allowed=", ".join(DOMAIN_OUTCOMES)))

    conj = probes.get("conjunction") if isinstance(probes.get("conjunction"), dict) else {}
    pairs = [x for x in (conj.get("pairs") or []) if isinstance(x, dict)]
    for pr in pairs:
        pid = _s(pr.get("id")) or "?"
        missing = [k for k in ("feature", "guarantee", "outcome") if not _s(pr.get(k))]
        if missing:
            errs.append(m("R20_pair_incomplete", lang, id=pid,
                          missing=" / ".join(missing)))
        out = _s(pr.get("outcome")).lower()
        if out and out not in PAIR_OUTCOMES:
            errs.append(m("R20_bad_outcome", lang, id=pid, got=out,
                          allowed=", ".join(PAIR_OUTCOMES)))

    for esc in [x for x in (probes.get("escaped") or []) if isinstance(x, dict)]:
        eid = _s(esc.get("id")) or "?"
        missing = [k for k in ("symptom", "found_by") if not _s(esc.get(k))]
        if missing:
            errs.append(m("R21_escape_incomplete", lang, id=eid,
                          missing=" / ".join(missing)))
        if not (_s(esc.get("class_ref")) or _s(esc.get("class_new"))):
            errs.append(m("R21_escape_unclassed", lang, id=eid))

    if not isinstance(cov, dict) or _s(cov.get("claim_tier")).upper() != "K":
        return errs

    # --- the gating half: a coverage block that says it covered the target ---
    why = None
    if not scenarios:
        why = "there is no domain probe" if lang != "tr" else "hiç alan probu yok"
    elif _s(dom.get("supplied_by")).lower() in SELF_SUPPLIED:
        who = _s(dom.get("supplied_by")) or "—"
        why = ((f"the scenarios are supplied_by {who!r} — self-report") if lang != "tr"
               else f"senaryoları veren {who!r} — kendi beyanı")
    elif _s(dom.get("written_before_work")).lower() not in ("true", "yes", "1"):
        why = ("the scenarios are not marked written_before_work — scenarios written after a gap "
               "was found are HARKing and prove nothing about coverage" if lang != "tr"
               else "senaryolar written_before_work olarak işaretli değil — bir boşluk bulunduktan "
                    "sonra yazılan senaryo HARKing'dir ve kapsam hakkında hiçbir şey kanıtlamaz")
    else:
        unchecked = [_s(sc.get("id")) or "?" for sc in scenarios
                     if _s(sc.get("outcome")).lower() == "unchecked"]
        if unchecked:
            why = (("these scenarios were never run: " if lang != "tr"
                    else "şu senaryolar hiç koşulmamış: ") + ", ".join(unchecked))
    if why:
        errs.append(m("R19_coverage_unprobed", lang, why=why))

    why = None
    if not pairs:
        why = "there is no conjunction pass" if lang != "tr" else "hiç bileşim pası yok"
    else:
        unchecked = [_s(pr.get("id")) or "?" for pr in pairs
                     if _s(pr.get("outcome")).lower() == "unchecked"]
        if unchecked:
            why = (("these pairs were never checked: " if lang != "tr"
                    else "şu çiftler hiç kontrol edilmemiş: ") + ", ".join(unchecked))
    if why:
        errs.append(m("R20_coverage_unpaired", lang, why=why))
    return errs


def _probe_warnings(probes: Any, cov: Any, lang: str) -> list[str]:
    """W5 — a coverage block with a pass missing. Advisory: it may simply not
    have run yet, and blocking would teach authors to write an empty block."""
    if not isinstance(cov, dict):
        return []
    p = probes if isinstance(probes, dict) else {}
    warns = []
    dom = p.get("domain") if isinstance(p.get("domain"), dict) else {}
    conj = p.get("conjunction") if isinstance(p.get("conjunction"), dict) else {}
    if not [x for x in (dom.get("scenarios") or []) if isinstance(x, dict)]:
        warns.append(m("W5_no_probe", lang, which="domain"))
    if not [x for x in (conj.get("pairs") or []) if isinstance(x, dict)]:
        warns.append(m("W5_no_probe", lang, which="conjunction"))
    return warns


def _check_coverage(cov: Any, lang: str) -> list[str]:
    """R16 — a whole-target coverage claim waits for reconciliation.

    The Coverage Ledger is the one place in this methodology where a
    DELIVERABLE decides a tier, and until schema 1.5 it lived in a Markdown
    table nothing could read. This checks completeness, never quality: that
    every row says done and a MERGE row exists, not that the reconciliation
    actually found the cross-slice hops it was supposed to look for.
    """
    if not isinstance(cov, dict):
        return []
    if _s(cov.get("claim_tier")).upper() != "K":
        return []
    phases = [ph for ph in (cov.get("phases") or []) if isinstance(ph, dict)]
    unfinished = [_s(ph.get("id")) or "?" for ph in phases
                  if _s(ph.get("status")).lower() != "done"]
    if unfinished:
        why = (("these phases are not done: " if lang != "tr" else "şu fazlar bitmemiş: ")
               + ", ".join(unfinished))
        return [m("R16_coverage_claim_unearned", lang, why=why)]
    if not any(_s(ph.get("id")).upper() == "MERGE" for ph in phases):
        why = "there is no MERGE row at all" if lang != "tr" else "hiç MERGE satırı yok"
        return [m("R16_coverage_claim_unearned", lang, why=why)]
    return []


def _coverage_warnings(cov: Any, lang: str) -> list[str]:
    """W4 — reconciliation planned up front, or skipped."""
    if not isinstance(cov, dict):
        return []
    phases = [ph for ph in (cov.get("phases") or []) if isinstance(ph, dict)]
    if phases and not any(_s(ph.get("id")).upper() == "MERGE" for ph in phases):
        return [m("W4_no_merge_row", lang)]
    return []


def _check_entry_discipline(hyps: dict, features: list[dict], bugs: list[dict],
                            results: list[dict], lang: str) -> list[str]:
    """R9-R12 — evidence for [K], numeric thresholds, a tier, the mandatory fields.

    None of these judges content. R9 checks a result EXISTS, not that it was
    a good experiment; R10 checks a quantity is NAMED, not that it is the
    right one; R12 checks prior art is present, not that the relatives found
    were the real ones. Contract completeness is machine-checkable; the
    judgement stays with a human or a frontier model (that separation is R7).
    """
    errs: list[str] = []
    supported = {
        _s(r.get("hypothesis"))
        for r in results
        if _s(r.get("threshold_met")).lower() == "yes" and _s(r.get("hypothesis"))
    }
    kinds = (("hypothesis", list(hyps.values())), ("feature", features), ("bug", bugs))

    for kind, coll in kinds:
        label = KIND_LABEL[kind][1 if lang == "tr" else 0]
        for e in coll:
            eid = e.get("id")
            tier = _s(e.get("tier")).upper()

            # R11 — no untagged assertions.
            if not tier:
                errs.append(m("R11_no_tier", lang, kind=label, id=eid))

            # R9 — [K] is earned by a result or by a cited external source.
            # prior_art is deliberately NOT accepted here: relatives are not
            # evidence for this claim, they are context for its originality.
            if tier == "K" and _s(eid) not in supported and not _s(e.get("external_evidence")):
                errs.append(m("R9_K_without_evidence", lang, kind=label, id=eid))

            # R10 — a threshold names a quantity.
            thr = _field(e, "threshold")
            if isinstance(thr, dict) and not _s(thr.get("non_numeric_justification")):
                for side in ("support", "refute"):
                    text = _s(thr.get(side))
                    if text and not HAS_NUMBER.search(text):
                        errs.append(m("R10_threshold_not_numeric", lang, kind=label, id=eid,
                                      side=side, text=text[:60]))

            # R12 — the mandatory fields of templates.md §1.
            for field in ("formal", "cost", "status"):
                if not _s(e.get(field)):
                    errs.append(m("R12_missing_field", lang, kind=label, id=eid, field=field))
            metric = _field(e, "metric")
            if not metric:
                errs.append(m("R12_missing_field", lang, kind=label, id=eid, field="metric"))
            elif isinstance(metric, dict) and not _s(metric.get("instrument")):
                errs.append(m("R12_metric_no_instrument", lang, kind=label, id=eid))
            pa = e.get("prior_art")
            if not (isinstance(pa, list) and any(_s(x) for x in pa)) and not _s(pa):
                errs.append(m("R12_missing_field", lang, kind=label, id=eid, field="prior_art"))
    return errs


def _check_feature_gates(features: list[dict], lang: str) -> list[str]:
    """R13/R14 — the two things that stop a feature gate being a wish list.

    Both come from references/feature-gate.md, both were MANDATORY in prose
    and unrepresented in the schema until 1.3. Neither checks quality: R13
    verifies a kill condition was WRITTEN, not that it is a good one, and
    R14 verifies the null alternative is PRESENT, not that it was honestly
    priced. Contract completeness is machine-checkable; judgement is not.
    """
    errs: list[str] = []
    for f in features:
        fid = f.get("id")
        if not _s(f.get("kill_condition")):
            errs.append(m("R13_no_kill_condition", lang, id=fid))

        alts = f.get("alternatives")
        if not isinstance(alts, list) or not alts:
            errs.append(m("R14_no_alternatives", lang, id=fid))
            continue
        kinds = {_s(a.get("kind")).lower() for a in alts if isinstance(a, dict)}
        if "cheaper" not in kinds:
            errs.append(m("R14_missing_kind", lang, id=fid, kind="cheaper",
                          why=("a feature that was never compared against a smaller version "
                               "of itself has not been gated, only described")
                          if lang != "tr" else
                          ("kendisinin daha küçük bir hâliyle hiç karşılaştırılmamış bir özellik "
                           "gate'lenmiş değil, sadece tarif edilmiştir")))
        if "null" not in kinds:
            errs.append(m("R14_missing_kind", lang, id=fid, kind="null",
                          why=("without pricing 'do nothing', the cost of leaving the problem "
                               "unsolved is assumed rather than compared")
                          if lang != "tr" else
                          ("'hiçbir şey yapma' fiyatlanmadan, problemi çözmemenin maliyeti "
                           "karşılaştırılmaz, varsayılır")))
    return errs


def _check_bug_rivals(bugs: list[dict], lang: str) -> list[str]:
    """R15 — Mode 4's reason for existing: never close on the first story that fits."""
    errs: list[str] = []
    for b in bugs:
        rivals = b.get("rival_hypotheses")
        if not isinstance(rivals, list) or not any(_s(r) for r in rivals):
            errs.append(m("R15_no_rivals", lang, id=b.get("id")))
    return errs


def _hist_len(e: dict) -> int:
    h = e.get("history")
    return len(h) if isinstance(h, list) else 0


def _append_only(new: dict, old: dict, lang: str) -> list[str]:
    errs: list[str] = []
    def _rows(d: dict, key: str) -> list:
        # The coverage ledger's rows live one level down, under
        # coverage.phases. code-audit.md: "rows are appended/updated, never
        # deleted; a re-scoped slice gets a new row, not an edit" — the same
        # rule as everywhere else, so it uses the same machinery.
        if key == "coverage.phases":
            cov = d.get("coverage")
            return (cov.get("phases") or []) if isinstance(cov, dict) else []
        return d.get(key) or []

    for kind, key in (("hypothesis", "hypotheses"), ("experiment", "experiments"),
                      ("result", "results"), ("feature", "features"), ("bug", "bugs"),
                      ("coverage phase", "coverage.phases")):
        old_by = {e.get("id"): e for e in _rows(old, key) if isinstance(e, dict)}
        new_by = {e.get("id"): e for e in _rows(new, key) if isinstance(e, dict)}
        for eid, oe in old_by.items():
            if eid not in new_by:
                errs.append(m("R4_entry_deleted", lang, kind=kind, id=eid))
                continue
            old_len, new_len = _hist_len(oe), _hist_len(new_by[eid])
            if new_len < old_len:
                errs.append(m("R4_history_shrank", lang, kind=kind, id=eid, old=old_len, new=new_len))
    return errs


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Mizan registry R1–R21 validator")
    ap.add_argument("registry", help="path to mizan-registry.yaml")
    ap.add_argument("--lang", choices=["en", "tr"], default="en")
    ap.add_argument("--against", metavar="GITREF",
                    help="git ref to diff against for the append-only (R4) check, e.g. HEAD")
    ap.add_argument("--as-of", metavar="YYYY-MM-DD",
                    help="treat this as today for R17 deadlines (default: the real date). "
                         "Pin it to make a run reproducible.")
    ap.add_argument("--strict", action="store_true",
                    help="treat W1-W4 warnings as violations (CI runs strict; local runs do not)")
    args = ap.parse_args(argv)

    # The catalog carries Turkish text and a ✗ glyph; ensure UTF-8 output even
    # on legacy Windows code pages (cp1254 etc.).
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")  # type: ignore[union-attr]
        except (AttributeError, ValueError):
            pass

    try:
        data = load(args.registry)
    except Exception as exc:
        sys.stderr.write(f"parse error: {exc}\n")
        return 2

    baseline = load_git_baseline(args.against, args.registry) if args.against else None
    errs, warns = check(data, args.lang, baseline, args.as_of)
    n = getattr(check, "n_entries", 0)

    if args.strict and warns:
        errs = errs + warns

    if errs:
        for e in errs:
            print("  ✗ " + e)
        # Warnings print next to violations too. Holding them back until the
        # blocking problems are fixed makes a second run reveal something
        # that was already known, which is how a warning gets ignored.
        if not args.strict:
            for w in warns:
                print("  ! " + w)
        print(m("found", args.lang, n=len(errs)))
        if args.strict and warns:
            print(m("warn_strict", args.lang, n=len(warns)))
        return 1

    print(m("clean", args.lang, n=n))
    if warns:
        for w in warns:
            print("  ! " + w)
        print(m("warn_header", args.lang, n=len(warns)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
