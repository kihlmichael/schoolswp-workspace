"""
Orchestrateur du pipeline article schoolsWP.

Flux standard :
  Agent 1   (Writer)         > V1
  Agent 2   (Auditor)        > Rapport d'audit (8 critères + diagnostic + Indice IA)
  Agent 3   (Editor)         > V2 conditionnelle selon diagnostic
  Agent 4   (LLM-SEO)        > V3 optimisée citations IA (ChatGPT / Gemini / Perplexity)
  Agent 4b  (NER-Analyzer)   > Graphe NER JSON (entités + relations + lacunes)
  Agent 4c  (Sem-Enricher)   > V4 sémantiquement enrichie + score autorité thématique
  Agent 4d  (Link-Strat)     > Plan maillage interne (5-12 liens, ancres, piliers, scoring)
  Agent 5   (Meta)           > Méta SEO + FAQ schema (optionnel)

Flux étendu (include_serp=True) :
  Agent 1   (Writer)         > V1
  Agent 2   (Auditor)        > Rapport d'audit
  Agent 2b  (SERP Sim)       > Simulation SERP Top 5 probable
  Agent 2c  (SERP Comp)      > Comparaison V1 vs SERP + verdict
  Agent 3   (Editor)         > V2 avec audit + SERP comparison
  Agent 4   (LLM-SEO)        > V3 LLM-ready
  Agent 4b  (NER-Analyzer)   > Graphe NER JSON
  Agent 4c  (Sem-Enricher)   > V4 sémantiquement enrichie
  Agent 4d  (Link-Strat)     > Plan maillage interne
  Agent 5   (Meta)           > Méta SEO (optionnel)
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field

from agents.article_pipeline.auditor import PipelineAuditorAgent
from agents.article_pipeline.editor import PipelineEditorAgent
from agents.article_pipeline.llm_optimizer import LlmOptimizerAgent
from agents.article_pipeline.meta_extractor import PipelineMetaExtractorAgent
from agents.article_pipeline.internal_link_strategist import InternalLinkStrategistAgent
from agents.article_pipeline.ner_analyzer import NerAnalyzerAgent
from agents.article_pipeline.semantic_enricher import SemanticEnricherAgent
from agents.article_pipeline.serp_comparator import SerpComparatorAgent
from agents.article_pipeline.serp_simulator import SerpSimulatorAgent
from agents.article_pipeline.writer import PipelineWriterAgent


@dataclass
class PipelineResult:
    """Résultat complet du pipeline article."""

    topic: str
    keyword: str
    intent: str
    angle: str

    v1: str = ""
    audit: str = ""
    v2: str = ""
    meta: str = ""

    # Scores 8 critères extraits du rapport d'audit
    score_alignement: str = ""
    score_profondeur: str = ""
    score_clarte: str = ""
    score_structure: str = ""
    score_densite: str = ""
    score_decisionnelle: str = ""
    score_seo_lt: str = ""
    score_differenciation: str = ""
    score_global: str = ""

    # Diagnostic automatique (RÉÉCRITURE MAJEURE / AMÉLIORATION STRATÉGIQUE / VALIDÉ)
    diagnostic: str = ""

    # Indice Citation IA
    score_citation_chatgpt: str = ""
    score_citation_snippet: str = ""
    score_citation_ai_overview: str = ""

    # Compatibilité ascendante avec l'ancien pipeline
    score_seo: str = ""
    score_value: str = ""
    score_diff: str = ""

    # Flux étendu — simulation SERP + comparaison
    serp_simulation: str = ""
    serp_comparison: str = ""

    # Scores SERP comparatif (extraits du rapport de comparaison)
    score_serp_pedagogique: str = ""
    score_serp_decisionnelle: str = ""
    score_serp_differenciation: str = ""
    score_serp_interchangeable: str = ""
    score_serp_top3: str = ""
    score_serp_global: str = ""

    # V3 — LLM-SEO optimisée (Agent LLM-Optimizer)
    v3: str = ""

    # Scores Indice Citation IA — 4 dimensions (extraits du bloc ---llm-scores---)
    score_llm_clarte: str = ""
    score_llm_autorite: str = ""
    score_llm_neutralite: str = ""
    score_llm_snippet: str = ""
    score_llm_global: str = ""

    # NER — graphe sémantique + enrichissement (Agents NER-Analyzer + Sem-Enricher)
    ner_json: str = ""   # JSON brut : entities + relations + semantic_gaps + coherence_score
    v4: str = ""         # Article enrichi sémantiquement (V4)
    score_ner_coherence: str = ""  # coherence_score extrait du JSON NER

    # Maillage interne (Agent Link-Strategist) — plan actionnable, ne modifie pas l'article
    internal_links: str = ""

    steps_completed: list[str] = field(default_factory=list)

    def summary(self) -> str:
        """Résumé lisible de l'exécution du pipeline."""
        lines = [
            f"Pipeline article — {self.topic}",
            f"  Mot-clé  : {self.keyword} | Intent : {self.intent}",
            f"  Etapes   : {' > '.join(self.steps_completed)}",
        ]
        if self.score_global:
            lines.append(f"  Score    : {self.score_global} | {self.diagnostic or '?'}")
        if self.score_alignement:
            lines.append(
                f"  Critères : align={self.score_alignement} prof={self.score_profondeur} "
                f"clarté={self.score_clarte} struct={self.score_structure} "
                f"densité={self.score_densite} décis={self.score_decisionnelle} "
                f"SEO={self.score_seo_lt} diff={self.score_differenciation}"
            )
        if self.score_citation_chatgpt:
            lines.append(
                f"  Cit. IA  : ChatGPT={self.score_citation_chatgpt} "
                f"Snippet={self.score_citation_snippet} "
                f"AIOverview={self.score_citation_ai_overview}"
            )
        if self.score_serp_global:
            lines.append(
                f"  SERP     : global={self.score_serp_global} "
                f"péda={self.score_serp_pedagogique} "
                f"décis={self.score_serp_decisionnelle} "
                f"diff={self.score_serp_differenciation}"
            )
        if self.score_llm_global:
            lines.append(
                f"  LLM-SEO  : global={self.score_llm_global} "
                f"clarté={self.score_llm_clarte} "
                f"autorité={self.score_llm_autorite} "
                f"snippet={self.score_llm_snippet}"
            )
        lines += [
            f"  V1       : {len(self.v1.split())} mots",
            f"  V2       : {len(self.v2.split())} mots",
        ]
        if self.v3:
            lines.append(f"  V3 (LLM) : {len(self.v3.split())} mots")
        if self.score_ner_coherence:
            lines.append(f"  NER      : cohérence={self.score_ner_coherence}")
        if self.v4:
            lines.append(f"  V4 (NER) : {len(self.v4.split())} mots")
        if self.internal_links:
            link_count = self.internal_links.count("| ")
            lines.append(f"  Maillage : {max(0, link_count - 2)} liens recommandés")
        return "\n".join(lines)

    def _parse_scores(self) -> None:
        """Stub — implémentation injectée en bas de module (évite import circulaire)."""

    def _parse_serp_scores(self) -> None:
        """Stub — implémentation injectée en bas de module (évite import circulaire)."""

    def _parse_llm_scores(self) -> None:
        """Stub — implémentation injectée en bas de module (évite import circulaire)."""

    def _parse_ner_data(self) -> None:
        """Stub — implémentation injectée en bas de module (évite import circulaire)."""


