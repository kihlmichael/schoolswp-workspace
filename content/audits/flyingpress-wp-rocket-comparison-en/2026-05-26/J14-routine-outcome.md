# J+14 Routine — /en/flyingpress-wp-rocket-comparison/

**Date** : 2026-05-26
**Post ID** : 343156
**Permalink** : <https://schoolswp.com/en/flyingpress-wp-rocket-comparison/>
**Statut** : publish
**Baseline push EN** : 2026-05-12 (J+0)

## Fixes appliqués aujourd'hui

### 1. Phrase FR résiduelle (body)

| Avant | Après |
|---|---|
| `<li>Pour <strong>1 site</strong>, le prix est souvent identique ($59/an).</li>` | `<li>For <strong>1 site</strong>, the price is usually the same ($59/year).</li>` |

Méthode : `$wpdb->update` direct sur `wp_posts.post_content` (pas `wp_update_post` — évite `wp_unslash`).

### 2. FAQ Q5 (schema FAQPage `mainEntity[4].name`)

| Avant | Après |
|---|---|
| `Puis-je tester ces plugins avant achat ?` | `Can I test these plugins before buying?` |

Méthode : `update_post_meta('rank_math_schema_FAQPage', ...)`.

## Verifications post-fix

- DB : `still_has_fr_body=false`, `has_new_body_phrase=true`, `q5_after="Can I test these plugins before buying?"` ✓
- `post_modified` : 2026-05-26 09:59:49
- Cache purges : `flying_press_purge_url`, `flying_press_purge_post`, `fp_purge_url`, `rocket_clean_post` ✓
- Rank Math Title : `FlyingPress vs WP Rocket (2026): Which One for WordPress?` — EN ✓
- Rank Math Meta Desc : `🚀 FlyingPress or WP Rocket? 2026 comparison: speed, Core Web Vitals, RUCSS, price. Find the best caching plugin for your WordPress site.` — EN ✓
- Rank Math Focus Keyword : `flyingpress vs wp rocket,wp rocket vs flyingpress` — EN ✓
- Schemas présents : `VideoObject`, `BlogPosting`, `FAQPage` ✓

## Résidu non touché — décision à prendre

Anchor ID HTML interne : `id="comparatif-fonctionnalites"` (sur le H2 "Feature comparison: FlyingPress vs WP Rocket"). C'est du slug ancré, pas du texte visible. Modifier l'ancre casserait les liens entrants (autres articles internes, bookmarks externes, social shares). **Non touché par défaut.**

Action recommandée si tu veux harmoniser :

1. Audit des liens entrants pointant vers `#comparatif-fonctionnalites` (Link Whisper + recherche `#comparatif-` dans la base)
2. Si zéro lien entrant : renommer l'ancre en `feature-comparison`
3. Si liens entrants : laisser tel quel

## KPI à mesurer côté humain (GSC)

Le routine cloud n'a pas d'accès OAuth GSC. À relever manuellement dans GSC Performance, 14 derniers jours, filtre page = `/en/flyingpress-wp-rocket-comparison/` :

| Métrique | Baseline 2026-05-12 | Cible J+14 | Mesure J+14 |
|---|---|---|---|
| Clics (14j) | ~2 / 14j | 10+ | `_à renseigner_` |
| CTR global page | 0.24% | min 0.5% / cible 0.7% | `_à renseigner_` |
| CTR query "wp rocket vs flyingpress" | 1.14% (pos 4.5) | 3%+ | `_à renseigner_` |
| CTR query "best wp rocket alternatives" | 0% (pos 8.9) | toute progression | `_à renseigner_` |

### Arbre de décision

- **CTR ≥ 0.5%** → marquer succès dans Sheet v3, programmer J+30
- **CTR 0.3–0.5%** → sous-cible. Les deux fixes du jour (body + FAQ Q5) peuvent encore faire bouger. Re-mesurer J+21
- **CTR < 0.3%** → pas d'effet textuel. Investiguer SERP (AI Overview EN ? changement layout ?)

## Liens

- Audit J+0 (push) : [content/audits/flyingpress-wp-rocket-comparison-en/2026-05-12/](../2026-05-12/)
- Rapport 90j global : `content/audits/schoolswp-90j-perf/2026-05-12/rapport-complet.pdf`
- Sheet v3 actions SEO : à compléter par l'humain

### 3. Featured image metadata (attachment 348847)

