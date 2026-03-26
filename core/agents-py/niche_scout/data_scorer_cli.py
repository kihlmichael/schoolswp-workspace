#!/usr/bin/env python3
"""
CLI — Data Scorer schoolsWP
Scoring SEO basé sur métriques réelles (Ahrefs / DataForSEO / Semrush / Manual)

Usage :
  # Depuis un CSV avec métriques réelles
  python -m agents.niche_scout.data_scorer_cli --file niches/metriques.csv --dr 22

  # Depuis un JSON (export DataForSEO / Ahrefs)
  python -m agents.niche_scout.data_scorer_cli --file niches/export.json --source dataforseo

  # Générer un template CSV vide
  python -m agents.niche_scout.data_scorer_cli --template > niches/template.csv

  # Niches sans données réelles (mode estimation pure)
  python -m agents.niche_scout.data_scorer_cli --niches "Tutor LMS + CRM" "CRM WordPress avancé"

Format CSV attendu :
  niche,volume,kd,serp_results,dr_avg_top10,overlap_pct,cpc,intent,notes
  "Tutor LMS + FluentCRM",450,18,12000,38,35,1.20,décisionnelle,""
  "LMS pour formateurs",600,22,28000,32,30,0.90,commerciale,""
  "LMS débutant WordPress",950,55,145000,48,15,0.40,informationnelle,""

  → Les colonnes optionnelles acceptent : vide, N/A, -, ?
  → volume : nb mensuel moyen | kd : 0–100 | serp_results : entier
  → dr_avg_top10 : DR moyen pages top 10 | overlap_pct : 0–100
  → cpc : EUR | intent : informationnelle|hybride|commerciale|décisionnelle|transactionnelle
"""

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.niche_scout.data_scorer import (
    DataScorerAgent,
    DataScorerInput,
    NicheMetrics,
    parse_csv_metrics,
    parse_json_metrics,
)

_SOURCES = ["ahrefs", "dataforseo", "semrush", "moz", "manual", "mixed"]