class ArticlePipeline:
    """
    Pipeline de production d'article schoolsWP — 5 agents séquentiels.

    Usage :
        pipeline = ArticlePipeline()
        result = await pipeline.run(
            topic="Choisir un hébergeur WordPress",
            keyword="meilleur hébergeur WordPress",
            intent="comparative",
            angle="focus coût réel vs performance — sans jargon technique",
        )
        print(result.v3)   # V3 LLM-optimisée (ou result.v2 si include_llm=False)
    """

    def __init__(self, model: str | None = None) -> None:
        model = model or os.getenv("MODEL_WRITER", "claude-sonnet-4-6")
        self.writer = PipelineWriterAgent(model=model)
        self.auditor = PipelineAuditorAgent(model=model)
        self.editor = PipelineEditorAgent(model=model)
        self.llm_optimizer = LlmOptimizerAgent(model=model)
        self.ner_analyzer = NerAnalyzerAgent(model=model)
        self.semantic_enricher = SemanticEnricherAgent(model=model)
        self.internal_link_strategist = InternalLinkStrategistAgent(model=model)
        self.meta_extractor = PipelineMetaExtractorAgent(model=model)
        self.serp_simulator = SerpSimulatorAgent(model=model)
        self.serp_comparator = SerpComparatorAgent(model=model)

    async def run(
        self,
        topic: str,
        keyword: str,
        intent: str,
        angle: str,
        include_meta: bool = True,
        include_serp: bool = False,
        include_llm: bool = True,
        include_ner: bool = True,
        include_links: bool = True,
        on_step: callable | None = None,
    ) -> PipelineResult:
        """
        Exécute le pipeline complet.

        Args:
            topic:         Sujet de l'article
            keyword:       Mot-clé principal
            intent:        informationnelle | comparative | décisionnelle
            angle:         Angle différenciant par rapport à la concurrence
            include_meta:  Activer Agent 5 (méta SEO + FAQ schema)
            include_serp:  Activer le flux étendu SERP (Agent 2b simulation +
                           Agent 2c comparaison) — passe le rapport à l'éditeur
            include_llm:   Activer Agent 4 LLM-SEO (V3 optimisée citations IA)
            include_ner:   Activer Agents 4b/4c NER (graphe sémantique → V4 enrichie)
                           Nécessite include_llm=True pour opérer sur V3 ; fonctionne
                           aussi sur V2 si include_llm=False.
            include_links: Activer Agent 4d Link-Strategist (plan maillage interne)
                           Utilise NER JSON si disponible, sinon analyse l'article seul.
            on_step:       Callback optionnel appelé après chaque étape
                           Signature : on_step(step_name: str, result: str)

        Returns:
            PipelineResult avec v1, audit, v2, v3, v4, meta et métadonnées d'exécution.
        """
        result = PipelineResult(
            topic=topic,
            keyword=keyword,
            intent=intent,
            angle=angle,
        )

        # ── Agent 1 : Rédaction V1 ─────────────────────────────────────────
        result.v1 = await self.writer.run(
            topic=topic,
            keyword=keyword,
            intent=intent,
            angle=angle,
        )
        result.steps_completed.append("V1")
        if on_step:
            on_step("writer", result.v1)

        # ── Agent 2 : Audit critique ────────────────────────────────────────
        result.audit = await self.auditor.run(
            article_v1=result.v1,
            keyword=keyword,
            intent=intent,
        )
        result.steps_completed.append("Audit")
        result._parse_scores()
        if on_step:
            on_step("auditor", result.audit)

        # ── Agent 2b : Simulation SERP Top 5 (flux étendu) ────────────────────
        if include_serp:
            result.serp_simulation = await self.serp_simulator.run(
                keyword=keyword,
                intent=intent,
            )
            result.steps_completed.append("SERP-Sim")
            if on_step:
                on_step("serp_simulator", result.serp_simulation)

            # ── Agent 2c : Comparaison V1 vs SERP ─────────────────────────────
            result.serp_comparison = await self.serp_comparator.run(
                article_v1=result.v1,
                serp_simulation=result.serp_simulation,
                keyword=keyword,
            )
            result.steps_completed.append("SERP-Comp")
            result._parse_serp_scores()
            if on_step:
                on_step("serp_comparator", result.serp_comparison)

        # ── Agent 3 : V2 finale (mode conditionnel selon diagnostic) ──────────
        result.v2 = await self.editor.run(
            article_v1=result.v1,
            audit_report=result.audit,
            keyword=keyword,
            diagnostic=result.diagnostic,
            serp_comparison=result.serp_comparison,
        )
        result.steps_completed.append("V2")
        if on_step:
            on_step("editor", result.v2)

        # ── Agent 4 : LLM-SEO (optimisation citations IA) ─────────────────
        if include_llm:
            result.v3 = await self.llm_optimizer.run(
                article_v2=result.v2,
                keyword=keyword,
            )
            result.steps_completed.append("V3-LLM")
            result._parse_llm_scores()
            if on_step:
                on_step("llm_optimizer", result.v3)

        # ── Agent 4b : NER Analyzer (graphe sémantique) ────────────────────
        if include_ner:
            ner_source = result.v3 if result.v3 else result.v2
            result.ner_json = await self.ner_analyzer.run(
                article=ner_source,
                keyword=keyword,
            )
            result.steps_completed.append("NER")
            result._parse_ner_data()
            if on_step:
                on_step("ner_analyzer", result.ner_json)

            # ── Agent 4c : Enrichisseur Sémantique → V4 ───────────────────
            result.v4 = await self.semantic_enricher.run(
                article=ner_source,
                ner_json=result.ner_json,
                keyword=keyword,
            )
            result.steps_completed.append("V4-NER")
            if on_step:
                on_step("semantic_enricher", result.v4)

        # ── Agent 4d : Maillage interne (plan actionnable) ─────────────────
        if include_links:
            links_source = result.v4 if result.v4 else (result.v3 if result.v3 else result.v2)
            result.internal_links = await self.internal_link_strategist.run(
                article=links_source,
                keyword=keyword,
                ner_json=result.ner_json,
            )
            result.steps_completed.append("Links")
            if on_step:
                on_step("internal_link_strategist", result.internal_links)

        # ── Agent 5 : Méta SEO (optionnel) ─────────────────────────────────
        if include_meta:
            final_article = result.v4 if result.v4 else (result.v3 if result.v3 else result.v2)
            result.meta = await self.meta_extractor.run(
                article_v2=final_article,
                keyword=keyword,
            )
            result.steps_completed.append("Meta")
            if on_step:
                on_step("meta_extractor", result.meta)

        return result


