# Roadmap SEO schoolsWP — 30 / 60 / 90 jours

## Résumé exécutif

Le workflow en 10 tâches couvre les leviers SEO fondamentaux de schoolsWP.com : inventaire, hygiène technique, analyse GSC, benchmark, architecture de clusters, maillage, multilingue, E-E-A-T et conversion. Les actions P1 (fondations) sont bloquantes pour les P2. Les quick wins identifiés peuvent être implémentés dès la première semaine sans attendre la complétion du workflow complet.

---

## Quick wins — Cette semaine

Actions immédiatement actionnables sans données supplémentaires :

| Action                                                                                                      | Effort | Impact SEO | Impact Business |
| ----------------------------------------------------------------------------------------------------------- | ------ | ---------- | --------------- |
| Noindexer les pages login/portail/feeds (Observable : présence dans sitemap)                                | XS     | H          | -               |
| Ajouter la disclosure affiliation sur tous les articles affiliés (Observable : absente sur plusieurs pages) | S      | M          | H               |
| Exporter GSC (28j) et identifier 5 pages CTR faible (données GSC)                                           | XS     | -          | -               |
| Ajouter 3 liens manuels depuis la homepage vers les piliers P1                                              | S      | M          | M               |
| Configurer GSC "Ciblage international" si non fait                                                          | XS     | M          | -               |

---

## Horizon 30 jours — Fondations (P1)

**Objectif :** Avoir les données de base et corriger les problèmes bloquants.

| #   | Action                                                                | Tâche | Effort | Priorité |
| --- | --------------------------------------------------------------------- | ----- | ------ | -------- |
| 1   | Compléter l'inventaire SEO (T1)                                       | T1    | S      | P1       |
| 2   | Lancer crawl complet (Screaming Frog) + plan hygiène                  | T2    | M      | P1       |
| 3   | Noindexer pages inutiles identifiées                                  | T2    | S      | P1       |
| 4   | Importer et analyser les exports GSC 3 périodes                       | T3    | S      | P1       |
| 5   | Identifier Top 10 opportunités trafic (CTR + positions 8-20)          | T3    | S      | P1       |
| 6   | Corriger les titles/metas des 5 pages CTR les plus faibles            | T3    | S      | P1       |
| 7   | Commencer benchmark DataForSEO clusters P1 (SEO, LMS, Automatisation) | T4    | M      | P2→P1    |

**KPI 30j :**

- ✓ 01_Inventory complété à ≥80%
- ✓ 02_Hygiene : ≥5 actions noindex/redirect identifiées
- ✓ 03_GSC : Top 10 opportunités documentées
- ✓ 5 titles/metas optimisés

---

## Horizon 60 jours — Structure (P2)

**Objectif :** Corriger l'architecture sémantique et technique.

| #   | Action                                                       | Tâche | Effort | Priorité |
| --- | ------------------------------------------------------------ | ----- | ------ | -------- |
| 8   | Finaliser benchmark DataForSEO + identifier gaps par cluster | T4    | M      | P2       |
| 9   | Cartographier les clusters, identifier cannibalisations      | T5    | M      | P2       |
| 10  | Fusionner ou rediriger les pages cannibalisées               | T5    | M      | P2       |
| 11  | Générer plan maillage interne (liens à ajouter)              | T6    | M      | P2       |
| 12  | Implémenter les 20 premiers liens internes prioritaires      | T6    | S      | P2       |
| 13  | Auditer hreflang + canoniques FR/EN/DE                       | T7    | M      | P2       |
| 14  | Noindexer pages EN/DE de faible qualité (si confirmé)        | T7    | S      | P2       |

**KPI 60j :**

- ✓ 05_Clusters : tous les clusters P1 ont une page pilier définie
- ✓ 06_Linking : ≥20 liens ajoutés vers pages piliers et money pages
- ✓ 07_Multilang : 0 erreur hreflang sur les pages FR
- ✓ GSC : premiers gains de CTR sur les pages optimisées (T3)

---

## Horizon 90 jours — Qualité & Conversion (P2)

**Objectif :** Maximiser la valeur business du trafic existant.

| #   | Action                                                  | Tâche | Effort | Priorité |
| --- | ------------------------------------------------------- | ----- | ------ | -------- |
| 15  | Déployer blocs E-E-A-T sur toutes les pages money       | T8    | S      | P2       |
| 16  | Créer templates Gutenberg pour blocs méthode/disclosure | T8    | M      | P2       |
| 17  | Optimiser CTA sur les 10 pages à fort trafic            | T9    | M      | P2       |
| 18  | Définir et implémenter 3 parcours de conversion         | T9    | M      | P2       |
| 19  | Mesurer impact GSC (comparer J0 vs J90)                 | T10   | S      | P1       |
| 20  | Réviser la roadmap selon les résultats                  | T10   | S      | P1       |

**KPI 90j :**

- ✓ 08_EEAT : 100% pages money avec disclosure + méthode
- ✓ 09_Conversion : 3 parcours de conversion définis et actifs
- ✓ GSC : +15-25% de clics organiques sur les pages optimisées
- ✓ 10_Backlog : ≥70% des actions P1 complétées

---

## Tableau de bord KPIs — Suivi mensuel

| KPI                              | J0 (baseline)   | J30  | J60   | J90   |
| -------------------------------- | --------------- | ---- | ----- | ----- |
| Pages P1 noindexées correctement | À mesurer       | ≥5   | 100%  | 100%  |
| CTR moyen pages P1               | À mesurer GSC   | +1pt | +3pts | +5pts |
| Pages en Top 3 (cluster SEO)     | À mesurer       | —    | +1    | +3    |
| Pages money avec E-E-A-T complet | À mesurer       | —    | 50%   | 100%  |
| Liens internes vers piliers      | À mesurer crawl | +10  | +30   | +50   |
| Trafic organique total           | À mesurer GSC   | +5%  | +15%  | +25%  |

---

## Données manquantes au démarrage

Les données suivantes sont requises avant de lancer le workflow — elles sont actuellement des Hypothèses à valider :

| Donnée manquante            | Comment la récupérer                           | Bloque     |
| --------------------------- | ---------------------------------------------- | ---------- |
| Export crawl complet        | Screaming Frog (gratuit ≤500 URLs) ou Sitebulb | T2, T6, T7 |
| Exports GSC (28j/3m/12m)    | GSC → Performance → Exporter                   | T3         |
| Clé API DataForSEO          | Créer compte DataForSEO → `.env`               | T4         |
| ID Google Sheet de pilotage | Créer le Sheet → copier l'ID dans l'URL        | Tous       |
| Taux de conversion actuels  | FluentCRM ou analytics                         | T9         |
