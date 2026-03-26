#!/usr/bin/env python3
"""
CLI — Professeur IA Vente Digitale WordPress schoolsWP

Usage :
  python -m agents.wp_digital_sales.cli --topic "La page de vente qui convertit"
  python -m agents.wp_digital_sales.cli --topic "..." --offer-type "formation vidéo" --audience "freelances"
  python -m agents.wp_digital_sales.cli --topic "..." --question "..." --output lecons/page-vente.md
  python -m agents.wp_digital_sales.cli --list-topics
"""

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base import safe_write_path
from agents.wp_digital_sales.agent import WpDigitalSalesAgent

_SUGGESTED_TOPICS = [
    # Fondements de l'offre
    "Clarifier son offre : que vend-on, à qui, pour quel résultat ?",
    "Un site, une offre principale : pourquoi la dispersion tue la conversion",
    "Le parcours d'achat : de l'inconnu à l'acheteur en 5 étapes",
    "Prix d'une formation ou d'un produit digital : comment le fixer et le justifier",
    # Architecture du site de vente
    "La page d'accueil d'un site de vente digitale",
    "La page de vente qui convertit : anatomie complète",
    "La page À propos orientée légitimité (pas CV)",
    "La FAQ qui lève les objections réelles",
    "La page de confirmation d'achat et l'accès immédiat",
    # Confiance et preuve sociale
    "Les témoignages qui convainquent (pas les avis génériques)",
    "Construire sa légitimité sans avoir 10 ans d'expérience",
    "La garantie de satisfaction : rassurer sans se mettre en danger",
    # Technique WordPress
    "WooCommerce pour vendre un produit numérique (ebook, template, pack)",
    "Tutor LMS ou LifterLMS : héberger une formation sur WordPress",
    "MemberPress / Paid Memberships Pro : créer un abonnement",
    "Stripe et PayPal sur WordPress : configuration de base",
    "Livraison automatique d'un produit numérique après achat",
    # Acquisition et conversion
    "Le lead magnet : offrir gratuitement pour vendre ensuite",
    "La séquence email post-inscription : nourrir avant de vendre",
    "Page d'atterrissage (landing page) pour un webinaire ou une masterclass",
    "Urgence éthique : créer de l'incitation sans manipulation",
    # Optimisation
    "Analyser ses conversions : les métriques qui comptent vraiment",
    "Optimiser une page de vente qui ne convertit pas",
    "Upsell et cross-sell : augmenter la valeur client sans forcer",
]

_OFFER_TYPES = [
    "formation vidéo en ligne",
    "programme d'accompagnement / coaching",
    "ebook / guide PDF",
    "template / pack de ressources",
    "membership / accès abonnement",
    "masterclass / webinaire payant",
    "bundle (formation + coaching + ressources)",
    "mini-cours (< 3h, prix < 100€)",
]

