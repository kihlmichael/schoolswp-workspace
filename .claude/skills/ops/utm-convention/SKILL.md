---
name: utm-convention
description: |
  Produit la convention UTM officielle schoolsWP en 9 sections (règles, paramètres source/medium/campaign/content/term, format standard, 6-10 cas concrets, quand utiliser/pas utiliser, erreurs à éviter). Couvre GA4, ClickWhale, FluentCRM, CTAs internes, réseaux sociaux, liens affiliés. Sortie minuscules + tirets + sans accents.
  Utilise ce skill quand l'utilisateur dit : "UTM", "tracking de liens", "convention paramètres URL", "campagnes GA4", "suivi clics ClickWhale", "j'organise mes UTMs", ou "comment je track mes liens".
  NE PAS utiliser pour : auditer la performance d'une campagne (utiliser GSC + GA4 directement), configurer FluentCRM smart links (utiliser `flow`), ou créer une page d'atterrissage (utiliser `landing-page-factory` ou `mini-offre-page-de-vente`).
---

# schoolswp-utm-convention

Produit la **convention UTM officielle schoolsWP** à partir de notes brutes ou de zéro.

## Ce que ce skill produit

Un document structuré en 9 sections, prêt à publier ou à partager en équipe :

1. Titre de la convention
2. Règles de base (5-7 règles impératives)
3. Section par paramètre UTM (rôle + valeurs conseillées + exemples)
4. Convention officielle recommandée schoolsWP (format standard)
5. Cas concrets (6-10 exemples complets avec tous les paramètres)
6. Quand mettre des UTMs
7. Quand ne PAS en mettre
8. Erreurs à éviter
9. Ma recommandation simple à retenir

---

## Contextes couverts

- **GA4** — attribution des sources de trafic, rapports acquisition
- **ClickWhale** — gestion short links, liens sociaux permanents, redirections
- **FluentCRM** — newsletters, séquences email, segmentation
- **CTAs internes** — boutons et liens sur schoolswp.com
- **Réseaux sociaux** — LinkedIn, YouTube, Facebook, Instagram
- **Liens affiliés** — tracking partenaires, programmes d'affiliation

---

## Règles de production

### Format UTM obligatoire

- Tout en **minuscules**
- **Tirets** uniquement (jamais d'underscores, jamais d'espaces)
- **Sans accents** (newsletter → newsletter, etude-de-cas → etude-de-cas)
- Valeurs courtes et lisibles (max 30 caractères par valeur)

### Logique d'analyse

1. Lire les notes sources si fournies
2. Identifier les contradictions et trancher (ne pas dire "ça dépend" sans recommandation)
3. Identifier les zones floues et les clarifier par une recommandation concrète
4. Supprimer les doublons et redondances
5. Compléter les cas manquants pour les 5 contextes clés (GA4/ClickWhale/FluentCRM/CTAs/social)

### Ton du document produit

- Expert mais accessible
- Pédagogique : expliquer le rôle de chaque paramètre en une phrase
- Pragmatique : toujours conclure par une recommandation actionnable
- Pas de "ça dépend" sans suite — toujours trancher

---

## Structure détaillée par section

### Section 1 — Titre

```
Convention UTM officielle schoolsWP — [date ou version]
```

### Section 2 — Règles de base

5 à 7 règles numérotées. Exemples de règles typiques :

- Toujours minuscules, tirets, sans accents
- Ne jamais taguer les liens internes (navigation du site)
- Toujours taguer les liens externes entrants (email, social, pub)
- utm_source = origine (qui envoie), utm_medium = canal (comment), utm_campaign = campagne (pourquoi)
- Cohérence absolue : une valeur = un sens, jamais deux valeurs pour la même chose

### Section 3 — Paramètres UTM (une sous-section par paramètre)

Pour **chaque paramètre** (source, medium, campaign, content, term) :

- **Rôle** : définition en une phrase
- **Valeurs recommandées** : liste des valeurs à utiliser pour schoolsWP
- **Exemples** : 3-4 exemples concrets avec le contexte

#### Valeurs de référence schoolsWP

