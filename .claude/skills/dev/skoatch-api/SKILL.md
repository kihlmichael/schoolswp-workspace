---
name: skoatch-api
description: |
  Pilote l'API Skoatch (https://skoatch.com/api) via le tool Python `tools/skoatch/` pour generer des articles, lister projets, recuperer crédits et statuts. Bearer token Sanctum, polling asynchrone integre, codes HTTP geres. Sert un AUTRE site WordPress que schoolswp.com.
  Utilise ce skill quand l'utilisateur dit : "Skoatch", "skoatch.com", "genere un article via Skoatch", "check mes credits Skoatch", "liste mes projets Skoatch", "publie l'article Skoatch X", ou demande de toucher au code de `tools/skoatch/`.
  NE PAS utiliser pour : produire un article a publier sur schoolswp.com (le pipeline schoolsWP a ses propres regles voix/brand `BRAND_RULES.md`), gerer le contenu d'un cocon schoolsWP (utiliser `schoolswp-article-workflow` ou `thruuu-writer`), ou se substituer au pipeline `brain.bat` / `content_factory` pour le site principal.
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Grep
  - Glob
last_reviewed: 2026-05-11
review_interval_days: 180
---

# Skoatch API

Client Python + CLI dans `tools/skoatch/` qui wrappe l'API Skoatch v1 (Laravel Sanctum bearer token). Pensé pour piloter la generation de contenu vers un site WordPress tiers (PAS schoolswp.com — voir la regle d'isolation en bas).

## Quand intervenir

L'utilisateur veut :

- consulter son solde de credits Skoatch
- lancer la generation d'un article (avec ou sans polling jusqu'au terminal)
- recuperer le statut d'un article en cours
- lister ses projets Skoatch et leurs articles termines
- publier ou marquer comme publie un article termine
- ajuster le code du tool / corriger un endpoint

## Architecture du tool

Tout vit dans `tools/skoatch/` :

- `client.py` : classe `SkoatchClient` + `SkoatchError` + helpers `pretty()` / `status_label()`
- `cli.py` : argparse, dispatch vers les methodes du client, output JSON sur stdout
- `__init__.py` : reexpose `SkoatchClient`, `SkoatchError`, `TERMINAL_STATUSES`
- `README.md` : reference complete pour l'humain
- `.env` (gitignored) : `SKOATCH_TOKEN=...`
- `.env.example` : template

Importable en Python depuis la racine projet (le tool est sous `tools/`, donc `from tools.skoatch import SkoatchClient` apres `cd projects/schoolswp`).

## Token

Ordre de resolution (le premier renseigne gagne) :

1. Flag `--token` sur la commande CLI
2. Variable d'env `SKOATCH_TOKEN`
3. `tools/skoatch/.env` (gitignored)
4. `.env` a la racine projet

Pour obtenir un token :

