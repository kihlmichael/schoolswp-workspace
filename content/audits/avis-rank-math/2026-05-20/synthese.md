---
slug: avis-rank-math
url: https://schoolswp.com/?p=2289943
post_id: 2289943
date_snapshot: 2026-05-20
trigger: Demande Michael (audit pré-publication)
status: refonte-decidee
---

# Audit pré-publication — Avis Rank Math

## 1. Contexte et déclencheur

Article en **brouillon** (post 2289943), audité avant publication sur la requête **« avis rank math »**.
Objectif : vérifier qu'il est prêt à publier et identifier ce qui le bloque. Verdict court : **non, réécriture nécessaire**. Le brouillon est un premier jet généré par IA, dense en remplissage et léger en preuves. Il a une bonne ossature de plan mais ne tient pas encore le rôle d'un « avis » crédible et convertissant.

## 2. Données collectées

| Source | Détail | Date |
| --- | --- | --- |
| Contenu article | `post_content` via Novamira (brouillon non scrapable par thruuu) | 2026-05-20 |
| SERP thruuu | `thruuu-raw/serp-analysis.xlsx` - top 20 FR, headings, questions, champ sémantique | 2026-05-20 |
| Volumes | DataForSEO Labs keyword_overview - `dataforseo-volume.json` | 2026-05-20 |
| Champ sémantique | DataForSEO keyword_suggestions (100 requêtes) - `dataforseo-google-sheet.csv` + [Google Sheet](https://docs.google.com/spreadsheets/d/1lliIN9uoVNAJVqcRVkvvGsG9iZpsazlV0mbMVP5fYrw/edit) | 2026-05-20 |
| Rank Math | focus keyword, title, description, score - via Novamira | 2026-05-20 |

> thruuu ne sait pas scraper un brouillon (il lit la 404). Seul l'export **SERP** est exploité ici ; l'audit page thruuu est ignoré.

## 3. État de l'article

- **1 837 mots** : court pour la SERP (concurrents 2 000 à 9 400 mots, médiane ~2 800).
- Structure : 6 H2 thématiques + 13 H3, plan logique et bien découpé.
- 1 encadré « L'essentiel à retenir », 1 sommaire Kadence, 1 tableau HTML, 1 FAQ (8 questions en 2 accordéons).
- **0 lien interne, 0 lien sortant, 0 image** dans le corps. Aucune image à la une.
- Rédaction très fragmentée : paragraphes de 1 à 2 phrases, beaucoup de phrases creuses (« Votre site reste rapide. C'est un atout majeur. »). Densité d'information faible.

## 4. SEO actuel

- **Rank Math non configuré** : focus keyword vide, balise title vide, meta description vide. Score Rank Math **13/100**.
- Slug `avis-rank-math` : conforme (pas d'année, pas de « schoolswp », pas de préfixe numérique).
- Titre H1 / post : « Avis Rank Math : le plugin SEO incontournable en 2026 » - mot-clé en tête, correct.
- Excerpt rédigé mais : emploie « notre avis » (voix au pluriel, à proscrire), « n°1 » (claim absolu non sourcé).
- Aucun balisage Schema (ni FAQPage, ni Review) alors que 3 concurrents du top 10 ont FAQPage et 2 ont Review.

### Volumes (DataForSEO, France, fr)

| Requête | Volume/mois | KD | Intent |
| --- | --- | --- | --- |
| avis rank math | résiduel (non mesurable) | - | informational |
| rank math | 880 | 20 | informational |
| rank math seo | 720 | 16 | commercial |
| rank math pro | 140 | - | informational |
| rank math vs yoast | 20 | 9 | informational |

La requête exacte « avis rank math » a un volume résiduel (omise par DataForSEO).

### Champ sémantique (DataForSEO keyword_suggestions, 100 requêtes « rank math »)

Export complet : `dataforseo-google-sheet.csv` + [Google Sheet des volumes](https://docs.google.com/spreadsheets/d/1lliIN9uoVNAJVqcRVkvvGsG9iZpsazlV0mbMVP5fYrw/edit).

- **Poids du champ** : ~3 030 recherches/mois une fois retirées 2 fausses positives d'éducation mathématique (« rank in math » 880, « math rank » 20).
- **Très long-tail** : seules 4 requêtes dépassent 100/mois (rank math 880, rank math seo 720, rank math pro 140, rank math seo wordpress 110). Tout le reste est une traîne de 10 à 90/mois.
- **Difficulté basse** (KD 9 à 20 sur les têtes) : créneau gagnable.
- **Sous-thèmes de la traîne** qui confirment les manques de l'article : comparaisons (vs Yoast, vs AIOSEO, vs SEOPress, vs All in One), schema et rich snippets, Content AI, instant indexing, sitemap, redirections, tutoriels, tarifs (free, pro, lifetime).
- **Tendance annuelle franchement négative** (-38 % à -100 % sur la majorité des requêtes) : l'intérêt pour la marque Rank Math décline. L'article doit capter la traîne pendant que le volume existe encore.

**Conclusion ciblage** : viser le cluster « rank math » / « rank math seo » (tête à ~1 600/mois cumulés, KD bas) via un vrai test, et ratisser la traîne (comparatifs, schema, tarifs) avec des sections dédiées.

## 5. SERP analysée (top 20 FR, google.fr)

- **Intent dominant** : avis/test de plugin, fortement teinté de comparaison **vs Yoast** (positions 7, 8, 18 sont des « Rank Math vs Yoast »).
- **Format majoritaire** : article de test long et illustré. Trustpilot (#1), Reddit (#4) et le site officiel rankmath.com (#5, #11, #13) occupent 5 places : la preuve sociale et l'avis tiers pèsent lourd.
- Concurrents FR directs : wpmarmite, lesmakers, webandseo, kingeo, nugg.ad. Tous ont **avantages ET inconvénients**, une **note chiffrée** (4,8/5 ou 4,9/5) et une **section tarifs**.
- Questions récurrentes de la SERP non traitées par le brouillon : **« Combien coûte Rank Math ? »**, **« Rank Math est-il sûr ? »** (8 occurrences), **« Quelles alternatives à Rank Math ? »** (6), **« À qui s'adresse Rank Math ? »**.
- Champ sémantique attendu (thruuu Topic) bien couvert sur : architecture/modules, schema, IndexNow, redirections, Search Console, Content AI. Sous-couvert sur : **tarifs/prix**, **Yoast** (comparaison), **sitemap**, **mots-clés/focus keyword**.

## 6. Audit 4 axes - Publish Score

> Publish Score = SEO×0,30 + LLM×0,25 + Conversion×0,25 + Autorité×0,20

### SEO - 40/100

- Meta Rank Math 100 % vides, score 13. À configurer entièrement.
- Contenu trop court (1 837 mots) face à une SERP à 2 800+.
- 0 maillage interne, 0 lien sortant, pas de lien vers le dépôt officiel WordPress.org (règle schoolsWP).
- Sujets SERP manquants : prix, sécurité, alternatives, public cible.
- Bon point : plan H2/H3 propre et aligné sur les intentions.

### LLM / GEO - 52/100

- L'encadré « L'essentiel à retenir » est bon pour l'extraction IA.
- FAQ en accordéon : structure favorable, mais **titre de section en anglais** (« Questions? We Have Answers. ») = signal de qualité catastrophique.
- Claims non sourcés : « 3 millions d'utilisateurs », « 4,9/5 », « 51 300 lignes de code contre 87 000 pour Yoast ». À sourcer ou retirer.
- Aucune donnée structurée (FAQPage / Review) alors que la FAQ existe déjà en clair.

### Conversion - 25/100 (axe le plus faible)

- **Aucun bouton CTA**, aucun lien vers Rank Math (ni affilié, ni officiel).
- **Aucune grille tarifaire** : impossible pour le lecteur de décider. Le tableau Free/Pro est cryptique (« Content AI : 5 / 7,5k » sans unité).
- Conclusion molle : « Activez l'assistant de configuration dès maintenant » sans lien ni offre.
- Pour un avis à visée affiliation, c'est rédhibitoire en l'état.

### Autorité - 35/100

- Article **100 % positif, zéro inconvénient** : red flag E-E-A-T pour un « avis ». Tous les concurrents FR ont une section avantages/inconvénients.
- Pas de preuve de test réel (pas de capture, pas de chiffre vécu, pas de profil d'auteur visible).
- **Violations de la voix schoolsWP** : « notre avis » (excerpt), « D'après nos analyses » (FAQ). Règle = un seul Michael derrière schoolsWP, écrire au « je ».
- Ton hyperbolique : « la véritable magie opère », « fulgurant », « dominer les recherches ».

### Publish Score global

**≈ 39/100** → seuil `<70` = **réécriture**.

## 7. Insights critiques

1. **Bugs de publication bloquants** : titre FAQ en anglais, balises `<meta charset>` parasites dans les accordéons, accent manquant sur « débuter », accordéon col. 2 (`paneCount:4` pour 3 panes). À corriger quoi qu'il arrive.
2. **Ce n'est pas encore un avis** : pas de note, pas d'inconvénients, pas de prix, pas de « pour qui c'est / pas pour qui ». C'est une fiche promo, pas un test. La SERP, elle, récompense le test équilibré.
3. **Tableau Free/Pro factuellement faux** : « Schema ❌ Free » et « Mots-clés ❌ Free » sont erronés. Rank Math **gratuit** inclut le générateur de Schema et jusqu'à 5 focus keywords par page. Le corps de l'article se contredit lui-même (la FAQ dit que la version Pro « étend » le Schema, donc le free l'a déjà). À convertir en Ninja Tables **après correction**, pas tel quel.
4. **Zéro conversion** : ni CTA, ni lien Rank Math, ni tarifs. L'article ne peut rien rapporter en l'état.
5. **Cibler le cluster marque, pas la requête exacte** : « avis rank math » seul ne vaut rien. Optimiser pour « rank math » / « rank math seo » (1 600/mois, KD 16-20) via un vrai test, c'est jouable.

## 8. Décision

**Réécriture ciblée avant publication** (statut : `refonte-decidee`). L'ossature H2/H3 est conservée ; le travail porte sur le fond (preuves, équilibre, profondeur), la conversion (CTA + tarifs + lien) et les corrections techniques.

## Corrections déjà appliquées (2026-05-20)

Dans la foulée de l'audit, le **Lot A** et le **tableau (Lot C)** ont été exécutés sur le brouillon :

- Titre + sous-titre de la section FAQ traduits en français.
- 11 balises `<meta charset>` parasites supprimées des accordéons.
- Accent corrigé : « débuter ».
- Accordéon colonne 2 : `paneCount` et classe CSS alignés sur 3 panes.
- Rank Math renseigné : focus keyword (`avis rank math, rank math, rank math seo`), balise title, meta description ; excerpt réécrit à la voix singulier.
- Tableau HTML Free/Pro remplacé par une table **Ninja Tables corrigée et enrichie** (#2915645, 10 lignes : tarif réel, Schema et focus keywords rectifiés, Rank Tracker, redirections, sitemap, SEO local).

Puis le **Lot B** (réécriture du fond) a été exécuté :

- Fond entièrement réécrit : **1 837 → 2 803 mots**, voix tutoiement intégrale (0 « vous »), fin des paragraphes de remplissage d'une phrase.
- Chiffres corrigés et sourcés : **4 millions+** d'installations actives et **4,8/5** sur ~7 500 avis (WordPress.org). Claim non sourcé « 51 300 lignes de code » supprimé.
- 3 nouvelles sections H2 : « Rank Math face à Yoast », « Combien coûte Rank Math Pro » (tarifs réels), « Rank Math, c'est pour qui (et est-ce risqué) ».
- Verdict **5/5** dans un encadré Kadence (choix Michael : positif sans réserve, limites tissées en bref sans section dédiée).
- Lien vers le dépôt officiel WordPress.org ajouté (`seo-by-rank-math`).
- FAQ : voix corrigée (tutoiement) + erreur factuelle retirée.

Puis le **Lot C** (conversion, maillage, image) a été exécuté :

- 2 boutons CTA Kadence vers Rank Math : « Installer Rank Math gratuitement » après le comparatif Yoast, et « Découvrir Rank Math » avant la FAQ. Lien affilié cloaké schoolswp.com/rank-math/ qui redirige en 302 vers rankmath.com/?ref=contact1975 ; le slug a été ajouté au mu-plugin schoolswp-affiliate-cloaks.php.
- 4 liens internes du cocon SEO schoolsWP, tous en FR : « Changer extension SEO » et « AIOSEO » dans la sous-section migration, « SEOPress vs Yoast » dans le comparatif Yoast, « référencement Google » dans la sous-section sur le score d'optimisation.
- Image à la une : cover éditoriale schoolsWP générée via HTML et Playwright, carte verdict 5/5, attachment #2916823.
- 3 captures d'écran du plugin (assistant de configuration, panneau Rank Math dans Gutenberg, module Schema), fournies par Michael, recadrées et chrome WordPress flouté en gaussien, placées dans les 3 sections correspondantes (centrées, légende en italique). Attachments #2918607, #2918608, #2918609.

Enfin, le **Lot D** (données structurées) a été exécuté :

- 3 schémas Rank Math ajoutés en postmeta, au format natif du site : BlogPosting (schéma article principal, conservé explicitement pour ne pas le perdre), FAQPage (les 7 questions de la FAQ) et Review (avis 5/5, itemReviewed SoftwareApplication Rank Math, 4 offres tarifaires, aggregateRating 4,8 sur 7428 avis WordPress.org). Vérifié : Rank Math expose bien les 3 schémas.
- 2 artefacts de texte corrigés dans la FAQ au passage : une marque de troncature parasite et un « votre » résiduel repassé au tutoiement.

À noter : Google n'affiche plus les rich results FAQ depuis 2023 (réservés aux sites gouvernementaux et de santé). Le balisage FAQPage reste valide et utile pour la compréhension par les moteurs et les IA. Le balisage Review, lui, peut faire apparaître des étoiles dans la SERP.

Optimisation finale des meta (2026-05-20) : meta description réécrite pour s'ouvrir sur la requête cible et couvrir le champ sémantique (Content AI, Schema, tarifs Pro, version gratuite, Yoast, limites), mots-clés focus passés de 3 à 5 (ajout de « rank math pro » et « rank math vs yoast »), balises Open Graph et Twitter renseignées (image OG = image à la une). La requête « avis Rank Math » a aussi été ajoutée à l'intro pour que Rank Math détecte le mot-clé principal. Le titre SEO était déjà conforme, conservé tel quel. Les 4 médias de l'article (image à la une #2916823 et les 3 captures #2918607 à #2918609) ont reçu leur champ Description WordPress, en complément des champs alt et légende déjà renseignés.

À noter : l'image à la une #2916823 affiche « 2026 » dans son visuel (badge et pied de carte). Michael a choisi de la conserver telle quelle. La règle posée à cette occasion (une featured image doit rester evergreen, sans date dans le visuel) s'applique aux prochaines covers.

Sauvegardes `post_content` : postmeta `_audit_backup_content_20260520` (pré-Lot A) et `_audit_backup_content_preB` (pré-Lot B), plus _audit_backup_content_preC pré-Lot C et _audit_backup_content_preD pré-Lot D, plus _audit_backup_content_preimg pré-captures, sur le post 2289943.

> Les 4 lots A, B, C et D sont terminés. Reste avant publication : un dernier passage Update dans Gutenberg (réévalue le score Rank Math, à 72 actuellement), puis passage du brouillon en publié.

## 9. Plan d'action

**Lot A - Corrections bloquantes** - APPLIQUÉ le 2026-05-20
- Traduire le titre + sous-titre de la section FAQ en français.
- Supprimer les `<meta charset="utf-8">` parasites des accordéons.
- Corriger « debuter » → « débuter » dans le H2.
- Aligner `paneCount` de l'accordéon col. 2 sur le nombre réel de panes.
- Renseigner Rank Math : focus keyword, balise title, meta description ; corriger l'excerpt (« notre » → « je »).

**Lot B - Fond et crédibilité**
- Allonger à ~2 800-3 200 mots en densifiant (fusionner les paragraphes d'une phrase, ajouter de la substance, pas du remplissage).
- Ajouter une section **Inconvénients / limites** honnête + un **verdict chiffré** (note /5, « pour qui c'est », « pour qui ça ne l'est pas »).
- Ajouter une section **Tarifs** réelle (plans et prix Rank Math à jour).
- Ajouter une section **vs Yoast** courte (la SERP la réclame) et traiter « Rank Math est-il sûr ? » + « alternatives ».
- Sourcer ou retirer les claims chiffrés (3 M d'utilisateurs, 4,9/5, lignes de code).
- Ajouter le lien vers le dépôt officiel `fr.wordpress.org/plugins/seo-by-rank-math/`.

**Lot C - Conversion et maillage** - APPLIQUÉ le 2026-05-20 (captures du plugin en attente d'arbitrage)
- Tableau Free/Pro **corrigé et enrichi** (prix, redirections, sitemap, Rank Tracker, SEO local) → version **Ninja Tables**.
- Ajouter 1 à 2 boutons CTA Kadence vers Rank Math (lien affilié cloaké si dispo, sinon lien officiel).
- Ajouter 3 à 5 liens internes (cocon SEO schoolsWP) et illustrer (image à la une + captures du plugin).

**Lot D - Schema** - APPLIQUÉ le 2026-05-20
- Activer le balisage FAQPage (la FAQ existe déjà) et envisager Review (note chiffrée).

## 10. Métriques de suivi (prochain snapshot)

- Score Rank Math (cible ≥ 80) et meta renseignées.
- Nb de mots, présence section inconvénients + tarifs + verdict.
- Position GSC sur « rank math » / « rank math seo » une fois indexé.
- Présence CTA + lien Rank Math + maillage interne.
- Publish Score recalculé (cible ≥ 80).
