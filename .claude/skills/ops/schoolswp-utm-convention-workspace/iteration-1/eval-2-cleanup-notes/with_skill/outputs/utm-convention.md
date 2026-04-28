# Convention UTM officielle schoolsWP — v1.0 (mars 2026)

---

## 1. Règles de base

1. **Tout en minuscules** — GA4 est sensible à la casse. `Newsletter` et `newsletter` sont deux sources distinctes dans tes rapports.
2. **Tirets uniquement** — jamais d'underscores, jamais d'espaces. `lms-wordpress` et non `lms_wordpress`.
3. **Sans accents** — `etude-de-cas`, pas `étude-de-cas`.
4. **Valeurs courtes** — max 30 caractères par paramètre, lisibles à l'œil.
5. **Une valeur = un sens** — cohérence absolue. Si tu utilises `newsletter` pour les emails, tu n'utilises jamais `email` pour la même chose.
6. **Jamais sur les liens internes** — les UTMs sur le maillage interne d'un article écrasent la source d'origine dans GA4 et faussent toute l'attribution.
7. **Toujours taguer les liens entrants externes** — email, réseaux sociaux, affiliés, campagnes pub : utm_source + utm_medium + utm_campaign sont obligatoires.

---

## 2. Paramètres UTM

### utm_source — d'où vient le visiteur ?

Identifie **qui** envoie le trafic. C'est l'origine.

**Valeurs officielles schoolsWP :**

| Valeur                | Contexte                                                  |
| --------------------- | --------------------------------------------------------- |
| `newsletter`          | Emails envoyés via FluentCRM (newsletters, séquences)     |
| `linkedin`            | Publications et profil LinkedIn                           |
| `youtube`             | Descriptions de vidéos YouTube, fiches YouTube            |
| `instagram`           | Bio, stories, liens Instagram                             |
| `facebook`            | Posts et groupes Facebook                                 |
| `google`              | Trafic Google Ads (CPC)                                   |
| `bing`                | Trafic Bing Ads                                           |
| `clickwhale`          | Short links permanents distribués via ClickWhale          |
| `themeforest`         | Liens affiliés ThemeForest                                |
| `[nom-du-partenaire]` | Autres affiliés/partenaires (ex: `elegantthemes`, `wpml`) |

**Exemples :**

- Lien dans ta newsletter hebdo → `utm_source=newsletter`
- Lien dans un post LinkedIn → `utm_source=linkedin`
- Lien affilié ThemeForest dans un article → `utm_source=themeforest`

---

### utm_medium — comment le trafic arrive ?

Identifie **le canal** de diffusion. C'est le type de lien.

**Valeurs officielles schoolsWP :**

| Valeur       | Contexte                                                    |
| ------------ | ----------------------------------------------------------- |
| `email`      | Tous les envois email (newsletters, séquences automatiques) |
| `social`     | Tous les réseaux sociaux organiques                         |
| `video`      | Liens dans les descriptions de vidéos YouTube               |
| `short-link` | Liens courts ClickWhale distribués en dehors du site        |
| `affiliate`  | Liens d'affiliation partenaires                             |
| `cpc`        | Campagnes publicitaires payantes                            |
| `referral`   | Mentions et articles invités sur d'autres sites             |
| `cta`        | CTAs internes sur schoolswp.com (boutons, banners)          |

**Exemples :**

- Email FluentCRM → `utm_medium=email`
- Post LinkedIn → `utm_medium=social`
- Vidéo YouTube → `utm_medium=video`
- Short link ClickWhale → `utm_medium=short-link`
- Lien ThemeForest → `utm_medium=affiliate`

---

### utm_campaign — pourquoi ce lien existe ?

Identifie **la campagne ou la raison** de l'envoi. Permet de regrouper plusieurs liens d'une même action.

**Format recommandé :** `[sujet]-[mois-annee]` ou `[nom-serie]`

**Valeurs exemples schoolsWP :**

```
newsletter-hebdo
lms-wordpress-mars-2026
launch-authority-system
black-friday-2024
guide-tutor-lms
comparatif-lms
```

**Règle :** toujours en tirets, jamais en underscores. `lms-wordpress` et non `lms_wordpress`.

---

### utm_content — quel lien exactement dans la campagne ?

Permet de **différencier plusieurs liens** qui pointent vers la même URL dans une même campagne. Utile quand tu as plusieurs CTAs dans un même email ou article.

**Valeurs exemples schoolsWP :**

```
cta-header
cta-footer
bouton-principal
lien-texte
image-banner
vignette-youtube
lien-bio
```

**Quand l'utiliser :** dès que tu as 2 liens ou plus vers la même page dans un même email ou une même publication. Sinon, tu peux l'omettre.

---

### utm_term — quel mot-clé cible ?

Réservé aux **campagnes payantes** pour identifier le mot-clé qui a déclenché l'affichage.

**Quand l'utiliser :** uniquement sur Google Ads ou Bing Ads. Ne pas utiliser sur les emails ou les réseaux sociaux.

