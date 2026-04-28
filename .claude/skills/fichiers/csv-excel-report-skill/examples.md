# Exemples d'usage

## Exemple 1 — Ventes e-commerce

**Colonnes typiques :** `date`, `product`, `category`, `orders`, `revenue`, `country`

**Prompt simple :**

```
Analyse ce fichier de ventes et produis un rapport complet.
```

**Attendus dans le rapport :**

- évolution du CA sur la période
- top produits / flop produits
- pays les plus rentables
- anomalies de période (pics, creux)
- top 5 / flop 5 produits par revenue
- recommandations concrètes pour les ventes

---

## Exemple 2 — CRM / Commercial

**Colonnes typiques :** `lead_source`, `sales_rep`, `stage`, `deal_value`, `created_at`, `won`

**Prompt enrichi :**

```
Analyse ce fichier CRM. Je veux comprendre les meilleures sources de leads,
les points de blocage dans le pipeline et les performances par commercial.
```

**Attendus dans le rapport :**

- volume de leads et taux de conversion global
- taux de gain par source
- sources les plus rentables
- étapes de blocage dans le pipeline
- top 5 / flop 5 sources ou commerciaux
- recommandations CRM

---

## Exemple 3 — Marketing / Analytics

**Colonnes typiques :** `date`, `channel`, `campaign`, `sessions`, `clicks`, `conversions`, `revenue`

**Prompt :**

```
Analyse ce fichier marketing. Identifie les canaux et campagnes les plus performants
et ceux qui sous-performent. Termine par des recommandations simples.
```

**Attendus dans le rapport :**

- canaux les plus performants (sessions, conversions, revenue)
- campagnes faibles
- taux de conversion par canal
- anomalies de période
- top 5 / flop 5 campagnes
- recommandations média

---

## Exemple 4 — Finance / Gestion

**Colonnes typiques :** `date`, `category`, `amount`, `type` (dépense/recette), `department`

**Prompt :**

```
Analyse ce tableau financier. Focus sur les postes dominants et les dérives inhabituelles.
```

**Attendus dans le rapport :**

- répartition revenus vs dépenses
- postes de coûts dominants
- dérives ou pics inhabituels
- concentration des dépenses
- top 5 postes par montant
- recommandations de suivi

---

## Exemple 5 — Support / Opérations

**Colonnes typiques :** `date`, `ticket_type`, `priority`, `resolution_time`, `agent`, `status`

**Prompt :**

```
Analyse ce fichier de tickets support. Je veux voir les catégories problématiques
et les délais de résolution.
```

**Attendus dans le rapport :**

- volume de tickets par type
- délais de résolution moyens
- catégories à fort volume ou long délai
- anomalies
- top 5 catégories par volume
- recommandations opérationnelles
