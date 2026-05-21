# Snapshot 2026-05-16 - learn-wordpress-day

Audit pré-publication du brouillon EN (WordPress post id 2274708).

## Fichiers

- [synthese.md](synthese.md) - synthèse exploitable (verdict, plan d'action, métriques)
- [article-current-snapshot.md](article-current-snapshot.md) - contenu de l'article au format markdown allégé (HTML brut récupérable côté serveur via une ability Novamira sur l'objet post id 2274708)
- [dataforseo-volume-en.json](dataforseo-volume-en.json) - volumes US/EN pour 11 mots-clés du champ sémantique (source JSON brute)
- [dataforseo-google-sheet.csv](dataforseo-google-sheet.csv) - export tabulaire (synthèse + historique 12 mois). Source du Google Sheet sur le Drive : [schoolsWP - Volumes SEO - Learn WordPress in a day (EN) - 2026-05-16](https://docs.google.com/spreadsheets/d/1wno-bbKXXiEupb1ju16yLjM336RS9CHEOqB7ODtEjBY/edit)
- [thruuu-serp-summary.md](thruuu-serp-summary.md) - synthèse SERP exploitée (structure SERP + AIO + concurrents + PAA + Related Search)
- [thruuu-raw/serp-analysis.xlsx](thruuu-raw/serp-analysis.xlsx) - export thruuu brut (54 onglets : SERP Overview, AIO Overview, Topic, Heading 2, FAQ, PAA, Related Search, etc.). NB : pas d'audit-article inclus (brouillon → thruuu renvoie 404 sur l'URL `?p=2274708`).
- [captures-brief.md](captures-brief.md) - brief 3 captures (Route A captures perso ou Route B prompts IA fallback). Specs complètes : alt text, captions, métadonnées SEO XMP/EXIF.
- [_generate-captures.py](_generate-captures.py) - script ad-hoc qui appelle Gemini 2.5 Flash Image GA directement (workaround MCP nano-banana cassé). Throttle 15s, 3 prompts éditoriaux schoolsWP-brand.
- [proposed-images/](proposed-images/) - 3 PNG 1024×1024 générés et uploadés sur WP (attachments 2900730, 2900731, 2900732). Contient aussi 3 sidecars .b64 (artefacts intermédiaires, à supprimer manuellement via Explorer).
- [youtube-script.md](youtube-script.md) - script complet vidéo YouTube companion 6'30 (titre + description + tags + script timestamped + brief production ElevenLabs/HeyGen + recyclage 9:16/1:1).

## Données non collectées (justification)

- **thruuu audit page** : non lancé (brouillon, retournerait 404). À lancer après publication.
- **GSC 90j queries + URL inspect** : non applicable (brouillon jamais indexé).
- **publish_ready.cli Publish Score** : non disponible (crédit Anthropic épuisé sur la clé en session). Audit manuel équivalent dans synthese.md sections 1 à 11.

## Status

refonte-effectuee (2026-05-16). Les 5 phases de corrections ont été appliquées et vérifiées byte-perfect côté serveur. Détails dans la section 12 de synthese.md.

Actions humaines restantes avant publication : 2e clic Update dans Gutenberg pour recalcul du score Rank Math (devrait passer à 65-80 après Phase 7 images + Phase 8 Ninja Tables EN), puis bascule du brouillon en publié.
