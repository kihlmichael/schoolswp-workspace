#!/usr/bin/env python3
"""
CLI — Module Auto-Audit SEO schoolsWP

Score un article sur 100 points (5 × 20) :
  SEO Structure | Intention | Pédagogie | Valeur Business | Branding schoolsWP

Usage :
  # Audit simple
  python -m agents.seo_auditor.cli \\
    --file content/articles/lms-pilier/v3.md \\
    --keyword "formation en ligne rentable wordpress" \\
    --intent décisionnelle

  # Audit + correction automatique si score < 90
  python -m agents.seo_auditor.cli \\
    --file content/articles/lms-pilier/v3.md \\
    --keyword "formation en ligne rentable wordpress" \\
    --fix \\
    --save-dir content/articles/lms-pilier/

  # Texte direct (sans fichier)
  python -m agents.seo_auditor.cli \\
    --text "# Mon article..." \\
    --keyword "lms wordpress" \\
    --fix --threshold 85

Interprétation des scores :
  95–100  ✅  Publication immédiate
  85–94   🟡  Ajustements mineurs
  70–84   🟠  Optimisation nécessaire
  < 70    🔴  Réécriture stratégique
"""
import argparse
import asyncio
import io
import sys
import time
from pathlib import Path

# Force UTF-8 sur Windows
if hasattr(sys.stdout, "buffer") and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "buffer") and sys.stderr.encoding.lower() not in ("utf-8", "utf8"):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base import safe_read_path, safe_write_path
from agents.seo_auditor.agent import AuditResult, SeoAuditorAgent

_INTENTS = ["informationnelle", "comparative", "décisionnelle", "transactionnelle"]

_SCORE_BAR_WIDTH = 20


def _score_bar(score: int, max_score: int = 100) -> str:
    """Barre de progression ASCII pour visualiser le score."""
    filled = round(score / max_score * _SCORE_BAR_WIDTH)
    bar = "█" * filled + "░" * (_SCORE_BAR_WIDTH - filled)
    return f"[{bar}] {score}/{max_score}"


def _bloc_bar(score: int, max_score: int = 20) -> str:
    filled = round(score / max_score * 10)
    bar = "█" * filled + "░" * (10 - filled)
    return f"[{bar}] {score}/{max_score}"


