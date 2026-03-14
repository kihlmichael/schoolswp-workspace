"""
Module LLM-SEO schoolsWP — Audit de citabilité IA + optimisation AI Overviews

Différent du LlmOptimizerAgent (pipeline V2→V3) :
  – Standalone : fonctionne sur n'importe quel article (publié ou draft)
  – Audit d'abord : détecte les signaux IA présents / absents
  – Scoring par plateforme : Google AI Overview, Perplexity, ChatGPT Browse, Bing Copilot
  – Mode optimize : injecte les signaux manquants sans réécrire ce qui fonctionne

Deux modes :
    # Audit uniquement (score + signaux + recommandations)
    agent = LlmSeoAgent()
    result = await agent.audit(article, keyword="lms wordpress rentable")
    print(result.citation_score)           # 78/100
    print(result.google_ai_overview_pct)   # 55 %

    # Audit + optimisation (injecte les signaux manquants)
    result = await agent.optimize(article, keyword="lms wordpress rentable")
    print(result.article_optimized)
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from agents.base import BaseContentAgent

# ---------------------------------------------------------------------------
# Prompt d'audit — détecte les 5 signaux de citabilité IA
# ---------------------------------------------------------------------------

_AUDIT_SYSTEM = """\
Tu es un expert LLM-SEO spécialisé en AI Overviews et extraction IA pour schoolsWP.

MISSION
Analyser un article WordPress et évaluer sa citabilité pour les moteurs IA :
Google AI Overviews · Perplexity · ChatGPT Browse · Bing Copilot.

━━━ 5 SIGNAUX À ÉVALUER ━━━

SIGNAL 1 — RÉPONSE RAPIDE (25 pts)
L'article contient-il un bloc "Réponse rapide" ou équivalent ?
Critères : placé avant le premier H2 · ≤ 60 mots · réponse directe et autonome ·
sans référence au contexte de l'article · compréhensible hors contexte.
Score sur 25 + justification.

SIGNAL 2 — BLOCS EXTRACTIBLES (25 pts)
Les paragraphes sont-ils autonomes (compréhensibles sans lire le reste) ?
Critères : ≤ 5 lignes par paragraphe · chaque section répond à UNE question ·
absence d'anaphores contextuelles ("comme vu ci-dessus", "précédemment") ·
listes courtes (≤ 8 items).
Score sur 25 + liste des 1-3 passages les moins autonomes.

SIGNAL 3 — DÉFINITIONS ET ENTITÉS (20 pts)
Les concepts clés sont-ils définis explicitement dans l'article ?
Critères : au moins 2 définitions encadrées ou inline · noms d'outils avec prix/version ·
entités sémantiques (plugins, tarifs, benchmarks) présentes et sourcées.
Score sur 20 + entités manquantes (max 3).

SIGNAL 4 — STRUCTURE SNIPPET-FRIENDLY (15 pts)
L'article est-il structuré pour les featured snippets et AI Overviews ?
Critères : section FAQ en H3 avec réponses directes · tableaux comparatifs ·
listes numérotées pour les étapes · H2 interrogatifs ou comparatifs ·
section "Ce qu'il faut retenir" ou "En résumé" en fin d'article.
Score sur 15.

SIGNAL 5 — COHÉRENCE THÉMATIQUE (15 pts)
L'article reste-t-il sur son sujet sans dispersion ?
Critères : chaque H2 renforce le mot-clé principal · pas de sections hors-sujet ·
angle unique maintenu du début à la fin · pas de répétitions de la même idée.
Score sur 15.

━━━ ESTIMATION PAR PLATEFORME ━━━

Sur la base des 5 signaux, estimer la probabilité de citation (0-100 %) :

- **Google AI Overview** : favorise réponse rapide + FAQ + tableaux + définitions
- **Perplexity** : favorise densité factuelle + sources implicites + entités nommées
- **ChatGPT Browse** : favorise blocs autonomes + définitions inline + logique claire
- **Bing Copilot** : favorise structure snippet + H2 interrogatifs + listes courtes

━━━ FORMAT DE SORTIE OBLIGATOIRE ━━━