_CSV_TEMPLATE = """\
# Template CSV — Data Scorer schoolsWP
# Supprimer les lignes # avant import
# Colonnes optionnelles : laisser vide ou mettre N/A si donnée manquante
#
# intent : informationnelle | hybride | commerciale | décisionnelle | transactionnelle
# kd     : 0 (très facile) → 100 (très difficile)
# cpc    : en EUR (ex: 1.20)
niche,volume,kd,serp_results,dr_avg_top10,overlap_pct,cpc,intent,notes
"Tutor LMS + FluentCRM automatisation",450,18,12000,38,35,1.20,décisionnelle,""
"Comparatif FluentCRM vs ActiveCampaign",320,24,18000,42,40,1.80,décisionnelle,""
"CRM WordPress pour freelances",280,20,9500,33,45,0.90,commerciale,""
"LMS pour formateurs indépendants",600,22,28000,32,30,0.90,commerciale,""
"Automatiser WooCommerce avec n8n",180,16,7200,29,55,1.40,décisionnelle,""
"Meilleur plugin SEO WordPress avancé",950,55,145000,48,15,1.10,hybride,""
"LMS WordPress débutant",1200,62,180000,52,10,0.40,informationnelle,""
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="data-scorer",
        description=(
            "Data Scorer schoolsWP — scoring SEO réel avec métriques Ahrefs / DataForSEO\n"
            "3 scores : SEO /10 + Business /10 → Score Combiné /10\n"
            "Formule SEO : (Vol×3 + KD_ease×3 + SERP_inv×2 + Overlap×2 + Auth×1) / 11 × 10"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n\n"
            "  # Depuis CSV avec données réelles Ahrefs\n"
            "  python -m agents.niche_scout.data_scorer_cli \\\n"
            "    --file niches/ahrefs-export.csv --source ahrefs --dr 22\n\n"
            "  # Depuis CSV avec score custom\n"
            "  python -m agents.niche_scout.data_scorer_cli \\\n"
            "    --file niches/metriques.csv --dr 20 \\\n"
            '    --context "Focus freelances, budget 4 content/articles/mois" \\\n'
            "    --output scores/data-scored.md\n\n"
            "  # Générer le template CSV\n"
            "  python -m agents.niche_scout.data_scorer_cli --template\n\n"
            "  # Mode estimation (sans données, niches inline)\n"
            "  python -m agents.niche_scout.data_scorer_cli \\\n"
            '    --niches "Tutor LMS + CRM" "CRM WordPress avancé" "LMS freelance"\n'
        ),
    )

    # Entrée
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument(
        "--file",
        metavar="FICHIER",
        help="Fichier CSV ou JSON avec métriques réelles (auto-détection par extension).",
    )
    input_group.add_argument(
        "--niches",
        nargs="+",
        metavar="NICHE",
        help="Niches sans données réelles → scoring en mode estimation pure.",
    )
    input_group.add_argument(
        "--template",
        action="store_true",
        help="Affiche le template CSV vide et quitte.",
    )

    # Paramètres
    parser.add_argument(
        "--dr",
        type=float,
        default=20.0,
        metavar="DR",
        help="Domain Rating de schoolswp.com (défaut : 20). Utilisé pour Authority_adv.",
    )
    parser.add_argument(
        "--source",
        default="manual",
        choices=_SOURCES,
        metavar="SOURCE",
        help=f"Source des données : {' | '.join(_SOURCES)} (défaut: manual)",
    )
    parser.add_argument(
        "--context",
        default=None,
        metavar="CONTEXTE",
        help="Contexte additionnel (budget éditorial, cible, contraintes).",
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


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    # Mode template
    if args.template:
        print(_CSV_TEMPLATE)
        return

    # Chargement des données
    niches: list[NicheMetrics] = []

    if args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"[data-scorer] Erreur : fichier introuvable → {file_path}", file=sys.stderr)
            sys.exit(1)

        content = file_path.read_text(encoding="utf-8")

        if file_path.suffix.lower() == ".json":
            niches = parse_json_metrics(content)
            print(f"\n[data-scorer] JSON chargé : {len(niches)} niches depuis {file_path}", flush=True)
        else:
            # CSV par défaut
            niches = parse_csv_metrics(content)
            print(f"\n[data-scorer] CSV chargé : {len(niches)} niches depuis {file_path}", flush=True)

    elif args.niches:
        niches = [NicheMetrics(name=n) for n in args.niches]
        print(f"\n[data-scorer] Mode estimation : {len(niches)} niches (sans données réelles)", flush=True)

    else:
        parser.print_help()
        sys.exit(0)

    if not niches:
        print("[data-scorer] Erreur : aucune niche valide trouvée.", file=sys.stderr)
        sys.exit(1)

    # Résumé des données chargées
    has_data = any(m.volume is not None or m.kd is not None for m in niches)
    print(f"  Niches       : {len(niches)}", flush=True)
    print(f"  DR schoolsWP : {args.dr}", flush=True)
    print(f"  Source       : {args.source}", flush=True)
    print(f"  Données      : {'réelles' if has_data else 'estimation'}", flush=True)
    if args.context:
        print(f"  Contexte     : {args.context}", flush=True)

    # Afficher les premières niches
    for m in niches[:5]:
        vol_str = f"vol={m.volume}" if m.volume is not None else "vol=N/A"
        kd_str = f"kd={m.kd}" if m.kd is not None else "kd=N/A"
        print(f"    • {m.name} ({vol_str}, {kd_str})", flush=True)
    if len(niches) > 5:
        print(f"    ... et {len(niches) - 5} autres", flush=True)
    print("", flush=True)

    # Scoring
    agent = DataScorerAgent(model=args.model)
    scorer_input = DataScorerInput(
        niches=niches,
        dr_schoolswp=args.dr,
        source=args.source,
        context=args.context or "",
    )

    result = await agent.run(scorer_input)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(result, encoding="utf-8")
        print(f"[data-scorer] Scores sauvegardés → {output_path}")
    else:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
