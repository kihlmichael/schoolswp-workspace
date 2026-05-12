---
slug: masteriyo-lms-avis
url: https://schoolswp.com/masteriyo-lms-avis/
date_snapshot: 2026-05-07
trigger: Rank Math weekly 2026-05-03 (-51 positions, 76e)
status: refonte-decidee
decision_doc: ../../../decisions/masteriyo-arbitrage-2026-05-06.md
---

# Audit Masteriyo LMS Avis — snapshot 2026-05-07

## 1. Contexte & déclencheur

L'article `https://schoolswp.com/masteriyo-lms-avis/` (4500 mots, MAJ 2026-04-11) recommande chaleureusement Masteriyo LMS comme "solution d'avenir que nous recommandons sans hésiter". Le rapport Rank Math hebdomadaire du 2026-05-03 l'affiche en position 76e (-51 places sur 7 jours).

Conflit stratégique : la stack commerciale schoolsWP s'appuie sur Tutor LMS (article principal FR + sprint corpus 164 docs + formation FluentBoards en préparation via Tutor LMS).

## 2. Données collectées

| Source | Scope | Statut | Fichier |
| --- | --- | --- | --- |
| GSC MCP | 90j (2026-02-06 → 2026-05-07) queries breakdown | OK | `gsc-90d.json` |
| GSC MCP | URL inspect indexation + rich results | OK | `gsc-url-inspect.json` |
| defuddle | Snapshot HTML article actuel | OK | `article-current-snapshot.md` |
| DataForSEO | volume + SERP FR + suggestions + intent | **DOWN (401)** | à compléter |
| thruuu | SERP "masteriyo lms avis" + audit article (2 variations kw) | **fait** 2026-05-07 | `thruuu-raw/` (4 fichiers) + extraits MD `thruuu-audit-*.md` + `thruuu-serp-*.md` |
| Rank Math weekly | rapport 2026-05-03 | externe | non archivé ici |

## 3. État de l'article actuel

**Structure** : 11 sections existantes : Intro / Résumé / Avantages-Inconvénients / Pour qui (4 audiences) / Fonctionnalités (4 sous-sections : SPA React JS, Quiz, Monétisation, Content Drip) / Optimisation SEO / Tarifs / vs Concurrents (LearnDash, Tutor LMS, LearnPress) / Avis clients / Avis final / FAQ.

**Longueur** : ~4500 mots. **MAJ** : 2026-04-11. **Note schema** : 4,8/5 sourcée WordPress.org (143 avis vérifiés, 134 à 5 étoiles).

**CTA actuel** : cloak interne `schoolswp.com/masteriyo/` via ClickWhale. **Visuels** : 10+ screenshots Masteriyo (création cours, quiz, paiement, content drip, permaliens).

**Verdict actuel** : "Une solution d'avenir que nous recommandons sans hésiter".

**Problèmes branding détectés** :

- Vouvoiement systématique (vs règle 5 BRAND_RULES.md tutoiement)
- Voix "nous" partout (vs mémoire `feedback_voice_singular_solo.md`)
- Mots interdits : "révolutionne" / "révolutionnent" 3x (vs règle 15)
- Section vs Tutor LMS qui dénature Tutor : *"Un utilisateur ayant testé Tutor LMS avec Bricks a rapporté des conflits"* + *"Tutor LMS reste dépendant de ses add-ons"* (vs règle 31 nouvellement ajoutée)
- Conclusion marketing creux : *"transformez votre expertise en formations captivantes !"* (vs anti-pattern règle 30)

## 4. SEO actuel (GSC 90j)

**Bilan global** : 0 clicks / 124 impressions sur 90 jours. CTR 0 %.

**Queries** :

| Query | Position | Impressions | Clicks |
| --- | --- | --- | --- |
| masteriyo | 7,4 | 22 | 0 |
| **masteriyo lms** | **4,5** | 13 | 0 |
| masteryio (typo) | 3,8 | 5 | 0 |
| lms avis | 7 | 1 | 0 |
| **lms rechargement automatique** | **10** | 1 | 0 |
| lms2026 | 12 | 1 | 0 |
| monétisation des offres éducatives avec lms | 37,4 | 57 | 0 |
| monétisation des compétences avec lms | 81,2 | 24 | 0 |

**Constats SEO** :

1. **Position 4,5 sur "masteriyo lms"** = asset commercial (intent décisionnel). 0 % CTR = snippet cassé.
2. **3 queries proches du top 10** ("masteriyo" 7,4 / "masteriyo lms" 4,5 / "masteryio" 3,8) sans aucun click.
3. **2 queries hors-sujet** ("monétisation des offres/compétences éducatives") = 81 impressions perdues sur intent informationnel trop générique.
4. **"lms rechargement automatique" position 10** = intent abonnements/subscriptions natives, opportunité argumentaire pour Tutor 3.0+.
5. **Indexation OK** (`PASS`, dernière crawl 2026-04-26).
6. **Pas de Review rich snippet** détecté par Google (uniquement Breadcrumbs) malgré note 4,8/5 dans le contenu. **Diagnostic confirmé 2026-05-07** : le `@graph` JSON-LD Rank Math contient bien Place + EducationalOrganization+Organization + WebSite + ImageObject + BreadcrumbList + WebPage + Person + BlogPosting, mais **pas de Review ni Product**. La note 4,8/5 est purement visuelle, pas dans le schema. Solution : ajouter un schema Review (snippet prêt dans `content/decisions/masteriyo-arbitrage-2026-05-06_schema-review-snippet.md`). Bug probablement systémique sur les autres articles d'avis schoolsWP.
7. **Référent interne unique** = article principal Tutor LMS. Google associe déjà sémantiquement les deux pages (bon pour la refonte).