_AUDIENCE_TYPES = [
    "freelances / indépendants",
    "entrepreneurs débutants",
    "créateurs de contenu",
    "professionnels en reconversion",
    "PME / dirigeants de petites entreprises",
    "coachs / thérapeutes",
    "artistes / créatifs",
]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wp-digital-sales",
        description=(
            "Professeur IA Vente Digitale WordPress schoolsWP — "
            "vendre formations et produits numériques, système de conversion"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  # Leçon simple\n"
            "  python -m agents.wp_digital_sales.cli \\\n"
            '    --topic "La page de vente qui convertit"\n\n'
            "  # Leçon contextualisée avec offre et audience\n"
            "  python -m agents.wp_digital_sales.cli \\\n"
            '    --topic "WooCommerce pour vendre un produit numérique" \\\n'
            '    --offer-type "template WordPress" \\\n'
            '    --audience "freelances WordPress" \\\n'
            "    --output lecons/woocommerce-produit-digital.md\n\n"
            "  # Débloquer un problème de conversion\n"
            "  python -m agents.wp_digital_sales.cli \\\n"
            '    --topic "Optimiser une page de vente" \\\n'
            '    --question "Ma page reçoit des visites mais personne n\'achète" \\\n'
            '    --offer-type "formation vidéo en ligne"\n\n'
            "  # Voir tous les sujets disponibles\n"
            "  python -m agents.wp_digital_sales.cli --list-topics"
        ),
    )
    parser.add_argument(
        "--topic",
        metavar="SUJET",
        help="Notion à apprendre (ex: 'La page de vente', 'WooCommerce produit numérique')",
    )
    parser.add_argument(
        "--question",
        metavar="QUESTION",
        default=None,
        help="Question ou problème de conversion précis",
    )
    parser.add_argument(
        "--offer-type",
        metavar="OFFRE",
        default=None,
        help="Type d'offre (ex: 'formation vidéo', 'ebook', 'programme coaching', 'membership')",
    )
    parser.add_argument(
        "--audience",
        metavar="AUDIENCE",
        default=None,
        help="Cible de l'offre (ex: 'freelances WordPress', 'entrepreneurs débutants')",
    )
    parser.add_argument(
        "--level",
        metavar="NIVEAU",
        default="débutant créateur de produit digital",
        help="Niveau déclaré (défaut : 'débutant créateur de produit digital')",
    )
    parser.add_argument(
        "--output",
        metavar="FICHIER",
        default=None,
        help="Chemin de sortie (.md). Si absent, affiche dans le terminal.",
    )
    parser.add_argument(
        "--model",
        default=None,
        metavar="MODEL",
        help="Modèle Claude (défaut : $MODEL_WRITER ou claude-sonnet-4-6)",
    )
    parser.add_argument(
        "--list-topics",
        action="store_true",
        default=False,
        help="Affiche tous les sujets vente digitale disponibles",
    )
    return parser


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.list_topics:
        print("\n🛒 Sujets Vente Digitale WordPress disponibles :\n")
        categories = {
            "Fondements de l'offre": _SUGGESTED_TOPICS[:4],
            "Architecture du site de vente": _SUGGESTED_TOPICS[4:9],
            "Confiance & preuve sociale": _SUGGESTED_TOPICS[9:12],
            "Technique WordPress": _SUGGESTED_TOPICS[12:17],
            "Acquisition & conversion": _SUGGESTED_TOPICS[17:21],
            "Optimisation": _SUGGESTED_TOPICS[21:],
        }
        for category, topics in categories.items():
            print(f"  {category} :")
            for topic in topics:
                print(f"    - {topic}")
            print()
        print("Types d'offres :")
        for o in _OFFER_TYPES:
            print(f"  - {o}")
        print("\nAudiences cibles :")
        for a in _AUDIENCE_TYPES:
            print(f"  - {a}")
        print('\nUtilise : python -m agents.wp_digital_sales.cli --topic "<sujet>" --offer-type "<offre>"\n')
        return

    if not args.topic:
        parser.error("L'argument --topic est requis. Utilise --list-topics pour voir les sujets disponibles.")

    agent = WpDigitalSalesAgent(model=args.model)

    print("\n[wp-digital-sales] Préparation de la leçon...", flush=True)
    print(f"  Sujet    : {args.topic}", flush=True)
    if args.offer_type:
        print(f"  Offre    : {args.offer_type}", flush=True)
    if args.audience:
        print(f"  Audience : {args.audience}", flush=True)
    if args.question:
        print(f"  Question : {args.question}", flush=True)
    print("", flush=True)

    lesson = await agent.run(
        topic=args.topic,
        question=args.question,
        offer_type=args.offer_type,
        audience=args.audience,
        level=args.level,
    )

    if args.output:
        try:
            output_path = safe_write_path(args.output)
        except ValueError as e:
            print(f"[wp-digital-sales] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(lesson, encoding="utf-8")
        print(f"[wp-digital-sales] Leçon sauvegardée → {output_path}")
    else:
        print(lesson)


if __name__ == "__main__":
    asyncio.run(main())
