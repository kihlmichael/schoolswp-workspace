# Convention UTM officielle schoolsWP — v1.0 — mars 2026

**Site** : schoolswp.com
**Outils de tracking** : GA4, ClickWhale, FluentCRM
**Canaux actifs** : LinkedIn, YouTube, Instagram, newsletters, liens affiliés
**Auteur** : Michael KIHL — contact@michaelkihl.fr

---

## 1. Regles de base

1. **Tout en minuscules, sans exception.** GA4 est sensible a la casse — "LinkedIn" et "linkedin" sont deux sources distinctes dans les rapports. Toujours minuscules.
2. **Tirets uniquement.** Jamais d'underscores, jamais d'espaces, jamais d'accents dans les valeurs UTM. Un espace devient `%20` dans l'URL et casse la lisibilite des rapports.
3. **Sans accents.** Les valeurs UTM ne contiennent pas de caracteres accentues : "newsletter" pas "newsletter avec accent", "etude-de-cas" pas "étude-de-cas".
4. **Source + Medium sont obligatoires ensemble.** Un lien tague avec uniquement `utm_source` sans `utm_medium` produit une attribution incomplete dans GA4. Les deux vont toujours de pair.
5. **Coherence absolue : une valeur = un sens, toujours.** Si "linkedin" est la source pour LinkedIn, cette valeur est utilisee partout, pour toujours. Jamais "linked-in", jamais "LinkedIn", jamais "li".
6. **Jamais d'UTMs sur les liens internes de navigation.** Un UTM sur un lien interne ecrase la source d'origine dans GA4 — un visiteur venu de LinkedIn et qui clique sur un lien interne tague se retrouve comptabilise comme une nouvelle session, faussant toute l'attribution.
7. **Valeurs courtes et lisibles.** Maximum 30 caracteres par valeur. Les UTMs apparaissent dans les rapports GA4 — une valeur claire facilite l'analyse sans tableau de correspondance.

---

## 2. Parametres UTM

### utm_source — D'ou vient le visiteur ?

**Role** : identifie l'origine du trafic, c'est-a-dire la plateforme ou le systeme qui envoie le visiteur vers schoolswp.com.

**Valeurs recommandees pour schoolsWP :**

| Valeur             | Contexte d'utilisation                                                 |
| ------------------ | ---------------------------------------------------------------------- |
| `newsletter`       | Emails envoyes via FluentCRM (newsletters hebdo, sequences)            |
| `linkedin`         | Publications organiques LinkedIn (posts, articles, commentaires)       |
| `youtube`          | Descriptions de videos YouTube, liens en commentaire epingle           |
| `instagram`        | Bio Instagram, liens en stories ou reels via ClickWhale                |
| `google`           | Campagnes Google Ads (si actives)                                      |
| `themforest`       | Liens affilies ThemeForest                                             |
| `affiliation`      | Liens affilies plugins WordPress non nommes individuellement           |
| `[nom-partenaire]` | Partenariat specifique (ex: `tutorpro`, `learndash`, `rankmath`)       |
| `clickwhale`       | Short links ClickWhale distribues sans source identifiable precisement |

**Exemples concrets :**

- Post LinkedIn pointant vers un article : `utm_source=linkedin`
- Email FluentCRM sequence "LMS en 5 jours" : `utm_source=newsletter`
- Description video YouTube "Tutoriel TutorLMS" : `utm_source=youtube`
- Lien affilie ThemeForest dans un article : `utm_source=themforest`

---

### utm_medium — Comment le visiteur arrive ?

**Role** : identifie le canal ou le type de support qui vehicule le lien — pas la plateforme, mais le mecanisme de diffusion.

**Valeurs recommandees pour schoolsWP :**

| Valeur       | Contexte d'utilisation                                                                   |
| ------------ | ---------------------------------------------------------------------------------------- |
| `email`      | Tout lien dans un email (newsletter, sequence, email transactionnel)                     |
| `social`     | Publications organiques sur les reseaux sociaux                                          |
| `affiliate`  | Liens dans le cadre d'un programme d'affiliation                                         |
| `short-link` | Short links ClickWhale distribues en externe                                             |
| `cpc`        | Liens dans des campagnes publicitaires payantes                                          |
| `referral`   | Liens depuis un site partenaire ou article invite                                        |
| `cta`        | Boutons ou CTAs instrumentes dans les articles ou pages du propre site (CTAs trackables) |

