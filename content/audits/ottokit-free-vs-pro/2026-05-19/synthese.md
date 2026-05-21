---
slug: ottokit-free-vs-pro
url: https://schoolswp.com/de/?p=2898734
lang: de
post_id: 2898734
date_snapshot: 2026-05-19
trigger: Demande Michael (audit pré-publication brouillon DE)
status: refonte-decidee
---

# Audit OttoKit Free vs. Pro (DE) - snapshot 2026-05-19

## 1. Contexte et déclencheur

- Article 2898734 en **brouillon allemand** (post_modified 2026-05-19 17:35:33).
- Demande explicite Michael : audit avant publication, focus keyword « OttoKit Free vs Pro ».
- Fichier SERP `thruuu_export_OttoKit Free vs Pro_2026-5-19.xlsx` fourni dans `D:\TÉLÉCHARGEMENT` (recherche US/EN, pas DE - voir limitation §2).
- Version FR `2592422` /ottokit-gratuit-vs-pro/ déjà **publiée** (modified 2026-05-16) : sert de référence cluster.
- Version EN `2865102` également **brouillon** (modified 2026-05-08).

## 2. Données collectées

| Source | Périmètre | Fichier |
| --- | --- | --- |
| Novamira REST (execute-php) | post_content + meta complets DE | backup serveur `/wp-content/uploads/audit-ottokit-de-20260519-154952.txt` |
| DataForSEO Labs - keyword overview DE | 7 keywords cibles | `dataforseo-volume.json` |
| DataForSEO SERP organic DE depth 20 | top 20 + AIO + related | `dataforseo-serp-de.json` |
| DataForSEO suggestions DE seed OttoKit | 5 suggestions retournées | `dataforseo-keyword-suggestions.json` |
| DataForSEO search intent DE | 5 keywords | `dataforseo-search-intent.json` |
| DataForSEO historical DE (24 mois) | ottokit, ottokit pro, suretriggers | inclus dans `dataforseo-volume.json` |
| GSC schoolswp.com 90j (2026-02-18 → 2026-05-19) | filtre page contains ottokit + query contains ottokit | `gsc-90d.json` |
| GSC URL inspect | /ottokit-gratuit-vs-pro/ FR (référence) | `gsc-url-inspect.json` |
| thruuu export brut | SERP DE google.de « OttoKit Free vs Pro » | `thruuu-raw/serp-analysis.xlsx` |
| thruuu DE synthèse | top 17 + concurrents DE + questions DE | `thruuu-de-summary.json` |
| CSV volumes pour Drive | 10 keywords cluster | `dataforseo-google-sheet.csv` |

> **Correction 2026-05-19 (re-import)** : le fichier thruuu initial provenait d'une recherche Google US/EN ; remplacé par le bon export DE (`google.de`, `hl=de`, `gl=DE`). Les insights SERP §5 ci-dessous reflètent désormais la SERP allemande native.

## 3. État de l'article DE actuel

| Critère | Valeur | Commentaire |
| --- | --- | --- |
| Statut | brouillon | Non publié, non indexable |
| Modified | 2026-05-19 17:35 | Création très récente |
| Word count | 1 739 mots | Court vs concurrents EN (1 542 - 2 006 mots) |
| H2 / H3 | 8 / 12 | Hiérarchie propre, pas de saut de niveau |
| Images | 1 (héro SVG) | Très faible. Concurrents : 15 - 140 images |
| TOC Kadence | oui | H2-only, replié, smooth scroll |
| FAQ Kadence accordion | oui (5 Q&A) | Mais **pas de FAQ schema** (Rank Math FAQ block absent) |
| Tableau Ninja | oui (id 2848098) | À vérifier que le contenu est en allemand |
| CTA Kadence | 2 | Code promo « schoolsWP20 » présent |
| Liens internes natifs DE | 1 (`/de/artikel/`) | Très faible |
| Liens internes cross-langue FR | 3 | **VIOLATION** règle [[feedback_links_same_language]] |
| Liens externes | 0 | Aucune source primaire référencée |
| Liens cloak affilié | 3 (`/ottokit/`) | OK, mu-plugin schoolswp-affiliate-cloaks |
| Em-dash (U+2014) | 0 | OK ✓ |
| En-dash (U+2013) | 4 | **VIOLATION** branding (à remplacer par « : » ou « . ») |
| Rank Math SEO score | 61/100 | Sous le seuil schoolsWP (≥ 80) |
| IDs H2 | tous en slug FR | À reslugger en allemand |

