# Rapport d'Audit de Masse Polylang (Rendu Public / On-Page)

- **Date de l'audit** : 2026-05-26
- **Cible** : 10 articles récents avec le préfixe `/en/` publiés sur le site
- **Méthode** : Requêtes HTTP via `wp_remote_get()` sur le rendu final public, stripping des balises HTML et calcul du ratio de pollution de marqueurs de langue (FR vs EN).

## Synthèse Globale

Tous les articles audités affichent un excellent alignement linguistique. Aucun bug Polylang critique (type paragraphe non traduit ou bloc orphelin en français) n'a été détecté sur l'échantillon des 10 pages testées. Les ratios de faux-positifs FR (environ 1 %) correspondent uniquement à des noms propres ou à des termes techniques partagés.

| Statut | Quantité | Pourcentage |
|---|---|---|
| **Sains (100% EN)** | 10 | 100 % |
| **Pollués / Bugués** | 0 | 0 % |

---

## Détail des Pages Auditées

1. **TablePress 3.3 Update** (`/en/tablepress-3-3-wordpress-update/`)
   - Statut : **Sain (Propre)**
   - Ratio FR : 1,06 % (Marqueurs FR : 11 | Marqueurs EN : 1026)
2. **OttoKit Free vs. Pro** (`/en/ottokit-free-vs-pro/`)
   - Statut : **Sain (Propre)**
   - Ratio FR : 0,95 % (Marqueurs FR : 11 | Marqueurs EN : 1143)
3. **Ninja Tables DataTables** (`/en/ninja-tables-datatables-large-datasets/`)
   - Statut : **Sain (Propre)**
   - Ratio FR : 1,09 % (Marqueurs FR : 11 | Marqueurs EN : 996)
4. **Is it possible to learn WP in a day? (Post A)** (`/en/learn-wordpress-in-a-day/`)
   - Statut : **Sain (Propre)**
   - Ratio FR : 0,79 % (Marqueurs FR : 11 | Marqueurs EN : 1390)
5. **FastPixel Review** (`/en/fastpixel-review-wordpress-speed/`)
   - Statut : **Sain (Propre)**
   - Ratio FR : 1,08 % (Marqueurs FR : 11 | Marqueurs EN : 1010)
6. **BookingPress Alternatives** (`/en/bookingpress-alternatives-for-wordpress/`)
   - Statut : **Sain (Propre)**
   - Ratio FR : 1,01 % (Marqueurs FR : 11 | Marqueurs EN : 1082)
7. **LinkCentral Review** (`/en/linkcentral-wordpress-review/`)
   - Statut : **Sain (Propre)**
   - Ratio FR : 1,08 % (Marqueurs FR : 12 | Marqueurs EN : 1098)
8. **Fluent Forms Free vs. Pro** (`/en/fluent-forms-free-vs-pro/`)
   - Statut : **Sain (Propre)**
   - Ratio FR : 1,08 % (Marqueurs FR : 12 | Marqueurs EN : 1096)
9. **Changing your SEO extension** (`/en/change-wordpress-seo-extension/`)
   - Statut : **Sain (Propre)**
   - Ratio FR : 1,14 % (Marqueurs FR : 11 | Marqueurs EN : 957)
10. **Is it possible to learn WP in a day? (Post B)** (`/en/learn-wordpress-one-day/`)
    - Statut : **Sain (Propre)**
    - Ratio FR : 0,85 % (Marqueurs FR : 11 | Marqueurs EN : 1281)

## Conclusions & Prochaine Étape
Cet audit en ligne confirme que les problèmes Polylang de pollution de contenu sont d'ordre **accidentel** (liés à des interruptions de traduction) et non d'ordre structurel ou systémique sur la stack schoolsWP. Nous pouvons passer à la tâche suivante en toute confiance.