| Champ | Avant | Après |
|---|---|---|
| Title | `FlyingPress vs WP Rocket – WordPress caching plugin comparison 2025` | `FlyingPress vs WP Rocket - WordPress caching plugin comparison` |
| Caption | `... performance in 2025.` | `... performance.` |
| Description | `"FlyingPress vs WP Rocket 2025"` | `"FlyingPress vs WP Rocket"` |
| Alt | `FlyingPress vs WP Rocket 2025 – best WordPress caching plugins ...` | `FlyingPress vs WP Rocket - best WordPress caching plugins ...` |

Corrigé : 2× en-dash (U+2013) interdits + 4× "2025" (article evergreen, repushé 2026). Méthode : `$wpdb->update` direct + `update_post_meta` pour alt. Cache image FlyingPress purgé.

Polylang : attachment 348847 est en `en` ✓, attachment_translations n'a qu'une langue (pas de doublon FR/DE à harmoniser).

### 4. Nouveau visuel à la une (fichier JPG)

Visuel régénéré via pipeline tools/html-to-png/ :

- **Template** : [slide-flyingpress-vs-wp-rocket.html](../../../../tools/html-to-png/featured-images-flyingpress-wp-rocket/slide-flyingpress-vs-wp-rocket.html)
- **Layout** : 1920x1080, grid 2 cols, vs-card pattern. FlyingPress card highlighted (border vert), WP Rocket card standard. Badge "Speed · Caching", titre "FlyingPress vs WP Rocket" (vs en accent vert italic), subtitle EN, wordmark schoolsWP, gradient top bar + glow vert. Brand strict (couleurs #00D400 / #0F1419 / #F4F5F7, Inter).
- **Pas de date** (evergreen), pas d'en/em-dash dans le rendu.

Pipeline d'upload :

1. Render JPG via Playwright (capture-jpg.mjs, q=92) → 109820 bytes
2. SHA256 local : 9d96e6f7...110a2995
3. Endpoint novamira/v1/upload en raw PUT renvoie 500 (incident connu, mémoire reference_novamira_upload_endpoint_500.md)
4. Fallback **multipart POST** → succès HTTP 200, bytes_written 109820, source multipart
5. wp_generate_attachment_metadata regénère sub-sizes : medium, large, thumbnail, medium_large, 1536x1536
6. Purges : FlyingPress hooks (flying purge url, flying purge post, fp purge url) + clean_post_cache. WebP variants inexistants.
7. Round-trip prod : curl HEAD → HTTP 200, Content-Length 109820, Last-Modified 26 May 2026 08:37:35 GMT. **SHA256 prod = SHA256 local** ✓ (byte-perfect)

Filename + path conservés (/wp-content/uploads/2025/08/flyingpress-vs-wp-rocket-wordpress-caching.jpg) → aucun lien entrant cassé, attachment ID 348847 inchangé.

### Optionnel — pas fait, à voir avec Michael

- **EXIF/XMP** (XPTitle, XPKeywords, XPSubject, XPComment, XPAuthor, Copyright) via skill wp-image-metadata-seo + ExifTool. Pas critique SEO direct, utile pour Google Images.
- **Cleanup artefacts locaux** dans le dossier featured-images-flyingpress-wp-rocket/ : image.b64, les 13 chunk_*.txt, et \_prod-roundtrip.jpg. Laissés en place (pas de delete sans validation).

## Inspection GSC 2026-05-26 10:23 — par Michael

Test en ligne après les fixes (09:59) :

- **Google a accès à cette URL** ✓
- **La page peut être indexée** ✓
- **Video discovery** : Vidéo détectée ✓
- **Fils d'Ariane** : 1 élément valide ✓
- **FAQ** : 1 élément valide ✓ (le Q5 patché en EN est validé)
- **Vidéos** : 1 élément valide ✓
- **Indexation demandée** envoyée

### Sur le statut vidéo "contenu complémentaire" (capture antérieure 22 mai)

Le rapport "Aucune vidéo indexée — La vidéo n'est pas sur une page de lecture" n'est **pas une erreur de structured data**. Google distingue :

- **Page de lecture** : page dont le but est de jouer la vidéo (ex: la page YouTube native)
- **Contenu complémentaire** : la vidéo enrichit un article (notre cas, article comparatif)

Pour un article SEO long format, "contenu complémentaire" est le statut attendu. La "vraie" page de lecture est sur YouTube côté Google. **Pas d'action requise.**

### Timing recrawl

Demande d'indexation envoyée 2026-05-26 10:23. Recrawl typique sous 24–72h. SERP devrait refléter le nouveau Q5 EN d'ici **2026-05-29**.

---

*Routine schedulée J+14 — exécutée 2026-05-26 par Claude Code (cloud agent). Inspection GSC 10:23 par Michael.*
