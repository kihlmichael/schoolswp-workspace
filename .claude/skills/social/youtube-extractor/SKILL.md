---
name: youtube-extractor
description: |
  Extrait les données d'une vidéo YouTube via pipeline 2 sources : Apify (`starvibe/youtube-video-transcript` pour transcript + métadonnées) + MCP RapidAPI YouTube (Video_Details pour stats enrichies + Video_Comments). Sortie : fichier Markdown structuré à la racine du projet, prêt à recycler en article ou brief.
  Utilise ce skill quand l'utilisateur dit : "extrais cette vidéo YouTube", "transcript de cette vidéo", "récupère les commentaires de cette vidéo", "scrape cette URL YT", "donne-moi les infos de cette vidéo", "YouTube to Markdown", ou fournit une URL YouTube à transformer en fichier exploitable.
  NE PAS utiliser pour : transcript YouTube uniquement via DataForSEO endpoint (utiliser `dataforseo_youtube_subtitles`, voir `reference_dataforseo_youtube_subtitles.md`), tentative via Apify pintostudio/topaz_sharingan (HTTP 402, voir `reference_apify_x402_transcripts.md`), ou production d'une nouvelle vidéo YouTube schoolsWP (utiliser `schoolswp-youtube-studio`).
---

# YouTube Extractor — Pipeline multi-sources

Extraire les metadonnees, le transcript et les commentaires d'une video YouTube
en chainant deux sources complementaires, puis structurer les resultats dans un
fichier Markdown a la racine du projet.

## Architecture du pipeline

Le pipeline utilise deux sources en parallele pour maximiser la couverture :

```
URL YouTube
    |
    +---> Source 1 : Apify (starvibe/youtube-video-transcript)
    |         -> transcript, metadonnees, description
    |
    +---> Source 2 : MCP RapidAPI YouTube
    |         -> Video_Details : metadonnees enrichies (vues, likes, chaine, date, description)
    |         -> Video_Comments : commentaires avec auteurs et likes
    |
    +---> Fusion --> Fichier Markdown
```

La source 1 (Apify) est l'acteur principal car il fournit le transcript. La source 2
(RapidAPI) complete avec les commentaires et sert de fallback pour les metadonnees.

## Prerequis

- Cle API Apify configuree dans `.env` (`APIFY_TOKEN=...`)
- MCP RapidAPI YouTube configure dans `.mcp.json`

Verifie la presence de la cle Apify avant de lancer l'extraction. Si absente, demande
a l'utilisateur de la configurer dans `.env`.

## Source 1 : Apify — starvibe/youtube-video-transcript

Acteur principal. Fournit transcript + metadonnees en un seul appel.

**Champs retournes** : title, description, channel_name, view_count, like_count,
comment_count, published_at, duration_seconds, transcript_text, video_id, thumbnail,
subscriber_count, language, is_auto_generated.

**Schema d'entree** :

```json
{
  "youtube_url": "https://www.youtube.com/watch?v=VIDEO_ID",
  "language": "en",
  "include_transcript_text": true
}
```

**Appel API REST** :

```bash
APIFY_TOKEN=$(grep APIFY_TOKEN .env | cut -d= -f2)
curl -s -X POST \
  "https://api.apify.com/v2/acts/starvibe~youtube-video-transcript/runs?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"youtube_url": "URL_ICI", "language": "en", "include_transcript_text": true}'
```

**Polling du statut** : interroger `/v2/actor-runs/{runId}` jusqu'a `status: SUCCEEDED`.
Intervalle recommande : 10 secondes. L'acteur finit generalement en moins de 30 secondes.

**Recuperation des resultats** :

```bash
curl -s "https://api.apify.com/v2/datasets/{datasetId}/items?token=$APIFY_TOKEN&format=json"
```

**Pricing** : $5.00 / 1 000 resultats (Pay-Per-Event).

### Alternatives transcript (si starvibe echoue)

| Acteur | Quand l'utiliser |
|--------|------------------|
| `topaz_sharingan/youtube-transcript-scraper` | Transcript echoue, besoin de formats multiples |
| `karamelo/youtube-transcripts` | Extraction en batch (canal entier) |

## Source 2 : MCP RapidAPI YouTube

Fournit les commentaires et sert de verification/complement pour les metadonnees.

**Outils MCP utilises** :