# Injection des méthodes de parse dans PipelineResult (évite import circulaire)
import json  # noqa: E402
import re  # noqa: E402

# Mapping mots-clés → attribut PipelineResult
_SCORE_PATTERNS: list[tuple[list[str], str]] = [
    (["alignement intention", "alignement"], "score_alignement"),
    (["profondeur"], "score_profondeur"),
    (["clarté pédagogique", "clarté"], "score_clarte"),
    (["structure", "hn"], "score_structure"),
    (["densité utile", "densité"], "score_densite"),
    (["qualité décisionnelle", "décisionnel"], "score_decisionnelle"),
    (["potentiel seo long terme", "seo long terme"], "score_seo_lt"),
    (["différenciation schoolswp", "différenciation"], "score_differenciation"),
    (["moyenne globale", "score global"], "score_global"),
]

_CITATION_PATTERNS: list[tuple[list[str], str]] = [
    (["chatgpt", "perplexity"], "score_citation_chatgpt"),
    (["featured snippet", "snippet"], "score_citation_snippet"),
    (["ai overview", "ai overviews"], "score_citation_ai_overview"),
]

_DIAGNOSTIC_KEYWORDS = {
    "RÉÉCRITURE MAJEURE NÉCESSAIRE": "RÉÉCRITURE MAJEURE NÉCESSAIRE",
    "RÉÉCRITURE MAJEURE": "RÉÉCRITURE MAJEURE NÉCESSAIRE",
    "AMÉLIORATION STRATÉGIQUE": "AMÉLIORATION STRATÉGIQUE",
    "VALIDÉ POUR PUBLICATION": "VALIDÉ POUR PUBLICATION",
    "VALIDÉ": "VALIDÉ POUR PUBLICATION",
}


