# schoolsWP CTR Hunter

Mini-système pour détecter, prioriser et améliorer le CTR des pages via Google Search Console.

**Pipeline** : Extraction GSC → Détection → Scoring → Priorisation → Génération de titles → Test TDD

---

## Étape 1 — Extraction GSC

GSC → Performance → Pages → Exporter :

- URL / Impressions / CTR / Position / Clicks
- Période : **90 jours** (lisser les variations)

---

## Étape 2 — Détection des pages à potentiel

**Filtres quick wins :**

| Critère     | Valeur |
| ----------- | ------ |
| Position    | 3 → 12 |
| Impressions | > 500  |
| CTR         | < 3 %  |

Google montre déjà la page, la position est exploitable, le CTR est améliorable. Levier immédiat sans nouveau contenu.

---

## Étape 3 — Score d'opportunité

```text
Score = Impressions × (CTR cible − CTR actuel)
```

**CTR cibles par position :**

| Position | CTR cible |
| -------- | --------- |
| 3        | 15 %      |
| 4        | 12 %      |
| 5        | 10 %      |
| 6        | 8 %       |
| 7        | 6 %       |
| 8–10     | 5 %       |

**Exemple :**

- Impressions : 5 000 — CTR actuel : 2 % — CTR cible : 8 %
- Gain potentiel : 5 000 × 6 % = **300 clics / mois**

---

## Étape 4 — Analyse SERP

Pour chaque page prioritaire, analyser les 5 premiers résultats :

- angle dominant
- promesse
- mots déclencheurs
- longueur du title
- présence de chiffres ou d'année

---

## Étape 5 — Génération de nouveaux titles

**Règle** : 1 variable par test — jamais title + meta en même temps.

**Déclencheurs CTR (toujours au moins 1) :**

| Catégorie   | Exemples                           |
| ----------- | ---------------------------------- |
| Performance | rapide, performant, optimisé       |
| Gain        | guide, méthode, checklist          |
| Curiosité   | erreurs, pièges, secrets           |
| Concret     | étape par étape, complet, débutant |

**Exemple — page "maintenance wordpress" :**

| Type       | Title                                                          |
| ---------- | -------------------------------------------------------------- |
| Actuel     | Maintenance WordPress : guide complet                          |
| Variante 1 | Maintenance WordPress : guide complet (+ checklist)            |
| Variante 2 | Maintenance WordPress : la checklist indispensable             |
| Variante 3 | Maintenance WordPress : 7 erreurs à éviter                     |
| Variante 4 | Maintenance WordPress : méthode simple pour sécuriser ton site |
| Variante 5 | Maintenance WordPress : le guide pratique pour débuter         |

---

## Étape 6 — Test TDD

- Modifier : **title uniquement**
- Observation : **14 à 21 jours**
- Comparer : CTR / impressions / position

---

## Étape 7 — Décision

| Résultat     | Action                                     |
| ------------ | ------------------------------------------ |
| CTR augmente | Conserver + itérer sur la meta description |
| CTR stable   | Tester un angle différent                  |
| CTR baisse   | Revenir au title précédent                 |

---

## Pipeline complet

```text
GSC export (90j)
     ↓
Filtrage quick wins (pos 3-12 / imp >500 / CTR <3%)
     ↓
Score opportunité (impressions × delta CTR)
     ↓
Analyse SERP top 5
     ↓
Génération 3-5 variantes de title
     ↓
Test TDD (1 variable, 14-21 jours)
     ↓
Décision : conserver / pivoter / revenir
     ↓
Itération suivante
```

---

## Routine hebdomadaire (30 min)

1. Ouvrir GSC
2. Repérer 1 page sous-optimisée
3. Générer 3 variantes de title
4. Lancer le test (1 variante)
5. Noter résultat dans tableau de suivi

**Accumulation semaine après semaine.**

---

## Impact réel possible

+3 % CTR sur 80 000 impressions = **+2 400 clics / mois**

Sans écrire un seul article.
