#!/usr/bin/env python3
"""
CLI — schoolsWP Brain Workflows

Trois workflows de production de contenu structurés :

  seo-audit        V1 → Audit sémantique → V2 optimisée
  competitive      Analyse SERP → Angle différenciant schoolsWP
  content-factory  Article SEO → 5 formats (newsletter, LinkedIn, X, FAQ AIO, YouTube)

Usage :
  python -m agents.schoolswp_brain.workflow_cli seo-audit \\
    --keyword "plugin cache WordPress" \\
    --intent comparative \\
    --audience "freelance WordPress intermédiaire" \\
    --save-dir content/articles/cache-wp/

  python -m agents.schoolswp_brain.workflow_cli competitive \\
    --keyword "LMS WordPress" \\
    --topic "Choisir son LMS WordPress en 2026" \\
    --output content/articles/lms-angle.md

  python -m agents.schoolswp_brain.workflow_cli content-factory \\
    --keyword "FluentCRM vs ActiveCampaign" \\
    --topic "FluentCRM vs ActiveCampaign : lequel choisir pour WordPress ?" \\
    --intent comparative \\
    --save-dir content/articles/fluentcrm-vs/
"""

import argparse
import asyncio
import io
import sys
import time
from pathlib import Path

# Force UTF-8 sur Windows (terminal CP1252 par défaut)
if hasattr(sys.stdout, "buffer") and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "buffer") and sys.stderr.encoding.lower() not in ("utf-8", "utf8"):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.schoolswp_brain.workflows import (
    CompetitiveAngleWorkflow,
    ContentFactoryWorkflow,
    SeoAuditWorkflow,
    WorkflowResult,
)

_INTENTS = ["informationnelle", "comparative", "décisionnelle", "transactionnelle"]


# ---------------------------------------------------------------------------
# Step logger
# ---------------------------------------------------------------------------


def _step_log(step: str, content: str) -> None:
    word_count = len(content.split())
    labels = {
        # W1
        "v1": f"Step 1 (V1)            → Article généré       ({word_count} mots)",
        "audit": f"Step 2 (Audit)          → Rapport prêt         ({word_count} mots)",
        "v2": f"Step 3 (V2)             → V2 optimisée         ({word_count} mots)",
        # W2
        "serp": f"Step 1 (SERP)           → Analyse prête        ({word_count} mots)",
        "angle": f"Step 2 (Angle)          → Angle construit      ({word_count} mots)",
        # W3
        "article": f"Step 1 (Article)        → Article généré       ({word_count} mots)",
        "newsletter": f"Step 2 (Newsletter)     → Résumé produit       ({word_count} mots)",
        "linkedin": f"Step 3 (LinkedIn)       → Post produit         ({word_count} mots)",
        "twitter": f"Step 4 (Thread X)       → Thread produit       ({word_count} mots)",
        "faq-aio": f"Step 5 (FAQ AIO/GEO)    → FAQ produite         ({word_count} mots)",
        "youtube": f"Step 6 (YouTube)        → Description produite ({word_count} mots)",
    }
    print(f"  [OK] {labels.get(step, step)}", flush=True)


# ---------------------------------------------------------------------------
# Save helpers
# ---------------------------------------------------------------------------


def _save_files(save_dir: str, files: dict[str, str]) -> None:
    """Sauvegarde les fichiers du workflow dans le dossier indiqué."""
    path = Path(save_dir)
    path.mkdir(parents=True, exist_ok=True)
    saved = []
    for filename, content in files.items():
        if content:
            (path / filename).write_text(content, encoding="utf-8")
            saved.append(filename)
    print(f"\n  Fichiers sauvegardés → {path}/")
    print(f"  {' | '.join(saved)}")


def _save_output(output: str, content: str) -> None:
    """Sauvegarde un fichier unique."""
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"\n  Fichier sauvegardé → {path}")


# ---------------------------------------------------------------------------
# W1 — seo-audit
# ---------------------------------------------------------------------------


async def _run_seo_audit(args: argparse.Namespace) -> None:
    workflow = SeoAuditWorkflow(model=args.model)

    print("\n[w1-seo-audit] Démarrage...", flush=True)
    print(f"  Mot-clé  : {args.keyword}", flush=True)
    print(f"  Intent   : {args.intent}", flush=True)
    print(f"  Audience : {args.audience}", flush=True)
    print("  Étapes   : V1 → Audit sémantique → V2 optimisée\n", flush=True)

    t_start = time.monotonic()

    result: WorkflowResult = await workflow.run(
        keyword=args.keyword,
        intent=args.intent,
        audience=args.audience,
        context=getattr(args, "context", None),
        on_step=_step_log,
    )

    elapsed = time.monotonic() - t_start
    print(f"\n  Terminé en {elapsed:.1f}s", flush=True)

    if args.save_dir:
        _save_files(
            args.save_dir,
            {
                "v1.md": result.v1,
                "audit.md": result.audit,
                "v2.md": result.v2,
            },
        )
    elif args.output:
        _save_output(args.output, result.v2)
    else:
        print("\n" + "=" * 70)
        print(result.v2)