- Dashboard Skoatch (https://skoatch.com/account/api) — recommande, fonctionne aussi pour comptes Google
- Ou via la sous-commande `login` (uniquement comptes avec mot de passe)

Stocker dans `tools/skoatch/.env` (plus localise) plutot que dans le `.env` global. Ne JAMAIS commiter le token.

## Commandes CLI (cheatsheet)

Lancer depuis la racine projet schoolsWP. Toutes les commandes sortent du JSON sur stdout et des messages d'avancement sur stderr.

Inspection :

    .venv/Scripts/python -m tools.skoatch.cli env-check
    .venv/Scripts/python -m tools.skoatch.cli credits
    .venv/Scripts/python -m tools.skoatch.cli form-data

Helpers (couteux en credits) :

    .venv/Scripts/python -m tools.skoatch.cli generate-title --input "..." --language-id 1
    .venv/Scripts/python -m tools.skoatch.cli generate-structure --input "..." --language-id 1

Lifecycle article :

    .venv/Scripts/python -m tools.skoatch.cli create --input "..." --language-id 1 --payload payload.json --wait
    .venv/Scripts/python -m tools.skoatch.cli status --id 42
    .venv/Scripts/python -m tools.skoatch.cli wait --id 42 --max-wait 7200
    .venv/Scripts/python -m tools.skoatch.cli publish --id 42
    .venv/Scripts/python -m tools.skoatch.cli mark-published --id 42 --wordpress-url https://...
    .venv/Scripts/python -m tools.skoatch.cli delete --id 42

Projets :

    .venv/Scripts/python -m tools.skoatch.cli projects
    .venv/Scripts/python -m tools.skoatch.cli project-posts --project-id 10
    .venv/Scripts/python -m tools.skoatch.cli mark-project-published --id 42

## Workflow type article sur-mesure

1. `env-check` pour confirmer token + reachability + solde.
2. `form-data` pour recuperer `language_id`, `site_id`, `image_style_id`, `content_prompt_id`, etc.
3. Construire un `payload.json` avec les options (`is_featured_image`, `is_images_in`, `content_options`, `quiz_*`, `outline`, `external_links`).
4. `create --payload payload.json --wait` : lance la generation et polle jusqu'au terminal. Sur succes (`job_status_id=20`), le contenu HTML est dans `data.content`, les images dans `data.pictures`.
5. Optionnel : `publish --id N` pour push WordPress (site connecte cote Skoatch obligatoire), ou `mark-published --id N --wordpress-url ...` si la publication WP est faite ailleurs.

## Polling : ce qui est gere

`poll_until_done()` (utilise par `wait` et `create --wait`) :

- 0 a 30 min : poll toutes les 30 s
- 30 a 120 min : backoff a 3 min
- Au-dela de `max_wait` (defaut 7200 s = 2 h) : leve `SkoatchError(408)`. Le post n'est PAS perdu cote Skoatch — relancer `status --id N` plus tard.

Statuts terminaux qui arretent le polling :

- `20` succes
- `30` erreur technique
- `31` erreur fetch URL
- `33`, `35` erreur images max (contenu OK sans images)
- `36` retry max atteint

## Codes HTTP & SkoatchError

Tout code >= 400 leve `SkoatchError(status_code, message, body)` :

- `401` token manquant ou invalide — verifier `SKOATCH_TOKEN`
- `402` credits insuffisants — `body["credits_needed"]` et `body["credits_available"]` sont disponibles
- `403` ressource pas a l'utilisateur (mauvais token)
- `422` validation — `body["errors"]` liste les champs
- `500` erreur serveur — retry plus tard

Le CLI imprime l'erreur sur stderr et exit 1, le JSON du body est print en bonus.

## Format outline

`outline` (champ optionnel de `create`) est une **chaine JSON** (pas un objet), tableau d'objets `{"text": "Titre H2"}`. Le tool ne fait pas la stringification automatique — passer la chaine deja serialisee dans le payload.

## Endpoints non encore implementes

Si l'utilisateur a besoin d'un endpoint absent, ajouter une methode dans `client.py` + une sous-commande dans `cli.py`. Endpoints actuellement non couverts : aucun cote articles, mais l'API peut evoluer — toujours verifier avec la doc Skoatch (paste fournie le 2026-05-11).

## Regle d'isolation (importante)

**Le tool Skoatch ne doit JAMAIS produire de contenu destine a schoolswp.com.** Le pipeline schoolsWP repose sur :

- Voix singulier solo "je" (memoire `feedback_voice_singular_solo`) — Skoatch ne respecte pas
- Interdiction em-dash (memoire `feedback_no_em_dash`) — Skoatch en genere
- Brand rules `content/docs/BRAND_RULES.md` — Skoatch ne connait pas
- Workflow defini par `brain.bat`, `content_factory`, `thruuu-writer`, `schoolswp-article-workflow`

L'usage Skoatch est destine a un autre site WordPress sans cette contrainte. Ne jamais piper la sortie Skoatch dans le pipeline de generation schoolsWP ni publier directement vers https://schoolswp.com.

## Liens

- API doc source : paste fournie le 2026-05-11 (https://skoatch.com/api)
- Tool : `tools/skoatch/README.md`
- Patterns equivalents : `tools/wp-media-upload/` (autre tool Python autonome avec CLI)
