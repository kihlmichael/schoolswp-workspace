# Audit : suredash-vs-fluent-community

- **Article** : SureDash vs Fluent Community : le comparatif WordPress 2026
- **Post ID** : 2969375 (brouillon, FR)
- **URL** : https://schoolswp.com/?p=2969375
- **Slug** : `suredash-vs-fluent-community`
- **Auteur** : Michaël KIHL
- **Pilier** : Adhésion & Espaces membres / Communauté WordPress (affiliation Fluent Community WPManageNinja + SureDash Brainstorm Force)

## Statut courant

`refonte-effectuee` (brouillon prêt, attente relecture + publication humaine). Refonte GEO/citation + affiliation **exécutée** : comparatif head-to-head FR ~1675 mots, tableau Ninja Tables (2974047), 2 CTA, schema FAQPage, tarifs corrigés, 8 bloquants réglés. **2e passe 2026-06-09** : tableau comparatif Kadence en boîtes produit (boutons FR + liens + étoiles WP.org + logos officiels), image à la une brand posée, 2 schemas SoftwareApplication, prix vérifiés sur sites officiels. Reste : lien affilié SureDash + relecture humaine. Détail en synthese section 8.

## Historique des snapshots

| Date       | Synthèse                              | Trigger                                                                       | Décision                                         | Publish Score estimé |
| ---------- | ------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------ | -------------------- |
| 2026-06-09 | [synthese.md](2026-06-09/synthese.md) | Demande Michaël (audit pré-publication + recherche mot-clé + classement cat.) | Refonte GEO/citation + affiliation (post-thruuu) | 38/100               |

## Insight clé (2026-06-09)

Comparatif de niche émergente, pas un pari de volume - mais forte opportunité GEO :

- Le mot-clé exact `suredash vs fluent community` a **0 volume** FR (mais intention **commerciale 0,76**) ; champ sémantique minuscule et **en effondrement** (-50 % à -97 %/an).
- **SERP + GEO = opportunité de premier entrant** : top SERP = 2 threads Reddit + forum WPManageNinja ; **aucun vrai comparatif head-to-head FR** (wphibou = avis mono-produit). Côté IA, les 4 moteurs répondent mais **schoolswp.com n'est cité par personne** (cf. [thruuu-analysis.md](2026-06-09/thruuu-analysis.md)).
- Les deux produits sont monétisables (SureDash cité 4/4 moteurs IA, Fluent Community 3/4) -> double affiliation.
- Fait corrigé : vrai prix Fluent Community = **159 $/an mono-site** (pas « 999 $/50 sites » du brouillon).

## Actions

- [x] Classement catégories : « Non classé » (1095) -> **Adhésion & Espaces membres (1655) + FluentCommunity (1661) + SureDash (1668)**.
- [x] Recherche DataForSEO (volumes, KD, intent, SERP, suggestions).
- [x] Recherche Ubersuggest (volume, SD, SERP avec DA).
- [x] Google Sheet volumes fusionnés (Drive).
- [x] **Intégration des exports thruuu (GEO + gap SERP)** -> [thruuu-analysis.md](2026-06-09/thruuu-analysis.md). Décision : refonte GEO/citation + affiliation.
- [x] Check cannibalisation cluster 1655 : aucun doublon (pas de comparatif SureDash existant ; `fluentcommunity-avis` = mono-produit, lié).
- [x] **Refonte exécutée** (push WP REST, brouillon) : plan + détail en synthese section 8.
- [x] B1 vouvoiement -> tutoiement (réécriture complète).
- [x] B2 tableau `wp:html` -> Ninja Tables (id 2974047).
- [x] B3 titres FAQ anglais -> FR.
- [x] B4 artefacts `<meta charset>` supprimés.
- [x] B5 tarifs corrigés (Fluent 159/319 $, SureDash 69/199 $ + lifetime ; les 2 ont un free).
- [x] B6 2 CTA Kadence verts (Fluent cloak `/fluentcommunity/` ; SureDash lien direct, à cloaker).
- [x] B7 citation client fabriquée retirée.
- [x] B8 excerpt réécrit (tutoiement + mot-clé).
- [x] Claim « natif vs app isolée » nuancé. Code promo : retiré (mort, confirmé Michaël).
- [x] Schema FAQPage Rank Math (6 Q/R) + verdict « pour qui ».
- [x] **Image à la une** (pipeline brand HTML+Playwright) : hero head-to-head « SureDash vs Fluent Community », WebP, posée sur le brouillon (att 2974203, remplace l'ancienne 2970692).
- [x] **Tableau comparatif Kadence** (boîtes produit ajoutées par Michaël) enrichi : boutons « Voir l'offre » (sites produits ; Fluent cloak sponsored, SureDash direct nofollow) + « Fiche WordPress.org » (repos `fluent-community` / `suredash`), étoiles vraies notes WP.org (SureDash 4,4/5 · 22 avis ; Fluent 4,9/5 · 84 avis), logos officiels à la place des placeholders manette (att 2974176 / 2974177).
- [x] **Schemas Rank Math `SoftwareApplication`** x2 (SureDash, FluentCommunity) : `operatingSystem` WordPress, `offers` + `aggregateRating` (notes WP.org). Réserve : agrégat tiers, affichage SERP non garanti par Google (à valider au Rich Results Test).
- [x] **Prix vérifiés sur sites officiels** (suredash.com, fluentcommunity.co) : les 8 lignes du tableau sont exactes (Fluent coupon 159/319/519 + lifetime 399 $ ; SureDash intro 69/149/199 + lifetime 499 $).
- [ ] **Lien affilié SureDash** (Brainstorm) -> créer cloak `/suredash/` + swap CTA.
- [ ] Relecture humaine éditeur WP + publication.
- [ ] Re-audit 1 mois après publication (citations IA + clics CTA affiliés).

## Livrables

- Google Sheet volumes : [schoolsWP - Volumes SEO - SureDash vs Fluent Community - 2026-06-09](https://docs.google.com/spreadsheets/d/1_Sd_NePDGHg-gpY42efXOsS4mBzNLmqYLGtcb4NMohE/edit)