**Attention** : `social` est le medium pour tous les reseaux sociaux organiques. `email` couvre toutes les communications FluentCRM. On ne melange pas la source et le medium.

**Exemples concrets :**

- LinkedIn (organique) : `utm_medium=social`
- Newsletter FluentCRM : `utm_medium=email`
- Bio Instagram via ClickWhale : `utm_medium=short-link`
- Lien affilie plugin WordPress : `utm_medium=affiliate`

---

### utm_campaign — Quelle campagne ou serie ?

**Role** : identifie la campagne marketing, la serie de contenu ou l'initiative specifique qui motive ce lien. Permet de regrouper plusieurs liens d'une meme action dans GA4.

**Format recommande :** `[sujet]-[mois-annee]` pour les campagnes ponctuelles, `[nom-serie]` pour les contenus permanents.

**Valeurs recommandees pour schoolsWP :**

| Valeur                         | Contexte d'utilisation                                       |
| ------------------------------ | ------------------------------------------------------------ |
| `newsletter-hebdo`             | Newsletter reguliere hebdomadaire                            |
| `lms-wordpress-[mois]-[annee]` | Campagne autour du sujet LMS (ex: `lms-wordpress-mars-2026`) |
| `guide-fluentcrm`              | Guide ou ressource permanente FluentCRM                      |
| `black-friday-[annee]`         | Campagne Black Friday                                        |
| `launch-[nom-produit]`         | Lancement d'un produit ou service                            |
| `serie-lms-5-jours`            | Sequence email automatisee de 5 jours                        |
| `bio-instagram`                | Lien permanent en bio Instagram                              |
| `partenariat-[nom]`            | Campagne affiliation ou partenariat specifique               |

**Exemples concrets :**

- Newsletter du 10 mars 2026 : `utm_campaign=newsletter-hebdo`
- Article sur TutorLMS publie en mars 2026 : `utm_campaign=lms-wordpress-mars-2026`
- Lien bio Instagram permanent : `utm_campaign=bio-instagram`
- Sequence email "LMS en 5 jours" : `utm_campaign=serie-lms-5-jours`

---

### utm_content — Quel lien specifique dans la campagne ?

**Role** : differencie plusieurs liens ou CTAs au sein d'une meme campagne. Indispensable quand une newsletter ou un article contient plusieurs liens pointant vers la meme destination.

**Valeurs recommandees pour schoolsWP :**

| Valeur              | Contexte d'utilisation                        |
| ------------------- | --------------------------------------------- |
| `cta-header`        | CTA en debut d'article ou d'email             |
| `cta-footer`        | CTA en fin d'article ou d'email               |
| `bouton-principal`  | Bouton CTA principal (visuellement prominent) |
| `lien-texte`        | Lien hypertexte dans le corps du contenu      |
| `image-banner`      | Lien sur une image ou banniere                |
| `vignette-youtube`  | Lien sur une vignette ou miniature YouTube    |
| `lien-bio`          | Lien unique en bio de reseau social           |
| `description-video` | Lien dans la description d'une video YouTube  |
| `email-p1`          | Premier lien d'un email (quand on numerate)   |
| `email-p2`          | Deuxieme lien d'un email                      |

**Exemples concrets :**

- Deux liens dans une newsletter vers le meme article : `utm_content=cta-header` et `utm_content=cta-footer`
- Lien image vs lien texte dans un post LinkedIn : `utm_content=image-banner` vs `utm_content=lien-texte`
- CTA bouton en bas d'un article de blog : `utm_content=bouton-principal`

---

### utm_term — Quel mot-cle cible ?

**Role** : identifie le mot-cle cible, principalement utilise dans les campagnes Google Ads pour distinguer les annonces par mot-cle. Optionnel pour les autres canaux.

**Regle schoolsWP** : utm_term est reserve aux campagnes publicitaires payantes. Il n'est pas utilise systematiquement sur les liens organiques, newsletters ou reseaux sociaux — cela surchargerait les URLs sans valeur analytique.

**Valeurs de reference pour schoolsWP (si campagnes Google Ads) :**

```
lms-wordpress | tutor-lms-avis | learndash-vs-tutorlms | fluentcrm-avis |
crm-wordpress | formation-wordpress | rankmath-pro
```

---

## 3. Convention officielle recommandee schoolsWP

