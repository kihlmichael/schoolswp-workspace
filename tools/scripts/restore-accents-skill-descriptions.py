"""
Vague 2 : restaure les accents dans les descriptions FR-sans-accents des SKILL.md.

Applique des remplacements UNIQUEMENT pour des mots FR ou l'absence d'accent
est sans ambiguite (pas de variante EN/contextuelle). Ne touche que le bloc
description du frontmatter (single-line ou multi-line block scalar).

Usage :
  python restore-accents-skill-descriptions.py            # dry-run + diff
  python restore-accents-skill-descriptions.py --apply    # ecrit sur disque
"""

import argparse
import os
import re
import sys

ROOT = ".claude/skills"

# Remplacements bidirectionnels casse-preserves (haute confiance)
# Format : pattern (sans accent) -> remplacement (avec accents)
# Important : on traite separement majuscule/minuscule pour preserver la casse
PAIRS = [
    # methode/methodologie
    ("methode", "méthode"),
    ("methodes", "méthodes"),
    ("methodologie", "méthodologie"),
    ("methodologies", "méthodologies"),
    # generer / genere / generation
    ("generer", "générer"),
    ("genere", "génère"),
    ("generes", "génères"),
    ("generee", "générée"),
    ("generees", "générées"),
    ("generation", "génération"),
    ("generations", "générations"),
    # deja
    ("deja", "déjà"),
    # requete
    ("requete", "requête"),
    ("requetes", "requêtes"),
    # reutilisable
    ("reutilisable", "réutilisable"),
    ("reutilisables", "réutilisables"),
    # integration
    ("integration", "intégration"),
    ("integrations", "intégrations"),
    ("integre", "intègre"),
    ("integree", "intégrée"),
    ("integres", "intègres"),
    ("integrees", "intégrées"),
    ("integrer", "intégrer"),
    # frequence / frequente / frequent
    ("frequence", "fréquence"),
    ("frequences", "fréquences"),
    ("frequente", "fréquente"),
    ("frequentes", "fréquentes"),
    ("frequent", "fréquent"),
    ("frequents", "fréquents"),
    # specifique
    ("specifique", "spécifique"),
    ("specifiques", "spécifiques"),
    # specialise
    ("specialise", "spécialisé"),
    ("specialisee", "spécialisée"),
    ("specialises", "spécialisés"),
    ("specialisees", "spécialisées"),
    ("specialiser", "spécialiser"),
    # coherent / coherence
    ("coherent", "cohérent"),
    ("coherente", "cohérente"),
    ("coherents", "cohérents"),
    ("coherentes", "cohérentes"),
    ("coherence", "cohérence"),
    # categorie
    ("categorie", "catégorie"),
    ("categories", "catégories"),
    ("categorise", "catégorisé"),
    ("categorisee", "catégorisée"),
    ("categoriser", "catégoriser"),
    # strategie / strategique
    ("strategie", "stratégie"),
    ("strategies", "stratégies"),
    ("strategique", "stratégique"),
    ("strategiques", "stratégiques"),
    # prerequis
    ("prerequis", "prérequis"),
    # aleatoire
    ("aleatoire", "aléatoire"),
    ("aleatoires", "aléatoires"),
    # pedagogique / pedagogie
    ("pedagogique", "pédagogique"),
    ("pedagogiques", "pédagogiques"),
    ("pedagogie", "pédagogie"),
    # decisionnel
    ("decisionnel", "décisionnel"),
    ("decisionnelle", "décisionnelle"),
    ("decisionnels", "décisionnels"),
    ("decisionnelles", "décisionnelles"),
    # interprete
    ("interprete", "interprète"),
    ("interpretee", "interprétée"),
    ("interpreter", "interpréter"),
    # opere / operer / operationnel
    ("operer", "opérer"),
    ("opere", "opère"),
    ("operee", "opérée"),
    ("operationnel", "opérationnel"),
    ("operationnels", "opérationnels"),
    ("operationnelle", "opérationnelle"),
    ("operationnelles", "opérationnelles"),
    # creer (verbe) - cree (forme)
    ("creer", "créer"),
    # NB: "cree" ambigu (peut etre "crée" ou "créé"), on saute
    # references / referencer
    ("references", "références"),  # nom pluriel
    ("referencer", "référencer"),
    ("reference", "référence"),  # nom singulier - mais peut etre verbe "il reference" -> "il référence"
    # priorite
    ("priorite", "priorité"),
    ("priorites", "priorités"),
    ("prioritaire", "prioritaire"),  # deja correct
    ("prioriser", "prioriser"),  # deja correct
    # cle / cible (mots courts ambigus avec EN, on les saute)
    # NB: "publie" / "publier" / "applique" / "applique" - ambigus, on saute
    # systeme
    ("systeme", "système"),
    ("systemes", "systèmes"),
    # detecter
    ("detecter", "détecter"),
    ("detectee", "détectée"),
    ("detecter", "détecter"),
    # determine / determiner
    ("determiner", "déterminer"),
    ("determinee", "déterminée"),
    ("determine", "détermine"),
    # definir
    ("definir", "définir"),
    ("definie", "définie"),
    ("defini", "défini"),
    ("definis", "définis"),
    ("definies", "définies"),
    ("definition", "définition"),
    ("definitions", "définitions"),
    # securite / securitaire
    ("securite", "sécurité"),
    ("securitaire", "sécuritaire"),
    # nettoyage
    ("nettoyage", "nettoyage"),  # OK
    # chronologique
    ("chronologique", "chronologique"),  # OK
    # recupere
    ("recuperer", "récupérer"),
    ("recupere", "récupère"),
    ("recuperee", "récupérée"),
    # qualifier
    ("qualifier", "qualifier"),  # OK
    ("qualifie", "qualifié"),
    ("qualifiee", "qualifiée"),
    # complete (adjectif "la liste complete" -> "complète" ; verbe "il complete" -> "il complète")
    ("complete", "complète"),
    ("completer", "compléter"),
    ("completee", "complétée"),
    # ameliore / ameliorer
    ("ameliorer", "améliorer"),
    ("amelioree", "améliorée"),
    ("ameliore", "améliore"),
    # detaille / detailler
    ("detailler", "détailler"),
    ("detaillee", "détaillée"),
    ("detaille", "détaille"),
    # echelle
    ("echelle", "échelle"),
    ("echelles", "échelles"),
    # Vague 3 : compléments
    ("donnee", "donnée"),
    ("donnees", "données"),
    ("reelle", "réelle"),
    ("reelles", "réelles"),
    ("reel", "réel"),
    ("reels", "réels"),
    ("acces", "accès"),
    ("execution", "exécution"),
    ("executer", "exécuter"),
    ("executee", "exécutée"),
    ("execute", "exécute"),
    ("controle", "contrôle"),
    ("controler", "contrôler"),
    ("controlee", "contrôlée"),
    ("modele", "modèle"),
    ("modeles", "modèles"),
    ("regles", "règles"),
    ("regle", "règle"),
    ("modeliser", "modéliser"),
    ("represente", "représente"),
    ("representer", "représenter"),
    ("representation", "représentation"),
    ("representations", "représentations"),
]