def _parse_scores(self: PipelineResult) -> None:
    """Extrait les 8 critères, la moyenne, le diagnostic et l'Indice IA de l'audit."""
    for line in self.audit.splitlines():
        line_lower = line.lower()
        score_match = re.search(r"(\d+(?:\.\d+)?)/10", line)

        # Diagnostic
        if not self.diagnostic:
            for keyword, normalized in _DIAGNOSTIC_KEYWORDS.items():
                if keyword.upper() in line.upper():
                    self.diagnostic = normalized
                    break

        # Critères 8 notes
        if score_match:
            val = f"{score_match.group(1)}/10"
            for keywords, attr in _SCORE_PATTERNS:
                if any(kw in line_lower for kw in keywords):
                    if not getattr(self, attr):
                        setattr(self, attr, val)
                    break

            # Indice Citation IA
            for keywords, attr in _CITATION_PATTERNS:
                if any(kw in line_lower for kw in keywords):
                    if not getattr(self, attr):
                        setattr(self, attr, val)
                    break

    # Compatibilité ascendante — anciens champs
    self.score_seo = self.score_seo_lt or self.score_global
    self.score_value = self.score_decisionnelle or self.score_clarte
    self.score_diff = self.score_differenciation


PipelineResult._parse_scores = _parse_scores


