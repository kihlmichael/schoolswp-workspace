# 5 erreurs WordPress SEO 2026 · Pack social complet

Article source : <https://schoolswp.com/erreurs-wordpress-seo-2026/> (à publier)
Brief : [_shared/brief.md](_shared/brief.md)

## Formats produits

| Plateforme | Format | Dimensions | Dossier | Fichiers |
|---|---|---|---|---|
| Instagram feed | 4:5 | 1080×1350 | [instagram-feed/](instagram-feed/) | 8 slides + PNG + meta |
| LinkedIn carrousel | 1:1 | 1080×1080 | [linkedin-carousel/](linkedin-carousel/) | 8 slides + PDF + meta |
| Pinterest pins | 2:3 | 1000×1500 | [pinterest-pins/](pinterest-pins/) | 5 pins + 2 meta YAML |
| Instagram Stories | 9:16 | 1080×1920 | [instagram-stories/](instagram-stories/) | 7 stories + meta |
| Instagram Square | 1:1 | 1080×1080 | [instagram-square/](instagram-square/) | pointer LinkedIn |
| Twitter / Bluesky | 16:9 | 1600×900 | [twitter-card/](twitter-card/) | 1 carte résumé + meta |
| YouTube thumbnail | 16:9 | 1280×720 | [youtube-thumbnail/](youtube-thumbnail/) | 1 thumb + meta |
| TikTok cover | 9:16 | 1080×1920 | [tiktok-cover/](tiktok-cover/) | 1 cover + meta |

## Workflow

    node tools/html-to-png/process-series.mjs content/social-series/5-erreurs-wp-seo

Le script orchestre `capture` + `inject-meta` + `export-pdf` (LinkedIn) sur tous les sous-dossiers détectés.

## Statut

Première série schoolsWP, validée 2026-05-07 par Michael. Migration vers `social-series/` + ajout des seo-meta.yaml rétroactivement le même jour.
