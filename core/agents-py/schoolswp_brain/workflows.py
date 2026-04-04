"""
schoolsWP Brain — Workflows de production structurés

3 workflows multi-étapes orchestrés en Python :

  W1 — SeoAuditWorkflow      : Génère V1 → Audit sémantique → V2 optimisée
  W2 — CompetitiveAngleWorkflow : Analyse SERP → Angle différenciant schoolsWP
  W3 — ContentFactoryWorkflow  : Article SEO → 5 formats en parallèle

Usage programmatique :
    from agents.schoolswp_brain.workflows import SeoAuditWorkflow, WorkflowResult

    workflow = SeoAuditWorkflow()
    result = await workflow.run(
        keyword="plugin cache WordPress",
        intent="comparative",
        audience="freelance WordPress intermédiaire",
    )
    print(result.v2)
"""

from __future__ import annotations

import asyncio
import os
from dataclasses import dataclass, field

from agents.base import BaseContentAgent
from agents.schoolswp_brain.agent import SchoolswpBrainAgent

# ---------------------------------------------------------------------------
# Prompts modulaires — W1 (Article SEO → Audit → V2)
# ---------------------------------------------------------------------------

W1_AUDITOR_SYSTEM = """\
Tu es l'auditeur sémantique senior de schoolsWP.

RÔLE
Analyser la V1 d'un article SEO WordPress selon 4 dimensions précises.
Ne réécrire aucune section. Uniquement diagnostiquer et prescrire.

DIMENSIONS D'ANALYSE (traiter les 4 sans exception)

1. COUVERTURE SÉMANTIQUE
   — Quels sous-thèmes l'audience cible s'attendrait à trouver mais sont absents ?
   — Quelles entités sémantiques manquent (plugins, cas d'usage, profils, termes clés) ?

2. EXEMPLES CONCRETS MANQUANTS
   — Chaque section principale (H2) dispose-t-elle d'au moins un exemple terrain concret ?
   — Lister les sections trop abstraites, sans illustration réelle.

3. OPPORTUNITÉS FAQ
   — Quelles questions l'audience poserait à un moteur IA après lecture ?
   — L'article y répond-il ? Lister les 5 à 8 questions non couvertes.

4. MAILLAGE INTERNE MANQUANT
   — Quels silos schoolsWP sont naturellement liés mais non référencés ?
     (automatisation, LMS, CRM, SEO, performance, thèmes, hébergement…)
   — Pour chaque opportunité : [[LIEN INTERNE : sujet / slug suggéré]]

NOTATION OBLIGATOIRE
Inclure dans la section ## Notes :
  - Couverture SEO : X/10
  - Valeur utilisateur : X/10
  - Différenciation : X/10

FORMAT DE SORTIE (markdown structuré, en français)

## Rapport d'audit W1

### Notes
SEO : X/10 | Valeur : X/10 | Différenciation : X/10

### 1. Couverture sémantique
…

### 2. Exemples manquants
…

### 3. Opportunités FAQ
…

### 4. Maillage interne
…

### Recommandations prioritaires pour V2
Liste numérotée, du plus impactant au moins impactant.\
"""

W1_EDITOR_SYSTEM = """\
Tu es l'éditeur senior de schoolsWP.

RÔLE
Améliorer un article WordPress SEO (V1) en intégrant les recommandations d'un audit.
Produire la V2 : plus complète, mieux structurée, plus différenciante.

RÈGLES D'ÉDITION

1. Intégrer TOUTES les recommandations prioritaires de l'audit.
2. Ne pas supprimer ce qui fonctionne dans la V1 — enrichir, pas remplacer.
3. Ajouter les exemples concrets manquants identifiés dans l'audit.
4. Intégrer les questions FAQ identifiées dans une section "Questions fréquentes" (H2).
5. Ajouter les liens internes suggérés [[LIEN INTERNE : …]] au format markdown.
6. Renforcer l'angle différenciant schoolsWP dans l'intro et la conclusion.

BRANDING SCHOOLSWP (obligatoire)
- Tutoiement systématique en français
- Voix : directe, pédagogique, chaleureuse, structurée
- Mots interdits : disruptif, game changer, scalable, hack, révolutionnaire,
  incroyable, "en un clic", "sans effort", "il suffit de"
- Zéro promesse non prouvée — toujours "dans mon cas" / "sur schoolsWP"
- Claims : jamais de superlatives non prouvées

FORMAT DE SORTIE
Article complet en markdown (H1/H2/H3), sans commentaires éditoriaux.
Pas de note d'introduction ou de résumé des changements.
Uniquement l'article V2 prêt à intégrer dans WordPress.\
"""