def _print_result(result: AuditResult, elapsed: float) -> None:
    """Affiche le rapport d'audit formaté dans le terminal."""
    emoji = result.diagnostic_emoji
    diag = result.diagnostic

    print("\n" + "━" * 56)
    print("  AUDIT SEO schoolsWP")
    print("━" * 56)
    print(f"  Score global   {_score_bar(result.score_global)}  {emoji}  {diag}")
    print("─" * 56)
    print(f"  SEO Structure  {_bloc_bar(result.seo_structure)}")
    print(f"  Intention      {_bloc_bar(result.intention)}")
    print(f"  Pédagogie      {_bloc_bar(result.pedagogie)}")
    print(f"  Business       {_bloc_bar(result.business)}")
    print(f"  Branding       {_bloc_bar(result.branding)}")
    print("─" * 56)

    if result.points_forts:
        print("  Points forts :")
        for p in result.points_forts:
            print(f"    + {p}")

    if result.points_faibles:
        print("  Points faibles :")
        for p in result.points_faibles:
            print(f"    – {p}")

    if result.axes_amelioration:
        print("  Axes prioritaires :")
        for i, a in enumerate(result.axes_amelioration, 1):
            print(f"    {i}. {a}")

    print("─" * 56)
    status = "Audit + correction" if result.fixed else "Audit seul"
    print(f"  {status} terminé en {elapsed:.1f}s")
    print("━" * 56)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="seo-auditor",
        description=(
            "Module Auto-Audit SEO schoolsWP — score /100 sur 5 dimensions. "
            "Mode --fix : correction automatique des sections faibles."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n\n"
            "  # Audit simple\n"
            "  python -m agents.seo_auditor.cli \\\n"
            '    --file content/articles/lms-pilier/v3.md \\\n'
            '    --keyword "formation en ligne rentable wordpress" \\\n'
            "    --intent décisionnelle\n\n"
            "  # Audit + auto-correction si score < 90\n"
            "  python -m agents.seo_auditor.cli \\\n"
            '    --file content/articles/lms-pilier/v3.md \\\n'
            '    --keyword "formation en ligne rentable wordpress" \\\n'
            "    --fix --save-dir content/articles/lms-pilier/\n\n"
            "  # Seuil personnalisé\n"
            "  python -m agents.seo_auditor.cli \\\n"
            '    --file article.md --keyword "..." \\\n'
            "    --fix --threshold 85 --save-dir output/"
        ),
    )

    # --- Source de contenu (l'un ou l'autre) ---
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument(
        "--file",
        metavar="FICHIER",
        help="Fichier markdown (.md) à auditer",
    )
    source.add_argument(
        "--text",
        metavar="TEXTE",
        help="Contenu markdown passé directement en argument (guillemets requis)",
    )

    # --- Contexte SEO ---
    parser.add_argument(
        "--keyword",
        required=True,
        metavar="MOT_CLÉ",
        help="Mot-clé SEO principal de l'article (ex: 'lms wordpress rentable')",
    )
    parser.add_argument(
        "--intent",
        default=None,
        choices=_INTENTS,
        metavar="INTENT",
        help=f"Intention de recherche : {' | '.join(_INTENTS)} (optionnel)",
    )

    # --- Mode auto-fix ---
    parser.add_argument(
        "--fix",
        action="store_true",
        help=(
            "Active la correction automatique si score < threshold. "
            "Réécrit uniquement les sections faibles pour atteindre ≥ threshold/100."
        ),
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=90,
        metavar="N",
        help="Score minimum pour déclencher l'auto-correction (défaut : 90)",
    )

    # --- Sorties ---
    parser.add_argument(
        "--save-dir",
        default=None,
        metavar="DOSSIER",
        help=(
            "Dossier de sauvegarde. "
            "Produit : audit-seo.md (rapport) + v2-fixed.md (si --fix déclenché)"
        ),
    )
    parser.add_argument(
        "--output",
        default=None,
        metavar="FICHIER",
        help="Fichier unique pour le rapport d'audit (.md)",
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

    # --- Chargement du contenu ---
    if args.file:
        try:
            p = safe_read_path(args.file)
        except (ValueError, FileNotFoundError) as e:
            print(f"[seo-auditor] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        article = p.read_text(encoding="utf-8")
        word_count = len(article.split())
        print(f"\n[seo-auditor] Fichier chargé : {p} ({word_count} mots)", flush=True)
    else:
        article = args.text
        word_count = len(article.split())
        print(f"\n[seo-auditor] Texte reçu ({word_count} mots)", flush=True)

    print(f"  Mot-clé  : {args.keyword}", flush=True)
    if args.intent:
        print(f"  Intent   : {args.intent}", flush=True)
    if args.fix:
        print(f"  Mode     : Audit + Auto-fix (seuil : {args.threshold}/100)", flush=True)
    else:
        print("  Mode     : Audit seul", flush=True)
    print("", flush=True)

    agent = SeoAuditorAgent(model=args.model)
    t_start = time.monotonic()

    # --- Exécution ---
    if args.fix:
        print("  → Audit en cours...", flush=True)
        result: AuditResult = await agent.audit_and_fix(
            article=article,
            keyword=args.keyword,
            intent=args.intent,
            threshold=args.threshold,
        )
        if result.fixed:
            wc_v2 = len(result.v2.split())
            print(
                f"  ✓ Audit {result.score_global}/100 → Correction déclenchée "
                f"(V2 = {wc_v2} mots)",
                flush=True,
            )
        else:
            print(
                f"  ✓ Audit {result.score_global}/100 → Seuil atteint, pas de correction",
                flush=True,
            )
    else:
        print("  → Audit en cours...", flush=True)
        result = await agent.run(
            article=article,
            keyword=args.keyword,
            intent=args.intent,
        )
        print(f"  ✓ Audit terminé : {result.score_global}/100", flush=True)

    elapsed = time.monotonic() - t_start

    # --- Affichage terminal ---
    _print_result(result, elapsed)

    # --- Sauvegarde ---
    if args.save_dir:
        save_path = safe_write_path(args.save_dir)
        save_path.mkdir(parents=True, exist_ok=True)

        report_file = save_path / "audit-seo.md"
        report_file.write_text(result.report, encoding="utf-8")
        saved = ["audit-seo.md"]

        if result.fixed and result.v2:
            fixed_file = save_path / "v2-fixed.md"
            fixed_file.write_text(result.v2, encoding="utf-8")
            saved.append("v2-fixed.md")

        print(f"\n  Fichiers → {save_path}/")
        print(f"  {' | '.join(saved)}")

    elif args.output:
        out = safe_write_path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(result.report, encoding="utf-8")
        print(f"\n  Rapport sauvegardé → {out}")

    else:
        # Affichage du rapport complet si pas de save-dir
        print("\n" + "=" * 60)
        print(result.report)
        if result.fixed and result.v2:
            print("\n" + "=" * 60)
            print("# Article V2 corrigé\n")
            print(result.v2)


if __name__ == "__main__":
    asyncio.run(main())
