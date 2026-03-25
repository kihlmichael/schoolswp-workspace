#!/usr/bin/env python3
"""
brain-lite CLI — Pipeline allégé 5 étapes

Usage:
  python -m agents.article_pipeline.brain_lite_cli --keyword "fluentcrm avis" --intent informationnelle --pilier crm
"""

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.article_pipeline.pipeline import ArticlePipeline
from agents.base import BaseContentAgent, safe_write_path


class BrainLiteAgent(BaseContentAgent):
    """Agent stratégique léger — retourne un dict avec topic, angle, audience, roi_ok.

    Utilisé par ContentFactoryAgent comme étape 1 (stratégie) avant le pipeline article.
    Un seul appel LLM (~15s) pour déterminer l'angle éditorial optimal.
    """

    name = "brain-lite-strategy"
    system_prompt = (
        "Tu es le stratège éditorial schoolsWP. "
        "Analyse le mot-clé et l'intention pour déterminer le meilleur angle de contenu.\n\n"
        "Réponds UNIQUEMENT en JSON valide avec ces clés :\n"
        '{"topic": "Titre H1 proposé", "angle": "Angle différenciant", '
        '"audience": "Profil lecteur cible", "roi_ok": true}\n\n'
        "roi_ok = false si le sujet n'a pas de potentiel business pour schoolsWP."
    )

    async def run(self, *, keyword: str, intent: str, pilier: str = "", **kwargs) -> dict:  # type: ignore[override]
        """Retourne un dict stratégique {topic, angle, audience, roi_ok}."""
        import json as _json

        user_msg = f"Mot-clé : {keyword}\nIntention : {intent}"
        if pilier:
            user_msg += f"\nPilier : {pilier}"

        response = await self._client.messages.create(
            model=self.model,
            max_tokens=500,
            system=self.system_prompt,
            messages=[{"role": "user", "content": user_msg}],
        )
        raw = response.content[0].text

        try:
            return _json.loads(raw)
        except _json.JSONDecodeError:
            return {"topic": keyword.title(), "angle": "", "audience": "", "roi_ok": True}


_INTENTS = ["informationnelle", "commerciale", "décisionnelle", "comparative", "navigationnelle"]
_PILIERS = ["lms", "crm", "seo", "automatisation", "ecommerce", "freelance", "formation"]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="brain-lite",
        description="Brain Lite — Pipeline allégé 5 étapes (Brain → Writer → Audit → LLM → Maillage)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--keyword", required=True, metavar="KW", help="Mot-clé cible principal")
    parser.add_argument(
        "--intent",
        choices=_INTENTS,
        required=True,
        metavar="INTENT",
        help=f"Intention de recherche : {' | '.join(_INTENTS)}",
    )
    parser.add_argument(
        "--pilier",
        choices=_PILIERS,
        metavar="PILIER",
        default=None,
        help=f"Pilier thématique : {' | '.join(_PILIERS)}",
    )
    parser.add_argument(
        "--save-dir", metavar="DIR", default=None, help="Dossier de sauvegarde des fichiers intermédiaires"
    )
    parser.add_argument(
        "--model", default=None, metavar="MODEL", help="Modèle Claude (défaut : $MODEL_WRITER ou claude-sonnet-4-6)"
    )
    return parser


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    print(f"\n[brain-lite] Pipeline 5 étapes — keyword: {args.keyword!r} | intent: {args.intent}", flush=True)
    if args.pilier:
        print(f"[brain-lite] Pilier: {args.pilier}", flush=True)
    print("", flush=True)

    pipeline = ArticlePipeline(model=args.model)
    result = await pipeline.run_lite(
        keyword=args.keyword,
        intent=args.intent,
        pilier=args.pilier,
    )

    save_dir = Path(args.save_dir) if args.save_dir else Path("content/articles") / args.keyword.replace(" ", "-")[:40]
    save_dir.mkdir(parents=True, exist_ok=True)

    for fname, content in [
        ("v1.md", result.draft),
        ("audit.md", result.audit),
        ("v2.md", result.final),
        ("llm-seo.md", result.llm_seo),
        ("maillage.md", result.cluster),
    ]:
        if content:
            out = safe_write_path(str(save_dir / fname))
            out.write_text(content, encoding="utf-8")
            print(f"[brain-lite] Sauvegardé → {out}")

    print(f"\n[brain-lite] Pipeline terminé. Fichiers dans : {save_dir}")


if __name__ == "__main__":
    asyncio.run(main())
