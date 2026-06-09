---
name: seo-audit-tracker
description: |
  Audit SEO complet, chiffré et tracé d'UN article en ligne (URL) : récupère la data du mot-clé cible avec DataForSEO ET Ubersuggest (volume, difficulté, CPC, intention, SERP top 10), note l'article sur 5 axes /100 (SEO on-page, contenu, intention de recherche, maillage interne, opportunité IA), rédige un rapport Markdown ton schoolsWP, puis enregistre la ligne de synthèse dans un Google Sheet cumulatif (onglets FR / DE / EN).
  Utilise ce skill quand l'utilisateur dit : "audit SEO complet de mon article [url]", "vérifie la data du mot-clé avec DataForSEO et Ubersuggest", "enregistre l'audit dans un Google Sheet", "audit SEO chiffré + suivi", "score SEO de cette URL et log dans Drive", ou fournit une URL d'article à auditer avec data externe et persistance Sheets.
  NE PAS utiliser pour : audit éditorial rapide d'une page SANS data externe ni Sheets (utiliser `seo-page-audit`), audit technique multi-pages du site complet (utiliser `seo-audit`), audit de publication d'un .md local avec Publish Score (utiliser `audit` / `publish_ready.cli`), ou simple append d'une ligne Sheets sans audit (utiliser `gws-sheets-append`).
metadata:
  version: 1.0.0
allowed-tools:
  - mcp__firecrawl__firecrawl_scrape
  - mcp__dataforseo__dataforseo_labs_google_keyword_overview
  - mcp__dataforseo__dataforseo_labs_search_intent
  - mcp__dataforseo__serp_organic_live_advanced
  - mcp__dataforseo__dataforseo_labs_google_related_keywords
  - mcp__dataforseo__on_page_instant_pages
  - mcp__ubersuggest__keyword_overview
  - mcp__ubersuggest__keyword_metrics
  - mcp__ubersuggest__serp_analysis
  - mcp__ubersuggest__keyword_suggestions
  - mcp__ubersuggest__location_suggest
  - Bash
  - Read
  - Write
---

# SEO Audit Tracker

Tu audites UN article publié (une URL), tu croises la data de deux fournisseurs (DataForSEO et Ubersuggest), tu notes l'article sur 5 axes, tu rédiges un rapport lisible, et tu logues une ligne de synthèse dans un Google Sheet cumulatif.

Le rapport Markdown est le livrable principal. Le Google Sheet est le tracker structuré qui s'enrichit à chaque audit. Sans data chiffrée et sans persistance, ce n'est pas ce skill : c'est `seo-page-audit`.

## Contexte schoolsWP (à respecter dans tout texte produit)

Lis ces sources de vérité avant de rédiger si tu as un doute : `content/docs/BRAND_RULES.md`, `content/docs/BRAND_CHECKLIST.md`, `content/docs/BRAND_CONTEXT.json`, `.claude/rules/branding.md`.

- Écris toujours `schoolsWP` (jamais SchoolsWP, schoolswp, Schools WP).
- Voix au singulier : Michaël KIHL est seul derrière schoolsWP. Utilise "je", "sur schoolsWP", "dans mon cas". Bannis "nous", "notre", "nos", "chez schoolsWP on...".
- Ton direct, clair, pédagogique, concret. Phrases courtes (20 mots max). Tutoiement.
- Pas de jargon SEO gratuit : si tu emploies un terme technique, explique-le en une incise.
- Typographie : jamais de tiret long "—" ni de tiret demi-cadratin "–". Uniquement le tiret simple "-", les deux-points, le point ou les parenthèses.
- Mots interdits : disruptif, game changer, scalable, hack, révolutionnaire, incroyable, en un clic, sans effort, il suffit de.
- Slugs evergreen, sans date.
- Termine toujours le rapport par un bloc Brand QA (voir plus bas).

## Étape 0 : collecte de l'input

| Entrée | Obligatoire | Comment la traiter |
| --- | --- | --- |
| **URL article** | Oui | L'article en ligne à auditer. |
| **Mot-clé cible** | Non | Si absent, déduis-le du H1, du title et du contenu, puis annonce-le. Si tu n'es pas sûr, demande. |
| **Langue** | Non | FR / DE / EN. Si absente, détecte-la depuis le contenu et l'URL. C'est elle qui choisit l'onglet du tracker. |