Détails composants et liste FAQ : voir [article-current-snapshot.md](article-current-snapshot.md).

## 4. SEO actuel et cluster OttoKit GSC (90j)

Sur le cluster OttoKit complet (4 pages indexées sur schoolswp.com) :

- **0 clic** sur 90 jours malgré 182 impressions sur « ottokit » seul.
- Cause probable : AI Overview + ottokit.com qui monopolisent les clics, et marché DE encore très faible.
- `/ottokit-gratuit-vs-pro/` FR (homologue) classé **pos 6.2** sur « ottokit » avec 20 impressions : preuve que le format Free vs Pro a sa place dans le cluster.
- `/en/suretriggers-ottokit-vs-zapier/` EN classé **pos 1.1** sur « suretriggers vs zapier » mais 0 clic : confirme l'effondrement de la marque SureTriggers (-89 % yearly volume DE).

URL inspect FR (référence) : PASS, indexée, crawled mobile, schema Breadcrumbs uniquement (pas de FAQPage malgré accordeon Kadence).

## 5. SERP DE analysée (DataForSEO + thruuu DE)

Top 10 confirmé par les **deux sources** (DataForSEO depth 20 + thruuu google.de) :

| Rank | Domaine | URL | Langue |
| ---: | --- | --- | :---: |
| 1 | ottokit.com | `/` (home officiel) | EN |
| 2 | wordpress.org | `/plugins/suretriggers/` | EN |
| 3 | reddit.com | thread `seeking_opinions_on_ottokit` | EN |
| 4 | wpastra.com | `/review/ottokit-review/` | EN |
| 5 | ottokit.com | `/wordpress/` | EN |
| 6 | youtube.com | vidéo (Robert Leitinger comparison) | - |
| 7 | crocoblock.com | `/blog/ottokit-wordpress-plugin-review/` | EN |
| 8 | newpulselabs.com | `/ottokit-review/` | EN |
| 9 | **bit-integrations.com** | `/de/best-ottokit-alternative-in-wordpress/` | **DE** |
| 10 | g2.com | `/products/ottokit/reviews` | EN |

Et plus profond (révélé par thruuu DE) :

| Rank | Domaine | URL | Langue | Pourquoi c'est important |
| ---: | --- | --- | :---: | --- |
| 13 | **robert-leitinger.com** | `/ottokit/` | **DE** | « OttoKit im Test - Wie gut ist die n8n / Make Alternative wirklich? » - 2e concurrent DE natif émergent, déjà présent en vidéo SERP, angle OttoKit vs n8n / Make non couvert par schoolsWP |
| 16 | ottokit.com | `/suretriggers-vs-wp-fusion-comparison/` | EN | Auto-référence : OttoKit publie son propre comparatif vs WP Fusion |

Observations critiques (mises à jour) :

- **AI Overview discordant** : DataForSEO dit oui (asynchrone pos 1), thruuu dit non. → **Vérifier en live** avant publication, l'AIO peut être A/B testé par Google.
- SERP DE **2 résultats DE natifs** (pos 9 + pos 13) au lieu d'1. Le marché DE est moins vierge que la première lecture le laissait penser, **mais le top 3-8 reste 100 % EN** - opportunité maintenue d'occuper la position 3-5 DE.
- **Robert Leitinger est un concurrent DE direct à monitorer** : blogueur + YouTubeur germanophone, angle OttoKit vs n8n / Make. Format vidéo + article = signal E-E-A-T fort.
- Aucun comparatif **Free vs Pro spécifique** dans le top 17 : angle exclusif maintenu pour schoolsWP DE.
- Pas de FAQ schema dans le top 10 DE. Activer le FAQPage côté DE = gain de visibilité maintenu.
- Format dominant top 10 : reviews long-form 1 500 - 2 000 mots EN + 1 vidéo + 1 forum Reddit.