**Valeurs exemples schoolsWP :**

```
lms-wordpress
tutor-lms
crm-wordpress
learndash-prix
```

---

## 3. Convention officielle schoolsWP

### Format standard

```
?utm_source=[source]&utm_medium=[medium]&utm_campaign=[campaign]&utm_content=[content]
```

`utm_term` est optionnel, uniquement pour les campagnes payantes.

### Tableau de référence rapide

| Source         | Medium       | Quand l'utiliser                             |
| -------------- | ------------ | -------------------------------------------- |
| `newsletter`   | `email`      | Emails FluentCRM (newsletters, séquences)    |
| `linkedin`     | `social`     | Posts et profil LinkedIn                     |
| `youtube`      | `video`      | Descriptions de vidéos YouTube               |
| `instagram`    | `social`     | Bio et stories Instagram                     |
| `clickwhale`   | `short-link` | Short links permanents distribués en externe |
| `themeforest`  | `affiliate`  | Liens affiliés ThemeForest dans les articles |
| `[partenaire]` | `affiliate`  | Autres liens affiliés partenaires            |
| `google`       | `cpc`        | Google Ads                                   |

---

## 4. Cas concrets

### Cas 1 — Newsletter FluentCRM (lien principal)

```
Contexte : lien vers l'article "TutorLMS vs LearnDash" dans la newsletter hebdo de mars 2026
URL : https://schoolswp.com/tutor-lms-vs-learndash/?utm_source=newsletter&utm_medium=email&utm_campaign=newsletter-hebdo&utm_content=lien-principal
Explication : source=newsletter (FluentCRM), medium=email (canal email), campaign=newsletter-hebdo (série récurrente), content=lien-principal (distingue ce lien d'un éventuel second lien dans le même email)
```

### Cas 2 — LinkedIn organique

```
Contexte : publication LinkedIn avec lien vers le guide LMS gratuit
URL : https://schoolswp.com/guide-lms-wordpress/?utm_source=linkedin&utm_medium=social&utm_campaign=guide-lms-mars-2026&utm_content=lien-post
Explication : source=linkedin, medium=social (réseau social organique, pas payant), campaign identifie la campagne de diffusion du guide
```

### Cas 3 — Vidéo YouTube (description)

```
Contexte : lien en description d'une vidéo "Comment choisir son LMS WordPress"
URL : https://schoolswp.com/choisir-lms-wordpress/?utm_source=youtube&utm_medium=video&utm_campaign=video-lms-mars-2026&utm_content=description
Explication : source=youtube, medium=video (le canal est une vidéo, pas un post social classique), content=description pour distinguer d'un éventuel lien en commentaire épinglé
```

### Cas 4 — Short link ClickWhale (bio Instagram)

```
Contexte : short link permanent "swp.fr/guide-lms" dans la bio Instagram, redirige vers le guide LMS
URL configurée dans ClickWhale : https://schoolswp.com/guide-lms-wordpress/?utm_source=clickwhale&utm_medium=short-link&utm_campaign=bio-instagram&utm_content=bio-link
Explication : source=clickwhale (c'est l'outil qui gère le lien), medium=short-link, campaign=bio-instagram identifie l'emplacement permanent
```

### Cas 5 — Lien affilié ThemeForest dans un article

```
Contexte : lien affilié vers un thème WordPress dans l'article "Meilleurs thèmes LMS"
URL : https://themeforest.net/item/education-wp/...?utm_source=themeforest&utm_medium=affiliate&utm_campaign=article-themes-lms&utm_content=lien-texte
Explication : source=themeforest (le partenaire), medium=affiliate, campaign identifie l'article source, content=lien-texte (vs un éventuel bouton ou image)
```

### Cas 6 — CTA interne sur schoolswp.com (bouton dans un article)

```
Contexte : bouton "Télécharger le guide gratuit" dans le footer d'un article sur schoolswp.com
URL : https://schoolswp.com/guide-lms-wordpress/?utm_source=schoolswp&utm_medium=cta&utm_campaign=guide-lms&utm_content=cta-footer-article
Explication : les CTAs internes sur le propre site peuvent être trackés avec source=schoolswp pour mesurer les conversions internes — c'est le seul cas légitime d'UTM sur un lien interne (bouton CTA, pas lien de maillage)
```

### Cas 7 — Séquence email automatique FluentCRM

```
Contexte : email J+3 d'une séquence de bienvenue, lien vers l'article "Démarrer avec TutorLMS"
URL : https://schoolswp.com/demarrer-tutor-lms/?utm_source=newsletter&utm_medium=email&utm_campaign=sequence-bienvenue&utm_content=email-j3
Explication : même source/medium que la newsletter, campaign=sequence-bienvenue identifie la séquence, content=email-j3 permet de savoir quel email de la séquence convertit le mieux
```

---

## 5. Quand mettre des UTMs

Les UTMs sont **obligatoires** dans ces contextes :