Si l'URL est fournie, lance l'audit. Ne réclame pas le reste si tu peux le déduire avec confiance : annonce simplement le mot-clé et la langue retenus en début de rapport.

Mapping langue -> marché pour la data (défaut, ajustable) :

| Langue | DataForSEO `location_name` / `language_code` | Ubersuggest |
| --- | --- | --- |
| FR | France / fr | locId France, lang fr |
| DE | Germany / de | locId Germany, lang de |
| EN | United Kingdom / en | locId United Kingdom, lang en |

## Étape 1 : lire l'article (on-page)

Récupère le contenu et les signaux on-page de l'URL :

- `mcp__firecrawl__firecrawl_scrape` pour le contenu propre (markdown) + metadata (title, description).
- En option, pour des signaux on-page structurés (Hn, nombre de mots, liens internes/externes, images sans alt), `mcp__dataforseo__on_page_instant_pages`.

Note : `firecrawl_scrape` ou un simple fetch ne voient pas le JSON-LD injecté en JavaScript. Ne conclus pas "pas de schema" sur cette seule base.

Relève : title, meta description, H1, structure Hn, nombre de mots, présence du mot-clé dans les 100 premiers mots, liens internes, liens sortants, images sans alt, fraîcheur apparente.

## Étape 2 : data du mot-clé (les deux fournisseurs)

Le but est de croiser deux sources, pas d'en moyenner une seule. Présente-les côte à côte et signale les écarts notables (volume ou difficulté qui divergent fortement = à prendre avec prudence).

**DataForSEO :**
- `dataforseo_labs_google_keyword_overview` : volume, difficulté (KD), CPC, competition, intention.
- `dataforseo_labs_search_intent` : intention dominante si l'overview ne la donne pas.
- `serp_organic_live_advanced` : SERP live top 10 (concurrents, titres, URLs).
- `dataforseo_labs_google_related_keywords` (option) : variantes sémantiques à couvrir.

**Ubersuggest :**
- `keyword_overview` ou `keyword_metrics` : volume, SEO difficulty (SD), CPC.
- `serp_analysis` : la vue SERP d'Ubersuggest sur le mot-clé.
- `keyword_suggestions` (option) : suggestions associées.
- `location_suggest` si tu dois résoudre le `locId` du marché.