### 5b. Questions DE détectées (thruuu, Frequent Questions)

Questions réelles posées dans les pages du SERP DE - **angle E-E-A-T à intégrer dans la FAQ** :

| Question DE | Source | Note pour intégration |
| --- | --- | --- |
| Was ist OttoKit ? | 4 pages | Question récurrente forte. À ajouter dans la FAQ DE. |
| Benötige ich Programmierkenntnisse für die Nutzung ? | bit-integrations | Pertinente pour cible débutante DE. |
| OttoKit vs Make vs n8n - Was ist der Unterschied ? | robert-leitinger | **Angle non couvert par schoolsWP** - opportunité d'ajout dans la FAQ. |
| Wo kann ich Unterstützung erhalten ? | 2 pages | Support / réactivité - argument Pro. |
| Haben Sie ein Partner-/Wiederverkäuferprogramm ? | bit-integrations | À noter (affiliation / agences). |

Les 5 questions actuelles de l'accordeon DE schoolsWP sont **bonnes** mais peuvent gagner 1-2 questions issues du SERP DE (au minimum « OttoKit vs Make vs n8n ? » qui adresse la vraie comparaison qu'attendent les utilisateurs allemands).

### 5c. Related searches Google DE

`ZipWP free plan` · `Ottokit affiliate` · `Uncanny Automator Pro` · `OttoKit integrations` · `Otto kit` · `Spectra Pro` · `SureRank Pro` · `Integrately`

Aucune related search « Free vs Pro » directement - confirme que l'angle est explorable mais ne reçoit pas encore beaucoup de recherches en DE.

## 6. Volumes et tendances DE (DataForSEO 24 mois)

| Keyword | Volume actuel | Trend mensuel | Trend annuel | Note |
| --- | ---: | ---: | ---: | --- |
| **ottokit** | 110/mois | +57 % | n/a (récent) | seed en croissance, KD 11 (facile) |
| ottokit pro | 10/mois | 0 % | 0 % | Stable mais volume marginal |
| ottokit pricing | 10/mois | 0 % | n/a | Stable |
| ottokit login | 10/mois | 0 % | n/a | Navigational (marque) |
| ottokit integrations | 10/mois | -100 % | n/a | Volume éphémère |
| suretriggers | 50/mois | -50 % | **-89 %** | Marque legacy morte (pic 320/mois en avril 2025) |
| OttoKit Free vs Pro | < 10/mois | n/a | n/a | Absent DB DataForSEO DE |
| OttoKit erfahrungen | < 10/mois | n/a | n/a | Absent DB |
| OttoKit kostenlos | < 10/mois | n/a | n/a | Absent DB |
| OttoKit review | < 10/mois | n/a | n/a | Absent DB |

**Lecture stratégique** : le marché DE est **en croissance rapide** sur le seed (« ottokit » +57 % mensuel) mais le volume des longs traînes Free/Pro/erfahrungen/kostenlos est encore non significatif. **Pari à 6-12 mois**, pas un quick win.

## 7. Insights critiques (5)

1. **Cible keyword DE trop fine pour briser GSC seul.** Le pari de l'article réside dans la **capture du cluster ottokit complet** côté DE (110/mois sur le seed) via maillage interne et structuration cocoon, pas dans le volume direct de « OttoKit Free vs Pro » (< 10/mois).

