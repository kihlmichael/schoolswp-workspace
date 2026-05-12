# tools/skoatch

Client Python + CLI pour l'API Skoatch (https://skoatch.com/api). Isole du pipeline schoolsWP — usage prevu pour un autre site WordPress.

## Install

Depuis la racine du projet schoolsWP, installer la dependance (uniquement requests, deja dans le venv) :

    .venv/Scripts/python -m pip install -r tools/skoatch/requirements.txt

## Token

Trois sources possibles, dans l'ordre de priorite :

1. Flag --token sur la ligne de commande
2. Variable d'environnement SKOATCH_TOKEN
3. Fichier tools/skoatch/.env (copie de .env.example), puis .env a la racine du projet

Le .env local est gitignored. Pour obtenir un token :

- Dashboard Skoatch : https://skoatch.com/account/api (recommande, fonctionne aussi pour les comptes Google).
- Via CLI (uniquement comptes avec mot de passe) :

      .venv/Scripts/python -m tools.skoatch.cli login --email you@example.com --password secret --device-name skoatch-cli

## Smoke test

    .venv/Scripts/python -m tools.skoatch.cli env-check

Sortie attendue :

    base_url:  https://skoatch.com/api
    token:     OK (hidden)
    connection: OK
    credits:    150

## Commandes

Inspection :

- env-check : verifie token + reachability + solde
- credits : GET /credits
- form-data : IDs necessaires (sites, languages, statuts, prompts, image styles)

Articles sur-mesure (single-posts) :

- generate-title --input "..." --language-id 1 (coute des credits)
- generate-structure --input "..." --language-id 1 [--title "..."] (coute des credits)
- create --input "..." --language-id 1 [--payload payload.json] [--wait]
- status --id 42 (etat actuel via job_status_id)
- wait --id 42 [--max-wait 7200] (polling jusqu'a statut terminal)
- list [--per-page 15] [--page 1]
- update --id 42 --title "..." --content-file body.html [--extra fields.json]
- publish --id 42 (push sur WordPress, site connecte cote Skoatch requis)
- mark-published --id 42 [--wordpress-url ...] (sans push WP)
- delete --id 42

Projets :

- projects : liste des projets non-standalone
- project-posts --project-id 10 [--per-page 15] [--page 1]
- mark-project-published --id 42 [--wordpress-url ...]
- mark-project-completed --id 42 (repasse 21 vers 20)

## Payload riche : utiliser --payload

Pour passer toutes les options (content_options, quiz_enabled, outline, external_links...), creer un fichier JSON et le passer via --payload payload.json. Les flags --input / --title / --language-id du CLI mergent par-dessus.

Exemple payload.json :

    {
      "language_id": 1,
      "is_auto_generated": true,
      "is_featured_image": true,
      "is_images_in": true,
      "image_style_id": 1,
      "content_options": {
        "min_words_count": 800,
        "max_words_count": 1400,
        "min_h2_count": 3,
        "max_h2_count": 6,
        "use_bold": true,
        "use_lists": true,
        "use_tables": true,
        "quiz_enabled": true,
        "quiz_questions_count": 5,
        "quiz_position_id": 6
      },
      "external_links": [
        {"url": "https://example.com/source", "anchor": "source officielle"}
      ]
    }

Workflow type, avec polling automatique :

    .venv/Scripts/python -m tools.skoatch.cli form-data > form.json
    # reperer language_id, image_style_id, site_id, etc.
    .venv/Scripts/python -m tools.skoatch.cli create --input "chaussures rando impermeables" --payload payload.json --wait > article.json

## Polling

poll_until_done() (utilise par les sous-commandes wait et create --wait) suit la strategie recommandee : poll toutes les 30 s pendant 30 min, puis backoff toutes les 3 min jusqu'a un timeout par defaut de 2 h. Si le timeout est atteint, l'article n'est PAS perdu : relancer status --id N plus tard.

## Statuts terminaux

- 20 succes (contenu disponible)
- 30 erreur technique
- 31 erreur fetch URL
- 33, 35 erreur images max (contenu generalement OK sans images)
- 36 retry max atteint

## Codes HTTP geres

- 401 token manquant ou invalide
- 402 credits insuffisants (body contient credits_needed et credits_available)
- 422 validation (body contient errors)
- Tout >= 400 leve SkoatchError(status_code, message, body)

## Usage Python direct

    from tools.skoatch import SkoatchClient
    
    client = SkoatchClient(token="...")
    print(client.get_credits())
    
    resp = client.create_article({
        "input": "fluentcrm avis",
        "language_id": 1,
        "is_auto_generated": True,
        "is_featured_image": True,
    })
    article_id = resp["data"]["id"]
    final = client.poll_until_done(article_id)
