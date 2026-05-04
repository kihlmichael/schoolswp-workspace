---
name: lead-magnet-schoolswp
description: |
  Produit un système de lead magnet schoolsWP complet et cohérent : PDF 1 page à forte valeur + landing page de capture newsletter (Fluent Forms) + séquence de bienvenue FluentCRM (4 emails sur 7 jours). Les 3 livrables forment un funnel unique, pas 3 livrables indépendants.
  Utiliser ce skill quand l'utilisateur demande : "lead magnet", "freebie", "ressource gratuite", "PDF à télécharger", "landing newsletter", "page d'inscription", "capture d'emails", "séquence de bienvenue", "welcome sequence", "lead magnet prompt SEO", ou veut transformer une ressource (prompt, checklist, template, mini-guide) en aimant à emails.
  NE PAS utiliser pour : landing d'affiliation produit tiers (voir landing-page-factory), page de vente d'offre propre schoolsWP (voir mini-offre-page-de-vente), séquence email de découverte plugin par affiliation (voir plugin-email-sequence), recyclage d'un email reçu (voir email-to-content), newsletter hebdo régulière (voir schoolswp-content-studio), article de blog long (voir schoolswp-article-workflow).
od:
  mode: marketing
  scenario: lead-capture
  preview:
    type: markdown
    entry: lead-magnet.md
  inputs:
    - name: source_resource
      type: enum
      enum: [prompt, checklist, template, mini-guide, framework]
      required: true
      description: Type de ressource source qui devient le lead magnet
    - name: main_promise
      type: string
      required: true
      description: Transformation concrete promise en une phrase
    - name: persona
      type: enum
      enum: [freelance, createur, formateur, entrepreneur]
      required: true
      description: Persona cible (oriente le ton et les exemples)
    - name: funnel_stage
      type: enum
      enum: [TOFU, MOFU]
      required: true
      description: Stade de funnel — TOFU decouverte (large) ou MOFU exploration (qualifie)
    - name: destination
      type: enum
      enum: [newsletter-hebdo, sequence-produit, academy]
      required: true
      description: Destination post-inscription (oriente la sequence email finale)
  parameters:
    - name: pdf_format
      type: enum
      enum: [A4-1page, A4-2pages]
      default: A4-1page
      description: Format du PDF (1 page strict par defaut)
    - name: welcome_email_count
      type: integer
      default: 4
      range: [3, 6]
      description: Nombre d'emails dans la sequence de bienvenue FluentCRM
    - name: welcome_duration_days
      type: integer
      default: 7
      range: [5, 10]
      description: Duree de la sequence de bienvenue en jours
  outputs:
    primary: lead-magnet-pdf.md
    secondary:
      - landing-capture.md
      - sequence-bienvenue.md
  capabilities_required:
    - file_write
---

# Lead Magnet schoolsWP — Système de capture complet

Skill spécialisé pour produire les **3 livrables en cascade** d'un lead magnet schoolsWP :

1. **PDF 1 page** à forte valeur (cœur de la promesse)
2. **Landing page de capture newsletter** (Fluent Forms + FluentCRM)
3. **Séquence de bienvenue** 4 emails sur 7 jours (accueil + livraison + valeur + transition newsletter)

Les 3 pièces forment un funnel unique et cohérent. Pas de livraison partielle.

## Style schoolsWP

- Phrases courtes (8-15 mots)
- Paragraphes 2-4 phrases
- Zéro jargon non expliqué
- Zéro hype marketing
- "schoolsWP" écrit correctement partout

## Préconditions (à confirmer en UN seul message groupé)

Avant de démarrer, confirmer avec l'utilisateur :

1. **Ressource source** : quel contenu devient le lead magnet ? (prompt, checklist, template, mini-guide, framework)
2. **Promesse principale** : quelle transformation concrète en une phrase ?
3. **Persona cible** : freelance, créateur, formateur, entrepreneur ?
4. **Stade funnel** : TOFU découverte ou MOFU exploration ?
5. **Destination post-inscription** : newsletter hebdo schoolsWP News, séquence produit, Academy ?

