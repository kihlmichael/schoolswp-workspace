# Convention UTM — Emails FluentCRM — schoolsWP

## Principes généraux

- Tout en minuscules, sans accents, sans espaces (utiliser des tirets `-`)
- Valeurs courtes et lisibles dans GA4
- `utm_medium` toujours `email` pour tous les emails sortants
- `utm_source` identifie l'expéditeur / la liste (ici toujours `fluentcrm`)
- `utm_campaign` identifie la campagne ou la séquence
- `utm_content` différencie les liens dans un même email

---

## Structure de base

```
utm_source=fluentcrm
utm_medium=email
utm_campaign=[type]-[slug]
utm_content=[position]-[descriptif]
```

---

## 1. Newsletter hebdo "WP Insights" (envoi manuel, chaque lundi)

**Logique** : campagne récurrente — inclure la date ou le numéro de semaine pour pouvoir comparer semaine par semaine dans GA4.

```
utm_source=fluentcrm
utm_medium=email
utm_campaign=newsletter-wp-insights-2026-w11
utm_content=cta-principal
```

| Paramètre      | Valeur                              | Explication                                           |
| -------------- | ----------------------------------- | ----------------------------------------------------- |
| `utm_source`   | `fluentcrm`                         | Origine : liste FluentCRM                             |
| `utm_medium`   | `email`                             | Canal : email                                         |
| `utm_campaign` | `newsletter-wp-insights-2026-w11`   | Identifie le numéro de semaine                        |
| `utm_content`  | `cta-principal` / `lien-secondaire` | Distingue les liens dans l'email (voir §4 ci-dessous) |

**Exemple de lien complet :**

```
https://schoolswp.com/article-lms/?utm_source=fluentcrm&utm_medium=email&utm_campaign=newsletter-wp-insights-2026-w11&utm_content=cta-principal
```

---

## 2. Séquences automatisées — Lead magnet "Guide LMS WordPress"

**Logique** : séquence fixe avec position du mail dans la séquence. Ne pas inclure de date (envoi décalé selon inscription de chaque lead).

```
utm_source=fluentcrm
utm_medium=email
utm_campaign=seq-guide-lms
utm_content=email-[n]-[descriptif]
```

| Paramètre      | Valeur                   | Explication                                 |
| -------------- | ------------------------ | ------------------------------------------- |
| `utm_source`   | `fluentcrm`              | Origine : FluentCRM                         |
| `utm_medium`   | `email`                  | Canal                                       |
| `utm_campaign` | `seq-guide-lms`          | Identifie la séquence (slug du lead magnet) |
| `utm_content`  | `email-01-cta-principal` | Position dans la séquence + type de lien    |

**Exemples :**

```
# Email 1 — lien principal (vers la ressource)
utm_campaign=seq-guide-lms&utm_content=email-01-cta-principal

# Email 3 — lien de nurturing (vers un article)
utm_campaign=seq-guide-lms&utm_content=email-03-lien-article

# Email 5 — lien de conversion (vers une offre)
utm_campaign=seq-guide-lms&utm_content=email-05-cta-offre
```

---

## 3. Emails de relance — Abandonnistes page de vente "Authority System"

**Logique** : séquence de relance comportementale. Identifier clairement le produit et le numéro de relance.

```
utm_source=fluentcrm
utm_medium=email
utm_campaign=relance-authority-system
utm_content=relance-[n]-[angle]
```

| Paramètre      | Valeur                                             | Explication                                    |
| -------------- | -------------------------------------------------- | ---------------------------------------------- |
| `utm_source`   | `fluentcrm`                                        | Origine                                        |
| `utm_medium`   | `email`                                            | Canal                                          |
| `utm_campaign` | `relance-authority-system`                         | Identifie le produit + type d'action (relance) |
| `utm_content`  | `relance-01-urgence` / `relance-02-preuve-sociale` | Numéro + angle de la relance                   |

**Exemples :**

```
# Relance J+1 — lien principal vers la page de vente
utm_campaign=relance-authority-system&utm_content=relance-01-cta-principal

# Relance J+3 — lien avec angle preuve sociale (témoignage)
utm_campaign=relance-authority-system&utm_content=relance-02-temoignage

# Relance J+7 — dernière chance, lien principal
utm_campaign=relance-authority-system&utm_content=relance-03-derniere-chance
```

---

## 4. Lien principal vs liens secondaires dans un même email

**Oui, il faut taguer différemment.** Les raisons :

1. GA4 agrège tous les clics d'un même email — sans différenciation, tu ne sais pas quel lien convertit
2. Un email contient souvent 2 à 4 liens : CTA principal, lien de contenu, lien PS, lien de désabonnement (ne pas taguer celui-ci)
3. La valeur des `utm_content` distincts te permet d'optimiser le placement des CTA

**Convention `utm_content` pour les positions :**

| Valeur `utm_content` | Usage                                              |
| -------------------- | -------------------------------------------------- |
| `cta-principal`      | Bouton ou lien principal, premier CTA visible      |
| `lien-texte`         | Lien inséré dans le corps du texte (pas un bouton) |
| `cta-secondaire`     | Second CTA ou lien répété plus bas                 |
| `ps-lien`            | Lien dans le PS (souvent haute performance)        |
| `image-header`       | Lien sur l'image d'en-tête si présente             |

**Exemple pour un email de la séquence Guide LMS avec plusieurs liens :**

```
# Lien 1 — CTA principal (bouton)
utm_campaign=seq-guide-lms&utm_content=email-02-cta-principal

# Lien 2 — lien dans le corps du texte
utm_campaign=seq-guide-lms&utm_content=email-02-lien-texte

# Lien 3 — PS
utm_campaign=seq-guide-lms&utm_content=email-02-ps-lien
```

---

## Tableau récapitulatif des 3 types

| Type d'email             | `utm_source` | `utm_medium` | `utm_campaign`                      | `utm_content` (principal)    |
| ------------------------ | ------------ | ------------ | ----------------------------------- | ---------------------------- |
| Newsletter WP Insights   | `fluentcrm`  | `email`      | `newsletter-wp-insights-2026-w[nn]` | `cta-principal`              |
| Séquence Guide LMS       | `fluentcrm`  | `email`      | `seq-guide-lms`                     | `email-[nn]-cta-principal`   |
| Relance Authority System | `fluentcrm`  | `email`      | `relance-authority-system`          | `relance-[nn]-cta-principal` |

---

## Notes d'implémentation FluentCRM

- Ajouter les UTMs directement dans l'éditeur de lien de FluentCRM (ne pas utiliser les raccourcis de tracking natifs si tu veux garder le contrôle total sur les valeurs)
- Si FluentCRM génère ses propres paramètres de tracking (`_fc_...`), les UTMs GA4 coexistent sans conflit
- Créer un segment GA4 filtré sur `utm_medium = email` pour analyser tous les emails ensemble, puis affiner par `utm_campaign`
- Pour les séquences, créer un rapport comparatif par `utm_content` pour identifier à quel email de la séquence les leads convertissent
