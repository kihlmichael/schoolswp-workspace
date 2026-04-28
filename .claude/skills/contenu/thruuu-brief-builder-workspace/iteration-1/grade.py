"""Grader programmatique pour eval-1 thruuu-brief-builder.

Vérifie 11 assertions sur chaque output (with_skill + without_skill).
Écrit grading.json au format attendu par le viewer skill-creator.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ITER_DIR = Path(__file__).parent
EVAL_DIR = ITER_DIR / "eval-1-affiliatepress-vs-solidaffiliate"
RUNS = ["with_skill", "without_skill"]

ASSERTIONS = [
    "L'output contient les 3 blocs dans l'ordre : ANALYSE GLOBALE, puis BRIEF STRUCTURÉ, puis TEXTES PRÊTS À COLLER",
    "En-tête minimal présent avec les 4 champs (Mot-clé, Mode, Sources utilisées, Confiance) avant le premier bloc",
    "Le mode de brief détecté est 'comparatif' (explicitement) avec 'avis' comme secondaire possible",
    "Le BLOC 1 contient 3 sections distinctes : Faits, Déductions, Recommandations",
    "Le niveau de confiance global est 'moyen' ou 'faible' (pas 'élevé' puisque GSC manquante)",
    "Le BLOC 2 contient les 10 onglets numérotés dans l'ordre (Info & directive, SERP métriques, Analyse concurrents, Meilleurs titres, Entête, Plan, FAQ, Termes fréquents, Maillage interne, Résumé décisionnel)",
    "Le BLOC 3 'TEXTES PRÊTS À COLLER' existe et contient au moins 6 sous-sections rédigées de façon compacte",
    "Le H1 recommandé ne contient pas 'en 2026' ni de date (règle schoolsWP evergreen)",
    "Les 2 URLs schoolsWP existantes sont présentes dans le maillage interne (/affiliatepress-avis/ et /solid-affiliate-top-plugin-affiliation-wordpress/)",
    "Le brief identifie explicitement le mismatch SERP (Google pivote vers 'Solid Affiliate vs AffiliateWP' au lieu de 'vs AffiliatePress')",
    "Le brief utilise le tutoiement (tu/ton/ta/toi) et pas le vouvoiement dans les formulations éditoriales",
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
        return False, f"Ordre incorrect : ANALYSE@{i_analyse}, BRIEF@{i_brief}, TEXTES@{i_textes}"
    return True, f"Ordre correct : ANALYSE@{i_analyse} < BRIEF@{i_brief} < TEXTES@{i_textes}"


def check_header_min(text: str) -> tuple[bool, str]:
    head = text[:500].lower()
    required = ["mot-clé", "mode", "source", "confiance"]
    missing = [k for k in required if k not in head]
    if missing:
        return False, f"Champs d'en-tête manquants dans les 500 premiers car : {missing}"
    return True, "Les 4 champs d'en-tête (Mot-clé, Mode, Sources, Confiance) sont présents en tête"


def check_mode_detected(text: str) -> tuple[bool, str]:
    head = text[:800].lower()
    if "comparatif" not in head:
        return False, "Mode 'comparatif' non mentionné dans l'en-tête"
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
        return False, f"Sections manquantes dans BLOC 1 : {missing}"
    return True, f"Les 3 sections (Faits, Déductions, Recommandations) sont présentes dans BLOC 1"


def check_confidence(text: str) -> tuple[bool, str]:
    head = text[:800].lower()
    m = re.search(r"confiance\s*[:\-]\s*(élevé|moyen|faible|[ée]leve|bas)", head)
    if not m:
        return False, "Niveau de confiance non spécifié dans l'en-tête"
    value = m.group(1).lower()
    if value in ("moyen", "faible"):
        return True, f"Confiance = '{value}' (cohérent avec GSC manquante)"
    return False, f"Confiance = '{value}' mais devrait être 'moyen' ou 'faible' (GSC absente)"


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
        ("question",),  # FAQ
        ("terme", "fréquent"),
        ("maillage",),
        ("résumé", "décisionnel"),
    ]
    missing = []
    for tab in required_tabs:
        if not all(keyword in brief_section for keyword in tab):
            missing.append(" & ".join(tab))
    if missing:
        return False, f"Onglets manquants dans BLOC 2 : {missing}"
    return True, "Les 10 onglets du BLOC 2 sont présents"


def check_bloc3_compact(text: str) -> tuple[bool, str]:
    idx = text.upper().find("TEXTES PRÊTS À COLLER")
    if idx == -1:
        return False, "BLOC 3 'TEXTES PRÊTS À COLLER' introuvable"
    bloc3 = text[idx:]
    # Compter les sous-sections H2 (##) ou H3 (###) dans le BLOC 3
    subsections = re.findall(r"^#{2,3}\s+\S", bloc3, re.MULTILINE)
    if len(subsections) < 6:
        return False, f"BLOC 3 ne contient que {len(subsections)} sous-sections (<6 requis)"
    return True, f"BLOC 3 contient {len(subsections)} sous-sections"


def check_h1_no_date(text: str) -> tuple[bool, str]:
    # Trouver le H1 recommandé : on cherche dans l'entête de l'article (section 5)
    # Heuristique : on cherche les lignes qui commencent par "H1" ou qui contiennent "H1 recommandé"
    matches = re.findall(r"(?:H1[^a-z]{0,20}[^\n]+)", text, re.IGNORECASE)
    if not matches:
        return False, "Aucun H1 recommandé trouvé"
    # Prendre tous les candidats H1 et vérifier qu'aucun ne contient une date
    for h1_line in matches:
        if re.search(r"\b(20[12][0-9])\b", h1_line):
            return False, f"H1 contient une date : '{h1_line.strip()[:100]}'"
    # Chercher aussi une ligne en gras qui ressemble à un H1 recommandé
    bold_h1 = re.findall(r"\*\*(?:(?:Retenu|Titre recommandé|Titre n°1|Titre principal)[^*]*)\*\*", text)
    for line in bold_h1:
        if re.search(r"\b(20[12][0-9])\b", line):
            return False, f"H1 en gras contient une date : '{line[:100]}'"
    return True, "Les H1 recommandés sont evergreen (aucune date)"


def check_schoolswp_urls(text: str) -> tuple[bool, str]:
    urls_required = [
        "/affiliatepress-avis/",
        "/solid-affiliate-top-plugin-affiliation-wordpress/",
    ]
    missing = [u for u in urls_required if u not in text]
    if missing:
        return False, f"URLs schoolsWP manquantes dans le maillage : {missing}"
    return True, "Les 2 URLs schoolsWP existantes sont présentes"


def check_serp_mismatch(text: str) -> tuple[bool, str]:
    lower = text.lower()
    has_pivot = ("pivot" in lower or "mismatch" in lower or "substitu" in lower or "google ne reconna" in lower)
    has_affiliatewp_mention = "affiliatewp" in lower
    if has_pivot and has_affiliatewp_mention:
        return True, "Le mismatch SERP est identifié (pivot/substitution vers AffiliateWP mentionnée)"
    return False, f"Mismatch SERP non identifié explicitement (pivot/substitu: {has_pivot}, affiliatewp: {has_affiliatewp_mention})"


def check_tutoiement(text: str) -> tuple[bool, str]:
    # Compter tu/ton/ta/toi vs vous/votre/vos dans l'accroche/intro (section 5)
    # Heuristique : compter les occurrences dans tout le doc
    tu_words = re.findall(r"\b(tu|t'|ton|ta|tes|toi)\b", text, re.IGNORECASE)
    vous_words = re.findall(r"\b(vous|votre|vos)\b", text, re.IGNORECASE)
    # Tutoiement dominant si tu_count >= 2x vous_count (et tu_count > 5 pour éviter les faux positifs)
    if len(tu_words) >= 5 and len(tu_words) >= 2 * len(vous_words):
        return True, f"Tutoiement dominant : {len(tu_words)} occurrences tu/ton/ta vs {len(vous_words)} vous/votre"
    return False, f"Tutoiement insuffisant : {len(tu_words)} tu/ton/ta vs {len(vous_words)} vous/votre"


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
        print(f"{run}: {grading['summary']['passed']}/{grading['summary']['total']} "
              f"({grading['summary']['pass_rate']*100:.0f}%)")
        for r in grading["expectations"]:
            mark = "OK" if r["passed"] else "KO"
            print(f"  [{mark}] {r['text'][:70]}")
            print(f"       {r['evidence']}")


if __name__ == "__main__":
    main()