**utm_source** (d'où vient le visiteur)

```
newsletter | linkedin | youtube | facebook | instagram | google | bing | direct |
clickwhale | affiliation | partenaire | [nom-du-partenaire]
```

> **Règle tranchée — emails FluentCRM** : toujours `utm_source=newsletter` (jamais `fluentcrm`).
> La source décrit ce que l'utilisateur reçoit, pas l'outil qui envoie.
> Si tu changes d'ESP, le tracking reste cohérent dans GA4.

**utm_medium** (canal de diffusion)

```
email | social | organic | cpc | referral | banner | cta | short-link | affiliate
```

**utm_campaign** (nom de la campagne)
Format recommandé : `[sujet]-[mois-annee]` ou `[nom-serie]`

```
lms-wordpress-mars-2024 | launch-authority-system | newsletter-hebdo | black-friday-2024
```

**utm_content** (différencier plusieurs liens dans la même campagne)

```
cta-header | cta-footer | bouton-principal | lien-texte | image-banner | vignette-youtube
```

**utm_term** (mots-clés — surtout pour les campagnes payantes)

```
lms-wordpress | tutor-lms | crm-wordpress | [mot-cle-cible]
```

### Section 4 — Convention officielle recommandée

Format standard schoolsWP :

```
?utm_source=[source]&utm_medium=[medium]&utm_campaign=[campaign]&utm_content=[content]
```

Règle : utm_term est optionnel, réservé aux campagnes payantes.

Tableau synthèse : source → medium → quand l'utiliser

### Section 5 — Cas concrets (6 à 10)

Produire au minimum ces 6 cas :

1. **CTA interne** — bouton "Télécharger le guide" en footer d'article sur schoolswp.com
2. **Newsletter FluentCRM** — lien principal dans une newsletter hebdomadaire
3. **LinkedIn** — lien dans une publication organique LinkedIn
4. **ClickWhale short link** — lien court permanent pour bio Instagram
5. **Lien affilié** — lien Themeforest ou plugin partenaire dans un article
6. **Campagne YouTube** — lien en description d'une vidéo YouTube

Format pour chaque cas :

```
Contexte : [description du contexte]
URL complète : https://schoolswp.com/[slug]?utm_source=[x]&utm_medium=[y]&utm_campaign=[z]&utm_content=[w]
Explication : [pourquoi ces valeurs]
```

### Section 6 — Quand mettre des UTMs

Liste des contextes où les UTMs sont obligatoires :

- Liens dans les emails (newsletters, séquences FluentCRM)
- Publications sur les réseaux sociaux (bio, posts, stories)
- Liens affiliés et partenariats
- Campagnes publicitaires (Google Ads, Meta Ads)
- Collaborations et articles invités
- Short links ClickWhale distribués en externe

### Section 7 — Quand NE PAS mettre des UTMs

Contextes où les UTMs sont contre-productifs :

- Liens internes de navigation (menu, sidebar, footer de navigation)
- Liens internes dans les articles (maillage interne) — GA4 les comptabilise comme rebonds
- Pages de paiement → confirmation de commande (casse le tracking e-commerce)
- Redirections techniques

Expliquer pourquoi : les UTMs sur liens internes écrasent la source d'origine dans GA4, faussant l'attribution.

### Section 8 — Erreurs à éviter

Liste de 5-8 erreurs concrètes avec explication :

- Mélanger underscores et tirets
- Utiliser des majuscules (GA4 est sensible à la casse — "Newsletter" ≠ "newsletter")
- Valeurs incohérentes pour la même source (ex: "linkedin" et "linked-in" et "LinkedIn")
- Oublier utm_medium (source seule ne suffit pas pour l'attribution)
- Taguer les liens internes (casse l'attribution)
- UTMs sur les liens canoniques du propre site
- Valeurs trop longues ou avec des caractères spéciaux

### Section 9 — Recommandation simple à retenir

Une formule mnémotechnique ou une règle en 1-2 phrases qui résume tout.
Exemple de format :

> "Source = qui t'envoie. Medium = comment. Campaign = pourquoi. Si tu doutes sur un lien, pose-toi cette question : est-ce que ce lien vient de l'extérieur ? Oui → UTM obligatoire. Non → pas d'UTM."

---

## Comment utiliser ce skill

### Si l'utilisateur fournit des notes brutes

1. Lire et analyser les notes
2. Identifier : valeurs définies / valeurs manquantes / contradictions / zones floues
3. Produire une première version complète basée sur les notes + compléments schoolsWP
4. Signaler en fin de document : "Points tranchés" (liste des décisions prises) et "Points à confirmer" (si des choix méritent validation)

### Si l'utilisateur repart de zéro

Produire directement la convention complète avec les valeurs recommandées schoolsWP définies dans ce skill.

### Si l'utilisateur veut juste un aspect

Répondre de façon ciblée (ex: "quelles valeurs pour utm_source ?") mais proposer de produire le document complet en fin de réponse.

---

## Qualité du document final

Avant de livrer, vérifier :

- [ ] Toutes les valeurs sont en minuscules, avec tirets, sans accents
- [ ] Chaque paramètre a au moins 3 valeurs recommandées
- [ ] Au moins 6 cas concrets avec URL complète
- [ ] Section "quand ne pas mettre" incluse (souvent oubliée)
- [ ] Recommandation finale mémorisable en 2 phrases max
- [ ] Aucun "ça dépend" sans recommandation concrète
