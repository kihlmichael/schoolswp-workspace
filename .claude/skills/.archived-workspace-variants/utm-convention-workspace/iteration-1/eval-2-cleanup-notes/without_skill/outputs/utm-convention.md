# Convention UTM officielle — schoolsWP

> Document de référence. Toujours copier-coller les valeurs depuis ce fichier — ne jamais les saisir de mémoire.

---

## Règles générales

- **Casse** : tout en minuscules, sans exception (Google Analytics est sensible à la casse — `LinkedIn` et `linkedin` créent deux sources distinctes)
- **Séparateurs** : tirets `-` uniquement (jamais d'underscores, jamais d'espaces)
- **Encodage** : pas de caractères spéciaux, pas d'accents
- **Obligatoires** : `utm_source` + `utm_medium` + `utm_campaign` sur tous les liens externes trackés
- **Optionnels** : `utm_content` et `utm_term` — voir règles d'usage ci-dessous

---

## Paramètres : valeurs officielles

### `utm_source` — origine du trafic

| Canal                     | Valeur officielle | Notes                                 |
| ------------------------- | ----------------- | ------------------------------------- |
| Newsletter / emails       | `newsletter`      | Toujours `newsletter`, jamais `email` |
| LinkedIn                  | `linkedin`        | Minuscule, jamais `LinkedIn`          |
| YouTube                   | `youtube`         |                                       |
| ClickWhale (liens courts) | `clickwhale`      | Source = l'outil qui génère le lien   |
| ThemeForest (affiliés)    | `themeforest`     |                                       |

**Règle pour ClickWhale :** la source est `clickwhale` car c'est le point de départ du clic. Le lien court est l'outil de distribution, pas une destination. `lien-court` est trop vague et non actionnable dans les rapports.

---

### `utm_medium` — type de canal

| Canal               | Valeur officielle | Notes                                                                                         |
| ------------------- | ----------------- | --------------------------------------------------------------------------------------------- |
| Emails / newsletter | `email`           |                                                                                               |
| LinkedIn            | `social`          |                                                                                               |
| YouTube             | `video`           | Plus précis que `social` — permet de distinguer YouTube des réseaux sociaux dans les rapports |
| ClickWhale          | `lien-court`      |                                                                                               |
| Affiliés            | `affiliate`       | Jamais `affiliation` — `affiliate` est la valeur standard GA4                                 |

---

### `utm_campaign` — nom de la campagne

- **Format** : tirets uniquement — jamais d'underscores
- **Structure** : `[sujet]-[type]` ou `[sujet]-[date]` selon le contexte
- **Exemples corrects** : `lms-wordpress`, `formation-gutenberg`, `black-friday-2025`
- **Exemples incorrects** : `lms_wordpress`, `LMS WordPress`, `lmswordpress`

---

### `utm_content` — différencier les variantes

Utiliser quand **plusieurs liens pointent vers la même destination dans le même canal**.

**Cas d'usage typiques :**

- Deux boutons CTA dans un même email (ex: `cta-haut` vs `cta-bas`)
- Deux visuels différents dans une campagne LinkedIn (ex: `visuel-rouge` vs `visuel-bleu`)
- Deux emplacements dans une même page (ex: `sidebar` vs `footer`)

**Format** : tirets, minuscules — ex: `bouton-hero`, `lien-bio`, `encart-article`

Si tu n'as qu'un seul lien vers une destination dans un canal donné : ne pas renseigner `utm_content`.

---

### `utm_term` — mots-clés payants

Réservé aux campagnes **SEA / publicités payantes au CPC** (Google Ads, Meta Ads).

Sur schoolsWP : pas de SEA actuellement → **ne pas utiliser `utm_term`**.

---

## Liens internes dans les articles

**Non.** Ne jamais mettre d'UTM sur les liens internes (d'une page schoolsWP vers une autre page schoolsWP).

Raisons :

1. Les UTM réinitialisent la session dans GA4 — un visiteur organique devient "newsletter" si tu cliques sur un lien interne tagué
2. Ça fausse l'attribution source/medium sur toutes les pages en aval
3. Le maillage interne se mesure avec les rapports de pages et les flux de navigation, pas avec les UTM

Pour les liens internes, utiliser les rapports GA4 "Flux d'utilisateurs" ou un outil comme GSC.

---

## Tableau récapitulatif par canal

| Canal                     | source        | medium       | campaign       | content              | term |
| ------------------------- | ------------- | ------------ | -------------- | -------------------- | ---- |
| Newsletter                | `newsletter`  | `email`      | `nom-campagne` | si plusieurs CTA     | —    |
| LinkedIn                  | `linkedin`    | `social`     | `nom-campagne` | si plusieurs visuels | —    |
| YouTube                   | `youtube`     | `video`      | `nom-campagne` | si plusieurs liens   | —    |
| ClickWhale                | `clickwhale`  | `lien-court` | `nom-campagne` | optionnel            | —    |
| ThemeForest (affiliation) | `themeforest` | `affiliate`  | `nom-produit`  | optionnel            | —    |

---

## Exemples complets

```
# Email newsletter — article LMS
?utm_source=newsletter&utm_medium=email&utm_campaign=lms-wordpress

# LinkedIn — post avec deux variantes de lien
?utm_source=linkedin&utm_medium=social&utm_campaign=formation-gutenberg&utm_content=lien-bio
?utm_source=linkedin&utm_medium=social&utm_campaign=formation-gutenberg&utm_content=lien-post

# YouTube — description de vidéo
?utm_source=youtube&utm_medium=video&utm_campaign=tutoliels-woocommerce

# ClickWhale — lien court vers page formation
?utm_source=clickwhale&utm_medium=lien-court&utm_campaign=formation-lms

# ThemeForest — lien affilié
?utm_source=themeforest&utm_medium=affiliate&utm_campaign=avada-theme
```

---

## Points tranchés — résumé des décisions

| Question                                                | Décision                                      |
| ------------------------------------------------------- | --------------------------------------------- |
| `newsletter` ou `email` pour source ?                   | `newsletter`                                  |
| `LinkedIn` ou `linkedin` ?                              | `linkedin` (minuscule)                        |
| YouTube : `video` ou `social` pour medium ?             | `video`                                       |
| ClickWhale : `clickwhale` ou `lien-court` pour source ? | `clickwhale` (source) / `lien-court` (medium) |
| Affiliés : `affiliation` ou `affiliate` ?               | `affiliate`                                   |
| Tirets ou underscores dans campaign ?                   | tirets `-` uniquement                         |
| UTM sur liens internes ?                                | Non, jamais                                   |
| Utiliser `utm_term` ?                                   | Non (pas de SEA)                              |
