#!/usr/bin/env python3
"""
CLI — schoolsWP Brain (Strategic Edition)

Agent stratégique central de schoolsWP : analyse business + contenu différenciant.
Orchestre 4 modes (seo-writer, plugin-comparator, wp-architect, automation-consultant).

Usage :
  python -m agents.schoolswp_brain.cli --query "Comment choisir son hébergeur WordPress premium"
  python -m agents.schoolswp_brain.cli --query "FluentCRM vs ActiveCampaign" --mode plugin-comparator
  python -m agents.schoolswp_brain.cli --query "Architecture LMS avec Tutor et WooCommerce" \\
    --mode wp-architect --intent décisionnelle --output articles/lms-architecture.md
  python -m agents.schoolswp_brain.cli --query "Automatiser son onboarding client WordPress" \\
    --mode automation-consultant --context "agence WordPress 3 personnes, budget limité"
"""
import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.schoolswp_brain.agent import SchoolswpBrainAgent

_MODES = ["seo-writer", "plugin-comparator", "wp-architect", "automation-consultant"]
_INTENTS = ["informationnelle", "comparative", "décisionnelle", "transactionnelle"]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="schoolswp-brain",
        description=(
            "schoolsWP Brain – Strategic Edition\n"
            "Agent stratégique central : contenu différenciant, orienté autorité et business."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Modes disponibles :\n"
            "  seo-writer          → Article SEO long terme (1800+ mots, meta inclus)\n"
            "  plugin-comparator   → Comparatif objectif 2-4 plugins + verdict profils\n"
            "  wp-architect        → Architecture technique WordPress + stack + roadmap\n"
            "  automation-consultant → Système automatisé + workflows + frictions\n\n"
            "Si --mode est absent, l'agent choisit automatiquement le mode optimal.\n\n"
            "Exemples :\n"
            "  python -m agents.schoolswp_brain.cli \\\n"
            '    --query "Choisir un hébergeur WordPress pour agence"\n\n'
            "  python -m agents.schoolswp_brain.cli \\\n"
            '    --query "FluentCRM vs Brevo vs ActiveCampaign" \\\n'
            "    --mode plugin-comparator --intent comparative\n\n"
            "  python -m agents.schoolswp_brain.cli \\\n"
            '    --query "Mettre en place un tunnel de vente formation WordPress" \\\n'
            "    --mode automation-consultant \\\n"
            '    --context "Tutor LMS + WooCommerce + FluentCRM, budget 0€/mois d\\'outils SaaS" \\\n'
            "    --output articles/tunnel-formation-wordpress.md"
        ),
    )
    parser.add_argument(
        "--query",
        required=True,
        metavar="REQUÊTE",
        help=(
            "Requête principale : sujet, question, thème ou angle à traiter "
            "(ex: 'Architecture LMS avec Tutor LMS et WooCommerce')"
        ),
    )
    parser.add_argument(
        "--mode",
        choices=_MODES,
        metavar="MODE",
        default=None,
        help=(
            f"Mode de production optionnel : {' | '.join(_MODES)}\n"
            "Si absent, l'agent choisit automatiquement selon la requête."
        ),
    )
    parser.add_argument(
        "--intent",
        choices=_INTENTS,
        metavar="INTENT",
        default=None,
        help=(
            f"Intention de recherche : {' | '.join(_INTENTS)}\n"
            "Si absent, l'agent l'infère depuis la requête."
        ),
    )
    parser.add_argument(
        "--context",
        metavar="CONTEXTE",
        default=None,
        help=(
            "Contexte supplémentaire : audience, contraintes, plugins impliqués, "
            "concurrents à éviter, budget, etc. "
            "(ex: 'freelance WordPress 3 ans d\\'expérience, budget hébergement < 30€/mois')"
        ),
    )
    parser.add_argument(
        "--output",
        metavar="FICHIER",
        help="Chemin de sortie (.md). Si absent, affiche dans le terminal.",
    )
    parser.add_argument(
        "--model",
        default=None,
        metavar="MODEL",
        help="Modèle Claude (défaut : $MODEL_WRITER ou claude-sonnet-4-6)",
    )
    return parser


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    agent = SchoolswpBrainAgent(model=args.model)

    mode_display = args.mode if args.mode else "auto (détection intelligente)"
    intent_display = args.intent if args.intent else "auto (inférée depuis la requête)"

    print("\n[schoolswp-brain] Analyse stratégique en cours...", flush=True)
    print(f"  Requête : {args.query}", flush=True)
    print(f"  Mode    : {mode_display}", flush=True)
    print(f"  Intent  : {intent_display}", flush=True)
    if args.context:
        print(f"  Contexte : {args.context}", flush=True)
    print("", flush=True)

    result = await agent.run(
        query=args.query,
        mode=args.mode,
        intent=args.intent,
        context=args.context,
    )

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(result, encoding="utf-8")
        print(f"[schoolswp-brain] Contenu sauvegardé → {output_path}")
    else:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