2. **Concurrence DE faible mais existante.** 2 résultats DE natifs dans le top 13 (bit-integrations.com/de/ pos 9, robert-leitinger.com pos 13) - et 0 dans le top 8. Toute publication DE propre entrera vite dans le top 5 si E-E-A-T + schema corrects. **Ne pas attendre, mais surveiller robert-leitinger.com** qui monte (vidéo + blog DE, angle n8n / Make).

3. **Article actuel a une bonne ossature mais trois fuites de qualité bloquantes** :
   - 3 liens internes cross-langue vers slugs FR (violation [[feedback_links_same_language]]).
   - 4 en-dash (U+2013) interdits par branding.
   - Score Rank Math 61/100, sous le seuil schoolsWP (≥ 80).

4. **Schema FAQPage absent malgré accordeon Kadence à 5 Q&A**. Activer le Rank Math FAQ block (ou ajouter `<script type="application/ld+json">` FAQPage manuel) capte un riche résultat **inexistant chez tous les concurrents top 10**.

5. **Marque SureTriggers est morte en DE (-89 % YoY).** Ne **pas** introduire « SureTriggers » dans le titre, H1 ou meta. Mentionner une seule fois en H3 « ehemals SureTriggers » pour capter le legacy traffic (modeste). Le concurrent #9 bit-integrations.com l'utilise dans son titre = pari sur le legacy.

6. **Angle « OttoKit vs n8n / Make » manquant côté schoolsWP DE.** Robert Leitinger occupe déjà ce terrain en DE (article + vidéo). Si schoolsWP veut élargir le cluster DE, c'est l'angle suivant à ouvrir (post publication de Free vs Pro). À ne **pas** mélanger avec ce comparatif Free vs Pro.

## 8. Décision

> **REFONTE LÉGÈRE PRÉ-PUBLICATION** (`refonte-decidee`).

Pas de réécriture totale. L'ossature, le ton et la structure sont valides pour le marché DE.

**Pourquoi pas publier immédiatement** : le Rank Math score à 61 et les 3 liens cross-langue sont des fuites mesurables qui vont coûter de l'autorité sur un cluster en démarrage. Coût correctif : 30-45 min, pas une refonte.

**Pourquoi pas attendre plus de volume** : la SERP DE est vide. Premier arrivé prend le top 3 sur le seed via maillage.

## 9. Plan d'action pré-publication

Effort estimé total : **45-60 min** dont 20 min côté Michael (Rank Math + Gutenberg), reste côté Claude via Novamira.

### Bloc 1 - Corrections obligatoires (bloque la publication)

1. **Remplacer les 4 en-dash (U+2013) par « : » ou « - » ou « . ».** Grep + remplacement Novamira `wp_update_post` direct (sans `wp_unslash` pour préserver Kadence). [[feedback_wp_update_post_unslash_kadence]]
2. **Reslugger les liens internes** :
   - `/automatisations-wordpress/` → vérifier si hub DE `/de/wordpress-automatisierungen/` (ou similaire) existe. Si non, retirer le lien plutôt qu'envoyer vers FR.
   - `/ottokit-avis-automatisation-wordpress/` → vérifier slug avis OttoKit DE. Si pas publié, retirer.
   - `/suretriggers-vs-zapier/` → idem, vérifier équivalent DE ou retirer (la marque est morte de toute façon).
3. **Reslugger les `id` des H2** en allemand (cohérence ancres SEO interne).

### Bloc 2 - Enrichissements forts (recommandés avant publication)

1. **Ajouter 3 liens externes** vers sources primaires :
   - ottokit.com (page tarif officielle, target=\_blank rel=noopener)
   - wordpress.org/plugins/suretriggers/ (avis 4.9/117)
   - Une review tierce DE-friendly (g2.com/products/ottokit ou capterra.com)
