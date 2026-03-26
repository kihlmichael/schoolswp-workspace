"""
schoolsWP Brain — Content Factory Agent

Agent orchestrateur complet : stratégie → génération → audit 4 modules → cluster.

Passe de "Je rédige un article" à "Je déploie un actif stratégique" :
  ✓ Angle stratégique (ROI check + différenciation schoolsWP)
  ✓ Article multi-étapes (Writer → Auditor → Editor → LLM-SEO → Links → Meta)
  ✓ Audit complet 4 modules en parallèle (SEO + IA + Conversion + Autorité)
  ✓ Plan cluster sémantique (pilier + satellites + maillage)
  ✓ Dashboard Publish Score /100 + plan d'action priorisé

Deux modes :

Mode génération (depuis mot-clé) :
    result = await agent.generate_and_audit(
        keyword="lms wordpress rentable",
        intent="décisionnelle",
        pillar="LMS",
    )
    print(result.publish_score)   # 84
    print(result.best_article)    # article complet

Mode audit seul (article existant) :
    result = await agent.audit_only(
        article=open("v3.md").read(),
        keyword="lms wordpress",
        pillar="LMS",
    )
    print(result.publish_score)
    print(result.cluster_plan)

Pipeline d'appels LLM :
    Mode génération :
        1. BrainLiteAgent         → stratégie (1 appel)
        2. ArticlePipeline        → V1 → V2 → V3 [→ V4] → links → meta (4-7 appels)
        3. PublishReadyAgent      → 4 audits ‖ + synthèse (5 appels)
        4. expand_cluster()       → plan cluster (1 appel)
        TOTAL : ~11-14 appels LLM | ~4-8 min

    Mode audit seul :
        1. PublishReadyAgent      → 4 audits ‖ + synthèse (5 appels)
        2. expand_cluster()       → plan cluster (1 appel)
        TOTAL : 6 appels LLM | ~90-120s
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

from agents.article_pipeline.brain_lite_cli import BrainLiteAgent
from agents.article_pipeline.pipeline import ArticlePipeline, PipelineResult
from agents.base import BaseContentAgent
from agents.publish_ready.agent import PublishReadyAgent, PublishReadyResult
from agents.topical_authority.agent import TopicalAuthorityAgent

# ---------------------------------------------------------------------------
# ContentFactoryResult — dataclass de résultat agrégé
# ---------------------------------------------------------------------------


@dataclass
class ContentFactoryResult:
    """
    Résultat complet du schoolsWP Brain / Content Factory.

    Champs principaux :
        topic           : Titre H1 généré par Brain
        angle           : Angle différenciant schoolsWP
        audience        : Profil lecteur cible
        keyword         : Mot-clé principal
        intent          : Intention de recherche
        pillar          : Pilier thématique schoolsWP
        roi_ok          : ROI check (True si sujet stratégique)

        pipeline        : PipelineResult complet (v1/v2/v3/v4/links/meta/scores)
                          None en mode audit-only

        article         : Meilleure version de l'article (V4 > V3 > V2 > V1)
        publish         : PublishReadyResult (4 scores + action_plan + dashboard)
        cluster_plan    : Plan cluster markdown (pilier + satellites + maillage)
        factory_report  : Rapport maître markdown (résumé de tout)
    """

    # Stratégie
    topic: str = ""
    angle: str = ""
    audience: str = ""
    keyword: str = ""
    intent: str = ""
    pillar: str = ""
    roi_ok: bool = True

    # Génération
    pipeline: PipelineResult | None = None
    strategy_raw: dict = field(default_factory=dict)

    # Article final
    article: str = ""

    # Audit
    publish: PublishReadyResult | None = None

    # Cluster
    cluster_plan: str = ""

    # Rapport maître
    factory_report: str = ""

    @property
    def publish_score(self) -> int:
        return self.publish.publish_score if self.publish else 0

    @property
    def publish_emoji(self) -> str:
        return self.publish.publish_emoji if self.publish else "—"

    @property
    def publish_diagnostic(self) -> str:
        return self.publish.publish_diagnostic if self.publish else "—"

    @property
    def best_article(self) -> str:
        """Retourne la meilleure version de l'article disponible."""
        if self.article:
            return self.article
        if self.pipeline:
            return self.pipeline.v4 or self.pipeline.v3 or self.pipeline.v2 or self.pipeline.v1 or ""
        return ""

    @property
    def article_version_label(self) -> str:
        if not self.pipeline:
            return "Fourni"
        if self.pipeline.v4:
            return "V4 (NER enrichi)"
        if self.pipeline.v3:
            return "V3 (LLM-optimisé)"
        if self.pipeline.v2:
            return "V2 (édité)"
        return "V1 (brut)"

    @property
    def word_count(self) -> int:
        art = self.best_article
        return len(art.split()) if art else 0


