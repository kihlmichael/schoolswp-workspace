"""thruuu Writer — transforme un brief thruuu (.docx) en article markdown."""

from __future__ import annotations

import re
from pathlib import Path

from agents.base import BaseContentAgent, safe_read_path, safe_write_path


SYSTEM_PROMPT = """\
Tu es un redacteur SEO senior. Tu recois des content briefs au format thruuu et tu produis
des articles complets, prets pour la relecture humaine.

## Regles absolues

1. Preserve la structure et le wording des headings du brief exactement tels quels.
   Ne change jamais un heading. Seule exception : corriger une faute d'orthographe evidente.
2. Les bullets ou sous-items dans une section de l'outline sont des instructions pour toi.
   Ils ne deviennent jamais des headings ou des H3.
3. Respecte les niveaux de heading : H2 -> ##, H3 -> ###, H4 -> ####.
4. Reste dans les ±10% du word count cible.

## Style schoolsWP (si applicable)

- Tutoiement systematique
- Mots interdits : disruptif, game changer, scalable, hack, revolutionnaire, incroyable,
  en un clic, sans effort, il suffit de
- Nom de marque : schoolsWP (jamais SchoolsWP, schoolswp, Schoolswp)

## Workflow

Pour chaque brief, tu dois :
1. Parser tous les elements (Writer Directive, Article Summary, Content Outline, Food For Thought,
   Top Topics, Frequent Questions, Links, SERP Insights, Competitors, Search Intent, Related Search)
2. Detecter la langue (outline > region > anglais par defaut)
3. Construire ta base de connaissances (fetcher URLs references)
4. Rediger section par section en suivant l'outline
5. Placer tous les liens du bloc Links
6. Produire une checklist finale
7. Retourner l'article complet en markdown avec les metadonnees en frontmatter

## Format de sortie

```
---
Meta Title: [title]
Meta Description: [description]
Slug: [slug]
Language: [langue]
Target Word Count: [cible]
Final Word Count: [reel]
---

[Article complet en markdown]

---checklist---
[Tableau de checklist finale]
```
"""


class ThruuuWriterAgent(BaseContentAgent):
    """Agent de redaction d'articles depuis des briefs thruuu."""

    name = "thruuu-writer"
    system_prompt = SYSTEM_PROMPT

    async def run(
        self,
        *,
        brief_content: str,
        guideline: str | None = None,
        language: str | None = None,
        **kwargs,
    ) -> str:
        """Genere un article complet a partir du contenu d'un brief thruuu.

        Args:
            brief_content: Le texte extrait du brief .docx.
            guideline: Contenu du GUIDELINE.md (optionnel).
            language: Forcer la langue de redaction (optionnel).
        """
        user_prompt_parts = []

        if guideline:
            user_prompt_parts.append(
                f"## GUIDELINE.md actif\n\n{guideline}\n\n---\n"
            )

        user_prompt_parts.append(f"## Brief thruuu\n\n{brief_content}")

        if language:
            user_prompt_parts.append(
                f"\n\n## Instruction supplementaire\n\nRedige l'article en {language}."
            )

        user_prompt = "\n".join(user_prompt_parts)

        response = await self._client.messages.create(
            model=self.model,
            max_tokens=16000,
            system=self.system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )
        return response.content[0].text


def extract_docx_text(file_path: Path) -> str:
    """Extrait le texte brut d'un fichier .docx."""
    try:
        from docx import Document  # type: ignore[import-untyped]
    except ImportError:
        raise ImportError(
            "python-docx est requis pour lire les briefs .docx. "
            "Installe-le avec : pip install python-docx"
        )

    doc = Document(str(file_path))
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    return "\n\n".join(paragraphs)


def load_guideline(search_dirs: list[Path] | None = None) -> str | None:
    """Cherche un GUIDELINE.md dans les repertoires indiques."""
    if search_dirs is None:
        search_dirs = [Path.cwd(), Path.cwd() / "content" / "docs"]

    for d in search_dirs:
        candidate = d / "GUIDELINE.md"
        if candidate.exists():
            return candidate.read_text(encoding="utf-8")

    return None


def save_draft(content: str, slug: str, save_dir: Path) -> Path:
    """Sauvegarde l'article dans le repertoire cible."""
    save_dir.mkdir(parents=True, exist_ok=True)

    # Nettoyer le slug pour en faire un nom de fichier valide
    safe_slug = re.sub(r"[^\w\-]", "-", slug.strip("/").split("/")[-1])
    if not safe_slug:
        safe_slug = "draft"

    output_path = save_dir / f"{safe_slug}.md"
    output_path.write_text(content, encoding="utf-8")
    return output_path
