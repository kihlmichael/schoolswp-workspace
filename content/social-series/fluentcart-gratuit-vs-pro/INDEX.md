# FluentCart Gratuit vs Pro · Pack social complet

Article source : <https://schoolswp.com/fluentcart-gratuit-vs-pro/>
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

Tout en 1 commande après écriture des slides + seo-meta.yaml :

    node tools/html-to-png/process-series.mjs content/social-series/fluentcart-gratuit-vs-pro

Le script orchestre `capture` + `inject-meta` + `export-pdf` (LinkedIn) sur tous les sous-dossiers de format détectés.

## Stratégie de publication

| Canal | Action | Contenu |
|---|---|---|
| Instagram | Carrousel feed | 8 PNG `instagram-feed/slide-*.png` |
| LinkedIn | Document carrousel | PDF `linkedin-carousel/carrousel-*.pdf` |
| Pinterest | 5 pins indépendants | PNG + meta YAML pour pinterest-pipeline |
| Instagram Stories | 7 stories successives | PNG + sticker LINK vers post feed |
| Instagram Square | Drop-in LinkedIn | Réutilise les PNG LinkedIn |
| Twitter / Bluesky | 1 post résumé | PNG `twitter-card/slide-01-summary.png` |
| YouTube | Thumbnail si vidéo | PNG `youtube-thumbnail/slide-01-thumbnail.png` |
| TikTok | Cover si vidéo | PNG `tiktok-cover/slide-01-cover.png` |

## Brand check

- Vert signature `#00D400` ✓
- Tagline "Apprends. Exécute. Gagne." sur slide 1 hook + slide CTA ✓
- Voix au "je" (Michael solo) ✓
- Tutoiement systématique ✓
- Em-dash interdit ✓
- Logo officiel + halftone vert ✓
- Metadata SEO bakées (XP*, XMP, IPTC, EXIF) ✓