### Format standard

```
https://schoolswp.com/[slug-page]?utm_source=[source]&utm_medium=[medium]&utm_campaign=[campaign]&utm_content=[content]
```

`utm_term` est **optionnel** — a ajouter uniquement pour les campagnes payantes.

### Tableau de correspondance source / medium

| Canal                          | utm_source         | utm_medium   | Notes                                                                |
| ------------------------------ | ------------------ | ------------ | -------------------------------------------------------------------- |
| Newsletter FluentCRM           | `newsletter`       | `email`      | Toujours les deux                                                    |
| Sequence email FluentCRM       | `newsletter`       | `email`      | Meme valeur que newsletter                                           |
| Publication LinkedIn           | `linkedin`         | `social`     | Organique uniquement                                                 |
| Description YouTube            | `youtube`          | `social`     | Organique                                                            |
| Bio Instagram (ClickWhale)     | `instagram`        | `short-link` | Via ClickWhale                                                       |
| Lien affilie ThemeForest       | `themforest`       | `affiliate`  | Dans articles                                                        |
| Lien affilie plugin WordPress  | `affiliation`      | `affiliate`  | Ou `[nom-plugin]` si trackable individuellement                      |
| Partenaire nomme               | `[nom-partenaire]` | `referral`   | Ex: `rankmath`, `learndash`                                          |
| CTA article (interne tracking) | `schoolswp`        | `cta`        | Uniquement pour CTAs d'articles instrumentes, jamais pour navigation |

### Ordre des parametres

Toujours respecter cet ordre dans l'URL :

1. `utm_source`
2. `utm_medium`
3. `utm_campaign`
4. `utm_content`
5. `utm_term` (si applicable)

---

## 4. Cas concrets

### Cas 1 — CTA interne : bouton "Telecharger le guide" en footer d'article

**Contexte :** Un article sur TutorLMS contient un bouton CTA en bas de page invitant a telecharger un guide gratuit. Ce CTA est instrumente pour mesurer les clics depuis le contenu.

```
URL complete :
https://schoolswp.com/guide-tutor-lms?utm_source=schoolswp&utm_medium=cta&utm_campaign=guide-tutor-lms&utm_content=cta-footer

Explication :
- source=schoolswp : le trafic vient du propre site (CTA interne instrumente)
- medium=cta : il s'agit d'un bouton d'action dans le contenu
- campaign=guide-tutor-lms : identifie la ressource promue
- content=cta-footer : precise que c'est le CTA en pied d'article (utile si un cta-header existe aussi)
```

---

### Cas 2 — Newsletter FluentCRM : lien principal dans la newsletter hebdomadaire

**Contexte :** La newsletter du lundi 10 mars 2026 met en avant un article sur FluentCRM. Le lien principal dans l'email pointe vers l'article.

```
URL complete :
https://schoolswp.com/fluentcrm-avis?utm_source=newsletter&utm_medium=email&utm_campaign=newsletter-hebdo&utm_content=lien-texte

Explication :
- source=newsletter : l'email est envoye depuis FluentCRM, la source est la newsletter
- medium=email : canal email
- campaign=newsletter-hebdo : campagne recurrente (pas de date car hebdo regulier)
- content=lien-texte : c'est un lien dans le corps du texte, pas un bouton
```

---

### Cas 3 — LinkedIn : lien dans une publication organique

**Contexte :** Un post LinkedIn presente un comparatif TutorLMS vs LearnDash et renvoie vers l'article sur schoolswp.com.

```
URL complete :
https://schoolswp.com/tutor-lms-vs-learndash?utm_source=linkedin&utm_medium=social&utm_campaign=lms-wordpress-mars-2026&utm_content=lien-post

Explication :
- source=linkedin : la plateforme d'origine est LinkedIn
- medium=social : canal reseau social organique
- campaign=lms-wordpress-mars-2026 : rattache a la campagne editoriale LMS du mois
- content=lien-post : le lien est dans le corps du post LinkedIn
```

---

### Cas 4 — ClickWhale short link : lien court permanent pour bio Instagram

**Contexte :** Le lien en bio Instagram pointe en permanence vers la page de ressources gratuites de schoolswp.com. Il est gere via ClickWhale pour permettre la modification de la destination sans changer l'URL courte.