# ---------------------------------------------------------------------------
# Prompts modulaires — W2 (Analyse SERP → Angle différenciant)
# ---------------------------------------------------------------------------

W2_SERP_ANALYST_SYSTEM = """\
Tu es l'analyste SERP et contenu de schoolsWP.

RÔLE
Analyser le paysage de contenu existant pour un mot-clé WordPress donné.
Identifier les patterns dominants, les angles répétitifs et les failles évidentes.

IMPORTANT
Tu raisonnes à partir de ta connaissance du secteur WordPress / SEO / blogging :
tendances de contenu, formats courants, acteurs habituels, manques structurels.
Sois honnête si la data est incertaine — précise "typiquement" ou "en général".

DIMENSIONS D'ANALYSE (4 obligatoires)

1. TYPES DE CONTENU PRÉSENTS
   Quels formats dominent typiquement ce sujet ?
   (listes, comparatifs, tutos pas-à-pas, avis, guides débutants, etc.)

2. ANGLES DOMINANTS
   Quel positionnement les contenus adoptent-ils en général ?
   Quel message récurrent ressort ? Quelle promesse implicite ?

3. FAIBLESSES FRÉQUENTES
   Que manque-t-il typiquement dans les contenus sur ce sujet ?
   (trop générique, trop technique, sans cas concret, sans contexte business…)

4. SEGMENTS SOUS-SERVIS
   Quels profils ou intentions ne sont pas bien couverts ?
   (freelances, formateurs en ligne, e-commerçants, débutants avancés…)

FORMAT DE SORTIE (markdown, en français)

## Analyse SERP — {mot-clé}

### Types de contenu dominants
…

### Angles récurrents
…

### Faiblesses communes
…

### Segments sous-servis
…

### Synthèse : opportunité identifiée
1 paragraphe — où est l'espace libre pour un contenu vraiment différenciant.\
"""

W2_ANGLE_BUILDER_SYSTEM = """\
Tu es le stratège éditorial de schoolsWP (Michaël KIHL, expert WordPress).

RÔLE
À partir d'une analyse SERP, construire le positionnement différenciant de schoolsWP
pour un contenu sur ce mot-clé. Produire un plan d'angle activable immédiatement.

IDENTITÉ SCHOOLSWP
- Audience cible : freelances WordPress, formateurs en ligne, entrepreneurs sérieux
- Voix : directe, pédagogique, authentique, sans jargon creux
- Tagline : "WordPress. Clair. Structuré. Utile."
- Approche : toujours concret, toujours business, toujours terrain
- Tutoiement systématique en français

FORMAT DE SORTIE (markdown, en français)

## Angle différenciant schoolsWP — {mot-clé}

### Positionnement
Comment schoolsWP aborde ce sujet différemment (1-2 phrases, précis et activable).

### Titres proposés
3 variantes de H1 différenciantes (pas de clickbait, pas de superlatifs vides).

### Structure alternative
Plan H2 complet (6-8 sections), avec pour chaque H2 une justification de son angle différenciant.

### Opportunités longue traîne
2-3 mots-clés dérivés, non couverts, avec potentiel business.

### CTA recommandé
Type de CTA adapté à ce contenu (affiliation, formation, newsletter, outil…)
+ formulation concrète d'un CTA schoolsWP pour ce sujet.

RÈGLES ABSOLUES
- Zéro généralités — tout doit être spécifique à ce mot-clé et à l'audience schoolsWP
- Mots interdits absents : disruptif, game changer, scalable, hack, révolutionnaire,
  incroyable, "en un clic", "sans effort", "il suffit de"\
"""

# ---------------------------------------------------------------------------
# Prompts modulaires — W3 (Content Factory multi-format)
# ---------------------------------------------------------------------------

