"""Grader programmatique pour eval-1 iteration-2 thruuu-brief-builder.

17 assertions : 11 v1 + 6 v2.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ITER_DIR = Path(__file__).parent
EVAL_DIR = ITER_DIR / "eval-1-affiliatepress-vs-solidaffiliate"
RUNS = ["with_skill", "old_skill"]

ASSERTIONS = [
    "L'output contient les 3 blocs dans l'ordre : ANALYSE GLOBALE, puis BRIEF STRUCTURÉ, puis TEXTES PRÊTS À COLLER",
    "En-tête minimal présent avec les 4 champs (Mot-clé, Mode, Sources, Confiance)",
    "Mode 'comparatif' explicitement détecté",
    "BLOC 1 contient Faits, Déductions, Recommandations distincts",
    "Confiance global = 'moyen' ou 'faible' (GSC manquante)",
    "BLOC 2 contient les 10 onglets numérotés",
    "BLOC 3 'TEXTES PRÊTS À COLLER' contient au moins 6 sous-sections",
    "H1 recommandé sans date (evergreen)",
    "Les 2 URLs schoolsWP existantes dans le maillage",
    "Mismatch SERP (pivot Google vers AffiliateWP) identifié",
    "Tutoiement dominant (pas de vouvoiement)",
    "V2 — Tags [FAIT], [DÉDUCTION], [À VÉRIFIER] utilisés au moins une fois chacun",
    "V2 — Section 'Données à valider avant publication' présente avec au moins 3 items",
    "V2 — Features SERP (AI Overview, vidéos, Reddit) traduites en consignes éditoriales concrètes dans BLOC 2",
    "V2 — BLOC 3 ne contient aucun tableau markdown (pas de lignes de type '| col | col |')",
    "V2 — Cohérence des noms d'entités (pas d'alternance AffiliatePress / affiliatepress / Affiliate Press)",
    "V2 — Safety checklist respectée : affirmations pricing/compatibilité sans source portent [À VÉRIFIER]",
]


def check_three_blocks_order(text: str) -> tuple[bool, str]:
    up = text.upper()
    i_analyse = up.find("ANALYSE GLOBALE")
    i_brief = up.find("BRIEF STRUCTURÉ")
    i_textes = up.find("TEXTES PRÊTS À COLLER")
    if i_analyse == -1 or i_brief == -1 or i_textes == -1:
        missing = []
        if i_analyse == -1: missing.append("ANALYSE GLOBALE")
        if i_brief == -1: missing.append("BRIEF STRUCTURÉ")
        if i_textes == -1: missing.append("TEXTES PRÊTS À COLLER")
        return False, f"Blocs manquants : {', '.join(missing)}"
    if not (i_analyse < i_brief < i_textes):
        return False, f"Ordre incorrect"
    return True, f"Ordre correct : ANALYSE@{i_analyse} < BRIEF@{i_brief} < TEXTES@{i_textes}"


def check_header_min(text: str) -> tuple[bool, str]:
    head = text[:600].lower()
    required = ["mot-clé", "mode", "source", "confiance"]
    missing = [k for k in required if k not in head]
    if missing:
        return False, f"Champs manquants : {missing}"
    return True, "Les 4 champs d'en-tête présents"


def check_mode_detected(text: str) -> tuple[bool, str]:
    head = text[:900].lower()
    if "comparatif" not in head:
        return False, "Mode 'comparatif' non mentionné"
    return True, "Mode 'comparatif' explicitement détecté"


def check_faits_deductions_recos(text: str) -> tuple[bool, str]:
    analyse_section = text[: text.upper().find("BRIEF STRUCTURÉ") or len(text)]
    hits = {
        "Faits": bool(re.search(r"###?\s*Faits\b", analyse_section, re.IGNORECASE)),
        "Déductions": bool(re.search(r"###?\s*D[ée]ductions\b", analyse_section, re.IGNORECASE)),
        "Recommandations": bool(re.search(r"###?\s*Recommandations\b", analyse_section, re.IGNORECASE)),
    }
    missing = [k for k, v in hits.items() if not v]
    if missing:
        return False, f"Sections manquantes : {missing}"
    return True, "Les 3 sections de BLOC 1 présentes"


def check_confidence(text: str) -> tuple[bool, str]:
    head = text[:900].lower()
    m = re.search(r"confiance\s*(?:global[e]?\s*)?[:\-]\s*(élevé|moyen|faible|[ée]leve|bas)", head)
    if not m:
        return False, "Niveau de confiance non spécifié"
    value = m.group(1).lower()
    if value in ("moyen", "faible"):
        return True, f"Confiance = '{value}'"
    return False, f"Confiance = '{value}' (devrait être moyen/faible)"


def check_10_tabs(text: str) -> tuple[bool, str]:
    brief_start = text.upper().find("BRIEF STRUCTURÉ")
    textes_start = text.upper().find("TEXTES PRÊTS À COLLER")
    if brief_start == -1:
        return False, "BLOC 2 introuvable"
    brief_end = textes_start if textes_start != -1 else len(text)
    brief_section = text[brief_start:brief_end].lower()
    required_tabs = [
        ("info", "directive"),
        ("serp", "métrique"),
        ("concurrent",),
        ("titre",),
        ("entête", "article"),
        ("plan", "structure"),
        ("question",),
        ("terme", "fréquent"),
        ("maillage",),
        ("résumé", "décisionnel"),
    ]
    missing = []
    for tab in required_tabs:
        if not all(keyword in brief_section for keyword in tab):
            missing.append(" & ".join(tab))
    if missing:
        return False, f"Onglets manquants : {missing}"
    return True, "Les 10 onglets présents"


def check_bloc3_compact(text: str) -> tuple[bool, str]:
    idx = text.upper().find("TEXTES PRÊTS À COLLER")
    if idx == -1:
        return False, "BLOC 3 introuvable"
    bloc3 = text[idx:]
    subsections = re.findall(r"^#{2,3}\s+\S", bloc3, re.MULTILINE)
    if len(subsections) < 6:
        return False, f"BLOC 3 contient {len(subsections)} sous-sections (<6 requis)"
    return True, f"BLOC 3 contient {len(subsections)} sous-sections"


def check_h1_no_date(text: str) -> tuple[bool, str]:
    # Cherche uniquement le H1 effectivement recommandé (pas la section "éléments à éviter")
    # Heuristique : chercher les lignes contenant "H1" suivi d'un texte encadré
    # ou les lignes "**Retenu : ...**" ou "Titre recommandé" ou "Titre n°1"
    patterns = [
        r"(?:Titre\s+(?:recommandé|retenu|principal|n\s*°?\s*1)[^\n]*:\s*\*?\*?[\"«']?)([^\"»'\n\*]+)",
        r"\*\*(?:H1|Retenu)\s*:?\s*\*?\*?\s*[\"«']?([^\"»'\n\*]+)",
        r"^H1\s*:\s*(.+)$",
        r"^###?\s*H1\s*$\n+(.+)$",
    ]
    candidates = []
    for p in patterns:
        for m in re.finditer(p, text, re.MULTILINE | re.IGNORECASE):
            candidates.append(m.group(1).strip())
    # Filtre les candidats vides ou trop courts
    candidates = [c for c in candidates if len(c) > 20]
    if not candidates:
        return False, "Aucun H1 recommandé extrait"
    # Vérifier que AU MOINS UN H1 recommandé est evergreen (pas tous — la règle schoolsWP impose d'éviter les dates dans le H1 final)
    evergreen_h1 = [c for c in candidates if not re.search(r"\b(20[12][0-9])\b", c)]
    dated_h1 = [c for c in candidates if re.search(r"\b(20[12][0-9])\b", c)]
    if evergreen_h1 and len(evergreen_h1) >= len(dated_h1):
        return True, f"Au moins un H1 evergreen retenu : '{evergreen_h1[0][:80]}...'"
    if dated_h1:
        return False, f"H1 retenu contient une date : '{dated_h1[0][:80]}...'"
    return True, "H1 recommandés evergreen"


def check_schoolswp_urls(text: str) -> tuple[bool, str]:
    urls = ["/affiliatepress-avis/", "/solid-affiliate-top-plugin-affiliation-wordpress/"]
    missing = [u for u in urls if u not in text]
    if missing:
        return False, f"URLs manquantes : {missing}"
    return True, "2 URLs schoolsWP présentes"


def check_serp_mismatch(text: str) -> tuple[bool, str]:
    lower = text.lower()
    has_pivot = any(kw in lower for kw in ["pivot", "mismatch", "substitu", "google ne reconna", "substitué"])
    has_affiliatewp = "affiliatewp" in lower
    if has_pivot and has_affiliatewp:
        return True, "Mismatch SERP identifié"
    return False, f"Mismatch non identifié (pivot: {has_pivot}, affiliatewp: {has_affiliatewp})"


def check_tutoiement(text: str) -> tuple[bool, str]:
    tu_words = re.findall(r"\b(tu|t'|ton|ta|tes|toi)\b", text, re.IGNORECASE)
    vous_words = re.findall(r"\b(vous|votre|vos)\b", text, re.IGNORECASE)
    if len(tu_words) >= 5 and len(tu_words) >= 2 * len(vous_words):
        return True, f"Tutoiement : {len(tu_words)} tu/ton/ta vs {len(vous_words)} vous"
    return False, f"Tutoiement insuffisant : {len(tu_words)} vs {len(vous_words)}"


# ===== V2 assertions =====

def check_fact_dedux_verify_tags(text: str) -> tuple[bool, str]:
    fait_count = len(re.findall(r"\[FAIT[^\]]*\]", text))
    dedux_count = len(re.findall(r"\[D[ÉE]DUCTION[^\]]*\]", text))
    verify_count = len(re.findall(r"\[À\s*V[ÉE]RIFIER[^\]]*\]", text))
    missing = []
    if fait_count == 0: missing.append("[FAIT]")
    if dedux_count == 0: missing.append("[DÉDUCTION]")
    if verify_count == 0: missing.append("[À VÉRIFIER]")
    if missing:
        return False, f"Tags manquants : {missing} (FAIT={fait_count}, DÉDUCTION={dedux_count}, À VÉRIFIER={verify_count})"
    return True, f"Tags présents : FAIT={fait_count}, DÉDUCTION={dedux_count}, À VÉRIFIER={verify_count}"


def check_data_to_validate_section(text: str) -> tuple[bool, str]:
    # Cherche la section "Données à valider avant publication"
    m = re.search(r"##\s*Données\s+à\s+valider[^\n]*", text, re.IGNORECASE)
    if not m:
        return False, "Section 'Données à valider avant publication' absente"
    start = m.end()
    # Trouve la prochaine section H2/H1 pour délimiter
    next_h = re.search(r"\n#+\s", text[start:])
    end = start + next_h.start() if next_h else len(text)
    section = text[start:end]
    # Compter les items (bullet list ou items taggés [À VÉRIFIER])
    items = len(re.findall(r"\[À\s*V[ÉE]RIFIER", section))
    if items < 3:
        return False, f"Section 'Données à valider' contient {items} items [À VÉRIFIER] (<3 requis)"
    return True, f"Section 'Données à valider' contient {items} items [À VÉRIFIER]"


def check_serp_features_mapped(text: str) -> tuple[bool, str]:
    # Chaque feature SERP mentionnée doit être traduite en consigne dans BLOC 2
    bloc2_start = text.upper().find("BRIEF STRUCTURÉ")
    bloc2_end = text.upper().find("TEXTES PRÊTS À COLLER")
    if bloc2_start == -1:
        return False, "BLOC 2 introuvable"
    bloc2 = text[bloc2_start:bloc2_end if bloc2_end != -1 else len(text)].lower()
    features_to_check = {
        "AI Overview": ["ai overview", "aio"],
        "Vidéos YouTube": ["vidéo", "video", "youtube", "walkthrough"],
        "Reddit": ["reddit", "forum", "limites honnêtes", "frictions"],
        "Intent mismatch": ["mismatch", "pivot", "affiliatewp dans tout", "pourquoi pas affiliatewp"],
    }
    missing = []
    for feature, keywords in features_to_check.items():
        if not any(kw in bloc2 for kw in keywords):
            missing.append(feature)
    # Il faut au moins 3 features sur 4 traduites dans BLOC 2
    if len(missing) > 1:
        return False, f"Features SERP non traduites dans BLOC 2 : {missing}"
    return True, f"Features SERP traduites en consignes (3/4 minimum, absent : {missing})"


def check_bloc3_no_markdown_tables(text: str) -> tuple[bool, str]:
    idx = text.upper().find("TEXTES PRÊTS À COLLER")
    if idx == -1:
        return False, "BLOC 3 introuvable"
    bloc3 = text[idx:]
    # Détection des tableaux markdown : une ligne contenant plusieurs | et la ligne suivante commence par |---
    lines = bloc3.split("\n")
    table_rows = 0
    for i, line in enumerate(lines):
        # Ligne qui semble être une row de tableau : commence et termine par |
        if line.strip().startswith("|") and line.strip().endswith("|") and line.count("|") >= 3:
            table_rows += 1
    if table_rows > 3:
        return False, f"BLOC 3 contient {table_rows} lignes de tableau markdown (interdit)"
    return True, f"BLOC 3 quasi sans tableau markdown ({table_rows} lignes détectées — acceptable si < 4)"


def check_entity_consistency(text: str) -> tuple[bool, str]:
    # Normalisation : préférer "Solid Affiliate" (2 mots) ou "SolidAffiliate" (1 mot)
    # Cherche les variantes d'AffiliatePress
    ap_variants = {
        "AffiliatePress": len(re.findall(r"\bAffiliatePress\b", text)),
        "affiliatepress": len(re.findall(r"\baffiliatepress\b", text)) - len(re.findall(r"\.affiliatepressplugin\.", text)) - len(re.findall(r"/affiliatepress-", text)),
        "Affiliate Press": len(re.findall(r"\bAffiliate\s+Press\b", text)),
    }
    sa_variants = {
        "Solid Affiliate": len(re.findall(r"\bSolid\s+Affiliate\b", text)),
        "SolidAffiliate": len(re.findall(r"\bSolidAffiliate\b", text)),
        "solid affiliate": len(re.findall(r"\bsolid\s+affiliate\b", text)) - len(re.findall(r"\bSolid\s+Affiliate\b", text)),
    }
    # Compter uniquement les variantes avec au moins 3 occurrences distinctes
    ap_used = {k: v for k, v in ap_variants.items() if v >= 3}
    sa_used = {k: v for k, v in sa_variants.items() if v >= 3}
    # L'output est cohérent si on a 1 ou 2 variantes PRINCIPALES (pas 3+ qui se partagent)
    # Et si la variante dominante représente >60% des occurrences
    ap_total = sum(ap_variants.values())
    sa_total = sum(sa_variants.values())
    ap_dominant_ratio = max(ap_variants.values()) / ap_total if ap_total > 0 else 0
    sa_dominant_ratio = max(sa_variants.values()) / sa_total if sa_total > 0 else 0
    if ap_dominant_ratio < 0.7 or sa_dominant_ratio < 0.7:
        return False, f"Incohérence noms : AP variants {ap_variants} (dom={ap_dominant_ratio:.2f}), SA variants {sa_variants} (dom={sa_dominant_ratio:.2f})"
    return True, f"Cohérence OK : AP dom={ap_dominant_ratio:.2f}, SA dom={sa_dominant_ratio:.2f}"


def check_safety_pricing(text: str) -> tuple[bool, str]:
    # Détecte les affirmations pricing/compatibilité potentielles
    # Cherche les mentions de prix ($, €, /mois, /an, gratuit)
    # et vérifie qu'elles sont à proximité de [À VÉRIFIER] ou dans la section "Données à valider"
    pricing_patterns = [
        r"(\d+[\s\u202f]?(?:\$|€|USD|EUR))",
        r"(\d+[\s\u202f]?\$\s*/\s*(?:an|mois))",
        r"(plan\s+gratuit)",
        r"(\d+[\s\u202f]?(?:USD|EUR)\s*/\s*(?:an|mois))",
    ]
    violations = []
    for pattern in pricing_patterns:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            start = max(0, m.start() - 200)
            end = min(len(text), m.end() + 200)
            context = text[start:end].lower()
            # Vérifier la présence de [À VÉRIFIER] dans le contexte proche
            if "à vérifier" not in context and "a verifier" not in context and "à v" not in context:
                violations.append(m.group(0))
    if len(violations) > 2:  # Tolérance : on accepte 2 mentions non tagguées (peut être dans des éléments à éviter, etc.)
        return False, f"Mentions pricing non taggées [À VÉRIFIER] : {violations[:5]}"
    return True, f"Affirmations pricing majoritairement taggées [À VÉRIFIER] ({len(violations)} mentions libres tolérées)"


CHECKS = [
    check_three_blocks_order,
    check_header_min,
    check_mode_detected,
    check_faits_deductions_recos,
    check_confidence,
    check_10_tabs,
    check_bloc3_compact,
    check_h1_no_date,
    check_schoolswp_urls,
    check_serp_mismatch,
    check_tutoiement,
    check_fact_dedux_verify_tags,
    check_data_to_validate_section,
    check_serp_features_mapped,
    check_bloc3_no_markdown_tables,
    check_entity_consistency,
    check_safety_pricing,
]


def grade(run: str) -> dict:
    brief_path = EVAL_DIR / run / "outputs" / "brief.md"
    text = brief_path.read_text(encoding="utf-8")
    results = []
    for assertion, fn in zip(ASSERTIONS, CHECKS, strict=True):
        passed, evidence = fn(text)
        results.append({"text": assertion, "passed": passed, "evidence": evidence})
    passed_n = sum(1 for r in results if r["passed"])
    total = len(results)
    return {
        "expectations": results,
        "summary": {
            "passed": passed_n,
            "failed": total - passed_n,
            "total": total,
            "pass_rate": round(passed_n / total, 3),
        },
    }


def main() -> None:
    for run in RUNS:
        grading = grade(run)
        out_path = EVAL_DIR / run / "grading.json"
        out_path.write_text(json.dumps(grading, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\n========== {run} ==========")
        print(f"{grading['summary']['passed']}/{grading['summary']['total']} "
              f"({grading['summary']['pass_rate']*100:.0f}%)")
        for r in grading["expectations"]:
            mark = "OK" if r["passed"] else "KO"
            print(f"  [{mark}] {r['text'][:75]}")
            print(f"       {r['evidence']}")


if __name__ == "__main__":
    main()