def case_preserve_replace(text: str, src: str, dst: str) -> str:
    """Replace whole-word src with dst, preserving case (UPPER/Title/lower)."""

    def replacement(match):
        word = match.group(0)
        if word == word.upper():
            return dst.upper()
        if word[0].isupper():
            return dst[0].upper() + dst[1:]
        return dst

    pattern = re.compile(rf"\b{re.escape(src)}\b", re.IGNORECASE)
    return pattern.sub(replacement, text)


def patch_description_block(content: str) -> tuple[str, list[str]]:
    """Apply accent restoration only inside the description block of frontmatter."""
    fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        return content, []
    fm = fm_match.group(1)
    fm_start, fm_end = fm_match.span(1)

    desc_re = re.compile(
        r"(^description:\s*[|>]?[+-]?\s*)([\s\S]+?)(?=\n[a-zA-Z_-]+:|\Z)",
        re.MULTILINE,
    )
    m = desc_re.search(fm)
    if not m:
        return content, []
    prefix = m.group(1)
    desc = m.group(2)

    new_desc = desc
    changes = []
    for src, dst in PAIRS:
        before = new_desc
        new_desc = case_preserve_replace(new_desc, src, dst)
        if before != new_desc:
            changes.append(f"{src} -> {dst}")

    if new_desc == desc:
        return content, []
    new_fm = fm[: m.start()] + prefix + new_desc + fm[m.end():]
    return content[:fm_start] + new_fm + content[fm_end:], changes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    total_changed = 0
    for root, _, files in os.walk(ROOT):
        for fname in files:
            if fname != "SKILL.md":
                continue
            path = os.path.join(root, fname)
            with open(path, encoding="utf-8") as f:
                content = f.read()
            new_content, changes = patch_description_block(content)
            if not changes:
                continue
            rel = os.path.relpath(path, ROOT).replace("\\", "/")
            print(f"{'OK' if args.apply else 'WILL'} : {rel}")
            for c in changes[:5]:
                print(f"     - {c}")
            if len(changes) > 5:
                print(f"     - (+{len(changes) - 5} autres)")
            if args.apply:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)
            total_changed += 1

    print(f"\nTotal : {total_changed} fichier(s) {'patches' if args.apply else 'a patcher'}")
    if not args.apply:
        print("Dry-run : relancer avec --apply pour ecrire.")


if __name__ == "__main__":
    main()