```
URL de destination (configuree dans ClickWhale) :
https://schoolswp.com/ressources-gratuites?utm_source=instagram&utm_medium=short-link&utm_campaign=bio-instagram&utm_content=lien-bio

URL courte ClickWhale affichee en bio :
https://swp.link/ressources (exemple)

Explication :
- source=instagram : trafic provenant d'Instagram
- medium=short-link : le lien passe par ClickWhale (lien court redistribue)
- campaign=bio-instagram : campagne permanente (pas de date car lien evergreen)
- content=lien-bio : le point d'entree est la bio du profil
```

---

### Cas 5 — Lien affilie ThemeForest dans un article

**Contexte :** Un article "Meilleurs themes WordPress LMS" contient un lien affilie vers ThemeForest pour un theme recommande.

```
URL complete (lien affilie avec parametres UTM en plus des params affilies) :
https://themeforest.net/item/lms-theme/12345678?ref=schoolswp&utm_source=themforest&utm_medium=affiliate&utm_campaign=partenariat-themeforest&utm_content=lien-texte-article

Explication :
- source=themforest : identifie ThemeForest comme plateforme partenaire (tracking du clic sortant)
- medium=affiliate : canal affiliation
- campaign=partenariat-themeforest : regroupe tous les liens affilies ThemeForest
- content=lien-texte-article : dans le corps de l'article
Note : ces UTMs sont ajoutes a l'URL de destination pour tracker les clics depuis schoolswp.com
dans GA4. Le parametre &ref=schoolswp est le parametre d'affiliation ThemeForest, distinct des UTMs.
```

---

### Cas 6 — Description video YouTube

**Contexte :** Une video YouTube "Installer TutorLMS en 10 minutes" contient dans sa description un lien vers le tutoriel complet sur schoolswp.com.

```
URL complete :
https://schoolswp.com/installer-tutor-lms?utm_source=youtube&utm_medium=social&utm_campaign=lms-wordpress-mars-2026&utm_content=description-video

Explication :
- source=youtube : la plateforme d'origine est YouTube
- medium=social : YouTube est considere comme canal social organique (pas payant ici)
- campaign=lms-wordpress-mars-2026 : meme campagne que le post LinkedIn sur le sujet LMS — GA4 regroupera les deux dans la meme campagne
- content=description-video : le lien est dans la description de la video (et non dans un commentaire epingle — dans ce cas utiliser content=commentaire-epingle)
```

---

### Cas 7 — Sequence email FluentCRM : 3e email de la serie "LMS en 5 jours"

**Contexte :** Une sequence automatisee de 5 emails sur le LMS WordPress. Le 3e email envoie vers un article comparatif.

```
URL complete :
https://schoolswp.com/tutor-lms-vs-learndash?utm_source=newsletter&utm_medium=email&utm_campaign=serie-lms-5-jours&utm_content=email-3-cta-principal

Explication :
- source=newsletter : meme source que toutes les communications FluentCRM
- medium=email : canal email
- campaign=serie-lms-5-jours : identifie specifiquement la sequence automatisee
- content=email-3-cta-principal : permet d'isoler le comportement des abonnes sur le 3e email
  en particulier (comparaison possible avec email-1, email-2, etc.)
```

---

## 5. Quand mettre des UTMs

Les UTMs sont **obligatoires** dans ces situations :

- **Emails FluentCRM** — newsletter hebdomadaire, sequences automatisees, emails ponctuels : chaque lien cliquable vers schoolswp.com doit etre tague
- **Publications reseaux sociaux** — tous les liens dans les posts LinkedIn, descriptions YouTube, stories et bio Instagram
- **Liens affilies** — chaque lien ThemeForest, plugin partenaire ou programme d'affiliation dans un article ou une page
- **Campagnes publicitaires** — si des Google Ads ou Meta Ads sont lances, les URLs de destination doivent etre taguees (souvent gere via le tracking automatique mais UTMs manuels recommandes en complement)
- **Articles invites et collaborations** — si schoolswp.com est mentionne dans un article sur un autre site, le lien doit porter des UTMs pour tracker ce trafic referral
- **Short links ClickWhale distribues en externe** — toute URL courte qui sort de schoolswp.com vers une audience externe (bio Instagram, lien YouTube, Linktree-like) doit pointer vers une URL destination avec UTMs

---

## 6. Quand NE PAS mettre des UTMs

Les UTMs sont **contre-productifs** dans ces situations :