W3_NEWSLETTER_SYSTEM = """\
Tu es le rédacteur newsletter de schoolsWP.

RÔLE
Transformer un article SEO WordPress en résumé newsletter engageant et concis.

FORMAT OBLIGATOIRE
Longueur : 150 à 250 mots exactement.
Structure :
  1. Accroche (1-2 phrases) — problème réel ou question directe, pas de question rhétorique vide
  2. Corps : 3 points clés maximum — ce que l'article apprend concrètement
  3. CTA (1 phrase) — invitation claire à lire l'article complet

RÈGLES SCHOOLSWP
- Tutoiement systématique en français
- Voix directe, pédagogique, sans jargon
- Mots interdits : disruptif, game changer, scalable, hack, révolutionnaire,
  incroyable, "en un clic", "sans effort", "il suffit de"
- Zéro promesse non prouvée — rester factuel
- Ton chaleureux mais efficace
- Pas d'emojis en excès (max 1-2 si vraiment pertinent)

FORMAT DE SORTIE
Texte brut avec markdown léger (bullets autorisés), prêt à coller dans
ConvertKit, Brevo ou MailPoet. Pas de ligne d'objet (subject line) — juste le corps.\
"""

W3_LINKEDIN_SYSTEM = """\
Tu es le stratège LinkedIn de schoolsWP (Michaël KIHL, expert WordPress).

RÔLE
Adapter un article SEO WordPress en post LinkedIn engageant et professionnel.

CONTRAINTES LINKEDIN
- Longueur : 1 200 à 1 500 caractères (hors hashtags)
- Première ligne : accroche forte — jamais commencer par "Je", jamais question creuse
  → Formats acceptés : affirmation provocante, chiffre concret, problème terrain
- Structure : hook → problème → insight ou solution → apprentissage → CTA
- Pas de bullet points avec tirets — sauts de ligne doubles pour aérer
- 3 à 5 hashtags pertinents en fin : #WordPress #SEO #Automatisation #Freelance #WPTips
- Mentionner schoolsWP ou schoolswp.com une fois maximum (authentique, pas promotionnel)

RÈGLES SCHOOLSWP
- Tutoiement systématique en français
- Ton authentique, expertise terrain, jamais de vente forcée
- Angle business concret : ce que ça change pour le freelance ou l'entrepreneur
- Mots interdits absents

FORMAT DE SORTIE
Post complet, prêt à copier-coller dans LinkedIn. Pas de commentaires ni d'explication.\
"""

W3_TWITTER_SYSTEM = """\
Tu es le créateur de threads X (ex-Twitter) de schoolsWP.

RÔLE
Transformer un article SEO WordPress en thread X pédagogique et engageant.

FORMAT THREAD
- 5 à 8 tweets numérotés [1/N] … [N/N]
- Tweet [1/N] : hook (problème ou insight fort) + annonce du sujet du thread
- Tweets [2/N] à [N-2/N] : 1 insight concret et actionnable par tweet
- Tweet [N-1/N] : synthèse ou recommandation finale
- Tweet [N/N] : CTA → lien article + invitation à s'abonner ou RT

CONTRAINTES PAR TWEET
- Longueur : max 280 caractères, viser 200-250 pour aérer
- Pas d'abréviations, pas de langage SMS
- Chaque tweet compréhensible isolément, hors contexte du thread

RÈGLES SCHOOLSWP
- Tutoiement systématique en français
- Ton direct, une idée par tweet, zéro remplissage
- Mots interdits absents

FORMAT DE SORTIE
Un tweet par ligne, séparés par une ligne vide, numérotation [1/N] en début.
N tweets au total clairement annoncé dans le tweet 1.\
"""

W3_FAQ_AIO_SYSTEM = """\
Tu es l'expert GEO/AIO de schoolsWP.

RÔLE
Créer une section FAQ optimisée pour les AI Overviews (Google AIO) et les réponses
des moteurs IA (ChatGPT, Perplexity, Claude), à partir d'un article WordPress.

RÈGLES CRITIQUES AIO
- Questions : formulées comme un utilisateur les poserait à une IA
  Exemple : non "Quels sont les avantages de X ?" → oui "Quel plugin X choisir en 2026 ?"
- Réponses : 2 à 4 phrases, directes, sans anaphore, sans référence au contexte
  Chaque réponse doit être compréhensible sans avoir lu l'article.
- Paragraphes ≤ 6 lignes
- Aucune promesse non prouvée dans les réponses

NOMBRE DE QUESTIONS : 5 à 7

FORMAT DE SORTIE (markdown + JSON-LD)

## Questions fréquentes

### {Question 1} ?
Réponse directe en 2-4 phrases.

[répéter pour chaque question]

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Question 1 ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Réponse 1 complète."
      }
    }
  ]
}
```

BRANDING SCHOOLSWP
- Tutoiement dans les réponses si pertinent
- Ton expert mais accessible
- Mots interdits absents\
"""

