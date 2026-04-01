#!/usr/bin/env python3
"""
Content Factory CLI — Pipeline complet schoolsWP

Orchestre : Strategy → Article → Audit SEO → LLM SEO → Conversion → Topical → Cluster

Usage (depuis projects/schoolswp/) :
  python -m agents.content_factory.cli --keyword "lms wordpress rentable" --intent décisionnelle --pillar LMS
  python -m agents.content_factory.cli --file content/articles/lms/v3.md --kw "lms wordpress" --intent décisionnelle
"""

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base import safe_read_path, safe_write_path

_INTENTS = ["informationnelle", "commerciale", "décisionnelle", "comparative", "navigationnelle"]
_PILLARS = ["LMS", "CRM", "SEO", "automatisation", "ecommerce", "freelance", "formation"]
_OBJECTIVES = ["email", "affiliation", "formation", "offre"]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="content-factory",
        description="Content Factory — Pipeline complet schoolsWP (Strategy → Article → Audits → Cluster)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--keyword", metavar="KW", help="Mot-clé cible (génère un nouvel article)")
    mode.add_argument("--file", metavar="FILE", help="Fichier article existant (.md) à auditer")

    parser.add_argument(
        "--kw",
        metavar="KW",
        help="Mot-clé cible (requis avec --file)",
    )
    parser.add_argument(
        "--intent",
        choices=_INTENTS,
        required=True,
        metavar="INTENT",
        help=f"Intention de recherche : {' | '.join(_INTENTS)}",
    )
    parser.add_argument(
        "--pillar",
        choices=_PILLARS,
        metavar="PILLAR",
        default=None,
        help=f"Pilier thématique : {' | '.join(_PILLARS)}",
    )
    parser.add_argument(
        "--objective",
        choices=_OBJECTIVES,
        metavar="OBJECTIVE",
        default=None,
        help=f"Objectif business : {' | '.join(_OBJECTIVES)}",
    )
    parser.add_argument("--include-serp", action="store_true", help="Inclure l'analyse SERP")
    parser.add_argument("--include-ner", action="store_true", help="Inclure l'extraction NER")
    parser.add_argument("--no-links", action="store_true", help="Désactiver le maillage interne")
    parser.add_argument("--no-cluster", action="store_true", help="Désactiver la génération de cluster")
    parser.add_argument("--force", action="store_true", help="Forcer la régénération même si les fichiers existent")
    parser.add_argument("--save-dir", metavar="DIR", default=None, help="Dossier de sauvegarde")
    parser.add_argument(
        "--output", metavar="FILE", default=None, help="Fichier de sortie unique pour l'article final (v2)"
    )
    parser.add_argument(
        "--model", default=None, metavar="MODEL", help="Modèle Claude (défaut : $MODEL_WRITER ou claude-sonnet-4-6)"
    )
    return parser


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    # Validation
    if args.file and not args.kw:
        parser.error("--kw est requis avec --file")

    keyword = args.keyword or args.kw

    # Résolution du chemin article source
    source_file: Path | None = None
    if args.file:
        source_file = safe_read_path(args.file)
        if not source_file.exists():
            parser.error(f"Fichier introuvable : {source_file}")

    # Dossier de sortie
    save_dir = Path(args.save_dir) if args.save_dir else Path("content/articles") / keyword.replace(" ", "-")[:40]
    save_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n[content-factory] Pipeline complet — keyword: {keyword!r} | intent: {args.intent}", flush=True)
    if args.pillar:
        print(f"[content-factory] Pilier: {args.pillar}", flush=True)
    if args.objective:
        print(f"[content-factory] Objectif: {args.objective}", flush=True)
    print(f"[content-factory] Sortie: {save_dir}", flush=True)
    print("", flush=True)

    from agents.content_factory.agent import ContentFactoryAgent

    factory = ContentFactoryAgent(model=args.model)
    result = await factory.run(
        keyword=keyword,
        intent=args.intent,
        pillar=args.pillar,
        objective=args.objective,
        source_file=source_file,
        include_serp=args.include_serp,
        include_ner=args.include_ner,
        no_links=args.no_links,
        no_cluster=args.no_cluster,
        force=args.force,
        save_dir=save_dir,
    )

    # Sauvegarde des fichiers
    pipe = result.pipeline
    pub = result.publish
    files = [
        ("strategy.md", result.factory_report),
        ("v1.md", pipe.v1 if pipe else ""),
        ("v2.md", pipe.v2 if pipe else ""),
        ("audit-seo.md", pub.seo_result.report if pub and pub.seo_result else ""),
        ("audit-llm.md", pub.llm_result.report if pub and pub.llm_result else ""),
        ("audit-conversion.md", pub.conversion_result.report if pub and pub.conversion_result else ""),
        ("audit-topical.md", pub.authority_result.report if pub and pub.authority_result else ""),
        ("final.md", result.best_article),
        ("cluster.md", result.cluster_plan),
        ("meta.md", pipe.meta if pipe else ""),
    ]
    for fname, content in files:
        if content:
            out = safe_write_path(str(save_dir / fname))
            out.write_text(content, encoding="utf-8")
            print(f"[content-factory] {fname} → {out}")

    score = result.publish_score
    if score is not None:
        label = (
            "Publication immédiate"
            if score >= 90
            else "Ajustements mineurs"
            if score >= 80
            else "Révision ciblée"
            if score >= 70
            else "Réécriture"
        )
        print(f"\n[content-factory] Publish Score: {score:.1f}/100 — {label}")

    if args.output:
        final = result.final or result.draft
        if final:
            out = safe_write_path(args.output)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(final, encoding="utf-8")
            print(f"[content-factory] Article final → {out}")

    print(f"\n[content-factory] Pipeline terminé. Fichiers dans : {save_dir}")


if __name__ == "__main__":
    asyncio.run(main())
