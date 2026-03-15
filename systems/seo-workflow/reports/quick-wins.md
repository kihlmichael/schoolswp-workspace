# Quick Wins SEO — schoolsWP

Quick wins actionnables immédiatement, classés par impact.

---

## QW1 — Noindexer les pages inutiles

**Type :** Observable
**Effort :** XS (30 min)
**Impact SEO :** H
**Condition :** Pages login/feeds/archives visibles dans le plan de site

**Action :**

1. Aller dans Rank Math → Titles & Meta → Archives/Tags → "No Index"
2. Aller dans Rank Math → Titles & Meta → Author Archive → "No Index"
3. Vérifier que le portail d'assistance `/portail-assistance/` a un meta noindex

**Vérification :** Soumettre l'URL dans GSC "Inspecter l'URL" → doit afficher "noindex"

---

## QW2 — Ajouter disclosure affiliation sur tous les articles affiliés

**Type :** Observable (absence confirmée par lecture de plusieurs pages)
**Effort :** S (2-3h pour toutes les pages)
**Impact SEO :** M
**Impact Business :** H (conformité légale + trust)
**Condition :** Aucune

**Action :**

1. Copier le bloc disclosure depuis `skills/eeat-template-builder.md` → Bloc 3
2. Créer un bloc Gutenberg réutilisable "Disclosure Affiliation" dans WordPress
3. L'ajouter en haut de chaque article contenant des liens affiliés

**Texte à utiliser :**

> **Transparence** : Cet article contient des liens d'affiliation. Si tu passes par ces liens pour acheter, je perçois une commission sans coût supplémentaire pour toi. Cela m'aide à maintenir schoolsWP gratuitement. Je ne recommande que les outils que j'utilise ou que j'ai testés.

---

## QW3 — Exporter GSC et identifier les 5 CTR les plus faibles

**Type :** Données réelles
**Effort :** XS (15 min pour l'export, 30 min d'analyse)
**Impact :** Déblocage de T3
**Condition :** Accès GSC schoolswp.com

**Action :**

1. GSC → schoolswp.com → Performance → Résultats de recherche
2. Grouper par "Pages" → Trier par "Impressions" décroissant
3. Filtrer : CTR < 3% ET impressions > 500
4. Exporter CSV
5. Identifier les 5 premières lignes → ce sont les quick wins T3

---

## QW4 — Réécrire le title de la page avec le plus d'impressions et le CTR le plus faible

**Type :** Données GSC (dès que QW3 complété)
**Effort :** S (1h max)
**Impact SEO :** H (effet rapide sur CTR)
**Condition :** Export GSC disponible

**Action :**

1. Identifier la requête principale de la page (requête avec le plus d'impressions)
2. Réécrire le title avec la requête principale en position 1 dans le H1 et le title tag
3. Ajouter un mot émotionnel ou chiffre dans la meta description (ex : "Guide complet", "En 2026", "[nombre] plugins")
4. Valider dans Rank Math
5. Demander une réindexation dans GSC "Inspecter l'URL"

**Mesure :** Comparer CTR à J+28 dans GSC

---

## QW5 — Ajouter 3 liens manuels depuis la homepage vers les piliers P1

**Type :** Observable (structure menu connue)
**Effort :** S (1h)
**Impact SEO :** M (link juice vers piliers)
**Impact Business :** M
**Condition :** Identifier les 3 pages piliers P1 depuis T1 (ou le menu)

**Action :**

1. Identifier les 3 pages piliers depuis `01_Inventory` ou le menu principal
2. Ajouter un bloc "Articles recommandés" ou "Nos guides essentiels" sur la page d'accueil
3. Lier vers ces 3 pages avec une ancre descriptive (ex : "Guide complet SEO WordPress")

---

## QW6 — Configurer GSC Ciblage international

**Type :** Bonne pratique Google
**Effort :** XS (10 min)
**Impact SEO :** M
**Condition :** Site multilingue FR/EN/DE

**Action :**

1. GSC → Paramètres → Ciblage international
2. Vérifier que le ciblage pays est défini correctement (FR = France ou pas de ciblage spécifique)
3. Si hreflang est implémenté, GSC devrait détecter les signaux automatiquement

---

## Suivi des quick wins

| QW  | Action                    | Statut | Date       | Résultat mesuré                                                                                                         |
| --- | ------------------------- | ------ | ---------- | ----------------------------------------------------------------------------------------------------------------------- |
| QW1 | Noindex pages inutiles    | done   | 2026-03-11 | Archives auteur + étiquettes + dates désactivées. /portail-assistance/ et /coming-soon/ vérifiés GSC : noindex confirmé |
| QW2 | Disclosure affiliation    | todo   | —          | —                                                                                                                       |
| QW3 | Export GSC                | todo   | —          | —                                                                                                                       |
| QW4 | Réécrire title CTR faible | todo   | —          | CTR J+28                                                                                                                |
| QW5 | Liens homepage → piliers  | todo   | —          | —                                                                                                                       |
| QW6 | GSC ciblage international | todo   | —          | —                                                                                                                       |
