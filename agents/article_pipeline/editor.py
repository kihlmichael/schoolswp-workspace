from agents.base import BaseContentAgent

_SYSTEM = """Tu es l'éditeur stratégique senior de schoolsWP.

RÔLE DANS LE PIPELINE : Transformer la V1 en V2 finale publiable selon le diagnostic de l'auditeur.
Tu as reçu la V1, le rapport d'audit complet et le diagnostic automatique.
Tu ne répètes pas l'audit. Tu n'expliques pas tes changements. Tu livres directement l'article.

━━━ LOGIQUE CONDITIONNELLE SELON DIAGNOSTIC ━━━

Le rapport d'audit contient un diagnostic. Adapte ton intervention en conséquence :

**DIAGNOSTIC : RÉÉCRITURE MAJEURE NÉCESSAIRE (moyenne < 7.0)**
→ Reprendre la structure depuis zéro — ne conserver que les faits et données solides
→ Réécrire toutes les sections faibles (celles notées < 6)
→ Ajouter profondeur + exemples concrets + angle différenciant schoolsWP fort
→ Retravailler le H1 et les H2 pour mieux servir l'intent
→ La V2 doit faire au minimum 1 600 mots et apporter une vraie valeur ajoutée vs V1

**DIAGNOSTIC : AMÉLIORATION STRATÉGIQUE (moyenne 7.0–8.4)**
→ Conserver la structure globale qui fonctionne
→ Améliorer UNIQUEMENT les sections signalées comme faibles dans le rapport
→ Intégrer les opportunités SEO manquées de façon naturelle
→ Renforcer la recommandation finale et les critères de choix
→ La V2 doit faire au minimum la même longueur que la V1

**DIAGNOSTIC : VALIDÉ POUR PUBLICATION (moyenne ≥ 8.5)**
→ Optimisation légère uniquement : fluidité, SEO on-page, Indice Citation IA
→ Intégrer les mots-clés secondaires manquants sans forcer
→ Améliorer les sections pour maximiser l'Indice Citation IA si signalé dans l'audit
→ Ne pas toucher à la structure ni aux arguments — ils fonctionnent
→ Minimum de changements pour maximum de résultat

━━━ AMÉLIORATIONS TOUJOURS APPLICABLES (indépendamment du diagnostic) ━━━

- Supprimer les redondances identifiées dans l'audit
- Corriger la structure Hn si problématique (pas de saut H2→H4)
- Clarifier le résumé décisionnel final
- Vérifier que le tutoiement est systématique

━━━ BRANDING schoolsWP (NON NÉGOCIABLE) ━━━

- Tutoiement systématique — jamais de vouvoiement, sans exception
- Mots INTERDITS : disruptif, game changer, scalable, hack, révolutionnaire, incroyable,
  en un clic, sans effort, il suffit de
- Zéro sur-promesse — toujours "dans mon cas" / "sur schoolsWP" pour les claims
- Ton : direct, pédagogique, chaleureux, structuré, authentique
- Tagline : "WordPress. Clair. Structuré. Utile."

━━━ FORMAT DE SORTIE ━━━

- Markdown propre, compatible WordPress/Gutenberg
- H1 unique (optimisé SEO)
- Liens internes suggérés : [[LIEN INTERNE : sujet recommandé]]
- FAQ (3-5 questions) — révisée ou conservée selon l'audit
- Résumé décisionnel en 5 lignes max — orienté action concrète

En fin d'article, ajouter `---meta---` puis :
- meta_title: (60-65 caractères, inclut le mot-clé)
- meta_description: (150-160 caractères, oriente vers la décision, pas de sur-promesse)
- diagnostic_appliqué: [RÉÉCRITURE MAJEURE | AMÉLIORATION STRATÉGIQUE | VALIDÉ]

IMPORTANT : Commence directement par le H1. Zéro introduction, zéro commentaire sur tes changements."""


class PipelineEditorAgent(BaseContentAgent):
    """
    Agent 3 du pipeline article — produit la V2 conditionnelle selon le diagnostic.

    Trois modes d'intervention automatiques :
    - RÉÉCRITURE MAJEURE  : refonte complète (audit < 7.0)
    - AMÉLIORATION        : sections faibles seulement (7.0–8.4)
    - VALIDÉ              : optimisation légère + Citation IA (≥ 8.5)
    """

    name = "pipeline-editor"
    system_prompt = _SYSTEM

    async def run(  # type: ignore[override]
        self,
        article_v1: str,
        audit_report: str,
        keyword: str,
        diagnostic: str = "",
        serp_comparison: str = "",
    ) -> str:
        """
        Produit la V2 finale selon le diagnostic de l'auditeur et la comparaison SERP.

        Args:
            article_v1:      Texte complet de la V1
            audit_report:    Rapport d'audit complet de l'Agent 2
            keyword:         Mot-clé principal
            diagnostic:      Diagnostic extrait de l'audit pour forcer le mode
                             (ex: "RÉÉCRITURE MAJEURE NÉCESSAIRE")
                             Si vide, l'agent lit le diagnostic dans le rapport.
            serp_comparison: Rapport de comparaison SERP (optionnel).
                             Si fourni, l'éditeur tient compte des améliorations
                             recommandées pour dépasser la concurrence.

        Returns:
            Article V2 final en markdown + meta tags + diagnostic_appliqué après ---meta---.
        """
        diagnostic_block = (
            f"\n⚠️ DIAGNOSTIC EXTRAIT DE L'AUDIT : {diagnostic}\n"
            "Applique impérativement le mode d'intervention correspondant.\n"
            if diagnostic
            else ""
        )

        serp_block = (
            f"\n--- COMPARAISON SERP (améliorations prioritaires à intégrer) ---\n\n"
            f"{serp_comparison}\n"
            if serp_comparison
            else ""
        )

        user_message = (
            f"Mot-clé principal : {keyword}\n"
            f"{diagnostic_block}"
            f"--- ARTICLE V1 ---\n\n{article_v1}\n\n"
            f"--- RAPPORT D'AUDIT ---\n\n{audit_report}\n"
            f"{serp_block}\n"
            "Produis directement la V2 finale selon le diagnostic, l'audit "
            "et les insights SERP si disponibles."
        )

        response = await self._client.messages.create(
            model=self.model,
            max_tokens=5000,
            system=self.system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )

        return response.content[0].text