Score citation global : XX/100

Signaux détectés :
RÉPONSE RAPIDE : X/25 | [présent / absent / insuffisant]
BLOCS EXTRACTIBLES : X/25 | [fort / moyen / faible]
DÉFINITIONS & ENTITÉS : X/20 | [complet / partiel / absent]
STRUCTURE SNIPPET : X/15 | [optimisée / partielle / absente]
COHÉRENCE THÉMATIQUE : X/15 | [forte / moyenne / faible]

Probabilités de citation :
Google AI Overview : XX %
Perplexity : XX %
ChatGPT Browse : XX %
Bing Copilot : XX %

Points forts citation :
– ...

Signaux manquants (prioritaires) :
– ...

Recommandations d'optimisation :
1. [action concrète — signal ciblé]
2. [action concrète]
3. [action concrète]

Respecte strictement ce format — les scores et probabilités sont parsés automatiquement.\
"""

# ---------------------------------------------------------------------------
# Prompt d'optimisation — injecte les signaux manquants
# ---------------------------------------------------------------------------

_OPTIMIZE_SYSTEM = """\
Tu es un expert LLM-SEO pour schoolsWP, spécialisé en optimisation AI Overviews.

CONTEXTE
Tu as reçu un article WordPress et le rapport d'audit de citabilité IA.
Certains signaux sont absents ou insuffisants.

MISSION
Injecter uniquement les signaux manquants pour maximiser la citabilité IA.
Ne pas réécrire ce qui fonctionne.
Préserver le style et le contenu existants.

TRANSFORMATIONS AUTORISÉES (uniquement si signal absent ou insuffisant)

1. RÉPONSE RAPIDE (si absente ou > 60 mots)
   Ajouter ou réécrire juste après le H1 :
   ## Réponse rapide
   [3 à 6 lignes · réponse directe · sans jargon · autonome · ≤ 60 mots]

2. BLOCS EXTRACTIBLES (si passages trop longs ou dépendants)
   Découper les paragraphes > 5 lignes en blocs courts.
   Supprimer les anaphores contextuelles ("voir ci-dessus", "comme mentionné").
   Chaque paragraphe doit être compréhensible hors contexte.

3. DÉFINITIONS MANQUANTES (si entités non définies)
   Ajouter au format inline ou encadré :
   > **Définition** : [terme] — [définition précise en 1-2 phrases]

4. STRUCTURE SNIPPET (si FAQ absente ou "En résumé" absent)
   Ajouter une section "## Ce qu'il faut retenir" en fin d'article :
   – Liste de 5 lignes · formulations déclaratives · aucune opinion sans preuve

5. COHÉRENCE THÉMATIQUE (si sections hors-sujet)
   Supprimer ou réduire les passages qui ne renforcent pas le mot-clé principal.

