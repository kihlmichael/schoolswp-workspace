#!/usr/bin/env python3
"""
CLI — Professeur IA WordPress Freelance schoolsWP

Usage :
  python -m agents.wp_freelance_teacher.cli --topic "Livraison d'un site client"
  python -m agents.wp_freelance_teacher.cli --topic "..." --client-type "coach" --mission "site vitrine"
  python -m agents.wp_freelance_teacher.cli --topic "..." --question "..." --output lecons/livraison.md
  python -m agents.wp_freelance_teacher.cli --list-topics
"""

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base import safe_write_path
from agents.wp_freelance_teacher.agent import WpFreelanceTeacherAgent

_SUGGESTED_TOPICS = [
    # Avant la mission
    "Faire un brief client efficace avant de commencer",
    "Fixer son tarif et rédiger un devis WordPress clair",
    "Choisir le bon thème pour un client (sans le piège du thème compliqué)",
    "Les plugins indispensables pour un site client pro (et rien de plus)",
    # Pendant la mission
    "Structurer un site vitrine vendable en 1 semaine",
    "La page d'accueil client qui convertit",
    "Optimiser la vitesse d'un site avant la livraison",
    "Configurer le SSL et la sécurité de base pour un client",
    "Créer un formulaire de contact qui fonctionne vraiment",
    "Configurer le SEO de base avec Rank Math ou Yoast",
    # Livraison
    "La checklist de livraison d'un site WordPress client",
    "Former le client à gérer son site (sans qu'il casse tout)",
    "Rédiger une documentation simple pour le client",
    "Tester un site avant livraison (les 10 points critiques)",
    # Après la mission
    "Proposer la maintenance mensuelle à un client",
    "Gérer les retours et modifications après livraison",
    "Facturer sereinement : acompte, solde, réclamations",
    "Fidéliser un client WordPress (récurrence = stabilité)",
    # Gestion de situation
    "Que faire quand un client veut tout changer après livraison ?",
    "Gérer un client qui ne sait pas ce qu'il veut",
    "Expliquer WordPress à un client non technique",
]

_CLIENT_TYPES = [
    "coach / formateur",
    "artisan / commerçant local",
    "consultant indépendant",
    "restaurant / café",
    "photographe / créatif",
    "thérapeute / praticien",
    "avocat / expert-comptable",
    "architecte / designer",
    "association",
    "startup early-stage",
]

_MISSION_TYPES = [
    "site vitrine",
    "site de services / consultant",
    "landing page",
    "site portfolio",
    "site e-commerce simple",
    "blog pro",
    "refonte de site existant",
]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wp-freelance-teacher",
        description=(
            "Professeur IA WordPress Freelance schoolsWP — créer et livrer des sites clients, logique terrain"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  # Leçon simple\n"
            "  python -m agents.wp_freelance_teacher.cli \\\n"
            '    --topic "La checklist de livraison d\'un site WordPress"\n\n'
            "  # Leçon contextualisée client + mission\n"
            "  python -m agents.wp_freelance_teacher.cli \\\n"
            '    --topic "Choisir le bon thème pour un client" \\\n'
            '    --client-type "artisan plombier" \\\n'
            '    --mission "site vitrine" \\\n'
            "    --output lecons/choisir-theme-client.md\n\n"
            "  # Débloquer une situation freelance concrète\n"
            "  python -m agents.wp_freelance_teacher.cli \\\n"
            '    --topic "Gestion des retours client" \\\n'
            '    --question "Mon client veut tout changer 2 semaines après la livraison" \\\n'
            '    --client-type "coach"\n\n'
            "  # Voir tous les sujets disponibles\n"
            "  python -m agents.wp_freelance_teacher.cli --list-topics"
        ),
    )
    parser.add_argument(
        "--topic",
        metavar="SUJET",
        help="Notion à apprendre ou situation à gérer (ex: 'Brief client', 'Livraison site')",
    )
    parser.add_argument(
        "--question",
        metavar="QUESTION",
        default=None,
        help="Question précise ou situation client concrète à résoudre",
    )
    parser.add_argument(
        "--client-type",
        metavar="CLIENT",
        default=None,
        help="Type de client (ex: 'coach', 'artisan plombier', 'consultant RH')",
    )
    parser.add_argument(
        "--mission",
        metavar="MISSION",
        default=None,
        help="Type de mission (ex: 'site vitrine', 'landing page', 'refonte')",
    )
    parser.add_argument(
        "--level",
        metavar="NIVEAU",
        default="débutant en freelance WordPress",
        help="Niveau déclaré (défaut : 'débutant en freelance WordPress')",
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
        help="Affiche tous les sujets freelance disponibles",
    )
    return parser


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.list_topics:
        print("\n🛠 Sujets WordPress Freelance disponibles :\n")
        categories = {
            "Avant la mission": _SUGGESTED_TOPICS[:4],
            "Pendant la mission": _SUGGESTED_TOPICS[4:10],
            "Livraison": _SUGGESTED_TOPICS[10:14],
            "Après la mission": _SUGGESTED_TOPICS[14:18],
            "Gestion de situation": _SUGGESTED_TOPICS[18:],
        }
        for category, topics in categories.items():
            print(f"  {category} :")
            for topic in topics:
                print(f"    - {topic}")
            print()
        print("Types de clients :")
        for c in _CLIENT_TYPES:
            print(f"  - {c}")
        print("\nTypes de missions :")
        for m in _MISSION_TYPES:
            print(f"  - {m}")
        print('\nUtilise : python -m agents.wp_freelance_teacher.cli --topic "<sujet>" --client-type "<client>"\n')
        return

    if not args.topic:
        parser.error("L'argument --topic est requis. Utilise --list-topics pour voir les sujets disponibles.")

    agent = WpFreelanceTeacherAgent(model=args.model)

    print("\n[wp-freelance-teacher] Préparation de la leçon...", flush=True)
    print(f"  Sujet   : {args.topic}", flush=True)
    if args.client_type:
        print(f"  Client  : {args.client_type}", flush=True)
    if args.mission:
        print(f"  Mission : {args.mission}", flush=True)
    print(f"  Niveau  : {args.level}", flush=True)
    if args.question:
        print(f"  Question: {args.question}", flush=True)
    print("", flush=True)

    lesson = await agent.run(
        topic=args.topic,
        question=args.question,
        client_type=args.client_type,
        mission=args.mission,
        level=args.level,
    )

    if args.output:
        try:
            output_path = safe_write_path(args.output)
        except ValueError as e:
            print(f"[wp-freelance-teacher] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(lesson, encoding="utf-8")
        print(f"[wp-freelance-teacher] Leçon sauvegardée → {output_path}")
    else:
        print(lesson)


if __name__ == "__main__":
    asyncio.run(main())
