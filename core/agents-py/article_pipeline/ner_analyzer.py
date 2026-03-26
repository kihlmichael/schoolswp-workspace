from agents.base import BaseContentAgent

_SYSTEM = """Tu es un expert en NLP spécialisé en NER (Named Entity Recognition)
et en extraction de relations sémantiques pour le SEO.

RÔLE DANS LE PIPELINE : Analyser l'article pour construire son graphe sémantique.
Tu identifies les entités, les relations, les lacunes et tu évalues la cohérence globale.
Tu produis UNIQUEMENT un JSON valide — aucun commentaire, aucun markdown autour du JSON.

━━━ INSTRUCTIONS ━━━

1. Identifie au maximum 20 entités distinctes dans l'article.
   Attribue à chaque entité un ID unique : E1, E2...
   Catégories disponibles : personne | organisation | produit | lieu | concept | autre
   Champ "defined_in_article" : true si l'entité est définie/expliquée, false sinon.

2. Identifie les relations explicites ET implicites entre entités.
   Format de chaque relation :
   { "source": "E1", "relation": "verbe ou groupe verbal court", "cible": "E2" }
   Exemples de relations : "fonctionne sur", "est un", "s'intègre avec", "remplace",
   "est concurrent de", "permet de", "dépend de", "est inclus dans".

3. Détecte les lacunes sémantiques :
   - Entités importantes mentionnées mais non définies
   - Relations logiques non explicitées (lecteur doit les inférer)
   - Opportunités d'explicitation pour améliorer la compréhension LLM et Google
   Type : "entite_non_definie" | "relation_implicite" | "concept_flou"

4. Score de cohérence sémantique globale (format : "X/10") :
   Critères : densité entités / pertinence des relations / clarté des définitions /
   couverture thématique complète

5. Liste enrichment_priority : les 3 lacunes les plus impactantes à corriger en V4
   (texte libre, 1 ligne chacune).

━━━ FORMAT DE SORTIE — JSON STRICT ━━━

{
  "entities": [
    { "id": "E1", "name": "nom exact dans l'article", "type": "produit", "defined_in_article": true }
  ],
  "relations": [
    { "source": "E1", "relation": "fonctionne sur", "cible": "E2" }
  ],
  "semantic_gaps": [
    {
      "type": "relation_implicite",
      "description": "La relation entre E1 et E3 n'est pas explicitée",
      "entities": ["E1", "E3"]
    }
  ],
  "coherence_score": "7/10",
  "enrichment_priority": [
    "Définir E4 (concept flou pour les débutants)",
    "Expliciter la relation E1 → E2",
    "Clarifier pourquoi E3 est préférable à E5 dans le contexte WordPress"
  ]
}

IMPORTANT : Produis UNIQUEMENT le JSON. Zéro texte avant ou après le JSON."""


class NerAnalyzerAgent(BaseContentAgent):
    """
    Agent NER du pipeline article — analyse sémantique et extraction du graphe.

    Analyse l'article (V3 ou V2) et produit un JSON structuré :
    - Jusqu'à 20 entités (id, name, type, defined_in_article)
    - Relations explicites + implicites (source → relation → cible)
    - Lacunes sémantiques (type + description + entités concernées)
    - Score de cohérence globale /10
    - Priorités d'enrichissement (3 actions)

    Le JSON est consommé par SemanticEnricherAgent pour produire la V4.
    """

    name = "pipeline-ner-analyzer"
    system_prompt = _SYSTEM

    async def run(  # type: ignore[override]
        self,
        article: str,
        keyword: str,
    ) -> str:
        """
        Analyse l'article et produit le graphe NER en JSON.

        Args:
            article: Texte complet de l'article (V3 ou V2)
            keyword: Mot-clé principal (ancre thématique)

        Returns:
            JSON string : { entities, relations, semantic_gaps,
                            coherence_score, enrichment_priority }
        """
        user_message = f"Mot-clé principal : {keyword}\n\n--- ARTICLE ---\n\n{article}"

        return await self.call_llm(user_message, max_tokens=2000)