Si la ressource source n'existe pas encore, la créer d'abord avant d'enchaîner landing et séquence.

## Workflow en cascade — 3 livrables

### Livrable 1 — PDF 1 page

**Règle d'or** : une page A4, lisible en 60 secondes, immédiatement actionnable.

**Structure obligatoire** :

```
[Titre principal — promesse claire, 6-10 mots]
[Sous-titre — pour qui et quel résultat]

[Section 1 : Le contexte — 2-3 phrases]
Pourquoi ce sujet mérite attention maintenant.

[Section 2 : Le cœur actionnable]
La ressource elle-même : prompt, checklist, framework, étapes.
Format visuellement scannable : encadré, liste, tableau.

[Section 3 : Comment l'utiliser — 3 étapes maximum]
Mode d'emploi concret.

[Footer]
schoolsWP — WordPress. Clair. Structuré. Utile.
Lien vers schoolswp.fr
```

**Règles de format** :

- **1 page A4 stricte.** Pas 2, pas 1,5.
- **Lisibilité mobile** : typo minimum 11pt, interlignage généreux.
- **Identité visuelle** : vert `#00D400`, typo Inter, logo schoolsWP.
- **Zéro bloc de texte dense.** Tout doit être scannable.
- **Une action claire** en sortie : que doit faire le lecteur après avoir lu ?

**Types validés** :

1. Prompt prêt à copier (ex : prompt SEO une page)
2. Checklist actionnable (ex : audit sécurité WordPress en 12 points)
3. Framework visuel (ex : matrice monétisation WordPress)
4. Template rempli (ex : calendrier éditorial exemple)
5. Mini-méthode en N étapes (ex : méthode schoolsWP en 5 étapes)

### Livrable 2 — Landing page de capture

**Objectif** : convertir le visiteur en abonné en moins de 15 secondes de lecture.

**Structure obligatoire** :

```
[H1 — Promesse principale, 8-12 mots, focalisée sur le BÉNÉFICE pas l'objet]
[Sous-titre — bénéfice concret + pour qui]
[Visuel du PDF ou mockup]

[Bloc valeur — 3 points max avec flèches]
→ Ce que contient le PDF
→ Ce que le lecteur saura faire
→ Le temps nécessaire pour l'appliquer

[Formulaire Fluent Forms]
- Champ prénom (optionnel)
- Champ email (obligatoire)
- Bouton CTA : verbe d'action + bénéfice

[Réassurance — 1 phrase]
Désinscription en 1 clic. Zéro spam. Promis.

[Signature Michaël — courte]
Qui je suis en 2 phrases + photo.
```

**Règles landing** :

- **H1 focalisé sur le bénéfice**, pas sur l'objet. ❌ "Télécharger le PDF gratuit". ✅ "Un prompt pour écrire vos articles WordPress 10x plus vite".
- **CTA bouton : verbe + bénéfice.** ❌ "S'inscrire". ✅ "Recevoir le prompt maintenant".
- **Zéro champ inutile.** Email obligatoire, prénom optionnel. Rien d'autre.
- **Mobile-first** : visuel au-dessus de la ligne de flottaison sur écran téléphone.

**À livrer** :

1. Copywriting complet (H1, sous-titre, bullets, CTA, réassurance, signature)
2. Specs de structure (ordre des blocs, hiérarchie visuelle)
3. Specs Fluent Forms (champs, validation, redirection post-inscription)
4. Texte exact du bouton CTA
5. Meta title HTML + meta description SEO

### Livrable 3 — Séquence de bienvenue FluentCRM

**Objectif** : accueillir le nouvel abonné, livrer la promesse, créer le lien, amorcer le funnel.

**Structure obligatoire : 4 emails sur 7 jours.**

