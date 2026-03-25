# SOP-01 — Collecte Apify

## Objectif

Recuperer les donnees brutes du post LinkedIn et de ses commentaires via Apify.

## Input

```json
{
  "linkedin_post_url": "https://www.linkedin.com/posts/..."
}
```

## Traitement

### Ce qu'Apify doit recuperer

| Champ | Description | Obligatoire |
|---|---|---|
| `post_url` | URL du post | oui |
| `post_text` | Texte complet du post | oui |
| `post_author_name` | Nom de l'auteur | oui |
| `post_author_profile_url` | URL profil auteur | non |
| `post_date` | Date de publication | non |
| `reaction_count` | Nombre de reactions | non |
| `comment_count` | Nombre de commentaires | non |
| `comments[]` | Liste des commentaires | oui |

### Champs par commentaire

| Champ | Description |
|---|---|
| `comment_id` | Identifiant unique |
| `comment_text` | Texte du commentaire |
| `commenter_name` | Nom du commentateur |
| `commenter_profile_url` | URL profil LinkedIn |
| `comment_date` | Date du commentaire |

### Actors Apify recommandes

- `curious_coder/linkedin-post-search-scraper` — scrape posts + commentaires
- `anchor/linkedin-scraper` — alternative

### Normalisation

1. Supprimer les commentaires vides (`comment_text` vide ou null)
2. Dedoublonner par `commenter_profile_url` (garder le premier commentaire)
3. Normaliser les espaces et caracteres speciaux
4. Conserver les emojis (ils portent du signal)

## Validation

Le scrape est **valide** si :
- `post_text` existe ET contient > 10 caracteres
- OU au moins 1 commentaire non vide existe

## Cas d'echec

| Erreur | Action |
|---|---|
| URL invalide | Stopper, log erreur |
| Post inaccessible (prive) | Stopper, log erreur |
| Scrape vide | Stopper, log erreur |
| Quota Apify atteint | Retry apres delai, puis stopper |
| Commentaires = 0 | Log warning, continuer avec post seul |

## Output

Voir `schemas/apify-normalized.json`
