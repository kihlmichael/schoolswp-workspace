"""ArticlePipeline — orchestrateur multi-agents pour la production d'articles SEO."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from typing import Optional

from agents.base import BaseContentAgent


@dataclass
class PipelineResult:
    """Résultat complet du pipeline de production."""

    keyword: str
    intent: str
    draft: str = ""
    audit: str = ""
    final: str = ""
    llm_seo: str = ""
    cluster: str = ""
    meta: str = ""
    seo_score: Optional[int] = None
    llm_score: Optional[int] = None
    conversion_score: Optional[int] = None
    authority_score: Optional[int] = None
    publish_score: Optional[float] = None
    errors: list[str] = field(default_factory=list)
    # Version aliases used by ContentFactoryResult
    v1: str = ""
    v2: str = ""
    v3: str = ""
    v4: str = ""
    score_global: Optional[int] = None
    score_llm_global: Optional[int] = None

    def compute_publish_score(self) -> Optional[float]:
        """Calcule le Publish Score pondéré si tous les scores sont disponibles."""
        scores = [self.seo_score, self.llm_score, self.conversion_score, self.authority_score]
        if any(s is None for s in scores):
            return None
        return (
            self.seo_score * 0.30 + self.llm_score * 0.25 + self.conversion_score * 0.25 + self.authority_score * 0.20
        )


def _inject_score_parsers() -> None:
    """Injecte les méthodes de parsing de scores dans PipelineResult."""
    import re

    def _parse_score(text: str, label: str) -> Optional[int]:
        pattern = rf"{label}[^\d]*(\d{{1,3}})"
        m = re.search(pattern, text, re.IGNORECASE)
        return int(m.group(1)) if m else None

    def parse_seo_score(self: PipelineResult) -> Optional[int]:
        return _parse_score(self.audit, "SEO")

    def parse_llm_score(self: PipelineResult) -> Optional[int]:
        return _parse_score(self.llm_seo, "LLM")

    PipelineResult.parse_seo_score = parse_seo_score  # type: ignore[attr-defined]
    PipelineResult.parse_llm_score = parse_llm_score  # type: ignore[attr-defined]


_inject_score_parsers()


class ArticlePipeline(BaseContentAgent):
    """Orchestre le pipeline de production d'articles SEO."""

    name = "article-pipeline"
    system_prompt = "Tu es un orchestrateur de pipeline SEO schoolsWP."

    async def run(  # type: ignore[override]
        self,
        *,
        topic: str,
        keyword: str,
        intent: str,
        angle: str = "",
        pillar: str = "",
        **kwargs,
    ) -> PipelineResult:
        """Pipeline complet : Writer → Auditor → Editor → LLM → Meta."""
        result = PipelineResult(keyword=keyword, intent=intent)

        # Étape 1 — Rédaction
        from agents.seo_writer.agent import SeoWriterAgent

        writer = SeoWriterAgent(model=self.model)
        result.draft = await writer.run(topic=topic, keyword=keyword, intent=intent, angle=angle)
        result.v1 = result.draft

        # Étape 2 — Audit SEO (parallèle avec LLM SEO)
        from agents.llm_seo.agent import LlmSeoAgent
        from agents.seo_auditor.agent import SeoAuditorAgent

        auditor = SeoAuditorAgent(model=self.model)
        llm_agent = LlmSeoAgent(model=self.model)

        result.audit, result.llm_seo = await asyncio.gather(
            auditor.run(article=result.draft, keyword=keyword),
            llm_agent.run(article=result.draft, keyword=keyword),
        )

        # Étape 3 — Édition
        try:
            from agents.seo_auditor.agent import SeoEditorAgent  # type: ignore[attr-defined]

            editor = SeoEditorAgent(model=self.model)
            result.final = await editor.run(
                draft=result.draft,
                audit=result.audit,
                keyword=keyword,
            )
        except (ImportError, AttributeError):
            result.final = result.draft
            result.errors.append("SeoEditorAgent non disponible — draft utilisé comme final")
        result.v2 = result.final

        # Étape 4 — Cluster sémantique
        from agents.cluster_architect.agent import ClusterArchitectAgent

        cluster = ClusterArchitectAgent(model=self.model)
        result.cluster = await cluster.run(thematique=keyword, objectif=pillar or keyword)

        result.publish_score = result.compute_publish_score()
        return result

    async def run_lite(
        self,
        *,
        keyword: str,
        intent: str,
        pilier: str = "",
        **kwargs,
    ) -> PipelineResult:
        """Pipeline allégé 5 étapes (brain-lite)."""
        result = PipelineResult(keyword=keyword, intent=intent)

        from agents.schoolswp_brain.agent import SchoolswpBrainAgent

        brain = SchoolswpBrainAgent(model=self.model)
        strategy = await brain.run(query=keyword, intent=intent)

        from agents.seo_writer.agent import SeoWriterAgent

        writer = SeoWriterAgent(model=self.model)
        result.draft = await writer.run(topic=keyword, keyword=keyword, intent=intent, angle=strategy[:500])
        result.v1 = result.draft

        from agents.llm_seo.agent import LlmSeoAgent
        from agents.seo_auditor.agent import SeoAuditorAgent

        auditor = SeoAuditorAgent(model=self.model)
        llm_agent = LlmSeoAgent(model=self.model)

        result.audit, result.llm_seo = await asyncio.gather(
            auditor.run(article=result.draft, keyword=keyword),
            llm_agent.run(article=result.draft, keyword=keyword),
        )

        result.final = result.draft  # pas d'édition en mode lite
        result.v2 = result.final

        from agents.cluster_architect.agent import ClusterArchitectAgent

        cluster = ClusterArchitectAgent(model=self.model)
        result.cluster = await cluster.run(thematique=keyword, objectif=pilier or keyword)

        return result
