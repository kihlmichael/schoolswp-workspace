#!/usr/bin/env python3
"""
CLI — Professeur IA Architecte de Sites Rentables schoolsWP

Usage :
  python -m agents.wp_profit_architect.cli --topic "La page d'accueil rentable"
  python -m agents.wp_profit_architect.cli --topic "..." --business-model "vente de services"
  python -m agents.wp_profit_architect.cli --topic "..." --objective "5 demandes devis/mois"
  python -m agents.wp_profit_architect.cli --list-topics
"""
import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base import safe_write_path
from agents.wp_profit_architect.agent import WpProfitArchitectAgent

_SUGGESTED_TOPICS = [
    # Fondements
    "Choisir le modèle économique de son site (les 4 options)",
    "Un site, un objectif : pourquoi les sites qui veulent tout faire ne font rien bien",
    "Le parcours utilisateur rentable : Attirer → Rassurer → Convertir → Fidéliser",
    # Architecture des pages
    "La page d'accueil rentable : orienter, pas décorer",
    "La landing page parfaite : une offre, un CTA, zéro distraction",
    "La page À propos qui rassure et convertit",
    "La page Services / Offres qui donne envie d'acheter",
    "La page Contact / RDV qui facilite le passage à l'action",
    # Conversion
    "Les CTA (Call to Action) qui transforment des visiteurs en prospects",
    "Les formulaires de capture de leads : quand et comment les utiliser",
    "Les témoignages et preuves sociales : lever les objections",
    "Le lead magnet : offrir de la valeur pour capturer un email",
    # Trafic & visibilité
    "SEO de base orienté conversion (pas juste du trafic)",
    "Blog WordPress rentable : écrire pour attirer ET convertir",
    "Construire sa liste email depuis WordPress",
    # Technique au service du profit
    "Vitesse de chargement : chaque seconde perdue coûte des clients",
    "Choisir un thème pour la conversion (pas pour le design)",
    "Les plugins qui servent le profit (et ceux à bannir)",
    "WooCommerce : vendre des produits ou services en ligne",
    # Mesure & optimisation
    "Analytics : mesurer ce qui rapporte, supprimer ce qui ne sert à rien",
    "A/B testing simple sur WordPress : tester avant d'investir",
    "Optimiser son tunnel de conversion existant",
]

_BUSINESS_MODELS = [
    "génération de leads (formulaire / RDV)",
    "vente de services (consulting, freelance, coaching)",
    "vente de produits physiques (e-commerce WooCommerce)",
    "vente de produits numériques (formations, templates, ebooks)",
    "monétisation d'audience (affilié, pub, sponsors)",
    "abonnement / membership",
]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wp-profit-architect",
        description=(
            "Architecte de Sites Rentables schoolsWP — "
            "WordPress orienté profit, conversion et ROI"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  # Leçon simple\n"
            "  python -m agents.wp_profit_architect.cli \\\n"
            '    --topic "La page d\'accueil rentable"\n\n'
            "  # Leçon avec modèle économique et objectif\n"
            "  python -m agents.wp_profit_architect.cli \\\n"
            '    --topic "La landing page parfaite" \\\n'
            '    --business-model "vente de services" \\\n'
            '    --objective "5 demandes de devis par mois" \\\n'
            "    --output lecons/landing-page-rentable.md\n\n"
            "  # Débloquer une décision business\n"
            "  python -m agents.wp_profit_architect.cli \\\n"
            '    --topic "Choisir le modèle économique" \\\n'
            '    --question "J\'hésite entre vendre mes services en direct ou créer une formation" \\\n\n'
            "  # Voir tous les sujets disponibles\n"
            "  python -m agents.wp_profit_architect.cli --list-topics"
        ),
    )
    parser.add_argument(
        "--topic",
        metavar="SUJET",
        help="Notion à apprendre (ex: 'La page d'accueil rentable', 'Les CTA qui convertissent')",
    )
    parser.add_argument(
        "--question",
        metavar="QUESTION",
        default=None,
        help="Question ou décision business à trancher (ex: 'blog vs landing page pour mes débuts ?')",
    )
    parser.add_argument(
        "--business-model",
        metavar="MODÈLE",
        default=None,
        help="Modèle économique (ex: 'vente de services', 'génération de leads', 'e-commerce')",
    )
    parser.add_argument(
        "--objective",
        metavar="OBJECTIF",
        default=None,
        help="Objectif principal mesurable (ex: '5 demandes de devis/mois', '10 ventes/semaine')",
    )
    parser.add_argument(
        "--level",
        metavar="NIVEAU",
        default="débutant orienté profit",
        help="Niveau déclaré (défaut : 'débutant orienté profit')",
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
        help="Affiche tous les sujets 'site rentable' disponibles",
    )
    return parser


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.list_topics:
        print("\n💰 Sujets Site WordPress Rentable disponibles :\n")
        categories = {
            "Fondements business": _SUGGESTED_TOPICS[:3],
            "Architecture des pages": _SUGGESTED_TOPICS[3:8],
            "Conversion": _SUGGESTED_TOPICS[8:12],
            "Trafic & visibilité": _SUGGESTED_TOPICS[12:15],
            "Technique au service du profit": _SUGGESTED_TOPICS[15:19],
            "Mesure & optimisation": _SUGGESTED_TOPICS[19:],
        }
        for category, topics in categories.items():
            print(f"  {category} :")
            for topic in topics:
                print(f"    - {topic}")
            print()
        print("Modèles économiques :")
        for m in _BUSINESS_MODELS:
            print(f"  - {m}")
        print(
            "\nUtilise : python -m agents.wp_profit_architect.cli "
            '--topic "<sujet>" --business-model "<modèle>"\n'
        )
        return

    if not args.topic:
        parser.error(
            "L'argument --topic est requis. "
            "Utilise --list-topics pour voir les sujets disponibles."
        )

    agent = WpProfitArchitectAgent(model=args.model)

    print("\n[wp-profit-architect] Analyse en cours...", flush=True)
    print(f"  Sujet         : {args.topic}", flush=True)
    if args.business_model:
        print(f"  Modèle éco.   : {args.business_model}", flush=True)
    if args.objective:
        print(f"  Objectif      : {args.objective}", flush=True)
    if args.question:
        print(f"  Question      : {args.question}", flush=True)
    print("", flush=True)

    lesson = await agent.run(
        topic=args.topic,
        question=args.question,
        business_model=args.business_model,
        objective=args.objective,
        level=args.level,
    )

    if args.output:
        try:
            output_path = safe_write_path(args.output)
        except ValueError as e:
            print(f"[wp-profit-architect] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(lesson, encoding="utf-8")
        print(f"[wp-profit-architect] Leçon sauvegardée → {output_path}")
    else:
        print(lesson)


if __name__ == "__main__":
    asyncio.run(main())
