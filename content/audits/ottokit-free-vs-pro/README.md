# Audit OttoKit Free vs. Pro

> Article comparatif Free vs Pro sur OttoKit (ex-SureTriggers), plateforme d'automatisation WordPress. Cluster « automatisations WordPress » + cluster affilié OttoKit (cloak `/ottokit/`).

## Identifiants

- **Slug** : `ottokit-free-vs-pro`
- **Post IDs** (Polylang) :
  - DE : `2898734` - programmé (`future`), slug `ottokit-kostenlos-vs-pro` → `/de/ottokit-kostenlos-vs-pro/`
  - EN : `2865102` - brouillon, slug `ottokit-free-vs-pro` → `/en/ottokit-free-vs-pro/`
  - FR : `2592422` - **publié** slug `ottokit-gratuit-vs-pro` → `/ottokit-gratuit-vs-pro/` (modified 2026-05-16)
- **Convention slug** : un slug unique par post (le site n'autorise aucun slug partagé entre langues), mot « free » localisé : `gratuit` (FR) / `free` (EN) / `kostenlos` (DE).
- **Focus keyword** : « OttoKit Free vs. Pro »
- **Catégories** : OttoKit, WordPress-Automatisierungen

## Statut courant

**DE + EN : `bloc-3-applique`** (2026-05-19 22:11) - Blocs 1, 2 et 3 appliqués via Novamira `$wpdb->update`. DE prêt à publier ; EN prêt à publier (Rank Math se recalculera à l'ouverture Gutenberg). Reste : captures écran manuelles (DE et EN), Person schema (mu-plugin), Bloc 4 (cluster post-publication).

**FR : `bloc-4-applique`** (2026-05-20 11:18) - Blocs 1, 2, 3 et 4 appliqués. Bloc 4 = nouveau hero (2913947) + 9 captures réelles du compte OttoKit intégrées dans le corps (attachments 2914187-2914195). **Modifications en ligne** (article publié, cache FlyingPress purgé). Reste : Bloc 5 (re-soumission Instant Indexing + recalcul Rank Math via Update Gutenberg + monitoring GSC).

### Historique d'exécution

| Timestamp | Action | Résultat |
| --- | --- | --- |
| 2026-05-19 18:47 | Backup pré-Bloc 1 | `/wp-content/uploads/audit-ottokit-de-PRE-BLOC1-20260519-184751.txt` (39 649 octets) |
| 2026-05-19 18:48 | Bloc 1 transaction `$wpdb->update` | 1 ligne maj, contenu -331 octets, md5 changé |
| 2026-05-19 18:48 | Backup post-Bloc 1 | `/wp-content/uploads/audit-ottokit-de-POST-BLOC1-20260519-184855.txt` |
| 2026-05-19 18:48 | Vérification intégrité Kadence post-Bloc 1 | OK (gradient escape unicode préservé, accordion/CTA/TOC/Ninja Table intacts) |
| 2026-05-19 18:55 | Backup pré-Bloc 2 | `/wp-content/uploads/audit-ottokit-de-PRE-BLOC2-20260519-185554.txt` (39 318 octets) |
| 2026-05-19 19:00 | Création Ninja Table DE jumeau | Nouveau post `ninja-table` ID 2912298 « OttoKit Free vs. Pro : Welchen Tarif sollten Sie 2026 wählen ? » + 4 colonnes DE (Kriterium / OttoKit Free / OttoKit Pro / Fazit) + 6 items DE traduits avec umlauts |
| 2026-05-19 19:03 | Backup pré-Bloc 2 (transaction principale) | `/wp-content/uploads/audit-ottokit-de-PRE-BLOC2-WRITE-20260519-190351.txt` |
| 2026-05-19 19:03 | Bloc 2 + Bloc 3 (KW) transaction `$wpdb->update` | 1 ligne maj, contenu +5 626 octets (39 318 → 44 944), md5 changé |
| 2026-05-19 19:03 | Backup post-Bloc 2 | `/wp-content/uploads/audit-ottokit-de-POST-BLOC2-20260519-190351.txt` |
| 2026-05-19 19:04 | Vérification intégrité Kadence post-Bloc 2 | OK : 6 panes FAQ (vs 5), 0 en-dash, 0 em-dash, JSON-LD FAQPage valide (6 questions), Ninja Table 2912298 rend 2 915 chars HTML |
| 2026-05-19 21:15 | Génération hero PNG via Playwright | 1920x1080 @ 1x, style FluentCRM (fond #F4F5F7, Inter Black, pill, titre avec « Pro » en vert, signature schoolsWP avec WP vert), 115 861 octets, source HTML `assets/featured-images/post-2898734/slide-00-hero-de.html` |
| 2026-05-19 21:17 | Injection métadonnées SEO PNG (ExifTool) | XPTitle, XPSubject, XPComment, XPKeywords, XMP-dc:Title/Description/Creator/Rights, XMP-iptcCore:AltTextAccessibility, EXIF:Artist/Copyright/Software |
| 2026-05-19 21:18 | Upload Novamira `create-upload-link` + PUT multipart | URL signée 10 min, multipart `-F file=@...`, écrit à `/wp-content/uploads/2026/05/hero-ottokit-free-vs-pro-de.png` |
| 2026-05-19 21:18 | `wp_insert_attachment` + métadonnées WP + Polylang DE | Attachment ID **2912480**, sizes WP générées (medium, large, thumbnail, medium_large, 1536x1536), alt allemand, langue Polylang=de |
| 2026-05-19 21:18 | `set_post_thumbnail(2898734, 2912480)` | Featured image définie ✓ (verify_thumbnail_id confirme 2912480) |
| 2026-05-19 20:01 | Backup pré-Blocs EN | `/wp-content/uploads/audit-ottokit-en-PRE-BLOCS-20260519-200109.txt` (37 134 octets) |
| 2026-05-19 20:08 | Création Ninja Table EN jumeau | Post `ninja-table` ID **2912655** « OttoKit Free vs. Pro : Which plan should you choose in 2026 ? » + 4 colonnes EN (Criterion / OttoKit Free / OttoKit Pro / Verdict) + 6 items EN traduits, Polylang=en |
| 2026-05-19 20:09 | Bloc 1 + Bloc 3 EN transaction `$wpdb->update` | 1 ligne maj, contenu +1 513 octets (37 134 → 38 647) : em-dash 2→0, en-dash 1→0, 7 IDs H2 EN, 2 liens cross-langue retirés, 3 liens externes ajoutés, intro KW densifié, 2 H3 Data Retention + Team Collaboration |
| 2026-05-19 20:09 | Backup mid-Blocs EN | `/wp-content/uploads/audit-ottokit-en-MID-BLOC13-20260519-200957.txt` |
| 2026-05-19 20:11 | Bloc 2 EN transaction `$wpdb->update` | 1 ligne maj, contenu +5 661 octets (38 647 → 44 308) : tableId swap 2848098→2912655, pane Make/n8n dans Accordion 0 (3→4 panes), pane Cost dans Accordion 1 (2→3 panes), JSON-LD FAQPage 7 questions EN |
| 2026-05-19 20:11 | Backup post-Blocs EN | `/wp-content/uploads/audit-ottokit-en-POST-BLOCS-20260519-201105.txt` |
| 2026-05-19 20:11 | Vérification intégrité Kadence post-Blocs EN | OK : 7 panes FAQ (vs 5), 0 en-dash, 0 em-dash, 7 H2 IDs EN, 0 lien cross-langue résiduel, JSON-LD FAQPage 7 questions, table EN 2912655 active, intro `<strong>OttoKit Free vs. Pro</strong>` densifié, H3 Data Retention + Team Collaboration insérés sous OttoKit Pro |
| 2026-05-19 20:30 | Correction slug DE | `post_name` 2898734 : `ottokit-free-vs-pro-2` → `ottokit-kostenlos-vs-pro` (update DB direct). Le `-2` était un artefact de collision avec le slug EN `ottokit-free-vs-pro`. Vérif site-wide : 0 slug partagé entre 2 posts → le site impose des slugs uniques. Slug DE désormais localisé et collision-proof (reste propre après un futur Update Gutenberg). |
| 2026-05-20 08:29 | Backup pré-audit FR | `/wp-content/uploads/audit-ottokit-fr-20260520-082921.txt` (38 755 octets) |
| 2026-05-20 08:51 | Bloc 1 + Bloc 3 + liens externes FR transaction `$wpdb->update` | 1 ligne maj, +683 octets (38 755 → 39 438) : en-dash 1→0, intro `<strong>OttoKit Gratuit vs Pro</strong>`, 3 liens externes (ottokit.com/wordpress/, wordpress.org/plugins/suretriggers/, g2.com). Backup mid : `audit-ottokit-fr-MID-BLOC13-20260520-085152.txt` |
| 2026-05-20 10:52 | Bloc 2 FR transaction `$wpdb->update` | 1 ligne maj, +6 015 octets (39 438 → 45 453) : pane Make/n8n (Accordion 0 : 3→4 panes), pane « Combien coûte OttoKit ? » (Accordion 1 : 2→3 panes), JSON-LD FAQPage 7 questions FR. Backup post : `audit-ottokit-fr-POST-BLOCS-20260520-085232.txt` |
| 2026-05-20 10:52 | Vérification intégrité Kadence post-Blocs FR | OK : 7 panes FAQ (vs 5), 0 en-dash, 0 em-dash, 3 liens externes, JSON-LD FAQPage 7 questions, Ninja Table 2848098 inchangée (FR natif), 7 H2 IDs FR inchangés, intro `<strong>OttoKit Gratuit vs Pro</strong>`. **Article publié : modifications en ligne immédiatement.** |
| 2026-05-20 11:02 | Génération hero FR PNG via Playwright | 1920x1080 @1x, style FluentCRM (fond #F4F5F7, Inter Black, pill « OttoKit \| Comparatif 2026 », titre avec « Pro » en vert, carte comparative Gratuit/Pro, signature schoolsWP avec WP vert), 116 459 octets. Source : `assets/featured-images/post-2592422/slide-00-hero-fr.html` |
| 2026-05-20 11:03 | Injection métadonnées SEO PNG (ExifTool) | XPTitle, XPSubject, XPComment, XPKeywords, XPAuthor, Copyright, ImageDescription, XMP-dc, IPTC, XMP-iptcCore:AltTextAccessibility, EXIF:Artist/Copyright/Software. Manifest `seo-meta.yaml` |
| 2026-05-20 11:05 | Upload Novamira + `wp_insert_attachment` + Polylang FR | Attachment **2913947** (`hero-ottokit-gratuit-vs-pro-fr.png`), sizes WP générées, alt/titre/légende/description médiathèque, langue Polylang=fr. `set_post_thumbnail(2592422, 2913947)` ✓ (remplace l'ancien hero 2852045) |
| 2026-05-20 11:13 | Optimisation 9 captures OttoKit | 9 captures réelles (`content/inspirations/ottokit/`) converties en WebP (ffmpeg, max 1600px, 21-44 KB) dans `assets/article-images/ottokit-gratuit-vs-pro/` |
| 2026-05-20 11:14 | Injection métadonnées SEO 9 WebP (ExifTool) | Manifest `seo-meta.yaml` : XPTitle, XPKeywords, XMP, IPTC, AltTextAccessibility, EXIF Artist/Copyright |
| 2026-05-20 11:17 | Upload Novamira + `wp_insert_attachment` × 9 + Polylang FR | Attachments **2914187-2914195**, sizes WP générées, alt/titre/légende/description médiathèque, Polylang=fr |
| 2026-05-20 11:18 | Insertion 9 blocs `wp:image` FR transaction `$wpdb->update` | +5 360 octets (45 453 → 50 813). 9 images insérées après le paragraphe pertinent de chaque section. Backup : `audit-ottokit-fr-POST-IMAGES-20260520-111825.txt` |
| 2026-05-20 11:18 | Vérification intégrité post-images FR | OK : 9/9 blocs `wp:image`, paragraphes 57/57, panes 7/7, accordéons 2/2, FAQPage présent, Ninja Table 2848098 inchangée, featured image 2913947, render OK |
| 2026-05-20 11:20 | Purge cache FlyingPress | `FlyingPress\Purge::purge_everything()` OK + object cache flush (le push DB direct ne déclenche pas l'auto-purge) |

### Bloc 1 - détails appliqués

- 4 en-dash (U+2013) supprimés ✓ remplacés par « : » (apposition allemande)
- 3 liens internes cross-langue (vers slugs FR) neutralisés ✓ balises `<a>` retirées, texte interne conservé. Pages DE cibles inexistantes (`/de/wordpress-automatisierungen/`, `/de/ottokit-erfahrungen/`, `/de/suretriggers-vs-zapier/` toutes NOT_FOUND).
- 7 `id` H2 reslugués en allemand ✓ (`zusammenfassung-vergleich-ottokit-free-pro`, `funktionen-ottokit-free-und-pro`, `ottokit-kostenlos`, `ottokit-pro`, `ottokit-free-vs-pro-preise`, `kundenbewertungen`, `ottokit-free-oder-pro-kaufen`)

### Bloc 2 + densité KW Bloc 3 - détails appliqués

- **Ninja Table DE jumeau** créé ID `2912298` ✓. Le post DE 2898734 référence désormais cet ID au lieu de `2848098` (qui pointait vers le tableau FR). 6 lignes DE : Monatliche Aufgaben, Aktive Workflows, KI-Agenten, Bedingte Logik, Support, Verbundene Websites. Header vert schoolsWP #00d400 préservé.
- **Densité focus KW** ✓ Premier paragraphe enrichi avec `<strong>OttoKit Free vs. Pro</strong>` exact (1 occurrence ajoutée, focus KW maintenant explicite en intro).
- **3 liens externes** ajoutés vers sources primaires :
  - [ottokit.com/wordpress/](https://ottokit.com/wordpress/) ✓ dans H3 « Bedingte Logik und erweiterte Webhooks » (mention « offizielle OttoKit-Plattform listet aktuell über 1 400 Apps »)
  - [wordpress.org/plugins/suretriggers/](https://wordpress.org/plugins/suretriggers/) ✓ dans H3 « Funktionen für einfache Automatisierungsanforderungen » (rating 4,9/5 / 117 Bewertungen)
  - [g2.com/products/ottokit/reviews](https://www.g2.com/products/ottokit/reviews) ✓ dans intro H2 « Kundenbewertungen » (4,5/5)
- **Question FAQ « Wie unterscheidet sich OttoKit von Make und n8n ? »** ✓ ajoutée comme 3e pane de l'accordion droit (3 paragraphes : positionnement OttoKit / Make-n8n / verdict WordPress-zentriert). Insight issu de la SERP DE thruuu (concurrent robert-leitinger.com).
- **JSON-LD FAQPage** ✓ injecté en fin de contenu via `wp:html` block. Schema valide, 6 questions (5 originales + Make/n8n), `mainEntity[]` complet avec answers. Permet d'obtenir le FAQ rich result Google sans dépendre du Rank Math FAQ block.
- **Total** : article passe de 39 318 à 44 944 octets (+ 5 626, +14 %). Balance Gutenberg OK, 6/6 panes accordion alignés, 0 lien cross-langue résiduel.

### Bloc 1 + 2 + 3 EN - détails appliqués (2026-05-19 20:11)

- **Bloc 1** :
  - 2 em-dash (U+2014) + 1 en-dash (U+2013) remplacés par « : » ou « . »
  - 7 `id` H2 reslugués en anglais : `summary-comparison`, `features-free-and-pro`, `ottokit-free`, `ottokit-pro`, `price-difference`, `customer-reviews`, `free-or-pro`
  - 2 liens internes cross-langue FR neutralisés : `/automatisations-wordpress/` (FR introuvable côté CMS) et `/ottokit-avis-automatisation-wordpress/` (pas de traduction EN). Texte reformulé proprement, lien retiré.
- **Bloc 2** :
  - Ninja Table EN jumeau créé ID `2912655` ✓ (4 colonnes EN, 6 items EN, Polylang=en). Post EN référence désormais cet ID au lieu de `2848098` (FR).
  - 3 liens externes ajoutés vers sources primaires :
    - [ottokit.com/wordpress/](https://ottokit.com/wordpress/) ✓ dans la section OttoKit Free (paragraphe « WordPress automations »)
    - [wordpress.org/plugins/suretriggers/](https://wordpress.org/plugins/suretriggers/) ✓ dans la section OttoKit Free (paragraphe « one click away »)
    - [g2.com/products/ottokit/reviews](https://www.g2.com/products/ottokit/reviews) ✓ dans la section Customer Reviews (« 4.5 stars on production usage »)
  - Pane FAQ « How does OttoKit compare to Make and n8n ? » ✓ ajouté à l'Accordion 0 (3 panes → 4)
  - Pane FAQ « How much does OttoKit cost ? » ✓ ajouté à l'Accordion 1 (2 panes → 3). Réponse explicite : free plan + Pro 9 $/mois + Business + Lifetime. PAA hint US matché.
  - JSON-LD FAQPage ✓ injecté en fin de contenu via `wp:html` block. Schema valide, **7 questions** (5 originales + Make/n8n + Cost), `mainEntity[]` complet avec answers alignées avec le contenu visible (rich result Google possible).
- **Bloc 3** :
  - Densité focus KW ✓ : premier paragraphe enrichi avec `<strong>OttoKit Free vs. Pro</strong>` exact (1 occurrence ajoutée, focus KW maintenant explicite en intro).
  - 2 H3 ajoutés sous OttoKit Pro (avant le H2 Price Difference) :
    - **Data retention** : retention étendue Pro, debugging post-mortem 10 jours vs 24 h en Free.
    - **Team collaboration** : team seats, workspace partagé, permission separation. Insight wpastra.com (#4 SERP US) qui manquait côté schoolsWP.
- **Total** : article passe de 37 134 à 44 308 octets (+ 7 174, +19 %). Balance Gutenberg OK (7 panes au total, 4 + 3 paneCount alignés), 0 lien cross-langue résiduel, FAQPage 7 questions visibles ET dans le schema.

## Historique des snapshots

| Date | Snapshot | Lang | Trigger | Décision |
| --- | --- | --- | --- | --- |
| 2026-05-19 | [2026-05-19/synthese.md](2026-05-19/synthese.md) | DE (draft) | Demande Michael, audit pré-publication | refonte-decidee → bloc-2-applique |
| 2026-05-19 | [2026-05-19-en/synthese.md](2026-05-19-en/synthese.md) | EN (draft) | Demande Michael, audit pré-publication suite à DE | refonte-decidee → bloc-3-applique (hero EN 2912562 + Ninja Table EN 2912655) |
| 2026-05-20 | [2026-05-20-fr/synthese.md](2026-05-20-fr/synthese.md) | FR (publié) | Demande Michael, audit de consolidation post-publication | refonte-decidee → bloc-3-applique (article pos 3 google.fr, blocs 1-3 en ligne, bloc 4 visuel en attente) |

## Ressources externes

- **Google Sheet volumes DE** : [schoolsWP - Volumes SEO - OttoKit Free vs Pro DE - 2026-05-19](https://docs.google.com/spreadsheets/d/17n_zD3x_-W3s2LlaFjWJHhE8IJ2IiZ-usbUPgW9d5Es/edit)
- **Google Sheet volumes EN** : [schoolsWP - Volumes SEO - OttoKit Free vs Pro EN - 2026-05-19](https://docs.google.com/spreadsheets/d/1W7mh8HYAQpjvb8gc8OSPOXFXNkPFSbjlYet39ZkpKi0/edit)
- **Google Sheet volumes FR** : [schoolsWP - Volumes SEO - OttoKit Free vs Pro FR - 2026-05-20](https://docs.google.com/spreadsheets/d/1iqf6lDW7aA6lhwv9oQiE_KzJHBcwpIf9whpMScmyog8/edit)
- **Backup contenu serveur DE** : `https://schoolswp.com/wp-content/uploads/audit-ottokit-de-20260519-154952.txt`
- **Backup contenu serveur EN (pré-corrections)** : `https://schoolswp.com/wp-content/uploads/audit-ottokit-en-PRE-BLOCS-20260519-200109.txt`
- **Backup contenu serveur EN (mid Bloc 1+3)** : `https://schoolswp.com/wp-content/uploads/audit-ottokit-en-MID-BLOC13-20260519-200957.txt`
- **Backup contenu serveur EN (post Blocs)** : `https://schoolswp.com/wp-content/uploads/audit-ottokit-en-POST-BLOCS-20260519-201105.txt`
- **Backup contenu serveur FR (pré-audit)** : `https://schoolswp.com/wp-content/uploads/audit-ottokit-fr-20260520-082921.txt`
- **Fichiers thruuu FR** : `thruuu_export_OttoKit Free vs Pro_2026-5-20.xlsx` + `Expor_audit_6a0d6f74f32ae5b75533efec.docx` (google.fr) - copiés dans `2026-05-20-fr/thruuu-raw/`
- **Fichier thruuu source DE** : `D:\TÉLÉCHARGEMENT\thruuu_export_OttoKit Free vs Pro_2026-5-19.xlsx` + le `(1).xlsx` (re-import DE, copié dans `2026-05-19/thruuu-raw/`)
- **Fichier thruuu EN** : `(2).xlsx` reçu de Michael (google.com US, Language=en, Country=US) -- copié dans `2026-05-19-en/thruuu-raw/serp-analysis-en-v2.xlsx`, synthèse dans `thruuu-en-summary.json`.

## Actions ouvertes (pré-publication DE)

### Bloc 1 - Bloquants ✓ APPLIQUÉ 2026-05-19 18:48

- [x] Remplacer les 4 en-dash (U+2013) du contenu DE
- [x] Reslugger les 3 liens internes cross-langue (vers FR) en équivalents DE ou retirer
- [x] Reslugger les `id` HTML des H2 en allemand

### Bloc 2 - Recommandés ✓ APPLIQUÉ 2026-05-19 19:03

- [x] Ajouter 3 liens externes (ottokit.com, wordpress.org/plugins/suretriggers/, g2.com)
- [x] Activer le FAQ schema (JSON-LD FAQPage injecté via `wp:html`, 6 questions DE)
- [x] **Hero featured image DE créée et set sur le post** (2026-05-19 21:18) - PNG 1920x1080 style FluentCRM, attachment 2912480, langue Polylang=de, alt/title/caption/description en allemand, métadonnées XP* / XMP / IPTC injectées. Source : `assets/featured-images/post-2898734/`
- [ ] Ajouter 2-3 captures écran dans le corps de l'article (dashboard OttoKit, KI-Agenten, pricing) - **manuel Michael via Gutenberg**
- [x] Vérifier que le Ninja Table id 2848098 est en allemand - non, FR. Solution : nouveau Ninja Table DE 2912298 créé et substitué dans le post

### Bloc 3 - Rank Math 61 → 80+

- [x] Renforcer densité focus KW dans premier paragraphe (2026-05-19 19:03)
- [ ] Enrichir sous-headings (H3) avec mots-clés - **suggestion** : à valider Michael via Gutenberg (densification fine du type « Aufgabenvolumen » → « Aufgabenvolumen OttoKit Free vs Pro » risque de sur-optimiser)
- [ ] Vérifier injection Person schema (mu-plugin schoolswp-person-schema) - **manuel Michael** : vérifier dans le rendu HTML après publication

### Bloc 4 - Post-publication

- [ ] Maillage cluster OttoKit DE depuis page produit + avis DE
- [ ] Re-audit GSC J+15, J+30, J+90 sur « ottokit », « ottokit pro » DE
- [ ] Mesurer clics affiliés cloak `/ottokit/`

## Re-audit programmé

**2026-07-19** (J+60 après publication estimée). Trigger anticipé possible si Rank Math weekly signale chute > 20 places ou si Google Search Console envoie une alerte indexation.

## Liens connexes

- Cluster OttoKit pilier (FR) : `/ottokit-avis-automatisation-wordpress/` (pos 9.0 sur « ottokit » FR, 110 impressions/90j)
- Page produit/stack (FR) : `/automatisations-wordpress/ottokit/` (pos 8.7)
- Comparatif EN (à monitorer) : `/en/suretriggers-ottokit-vs-zapier/` (pos 1.1 sur « suretriggers vs zapier » mais 0 clic - marque morte)
- Cloak affiliation : `/ottokit/` → destination cible avec ref schoolsWP, code promo `schoolsWP20`