## 5. SERP analysée (audit thruuu intégré 2026-05-07)

Audit thruuu réalisé sur 2 variations de keyword (`masteriyo lms avis` + `avis masteriyo lms`). Données complètes : `thruuu-audit-*.md` + `thruuu-serp-*.md` dans ce dossier.

### Position schoolsWP

- **Position 2** sur "masteriyo lms avis" (variation principale, FR desktop)
- **Position 2** sur "avis masteriyo lms" (variation inverse)
- Cohérent avec GSC (position 4,5 sur "masteriyo lms" + 76e Rank Math sur "masteriyo lms avis" exact = écart possible entre rapports car keyword stricter)

### Typologie SERP (top 20)

La SERP n'est **PAS dominée par des avis dédiés FR** mais par :

| Type | Count | Exemples |
| --- | --- | --- |
| Featured snippet (comparatif) | 1 | one.com Top 11 plugins LMS (#1) |
| Avis dédié FR | 1 | **schoolsWP** (#2) |
| Review aggregator | 2 | g2.com (#3), elearningindustry (#15) |
| Comparatif multi-LMS FR | 2 | wp-support.fr (#4), aventuredentrepreneur (#17) |
| Forum / Reddit FR | 1 | reddit r/Wordpress (#7) |
| Officiel Masteriyo | 3 | masteriyo.com homepage (#9), pricing (#11), Facebook (#13) |
| Plugin pages WP.org | 3 | wp.org FR (#8), en-gb (#12), reviews (#19) |
| Avis EN (copies/syndications) | 5 | zoom-eco, dnsafrica, wphive, wpnewsboard, wp.org topic |

**Insight stratégique fort** : schoolsWP est **le seul avis Masteriyo FR détaillé** dans le top 20. Pas de concurrent direct FR. Position 2 = défendable et stratégique.

### Métriques comparatives schoolsWP vs SERP avg

| Métrique | schoolsWP | SERP avg (kw "masteriyo lms avis") | SERP avg (kw "avis masteriyo lms") | Constat |
| --- | --- | --- | --- | --- |
| Word count | 3601 | 2116 | 1459 | OK (> avg) |
| Image count | 24 | 65 | 14 | Mixte selon kw — sur "masteriyo lms avis" thruuu suggère +22 images |
| Page Rank Score | 28 | 42 | 39 | **Sous-optimal autorité** (schoolsWP < SERP avg) |
| Schema Type | Place + Org + WebSite + ImageObject + Breadcrumb + WebPage + Person + BlogPosting | mix | mix | **Pas de Review/Product** (concurrents elearningindustry a Product, masteriyo.com a Article + FAQPage) |

### Bug technique critique (thruuu confirme GSC)

- **Title 586,4 pixels > 580 px max Google** → tronqué sur SERP. Cause : ancien title "Avis Masteriyo LMS 2026 : paiement intégré sans WooCommerce" (59 chars mais lourd en pixels). À corriger dans la refonte avec un title plus court en pixels.
- Description 147 chars (< 155) → OK
- 4 questions dans headings (vs SERP avg 1) → ✅ excellent
- Pas de Review schema → confirmé thruuu (Schema Type listé sans Review ni Product)

### Headings fréquents non-couverts par schoolsWP (à ajouter en refonte)

Détectés via thruuu sur top 20 :

- **Migration** : "Already using a different lms?", "Can i migrate from another lms?" → **valide la section migration prévue dans le brief** (snippet déjà préparé)
- **Comparatif multi-LMS** : "How does masteriyo compare to learndash, tutorlms, or lifterlms?" → la section vs concurrents doit citer plus de LMS (actuellement seulement LearnDash / Tutor / LearnPress, ajouter LifterLMS + Sensei mentionnés)
- **Cas d'usage** : "Does masteriyo work for corporate training, schools, or online academies?" → étoffer la section "Pour qui Masteriyo" existante
- **Course bundle** : terme attendu mais non couvert → opportunité Tutor 3.0+ (Course Bundle natif vs Masteriyo)
- **Course creation and management** : à intégrer dans H2/H3
- **Quiz, assignment, and assessment** : déjà partiellement couvert
- **Monetization & payments** : déjà couvert

### People Also Ask (PAA)

- "Quelle est la meilleure plateforme LMS ?"
- "Quels sont les avis des clients sur la formation WordPress ?"
- "Comment choisir son LMS ?"
- "Quels sont les avis sur 360Learning ?" (off-topic mais Google l'associe)

→ FAQ refonte peut intégrer 1-2 de ces questions (sauf 360Learning qui est hors-scope schoolsWP).

### Frequent terms manquants (selon thruuu)

À intégrer naturellement (pas bourrage) dans la refonte :

- "course builder" (0/3-7 attendus)
- "online course" (0/5-7 attendus)
- "course bundle" (0/3-4) → angle Tutor 3.0+
- "course creation" (0/3-3)
- "lms plugin" (1 attendu, écart faible)

### Recommandations IA thruuu (titres/metas)

**À ignorer** : les suggestions thruuu ("Une Révolution eLearning", "transformez votre passion en revenus", "lancez-vous dès maintenant !") violent les règles 15 + 30 BRAND_RULES.md. On garde le title patché : "Masteriyo LMS Avis 2026 : je suis passé à Tutor LMS" (51 chars, pixels-safe vs ancien 586 px) ou variante plus courte si pixels encore trop larges.

## 6. Insights critiques

1. **Coût d'opportunité refonte = nul** (0 clicks actuels). Marge de manœuvre maximale.
2. **Position 4,5 sur "masteriyo lms" + position 2 thruuu sur "masteriyo lms avis"** = asset à préserver. Refonte ne doit pas casser l'URL.
3. **schoolsWP est le seul avis Masteriyo FR détaillé** dans le top 20 SERP → position 2 stratégiquement défendable, pas de concurrent direct FR à craindre.
4. **Snippet refondu = potentiel boost CTR** (de 0 % à 3-8 % réaliste = 4-10 clicks/mois).
5. **Pivot pro-Tutor** doit respecter Masteriyo (règle 31 BRAND_RULES.md).
6. **Schema Review à corriger** : la note est dans le contenu mais Google ne la qualifie pas en rich snippet (thruuu confirme + GSC confirme).
7. **Title trop large en pixels (586,4 > 580)** : tronqué sur SERP. Refonte doit raccourcir.
8. **Sujet migration validé par SERP** : "Already using a different lms?" + "Can i migrate from another lms?" sont des headings fréquents → la section migration préparée est en plein dans la cible.
9. **Page Rank Score 28 vs SERP avg 42** : autorité sous le marché. Refonte doit s'accompagner d'un effort netlinking ciblé (cf. mémoire `project_netlinking_plan.md`).
10. **Headings concurrents à ajouter** : LifterLMS + Sensei dans la comparaison, course bundle (angle Tutor 3.0+), cas d'usage corporate training.

## 7. Décision

**Option D : Refonte chirurgicale ancrée "dans mon cas / sur schoolsWP"** (pas réécriture from scratch, pas désindex, pas 301).

Détails complets : [`../../../decisions/masteriyo-arbitrage-2026-05-06.md`](../../../decisions/masteriyo-arbitrage-2026-05-06.md).

## 8. Plan d'action

| # | Action | Effort | Statut | Livrable |
| --- | --- | --- | --- | --- |
| 1 | Backup HTML article actuel | 5 min | **fait** 2026-05-07 | `content/articles/lms/_backup/2026-05-07_masteriyo-lms-avis-original.html` (97 KB décompressé) |
| 2 | Vérifier programme affilié Themeum (Tutor LMS Pro) | 10 min | à faire (externe) | - |
| 3 | Préparer snippet migration Masteriyo vers Tutor | 30 min | **fait** 2026-05-07 | `content/decisions/masteriyo-arbitrage-2026-05-06_migration-snippet-draft.md` (310 mots, source : sprint corpus 11-migration) |
| 4 | Refonte chirurgicale 11 sections (8 passes ton + 2 réécritures + 1 ajout) | ~4h | **draft v1 livré** 2026-05-07 | `content/articles/lms/masteriyo-lms-avis-refonte-v1.md` (4363 mots, QA passée) |
| 5 | Investiguer Review schema | 30 min | **fait diagnostic** 2026-05-07 | `content/decisions/masteriyo-arbitrage-2026-05-06_schema-review-snippet.md` (cause confirmée + JSON snippet prêt) |
| 5-bis | Pousser le schema Review (Option A manuel ou B mu-plugin) | 15 min | à faire | snippet prêt |
| 6 | Audit thruuu (SERP + audit article) à intégrer | 30 min | **fait** 2026-05-07 | section 5 mise à jour + insights critiques 7-10 ajoutés |
| 7 | Mission séparée : auditer schema Review sur tous articles d'avis schoolsWP | 1h | à planifier | bug probablement systémique |

## 9. Métriques de suivi (snapshots futurs)

Voir [`../README.md`](../README.md) section "Métriques de suivi (post-refonte)" pour les baselines + cibles J+30 / J+60 / J+90.

Au prochain snapshot (J+30 post-refonte), créer `_diff.md` qui répond à :

- Positions ont-elles bougé ? (cf `gsc-90d.json`)
- Queries gagnées / perdues ?
- SERP top 10 a-t-elle bougé ?
- L'article a-t-il été refondu comme prévu ?
- Review rich snippet est-il maintenant détecté ?