1. `mcp__rapidapi-youtube__Video_Details` — metadonnees completes (titre, description, vues, likes, chaine, date, thumbnail)
   - Parametre : `id` = video ID ou URL complete
2. `mcp__rapidapi-youtube__Video_Comments` — commentaires avec auteur et likes
   - Parametre : `id` = video ID

## Process d'execution

1. **Extraire le video ID** — depuis l'URL (youtube.com/watch?v=ID ou youtu.be/ID)
2. **Lancer les deux sources en parallele** :
   - Apify `starvibe/youtube-video-transcript` (pour le transcript)
   - MCP `Video_Details` (pour les metadonnees enrichies)
   - MCP `Video_Comments` (pour les commentaires)
3. **Fusionner les resultats** — privilegier Apify pour le transcript, RapidAPI pour les metadonnees et commentaires
4. **Gerer les absences** — si une donnee est absente des deux sources, l'indiquer explicitement
5. **Generer le fichier Markdown** — selon le template ci-dessous
6. **Nommer le fichier** — `YYYY-MM-DD_youtube_{titre-en-kebab-case}.md` (date du jour, max 60 caracteres pour le slug)
7. **Sauvegarder a la racine du projet**
8. **Afficher le recapitulatif**

## Regles de fusion

Quand les deux sources retournent le meme champ, appliquer cette priorite :

| Champ | Source prioritaire | Raison |
|-------|-------------------|--------|
| Titre | RapidAPI | Titre propre sans suffixe " - YouTube" |
| Description | RapidAPI | Description complete |
| Vues | RapidAPI | Temps reel |
| Likes | RapidAPI | Temps reel |
| Chaine | Apify (channel_name) | Disponible dans les deux |
| Date | Apify (published_at) | Format ISO 8601 |
| Transcript | Apify (transcript_text) | Seule source |
| Commentaires | RapidAPI (Video_Comments) | Plus complet, avec likes |

## Gestion d'erreurs

- **Video privee / supprimee** — l'indiquer dans le fichier, ne pas bloquer l'execution
- **Transcript indisponible** — section "Non disponible — aucun sous-titre detecte"
- **Apify timeout** — retenter une fois, puis passer aux metadonnees RapidAPI seules
- **RapidAPI echoue** — utiliser les metadonnees Apify comme fallback
- **Aucune source ne repond** — creer le fichier avec toutes les sections en "Non disponible" + raison

## Template Markdown

TOUJOURS utiliser ce template exact :

```markdown
# Extraction YouTube — {titre}

## Metadonnees

| Champ     | Valeur |
|-----------|--------|
| URL       | {url} |
| Titre     | {titre} |
| Chaine    | {nom chaine} |
| Vues      | {nombre} |
| Likes     | {nombre} |
| Commentaires | {nombre total} |
| Date      | {date publication} |
| Duree     | {duree en secondes ou mm:ss} |

## Description

{description complete}

## Transcript

{transcript complet, formate en paragraphes lisibles — retirer les marqueurs [Music] si non pertinents}

## Commentaires

{liste des commentaires, format : **@auteur** — commentaire (X likes)}

## Donnees indisponibles

{liste des champs non recuperes + raison, ou "Aucune — toutes les donnees ont ete recuperees"}

## Metadonnees d'extraction

- **Sources** : starvibe/youtube-video-transcript (Apify) + RapidAPI YouTube
- **Date d'extraction** : {YYYY-MM-DD}
- **Langue transcript** : {langue detectee}
- **Sous-titres** : {auto-generes ou manuels}
```

## Recapitulatif final

Apres creation du fichier, afficher en console :

```
Fichier cree : YYYY-MM-DD_youtube_{slug}.md
Champs recuperes : titre, description, vues, likes, chaine, date, transcript, commentaires
Champs manquants : {liste ou "aucun"}
Sources : starvibe/youtube-video-transcript + RapidAPI YouTube
```

## Regles

- Ne jamais fabriquer une donnee absente ou inaccessible — la fiabilite du fichier en depend
- Ne sauter aucune etape du process
- Documenter chaque source utilisee dans la section "Metadonnees d'extraction"
- Le fichier Markdown doit etre propre, lisible et directement exploitable dans un pipeline editorial
- Toujours lancer les sources en parallele quand c'est possible (gain de temps)