```
Email 1 — Livraison (T+0, immédiat)
Objet : Ton [ressource] est juste ici
- Accueil chaleureux (2 phrases)
- Lien de téléchargement direct en haut
- "Voilà comment l'utiliser" — 3 étapes
- Signature Michaël

Email 2 — Contexte (T+1 jour)
Objet : Pourquoi j'ai créé [ressource]
- Histoire personnelle courte (problème rencontré)
- Ce que ça a changé
- Invitation à répondre : "Dis-moi ce que tu essaies de résoudre"
- Signature Michaël

Email 3 — Valeur additionnelle (T+3 jours)
Objet : Une astuce que j'utilise avec [ressource]
- Tip concret lié à la ressource
- Exemple chiffré ou captures
- Lien vers article schoolsWP pertinent
- Signature Michaël

Email 4 — Transition (T+7 jours)
Objet : Ce que tu vas recevoir ensuite
- Récap de ce qu'on a vu
- Ce que la newsletter schoolsWP News couvre vraiment
- Une question ouverte pour engager
- Signature Michaël
```

**Règles par email** :

- **300 à 500 mots maximum.**
- **Objet : 40-50 caractères.** Curiosité ou bénéfice concret.
- **Pré-header** : prolonge l'objet, ne le répète pas.
- **Un seul lien principal par email.** Pas de boutons multiples.
- **Tag FluentCRM** à chaque email pour traçabilité.
- **Conditions de sortie** : si le lead clique sur un CTA commercial, bascule vers liste engagée.

**À livrer** :

