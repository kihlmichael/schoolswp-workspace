"""CLI pour l'agent thruuu-writer.

Usage:
    .venv/Scripts/python -m agents.thruuu_writer.cli --brief briefs/mon-brief.docx
    .venv/Scripts/python -m agents.thruuu_writer.cli --brief briefs/mon-brief.docx --save-dir content/articles/crm/
    .venv/Scripts/python -m agents.thruuu_writer.cli --brief briefs/mon-brief.docx --language francais --model claude-sonnet-4-6
"""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

from agents.base import safe_read_path, safe_write_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="thruuu Writer — transforme un brief .docx en article markdown"
    )
    parser.add_argument(
        "--brief",
        required=True,
        help="Chemin vers le fichier brief .docx",
    )
    parser.add_argument(
        "--guideline",
        default=None,
        help="Chemin vers un GUIDELINE.md (auto-detecte si absent)",
    )
    parser.add_argument(
        "--save-dir",
        default="drafts",
        help="Repertoire de sortie pour le draft (defaut: drafts/)",
    )
    parser.add_argument(
        "--language",
        default=None,
        help="Forcer la langue de redaction (ex: francais, english)",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Modele Claude a utiliser (defaut: MODEL_WRITER ou claude-sonnet-4-6)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Fichier de sortie (alternative a --save-dir, ecrit directement)",
    )
    return parser.parse_args()


async def main() -> None:
    args = parse_args()

    from agents.thruuu_writer.agent import (
        ThruuuWriterAgent,
        extract_docx_text,
        load_guideline,
        save_draft,
    )

    # Lire le brief
    brief_path = safe_read_path(args.brief)
    if not brief_path.suffix.lower() == ".docx":
        print(f"Erreur : le fichier doit etre un .docx, recu : {brief_path.suffix}")
        sys.exit(1)

    print(f"Lecture du brief : {brief_path.name}")
    brief_content = extract_docx_text(brief_path)

    if not brief_content.strip():
        print("Erreur : le brief est vide.")
        sys.exit(1)

    # Charger le guideline
    guideline = None
    if args.guideline:
        guideline_path = safe_read_path(args.guideline)
        guideline = guideline_path.read_text(encoding="utf-8")
        print(f"GUIDELINE.md charge : {guideline_path.name}")
    else:
        guideline = load_guideline()
        if guideline:
            print("GUIDELINE.md auto-detecte et charge.")
        else:
            print("Aucun GUIDELINE.md trouve — redaction sans guideline.")

    # Lancer l'agent
    agent = ThruuuWriterAgent(model=args.model)
    print(f"Redaction en cours avec {agent.model}...")

    result = await agent.run(
        brief_content=brief_content,
        guideline=guideline,
        language=args.language,
    )

    # Sauvegarder
    if args.output:
        output_path = safe_write_path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(result, encoding="utf-8")
        print(f"Draft sauvegarde : {output_path}")
    else:
        # Extraire le slug du frontmatter si possible
        slug = "draft"
        for line in result.split("\n"):
            if line.lower().startswith("slug:"):
                slug = line.split(":", 1)[1].strip()
                break

        save_path = safe_write_path(args.save_dir)
        output_path = save_draft(result, slug, save_path)
        print(f"Draft sauvegarde : {output_path}")

    print(result)


if __name__ == "__main__":
    asyncio.run(main())
