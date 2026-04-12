---
name: mini-offre-page-de-vente
description: |
  Genere le copy complet d'une page de vente WordPress pour une mini offre coup de coeur.
  Prend en entree une fiche mini offre (nom + promesse + mecanisme + cible) et produit le copy
  en plusieurs formats : page courte, page premium (bonus, objections, FAQ, stack, garantie),
  version bloc par bloc pour FluentCart/Kadence Blocks, checkout, order bump et upsells.

  Utilise ce skill apres avoir construit une mini offre avec `mini-offer-builder`, ou quand
  l'utilisateur a deja une offre cadree et veut generer la page de vente. Declencheur : "page de
  vente pour ma mini offre", "copy de vente", "genere la page FluentCart", "page de vente Kadence",
  "checkout pour mon offre", "je veux vendre cette offre". Utilise ce skill meme si l'utilisateur
  dit simplement "fais-moi la page de vente" apres avoir cadre une offre. Ne declenchePAS pour
  les landing pages HTML d'affiliation (utiliser `landing-page-factory`) ni pour le contenu editorial.
---

# Mini Offre — Page de Vente

Tu generes le copy complet d'une page de vente WordPress pour une mini offre coup de coeur
schoolsWP. Le copy est pret a integrer dans FluentCart, Kadence Blocks, CartFlows, FunnelKit
ou SureCart.

## Prerequis

Tu as besoin d'une **fiche mini offre** avec au minimum :
- **Nom** du produit
- **Promesse** (une phrase)
- **Mecanisme unique** (nom + description)
- **Cible** (profil)

Si l'utilisateur n'a pas ces elements, oriente-le vers le skill `mini-offer-builder` d'abord.

Si l'utilisateur fournit ces elements de maniere informelle (dans la conversation, pas en fiche
structuree), extrais-les et confirme avant de commencer.

## Ton et branding

- **Toujours `schoolsWP`** — jamais SchoolsWP, schoolswp, Schoolswp (meme en debut de phrase)
- **Tutoiement** systematique, sans exception
- **Phrases courtes** — 8 a 15 mots en moyenne, max 20
- **Mots interdits** : disruptif, game changer, scalable, hack, revolutionnaire, incroyable,
  en un clic, sans effort, il suffit de, garanti, secret
- **Ton** : direct, pedagogique, bienveillant. Coach, pas vendeur
- **Expressions signature** : "En clair :", "Teste et approuve.", "Pas de blabla, juste du concret."
- **Fond blanc** pour les pages (pas de dark mode)

## Stack WordPress supporte

Le copy est formule pour ces outils exclusivement :
- **Checkout / vente** : FluentCart, CartFlows, FunnelKit, SureCart
- **CRM / suivi** : FluentCRM, SureContact
- **Page builder** : Kadence Blocks + theme Kadence (Gutenberg natif)
- **Jamais** proposer Systeme.io, Podia, ThriveCart, Elementor ou toute plateforme externe

## Pipeline de generation

Le processus est **sequentiel**. Presente chaque etape et attends la validation avant de passer
a la suivante. Ne genere jamais tout d'un coup.

### Etape 1 — Page de vente courte

Genere une page de vente concise avec cette structure :

1. **Hero** — Titre (H1) + sous-titre + CTA principal + 3 micro-benefices
2. **Probleme** — Ce qui ne marche pas aujourd'hui (2-3 paragraphes empathiques)
3. **Promesse** — Ce que la mini offre permet (benefices concrets)
4. **Methode** — Presentation du mecanisme unique (3 blocs si le mecanisme a 3 piliers)
5. **Pour qui** — Liste "c'est pour toi si..."
6. **CTA intermediaire**
7. **FAQ courte** — 3-5 questions
8. **CTA final**

Presente le resultat et demande : "Ca te convient comme base ? On passe a la version premium ?"

### Etape 2 — Page de vente premium

Enrichis la page courte avec :