def _build_factory_report(result: ContentFactoryResult) -> str:
    """Construit le rapport maître markdown du Content Factory."""
    lines = [
        "# schoolsWP Brain — Rapport Factory",
        f"**Mot-clé** : {result.keyword}",
        f"**Intent** : {result.intent}",
        "",
    ]

    if result.topic:
        lines += [
            "## Stratégie éditoriale",
            f"- **Sujet** : {result.topic}",
            f"- **Angle** : {result.angle}",
            f"- **Audience** : {result.audience}",
            f"- **ROI** : {'✓ Stratégique' if result.roi_ok else '⚠ Faible'}",
            "",
        ]

    if result.pipeline:
        p = result.pipeline
        lines += [
            "## Pipeline de génération",
            f"- Version article : {result.article_version_label}",
            f"- Mots : {result.word_count}",
        ]
        if p.score_global:
            lines.append(f"- Score audit pipeline : {p.score_global}/10")
        if p.score_llm_global:
            lines.append(f"- Score LLM-SEO pipeline : {p.score_llm_global}/10")
        lines.append("")

    if result.publish:
        pub = result.publish
        scores = pub.scores_summary()
        lines += [
            "## Publish Score",
            f"**{pub.publish_score}/100** {pub.publish_emoji} — {pub.publish_diagnostic}",
            "",
            "| Module | Score | Poids |",
            "|--------|-------|-------|",
            f"| SEO Structure | {scores.get('SEO Structure', 0)}/100 | 30% |",
            f"| Citabilité IA | {scores.get('Citabilité IA', 0)}/100 | 25% |",
            f"| Conversion & CTA | {scores.get('Conversion', 0)}/100 | 25% |",
            f"| Autorité Thématique | {scores.get('Autorité thème', 0)}/100 | 20% |",
            "",
            f"**Bloc le plus faible** : {pub.weakest_module}",
            "",
        ]
        if pub.action_plan:
            lines += ["## Plan d'action priorisé", pub.action_plan, ""]

    if result.cluster_plan:
        lines += ["---", "", result.cluster_plan]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# ContentFactoryAgent — orchestrateur principal
# ---------------------------------------------------------------------------