# Patterns pour les scores SERP comparatifs (extraits du rapport serp_comparison)
_SERP_PATTERNS: list[tuple[list[str], str]] = [
    (["pédagogique", "pedagogique"], "score_serp_pedagogique"),
    (["décisionnelle", "decisionnelle"], "score_serp_decisionnelle"),
    (["différenciation", "differenciation", "différenciati"], "score_serp_differenciation"),
    (["interchangeabilité", "interchangeable", "interchangeab"], "score_serp_interchangeable"),
    (["top 3", "top3", "top-3"], "score_serp_top3"),
    (["score global", "verdict global", "score combiné", "score final"], "score_serp_global"),
]


def _parse_serp_scores(self: PipelineResult) -> None:
    """Extrait les scores SERP comparatifs depuis le rapport de comparaison."""
    for line in self.serp_comparison.splitlines():
        line_lower = line.lower()
        score_match = re.search(r"(\d+(?:\.\d+)?)/10", line)
        if not score_match:
            continue
        val = f"{score_match.group(1)}/10"
        for keywords, attr in _SERP_PATTERNS:
            if any(kw in line_lower for kw in keywords):
                if not getattr(self, attr):
                    setattr(self, attr, val)
                break


PipelineResult._parse_serp_scores = _parse_serp_scores


# Patterns pour les scores LLM-SEO (extraits du bloc ---llm-scores--- dans v3)
_LLM_SCORE_PATTERNS: list[tuple[list[str], str]] = [
    (["clarté extractible", "clarte extractible", "clarté"], "score_llm_clarte"),
    (["autorité perçue", "autorite percue", "autorité"], "score_llm_autorite"),
    (["neutralité experte", "neutralite experte", "neutralité"], "score_llm_neutralite"),
    (["snippet-friendly", "snippet friendly", "snippet"], "score_llm_snippet"),
    (["score global llm", "llm-seo", "score global"], "score_llm_global"),
]


def _parse_llm_scores(self: PipelineResult) -> None:
    """Extrait les scores LLM-SEO depuis le bloc ---llm-scores--- de la V3."""
    # Cherche d'abord le bloc délimité par ---llm-scores---
    marker = "---llm-scores---"
    source = self.v3
    idx = source.lower().find(marker)
    block = source[idx + len(marker):] if idx != -1 else source

    for line in block.splitlines():
        line_lower = line.lower()
        score_match = re.search(r"(\d+(?:\.\d+)?)/10", line)
        if not score_match:
            continue
        val = f"{score_match.group(1)}/10"
        for keywords, attr in _LLM_SCORE_PATTERNS:
            if any(kw in line_lower for kw in keywords):
                if not getattr(self, attr):
                    setattr(self, attr, val)
                break


PipelineResult._parse_llm_scores = _parse_llm_scores


def _parse_ner_data(self: PipelineResult) -> None:
    """Extrait le coherence_score depuis le JSON NER (avec fallback regex)."""
    if not self.ner_json:
        return
    try:
        raw = self.ner_json.strip()
        # Nettoyage des balises markdown que certains LLM ajoutent
        if raw.startswith("```"):
            parts = raw.split("```", 2)
            raw = parts[1]
            if raw.startswith("json"):
                raw = raw[4:]
            raw = raw.rsplit("```", 1)[0]
        data = json.loads(raw.strip())
        self.score_ner_coherence = str(data.get("coherence_score", ""))
    except (json.JSONDecodeError, AttributeError, IndexError):
        # Fallback regex si le JSON est mal formé
        match = re.search(r'"coherence_score"\s*:\s*"([^"]+)"', self.ner_json)
        if match:
            self.score_ner_coherence = match.group(1)


PipelineResult._parse_ner_data = _parse_ner_data