W3_YOUTUBE_SYSTEM = """\
Tu es le créateur de contenu YouTube de schoolsWP (Michaël KIHL, expert WordPress).

RÔLE
Rédiger la description YouTube optimisée d'une future vidéo basée sur un article WordPress.

STRUCTURE DESCRIPTION
1. Phrase d'accroche (1-2 lignes) — visible sans déplier → problème concret ou insight fort
2. Ce que la vidéo couvre (3 à 5 bullets courts)
3. Timestamps suggérés (3 à 5 chapitres)
   Format : 00:00 Titre du chapitre
   → Baser sur la structure de l'article (H2 → chapitres vidéo)
   → Les timecodes sont fictifs mais réalistes (vidéo estimée 10-15 min)
4. CTA (1 ligne) — s'abonner ou visiter schoolswp.com
5. 5 hashtags YouTube : #WordPress #SEO + 3 hashtags spécifiques au sujet

CONTRAINTES
- Longueur totale : 150 à 300 mots
- Premiers 125 caractères : critiques (visibles sans clic "voir plus")
- Pas de promesses vides type "tu vas tout comprendre en 5 minutes"
- Ton pédagogique et authentique

RÈGLES SCHOOLSWP
- Tutoiement systématique en français
- Mots interdits absents
- Aucune affirmation non prouvée

FORMAT DE SORTIE
Description prête à coller dans YouTube Studio. Pas de commentaires éditoriaux.\
"""


# ---------------------------------------------------------------------------
# WorkflowResult — dataclass de résultat unifiée pour les 3 workflows
# ---------------------------------------------------------------------------


@dataclass
class WorkflowResult:
    """
    Résultat unifié pour les 3 workflows schoolsWP.

    Le champ `workflow` indique quel workflow a été exécuté :
      "w1-seo-audit" | "w2-competitive-angle" | "w3-content-factory"

    Seuls les champs correspondants au workflow exécuté sont remplis.
    """

    workflow: str
    keyword: str
    topic: str

    # W1 — Article SEO → Audit → V2
    v1: str = ""
    audit: str = ""
    v2: str = ""

    # W2 — Analyse SERP → Angle différenciant
    serp_analysis: str = ""
    differentiating_angle: str = ""

    # W3 — Content Factory multi-format
    article: str = ""
    newsletter: str = ""
    linkedin: str = ""
    twitter_thread: str = ""
    faq_aio: str = ""
    youtube_description: str = ""

    steps_completed: list[str] = field(default_factory=list)

    def summary(self) -> str:
        """Résumé lisible des étapes complétées et du nombre de mots par output."""
        lines = [f"Workflow : {self.workflow}", f"Mot-clé : {self.keyword}", ""]
        field_labels = {
            "v1": "Article V1",
            "audit": "Audit sémantique",
            "v2": "Article V2",
            "serp_analysis": "Analyse SERP",
            "differentiating_angle": "Angle différenciant",
            "article": "Article SEO",
            "newsletter": "Newsletter",
            "linkedin": "LinkedIn",
            "twitter_thread": "Thread X",
            "faq_aio": "FAQ AIO/GEO",
            "youtube_description": "Description YouTube",
        }
        for step in self.steps_completed:
            key_map = {
                "v1": "v1",
                "audit": "audit",
                "v2": "v2",
                "serp": "serp_analysis",
                "angle": "differentiating_angle",
                "article": "article",
                "newsletter": "newsletter",
                "linkedin": "linkedin",
                "twitter": "twitter_thread",
                "faq-aio": "faq_aio",
                "youtube": "youtube_description",
            }
            attr = key_map.get(step, step)
            content = getattr(self, attr, "")
            wc = len(content.split()) if content else 0
            label = field_labels.get(attr, step)
            lines.append(f"  [OK] {label:<30} {wc:>5} mots")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Sous-agents privés — uniquement utilisés par les workflows ci-dessous
# ---------------------------------------------------------------------------


