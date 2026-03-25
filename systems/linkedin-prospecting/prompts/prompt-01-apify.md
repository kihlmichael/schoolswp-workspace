# Prompt SOP-01 — Analyse et normalisation du scrape Apify

> A utiliser dans un noeud Claude dedie, apres le noeud Apify.
> Input : payload brut Apify. Output : JSON normalise.

---

Tu executes la SOP-01 : Collecte et normalisation des donnees source d'un post LinkedIn.

## Objectif

Transformer les donnees brutes issues d'Apify en un JSON propre, normalise et exploitable pour la suite du pipeline de prospection.

## Input

Un payload brut provenant d'Apify contenant :
- Metadonnees du post LinkedIn
- Liste des commentaires
- Auteurs des commentaires
- URLs ou identifiants de profils si disponibles

Voici le payload Apify :

```json
{{apify_raw_output}}
```

## Procedure

1. Extraire les metadonnees du post (url, texte, auteur, date, reactions, nombre de commentaires)
2. Extraire chaque commentaire avec ses champs (id, texte, auteur, url profil, date)
3. Supprimer les commentaires ou `comment_text` est vide, null ou ne contient que des espaces
4. Dedoublonner par `commenter_profile_url` — garder le premier commentaire si doublon
5. Normaliser les espaces (trim, remplacer multi-espaces par un seul)
6. Conserver les emojis (ils portent du signal)
7. Generer un `lead_id` unique par commentateur (format : `lead_XXX`)
8. Lister les anomalies dans `warnings`

## Format de sortie

Retourne **uniquement** un JSON strict avec cette structure :

```json
{
  "post_metadata": {
    "post_url": "",
    "post_text": "",
    "post_author_name": "",
    "post_author_profile_url": "",
    "post_date": "",
    "reaction_count": 0,
    "comment_count": 0
  },
  "comments": [
    {
      "comment_id": "",
      "comment_text": "",
      "commenter_name": "",
      "commenter_profile_url": "",
      "comment_date": ""
    }
  ],
  "raw_leads": [
    {
      "lead_id": "",
      "source_comment_id": "",
      "commenter_name": "",
      "commenter_profile_url": ""
    }
  ],
  "warnings": []
}
```

## Regles strictes

- Pas de texte hors du JSON
- Dedoublonnage obligatoire
- Signaler les donnees manquantes dans `warnings`
- Garder les IDs source quand ils existent
- Si un champ est absent du payload Apify, mettre `null` (pas de string vide)
