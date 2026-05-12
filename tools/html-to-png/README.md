# html-to-png

Convertit les fichiers `slide-*.html` d'un dossier en PNG. Conçu pour les carrousels Instagram schoolsWP, réutilisable pour n'importe quel deck HTML.

Format par défaut : 1080×1350 (Instagram feed 4:5), deviceScaleFactor 2 (retina).

## Setup (une fois)

Depuis le dossier `tools/html-to-png/` :

    npm install

Playwright télécharge Chromium au premier install (~150 Mo).

## Usage

Carrousel Instagram 4:5 (format par défaut) :

    node tools/html-to-png/capture.mjs content/inspirations/instagram-carrousels/5-erreurs-wp-seo

Format carré 1:1 :

    node tools/html-to-png/capture.mjs <dossier> --width=1080 --height=1080

Format Stories 9:16 :

    node tools/html-to-png/capture.mjs <dossier> --width=1080 --height=1920

## Options

| Flag | Défaut | Description |
| --- | --- | --- |
| `--width` | 1080 | Largeur viewport |
| `--height` | 1350 | Hauteur viewport (1350 = Instagram 4:5) |
| `--scale` | 2 | deviceScaleFactor (2 = retina) |
| `--selector` | `.slide` | Élément CSS à capturer |
| `--pattern` | `slide-` | Préfixe des fichiers HTML à matcher |
| `--output` | (même que input) | Dossier de sortie |
| `--help` | - | Affiche l'aide |

## Convention HTML attendue

Le script capture l'élément qui matche `--selector` (par défaut `.slide`). Le HTML doit contenir un wrapper avec cette classe et les dimensions exactes du format cible.

Exemple minimal :

    <!DOCTYPE html>
    <html>
    <head><link rel="stylesheet" href="_styles.css"></head>
    <body>
      <div class="slide">
        <!-- contenu de la slide -->
      </div>
    </body>
    </html>

## Carrousels schoolsWP existants

- [`content/inspirations/instagram-carrousels/5-erreurs-wp-seo/`](../../content/inspirations/instagram-carrousels/5-erreurs-wp-seo/) - 8 slides, premier carrousel template