# ---------------------------------------------------------------------------
# W2 — competitive
# ---------------------------------------------------------------------------


async def _run_competitive(args: argparse.Namespace) -> None:
    workflow = CompetitiveAngleWorkflow(model=args.model)

    print("\n[w2-competitive] Démarrage...", flush=True)
    print(f"  Mot-clé : {args.keyword}", flush=True)
    print(f"  Sujet   : {args.topic}", flush=True)
    if getattr(args, "intent", None):
        print(f"  Intent  : {args.intent}", flush=True)
    print("  Étapes  : Analyse SERP → Angle différenciant schoolsWP\n", flush=True)

    t_start = time.monotonic()

    result: WorkflowResult = await workflow.run(
        keyword=args.keyword,
        topic=args.topic,
        intent=getattr(args, "intent", None),
        context=getattr(args, "context", None),
        on_step=_step_log,
    )

    elapsed = time.monotonic() - t_start
    print(f"\n  Terminé en {elapsed:.1f}s", flush=True)

    if args.save_dir:
        _save_files(
            args.save_dir,
            {
                "serp-analysis.md": result.serp_analysis,
                "angle.md": result.differentiating_angle,
            },
        )
    elif args.output:
        _save_output(args.output, result.differentiating_angle)
    else:
        print("\n" + "=" * 70)
        print(result.serp_analysis)
        print("\n" + "=" * 70)
        print(result.differentiating_angle)


# ---------------------------------------------------------------------------
# W3 — content-factory
# ---------------------------------------------------------------------------


async def _run_content_factory(args: argparse.Namespace) -> None:
    workflow = ContentFactoryWorkflow(model=args.model)

    print("\n[w3-content-factory] Démarrage...", flush=True)
    print(f"  Mot-clé : {args.keyword}", flush=True)
    print(f"  Sujet   : {args.topic}", flush=True)
    print(f"  Intent  : {args.intent}", flush=True)
    print("  Étapes  : Article → [Newsletter | LinkedIn | Thread X | FAQ AIO | YouTube]\n", flush=True)

    t_start = time.monotonic()

    result: WorkflowResult = await workflow.run(
        keyword=args.keyword,
        topic=args.topic,
        intent=args.intent,
        context=getattr(args, "context", None),
        on_step=_step_log,
    )

    elapsed = time.monotonic() - t_start
    print(f"\n  Terminé en {elapsed:.1f}s", flush=True)

    if args.save_dir:
        _save_files(
            args.save_dir,
            {
                "article.md": result.article,
                "newsletter.md": result.newsletter,
                "linkedin.md": result.linkedin,
                "twitter.md": result.twitter_thread,
                "faq-aio.md": result.faq_aio,
                "youtube.md": result.youtube_description,
            },
        )
    elif args.output:
        _save_output(args.output, result.article)
    else:
        sections = [
            ("Article SEO", result.article),
            ("Newsletter", result.newsletter),
            ("LinkedIn", result.linkedin),
            ("Thread X", result.twitter_thread),
            ("FAQ AIO/GEO", result.faq_aio),
            ("Description YouTube", result.youtube_description),
        ]
        for label, content in sections:
            print(f"\n{'=' * 70}")
            print(f"# {label}")
            print("=" * 70)
            print(content)


