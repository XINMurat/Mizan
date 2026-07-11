#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mizan registry validator — LLM-free static enforcement of hard rules R1–R7.

This is the cheap, judgment-free baseline of feature FEAT-M001 (in the
project's roadmap registry). It does NOT evaluate the *quality* of a
hypothesis; it only checks the mechanical, machine-checkable invariants of
the mizan-registry.yaml schema. Semantic judgment stays with a human or a
frontier model (that separation is rule R7 itself).

Bilingual: messages are emitted in the requested language (--lang tr|en).

Usage:
    python tools/mizan_validate.py path/to/mizan-registry.yaml
    python tools/mizan_validate.py --lang tr registry.yaml
    python tools/mizan_validate.py --against HEAD registry.yaml   # append-only check

Exit code 0 = clean, 1 = violations found, 2 = usage/parse error.

Dependency: PyYAML  (pip install pyyaml)
"""
from __future__ import annotations

import argparse
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

VALID_TIERS = {"K", "H", "S", "R", "KKE", "Y"}

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
    "bad_tier": (
        "SCHEMA: {kind} '{id}' has invalid tier '{tier}' (allowed: K H S R KKE Y).",
        "ŞEMA: {kind} '{id}' geçersiz tier '{tier}' taşıyor (izinli: K H S R KKE Y).",
    ),
    "clean": (
        "OK — {n} entries checked, no R1–R7 violations.",
        "OK — {n} girdi kontrol edildi, R1–R7 ihlali yok.",
    ),
    "found": (
        "{n} violation(s) found.",
        "{n} ihlal bulundu.",
    ),
}


def m(key: str, lang: str, **kw: Any) -> str:
    en, tr = MSG[key]
    return (tr if lang == "tr" else en).format(**kw)


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


def check(data: dict, lang: str, baseline: dict | None = None) -> list[str]:
    errs: list[str] = []
    hyps = {h.get("id"): h for h in (data.get("hypotheses") or []) if isinstance(h, dict)}
    exps = {e.get("id"): e for e in (data.get("experiments") or []) if isinstance(e, dict)}
    results = [r for r in (data.get("results") or []) if isinstance(r, dict)]
    features = [f for f in (data.get("features") or []) if isinstance(f, dict)]
    bugs = [b for b in (data.get("bugs") or []) if isinstance(b, dict)]

    n_entries = len(hyps) + len(exps) + len(results) + len(features) + len(bugs)

    # tier sanity
    for kind, coll in (("hypothesis", hyps.values()), ("feature", features), ("bug", bugs)):
        for e in coll:
            t = _s(e.get("tier"))
            if t and t not in VALID_TIERS:
                errs.append(m("bad_tier", lang, kind=kind, id=e.get("id"), tier=t))

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
        bl = e.get("baseline") or {}
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

    # R4 — append-only vs. a git baseline (history may only grow; entries may not vanish)
    if baseline:
        errs += _append_only(data, baseline, lang)

    check.n_entries = n_entries  # type: ignore[attr-defined]
    return errs


def _hist_len(e: dict) -> int:
    h = e.get("history")
    return len(h) if isinstance(h, list) else 0


def _append_only(new: dict, old: dict, lang: str) -> list[str]:
    errs: list[str] = []
    for kind, key in (("hypothesis", "hypotheses"), ("experiment", "experiments"),
                      ("result", "results"), ("feature", "features"), ("bug", "bugs")):
        old_by = {e.get("id"): e for e in (old.get(key) or []) if isinstance(e, dict)}
        new_by = {e.get("id"): e for e in (new.get(key) or []) if isinstance(e, dict)}
        for eid, oe in old_by.items():
            if eid not in new_by:
                errs.append(m("R4_entry_deleted", lang, kind=kind, id=eid))
                continue
            old_len, new_len = _hist_len(oe), _hist_len(new_by[eid])
            if new_len < old_len:
                errs.append(m("R4_history_shrank", lang, kind=kind, id=eid, old=old_len, new=new_len))
    return errs


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Mizan registry R1–R7 validator")
    ap.add_argument("registry", help="path to mizan-registry.yaml")
    ap.add_argument("--lang", choices=["en", "tr"], default="en")
    ap.add_argument("--against", metavar="GITREF",
                    help="git ref to diff against for the append-only (R4) check, e.g. HEAD")
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
    errs = check(data, args.lang, baseline)
    n = getattr(check, "n_entries", 0)

    if errs:
        for e in errs:
            print("  ✗ " + e)
        print(m("found", args.lang, n=len(errs)))
        return 1
    print(m("clean", args.lang, n=n))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