RÈGLES ABSOLUES
– Tutoiement systématique (jamais "vous" pour s'adresser au lecteur)
– Mots interdits absents : disruptif, game changer, scalable, hack, révolutionnaire,
  incroyable, "en un clic", "sans effort", "il suffit de"
– Aucune promesse non prouvée — toujours "dans mon cas" / "sur schoolsWP"
– Phrases déclaratives claires — pas de métaphores floues
– Comparaisons factuelles — pas d'affirmations sans données
– Pas de contenu générique non contextualisé WordPress

FORMAT DE SORTIE
L'article complet optimisé en markdown (H1/H2/H3).
Pas de commentaires éditoriaux.
En fin d'article, la ligne exacte `---citation-signals---` puis :

RÉPONSE RAPIDE : [présent / absent / insuffisant]
BLOCS EXTRACTIBLES : [fort / moyen / faible]
DÉFINITIONS & ENTITÉS : [complet / partiel / absent]
STRUCTURE SNIPPET : [optimisée / partielle / absente]
COHÉRENCE THÉMATIQUE : [forte / moyenne / faible]
Score citation estimé post-optimisation : XX/100\
"""


# ---------------------------------------------------------------------------
# CitationSignalResult — dataclass de résultat
# ---------------------------------------------------------------------------


@dataclass
class CitationSignalResult:
    """
    Résultat d'un audit ou d'une optimisation LLM-SEO schoolsWP.

    Produit par LlmSeoAgent.audit() ou LlmSeoAgent.optimize().

    Champs signaux (score /max) :
        signal_reponse_rapide      : /25
        signal_blocs_extractibles  : /25
        signal_definitions         : /20
        signal_structure_snippet   : /15
        signal_coherence           : /15

    Probabilités par plateforme (0-100) :
        google_ai_overview_pct
        perplexity_pct
        chatgpt_pct
        bing_pct

    Mode optimize :
        article_optimized : article modifié (vide si mode audit uniquement)
        optimized         : True si optimize() a été appelé
    """

    citation_score: int = 0

    # Signaux /max
    signal_reponse_rapide: int = 0       # /25
    signal_blocs_extractibles: int = 0   # /25
    signal_definitions: int = 0          # /20
    signal_structure_snippet: int = 0    # /15
    signal_coherence: int = 0            # /15

    # Statuts texte
    status_reponse_rapide: str = ""
    status_blocs: str = ""
    status_definitions: str = ""
    status_snippet: str = ""
    status_coherence: str = ""

    # Probabilités par plateforme
    google_ai_overview_pct: int = 0
    perplexity_pct: int = 0
    chatgpt_pct: int = 0
    bing_pct: int = 0

    # Contenu
    points_forts: list[str] = field(default_factory=list)
    signaux_manquants: list[str] = field(default_factory=list)
    recommandations: list[str] = field(default_factory=list)

    # Sorties texte
    report: str = ""          # rapport d'audit complet
    article_optimized: str = ""  # article optimisé (mode optimize uniquement)
    optimized: bool = False

    @property
    def diagnostic(self) -> str:
        if self.citation_score >= 85:
            return "Hautement citable"
        elif self.citation_score >= 70:
            return "Citable — optimisations mineures"
        elif self.citation_score >= 50:
            return "Partiellement citable"
        else:
            return "Non optimisé pour les IA"

    @property
    def diagnostic_emoji(self) -> str:
        if self.citation_score >= 85:
            return "✅"
        elif self.citation_score >= 70:
            return "🟡"
        elif self.citation_score >= 50:
            return "🟠"
        else:
            return "🔴"

    @property
    def best_platform(self) -> str:
        """Plateforme avec la plus haute probabilité de citation."""
        platforms = {
            "Google AI Overview": self.google_ai_overview_pct,
            "Perplexity": self.perplexity_pct,
            "ChatGPT Browse": self.chatgpt_pct,
            "Bing Copilot": self.bing_pct,
        }
        return max(platforms, key=lambda k: platforms[k])

    @classmethod
    def parse(cls, report: str) -> "CitationSignalResult":
        """Parse le rapport d'audit LLM en CitationSignalResult structuré."""
        result = cls(report=report)

        # Score global
        m = re.search(r"Score citation global\s*:\s*(\d+)/100", report, re.IGNORECASE)
        if m:
            result.citation_score = int(m.group(1))

        # Signaux — score + statut
        # Gère le format avec ou sans bold : "RÉPONSE RAPIDE : 24/25 | présent"
        # et "**RÉPONSE RAPIDE : 24/25** | présent"
        signal_patterns = [
            ("signal_reponse_rapide", "status_reponse_rapide",
             r"\*{0,2}RÉPONSE RAPIDE\s*:\s*(\d+)/25\*{0,2}\s*\|\s*\[?([^\]\n]+?)\]?\s*$"),
            ("signal_blocs_extractibles", "status_blocs",
             r"\*{0,2}BLOCS EXTRACTIBLES\s*:\s*(\d+)/25\*{0,2}\s*\|\s*\[?([^\]\n]+?)\]?\s*$"),
            ("signal_definitions", "status_definitions",
             r"\*{0,2}DÉFINITIONS[^:\*]*:\s*(\d+)/20\*{0,2}\s*\|\s*\[?([^\]\n]+?)\]?\s*$"),
            ("signal_structure_snippet", "status_snippet",
             r"\*{0,2}STRUCTURE SNIPPET[^:\*]*:\s*(\d+)/15\*{0,2}\s*\|\s*\[?([^\]\n]+?)\]?\s*$"),
            ("signal_coherence", "status_coherence",
             r"\*{0,2}COHÉRENCE THÉMATIQUE\s*:\s*(\d+)/15\*{0,2}\s*\|\s*\[?([^\]\n]+?)\]?\s*$"),
        ]
        for score_attr, status_attr, pattern in signal_patterns:
            m = re.search(pattern, report, re.IGNORECASE | re.MULTILINE)
            if m:
                setattr(result, score_attr, int(m.group(1)))
                setattr(result, status_attr, m.group(2).strip())

        # Probabilités par plateforme
        platform_patterns = [
            ("google_ai_overview_pct", r"Google AI Overview\s*:\s*(\d+)\s*%"),
            ("perplexity_pct", r"Perplexity\s*:\s*(\d+)\s*%"),
            ("chatgpt_pct", r"ChatGPT Browse\s*:\s*(\d+)\s*%"),
            ("bing_pct", r"Bing Copilot\s*:\s*(\d+)\s*%"),
        ]
        for attr, pattern in platform_patterns:
            m = re.search(pattern, report, re.IGNORECASE)
            if m:
                setattr(result, attr, int(m.group(1)))

        # Points forts
        m = re.search(
            r"Points forts citation\s*:\s*\n((?:[\–\-][^\n]+\n?)+)",
            report, re.IGNORECASE,
        )
        if m:
            result.points_forts = [
                re.sub(r"^[\–\-]\s*", "", l).strip()
                for l in m.group(1).strip().splitlines() if l.strip()
            ]

        # Signaux manquants
        m = re.search(
            r"Signaux manquants[^\n]*:\s*\n((?:[\–\-][^\n]+\n?)+)",
            report, re.IGNORECASE,
        )
        if m:
            result.signaux_manquants = [
                re.sub(r"^[\–\-]\s*", "", l).strip()
                for l in m.group(1).strip().splitlines() if l.strip()
            ]

        # Recommandations
        m = re.search(
            r"Recommandations d.optimisation\s*:\s*\n((?:\d+\.[^\n]+\n?)+)",
            report, re.IGNORECASE,
        )
        if m:
            result.recommandations = [
                re.sub(r"^\d+\.\s*", "", l).strip()
                for l in m.group(1).strip().splitlines() if l.strip()
            ]

        return result

    def summary(self) -> str:
        lines = [
            f"  Citation score : {self.citation_score}/100  {self.diagnostic_emoji}  {self.diagnostic}",
            f"  Meilleure plateforme : {self.best_platform}",
            "",
            f"  Réponse rapide      : {self.signal_reponse_rapide}/25  {self.status_reponse_rapide}",
            f"  Blocs extractibles  : {self.signal_blocs_extractibles}/25  {self.status_blocs}",
            f"  Définitions         : {self.signal_definitions}/20  {self.status_definitions}",
            f"  Structure snippet   : {self.signal_structure_snippet}/15  {self.status_snippet}",
            f"  Cohérence           : {self.signal_coherence}/15  {self.status_coherence}",
            "",
            f"  Google AI Overview  : {self.google_ai_overview_pct} %",
            f"  Perplexity          : {self.perplexity_pct} %",
            f"  ChatGPT Browse      : {self.chatgpt_pct} %",
            f"  Bing Copilot        : {self.bing_pct} %",
        ]
        if self.signaux_manquants:
            lines += ["", "  Signaux manquants :"]
            for s in self.signaux_manquants[:3]:
                lines.append(f"    – {s}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent d'optimisation (privé — injecte les signaux manquants)
# ---------------------------------------------------------------------------


class _OptimizerAgent(BaseContentAgent):
    """Injecte les signaux manquants identifiés par l'audit."""

    name = "llm-seo-optimizer"
    system_prompt = _OPTIMIZE_SYSTEM

    async def run(  # type: ignore[override]
        self,
        article: str,
        audit_report: str,
        keyword: str,
    ) -> str:
        user_message = (
            f"Mot-clé principal : {keyword}\n\n"
            "--- RAPPORT D'AUDIT CITABILITÉ IA ---\n\n"
            f"{audit_report}\n\n"
            "--- ARTICLE À OPTIMISER ---\n\n"
            f"{article}"
        )
        response = await self._client.messages.create(
            model=self.model,
            max_tokens=6000,
            system=self.system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )
        return response.content[0].text


# ---------------------------------------------------------------------------
# LlmSeoAgent — agent principal
# ---------------------------------------------------------------------------


class LlmSeoAgent(BaseContentAgent):
    """
    Module LLM-SEO schoolsWP — Audit citabilité IA + optimisation AI Overviews.

    DIFFÉRENT du LlmOptimizerAgent (pipeline) :
    – Standalone : fonctionne sur tout article, pas uniquement sur la V2 du pipeline
    – Audit d'abord : score de citabilité IA /100 sur 5 signaux
    – Probabilités par plateforme : Google AI Overview, Perplexity, ChatGPT Browse, Bing
    – Mode optimize : injecte uniquement les signaux manquants (ne réécrit pas l'existant)

    Usage :
        agent = LlmSeoAgent()

        # Audit uniquement
        result = await agent.audit(article, keyword="lms wordpress rentable")
        print(result.citation_score)           # 78/100
        print(result.google_ai_overview_pct)   # 55 %

        # Audit + injection des signaux manquants
        result = await agent.optimize(article, keyword="lms wordpress rentable")
        if result.optimized:
            print(result.article_optimized)
    """

    name = "llm-seo"
    system_prompt = _AUDIT_SYSTEM

    async def audit(
        self,
        article: str,
        keyword: str,
        intent: str | None = None,
    ) -> CitationSignalResult:
        """
        Audite la citabilité IA d'un article (5 signaux + probabilités par plateforme).

        Args:
            article : Contenu markdown à analyser
            keyword : Mot-clé SEO principal
            intent  : Intention de recherche (contexte pour le signal 1 et 4)

        Returns:
            CitationSignalResult avec score /100, 5 signaux, probabilités par plateforme
            et recommandations d'optimisation prioritaires.
        """
        intent_block = f"\nIntention de recherche : {intent}" if intent else ""
        user_message = (
            f"Mot-clé principal : {keyword}"
            f"{intent_block}\n\n"
            "--- ARTICLE À AUDITER ---\n\n"
            f"{article}"
        )
        response = await self._client.messages.create(
            model=self.model,
            max_tokens=2500,
            system=self.system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )
        raw = response.content[0].text
        return CitationSignalResult.parse(raw)

    async def optimize(
        self,
        article: str,
        keyword: str,
        intent: str | None = None,
    ) -> CitationSignalResult:
        """
        Audit + injection des signaux manquants dans l'article.

        Étape 1 : audit (détecte les signaux absents)
        Étape 2 : optimisation ciblée (injecte uniquement ce qui manque)

        Args:
            article : Article à optimiser
            keyword : Mot-clé SEO principal
            intent  : Intention de recherche (optionnel)

        Returns:
            CitationSignalResult avec result.optimized=True et
            result.article_optimized contenant l'article amélioré.
        """
        # Étape 1 — Audit
        result = await self.audit(article=article, keyword=keyword, intent=intent)

        # Étape 2 — Optimisation (même si score élevé — pour injection signaux manquants)
        optimizer = _OptimizerAgent(model=self.model)
        result.article_optimized = await optimizer.run(
            article=article,
            audit_report=result.report,
            keyword=keyword,
        )
        result.optimized = True

        return result

    # Alias pour compatibilité avec le nom "run" attendu par certains workflows
    async def run(  # type: ignore[override]
        self,
        article: str,
        keyword: str,
        intent: str | None = None,
    ) -> CitationSignalResult:
        """Alias de audit() — pour compatibilité avec les workflows."""
        return await self.audit(article=article, keyword=keyword, intent=intent)