- Liens dans les emails (newsletters FluentCRM, séquences automatiques)
- Publications sur les réseaux sociaux (bio, posts, stories)
- Liens affiliés et partenariats dans les articles
- Campagnes publicitaires (Google Ads, Meta Ads)
- Short links ClickWhale distribués en externe (bio, stories, QR codes)
- Collaborations et articles invités sur d'autres sites
- Liens dans les descriptions de vidéos YouTube

---

## 6. Quand NE PAS mettre des UTMs

Les UTMs sont **contre-productifs** dans ces contextes :

- **Liens de maillage interne dans les articles** — un lien d'un article vers un autre article sur schoolswp.com n'a pas besoin d'UTM. GA4 considérerait la session comme une nouvelle session avec `source=schoolswp`, écrasant la vraie source d'origine (ex: LinkedIn).
- **Menu de navigation, sidebar, footer de navigation** — même raison : casse l'attribution.
- **Pages de paiement vers confirmation de commande** — les UTMs sur ces liens cassent le tracking e-commerce.
- **Redirections techniques** — les UTMs sur les URLs de redirection créent des doublons et des conflits d'attribution.

**Règle à retenir :** si le lien reste sur schoolswp.com et que ce n'est pas un bouton CTA mesurable, pas d'UTM.

---

## 7. Erreurs à éviter

1. **Majuscules dans les valeurs** — `LinkedIn` et `linkedin` sont deux sources différentes dans GA4. Toujours minuscules.
2. **Underscores dans les noms de campagne** — `lms_wordpress` sera affiché comme `lms wordpress` dans certains outils. Utiliser `lms-wordpress`.
3. **Valeurs incohérentes pour la même source** — choisir `newsletter` et s'y tenir. Ne jamais alterner avec `email` pour désigner la même source.
4. **Oublier utm_medium** — `utm_source` seul ne suffit pas pour l'attribution dans GA4. Source + Medium sont toujours ensemble.
5. **Taguer les liens de maillage interne** — l'erreur la plus fréquente. Elle fausse toute l'attribution du trafic.
6. **Valeurs trop longues ou avec des caractères spéciaux** — éviter les `?`, `&`, `=` dans les valeurs. Encoder si nécessaire.
7. **Oublier utm_content sur les emails avec plusieurs liens** — sans `utm_content`, tu ne sais pas quel lien dans l'email a converti.
8. **Utiliser utm_term hors campagnes payantes** — ce paramètre est réservé aux mots-clés publicitaires. Sur du social ou de l'email, il n'a aucun sens.

---

## 8. Recommandation simple à retenir

> **Source = qui t'envoie. Medium = comment. Campaign = pourquoi.**
>
> Si tu doutes : est-ce que ce lien vient de l'extérieur de schoolswp.com ? Oui → UTM obligatoire. Non (maillage interne, navigation) → pas d'UTM. La seule exception : les boutons CTA internes que tu veux mesurer explicitement.

---

## Points tranchés

Les décisions suivantes ont été prises en tranchant les zones floues de tes notes :

1. **newsletter vs email pour les sources email** → tranché : `utm_source=newsletter` (identifie l'outil FluentCRM et la nature du contenu), `utm_medium=email` (identifie le canal). Les deux coexistent mais à des endroits différents.

2. **LinkedIn avec ou sans majuscule** → tranché : `utm_source=linkedin` — tout en minuscules, sans exception. GA4 est case-sensitive.

3. **YouTube : medium=video ou social ?** → tranché : `utm_medium=video`. YouTube est une plateforme vidéo, pas un réseau social classique. Cela permet de distinguer le trafic YouTube du trafic LinkedIn/Instagram dans tes rapports.

4. **ClickWhale : source=clickwhale ou source=lien-court ?** → tranché : `utm_source=clickwhale`. C'est le nom de l'outil qui gère le lien. `lien-court` décrit le format, pas la source. Pour le medium, utiliser `utm_medium=short-link`.

5. **Affiliés ThemeForest : medium=affiliation ou affiliate ?** → tranché : `utm_medium=affiliate` (terme standard GA4/marketing). `affiliation` avec accent ou graphie variable est à éviter.

6. **Tirets ou underscores dans les campagnes** → tranché : tirets uniquement. `lms-wordpress` partout, jamais `lms_wordpress`.

7. **utm_content : quand l'utiliser ?** → tranché : à utiliser dès qu'il y a 2 liens ou plus vers la même URL dans un même email ou publication. Sinon optionnel mais recommandé pour les emails.

8. **utm_term : quand l'utiliser ?** → tranché : réservé aux campagnes payantes (Google Ads, Bing Ads) uniquement. Ne pas utiliser sur les emails, réseaux sociaux ou liens affiliés.

9. **UTMs sur les liens internes dans les articles** → tranché : non, jamais sur le maillage interne. Seule exception : les boutons CTA internes explicitement mesurés (`utm_source=schoolswp&utm_medium=cta`).
