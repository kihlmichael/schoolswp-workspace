---
slug: ottokit-free-vs-pro
url: https://schoolswp.com/ottokit-gratuit-vs-pro/
lang: fr
post_id: 2592422
date_snapshot: 2026-05-20
trigger: Demande Michael (audit de consolidation post-publication)
status: bloc-3-applique
---

# Audit OttoKit Gratuit vs Pro (FR) - snapshot 2026-05-20

## 1. Contexte et déclencheur

- Article `2592422` **publié** le 2026-05-08, modifié le 2026-05-16. Slug `ottokit-gratuit-vs-pro`.
- Article le plus mature de la triade : la DE (`2898734`) et l'EN (`2865102`) en sont des traductions auditées et corrigées les 2026-05-19 / 2026-05-20.
- Demande Michael : audit de la version FR avec analyse SERP fournie (thruuu xlsx `2026-5-20` + rapport d'audit on-page docx `Expor_audit_6a0d6f74f32ae5b75533efec.docx`).
- Différence clé avec DE/EN : l'article FR est **déjà en ligne et déjà classé** (position 3 google.fr). L'audit est une **consolidation**, pas une pré-publication ni un sauvetage.

## 2. Données collectées

| Source | Périmètre | Fichier |
| --- | --- | --- |
| Novamira REST (execute-php) | post_content + meta complets FR | backup serveur `/wp-content/uploads/audit-ottokit-fr-20260520-082921.txt` (38 755 octets) |
| thruuu export SERP FR | google.fr, Language=fr, Country=FR | `thruuu-raw/serp-analysis-fr.xlsx` |
| thruuu rapport d'audit on-page | audit page schoolsWP vs SERP | `thruuu-raw/thruuu-audit-report-fr.docx` |
| thruuu synthèse exploitable | top 17 + Page Rank + word/image counts + questions | `thruuu-fr-summary.json` |
| DataForSEO Labs - keyword overview FR | 8 keywords (2 avec données) | `dataforseo-volume.json` |
| DataForSEO Labs - search intent FR | 6 keywords | `dataforseo-search-intent.json` |
| DataForSEO Labs - suggestions FR seed ottokit | 3 suggestions retournées | `dataforseo-keyword-suggestions.json` |
| GSC schoolswp.com 90j (2026-02-19 → 2026-05-20) | filtre page contains ottokit-gratuit-vs-pro | `gsc-90d.json` |
| CSV volumes pour Drive | 10 keywords cluster FR | `dataforseo-google-sheet.csv` |

## 3. État de l'article FR actuel

| Critère | Valeur | Commentaire |
| --- | --- | --- |
| Statut | publié | En ligne depuis 2026-05-08 |
| Modified | 2026-05-16 | |
| Slug | `ottokit-gratuit-vs-pro` | Propre, localisé FR ✓ |
| Word count | 2 101 mots (thruuu) | Au-dessus de la moyenne SERP (1 911) ✓ |
| H2 / IDs | 7 H2, IDs déjà en slug FR | ✓ Aucune correction nécessaire |
| Images | ~12 (thruuu, dont logo + icônes) ; ~2-3 images éditoriales réelles dans le corps | **ÉCART** : moyenne articles concurrents 15-31 |
| TOC Kadence | oui | OK |
| FAQ Kadence accordion | oui (2 accordions, 5 panes) | OK structurellement |
| Ninja Table | oui (id 2848098, FR natif) | ✓ Aucun swap nécessaire |
| Kadence CTA | 2 | OK |
| Liens internes cross-langue | 0 | ✓ Propre |
| Liens externes | **0** | **ÉCART** : aucune source primaire référencée |
| Em-dash (U+2014) | 0 | ✓ |
| En-dash (U+2013) | **1** | **VIOLATION** branding (dans l'alt du logo) |
| JSON-LD FAQPage | **non** | **ÉCART** : `Has On Page FAQ: False`, schema sans FAQPage |
| Schema types | Place, EducationalOrganization, Organization, WebSite, ImageObject | Article et FAQPage absents |
| Rank Math SEO score | 71/100 | Sous le seuil schoolsWP (≥ 80) |
| Featured image | 2852045 (ancien hero) | Pas le style éditorial FluentCRM validé sur DE/EN |

## 4. SEO actuel et GSC (90j FR)

L'article est publié depuis 12 jours seulement : les données GSC sont fines mais déjà réelles.

- « ottokit » : 20 impressions, 0 clic, position **6,2**.
- « ottokit pro » : 2 impressions, 0 clic, position 4,0.
- thruuu confirme par ailleurs la position **3** sur la requête exacte « OttoKit Free vs Pro » (google.fr).

**Lecture** : pour un article de 12 jours, une position 6,2 sur le seed « ottokit » (110/mois) est une base de départ correcte. 0 clic est normal à position 6 avec 20 impressions cumulées. L'objectif de consolidation : passer de 6,2 à top 3 sur « ottokit » et tenir le top 3 sur le longtail comparatif.

## 5. SERP FR analysée (thruuu google.fr)

Top organique :

1. Video pack (3 YouTube : OttoKit Review 2025, OttoKit vs n8n, WordPress Automations)
2. ottokit.com (PR 41, 1 666 mots, 140 images)
3. **schoolswp.com/ottokit-gratuit-vs-pro/** (PR 28, 2 101 mots, 12 images)
4. wpastra.com/review/ottokit-review/ (PR 49, 1 969 mots)
5. wordpress.org/plugins/suretriggers/ (PR 76, 4 043 mots)
6. crocoblock.com (PR 49, 1 542 mots)
7. newpulselabs.com (PR 29, 2 006 mots)
8. ottokit.com/features/ (PR 41)
9. wpwebzon.com (PR 6, 1 881 mots)
10. blogkraft.com (PR 13, 1 426 mots)
12-14. ciroapp.com, getapp.com, defenderbot.tech - **les 3 ont le schema FAQPage**

Observations critiques :

- **Aucun concurrent natif « Free vs Pro » spécifique** dans le top 17. L'angle comparatif de schoolsWP reste exclusif (idem DE et EN).
- **Video pack en position 1** : un Short YouTube FR sur le même angle gratterait de la visibilité.
- **3 concurrents ont le schema FAQPage** (pos 12, 13, 14). schoolsWP a une FAQ visuelle mais pas le schema → on rate un signal et le rich-result potentiel.
- wpwebzon (PR 6) et blogkraft (PR 13) rankent en pos 9-10 : l'autorité de domaine n'est pas le facteur bloquant, la pertinence et la structuration priment.
- L'article schoolsWP est déjà mieux placé (pos 3) que des concurrents plus anciens et plus autoritaires (wpastra PR 49, crocoblock PR 49). Bon signal de pertinence.

### 5b. Rapport d'audit on-page thruuu (docx)

| Critère | Verdict thruuu | Lecture |
| --- | --- | --- |
| Word count | success | 2 101 mots, dans la fourchette |
| **Image count** | **error** | 12 vs 35 de moyenne SERP, « ajouter ~13 images » |
| Page Rank | success | 28, dans la fourchette concurrents |
| Title | success | longueur OK, pixel width OK, contient le focus KW |
| Description | success | 126 caractères, OK |
| Questions dans les titres | success | 3 questions (moyenne SERP = 1) |
| Angle éditorial | success | angle comparatif unique |
| Titres communs SERP | error | aucun titre commun (artefact partiel : SERP dominée par des reviews EN) |
| Termes fréquents | error | artefact : analyse de termes basée sur la SERP majoritairement EN |

> **Nuance importante** : la moyenne « 35 images » est gonflée par les pages vitrine ottokit.com (60-140 images). Les vrais articles concurrents sont à 15-31 (wpastra 31, crocoblock 15, newpulselabs 18) ou même moins (wpwebzon 6, blogkraft 6). Cible réaliste schoolsWP : **18-25 images éditoriales** (captures dashboard, agents IA, pricing), pas 35.

## 6. Volumes et tendances FR (DataForSEO)

| Keyword | Volume FR | KD | Intent | Trend | Note |
| --- | ---: | ---: | --- | --- | --- |
| ottokit | 110/mois | 16 | transactional | +29 % trim. | Seed principal |
| suretriggers | 40/mois | 15 | informational | **-89 % an** | Marque morte |
| ottokit gratuit vs pro | n/a | n/a | commercial (0,79) | n/a | Focus KW, pas de volume mesurable |
| ottokit prix | n/a | n/a | commercial (0,80) | n/a | Longtail commercial |
| ottokit avis | n/a | n/a | informational (0,71) | n/a | Cluster avis |

**Comparaison FR / DE / US** :

| Métrique | FR | DE | US |
| --- | ---: | ---: | ---: |
| Volume seed « ottokit » | 110 | 110 | 390 |
| KD seed | 16 | 11 | 16 |
| Concurrent natif « Free vs Pro » top 10 | 0 | 0 | 0 |

Le marché FR pèse comme le DE (~110/mois), 3,5× plus petit que les US. Le longtail FR mesuré est quasi inexistant : la stratégie est de **dominer le seed « ottokit »** et de capter le longtail comparatif non mesuré via la profondeur de contenu et le schema.

## 7. Insights critiques (5)

1. **Article déjà performant (pos 3) et très récent (12 jours)**. L'audit consolide un actif qui monte, il ne corrige pas un échec. L'effort doit être proportionné : corrections ciblées, pas de refonte lourde.

2. **L'angle « Free vs Pro » reste exclusif** sur la SERP FR : aucun concurrent ne le traite frontalement. C'est le moat de l'article, à ne pas diluer.

3. **3 fuites concrètes, toutes corrigeables rapidement** : 1 en-dash, 0 lien externe, 0 schema FAQPage. Les deux dernières sont exactement les manques corrigés sur DE et EN.

4. **L'écart d'images est le seul chantier lourd** : 12 (dont icônes) contre 15-31 chez les vrais concurrents articles. C'est le poste qui demande de la production réelle (captures), partiellement manuel.

5. **Rank Math 71** : sous le seuil. La densification du focus KW + le schema FAQPage + les liens externes devraient suffire à passer 80, sans sur-optimiser.

## 8. Décision

> **REFONTE LÉGÈRE DE CONSOLIDATION** : Blocs 1, 2 et 3 appliqués 2026-05-20 10:52 (`bloc-3-applique`). Bloc 4 (visuel) en attente.

Mêmes blocs que DE/EN mais encore plus légers (l'article FR est l'original, déjà propre sur les IDs, les liens cross-langue et la table). Coût estimé blocs 1-3 : **20-30 min**. Le bloc visuel (images) est un chantier séparé, partiellement manuel.

**Pourquoi agir maintenant** : l'article est jeune et grimpe. Consolider tôt (schema, liens, densité) maximise la vitesse d'ascension avant que la concurrence FR ne se réveille.

**Pourquoi ne pas tout refondre** : l'article est déjà en position 3. Une refonte lourde risquerait de casser ce qui marche. On corrige les fuites, on ajoute le schema, on enrichit visuellement.

## 9. Plan d'action

### Bloc 1 - Correction obligatoire ✓ APPLIQUÉ 2026-05-20 08:51

1. [x] Remplacer le 1 en-dash (U+2013) présent dans l'attribut `alt` du logo OttoKit par « : » (en-dash 1→0).

### Bloc 2 - Enrichissements ✓ APPLIQUÉ 2026-05-20 10:52

1. [x] JSON-LD FAQPage injecté en fin de contenu via `wp:html` : 7 questions FR (5 existantes + « Combien coûte OttoKit ? » + « Comment OttoKit se compare-t-il à Make et n8n ? »).
2. [x] 3 liens externes ajoutés : `ottokit.com/wordpress/` (section OttoKit Gratuit), `wordpress.org/plugins/suretriggers/` (section OttoKit Gratuit), `g2.com/products/ottokit/reviews` (section Avis clients).
3. [x] Pane FAQ « Comment OttoKit se compare-t-il à Make et n8n ? » ajoutée à l'Accordion 0 (3→4 panes) + pane « Combien coûte OttoKit ? » à l'Accordion 1 (2→3 panes). 7 panes au total, toutes alignées avec le schema.

### Bloc 3 - Rank Math 71 → 80+ ✓ APPLIQUÉ 2026-05-20 08:51

1. [x] Densité du focus KW renforcée dans le premier paragraphe (`<strong>OttoKit Gratuit vs Pro</strong>` exact en intro).
2. [x] Title et meta description : déjà jugés bons par thruuu, aucune retouche.

> **Note Rank Math** : le score `rank_math_seo_score` reste à 71 après le push direct DB. Il se recalcule à l'ouverture suivante dans Gutenberg (clic « Update ») ou via l'endpoint `rankmath/v1/updateMeta`. Le contenu coche désormais les critères ≥ 80 (focus KW en intro+strong+H2, 3 liens externes, JSON-LD FAQPage, 7 panes accordion, 2 101 mots).
>
> **Article publié** : ces modifications sont **en ligne immédiatement** sur schoolswp.com (contrairement aux DE/EN qui étaient en brouillon/programmé). Voir Bloc 5 pour la re-soumission Instant Indexing.

### Bloc 4 - Enrichissement visuel ✓ APPLIQUÉ 2026-05-20

1. [x] **9 captures réelles** du compte OttoKit de Michael intégrées dans le corps ✓ APPLIQUÉ 2026-05-20 11:18. Captures fournies dans `content/inspirations/ottokit/`, optimisées en WebP (max 1600px, 21-44 KB) dans `assets/article-images/ottokit-gratuit-vs-pro/`, métadonnées SEO complètes (EXIF + alt/titre/légende/description médiathèque), uploadées et insérées via `wp:image` après le paragraphe pertinent de chaque section. Attachments **2914187 à 2914195**. L'article passe de ~3 à ~12 images éditoriales (dans la fourchette concurrents). Captures = compte réel : E-E-A-T fort, rendu unique.
2. [x] Nouveau hero featured image au format éditorial FluentCRM ✓ APPLIQUÉ 2026-05-20 11:05. Attachment **2913947** (`hero-ottokit-gratuit-vs-pro-fr.png`, 1920x1080, 116 KB), Polylang=fr, métadonnées SEO complètes (XP* / XMP / IPTC / EXIF + alt/titre/légende/description médiathèque). Défini comme image à la une (remplace l'ancien 2852045). Cohérent avec les heros DE (2912480) et EN (2912562). Source : `assets/featured-images/post-2592422/slide-00-hero-fr.html`.

Mapping des 9 captures intégrées :

| Attachment | Image | Section |
| --- | --- | --- |
| 2914187 | Tableau de bord OttoKit | Résumé de la comparaison |
| 2914188 | Bibliothèque de recettes | Fonctionnalités (intro) |
| 2914189 | Éditeur de workflow visuel + agent IA | H3 Agents IA et automatisation multi-étapes |
| 2914190 | Bibliothèque d'intégrations | H3 Capacités pour besoins simples |
| 2914191 | Détail du plan gratuit | OttoKit Gratuit (intro) |
| 2914192 | Panneau Usage & Limit | H3 Plafonds techniques |
| 2914193 | Ajout d'une action | H3 Logique conditionnelle et webhooks |
| 2914194 | Historique d'exécution | H3 Rétention des données |
| 2914195 | Page tarifs (plans payants) | H2 Différences de prix |

### Bloc 5 - Post-update

1. Re-soumettre l'URL via Instant Indexing après modification.
2. Surveiller GSC FR à J+15 et J+30 sur « ottokit », « ottokit pro », « ottokit avis ».
3. Mesurer les clics affiliés cloak `/ottokit/`.

## 10. Métriques de suivi (prochain snapshot)

- Position GSC « ottokit » FR (objectif : 6,2 → top 3 sous 30-45j).
- Position sur le longtail comparatif (maintien top 3).
- Apparition d'un FAQ rich result (oui/non, via URL inspect).
- Rank Math score (objectif ≥ 80 après blocs 1-3).
- Clics et impressions cumulés (baseline : 22 impressions / 0 clic).
- Clics affiliés OttoKit cloak `/ottokit/`.

Re-audit recommandé : **2026-06-20** (J+30) ou plus tôt si Rank Math weekly signale une chute.

## Annexes (fichiers du snapshot)

- [thruuu-fr-summary.json](thruuu-fr-summary.json) - synthèse exploitable de la SERP FR
- [thruuu-raw/serp-analysis-fr.xlsx](thruuu-raw/serp-analysis-fr.xlsx) - export brut thruuu google.fr
- [thruuu-raw/thruuu-audit-report-fr.docx](thruuu-raw/thruuu-audit-report-fr.docx) - rapport d'audit on-page thruuu
- [dataforseo-volume.json](dataforseo-volume.json)
- [dataforseo-search-intent.json](dataforseo-search-intent.json)
- [dataforseo-keyword-suggestions.json](dataforseo-keyword-suggestions.json)
- [dataforseo-google-sheet.csv](dataforseo-google-sheet.csv) - source du Sheet Drive FR
- [gsc-90d.json](gsc-90d.json)
- Backup serveur : `https://schoolswp.com/wp-content/uploads/audit-ottokit-fr-20260520-082921.txt`
