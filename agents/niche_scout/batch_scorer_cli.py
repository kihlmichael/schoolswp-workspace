#!/usr/bin/env python3
"""
CLI — Batch Niche Scorer schoolsWP
Scoring industriel de 10 à 50 niches en une seule exécution

Usage :
  python -m agents.niche_scout.batch_scorer_cli --niches-file niches/lms-batch.txt
  python -m agents.niche_scout.batch_scorer_cli --niches-file niches/batch.txt --topics "FluentCRM, n8n, LMS" --output scores/batch.md
  python -m agents.niche_scout.batch_scorer_cli --niches "Niche A" "Niche B" ... (jusqu'à 50)

Format fichier .txt (--niches-file) :
  # Commentaires ignorés
  Automatiser Tutor LMS avec FluentCRM
  CRM WordPress pour freelances
  LMS pour formateurs indépendants
  ...
"""
import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.niche_scout.batch_scorer import BatchNicheScorerAgent

_MAX_NICHES = 50
_MIN_NICHES = 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="batch-niche-scorer",
        description=(
            "Batch Niche Scorer schoolsWP — scoring de 10 à 50 niches en une passe\n"
            "Formule 6 variables : Score = (V1+V2+V3+V4+V5+V6) / 3  →  /10"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n\n"
            "  # Mode fichier (recommandé pour les grands batches)\n"
            "  python -m agents.niche_scout.batch_scorer_cli \\\n"
            "    --niches-file niches/batch.txt \\\n"
            '    --topics "FluentCRM, Tutor LMS, n8n, SEO sémantique" \\\n'
            "    --output scores/batch-resultat.md\n\n"
            "  # Mode inline (pratique pour tester)\n"
            "  python -m agents.niche_scout.batch_scorer_cli \\\n"
            '    --niches "Tutor LMS + CRM" "LMS freelance rentable" "CRM WordPress avancé" \\\n'
            '    --context "DA schoolsWP ~25, focus freelances"\n\n'
            "  # Avec contexte complet\n"
            "  python -m agents.niche_scout.batch_scorer_cli \\\n"
            "    --niches-file niches/crm-wordpress.txt \\\n"
            '    --topics "FluentCRM, automatisation, tunnels de vente" \\\n'
            '    --context "Budget : 4 articles/mois. Priorité : leads freelances." \\\n'
            "    --output scores/crm-batch.md\n\n"
            "Format fichier .txt :\n"
            "  # Une niche par ligne, # pour commenter\n"
            "  Automatiser Tutor LMS avec FluentCRM\n"
            "  CRM WordPress pour freelances\n"
            "  LMS pour formateurs indépendants\n"
        ),
    )

    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "--niches",
        nargs="+",
        metavar="NICHE",
        help=f"Niches à scorer (entre guillemets, max {_MAX_NICHES}). Ex: \"Tutor LMS + CRM\"",
    )
    input_group.add_argument(
        "--niches-file",
        metavar="FICHIER",
        help="Fichier .txt : une niche par ligne, les lignes # sont ignorées.",
    )

    parser.add_argument(
        "--topics",
        default=None,
        metavar="THÈMES",
        help=(
            "Thèmes existants de schoolsWP pour calculer V3 (Overlap) et V6 (Alignement). "
            "Format : virgule-séparé. "
            "Ex: 'FluentCRM, Tutor LMS, n8n, SEO sémantique, IA WordPress'"
        ),
    )
    parser.add_argument(
        "--context",
        default=None,
        metavar="CONTEXTE",
        help=(
            "Contexte additionnel : DA, budget éditorial, cible, contenu existant. "
            "Ex: 'DA ~25, budget 4 articles/mois, focus freelances WordPress'"
        ),
    )
    parser.add_argument(
        "--output",
        metavar="FICHIER",
        help="Chemin de sortie .md. Si absent, affiche dans le terminal.",
    )
    parser.add_argument(
        "--model",
        default=None,
        metavar="MODEL",
        help="Modèle Claude (défaut : $MODEL_WRITER ou claude-sonnet-4-6)",
    )
    return parser


def load_niches_from_file(path: Path) -> list[str]:
    """Charge les niches depuis un fichier texte (1 par ligne, # = commentaire)."""
    if not path.exists():
        print(f"[batch-scorer] Erreur : fichier introuvable → {path}", file=sys.stderr)
        sys.exit(1)
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    # Chargement des niches
    if args.niches_file:
        niches = load_niches_from_file(Path(args.niches_file))
    else:
        niches = args.niches

    # Validation de la taille du batch
    if len(niches) < _MIN_NICHES:
        print(
            f"[batch-scorer] Erreur : minimum {_MIN_NICHES} niches requises "
            f"(reçu : {len(niches)}).",
            file=sys.stderr,
        )
        sys.exit(1)

    if len(niches) > _MAX_NICHES:
        print(
            f"[batch-scorer] Attention : {len(niches)} niches détectées "
            f"(max recommandé : {_MAX_NICHES}). "
            "Le score pourrait être tronqué. Envisager de diviser en plusieurs batches.",
            file=sys.stderr,
        )

    agent = BatchNicheScorerAgent(model=args.model)

    print(f"\n[batch-scorer] Scoring batch en cours ({len(niches)} niches)...", flush=True)
    if len(niches) <= 15:
        for n in niches:
            print(f"  • {n}", flush=True)
    else:
        for n in niches[:5]:
            print(f"  • {n}", flush=True)
        print(f"  ... et {len(niches) - 5} autres", flush=True)

    if args.topics:
        print(f"\n  Thèmes schoolsWP : {args.topics}", flush=True)
    if args.context:
        print(f"  Contexte         : {args.context}", flush=True)
    print("", flush=True)

    result = await agent.run(
        niches=niches,
        schoolswp_topics=args.topics,
        context=args.context,
    )

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(result, encoding="utf-8")
        print(f"[batch-scorer] Résultats sauvegardés → {output_path}")
    else:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