class ContentFactoryAgent(BaseContentAgent):
    """
    schoolsWP Brain — Content Factory Agent.

    Orchestrateur complet : stratégie → génération → audit 4 modules → cluster.

    Ne définit pas de system_prompt propre — délègue à des agents spécialisés.
    Hérite de BaseContentAgent uniquement pour la gestion du modèle et du client.
    """

    name = "content-factory"
    system_prompt = ""  # Orchestrateur — pas de system_prompt direct

    async def generate_and_audit(
        self,
        keyword: str,
        intent: str,
        pillar: str | None = None,
        objective: str | None = None,
        include_serp: bool = False,
        include_ner: bool = False,
        include_links: bool = True,
        expand_cluster: bool = True,
        force: bool = False,
        on_step: Callable | None = None,
    ) -> ContentFactoryResult:
        """
        Pipeline complet : stratégie → génération → audit 4 modules → cluster.

        Args:
            keyword        : Mot-clé SEO principal
            intent         : Intention (informationnelle|comparative|décisionnelle)
            pillar         : Pilier thématique (SEO|LMS|CRM|Performance|Automatisation)
            objective      : Objectif business (email|affiliation|formation|offre)
            include_serp   : Simulation SERP Top 5 (ralentit le pipeline de ~2 min)
            include_ner    : Enrichissement NER sémantique (V4) (+1-2 min)
            include_links  : Maillage interne (recommandé, ~30s)
            expand_cluster : Plan cluster (pilier + satellites + maillage)
            force          : Forcer si ROI faible
            on_step        : Callback optionnel sur chaque étape pipeline

        Returns:
            ContentFactoryResult avec article, audits, cluster plan et rapport.
        """
        result = ContentFactoryResult(keyword=keyword, intent=intent, pillar=pillar or "")

        # ── Étape 1 : Stratégie (BrainLiteAgent) ──────────────────────
        if on_step:
            on_step("Brain", "")
        brain = BrainLiteAgent(model=self.model)
        strategy = await brain.run(keyword=keyword, intent=intent, pilier=pillar or "")

        result.topic = strategy.get("topic") or keyword.title()
        result.angle = strategy.get("angle") or "Vision système schoolsWP — concret, actionnable"
        result.audience = strategy.get("audience") or "freelance WordPress intermédiaire"
        result.roi_ok = bool(strategy.get("roi_ok", True))
        result.strategy_raw = strategy

        if not result.roi_ok and not force:
            # ROI faible → arrêt préventif (le CLI gère l'avertissement)
            return result

        # ── Étape 2 : Génération (ArticlePipeline) ────────────────────
        pipeline = ArticlePipeline(model=self.model)
        pipe_result = await pipeline.run(
            topic=result.topic,
            keyword=keyword,
            intent=intent,
            angle=result.angle,
            include_serp=include_serp,
            include_ner=include_ner,
            include_llm=True,
            include_links=include_links,
            include_meta=True,
            on_step=on_step,
        )
        result.pipeline = pipe_result
        result.article = pipe_result.v4 or pipe_result.v3 or pipe_result.v2 or pipe_result.v1 or ""

        # ── Étape 3 : Audit 4 modules en parallèle ────────────────────
        if on_step:
            on_step("Audit", "")
        result = await self._run_audit_and_cluster(
            result=result,
            article=result.article,
            keyword=keyword,
            intent=intent,
            pillar=pillar,
            objective=objective,
            expand_cluster=expand_cluster,
            on_step=on_step,
        )

        return result

    async def audit_only(
        self,
        article: str,
        keyword: str,
        intent: str | None = None,
        pillar: str | None = None,
        objective: str | None = None,
        expand_cluster: bool = True,
        on_step: Callable | None = None,
    ) -> ContentFactoryResult:
        """
        Audit complet d'un article existant (sans génération).

        4 modules en parallèle + cluster plan. Pas de BrainLiteAgent ni ArticlePipeline.

        Args:
            article        : Article markdown à auditer
            keyword        : Mot-clé SEO principal
            intent         : Intention de recherche (optionnel)
            pillar         : Pilier thématique (optionnel)
            objective      : Objectif business (optionnel)
            expand_cluster : Plan cluster sémantique
            on_step        : Callback optionnel

        Returns:
            ContentFactoryResult avec publish_score, action_plan, cluster_plan.
        """
        result = ContentFactoryResult(
            keyword=keyword,
            intent=intent or "",
            pillar=pillar or "",
            article=article,
        )

        if on_step:
            on_step("Audit", "")

        result = await self._run_audit_and_cluster(
            result=result,
            article=article,
            keyword=keyword,
            intent=intent,
            pillar=pillar,
            objective=objective,
            expand_cluster=expand_cluster,
            on_step=on_step,
        )

        return result

    async def _run_audit_and_cluster(
        self,
        result: ContentFactoryResult,
        article: str,
        keyword: str,
        intent: str | None,
        pillar: str | None,
        objective: str | None,
        expand_cluster: bool,
        on_step: Callable | None,
    ) -> ContentFactoryResult:
        """Audit 4 modules + cluster — partagé entre generate_and_audit et audit_only."""

        publish_agent = PublishReadyAgent(model=self.model)
        publish_result = await publish_agent.run(
            article=article,
            keyword=keyword,
            intent=intent,
            pillar=pillar,
            objective=objective,
        )
        result.publish = publish_result

        # Cluster : réutilise le rapport d'autorité déjà calculé (évite un LLM call)
        if expand_cluster and publish_result.authority_result.report:
            if on_step:
                on_step("Cluster", "")
            auth_agent = TopicalAuthorityAgent(model=self.model)
            result.cluster_plan = await auth_agent.expand_cluster(
                article=article,
                existing_result=publish_result.authority_result,
                keyword=keyword,
                pillar=pillar,
            )

        result.factory_report = _build_factory_report(result)
        return result
