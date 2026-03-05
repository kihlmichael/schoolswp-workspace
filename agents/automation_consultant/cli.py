#!/usr/bin/env python3
"""
CLI — Consultant automatisation WordPress schoolsWP

Usage :
  python -m agents.automation_consultant.cli --objective "Tunnel de vente formation en ligne"
  python -m agents.automation_consultant.cli --objective "..." --tools "FluentCRM" "WooCommerce"
  python -m agents.automation_consultant.cli --objective "..." --constraints "budget < 50€/mois, pas de Make"
"""
import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.automation_consultant.agent import AutomationConsultantAgent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="automation-consultant",
        description="Consultant automatisation WordPress schoolsWP — architecture de systèmes, tunnels, CRM",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  python -m agents.automation_consultant.cli \\\n"
            '    --objective "Tunnel de vente pour formation WordPress"\n\n'
            "  python -m agents.automation_consultant.cli \\\n"
            '    --objective "CRM automatisé onboarding client freelance" \\\n'
            '    --tools "FluentCRM" "Fluent Forms" "n8n" \\\n'
            '    --constraints "budget SaaS < 30€/mois, hébergeur mutualisé" \\\n'
            "    --output articles/crm-onboarding-freelance.md\n\n"
            "  python -m agents.automation_consultant.cli \\\n"
            '    --objective "Système de réengagement abonnés inactifs" \\\n'
            '    --tools "FluentCRM" "WooCommerce"'
        ),
    )
    parser.add_argument(
        "--objective",
        required=True,
        metavar="OBJECTIF",
        help=(
            "Ce qu'on veut automatiser "
            "(ex: 'tunnel de vente formation en ligne', 'CRM automatisé avec FluentCRM')"
        ),
    )
    parser.add_argument(
        "--tools",
        nargs="+",
        metavar="OUTIL",
        default=None,
        help="Stack imposée ou souhaitée (ex: 'FluentCRM' 'WooCommerce' 'n8n')",
    )
    parser.add_argument(
        "--constraints",
        metavar="CONTRAINTES",
        default=None,
        help=(
            "Contraintes techniques ou budget "
            "(ex: 'budget < 50€/mois, hébergeur mutualisé, pas de Make')"
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

    agent = AutomationConsultantAgent(model=args.model)

    print(f"\n[automation-consultant] Architecture en cours...", flush=True)
    print(f"  Objectif    : {args.objective}", flush=True)
    if args.tools:
        print(f"  Stack       : {', '.join(args.tools)}", flush=True)
    if args.constraints:
        print(f"  Contraintes : {args.constraints}", flush=True)
    print("", flush=True)

    plan = await agent.run(
        objective=args.objective,
        tools=args.tools,
        constraints=args.constraints,
    )

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(plan, encoding="utf-8")
        print(f"[automation-consultant] Plan sauvegardé → {output_path}")
    else:
        print(plan)


if __name__ == "__main__":
    asyncio.run(main())