1. Les 4 emails complets (objet + pré-header + corps + signature)
2. Planning FluentCRM (délais en jours, tags, conditions)
3. Points de bascule entre listes (welcome → newsletter active)
4. KPIs à suivre (taux d'ouverture, taux de clic, taux de réponse email 2)

## Workflow d'exécution (ordre strict)

### Phase 1 — Cadrage
Valider les 5 préconditions en un message. Attendre réponse utilisateur avant d'écrire.

### Phase 2 — Livrable 1 : PDF
Rédiger d'abord le contenu du PDF. C'est le cœur du système. Tout le reste en découle.

### Phase 3 — Livrable 2 : Landing
Rédiger la landing en s'appuyant sur la promesse exacte du PDF. Cohérence totale promesse landing ↔ contenu PDF.

### Phase 4 — Livrable 3 : Séquence
Rédiger les 4 emails. L'email 1 doit livrer exactement ce que la landing a promis. Aucun écart.

### Phase 5 — Vérification de cohérence
Relire les 3 livrables en mode funnel : un visiteur qui passe landing → inscription → email 1 → PDF doit vivre une expérience fluide. Aucune friction, aucune promesse non tenue.

## Erreurs fréquentes à éviter

- ❌ PDF qui déborde sur 2-3 pages par faiblesse de synthèse
- ❌ Landing qui vend l'objet ("un PDF gratuit") au lieu de la transformation
- ❌ Formulaire avec 5 champs au lieu de 1-2
- ❌ Email 1 qui ne livre pas immédiatement la ressource promise
- ❌ Séquence qui bascule en mode vente dès l'email 2
- ❌ Incohérence entre promesse landing et contenu PDF
- ❌ CTA bouton mou ("Envoyer", "Valider", "OK")
- ❌ Absence de réassurance sur la désinscription
- ❌ Séquence FluentCRM sans tags ni conditions de sortie

## Checklist finale

1. ✅ PDF : 1 page, scannable en 60 secondes, actionnable immédiatement
2. ✅ PDF : identité visuelle schoolsWP respectée (vert #00D400 + Inter)
3. ✅ Landing : H1 focalisé bénéfice, pas objet
4. ✅ Landing : formulaire minimal (1-2 champs max)
5. ✅ Landing : CTA bouton verbe + bénéfice
6. ✅ Séquence : 4 emails, 7 jours, délais précis
7. ✅ Séquence : objets 40-50 caractères, curiosité ou bénéfice
8. ✅ Séquence : email 1 livre exactement la promesse landing
9. ✅ Cohérence totale des 3 livrables en mode funnel
10. ✅ Tags FluentCRM et conditions de sortie documentés
11. ✅ KPIs de suivi listés
12. ✅ "schoolsWP" écrit correctement partout

## Références internes schoolsWP

- Stack conversion : Fluent Forms + FluentCRM
- Destination post-inscription par défaut : newsletter schoolsWP News
- Priorité roadmap actuelle : lead magnet prompt SEO 1 page avant publication YouTube Shorts
- Identité visuelle : vert `#00D400`, typo Inter
- Ressource WordPress primaire : bitapps.pro

## Format de livraison

Livrer les 3 livrables dans l'ordre strict, en Markdown, séparés par des sections claires :

```markdown
# Lead Magnet : [Nom]

## Livrable 1 — PDF (contenu)
[Contenu complet du PDF, prêt à mettre en page]

## Livrable 2 — Landing Page
[Copywriting complet + specs structure + specs Fluent Forms]

## Livrable 3 — Séquence FluentCRM
[Les 4 emails complets + planning + tags + conditions]

## Cohérence funnel
[Bref récap : promesse landing → contenu email 1 → contenu PDF]

## KPIs à suivre
[Liste des métriques]
```

Pas de préambule. Pas de "voici ton lead magnet". Directement les livrables.

## Self-check final

Avant de cloturer la livraison du systeme complet (les 3 livrables), verifier :

**Coherence funnel**

- [ ] Les 3 livrables sont bien produits : `lead-magnet-pdf.md` (primary) + `landing-capture.md` + `sequence-bienvenue.md` (secondary)
- [ ] La promesse principale (`main_promise`) est identique mot-pour-mot dans le PDF, la landing hero, et l'objet du premier email
- [ ] Le persona (`persona`) oriente le ton de TOUS les livrables — pas de mismatch (ex landing freelance + emails entrepreneur)
- [ ] Le stade funnel (`funnel_stage`) est respecte : TOFU = ton large/decouverte, MOFU = ton plus qualifie/expert
- [ ] La destination post-inscription (`destination`) est explicite dans le dernier email de la sequence

**Livrable 1 : PDF**

- [ ] Format respecte : `pdf_format` (A4-1page par defaut, strict — pas 1,5 ni 2)
- [ ] Type ressource correspond a `source_resource` (prompt, checklist, template, mini-guide, framework)
- [ ] Footer schoolsWP present : "schoolsWP — WordPress. Clair. Structure. Utile." + lien schoolswp.fr
- [ ] Identite visuelle : vert `#00D400`, typo Inter, logo schoolsWP
- [ ] Une action claire en sortie

**Livrable 2 : landing**

- [ ] Hero reprend la promesse principale (verbatim possible)
- [ ] Specs Fluent Forms structurees (champ email + tag FluentCRM + redirect post-submit)
- [ ] Aucune mention d'une plateforme externe (Mailchimp, ConvertKit, Systeme.io)

**Livrable 3 : sequence FluentCRM**

- [ ] Nombre d'emails = `welcome_email_count` (par defaut 4, range 3-6)
- [ ] Duree totale = `welcome_duration_days` (par defaut 7 jours, range 5-10)
- [ ] Email 1 = livraison du PDF (lien telechargement) + accueil
- [ ] Dernier email = transition explicite vers `destination` (newsletter-hebdo, sequence-produit, ou academy)
- [ ] Tags FluentCRM specifies pour chaque email + conditions de declenchement

**Branding schoolsWP**

- [ ] `schoolsWP` ecrit correctement partout (jamais SchoolsWP, schoolswp, Schoolswp)
- [ ] Phrases courtes (8-15 mots), paragraphes 2-4 phrases
- [ ] Zero jargon non explique, zero hype marketing

**KPIs annonces**

- [ ] La section "KPIs a suivre" est presente avec metriques concretes (taux opt-in, taux d'ouverture par email, taux de clic vers `destination`)

## Handoff

Après livraison du système complet :

- Pour promouvoir le lead magnet par email à une liste existante → `plugin-email-sequence` (adapté en mode promo de la ressource)
- Pour recycler la landing en post social / article → `article-multiformat` ou `schoolswp-content-studio`
- Pour optimiser un livrable existant si conversion faible → `rewrite-conversion`
- Pour créer la page de vente d'une offre premium en follow-up → `mini-offre-page-de-vente`
