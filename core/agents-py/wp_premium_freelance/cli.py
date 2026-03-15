#!/usr/bin/env python3
"""
CLI — Professeur IA WordPress Premium Freelance schoolsWP

Usage :
  python -m agents.wp_premium_freelance.cli --topic "Positionner son offre premium"
  python -m agents.wp_premium_freelance.cli --topic "..." --client-profile "consultant senior"
  python -m agents.wp_premium_freelance.cli --topic "..." --budget-range "5000-15000€" --output lecons/premium.md
  python -m agents.wp_premium_freelance.cli --list-topics
"""
import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base import safe_write_path
from agents.wp_premium_freelance.agent import WpPremiumFreelanceAgent

_SUGGESTED_TOPICS = [
    # Positionnement premium
    "La différence fondamentale entre un site standard et un site premium",
    "Positionner son offre freelance WordPress en haut de gamme",
    "Fixer ses tarifs premium et les justifier avec confiance",
    "Comment parler à un client premium lors du premier rendez-vous",
    "Le brief premium : poser les bonnes questions dès le début",
    # Conception premium
    "Choisir un thème WordPress sobre, rapide et premium",
    "Typographie et couleurs : les bases d'un design crédible",
    "La page d'accueil premium : clarté et confiance en 5 secondes",
    "Les plugins premium : choisir peu, choisir bien, justifier chaque choix",
    "Vitesse et performance : le minimum non négociable en haut de gamme",
    # Expérience utilisateur
    "Navigation fluide : zéro friction, zéro confusion",
    "Mobile-first premium : l'expérience sur téléphone d'abord",
    "Les images et visuels : qualité vs optimisation",
    "Accessibilité de base : inclure sans complexifier",
    # Livraison et relation client
    "La présentation de projet : comment pitcher un site premium",
    "La documentation client premium : simple, claire, utilisable",
    "Former un client premium à utiliser son propre site",
    "Gérer les retours d'un client exigeant sans perdre sa posture",
    "La maintenance premium : une offre récurrente à proposer systématiquement",
    # Réputation et croissance
    "Construire une réputation d'expert WordPress premium",
    "Le portfolio premium : montrer son niveau sans tout montrer",
    "Transformer un client satisfait en client récurrent et en recommandation",
]

_CLIENT_PROFILES = [
    "entrepreneur digital / solopreneur établi",
    "consultant senior / expert de niche",
    "coach / formateur premium (offre > 2 000€)",
    "PME établie (5-50 salariés)",
    "marque personnelle forte",
    "professionnel libéral (médecin, avocat, architecte)",
    "créatif / studio indépendant",
    "startup post-levée de fonds",
]

_BUDGET_RANGES = [
    "1 500 – 3 000€ (premium entrée de gamme)",
    "3 000 – 6 000€ (premium établi)",
    "6 000 – 15 000€ (premium haut de gamme)",
    "15 000€+ (sur-mesure exclusif)",
]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wp-premium-freelance",
        description=(
            "Professeur IA WordPress Premium schoolsWP — "
            "positionner, concevoir et livrer des sites haut de gamme"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  # Leçon simple\n"
            "  python -m agents.wp_premium_freelance.cli \\\n"
            '    --topic "La différence entre un site standard et premium"\n\n'
            "  # Leçon avec profil client et fourchette tarifaire\n"
            "  python -m agents.wp_premium_freelance.cli \\\n"
            '    --topic "La présentation de projet" \\\n'
            '    --client-profile "consultant senior" \\\n'
            '    --budget-range "5000-15000€" \\\n'
            "    --output lecons/presenter-projet-premium.md\n\n"
            "  # Gérer une situation difficile avec un client premium\n"
            "  python -m agents.wp_premium_freelance.cli \\\n"
            '    --topic "Gérer les retours client" \\\n'
            '    --question "Mon client premium trouve le site trop simple et veut ajouter des effets"\n\n'
            "  # Voir tous les sujets premium disponibles\n"
            "  python -m agents.wp_premium_freelance.cli --list-topics"
        ),
    )
    parser.add_argument(
        "--topic",
        metavar="SUJET",
        help="Notion à apprendre (ex: 'Positionner son offre premium', 'Brief client haut de gamme')",
    )
    parser.add_argument(
        "--question",
        metavar="QUESTION",
        default=None,
        help="Question ou situation précise (ex: 'comment répondre quand le client veut tout changer ?')",
    )
    parser.add_argument(
        "--client-profile",
        metavar="PROFIL",
        default=None,
        help="Profil du client premium (ex: 'consultant senior', 'PME établie', 'coach premium')",
    )
    parser.add_argument(
        "--budget-range",
        metavar="TARIF",
        default=None,
        help="Fourchette tarifaire (ex: '3000-6000€', '6000-15000€')",
    )
    parser.add_argument(
        "--level",
        metavar="NIVEAU",
        default="freelance WordPress en montée en gamme",
        help="Niveau déclaré (défaut : 'freelance WordPress en montée en gamme')",
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
        help="Affiche tous les sujets WordPress Premium disponibles",
    )
    return parser


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.list_topics:
        print("\n✦ Sujets WordPress Premium disponibles :\n")
        categories = {
            "Positionnement premium": _SUGGESTED_TOPICS[:5],
            "Conception premium": _SUGGESTED_TOPICS[5:10],
            "Expérience utilisateur": _SUGGESTED_TOPICS[10:14],
            "Livraison & relation client": _SUGGESTED_TOPICS[14:19],
            "Réputation & croissance": _SUGGESTED_TOPICS[19:],
        }
        for category, topics in categories.items():
            print(f"  {category} :")
            for topic in topics:
                print(f"    - {topic}")
            print()
        print("Profils clients premium :")
        for c in _CLIENT_PROFILES:
            print(f"  - {c}")
        print("\nFourchettes tarifaires :")
        for b in _BUDGET_RANGES:
            print(f"  - {b}")
        print(
            "\nUtilise : python -m agents.wp_premium_freelance.cli "
            '--topic "<sujet>" --client-profile "<profil>"\n'
        )
        return

    if not args.topic:
        parser.error(
            "L'argument --topic est requis. "
            "Utilise --list-topics pour voir les sujets disponibles."
        )

    agent = WpPremiumFreelanceAgent(model=args.model)

    print("\n[wp-premium-freelance] Préparation de la leçon...", flush=True)
    print(f"  Sujet   : {args.topic}", flush=True)
    if args.client_profile:
        print(f"  Client  : {args.client_profile}", flush=True)
    if args.budget_range:
        print(f"  Tarif   : {args.budget_range}", flush=True)
    if args.question:
        print(f"  Question: {args.question}", flush=True)
    print("", flush=True)

    lesson = await agent.run(
        topic=args.topic,
        question=args.question,
        client_profile=args.client_profile,
        budget_range=args.budget_range,
        level=args.level,
    )

    if args.output:
        try:
            output_path = safe_write_path(args.output)
        except ValueError as e:
            print(f"[wp-premium-freelance] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(lesson, encoding="utf-8")
        print(f"[wp-premium-freelance] Leçon sauvegardée → {output_path}")
    else:
        print(lesson)


if __name__ == "__main__":
    asyncio.run(main())
