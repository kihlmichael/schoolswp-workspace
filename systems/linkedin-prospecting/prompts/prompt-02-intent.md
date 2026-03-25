# Prompt SOP-02 — Detection d'intention

> A utiliser dans un noeud Claude dedie, apres la normalisation Apify.
> Input : JSON normalise SOP-01 + variables metier. Output : intent_analysis JSON.

---

Tu executes la SOP-02 : Analyse d'intention et pertinence business.

## Objectif

Evaluer les commentaires issus d'un post LinkedIn pour detecter :
- Signaux d'intention business
- Mots-cles dominants
- Pertinence commerciale
- Potentiel de qualification

## Input

### JSON normalise du post

```json
{{normalized_post_json}}
```

### Contexte metier

- offre = {{offre}}
- icp_principal = {{icp_principal}}
- signaux_forts = {{signaux_forts}}
- signaux_faibles = {{signaux_faibles}}
- exclusions = {{exclusions}}

## Procedure

1. Lire le texte du post pour comprendre le sujet et l'audience
2. Pour chaque commentaire :
   a. Detecter les mots-cles business lies a l'offre
   b. Identifier les signaux d'intention (voir reference ci-dessous)
   c. Classer le niveau d'intention
   d. Justifier en 1-2 phrases

### Reference signaux forts

- Demande explicite ("comment faire", "tu recommandes quoi")
- Besoin exprime ("on cherche", "on a besoin de")
- Probleme concret ("notre probleme c'est", "on galere avec")
- Recherche d'outil ("quel outil pour", "tu utilises quoi")
- Volonte d'echanger ("on peut en parler ?", "je suis preneur")
- Question operationnelle ("ca marche comment", "c'est quoi le process")

### Reference signaux faibles

- Accord generique ("tout a fait", "je suis d'accord")
- Reaction simple ("top", "genial", "bravo")
- Compliment vide ("super post")
- Commentaire flou ("interessant")
- Tag sans contexte

## Niveaux d'intention

| Niveau | Definition |
|---|---|
| `high_intent` | Besoin explicite, demande concrete, recherche de solution |
| `medium_intent` | Interet implicite, engagement reel sans demande directe |
| `low_intent` | Engagement faible, reaction sociale |
| `no_intent` | Aucun signal exploitable |

## Format de sortie

Retourne **uniquement** un JSON strict :

```json
{
  "detected_keywords": [],
  "intent_analysis": [
    {
      "comment_id": "",
      "commenter_name": "",
      "comment_text": "",
      "intent_level": "high_intent|medium_intent|low_intent|no_intent",
      "intent_signals": [],
      "business_relevance": "high|medium|low|none",
      "intent_reason": ""
    }
  ],
  "warnings": []
}
```

## Regles strictes

- Pas de texte hors du JSON
- Chaque commentaire doit etre analyse
- Justification obligatoire pour chaque classification
- Les signaux_forts et signaux_faibles du contexte metier priment sur les references par defaut