- **Liens internes de navigation** — menu principal, sidebar, footer de navigation, breadcrumbs : ne jamais taguer. Un UTM sur un lien interne cree une nouvelle session dans GA4 et ecrase la source d'origine. Un visiteur venu de LinkedIn qui clique sur le menu sera comptabilise comme une session "interne" distincte, ce qui fausse completement l'attribution.
- **Maillage interne dans les articles** — les liens hypertextes entre articles (liens de contexte dans le corps du texte) ne doivent pas porter d'UTMs pour les memes raisons d'attribution.
- **Redirections techniques** — les redirections 301/302 configurees au niveau serveur ou via ClickWhale pour des raisons techniques (pas de diffusion externe) ne doivent pas porter d'UTMs.
- **Liens depuis les pages de paiement vers la confirmation** — l'ajout d'UTMs entre la page de paiement et la page de confirmation casse le tracking e-commerce GA4 (la conversion n'est plus rattachee a la bonne session).
- **Liens de desabonnement ou de preference email** — les liens FluentCRM de desabonnement/gestion des preferences ne doivent pas porter d'UTMs (donnees sans interet analytique et URLs inutilement chargees).
- **Liens canaux propres deja identifies** — si GA4 reconnait automatiquement une source (trafic direct, Google organique via GSC), ajouter des UTMs manuels peut creer des doublons ou des conflits.

---

## 7. Erreurs a eviter

1. **Majuscules dans les valeurs UTM.** "LinkedIn" et "linkedin" sont deux sources separees dans GA4. Apres six mois de donnees mixtes, les rapports deviennent inutilisables. Regle : toujours minuscules, sans exception.

2. **Underscores au lieu de tirets.** `utm_campaign=lms_wordpress` vs `utm_campaign=lms-wordpress` : ces deux valeurs coexistent comme des campagnes distinctes dans GA4. Choisir les tirets et ne jamais en devier.

3. **Valeurs inconcistantes pour la meme source.** Utiliser "linkedin", "linked-in", "linkedin-organic" et "li" a differents moments pour LinkedIn produit 4 sources dans GA4 au lieu d'une. La coherence est plus importante que la "precision" — mieux vaut une valeur simple et toujours identique.

4. **Oublier utm_medium.** Un lien avec `utm_source=newsletter` sans `utm_medium=email` produit une source "newsletter" rattachee au medium "(not set)" dans GA4 — ce qui la rend difficile a filtrer et a exploiter. Source et medium vont toujours ensemble.

5. **Taguer les liens internes.** C'est l'erreur la plus frequente et la plus devastatrice pour l'attribution. GA4 interprete chaque nouvelle URL avec UTMs comme le debut d'une nouvelle session. Un visiteur LinkedIn qui clique sur 3 liens internes tagues genere 3 sessions, toutes comptees comme internes, aucune rattachee a LinkedIn.

6. **Valeurs trop longues ou avec des caracteres speciaux.** Une campagne nommee `utm_campaign=article-sur-l'installation-de-tutor-lms-en-2026` contient une apostrophe qui sera encodee en %27 dans l'URL et posera des problemes de parsing. Rester sous 30 caracteres, sans apostrophes ni caracteres speciaux.

7. **Dupliquer les UTMs dans les redirections ClickWhale.** Si l'URL de destination dans ClickWhale porte deja des UTMs, ne pas ajouter des UTMs supplementaires sur le short link lui-meme — GA4 ne peut pas interpreter deux series de parametres UTMs simultanement et prendra la premiere ou la derniere selon la configuration.

8. **Oublier de tester l'URL finale.** Avant de publier une newsletter ou un post LinkedIn, tester l'URL complete dans un navigateur pour verifier que les UTMs apparaissent correctement dans GA4 (via le mode debug de GA4 ou l'extension "GA Debugger").

---

## 8. Ma recommandation simple a retenir

> **Source = qui t'envoie. Medium = comment. Campaign = pourquoi.**
> Si le lien quitte l'exterieur pour entrer sur schoolswp.com, il porte des UTMs. Si le lien reste sur schoolswp.com ou va d'une page a une autre du site, il n'en porte pas.

La question a se poser avant de coller un UTM : **"Ce lien vient-il d'une source externe ?"** Oui → UTMs obligatoires. Non → pas d'UTMs.

---

_Convention UTM schoolsWP — v1.0 — mars 2026 — Michael KIHL_