class _W1AuditorAgent(BaseContentAgent):
    """Audite la V1 d'un article SEO selon 4 dimensions (W1 Step 2)."""

    name = "w1-auditor"
    system_prompt = W1_AUDITOR_SYSTEM

    async def run(  # type: ignore[override]
        self,
        article_v1: str,
        keyword: str,
        intent: str,
        audience: str,
    ) -> str:
        user_message = (
            f"Mot-clé cible : {keyword}\n"
            f"Intention de recherche : {intent}\n"
            f"Audience cible : {audience}\n\n"
            "--- ARTICLE V1 À AUDITER ---\n\n"
            f"{article_v1}"
        )
        return await self.call_llm(user_message, max_tokens=2048)


class _W1EditorAgent(BaseContentAgent):
    """Génère la V2 optimisée à partir de V1 + rapport d'audit (W1 Step 3)."""

    name = "w1-editor"
    system_prompt = W1_EDITOR_SYSTEM

    async def run(  # type: ignore[override]
        self,
        article_v1: str,
        audit_report: str,
        keyword: str,
    ) -> str:
        user_message = (
            f"Mot-clé cible : {keyword}\n\n"
            "--- RAPPORT D'AUDIT ---\n\n"
            f"{audit_report}\n\n"
            "--- ARTICLE V1 ---\n\n"
            f"{article_v1}"
        )
        return await self.call_llm(user_message, max_tokens=4096)


class _W2SerpAnalystAgent(BaseContentAgent):
    """Analyse le paysage de contenu SERP pour un mot-clé (W2 Step 1)."""

    name = "w2-serp-analyst"
    system_prompt = W2_SERP_ANALYST_SYSTEM

    async def run(  # type: ignore[override]
        self,
        keyword: str,
        topic: str,
        intent: str | None = None,
        context: str | None = None,
    ) -> str:
        intent_block = f"\nIntention de recherche : {intent}" if intent else ""
        context_block = f"\n\nContexte supplémentaire :\n{context}" if context else ""
        user_message = (
            f"Mot-clé à analyser : {keyword}\nSujet de l'article envisagé : {topic}{intent_block}{context_block}"
        )
        return await self.call_llm(user_message, max_tokens=2048)


class _W2AngleBuilderAgent(BaseContentAgent):
    """Construit l'angle différenciant schoolsWP depuis l'analyse SERP (W2 Step 2)."""

    name = "w2-angle-builder"
    system_prompt = W2_ANGLE_BUILDER_SYSTEM

    async def run(  # type: ignore[override]
        self,
        keyword: str,
        topic: str,
        serp_analysis: str,
        context: str | None = None,
    ) -> str:
        context_block = f"\n\nContexte supplémentaire :\n{context}" if context else ""
        user_message = (
            f"Mot-clé cible : {keyword}\n"
            f"Sujet envisagé : {topic}\n"
            f"{context_block}\n\n"
            "--- ANALYSE SERP ---\n\n"
            f"{serp_analysis}"
        )
        return await self.call_llm(user_message, max_tokens=1500)


class _W3FormatAgent(BaseContentAgent):
    """
    Agent générique pour la production d'un format multi-canal (W3 Steps 2-6).

    Le system prompt est injecté à l'instanciation, ce qui permet de réutiliser
    la même classe pour les 5 formats parallèles du Content Factory.
    """

    name = "w3-format"

    def __init__(self, system: str, model: str | None = None) -> None:
        super().__init__(model=model)
        self.system_prompt = system

    async def run(  # type: ignore[override]
        self,
        article: str,
        keyword: str,
        topic: str,
    ) -> str:
        user_message = f"Mot-clé principal : {keyword}\nSujet : {topic}\n\n--- ARTICLE SOURCE ---\n\n{article}"
        return await self.call_llm(user_message, max_tokens=1024)


# ---------------------------------------------------------------------------
# W1 — SeoAuditWorkflow
# ---------------------------------------------------------------------------