# ---------------------------------------------------------------------------
# Parseur principal
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="schoolswp-workflow",
        description="schoolsWP Brain — Workflows de production structurés",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n\n"
            "  # W1 — Article SEO complet avec audit et V2 optimisée\n"
            "  python -m agents.schoolswp_brain.workflow_cli seo-audit \\\n"
            '    --keyword "plugin cache WordPress" \\\n'
            "    --intent comparative \\\n"
            '    --audience "freelance WordPress intermédiaire" \\\n'
            "    --save-dir content/articles/cache-wp/\n\n"
            "  # W2 — Analyse SERP + angle différenciant\n"
            "  python -m agents.schoolswp_brain.workflow_cli competitive \\\n"
            '    --keyword "LMS WordPress" \\\n'
            '    --topic "Choisir son LMS WordPress en 2026" \\\n'
            "    --output content/articles/lms-angle.md\n\n"
            "  # W3 — Content factory : 1 article → 5 formats\n"
            "  python -m agents.schoolswp_brain.workflow_cli content-factory \\\n"
            '    --keyword "FluentCRM vs ActiveCampaign" \\\n'
            '    --topic "FluentCRM vs ActiveCampaign : lequel choisir ?" \\\n'
            "    --intent comparative \\\n"
            "    --save-dir content/articles/fluentcrm-vs/"
        ),
    )

    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    # ---- W1 — seo-audit ----
    p_audit = subparsers.add_parser(
        "seo-audit",
        help="W1 — Génère un article V1, l'audite, produit la V2 optimisée",
        description="Workflow W1 : Article V1 → Audit sémantique (4 dimensions) → V2 optimisée",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p_audit.add_argument(
        "--keyword",
        required=True,
        metavar="MOT_CLÉ",
        help="Mot-clé SEO principal (ex: 'plugin cache WordPress')",
    )
    p_audit.add_argument(
        "--intent",
        required=True,
        choices=_INTENTS,
        metavar="INTENT",
        help=f"Intention de recherche : {' | '.join(_INTENTS)}",
    )
    p_audit.add_argument(
        "--audience",
        required=True,
        metavar="AUDIENCE",
        help="Profil cible (ex: 'freelance WordPress intermédiaire')",
    )
    p_audit.add_argument(
        "--context",
        default=None,
        metavar="CONTEXTE",
        help="Contexte supplémentaire (plugins ciblés, angle, concurrents…)",
    )
    p_audit.add_argument(
        "--save-dir",
        default=None,
        metavar="DOSSIER",
        help="Dossier où sauvegarder v1.md / audit.md / v2.md",
    )
    p_audit.add_argument(
        "--output",
        default=None,
        metavar="FICHIER",
        help="Fichier de sortie pour v2.md uniquement (si pas --save-dir)",
    )
    p_audit.add_argument(
        "--model",
        default=None,
        metavar="MODEL",
        help="Modèle Claude (défaut : $MODEL_WRITER ou claude-sonnet-4-6)",
    )

    # ---- W2 — competitive ----
    p_comp = subparsers.add_parser(
        "competitive",
        help="W2 — Analyse SERP puis construit l'angle différenciant schoolsWP",
        description="Workflow W2 : Analyse SERP → Positionnement et angle différenciant schoolsWP",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p_comp.add_argument(
        "--keyword",
        required=True,
        metavar="MOT_CLÉ",
        help="Mot-clé SEO à analyser (ex: 'LMS WordPress')",
    )
    p_comp.add_argument(
        "--topic",
        required=True,
        metavar="SUJET",
        help="Sujet de l'article envisagé (ex: 'Choisir son LMS WordPress en 2026')",
    )
    p_comp.add_argument(
        "--intent",
        default=None,
        choices=_INTENTS,
        metavar="INTENT",
        help=f"Intention de recherche optionnelle : {' | '.join(_INTENTS)}",
    )
    p_comp.add_argument(
        "--context",
        default=None,
        metavar="CONTEXTE",
        help="Contexte supplémentaire (audience, budget, concurrents à éviter…)",
    )
    p_comp.add_argument(
        "--save-dir",
        default=None,
        metavar="DOSSIER",
        help="Dossier où sauvegarder serp-analysis.md / angle.md",
    )
    p_comp.add_argument(
        "--output",
        default=None,
        metavar="FICHIER",
        help="Fichier de sortie pour angle.md uniquement (si pas --save-dir)",
    )
    p_comp.add_argument(
        "--model",
        default=None,
        metavar="MODEL",
        help="Modèle Claude (défaut : $MODEL_WRITER ou claude-sonnet-4-6)",
    )

    # ---- W3 — content-factory ----
    p_factory = subparsers.add_parser(
        "content-factory",
        help="W3 — Transforme un article SEO en 5 formats distribués",
        description=(
            "Workflow W3 : Article SEO → Newsletter + LinkedIn + Thread X + FAQ AIO/GEO + YouTube\n"
            "Les 5 formats sont générés en parallèle après l'article principal."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p_factory.add_argument(
        "--keyword",
        required=True,
        metavar="MOT_CLÉ",
        help="Mot-clé SEO principal (ex: 'FluentCRM vs ActiveCampaign')",
    )
    p_factory.add_argument(
        "--topic",
        required=True,
        metavar="SUJET",
        help="Sujet complet de l'article (ex: 'FluentCRM vs ActiveCampaign : lequel choisir ?')",
    )
    p_factory.add_argument(
        "--intent",
        required=True,
        choices=_INTENTS,
        metavar="INTENT",
        help=f"Intention de recherche : {' | '.join(_INTENTS)}",
    )
    p_factory.add_argument(
        "--context",
        default=None,
        metavar="CONTEXTE",
        help="Contexte supplémentaire (audience, plugins, contraintes…)",
    )
    p_factory.add_argument(
        "--save-dir",
        default=None,
        metavar="DOSSIER",
        help=(
            "Dossier où sauvegarder les 6 fichiers : "
            "article.md / newsletter.md / linkedin.md / twitter.md / faq-aio.md / youtube.md"
        ),
    )
    p_factory.add_argument(
        "--output",
        default=None,
        metavar="FICHIER",
        help="Fichier de sortie pour article.md uniquement (si pas --save-dir)",
    )
    p_factory.add_argument(
        "--model",
        default=None,
        metavar="MODEL",
        help="Modèle Claude (défaut : $MODEL_WRITER ou claude-sonnet-4-6)",
    )

    return parser


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    dispatch = {
        "seo-audit": _run_seo_audit,
        "competitive": _run_competitive,
        "content-factory": _run_content_factory,
    }

    handler = dispatch.get(args.subcommand)
    if handler is None:
        parser.print_help()
        sys.exit(1)

    await handler(args)


if __name__ == "__main__":
    asyncio.run(main())