2. **Activer le Rank Math FAQ schema block** ou injecter le JSON-LD FAQPage manuellement. 5 questions déjà rédigées dans l'accordeon, **ajouter 1 à 2 questions issues du SERP DE** :
   - « Was unterscheidet OttoKit von n8n oder Make ? » (capte l'angle de robert-leitinger.com)
   - « Benötige ich Programmierkenntnisse für OttoKit ? » (question DE récurrente)
3. **Ajouter 2-3 captures écran** (dashboard OttoKit, écran KI-Agenten, tableau pricing) - aujourd'hui 1 seule image héro SVG.
4. **Vérifier Ninja Table 2848098** : est-il bien en allemand ? Si copié du FR, créer une variante DE (cf. [[reference_ninja_tables_rest]] CSV multipart).

### Bloc 3 - Optimisation Rank Math 61 → 80+

1. **Densité focus KW** : « OttoKit Free vs. Pro » apparaît dans H1 et meta mais peut être renforcé dans le premier paragraphe.
2. **Méta title** : actuel « OttoKit Free vs. Pro: Welches bringt dir den größten Nutzen? » - garder mais raccourcir si > 60 chars rendu (actuel = 62 chars, limite OK).
3. **Sous-headings avec mots-clés** : enrichir « Aufgabenvolumen » → « Aufgabenvolumen OttoKit Free vs Pro » par exemple.
4. **Ajouter un slot Person schema** (auteur Michael KIHL) si pas déjà ajouté par le mu-plugin schoolswp-person-schema [[project_person_schema_enrichment]].

### Bloc 4 - Cluster (post-publication)

1. Mettre à jour le maillage interne du cluster OttoKit DE : la page produit `/de/wordpress-automatisierungen/ottokit/` (si elle existe) et le futur avis OttoKit DE doivent renvoyer vers ce comparatif.
2. **Surveiller GSC** à J+15, J+30, J+90 : positions sur « ottokit pro », « ottokit kostenlos », « ottokit erfahrungen » + impressions sur « ottokit » DE.

## 10. Métriques de suivi (prochain snapshot)

- Statut indexation GSC (PASS attendu sous 48h après publication).
- Position GSC sur « ottokit » et « ottokit pro » DE (objectif : top 10 sous 30 jours, top 5 sous 60 jours).
- Impressions cluster OttoKit DE (baseline : 0 sur 90j actuels).
- Clics affiliés via cloak `/ottokit/` (à mesurer côté FluentAffiliate ou tracker dédié).
- Featured snippet / FAQ rich result détecté (oui/non, via URL inspect).
- Évolution volume `ottokit` DE (110/mois actuel, +57 % mensuel → 170-200/mois projeté Q3 2026).

Re-audit recommandé : **2026-07-19** (J+60) ou plus tôt si Rank Math weekly signale une chute.

## Annexes (fichiers du snapshot)

- [article-current-snapshot.md](article-current-snapshot.md) - inventaire structurel détaillé
- [dataforseo-volume.json](dataforseo-volume.json)
- [dataforseo-serp-de.json](dataforseo-serp-de.json)
- [dataforseo-search-intent.json](dataforseo-search-intent.json)
- [dataforseo-keyword-suggestions.json](dataforseo-keyword-suggestions.json)
- [dataforseo-google-sheet.csv](dataforseo-google-sheet.csv) - source du Sheet Drive
- [gsc-90d.json](gsc-90d.json)
- [gsc-url-inspect.json](gsc-url-inspect.json)
- [thruuu-de-summary.json](thruuu-de-summary.json) - synthèse SERP DE native (top 17 + concurrents DE + questions DE)
- [thruuu-raw/serp-analysis.xlsx](thruuu-raw/serp-analysis.xlsx) - 30 onglets, SERP DE google.de (remplacé le 2026-05-19 après import initial US/EN)
- Backup serveur : `https://schoolswp.com/wp-content/uploads/audit-ottokit-de-20260519-154952.txt`

Google Sheet : « schoolsWP - Volumes SEO - OttoKit Free vs Pro DE - 2026-05-19 » sur Drive Michael (lien dans README.md de l'article).