class SeoAuditWorkflow:
    """
    Workflow W1 — Article SEO → Auto-Audit → V2 Optimisée

    Étapes :
      1. Génère un article V1 complet avec l'analyse stratégique de SchoolswpBrainAgent
      2. Audite la V1 selon 4 dimensions (sémantique, exemples, FAQ, maillage)
      3. Produit la V2 en intégrant toutes les recommandations de l'audit

    Usage :
        workflow = SeoAuditWorkflow()
        result = await workflow.run(
            keyword="plugin cache WordPress",
            intent="comparative",
            audience="freelance WordPress intermédiaire",
            on_step=lambda step, content: print(f"[{step}] {len(content.split())} mots"),
        )
    """

    def __init__(self, model: str | None = None) -> None:
        model = model or os.getenv("MODEL_WRITER", "claude-sonnet-4-6")
        self._brain = SchoolswpBrainAgent(model=model)
        self._auditor = _W1AuditorAgent(model=model)
        self._editor = _W1EditorAgent(model=model)

    async def run(
        self,
        keyword: str,
        intent: str,
        audience: str,
        context: str | None = None,
        on_step: object | None = None,
    ) -> WorkflowResult:
        """
        Exécute le workflow W1 en 3 étapes séquentielles.

        Args:
            keyword:   Mot-clé SEO principal cible
            intent:    Intention de recherche (informationnelle|comparative|décisionnelle)
            audience:  Profil cible (ex : "freelance WordPress intermédiaire")
            context:   Contexte supplémentaire optionnel (plugins, concurrents, angle…)
            on_step:   Callback appelé après chaque étape — signature : (step: str, content: str)

        Returns:
            WorkflowResult avec v1, audit et v2 remplis.
        """
        result = WorkflowResult(
            workflow="w1-seo-audit",
            keyword=keyword,
            topic=keyword,
        )

        brain_context = f"Audience cible : {audience}"
        if context:
            brain_context += f"\n{context}"

        # Step 1 — Génération V1 avec analyse stratégique complète
        result.v1 = await self._brain.run(
            query=keyword,
            mode="w1-article",
            intent=intent,
            context=brain_context,
        )
        result.steps_completed.append("v1")
        if callable(on_step):
            on_step("v1", result.v1)

        # Step 2 — Audit sémantique de la V1
        result.audit = await self._auditor.run(
            article_v1=result.v1,
            keyword=keyword,
            intent=intent,
            audience=audience,
        )
        result.steps_completed.append("audit")
        if callable(on_step):
            on_step("audit", result.audit)

        # Step 3 — Génération V2 optimisée
        result.v2 = await self._editor.run(
            article_v1=result.v1,
            audit_report=result.audit,
            keyword=keyword,
        )
        result.steps_completed.append("v2")
        if callable(on_step):
            on_step("v2", result.v2)

        return result


# ---------------------------------------------------------------------------
# W2 — CompetitiveAngleWorkflow
# ---------------------------------------------------------------------------


class CompetitiveAngleWorkflow:
    """
    Workflow W2 — Analyse SERP → Angle Différenciant schoolsWP

    Étapes :
      1. Analyse le paysage de contenu SERP pour le mot-clé (types, angles, faiblesses)
      2. Construit un angle différenciant schoolsWP activable (positionnement + structure)

    Usage :
        workflow = CompetitiveAngleWorkflow()
        result = await workflow.run(
            keyword="LMS WordPress",
            topic="Choisir son LMS WordPress en 2026",
        )
        print(result.differentiating_angle)
    """

    def __init__(self, model: str | None = None) -> None:
        model = model or os.getenv("MODEL_WRITER", "claude-sonnet-4-6")
        self._serp_analyst = _W2SerpAnalystAgent(model=model)
        self._angle_builder = _W2AngleBuilderAgent(model=model)

    async def run(
        self,
        keyword: str,
        topic: str,
        intent: str | None = None,
        context: str | None = None,
        on_step: object | None = None,
    ) -> WorkflowResult:
        """
        Exécute le workflow W2 en 2 étapes séquentielles.

        Args:
            keyword:  Mot-clé SEO à analyser
            topic:    Sujet de l'article envisagé
            intent:   Intention de recherche optionnelle
            context:  Contexte supplémentaire (audience, budget, concurrents…)
            on_step:  Callback — signature : (step: str, content: str)

        Returns:
            WorkflowResult avec serp_analysis et differentiating_angle remplis.
        """
        result = WorkflowResult(
            workflow="w2-competitive-angle",
            keyword=keyword,
            topic=topic,
        )

        # Step 1 — Analyse SERP
        result.serp_analysis = await self._serp_analyst.run(
            keyword=keyword,
            topic=topic,
            intent=intent,
            context=context,
        )
        result.steps_completed.append("serp")
        if callable(on_step):
            on_step("serp", result.serp_analysis)

        # Step 2 — Construction de l'angle différenciant schoolsWP
        result.differentiating_angle = await self._angle_builder.run(
            keyword=keyword,
            topic=topic,
            serp_analysis=result.serp_analysis,
            context=context,
        )
        result.steps_completed.append("angle")
        if callable(on_step):
            on_step("angle", result.differentiating_angle)

        return result


