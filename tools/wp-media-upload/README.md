# wp-media-upload

Outil d'upload d'images WordPress avec métadonnées SEO completes pour schoolswp.com.

Par article : depose tes captures dans inbox/[slug-article]/, cree un manifest YAML avec les metadonnees, lance la commande, et les images sont sur WordPress avec Alt text, Titre, Legende et Description remplis automatiquement.

## Prerequis

- Python 3.11+
- ExifTool (recommande pour baker les metadonnees XP dans le JPEG)
- Variables d'environnement WordPress definies system-wide :
  - WP_API_URL (ex: https://schoolswp.com/wp-json)
  - WP_API_USERNAME
  - WP_API_PASSWORD (Application Password, pas mot de passe admin)

## Install

Depuis projects\schoolswp\tools\wp-media-upload\ :

    pip install -r requirements.txt

Puis ExifTool (une fois) :

    winget install OliverBetz.ExifTool

## Workflow type

1. Depose tes JPEG dans inbox/flyingpress-avis/
2. Cree manifest.yaml dans le meme dossier (template fourni par Claude via skill wp-image-metadata-seo)
3. Lance : python cli.py upload --article flyingpress-avis --dry-run
4. Verifie le rapport, ajuste si besoin
5. Lance : python cli.py upload --article flyingpress-avis

## Commandes

    python cli.py env-check                        # verifie env + connexion WP
    python cli.py list --article <slug>            # liste inbox/<slug>/
    python cli.py upload --article <slug>          # upload reel
    python cli.py upload --article <slug> --dry-run
    python cli.py upload --article <slug> --no-exif

## Regles de nommage (schoolsWP)

- Pas de date dans le nom de fichier (pas de -2026, -avril)
- Pas de mention schoolswp (le domaine le contient deja)
- Prefixe numerique 01-, 02- pour garantir l'ordre

## Idempotence

Si un fichier est deja dans processed/<slug>/, il est ignore. Pour re-uploader : supprime manuellement de processed/ et relance.

## Logs

Tout est logue dans logs/uploads.log (timestamp, fichier, media ID, URL, status HTTP).

## Depannage

- 401 : verifie les 3 variables d'environnement WP (Application Password obligatoire)
- 404 sur l'article : article probablement en draft, mets en publish ou utilise un ID publie
- ExifTool not found : installe via winget, ou utilise --no-exif
