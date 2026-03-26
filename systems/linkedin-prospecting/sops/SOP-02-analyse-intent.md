# SOP-02 — Analyse d'intention

## Objectif

Analyser les commentaires du post pour detecter les signaux d'intention business et classer la pertinence de chaque commentateur.

## Input

- JSON normalise issu de SOP-01
- Variables metier : `signaux_forts`, `signaux_faibles`, `exclusions`, `offre`, `icp_principal`

## Outil

Claude (prompt `prompts/prompt-02-intent.md`)

## Traitement

### Etape 1 — Lecture du post

Comprendre le sujet, le contexte et le type d'audience attire.

### Etape 2 — Analyse de chaque commentaire

Pour chaque commentaire :
1. Detecter les mots-cles business
2. Identifier les signaux d'intention
3. Classer le niveau d'intention
4. Justifier la classification

### Niveaux d'intention

| Niveau | Definition | Exemples |
|---|---|---|
| `high_intent` | Besoin explicite, demande concrete, recherche de solution | "On cherche justement un outil pour ca", "Comment tu fais pour...?" |
| `medium_intent` | Interet implicite, engagement reel sans demande directe | "Tres pertinent, on a le meme probleme", "Interessant pour notre equipe" |
| `low_intent` | Engagement faible, reaction sociale | "Bravo !", "Top", "Merci pour le partage" |
| `no_intent` | Aucun signal exploitable | emoji seul, tag d'un contact, commentaire hors sujet |

### Signaux forts (exemples par defaut)

- Demande explicite ("comment faire", "tu recommandes quoi")
- Besoin exprime ("on cherche", "on a besoin de")
- Probleme concret ("notre probleme c'est", "on galere avec")
- Recherche d'outil ("quel outil pour", "tu utilises quoi")
- Volonte d'echanger ("on peut en parler ?", "je suis preneur")
- Question operationnelle ("ca marche comment", "c'est quoi le process")

### Signaux faibles (exemples par defaut)

- Accord generique ("tout a fait", "je suis d'accord")
- Reaction simple ("top", "genial", "bravo")
- Compliment vide ("super post")
- Commentaire flou ("interessant")
- Tag sans contexte ("@prenom regarde ca")

## Output

Voir champ `intent_analysis` dans `schemas/apify-normalized.json`

```json
{
  "detected_keywords": ["automatisation", "linkedin", "outbound", "pipeline"],
  "intent_analysis": [
    {
      "comment_id": "c1",
      "commenter_name": "Jane Doe",
      "comment_text": "Interessant, on cherche justement a structurer ca.",
      "intent_level": "high_intent",
      "intent_signals": ["cherche solution", "besoin actuel"],
      "business_relevance": "high",
      "intent_reason": "Besoin explicite et contexte d'usage confirme."
    }
  ],
  "warnings": []
}
```