# ---------------------------------------------------------------------------
# W3 — ContentFactoryWorkflow
# ---------------------------------------------------------------------------


class ContentFactoryWorkflow:
    """
    Workflow W3 — Content Factory schoolsWP (multi-format)

    1 article SEO → 5 formats en parallèle :
      Article principal (Step 1, séquentiel)
      → Newsletter + LinkedIn + Thread X + FAQ AIO/GEO + Description YouTube (Steps 2-6, parallèles)

    Note : les Steps 2-6 lancent 5 appels API simultanément via asyncio.gather.
    En cas de rate limiting sur votre tier Anthropic, certains appels peuvent
    échouer. Relancer le workflow en cas d'erreur APIStatusError 529.

    Usage :
        workflow = ContentFactoryWorkflow()
        result = await workflow.run(
            keyword="FluentCRM vs ActiveCampaign",
            topic="FluentCRM vs ActiveCampaign : lequel choisir pour WordPress ?",
            intent="comparative",
        )
    """

    def __init__(self, model: str | None = None) -> None:
        model = model or os.getenv("MODEL_WRITER", "claude-sonnet-4-6")
        self._brain = SchoolswpBrainAgent(model=model)
        self._newsletter = _W3FormatAgent(system=W3_NEWSLETTER_SYSTEM, model=model)
        self._linkedin = _W3FormatAgent(system=W3_LINKEDIN_SYSTEM, model=model)
        self._twitter = _W3FormatAgent(system=W3_TWITTER_SYSTEM, model=model)
        self._faq_aio = _W3FormatAgent(system=W3_FAQ_AIO_SYSTEM, model=model)
        self._youtube = _W3FormatAgent(system=W3_YOUTUBE_SYSTEM, model=model)

    async def run(
        self,
        keyword: str,
        topic: str,
        intent: str,
        context: str | None = None,
        on_step: object | None = None,
    ) -> WorkflowResult:
        """
        Exécute le workflow W3 : Step 1 séquentiel, Steps 2-6 en parallèle.

        Args:
            keyword:  Mot-clé SEO principal
            topic:    Sujet complet de l'article
            intent:   Intention de recherche (informationnelle|comparative|décisionnelle)
            context:  Contexte supplémentaire optionnel
            on_step:  Callback — signature : (step: str, content: str)

        Returns:
            WorkflowResult avec article + 5 formats remplis.
        """
        result = WorkflowResult(
            workflow="w3-content-factory",
            keyword=keyword,
            topic=topic,
        )

        # Step 1 — Article SEO principal (séquentiel — les autres en dépendent)
        result.article = await self._brain.run(
            query=topic,
            mode="w3-article",
            intent=intent,
            context=context,
        )
        result.steps_completed.append("article")
        if callable(on_step):
            on_step("article", result.article)

        # Steps 2-6 — 5 formats en parallèle (tous lisent l'article, indépendants entre eux)
        tasks = [
            self._newsletter.run(article=result.article, keyword=keyword, topic=topic),
            self._linkedin.run(article=result.article, keyword=keyword, topic=topic),
            self._twitter.run(article=result.article, keyword=keyword, topic=topic),
            self._faq_aio.run(article=result.article, keyword=keyword, topic=topic),
            self._youtube.run(article=result.article, keyword=keyword, topic=topic),
        ]
        outputs = await asyncio.gather(*tasks)
        (
            result.newsletter,
            result.linkedin,
            result.twitter_thread,
            result.faq_aio,
            result.youtube_description,
        ) = outputs

        # Log des étapes parallèles après gather (on_step appelé séquentiellement)
        parallel_steps = [
            ("newsletter", result.newsletter),
            ("linkedin", result.linkedin),
            ("twitter", result.twitter_thread),
            ("faq-aio", result.faq_aio),
            ("youtube", result.youtube_description),
        ]
        for step_name, content in parallel_steps:
            result.steps_completed.append(step_name)
            if callable(on_step):
                on_step(step_name, content)

        return result