Reste sobre sur la consommation d'API : un appel par besoin, pas de boucle. Si un fournisseur renvoie une erreur ou rien, note-le dans le rapport et continue avec l'autre (ne bloque pas l'audit).

## Étape 3 : noter l'article (5 axes /100)

Ces 5 scores alimentent le tracker. Note chaque axe sur 100 avec une courte justification ancrée dans du concret (cite des éléments réels de la page). Garde la même grille d'un audit à l'autre pour que le suivi ait du sens.

| Axe | Ce qui compte |
| --- | --- |
| **Score SEO** (on-page) | Title (50-60 car., mot-clé placé), meta (150-160 car.), H1 unique, hiérarchie Hn, mot-clé dans les 100 premiers mots, URL propre, alt des images, longueur adaptée. |
| **Score contenu** | Profondeur vs SERP top 3, angle clair dès l'intro, valeur unique, fraîcheur, E-E-A-T (expérience réelle, sources). |
| **Score intention de recherche** | Alignement avec l'intention dominante (data DataForSEO + lecture SERP), couverture des intentions secondaires attendues. |
| **Score maillage interne** | Liens internes contextuels, ancres descriptives, liens vers pages stratégiques, risque de page orpheline. |
| **Score opportunité IA / citation IA** | Réponses extractibles, définitions nettes, blocs snippet (listes, tableaux, FAQ), citabilité pour les AI Overviews et assistants. |

Indique aussi un verdict global lisible (ex : "publiable, ajustements mineurs" / "à retravailler") déduit des scores, mais ce sont les 5 scores qui font foi dans le tracker.

## Étape 4 : rapport Markdown (livrable principal)

Sauvegarde le rapport dans `content/audits/seo/audit-seo-[slug-article]-[langue].md` (slug evergreen, sans date ; langue en minuscules : fr/de/en). Relancer un audit du même article et de la même langue écrase le rapport précédent : c'est voulu, on garde le dernier état.

Structure du rapport (garde cet ordre) :

```
# Audit SEO - [titre court de l'article]

Mot-clé cible : [mot-clé]  -  Langue : [FR/DE/EN]  -  URL : [url]
Date de l'audit : [AAAA-MM-JJ]

## Verdict en une phrase
[Ce que fait la page, pour qui, et si elle performe. Mentionne le verdict global.]

## Scores
| Axe | Score /100 |
| --- | --- |
| SEO on-page | .. |
| Contenu | .. |
| Intention de recherche | .. |
| Maillage interne | .. |
| Opportunité IA / citation IA | .. |

## Data du mot-clé (DataForSEO vs Ubersuggest)
| Métrique | DataForSEO | Ubersuggest |
| --- | --- | --- |
| Volume | .. | .. |
| Difficulté | KD .. | SD .. |
| CPC | .. | .. |
| Intention | .. | - |
[Une ligne de lecture si les deux sources divergent.]

## SERP top 10 (concurrents)
[Liste courte : position, titre, URL. Ce que le top 3 couvre que la page ignore.]

## Audit on-page
[Title, meta, H1/Hn, mots, mot-clé en intro, liens internes/sortants, images sans alt. Constats concrets.]

## Problèmes prioritaires
[Top 3, du plus bloquant au moins bloquant. Problème + impact en une ligne.]

## Recommandations concrètes
[3 à 5 actions faisables, chacune avec le résultat attendu.]

## Actions à faire
[Checklist ordonnée, prête à exécuter.]

## Sources & ressources
- *DataForSEO* - data mot-clé - 2026
- *Ubersuggest* - data mot-clé - 2026

**Brand QA** - schoolsWP
Ton : X/5 | Clarté : X/5 | Valeurs : X/5 | Interdits : X/5 | Vocabulaire : X/5
```

La section `## Sources & ressources` est obligatoire dès qu'on cite de la data externe (règle branding). Le `Brand QA` se note sur 5 par critère ; si un critère passe sous 4, réécris la section concernée avant de livrer.

## Étape 5 : enregistrer dans le Google Sheet (tracker cumulatif)

Le tracker est un Google Sheet unique avec 3 onglets : `FR`, `DE`, `EN`. Chaque audit ajoute UNE ligne dans l'onglet de la langue détectée. Les 15 colonnes (ordre fixe, ne pas réordonner) :

`Date audit | Langue | URL article | Mot-clé cible | Score SEO | Score contenu | Score intention de recherche | Score maillage interne | Score opportunité IA / citation IA | Problèmes prioritaires | Recommandations concrètes | Actions à faire | Priorité | Statut | Notes`

L'écriture passe par le script bundlé `scripts/push_seo_audit.py` (déterministe, idempotent sur les en-têtes). Tu produis un JSON de payload, le script fait toute l'I/O Sheets.

### Configuration du Sheet ID (ne jamais le coder en dur)

Le script lit l'ID du tracker depuis la variable d'environnement `SEO_AUDIT_SHEET_ID` (ou l'argument `--sheet-id`). L'ID de test fourni par Michaël sert de valeur d'exemple, jamais de constante dans le code :

```
SEO_AUDIT_SHEET_ID=1_Sd_NePDGHg-gpY42efXOsS4mBzNLmqYLGtcb4NMohE
```

Pour changer de tracker : modifie `SEO_AUDIT_SHEET_ID` dans ton shell (ou dans `scripts/.env`, voir `scripts/.env.example`), ou passe `--sheet-id <NOUVEL_ID>`. Le script ne contient aucun ID en dur.

### Construire le payload

Écris un fichier JSON temporaire, par exemple `content/audits/seo/.payload-[slug]-[langue].json` :

```json
{
  "tracker_row": {
    "date_audit": "2026-06-09",
    "langue": "FR",
    "url": "https://schoolswp.com/...",
    "mot_cle": "lms wordpress",
    "score_seo": 82,
    "score_contenu": 75,
    "score_intention": 80,
    "score_maillage": 60,
    "score_ia": 70,
    "problemes": "1) Meta absente. 2) H1 sans mot-clé. 3) Zéro lien interne contextuel.",
    "recommandations": "Réécrire la meta (150-160 car.). Placer le mot-clé en H1. Ajouter 3 liens internes.",
    "actions": "Meta -> H1 -> liens internes -> alt images",
    "priorite": "Haute",
    "statut": "À faire",
    "notes": "Volume DataForSEO 880 vs Ubersuggest 720 : écart à surveiller."
  },
  "detailed": {
    "title": "Audit SEO - lms-wordpress - 2026-06-09",
    "tabs": {
      "Synthèse": [["Axe", "Score"], ["SEO on-page", "82"], ["Contenu", "75"]],
      "Mot-clé": [["Métrique", "DataForSEO", "Ubersuggest"], ["Volume", "880", "720"]],
      "SERP top10": [["Position", "Titre", "URL"], ["1", "...", "..."]],
      "On-page": [["Élément", "Constat"], ["Title", "58 car., mot-clé OK"]]
    }
  }
}
```

`detailed` est optionnel. Voir la note sur la création du Sheet détaillé plus bas.

### Lancer le script

Depuis `projects/schoolswp/` :

```bash
# Tracker seul (cas par défaut, 1 ligne dans l'onglet de la langue)
.venv/Scripts/python .claude/skills/seo/seo-audit-tracker/scripts/push_seo_audit.py \
  --data "content/audits/seo/.payload-lms-wordpress-fr.json" --lang FR

# Vérifier sans écrire (recommandé en premier)
.venv/Scripts/python .claude/skills/seo/seo-audit-tracker/scripts/push_seo_audit.py \
  --data "content/audits/seo/.payload-lms-wordpress-fr.json" --lang FR --dry-run

# Tracker + Sheet détaillé par audit (multi-onglets, nouveau fichier)
.venv/Scripts/python .claude/skills/seo/seo-audit-tracker/scripts/push_seo_audit.py \
  --data "content/audits/seo/.payload-lms-wordpress-fr.json" --lang FR --detailed
```

Le script :
1. lit le token Google via `gws auth export` (le CLI `gws` doit être authentifié, comme pour les autres skills `gws-*`) ;
2. s'assure que l'onglet `FR`/`DE`/`EN` existe avec la bonne ligne d'en-tête (création idempotente si manquant) ;
3. ajoute la ligne de synthèse via `values:append` dans le bon onglet ;
4. si `--detailed`, crée un nouveau spreadsheet multi-onglets (titre = `detailed.title`), le déplace dans le dossier `SEO_AUDIT_FOLDER_ID` si défini, et renvoie son URL.

### "Les deux" : tracker + Sheet détaillé

Le design prévoit les deux sorties Sheets demandées : (1) le tracker cumulatif FR/DE/EN, toujours alimenté ; (2) un Sheet détaillé par audit, via `--detailed`. Le détaillé est opt-in pour éviter de créer un fichier Drive à chaque petit test. En usage normal, propose-le. Pour un test léger (une seule ligne, aucun fichier créé en plus), lance sans `--detailed`.

## Garde-fous

- Toujours `--dry-run` d'abord si tu as un doute sur l'ID ou la langue, puis l'écriture réelle.
- Une seule ligne par audit dans le tracker. Ne ré-append pas la même ligne en cas de relance : préviens l'utilisateur qu'une relance ajoute une nouvelle ligne (le tracker est un historique, il ne dé-duplique pas).
- Sobriété API : pas de boucle, pas de batch massif sur DataForSEO/Ubersuggest.
- Si `gws` n'est pas authentifié, le script échoue proprement : indique à l'utilisateur de lancer l'auth `gws` et garde le rapport Markdown (qui, lui, ne dépend pas de Google).

## Rejouer un test plus complet plus tard

Le test de validation est volontairement léger (1 URL, 1 ligne, pas de `--detailed`). Pour une passe plus poussée plus tard :
- ajoute `--detailed` pour générer le Sheet multi-onglets ;
- audite plusieurs URLs d'affilée (une commande par URL, jamais en parallèle pour rester sobre côté API) ;
- compare deux langues du même article en écrivant dans `FR` puis `EN` ;
- pour un vrai benchmark skill-creator (runs parallèles with/without), garde en tête que chaque run consomme des crédits DataForSEO/Ubersuggest et écrit dans le Sheet : isole alors un Sheet de test dédié via `SEO_AUDIT_SHEET_ID`.