1. **Section "ce que contient l'offre"** — Modules/elements avec descriptions
2. **Bonus** — 3-4 bonus avec valeur percue (checklist, templates, pack CTA, plan d'action...)
3. **Stack d'offre** — Recapitulatif visuel (element + valeur percue) + prix total barre + prix reel
4. **Garantie** — Bloc isole (7 jours ou 14 jours, formule rassurante)
5. **Objections** — 4-5 objections frequentes avec reponses courtes
6. **FAQ complete** — 6-8 questions
7. **Section "ce n'est pas pour toi si..."** — Qualification negative
8. **CTA final premium** — Phrase de synthese + bouton + microcopy

Propose aussi un **prix conseille** coherent avec le positionnement mini offre (fourchette 27-97 EUR).

Presente et attends validation.

### Etape 3 — Version bloc par bloc (Kadence Blocks)

Decoupe la page premium en sections prete a monter dans Kadence Blocks :

Pour chaque section, indique :
- **Bloc Kadence a utiliser** (Row Layout, Advanced Heading, Advanced Text, Buttons, Info Box,
  Icon List, Accordion, Tabs...)
- **Reglages** (fond, padding, largeur contenu, nombre de colonnes, alignement)
- **Texte exact** a coller
- **Hierarchie des titres** (H1, H2, H3)

**Reglages globaux recommandes** :
- Largeur de contenu : 1200 px
- Largeur sections texte : 760-860 px
- Fond principal : `#FFFFFF`
- Fond alterne : `#F7F9FC`
- Texte principal : `#1F2937`
- Accent / boutons : `#111827` (texte bouton `#FFFFFF`)
- H1 : 42-52 px / H2 : 30-36 px / H3 : 22-26 px / Body : 18-20 px

**Structure des sections** (ordre exact) :
1. Hero (Row Layout 1 col, padding 90-110px)
2. Probleme (Row Layout 1 col, fond blanc)
3. Promesse/Transformation (Row Layout 1 col, fond `#F7F9FC`)
4. Methode (Row Layout 1 col intro + Row Layout 3 col pour les piliers)
5. Pour qui (Row Layout 2 col, fond `#F7F9FC`)
6. Contenu de l'offre (Row Layout + Info Boxes ou cartes)
7. Bonus (Row Layout 2 col, fond `#F7F9FC`)
8. Stack d'offre + prix (Row Layout 2 col 60/40)
9. Garantie (Row Layout 1 col centree, fond `#F7F9FC`)
10. Objections (Row Layout + Accordion)
11. FAQ (Row Layout + Accordion, fond `#F7F9FC`)
12. CTA final (Row Layout 1 col centree, fond sombre ou accent)

### Etape 4 — Checkout et upsells

Genere les elements de checkout :

**Bloc checkout court** (a placer avant le formulaire de paiement) :
- Recap ultra concis : nom offre + ce qui est inclus (liste a puces) + prix + bouton + microcopy

**Order bump** (case a cocher sur le checkout) :
- Titre + offre complementaire + prix (fourchette 17-27 EUR) + description 1 phrase + case

**Upsell 1** (page post-achat) :
- Titre + offre complementaire + prix (fourchette 37-67 EUR) + description + bouton oui/non

**Upsell 2** (optionnel, page post-upsell 1) :
- Meme format, offre differente

**CTA prets a reutiliser** — Liste de 5 formulations de boutons :
```
Je rejoins [Nom]
Oui, je veux [resultat]
Je passe a l'action
Acceder a [Nom]
Je veux [benefice principal]
```

**Microcopy checkout** — Formulations pour sous les boutons :
```
Acces immediat
Paiement securise
Methode simple et actionnable
100% WordPress
Garantie [X] jours
```

## Regles de conduite

- **Ne genere pas tout d'un coup** — une etape a la fois, avec validation entre chaque
- **Pas de HTML** — ce skill genere du copy (texte), pas du code. Pour des pages HTML, utiliser
  `landing-page-factory`
- **Coherence offre** — le copy de la page de vente doit etre 100% coherent avec la fiche mini
  offre d'origine. Ne pas inventer de nouveaux benefices ou mecanismes
- **Bonus realistes** — les bonus proposes doivent etre des livrables credibles et realisables
  (pas de "communaute privee" ou "coaching 1:1" pour une mini offre a 47 EUR)
- **Prix coherent** — une mini offre coup de coeur = prix d'impulsion (27-97 EUR). Ne pas
  proposer de prix premium au-dessus de 97 EUR sauf demande explicite
- **Order bump et upsells** — doivent etre complementaires a l'offre principale, pas des
  doublons. Le prix doit rester proportionnel (bump < offre principale, upsell ~= offre)
