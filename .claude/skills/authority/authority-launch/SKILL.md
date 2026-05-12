---
name: authority-launch
description: |
  Pilote la stratégie de lancement complète Authority System™ : modèle cohorte 21 jours (pré-chauffe → masterclass → ouverture → fermeture), assets à produire (lead magnet, masterclass, posts LinkedIn, emails, landing), automations FluentCRM, KPIs de conversion, tunnel de vente. Vue d'ensemble du lancement, pas un livrable isolé.
  Utilise ce skill quand l'utilisateur dit : "prépare le lancement formation", "stratégie cohorte 21 jours", "tunnel de vente Authority System", "KPIs conversion lancement", ou veut orchestrer toute la mécanique de lancement.
  NE PAS utiliser pour : rédiger uniquement les 7 emails de la séquence (utiliser `authority-email-launch`), écrire la page de vente seule (utiliser `authority-sales-page-copy`), ou rédiger les posts LinkedIn (utiliser `pulse` agent ou skill plateforme LinkedIn).
---

# schoolsWP Authority System™ — Stratégie de Lancement

**Modèle cohorte 7 jours. Mécanique simple et répétable. Vendre sans forcer.**

---

## Positionnement du lancement

**Angle principal :** "Arrête de publier. Construis un système."

**Promesse :** en 6 modules, tu passes de contenu dispersé à un écosystème WordPress (SEO + IA + conversion) piloté par la data.

**Objection principale à casser :**

> "J'ai déjà une formation SEO."
> → Réponse : "Ici, c'est architecture + production + repurposing + tests + optimisation. Pas un plugin, pas un titre. Un système."

---

## Modèle de lancement recommandé

### Option A — Cohorte 7 jours (recommandée)

- Plus de traction et de preuve sociale
- Live Q&A + onboarding collectif
- Urgence réelle (fermeture inscriptions)
- À utiliser pour les premières cohortes (0 à 50 élèves)

### Option B — Evergreen

- À activer après 10–30 élèves + retours + cas clients
- Conversion plus faible mais trafic automatisé

---

## Timeline 21 jours

### J-21 → J-14 — Pré-chauffe

**Objectif :** faire comprendre le problème + introduire le système

**Actions :**

- 3 posts LinkedIn "mythbusters" (briser les croyances sur le SEO classique)
- 1 article SEO pilier : "Comment construire un écosystème WordPress orienté IA & conversion"
- 1 lead magnet simple : Blueprint 90 jours (PDF ou Notion)
- Page d'attente : "Liste prioritaire" + bénéfice clair

**CTA :** "Reçois le Blueprint + accès prioritaire"

---

### J-14 → J-7 — Activation

**Objectif :** capturer les emails + installer la confiance

**Actions :**

- Mini-série email "5 erreurs" (1 email/jour sur 5 jours)
- 1 live atelier 45 min : audit d'une page + démonstration Growth Loop / Performance Loop
  - Alternative : workshop enregistré + Q&A live

**CTA :** "Inscription à la masterclass + liste prioritaire"

---

### J-7 → J0 — Conversion (semaine de vente)

**Objectif :** ouvrir + vendre avec urgence propre

**Jour 1 — Ouverture :**

- Email ouverture + offre + bonus early
- Post LinkedIn "ouverture des portes"
- Page de vente en live

**Jours 2–3 — Preuve + méthode :**

- Email "preuves / avant-après / méthode"
- Post LinkedIn "frameworks : Architecture → Decision → Production → Scale → Test → Optimize"
- Stories / micro-posts "1 idée = 1 action"

**Jour 4 — Objections :**

- Email "objections" (temps, niveau, outils)
- Live Q&A 30 min

**Jours 5–6 — Cas d'usage :**

- Email "profils" (freelance, créateur, agence)
- Post "pour qui / pas pour qui"

**Jour 7 — Fermeture :**

- Rappel matin
- Rappel soir
- Bonus de clôture ou fermeture stricte

---

## Offre et bonus

### Bonus "early bird" (48h)

- Template Blueprint 90 jours (Google Doc / Notion)
- Checklist Page Pilier IA-friendly (H2/H3 + FAQ + snippets)
- 1 scorecard GSC (CTR, impressions, pages à pousser)

### Bonus "cohorte"

- 1 session onboarding live
- 1 session Q&A milieu de cohorte
- 1 session "audit collectif" fin de cohorte

---

## Tunnel (structure minimale)

```
Trafic (SEO + LinkedIn + newsletter)
  → Lead Magnet / Masterclass
  → Séquence emails
  → Page de vente
  → Checkout
  → Onboarding + activation
```

---

## Automations FluentCRM

### Tags

| Tag                         | Déclencheur                     |
| --------------------------- | ------------------------------- |
| `AS_interest`               | Lead magnet téléchargé          |
| `AS_masterclass_registered` | Inscription masterclass         |
| `AS_sales_open`             | Email ouverture ouvert / cliqué |
| `AS_buyer`                  | Achat confirmé                  |
| `AS_not_buyer`              | J0 passé sans achat             |
| `AS_high_intent`            | Clics répétés sur page de vente |

### Séquences

| Séquence             | Durée       | Objectif                                    |
| -------------------- | ----------- | ------------------------------------------- |
| Warm-up 5 emails     | J-14 à J-10 | Installer confiance + problème              |
| Masterclass + rappel | J-9 à J-7   | Inscription + présence                      |
| Sales 7 emails       | J-7 à J0    | Conversion                                  |
| Onboarding buyer     | J0 à J+7    | Activation + engagement                     |
| Nurture non-buyer    | 7 jours     | Garder le lien + waitlist prochaine cohorte |

### Scoring

| Action                       | Points |
| ---------------------------- | ------ |
| Clic page de vente           | +5     |
| Visite checkout              | +10    |
| Présence live / replay > 50% | +15    |
| Réponse email ou DM          | +20    |

---

## KPIs à suivre

### Pré-lancement

- Taux opt-in lead magnet : **25–45%**
- Inscrits masterclass : **150–500** (selon taille audience)

### Lancement

- Taux d'ouverture emails : **35–55%**
- Taux de clic : **2–6%**
- Taux de conversion liste → achat :

| Type d'audience | Taux attendu |
| --------------- | ------------ |
| Froide          | 1–3%         |
| Tiède           | 3–8%         |
| Chaude / live   | 8–15%        |

---

## 7 assets minimum à produire

| Asset                          | Format                         | Priorité |
| ------------------------------ | ------------------------------ | -------- |
| Page de vente                  | Courte d'abord, longue ensuite | P1       |
| Lead magnet Blueprint 90 jours | PDF ou Notion                  | P1       |
| Masterclass (plan + slides)    | Slides simples + script        | P1       |
| Séquence emails warm-up (5)    | Texte email                    | P1       |
| Séquence emails vente (7)      | Texte email                    | P1       |
| 10 posts LinkedIn              | Pré-chauffe + vente            | P2       |
| Page checkout + onboarding     | WordPress / TutorLMS           | P1       |

---

## Plan de lancement 7 jours — exécution détaillée

Structure émotionnelle : Excitation → Identification → Compréhension → Crédibilité → Sécurité → Tension → Décision

### Pré-chauffe (J-5 à J-1)

Objectif : prise de conscience, pas de vente.

- Post LinkedIn : "Pourquoi publier ne suffit plus"
- Newsletter : "Le vrai problème des sites WordPress"
- Teaser mécanisme : Authority Loop™ en 1 ligne

### J1 — Ouverture

Email ouverture + post LinkedIn + landing page live. Angle : "Arrête de publier au hasard." Bonus activés.

### J2 — Le problème profond

Email : "Pourquoi la majorité des sites stagnent malgré le travail." Amplifier la douleur. Pas vendre encore.

### J3 — Authority Loop™ en détail

Email + post : 5 étapes expliquées. Objectif : clarifier le mécanisme, rassurer, montrer la logique.

### J4 — Preuve & résultats

Email : études de cas + chiffres. Post : extrait étude de cas. Installer la crédibilité.

### J5 — Objections

Email : réponses aux 4 freins principaux (pas le temps / pas expert SEO / déjà du contenu / trop structuré).

### J6 — Urgence modérée

Email matin : rappel fermeture J+1. Email soir : focus bonus limités. "Les bonus disparaissent demain."

### J7 — Fermeture

Email matin : "Dernier jour." Email 18h : "Plus que quelques heures." Email 2h avant : court, direct, sans drama.

> Les portes ferment ce soir. Prochaine ouverture : indéterminée.

**Rythme total :** 8 à 10 emails sur 7 jours (J1: 1 / J2–J5: 1/jour / J6: 2 / J7: 2 à 3).

---

## Séquence email complète — 9 emails (lancement 7 jours)

### E1 — Ouverture (J1)

**Objet :** Les portes sont ouvertes.

Tu publies peut-être régulièrement. Mais si ton trafic stagne, ce n'est pas un problème d'effort. C'est un problème de structure.

Aujourd'hui, j'ouvre les inscriptions à schoolsWP Authority System™ — basé sur un mécanisme simple :

> Authority Loop™ — Structurer → Produire → Amplifier → Tester → Optimiser.

Une boucle stratégique. Pas une checklist.

Les bonus de lancement sont activés. Ils disparaîtront à la fermeture.

> [Rejoindre Authority System™]

---

### E2 — Le problème (J2)

**Objet :** Publier ne crée pas l'autorité

Tu peux publier 100 articles. Si ton site n'est pas structuré : Google comprend mal ton expertise, les IA ne peuvent pas te citer, tes visiteurs ne perçoivent pas ta cohérence. Résultat : stagnation.

Authority Loop™ commence par l'architecture. Sans structure, rien ne tient.

> [Découvrir la méthode]

---

### E3 — Le mécanisme (J3)

**Objet :** La boucle stratégique en 5 étapes

Authority Loop™ en clair : Structurer / Produire stratégique / Amplifier / Tester / Optimiser.

Chaque cycle renforce le précédent. Tu ne publies plus au hasard. Tu construis un actif.

> [Voir le programme]

---

### E4 — Preuve (J4)

**Objet :** Des résultats mesurables

Après application complète : +15 à +40 % CTR / +20 à +60 % trafic sur cluster structuré / +10 à +35 % conversion.

Pas en 7 jours. De manière cumulative. Authority Loop™ fonctionne parce qu'il repose sur structure, cohérence, itération.

> [Rejoindre Authority System™]

---

### E5 — Objections (J5)

**Objet :** "Je n'ai pas le temps."

Authority Loop™ ne te demande pas de produire plus. Il te demande de produire mieux. 1 page pilier stratégique vaut 10 articles isolés. Tu élimines le gaspillage.

Si tu cherches un hack rapide : ce n'est pas pour toi. Si tu veux construire un système durable :

> [Accéder au programme]

---

### E6 — Urgence (J6 matin)

**Objet :** Les bonus disparaissent bientôt

Encore inclus : Audit Authority Express / Dashboard stratégique / Workshop privé. Ils disparaissent à la fermeture. La méthode restera. Les bonus non.

> [Rejoindre maintenant]

---

### E7 — J-1 (J6 soir)

**Objet :** Demain, fermeture

Demain soir, les portes ferment. Si tu veux structurer ton site, construire une vraie autorité, arrêter de publier au hasard — c'est maintenant.

> [Rejoindre Authority System™]

---

### E8 — Dernier jour matin (J7)

**Objet :** Dernier jour

Ce soir, fermeture. La question n'est pas "est-ce que ça peut fonctionner ?". La question est : "Est-ce que continuer sans système est viable ?"

> [Je construis mon système stratégique]

---

### E9 — Dernière heure (J7, 2h avant fermeture)

**Objet :** Fermeture imminente

Les portes ferment dans quelques heures. Pas de relance. Pas de prolongation.

Soit tu continues à publier au hasard. Soit tu construis un système.

> [Rejoindre maintenant]

---

## Séquence email alignée VSL — 7 emails

Chaque email prépare → renforce → pousse vers la vidéo → pousse vers l'action. Lien VSL à insérer dans chaque email.

### V-E1 — Ouverture (J1)

**Objet :** Arrête de publier au hasard.

Tu publies. Tu travailles. Tu optimises. Mais si ton trafic stagne, ce n'est pas un problème d'effort. C'est un problème de structure.

Aujourd'hui, j'ouvre officiellement les inscriptions à schoolsWP Authority System™. J'y présente le mécanisme Authority Loop™ : une boucle stratégique en 5 étapes pour transformer ton WordPress en système d'autorité mesurable.

> [Regarde la vidéo ici]

Les bonus sont activés pour les premiers inscrits.

---

### V-E2 — Problème profond (J2)

**Objet :** Le vrai problème de ton site WordPress

La majorité des sites : accumulent du contenu / espèrent un pic SEO / testent au feeling. Publier plus ne crée pas l'autorité. L'autorité vient d'un système cohérent.

Dans la vidéo : pourquoi la structure change tout / pourquoi les IA privilégient la clarté / pourquoi l'itération est la clé.

> [Regarde la VSL ici]

---

### V-E3 — Mécanisme (J3)

**Objet :** La boucle stratégique en 5 étapes

Authority Loop™ : Structurer / Produire stratégique / Amplifier / Tester / Optimiser. Ce n'est pas une checklist. C'est une boucle. Chaque cycle renforce le précédent. Dans la vidéo, je te montre comment.

> [Accéder à la présentation]

---

### V-E4 — Preuve (J4)

**Objet :** +38 % de trafic sans publier plus

Quand on restructure un cluster existant : +20 à +60 % de trafic possible / +15 à +40 % de CTR / +10 à +35 % de conversion. Sans produire 50 contenus supplémentaires. Ce n'est pas magique. C'est structurel.

> [Voir Authority Loop™]

---

### V-E5 — Objections (J5)

**Objet :** "Je n'ai pas le temps."

Si tu manques de temps, tu as encore plus besoin d'un système. Authority Loop™ ne demande pas de produire plus. Il demande de produire mieux. Si tu as déjà du contenu, c'est un avantage. Je réponds aux objections dans la VSL.

> [Regarder maintenant]

---

### V-E6 — Urgence (J6)

**Objet :** Les bonus disparaissent demain

Bonus de lancement encore inclus : Audit Authority Express / Template Dashboard / Workshop privé. Ils disparaissent à la fermeture. Si tu voulais rejoindre, c'est le moment.

> [Rejoindre Authority System™]

---

### V-E7 — Fermeture (J7)

**Objet :** Ce soir, les portes ferment.

Continuer à publier au hasard — ou construire un système stratégique durable. Les inscriptions ferment ce soir. Prochaine ouverture : non définie.

> [Accès final ici]

---

## Modes d'utilisation

### Mode rédaction — produire un asset

Donne l'asset à créer (email, post LinkedIn, page de vente, script masterclass) — je le rédige dans le bon format, au bon ton, aligné sur la promesse Authority System.

### Mode planning — construire le calendrier

Donne la date d'ouverture cible — je génère le calendrier complet J-21 → J0 avec les actions par jour.

### Mode FluentCRM — configurer les automations

Donne le contexte (outil, liste, séquence existante) — je génère les configs FluentCRM (tags, séquences, scoring) prêtes à implémenter.

### Mode analyse — optimiser un lancement en cours

Donne les stats (ouvertures, clics, conversions) — j'identifie les points de friction et propose des corrections.

---

## Commandes rapides

| Commande                                | Action                                                                |
| --------------------------------------- | --------------------------------------------------------------------- |
| `Calendrier lancement [date ouverture]` | Génère le planning J-21 → J0 complet                                  |
| `Email [numéro] warm-up`                | Rédige l'email warm-up demandé (1 à 5)                                |
| `Email [numéro] vente`                  | Rédige l'email de vente demandé (1 à 7)                               |
| `Post LinkedIn [phase]`                 | Rédige le post pour la phase demandée (pré-chauffe / vente / clôture) |
| `Script masterclass`                    | Plan + script complet de la masterclass 45 min                        |
| `Page de vente courte`                  | Version condensée prête à publier                                     |
| `Page de vente longue`                  | Version complète 2000+ mots                                           |
| `Lead magnet Blueprint`                 | Contenu du Blueprint 90 jours à mettre en page                        |
| `Config FluentCRM`                      | Tags + séquences + scoring complets                                   |
| `KPIs lancement pour [audience N]`      | Projections réalistes selon la taille d'audience                      |
| `Donne la réponse pour [phase]`         | Output direct sans questions pour la phase demandée                   |

---

## Script VSL — Version standard (12–18 min)

Structure : Hook → Identification → Mécanisme → Logique → Preuve → Programme → Objections → Bonus/Urgence → CTA

**1 — Hook (0:00–1:30)**

> Si ton site WordPress publie régulièrement… mais que ton trafic stagne, que tes contenus vivent isolés, et que tes résultats sont irréguliers… Ce n'est pas un problème d'effort. C'est un problème de structure. Aujourd'hui, je vais te montrer comment transformer ton site en système d'autorité mesurable, grâce à un mécanisme simple : Authority Loop™.

**2 — Identification (1:30–3:00)**

La majorité des freelances et créateurs : publient sans architecture claire / optimisent au feeling / espèrent que "le prochain article" fera la différence. Mais publier plus ne crée pas l'autorité. L'autorité vient d'un système cohérent.

**3 — Introduction du mécanisme (3:00–6:00)**

Authority Loop™ — 5 étapes : Structurer / Produire stratégique / Amplifier / Tester / Optimiser. Ce n'est pas une checklist. C'est une boucle. Chaque cycle renforce le précédent. Tu construis un actif digital, pas une série d'articles.

**4 — Pourquoi ça fonctionne (6:00–8:00)**

Google fonctionne par structure sémantique. Les IA privilégient les contenus clairs et hiérarchisés. La performance repose sur l'itération. Authority Loop™ aligne architecture + contenu + amplification + test + optimisation. Logique d'ingénierie appliquée à WordPress.

**5 — Preuve & résultats (8:00–10:00)**

+15 à +40 % de CTR / +20 à +60 % de trafic cluster / +10 à +35 % d'amélioration conversion. Sans produire 50 contenus supplémentaires. Ce n'est pas magique. C'est structurel.

**6 — Présentation du programme (10:00–13:00)**

6 modules : Architecture / Priorisation / Autorité / Scalabilité / Expérimentation / Performance. Tu repars avec : architecture claire + page pilier stratégique + système omnicanal + boucle d'optimisation durable. Ce n'est pas théorique. C'est implémentable.

**7 — Objections (13:00–15:00)**

- Pas le temps ? Un système te fait gagner du temps.
- Pas expert SEO ? La méthode repose sur la structure, pas des hacks.
- Déjà du contenu ? Encore mieux — tu vas le transformer en actif stratégique.

**8 — Bonus & urgence (15:00–16:30)**

Pendant la période de lancement : Audit Authority Express / Template Dashboard / Workshop privé. Bonus réservés aux premiers inscrits. Quand les portes ferment, ils disparaissent.

**9 — CTA final (16:30–fin)**

> Continuer à publier au hasard ou construire un système stratégique durable. Les inscriptions sont ouvertes. Rejoins Authority System™ maintenant.

---

## Script VSL — Version high-ticket (15–20 min)

Posture : moins "formation", plus "méthode stratégique". Plus sélectif, plus premium, plus décisionnel. Orienté transformation profonde.

**1 — Hook polarisant (0:00–1:30)**

> Si tu veux juste publier plus… cette vidéo n'est pas pour toi. Si tu cherches un hack SEO rapide… ce n'est pas ici. Mais si tu veux transformer ton site WordPress en actif stratégique capable de générer trafic, autorité et conversion de manière prévisible… alors écoute attentivement.

**2 — La vérité inconfortable (1:30–3:30)**

La majorité travaille beaucoup mais ne construit pas. Ils produisent, optimisent ponctuellement, testent au hasard. Résultat : croissance irrégulière, autorité fragile, conversion moyenne, fatigue stratégique. Le problème n'est pas le travail. Le problème est l'absence de système.

**3 — Positionnement haut de gamme (3:30–5:00)**

Un site performant n'est pas un blog. C'est une architecture. Un système. Une machine cohérente. Les entreprises structurées opèrent avec une logique d'ingénierie. C'est exactement ce que fait Authority Loop™.

**4 — Le mécanisme (5:00–8:00)**

Authority Loop™ : Structurer / Produire stratégique / Amplifier / Tester / Optimiser. Chaque cycle augmente : cohérence thématique / compréhension algorithmique / conversion / stabilité. Ce n'est pas une méthode créative. C'est une logique systémique.

**5 — Logique avancée (8:00–11:00)**

Moteurs modernes : relations sémantiques + densité thématique + clarté informationnelle + cohérence interne. IA : structures hiérarchisées + contenus synthétisables + réponses explicites. Authority Loop™ aligne le site avec ces réalités et intègre l'itération mesurable. Pas d'optimisation au feeling. Des cycles contrôlés.

**6 — Preuve & impact (11:00–13:00)**

CTR en hausse / trafic cluster en progression / conversion améliorée / fatigue stratégique réduite. Pas des promesses spectaculaires. Des améliorations structurelles. Et les améliorations structurelles sont durables.

**7 — Ce que tu reçois (13:00–16:00)**

Authority System™ n'est pas une formation. C'est un cadre d'implémentation. Architecture stratégique + page pilier + système omnicanal + plan d'expérimentation + boucle d'optimisation. Et selon la version : audit personnalisé + feedback stratégique + accompagnement 90 jours. Ce n'est pas de l'information. C'est une transformation.

**8 — Filtrage (16:00–17:30)**

Pas pour : ceux qui veulent un hack rapide / qui refusent la discipline / qui cherchent une solution miracle. Pour : freelances ambitieux / créateurs structurés / agences qui veulent un système / ceux qui pensent long terme.

**9 — Urgence premium (17:30–18:30)**

Les places pour la version accompagnement sont limitées. Ce n'est pas un produit de masse. C'est un cadre stratégique. Quand les portes ferment, elles ferment.

**10 — CTA final (18:30–fin)**

> Tu peux continuer à publier et espérer. Ou tu peux construire un système. Si tu veux transformer ton WordPress en actif stratégique structuré… Rejoins Authority System™ maintenant.

### Notes de production VSL

- Durée cible : 12–18 min (standard) / 15–20 min (high-ticket)
- Format : face caméra ou voix over sur slides simples
- Rythme : 1 idée par plan, phrases courtes, pauses visuelles
- Slides : texte minimal — 3 mots max par ligne
- CTA à l'écran : le lien apparaît au moment du CTA final (pas avant)

### Structure visuelle — 33 slides (mapping complet)

**Acte 1 — Hook (Slides 1–4) : rapide**

- S1 : Écran noir, texte blanc — "Arrête de publier au hasard." (2s silence)
- S2 : "Si ton site WordPress : publie / travaille / mais stagne"
- S3 : "Ce n'est pas un problème d'effort. C'est un problème de structure."
- S4 : "Aujourd'hui, je vais te montrer le mécanisme Authority Loop™." → transition + musique légère

**Acte 2 — Problème (Slides 5–9) : rapide**

- S5 : "La majorité des sites : Produisent / Espèrent / Recommencent"
- S6 : "Articles isolés. Pas d'architecture. Pas de boucle."
- S7 : "Publier plus ne crée pas l'autorité."
- S8 : "L'autorité vient d'un système."
- S9 : "Sans système → pas d'effet cumulatif." → cut net

**Acte 3 — Mécanisme (Slides 10–16) : pédagogique**

- S10 : "Authority Loop™" + logo/cercle animé simple
- S11 : "STRUCTURER — Architecture. Clarté. Positionnement."
- S12 : "PRODUIRE STRATÉGIQUE — Pages piliers. FAQ IA. Maillage."
- S13 : "AMPLIFIER — Un contenu → 5 impacts."
- S14 : "TESTER — Hypothèse. KPI. Validation."
- S15 : "OPTIMISER — Itération continue."
- S16 : "Une boucle. Chaque cycle renforce le précédent." → animation circulaire douce

**Acte 4 — Logique (Slides 17–20) : crédibilité**

- S17 : "Google analyse la structure."
- S18 : "Les IA privilégient la clarté."
- S19 : "La performance repose sur l'itération."
- S20 : "Authority Loop™ aligne tout."

**Acte 5 — Preuve (Slides 21–24) : crédibilité**

- S21 : "+15 à +40 % de CTR"
- S22 : "+20 à +60 % de trafic cluster"
- S23 : "+10 à +35 % de conversion"
- S24 : "Pas magique. Structurel."

**Acte 6 — Offre (Slides 25–29) : décisif**

- S25 : "schoolsWP Authority System™"
- S26 : "6 Modules — Architecture / Autorité / Amplification / Test / Performance"
- S27 : "Tu repars avec : Architecture claire / Page pilier stratégique / Boucle durable"
- S28 : "Bonus limités : Audit / Dashboard / Workshop"
- S29 : "Accès immédiat."

**Acte 7 — Urgence & CTA (Slides 30–33) : décisif**

- S30 : "Les portes sont ouvertes."
- S31 : "Les bonus disparaissent à la fermeture."
- S32 : "Continuer à publier au hasard — OU — Construire un système stratégique"
- S33 : CTA final — fond clair, bouton visible, silence 3 secondes

**Règles visuelles**

- 1 idée = 1 slide
- Texte minimal (3 mots max par ligne)
- Fond clair premium, couleur chaude sur mots-clés
- Animation : fade + zoom léger — pas d'effets tape-à-l'œil
- Facecam : petite vignette, regard caméra sur CTA

**Outils compatibles** : Canva / Keynote / PowerPoint + OBS facecam

---

## Script VSL 3 minutes — Ultra condensée

Idéal pour : trafic froid, page mobile, ads, retargeting. Impact immédiat, aucun détour, CTA net.

**1 — Hook (0:00–0:30)**

> Si ton site WordPress publie régulièrement mais que ton trafic stagne, ce n'est pas un problème d'effort. C'est un problème de structure. Publier plus ne crée pas l'autorité. Construire un système, oui.

**2 — Le problème (0:30–1:00)**

La majorité des sites : publient sans architecture claire / produisent du contenu isolé / optimisent au feeling / espèrent un pic SEO. Résultat : stagnation. Tu travailles. Mais tu ne capitalises pas.

**3 — Authority Loop™ (1:00–1:45)**

Authority Loop™ : Structurer / Produire stratégique / Amplifier / Tester / Optimiser. Ce n'est pas une checklist. C'est une boucle. Chaque cycle renforce le précédent. Ton site devient plus fort, mois après mois.

**4 — Pourquoi ça fonctionne (1:45–2:15)**

Google comprend la structure. Les IA privilégient la clarté. La performance repose sur l'itération. Authority Loop™ aligne tout.

**5 — Résultats (2:15–2:35)**

+15 à +40 % de CTR / +20 à +60 % de trafic cluster / +10 à +35 % de conversion. Pas grâce à un hack. Grâce à un système.

**6 — L'offre (2:35–2:55)**

schoolsWP Authority System™ — 6 modules. Tu construis : architecture claire + page pilier stratégique + système omnicanal + boucle d'optimisation durable.

**7 — CTA final (2:55–fin)**

> Continuer à publier au hasard ou construire un actif stratégique durable ? Les inscriptions sont ouvertes. Rejoins Authority System™ maintenant.

---

## Script VSL courte — 5 à 7 minutes — Slides détaillées (11 slides, ~6 min 30)

Idéal pour : landing page / trafic froid-tiède / ads retargeting / page mobile. Impact rapide, clarté radicale, CTA net.

Style visuel : fond clair, typographie forte, beaucoup d'espace blanc, accent couleur chaude sur mots-clés / CTA, aucun stock photo.

| Slide | Timing    | Texte écran                                                                             | Ce que tu dis                                                       | Visuel                                            |
| ----- | --------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------- |
| S1    | 0:00–0:25 | "Arrête de publier au hasard."                                                          | Intro problème — stagnation pas liée à l'effort mais à la structure | Fond clair, gros texte centré                     |
| S2    | 0:25–1:00 | Contenus isolés / Maillage improvisé / Optimisations au feeling / Résultats irréguliers | La majorité travaille dur, peu construisent un système              | Liste simple, icônes fines                        |
| S3    | 1:00–1:20 | "Tu n'as pas besoin de plus d'articles. Tu as besoin d'un système."                     | Transition vers la solution                                         | Typographie seule, centré                         |
| S4    | 1:20–2:30 | Cercle Authority Loop™ — 5 étapes + logo au centre                                      | Explication brève de chaque étape (10–15 sec / étape)               | Cercle minimaliste, couleur chaude, flèches fines |
| S5    | 2:30–3:10 | "Chaque cycle renforce le précédent."                                                   | Logique boucle — le système devient plus fort chaque mois           | Typo seule, fond clair                            |
| S6    | 3:10–3:50 | Structure sémantique / Clarté IA / Itération mesurable                                  | Google + IA + performance = Authority Loop™ aligne tout             | Liste 3 points, icônes fines                      |
| S7    | 3:50–4:40 | +15–40 % CTR / +20–60 % trafic / +10–35 % conversion                                    | Présentation ton posé, crédible                                     | Chiffres en grand, fond sobre                     |
| S8    | 4:40–5:10 | Avant : Publier → Après : Construire un actif                                           | Tu passes d'un site qui publie à un système qui progresse           | Split visuel Avant / Après                        |
| S9    | 5:10–5:50 | schoolsWP Authority System™ — 6 modules / Templates / Application guidée                | Description du programme                                            | Titre fort + liste courte                         |
| S10   | 5:50–6:15 | Bonus : Audit / Dashboard / Workshop                                                    | Bonus lancement limités                                             | Liste 3 bonus, fond sobre                         |
| S11   | 6:15–fin  | "Continuer à publier au hasard — ou — Construire un système stratégique ?" + Bouton CTA | Fermeture décisionnelle                                             | Fond clair, bouton visible, silence 3 sec         |

**1 — Hook (0:00–0:45)**

> Si ton site WordPress publie régulièrement mais que ton trafic stagne, ce n'est pas un problème d'effort. C'est un problème de structure. La majorité des sites travaillent dur. Très peu construisent un système. Aujourd'hui, je vais te montrer comment transformer ton site en système d'autorité mesurable grâce à Authority Loop™.

**2 — Le problème (0:45–1:45)**

Tu publies. Tu optimises. Tu ajustes. Mais : tes contenus vivent isolés / ton maillage est improvisé / tes décisions sont intuitives / tes résultats sont irréguliers. Publier plus ne crée pas l'autorité. La cohérence, oui.

**3 — Le mécanisme (1:45–3:15)**

Authority Loop™ : Structurer / Produire stratégique / Amplifier / Tester / Optimiser. Ce n'est pas une checklist. C'est une boucle. Chaque cycle renforce le précédent. Tu passes d'un site qui publie à un système qui progresse.

**4 — Pourquoi ça fonctionne (3:15–4:15)**

Google comprend la structure. Les IA privilégient les contenus clairs. La performance repose sur l'itération. Authority Loop™ aligne architecture + contenu + amplification + test + optimisation. Logique d'ingénierie appliquée à WordPress.

**5 — Résultats (4:15–5:15)**

+15 à +40 % de CTR / +20 à +60 % de trafic cluster / +10 à +35 % de conversion. Pas grâce à un hack. Grâce à un système.

**6 — L'offre (5:15–6:15)**

schoolsWP Authority System™ — 6 modules. Tu construis : architecture claire + page pilier stratégique + cluster cohérent + machine omnicanale + boucle d'optimisation durable. Tu ne repars pas avec des idées. Tu repars avec un système.

**7 — Urgence & CTA (6:15–fin)**

> Les inscriptions sont ouvertes. Les bonus de lancement sont limités. Si tu veux arrêter de publier au hasard et commencer à construire un actif digital stratégique, rejoins Authority System™ maintenant.

---

## Ouverture story personnelle — Module VSL (0:00–1:20)

À insérer en tête de n'importe quelle version VSL. Remplace le hook générique. Humanise, installe la crédibilité, crée l'identification, amène naturellement au mécanisme.

**Slide 1 — Fond sobre, texte centré : "J'ai longtemps cru que publier plus suffisait."**

> Quand j'ai commencé à développer des sites WordPress, je pensais que la clé était simple : publier plus, optimiser un peu, ajouter un plugin SEO. Et attendre. Je travaillais. Je produisais. Mais les résultats restaient irréguliers.

**Slide 2 — Texte : "Le problème n'était pas le contenu. C'était l'absence de système."**

> Ce que j'ai compris plus tard, c'est que je n'avais pas un site stratégique. J'avais une accumulation de contenus. Pas de vraie architecture. Pas de logique de cluster. Pas de boucle d'optimisation. Je publiais. Mais je ne construisais pas.

**Slide 3 — Texte : "Le déclic : penser en système."**

> Le jour où j'ai arrêté de penser "article" et commencé à penser "architecture", tout a changé. J'ai structuré. J'ai relié. J'ai testé. J'ai optimisé. Et les résultats sont devenus cohérents. Prévisibles. Mesurables.

**Slide 4 — Texte : "C'est comme ça qu'est né Authority Loop™."**

> Authority Loop™ n'est pas né d'une théorie. Il est né d'un constat : un site WordPress performant n'est pas un blog actif. C'est un système structuré. Et aujourd'hui, je vais te montrer exactement comment le construire.

**Pourquoi ça fonctionne** : te positionne en praticien (pas formateur) / montre une évolution logique / introduit le mécanisme naturellement / crée confiance sans exagération.

**Version courte (VSL 5 min)** :

> J'ai longtemps cru que publier plus suffisait. Jusqu'à comprendre que ce n'était pas un problème de contenu… mais de structure. Authority Loop™ est né de ce déclic : arrêter de publier au hasard et construire un système.

---

## Script VSL high-ticket agressive — 6 à 8 minutes

Posture : autorité calme, tranchante. Polarise → filtre → élève. Vend transformation, pas contenu.

**1 — Ouverture polarisante (0:00–0:50)**

> Je vais être direct. Si ton site WordPress dépend encore de publier plus, espérer un pic SEO ou copier des stratégies génériques — tu ne construis pas un actif. Tu entretiens une illusion de progression. La question n'est pas "Comment publier plus ?" La question est : "Comment construire un système qui devient plus puissant chaque mois ?"

**2 — La vérité que personne ne dit (0:50–1:50)**

La majorité : travaillent énormément / publient régulièrement / optimisent au feeling. Mais ils n'ont aucun système. Résultat : trafic instable, autorité fragile, conversion irrégulière. Ce n'est pas un problème de compétence. C'est un problème d'ingénierie.

**3 — Le shift (1:50–3:00)**

Les sites qui dominent ne publient pas plus. Ils sont structurés. Ils fonctionnent comme des systèmes. Authority Loop™ : Structurer / Produire stratégique / Amplifier / Tester / Optimiser. Simple à comprendre. Extrêmement puissant quand appliqué correctement.

**4 — Pourquoi ça change tout (3:00–4:10)**

Authority Loop™ aligne : architecture sémantique + production stratégique + effet levier omnicanal + tests mesurables + optimisation continue. Ce n'est pas une technique SEO. C'est une logique d'ingénierie. Chaque cycle renforce le précédent. Tu ne dépends plus d'un article. Tu construis un actif.

**5 — Positionnement premium (4:10–5:10)**

CTR en hausse / trafic cluster renforcé / conversion améliorée / autorité cumulative. Mais surtout : clarté stratégique totale. Et ça, c'est ce qui change vraiment la trajectoire d'un business.

**6 — Le programme (5:10–6:10)**

schoolsWP Authority System™ n'est pas un cours. C'est une implémentation guidée. Tu construis : architecture stratégique + page pilier IA-friendly + cluster cohérent + système omnicanal + boucle d'optimisation. Tu repars avec un système opérationnel.

**7 — Filtrage (6:10–6:50)**

Ce programme n'est pas pour tout le monde. Pas pour ceux qui cherchent un hack rapide, une astuce SEO miracle, une méthode "publier plus". Pour ceux qui veulent : construire un actif / structurer leur expertise / dominer leur thématique.

**8 — Urgence calme (6:50–fin)**

> Les inscriptions sont ouvertes. Les bonus sont limités. Si tu veux continuer à publier au hasard, tu peux. Si tu veux construire un système stratégique durable, rejoins Authority System™ maintenant. La décision est simple. Continuer à produire. Ou commencer à structurer.

---

## Plan LinkedIn — Lancement 7 jours

Logique : Email convertit. LinkedIn chauffe. 1 post/jour, commentaires stratégiques, réponses actives. Jamais copier-coller des emails.

### Pré-chauffe (J-5 à J-1)

**Post 1 — Prise de conscience**

Hook : "Publier plus ne résout pas un problème de structure."

Contenu : 3 erreurs fréquentes + mini insight + question ouverte. CTA doux : "Je prépare quelque chose pour ceux qui veulent structurer leur WordPress." Pas encore de lien.

**Post 2 — Autorité**

Hook : "Ce qui bloque 80 % des sites WordPress n'est pas technique."

Explique : architecture absente, contenus isolés, pas de boucle d'optimisation. Pas encore de lien.

### J1 — Ouverture

Hook fort : "Les inscriptions sont ouvertes."

Structure : Problème → Mécanisme Authority Loop™ → Résultat → Lien. CTA : "Détails dans le premier commentaire." **Toujours mettre le lien en commentaire pour la portée organique.**

### J2 — Problème (narratif)

Format : "Un freelance me disait…" Décris le chaos sans système. Fin : "C'est exactement pour ça que j'ai créé Authority Loop™." Lien discret.

### J3 — Le mécanisme (pédagogique)

Décris les 5 étapes — 1 ligne par étape. Fin : "Ce n'est pas une checklist. C'est une boucle." Lien.

### J4 — Preuve (étude de cas)

Structure : Situation → Intervention → Résultat chiffré. CTA : "Les portes sont ouvertes cette semaine uniquement."

### J5 — Objections (filtrage fort)

Format : "Ce que ce programme n'est PAS." — Pas un hack / Pas une formation gadget / Pas pour tout le monde. Positionne en sélectivité, pas en défensive.

### J6 — Urgence maîtrisée

Hook : "Les bonus disparaissent demain." Rappelle valeur bonus. Lien.

### J7 — Fermeture

Matin : "Dernier jour pour rejoindre Authority System™."

Soir (post court) : "Les portes ferment ce soir. Prochaine session : incertaine." Lien.

### Stratégie commentaires (critique)

Sous chaque post : répondre rapidement, relancer discussion, ajouter mini-clarifications. Remonte le post dans l'algorithme + signale engagement.

### Optimisations profil pendant le lancement

- Épingler le post d'ouverture
- Mettre le lien en bio temporairement
- Ajouter bannière profil "Authority Loop™"
- Headline clair : "J'aide les freelances WordPress à structurer leur autorité et convertir durablement."

---

## Version lancement high-ticket — Edition Accompagnement

Positionnement : on ne vend plus une formation. On vend un système stratégique + accompagnement + transformation professionnelle. Ton posé, mais niveau élevé.

### Angle d'entrée

> Si ton WordPress ne génère pas de levier stratégique, ce n'est pas un site. C'est une vitrine. Et une vitrine ne construit pas une autorité.

### Ce que cette édition propose

Ce programme n'est pas une formation passive. C'est un accompagnement stratégique pour : structurer ton architecture, construire ton premier pilier, déployer ton cluster, lancer ton système omnicanal, installer ta boucle d'optimisation.

Tu ne regardes pas des vidéos. Tu construis.

### Positionnement sélectif

Réservé aux freelances établis, créateurs avancés, agences, entrepreneurs déjà en activité. Pas aux débutants, curieux ou testeurs.

### Ce qu'on délivre

- Audit stratégique complet
- Blueprint personnalisé
- Construction guidée du pilier
- Validation architecture cluster
- Plan d'expérimentation priorisé
- Suivi 90 jours
- Feedback direct

### Investissement assumé

Positionnement 2 000€ à 3 000€ selon formule. Justification : tu construis un actif stratégique + architecture durable + levier business. Ce n'est pas une dépense. C'est une construction.

### Places limitées — pourquoi c'est crédible

L'accompagnement est réel. Nombre restreint de participants pour garantir qualité et suivi. Pas de cohorte massive.

### Angle psychologique central

> Si ton site doit devenir un actif stratégique, il mérite un système structuré.

On n'applique pas de pression. On élève le niveau.

### CTA high-ticket

Ne jamais utiliser "Acheter maintenant". Utiliser :

- "Candidater à Authority System™ Edition Accompagnement"
- "Réserver un appel stratégique"

### Calendrier 7 jours (variante high-ticket)

| Jour | Contenu                                                 |
| ---- | ------------------------------------------------------- |
| J1   | Ouverture + positionnement sélectif                     |
| J2   | Pourquoi 90 % des sites stagnent malgré le travail      |
| J3   | Authority Loop™ en profondeur + démonstration mécanisme |
| J4   | Étude de cas avancée + résultats mesurables             |
| J5   | Ce qui différencie cette édition vs formation standard  |
| J6   | Fermeture imminente + processus de sélection            |
| J7   | Clôture des candidatures — décision finale              |

### Options version ultra-sélective

- Sélection sur dossier
- Entretien préalable obligatoire
- Bonus exclusifs pour les 10 premiers
- Prix progressif après lancement (tarif augmente J3 → J7)

Positionnement terminal : "Ce n'est pas pour tout le monde."

---

## Objets emails + preview text — optimisés A/B

> 3 variantes objet + 3 variantes preview par email. Objectif : maximiser l'ouverture.
> Règle de base : objet ≤ 45 caractères, preview 60–90 caractères, pas de répétition mot pour mot.

### EMAIL 1 — Ouverture (angle : déclic)

**Objets**

- A. Tu publies… mais ça stagne ?
- B. Le vrai problème de ton WordPress
- C. Ce n'est pas un problème d'effort

**Preview**

- A. Ce n'est pas un problème d'effort.
- B. Le vrai blocage est ailleurs.
- C. Voici ce qui manque à ton site.

### EMAIL 2 — Le problème (angle : recadrage)

**Objets**

- A. Publier plus ne suffit pas
- B. Pourquoi ton trafic plafonne
- C. Le piège des contenus isolés

**Preview**

- A. Le volume ne crée pas l'autorité.
- B. Sans système, tu accumules seulement.
- C. Ce n'est pas une question d'articles.

### EMAIL 3 — Le mécanisme (angle : curiosité structurée)

**Objets**

- A. La boucle qui change tout
- B. 5 étapes. Pas plus.
- C. Voici le mécanisme

**Preview**

- A. Une boucle stratégique simple.
- B. Voici le mécanisme complet.
- C. Structurer. Tester. Optimiser.

### EMAIL 4 — Preuve (angle : concret)

**Objets**

- A. +38 % de trafic sans publier plus
- B. Ce que ça change vraiment
- C. Des résultats mesurables

**Preview**

- A. Structure + itération.
- B. Des résultats mesurables.
- C. Pas de hack. Un système.

### EMAIL 5 — Objections (angle : frein principal)

**Objets**

- A. "Je manque de temps."
- B. Pas expert SEO ?
- C. Trop structuré pour toi ?

**Preview**

- A. Justement. C'est le problème.
- B. Un système fait gagner du temps.
- C. Moins d'improvisation. Plus d'impact.

### EMAIL 6 — Urgence douce (angle : bonus)

**Objets**

- A. Les bonus disparaissent
- B. Derniers jours pour les bonus
- C. Après ça, c'est fini

**Preview**

- A. Fin du lancement bientôt.
- B. Après ça, ils ne reviendront pas.
- C. Derniers jours pour en profiter.

### EMAIL 7 — Dernier jour (angle : décision)

**Objets**

- A. Ce soir, ça ferme
- B. Dernière chance
- C. La décision est stratégique

**Preview**

- A. Prochaine ouverture : inconnue.
- B. Décision stratégique.
- C. Dernières heures pour rejoindre.

### EMAIL 8 — Dernières heures (angle : minimaliste)

**Objets**

- A. Fermeture imminente
- B. Dernier rappel
- C. On ferme

**Preview**

- A. Après minuit, c'est terminé.
- B. C'est maintenant ou plus tard.
- C. Le système reste. Les bonus non.

### Combos ultra performants (objet + preview)

| Objet                      | Preview                                   |
| -------------------------- | ----------------------------------------- |
| 5 étapes. Pas plus.        | Une boucle stratégique que peu utilisent. |
| Ce soir, ça ferme          | Après ça, plus de bonus.                  |
| Publier plus ne suffit pas | Sans structure, tu accumules seulement.   |
| "Je manque de temps."      | Justement. C'est le problème.             |

### Objets format brut (1–2 utilisations max par séquence)

`Structure.` / `Stop.` / `Réfléchis.` / `Décision.` / `Lis ça.`

---

## Preview texts finaux — lancement + post-fermeture

> Version affinée, 3 options par email. Règle : objet = tension, preview = contexte/bénéfice.

### Lancement

| Email | Objet                             | Preview A                                | Preview B                            | Preview C                            |
| ----- | --------------------------------- | ---------------------------------------- | ------------------------------------ | ------------------------------------ |
| E1    | Tu publies… mais ça stagne ?      | Ce n'est pas un problème d'effort.       | Le vrai problème est ailleurs.       | Tu n'as pas besoin de publier plus.  |
| E2    | Publier plus ne suffit pas        | Voici ce qui bloque vraiment ton trafic. | Le contenu isolé ne construit rien.  | Sans système, tu accumules.          |
| E3    | La boucle qui change tout         | 5 étapes. Pas plus.                      | Une logique simple, mais structurée. | Ce n'est pas une checklist.          |
| E4    | +38 % de trafic sans publier plus | Structure + itération = progression.     | Pas un hack. Un système.             | Même effort, plus d'impact.          |
| E5    | "Je manque de temps."             | Justement.                               | Un système te fait gagner du temps.  | Le vrai coût, c'est l'improvisation. |
| E6    | Les bonus disparaissent           | Après ça, ils ne reviennent pas.         | Décision stratégique.                | Les portes ferment bientôt.          |
| E7    | Ce soir, ça ferme                 | Continuer au hasard ou structurer ?      | Prochaine ouverture : indéterminée.  | La décision est maintenant.          |
| E8    | Fermeture imminente               | Dernier rappel.                          | Plus que quelques heures.            | Après ce soir, c'est terminé.        |

### Séquence post-fermeture (PF1–PF5)

**PF1 — C'est fermé**
Objet : `C'est fermé. Voilà la suite.`

- A. Ce que je te recommande maintenant.
- B. Voici ton prochain pas stratégique.
- C. Tu peux avancer quand même.

**PF2 — Mini action**
Objet : `Fais ça en 30 minutes`

- A. Ton premier mini Authority Loop.
- B. Simple. Structuré. Actionnable.
- C. Applique ça aujourd'hui.

**PF3 — Croyance**
Objet : `Pourquoi publier ne suffit plus`

- A. Le problème n'est pas WordPress.
- B. Ce n'est pas une question d'effort.
- C. La cohérence crée la croissance.

**PF4 — Alternative**
Objet : `Plan 7 jours (gratuit)`

- A. Lance ton premier cycle maintenant.
- B. Même sans la formation.
- C. Voici comment avancer.

**PF5 — Liste d'attente**
Objet : `Tu veux être prévenu ?`

- A. Réponds simplement à cet email.
- B. Je te mets sur liste prioritaire.
- C. On se reparle à la prochaine ouverture.

### Preview cassé (effet rupture — max 2x/séquence)

| Objet      | Preview                  |
| ---------- | ------------------------ |
| Structure. | Ce que personne ne fait. |
| Stop.      | Lis ça avant de publier. |

---

## Règles de ton (toujours respecter)

- Tutoiement systématique
- Zéro promesse non prouvée — toujours "dans mon cas" / "sur schoolsWP"
- Mots interdits : disruptif, game changer, scalable, hack, révolutionnaire, incroyable, en un clic, sans effort, il suffit de
- Urgence réelle, jamais artificielle — la fermeture doit être tenue
- Ton : direct, pédagogique, chaleureux, orienté résultats

---

## Plan LinkedIn conversationnel — 7 jours

> Objectif : conversation avant conversion. Pas "vendeur agressif". Lien toujours en commentaire.
> Structure psychologique : Polarisation → Diagnostic → Éducation → Story → Preuve → Tension → Fermeture.

### J1 — Polarisation

**Hook :** Tu publies. Mais est-ce que tu construis ?

Publier régulièrement ne crée pas l'autorité. La structure, oui.

La majorité des sites WordPress accumulent du contenu, espèrent un pic SEO, optimisent au feeling. Ce n'est pas un problème d'effort. C'est un problème de structure.

**Question finale :** Tu es plutôt "volume" ou "structure" ?

_CTA : "Lien en commentaire." — lien vers la page de vente ou VSL_

---

### J2 — Diagnostic

**Hook :** Ton site WordPress a-t-il une vraie architecture stratégique ?

Checklist rapide : Page pilier claire ? / Cluster cohérent ? / Maillage pensé ? / Priorités définies ?

**Question finale :** Honnêtement, combien de points as-tu cochés ?

---

### J3 — Éducation

**Hook :** Authority Loop™ en 5 mots.

Structurer. Produire. Amplifier. Tester. Optimiser.

**Question finale :** Laquelle de ces 5 étapes est la plus négligée selon toi ?

---

### J4 — Story

**Hook :** "Pendant longtemps, je pensais que publier plus suffisait…"

Raconter la prise de conscience. Transition vers le mécanisme.

**Question finale :** À quel moment tu as réalisé que publier plus ne suffisait pas ?

---

### J5 — Preuve

**Hook :** +38 % de trafic après simple restructuration. Pas de nouveau contenu. Juste structure + maillage.

**Question finale :** Tu optimises plus… ou tu crées plus ?

---

### J6 — Friction (tension / polarisation)

**Hook :** Tu veux un hack rapide ? Authority Loop™ n'est pas pour toi.

Tu veux construire un actif durable ? On peut parler.

**Question finale :** Team hack rapide ou team système durable ?

---

### J7 — Fermeture

**Hook :** Ce soir, je ferme les inscriptions. Mais la vraie question n'est pas "est-ce que tu rejoins". C'est : est-ce que tu veux continuer sans système ?

_CTA discret : "Lien en commentaire."_

---

### Techniques pour multiplier les commentaires

| Technique           | Application                                                        |
| ------------------- | ------------------------------------------------------------------ |
| Micro-questions A/B | "Volume ou Structure ?" — réponse facile, engagement élevé         |
| Demande d'avis      | "Tu en penses quoi ?" — simple et puissant                         |
| Réponses manuelles  | Répondre à chaque commentaire + sous-question = portée doublée     |
| DM intelligent      | Commentaire "je veux structurer" → "Je t'envoie les détails en DM" |

### Règles de format LinkedIn

- Phrases courtes, lignes espacées
- 1 idée par paragraphe
- 0 jargon
- Lien JAMAIS dans le post — toujours en commentaire (portée organique)
- Répondre à chaque commentaire manuellement

### Extensions optionnelles

- 1 carrousel "Authority Loop™ en 5 slides"
- 1 post storytelling personnel ("ce que j'ai mal fait pendant 2 ans")
- 1 mini vidéo face cam 60 secondes
- 1 post "ce que personne ne dit sur le SEO WordPress"

---

## Scripts LinkedIn — légendes exactes J1–J7

> Prêts à copier-coller. CTA toujours en commentaire (jamais dans la légende).
> Variante conversationnelle disponible pour booster les commentaires (voir fin de section).

---

**J1 — Déclic**

Tu publies régulièrement.

Mais est-ce que tu construis vraiment quelque chose ?

La plupart des sites WordPress travaillent dur.
Très peu construisent un système.

Sans architecture claire :
– tes contenus vivent isolés
– ton trafic stagne
– tes résultats restent irréguliers

Ce n'est pas un problème d'effort.
C'est un problème de structure.

J'ai formalisé ça dans un mécanisme simple : Authority Loop™.

Je l'explique en détail ici. 👇

_CTA commentaire :_ Commente STRUCTURE et je t'envoie le lien en DM. (ou lien direct en premier commentaire)

---

**J2 — Le vrai problème**

Publier plus ne crée pas l'autorité.

Tu peux écrire 100 articles… et rester "moyen" partout.

Pourquoi ?

Parce que Google et les IA lisent la cohérence.

Un article isolé = impact limité.
Un système cohérent = effet cumulatif.

La différence est là. 👇

_CTA commentaire :_ Si tu veux voir comment structurer ça proprement, le lien est en commentaire.

---

**J3 — Le mécanisme**

Authority Loop™ repose sur 5 étapes :

1️⃣ Structurer
2️⃣ Produire stratégique
3️⃣ Amplifier
4️⃣ Tester
5️⃣ Optimiser

Ce n'est pas une checklist.

C'est une boucle.

Chaque cycle renforce le précédent.

Tu passes d'un site qui publie à un système qui progresse. 👇

_CTA commentaire :_ Si tu veux appliquer ça sur ton WordPress, lien en commentaire.

---

**J4 — Preuve**

Quand tu structures + itères :

✔ +15 à +40 % de CTR
✔ +20 à +60 % de trafic cluster
✔ +10 à +35 % de conversion

Sans produire 50 contenus supplémentaires.

La différence ? Structure + cohérence + itération.

Pas un hack. Un système. 👇

_CTA commentaire :_ Tu peux voir le programme complet ici → (lien en commentaire)

---

**J5 — Objections**

"Je manque de temps."

Justement.

Un système te fait gagner du temps.

Tu arrêtes :
– d'improviser
– de publier sans cap
– de tester au hasard

Tu suis une logique claire. Et tu capitalises. 👇

_CTA commentaire :_ Si tu veux arrêter d'improviser, le lien est en commentaire.

---

**J6 — Bonus limité**

Les bonus de lancement disparaissent demain.

Audit Authority Express.
Authority Dashboard.
Workshop structuration pilier.

Après fermeture : retirés.

Simple. 👇

_CTA commentaire :_ Si tu veux en profiter avant fermeture, lien en commentaire.

---

**J7 — Fermeture**

Ce soir, les inscriptions ferment.

Deux options :

1️⃣ Continuer à publier au hasard.
2️⃣ Construire un système stratégique durable.

Authority Loop™ n'est pas un hack.

C'est une logique d'ingénierie appliquée à WordPress.

Les portes ferment ce soir. 👇

_CTA commentaire :_ Dernière fenêtre → lien en commentaire.

---

### Variante conversationnelle (fort engagement — 1–2x max)

À utiliser à la place du CTA standard sur 1 ou 2 posts :

- "Tu publies sans architecture claire ? Oui / Non ?"
- "Quel est ton principal blocage aujourd'hui : Structure, trafic ou conversion ?"

Génère commentaires + DM + signal algorithmique.

---

## Carrousels LinkedIn — 7 jours complets

> Format 1080×1350 (4:5) — 8 slides : Cover + 6 contenu + 1 CTA
> Texte : 8–14 mots max/slide. Style : fond clair, typo nette, accent chaud sur CTA.

### J1 — Déclic

| Slide   | Texte                                                                         |
| ------- | ----------------------------------------------------------------------------- |
| 1 Cover | Tu publies. Mais est-ce que tu construis ?                                    |
| 2       | La plupart des sites WordPress… publient sans système.                        |
| 3       | Résultat : contenu isolé, trafic dispersé, conversions instables.             |
| 4       | Ce n'est pas un problème d'effort. C'est un problème de structure.            |
| 5       | Un article isolé = impact limité.                                             |
| 6       | Un système cohérent = effet cumulatif.                                        |
| 7       | J'ai formalisé ça en un mécanisme : Authority Loop™.                          |
| 8 CTA   | Si tu veux arrêter d'improviser : lien en commentaire (inscriptions ouvertes) |

**Covers A/B :** A — "Tu publies. Mais tu ne construis pas." / B — "Transforme ton WordPress en système stratégique."

**Caption :** Tu publies. Mais est-ce que tu construis vraiment quelque chose de cohérent ? Ce n'est pas un problème de motivation. C'est un problème de système. 👉 Ton site est structuré… ou improvisé ? Écris "STRUCTURE" en commentaire si tu veux que je t'explique Authority Loop™.

---

### J2 — Le vrai problème

| Slide   | Texte                                                      |
| ------- | ---------------------------------------------------------- |
| 1 Cover | Publier plus ne crée pas l'autorité.                       |
| 2       | Tu peux écrire 100 articles… et rester "moyen" partout.    |
| 3       | Pourquoi ? Parce que Google et les IA lisent la cohérence. |
| 4       | Sans architecture : tes contenus ne se renforcent pas.     |
| 5       | Sans boucle : tu optimises au feeling.                     |
| 6       | Sans système : les résultats restent irréguliers.          |
| 7       | La solution n'est pas "plus". C'est "mieux structuré".     |
| 8 CTA   | Je t'explique le mécanisme demain. (lien en commentaire)   |

**Covers A/B :** A — "Publier plus ne crée pas l'autorité." / B — "Pourquoi ton trafic plafonne vraiment."

**Caption :** Publier plus ne crée pas l'autorité. La cohérence, oui. Un article isolé = visibilité ponctuelle. Un cluster structuré = effet cumulatif. Est-ce que ton contenu se renforce mutuellement ? Dis-moi en commentaire : "ISOLÉ" ou "STRUCTURÉ".

---

### J3 — Le mécanisme

| Slide   | Texte                                                  |
| ------- | ------------------------------------------------------ |
| 1 Cover | Authority Loop™ : la boucle en 5 étapes                |
| 2       | 1) Structurer : architecture, piliers, clusters.       |
| 3       | 2) Produire : contenu profond, clair, IA-friendly.     |
| 4       | 3) Amplifier : 1 contenu → multi-canaux.               |
| 5       | 4) Tester : CTR, CTA, angle, offre.                    |
| 6       | 5) Optimiser : GSC, itération, conversion.             |
| 7       | Ce n'est pas une checklist. C'est une boucle.          |
| 8 CTA   | Tu veux l'appliquer sur ton site ? lien en commentaire |

**Covers A/B :** A — "Authority Loop™ en 5 étapes simples" / B — "La boucle que 90% ignorent"

**Caption :** 5 étapes. Pas 27 hacks. Structurer → Produire → Amplifier → Tester → Optimiser. Simple. Quelle étape bloques-tu le plus en ce moment ? Réponds avec le chiffre : 1 / 2 / 3 / 4 / 5 ?

---

### J4 — Preuve

| Slide   | Texte                                                |
| ------- | ---------------------------------------------------- |
| 1 Cover | Des résultats mesurables. Pas des promesses.         |
| 2       | Quand tu structures + itères, tu capitalises.        |
| 3       | CTR : +15 à +40 % (titles + intention + clarté)      |
| 4       | Trafic cluster : +20 à +60 % (maillage + profondeur) |
| 5       | Conversion : +10 à +35 % (cohérence + friction ↓)    |
| 6       | Pas en 7 jours. Mais structurellement.               |
| 7       | La magie n'existe pas. L'itération, oui.             |
| 8 CTA   | Tu veux un système durable ? lien en commentaire     |

**Covers A/B :** A — "+38% sans publier plus" / B — "Structure > Volume"

**Caption :** Quand tu arrêtes de publier au hasard : ✔ CTR augmente ✔ Trafic cluster progresse ✔ Conversion s'améliore. Pas grâce à un hack. Grâce à une logique. Tu préfères : A) Produire plus — B) Structurer mieux. Réponds A ou B.

---

### J5 — Objections

| Slide   | Texte                                                                  |
| ------- | ---------------------------------------------------------------------- |
| 1 Cover | "Oui mais…" 3 objections qui te bloquent                               |
| 2       | "Je manque de temps." → Un système fait gagner du temps.               |
| 3       | "Je ne suis pas expert SEO." → Méthode de structure, pas de hacks.     |
| 4       | "J'ai déjà du contenu." → Parfait : on transforme l'existant en actif. |
| 5       | Ce qui coûte cher : publier sans cap pendant des mois.                 |
| 6       | Ce qui paie : un cycle clair, répété.                                  |
| 7       | Authority Loop™ = ordre + logique + itération.                         |
| 8 CTA   | Si tu veux du concret : lien en commentaire                            |

**Covers A/B :** A — ""Je manque de temps."" / B — "Ce n'est pas un problème de temps."

**Caption :** "Je manque de temps." C'est l'objection que j'entends le plus. Mais publier sans système… ça prend encore plus de temps. Si tu avais un système clair, qu'est-ce que ça changerait pour toi ? Réponds en une phrase.

---

### J6 — Bonus

| Slide   | Texte                                                   |
| ------- | ------------------------------------------------------- |
| 1 Cover | Bonus de lancement : dernier jour demain                |
| 2       | Si tu rejoins maintenant, tu reçois…                    |
| 3       | 🎁 Audit Authority Express (retour ciblé)               |
| 4       | 🎁 Authority Dashboard (pilotage GSC/CTR)               |
| 5       | 🎁 Workshop Pilier (structure + plan action)            |
| 6       | Après fermeture : bonus retirés. Point.                 |
| 7       | Tu peux attendre. Ou construire ton système maintenant. |
| 8 CTA   | Dernière fenêtre pour les bonus : lien en commentaire   |

**Covers A/B :** A — "Les bonus disparaissent demain" / B — "Maintenant ou plus tard ?"

**Caption :** Les bonus de lancement disparaissent demain. Mais ce n'est pas ça le plus important. La vraie question : est-ce que tu veux encore improviser 6 mois de plus ? Écris "MAINTENANT" si tu veux le lien.

---

### J7 — Fermeture

| Slide   | Texte                                                        |
| ------- | ------------------------------------------------------------ |
| 1 Cover | Ce soir, ça ferme.                                           |
| 2       | Deux options :                                               |
| 3       | 1) Continuer à publier au hasard.                            |
| 4       | 2) Construire un système stratégique durable.                |
| 5       | Un site "moyen" coûte cher : temps + énergie + opportunités. |
| 6       | Un système progresse : mois après mois.                      |
| 7       | Authority Loop™ = structure → itération → cumul.             |
| 8 CTA   | Dernier jour : lien en commentaire (portes ferment ce soir)  |

**Covers A/B :** A — "Ce soir, ça ferme." / B — "Improviser… ou structurer ?"

**Caption :** Ce soir, les portes ferment. Tu peux continuer à publier sans cap. Ou construire un système stratégique durable. Il n'y a pas de bon choix universel. Il y a ton choix. Tu en es où aujourd'hui ?

---

### Kit design carrousels

- **Format** : 1080×1350 (4:5)
- **Couleurs** : fond gris très clair ou blanc / accent chaud (#E668D4 ou #00D400) pour CTA
- **Typo** : Nunito Sans headings, Roboto body
- **Icons** : set minimal ligne — architecture / plume / mégaphone / éprouvette / clé
- **CTA** : toujours en bas, même position sur chaque slide 8 (répétition = conversion)
- **Recommandation A/B par jour** : J1→A, J2→B, J3→B, J4→A, J5→A, J6→A, J7→B

---

## Plan DM → Appel stratégique

> Commentaire LinkedIn → DM → qualification → appel 20–30 min → inscription.
> Logique : diagnostiquer, clarifier, projeter, relier, proposer. Jamais forcer.

### Vue d'ensemble

Commentaire → DM d'ouverture → Qualification → Diagnostic rapide → Invitation appel → Appel structuré → Proposition → Suivi

---

### Étape 1 — DM d'ouverture

Message court, naturel, après un commentaire :

> "Merci pour ton commentaire 👌 Dis-moi, aujourd'hui ton principal blocage c'est quoi : trafic / structure / conversion ?"

---

### Étape 2 — Qualification

Selon réponse :

> "OK, tu me dis que c'est surtout [blocage]. Aujourd'hui tu as combien de contenus environ ?"

Puis : "Tu as déjà une page pilier centrale ?"

Chercher : volume existant / niveau de structuration / maturité.

---

### Étape 3 — Mini diagnostic express

Après 2–3 réponses :

> "Si je résume : tu publies régulièrement / tu n'as pas de vraie architecture / tu optimises au feeling — c'est cohérent ?"

Attendre validation avant de continuer.

---

### Étape 4 — Transition vers appel

> "Je pense qu'en 20 minutes je peux t'aider à clarifier ta priorité stratégique. On peut faire un appel rapide cette semaine si tu veux."

Positionner comme **diagnostic**, pas vente.

---

### Étape 5 — Planification

Toujours proposer 2 créneaux précis :

> "Je suis dispo mercredi 14h ou jeudi 17h — lequel te convient ?"

---

### Structure appel (20–30 min)

| Étape       | Durée  | Contenu                                                                                           |
| ----------- | ------ | ------------------------------------------------------------------------------------------------- |
| Contexte    | 5 min  | Où en es-tu ? Objectif 6 mois ?                                                                   |
| Diagnostic  | 10 min | Pages piliers / maillage / GSC / CTR / tunnel — identifier 1–2 points bloquants                   |
| Projection  | 5 min  | "Si tu continues comme maintenant, où tu seras dans 6 mois ?" — créer tension légère              |
| Solution    | 5 min  | Relier au mécanisme Authority Loop™ — phase concernée                                             |
| Proposition | —      | "Authority System™ est fait pour ça. Je peux t'expliquer comment ça fonctionnerait pour ton cas." |

**Clôture :** "Est-ce que tu veux qu'on mette ça en place ?" → silence → laisser répondre.

**Si hésitation :** "Qu'est-ce qui te freine aujourd'hui ?" — jamais de pression.

---

### Taux réaliste (sur 20 DM qualifiés)

- 8–12 appels
- 3–6 inscriptions

---

### Options avancées

- Enregistrer mini Loom 3 min en DM avant appel (ultra puissant)
- Proposer audit visuel express avant appel
- Format appel collectif mini-groupe (scalable)

---

## Scripts DM LinkedIn — Qualification & Closing

> Flow complet : commentaire → DM → qualification → micro-valeur → offre.
> Règle d'or : poser 1 question / reformuler / micro-valeur / proposer. Jamais pousser.

### CTA déclencheurs (mots-clés commentaires)

| Mot-clé   | Post           | Réponse publique      |
| --------- | -------------- | --------------------- |
| SYSTEME   | J1 — Déclic    | "Je t'écris en DM 👌" |
| STRUCTURE | J2 — Problème  | "Je t'écris en DM 👌" |
| LOOP      | J3 — Mécanisme | "Je t'écris en DM 👌" |
| ANALYSE   | J4 — Preuve    | "Je t'écris en DM 👌" |
| PRIORITÉ  | J5 — Objection | "Je t'écris en DM 👌" |
| BONUS     | J6 — Bonus     | "Je t'écris en DM 👌" |
| QUESTION  | J7 — Fermeture | "Je t'écris en DM 👌" |

---

### Message d'ouverture DM (standard)

> "Merci pour ton commentaire 👌 Pour que je t'oriente correctement : aujourd'hui ton principal blocage c'est quoi ? 1️⃣ Trafic 2️⃣ Structure 3️⃣ Conversion 4️⃣ Priorité floue — Réponds avec le numéro."

---

### Branchements selon réponse

**1️⃣ Trafic :** "Tu as combien d'articles environ ? Et est-ce que tu as une vraie page pilier centrale ?"

**2️⃣ Structure :** "Ton contenu est plutôt : A) Beaucoup d'articles dispersés / B) Peu mais non reliés / C) Pas encore structuré"

**3️⃣ Conversion :** "Tu as déjà un lead magnet ou une séquence email active ?"

**4️⃣ Priorité floue :** "Dis-moi en une phrase : ton objectif dans 6 mois ?"

---

### Scripts par situation

**Pas de page pilier (trafic stagnant)**

> "Le vrai levier dans ton cas n'est pas 'plus de contenu'. C'est centralisation + maillage. 8–12 contenus autour d'un pilier changent totalement la dynamique. C'est la première étape d'Authority Loop™. Tu veux que je t'envoie le détail ?"

**Manque de temps**

> "Justement. Publier sans système prend plus de temps que structurer correctement. Authority Loop™ te fait concentrer sur l'essentiel, pas sur la dispersion."

**Sceptique sur la niche**

> "Google analyse structure + profondeur, pas la niche. La vraie question : est-ce que ton expertise est structurée clairement ? Si oui → effet cumulatif. Sinon → dispersion."

**Déjà 80–100 articles**

> "Parfait. Tu es assis sur un potentiel énorme. La question n'est pas 'plus'. C'est 'mieux structuré'. C'est exactement le profil idéal pour Authority System™."

**Hésitant**

> "C'est une bonne question. Ton objectif principal sur les 6 prochains mois, c'est quoi ? Si ton objectif est [X], alors oui, un système structuré est clé. Sinon, ce n'est pas prioritaire."

---

### 5 conversations types (entraînement)

**Conv. 1 — 50 articles, pas de pilier :** Blocage trafic → pas de pilier central → "50 articles sans pilier = 50 signaux dispersés" → lien Authority Loop™

**Conv. 2 — Manque de temps + clarté :** "Souvent le manque de temps vient du manque de structure" → décris les 3 pertes de temps → propose le programme

**Conv. 3 — Sceptique coaching parental :** Valider que Google lit la structure, pas la niche → "L'expertise structurée crée l'effet cumulatif"

**Conv. 4 — 100+ articles :** Problème de hiérarchie, pas de volume → "Si ton positionnement n'est pas clair pour toi, il ne l'est pas pour Google"

**Conv. 5 — Profil chaud (GSC actif) :** Identifier pages à potentiel → pilier central → maillage → proposer appel stratégique direct

---

### Flow semi-automatisé

```
Commentaire mot-clé
→ Réponse publique "Je t'écris en DM"
→ DM ouverture (4 choix numérotés)
→ Branchement adapté
→ Diagnostic semi-scripté
→ Micro-valeur
→ "Tu veux que je t'envoie le détail ?" (demander permission)
→ Envoi lien + "lis la partie mécanisme"
→ Option appel 20 min (profils chauds)
→ Relance douce 48h si silence
```

**Outils recommandés :** réponses enregistrées LinkedIn / Text Blaze / Notion banque de réponses / tagging manuel chaud–tiède–froid.

---

## Système scoring + closing premium

> Pour profils haute valeur — accompagnement 90 jours high-ticket.

### Scoring rapide (4 critères)

| Critère                 | +1            | +2                  | +3                       |
| ----------------------- | ------------- | ------------------- | ------------------------ |
| Trafic actuel           | 0–500/mois    | 500–5k              | 5k+                      |
| Volume contenu          | < 20 articles | 20–80               | 80+                      |
| Clarté objectif         | Flou          | Moyen               | Clair                    |
| Capacité investissement | Non exprimée  | Intéressé formation | Intéressé accompagnement |

**Résultat :** 4–6 → Formation autonome / 7–9 → Premium / 10–12 → High-ticket accompagnement

---

### Script appel stratégique premium (20 min)

| Phase          | Durée     | Script                                                                                                                          |
| -------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Cadrage        | 0–3 min   | "L'objectif n'est pas de te vendre quoi que ce soit. C'est de voir si un système structuré peut accélérer ta trajectoire."      |
| Diagnostic     | 3–8 min   | Trafic source ? / Pilier central ? / Maillage pensé ou organique ? / GSC actif ? — noter les failles                            |
| Projection     | 8–12 min  | "Si rien ne change, dans 6 mois ton site sera où ?" → silence → "Et si tu avais une architecture claire + boucle d'itération ?" |
| Recommandation | 12–16 min | Formation (autonomie) / Premium (besoin cadre) / High-ticket (fort potentiel)                                                   |
| Closing        | 16–20 min | "Si tu veux le faire seul, la formation suffit. Si tu veux accélérer, on peut le faire ensemble." → silence → laisser parler    |

---

### Script closing high-ticket (score 10–12)

> "Tu as déjà le trafic. Tu as déjà le volume. Ce qui manque, c'est l'orchestration. Si tu continues seul, tu avanceras. Si on structure ensemble, tu accélères. Je prends X accompagnements par trimestre. Si tu veux, on bloque ta place."

---

### Suivi post-appel (si pas de décision immédiate)

Message 24h après :

> "J'ai repensé à notre échange. Le vrai levier dans ton cas reste [X]. Si tu veux qu'on le structure ensemble, dis-le moi."

---

### Règle d'or closing

Ne jamais envoyer le lien sans permission. Ne jamais pitcher sans avoir reformulé le problème. Toujours : diagnostiquer → clarifier → projeter → relier → proposer.

---

## Séquence email VSL — 8 emails alignés à la vidéo

Séquence 7 jours + email J8 (fermeture imminente). Ton : direct, structuré, posé. Structure psychologique : Déclic → Problème → Mécanisme → Preuve → Sécurité → Urgence → Décision → Fermeture.

### E1 — Déclic (J1)

**Objet :** Arrête de publier au hasard.

Tu publies. Tu optimises. Tu travailles.
Mais si ton trafic stagne, ce n'est pas un problème d'effort. C'est un problème de structure.

La majorité des sites WordPress publient sans système.

Authority Loop™ est un mécanisme simple en 5 étapes :
Structurer → Produire → Amplifier → Tester → Optimiser

Une boucle stratégique qui transforme ton site en actif digital.

Les inscriptions à schoolsWP Authority System™ sont ouvertes.

👉 Découvrir la méthode

Accès immédiat. Bonus limités pendant le lancement.

---

### E2 — Problème (J2)

**Objet :** Publier plus ne résout pas ça.

Publier plus ne crée pas l'autorité.

Ce qui crée l'autorité : une architecture claire, un maillage stratégique, une logique d'itération.

Sans système, tu accumules. Avec un système, tu capitalises.

Authority Loop™ transforme ton contenu existant en actif structuré.

👉 Construire ton système stratégique

---

### E3 — Mécanisme (J3)

**Objet :** La boucle qui change tout.

Authority Loop™ repose sur 5 étapes :

1️⃣ Structurer — 2️⃣ Produire stratégique — 3️⃣ Amplifier — 4️⃣ Tester — 5️⃣ Optimiser

Chaque cycle renforce le précédent. Ce n'est pas une checklist. C'est une boucle.

Tu ne dépends plus du hasard.

👉 Voir le programme

---

### E4 — Preuve (J4)

**Objet :** Ce que ça change concrètement.

Quand Authority Loop™ est appliqué :

✔ +15 à +40 % de CTR — ✔ +20 à +60 % de trafic cluster — ✔ +10 à +35 % de conversion

Sans produire 50 contenus supplémentaires. La différence ? Structure + itération.

👉 Rejoindre Authority System™

---

### E5 — Sécurité (J5)

**Objet :** "Je manque de temps."

Justement. Un système te fait gagner du temps.

Tu arrêtes : d'improviser / de publier sans stratégie / de tester au hasard.

Authority System™ est conçu pour être appliqué progressivement.

👉 Construire ton Authority Loop™

---

### E6 — Urgence (J6)

**Objet :** Les bonus disparaissent bientôt.

Les bonus de lancement sont réservés aux inscrits actuels :

- Audit Authority Express
- Template Dashboard
- Workshop privé

Quand les portes ferment, ils disparaissent.

👉 Rejoindre avec les bonus

---

### E7 — Décision (J7)

**Objet :** Ce soir, ça ferme.

Continuer à publier au hasard — ou — Construire un système stratégique durable.

Les inscriptions ferment ce soir. Prochaine ouverture : indéterminée.

👉 Je construis mon système maintenant

---

### E8 — Fermeture imminente (J7 soir)

**Objet :** Fermeture imminente.

Dernier rappel. Les portes ferment dans quelques heures.

Si tu veux transformer ton site en système d'autorité mesurable :

👉 Rejoins Authority System™ maintenant.

---

## Séquence post-fermeture — 5 emails

Objectif : gérer frustration, récupérer hésitants, préparer réouverture, maintenir autorité. Pas de réouverture magique — rester premium.

### PF1 — Fermeture confirmée (J+1)

**Objet :** C'est fermé.

Les inscriptions à schoolsWP Authority System™ sont officiellement fermées.

La réalité reste la même : publier sans système te coûtera plus cher que la formation.

Prochaine ouverture : non planifiée. En attendant, je partage des contenus pour t'aider à structurer ta réflexion.

---

### PF2 — Coût de l'inaction (J+3)

**Objet :** Le coût invisible.

Chaque mois sans structure : temps gaspillé, opportunités perdues, autorité diluée.

Authority Loop™ n'est pas un hack. C'est un accélérateur stratégique.

Si tu veux être prioritaire à la prochaine ouverture :
👉 Inscris-toi sur la liste d'attente.

---

### PF3 — Mini-valeur stratégique (J+5)

**Objet :** Une chose à corriger dès aujourd'hui.

Exercice : regarde tes 10 derniers articles.

- Sont-ils reliés stratégiquement ?
- Ont-ils un pilier central ?
- Ont-ils un objectif mesurable ?

Si la réponse est non, tu viens d'identifier ton premier levier Authority Loop™.

👉 Rejoindre la liste d'attente

---

### PF4 — Témoignage post-lancement (J+10)

**Objet :** Retour d'un membre.

"Je pensais manquer de trafic. En réalité, je manquais de structure."

En 30 jours : architecture clarifiée, pilier structuré, tests lancés.

Authority Loop™ n'accélère pas le hasard. Il accélère la cohérence.

👉 Liste prioritaire ici

---

### PF5 — Pré-annonce douce (J+15)

**Objet :** Réouverture prochaine.

Je prépare la prochaine session Authority System™.

Les membres de la liste d'attente auront : accès prioritaire, bonus exclusifs, conditions de lancement.

👉 Liste d'attente prioritaire

---

## Séquence liste d'attente chauffée — 7 emails

Durée : 7–10 jours. Rythme : 1 email tous les 2 jours. Logique : Éducation → Projection → Autorité → Qualification → Pré-vente mentale.

### LA1 — Confirmation + Positionnement

**Objet :** Tu es sur la liste prioritaire.

Tu es maintenant sur la liste d'attente Authority System™.

Ça veut dire une chose : tu veux structurer ton site. Pas juste publier.

Authority Loop™ : Structurer → Produire stratégique → Amplifier → Tester → Optimiser.

Dans les prochains emails, j'explique pourquoi la majorité des sites stagnent malgré le travail.

---

### LA2 — Coût structurel invisible

**Objet :** Le vrai coût de l'absence de système.

Chaque mois sans structure : contenus isolés, autorité diluée, opportunités perdues.

Le problème n'est pas le trafic. C'est la cohérence.

Authority Loop™ ne t'apprend pas à produire plus. Il t'apprend à construire mieux.

---

### LA3 — Projection concrète

**Objet :** Imagine ton site dans 90 jours.

Architecture claire. Pilier central fort. Cluster cohérent. Boucle d'optimisation active.

Pas plus de travail. Plus de structure.

C'est ce que construit Authority System™.

---

### LA4 — Mini-preuve pédagogique

**Objet :** Un exercice simple (2 minutes).

3 questions :

1. As-tu une page pilier centrale forte ?
2. Ton maillage renforce-t-il réellement ton autorité ?
3. As-tu une boucle d'optimisation active ?

Si non → tu as identifié ton levier principal. C'est exactement ce que nous structurons dans Authority System™.

---

### LA5 — Différenciation forte

**Objet :** Pourquoi 90 % des formations SEO échouent.

Elles enseignent des techniques, des outils, des hacks. Mais pas un système.

Authority Loop™ est une logique complète :
Architecture → Production → Amplification → Test → Optimisation

Ce n'est pas une méthode partielle. C'est un cadre global.

---

### LA6 — Qualification

**Objet :** Est-ce vraiment pour toi ?

Authority System™ est pour toi si :
✔ Tu veux structurer ton expertise
✔ Tu veux un système durable
✔ Tu es prêt à appliquer

Ce n'est pas pour toi si : tu cherches un hack rapide, tu refuses la discipline.

---

### LA7 — Pré-annonce réouverture

**Objet :** Réouverture imminente.

La prochaine session Authority System™ ouvre bientôt.

Les membres de la liste prioritaire auront : accès anticipé, bonus spécifiques, places limitées.

Je t'envoie les détails très bientôt.

---

## Plan LinkedIn post-fermeture — 15 jours

Logique : Clarté → Autorité → Tension → DM → Liste d'attente. Ton : posé, structuré, premium. Pas de "désolé c'est fermé". On reste en position d'autorité.

### Semaine 1 — Consolider l'autorité

**Post 1 — "C'est fermé." (J+1)**

Hook : "Les inscriptions sont fermées."

Corps : La plupart des gens attendent le dernier moment. Les décisions stratégiques ne sont pas impulsives.

CTA : Prochaine ouverture non planifiée. Commentaire "SYSTEME" si tu veux être prioritaire.

Objectif : générer commentaires + DM entrants.

---

**Post 2 — Le coût invisible (J+3)**

Hook : "Le vrai coût, ce n'est pas la formation."

Corps : Le vrai coût = publier sans structure / optimiser sans système / produire sans capitaliser.

CTA : "Tu as une architecture claire ?"

Objectif : provoquer introspection.

---

**Post 3 — Mini audit public (J+5)**

Hook : "Regarde tes 10 derniers articles."

Corps checklist :

- Pilier central ?
- Maillage cohérent ?
- Objectif mesurable ?
- CTA aligné ?

CTA : "Si tu veux que je regarde ton cas, écris AUDIT."

Objectif : DM entrants qualifiés.

---

### Semaine 2 — Créer l'anticipation

**Post 4 — Étude de cas courte (J+7)**

Format Avant/Après : site structuré, CTR amélioré, cluster renforcé.

CTA : "C'est ça Authority Loop™."

Objectif : crédibilité.

---

**Post 5 — Polarisation douce (J+10)**

Hook : "Publier plus n'est pas une stratégie."

Corps : Ce qui compte = Structure + Itération + Optimisation.

CTA : "Tu publies ou tu construis ?"

Objectif : engagement + filtrage.

---

**Post 6 — Liste prioritaire (J+12)**

Hook : "La prochaine session ouvrira uniquement aux inscrits prioritaires."

Corps : accès anticipé, bonus spécifiques, places limitées.

CTA : Commentaire "LOOP" pour être prioritaire.

---

### Micro-stratégie DM post-fermeture

Quand quelqu'un commente → répondre en DM :

> "Tu veux structurer ton site ou optimiser un existant ?"

Ensuite : identifier niveau → envoyer ressource → proposer liste prioritaire.

Règle : qualification d'abord, pas de closing brutal.

| Objectif                | Levier                          |
| ----------------------- | ------------------------------- |
| Maintenir visibilité    | Posts réguliers (2–3/semaine)   |
| Créer tension           | Rareté réelle + ouverture floue |
| Qualifier naturellement | Mots-clés DM (AUDIT, LOOP)      |
| Alimenter liste attente | CTA doux sur chaque post        |

---

## Stratégie lancement high-ticket

Positionnement : Autorité. Sélectivité. Clarté. On ne vend plus une méthode — on vend une implémentation stratégique accompagnée.

**Prix cible** : 2 000€ → 5 000€+ selon niveau d'implication.

**Promesse** : En 90 jours, tu structures ton écosystème WordPress et lances ton premier cycle Authority Loop™ avec validation stratégique.

### Repositionnement fondamental

| Low-ticket             | High-ticket                           |
| ---------------------- | ------------------------------------- |
| "Rejoins la formation" | "Candidater pour travailler ensemble" |
| Convaincre             | Sélectionner                          |
| Urgence artificielle   | Sélectivité réelle                    |
| Page de vente longue   | Contenu → Qualification → Appel       |

---

### Phase 1 — Contenu d'autorité (J1–J10)

Objectif : créer la prise de conscience profonde. Pas de vente directe.

- Post LinkedIn long format : "Pourquoi la majorité des sites stagnent"
- Mini-audit public (commentaire AUDIT)
- Étude de cas détaillée (Avant/Après)
- Contenu pédagogique Authority Loop™

---

### Phase 2 — Masterclass / Workshop stratégique

Titre : "Comment transformer ton WordPress en système d'autorité mesurable en 90 jours."

Structure :

1. Le problème systémique
2. Authority Loop™ (mécanisme)
3. Étude de cas
4. Erreurs fréquentes
5. Invitation à candidater (pas vendre — qualifier)

---

### Phase 3 — Candidature

Formulaire filtrant :

- Situation actuelle (trafic, volume, ancienneté site)
- Objectif 90 jours
- Blocage principal
- Motivation / investissement envisagé

High-ticket = sélectivité. Filtrer avant l'appel.

---

### Phase 4 — Appel stratégique (structure)

| Phase        | Contenu                                                      |
| ------------ | ------------------------------------------------------------ |
| Diagnostic   | Trafic, architecture, pilier, maillage                       |
| Blocage      | Identifier le point de friction principal                    |
| Projection   | "Si on structure ensemble, dans 90 jours ton site sera où ?" |
| Présentation | Accompagnement, roadmap, livrables, suivi                    |
| Décision     | Silence après proposition — laisser parler                   |

---

### Livrables high-ticket — ce qui justifie le prix

- Audit stratégique complet
- Roadmap 90 jours personnalisée
- Validation page pilier
- Feedback mensuel sur production
- Session optimisation CTR
- Suivi KPI éditorial

On vend : **Clarté + Accélération + Sécurité**.

---

### Script d'invitation à candidature

> "Si tu veux implémenter Authority Loop™ seul, la version standard est faite pour toi. Si tu veux que je t'accompagne personnellement pour structurer ton écosystème et accélérer les résultats sur 90 jours, alors tu peux candidater."

CTA : 👉 Candidater pour l'accompagnement Authority

---

### Positionnement mental high-ticket (à communiquer)

- Ce n'est pas pour tout le monde
- Places limitées (3–5 par trimestre)
- Intense et structurant
- Je choisis avec qui je travaille

---

### Timeline lancement high-ticket

| Semaine | Action                                  |
| ------- | --------------------------------------- |
| S1      | Contenu d'autorité (4–5 posts LinkedIn) |
| S2      | Masterclass + ouverture candidatures    |
| S3      | Appels stratégiques + closing           |

---

### Structure tarifaire

| Offre              | Prix    | Format                      |
| ------------------ | ------- | --------------------------- |
| Groupe limité      | 2 500€  | 5–8 personnes, 90 jours     |
| Semi-privé         | 4 000€  | 2–3 personnes, accès direct |
| Accompagnement 1:1 | 6 000€+ | Individuel, roadmap dédiée  |

---

## Lancement high-ticket avec appel stratégique obligatoire

Dynamique fondamentale : on ne vend plus, on sélectionne. Pas de paiement direct — Application → Appel → Décision.

**Positionnement** : Ce programme n'est pas ouvert à tous. Accessible sur candidature uniquement. Tu ne poursuis pas le prospect. Tu filtres.

---

### Structure lancement (10 jours)

**Phase 1 — Pré-positionnement (J-7 à J-3)**

Objectif : élever le niveau mental. Pas d'offre. Juste du cadre.

Contenus LinkedIn / email :

- "Pourquoi la majorité des sites ne deviendront jamais des actifs"
- "La différence entre publier et construire"
- "Ce que j'ai changé pour passer au niveau stratégique"

---

**Phase 2 — Annonce (J-2)**

> "J'ouvre 15 places pour un accompagnement stratégique Authority System™."

Points clés à communiquer :

- Pas une formation de masse
- Accompagnement structuré
- Candidature obligatoire

CTA : lien vers page candidature.

---

**Phase 3 — Page application (minimaliste)**

Structure :

- **Headline** : "Deviens stratégique ou reste dans l'improvisation."
- **Qui est sélectionné** : freelances sérieux, entrepreneurs structurés, agences ambitieuses
- **Qui n'est pas sélectionné** : chercheurs de hacks, curieux non engagés, "je verrai plus tard"
- **CTA** : 👉 Je candidate pour un appel stratégique

---

**Phase 4 — Appel stratégique (45 min)**

| Étape              | Durée  | Contenu                                        |
| ------------------ | ------ | ---------------------------------------------- |
| Diagnostic actuel  | 10 min | Trafic, architecture, contenu, positionnement  |
| Analyse structure  | 15 min | Pilier, maillage, cluster, GSC                 |
| Projection         | 10 min | "Dans 90 jours avec ce système, tu seras où ?" |
| Présentation offre | 5 min  | Authority System™ premium — livrables + format |
| Décision           | 5 min  | Silence. Laisser parler.                       |

Règle d'or :

> "Si ça fait sens pour toi, on peut avancer. Sinon, tu repars avec un plan clair."

---

**Phase 5 — Fermeture (J+7)**

Email : "Les candidatures ferment ce soir."

- Nombre de places réel (10–20 max)
- Pas de fausse rareté

---

### Offre high-ticket — Authority System™ Accompagnement 90 jours

Inclut :

- Audit architecture complet
- Structuration cluster sémantique
- Refonte page pilier
- Plan omnicanal (contenu + LinkedIn)
- Tests prioritaires + optimisation GSC avancée
- Sessions privées hebdomadaires

**Positionnement prix** : 3 000€ – 6 000€ selon niveau d'accompagnement.

---

### Comparatif lancement classique vs high-ticket

| Classique     | High-ticket             |
| ------------- | ----------------------- |
| Vente directe | Candidature             |
| Volume        | Sélection               |
| Urgence prix  | Urgence place           |
| CTA achat     | CTA appel               |
| "Rejoins"     | "Montre que tu es prêt" |

---

### Script court d'annonce premium

> "J'ouvre 15 places pour accompagner des freelances et entrepreneurs qui veulent transformer leur WordPress en actif stratégique.
>
> Ce n'est pas une formation de masse. C'est un cadre structuré avec accompagnement réel.
>
> Si tu veux candidater pour un appel stratégique, le lien est ci-dessous."

---

## VSL — Ouverture story personnelle (1–2 min)

Script d'ouverture pour ancrer la crédibilité sans ego, créer l'identification, et introduire Authority Loop™ naturellement.

> Il y a quelques années, je faisais exactement comme tout le monde.
>
> Je publiais. Régulièrement. Sérieusement. Avec de bons contenus.
>
> Et pourtant… les résultats étaient instables.
>
> Un article performait. Le suivant disparaissait. Le trafic montait… puis stagnait.
>
> Je travaillais. Mais je ne construisais pas.
>
> Et c'est là que j'ai compris quelque chose de simple.
>
> Le problème n'était pas la qualité. Ce n'était pas WordPress. Ce n'était pas le SEO.
>
> C'était l'absence de système.
>
> Je produisais du contenu. Je n'avais pas d'architecture. Pas de logique cumulative. Pas de boucle d'optimisation.
>
> Alors j'ai arrêté de chercher des hacks.
>
> Et j'ai commencé à structurer. Architecture claire. Pages piliers. Clusters cohérents. Tests mesurables. Optimisation continue.
>
> Et tout a changé. Pas en une semaine. Mais de manière structurelle. Chaque mois devenait plus solide que le précédent.
>
> C'est de là qu'est né Authority Loop™.

**Transition** : "Aujourd'hui, je vais te montrer comment appliquer cette logique à ton propre site WordPress. Pas pour publier plus. Mais pour construire un actif digital durable."

---

## VSL Premium / High-Ticket — Script complet (11 min)

Ton : posé, sélectif, systémique. On vend un changement de niveau, pas une formation.

**0:00–1:30 — Positionnement élite**

> La plupart des sites WordPress publient. Très peu construisent.
>
> Publier est une activité. Construire est une stratégie.
>
> Si ton objectif est simplement de "faire du contenu", ce programme n'est pas pour toi.
>
> Si ton objectif est de transformer ton site en actif stratégique durable, alors écoute attentivement.

**1:30–3:00 — Le vrai problème**

> Le problème n'est pas le SEO. Pas l'IA. Pas ton thème.
>
> C'est l'absence d'architecture décisionnelle.
>
> La majorité des créateurs produisent sans cartographie claire, optimisent sans logique cumulative, mesurent sans stratégie.
>
> Ils travaillent dans le flux. Ils ne construisent pas un système.
>
> Sans système, il n'y a pas d'effet composé.

**3:00–5:00 — Le changement de niveau**

> Authority Loop™ n'est pas une méthode de contenu. C'est une logique d'ingénierie.
>
> Structurer → Produire stratégique → Amplifier → Tester → Optimiser.
>
> Chaque cycle renforce l'autorité. Chaque itération augmente la valeur de l'actif.
>
> Tu passes de "créer du contenu" à "construire un système d'autorité."

**5:00–6:30 — Pourquoi ça fonctionne**

> Les moteurs modernes fonctionnent par cohérence sémantique. Les IA privilégient les structures hiérarchisées. Les systèmes performants reposent sur l'itération mesurable.
>
> Authority Loop™ aligne : Architecture → Production → Amplification → Validation → Optimisation. Ce n'est pas créatif. C'est systémique.

**6:30–8:00 — Ce que ça change concrètement**

> Le trafic devient prévisible. Les pages deviennent des actifs. Les clusters se renforcent mutuellement. La conversion devient structurelle.
>
> Tu ne cherches plus "le prochain pic". Tu construis une courbe stable et cumulative.

**8:00–10:00 — L'offre**

> schoolsWP Authority System™ est un programme stratégique structuré. 6 modules. Mais surtout : un cadre décisionnel.
>
> Tu y construis : architecture claire, page pilier stratégique, cluster cohérent, logique omnicanale maîtrisée, boucle d'optimisation durable.
>
> Ce programme demande de la discipline. Il n'est pas conçu pour ceux qui cherchent un raccourci. Il est conçu pour ceux qui veulent changer de niveau.

**10:00–11:00 — Sélectivité & CTA**

> Ce programme n'est pas pour tout le monde. Il est pour les freelances qui veulent devenir référence, les créateurs qui veulent structurer leur expertise, les agences qui veulent industrialiser intelligemment.
>
> Les inscriptions sont ouvertes. La décision n'est pas émotionnelle. Elle est stratégique.
>
> Si tu veux construire un actif WordPress durable, rejoins schoolsWP Authority System™.

---

## Séquence email premium — alignée VSL high-ticket

7 jours, 8 emails. Ton : posé, clair, exigeant. Pas de dramatisation ni de faux compte à rebours.

### EP1 — Ouverture (J1)

**Objet :** Publier n'est pas construire.

Tu publies. Tu optimises. Tu ajustes.

Mais la vraie question : est-ce que tu construis un actif… ou est-ce que tu produis du contenu ?

La majorité des sites WordPress travaillent dur. Très peu ont une architecture stratégique.

C'est précisément pour ça que j'ai créé schoolsWP Authority System™. Un cadre structuré. Un mécanisme clair : Authority Loop™. Pas pour produire plus. Pour construire mieux.

👉 Découvrir Authority System™

---

### EP2 — Problème structurel (J2)

**Objet :** Le vrai blocage n'est pas le SEO.

Ce n'est pas ton plugin. Ce n'est pas ton thème. Ce n'est pas l'algorithme.

Le vrai blocage est l'absence d'architecture. Sans architecture : pas d'effet cumulatif, pas de cohérence sémantique forte, pas d'optimisation durable.

Authority Loop™ commence là. Structurer avant de produire.

👉 Voir comment fonctionne la méthode

---

### EP3 — Changement de niveau (J3)

**Objet :** Il y a deux types de créateurs.

Ceux qui publient. Et ceux qui construisent.

La différence ? Les seconds pensent en système. L'autorité est cumulative. L'optimisation est itérative. La cohérence est stratégique.

Authority System™ n'est pas un programme de contenu. C'est un changement de niveau.

👉 Accéder au programme

---

### EP4 — Preuve rationnelle (J4)

**Objet :** Pourquoi Authority Loop™ fonctionne réellement.

Google comprend la structure. Les IA privilégient la hiérarchie claire. Les systèmes performants reposent sur l'itération mesurable.

Authority Loop™ aligne : Architecture → Production → Amplification → Test → Optimisation.

Quand cette logique est appliquée : CTR en hausse, trafic cluster renforcé, conversion plus stable. Ce n'est pas magique. C'est structurel.

👉 Rejoindre Authority System™

---

### EP5 — Objection temps (J5)

**Objet :** "Je n'ai pas le temps."

Justement. Un système te fait gagner du temps. Parce qu'il élimine : la production dispersée, les tests improvisés, les décisions floues.

Authority Loop™ ne rajoute pas du travail. Il supprime le gaspillage.

👉 Construire mon système stratégique

---

### EP6 — Sélectivité (J6)

**Objet :** Ce programme n'est pas pour tout le monde.

Si tu cherches un hack rapide, ne t'inscris pas. Si tu refuses la discipline stratégique, ne t'inscris pas.

Authority System™ est conçu pour ceux qui veulent structurer leur expertise, un actif durable, changer de niveau.

Les inscriptions ferment bientôt.

👉 Voir les détails

---

### EP7 — Dernier jour matin (J7)

**Objet :** Dernière opportunité.

Ce soir, les inscriptions ferment. Les bonus disparaissent.

La décision n'est pas émotionnelle. Elle est stratégique.

Continuer à publier sans système — ou — Construire un actif durable.

👉 Rejoindre Authority System™

---

### EP8 — Fermeture (J7 soir)

**Objet :** Fermeture dans quelques heures.

Les portes ferment ce soir. Pas de réouverture immédiate prévue.

Si Authority Loop™ correspond à ton niveau d'exigence, c'est maintenant.

👉 Accéder au programme

---

## Page de vente minimaliste luxe

Espace, gravité, sélectivité. Moins de texte — plus de silence. Page qui respire.

---

**schoolsWP Authority System™**

Transforme ton WordPress en actif stratégique durable.

Basé sur le mécanisme propriétaire Authority Loop™.

Architecture. Autorité. Optimisation continue.

---

Publier est une activité.
Construire est une stratégie.

La majorité des sites publient. Très peu structurent.

Sans architecture : pas d'autorité cumulative, pas de cohérence sémantique, pas de performance durable.

---

**Authority Loop™** — une boucle stratégique en 5 phases :

Structurer → Produire stratégique → Amplifier → Tester → Optimiser

Chaque cycle renforce le précédent. Ce n'est pas une méthode de contenu. C'est une logique d'ingénierie.

---

**Résultats observables**

+15 à +40 % de CTR après optimisation stratégique
+20 à +60 % de trafic sur cluster structuré
+10 à +35 % d'amélioration conversion

Pas de hack. Un système.

---

**Le programme — 6 modules structurés**

Tu construis : architecture claire, page pilier stratégique, cluster cohérent, logique omnicanale maîtrisée, boucle d'optimisation durable. Tu repars avec un système.

---

**Sélectif par nature**

Pour : freelances qui veulent devenir référence, créateurs qui veulent structurer leur expertise, agences qui veulent industrialiser intelligemment.

Pas pour : ceux qui cherchent un raccourci, ceux qui refusent la discipline stratégique.

---

**Offre de lancement — bonus réservés aux premiers inscrits**

Audit stratégique. Dashboard d'optimisation. Workshop structuration pilier.

Disparaissent à la fermeture.

---

La décision est stratégique.

Continuer à publier — ou — Construire un actif.

**👉 Rejoindre Authority System™**

Accès immédiat.

---

## Landing ultra courte — 1 scroll

Impact immédiat. Zéro bruit. 1 seule décision. Page qui filtre.

---

Transforme ton site WordPress en actif stratégique durable.

Basé sur le mécanisme propriétaire Authority Loop™.

**Structurer. Produire. Amplifier. Tester. Optimiser.**

---

Publier est une activité. Construire est une stratégie.

La majorité des sites publient. Très peu créent une autorité cumulative.

Sans architecture : pas de cohérence, pas d'effet levier, pas d'optimisation durable.

---

Authority Loop™ est une boucle stratégique. Chaque cycle renforce le précédent. Chaque mois devient plus solide que le précédent.

Pas un hack. Un système.

---

Ce que tu construis :

- Une architecture claire
- Une page pilier stratégique
- Un cluster cohérent
- Une logique omnicanale maîtrisée
- Une boucle d'optimisation continue

---

Ce programme est pour ceux qui veulent changer de niveau. Pas pour ceux qui cherchent un raccourci.

La décision est stratégique.

Continuer à publier — ou — Construire un actif.

**👉 Rejoindre Authority System™**

Accès immédiat.

---

## Authority Domination — Roadmap 24 mois

Objectif : faire de schoolsWP la référence francophone WordPress orientée business, SEO et automatisation. Effet d'autorité cumulatif — pas "du contenu", un actif.

### Phase 1 — Fondation (M1–M6)

**Cibles** : freelances WP, créateurs, formateurs, entrepreneurs solo.

**3 piliers SEO** : Apprendre WordPress / Optimiser WordPress (SEO, performance) / Monétiser WordPress (funnels, LMS, affiliation).

**Production minimale** : 2 articles SEO profonds + 4 posts LinkedIn + 2 vidéos YouTube + 1 lead magnet /2 mois + 2 newsletters/mois.

**KPI cibles** : 50–80 articles, 1 500–3 000 visiteurs/mois, 1 000 abonnés email, 1ère traction affiliation.

### Phase 2 — Expansion (M7–M12)

**Leviers** : interviews experts WP, articles invités, podcast/série YouTube experts, études de cas réelles, comparatifs ultra complets, amplification LinkedIn.

**KPI cibles** : 5 000–10 000 visiteurs/mois, 3 000+ abonnés email, 10+ backlinks solides, CA affilié régulier, premiers clients consulting inbound.

### Phase 3 — Domination (M13–M18)

**Leviers** : guides définitifs 10 000+ mots, masterclasses trimestrielles, outils gratuits, templates premium, mini formations gratuites.

**KPI cibles** : 15 000+ visiteurs/mois, 8 000+ abonnés email, pipeline consulting stable.

### Phase 4 — Monétisation max (M19–M24)

**Déploiement** : formation signature schoolsWP, programme avancé SEO + Funnel WP, communauté premium, bundle templates, partenariats marques WP.

**Architecture revenus** : affiliation récurrente + formation signature + consulting haut de gamme + communauté premium + templates.

**KPI cibles** : 25 000+ visiteurs/mois, 15 000+ abonnés email, 6 figures annuelles.

---

### Plan chiffré mois par mois

| Période | Trafic | Emails | CA affilié | CA formation | Consulting |
| ------- | ------ | ------ | ---------- | ------------ | ---------- |
| M6      | 2 500  | 1 000  | 1 200 €    | —            | 2 leads    |
| M12     | 10 000 | 5 000  | 4 000 €    | —            | 5 leads    |
| M18     | 22 000 | 12 500 | 7 000 €    | 15 000 €     | 9 leads    |
| M24     | 30 000 | 18 000 | 10 000 €   | 30 000 €     | 10 000 €   |

**Fin Année 1** : ~25–35k€ cumulés. **Accélérateurs x2** : 3 articles/mois, backlinks actifs, collaborations influenceurs WP, ads retargeting, lead magnet agressif.

---

### 10 sujets SEO à effet levier maximal

| #   | Sujet                           | Levier                                           |
| --- | ------------------------------- | ------------------------------------------------ |
| 1   | Meilleur plugin SEO WordPress   | Intent commerciale + affiliation Rank Math/Yoast |
| 2   | Meilleur hébergement WordPress  | Commissions élevées + décision critique          |
| 3   | Créer une formation en ligne WP | LMS + affiliation Tutor LMS/LearnDash            |
| 4   | Tunnel de vente WordPress       | Consulting + formation premium                   |
| 5   | WordPress pour freelance        | Consulting + formation avancée                   |
| 6   | Optimiser la vitesse WordPress  | Universel + plugins premium affiliés             |
| 7   | Meilleur CRM WordPress          | FluentCRM + automation — angle rare FR           |
| 8   | Créer un site WP de A à Z       | TOFU massif — porte d'entrée cocon               |
| 9   | Maintenance WordPress           | Intent business + consulting récurrent           |
| 10  | Monétiser son site WordPress    | Sujet signature — synthèse de tout               |

**Top 3 à attaquer en premier** : hébergement (CA affilié) → plugin SEO (autorité) → formation en ligne (positionnement premium).

---

### Cocon interne Top 3 — structure exacte

**Cocon Hébergement** — Pillar : `/meilleur-hebergement-wordpress/` (BOFU)
Clusters : comparatif premium, pas cher, rapide, WooCommerce, freelance, VPS vs mutualisé, migration, checklist.
Supports P2 : TTFB, optimiser serveur, CDN, sauvegardes, sécurité hébergeur.
Maillage : pillar → tous clusters → pillar + 2 voisins + 1 support preuve.

**Cocon Plugin SEO** — Pillar : `/meilleur-plugin-seo-wordpress/` (BOFU)
Clusters : Rank Math vs Yoast, Rank Math avis, Rank Math Pro, configurer Rank Math, Yoast avis, SEOPress avis, schemas, erreurs SEO, SEO WP 2026.
Supports P2 : sitemap, indexation GSC, maillage interne, titles/metas, redirections 301, Open Graph.

**Cocon Formation** — Pillar : `/creer-formation-en-ligne-wordpress/` (MOFU→BOFU)
Clusters : meilleur LMS, Tutor LMS avis, LearnDash avis, comparatif LMS, vendre formation stack, Stripe WP, espace membre, FluentCRM, tunnel evergreen.
Supports P2 : plan de cours, filmer vidéos, héberger vidéos, page de vente formation, FAQ légale.

**Pages ponts** : `/optimiser-vitesse-wordpress/` (hébergement ↔ SEO) + `/automatisation-wordpress/` (formation ↔ CRM ↔ funnel) + `/funnel-wordpress/` (SEO ↔ formation ↔ consulting).

---

### Plan contenu 4 semaines

**S1** — Hébergement : PILLAR "Meilleur hébergement WP 2026" (BOFU, checklist) + cluster "Hébergement WP rapide + CWV".

**S2** — Plugin SEO : PILLAR "Meilleur plugin SEO WP : Rank Math vs Yoast vs SEOPress 2026" + cluster "Rank Math avis complet".

**S3** — Formation : PILLAR "Créer formation en ligne avec WP : LMS, paiement, tunnel" + cluster "Tutor LMS avis".

**S4** — Ponts : "Optimiser vitesse WordPress" (hébergement ↔ SEO) + "Tunnel de vente WordPress" (SEO ↔ formation ↔ consulting).

Résultat : 3 Pillars + 5 clusters BOFU + 2 ponts = 8 pages à fort potentiel. Impact SEO sous 3–6 mois.

---

### H1/H2 optimisés — 3 Pillars

**Hébergement** — H1 : "Meilleur hébergement WordPress en 2026 : comparatif, tests de performance et avis détaillés"
H2 clés : Pourquoi stratégique / Protocole test / Comparatif top 5 / Rapide / WooCommerce / VPS vs mutualisé / Migration / Erreurs / FAQ.
Champs lexicaux : serveur, PHP, HTTP/3, Core Web Vitals, CDN, SSL.

**Plugin SEO** — H1 : "Meilleur plugin SEO WordPress : comparatif complet Rank Math vs Yoast vs SEOPress (2026)"
H2 clés : Pourquoi indispensable / Critères / Comparatif / Rank Math avis / Yoast / SEOPress FR / CWV / Configurer / Erreurs / Profil / FAQ.
Champs lexicaux : sitemap XML, balises title, meta description, schema.org, redirections 301, Search Console.

**Formation en ligne** — H1 : "Créer une formation en ligne avec WordPress : guide complet (LMS, paiement, tunnel de vente)"
H2 clés : Pourquoi WP idéal / Meilleur LMS / Tutor vs LearnDash / Espace membre / Stripe / Automatiser emails / Tunnel evergreen / Héberger vidéos / Erreurs / CA potentiel / FAQ.
Champs lexicaux : checkout, upsell, membership, marketing automation, page de vente, tunnel evergreen.

---

## Ancres exactes stratégiques — Maillage chirurgical

**Règle d'or :** ne jamais répéter exactement la même ancre 50 fois. Créer : 1 ancre principale (exact match) + 3–5 variantes naturelles + 2 ancres larges + 1 ancre brandée.

### Cocon 1 — Hébergement WordPress

**Ancre principale** (30–40% des liens internes) : `meilleur hébergement WordPress`

**Variantes secondaires :** hébergement WordPress rapide / hébergement WordPress performant / comparatif hébergement WordPress / hébergeur WordPress fiable / quel hébergement choisir pour WordPress

**Ancres larges :** choisir son hébergeur / solution d'hébergement adaptée / performance serveur

**Ancre brandée :** notre comparatif sur schoolsWP / test complet sur schoolsWP

**Répartition recommandée (sur 20 liens internes) :** 6 → ancre principale / 6 → variantes / 5 → ancres larges / 3 → brandées

### Cocon 2 — Plugin SEO WordPress

**Ancre principale :** `meilleur plugin SEO WordPress`

**Variantes :** plugin SEO WordPress / comparatif plugin SEO / outil SEO pour WordPress / extension SEO WordPress / solution SEO WordPress

**Spécifiques Rank Math :** Rank Math avis / configurer Rank Math / Rank Math vs Yoast

**Ancres larges :** optimiser le SEO WordPress / améliorer son référencement

**Structure idéale (20 liens) :** 5 → meilleur plugin SEO WordPress / 5 → Rank Math avis / configurer Rank Math / 6 → variantes / 4 → ancres larges

### Cocon 3 — Formation en ligne WordPress

**Ancre principale :** `créer une formation en ligne avec WordPress`

**Variantes :** vendre une formation WordPress / lancer un cours en ligne WordPress / plugin LMS WordPress / plateforme de formation WordPress / créer un espace membre WordPress

**Spécifiques :** Tutor LMS avis / Tutor LMS vs LearnDash / tunnel evergreen formation

**Ancres larges :** monétiser son expertise / automatiser la vente

**Répartition type (20 liens) :** 5 → ancre principale / 5 → Tutor LMS / comparatifs / 6 → variantes / 4 → ancres larges

### Ancres ponts (ultra stratégiques)

Ces ancres relient les 3 cocons entre eux. À utiliser 2–4 fois par article :

- optimiser la vitesse WordPress
- automatiser son site WordPress
- tunnel de vente WordPress
- monétiser son site WordPress
- stratégie WordPress orientée business

**Erreurs à éviter :** toujours la même ancre exacte / liens uniquement descendants / pas de liens horizontaux entre clusters / trop d'ancres commerciales directes

### Ratio global idéal sur l'ensemble du site

| Type        | Ratio |
| ----------- | ----- |
| Exact match | 35%   |
| Variantes   | 40%   |
| Larges      | 20%   |
| Brandées    | 5%    |

**Impact attendu :** renforcement topic authority / meilleure compréhension Google / augmentation progressive des positions / hausse CTR pages BOFU.

---

## Cartographie visuelle du maillage interne

### Vue Macro — Architecture globale

```
                         [Homepage]
                              |
         ------------------------------------------------
         |                     |                      |
   [Pillar Hébergement]  [Pillar Plugin SEO]  [Pillar Formation]
         |                     |                      |
   Clusters & Supports   Clusters & Supports   Clusters & Supports
         \___________________|_____________________/
                         |
                 [Pages Ponts Stratégiques]
```

### Cocon 1 — Hébergement (schéma détaillé)

```
                 [PILLAR]
     Meilleur hébergement WordPress
                  |
     -----------------------------------
     |        |        |        |     |
   Rapide   Pas cher  Woo     VPS   Migration
     |        |        |        |     |
   TTFB    CDN     Sécurité  Sauvegarde  Optimiser serveur
```

**Flux d'autorité :** tous les clusters → renvoient vers Pillar / tous les supports → renvoient vers cluster + Pillar / clusters → se lient horizontalement

**Exemple :**

```
Hébergement rapide
   ↔ TTFB
   ↔ CDN
   ↔ Optimiser vitesse
   ↔ Pillar
```

### Cocon 2 — Plugin SEO (schéma)

```
              [PILLAR]
    Meilleur plugin SEO WordPress
                 |
    -------------------------------------
    |        |         |        |      |
 RankMath  Yoast   SEOPress  Config   Erreurs SEO
    |        |         |        |      |
 Sitemap   Schema   Titles   Maillage  Redirections
```

**Flux stratégique :** les pages "avis" poussent le Pillar / les pages "how-to" poussent les avis / la page "SEO WordPress 2026" pousse tout le cocon

**Exemple circulation :**

```
Rank Math avis
   ↔ Configurer Rank Math
   ↔ Schema WordPress
   ↔ Pillar
```

### Cocon 3 — Formation en ligne

```
                  [PILLAR]
   Créer formation en ligne WordPress
                     |
   ------------------------------------------------
   |        |        |         |        |        |
  LMS    Tutor   LearnDash  Stripe  Tunnel  Automatisation
   |        |        |         |        |        |
Plan cours  Vidéo  Page vente  Email  Evergreen  Hébergement
```

**Logique :** Pillar = vision globale / "Meilleur LMS" = décision / "Tunnel evergreen" = monétisation / Supports = crédibilité opérationnelle

### Pages ponts (zone stratégique centrale)

```
         [Optimiser vitesse WordPress]
            ↔ Hébergement
            ↔ Plugin SEO

         [Tunnel WordPress]
            ↔ Plugin SEO
            ↔ Formation

         [Automatisation WordPress]
            ↔ Formation
            ↔ CRM
            ↔ Consulting
```

Ces pages doivent : recevoir beaucoup de liens / redistribuer vers les 3 Pillars / être mises à jour régulièrement.

### Règles quantitatives optimales

**Pour chaque Pillar :** 8–12 clusters directs / 5–8 supports techniques / 2–3 liens entrants depuis pages ponts / 3–5 liens horizontaux entre clusters

**Pour l'ensemble du site :** chaque page = minimum 3 liens sortants internes / chaque page = minimum 2 liens entrants internes / aucun contenu isolé

---

## Simulation puissance SEO par page — Scoring & priorisation

**Méthode de scoring (sur 100) :**

| Critère                        | Pondération |
| ------------------------------ | ----------- |
| Intent transactionnelle        | 30          |
| Volume potentiel               | 25          |
| Difficulté SEO estimée         | 15          |
| Potentiel affiliation          | 15          |
| Potentiel consulting/formation | 15          |

### Niveau S — Priorité absolue (Score 85–95)

| Page                               | Score | Pourquoi                           |
| ---------------------------------- | ----- | ---------------------------------- |
| Meilleur hébergement WordPress     | 93    | Intent BOFU + commissions élevées  |
| Meilleur plugin SEO WordPress      | 90    | Transaction + forte demande        |
| Créer formation en ligne WordPress | 88    | Business + affiliation + formation |
| Rank Math avis                     | 87    | Longue traîne BOFU                 |
| Meilleur plugin LMS WordPress      | 86    | Achat direct                       |

**À produire en premier.**

### Niveau A — Levier majeur (Score 75–84)

| Page                                   | Score |
| -------------------------------------- | ----- |
| Hébergement WordPress rapide           | 82    |
| Tutor LMS avis                         | 81    |
| Rank Math vs Yoast                     | 80    |
| Tunnel de vente WordPress              | 79    |
| Vendre formation WordPress             | 78    |
| Maintenance WordPress                  | 77    |
| WP Rocket avis (futur cluster vitesse) | 76    |

### Niveau B — Structuration & autorité (Score 65–74)

| Page                     | Score |
| ------------------------ | ----- |
| Schema WordPress         | 72    |
| Configurer Rank Math     | 70    |
| Automatisation WordPress | 70    |
| Stripe WordPress         | 69    |
| Espace membre WordPress  | 68    |
| CDN WordPress            | 67    |

### Niveau C — Support & profondeur (Score 50–64)

| Page                 | Score |
| -------------------- | ----- |
| Sauvegarde WordPress | 60    |
| Redirections 301     | 58    |
| Titles & metas       | 57    |
| Filmer une formation | 55    |
| Plan de cours        | 53    |

### Ordre optimal de production (budget/temps limité)

1. Meilleur hébergement WordPress
2. Meilleur plugin SEO WordPress
3. Rank Math avis
4. Créer formation en ligne WordPress
5. Meilleur plugin LMS WordPress
6. Hébergement WordPress rapide
7. Tutor LMS avis
8. Tunnel WordPress

Ensuite seulement : profondeur technique.

### Projection d'impact cumulée (si Top 5 bien exécutées)

- 60–70% du futur CA affilié
- 50% du trafic BOFU
- 40% des leads consulting
- 80% de la perception d'expertise

**Insight stratégique :** les pages techniques seules ne créent pas l'autorité business. Les pages transactionnelles + comparatives le font. Produire en priorité ce qui vend → ce qui structure → ce qui approfondit.

---

## Roadmap de production priorisée — Media business

Raisonnement media business, pas blog. Chaque page scorée sur : potentiel monétisation (affiliation/consulting/formation) + intent transactionnelle + volume estimé + rôle structurel (hub ou support) + rapidité de ranking.

### Phase 1 — Structure monétisable immédiate (Mois 1–2)

**Objectif :** créer les hubs + premières pages BOFU.

**Priorité absolue (Semaine 1–2)**

1. Meilleur hébergement WordPress (Pillar)
2. Hébergement WordPress rapide (Cluster BOFU)
3. Meilleur plugin SEO WordPress (Pillar)
4. Rank Math avis (Cluster BOFU)
5. Créer une formation en ligne WordPress (Pillar)

Pourquoi : intent transactionnelle directe + affiliation immédiate + structure centrale du cocon.

**Priorité élevée (Semaine 3–4)**

6. Tutor LMS avis
7. Rank Math vs Yoast
8. Migration WordPress vers nouvel hébergeur
9. Meilleur plugin LMS WordPress
10. Optimiser la vitesse WordPress (page pont)

À ce stade : 3 cocons + 1 page pont stratégique.

### Phase 2 — Accélération authority (Mois 3–4)

**Objectif :** renforcer la profondeur + capter longue traîne.

11. Configurer Rank Math (how-to)
12. Hébergement WordPress WooCommerce
13. Stripe sur WordPress (paiement formation)
14. Tunnel evergreen formation WordPress
15. Erreurs SEO WordPress fréquentes
16. Maillage interne WordPress

Ces pages nourrissent les Pillars existants et renforcent la topical authority.

### Phase 3 — Profondeur & consolidation (Mois 5–6)

**Objectif :** passer de structure solide → autorité dominante.

17. SEO WordPress 2026 (guide TOFU massif)
18. Sauvegarde WordPress meilleures pratiques
19. CDN WordPress guide complet
20. Automatisation email WordPress (FluentCRM)
21. Page de vente formation WordPress
22. VPS vs mutualisé vs cloud

À ce stade : écosystème complet.

### Phase 4 — Domination thématique (Mois 7–12)

**Objectif :** créer la profondeur qui écrase la concurrence.

23. Core Web Vitals WordPress
24. Schema WordPress guide
25. Redirections 301 WordPress
26. Sécurité hébergement WordPress
27. Plan de cours formation en ligne
28. Filmer vidéos formation
29. Monétiser son site WordPress
30. Funnel WordPress complet

### Résumé priorisation

| Phase   | Pages | Objectif                 |
| ------- | ----- | ------------------------ |
| Phase 1 | 10    | Structure + monétisation |
| Phase 2 | 6     | Renforcement authority   |
| Phase 3 | 6     | Profondeur sémantique    |
| Phase 4 | 8+    | Domination thématique    |

**Pourquoi cette roadmap fonctionne :** on sécurise le business dès le début / on nourrit les Pillars rapidement / on évite les pages isolées / on construit par couches successives / on maximise l'effet levier SEO.

**Projection stratégique :**

- Dès Phase 1 : premiers clics affiliés, premiers leads consulting, premiers signaux SEO.
- Dès Phase 2 : rankings longue traîne, autorité thématique visible, croissance trafic exponentielle.

---

## Architecture scalable 50+ pages

Objectif : monter à 50–120 pages en gardant la cohérence sémantique, maximisant le PageRank interne, alimentant affiliation + consulting, extensible sans casser la structure.

### Vue macro — Structure cible

```
                     Homepage
                         |
      -------------------------------------------------
      |                    |                        |
  Pilier 1             Pilier 2                 Pilier 3
 Hébergement          Plugin SEO              Formation/LMS
      |                    |                        |
  Clusters (10+)      Clusters (12+)           Clusters (12+)
      |                    |                        |
  Supports (10+)      Supports (15+)           Supports (15+)
                         |
                    Pages Ponts (10+)
                         |
                 Pages Business & Conversion
```

### Volume cible (56–73 pages cohérentes)

| Type de page            | Nombre cible |
| ----------------------- | ------------ |
| Pillars                 | 3            |
| Clusters BOFU           | 20–25        |
| Supports techniques     | 20–25        |
| Pages ponts             | 8–12         |
| Pages business (offres) | 5–8          |

### Cocon 1 — Hébergement (≈ 18 pages)

**1 Pillar :** Meilleur hébergement WordPress

**8 Clusters :** Hébergement rapide / WooCommerce / freelance / agence / VPS vs Cloud / pas cher / Migration WordPress / Comparatif détaillé

**9 Supports :** TTFB / CDN / Sauvegardes / Sécurité serveur / Optimiser PHP / HTTP/3 / Uptime monitoring / Cache serveur / Erreurs fréquentes hébergement

### Cocon 2 — Plugin SEO (≈ 22 pages)

**1 Pillar :** Meilleur plugin SEO WordPress

**10 Clusters :** Rank Math avis / Rank Math Pro avis / Rank Math vs Yoast / Yoast avis / SEOPress avis / Configurer Rank Math / Schema WordPress / SEO WooCommerce / SEO local WordPress / SEO WordPress 2026

**11 Supports :** Sitemap / Robots.txt / Redirections / Open Graph / Titles & metas / Indexation Google / Core Web Vitals SEO / Maillage interne / Breadcrumbs / Pagination SEO / Cannibalisation mots-clés

### Cocon 3 — Formation / LMS (≈ 22 pages)

**1 Pillar :** Créer une formation en ligne WordPress

**11 Clusters :** Meilleur plugin LMS / Tutor LMS avis / Tutor vs LearnDash / LearnDash avis / Stripe WordPress / Tunnel evergreen / Page de vente formation / Espace membre / Automatisation email / Membership WordPress / Vendre formation WordPress

**10 Supports :** Plan de cours / Filmer ses vidéos / Hébergement vidéo / TVA formation France / CGV formation / Upsell formation / Webinaire automatique / Séquence email lancement / Preuve sociale / Pricing formation

### Pages ponts stratégiques (≈ 10 pages)

Ces pages distribuent l'autorité entre cocons : Optimiser vitesse WordPress / Tunnel WordPress / Automatisation WordPress / Monétiser son site WordPress / CRM WordPress / WordPress pour freelance / Maintenance WordPress / Stack WordPress business / Outils indispensables WordPress / Checklist lancement site

### Règles de maillage scalable

**Règle 1 — Chaque page doit :** lier vers son Pillar + lier vers 2 clusters du même cocon + lier vers 1 page pont + recevoir minimum 2 liens internes entrants

**Règle 2 — Pages Pont :** lient vers les 3 Pillars + lient vers 3 clusters différents + servent de carrefour stratégique

**Règle 3 — Pages business :** reçoivent des liens depuis clusters BOFU + pages pont + newsletter — n'envoient pas trop de PageRank vers l'extérieur

### Ratio interne optimal (site complet)

| Type de lien                   | Ratio |
| ------------------------------ | ----- |
| Liens intra-cocon              | 35%   |
| Liens vers Pillars             | 25%   |
| Liens vers pages pont          | 20%   |
| Liens vers pages business      | 10%   |
| Liens horizontaux stratégiques | 10%   |

### Roadmap scalable production

- **Phase 1 (0–3 mois)** → 3 Pillars + 6 clusters BOFU + 3 pages pont
- **Phase 2 (3–6 mois)** → +15 clusters + 10 supports
- **Phase 3 (6–12 mois)** → compléter à 50+ pages + optimisation maillage + mise à jour stratégique des Pillars

**Résultat SEO attendu à 50+ pages :** autorité thématique claire / forte augmentation trafic longue traîne / meilleure résistance aux updates Google / meilleur taux de conversion par spécialisation.

**Vision finale :** schoolsWP devient un écosystème organisé — pas une accumulation d'articles, un réseau logique.

---

## Plan monétisation détaillé — 4 piliers

Objectif : transformer l'autorité schoolsWP en machine de revenus stable, scalable et prévisible. 4 piliers complémentaires — jamais dépendant d'une seule source.

### Pilier 1 — Affiliation stratégique (cash-flow immédiat)

**Positionnement :** pas "liste de plugins" — mais "voici ce que j'utilise pour générer du business". Orientation ROI.

**Catégories prioritaires :** hébergement WordPress premium / SEO (Rank Math, etc.) / LMS / CRM & Email / Performance / Outils automation

**Architecture par outil :** 1 article comparatif + 1 article dédié + 1 vidéo tuto + 1 section dans pillar page + 1 mention newsletter + 1 CTA contextuel

**Objectif 12 mois :** 5 000–10 000 €/mois en affiliation récurrente.

### Pilier 2 — Formation signature

**Produit phare :** "WordPress Business System" — Créer / Optimiser / Monétiser

**Format :** 6–8 modules + vidéos + templates + SOP + accès communauté privée

**Pricing :** Phase 1 : 297–497 € / Phase 2 : 697–997 €

**Projection :** 50 ventes/an à 697 € ≈ 35 000 €

### Pilier 3 — Consulting premium

**Cible :** entrepreneurs en activité, formateurs, freelances avancés

**Offres :** Audit WordPress SEO → 1 500–2 500 € / Accompagnement 3 mois → 4 000–8 000 €

**Objectif :** 2–4 clients/mois max. Pas volume — positionnement premium.

### Pilier 4 — Produits digitaux scalables

**Exemples :** templates funnels WP / pack SOP SEO / templates Notion-Google Sheet / templates emails / mini formations spécialisées

**Pricing :** 29 € / 49 € / 97 € — volume + upsell vers formation.

### Structure de revenus cible — 24 mois

| Source            | Objectif mensuel |
| ----------------- | ---------------- |
| Affiliation       | 7 000 €          |
| Formation         | 4 000 €          |
| Consulting        | 8 000 €          |
| Produits digitaux | 2 000 €          |

≈ 21 000 €/mois possible — > 250 000 € annuel potentiel.

### Funnel intégré

**TOFU :** Articles SEO / YouTube / LinkedIn → **MOFU :** Lead magnets / Webinars / Études de cas → **BOFU :** Formation / Consulting / Bundles premium

**Effet multiplicateur :** l'affiliation nourrit le cash-flow / la formation nourrit la crédibilité / le consulting nourrit le positionnement premium / les templates nourrissent le volume / l'email nourrit tout.

**Clé stratégique :** ne jamais vendre frontalement — toujours Éduquer → Démontrer → Apporter du ROI → Proposer.

---

## Funnel exact — Formation signature

Formation cible : **WordPress Business System** (Créer – Optimiser – Monétiser).
Système hybride evergreen + pics de lancement.

### Architecture globale

```
SEO / Social / YouTube
        ↓
Lead Magnet ciblé
        ↓
Séquence Nurturing (5–7 emails)
        ↓
Masterclass / Workshop
        ↓
Offre formation (ou appel stratégique)
        ↓
Upsell / Bundle / Consulting
```

### Étape 1 — Lead magnet ultra ciblé

1 lead magnet = 1 douleur précise = 1 promesse claire. Exemples alignés schoolsWP :

- "Checklist SEO WordPress 2026"
- "Blueprint Funnel WordPress rentable"
- "Stack WordPress Business validée"
- "Plan 30 jours pour lancer son site"

### Étape 2 — Séquence email 7 jours

| Jour | Objectif                | Message                                                                     |
| ---- | ----------------------- | --------------------------------------------------------------------------- |
| J1   | Crédibilité             | Livraison + positionnement — comment j'ai structuré mon système WP business |
| J2   | Agiter le problème      | Erreurs classiques                                                          |
| J3   | Preuve                  | Étude de cas                                                                |
| J4   | Changement de paradigme | WP n'est pas technique — c'est stratégique                                  |
| J5   | Méthode                 | Framework "WP Business Engine™"                                             |
| J6   | Invitation              | Masterclass                                                                 |
| J7   | Rappel                  | Urgence douce                                                               |

### Étape 3 — Masterclass (45–60 min)

Structure : situation actuelle du marché WP → pourquoi la majorité stagnent → 3 erreurs critiques → présentation du système complet → étude de cas → offre formation → bonus limités.

### Étape 4 — Page de vente

Structure : promesse forte orientée résultat / vision transformation / problème amplifié / solution structurée / modules détaillés / bonus / garanties / FAQ objections / CTA clair.

### Étape 5 — Version evergreen hybride

Après phase lancement : masterclass en replay automatisé + deadline dynamique + séquence post-webinaire J+2 / J+4 / J+6.

### Étape 6 — Upsell stratégique

Après achat : Pack templates premium (+97 €) / Session stratégique 1:1 (+297 €) / Accès communauté premium annuel.

### Métriques cibles

| Étape                     | Taux cible |
| ------------------------- | ---------- |
| Landing → opt-in          | 30–45%     |
| Emails → clic masterclass | 20%        |
| Masterclass → achat       | 3–8%       |

Avec 3 000 leads : 90–240 ventes possibles.

### Intégration SEO → Funnel

Chaque cluster SEO renvoie vers lead magnet spécifique + masterclass adaptée.

Exemple : Cluster "SEO WordPress" → Lead magnet SEO → Masterclass SEO Business → Formation complète.

### Version premium high-ticket

Alternative : après masterclass → Application → Appel stratégique → Programme avancé 2 000–5 000 €.

**Vision stratégique :** ne pas vendre une formation. Vendre un système, une méthode, une vision, un levier business.

---

## Plan anti-dépendance affiliation

**Principe :** aucune source ne doit représenter +40% du CA. L'affiliation = levier, pas fondation.

Pourquoi : les programmes changent / les commissions baissent / les plateformes ferment / les concurrents copient. Ce que tu contrôles toujours : ton audience, tes offres, ton pricing, ton positionnement.

### Architecture de revenus équilibrée — Cible 24 mois

| Source              | % cible |
| ------------------- | ------- |
| Consulting          | 35%     |
| Formation signature | 30%     |
| Produits digitaux   | 20%     |
| Affiliation         | 15%     |

L'affiliation devient complément, pas pilier central.

### Étape 1 — Transformer le trafic affilié en audience propriétaire

**Erreur classique :** Article → lien affilié → fin.

**Stratégie schoolsWP :** Article affilié → Lead magnet spécifique → Email nurturing → Offre propre.

Exemple : article "Meilleur plugin SEO WordPress" → au lieu de "Clique ici" → "Télécharge la checklist SEO schoolsWP" → méthode complète → formation ou consulting. Tu récupères l'audience.

### Étape 2 — Chaque outil affilié devient un pont vers ton offre

Rank Math → tu proposes Audit SEO + Mini formation SEO + Masterclass Funnel SEO. L'outil devient déclencheur, pas finalité.

### Étape 3 — Micro-produits indépendants par cluster

- Cluster LMS → mini formation "Créer sa formation WordPress"
- Cluster Funnel → template tunnel complet WordPress
- Cluster Performance → pack optimisation technique

Prix : 29–97 €. Volume stable.

### Étape 4 — Actif premium impossible à copier

Les affiliés peuvent copier des comparatifs. Ils ne peuvent pas copier : ton système / ton branding / ta méthode / ta communauté.

Actif défensif : Formation signature schoolsWP = positionnement stratégique + communauté + méthode propriétaire (Authority Loop™).

### Étape 5 — Consulting pour sécuriser le cash-flow

Même avec trafic fluctuant : 2 clients premium = stabilité. L'affiliation varie, le consulting stabilise.

### Étape 6 — Machine email dominante

Chaque article affilié doit : générer un opt-in → séquence → offre propriétaire → upsell. L'email absorbe la volatilité SEO.

### Étape 7 — Écosystème partenaire propre

Négocier deals exclusifs + codes promo personnalisés + bonus spécifiques schoolsWP + bundles formation + outil. Tu deviens co-acteur, plus dépendant.

### Règle stratégique long terme

Si demain Google chute, une commission disparaît, un plugin ferme — schoolsWP continue grâce à : Email / Formation / Consulting / Templates.

**Modèle final robuste :** Trafic → Lead → Email → Offre propre → Upsell → Communauté → Consulting.

L'affiliation devient preuve, recommandation, bonus — plus jamais fondation.

**Vision finale :** schoolsWP ne vend pas des outils. schoolsWP vend une méthode, une transformation, une stratégie WordPress business. Les outils sont des briques. Tu vends l'architecture.

---

## Système d'upsell automatisé

Objectif : augmenter la LTV sans augmenter le trafic. 5 briques : segmentation intelligente / séquences comportementales / micro-offres intermédiaires / upsell progressif / relance conditionnelle.

### Flow logique global

```
Acquisition → Nurturing → Micro-offre → Formation → Consulting → Client premium
```

### LTV réaliste par contact premium

Abonné gratuit → Template 47 € → Formation 697 € → Consulting 3 000 € = **LTV 3 744 €**

### Tags FluentCRM — 4 familles

**A — Niveau :** `lvl_debutant` / `lvl_freelance` / `lvl_agence` / `lvl_formateur`

**B — Intent :** `intent_seo` / `intent_lms` / `intent_funnel` / `intent_performance` / `intent_monetisation`

**C — Comportement :** `lead_magnet_downloaded` / `opened_3_emails` / `clicked_affiliation` / `visited_sales_page` / `attended_masterclass` / `warm_lead` / `hot_lead` / `inactive_60d`

**D — Achat :** `buyer_template` / `buyer_formation` / `buyer_consulting`

### Lead scoring

| Action            | Points |
| ----------------- | ------ |
| Email ouvert      | +5     |
| Clic              | +10    |
| Visite page vente | +20    |
| Masterclass vue   | +30    |

Score > 50 → proposition formation / Score > 80 → invitation appel stratégique

### Scénarios comportementaux

- Clique affiliation 3x → email "Comparatif avancé + erreur à éviter" + offre bundle
- Visite page consulting sans achat → email 48h : "Est-ce que ceci vous bloque ?" + étude de cas
- Inactif 60 jours → séquence réactivation : best of + nouveau guide + offre spéciale

---

## Flow FluentCRM — Implémentation menu par menu

### 0. Tags à créer en premier

Menu → Contacts → Tags — créer toutes les familles A/B/C/D listées ci-dessus.

### Automation 1 — Lead Magnet SEO

Menu → Automations → New Automation

**Trigger :** Submits Form → Checklist SEO

**Actions :** Add Tag `lead_magnet_downloaded` + `intent_seo` + `lvl_debutant` → Start Sequence "Nurturing SEO"

### Sequence — Nurturing SEO (5 emails)

Menu → Email Sequences → New Sequence "Nurturing SEO"

| Email | Délai    | Sujet                          |
| ----- | -------- | ------------------------------ |
| E1    | Immédiat | Livraison + positionnement     |
| E2    | +2j      | Erreur SEO classique           |
| E3    | +3j      | Méthode schoolsWP              |
| E4    | +3j      | Outil recommandé + cas concret |
| E5    | +4j      | Transition vers template       |

Dernière action : Add Tag `warm_lead`

### Automation 2 — Micro-offre Template 47€

**Trigger :** Tag Added `warm_lead`

**Actions :** Wait 1 day → Send Email offre template

**Condition :** IF Purchase Template → Add Tag `buyer_template` + Remove `warm_lead` + Start Automation "Upsell Formation" / NON → Wait 5j + Reminder

### Automation 3 — Upsell Formation

**Trigger :** Tag Added `buyer_template`

**Séquence :** Wait 3j → Email "pourquoi les templates ne suffisent pas" → Wait 3j → étude de cas → Wait 2j → offre formation 697€

**Condition comportementale :** IF Click Page Formation → Add Tag `hot_lead`

**Achat formation (trigger séparé) :** Purchase Formation → Add Tag `buyer_formation` + Stop All Active Sales Sequences + Start Automation "Onboarding Formation"

### Automation 4 — Consulting Premium

**Trigger :** Tag Added `buyer_formation`

**Actions :** Wait 30 jours → Email proposition audit stratégique → Wait 5j → Reminder

**Si clic Calendly :** Add Tag `hot_prospect_consulting`

**Achat consulting :** Add Tag `buyer_consulting` + Remove All Sales Tags + Stop All Sales Automations

### Automation Réactivation

**Trigger :** Contact Inactive 60 Days

**Actions :** Add Tag `inactive_60d` → Email "Toujours intéressé ?" → Wait 3j → Best of schoolsWP → Remove Tag `inactive_60d`

### Règle d'or FluentCRM

Ne jamais proposer consulting à `lvl_debutant` ou Score < 50. Toujours filtrer.

**1 trigger = 1 logique claire. Nettoyer les tags après achat. Stopper les séquences inutiles.**

### Impact attendu (1 000 leads/mois)

- 5–10% → achètent Template
- 10–20% des acheteurs template → Formation
- 5–10% des acheteurs formation → Consulting

Effet multiplicateur LTV ×3 sans trafic supplémentaire.

---

## Système high-ticket pur

**Offre centrale :** WordPress Business Authority Program — accompagnement stratégique 8–12 semaines.
**Prix cible :** 3 000–8 000 €. Pas une formation, une transformation business.
**Objectif :** 3 clients/mois à 5 000 € = 15 000 €/mois. Pas besoin de 10 000 leads.

### Funnel high-ticket (pas de tunnel classique)

```
Contenu expert → Lead magnet premium → Masterclass stratégique
→ Qualification → Appel stratégique → Programme premium
```

### 1. Acquisition qualifiée

Pas d'ebook "débutant". Lead magnets premium ciblés :

- Audit SEO WordPress avancé (PDF stratégique)
- Scorecard business WordPress
- Mini training "Pourquoi 90% des sites WP ne monétisent pas"

Objectif : attirer profils déjà engagés.

### 2. Masterclass stratégique

Sujet type : "Construire un système WordPress qui génère des clients automatiquement"

Durée : 60–90 min. Démontre expertise + framework propriétaire. Pas de vente agressive — invitation à candidater.

### 3. Formulaire de qualification obligatoire

Champs : CA actuel / Objectif 12 mois / Budget prévu / Niveau technique / Blocage principal.

### 4. Tags FluentCRM high-ticket

`ht_registered_masterclass` / `ht_attended_live` / `ht_watched_replay` / `ht_applied` / `ht_qualified` / `ht_unqualified` / `ht_client`

### Flow high-ticket détaillé

| Trigger                | Condition | Actions                                                 |
| ---------------------- | --------- | ------------------------------------------------------- |
| Registered Masterclass | —         | Add Tag `ht_registered_masterclass` + Reminder Sequence |
| Attended > 60%         | —         | Add Tag `ht_attended_live` + Send Application Email     |
| Applied                | —         | Add Tag `ht_applied` + Manual Review                    |
| Profil cohérent        | OUI       | Add Tag `ht_qualified` + Send Calendly                  |
| Profil non cohérent    | NON       | Add Tag `ht_unqualified` + Redirect Formation Signature |

### Structure de l'offre

6 modules : Diagnostic stratégique / Architecture WordPress Business / SEO & Autorité / Funnel & Conversion / Automatisation & CRM / Scaling & Positionnement + support direct + feedback personnalisé + templates premium.

### Système d'exclusion stratégique

Refuser : débutants complets / budget < 1 500 € / projets flous. Cela augmente la désirabilité.

### LTV high-ticket

Client 5 000 € → upsell consulting annuel → 10 000–20 000 € possible/client. Peu de clients, relation forte, autorité massive.

### Positionnement psychologique

Ce n'est pas "apprendre WordPress". C'est "structurer un système business rentable avec WordPress". Transformation > Information.

**Leviers de conversion :** études de cas réelles / ROI chiffré / framework propriétaire / limitation volontaire des places / process de sélection.

**Résultat attendu :** schoolsWP devient référence business WordPress premium — pas "blog comparatif".

---

## FluentCRM version minimaliste — À lancer en moins de 2h

**Principe :** 1 lead magnet / 1 séquence / 1 micro-offre / 1 formation / 1 option consulting. C'est tout.

### 6 tags indispensables (et rien de plus)

`lead` / `warm` / `buyer_template` / `buyer_formation` / `consulting_interest` / `inactive`

### Flow simplifié

**Étape 1 — Entrée :**
Trigger : Form Submitted → Add Tag `lead` → Start Sequence "Nurturing"

**Étape 2 — Séquence Nurturing 7 emails :**

| Email | Sujet                    |
| ----- | ------------------------ |
| E1    | Erreur SEO fréquente     |
| E2    | Méthode schoolsWP        |
| E3    | Outil recommandé         |
| E4    | Cas concret              |
| E5    | Erreurs avancées         |
| E6    | Transition               |
| E7    | Micro-offre Template 47€ |

Condition : IF opened 3 emails → Add Tag `warm`

**Étape 3 — Achat template :**
→ Add Tag `buyer_template` + Stop nurturing + Start Sequence "Formation"

**Étape 4 — Séquence Formation 4 emails :**
E1 Pourquoi un système complet / E2 Étude de cas / E3 Objections / E4 Offre formation 697€

Achat formation : Add Tag `buyer_formation` + Stop séquence + Delay 30 jours + Send Consulting Offer

**Étape 5 — Consulting ultra simple :**
Email unique "Tu veux aller plus vite ?" + lien Calendly → IF clic : Add Tag `consulting_interest`

**Étape 6 — Réactivation minimale :**
No open 60 days → Add Tag `inactive` → 2 emails best-of

### Projection réaliste (500 leads/mois)

| Étape          | Taux                    | Résultat          |
| -------------- | ----------------------- | ----------------- |
| Template 47€   | 3%                      | 15 × 47€ = 705€   |
| Formation 697€ | 20% des buyers template | 3 × 697€ = 2 091€ |
| Consulting     | 1/mois                  | 3 000€            |
| **Total**      |                         | **≈ 5 800€/mois** |

Avec un système ultra simple.

**Règle stratégique :** démarre simple → mesure → optimise. Ne complexifie que quand le revenu est stable.

---

## Séquences emails complètes — FluentCRM ready

**Ton :** direct, pédagogique, orienté ROI.
**Positionnement :** schoolsWP = WordPress + business.
**Objectif global :** construire la confiance → micro-engagement → montée en gamme naturelle, sans pression agressive.

---

### SÉQUENCE 1 — Nurturing SEO (après Lead Magnet)

**Contexte :** téléchargement checklist SEO
**Objectif :** crédibilité + préparer micro-offre

---

**Email 1 — Bienvenue + erreur fatale**

Objet : L'erreur SEO que 80% des sites WP font

Salut,

Merci pour le téléchargement.

Avant d'optimiser quoi que ce soit, il faut comprendre une chose :

Le problème n'est presque jamais technique.

C'est stratégique.

La plupart :

- installent un plugin
- cochent 3 cases
- espèrent du trafic

Le SEO WordPress fonctionne si :

- La structure est pensée
- Le maillage est logique
- L'intention est claire

Demain, je te montre comment structurer ça correctement.

À très vite,
Michaël

---

**Email 2 — La méthode schoolsWP**

Objet : La structure qui change tout

Si ton site est une collection d'articles isolés, Google ne comprend rien.

Ce qu'il faut :

- Une page pilier
- Des clusters
- Un maillage interne cohérent

C'est ce qu'on appelle un cocon sémantique.

Sans ça, tu perds de l'autorité.

Dans le prochain email : l'outil que j'utilise pour accélérer.

---

**Email 3 — Outil recommandé**

Objet : L'outil que j'utilise personnellement

Pour structurer proprement, je recommande [outil SEO].

Pourquoi ?

- Gain de temps
- Meilleure lisibilité
- Meilleur contrôle

Mais attention.

L'outil ne remplace pas la stratégie.

Demain je te montre un cas concret.

---

**Email 4 — Cas concret**

Objet : +214% en 4 mois

Un freelance m'a contacté.

Site propre. Plugin installé. Aucun trafic.

On a :

- restructuré 12 pages
- corrigé le maillage
- clarifié les intentions

Résultat : +214% trafic en 4 mois.

La différence ? Structure.

Prochain email : comment aller plus loin.

---

**Email 5 — Transition micro-offre**

Objet : Si tu veux aller plus vite

Tu peux tout faire seul.

Ou gagner du temps.

J'ai regroupé :

- Templates SEO
- Structure type
- Checklist avancée

Dans un pack simple.

Je te présente ça demain.

---

### SÉQUENCE 2 — Micro-offre Template (47€)

---

**Email 6 — Offre directe**

Objet : Le pack que j'utilise pour mes clients

Voici ce que contient le pack :

- Modèle de structure SEO WordPress
- Plan de maillage interne
- Checklist avancée
- Template optimisation page

Prix : 47€

C'est le raccourci.

👉 [Lien]

---

**Email 7 — Objections**

Objet : "Je peux le faire seul…"

Oui.

Mais combien d'heures ?

Ce pack n'achète pas de l'information.

Il achète du temps.

Et des erreurs évitées.

👉 [Lien]

---

**Email 8 — Dernier rappel**

Objet : Je ferme l'accès ce soir

Je garde le pack simple.

Pas une formation.

Un accélérateur.

Après ce soir, retour prix normal.

👉 [Lien]

---

### SÉQUENCE 3 — Upsell Formation

**Trigger :** achat template

---

**Email 1 — Limite du template**

Objet : Le template ne suffit pas

Un template aide.

Un système transforme.

Si tu veux :

- Générer du trafic stable
- Structurer ton offre
- Monétiser correctement

Il faut un cadre complet.

Je te montre ça demain.

---

**Email 2 — Présentation formation**

Objet : Le système complet WordPress Business

Dans la formation :

- Structure SEO complète
- Funnel WordPress
- Monétisation
- Automatisation

Ce n'est pas du tuto.

C'est un système.

👉 [Lien]

---

**Email 3 — Étude de cas**

Objet : Comment X a structuré son business

Un membre :

- Site existant
- Peu de trafic
- Pas d'offre claire

En 3 mois :

- Structure propre
- Offre claire
- Clients réguliers

Le système fonctionne.

👉 [Lien]

---

**Email 4 — Rappel + urgence**

Objet : Fermeture des inscriptions

La formation ferme dans 48h.

Je préfère accompagner moins de personnes.

Mais sérieusement.

Si tu veux structurer ton WordPress business : c'est maintenant.

👉 [Lien]

---

### SÉQUENCE 4 — Consulting Premium

**Trigger :** achat formation + 30 jours

---

**Email 1 — Accélération**

Objet : Tu veux aller plus vite ?

Tu as la méthode.

Mais parfois, l'exécution bloque.

Je propose : audit + stratégie personnalisée.

Ce n'est pas pour tout le monde.

C'est pour ceux qui veulent accélérer.

👉 Candidature ici

---

**Email 2 — Filtrage**

Objet : Ce n'est pas pour débuter

Le consulting est réservé :

- Aux projets actifs
- Aux entrepreneurs sérieux
- À ceux qui veulent scaler

Si tu es prêt :

👉 [Calendly]

---

### SÉQUENCE RÉACTIVATION

---

**Email 1**

Objet : Toujours intéressé par WordPress business ?

Je n'ai plus eu de nouvelles.

Je t'envoie le meilleur contenu récent.

👉 [Best of]

---

**Email 2**

Objet : Je nettoie la liste

Si tu veux rester : clique ici.

Sinon je supprime ton accès.

Simple.

---

### Résultat système séquences

Ce système :

- Crée une progression naturelle
- Augmente le panier moyen
- Segmente automatiquement
- Filtre les profils non sérieux

**Déclencheurs FluentCRM :**

| Séquence      | Trigger                                            | Tags ajoutés          |
| ------------- | -------------------------------------------------- | --------------------- |
| Nurturing SEO | Form soumis (lead magnet)                          | `lead`                |
| Micro-offre   | Email 5 envoyé                                     | `warm`                |
| Upsell form.  | Achat template (tag `buyer_template`)              | `buyer_template`      |
| Consulting    | Achat formation + 30 jours (tag `buyer_formation`) | `consulting_interest` |
| Réactivation  | No open 60 days                                    | `inactive`            |

---

## Launch Mode — 7 jours de ventes massives

**Objectif :** créer un pic massif de ventes sur 7 jours.
Pas juste "ouvrir les portes" — créer tension + preuve + momentum.

**Structure :** Pré-chauffe → Ouverture → Accélération → Clôture → Post-fermeture

---

### PHASE 1 — Pré-chauffe (J-7 à J-1)

**But :** créer le désir avant l'ouverture.

---

**Email 1 — Problème**

Objet : Pourquoi ton site ne décolle pas

Tu publies. Tu optimises. Tu testes des plugins.

Mais ton site ne devient pas un système.

Le problème n'est pas technique.
Il est stratégique.

Dans quelques jours, je montre la méthode complète.

---

**Email 2 — Diagnostic**

Objet : Les 3 niveaux WordPress

- Niveau 1 → Site vitrine
- Niveau 2 → Site optimisé
- Niveau 3 → Site business

La majorité reste au niveau 2.

Je vais ouvrir un programme pour passer au niveau 3.

---

**Email 3 — Preuve**

Objet : Ce que mes clients font différemment

Structure. Offre claire. Tunnel simple. Automatisation.

Résultat : clients réguliers.

Ouverture imminente.

---

### PHASE 2 — Ouverture (Jour 1)

---

**Email 4 — Ouverture officielle**

Objet : Les portes sont ouvertes

La formation WordPress Business System est ouverte.

Tu vas apprendre :

- Structurer ton SEO
- Construire ton funnel
- Monétiser intelligemment

Bonus lancement inclus jusqu'à dimanche.

👉 [Lien]

---

### PHASE 3 — Accélération (J2 → J5)

---

**Email 5 — Objections**

Objet : "Je manque de temps"

Justement.

La formation te fait gagner des mois d'erreurs.

Ce n'est pas une charge.

C'est un levier.

---

**Email 6 — Étude de cas**

Objet : Avant / Après réel

Avant : site désorganisé, peu de trafic, aucune offre claire.

Après : structure propre, funnel simple, ventes régulières.

👉 [Lien]

---

**Email 7 — FAQ**

Objet : Réponses aux questions fréquentes

- Est-ce pour débutant ? → Oui, si motivé.
- Faut-il coder ? → Non.
- Combien de temps ? → 6 à 8 semaines.

Clôture dimanche.

---

### PHASE 4 — Clôture (J6 & J7)

---

**Email 8 — 48h restantes**

Objet : 48h avant fermeture

Après dimanche :

- Bonus supprimés
- Prix augmente
- Accès fermé

Décision à prendre maintenant.

---

**Email 9 — 12h restantes**

Objet : On ferme ce soir

Dernière opportunité.

Si tu veux structurer ton WordPress business en 2026 : c'est maintenant.

👉 [Lien]

---

### PHASE 5 — Post-fermeture

---

**Email 10 — Fermeture réelle**

Objet : C'est fermé

Les inscriptions sont terminées.

Prochaine ouverture : date inconnue.

Si tu veux être prioritaire :

👉 Liste d'attente.

---

### Bonus Launch Mode (clés psychologiques)

Inclure lors du lancement :

| Bonus                         | Retrait  |
| ----------------------------- | -------- |
| Template Funnel avancé        | Après J7 |
| Session Q&A live              | Après J7 |
| Audit collectif               | Après J7 |
| Accès anticipé module premium | Après J7 |

---

### Structure émotionnelle du launch (ordre obligatoire)

1. Problème
2. Diagnostic
3. Preuve
4. Solution
5. Objections
6. Urgence
7. Fermeture réelle

### Pourquoi ça fonctionne

- Tension progressive
- Preuve sociale
- Rareté authentique
- Clarté offre
- Bonus temporisés

### Projection réaliste Launch Mode

| Variable        | Valeur               |
| --------------- | -------------------- |
| Liste emails    | 3 000                |
| Taux conversion | 2%                   |
| Ventes          | 60                   |
| Prix unitaire   | 697€                 |
| **CA launch**   | **41 820€ sans pub** |

### Différence clé Launch Mode

Ce n'est pas "je lance un produit".

C'est : "Je t'aide à passer au niveau business."

**Règle :** fermeture réelle = rareté crédible. Ne jamais rouvrir immédiatement après fermeture annoncée.

---

## Système High-Ticket Uniquement — schoolsWP Premium

**Positionnement :** sélectif, structuré, haut niveau.

**Ce qu'on supprime :**

- Template 47€
- Micro-offres
- Promotions
- Séquences agressives

**Ce qu'on garde :**

- Autorité
- Sélection
- Candidature

---

### Offre centrale unique — WordPress Business Architecture™

Programme premium + accompagnement stratégique.

**Promesse :** construire un système WordPress qui génère clients et revenus.

**Pricing :**

| Option              | Prix   | Contenu                        |
| ------------------- | ------ | ------------------------------ |
| Accompagnement      | 2 500€ | Programme seul                 |
| Premium             | 4 000€ | Programme + suivi mensuel      |
| Architecture totale | 6 000€ | Programme + suivi + audit live |

---

### Funnel High-Ticket

```
Contenu expert
    ↓
Lead magnet stratégique
    ↓
Masterclass (sur candidature)
    ↓
Appel stratégique (obligatoire)
    ↓
Programme premium
```

---

### Séquence Email High-Ticket (3 emails de positionnement)

**Objectif :** élever le niveau, filtrer, positionner.

---

**Email 1 — Positionnement**

Objet : Je ne vends pas des tutos WordPress

Si tu veux apprendre à installer un plugin,
ce n'est pas ici.

Si tu veux construire un système rentable,
on peut parler.

Je travaille avec :

- Freelances structurés
- Formateurs
- Entrepreneurs

Pas avec les curieux.

Demain je t'explique ma méthode.

---

**Email 2 — Méthode**

Objet : Le vrai problème n'est pas WordPress

Le problème est :

- Pas d'architecture
- Pas d'offre claire
- Pas de funnel

WordPress est un outil.

Ce qui génère des revenus, c'est le système.

Je montre ça en détail dans ma masterclass privée.

---

**Email 3 — Invitation Masterclass**

Objet : Accès limité

Masterclass : "Construire un WordPress Business rentable"

Ce que je montre :

- Architecture complète
- Funnel intégré
- Automatisation
- Positionnement premium

Inscription sur candidature.

👉 [Lien]

---

### Structure Masterclass (60–90 min)

1. Pourquoi 90% des sites WP ne génèrent rien
2. Architecture WordPress Business
3. Cocon sémantique business
4. Funnel intégré
5. Cas concret
6. Invitation programme

---

### Appel Stratégique (45 min)

**Objectif :** comprendre le projet, identifier les blocages, proposer l'accompagnement.

**Structure :**

| Étape | Question / Action                  |
| ----- | ---------------------------------- |
| 1     | Situation actuelle                 |
| 2     | Objectif 12 mois                   |
| 3     | Blocage principal                  |
| 4     | Gap stratégique identifié          |
| 5     | Proposition adaptée (prix/formule) |

**Règle :** pas de proposition sans appel. Pas d'appel sans candidature qualifiée.

---

### Séquence Post-Appel (2 emails)

**Email 1 — Résumé personnalisé**

Objet : Ce que nous avons identifié ensemble

Voici ce que nous avons identifié :

- Blocage A : [personnalisé]
- Blocage B : [personnalisé]
- Opportunité C : [personnalisée]

Si tu veux avancer, voici le lien pour rejoindre.

👉 [Lien programme]

---

**Email 2 — Dernière opportunité**

Objet : Je ferme les inscriptions ce soir

Je préfère accompagner peu de personnes,
mais sérieusement.

Si tu es prêt : c'est maintenant.

---

### Pourquoi ce système fonctionne mieux

| Critère          | Micro-offres | High-Ticket uniquement |
| ---------------- | ------------ | ---------------------- |
| Volume clients   | Élevé        | Faible (2–4/mois)      |
| Support          | Lourd        | Léger                  |
| Qualité relation | Faible       | Haute                  |
| CA mensuel       | Variable     | Prévisible             |
| Positionnement   | Généraliste  | Expert premium         |

---

### Projection réaliste High-Ticket

| Variable       | Valeur      |
| -------------- | ----------- |
| Clients/mois   | 2           |
| Prix moyen     | 4 000€      |
| **CA mensuel** | **8 000€**  |
| Clients/mois   | 3           |
| Prix moyen     | 4 000€      |
| **CA mensuel** | **12 000€** |

Stabilité > volume.

---

### Message central High-Ticket

schoolsWP ne vend plus :

- Des plugins
- Des hacks
- Des checklists

schoolsWP vend :

**Une architecture business.**

**Règle :** chaque contenu, chaque email, chaque page doit filtrer vers le haut — pas convertir à tout prix.

---

## Version Ultra Simple — Upsell schoolsWP

**Objectif :** système minimaliste, rapide à déployer, capable de générer du cash, monter en gamme et filtrer les profils sérieux. Sans 25 tags, sans usine à gaz.

### Architecture (3 niveaux)

```
Lead Magnet → Formation → Consulting
```

Optionnel : 1 micro-produit intermédiaire si besoin.

### Tags minimaux FluentCRM (6 max)

`lead` / `warm` / `buyer_template` / `buyer_formation` / `buyer_consulting` / `inactive`

### Flow simplifié

**Étape 1 — Entrée Lead Magnet**

- Trigger : formulaire checklist SEO
- Actions : Add tag `lead` → Start séquence "Nurturing 5 emails"

**Étape 2 — Séquence Nurturing (5 emails)**

- Autorité → Méthode → Cas concret → Vision business → Transition formation
- Condition : si ouvre 3 emails → Add tag `warm`

**Étape 3 — Proposition Formation Directe**

- Email 6 : présentation formation signature (pas de micro-offre obligatoire)

**Étape 4 — Achat Formation**

- Trigger : Purchase formation
- Actions : Remove tag `lead` → Add tag `buyer_formation` → Stop séquence → Start onboarding

**Étape 5 — Upsell Consulting (J+30)**

- Trigger : tag `buyer_formation` + delay 30 jours
- Email unique : "Tu veux accélérer ? Audit stratégique personnalisé." + lien Calendly

**Étape 6 — Réactivation**

- Trigger : no open 60 days → Add tag `inactive` → 2 emails max → si aucun clic : suppression

### Version email condensée (6 emails)

1. Erreur classique
2. Méthode schoolsWP
3. Cas concret
4. Vision business
5. Offre formation
6. Rappel + urgence douce

### Projection réaliste (1 000 leads)

| Palier     | Taux             | Résultat       |
| ---------- | ---------------- | -------------- |
| Formation  | 2–4%             | 20–40 ventes   |
| Consulting | 10–15% acheteurs | 3–6 consulting |

**Minimaliste ≠ faible. Minimaliste = clair.**

---

## Système Minimaliste Final — Déployable en 1h

**Ligne de progression unique :**

```
Lead Magnet → Formation Signature → Consulting Premium
```

### Tags à créer dans FluentCRM (6 max)

`lead` / `warm` / `buyer_formation` / `buyer_consulting` / `inactive` / `client`

### Automation 1 — Acquisition

- Trigger : formulaire Lead Magnet soumis
- Actions : Add tag `lead` → Start séquence "Nurturing Core"

**Séquence Nurturing Core (6 emails) :**

| Email | Objet / Thème                                 |
| ----- | --------------------------------------------- |
| 1     | L'erreur classique WordPress business         |
| 2     | La méthode (structure + cocon + vision)       |
| 3     | Cas concret + preuve réelle                   |
| 4     | Positionnement (pourquoi la plupart bloquent) |
| 5     | Présentation formation signature              |
| 6     | Rappel + urgence douce                        |

Condition optionnelle : IF ouvre 3 emails → Add tag `warm`

### Automation 2 — Achat Formation

- Trigger : Purchase "Formation Signature"
- Actions : Remove tag `lead` → Add tag `buyer_formation` → Stop all sequences → Start onboarding

### Automation 3 — Upsell Consulting

- Trigger : tag `buyer_formation` + delay 30 jours
- Email unique : "Tu veux accélérer ? Audit stratégique personnalisé." + Calendly

### Automation 4 — Achat Consulting

- Trigger : Purchase consulting
- Actions : Add tag `buyer_consulting` + `client` → Stop all sales automations

### Automation 5 — Réactivation

- Trigger : no open 60 days
- Actions : Add tag `inactive` → 2 emails → si pas de clic : suppression automatique

### KPI simples à suivre

- % conversion lead → formation
- % conversion formation → consulting
- LTV moyenne
- Coût acquisition vs revenu

**Règle :** complexifie seulement si le volume le justifie.

---

## Optimisation Conversion Formation — Cible 5–8%

**Objectif :** passer de 2–4% à 5–8% lead → formation.
**Leviers :** page de vente + séquence email + déclencheurs psychologiques.

---

### Page de vente — Structure optimisée conversion

**Hero Section**

Headline : _Transforme ton site WordPress en machine à clients en 90 jours._

Sous-titre : Sans dépendre d'outils miracles. Sans stratégie floue. Avec un système clair et duplicable.

CTA immédiat : Rejoindre la formation.

---

**Section Problème**

- Tu publies sans trafic stable
- Ton site ne génère pas de leads
- Tu installes des plugins sans stratégie
- Tu avances à l'intuition

Phrase clé : _WordPress n'est pas le problème. L'absence de système l'est._

---

**Mécanisme unique — nommer le système**

Exemple : "Le WordPress Business Loop™"

3 piliers :

1. Structure SEO intelligente
2. Funnel WordPress intégré
3. Automatisation & monétisation

---

**Preuve**

- Résultats chiffrés
- Captures trafic
- Témoignages
- Cas concret

3 preuves simples > longue théorie.

---

**Contenu formation — orienté résultats**

- Construire structure SEO rentable
- Installer funnel WordPress
- Intégrer CRM
- Générer premières ventes

Toujours parler résultat, jamais contenu brut.

---

**Offre & Bonus**

| Bonus                 | Condition            |
| --------------------- | -------------------- |
| Template Funnel WP    | Inclus               |
| Checklist SEO avancée | Inclus               |
| Audit rapide offert   | 20 premiers inscrits |

Urgence réelle. Pas artificielle.

---

**Objections traitées**

| Objection                   | Réponse               |
| --------------------------- | --------------------- |
| "Je débute"                 | Justement.            |
| "Je manque de temps"        | Le système structure. |
| "J'ai testé des formations" | Ici tu implémentes.   |

CTA répétés tous les 2–3 blocs.

---

### Séquence email agressive (6 emails)

**Email 1 — Ouverture forte**

Objet : Tu veux un site ou un business ?

La différence entre les deux ? Un système.
Demain je t'explique pourquoi 80% échouent.

---

**Email 2 — Briser une croyance**

Objet : Les plugins ne servent à rien

Ils aident. Mais sans architecture business, ils ne génèrent rien.
La formation n'est pas technique. Elle est stratégique.

---

**Email 3 — Polarisation**

Objet : Ce n'est pas pour tout le monde

Si tu veux bidouiller, tester 15 plugins, espérer → ce n'est pas pour toi.
Si tu veux structurer → oui.

---

**Email 4 — Preuve + chiffre**

Objet : +214% en 4 mois

Structure. Maillage. Offre claire.
Pas magie.

---

**Email 5 — Offre**

Objet : Tu peux continuer seul… ou accélérer

Présentation claire. CTA unique.

---

**Email 6 — Urgence réelle**

Objet : Je ferme dans 48h

Raison logique : je préfère un groupe engagé, pas une masse passive.

---

### Optimisations psychologiques

| Levier      | Application                                         |
| ----------- | --------------------------------------------------- |
| Effet perte | "Chaque mois sans structure = opportunités perdues" |
| Rareté      | Places limitées (réel)                              |
| Statut      | "Ceux qui rejoignent sont déjà dans l'action"       |
| Simplicité  | 1 seule offre. Clarté = conversion.                 |

### Projection cible

| Variable            | Avant            | Après optimisation |
| ------------------- | ---------------- | ------------------ |
| Trafic qualifié     | identique        | identique          |
| Séquence directe    | 6 emails neutres | 6 emails tension   |
| Page structurée     | basique          | conversion-first   |
| **Taux conversion** | **2–4%**         | **5–8%**           |

---

## Formation Signature Premium — WordPress Revenue System™

**Positionnement :** pas technique. Stratégique. ROI. Exécution.

**Nom :** WordPress Revenue System™
**Sous-titre :** Construire un écosystème WordPress structuré, rentable et automatisé.

---

### Ce que c'est / ce que ce n'est pas

| Ce n'est PAS          | C'est                  |
| --------------------- | ---------------------- |
| Apprendre WordPress   | Structurer une machine |
| Installer des plugins | Générer du trafic      |
| Créer un site joli    | Convertir + monétiser  |
|                       | Automatiser            |

### Cible exacte

**Pas débutant absolu.** Profil idéal :

- Freelance WP
- Créateur de contenu
- Formateur
- Entrepreneur solo
- Agence en structuration

Ils ont déjà : un site, une offre, peu ou mal structuré.

### Promesse premium

_En 8 semaines, tu passes d'un site WordPress désorganisé à un système structuré capable de générer trafic, leads et ventes de manière prévisible._

---

### Structure du programme — 8 modules

| Module | Titre                    | Livrable                        |
| ------ | ------------------------ | ------------------------------- |
| 1      | Architecture stratégique | Canvas stratégique personnalisé |
| 2      | Cocon sémantique avancé  | Plan SEO complet personnalisé   |
| 3      | Infrastructure technique | Stack validée + checklist       |
| 4      | Funnel WordPress         | Tunnel complet opérationnel     |
| 5      | Email & Automation       | Automations prêtes à déployer   |
| 6      | Monétisation             | Plan monétisation personnalisé  |
| 7      | Autorité & acquisition   | Calendrier éditorial 90 jours   |
| 8      | Scaling                  | Plan croissance annuel          |

**Détail modules :**

- **M1 :** positionnement, offre claire, structure business, mapping revenus
- **M2 :** pillar pages, clusters, maillage, intent mapping
- **M3 :** stack idéale, performance, sécurité, plugins utiles
- **M4 :** lead magnet, pages de capture, séquences, upsell
- **M5 :** segmentation simple, séquences, scoring, upsell logique
- **M6 :** affiliation stratégique, produits digitaux, offre premium, pricing
- **M7 :** LinkedIn stratégique, YouTube structuré, effet omnicanal
- **M8 :** optimisation conversion, analytics utiles, roadmap 12 mois

### Bonus premium

- Templates funnels
- SOP SEO
- Templates email
- Accès groupe privé
- 2 sessions live Q&A

### Pricing stratégique

| Phase          | Prix     |
| -------------- | -------- |
| Lancement      | 697€     |
| Premium stable | 997€     |
| Paiement       | 3× dispo |

### Projection réaliste

| Volume       | CA      |
| ------------ | ------- |
| 30 ventes/an | 29 910€ |
| 50 ventes/an | 49 850€ |

---

## Page de vente premium — WordPress Revenue System™

**Objectif :** positionner comme méthode stratégique, pas formation technique.

---

### Hero Section

**Headline :** Transforme ton site WordPress en système rentable, structuré et automatisé.

**Sous-headline :** En 8 semaines, construis une architecture claire, un tunnel efficace et un plan de monétisation solide. Sans bricolage. Sans dispersion.

**CTA :** Rejoindre WordPress Revenue System™

---

### Section 1 — Le problème réel

Tu n'as pas un problème de plugin.

Tu as un problème de structure.

La majorité des sites WordPress :

- accumulent du contenu
- installent des outils
- testent des stratégies
- espèrent des résultats

Résultat : trafic irrégulier, peu de conversions, aucune montée en gamme.

**WordPress n'est pas le problème. L'absence de système l'est.**

---

### Section 2 — Le changement de paradigme

WordPress n'est pas un site.

C'est une infrastructure business.

Quand tu maîtrises la structure + le maillage + le funnel + l'automatisation + la monétisation → ton site devient un actif.

WordPress Revenue System™ est construit pour ça.

---

### Section 3 — Le mécanisme : Revenue Architecture™

Un cadre en 5 couches :

1. Architecture stratégique
2. Cocon sémantique intelligent
3. Funnel WordPress intégré
4. Automatisation email simple
5. Monétisation multi-niveaux

Chaque couche renforce la suivante.

---

### Section 4 — Ce que tu vas construire

En 8 semaines :

- Une structure claire
- Un plan SEO cohérent
- Un tunnel opérationnel
- Des séquences email actives
- Une offre premium positionnée

Tu repars avec un système, pas des notes.

---

### Section 5 — Programme (8 modules résumés)

M1 Architecture → M2 Cocon → M3 Stack → M4 Funnel → M5 Automation → M6 Monétisation → M7 Autorité → M8 Scaling

---

### Section 6 — Bonus premium

Templates funnels · SOP SEO · Templates emails · Accès groupe privé · 2 sessions live Q&A

---

### Section 7 — Résultats attendus

- Trafic plus stable
- Offre plus claire
- Meilleure conversion
- Augmentation panier moyen
- Passage au premium naturel

---

### Section 8 — Ce n'est PAS pour toi si

- Tu veux un thème "joli"
- Tu cherches des hacks rapides
- Tu refuses de structurer ton business
- Tu veux du passif sans travail

### Section 9 — C'est pour toi si

- Tu veux un système clair
- Tu veux structurer ton WordPress business
- Tu veux arrêter l'improvisation
- Tu veux passer au niveau supérieur

---

### Section 10 — Investissement

Prix lancement : **697€** · Prix premium : **997€** · Paiement en 3× disponible.

Accès immédiat + mises à jour incluses.

---

### Section 11 — Garantie

Garantie 14 jours. Teste le système. Si tu n'es pas convaincu, remboursement. Simple.

---

### Section 12 — Appel final

Tu peux continuer à bricoler.

Ou structurer ton actif digital.

**Rejoindre WordPress Revenue System™**

---

### Ce qui rend la page premium

| Levier                  | Application                      |
| ----------------------- | -------------------------------- |
| Focus transformation    | Pas surcontenu                   |
| Positionnement business | Pas tutoriel technique           |
| Narration stratégique   | Problème → Paradigme → Mécanisme |
| Livrables concrets      | 1 livrable par module            |
| Rareté réelle           | Accompagnement limité            |

**Règle de copy :** chaque section répond à une objection ou renforce un désir. Aucun bloc décoratif.

---

## Funnel Exact de Lancement — WordPress Revenue System™

**Type :** lancement autorité 14 jours (pas "promo", positionnement expert)
**Structure :** Contenu → Masterclass → Ouverture → Relances → Fermeture

---

### Timeline exacte (14 jours)

| Jour     | Phase            | Action principale                          |
| -------- | ---------------- | ------------------------------------------ |
| J-10→J-4 | Pré-chauffage    | 3 emails + 3 posts LinkedIn                |
| J-3→J-1  | Masterclass      | Live 60–90 min + rappels                   |
| J0       | Ouverture        | Email ouverture officielle (5 jours)       |
| J1→J5    | Séquence ventes  | FAQ / Cas concret / Focus module / Urgence |
| J5 soir  | Fermeture réelle | 2 emails (matin + soir)                    |
| J6+      | Post-lancement   | 3 emails (replay + attente)                |

---

### PHASE 1 — Pré-chauffage (J-10 à J-4)

**Objectif :** créer tension + prise de conscience.

**3 emails :**

1. Pourquoi 80% des sites WP ne génèrent rien
2. Le vrai problème n'est pas technique
3. Annonce masterclass gratuite

**3 posts LinkedIn :**

1. Post problème
2. Post erreur stratégique
3. Teasing "Je prépare quelque chose"

---

### PHASE 2 — Masterclass (J-3 à J-1)

**Titre :** Transformer WordPress en machine à revenus : la méthode structurée

**Structure Masterclass (60–90 min) :**

1. Erreurs communes
2. Le modèle Revenue System
3. Cas concret
4. Plan 8 étapes
5. Invitation formation

**Rappels :** email J-2 (confirmation) + email J-1 (rappel 24h) + email J0 matin (rappel 2h)

---

### PHASE 3 — Ouverture (J0)

Email : "Les inscriptions sont ouvertes"

Contenu :

- Résumé masterclass + valeur
- Ce que contient le programme
- Bonus inclus
- Deadline claire (5 jours)

---

### PHASE 4 — Séquence ventes (J1 → J5)

| Jour     | Email                  | Objectif                                           |
| -------- | ---------------------- | -------------------------------------------------- |
| J1       | FAQ objections         | Je n'ai pas le temps / pas technique / déjà avancé |
| J2       | Étude de cas détaillée | Transformation réelle prouvée                      |
| J3       | Focus module + bonus   | Zoom sur 2 modules clés                            |
| J4       | Urgence douce          | "Plus que 48h"                                     |
| J5 matin | Dernière journée       | Clarté + CTA direct                                |
| J5 soir  | Fermeture imminente    | "Fermeture dans quelques heures"                   |

### Bonus limités (tension réelle)

| Bonus              | Condition            |
| ------------------ | -------------------- |
| 1 audit offert     | 10 premiers inscrits |
| Template exclusif  | Durée lancement      |
| Session privée Q&A | Durée lancement      |

---

### PHASE 5 — Post-lancement

**Si achat :** → onboarding premium (séquence dédiée)

**Si non-achat (3 emails) :**

1. Replay disponible 48h
2. Pourquoi j'ai fermé (positionnement)
3. Liste d'attente prochaine session

---

### Structure technique FluentCRM — Tags lancement

| Tag                      | Déclencheur                        |
| ------------------------ | ---------------------------------- |
| `registered_masterclass` | Inscription formulaire masterclass |
| `attended_masterclass`   | Participation live                 |
| `visited_sales_page`     | Visite page de vente               |
| `buyer_wrs`              | Achat WordPress Revenue System™    |
| `non_buyer_launch`       | Non-acheteur fin lancement         |

### Automations FluentCRM — Lancement

| Automation        | Trigger → Action                                       |
| ----------------- | ------------------------------------------------------ |
| Inscription       | Form → Add tag `registered_masterclass` → Rappels live |
| Participation     | Tag `attended_masterclass` → Séquence ouverture        |
| Visite page vente | Tag `visited_sales_page` → Relance spécifique          |
| Non acheteur      | Fin lancement + no purchase → Séquence post-fermeture  |

---

### KPI cibles lancement

| Variable             | Valeur                |
| -------------------- | --------------------- |
| Inscrits masterclass | 1 000                 |
| Taux conversion      | 2–5%                  |
| Ventes               | 20–50                 |
| **CA (à 697€)**      | **13 940€ → 34 850€** |

---

### Positionnement premium clé

**Pas :** "Promo exceptionnelle !"

**Mais :** "Je ferme pour préserver la qualité de l'accompagnement."

### Pourquoi ce funnel fonctionne

- Autorité démontrée par la valeur (masterclass)
- Pas de pression agressive
- Transformation prouvée avant vente
- Deadline réelle et justifiée
- Bonus stratégiques (pas gadgets)

**Règle lancement :** la masterclass doit apporter assez de valeur pour que quelqu'un soit frustré de ne pas aller plus loin.

---

## Mécanisme Unique — Authority Loop™

**Concept propriétaire schoolsWP.** Pas "méthode", pas "framework", pas "formation".

**Nom :** Authority Loop™
**Sous-titre :** Le système en 5 boucles qui transforme un site WordPress en moteur d'autorité et de revenus.

### Pourquoi "Loop" ?

- Ce n'est pas linéaire
- Ce n'est pas une checklist
- C'est un cycle auto-renforçant — chaque étape nourrit la suivante

---

### Structure de l'Authority Loop™ (5 boucles)

```
Structure → Attraction → Conversion → Monétisation → Amplification
     ↑                                                      |
     └──────────────────────────────────────────────────────┘
```

**Boucle 1 — Structure**

- Positionnement clair
- Offre définie
- Cocon sémantique
- Stack technique propre

_Sans structure → pas d'autorité._

**Boucle 2 — Attraction**

- Contenu SEO stratégique
- LinkedIn
- YouTube
- Lead magnet

_Tu attires avec la valeur._

**Boucle 3 — Conversion**

- Funnel WordPress
- Pages de capture
- Séquences email
- Micro-engagement + upsell logique

_Tu transformes le trafic en leads._

**Boucle 4 — Monétisation**

- Formation
- Affiliation
- Produits digitaux
- Consulting

_Tu transformes les leads en cash._

**Boucle 5 — Amplification**

- Témoignages + études de cas
- Autorité sociale
- Backlinks

_L'autorité attire plus de trafic → la boucle recommence._

---

### Ce qui rend le mécanisme puissant

Il explique pourquoi la plupart échouent :

| Symptôme observé                      | Boucle manquante |
| ------------------------------------- | ---------------- |
| Du trafic mais pas de ventes          | Conversion       |
| Des ventes mais sans système stable   | Structure        |
| Du contenu sans résultat              | Attraction       |
| Des leads mais pas de montée en gamme | Monétisation     |

**Le problème n'est pas WordPress. C'est l'absence de boucle.**

---

### Alternatives si besoin d'autre nom

| Nom                          | Positionnement                               |
| ---------------------------- | -------------------------------------------- |
| Revenue Architecture System™ | Plus business/sérieux                        |
| WP Growth Engine™            | Plus stratégique                             |
| Système C.O.R.E.™            | Contenu–Offre–Revenus–Expansion (FR premium) |

**Recommandation :** Authority Loop™ — simple, pédagogique, visuel, facile à décliner partout.

---

### Déclinaisons marketing Authority Loop™

| Support       | Application                                                            |
| ------------- | ---------------------------------------------------------------------- |
| Page de vente | "Tu rejoins le Authority Loop™"                                        |
| Emails        | "Voici comment fonctionne le Authority Loop™"                          |
| LinkedIn      | Carrousel "Les 5 boucles du Authority Loop™"                           |
| YouTube       | Vidéo "Pourquoi ton site ne génère rien (et comment fermer la boucle)" |
| Masterclass   | Slide centrale du pitch                                                |

### Positionnement final

Tu ne vends pas "une formation WordPress".

Tu vends : **l'accès au Authority Loop™**.

**Règle :** chaque contenu, chaque email, chaque page doit référencer le mécanisme pour créer une signature de marque reconnaissable.

---

## Promesse Optimisée — Conversion Maximale

**Problème de la promesse standard :** trop générique, trop pédagogique, pas assez transformationnelle, pas assez sélective.

**Objectifs :** augmenter la perception premium · clarifier la transformation · éliminer les profils non qualifiés · maximiser la conversion.

---

### Formule haute performance

> Aider **[profil précis]** à passer de **[problème douloureux]** à **[résultat désirable mesurable]** en **[délai réaliste]**, sans **[objection principale]**.

---

### 6 versions testables

| #   | Nom                        | Promesse                                                                                                                                                                                               |
| --- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| V1  | Claire & directe           | En 8 semaines, transforme ton site WordPress en système structuré capable de générer trafic, leads et ventes de manière prévisible — sans passer tes journées à bidouiller des plugins.                |
| V2  | Premium business           | Pour freelances et entrepreneurs WordPress sérieux : construis un écosystème structuré qui attire du trafic qualifié et convertit en ventes récurrentes — même si ton site stagne aujourd'hui.         |
| V3  | Radicale & différenciante  | Arrête d'avoir un "site WordPress". Construis une machine structurée qui génère des revenus.                                                                                                           |
| V4  | Ultra premium positionnée  | WordPress Revenue System™ — Le programme stratégique qui transforme un site WordPress désorganisé en écosystème structuré capable de générer trafic, leads et revenus mesurables en moins de 90 jours. |
| V5  | Sélective (filtre naturel) | Réservé aux freelances et créateurs déjà en activité : structure ton WordPress pour qu'il devienne un levier de croissance rentable — pas un simple site vitrine.                                      |
| V6  | Axée ROI                   | Passe d'un site WordPress qui existe… à un système qui génère du chiffre.                                                                                                                              |

---

### Recommandation stratégique schoolsWP

**Promesse principale :**

> Transforme ton WordPress en système structuré capable de générer trafic, leads et ventes de manière prévisible en 90 jours.

**Sous-promesse (objections levées) :**

> Sans dépendre uniquement de l'affiliation. Sans complexifier ton stack. Sans passer 6 mois à tester.

---

### Avant / Après positionnement

| Avant                         | Après                               |
| ----------------------------- | ----------------------------------- |
| "Formation WordPress avancée" | "Transformation business mesurable" |
| Générique                     | Ciblé + exclusif                    |
| Pédagogique                   | Orienté ROI                         |

---

### Déclencheurs psychologiques à inclure systématiquement

| Déclencheur            | Pourquoi ça convertit              |
| ---------------------- | ---------------------------------- |
| Délai clair (90 jours) | Crédibilité + vision concrète      |
| "Mesurable"            | Réduit le risque perçu             |
| Filtrage audience      | Augmente le désir par exclusivité  |
| "Système"              | Signale durabilité vs tip ponctuel |
| "Structuré"            | Signale méthode vs improvisation   |

**Règle promesse :** une promesse qui filtre les mauvais profils convertit mieux qu'une promesse qui tente de plaire à tous.

---

## 10 Hooks LinkedIn + Outlines — Prêts à publier

**Ton :** clair, stratégique, orienté ROI.
**Rythme :** 2 posts/semaine — alterner : opinion → framework → coulisses.
**Règle :** 1 idée forte + 1 question ou CTA léger par post.

---

**Hook 1**

_La vérité que personne ne dit sur WordPress : ce n'est pas un outil. C'est un système de vente._

Outline :

- Problème : la majorité utilisent WordPress comme un CMS
- Réalité : un site doit avoir un job précis (attirer / capturer / convertir)
- Framework : Trafic → Lead magnet → Email → Offre
- Conclusion : si ton site ne génère pas d'opportunités, ce n'est pas un actif
- CTA subtil : "Je peux détailler ce système si ça t'intéresse."

---

**Hook 2**

_90% des sites WordPress échouent pour une raison simple : ils n'ont pas de job précis._

Outline :

- Définis "le job d'un site"
- Erreur classique : site vitrine sans funnel
- 3 jobs possibles : génération leads / vente directe / autorité SEO
- Question finale : quel est le job de ton site ?

---

**Hook 3**

_Tu n'as pas besoin de plus de trafic. Tu as besoin d'un meilleur chemin de conversion._

Outline :

- Idée contre-intuitive
- Exemple chiffré : 1 000 visiteurs mal convertis vs 300 qualifiés
- Mini-framework : page claire + offre claire + CTA visible + email
- Punchline finale

---

**Hook 4**

_Si je devais relancer un site WordPress de zéro aujourd'hui, je ferais exactement ça._

Outline :

- Pas de design complexe
- 3 pages seulement : pilier + lead magnet + offre
- SEO dès le début, email avant social
- Conclusion : simplicité > complexité

---

**Hook 5**

_J'ai analysé des dizaines de sites WordPress. Les mêmes 3 erreurs reviennent._

Outline :

- Erreur 1 : trop de plugins inutiles
- Erreur 2 : pas de stratégie contenu
- Erreur 3 : aucun funnel
- Comment corriger ça simplement

---

**Hook 6**

_Arrête de chercher le "meilleur plugin". Commence par définir ton objectif business._

Outline :

- Le piège du comparatif infini
- Vrai critère : génère-t-il du revenu ? simplifie-t-il le système ?
- Question finale au lecteur

---

**Hook 7**

_WordPress est sous-exploité en France. Et c'est une opportunité._

Outline :

- Observation marché
- Peu de stratégie, beaucoup de technique
- Opportunité pour ceux qui pensent ROI
- Conclusion : il y a de la place

---

**Hook 8**

_Le funnel WordPress en 5 étapes (que personne ne t'explique clairement)._

Outline :

1. Trafic
2. Capture
3. Séquence email
4. Offre
5. Upsell

Simple. Structuré. Actionnable.

---

**Hook 9**

_Le trafic SEO ne suffit pas. Voilà pourquoi._

Outline :

- Mythe : plus de trafic = plus de ventes
- Réalité : intention + structure > volume
- Exemple simple
- Lien avec stratégie contenu

---

**Hook 10**

_Voici la différence entre un site WordPress amateur et un site stratégique._

Outline :

| Amateur       | Stratégique    |
| ------------- | -------------- |
| Design        | Objectif clair |
| Plugins       | Funnel         |
| Pages isolées | Tracking       |
|               | Monétisation   |

Conclusion forte.

---

### Utilisation intelligente

| Variable       | Valeur recommandée                     |
| -------------- | -------------------------------------- |
| Fréquence      | 2 posts/semaine                        |
| Alternance     | Opinion → Framework → Coulisses        |
| Structure      | 1 idée forte + 1 CTA léger ou question |
| Longueur cible | 5–12 lignes (mobile first)             |
| Hook           | Toujours en première ligne, accrocheur |

---

## 40 Hooks Thématiques LinkedIn (SEO / Funnel / Affiliation / Automatisation)

### SEO — 10 Hooks

1. Mon site schoolsWP n'existait pas sur Google il y a 18 mois. Aujourd'hui il génère 4 200 visites organiques/mois. Voici exactement ce que j'ai changé :

2. La plupart des formateurs WordPress publient du contenu. Moi j'ai construit une architecture sémantique. La différence : +340% de trafic en 6 mois.

3. J'ai mis 2 ans à comprendre pourquoi mes articles ne rankaient pas. La réponse n'était pas dans le contenu — elle était dans la structure du site.

4. Stop au blog WordPress "régulier". Voici le système de contenu qui génère du trafic même quand tu ne publies pas :

5. Google ne classe pas les articles. Il classe les sites qui ont une autorité thématique. Comment construire cette autorité avec 2h/semaine :

6. J'ai analysé les 10 premiers résultats Google sur "formation WordPress". Ils ont tous un point commun — et ce n'est pas leur nombre de backlinks.

7. Mon article le plus trafiqué a été écrit en 45 minutes. L'article qui m'a pris 3 heures ne classe pas. Leçon :

8. L'erreur SEO que font 90% des formateurs WordPress indépendants (et comment l'éviter en une décision) :

9. RankMath seul ne fait pas le SEO. Ce qui fait le SEO c'est l'intention de recherche. Voici comment je l'intègre dans chaque page :

10. Le SEO gratuit vs le SEO payant pour un formateur WordPress indépendant — comparaison honnête après 3 ans de tests :

---

### Funnel — 10 Hooks

1. Mon funnel WordPress génère en moyenne 3 500€/mois avec 0 publicité. Il a 4 étapes. Voici la structure :

2. J'ai eu un funnel complexe (7 étapes, 3 upsells, 12 emails). Conversion : 1,2%. Je l'ai simplifié à 4 étapes. Conversion : 4,7%. Ce qui a changé :

3. La vraie raison pour laquelle ton funnel ne convertit pas n'est pas le copywriting. C'est la logique de transformation que tu proposes.

4. Un formateur WordPress m'a demandé pourquoi son lead magnet ne convertissait pas. Je lui ai lu sa page d'accueil. Réponse trouvée en 30 secondes :

5. Funnel minimaliste pour freelance WordPress solo : 1 lead magnet → 1 séquence email → 1 offre. KPIs visés et comment les atteindre :

6. Le moment exact où un prospect décide d'acheter ta formation WordPress — et comment structurer ton funnel autour de ce moment :

7. FluentCRM + WooCommerce + un bon copywriting = système de vente autonome. Voici l'architecture que j'utilise sur schoolsWP :

8. Je teste mes funnels avec une règle simple : si je dois l'expliquer à quelqu'un, c'est qu'il est trop complexe. Ce que ça m'a appris :

9. La page de vente la plus convertissante que j'aie jamais écrite faisait 800 mots. Elle remplaçait une page de 2 400 mots. Pourquoi :

10. Stop aux tunnels de vente copiés-collés. Voici comment construire un funnel qui correspond à TON positionnement WordPress :

---

### Affiliation — 10 Hooks

1. L'affiliation WordPress ne fonctionne pas si tu recommandes tout. Voici comment j'ai sélectionné 6 plugins qui génèrent 90% de mes commissions :

2. Mois 1 d'affiliation WordPress : 47€. Mois 12 : 1 840€. Ce qui a changé entre les deux n'est pas le trafic.

3. Je refuse de recommander des plugins que je n'utilise pas. Ça m'a coûté des commissions. Ça m'a aussi construit une autorité que je n'aurais pas autrement.

4. L'erreur d'affiliation la plus fréquente chez les blogueurs WordPress : placer les liens avant d'avoir construit la confiance. Comment corriger ça :

5. Comparatif honnête entre 3 programmes d'affiliation WordPress : TutorLMS, FluentCRM, WP Rocket. Commissions, cookies, conversions :

6. Mon article de comparaison TutorLMS vs LearnDash m'a rapporté 4 200€ en affiliation en 12 mois. Structure exacte de l'article :

7. L'affiliation ne remplace pas une offre propre. Elle l'amplifie. Voici comment les deux s'articulent dans mon modèle de revenus schoolsWP :

8. Disclosure affilié : obligatoire légalement, utile stratégiquement. Comment je le formule pour que ça renforce la confiance :

9. Certains plugins ne méritent pas d'être recommandés même si la commission est haute. Les critères que j'utilise pour décider :

10. Le contenu evergreen d'affiliation WordPress qui génère des commissions passives 18 mois après publication — type, structure, mise à jour :

---

### Automatisation — 10 Hooks

1. J'ai automatisé 80% de mon système de contenu WordPress avec n8n et FluentCRM. Résultat : 6h libérées par semaine. Ce que j'ai automatisé en premier :

2. L'erreur d'automatisation que j'ai faite pendant 1 an : automatiser ce qui n'était pas encore optimisé manuellement. Leçon apprise :

3. FluentCRM seul peut gérer tout le nurturing d'une formation WordPress indépendante. Setup minimal qui fonctionne :

4. n8n + WordPress + Google Sheets = système de reporting automatique. Workflow complet que j'utilise chaque semaine :

5. Tu n'as pas besoin d'ActiveCampaign si tu es un formateur WordPress solo. FluentCRM fait 90% du travail pour 0€/mois de frais variables.

6. Automatisation ≠ impersonnel. Voici comment mes séquences email automatiques donnent l'impression d'être écrites à la main :

7. Le workflow n8n le plus utile que j'aie créé pour schoolsWP (et qui me fait gagner 3h/semaine) — description et logique :

8. 3 automatisations WordPress que tout formateur indépendant devrait avoir avant même de penser à scaler :

9. Comment j'ai connecté mon système de contenu, mon CRM et mes ventes en un seul flux automatisé — sans une ligne de code custom :

10. Automatiser l'onboarding d'un nouvel élève WordPress : de l'achat à la première connexion LMS en 0 intervention manuelle. Architecture :

---

## 10 Hooks Ultra Polarisants (Prise de position forte)

1. Les "formateurs WordPress" qui vendent du trafic avant de vendre de la transformation ont tort. Et voici pourquoi leurs élèves échouent.

2. WordPress est devenu le plugin le plus vendu de l'internet. C'est aussi devenu l'excuse la plus utilisée pour justifier un mauvais positionnement.

3. Tu n'as pas besoin d'un funnel complexe. Tu as besoin d'une promesse claire. L'industrie du marketing digital nous a vendus de la complexité inutile.

4. Avis impopulaire : la plupart des "formations WordPress" ne forment pas. Elles listent des fonctionnalités. C'est pour ça qu'elles ne se vendent plus.

5. Je ne cherche pas à plaire à tout le monde. Sur schoolsWP je m'adresse aux formateurs qui veulent construire quelque chose de réel — pas aux chasseurs de "side hustle rapide".

6. Le SEO ne sauvera pas ton business WordPress si ton positionnement est flou. Arrêtez de blâmer l'algorithme.

7. La vérité sur les revenus passifs WordPress que personne ne dit : c'est du travail actif bien automatisé. Il n'y a pas de magie. Il y a un système.

8. J'aurais pu vendre une formation à 97€ à 500 personnes. J'ai choisi de vendre à 997€ à 50 personnes. Voici pourquoi — et ce que ça change pour l'élève.

9. Le plus grand ennemi d'un formateur WordPress indépendant n'est pas la concurrence. C'est son incapacité à dire non aux mauvais clients.

10. Je suis contre les "packs démarrage" WordPress à bas prix. Non pas parce que je veux vendre cher — mais parce qu'ils forment des clients qui ne savent pas se vendre eux-mêmes.

---

### Règle des hooks polarisants

- **Utiliser avec parcimonie** : 1 sur 5 posts maximum
- **Toujours argumenter** : la prise de position doit être suivie d'un développement logique
- **Jamais attaquer des personnes** : critiquer des pratiques, pas des individus
- **Assumer** : ne pas rétropédaler dans les commentaires — tenir la position ou l'enrichir

---

## 10 Hooks Optimisés pour Déclencher des DM

> Objectif : provoquer des DM qualifiés, pas des likes. Chaque hook cible un profil précis, pointe une douleur business, ouvre une boucle — et invite à écrire en privé.

---

### Hook 1 — "Audit implicite"

Si ton site WordPress fait du trafic mais peu de ventes, il y a probablement un problème de structure — pas de visibilité.

[Développement : 4–6 lignes sur les 3 raisons les plus fréquentes]

_CTA : "Si tu veux que je te dise où ça bloque, écris-moi 'audit' en DM."_

---

### Hook 2 — "Segment clair"

Freelances WordPress : si vous facturez uniquement des sites vitrines, vous laissez énormément d'argent sur la table.

[Développement : chiffres, repositionnement offre, exemple concret]

_CTA : "Je peux t'expliquer comment repositionner ton offre — écris-moi."_

---

### Hook 3 — "Erreur invisible"

80% des funnels WordPress que j'analyse ont la même erreur — et elle n'est pas technique.

[Développement : décrire l'erreur (absence de promesse claire, pas de séquence nurturing…)]

_CTA : "Je peux te dire laquelle si tu veux — DM."_

---

### Hook 4 — "Projection personnelle"

Si je devais analyser ton site aujourd'hui, je regarderais une seule chose en priorité.

[Développement : les 3 éléments que je scrute + ce que ça révèle sur le business]

_CTA : "Curieux de savoir laquelle ? Écris-moi."_

---

### Hook 5 — "Comparaison frustrante"

Deux sites WordPress. Même trafic. Résultats ×5 différents. La différence ? Le système derrière.

[Développement : décrire les 2 profils, ce qui diffère structurellement]

_CTA : "Si tu veux comprendre ce que je regarde en premier, écris-moi."_

---

### Hook 6 — "Stack stratégique"

Ton problème n'est peut-être pas ton plugin SEO. C'est peut-être ton absence de stratégie globale.

[Développement : les 3 erreurs de stack les plus fréquentes + leur impact réel]

_CTA : "Je peux t'aider à clarifier ça — DM ouvert."_

---

### Hook 7 — "Diagnostic rapide"

Si ton WordPress dépend de toi chaque jour pour vendre, tu n'as pas un système. Tu as un job.

[Développement : les 3 automatisations minimales pour décrocher de l'opérationnel]

_CTA : "Je peux te montrer comment automatiser ça — écris-moi."_

---

### Hook 8 — "Niveau supérieur"

La plupart des créateurs WordPress stagnent parce qu'ils pensent technique, pas business.

[Développement : différence concrète entre mindset technique vs business, exemples]

_CTA : "Tu veux passer au niveau business ? DM."_

---

### Hook 9 — "Invitation fermée"

Je regarde 3 sites WordPress cette semaine pour analyser leur funnel en profondeur.

[Pas de développement — la rareté fait tout. Stopper ici.]

_CTA : "Si tu veux en faire partie, écris-moi avant jeudi."_

> **Note** : ultra efficace mais à utiliser rarement. Maximum 1x/mois, engagement fort garanti.

---

### Hook 10 — "Clarté brutale"

Si ton site ne capture pas d'email, il ne travaille pas pour toi.

[Développement : ce qu'un site qui "travaille" fait automatiquement — liste courte et percutante]

_CTA : "Je peux te montrer comment corriger ça simplement — DM."_

---

### Pourquoi ces hooks déclenchent des DM

| Mécanisme               | Effet                                             |
| ----------------------- | ------------------------------------------------- |
| Ciblage profil précis   | Le lecteur se reconnaît — il se sent visé         |
| Douleur business nommée | Crée un sentiment d'urgence ou de reconnaissance  |
| Boucle incomplète       | La curiosité pousse à agir pour avoir la réponse  |
| Aide personnalisée      | Différencie du contenu générique                  |
| Ton sobre               | Pas agressif → crédibilité + confiance maintenues |

### Règles d'utilisation

- **Fréquence** : 1 hook DM sur 4 posts (pas plus)
- **Honorer les DM** : répondre dans les 24h, toujours
- **Hook 9 (invitation fermée)** : max 1x/mois — perdrait son effet si répété
- **Jamais deux CTA DM consécutifs** : alterner avec posts de valeur pure sans appel à l'action

---

## 10 Hooks Orientés Preuve Sociale

> Objectif : installer l'autorité silencieusement. On montre — on ne se vante pas. Volume + expérience + observation experte.

---

### Hook 1 — "Après avoir analysé…"

Après avoir analysé plus de 50 sites WordPress, le problème n'est presque jamais technique.

[Développement : les 3 vrais problèmes récurrents — positionnement flou, absence de parcours, pas de système de capture]

---

### Hook 2 — "Sur les X derniers projets…"

Sur mes 12 derniers audits WordPress, 10 avaient exactement la même faille stratégique.

[Développement : nommer la faille, expliquer pourquoi elle est invisible pour son propriétaire]

---

### Hook 3 — "Les clients avec lesquels je travaille…"

Les freelances WordPress qui structurent un vrai funnel doublent presque toujours leur taux de conversion — sans augmenter leur trafic.

[Développement : mécanisme expliqué, chiffres si disponibles, avant/après]

---

### Hook 4 — "Voici ce que j'observe systématiquement…"

Voici ce que j'observe systématiquement chez les sites qui dépassent 10 000 visiteurs/mois.

[Développement : liste des 3–4 caractéristiques communes — structure, contenu, parcours, email]

---

### Hook 5 — "Les données montrent que…"

Les données montrent que le trafic SEO ne vaut rien sans chemin de conversion clair.

[Développement : exemple concret, ratio trafic/conversion, ce qui change quand on ajoute un funnel minimal]

---

### Hook 6 — "Les sites qui performent…"

Les sites WordPress qui performent ne publient pas plus. Ils publient plus stratégiquement.

[Développement : différence entre volume et architecture éditoriale — cocon, intention, maillage]

---

### Hook 7 — "Depuis que j'ai mis en place…"

Depuis que j'ai structuré mon contenu en cocon sémantique, mes articles ne vivent plus isolés — ils se renforcent mutuellement.

[Développement : résultat mesurable, délai, ce que ça a changé concrètement sur le trafic ou la conversion]

---

### Hook 8 — "La différence entre mes clients A et B…"

La seule différence entre mes clients qui stagnent et ceux qui progressent : la clarté de leur offre.

[Développement : ce que "clarté" veut dire concrètement — cible, transformation, preuve, prix assumé]

---

### Hook 9 — "Les 3 patterns qui reviennent…"

Après plusieurs années dans l'écosystème WordPress, 3 patterns reviennent toujours chez ceux qui monétisent réellement.

[Développement : les 3 patterns nommés et expliqués brièvement — autorité thématique, système email, offre positionnée]

---

### Hook 10 — "Ce que montrent les chiffres…"

Les chiffres sont clairs : un site bien structuré convertit plus avec moins de trafic.

[Développement : exemples de ratios — site moyen vs site structuré, ce que ça implique pour l'effort de création]

---

### Pourquoi ces hooks installent l'autorité

| Mécanisme                     | Effet                                               |
| ----------------------------- | --------------------------------------------------- |
| Observateur expérimenté       | Sous-entend volume de cas traités sans le dire      |
| Données + patterns            | Crédibilité factuelle, pas d'opinion vide           |
| Boucle de curiosité           | Le lecteur veut savoir ce qu'il fait ou ne fait pas |
| Ton sobre, non arrogant       | Autorité ressentie, pas proclamée — plus efficace   |
| Résultats implicites ou réels | Preuve sociale diffuse : "ça marche pour d'autres"  |

### Règles d'utilisation

- **Sincérité obligatoire** : n'utiliser que des chiffres/observations réels — jamais inventés
- **Précision > généralité** : "12 audits" est plus fort que "de nombreux clients"
- **Sans CTA agressif** : ces hooks n'ont pas besoin d'appel à l'action explicite — l'autorité attire naturellement
- **Alterner avec hooks DM** : preuve sociale prépare le terrain, hook DM convertit — les deux se complètent

---

## 10 Hooks Narratifs Storytelling

> Objectif : humaniser l'autorité. Créer de la connexion. Montrer qu'on pense en stratège — via une expérience vécue, une erreur assumée, une leçon concrète.

1. Au début, je pensais que WordPress, c'était juste installer des thèmes et des plugins. J'avais totalement tort.

2. Le jour où j'ai compris que mon site ne vendait pas, tout a changé.

3. J'ai passé des mois à optimiser mon SEO… sans jamais optimiser ce qui venait après.

4. Un client m'a dit une phrase qui m'a fait revoir toute ma vision du WordPress business.

5. Je me suis trompé sur un point crucial quand j'ai lancé mon premier site.

6. Personne ne m'avait expliqué que le vrai problème n'était pas le trafic.

7. Pendant longtemps, j'ai publié du contenu comme tout le monde. Jusqu'à ce que je comprenne que je construisais du bruit, pas un système.

8. J'ai analysé mon propre site comme si c'était celui d'un client. Le diagnostic m'a surpris.

9. Si je pouvais parler au moi d'il y a 3 ans, je lui dirais une seule chose sur WordPress.

10. Je pensais que le problème venait du design. En réalité, c'était l'absence de stratégie.

### Pourquoi ces hooks fonctionnent

| Mécanisme                   | Effet                                                      |
| --------------------------- | ---------------------------------------------------------- |
| Curiosité activée           | Boucle ouverte — le lecteur veut savoir la suite           |
| Vulnérabilité maîtrisée     | Humanise sans fragiliser — renforce la confiance           |
| Identification              | Le lecteur se reconnaît dans l'erreur ou la situation      |
| Leçon stratégique implicite | Positionne comme quelqu'un qui pense + loin que les autres |

---

## 5 Posts Complets Prêts à Publier (Storytelling)

---

### Post 1 — "Au début, je pensais…"

Au début, je pensais que WordPress, c'était juste installer des thèmes et des plugins.
J'avais totalement tort.

Je passais mon temps à comparer des thèmes.
Tester des plugins.
Optimiser des détails techniques.

Mais je ne me posais jamais la vraie question :

Pourquoi ce site existe ?

Un site WordPress n'est pas un projet technique.
C'est un actif stratégique.

Il doit :

- Attirer une audience qualifiée
- Structurer un parcours
- Convertir
- Nourrir
- Vendre

Sinon, c'est juste une vitrine.

**Leçon** : Le problème n'est pas ton thème. C'est ton absence de système.

_Si tu devais définir la mission précise de ton site en une phrase, ce serait quoi ?_

---

### Post 2 — "J'ai passé des mois à…"

J'ai passé des mois à optimiser mon SEO… sans jamais optimiser ce qui venait après.

Plus de trafic.
Plus de clics.
Plus d'impressions.

Et pourtant ?

Aucune vraie croissance.

Parce que le SEO attire.
Mais le funnel convertit.

Si ton article ne mène nulle part,
tu construis une audience pour quelqu'un d'autre.

Le vrai levier :
SEO → Lead magnet → Email → Offre claire.

Sans ça, ton trafic s'évapore.

**Leçon** : Le SEO sans structure business est une illusion de progression.

_Tu as combien d'étapes entre ton article et ton offre ?_

---

### Post 3 — "Le jour où j'ai compris…"

Le jour où j'ai compris que mon site ne vendait pas, tout a changé.

Je pensais que le problème venait du design.
Puis du copywriting.
Puis du plugin.

En réalité ?

Il n'y avait aucun parcours.

Pas de logique.
Pas de segmentation.
Pas d'intention.

Juste des pages.

Un site devient puissant quand chaque page a une mission unique.
Pas cinq.

**Leçon** : Un site n'est pas un ensemble de pages. C'est un chemin.

_Si je te demande : "Quelle est la prochaine action après ton article principal ?" — tu réponds quoi ?_

---

### Post 4 — "Un client m'a dit…"

Un client m'a dit une phrase qui m'a fait revoir toute ma vision du WordPress business.

Il m'a dit :

"Je ne veux pas un site. Je veux des clients."

Ça paraît évident.

Mais 90% des projets WordPress sont pensés comme des projets web.
Pas comme des systèmes d'acquisition.

On parle design, animations, couleurs.
On ne parle pas assez flux, positionnement, conversion, nurturing.

**Leçon** : Un site ne doit pas être beau. Il doit être rentable.

_Est-ce que ton site travaille pour toi… ou juste avec toi ?_

---

### Post 5 — "Si je pouvais parler au moi d'il y a 3 ans…"

Si je pouvais parler au moi d'il y a 3 ans, je lui dirais une seule chose sur WordPress.

Arrête de courir après les outils.

Choisis une stack.
Structure un funnel.
Construis une liste email.
Publie stratégique.

Puis répète.

La dispersion est l'ennemi numéro 1 des indépendants.

Ce n'est pas le manque d'outils.
C'est le manque de focus.

**Leçon** : La simplicité structurée bat la complexité brillante.

_Tu es plutôt en phase d'exploration… ou de structuration ?_

---

### Format posts LinkedIn — Règles

| Élément     | Recommandation                                                    |
| ----------- | ----------------------------------------------------------------- |
| Longueur    | 150–250 mots (5–12 lignes visibles avant "voir plus")             |
| Rythme      | Phrases courtes + sauts de ligne — jamais de blocs denses         |
| Leçon       | Toujours en gras, en fin de développement                         |
| CTA         | Question ouverte — pas de lien en premier commentaire             |
| Fréquence   | 1 post storytelling sur 3 posts publiés                           |
| Premier mot | Jamais "Je" — commencer par un chiffre, une situation, une action |

---

## 5 Carrousels Signature schoolsWP

> Structure type : Hook fort → Contexte → Problème → Insight → Framework → Erreur fréquente → Application → CTA subtil

---

### Carrousel 1 — "Au début, je pensais que…"

**Slide 1** — Au début, je pensais que WordPress, c'était installer des thèmes et des plugins.

**Slide 2** — Je pensais que plus le site était "complet", plus il serait performant.

**Slide 3** — Résultat ? Beaucoup d'efforts. Peu de résultats.

**Slide 4** — La vraie question n'était pas : "Quel plugin utiliser ?"

**Slide 5** — Mais : Quel rôle joue ce site dans mon business ?

**Slide 6 — Framework**
Un site WordPress efficace =

- Une cible claire
- Une offre claire
- Un chemin clair

**Slide 7** — Sans ça, WordPress devient un hobby technique.

**Slide 8 — CTA** — Si tu veux la checklist pour transformer ton site en levier business, dis "CHECKLIST".

---

### Carrousel 2 — "Le jour où j'ai compris…"

**Slide 1** — Le jour où j'ai compris que mon site ne vendait pas, tout a changé.

**Slide 2** — J'avais du trafic. Mais aucune progression logique.

**Slide 3** — Un site sans parcours = un trou noir d'attention.

**Slide 4** — Voici ce que j'ai changé.

**Slide 5 — Framework**

- Étape 1 : Attirer (SEO ciblé)
- Étape 2 : Capturer (lead magnet)
- Étape 3 : Nourrir (email)
- Étape 4 : Convertir (offre)

**Slide 6** — Simple. Mais structuré.

**Slide 7** — La plupart optimisent l'étape 1… Et oublient les 3 suivantes.

**Slide 8 — CTA** — Je peux détailler ce système si ça t'intéresse.

---

### Carrousel 3 — "Pendant longtemps, j'ai publié comme tout le monde…"

**Slide 1** — Pendant longtemps, j'ai publié du contenu comme tout le monde.

**Slide 2** — Des tutos. Des astuces. Des comparatifs.

**Slide 3** — Mais rien n'était relié.

**Slide 4** — Le problème n'était pas la qualité. C'était l'absence de structure.

**Slide 5 — Insight** — Le contenu isolé fatigue. Le contenu structuré construit.

**Slide 6 — Méthode schoolsWP**

- 3 piliers
- 1 cocon sémantique
- 1 funnel
- 1 offre reliée

**Slide 7** — Chaque contenu doit renforcer un actif.

**Slide 8 — CTA** — Tu veux voir comment je structure ça ? Écris "CSOA".

---

### Carrousel 4 — "Si je pouvais parler au moi d'il y a 3 ans…"

**Slide 1** — Si je pouvais parler au moi d'il y a 3 ans, je lui dirais une chose.

**Slide 2** — Arrête de chercher la perfection technique.

**Slide 3** — Cherche la cohérence stratégique.

**Slide 4** — Un site performant n'est pas complexe. Il est intentionnel.

**Slide 5 — Framework**
Avant chaque contenu, demande-toi :

- Pour qui ?
- Pourquoi ?
- Vers quoi je l'oriente ?

**Slide 6** — Sans direction → pas de conversion.

**Slide 7** — La stratégie précède le design.

**Slide 8 — CTA** — Je partage souvent ce type de frameworks ici.

---

### Carrousel 5 — "Je pensais que le problème venait du design…"

**Slide 1** — Je pensais que le problème venait du design.

**Slide 2** — Je changeais les couleurs. Les blocs. Les animations.

**Slide 3** — Mais les ventes ne bougeaient pas.

**Slide 4** — Le vrai problème ? Aucune offre claire.

**Slide 5** — Un beau site sans promesse forte = vitrine vide.

**Slide 6 — Insight**
Ce qui vend, c'est :

- La clarté
- La structure
- La progression

**Slide 7** — Le design amplifie. Il ne sauve pas.

**Slide 8 — CTA** — Si ton site stagne, le problème n'est peut-être pas là où tu crois.

---

### Signature visuelle schoolsWP — Carrousels

| Élément        | Règle                                            |
| -------------- | ------------------------------------------------ |
| Fond           | Clair, minimal — jamais chargé                   |
| Titres         | Forts, 1 phrase max par slide                    |
| Densité        | 1 idée par slide — jamais plus                   |
| Longueur ligne | Max 10 mots par ligne                            |
| Frameworks     | Bullet points, pas de paragraphes                |
| CTA            | Discret — mot-clé en DM ou question ouverte      |
| Slides idéales | 6–10 slides — jamais moins de 6, rarement plus   |
| Première slide | Hook seul — rien d'autre, pas de titre de marque |

---

## 10 Hooks Storytelling Optimisés pour Déclencher des DM

> Mécanique : tension narrative → révélation partielle → mot-clé DM. Pas de vente directe — invitation personnalisée.

---

**1 — "SYSTÈME"**

Au début, je pensais que WordPress, c'était juste installer des thèmes et des plugins.
J'avais totalement tort.

Le vrai levier n'est pas technique.

Si tu veux que je te montre ce qui change vraiment la donne, écris-moi "SYSTÈME" en DM.

---

**2 — "SEO"**

J'ai passé des mois à optimiser mon SEO…

Et zéro impact sur mes revenus.

Ce que j'ai corrigé ensuite a tout changé.

Si tu veux le détail du switch, envoie "SEO" en message privé.

---

**3 — "FUNNEL"**

Le jour où j'ai compris que mon site ne vendait pas, j'ai arrêté de chercher plus de trafic.

J'ai changé une seule chose.

Si tu veux que je t'explique laquelle, DM "FUNNEL".

---

**4 — "DIAGNOSTIC"**

Un client m'a dit : "J'ai du trafic, mais je ne comprends pas pourquoi je ne vends rien."

Ce n'était pas un problème de visiteurs.

Si tu veux que je t'explique l'erreur classique, écris "DIAGNOSTIC".

---

**5 — "CHECKLIST"**

Si je devais relancer un site WordPress aujourd'hui, je ne commencerais pas par le design.

Je commencerais par autre chose.

Si tu veux la checklist exacte, envoie "CHECKLIST".

---

**6 — "STRATÉGIE"**

Pendant longtemps, j'ai publié du contenu comme tout le monde.

Beaucoup de vues. Peu de clients.

Le problème n'était pas le contenu.

Si tu veux comprendre pourquoi, DM "STRATÉGIE".

---

**7 — "AUDIT"**

J'ai analysé mon propre site comme si c'était celui d'un client.

Verdict : pas assez orienté conversion.

Si tu veux la grille d'analyse que j'utilise, écris "AUDIT".

---

**8 — "PARCOURS"**

Personne ne m'avait expliqué que le trafic froid ne convertit presque jamais.

Il faut le guider.

Si tu veux que je te montre comment, envoie "PARCOURS".

---

**9 — "POSITIONNEMENT"**

Je pensais que le problème venait du plugin.

En réalité, c'était l'absence de positionnement clair.

Si tu veux travailler ça sur ton site, DM "POSITIONNEMENT".

---

**10 — "AUTO"**

Si ton site dépend de toi chaque jour, ce n'est pas un système.

C'est un job.

Si tu veux automatiser intelligemment ton WordPress, écris "AUTO".

---

### Tableau des mots-clés DM

| Mot-clé        | Sujet abordé en DM                              |
| -------------- | ----------------------------------------------- |
| SYSTÈME        | Architecture stratégique du site WordPress      |
| SEO            | Passage du trafic SEO à la conversion réelle    |
| FUNNEL         | Structure funnel minimal qui convertit          |
| DIAGNOSTIC     | Audit rapide du site (pourquoi ça ne vend pas)  |
| CHECKLIST      | Checklist de relance / lancement site WordPress |
| STRATÉGIE      | Système de contenu structuré vs contenu isolé   |
| AUDIT          | Grille d'analyse conversion / architecture      |
| PARCOURS       | Structuration du parcours visiteur → client     |
| POSITIONNEMENT | Clarté de l'offre et ciblage                    |
| AUTO           | Automatisation WordPress (FluentCRM / n8n)      |

### Règles des hooks DM à mot-clé

- **Mot-clé court** (1 mot, majuscules) : action minimale, friction nulle
- **Honorer chaque DM** : répondre dans les 6h max — la réactivité amplifie la confiance
- **Préparer la réponse en avance** : template DM prêt par mot-clé
- **Pas de lien en réponse DM** : d'abord une question, puis la valeur, puis l'offre si pertinent
- **Fréquence** : max 1 post avec mot-clé DM tous les 5 posts — rareté = désirabilité

---

## 10 Hooks Polarisants Optimisés pour DM

> Structure : accroche polarisante → micro-leçon → question ciblée → CTA conversationnel mot-clé.

---

**1 — "SYSTÈME"**

J'ai cru que WordPress, c'était "technique".
En réalité, c'est surtout un marché rempli de gens qui font du bruit… sans résultats.

La différence ? Une structure business derrière le site.

Tu as une vraie stratégie derrière ton WordPress… ou juste du contenu ?
Écris-moi "SYSTÈME" en DM, je te montre comment je structure ça.

---

**2 — "FUNNEL"**

Le jour où j'ai compris que mon site ne vendait pas, j'ai arrêté de "créer du contenu".
J'ai commencé à construire un système.

Un site qui informe ≠ un site qui transforme.

Ton site guide vraiment vers une décision ?
Si tu veux un diagnostic rapide, envoie-moi "FUNNEL" en message privé.

---

**3 — "SEO"**

J'ai passé des mois à optimiser mon SEO.
Le problème ? Je n'avais rien à vendre correctement derrière.

Le trafic sans intention claire = ego boost, pas business.

Tu sais exactement ce que ton trafic doit faire ?
Je peux t'expliquer comment relier SEO → offre. DM "SEO".

---

**4 — "CLARTÉ"**

"Ton site est beau… mais je ne comprends pas ce que tu veux que je fasse."
Cette phrase m'a fait revoir toute ma structure.

Clarté > Design.

Si un visiteur arrive sur ton site aujourd'hui, sait-il quoi faire en 5 secondes ?
Écris-moi "CLARTÉ" si tu veux que je t'explique ma méthode.

---

**5 — "STACK"**

Je pensais qu'un bon plugin pouvait compenser une stratégie absente.
Spoiler : non.

Un outil amplifie. Il ne sauve pas.

Tu choisis tes plugins par effet de mode ou par logique business ?
DM "STACK" si tu veux voir la mienne.

---

**6 — "VISION"**

La plupart des conseils WordPress oublient l'objectif business.

Installer n'est pas structurer.

Ton site est-il pensé pour vendre, qualifier ou juste exister ?
Si tu veux un angle plus stratégique, écris-moi "VISION".

---

**7 — "MACHINE"**

J'ai publié pendant des mois.
J'ai construit une bibliothèque… pas une machine.

Publier n'est pas convertir.

Ton contenu mène quelque part ?
Si tu veux comprendre la différence, DM "MACHINE".

---

**8 — "AUDIT"**

J'ai audité mon propre site.
J'ai trouvé exactement les erreurs que je critique chez les autres.

Le problème n'est pas technique. Il est structurel.

Tu as déjà audité ton site comme un business, pas comme un designer ?
Écris "AUDIT" en DM si tu veux le framework.

---

**9 — "POSITIONNEMENT"**

Si je pouvais parler au moi d'il y a 3 ans :
"Assume une niche. Construis un parcours."

La spécialisation crée l'autorité.

Tu es clair sur ton positionnement aujourd'hui ?
Si tu hésites encore, DM "POSITIONNEMENT".

---

**10 — "CONVERSION"**

Je pensais que mon problème venait du design.
En réalité, j'avais peur de vendre.

Beaucoup se cachent derrière du contenu "utile".

Ton site vend-il vraiment, ou est-il confortable ?
Si tu veux structurer une vraie logique de conversion, écris "CONVERSION".

---

### Phrases "couteau" — Amplificateurs de tension

Ajouter l'une de ces phrases juste après le hook pour renforcer la prise de position :

- "Et c'est pour ça que 90% des sites ne décollent jamais."
- "C'est dur à entendre, mais c'est la vérité."
- "Si tu fais ça, tu perds du temps."
- "Si tu veux des résultats, il faut arrêter de jouer."
- "Le confort tue plus de projets WordPress que la technique."

### Tableau des mots-clés DM (version polarisante)

| Mot-clé        | Sujet abordé                                 |
| -------------- | -------------------------------------------- |
| SYSTÈME        | Architecture stratégique WordPress           |
| FUNNEL         | Diagnostic site → conversion                 |
| SEO            | Liaison SEO / offre                          |
| CLARTÉ         | Méthode clarté de parcours visiteur          |
| STACK          | Stack plugins raisonnée par logique business |
| VISION         | Positionnement stratégique du site           |
| MACHINE        | Système de contenu qui convertit             |
| AUDIT          | Framework d'audit business du site           |
| POSITIONNEMENT | Niche + parcours + autorité                  |
| CONVERSION     | Structure de conversion WordPress            |

---

## 5 Posts Complets Version DM Optimisée

> Structure : Hook polarisant → leçon condensée → CTA mot-clé. Objectif : déclencher des DM qualifiés, identifier les prospects chauds, alimenter consulting/formation.

---

### Post 1 — "SCHÉMA"

J'ai passé des mois à optimiser mon SEO.
Le problème ? Je n'avais rien à vendre correctement derrière.

Je publiais régulièrement.
Je travaillais mes mots-clés.
Je regardais mes positions monter.

Mais quand quelqu'un arrivait sur le site…
Il n'y avait aucun chemin clair.

Pas d'offre structurée.
Pas de séquence email.
Pas de progression logique.

Du trafic.
Pas de système.

**Le SEO amplifie ce que tu as déjà. Si ton offre est floue, il amplifie… le flou.**

Si tu veux, je peux t'envoyer le schéma simple que j'utilise pour relier SEO → offre → email → vente.

Écris-moi "SCHÉMA" en commentaire ou en DM.

---

### Post 2 — "LIEN"

"Ton site est beau… mais je ne comprends pas ce que tu veux que je fasse."

Ça pique.

Parce qu'on pense que le design suffit.
Qu'un site "propre" inspire confiance.

Mais un site n'est pas une galerie.
C'est un parcours.

Si l'utilisateur ne comprend pas quelle est l'étape suivante, il part.

**Un site performant = une action principale claire. Tout le reste est secondaire.**

Si tu veux, envoie-moi le lien de ton site en DM.
Je te dirai en 2 phrases ce que je comprends… et ce qui bloque.

---

### Post 3 — "MACHINE"

Pendant longtemps, j'ai publié du contenu comme tout le monde.
Résultat : j'ai construit une bibliothèque. Pas une machine.

Articles isolés.
Tutos techniques.
Comparatifs.

Chaque contenu était "utile".
Mais aucun ne menait quelque part.

Pas de logique de progression.
Pas de cluster.
Pas de funnel.

**Un contenu isolé attire. Un système convertit. La différence : le maillage + l'intention business.**

Je peux te partager la checklist "Site Machine vs Site Bibliothèque".

Commente "MACHINE" ou écris-moi en privé.

---

### Post 4 — "OFFRE"

Je pensais que mon problème venait du design.
En réalité, j'avais juste peur de vendre.

C'est confortable d'optimiser les couleurs.
Les animations.
Les micro-détails.

Ça donne l'impression d'avancer.

Mais ça évite le vrai sujet :
Clarifier son offre. Assumer son positionnement. Demander une action.

**Le design rassure. La structure convertit.**

Si tu veux, je peux te montrer la structure minimale que j'utilise pour clarifier une offre en 15 minutes.

Écris "OFFRE" en commentaire.

---

### Post 5 — "RESET"

Si je relançais un site WordPress aujourd'hui, je commencerais par l'offre. Pas par le thème.

Avant, je commençais par : le thème, les plugins, le SEO.
Aujourd'hui, je commencerais par : l'offre, le parcours, la segmentation, l'automatisation — puis seulement le contenu.

Parce qu'un site n'est pas un projet créatif.
C'est un actif.

**WordPress devient puissant quand il est pensé comme un système. Pas comme un site.**

Je prépare un mini guide "Relancer son site en 5 étapes".
Si tu le veux, écris "RESET".

---

### Niveau supérieur — Escalade de la conversation DM

| Étape | Action                                                             | Quand l'utiliser                    |
| ----- | ------------------------------------------------------------------ | ----------------------------------- |
| 1     | Envoi du contenu promis (schéma, checklist…)                       | Immédiatement après le DM           |
| 2     | Question de qualification ("tu es à quelle étape de ton projet ?") | Après l'envoi du contenu            |
| 3     | Mini audit express ("je peux regarder ton site ?")                 | Si prospect semble chaud            |
| 4     | Score rapide ("ton site est à combien /10 ?")                      | Pour créer engagement + curiosité   |
| 5     | Invitation douce call stratégique                                  | Uniquement si besoin réel identifié |

**Règle d'or** : jamais de lien vers une offre payante avant l'étape 3 minimum.

---

## CTA Stratégiques — Newsletter et Consulting

> Objectif : chaque post se termine par une action mesurable. Un mot-clé simple, une promesse claire, une transition vers email ou RDV.

---

### Post 1 — SEO → Newsletter

CTA version newsletter :

Je prépare un guide complet sur "SEO WordPress orienté conversion".
Si tu veux que je te l'envoie quand il sort, écris "SEO" en commentaire.

---

### Post 2 — Structure site → Audit consulting

CTA version consulting :

Si tu veux que je regarde ton site et que je t'indique l'action prioritaire à corriger,
envoie-moi "SITE" en DM.

---

### Post 3 — Bibliothèque vs Machine → Newsletter premium

CTA version standard :

J'ai structuré le modèle exact que j'utilise pour transformer un site en "machine".
Je peux l'envoyer à ceux qui veulent. Commente "MACHINE".

CTA version premium :

Je le partage uniquement avec les abonnés newsletter. [Lien inscription en commentaire]

---

### Post 4 — Design vs Stratégie → Diagnostic court

CTA version expert :

Si tu hésites entre "améliorer ton design" ou "repenser ta stratégie",
écris-moi "STRATÉGIE".
Je te donne mon avis honnête.

---

### Post 5 — Repartir de zéro → Lead magnet

CTA version lead magnet :

J'ai créé une checklist "Repartir de zéro avec WordPress (version business)".
Si tu la veux, commente "ZERO".

CTA version consulting :

Si tu es freelance WP et que tu veux structurer ton système,
on peut en parler en message privé.

---

### Règles CTA Stratégique schoolsWP

| Règle             | Détail                                                   |
| ----------------- | -------------------------------------------------------- |
| Mot-clé simple    | 1 mot, majuscules, facile à taper même depuis mobile     |
| Promesse claire   | Ce que la personne reçoit — aucune ambiguïté             |
| Valeur perçue     | Contenu, diagnostic, checklist — pas juste "on en parle" |
| Transition fluide | Newsletter OU RDV — jamais les deux dans le même CTA     |

---

### Système derrière les CTA (LinkedIn → Pré-Funnel)

Quand quelqu'un commente un mot-clé :

1. **Réponse publique courte** ("Super, je t'envoie ça en DM !") — visibilité algorithm
2. **DM personnalisé** — envoi du contenu promis immédiatement
3. **Proposition newsletter** ou lien audit selon le profil
4. **Tag CRM FluentCRM** selon l'intérêt (SEO / Funnel / Consulting / Automatisation)

LinkedIn devient alors un pré-funnel qualifié — les DM entrants sont plus chauds qu'un trafic froid.

### Tableau des mots-clés CTA actifs

| Mot-clé   | Promesse                                    | Destination finale        |
| --------- | ------------------------------------------- | ------------------------- |
| SEO       | Guide "SEO WordPress orienté conversion"    | Newsletter                |
| SITE      | Analyse priorité n°1 à corriger             | Audit consulting (payant) |
| MACHINE   | Modèle "Site Machine"                       | Newsletter ou lead magnet |
| STRATÉGIE | Avis honnête design vs stratégie            | Conversation → consulting |
| ZERO      | Checklist "Repartir de zéro en version biz" | Lead magnet → nurturing   |
| SCHÉMA    | Schéma SEO → offre → email → vente          | Newsletter                |
| OFFRE     | Structure clarification offre en 15 min     | Call ou consulting        |
| RESET     | Mini guide "Relancer son site en 5 étapes"  | Lead magnet               |

---

## 10 posts complets prêts à publier (hook + développement + CTA)

Structure systématique : hook fort → développement structuré → CTA subtil.
Ton : direct, business, zéro blabla.

---

### POST 1 — SEO ≠ Trafic

**Hook :**
Le SEO WordPress ne sert pas à générer du trafic. Il sert à générer des décisions.

**Développement :**
La plupart des sites visent des mots-clés larges.
Ils attirent du monde.
Mais ils ne guident personne.

Un bon contenu SEO doit :

- Répondre à une intention précise
- Éduquer
- Orienter vers une action claire

Sinon, tu construis une audience qui lit… et repart.

Le SEO n'est pas une course au volume.
C'est une architecture stratégique.

**CTA :**
Si tu veux que je détaille comment structurer un vrai cocon orienté conversion, dis-le en commentaire.

---

### POST 2 — Le mythe du "beau site"

**Hook :**
Un site WordPress "premium" peut convertir moins qu'un site simple.

**Développement :**
Beaucoup de freelances optimisent :

- Le design
- Les animations
- Les micro-détails

Mais pas le parcours.

Un bon site :
→ Une page = une action
→ Un message = une promesse
→ Un chemin = une progression

La conversion vient de la clarté. Pas du wow effect.

**CTA :**
Tu veux que je partage la structure minimale d'un site qui vend ?

---

### POST 3 — Funnel invisible

**Hook :**
Un site sans funnel est juste une carte de visite.

**Développement :**
Tu as :

- Une page d'accueil
- Une page services
- Un blog

Mais après ?

Qui capture l'email ?
Qui qualifie ?
Qui relance ?
Qui propose l'offre suivante ?

Un funnel WordPress simple :

1. Contenu ciblé
2. Lead magnet
3. Email nurturing
4. Offre adaptée

Rien de compliqué. Mais structuré.

**CTA :**
Si tu veux le framework exact en 5 étapes, je peux le publier.

---

### POST 4 — Erreur freelance WP

**Hook :**
90% des freelances WordPress vendent du temps. Pas un système.

**Développement :**
Créer un site pour un client, c'est bien.
Créer un actif pour lui, c'est différent.

La vraie valeur :

- SEO structuré
- Funnel intégré
- CRM connecté
- Mesure du ROI

Sinon, tu restes exécutant. Pas partenaire stratégique.

**CTA :**
Tu es freelance WP ? Dis-moi si tu veux que je détaille ce modèle "site → actif".

---

### POST 5 — Affiliation mal comprise

**Hook :**
L'affiliation WordPress n'est pas un revenu passif. C'est un revenu stratégique.

**Développement :**
Mettre un lien affilié dans un article ne suffit pas.

Il faut :

- Un problème précis
- Un comparatif clair
- Une recommandation assumée
- Un contexte business

L'affiliation fonctionne quand elle renforce ton autorité.
Pas quand elle l'affaiblit.

**CTA :**
Je peux partager ma méthode pour intégrer l'affiliation sans perdre en crédibilité.

---

### POST 6 — Le faux problème

**Hook :**
Tu n'as pas un problème de trafic. Tu as un problème de direction.

**Développement :**
Plus de visiteurs ne résout rien si :

- Ton message est flou
- Ton offre est mal positionnée
- Ton parcours est incohérent

Le trafic amplifie. Il ne corrige pas.

Commence par clarifier :
→ À qui tu parles
→ Quel problème tu résous
→ Quelle action tu veux provoquer

Ensuite seulement, scale.

**CTA :**
Tu veux que je partage un audit simplifié pour tester ton site ?

---

### POST 7 — L'automatisation mal utilisée

**Hook :**
Automatiser un mauvais système ne le rend pas meilleur.

**Développement :**
Beaucoup installent :

- CRM
- Automations
- Séquences email

Mais sans stratégie claire.

L'automatisation doit servir :

- Une segmentation
- Un parcours
- Une montée en maturité

Sinon, c'est juste du bruit automatisé.

**CTA :**
Je peux détailler l'architecture simple que j'utilise sur WordPress.

---

### POST 8 — Positionnement fort

**Hook :**
La majorité des blogs WordPress en France sont techniquement corrects. Stratégiquement faibles.

**Développement :**
Ils expliquent "comment faire".
Rarement "pourquoi le faire".
Encore moins "dans quel ordre".

Un site performant repose sur :

- Une vision
- Une hiérarchie
- Une logique business

WordPress est un outil. La stratégie fait la différence.

**CTA :**
Si tu veux voir comment structurer ça proprement, je peux le détailler.

---

### POST 9 — Si je repartais de zéro

**Hook :**
Si je devais relancer un site WordPress aujourd'hui, je ferais 3 choses.

**Développement :**

1. Définir une offre claire
2. Construire un funnel simple
3. Créer 10 contenus ultra ciblés

Pas 50 articles génériques.
Pas 12 plugins inutiles.
Pas un design complexe.

Clarté > Complexité.

**CTA :**
Tu veux que je détaille ces 3 étapes ?

---

### POST 10 — Vision long terme

**Hook :**
Dans 3 ans, il restera deux types de créateurs WordPress.

**Développement :**
Ceux qui font des tutos.
Et ceux qui construisent des actifs.

Les actifs :

- Cocon SEO
- Email list
- Offres structurées
- Autorité personnelle

WordPress n'est pas le centre. Le système l'est.

**CTA :**
Tu construis quoi aujourd'hui ? Un site ou un actif ?

---

### Tableau récapitulatif — 10 posts

| #   | Thème                       | Hook central                                     | CTA déclencheur              |
| --- | --------------------------- | ------------------------------------------------ | ---------------------------- |
| 1   | SEO ≠ Trafic                | SEO sert à générer des décisions                 | Cocon orienté conversion     |
| 2   | Mythe du beau site          | Premium peut convertir moins que simple          | Structure minimale qui vend  |
| 3   | Funnel invisible            | Site sans funnel = carte de visite               | Framework 5 étapes           |
| 4   | Erreur freelance            | 90% vendent du temps, pas un système             | Modèle "site → actif"        |
| 5   | Affiliation mal comprise    | Revenu stratégique, pas passif                   | Méthode affiliation + crédit |
| 6   | Faux problème trafic        | Pas un problème de trafic, de direction          | Audit simplifié              |
| 7   | Automatisation mal utilisée | Automatiser un mauvais système ne l'améliore pas | Architecture WordPress       |
| 8   | Positionnement fort         | Techniquement correct, stratégiquement faible    | Structuration détaillée      |
| 9   | Repartir de zéro            | 3 choses seulement                               | Détail des 3 étapes          |
| 10  | Vision long terme           | 2 types de créateurs dans 3 ans                  | Site ou actif ?              |

### Règles d'utilisation

- Publier 2 posts / semaine max — laisser les commentaires respirer
- Répondre à chaque commentaire dans les 2h pour l'algorithme
- Chaque CTA ouvre une conversation, pas un lien direct
- Suivre qui interagit → amorcer le système DM

---

## Système DM → RDV Consulting (pipeline complet)

Pipeline reproductible : Post → DM → Qualification → RDV → Offre.

---

### Étape 1 — Post déclencheur

Chaque post contient un CTA qui ouvre la conversation sans pitcher.

**Formulations efficaces :**

- "Je peux partager le framework en détail."
- "Dis-moi si tu veux le modèle."
- "Je peux t'envoyer la checklist."
- "Je peux auditer ton site."

But : provoquer un commentaire ou un DM naturel.

---

### Étape 2 — DM 1 : Ouverture naturelle

Déclencher après commentaire ou interactions répétées :

> Merci pour ton message 🙌
> Par curiosité, tu utilises WordPress pour quoi aujourd'hui ? (site vitrine, freelance, formation, autre ?)

But : obtenir le contexte, qualifier sans forcer.

---

### Étape 3 — DM 2 : Qualification stratégique

Selon la réponse reçue :

> Intéressant.
> Tu as déjà structuré un système (SEO + capture email + offre claire) ou c'est encore en construction ?

Identifier le profil :

- Débutant
- Freelance
- Business établi
- Agence

---

### Étape 4 — DM 3 : Micro-diagnostic

Reformuler le blocage identifié :

> De ce que tu me dis, le point clé semble être [résumer son blocage].
> La plupart des sites perdent énormément d'opportunités à ce niveau.

But : créer une prise de conscience. Montrer l'expertise sans vendre.

---

### Étape 5 — DM 4 : Micro-valeur avant RDV

Toujours donner de la valeur avant de proposer :

> Si je devais te donner un conseil rapide : clarifie ton offre principale et relie chaque page à une action unique.

Puis, seulement si besoin réel identifié :

> Si tu veux, on peut prendre 20 minutes.
> Je regarde ton site et je te dis exactement où sont les leviers prioritaires.

Clair. Simple. Sans pression.

---

### Framework d'audit express (20 min)

Structure du call de qualification :

**1. Clarifier l'objectif (5 min)**

- CA cible ?
- Type de client ?
- Offre principale ?

**2. Analyse rapide du site (7 min)**

- Proposition de valeur claire ?
- Appel à l'action unique par page ?
- Capture email présente ?
- Parcours logique ?
- Offre visible ?

**3. Opportunités manquées (5 min)**
Formuler en opportunité :

> "Si tu structures X, tu peux probablement doubler Y."

**4. Transition offre (3 min)**

> "Si tu veux qu'on le mette en place ensemble, voilà comment je fonctionne."

---

### Funnel complet LinkedIn → RDV

| Étape | Action                     | Contenu                                      |
| ----- | -------------------------- | -------------------------------------------- |
| A     | Post stratégique           | CTA ouverture conversation                   |
| B     | Lead magnet (optionnel)    | Checklist SEO / Template funnel / Audit PDF  |
| C     | Email nurturing (3 emails) | Diagnostic → Erreur fréquente → Étude de cas |
| D     | RDV call                   | Audit express → Offre → Suivi CRM            |

**Séquence email nurturing (3 emails) :**

- Email 1 : Diagnostic courant → problème récurrent identifié
- Email 2 : Erreur fréquente → ce que la plupart font mal
- Email 3 : Étude de cas → résultat concret → "Si tu veux un audit personnalisé…"

---

### Offre consulting premium — Structure

**Positionnement :**
Pas "création de site".
Mais : architecture stratégique WordPress orientée croissance.

**Option A — Audit stratégique (ticket d'entrée)**

- 297€ – 597€
- Audit complet site + parcours
- Plan d'action priorisé

**Option B — Accompagnement structuration (milieu de gamme)**

- 1 500€ – 3 000€
- Refonte parcours + funnel + SEO + automatisation

**Option C — Partenaire stratégique (haut de gamme)**

- 800€ – 2 000€ / mois
- Suivi mensuel + optimisation continue + CRO + SEO

---

### Système d'automatisation post-call

1. Ajouter au CRM FluentCRM
2. Tag : `LinkedIn_Consulting`
3. Séquence email personnalisée selon profil
4. Relance J+3 si pas de réponse

---

### Projection réaliste

| Activité                    | Volume          |
| --------------------------- | --------------- |
| Posts publiés               | 2 / semaine     |
| Conversations actives       | 5 à 10          |
| RDV générés                 | 3 à 5 / semaine |
| Taux closing estimé         | 25 – 40%        |
| **Clients / mois possible** | **2 à 4**       |

Sans prospection agressive.

### Règles d'or du système DM

**Ne jamais :**

- Pitcher trop tôt
- Envoyer un lien Calendly en premier message
- Être générique dans les DM

**Toujours :**

- Diagnostiquer avant de proposer
- Apporter une micro-clarté
- Créer un déclic avant toute offre

---

## 5 carrousels signature schoolsWP

Structure systématique : 9 slides — Hook → Pédagogie → Framework → Punchline → CTA conversationnel.
Format : minimaliste, clair, business-first.

---

### CARROUSEL 1 — SEO sans funnel = inutile

**Slide 1** — Tu fais du SEO… mais tu ne vends pas ?

**Slide 2** — Beaucoup optimisent :

- Les mots-clés
- Les balises
- La vitesse
- Le score SEO

**Slide 3** — Mais ils oublient une chose essentielle :
→ Ce qui se passe APRÈS le clic.

**Slide 4** — Du trafic sans structure = Du bruit.

**Slide 5** — Un SEO efficace doit mener vers :

- Une offre
- Un lead magnet
- Une décision

**Slide 6** — Sinon ? Tu construis une audience… Pour quelqu'un d'autre.

**Slide 7** _(framework)_ — Le modèle simple :
`Trafic → Capture → Nurturing → Conversion`
Pas l'inverse.

**Slide 8** _(punchline)_ — Le SEO n'est pas une fin. C'est un amplificateur.

**Slide 9** _(CTA)_ — Tu as un vrai chemin après ton trafic ? Dis-moi "SEO" en commentaire.

---

### CARROUSEL 2 — Le site "beau" qui ne convertit pas

**Slide 1** — "Ton site est beau… mais je ne comprends pas quoi faire."

**Slide 2** — Ça pique. Mais c'est la phrase la plus honnête qu'on puisse te dire.

**Slide 3** — Un site n'est pas une galerie. C'est un parcours.

**Slide 4** — Chaque page doit répondre à une question :
→ Quelle action veux-tu déclencher ?

**Slide 5** — Erreur fréquente :

- Trop d'options
- Trop de messages
- Trop de dispersion

**Slide 6** — Clarté > Esthétique. Toujours.

**Slide 7** _(framework)_ — Règle simple :
`1 page = 1 objectif = 1 CTA dominant`

**Slide 8** _(punchline)_ — Un site joli rassure. Un site structuré vend.

**Slide 9** _(CTA)_ — Si tu devais définir l'action principale de ton site en une phrase, ce serait quoi ?

---

### CARROUSEL 3 — Bibliothèque vs Machine

**Slide 1** — Tu construis une bibliothèque… ou une machine ?

**Slide 2** — Publier du contenu, c'est facile. Structurer un système, c'est stratégique.

**Slide 3** — Une bibliothèque :

- Articles isolés
- Pas de lien logique
- Pas de progression

**Slide 4** — Une machine :

- Cocon sémantique
- Maillage interne
- Funnel intégré

**Slide 5** — La différence ? L'intention business.

**Slide 6** — Un contenu isolé attire. Un système convertit.

**Slide 7** _(framework)_ — Modèle schoolsWP :
`Pillar → Cluster → Capture → Séquence → Offre`

**Slide 8** _(punchline)_ — Le contenu est un actif. S'il est relié.

**Slide 9** _(CTA)_ — Ton contenu mène vers quoi exactement ?

---

### CARROUSEL 4 — Design vs Stratégie

**Slide 1** — Tu optimises le design… Mais évites-tu la stratégie ?

**Slide 2** — Changer les couleurs / Modifier les animations / Tester 3 thèmes

**Slide 3** — Ça donne l'impression d'avancer.

**Slide 4** — Mais le vrai travail est ailleurs :

- Positionnement
- Offre
- Promesse
- Parcours

**Slide 5** — Un beau site sans stratégie = Un hobby.

**Slide 6** — Un site simple + clair = Un levier.

**Slide 7** _(framework)_ — Commence toujours par :
`Offre → Parcours → Message → Design`

**Slide 8** _(punchline)_ — Le design rassure. La structure convertit.

**Slide 9** _(CTA)_ — Tu bosses sur quoi en ce moment ?

---

### CARROUSEL 5 — Repartir de zéro

**Slide 1** — Si je relançais un site WordPress demain…

**Slide 2** — Je ne commencerais pas par le thème.

**Slide 3** — Je commencerais par :

1. L'offre
2. La cible
3. Le problème précis

**Slide 4** — Puis : 4. Le parcours 5. La capture 6. L'automatisation

**Slide 5** — Et seulement ensuite : Le contenu.

**Slide 6** — Pourquoi ? Parce qu'un site n'est pas créatif. C'est stratégique.

**Slide 7** _(framework)_ — WordPress devient puissant quand il devient un écosystème.

**Slide 8** _(punchline)_ — Sinon, c'est juste un site.

**Slide 9** _(CTA)_ — Si tu repartais de zéro, tu changerais quoi ?

---

### Tableau récapitulatif — 5 carrousels

| #   | Titre                             | Angle central                | Mot-clé CTA |
| --- | --------------------------------- | ---------------------------- | ----------- |
| 1   | SEO sans funnel = inutile         | SEO → structure → conversion | SEO         |
| 2   | Le site beau qui ne convertit pas | Clarté > esthétique          | Parcours    |
| 3   | Bibliothèque vs Machine           | Contenu isolé vs système     | MACHINE     |
| 4   | Design vs Stratégie               | Design secondaire            | STRATÉGIE   |
| 5   | Repartir de zéro                  | Méthode > outil              | ZERO        |

### Règles carrousels signature schoolsWP

- Slide 1 = hook choc (question ou affirmation décalée)
- Slides 2-6 = pédagogie progressive, une idée par slide
- Slide 7 = framework visuel simple (schéma texte ou liste numérotée)
- Slide 8 = punchline courte et mémorable
- Slide 9 = CTA avec mot-clé DM
- Typographie : Nunito Sans titres, Roboto corps — couleur accent `#E668D4` sur slide 1
- Fond : blanc ou `#00D400` pour slides framework

---

## Série LinkedIn 30 jours — "WordPress Business"

Programme de montée en puissance : autorité, DM qualifiés, newsletter, consulting.
Rythme : 3-4 posts / semaine sur 30 jours.
Angle fil rouge : WordPress comme système business, pas comme outil.

---

### Semaine 1 — Réveil stratégique

Objectif : casser les croyances de base.

| Jour | Hook                                                               | Angle                 |
| ---- | ------------------------------------------------------------------ | --------------------- |
| J1   | WordPress n'est pas un outil. C'est un levier de croissance.       | Changement perception |
| J2   | 90% des sites WordPress sont mal positionnés.                      | Clarté offre          |
| J3   | Ton site ne manque pas de trafic. Il manque de direction.          | Funnel                |
| J4   | Si ton site ne capture pas un email, il ne travaille pas pour toi. | Base système          |

---

### Semaine 2 — Structure & Méthode

Objectif : introduire le framework schoolsWP.

| Jour | Sujet                                                  | Format         |
| ---- | ------------------------------------------------------ | -------------- |
| J5   | La différence entre un blog et un actif business.      | Post           |
| J6   | Modèle : Pillar → Cluster → Capture → Séquence → Offre | Carrousel      |
| J7   | Pourquoi le design est secondaire.                     | Post           |
| J8   | Le framework WordPress Business en 5 étapes.           | Post/Carrousel |

---

### Semaine 3 — Autorité & Profondeur

Objectif : installer la crédibilité.

| Jour | Sujet                                                        | Angle          |
| ---- | ------------------------------------------------------------ | -------------- |
| J9   | J'ai audité X sites WordPress. Les mêmes erreurs reviennent. | Preuve sociale |
| J10  | Le SEO sans funnel est inutile.                              | Expertise      |
| J11  | L'affiliation bien faite peut battre le consulting.          | Opinion forte  |
| J12  | Le vrai pouvoir de WordPress ? L'intégration.                | Vision         |

---

### Semaine 4 — Domination thématique

Objectif : saturer 3 thèmes clés.

| Jour | Thème                             | Format    |
| ---- | --------------------------------- | --------- |
| J13  | SEO WordPress stratégique         | Post      |
| J14  | Funnel WordPress simplifié        | Carrousel |
| J15  | Automatisation CRM WordPress      | Post      |
| J16  | Monétiser son site intelligemment | Post      |

---

### Semaine 5 — Coulisses & Transparence

Objectif : humaniser + renforcer la crédibilité.

| Jour | Sujet                                           | Angle        |
| ---- | ----------------------------------------------- | ------------ |
| J17  | Comment je structure schoolsWP.                 | Coulisses    |
| J18  | Ma stack WordPress actuelle.                    | Transparence |
| J19  | Ce que j'aurais fait différemment.              | Leçons       |
| J20  | Les erreurs que je vois chez les freelances WP. | Expertise    |

---

### Semaine 6 — Leader d'opinion

Objectif : devenir une voix de référence.

| Jour | Sujet                                                      | Ton        |
| ---- | ---------------------------------------------------------- | ---------- |
| J21  | Pourquoi le marché WordPress FR manque de vision business. | Polarisant |
| J22  | Le futur de WordPress avec l'IA.                           | Vision     |
| J23  | Le piège des micro-tutos.                                  | Opinion    |
| J24  | Pourquoi les freelances WP doivent penser "système".       | Conviction |

---

### Semaine 7 — Conversion stratégique

Objectif : transformer l'audience en leads newsletter et consulting.

| Jour | Sujet                                                              | CTA                            |
| ---- | ------------------------------------------------------------------ | ------------------------------ |
| J25  | Je prépare un guide WordPress Business                             | CTA newsletter                 |
| J26  | Étude de cas simplifiée                                            | CTA conversation               |
| J27  | Mini framework téléchargeable                                      | Lead magnet → newsletter       |
| J28  | Invitation discussion stratégique                                  | CTA consulting                 |
| J29  | Post synthèse : 30 jours de leçons                                 | Récap + engagement             |
| J30  | WordPress peut être un hobby. Ou un actif stratégique. Tu choisis. | CTA final newsletter / échange |

---

### Logique de progression — vue d'ensemble

| Phase      | Semaines | Objectif                 | Mécanisme           |
| ---------- | -------- | ------------------------ | ------------------- |
| Réveil     | S1       | Casser les croyances     | Hooks décalés       |
| Méthode    | S2       | Introduire le framework  | Posts + carrousels  |
| Expertise  | S3-S4    | Installer la crédibilité | Profondeur + thèmes |
| Humain     | S5       | Humaniser                | Coulisses           |
| Voix       | S6       | Leadership d'opinion     | Polarisation        |
| Conversion | S7       | Leads et DM              | CTAs ciblés         |

### Résultats attendus après 30 jours

- Positionnement clair sur WordPress Business
- 1 000 à 2 000 abonnés qualifiés
- DM entrants qualifiés
- Trafic newsletter en croissance
- Autorité installée sur LinkedIn FR WordPress

### Règles d'exécution série 30 jours

- Ne jamais pitcher une offre avant la semaine 7
- Répondre à chaque commentaire dans les 2h (signal algorithme)
- Chaque post avec mot-clé DM → déclenche la séquence DM scriptée
- Tracker : commentaires / impressions / DM entrants / abonnés newsletter
- Réutiliser les posts forts en carrousels la semaine suivante

---

## Série #WordPressBusiness — 30 posts rédigés

Série LinkedIn complète. Positionnement : WordPress = levier de croissance, pas un outil technique.
Structure type : Hook → 3-6 lignes courtes → framework / idée → leçon business → CTA conversationnel.

---

### POST 1 — 90% des sites ne génèrent rien

90% des sites WordPress ne génèrent aucun revenu.

Et ce n'est pas un problème technique.

C'est un problème d'intention.

La plupart des sites sont construits comme :

- une vitrine
- un portfolio
- un blog

Mais jamais comme un système.

Un site qui génère doit avoir :
→ une offre claire
→ un parcours logique
→ une capture email
→ une suite derrière

Sinon tu publies… pour le vide.

Un site WordPress est un actif.
Pas une décoration digitale.

Tu construis quoi aujourd'hui : une vitrine ou un levier ?

---

### POST 2 — Le trafic n'est pas le problème

Le problème n'est pas ton trafic.

C'est ce qu'il se passe après.

Tu peux avoir :

- 500 visiteurs
- 5 000 visiteurs
- 50 000 visiteurs

Si personne ne sait :
→ quoi faire
→ pourquoi agir
→ quelle est l'étape suivante

Tu n'as rien.

Le trafic sans structure = bruit.

La vraie question :
Combien de visiteurs passent à l'étape 2 ?

Tu connais ton taux de progression ?

---

### POST 3 — WordPress n'est pas un site

WordPress n'est pas un site.

C'est un système.

Un système relie :

- contenu
- capture
- email
- offre
- automatisation

Un site isolé attire.

Un système convertit.

Si ton WordPress dépend de toi chaque jour pour vendre,
ce n'est pas un actif.

C'est un job.

Ton site travaille pour toi… ou tu travailles pour lui ?

---

### POST 4 — Les freelances pensent projet

Les freelances WordPress pensent "projet".

Les stratèges pensent "actif".

Un projet :
→ livré
→ facturé
→ terminé

Un actif :
→ attire
→ qualifie
→ convertit
→ évolue

La vraie différence n'est pas technique.
Elle est mentale.

Tu construis des projets… ou un écosystème ?

---

### POST 5 — Le design ne sauvera rien

Le design ne sauvera jamais une mauvaise stratégie.

Oui, un beau site rassure.

Mais s'il ne dit pas :
→ pour qui
→ pour quoi
→ pourquoi maintenant

Il échoue.

Beaucoup optimisent :

- les couleurs
- les animations
- les détails

Très peu optimisent :

- l'offre
- le message
- le parcours

Le design habille.
La stratégie convertit.

Tu optimises quoi en ce moment ?

---

### POST 6 — Le cocon expliqué simplement

Le cocon sémantique n'est pas une technique SEO.

C'est une architecture de décision.

Chaque contenu doit :
→ répondre à une question
→ orienter vers une suivante
→ mener vers une offre

Un article isolé attire.

Un cluster dirige.

Si ton contenu ne mène nulle part,
il ne vaut que le trafic qu'il génère.

Ton contenu crée-t-il un parcours ?

---

### POST 7 — Transformer un article en actif

Un article peut être un actif.

Ou juste un post oublié.

Pour devenir un actif, il doit :

1. Cibler une intention claire
2. Diriger vers un lead magnet
3. Être relié à une séquence
4. Pointer vers une offre

Sinon, il ne fait qu'informer.

Informer ≠ transformer.

Combien de tes articles sont reliés à un système ?

---

### POST 8 — Les 3 pages indispensables

Ton site WordPress a besoin de 3 pages stratégiques.

1. Une page pilier (autorité SEO)
2. Une page capture (lead magnet clair)
3. Une page offre (positionnement net)

Beaucoup ont :

- 15 pages inutiles
- 0 structure

Moins de pages.
Plus d'intention.

Tu as ces 3 fondations ?

---

### POST 9 — SEO vs Funnel

SEO sans funnel = audience gratuite pour quelqu'un d'autre.

Funnel sans SEO = dépendance au trafic payant.

Les deux doivent fonctionner ensemble.

Le SEO attire.
Le funnel guide.
L'email convertit.
L'offre monétise.

Tout est relié.

Si tu devais noter ton système sur 10, il vaut combien ?

---

### POST 10 — Le maillage invisible

Le maillage interne est le levier invisible de WordPress.

La plupart publient des articles isolés.

Résultat :
Google ne comprend pas la hiérarchie.
Le lecteur ne comprend pas la progression.

Un bon maillage :
→ renforce l'autorité
→ augmente le temps passé
→ guide vers l'offre

C'est simple.

Mais peu le font stratégiquement.

Ton site est-il un réseau… ou une liste ?

---

### Tableau récapitulatif — 30 sujets série #WordPressBusiness

| #   | Titre                                    | Semaine | Objectif            |
| --- | ---------------------------------------- | ------- | ------------------- |
| 1   | 90% des sites ne génèrent rien           | S1      | Choc réalité        |
| 2   | Le trafic n'est pas le problème          | S1      | Choc réalité        |
| 3   | WordPress n'est pas un site              | S1      | Choc réalité        |
| 4   | Les freelances pensent projet            | S1      | Choc réalité        |
| 5   | Le design ne sauvera rien                | S1      | Choc réalité        |
| 6   | Le cocon expliqué simplement             | S2      | Expertise SEO       |
| 7   | Transformer un article en actif          | S2      | Expertise SEO       |
| 8   | Les 3 pages indispensables               | S2      | Expertise SEO       |
| 9   | SEO vs Funnel                            | S2      | Expertise SEO       |
| 10  | Le maillage invisible                    | S2      | Expertise SEO       |
| 11  | Pourquoi ton formulaire ne convertit pas | S3      | Funnel / Conversion |
| 12  | Le parcours idéal d'un visiteur          | S3      | Funnel / Conversion |
| 13  | Structurer un lead magnet stratégique    | S3      | Funnel / Conversion |
| 14  | L'erreur fatale des pages "À propos"     | S3      | Funnel / Conversion |
| 15  | Relier contenu, email et offre           | S3      | Funnel / Conversion |
| 16  | Penser affiliation intelligemment        | S4      | Monétisation        |
| 17  | L'erreur des comparatifs WordPress       | S4      | Monétisation        |
| 18  | Transformer un tuto en machine à leads   | S4      | Monétisation        |
| 19  | Automatiser sans perdre l'humain         | S4      | Automatisation      |
| 20  | Le vrai rôle d'un CRM dans WordPress     | S4      | Automatisation      |
| 21  | Où va WordPress dans 3 ans               | S5      | Vision / Autorité   |
| 22  | Penser écosystème                        | S5      | Vision / Autorité   |
| 23  | Le piège du "tout IA" sans stratégie     | S5      | Vision / Autorité   |
| 24  | Pourquoi les contenus WP sont oubliables | S5      | Vision / Autorité   |
| 25  | Devenir la référence dans sa niche       | S5      | Vision / Autorité   |
| 26  | Les 5 niveaux de maturité WordPress      | Bonus   | Domination          |
| 27  | Site vs Tunnel vs Écosystème             | Bonus   | Domination          |
| 28  | Ma stack WordPress 2026                  | Bonus   | Coulisses           |
| 29  | Ce que je ferais avec 0 audience         | Bonus   | Coulisses           |
| 30  | La méthode WordPress Business en résumé  | Bonus   | Conversion finale   |

### Règles de la série

- Hashtag systématique : `#WordPressBusiness`
- CTA final toujours conversationnel — jamais de lien direct
- Posts 25-30 : intégrer CTA newsletter ou consulting
- Recycler les posts forts en carrousels 2 semaines après publication
- Tracker : taux engagement / DM entrants / abonnés newsletter par semaine

---

## Séquences post-fermeture

Objectif : récupérer les "presque acheteurs", maintenir la relation, basculer en liste d'attente ou consulting.

---

### Séquence post-fermeture — Formation (5 emails)

Trigger FluentCRM : tag `offer_closed_formation`

**Email PF1 — Fermeture officielle + repositionnement**

Objet : C'est fermé (et c'est volontaire)

> Salut,
>
> Je ferme les inscriptions.
>
> Pas pour créer de la rareté artificielle.
> Juste parce que je veux accompagner proprement.
>
> Si tu voulais entrer et que tu as raté :
> → Liste d'attente ici : [Lien]
>
> Demain je t'envoie :
> les 3 erreurs qui empêchent la majorité des sites WordPress de convertir (même avec du trafic).
>
> Michaël

---

**Email PF2 — Valeur + diagnostic**

Objet : Les 3 blocages qui te coûtent (cher)

> Voici les 3 erreurs qui reviennent :
>
> 1. Un site sans structure (Google comprend mal)
> 2. Une offre floue (personne n'achète "un site")
> 3. Aucun système de capture (tu laisses partir les visiteurs)
>
> Question simple :
> → Lequel te bloque le plus ? Réponds juste avec : 1 / 2 / 3
>
> Je réponds perso à ceux qui sont sérieux.

---

**Email PF3 — Cas concret + preuve**

Objet : Ce qui change tout en pratique

> Cas typique :
>
> - Contenu existant / Plugin SEO installé / Zéro business
>
> Ce qu'on a fait : 1 page pilier → 8 contenus cluster → 1 lead magnet → 1 séquence email simple
>
> Résultat : trafic + leads + ventes.
>
> Si tu veux le plan exact :
> → Je l'explique ici : [Lien contenu / vidéo]

---

**Email PF4 — Option "plan B" (micro-offre / bundle)**

Objet : Si tu veux avancer maintenant (sans attendre)

> La formation est fermée.
>
> Mais tu peux avancer maintenant avec :
> ✅ Pack templates + SOP (celui que j'utilise)
> → [Lien]
>
> C'est le kit "mise en place".
> Ensuite, quand la formation rouvre, tu seras prêt.

---

**Email PF5 — Liste d'attente + pré-qualification premium**

Objet : Dernier message (après je te laisse tranquille)

> Si tu veux être prévenu à la réouverture :
> → Liste d'attente : [Lien]
>
> Et si tu veux accélérer sans attendre :
> Je prends quelques personnes en audit stratégique.
> → Candidature : [Lien]
>
> Sinon, aucun souci. Je continue à t'envoyer du contenu utile.
>
> Michaël

---

### Séquence post-fermeture — Micro-offre 47€ (3 emails)

Trigger FluentCRM : tag `offer_closed_template`

**Email PF-T1 — Fermé + alternative**

Objet : OK c'est fermé

> Le pack est fermé.
>
> Si tu veux quand même avancer :
> Je te donne une alternative gratuite :
> → [Lien vers article / vidéo "structure SEO WP"]
>
> Et si tu veux être notifié à la prochaine ouverture :
> → Liste d'attente : [Lien]

---

**Email PF-T2 — Erreur de perception**

Objet : Le vrai sujet n'est pas le prix

> La question n'est pas "47€"…
>
> La question c'est :
> Combien d'heures tu vas perdre à improviser ?
>
> Ce pack évite les oublis, les mauvais choix, les tunnels bancals.
>
> Je préviens en priorité la liste d'attente.
> → [Lien]

---

**Email PF-T3 — Qualification douce**

Objet : Je te pose une seule question

> Tu cherches à :
> A) Attirer du trafic
> B) Convertir ce trafic
> C) Vendre une offre premium
>
> Réponds avec A/B/C.
> Je t'enverrai la ressource la plus utile.

---

### Tags FluentCRM post-fermeture

| Tag                       | Déclencheur                      |
| ------------------------- | -------------------------------- |
| `offer_closed_template`   | Fin promo pack templates         |
| `offer_closed_formation`  | Fermeture inscriptions formation |
| `waitlist_template`       | Clic "Liste d'attente" template  |
| `waitlist_formation`      | Clic "Liste d'attente" formation |
| `hot_prospect_consulting` | Clic lien audit stratégique      |
| `replied_qualification`   | Réponse email qualification      |

---

## FluentCRM — 5 automations complètes (menu par menu)

Structure recréable en 20-30 minutes. Logique propre, sans spaghetti.

---

### Préparation — Tags à créer

**Niveau :**
`lvl_debutant` / `lvl_freelance` / `lvl_agence` / `lvl_formateur`

**Intent :**
`intent_seo` / `intent_lms` / `intent_funnel` / `intent_monetisation`

**Comportement :**
`lead_magnet_downloaded` / `warm_lead` / `inactive_60d` / `visited_sales_page` / `attended_masterclass`

**Achat :**
`buyer_template` / `buyer_formation` / `buyer_consulting`

**Offre :**
`offer_closed_template` / `offer_closed_formation` / `waitlist_template` / `waitlist_formation` / `hot_prospect_consulting`

---

### Automation 1 — Lead Magnet → Nurturing

**Trigger :** Form Submitted → Checklist SEO

1. Add Tag → `lead_magnet_downloaded`
2. Add Tag → `intent_seo`
3. Send Email → Email 1
4. Delay 1 day → Send Email 2
5. Delay 1 day → Send Email 3
6. Delay 1 day → Send Email 4
7. Delay 1 day → Send Email 5

**Condition après Email 3 :**
If Email Opened (any of first 3) → Add Tag: `warm_lead`

**Final step :**
Send Email 6 (Micro-offre Template) → END

---

### Automation 2 — Achat Template → Upsell Formation

**Trigger :** Purchase Product → Template SEO

1. Add Tag → `buyer_template`
2. Remove Tag → `warm_lead`
3. Delay 1 day → Send Email Upsell 1
4. Delay 2 days → Send Email Upsell 2
5. Delay 2 days → Send Email Upsell 3
6. Delay 2 days → Send Email Upsell 4

**Condition intelligente :**

- After Email 2 : If Visited URL contains `/formation` → Add Tag: `visited_sales_page`
- After Email 3 : If Tag = `visited_sales_page` → Send Reminder Email

---

### Automation 3 — Achat Formation → Consulting

**Trigger :** Purchase → Formation

1. Add Tag → `buyer_formation`
2. Stop Other Automations
3. Delay 30 days → Send Email Consulting 1
4. Delay 3 days → Send Email Consulting 2

**Condition :**
If Click Link "Audit" → Add Tag: `hot_prospect_consulting` → Send Email Calendly link

---

### Automation 4 — Post-Fermeture Formation

**Trigger :** Tag Added → `offer_closed_formation`

1. Send Email PF1
2. Delay 2 days → Send Email PF2
3. Delay 2 days → Send Email PF3
4. Delay 2 days → Send Email PF4
5. Delay 2 days → Send Email PF5

**Condition :**
If Click "Liste d'attente" → Add Tag: `waitlist_formation`

---

### Automation 5 — Réactivation

**Trigger :** Contact has not opened email in 60 days

1. Add Tag → `inactive_60d`
2. Send Email Reactivation 1
3. Delay 3 days → Send Email Reactivation 2

**Condition :**
If No Open after 7 days → Add Tag: `cold_contact` → Remove from main broadcast list

---

### Lead Scoring (FluentCRM)

Settings → CRM → Scoring

| Action               | Points |
| -------------------- | ------ |
| Email open           | +5     |
| Link click           | +10    |
| Visit sales page     | +20    |
| Masterclass attended | +30    |

**Automation scoring :**
If Score > 80 → Send Email "Appel stratégique"

---

### Règle universelle — Exit condition

Ajouter en haut de chaque automation :

> If Tag `buyer_consulting` exists → **Exit**

Évite de vendre à un client déjà premium.

---

## Optimisation psychologique des emails

7 leviers propres pour transformer les emails en déclencheurs d'action, sans manipulation.

| Levier                  | Mécanisme                            |
| ----------------------- | ------------------------------------ |
| Clarté                  | Réduction de la confusion            |
| Coût caché inaction     | Rendre visible le prix de l'inaction |
| Projection future       | Visualisation du résultat            |
| Identification (miroir) | Le lecteur se reconnaît              |
| Preuve concrète         | Cas réel, chiffres, avant/après      |
| Engagement progressif   | Petites actions avant la grande      |
| Contrôle                | Pas de pression — choix assumé       |

---

### Structure email haute conversion

1. **Ouverture** → validation de la frustration
2. **Clarification** → nommer le vrai problème
3. **Reframe** → nouvelle perspective
4. **Projection** → résultat futur concret
5. **CTA simple** → 1 seule action

---

### Exemples optimisés

**Email Nurturing 1 — Optimisé**

Objet : Pourquoi ton site WP ne décolle pas (même si tu fais "tout bien")

> Tu fais peut-être tout "correctement".
> Plugin installé. Pages propres. Articles publiés.
> Mais ton site reste invisible.
>
> Ce n'est pas un problème d'effort. C'est un problème d'architecture.
>
> Demain je te montre la structure qui change tout.
>
> → Dis-moi : tu publies combien d'articles par mois ? (Je lis les réponses.)

_Leviers : validation émotionnelle + frustration latente + engagement via question_

---

**Email Micro-offre 47€ — Optimisé**

Objet : Combien vaut 10 heures de ton temps ?

> Tu peux improviser.
> Ou utiliser exactement la structure que j'utilise avec mes clients.
>
> Ce pack n'est pas une formation, ni du blabla, ni un PDF générique.
> C'est la structure prête à appliquer. 47€.
>
> Si ça te fait gagner 10 heures, c'est rentable dès aujourd'hui.
> → [Lien]
>
> PS : Si tu hésites, réponds-moi "question".

_Leviers : comparaison valeur/prix + concrétisation bénéfice + réduction risque + ouverture dialogue_

---

**Email Formation — Optimisé**

Objet : Le vrai problème n'est pas ton SEO

> Le vrai problème : tu n'as pas de système.
>
> Un site sans système, c'est : du trafic sans conversion / des outils sans cohérence / du contenu sans stratégie.
>
> La formation ne t'apprend pas "WordPress".
> Elle t'apprend à transformer WordPress en machine business.
>
> La question n'est pas "est-ce que c'est bien ?"
> La question est : → Est-ce que tu veux structurer ça sérieusement ?

_Leviers : reframing + identité + projection long terme_

---

**Email Consulting — Optimisé**

Objet : Tu veux aller vite ou continuer à tester ?

> Tu as la méthode.
> Mais si tu continues à tester seul : tu doutes / tu ajustes / tu perds du temps.
>
> Un audit stratégique, c'est : 90 minutes / une feuille de route claire / zéro flou.
>
> Je ne prends que des projets actifs.
> Si c'est ton cas : → Candidature ici.

_Leviers : polarisation douce + rareté qualitative + filtrage statutaire_

---

### Technique CTA conversationnel

Au lieu de "Clique ici", utiliser :

> "Réponds-moi avec : SEO / Funnel / LMS"

Avantages : engagement actif + meilleure délivrabilité + segmentation naturelle + conversion indirecte

**Phrase universelle haute conversion :**

> "Ce n'est pas pour tout le monde."
> → Active : sélection + désir statutaire + auto-qualification

---

## Scripts émotionnels par persona

Même offre, angle émotionnel différent selon le profil.

---

### Persona 1 — Débutant

**Émotion dominante :** confusion + peur de se tromper
**Douleur cachée :** "Je ne suis pas sûr de faire les bons choix."

**Email Formation — Script débutant**

Objet : Tu n'as pas besoin d'être "technique"

> Tu n'es pas bloqué par WordPress.
> Tu es bloqué par la surcharge d'informations.
>
> Un tuto dit A. Un autre dit B. Un forum dit l'inverse.
> Résultat : tu avances… mais dans le flou.
>
> Ce que tu cherches, ce n'est pas plus d'outils. C'est un chemin clair.
>
> La formation te donne : l'ordre exact / les bons choix / les erreurs à éviter.
>
> Tu n'as pas besoin d'être expert. Tu as besoin d'un cadre.
>
> → Si tu veux arrêter d'improviser : [Lien]

_Leviers : réduction anxiété + simplification + sécurité + guidage_

---

### Persona 2 — Freelance

**Émotion dominante :** frustration + stagnation
**Douleur cachée :** "Je travaille beaucoup, mais je ne scale pas."

**Email Formation — Script freelance**

Objet : Le plafond invisible des freelances WordPress

> Tu es compétent. Tes sites sont propres. Tes clients sont satisfaits.
>
> Mais : tu vends au temps / tu repars de zéro à chaque projet / tu n'as pas de système.
>
> Le problème n'est pas ton niveau technique. C'est l'absence de structure business.
>
> Ce que je t'apprends : transformer ton expertise en actif / créer un funnel / automatiser une partie de l'acquisition.
>
> La question : → Est-ce que tu veux sortir du plafond freelance ?

_Leviers : identité professionnelle + frustration latente + désir d'évolution + projection statut supérieur_

---

### Persona 3 — Agence

**Émotion dominante :** pression + rentabilité + image
**Douleur cachée :** "On pourrait faire mieux, mais on manque de système."

**Email Consulting — Script agence**

Objet : Ton agence n'a pas besoin de plus de clients

> Elle a besoin de meilleure structure.
>
> Ce que je vois souvent : bon trafic / bon portfolio / bon réseau.
> Mais : pas de funnel clair / pas de nurturing / pas d'optimisation LTV.
>
> Résultat : acquisition constante. Rentabilité irrégulière.
>
> Un audit stratégique, ce n'est pas "du SEO".
> C'est optimiser la machine complète.
>
> Je travaille avec peu d'agences.
> → Candidature ici.

_Leviers : positionnement élite + optimisation interne + rentabilité + sélectivité_

---

### Tableau récapitulatif — Angles par persona

| Persona   | Peur principale | Désir profond | Angle email     | CTA               |
| --------- | --------------- | ------------- | --------------- | ----------------- |
| Débutant  | Se tromper      | Clarté        | Guide rassurant | Structure propre  |
| Freelance | Stagner         | Évolution     | Système / actif | Sortir du plafond |
| Agence    | Perdre marge    | Optimisation  | Rentabilité     | Candidature élite |

### Implémentation FluentCRM — Segmentation par persona

Même email → introduction différente selon tag :

- Tag `lvl_debutant` → version anxiété rassurante
- Tag `lvl_freelance` → version plafond freelance
- Tag `lvl_agence` → version rentabilité premium

Corps identique. Angle d'entrée différent. Impact maximum.

---

## Séquence email affiliation — 7 jours (textes complets)

Objectif : transformer un lead en utilisateur de la stack recommandée + client affilié + lecteur long terme.
Angle : logique stratégique d'abord, outil ensuite. On ne pousse jamais un lien, on pousse un raisonnement.

---

### Email J1 — Le problème

**Objet :** Pourquoi la plupart des sites WordPress sont mal construits

> Tu veux une vérité simple ?
>
> La majorité des sites WordPress sont construits à l'envers.
>
> On choisit un thème.
> On installe 15 plugins.
> On croise les doigts.
>
> Résultat ?
>
> - Site lent
> - SEO mal optimisé
> - Tunnel inexistant
> - Aucune capture
> - Aucune stratégie
>
> Le problème n'est pas WordPress.
> Le problème, c'est l'absence d'architecture.
>
> Demain, je t'explique la logique qu'un site devrait toujours respecter.
>
> — Michaël

---

### Email J2 — La logique système

**Objet :** Un site WordPress, c'est une architecture

> Un site n'est pas une vitrine.
> C'est un système.
>
> Il repose sur 5 blocs :
>
> 1. Infrastructure (hébergement fiable)
> 2. Performance (vitesse)
> 3. SEO (visibilité)
> 4. Capture (email)
> 5. Offre (monétisation)
>
> Si un bloc est faible, tout le système est fragile.
>
> La plupart des freelances optimisent le design.
> Très peu optimisent la structure.
>
> Demain, je te partage la stack que je recommande pour construire proprement.
>
> — Michaël

---

### Email J3 — La stack schoolsWP

**Objet :** Voici la stack que je recommande en 2026

> Si je devais reconstruire un site aujourd'hui, voici ce que je ferais.
>
> 1️⃣ Hébergement solide
> La performance commence ici.
> Un hébergement trop cheap = SEO pénalisé + conversions faibles.
>
> 2️⃣ Plugin SEO structuré
> Un outil clair, pas surchargé, avec vraie logique sémantique.
>
> 3️⃣ Plugin cache / performance
> La vitesse est un levier business.
>
> 4️⃣ CRM intégré à WordPress
> Email = actif long terme.
>
> 5️⃣ LMS si tu vends une formation
> Pas bricoler avec 3 plugins différents.
>
> J'ai détaillé la stack complète ici :
> → [Lien affilié contextualisé]
>
> Je recommande uniquement ce que j'utilise ou que j'ai testé sérieusement.
>
> Demain, je t'explique pourquoi je ne recommande pas certaines alternatives populaires.
>
> — Michaël

---

### Email J4 — Comparatif intelligent

**Objet :** Pourquoi je ne recommande pas toujours les outils "à la mode"

> Beaucoup choisissent leurs outils en fonction :
>
> - Du marketing
> - Du prix
> - De la popularité
>
> C'est une erreur.
>
> Un bon outil dépend :
>
> - De ton niveau
> - De ton modèle business
> - De ton objectif réel
>
> Exemple :
> Un hébergement très bon marché peut suffire pour un blog perso.
> Il est catastrophique pour un site orienté business.
>
> J'ai comparé les principales solutions ici :
> → [Lien vers article comparatif affilié]
>
> Toujours choisir un outil en fonction du ROI, pas du prix.
>
> Demain, je te montre un cas réel.
>
> — Michaël

---

### Email J5 — Cas réel

**Objet :** Avant / Après : même site, stack différente

> Cas réel.
>
> Freelance WordPress. 2 000 visiteurs/mois. Conversions faibles.
>
> Problèmes :
>
> - Hébergement lent
> - Plugins mal optimisés
> - Aucun système email structuré
>
> On restructure :
>
> - Nouvelle base d'hébergement
> - Optimisation performance
> - CRM intégré
> - Tunnel simple
>
> Résultat :
>
> - Temps de chargement divisé par 2
> - +18% conversions
> - Premiers revenus récurrents
>
> La stack change le résultat.
>
> Si tu veux voir les outils exacts utilisés :
> → [Lien affilié]
>
> Demain : 3 erreurs coûteuses à éviter.
>
> — Michaël

---

### Email J6 — Les erreurs coûteuses

**Objet :** 3 erreurs qui te coûtent de l'argent

> Erreur 1 : Choisir le moins cher.
> Erreur 2 : Multiplier les plugins inutiles.
> Erreur 3 : Ignorer la performance.
>
> Chaque seconde de chargement en plus = conversions en moins.
>
> Un site WordPress orienté business doit être :
>
> - Rapide
> - Structuré
> - Minimaliste
> - Stratégique
>
> Voici la stack que je recommande pour éviter ces erreurs :
> → [Lien affilié global]
>
> Demain, je résume tout simplement.
>
> — Michaël

---

### Email J7 — Décision

**Objet :** Si je devais recommencer aujourd'hui

> Si je repartais de zéro :
>
> 1. Hébergement solide dès le départ
> 2. Plugin SEO bien configuré
> 3. CRM intégré immédiatement
> 4. Tunnel simple
> 5. Pas de bricolage
>
> C'est tout. Pas 20 outils. Pas de complexité inutile.
>
> La stack complète que j'utiliserais aujourd'hui est ici :
> → [Lien affilié final]
>
> Si tu passes par mon lien, j'ai prévu un bonus :
> Je t'envoie ma checklist performance complète.
>
> Réponds simplement "STACK".
>
> — Michaël

---

### Stratégie psychologique — Séquence affiliation

| Jour | Angle           | Levier principal           | Lien affilié    |
| ---- | --------------- | -------------------------- | --------------- |
| J1   | Problème        | Frustration latente        | Non             |
| J2   | Logique système | Clarté / Architecture      | Non             |
| J3   | Stack complète  | Confiance + recommandation | Oui (principal) |
| J4   | Comparatif      | Crédibilité / anti-bias    | Oui (article)   |
| J5   | Cas réel        | Preuve sociale + résultats | Oui             |
| J6   | Erreurs         | Coût caché inaction        | Oui (rappel)    |
| J7   | Décision        | Projection + bonus         | Oui (final)     |

### Règles affiliation — Ne jamais / Toujours

**Ne jamais :**

- Mettre 10 liens affiliés dans un seul email
- Utiliser le mot "promo" ou "offre"
- Parler tarif avant avoir installé la valeur

**Toujours :**

- Expliquer le pourquoi avant l'outil
- Contextualiser chaque recommandation
- Mentionner la transparence affiliée
- Parler ROI, pas prix

### Version premium — Bonus conversationnel

> "Si tu passes par mon lien, je t'offre la checklist performance."

Déclenche : `tag buyer_affiliate` → séquence upsell formation

### Projection revenus evergreen

| Variable            | Valeur estimée |
| ------------------- | -------------- |
| Inscrits liste      | 1 000          |
| Open rate           | 40%            |
| Taux clic affilié   | 10%            |
| Taux conversion     | 5%             |
| Commission moyenne  | 80€            |
| **Revenu séquence** | **~1 600€**    |

Multiplié × 12 mois = actif evergreen récurrent.

### Segmentation avancée post-clic

| Clic sur    | Séquence déclenchée     |
| ----------- | ----------------------- |
| Hébergement | Séquence performance    |
| Plugin SEO  | Séquence SEO avancée    |
| LMS         | Séquence formation      |
| CRM         | Séquence automatisation |

---

## Plan 5 000€/mois en affiliation

Objectif : revenu récurrent stable et prévisible, evergreen, sans lancement ni ads.
Axe : on ne vend pas des outils — on vend une stack stratégique, une méthode, un système WordPress business. L'affiliation est la conséquence logique.

---

### Structure des revenus cibles

| Pôle                       | Cible            | Objectif mensuel |
| -------------------------- | ---------------- | ---------------- |
| Hébergement                | Tous profils     | 2 000€           |
| Plugins SEO / Performance  | SEO / Freelances | 1 500€           |
| CRM / LMS / Automatisation | Formateurs       | 1 500€           |
| **Total**                  |                  | **5 000€**       |

---

### Mécanique chiffrée (phase 3 Authority)

| Variable           | Valeur           |
| ------------------ | ---------------- |
| Trafic mensuel     | 15 000 visiteurs |
| Taux clic affilié  | 3% = 450 clics   |
| Taux conversion    | 5% = 22 ventes   |
| Commission moyenne | 200€             |
| Sous-total         | ~4 400€          |
| + 5 ventes LMS HT  | 300€/comm.       |
| **Total estimé**   | **~5 900€**      |

---

### Pilier 1 — Articles SEO transactionnels

Pages à créer en priorité :

- "Meilleur hébergement WordPress 2026"
- "Rank Math vs Yoast : comparatif complet"
- "FluentCRM avis et test"
- "Tutor LMS vs LearnDash"
- "Meilleur plugin cache WordPress"

Chaque page doit être : ultra détaillée / structurée / mise à jour trimestriellement / maillée vers les autres comparatifs.

---

### Pilier 2 — Carrousels LinkedIn mappés vers affiliation

Sujets à produire :

- "Ma stack WordPress 2026"
- "Les 5 outils que j'utilise"
- "Ce que j'installerais aujourd'hui si je repartais de zéro"

Objectif de chaque carrousel : rediriger vers l'article comparatif affilié central.

---

### Pilier 3 — Séquence email affiliée evergreen

Chaque nouveau lead passe automatiquement par :

1. Stack recommandée (J3)
2. Comparatif intelligent (J4)
3. Cas réel (J5)
4. Erreurs coûteuses (J6)
5. Récap + bonus (J7)

Séquence FluentCRM : automatisée, evergreen, taggage post-clic.

---

### Pilier 4 — Bonus exclusif (conversion +++)

Augmenter le taux de conversion avec :

- Checklist performance offerte
- Mini audit offert si achat via lien
- Template SEO prêt à l'emploi
- Guide de configuration étape par étape

Formule : "Passe par mon lien → je t'offre [bonus spécifique]."

---

### Pilier 5 — Mise à jour trimestrielle

Re-optimiser tous les 3 mois :

- Titres et balises SEO
- CTA et formulations
- Comparatifs et tarifs
- Screenshots et interfaces
- Données de performance

Google récompense la fraîcheur. Les conversions aussi.

---

### Stratégie cluster hébergement (exemple)

Structure de cluster complet :

- Page pilier : "Meilleur hébergement WordPress"
- Satellite 1 : Pourquoi l'hébergement est stratégique
- Satellite 2 : Erreurs fréquentes de choix
- Satellite 3 : Comparatif détaillé
- Satellite 4 : Guide de migration
- Satellite 5 : Optimisation post-installation

Tout le cluster renvoie vers la page affiliée centrale.

---

### Règle schoolsWP — Positionnement affiliation

**Toujours répondre à :**

- Pour qui ?
- Quand l'utiliser ?
- Pourquoi ce choix ?
- ROI estimé ?

**Jamais :** "Voici le meilleur plugin."
**Toujours :** "Voici le meilleur choix selon ton niveau et ton objectif."

---

### Plan 12 mois

| Phase      | Mois    | Actions                                        |
| ---------- | ------- | ---------------------------------------------- |
| Fondation  | M1-M3   | 5 pages piliers transactionnelles              |
| Activation | M4-M6   | Carrousels LinkedIn + séquence email affiliée  |
| Croissance | M7-M9   | Optimisation SEO + backlinks                   |
| Expansion  | M10-M12 | +3 nouveaux comparatifs + clusters secondaires |

---

### Multiplicateur ×2 — Multi-canal

1 contenu → 5 points d'entrée :

- Article SEO (trafic organique)
- Carrousel LinkedIn (DM + réseau)
- Email newsletter (liste existante)
- YouTube review (vidéo + description affiliée)
- Shorts (reach court)

---

### Facteur clé : transparence

Mentionner systématiquement :

- Pourquoi cette recommandation
- Les limites de l'outil
- Les alternatives sérieuses
- La nature affiliée si demandé

La confiance augmente la conversion sur le long terme.

---

### Résultats attendus

| Horizon    | Résultat                                       |
| ---------- | ---------------------------------------------- |
| 6 mois     | Premières commissions régulières (~500-1 000€) |
| 12 mois    | Machine stable (2 000-3 500€/mois)             |
| 18-24 mois | Objectif 5 000€/mois atteint                   |

Sans lancement. Sans ads. Basé sur actifs SEO evergreen.

### Vision long terme — Modèle économique complet

| Flux        | Nature    | Rôle                  |
| ----------- | --------- | --------------------- |
| Affiliation | Récurrent | Finance la croissance |
| Formation   | Scalable  | Levier principal      |
| Consulting  | Cash flow | Marge premium         |

L'affiliation finance les actifs SEO.
Les actifs SEO alimentent la newsletter.
La newsletter convertit en formation et consulting.

---

## Stratégie affiliation ×3 — SEO + LinkedIn + Email combinés

Principe : un outil affilié présent sur 3 canaux synchronisés = actif scalable. Un seul canal = potentiel limité.

---

### Sélection stratégique des outils (max 5-7 outils cœur)

| Catégorie           | Critères de sélection                           |
| ------------------- | ----------------------------------------------- |
| Hébergement         | Récurrence commission + qualité réelle          |
| Plugin SEO          | Alignement vision schoolsWP + cas d'usage clair |
| CRM / Email         | Commission récurrente (SaaS idéal)              |
| LMS                 | Ticket élevé = commission élevée                |
| Cache / Performance | Universel = volume élevé                        |
| Sécurité            | Récurrent + besoin permanent                    |

---

### Pilier 1 — SEO (moteur long terme)

**Types d'articles à produire :**

- Comparatif complet (2 500 – 4 000 mots)
- Avis détaillé avec test réel
- Guide d'installation étape par étape
- "X vs Y" avec verdict tranché
- Cas d'usage spécifique par profil

**Structure idéale d'un article affilié :**

- H1 : Avis + Comparatif [Outil] 2026
- H2 : Pour qui ?
- H2 : Avantages / limites honnêtes
- H2 : Cas réel (avant/après)
- H2 : Alternatives sérieuses
- H2 : Verdict schoolsWP

**Toujours intégrer :**

- Capture email (lead magnet contextuel)
- Bonus téléchargeable (checklist / template)
- Lien affilié contextualisé (pas agressif)

**KPI cibles :**

- Position Google : Top 5 sur requêtes transactionnelles
- CTR : > 5%
- Taux clic affilié : 3–8%

---

### Pilier 2 — LinkedIn (amplificateur)

LinkedIn ne vend pas l'outil. Il vend la logique stratégique.

**Types de contenus :**

- Carrousel "Stack idéale 2026"
- Post "Pourquoi j'ai choisi X (et pas Y)"
- Post "Pourquoi X est surévalué dans ce cas"
- Cas réel (avant/après)
- Erreurs fréquentes de choix d'outil

**Structure type :**

1. Problème / tension
2. Logique système
3. Recommandation contextualisée (profil + objectif)
4. Redirection vers article ou bonus

**CTA systématique :**

> "Je détaille ça dans l'article lié."
> Jamais : "Clique mon lien affilié."

**KPI cibles :**

- 20 000+ impressions sur posts clés
- 5–10 DM qualifiés par post fort
- 200–500 clics vers l'article affilié

---

### Pilier 3 — Email (convertisseur)

L'email transforme la confiance en action concrète.

**Séquence evergreen affiliée (7 jours) :**
J1 → Problème | J2 → Logique système | J3 → Stack | J4 → Comparatif | J5 → Cas réel | J6 → Erreurs | J7 → Décision

**Segmentation post-clic :**

- Clic hébergement → séquence performance
- Clic LMS → séquence formation
- Clic CRM → séquence automatisation

**Bonus conversion :**

> "Passe par mon lien → je t'offre [checklist / template / mini audit]."

---

### Flux combinés — 3 scénarios

| Scénario | Flux                                                       |
| -------- | ---------------------------------------------------------- |
| 1        | LinkedIn → Article SEO → Lead Magnet → Email → Affiliation |
| 2        | SEO → Capture → Email → Affiliation                        |
| 3        | LinkedIn → DM → Email direct → Affiliation                 |

---

### Simulation réaliste mensuelle (1-2 outils forts)

| Canal     | Trafic / Liste  | Taux clic | Conversion | Commission | Revenus     |
| --------- | --------------- | --------- | ---------- | ---------- | ----------- |
| SEO       | 5 000 visiteurs | 5%        | 5%         | 80€        | ~1 000€     |
| LinkedIn  | 1 post fort     | 300 clics | 5%         | 80€        | ~1 200€     |
| Email     | 2 000 abonnés   | 10%       | 5%         | 80€        | ~800€       |
| **Total** |                 |           |            |            | **~3 000€** |

---

### Positionnement psychologique — Architecte de stack

**Ne pas se positionner comme :**

> "Voici un bon plugin."

**Se positionner comme :**

> "Voici la stack stratégique pour atteindre [objectif précis]."

On vend la transformation, pas l'outil.
On n'est pas affilié. On est architecte de stack.

---

### Pour viser 5 000€/mois affilié ×3

- 3 clusters SEO majeurs (hébergement / SEO / LMS)
- 1 séquence email dédiée par outil principal
- 1 carrousel LinkedIn par outil, par trimestre
- 1 bonus exclusif schoolsWP par outil (différenciation forte)

---

## SCRIPTS EMAIL AFFILIÉS — MOT À MOT (SÉQUENCE EVERGREEN 7 JOURS)

Objectif : vendre la stack WordPress recommandée sans forcer.
Positionnement : stratégique, ROI, pédagogique.
À déployer comme séquence automatisée post-capture (lead magnet stack / hébergement).

---

### EMAIL 1 — Le problème (J1)

**Objet :** Pourquoi la majorité des sites WordPress stagnent

---

Beaucoup de sites WordPress stagnent.

Pas à cause du contenu.
Pas à cause du design.

Mais à cause de la structure.

Hébergement moyen.
Plugins empilés.
SEO mal configuré.
Aucune logique d'ensemble.

Résultat ?

Un site qui "existe"…
Mais qui ne performe pas.

WordPress n'est pas le problème.
La stack l'est.

Demain, je te montre comment je structure un site WordPress orienté performance et business.

À demain,
Michaël

---

### EMAIL 2 — La logique système (J2)

**Objet :** WordPress n'est pas un outil, c'est une architecture

---

Un site WordPress performant repose sur 5 briques :

1. Hébergement solide
2. Performance maîtrisée
3. SEO structuré
4. Capture email
5. Automatisation

Si une brique est faible, tout ralentit.

La majorité des gens choisissent leurs outils au hasard.

Moi, je raisonne en système.

Demain, je te partage la stack exacte que je recommande.

— Michaël

---

### EMAIL 3 — La stack recommandée (J3)

**Objet :** Voici la stack que je recommande

---

Voici la stack minimale viable que je recommande aujourd'hui.

**1️⃣ Hébergement rapide et stable**
→ C'est la fondation.
Un mauvais hébergement ruine tout.

**2️⃣ Plugin SEO structurant**
→ Pour contrôler indexation, maillage, schémas.

**3️⃣ Plugin cache / performance**
→ Pour réduire le temps de chargement.

**4️⃣ CRM natif WordPress**
→ Pour ne pas dépendre d'outils externes inutiles.

**5️⃣ LMS si tu vends des formations**

Je détaille chaque outil ici :
👉 [Lien vers ta page ressource affiliée]

Je recommande uniquement ce que j'utilise réellement.

— Michaël

---

### EMAIL 4 — Comparatif intelligent (J4)

**Objet :** Pourquoi je ne recommande pas tout

---

On me demande souvent :

"Pourquoi ne pas utiliser l'outil X ?"

Parce qu'un bon outil n'est pas forcément adapté à ton contexte.

Exemple :

Un hébergement premium est inutile si tu as 200 visiteurs/mois.
Un CRM avancé est inutile sans funnel.

Je détaille ici les différences clés entre les principales options :
👉 [Lien vers comparatif affilié]

Toujours choisir en fonction de ta stratégie.

— Michaël

---

### EMAIL 5 — Cas concret (J5)

**Objet :** Avant / Après avec la bonne stack

---

Cas réel :

Freelance.
Site lent.
Plugins empilés.
Peu de conversions.

On restructure :

- Hébergement optimisé
- SEO configuré correctement
- Funnel simple
- Capture email intégrée

Résultat :

+38% trafic en 3 mois
+2 000€ générés via formation

La stack change tout.

Je détaille les outils utilisés ici :
👉 [Lien affilié]

— Michaël

---

### EMAIL 6 — Les erreurs coûteuses (J6)

**Objet :** 3 erreurs qui coûtent cher

---

Erreur 1 : choisir le moins cher.
Erreur 2 : installer 25 plugins.
Erreur 3 : ignorer la performance.

Un site lent, mal structuré, mal configuré = perte d'argent.

La solution ?

Une stack simple, cohérente, maîtrisée.

Voici celle que je recommande :
👉 [Lien page ressource]

— Michaël

---

### EMAIL 7 — Récap stratégique (J7)

**Objet :** Si je devais recommencer aujourd'hui

---

Si je devais relancer un site WordPress demain :

- Hébergement performant
- SEO propre dès le départ
- Performance configurée
- CRM intégré
- Funnel simple

Pas plus.

Tu peux voir les outils précis que j'utiliserais ici :
👉 [Lien affilié global]

Si tu passes par mes liens, ça soutient schoolsWP.
Je recommande uniquement ce que j'utilise et teste.

— Michaël

---

### Ce que cette séquence fait

| Objectif         | Mécanique                                               |
| ---------------- | ------------------------------------------------------- |
| Autorité         | Positionne comme architecte de stack, pas comme affilié |
| Confiance        | Transparence sur les recommandations ("je l'utilise")   |
| Clics naturels   | Liens contextuels, jamais promos                        |
| Conversion douce | Logique système → solution évidente                     |
| Evergreen        | Aucune date, aucun événement → toujours valide          |

### Règles d'utilisation

- **Ne jamais** mettre le nom de l'outil affilié en objet d'email (filtre spam + perte d'autorité)
- **Toujours** contextualiser le lien ("je détaille ici" / "voici ce que j'utiliserais")
- **Disclosure** affiliée obligatoire : "Si tu passes par mes liens, ça soutient schoolsWP."
- **Personnaliser** les cas concrets avec de vrais chiffres issus de ton expérience
- **Tagger** FluentCRM sur clic lien : `intent_affiliation_stack` → entrée dans séquence dédiée

---

## TABLEAU PRÉVISIONNEL AFFILIATION — 12 MOIS

### Hypothèses de base

| Paramètre                   | Valeur               |
| --------------------------- | -------------------- |
| Trafic initial (mois 1)     | 3 000 visiteurs/mois |
| Croissance mensuelle        | +15% (SEO + ampli.)  |
| % visiteurs → page affiliée | 6%                   |
| % clics sur lien affilié    | 12%                  |
| Taux de conversion          | 4%                   |
| Commission moyenne          | 70€                  |

---

### Scénario prudent (SEO seul)

| Mois | Trafic | Page affiliée (6%) | Clics (12%) | Ventes (4%) | CA mensuel |
| ---- | ------ | ------------------ | ----------- | ----------- | ---------- |
| 1    | 3 000  | 180                | 22          | 1           | 70€        |
| 2    | 3 450  | 207                | 25          | 1           | 70€        |
| 3    | 3 970  | 238                | 29          | 1           | 70€        |
| 4    | 4 560  | 274                | 33          | 1           | 70€        |
| 5    | 5 240  | 314                | 38          | 2           | 140€       |
| 6    | 6 030  | 362                | 43          | 2           | 140€       |
| 7    | 6 930  | 416                | 50          | 2           | 140€       |
| 8    | 7 970  | 478                | 57          | 2           | 140€       |
| 9    | 9 160  | 550                | 66          | 3           | 210€       |
| 10   | 10 530 | 632                | 76          | 3           | 210€       |
| 11   | 12 110 | 726                | 87          | 3           | 210€       |
| 12   | 13 930 | 836                | 100         | 4           | 280€       |

**Total année 1 (scénario prudent) : ~1 750€ à 2 000€**

---

### Scénario optimisé (SEO + Email + LinkedIn)

Leviers activés : séquence email performante + 2 carrousels stack/mois + page ressource optimisée + bonus exclusif.

| Paramètre amélioré          | Valeur |
| --------------------------- | ------ |
| % visiteurs → page affiliée | 8%     |
| % clics sur lien affilié    | 15%    |
| Taux de conversion          | 5%     |

**Projection fin d'année → 800 à 1 200€/mois → 6 000 à 8 000€ sur 12 mois**

---

### Scénario domination (mois 12 → 24)

Conditions : 25 000 visiteurs/mois, 10 pages affiliées fortes, SEO solide, email segmenté, autorité LinkedIn installée.

| Paramètre              | Valeur              |
| ---------------------- | ------------------- |
| Trafic                 | 25 000              |
| % page affiliée        | 10%                 |
| % clic                 | 15%                 |
| Conversion             | 5%                  |
| Commission moyenne     | 80€                 |
| **CA mensuel projeté** | **~3 000 à 5 000€** |

---

### Leviers qui changent tout

| Levier                      | Impact estimé           |
| --------------------------- | ----------------------- |
| Page ressource unique forte | ×2 sur CTR              |
| Bonus exclusif via ton lien | ×1.5 conversion         |
| Comparatifs ultra détaillés | ×2 trafic longue traîne |
| Études de cas chiffrées     | ×1.5 confiance          |
| Segmentation CRM par outil  | ×1.5 revenus email      |

---

### KPIs à suivre mensuellement

- Trafic SEO global
- CTR affilié (clics / visiteurs page)
- Taux de conversion par outil
- CA mensuel par outil
- CA par canal (SEO / Email / LinkedIn)

---

### Stratégie d'accélération (1 000€ → 5 000€/mois)

1. Doubler les pages transactionnelles (comparatifs, alternatives)
2. Ajouter des contenus longue traîne ciblés par outil
3. Créer un mini bonus exclusif par outil principal
4. Segmenter l'email par outil (séquence dédiée)
5. Multiplier les études de cas avec chiffres réels

---

### Conclusion stratégique

| Phase    | Objectif                                           |
| -------- | -------------------------------------------------- |
| Année 1  | Validation + fondation (~2 000€)                   |
| Année 2  | Scalabilité (~5 000€/mois)                         |
| Objectif | Couvrir les charges fixes → financer la croissance |

---

## STRATÉGIE AFFILIATION ×3 — SEO + LINKEDIN + EMAIL COMBINÉS

### Vision globale

Pas trois stratégies séparées.

Un système unique :
**1 pilier affilié → décliné sur 3 canaux → convergeant vers 1 page ressource → 1 séquence → 1 logique ROI.**

---

### Base du système — Page ressource centrale

**"La stack WordPress business recommandée par schoolsWP"**

Structure de la page :

| Catégorie      | Éléments à couvrir                                     |
| -------------- | ------------------------------------------------------ |
| Hébergement    | Pour qui / Pourquoi / ROI / Alternative / Lien + Bonus |
| Plugin SEO     | Pour qui / Pourquoi / ROI / Alternative / Lien + Bonus |
| Performance    | Pour qui / Pourquoi / ROI / Alternative / Lien + Bonus |
| CRM            | Pour qui / Pourquoi / ROI / Alternative / Lien + Bonus |
| LMS            | Pour qui / Pourquoi / ROI / Alternative / Lien + Bonus |
| Automatisation | Pour qui / Pourquoi / ROI / Alternative / Lien + Bonus |

Cette page est le hub. Tout le système renvoie ici.

---

### Pilier 1 — SEO (Attraction chaude)

**Objectif :** capter le trafic transactionnel.

**Contenus à produire :**

- "Meilleur hébergement WordPress 2026"
- "Avis complet [outil]"
- "[Outil A] vs [Outil B]"
- "Alternative à [outil populaire]"
- "Stack WordPress idéale pour freelance"

**Structure de chaque article :** intent d'achat → tableau comparatif → cas d'usage → CTA page ressource.

**Logique de flux :**

```
Article transactionnel
→ Maillage interne
→ Page ressource
→ Pop-up checklist stack
→ Séquence email affiliée
```

---

### Pilier 2 — LinkedIn (Amplification stratégique)

**Objectif :** créer confiance + trafic qualifié.

**Types de carrousels :**

- Stack WordPress idéale
- Pourquoi ton hébergement te pénalise
- 3 erreurs de plugin SEO
- Ma stack si je recommençais aujourd'hui
- Outils que j'ai testés et abandonnés

**CTA systématique :** "J'ai détaillé ça ici." → Article SEO ou Page ressource

**Rôle de LinkedIn :**

| Ce que LinkedIn fait   | Ce que LinkedIn ne fait pas |
| ---------------------- | --------------------------- |
| Installe l'autorité    | Ne vend pas directement     |
| Crée la curiosité      |                             |
| Envoie du trafic chaud |                             |

---

### Pilier 3 — Email (Conversion & répétition)

**Déclencheur :** téléchargement d'un lead magnet (checklist stack / guide performance / guide SEO).

**Séquence evergreen 7 jours :** voir section SCRIPTS EMAIL AFFILIÉS ci-dessus.

**Segmentation post-clic :**

| Clic sur... | Séquence déclenchée       | Tag FluentCRM        |
| ----------- | ------------------------- | -------------------- |
| Hébergement | Mini séquence performance | `intent_hebergement` |
| Plugin SEO  | Mini séquence SEO         | `intent_seo_tool`    |
| LMS         | Mini séquence formation   | `intent_lms`         |

---

### Mapping complet du système

```
SEO       → Page ressource → Email → Vente
LinkedIn  → Article → Page ressource → Email → Vente
Newsletter → Page ressource → Vente
```

Tout converge vers un seul point d'entrée.

---

### Modèle chiffré réaliste (objectif 5 000€/mois)

**Hypothèse : 10 000 visiteurs/mois cumulés (SEO + LinkedIn + email)**

| Étape                    | Taux | Volume |
| ------------------------ | ---- | ------ |
| Visiteurs page ressource | 5%   | 500    |
| Clics affilié            | 20%  | 100    |
| Conversion               | 5%   | 5      |
| Commission moyenne       | 80€  | 400€   |

**Par outil → ~400€/mois**

Avec 10 outils bien positionnés : **~4 000€**

- Email + relances + segmentation : **→ 5 000€ atteignable**

---

### Optimisation avancée

| Levier               | Action                                                  |
| -------------------- | ------------------------------------------------------- |
| Bonus exclusifs      | Template / audit rapide / checklist premium par outil   |
| Retargeting          | Pixel Meta/Google → retarget visiteurs page ressource   |
| Mise à jour annuelle | "Stack WordPress 2026" → relance ventes effet nouveauté |

---

### Règle stratégique schoolsWP

**Ne pas dire :** "C'est le meilleur."

**Dire :** Pourquoi dans tel contexte. Pourquoi pas dans tel autre. Quel ROI attendre. Quel profil concerné.

> Autorité → confiance → conversion.

---

### Résultat à 12 mois

| Canal          | Rôle                             |
| -------------- | -------------------------------- |
| SEO            | Flux stable et prévisible        |
| LinkedIn       | Pics d'attention et trafic chaud |
| Email          | Conversion en continu            |
| Page ressource | Actif central du système         |

**L'affiliation devient prévisible.**

---

## SCRIPTS EMAIL AFFILIÉS — VERSION OPTIMISÉE (AVEC "BONJOUR")

Contexte : lead intéressé par "stack WordPress / SEO / performance".
Ton : direct, stratégique, pédagogique. Séquence evergreen 7 jours.

---

### EMAIL 1 — Le problème (J1)

**Objet :** Pourquoi ton site WordPress rame (et ça te coûte cher)

---

Bonjour,

La majorité des sites WordPress que j'analyse ont le même problème.

Ce n'est pas le design.
Ce n'est pas le thème.
Ce n'est même pas le SEO.

C'est la stack.

Hébergement trop faible.
Plugins empilés sans logique.
Aucune stratégie de performance.

Résultat :
Site lent.
SEO pénalisé.
Conversions faibles.

Un site WordPress, ce n'est pas un assemblage d'outils.
C'est une architecture.

Demain, je te montre la structure que j'utilise et que je recommande.

À demain,
Michaël

---

### EMAIL 2 — La logique système (J2)

**Objet :** Un site WordPress est un système, pas un blog

---

Bonjour,

Avant de parler d'outils, parlons logique.

Un site WordPress efficace repose sur 5 briques :

1. Un hébergement solide
2. Une base SEO claire
3. Une performance optimisée
4. Un système de capture
5. Une offre structurée

Si une seule brique est faible, tout le système ralentit.

La plupart des gens commencent par le thème.
C'est l'inverse qu'il faut faire.

Demain, je te partage la stack exacte que je recommande en 2026.

Michaël

---

### EMAIL 3 — La stack recommandée (J3)

**Objet :** Voici la stack que je recommande

---

Bonjour,

Voici la structure minimale viable que je recommande :

**Hébergement performant**
Rapidité + stabilité + support sérieux.
C'est la fondation.

**Plugin SEO solide**
Structure propre + indexation maîtrisée.

**Système de cache / performance**
Pour garder un site rapide.

**CRM intégré**
Pour capter et structurer tes leads.

Je détaille chaque outil ici, avec les cas d'usage et les alternatives :
👉 [Lien vers page ressource affiliée]

Je précise toujours quand un outil n'est PAS adapté.

L'objectif n'est pas de multiplier les plugins.
C'est de simplifier.

Michaël

---

### EMAIL 4 — Comparatif intelligent (J4)

**Objet :** Pourquoi je ne recommande pas toujours l'option la moins chère

---

Bonjour,

On me demande souvent :

"Pourquoi ne pas prendre l'hébergement le moins cher ?"

Parce qu'un hébergement trop faible te coûte :

- Du temps
- Du SEO
- Des ventes

Même chose pour les plugins "gratuits".

Ils peuvent suffire…
Mais rarement si tu veux un site qui génère du revenu.

J'ai comparé les principales options ici :
👉 [Lien comparatif affilié]

Je détaille les différences réelles.
Pas juste les promesses marketing.

Michaël

---

### EMAIL 5 — Cas concret (J5)

**Objet :** Avant / Après (chiffres réels)

---

Bonjour,

Un freelance que j'ai accompagné avait :

- 1 800 visiteurs/mois
- Site lent
- Aucun système de capture

Après restructuration :

- Meilleur hébergement
- Plugin SEO optimisé
- Stack simplifiée

Résultat :

+40% trafic en 4 mois
+3 200€ générés via son site

Les outils seuls ne font pas tout.
Mais une mauvaise stack bloque tout.

Voici ceux que j'utilise / recommande :
👉 [Lien page ressource]

Michaël

---

### EMAIL 6 — Les erreurs coûteuses (J6)

**Objet :** 3 erreurs WordPress qui coûtent cher

---

Bonjour,

Voici les 3 erreurs que je vois le plus souvent :

1. Hébergement sous-dimensionné
2. 20 plugins inutiles
3. Aucun système email

Un site WordPress rentable est simple.

Si tu veux voir la structure que je recommande :
👉 [Lien affilié]

Je préfère toujours une stack claire à un site "complexe".

Michaël

---

### EMAIL 7 — Récap & décision (J7)

**Objet :** Si je devais recommencer aujourd'hui

---

Bonjour,

Si je repartais de zéro aujourd'hui, je choisirais :

- Un hébergement performant dès le départ
- Un plugin SEO sérieux
- Un système email intégré
- Une stack minimaliste

Pas de bricolage.
Pas d'empilement inutile.

Tu peux retrouver la liste complète ici :
👉 [Lien page ressource affiliée]

Si tu passes par mon lien, je mets à disposition une checklist performance en bonus.

À toi de jouer.

Michaël

---

### Optimisations à ajouter en CRM

- Code promo exclusif si disponible
- Bonus téléchargeable après preuve d'achat
- Tag automatique si clic affilié : `intent_affiliation_stack`

### Ce que cette séquence produit

| Objectif     | Résultat                          |
| ------------ | --------------------------------- |
| Éducation    | Installe la logique système       |
| Autorité     | Positionne comme architecte stack |
| Conversion   | Naturelle, sans pression          |
| Durée de vie | Evergreen — toujours valide       |

---

## PAGE RESSOURCE AFFILIÉE — PRÊTE À PUBLIER

Page pilier WordPress. Coller dans WordPress, insérer les liens affiliés + codes promos.

---

### Titre SEO

**Ma Stack WordPress Recommandée (Testée en Conditions Réelles)**

Les outils que j'utilise réellement pour construire des sites WordPress rapides, rentables et optimisés SEO.

---

### Introduction (positionnement)

Si tu veux :

- Un site rapide
- Un SEO solide
- Un système automatisé
- Une base scalable

Alors tu as besoin d'une stack cohérente.

Pas 20 plugins. Pas du bricolage. Un système structuré.

Voici les outils que je recommande — et pourquoi.

---

### 1. Hébergement WordPress (La fondation)

**Recommandation principale : [Nom de l'hébergeur]**

Pourquoi : performances stables / support technique compétent / optimisation WordPress native / scalabilité

Pour qui : freelances, créateurs, projets sérieux

Pas adapté si : petit site hobby ou budget ultra limité

👉 [Lien affilié]

**Bonus schoolsWP :** Checklist performance offerte si tu passes par mon lien.

---

### 2. Plugin SEO

**Recommandation : [Nom plugin SEO]**

Pourquoi : gestion fine des schémas / optimisation contenu / intégration WooCommerce / performance propre

Alternative sérieuse : [Alternative]

Pour qui : site orienté SEO, blog business, tunnel optimisé

👉 [Lien affilié]

---

### 3. Performance & Cache

**Recommandation : [Nom plugin cache]**

Pourquoi : gain vitesse mesurable / compatible Core Web Vitals / configuration simple

Erreur fréquente : installer 3 plugins cache différents.

👉 [Lien affilié]

---

### 4. CRM & Email Marketing

**Recommandation : [Nom CRM]**

Pourquoi : automatisation simple / segmentation intelligente / funnel intégré

Cas d'usage : lead magnet / masterclass / séquence evergreen

👉 [Lien affilié]

---

### 5. LMS (si tu vends une formation)

**Recommandation : [Nom LMS]**

Pourquoi : intégration native WordPress / gestion des paiements / progression utilisateur

Pour qui : formateurs, coachs, créateurs de contenu

👉 [Lien affilié]

---

### 6. Outils complémentaires

- Sécurité
- Sauvegarde
- Page builder (si nécessaire)
- Automatisation

Toujours avec logique. Pas d'empilement inutile.

---

### Tableau comparatif rapide

| Besoin      | Outil recommandé | Alternative | Pour qui        |
| ----------- | ---------------- | ----------- | --------------- |
| Hébergement | X                | Y           | Projets sérieux |
| SEO         | X                | Y           | SEO avancé      |
| Cache       | X                | Y           | Performance     |
| CRM         | X                | Y           | Funnel          |
| LMS         | X                | Y           | Formation       |

---

### Comment choisir ?

3 questions à se poser :

1. Quel est ton objectif business ?
2. Quel est ton niveau technique ?
3. Quel est ton budget ?

La stack dépend de ça.

---

### Bonus schoolsWP

Si tu passes par mes liens :

- Checklist performance offerte
- Modèle funnel WordPress
- Template stack idéale

Il suffit de me répondre avec ta preuve d'achat.

---

### Transparence (disclosure affiliée)

Oui, certains liens sont affiliés. Ça ne change rien pour toi. Ça me permet de continuer à produire du contenu gratuit, de tester les outils, et d'être indépendant.

Je ne recommande que ce que j'utilise ou que j'ai réellement analysé.

---

### Conclusion stratégique

Un site WordPress performant n'est pas un hasard. C'est une architecture.

Une bonne stack te fait gagner : du temps, de l'argent, de la stabilité.

👉 Télécharge la checklist complète
👉 Ou rejoins la newsletter schoolsWP

---

### Optimisations de conversion à ajouter

- FAQ SEO en bas de page
- Bloc témoignage
- Mini étude de cas
- Captation email sticky
- Internal linking vers articles comparatifs

---

### Potentiel de la page ressource

| Scenario | Revenus estimés      |
| -------- | -------------------- |
| Bas      | 500 à 1 000€/mois    |
| Réaliste | 1 000 à 3 000€/mois  |
| Optimisé | Top 1 revenu du site |

Cette page devient le hub vers tous les contenus affiliés.

---

## PAGE RESSOURCE AFFILIÉE — VERSION SEO ULTRA OPTIMISÉE

Structure SEO transactionnelle — requêtes ciblées : "meilleure stack WordPress", "meilleurs plugins WordPress", "plugin SEO WordPress avis", "hébergement WordPress recommandé", "LMS WordPress comparatif".

---

### TITLE SEO (≤ 60 caractères)

`Meilleure Stack WordPress 2026 : Outils & Plugins Recommandés`

### META DESCRIPTION (≤ 155 caractères)

`Découvrez ma stack WordPress testée : hébergement, plugin SEO, CRM, LMS. Comparatifs, avis détaillés et recommandations stratégiques.`

---

### H1

**Meilleure Stack WordPress 2026 : Les Outils Que Je Recommande (Avis & Comparatif)**

---

### Introduction optimisée (mots-clés intégrés)

Si vous cherchez :

- le meilleur hébergement WordPress
- le meilleur plugin SEO WordPress
- les meilleurs plugins WordPress pour la performance
- un LMS WordPress fiable
- un CRM compatible WordPress

Voici la stack WordPress complète que je recommande après tests réels.

Objectif : créer un site rapide, optimisé SEO et orienté conversion.

---

### H2 — Quel est le meilleur hébergement WordPress ?

**H3 — Mon choix principal : [Nom]**

Pourquoi c'est l'un des meilleurs hébergements WordPress en 2026 :

- Serveurs optimisés WP
- Cache serveur intégré
- Support expert WordPress
- Excellentes performances Core Web Vitals

👉 [Lien affilié]

**H3 — Alternative économique**

| Critère     | Option A   | Option B |
| ----------- | ---------- | -------- |
| Performance | ⭐⭐⭐⭐⭐ | ⭐⭐⭐   |
| Support     | ⭐⭐⭐⭐⭐ | ⭐⭐     |
| Prix        | €€€        | €€       |

---

### H2 — Meilleur plugin SEO WordPress

Requête ciblée : "meilleur plugin SEO WordPress 2026"

**H3 — [Nom plugin]**

Avantages : gestion avancée des balises / schémas automatiques / optimisation contenu / intégration WooCommerce

Limites : trop complexe pour débutant total

👉 [Lien affilié]

**H3 — Alternative : [Autre plugin]**

Pour qui : site simple / moins d'options avancées

---

### H2 — Meilleur plugin cache WordPress

Requête ciblée : "plugin cache WordPress comparatif"

Pourquoi la performance est cruciale : impact SEO / impact conversion / Core Web Vitals

Comparatif rapide + lien affilié.

---

### H2 — Meilleur CRM pour WordPress

Requête ciblée : "CRM WordPress comparatif"

Pourquoi un CRM est indispensable : capture email / séquence automatique / funnel intégré

Comparatif tableau + lien affilié.

---

### H2 — Meilleur LMS WordPress

Requête ciblée : "meilleur LMS WordPress"

Points clés : paiements intégrés / progression apprenant / intégration WooCommerce

Lien affilié.

---

### H2 — Comparatif global de la meilleure stack WordPress

| Besoin      | Outil recommandé | Alternative | Idéal pour  |
| ----------- | ---------------- | ----------- | ----------- |
| Hébergement | X                | Y           | Sites pros  |
| SEO         | X                | Y           | SEO avancé  |
| Cache       | X                | Y           | Performance |
| CRM         | X                | Y           | Funnel      |
| LMS         | X                | Y           | Formation   |

Optimisé featured snippet.

---

### H2 — FAQ : Comment choisir les meilleurs plugins WordPress ?

Format FAQ pour rich results (Schema FAQ Rank Math).

- Quel est le meilleur plugin SEO WordPress ?
- Quel hébergement WordPress choisir en 2026 ?
- Combien coûte une stack WordPress complète ?
- Peut-on utiliser plusieurs plugins cache ?

---

### H2 — Bonus exclusif schoolsWP

Si vous passez par mes liens affiliés :

- Checklist performance offerte
- Template funnel WordPress
- Audit rapide offert

---

### Optimisation technique à ajouter

- Schema FAQ (Rank Math ou équivalent)
- Schema Review
- Table of contents automatique
- Liens internes vers : article comparatif hébergement / guide SEO / guide performance

---

### Clusters à créer autour de cette page (maillage)

Cette page devient pilier. Créer autour :

- Avis détaillé [Nom outil]
- Alternative à [Nom]
- Tutoriel configuration
- Comparatif 2026
- "Pourquoi je recommande X"

---

### Objectif SEO à 6 mois

| Indicateur            | Cible                            |
| --------------------- | -------------------------------- |
| Positions             | Top 10 sur 3–5 requêtes transac. |
| Trafic qualifié       | 2 000 visiteurs/mois             |
| Ventes affiliées      | 5–10/mois minimum                |
| Rang rentabilité site | Top 3                            |

---

### Version avancée (niveau supérieur)

Pour maximiser les conversions :

- Études de cas réelles avec chiffres
- Screenshots de performances mesurées
- Vidéo YouTube intégrée
- Bloc CTA sticky
- Données chiffrées vérifiables

---

## PLAN — FAIRE DE LA PAGE RESSOURCE LE TOP REVENU DU SITE

Objectif : 3 000 à 8 000€/mois en affiliation depuis une seule page pilier evergreen.

---

### Étape 1 — Positionnement stratégique

Cette page ne doit pas être une liste d'outils.

Elle doit être **la référence WordPress business francophone**.

| Ce que la page EST                    | Ce que la page N'EST PAS  |
| ------------------------------------- | ------------------------- |
| Stack orientée ROI                    | Liste de liens sponsors   |
| Cas d'usage concrets et argumentés    | Catalogue sans filtre     |
| Alternatives comparées avec honnêteté | Page de promotion basique |
| Bonus exclusifs schoolsWP             |                           |

Elle devient : la page qu'on partage, qu'on bookmark, qu'on cite.

---

### Étape 2 — Domination SEO transactionnelle (3 couches)

**Couche 1 : Page pilier**

Mots-clés cibles : "stack WordPress" / "outils WordPress recommandés" / "meilleurs plugins WordPress business" / "outils WordPress 2026"

Longueur cible : 2 500 – 3 500 mots.

**Couche 2 : Satellites transactionnels**

Créer autour :

- Avis complet Hébergement X
- Avis complet Plugin SEO Y
- Comparatif X vs Y
- Alternative à Z

Chaque satellite renvoie vers la page ressource.

**Couche 3 : Internal linking massif**

Depuis : articles SEO, études de cas, guides, comparatifs.
Anchor text optimisé → page stack.
Objectif : signaler à Google que c'est la page centrale.

---

### Étape 3 — Amplification LinkedIn

2 carrousels / mois sur :

- "La stack idéale WordPress"
- "Pourquoi ton hébergement te pénalise"
- "La vraie différence entre ces plugins"

CTA systématique : "J'ai détaillé la stack ici." → redirection page ressource.

---

### Étape 4 — Email automatisé

- 1 séquence affiliée evergreen (7 jours)
- Bloc fixe en bas de newsletter : "Ma stack recommandée."
- Segmenter selon le clic → mini-séquences spécifiques (hébergement / SEO / LMS)

---

### Étape 5 — Bonus pour booster la conversion

| Bonus                     | Déclencheur            |
| ------------------------- | ---------------------- |
| Checklist performance     | Tout achat via lien    |
| Template funnel WordPress | Hébergement / CRM      |
| Mini audit gratuit        | Preuve d'achat envoyée |
| Guide PDF premium stack   | Achat LMS ou formation |

Plus la valeur perçue est forte, plus le clic devient rationnel.

---

### Étape 6 — Optimisation continue (mensuelle)

**Analyser :** CTR affilié / taux conversion post-clic / outils les plus rentables / sections les plus cliquées

**Optimiser :** ordre d'affichage / argumentaire / position des CTA / témoignages

---

### Objectif chiffré (12 mois)

| Étape                   | Volume     |
| ----------------------- | ---------- |
| Visiteurs/mois          | 12 000     |
| Consultent la page (8%) | 960        |
| Cliquent (20%)          | 192        |
| Achètent (5%)           | ~10 ventes |
| Commission moyenne      | 80€        |
| **CA / outil dominant** | **~800€**  |

Avec 5 outils performants : **4 000 – 6 000€/mois**

---

### Étape 7 — Positionnement premium

**Ne jamais dire :** "Voici mes liens affiliés."

**Toujours dire :** "Voici la stack que j'utiliserais si je recommençais aujourd'hui."

> Autorité > vente.

---

### Étape 8 — Roadmap progressive (12 mois)

| Période   | Actions prioritaires                           |
| --------- | ---------------------------------------------- |
| Mois 1–2  | Optimisation SEO + bonus activation            |
| Mois 3–4  | Carrousels LinkedIn + email + internal linking |
| Mois 5–6  | Comparatifs ultra détaillés par outil          |
| Mois 7–12 | Autorité forte + backlinks + interviews        |

---

### Effet long terme — Écosystème

Quand quelqu'un cherche : "meilleur hébergement WordPress" / "plugin SEO WordPress" / "CRM WordPress" / "LMS WordPress" — il entre dans l'écosystème schoolsWP et finit sur la page stack.

**Objectif final :**

| Critère        | Cible                        |
| -------------- | ---------------------------- |
| Consultations  | Page la plus visitée du site |
| Liens entrants | Page la plus linkée          |
| Partages       | Page la plus partagée        |
| Revenus        | Page la plus rentable        |

---

## PAGE RESSOURCE AFFILIÉE — VERSION LONGUE PERSUASIVE (~2 500 MOTS)

Prête à publier dans WordPress. Insérer les liens affiliés + noms d'outils.

---

### Introduction

Si tu construis un site WordPress avec une logique "bricolage", tu paieras le prix.

En performance. En SEO. En conversions. En temps perdu.

La majorité des sites WordPress échouent pour une raison simple : ils n'ont pas d'architecture.

On empile des plugins. On choisit un hébergement "pas cher". On copie une config YouTube.

Puis on se demande pourquoi le site est lent, le SEO ne décolle pas, les emails ne convertissent pas, les ventes stagnent.

Un site WordPress sérieux est un système. Et un système repose sur une stack cohérente.

Voici la mienne.

---

### 1. L'Hébergement : La Fondation Invisible

Tu peux avoir le meilleur SEO du monde. Si ton hébergement est instable, tout s'effondre.

**Pourquoi l'hébergement est stratégique**

Google prend en compte : temps de chargement, stabilité serveur, Core Web Vitals, temps de réponse.

Un hébergement médiocre peut tuer ton référencement, diminuer ton taux de conversion, créer des bugs aléatoires.

**Mon choix recommandé : [Nom Hébergeur]**

Pourquoi je le recommande : serveurs optimisés WordPress / support réellement compétent / mise en cache native / scalabilité propre / SSL et sauvegardes incluses.

Pour qui : freelances sérieux, créateurs, formateurs, sites business.
Pas pour : projet hobby ou blog expérimental.

👉 [Lien affilié]

**Bonus :** si tu passes par mon lien, je t'envoie ma checklist "Configuration performance optimale".

---

### 2. Le Plugin SEO : Le Cerveau Stratégique

Le SEO n'est pas un bouton magique. C'est une architecture.

Un bon plugin SEO doit : gérer les balises / structurer les schémas / optimiser les pages / rester léger.

**Recommandation : [Nom Plugin SEO]**

Pourquoi : gestion avancée des rich snippets / intégration WooCommerce / redirections propres / analyse on-page claire.

Il permet de travailler un cocon sémantique proprement.

Alternative sérieuse : [Alternative]

Attention : ce n'est pas le plugin qui fait le SEO. C'est la stratégie.

👉 [Lien affilié]

---

### 3. Performance & Cache : La Vitesse = Argent

Une seconde de chargement en plus peut faire chuter la conversion.

**Recommandation : [Nom Plugin Cache]**

Pourquoi : gain immédiat mesurable / compatible Core Web Vitals / paramétrage propre.

Erreur fréquente : installer 3 plugins cache. Ça crée conflits et instabilité. Un seul bon plugin suffit.

👉 [Lien affilié]

---

### 4. CRM & Email : Le Levier Caché

Un site sans capture email est un site fragile. Tu dépends de Google, des réseaux sociaux, de l'algorithme.

Un CRM transforme ton trafic en actif.

**Recommandation : [Nom CRM]**

Pourquoi : automatisation simple / segmentation intelligente / funnels natifs / intégration WordPress fluide.

Cas d'usage : lead magnet / masterclass / séquence evergreen / upsell formation.

👉 [Lien affilié]

---

### 5. LMS : Si Tu Vends une Formation

Beaucoup choisissent une plateforme externe. Erreur stratégique. WordPress + LMS = contrôle total.

**Recommandation : [Nom LMS]**

Pourquoi : paiements intégrés / gestion des étudiants / progression propre / compatible CRM.

Pour qui : coach, formateur, créateur.

👉 [Lien affilié]

---

### 6. Sécurité & Sauvegarde

Un site piraté peut détruire des années d'effort.

Recommandations : plugin sécurité léger / sauvegarde automatique quotidienne / stockage externe.

👉 [Lien affilié]

---

### Tableau récapitulatif

| Besoin      | Outil | Pourquoi             |
| ----------- | ----- | -------------------- |
| Hébergement | X     | Performance stable   |
| SEO         | X     | Structure sémantique |
| Cache       | X     | Vitesse              |
| CRM         | X     | Capture & conversion |
| LMS         | X     | Monétisation         |
| Sécurité    | X     | Protection           |

---

### Comment choisir intelligemment

Avant d'acheter, pose-toi 3 questions :

1. Quel est ton objectif business ?
2. Combien de trafic vises-tu ?
3. Vends-tu quelque chose et as-tu un funnel ?

La stack dépend de ça.

---

### Combien ça coûte réellement ?

| Outil       | Budget indicatif |
| ----------- | ---------------- |
| Hébergement | 15–30€/mois      |
| SEO         | 60–100€/an       |
| Cache       | 50€/an           |
| CRM         | 15–40€/mois      |
| LMS         | 100–200€/an      |

Total raisonnable. Un client gagné rembourse tout.

---

### Pourquoi je partage cette stack (transparence)

Oui, certains liens sont affiliés. Mais tu ne paies pas plus cher. Je recommande uniquement ce que j'utilise ou analyse sérieusement. Ça finance schoolsWP.

Je préfère un revenu propre basé sur des outils solides qu'un contenu sponsorisé douteux.

---

### Bonus schoolsWP

Si tu passes par mes liens : checklist performance / template funnel WordPress / mini guide SEO / modèle stack minimal viable.

Il suffit de m'envoyer la preuve d'achat.

---

### Le vrai message

Le problème n'est pas ton plugin. Le problème est l'absence de système.

Un site WordPress rentable repose sur : une fondation solide / une architecture SEO / une vitesse optimale / une capture intelligente / une offre claire.

La stack ne fait pas tout. Mais sans bonne stack, rien ne tient.

---

### Conclusion

Un site WordPress n'est pas un blog. C'est un actif.

Et un actif doit être : structuré / optimisé / automatisé / monétisé.

La stack que je recommande est celle qui me permet de faire ça.

Simple. Solide. Scalable.

👉 Télécharge la checklist complète
👉 Ou rejoins la newsletter schoolsWP

---

## PLAN STRATÉGIQUE — DOMINATION PAGE STACK (NIVEAU AVANCÉ)

---

### 1. Repositionner comme "Page Pilier Business"

Elle ne doit pas être "une page ressource sympa". Elle doit être la page centrale de l'écosystème.

Tous les contenus affiliés doivent pointer vers elle.

---

### 2. Ajouter 4 blocs stratégiques clés

**Bloc 1 — Promesse forte dès le haut**

Avant la liste d'outils : "Cette stack m'a permis de structurer des sites qui génèrent X."
Requis : une preuve / un résultat / un angle ROI.

**Bloc 2 — Tableau comparatif premium**

Colonnes : Pour qui / Niveau requis / ROI potentiel / Budget / Recommandé ou non.
Plus clair = plus de clics.

**Bloc 3 — Bonus exclusif différenciant**

Offrir : template funnel / checklist performance / mini formation / audit express.
L'affiliation devient : "J'achète via ton lien car j'ai plus."

**Bloc 4 — FAQ SEO transactionnelle**

- Quel est le meilleur hébergement WordPress ?
- Quel plugin SEO choisir ?
- Quelle stack pour débuter ?
- Quelle stack pour freelance ?

Impact : SEO + temps passé + conversion.

---

### 3. Intégrer dans le cocon sémantique

Créer minimum : 5 articles comparatifs / 5 avis détaillés / 5 alternatives / 3 études de cas.

Tous renvoient vers la page stack → internal linking massif → Google la considère page autorité.

---

### 4. LinkedIn stratégique (2×/mois)

Pas "voici mes outils". Plutôt :

- "Pourquoi ton hébergement te pénalise"
- "La stack minimale viable"
- "Ce que je referais en 2026"

CTA : "J'ai détaillé la stack ici."

---

### 5. Email = multiplicateur

Chaque mois : 1 rappel naturel dans la newsletter.

Format : "On me demande souvent quels outils j'utilise…"

Pas agressif. Naturel.

---

### 6. Segmentation CRM pour maximiser le revenu

| Clic sur... | Mini-séquence déclenchée | Contenu                           |
| ----------- | ------------------------ | --------------------------------- |
| Hébergement | Performance              | 3 emails + bonus performance      |
| Plugin SEO  | SEO avancé               | 3 emails + bonus SEO              |
| LMS         | Monétisation formation   | 3 emails + bonus funnel formation |

---

### 7. Objectif chiffré par phase

| Phase    | Visiteurs page/mois | Clic affilié | Conversion | CA estimé    |
| -------- | ------------------- | ------------ | ---------- | ------------ |
| Phase 1  | 3 000               | 10%          | 5%         | ~1 200€/mois |
| Phase 2  | 8 000               | 15%          | 5%         | ~4 800€/mois |
| Optimisé | + bonus + email     |              |            | **5 000€+**  |

---

### 8. Optimisations avancées (domination)

- **Preuve sociale** : témoignages, screenshots résultats, mini études de cas
- **Heatmap/tracking** : identifier où les gens cliquent et quelle section convertit
- **Comparateur interactif** : mini quiz "Quel outil est fait pour toi ?" → recommandation personnalisée → CTR ×2

---

### 9. Vision 12 mois

La page doit ranker sur : "stack WordPress" / "meilleur plugin WordPress" / "meilleur hébergement WordPress"

Elle doit concentrer **30 à 50% des revenus affiliés**.

Ce qui la rendra imbattable : la logique / le contexte / le ROI / la pédagogie / la transparence.

---

### Résultat attendu (12 mois)

| Indicateur        | Impact                             |
| ----------------- | ---------------------------------- |
| Cashflow mensuel  | Finance le contenu schoolsWP       |
| Stabilité revenus | Réduit pression sur les lancements |
| Autorité SEO      | Renforce la crédibilité globale    |
| Actif evergreen   | Tourne sans intervention continue  |

---

## PRÉVISIONNEL AFFILIATION 12 MOIS — VERSION DÉTAILLÉE PAR PHASE

Hypothèses : commission moyenne 70€ / taux clic affilié 8–12% / taux conversion post-clic 4–6% / SEO progressif / séquence email evergreen active dès M2.

---

### Tableau mensuel

| Mois | Visiteurs/mois | Clics affiliés | Ventes | Commission | CA mensuel |
| ---- | -------------- | -------------- | ------ | ---------- | ---------- |
| M1   | 1 500          | 90             | 4      | 70€        | 280€       |
| M2   | 2 000          | 160            | 8      | 70€        | 560€       |
| M3   | 3 000          | 300            | 15     | 70€        | 1 050€     |
| M4   | 4 000          | 420            | 20     | 70€        | 1 400€     |
| M5   | 5 500          | 550            | 27     | 70€        | 1 890€     |
| M6   | 7 000          | 700            | 35     | 70€        | 2 450€     |
| M7   | 8 500          | 850            | 43     | 70€        | 3 010€     |
| M8   | 10 000         | 1 000          | 50     | 70€        | 3 500€     |
| M9   | 12 000         | 1 320          | 66     | 70€        | 4 620€     |
| M10  | 13 500         | 1 485          | 74     | 70€        | 5 180€     |
| M11  | 15 000         | 1 650          | 82     | 70€        | 5 740€     |
| M12  | 18 000         | 1 980          | 99     | 70€        | 6 930€     |

---

### Phases stratégiques

| Phase             | Mois    | Actions clés                                                      | Objectif mensuel |
| ----------------- | ------- | ----------------------------------------------------------------- | ---------------- |
| Mise en place     | M1–M3   | Page ressource + 5 articles transac + séquence email + carrousels | 1 000€           |
| Accélération      | M4–M6   | 10 articles optimisés + internal linking + segmentation email     | 2 500€           |
| Effet SEO         | M7–M9   | Pages rankent + comparatifs dominants + email+LI convertissent    | 4 000€           |
| Stabilisation 5K+ | M10–M12 | Optimisation conversion + top 3 outils + codes promo + MAJ        | 5 000–7 000€     |

---

### Répartition idéale des revenus à M12

| Catégorie   | CA estimé   |
| ----------- | ----------- |
| Hébergement | 2 200€      |
| Plugin SEO  | 1 200€      |
| CRM         | 900€        |
| LMS         | 1 000€      |
| Autres      | 600€        |
| **Total**   | **~6 900€** |

Diversification = stabilité.

---

### Leviers d'accélération

- Bonus exclusif par outil
- Études de cas réelles avec chiffres
- Comparatifs ultra détaillés
- Mise à jour pages tous les 3 mois
- Retargeting email segmenté

---

### Facteur déterminant

Ce n'est pas le nombre d'articles. C'est **le trafic transactionnel ciblé**.

---

### Objectif stratégique à 12 mois

L'affiliation doit couvrir : hébergement + outils + éventuellement freelance + partie du revenu personnel.

Elle finance le développement formation + consulting schoolsWP.

---

## SYSTÈME EVERGREEN AUTOMATISÉ

Architecture complète pour transformer le trafic SEO en revenus d'affiliation passifs sans intervention manuelle continue.

---

### Vue d'ensemble du flux

```
SOURCE DE TRAFIC
    ↓
[SEO] Articles transactionnels / comparatifs / page ressource
[LinkedIn] Posts + carrousels → redirect blog
[Email] Séquence 7 jours → articles ciblés

    ↓
CAPTURE LEAD
Lead magnet → Checklist / Guide / Comparatif PDF
Formulaire OptinMonster ou FluentForms

    ↓
SÉQUENCE EMAIL EVERGREEN (7 JOURS)
J0 : Bienvenue + lead magnet
J1 : Problème + contexte
J3 : Solution + outil #1 (lien affilié)
J5 : Cas pratique + outil #2 (lien affilié)
J7 : Offre directe + page ressource complète

    ↓
SEGMENTATION COMPORTEMENTALE
FluentCRM : tag selon clic (Formation / Consulting / Affiliation / Non-engagé)

    ↓
OFFRE ADAPTÉE PAR SEGMENT
Formation → page vente Authority System™
Consulting → formulaire diagnostic gratuit
Affiliation → page ressource outils recommandés
Non-engagé → séquence nurturing 30 jours

    ↓
BOUCLE NURTURING
Newsletter mensuelle → nouveaux articles → nouveaux liens affiliés
```

---

### Les 4 piliers du système evergreen

| Pilier             | Rôle                                    | Fréquence           |
| ------------------ | --------------------------------------- | ------------------- |
| SEO transactionnel | Apporte trafic qualifié en continu      | Articles 1x/semaine |
| Lead magnet        | Capture email en échange de valeur      | Set une fois        |
| Séquence 7 jours   | Éduque + recommande + convertit         | Automatique         |
| Segmentation tags  | Personnalise l'offre selon comportement | Temps réel          |

---

### Contenu du lead magnet optimal

**Option A — Checklist** : "7 outils indispensables pour créer une formation WordPress rentable"
**Option B — Guide PDF** : "Comparatif complet hébergement WordPress : les 5 meilleurs en 2025"
**Option C — Mini-formation** : "Lancer ta première formation WordPress en 7 jours" (email-cours)

Critère de choix : Option A si débutant en email marketing, Option C si liste existante.

---

### Règles d'or du système evergreen

- Un seul lead magnet principal — ne pas disperser
- La séquence 7 jours ne vend qu'un outil par email
- Le lien affilié arrive après la valeur, jamais avant
- Chaque email a un seul CTA
- La page ressource est le hub central vers lequel tout renvoie
- Mise à jour trimestrielle des liens affiliés (vérifier commissions + disponibilité)

---

### Indicateurs de performance

| KPI                       | Cible M3 | Cible M6   | Cible M12    |
| ------------------------- | -------- | ---------- | ------------ |
| Taux ouverture séquence   | 35–40%   | 40–45%     | 45%+         |
| Taux clic email affilié   | 6–8%     | 8–12%      | 10–15%       |
| Taux conversion post-clic | 3–5%     | 4–6%       | 5–7%         |
| Revenus séquence/mois     | 200–500€ | 500–1 500€ | 1 500–3 000€ |

---

## SCHÉMA EXACT D'AUTOMATION — FLUENTCRM

Structure technique complète à reproduire dans FluentCRM pour automatiser l'ensemble du parcours affilié.

---

### Trigger principal

**Déclencheur** : Soumission formulaire lead magnet
**Action immédiate** :

1. Ajouter contact à liste "Prospects Affiliation"
2. Appliquer tag `Lead-Nouveau`
3. Démarrer séquence email "Affiliation Evergreen 7J"
4. Score +10 points

---

### Automation 1 — Séquence Evergreen 7 Jours

```
TRIGGER : Tag ajouté = Lead-Nouveau

J0 (immédiat)
→ Email : "Voici ton [lead magnet] + bienvenue"
→ Tag : Lead-Séquence-Active

J1 (+24h)
→ Email : "Le vrai problème avec WordPress et les formations"
→ Si clic lien → Score +5

J3 (+72h)
→ Email : "L'outil que j'utilise pour [cas précis] — mon avis honnête"
→ Lien affilié outil #1
→ Si clic lien affilié → Tag : Intérêt-[Catégorie-Outil]

J5 (+120h)
→ Email : "Ce que j'aurais aimé savoir avant de choisir mon hébergement"
→ Lien affilié outil #2
→ Si clic lien affilié → Tag : Intérêt-Hébergement

J7 (+168h)
→ Email : "Tous mes outils recommandés en un seul endroit"
→ Lien page ressource
→ Si clic → Tag : Lead-Qualifié + Score +20
→ Fin séquence → Branchement comportemental
```

---

### Automation 2 — Branchement Formation

```
TRIGGER : Tag = Intérêt-Formation

→ Email J+1 : Présentation Authority System™
→ Email J+3 : Témoignage + cas concret
→ Email J+5 : Offre + bonus exclusif
→ Si achat → Tag : Client-Formation + retirer Lead-Qualifié
→ Si pas d'achat J+7 → Automation Newsletter mensuelle
```

---

### Automation 3 — Branchement Consulting

```
TRIGGER : Tag = Intérêt-Consulting

→ Email J+1 : "Tu veux qu'on travaille ensemble ?"
→ CTA : Formulaire diagnostic gratuit
→ Si formulaire rempli → Tag : Client-Consulting-Prospect + Score +50
→ Notification interne (email à Michael)
→ Si pas de formulaire J+5 → Automation Newsletter mensuelle
```

---

### Automation 4 — Branchement Affiliation (intérêt outils)

```
TRIGGER : Tag = Intérêt-Affiliation OU Intérêt-Hébergement OU Intérêt-LMS

→ Email J+1 : Comparatif détaillé de la catégorie d'intérêt
→ Liens affiliés ciblés selon tag
→ Email J+3 : Article de blog approfondi sur l'outil
→ Si clic affilié → Score +10
→ J+7 → Automation Newsletter mensuelle
```

---

### Automation 5 — Non-engagés (nurturing 30 jours)

```
TRIGGER : Fin séquence 7J SANS clic sur aucun lien

→ Tag : Non-engagé
→ Email J+14 : Contenu valeur pure (article SEO récent)
→ Email J+21 : Ressource gratuite différente
→ Email J+30 : Dernière chance — lien page ressource
→ Si toujours pas de clic → Tag : Inactif + retirer de liste active
→ Campagne réactivation dans 90 jours
```

---

### Structure tags recommandée

| Catégorie | Tags                                                                   |
| --------- | ---------------------------------------------------------------------- |
| Source    | LM-SEO, LM-LinkedIn, LM-Email, LM-Autre                                |
| Intérêt   | Intérêt-Formation, Intérêt-Consulting, Intérêt-Affiliation             |
| Outil     | Intérêt-Hébergement, Intérêt-LMS, Intérêt-CRM, Intérêt-PageBuilder     |
| Statut    | Lead-Nouveau, Lead-Séquence-Active, Lead-Qualifié, Non-engagé, Inactif |
| Client    | Client-Formation, Client-Consulting-Prospect, Client-Payant            |

---

### Scoring leads

| Action                            | Points |
| --------------------------------- | ------ |
| Soumission formulaire lead magnet | +10    |
| Clic sur lien email               | +5     |
| Clic sur lien affilié             | +10    |
| Clic sur page ressource           | +20    |
| Formulaire diagnostic rempli      | +50    |
| Achat formation                   | +100   |

**Seuils** : 0–20 → cold | 21–50 → warm | 51+ → hot (relance manuelle possible)

---

### KPI stratégiques à suivre chaque mois

| Métrique                        | Source              | Fréquence     |
| ------------------------------- | ------------------- | ------------- |
| Nouveaux leads/mois             | FluentCRM           | Mensuelle     |
| Taux complétion séquence 7J     | FluentCRM           | Mensuelle     |
| Revenus affiliés générés        | Dashboards affiliés | Mensuelle     |
| Taux conversion lead → client   | FluentCRM           | Trimestrielle |
| Articles en top 10 Google       | GSC                 | Mensuelle     |
| Trafic organique transactionnel | GA4                 | Mensuelle     |

---

### Règle d'or automation

**Ne pas sur-automatiser.** Le système doit sembler humain. Maximum 1 email tous les 2 jours. Jamais plus de 2 liens affiliés par email. Toujours 80% valeur / 20% promotion.

---

## SCRIPTS DM LINKEDIN — PUSH VERS PAGE RESSOURCE

Logique invariable : ne jamais envoyer le lien au premier message.

**Séquence en 3 temps : Diagnostic → Valeur → Ressource**

---

### Scénario 1 — Après un commentaire "stack" sous un carrousel

**Message 1**

> Merci pour ton commentaire.
> Tu es plutôt sur quel type de projet en ce moment ? (blog, client, formation…)

**Message 2** (après réponse)

> OK je vois.
> Le point clé dans ton cas, c'est surtout [performance / SEO / structure].
> Beaucoup sous-estiment cette partie.

**Message 3**

> J'ai structuré une page avec la stack complète que je recommande selon les cas.
> Ça peut t'aider à éviter les erreurs classiques.
> Je te l'envoie ?

**Message 4** (après validation)

> Voici la page 👇
> [Lien vers page ressource]
>
> Regarde surtout la partie [hébergement / SEO / CRM], c'est là que ça change vraiment la donne.

---

### Scénario 2 — DM inbound spontané

Quelqu'un demande : "Tu recommandes quoi comme plugin SEO ?"

**Réponse**

> Ça dépend de ton objectif.
> Tu cherches plutôt trafic long terme ou optimisation locale ?

**Suite**

> Dans 80% des cas, j'oriente vers [outil] pour [raison stratégique].
> J'ai détaillé les différences ici :
> [Lien page ressource]
>
> Si tu veux, je peux aussi te dire ce que j'éviterais selon ton contexte.

---

### Scénario 3 — Prospect consulting léger

Quelqu'un publie : "Mon site est lent."

**Message 1**

> Je viens de voir ton post.
> 9 fois sur 10, le problème vient de la base (hébergement + cache).
> Tu es chez qui actuellement ?

**Message 2**

> OK je comprends.
> Dans ton cas, je regarderais surtout [élément].
>
> J'ai synthétisé ma stack recommandée ici :
> [Lien]
>
> Ça peut déjà te donner une direction claire.

---

### Scénario 4 — Relance douce

Après qu'une personne a cliqué mais n'a pas réagi :

> Tu as pu jeter un œil à la stack ?
> Curieux de savoir ce que tu utilises aujourd'hui.

---

### Scénario 5 — Bonus exclusif pour doubler la conversion

> Si tu passes par mon lien, envoie-moi la preuve d'achat et je t'envoie :
> – La checklist performance
> – Le modèle funnel
>
> Ça t'évite pas mal d'erreurs.

---

### Règles d'or DM

- Toujours poser une question avant de donner le lien
- Toujours contextualiser selon le projet de l'interlocuteur
- Ne jamais spammer, ne jamais envoyer le lien en masse
- Toujours parler ROI, pas outil

---

### Volume hebdomadaire minimal

| Action                       | Fréquence    |
| ---------------------------- | ------------ |
| Carrousels stack publiés     | 2/semaine    |
| Conversations DM ouvertes    | 5–10/semaine |
| Envois ciblés page ressource | 3–5/semaine  |

**Projection conservative** : 10 envois/semaine × 20% clic × 10% conversion = 1–2 ventes/semaine.

---

### Version avancée — LinkedIn comme canal affilié discret

1. **Réponses rapides LinkedIn** — pré-rédiger les 5 scénarios pour gain de temps
2. **Tag FluentCRM "Intéressé-Stack"** — dès qu'un contact clique sur la page via DM
3. **Mini séquence email post-DM** — 3 emails sur 5 jours pour nurturing après contact LinkedIn
   - J0 : Récap page ressource + contexte personnalisé
   - J2 : Article comparatif ciblé selon intérêt
   - J4 : Bonus exclusif + lien affilié direct

**Ce qui transforme LinkedIn en canal affilié structuré, pas aléatoire.**

---

## SÉQUENCE EMAIL EVERGREEN 7 JOURS — PRÊTE À INJECTER

Lead magnet : "Le modèle WordPress en levier business"
Objectif : Vente formation OU RDV consulting
Ton : direct, pédagogique, orienté business
Segmentation FluentCRM : clic Formation → tag Formation | clic Audit → tag Consulting | aucun clic → nurturing long terme

---

### Email 1 — J0 — Le Déclic

**Objet : Pourquoi ton site ne génère rien**

Tu as peut-être du trafic.
Tu as peut-être un beau site.

Mais si ton site ne génère pas d'opportunités régulières…
ce n'est pas un levier.

C'est une vitrine.

Le problème n'est pas WordPress.
Le problème, c'est l'absence de système.

Un site doit faire 3 choses :

- Attirer un trafic qualifié
- Capturer une audience
- Diriger vers une offre claire

Demain, je te montre pourquoi 90% des sites échouent.

— Michaël

---

### Email 2 — J1 — Le Mythe du Trafic

**Objet : Le trafic ne sert à rien (si…)**

On t'a vendu le trafic comme solution.

"Plus de visiteurs = plus de clients."

Faux.

Le trafic sans structure = bruit.

La vraie question :

- Où vont tes visiteurs ?
- Que doivent-ils faire ?
- Quelle est l'étape suivante ?

Si tu ne peux pas répondre clairement,
tu n'as pas un système.

Demain, je te partage le modèle exact que j'utilise.

— Michaël

---

### Email 3 — J3 — Le Modèle schoolsWP

**Objet : Le modèle en 3 piliers**

Voici la structure simple :

**Pilier 1 — Trafic stratégique**
SEO ciblé. Intent claire. Cluster structuré.

**Pilier 2 — Capture intelligente**
Lead magnet précis. Email. Séquence courte.

**Pilier 3 — Offre claire**
Formation. Consulting. Affiliation.

Si un pilier manque, tout s'effondre.

La majorité travaille uniquement le pilier 1.

Erreur.

Je détaille le plan complet ici :
[👉 Lire le guide complet]

— Michaël

---

### Email 4 — J4 — La Preuve

**Objet : 2 000 visiteurs → 3 500€**

Un freelance que j'ai accompagné :

2 000 visiteurs / mois
0 système
0 capture

Résultat : quasi aucun client inbound.

On a :

- Créé un lead magnet précis
- Structuré une séquence simple
- Clarifié l'offre

Résultat : 3 500€ / mois en 90 jours.

Pas plus de trafic.
Juste plus de structure.

Demain, je t'explique l'erreur qui bloque la majorité.

— Michaël

---

### Email 5 — J5 — L'Erreur Structurelle

**Objet : Ce que 90% des freelances WP font mal**

Ils publient.

Ils optimisent.

Ils testent des plugins.

Mais ils ne construisent pas un système.

WordPress n'est pas un site.
C'est une machine.

Si ton site n'a pas :

- Un parcours clair
- Une offre visible
- Une capture stratégique

Tu perds de l'énergie.

Si tu veux structurer ça sérieusement,
je peux t'accompagner.

— Michaël

---

### Email 6 — J6 — L'Opportunité

**Objet : Structurer ton système en 30 jours**

Voici un plan simple :

Semaine 1 → Audit & positionnement
Semaine 2 → Capture & séquence
Semaine 3 → Offre claire
Semaine 4 → Optimisation

En 30 jours, ton site peut devenir un levier.

Si tu veux aller plus vite :

- Je propose un accompagnement stratégique
- Ou une formation complète SEO & Funnel WordPress

Les deux sont détaillés ici :

[👉 Découvrir la formation]
[👉 Réserver un appel stratégique]

— Michaël

---

### Email 7 — J7 — La Décision

**Objet : Dernier message**

Tu as maintenant :

- Le problème
- Le modèle
- La preuve
- Le plan

La question est simple :

Est-ce que tu laisses ton site continuer comme avant ?

Ou est-ce que tu le transformes en levier ?

Si tu veux passer à l'étape suivante :

[👉 Formation]
[👉 Audit stratégique]

Je ferme les créneaux cette semaine.

— Michaël

---

### Segmentation FluentCRM à configurer

| Clic sur                 | Tag à appliquer    | Suite                         |
| ------------------------ | ------------------ | ----------------------------- |
| Lien "Formation"         | Intérêt-Formation  | Automation branche Formation  |
| Lien "Audit stratégique" | Intérêt-Consulting | Automation branche Consulting |
| Aucun clic sur 7 jours   | Non-engagé         | Nurturing long terme 30 jours |

---

### Objectif de la séquence

Installer l'autorité → Clarifier le problème → Montrer la méthode → Donner une preuve → Proposer l'action.

Sans forcer. Mais sans flou.

---

## ARCHITECTURE FLUENTCRM — STACK SCHOOLSWP COMPLÈTE

Implémentation concrète dans la stack WordPress : WordPress + Fluent Forms + FluentCRM + (optionnel) TutorLMS / WooCommerce.

---

### Architecture globale

```
Trafic (SEO / LinkedIn / YouTube)
        ↓
Landing page (Lead Magnet)
        ↓
Fluent Forms
        ↓
FluentCRM (Tag + Séquence)
        ↓
Segmentation comportementale
        ↓
Offre adaptée
```

---

### 1. Structure des listes

**1 seule liste principale** : `schoolsWP – Main Audience`

Tout repose sur les tags. Ne pas multiplier les listes.

---

### 2. Nomenclature des tags

| Namespace    | Tags                                                             |
| ------------ | ---------------------------------------------------------------- |
| Source       | `src_linkedin`, `src_seo`, `src_youtube`                         |
| Intérêt      | `int_seo`, `int_funnel`, `int_stack`, `int_consulting`           |
| Maturité     | `lvl_beginner`, `lvl_freelance`, `lvl_agency`                    |
| Comportement | `click_offer`, `click_audit`, `click_affiliation`, `no_click_7d` |
| Température  | `lead_cold`, `lead_warm`, `lead_hot`                             |

---

### 3. Automation — Inscription Lead Magnet

**Trigger** : "When contact is added via Fluent Form – Funnel WP"

**Actions immédiates** :

- Add to list : `schoolsWP – Main Audience`
- Add tag : `int_funnel` + `src_linkedin` (si page dédiée)
- Start sequence : `SEQ_7J_Funnel`

---

### 4. Séquence 7 jours dans FluentCRM

Créer une Email Sequence nommée `SEQ_7J_Funnel` :

| Jour | Email   |
| ---- | ------- |
| J0   | Email 1 |
| J1   | Email 2 |
| J2   | Email 3 |
| J3   | Email 4 |
| J4   | Email 5 |
| J5   | Email 6 |
| J6   | Email 7 |

---

### 5. Segmentation intelligente

Après Email 3, conditions :

**Si clic "Formation SEO"**
→ Add tag `int_seo` + `lead_warm`
→ Remove from `SEQ_7J_Funnel`
→ Start `SEQ_SEO_Conversion`

**Si clic "Audit"**
→ Add tag `int_consulting` + `lead_hot`
→ Send internal notification
→ Send email "Réserver un appel"

**Si aucun clic après 7 jours**
→ Add tag `no_click_7d` + `lead_cold`
→ Start `SEQ_Nurturing_LongTerm`

---

### 6. Branches dédiées

**`SEQ_SEO_Conversion`** (4 emails) : Checklist SEO → Cas client → Erreurs techniques → Offre formation SEO

**`SEQ_Consulting`** (3 emails) : Ce que j'analyse dans un audit → Résultats clients → Lien Calendly

**`SEQ_Affiliation`** : Stack recommandée → Comparatif détaillé → Bonus exclusif

---

### 7. Boucle nurturing long terme

Après 14 jours sans conversion → Start `SEQ_Newsletter_Weekly` (autorité + contenu stratégique + lancements ponctuels)

---

### 8. Lead Scoring FluentCRM

| Action                  | Points |
| ----------------------- | ------ |
| Clic email              | +5     |
| Clic offre              | +10    |
| Page checkout visitée   | +15    |
| Formulaire audit rempli | +20    |

Si score > 40 → Tag `lead_hot` + email personnalisé + notification interne

---

### 9. Mapping offres par tag

| Tag principal    | Offre finale       |
| ---------------- | ------------------ |
| `int_seo`        | Formation SEO WP   |
| `int_funnel`     | Formation Funnel   |
| `int_consulting` | Consulting Premium |
| `int_stack`      | Affiliation        |

---

### 10. Version avancée — Automations additionnelles

- Automation "Abandon checkout"
- Automation "Non ouverture 30 jours"
- Automation "Client → Upsell"
- Automation "Formation → Programme premium"

---

### Règle schoolsWP

1 seule liste. Tags propres. Automations claires. Pas de complexité inutile. Toujours relier à une offre.

---

### Projection

300 leads/mois × 3% conversion formation 297€ + 1% consulting 2 000€ = système stable à >3 500€/mois récurrent.

---

## STRUCTURE CRM SEGMENTÉE — DÉBUTANT / FREELANCE / AGENCE

Transformer FluentCRM en cerveau business segmenté par maturité. Pas une liste d'emails — un pipeline.

---

### Principe fondamental

1 seule liste. Segmentation par tags de maturité. Automations conditionnelles. Offres adaptées au niveau.

**Liste unique** : `schoolsWP – Audience Principale`

---

### Tags de maturité (pilier central)

| Tag             | Profil                             |
| --------------- | ---------------------------------- |
| `lvl_beginner`  | Débutant — crée son premier site   |
| `lvl_freelance` | Freelance — structure son business |
| `lvl_agency`    | Agence — scale et automatise       |

Règle : chaque contact a **1 seul niveau actif** à la fois.

---

### Détection du niveau

**Option A — Formulaire intelligent (recommandé)**

Dans Fluent Forms, question obligatoire :

> "Quel est ton profil ?"
>
> - Je débute → tag `lvl_beginner`
> - Je suis freelance → tag `lvl_freelance`
> - Je gère une agence → tag `lvl_agency`

**Option B — Segmentation comportementale**

- Clic "Créer son site" → `lvl_beginner`
- Clic "Audit client" → `lvl_freelance`
- Clic "Scaling agence" → `lvl_agency`

---

### Segment Débutant — `lvl_beginner`

**Objectif** : Éducation → Confiance → Formation entrée de gamme

**Séquences** : `SEQ_Beginner_Onboarding` → `SEQ_Beginner_Education` → `SEQ_Formation_Fondamentaux`

**Contenus** : Bases WordPress, stack simple, SEO fondamental, erreurs à éviter

**Offre principale** : Formation WordPress Essentielle — 97–197€

---

### Segment Freelance — `lvl_freelance`

**Objectif** : Structuration business → Funnel → Monétisation

**Séquences** : `SEQ_Freelance_Structure` → `SEQ_Freelance_Funnel` → `SEQ_Freelance_SEO_Avancé`

**Contenus** : Stack premium, audit client, positionnement, process projet

**Offre principale** : Formation SEO/Funnel + Templates + Coaching de groupe — 297–997€

---

### Segment Agence — `lvl_agency`

**Objectif** : Scaling → Automatisation → Consulting premium

**Séquences** : `SEQ_Agency_Scaling` → `SEQ_Agency_Automation` → `SEQ_Agency_Premium`

**Contenus** : Process équipe, automatisation CRM, récurrence, upsell clients

**Offre principale** : Consulting stratégique + Programme premium — 2 000€+

---

### Logique d'évolution dynamique

```
lvl_beginner → [30 jours + clic contenu avancé]
→ Retirer lvl_beginner
→ Ajouter lvl_freelance
→ Lancer SEQ_Freelance_Structure

lvl_freelance → [30 jours + comportement avancé]
→ Retirer lvl_freelance
→ Ajouter lvl_agency
→ Lancer SEQ_Agency_Scaling
```

Le CRM accompagne la progression. Pas de cases figées.

---

### Mapping offres par niveau

| Niveau          | Offre principale       | Ticket moyen |
| --------------- | ---------------------- | ------------ |
| `lvl_beginner`  | Formation fondamentale | 97–197€      |
| `lvl_freelance` | Formation avancée      | 297–997€     |
| `lvl_agency`    | Consulting / Programme | 2 000€+      |

---

### Tags transversaux (s'appliquent à tous les niveaux)

- Intérêt : `int_seo`, `int_funnel`, `int_automation`, `int_affiliation`
- Température : `lead_cold`, `lead_warm`, `lead_hot`

---

### KPI à suivre par segment

| KPI                          | Fréquence     |
| ---------------------------- | ------------- |
| Open rate par niveau         | Mensuelle     |
| CTR par niveau               | Mensuelle     |
| Conversion par offre         | Mensuelle     |
| Passage Beginner → Freelance | Trimestrielle |
| Passage Freelance → Agency   | Trimestrielle |

---

### Vision finale

FluentCRM = pipeline évolutif basé sur la maturité.
Message ultra-pertinent → meilleur taux de conversion → upsell naturel → positionnement premium progressif.

```
Audience Principale
   ↓ Tag Niveau
   ↓ Séquence adaptée
   ↓ Segmentation comportementale
   ↓ Offre correspondante
   ↓ Upsell niveau supérieur
```

---

## WEBINAIRE EVERGREEN — INTÉGRÉ FLUENTCRM

Transformer le trafic SEO + LinkedIn en ventes formation et RDV consulting. Sans live permanent. 100% stack WordPress.

---

### Architecture globale

```
Trafic (SEO / LinkedIn)
   ↓ Landing Webinaire
   ↓ Inscription (Fluent Forms)
   ↓ Séquence Pré-Webinaire (3 emails)
   ↓ Page Replay Evergreen
   ↓ Pitch Offre
   ↓ Séquence Post-Webinaire
   ↓ Relances + Segmentation
```

---

### Stack recommandée (100% WordPress)

WordPress + Fluent Forms + FluentCRM + vidéo hébergée (Vimeo / Bunny / YouTube non listé)
Optionnel : WooCommerce + TutorLMS — pas besoin d'outil externe type WebinarJam.

---

### 1. Landing page webinaire

**Titre** : "Comment transformer WordPress en machine à revenus en 30 jours"

Contenu : promesse claire, 3 bénéfices concrets, pour qui, ce que tu vas apprendre, formulaire Fluent Forms.

**Tags ajoutés à l'inscription** : `event_webinar`, `int_funnel`, `lead_warm`

**Déclenche** : `AUTO_Webinar_PreSequence`

---

### 2. Séquence pré-webinaire (3 emails)

**Email 1 — Immédiat**

> Objet : Ton accès au webinaire
>
> Lien accès + ce que tu vas découvrir + invitation à répondre.

**Email 2 — J+1**

> Objet : Pourquoi 90% des sites WP ne convertissent pas
>
> Micro tension + rappel du lien.

**Email 3 — J+2**

> Objet : Regarde-le avant qu'il disparaisse
>
> Urgence douce + rappel transformation.

---

### 3. Page replay evergreen — Structure

1. Hook fort (3 premières minutes)
2. Agitation problème
3. Modèle schoolsWP
4. Cas réel
5. Transition naturelle vers offre
6. Pitch formation / consulting
7. Bonus limité

---

### 4. Pitch intégré

- Formation signature : 497€ ou 997€
- Bonus stack outils + template exclusif
- Timer evergreen (facultatif)

---

### 5. Tracking comportemental dans FluentCRM

| Événement            | Tag à ajouter      |
| -------------------- | ------------------ |
| Visionne le replay   | `watched_webinar`  |
| Clique sur l'offre   | `clicked_offer`    |
| Commence le checkout | `checkout_started` |
| Achète               | `client_formation` |

---

### 6. Automation principale FluentCRM

```
TRIGGER : Tag event_webinar

→ Wait 1h → Email 1 (accès)
→ Wait 24h → Email 2 (tension)
→ Wait 24h → Email 3 (urgence)

→ Condition :
   IF tag clicked_offer
   → Start SEQ_ObjectionHandling

   ELSE
   → Start SEQ_Reminder
```

---

### 7. Séquences post-webinaire

**Si regarde mais ne clique pas** — SEQ_Reminder (4 emails)

- E1 : Résumé modèle
- E2 : Erreurs fréquentes
- E3 : Cas client
- E4 : Rappel offre + bonus

**Si clique mais n'achète pas** — SEQ_ObjectionHandling (3 emails)

- E1 : Réponse objections
- E2 : FAQ
- E3 : Dernier rappel

**Si achète** :
→ Tag `client_formation` + retirer des séquences de vente + lancer onboarding

---

### KPI cibles

| Métrique                 | Benchmark |
| ------------------------ | --------- |
| Taux inscription landing | 30–40%    |
| Taux visionnage          | 30–50%    |
| Conversion formation     | 5–12%     |
| Conversion consulting    | 1–3%      |

---

### Simulation

500 inscrits/mois × 8% conversion × 497€ = **~19 900€/mois potentiel brut** (evergreen).

---

### Version domination

- Retargeting Meta sur visiteurs landing
- Retargeting Google/YouTube viewers
- Upsell programme premium post-achat
- Webinaire avancé dédié consulting

---

### Vision globale

```
LinkedIn → Lead Magnet → Webinaire → Formation → Upsell
SEO → Article → Webinaire → Formation → Consulting
```

Tout converge vers le même moteur evergreen.

---

## WEBINAIRE EVERGREEN AUTOMATISÉ — STRUCTURE COMPLÈTE

### Structure du webinaire (60–75 min)

| Bloc               | Durée     | Contenu                                                                |
| ------------------ | --------- | ---------------------------------------------------------------------- |
| Hook               | 5 min     | Pourquoi 90% des sites WP ne génèrent rien — créer tension             |
| Problème structuré | 10 min    | Absence funnel, mauvaise stack, pas d'offre — faire prendre conscience |
| Modèle schoolsWP   | 25 min    | 3 piliers : Trafic stratégique / Capture intelligente / Offre claire   |
| Étude de cas       | 10 min    | Avant/après chiffré — crédibilité                                      |
| Transition offre   | 5 min     | "Si tu veux le système complet, je t'ai préparé quelque chose."        |
| Pitch              | 10–15 min | Modules, bonus, résultat, pour qui, prix, garantie, CTA                |

---

### Architecture 100% WordPress — FluentCRM + TutorLMS

**Pages à créer**

| URL                 | Rôle                               |
| ------------------- | ---------------------------------- |
| `/webinaire`        | Landing inscription                |
| `/merci-webinaire`  | Confirmation + teaser              |
| `/replay-webinaire` | Page replay (protégée ou TutorLMS) |
| `/offre-formation`  | Page vente                         |
| `/checkout`         | TutorLMS / WooCommerce             |
| `/merci-commande`   | Confirmation + onboarding          |

**Accès replay — Option A** : lien direct + relances email (simple)
**Accès replay — Option B** : cours gratuit TutorLMS avec vidéo + chapitres + ressources + CTA formation (plus premium)

---

### Nomenclature FluentCRM

**Listes** : `L_Webinar_Evergreen`, `L_Customers`

**Tags**

| Catégorie   | Tags                                                                                         |
| ----------- | -------------------------------------------------------------------------------------------- |
| Source      | `src:webinar`                                                                                |
| Statut      | `webinar:registered`, `webinar:replay_clicked`, `webinar:offer_clicked`, `webinar:purchased` |
| Température | `temp:hot`, `temp:warm`, `temp:cold`                                                         |
| Intérêt     | `interest:seo`, `interest:funnel`, `interest:tools`                                          |

---

### Automation 1 — Inscription webinaire

**Trigger** : Tag `webinar:registered`

```
Email 1 (immédiat) : Confirmation + lien replay + "réponds avec ton objectif"
Wait 1 jour
Email 2 : "Le vrai problème n'est pas le trafic" + lien replay
Wait 1 jour
Email 3 : "Le modèle 3 piliers" + lien replay
Wait 2 jours
Condition : SI webinar:replay_clicked → sortir
SINON → Email 4 : "Dernier rappel replay"
Après 7j sans clic → Tag temp:cold
```

---

### Automation 2 — Replay → Offre

**Trigger** : Tag `webinar:replay_clicked`

```
Wait 2h
Email 1 : Synthèse modèle + lien offre
→ Si clic offre : Tag webinar:offer_clicked + temp:hot
Wait 1 jour
Email 2 : Étude de cas chiffrée + lien offre
Wait 1 jour
Email 3 : Objection "pas le temps" + lien offre + garantie
Wait 1 jour
Email 4 : Dernier rappel bonus + CTA fort
```

---

### Automation 3 — Achat formation

**Trigger** : Purchase WooCommerce OU Course Enrolled (TutorLMS)

```
Apply tag webinar:purchased
Remove tags temp:hot / temp:warm / temp:cold
Stop automations webinar en cours
Add to L_Customers
Start Automation 4 (Onboarding)
```

---

### Automation 4 — Onboarding formation (7 jours)

```
J0 : Bienvenue + où commencer
J2 : Module 1 + quick win
J4 : Module 2 + erreur fréquente
J7 : Check-in + upsell soft consulting
```

---

### Automation 5 — Nurturing long terme

**Trigger** : Tag `temp:cold`

```
Entrée dans SEQ_Newsletter_Weekly
Tous les 21 jours : email soft "Le replay est toujours dispo"
```

---

### Tracking clics dans FluentCRM

| Lien dans l'email   | Tag à appliquer          |
| ------------------- | ------------------------ |
| Lien replay         | `webinar:replay_clicked` |
| Lien offre          | `webinar:offer_clicked`  |
| Lien article SEO    | `interest:seo`           |
| Lien audit/Calendly | `interest:funnel`        |

---

### TutorLMS — Cours "Webinaire gratuit"

Créer cours : "Webinaire : Transformer son site WP en levier business"

- Leçon 1 : Vidéo webinaire
- Leçon 2 : Ressources (checklist / templates)
- Leçon 3 : Plan 30 jours
- Leçon 4 : CTA vers formation signature

---

### Checklist d'implémentation (ordre exact)

1. Créer pages WP (`/webinaire`, `/merci-webinaire`, `/replay-webinaire`, `/offre-formation`)
2. Créer formulaire Fluent Forms + intégration FluentCRM
3. Créer tags + listes dans FluentCRM
4. Créer automations 1→5
5. Héberger replay dans TutorLMS (cours gratuit)
6. Connecter vente TutorLMS + WooCommerce + tag achat
7. Tester avec 2 emails (test + vrai)
8. Lancer 1 carrousel LinkedIn → `/webinaire`

---

### Projection réaliste

300 inscrits/mois × 40% replay × 5% conversion × 497€ = **~3 000€/mois** + upsell consulting + affiliation stack.

---

## 12 EMAILS WEBINAIRE — MOT À MOT

Séquence complète prête à injecter dans FluentCRM. Ton direct, stratégique, orienté ROI.

---

### Email 1 — Confirmation (immédiat)

**Objet : Ton accès au webinaire est prêt**

Bonjour,

Ton accès au webinaire est confirmé.

Dans cette session, je t'explique pourquoi 90% des sites WordPress ne génèrent aucun revenu…
et comment transformer le tien en véritable levier business.

👉 Accède au replay ici :
[LIEN REPLAY]

Prévois 60 minutes.
Prends des notes.

PS : réponds à cet email et dis-moi ton objectif actuel avec WordPress.

— Michaël

---

### Email 2 — L'erreur fondamentale (J+1)

**Objet : Le vrai problème n'est pas le trafic**

On te répète partout :

"Génère du trafic."

C'est faux.

Le trafic ne convertit pas.
Un système convertit.

La majorité des sites WordPress :

- Publient
- Espèrent
- Attendent

Sans funnel.
Sans capture.
Sans offre claire.

Je détaille tout dans le webinaire.

👉 Regarde-le ici :
[LIEN REPLAY]

— Michaël

---

### Email 3 — Le modèle (J+2)

**Objet : Le modèle en 3 piliers**

Un site WordPress rentable repose sur 3 blocs :

1. Trafic stratégique (SEO + intention forte)
2. Capture intelligente (lead magnet + séquence)
3. Offre claire (formation / consulting / stack)

Si un seul bloc manque → ça ne fonctionne pas.

Dans le webinaire, je démonte chaque étape.

👉 Accès ici :
[LIEN REPLAY]

— Michaël

---

### Email 4 — Dernier rappel replay (J+4 si pas de clic)

**Objet : Tu n'as pas encore vu le modèle ?**

Le replay est toujours là.

60 minutes pour comprendre pourquoi ton site ne génère pas encore de revenus réguliers.
Et comment changer ça.

👉 [LIEN REPLAY]

— Michaël

---

### Email 5 — Synthèse + offre (après clic replay, +2h)

**Objet : Si tu veux appliquer ça**

Tu as deux options :

Tester seul pendant des mois.

Appliquer un système structuré.

J'ai créé une formation complète pour ça.

Elle contient :

- Le framework complet
- Les templates
- Les séquences
- La stack exacte

👉 Découvre-la ici :
[LIEN OFFRE]

— Michaël

---

### Email 6 — Étude de cas (J+1 après clic replay)

**Objet : 2 000 visiteurs → 3 500€**

Un freelance me contacte.

2 000 visiteurs/mois.
0 client récurrent.

Le problème ? Pas de système.

On restructure :

- 1 lead magnet
- 1 séquence email
- 1 offre claire

Résultat : 3 500€/mois en 90 jours.

Le modèle complet est ici :
[LIEN OFFRE]

— Michaël

---

### Email 7 — Objection temps (J+2 après clic replay)

**Objet : "Je n'ai pas le temps"**

C'est l'objection la plus fréquente.

Mais la vraie question est :

As-tu le temps de continuer sans système ?

Le modèle schoolsWP te fait gagner du temps,
pas l'inverse.

👉 Tous les détails ici :
[LIEN OFFRE]

— Michaël

---

### Email 8 — Objection technique (J+3 après clic replay)

**Objet : "C'est trop technique pour moi"**

Non.

WordPress n'est pas compliqué.
Il est mal structuré.

Dans la formation :

- Tout est découpé
- Tout est guidé
- Tout est actionnable

Tu n'as pas besoin d'être développeur.

👉 Voir la formation :
[LIEN OFFRE]

— Michaël

---

### Email 9 — Bonus

**Objet : Bonus encore disponible**

En ce moment, j'inclus :

- Checklist stratégique
- Template funnel
- Stack outil détaillée

Ces bonus ne resteront pas éternellement.

👉 Accès ici :
[LIEN OFFRE]

— Michaël

---

### Email 10 — Dernier rappel

**Objet : Dernier rappel**

Je referme les bonus très bientôt.

Si tu veux structurer ton système WordPress maintenant,
c'est le moment.

👉 Voir la formation :
[LIEN OFFRE]

— Michaël

---

### Email 11 — Alternative consulting

**Objet : Si tu préfères aller plus vite**

Certaines personnes veulent un accompagnement direct.

Si tu veux :

- Audit stratégique
- Plan personnalisé
- Mise en place guidée

Je propose quelques créneaux.

👉 Réserve ici :
[LIEN CALENDLY]

— Michaël

---

### Email 12 — Boucle evergreen (nurturing long terme)

**Objet : On continue**

Même si tu ne passes pas à l'action maintenant :

Continue à structurer.

Chaque semaine, je partage :

- SEO WordPress
- Funnel
- Monétisation
- Automatisation

Si tu veux aller plus loin un jour,
le système sera toujours là.

À bientôt,
Michaël

---

### Logique de la séquence complète

Éduque → crée tension → apporte preuve → propose → relance → ouvre consulting → intègre affiliation.
Tout en restant cohérente du premier au dernier email.

---

## PAGE DE VENTE — CONSULTING STRATÉGIQUE schoolsWP

Page positionnée autorité. Filtre naturel. Conversion qualitative. Pas de marketing agressif.

---

### Section 1 — Positionnement

**Transformer ton site WordPress en actif stratégique.**

Ton site ne doit pas être une vitrine.
Il doit être une architecture de conversion.

Si ton WordPress :

- Génère peu de leads qualifiés
- Ne convertit pas malgré du trafic
- Manque de structure stratégique
- Dépend trop de l'improvisation

Alors le problème n'est pas technique.

Il est architectural.

Je restructure des sites WordPress pour en faire des leviers business.

---

### Section 2 — Pour qui

**Ce consulting est fait pour :**

- Freelances WordPress qui veulent monter en gamme
- Formateurs / créateurs avec un site sous-exploité
- Entrepreneurs qui veulent structurer un funnel solide
- Indépendants qui veulent passer d'exécutant à stratège

**Ce n'est pas pour :**

- Installer un plugin
- Corriger un bug
- Faire un site vitrine

Je travaille uniquement sur des projets à ambition business.

---

### Section 3 — Ce que nous faisons concrètement

**1. Architecture d'acquisition**
Positionnement SEO stratégique — Ciblage intentionnel — Cocon sémantique optimisé

**2. Capture et segmentation**
Lead magnet structuré — Séquences email alignées — Segmentation intelligente

**3. Offre et positionnement premium**
Clarification proposition de valeur — Structuration offre consulting / formation — Optimisation conversion

Tout est pensé comme un système.

---

### Section 4 — Résultats attendus

Après restructuration : un site qui guide, des leads qualifiés, une offre claire, un positionnement premium, une architecture scalable.

Ce n'est pas une optimisation superficielle. C'est une transformation structurelle.

---

### Section 5 — Méthodologie

Audit stratégique complet → Diagnostic architecture → Plan d'action détaillé → Implémentation guidée → Optimisation conversion

Je travaille en profondeur. Peu de projets. Implication maximale.

---

### Section 6 — Formats d'accompagnement

| Format                   | Contenu                                                   | Investissement   |
| ------------------------ | --------------------------------------------------------- | ---------------- |
| Audit stratégique        | 45 min analyse + diagnostic + plan d'action priorisé      | À partir de 500€ |
| Restructuration complète | Architecture + funnel + positionnement + email + offre    | 2 000€ – 5 000€  |
| Accompagnement 3 mois    | Pilotage + ajustements + optimisation + vision long terme | Sur candidature  |

---

### Section 7 — Pourquoi travailler avec moi

Je ne suis pas un simple exécutant WordPress.

Je combine : SEO + Funnel + Automatisation + Monétisation + Vision business.

Je travaille sur la structure, pas sur les symptômes.

---

### Section 8 — Process de sélection

Je prends un nombre limité de projets.

1. Remplis le formulaire
2. Je valide l'alignement
3. On planifie un appel stratégique

Je privilégie les projets ambitieux.

---

### Section 9 — Appel à l'action

> Si tu veux que ton site devienne un levier structuré :
> **👉 Réserve un audit stratégique.**

Si tu veux simplement "optimiser un peu" :
Ce n'est probablement pas pour toi.

---

### Effet recherché

Cette page filtre, positionne, rassure, justifie le prix, attire les bons profils.

Pas de volume. De la qualité. Des projets alignés.

---

## SÉQUENCE EMAIL 7 JOURS — CONSULTING PREMIUM

Positionnement : consulting WordPress stratégique haut de gamme. Filtre les petits budgets. Attire les décideurs. Ton posé, autorité calme.

---

### Email 1 — J0 — Le Diagnostic

**Objet : Ton site est-il un actif… ou une carte de visite ?**

Bonjour,

La plupart des sites WordPress que je vois ne sont pas des actifs.

Ce sont des cartes de visite améliorées.

Ils présentent.
Ils expliquent.
Ils rassurent.

Mais ils ne convertissent pas.

Question simple :

- As-tu une capture stratégique claire ?
- As-tu une offre premium visible ?
- As-tu une séquence qui transforme un visiteur en prospect ?

Si la réponse est floue, ton site est passif.

Demain, je t'explique pourquoi le trafic ne règle rien.

— Michaël

---

### Email 2 — J1 — Le Problème Structurel

**Objet : Le mythe du trafic**

On me dit souvent :

"Il me faut plus de trafic."

Non.

Il te faut une architecture.

Un site sans structure de conversion, c'est un seau percé.

Tu peux verser 10 000 visiteurs dedans.
Ils repartent.

Le vrai problème n'est pas le SEO.
Ce n'est pas le design.

C'est l'absence de système.

Demain, je te montre le modèle que j'utilise pour restructurer un site WordPress.

— Michaël

---

### Email 3 — J2 — Le Modèle

**Objet : Le modèle en 3 piliers**

Quand j'analyse un site, je regarde 3 choses :

1. Acquisition ciblée
2. Capture segmentée
3. Offre claire et premium

Pas les plugins.
Pas le thème.

L'architecture.

Un site performant doit guider :
Visiteur → Intérêt → Relation → Décision.

Sans ça, tout le reste est décoratif.

Si tu veux, je peux analyser ton architecture actuelle.

— Michaël

---

### Email 4 — J3 — La Preuve

**Objet : Cas réel : restructuration en 45 jours**

Un freelance me contacte.

Trafic correct.
Zéro leads qualifiés.

Problème :

- Pas de segmentation
- Pas d'offre structurée
- Pas de funnel

On restructure :

- Nouvelle proposition de valeur
- Capture stratégique
- Séquence email alignée
- Offre premium clarifiée

45 jours plus tard :

Premiers leads qualifiés.
Premières ventes.

Ce n'est pas magique.
C'est architectural.

Si tu veux ce type d'analyse sur ton site :
[Réserver un créneau]

— Michaël

---

### Email 5 — J4 — Positionnement Premium

**Objet : Pourquoi je refuse certains projets**

Je ne fais pas :

- De dépannage WordPress
- D'installation de plugin
- De "petites optimisations"

Je restructure des actifs.

Si ton objectif est d'avoir "un site joli", je ne suis pas la bonne personne.

Si ton objectif est d'avoir un levier business structuré, là on peut travailler ensemble.

Je prends peu de projets.
Mais je m'implique réellement.

[Réserver un audit]

— Michaël

---

### Email 6 — J5 — L'Invitation

**Objet : Je prends 3 audits stratégiques ce mois-ci**

Chaque mois, j'ouvre 3 créneaux pour un audit stratégique 45 minutes.

Objectif :

- Analyser ton architecture
- Identifier les fuites
- Proposer un plan d'action concret

Ce n'est pas un appel "découverte".

C'est un travail stratégique.

Si ton projet est sérieux, réserve ici :
[Lien calendrier]

Les places partent vite.

— Michaël

---

### Email 7 — J6 — La Décision

**Objet : Dernier message**

Cette semaine, je t'ai parlé de :

- Architecture
- Funnel
- Conversion
- Positionnement

La vraie question est simple :

Ton site travaille-t-il pour toi ?

Ou attends-tu qu'il le fasse un jour ?

L'inaction coûte plus cher que la décision.

Si tu veux transformer ton site en actif structuré :
Réserve ici : [Lien]

Sinon, je continuerai à partager des analyses dans la newsletter.

À toi de voir.

— Michaël

---

### Effet de la séquence

Filtre les petits budgets → Installe posture premium → Attire les décideurs → Crée cadre stratégique fort → Transforme LinkedIn + SEO en pipeline consulting.

**Projection** : 500 inscrits qualifiés → 10–20 demandes audit → 5 appels → 2–3 clients premium à 2 500€ = 5 000–7 500€ par séquence.

---

## PACKAGING CONSULTING 3 NIVEAUX — schoolsWP

Positionnement : "Je ne crée pas des sites. Je restructure des actifs WordPress."

---

### Niveau 1 — Audit Stratégique "Architecture"

**Pour qui** : freelance / créateur / formateur avec site existant mais sans système clair

**Inclus** :

- Audit complet architecture (acquisition, capture, offre, tunnel, conversion)
- Mapping des fuites
- 45–60 min visio
- Compte rendu PDF stratégique (10–15 pages)
- Plan d'action priorisé 30 jours

**Tarif** : 500€ – 800€

**Objectif business** : cash immédiat + identification projets premium + upsell niveau 2 ou 3

---

### Niveau 2 — Restructuration "Levier Business"

**Pour qui** : entrepreneurs sérieux, freelances avec traction, formateurs / agences en croissance

**Inclus** :

- Audit approfondi + repositionnement offre
- Refonte proposition de valeur
- Architecture funnel complète
- Structuration capture & séquence email
- Maillage SEO stratégique
- Stack outil optimisée
- Blueprint stratégique + arborescence funnel + roadmap 60 jours

**Tarif** : 2 000€ – 4 000€

**Objectif business** : ticket moyen solide + transformation visible + preuve sociale forte

---

### Niveau 3 — Accompagnement "Architecture Premium"

**Pour qui** : projet à fort potentiel, positionnement premium, ambition 5–6 figures

**Inclus** :

- Tout le niveau 2
- Accompagnement 3 mois (2 sessions stratégiques/mois)
- Ajustement en temps réel + optimisation conversion continue
- Stratégie contenu alignée funnel
- Structuration autorité LinkedIn
- Pilotage KPI
- Slack / support prioritaire + revue mensuelle

**Tarif** : 5 000€ – 12 000€

**Objectif business** : peu de clients, marge forte, positionnement haut de gamme

---

### Logique de montée en gamme

```
Carrousel LinkedIn
↓ Lead Magnet
↓ Séquence 7 jours
↓ Audit (Niveau 1)
↓ Restructuration (Niveau 2)
↓ Accompagnement (Niveau 3)
```

---

### Vocabulaire à utiliser / éviter

| À dire       | À éviter              |
| ------------ | --------------------- |
| Architecture | Installation          |
| Système      | Dépannage             |
| Actif        | Petites optimisations |
| ROI          | Joli                  |
| Levier       | Vitrine               |

**Formulation signature** : "Je travaille avec des entrepreneurs qui veulent que leur site devienne un actif stratégique."

---

### Projection mensuelle

| Offre                       | Volume | CA           |
| --------------------------- | ------ | ------------ |
| 4 audits à 600€             | 4/mois | 2 400€       |
| 2 restructurations à 3 000€ | 2/mois | 6 000€       |
| 1 accompagnement premium    | 1/mois | 7 000€       |
| **Total**                   |        | **~15 400€** |

---

## SYSTÈME EVERGREEN POUR VENDRE LE CONSULTING

Architecture complète pour créer un flux continu de prospects qualifiés. 5 blocs automatisés.

---

### Architecture globale

```
LinkedIn / SEO
↓ Lead Magnet (checklist audit)
↓ Séquence email 7 jours
↓ Masterclass evergreen (60 min)
↓ Audit stratégique (formulaire qualifié)
↓ Consulting premium
```

---

### Bloc 1 — Entrée stratégique

**Lead magnet** : "Checklist : Transformer son site WordPress en actif stratégique"
Contenu : 20 points d'audit + scoring + erreurs critiques + indicateurs ROI

**Sources de trafic** : carrousels LinkedIn, articles SEO piliers, YouTube, page ressource, footer site, pop-up contextualisé

---

### Bloc 2 — Séquence email 7 jours

Séquence consulting premium ci-dessus. But : installer autorité + filtrer + introduire audit stratégique.

---

### Bloc 3 — Masterclass evergreen (60 min)

**Objectif** : appel après démonstration convertit beaucoup plus qu'un appel à froid.

**Structure** :

1. Pourquoi 90% des sites WP échouent
2. Le modèle architecture stratégique
3. Cas réel
4. Erreurs fréquentes
5. Invitation audit

**Automatisation** : inscription via email → replay 48h → rappels J+1/J+2 → CTA audit

---

### Bloc 4 — Qualification avant audit

**Landing page audit** : problème, positionnement premium, process, pour qui / pas pour qui, formulaire

**Formulaire de qualification obligatoire** :

- Chiffre d'affaires actuel
- Objectif
- Type d'offre
- Budget estimé

→ Filtrage automatique avant accès calendrier

---

### Bloc 5 — Appel audit → offre

Pendant l'appel : diagnostic + projection ROI + proposition adaptée (Niveau 2 ou 3).
Pas de pitch. Proposition structurée.

---

### Stack WordPress pour automatiser

WordPress + FluentCRM + Fluent Forms + TutorLMS (masterclass)

Flux : Formulaire → Tag → Séquence → Condition clic → Masterclass → Tag → Proposition audit

---

### Projection sur 1 000 leads/mois

| Étape                    | Taux         | Volume |
| ------------------------ | ------------ | ------ |
| Ouvrent séquence         | 40%          | 400    |
| Regardent masterclass    | 15%          | 60     |
| Demandent audit          | 5% des leads | 50     |
| Signent (30% des audits) | 30%          | 15     |

15 clients × 1 000€ moyen = **15 000€/mois** + upsells.

---

### Résultat système

Tu ne vends plus. Tu sélectionnes.

SEO long terme + LinkedIn autorité + email nurturing + masterclass pédagogique + consulting premium = peu de concurrents FR avec cette structure.

---

## CHECKLIST QUOTIDIENNE — schoolsWP OS (15–45 min)

Courte. Exécutable. Zéro blabla. Un focus par jour.

---

### 1) Pulse (2 min)

- [ ] Je sais ce que je veux améliorer aujourd'hui : trafic / autorité / leads / conversion
- [ ] Je choisis 1 seul focus (sinon dispersion garantie)

---

### 2) Scoreboard (5–10 min)

**GSC :**

- [ ] Pages en baisse (clics / impressions / CTR)
- [ ] 1 opportunité CTR : position 3–10 + impressions fortes
- [ ] 1 requête qui mérite une FAQ / section (impressions fortes, clics faibles)

**GA4 (si utile) :**

- [ ] 1 page money : taux de conversion / scroll / engagement
- [ ] 1 friction évidente (CTA absent, page lente, promesse floue)

---

### 3) Décision (2 min)

Choisir 1 action :

- [ ] **P1 SEO CTR** — title/meta + snippet
- [ ] **P1 Contenu** — ajout section + FAQ + internal linking
- [ ] **P1 Conversion** — CTA + bloc offre + preuve
- [ ] **P1 Technique** — perf / indexation / erreurs

**Règle** : une action, un KPI.

---

### 4) Action (15–30 min)

**Bloc A — Quick Win CTR (15 min)**

- [ ] Nouveau title (promesse + bénéfice + mot-clé)
- [ ] Meta description orientée clic (preuve + résultat + CTA)
- [ ] FAQ courte (3–5 Q/R) si pertinent

**Bloc B — Quick Win Contenu (20–30 min)**

- [ ] Ajouter 1 section qui répond à l'intention
- [ ] Ajouter 3 liens internes (pilier → support + support → pilier)
- [ ] Ajouter un bloc "à faire maintenant" (checklist)

**Bloc C — Quick Win Conversion (20–30 min)**

- [ ] CTA clair (1 phrase + bouton)
- [ ] Bloc "pour qui / pas pour qui"
- [ ] Preuve (résultat, chiffre, capture, mini cas)

**Bloc D — Quick Win Technique (30 min)**

- [ ] Vérifier indexation / canonicals / noindex
- [ ] Corriger 1 problème perf évident (image lourde, script, cache)
- [ ] Nettoyer 1 plugin/feature inutile si impact

---

### 5) Scale (5–10 min)

- [ ] Transformer la mise à jour en 1 micro-contenu :
  - 1 post LinkedIn (hook + leçon + action)
  - ou 1 note newsletter (5 lignes)
- [ ] Sauvegarder 1 "pattern" réutilisable (title, CTA, structure)

---

### 6) Loop (2 min)

- [ ] Je note : Action → KPI → Date → où mesurer
- [ ] Je définis la prochaine itération (OK → scaler / KO → ajuster)

---

### Variante "jour de production" (60–120 min)

À faire 2–3x / semaine :

- [ ] **Architecture Blueprint (SPECS)** : cadrer un livrable
- [ ] **Strategic Engine (CREDO)** : produire
- [ ] **Omnichannel Engine (DITO)** : décliner 2 formats

---

### Règle d'or

> Chaque jour : **1 KPI → 1 action → 1 trace.**

---

### Tableau Daily Log (backlog + tracking)

| Date       | Focus                                  | Action réalisée             | KPI visé | Résultat J+7 | Prochaine itération   |
| ---------- | -------------------------------------- | --------------------------- | -------- | ------------ | --------------------- |
| JJ/MM/AAAA | CTR / Contenu / Conversion / Technique | ex : Nouveau title page LMS | CTR +15% | à mesurer    | ajuster meta / scaler |

**Backlog P1/P2/P3 :**

| Priorité | Page / Action          | KPI attendu | Statut  |
| -------- | ---------------------- | ----------- | ------- |
| P1       | ex : Title pilier LMS  | CTR +20%    | À faire |
| P2       | ex : Section FAQ CRM   | Position +3 | Backlog |
| P3       | ex : Perf page contact | LCP < 2.5s  | Backlog |

---

## META-PROMPT OS — schoolsWP Strategic Brain

Trois niveaux selon le besoin. Copier-coller tel quel dans Claude / ChatGPT.

---

### Niveau 1 — AUTO MODE (prompt général)

```
schoolsWP OS – AUTO MODE

Tu es le moteur interne schoolsWP OS.

Mission :
Analyser ma demande et activer automatiquement le bon module parmi :

1) Architecture Blueprint (cadrage stratégique)
2) Decision Engine (arbitrage structuré)
3) Strategic Engine (production premium)
4) Omnichannel Engine (transformation multi-canal)
5) Growth Loop (expérimentation)
6) Performance Loop (optimisation continue)

ÉTAPE 1 — DIAGNOSTIC
Détermine :
- Est-ce un besoin de cadrage ?
- Une décision à prendre ?
- Une production à créer ?
- Une transformation de contenu ?
- Un test à lancer ?
- Une optimisation à améliorer ?

ÉTAPE 2 — ACTIVATION
Active automatiquement le module le plus pertinent.
Si nécessaire, combine maximum 2 modules.

ÉTAPE 3 — EXÉCUTION
Produis une réponse structurée, actionnable, orientée ROI.
Toujours inclure :
- Objectif clair
- KPI impacté
- Priorité (P1 / P2 / P3)
- Prochaine étape concrète

Règles :
- Ton direct, clair, sans jargon inutile.
- Zéro blabla.
- Si données manquantes : maximum 3 questions.
- Sinon : exécute immédiatement.
```

**Usage** : `schoolsWP OS : [ta demande]`

---

### Niveau 2 — STRATEGIC BRAIN (v2 alignée méthode)

```
schoolsWP OS – STRATEGIC BRAIN MODE

Tu es le cerveau stratégique interne de schoolsWP.

Tu maîtrises :
- SEO long terme (Google + IA)
- CSOA – Cocon Sémantique Omnicanal
- Authority Domination 24 mois
- Monétisation (offres, consulting, affiliation, evergreen)
- Stack WordPress (Rank Math, FluentCRM, Fluent Forms, TutorLMS)
- Optimisation data (GSC, GA4, CTR, conversion)

MISSION
Analyser ma demande et activer automatiquement le bon module parmi :

1) Architecture Blueprint → cadrage stratégique
2) Decision Engine → arbitrage
3) Strategic Engine → production premium
4) Omnichannel Engine → transformation & scaling
5) Growth Loop → expérimentation
6) Performance Loop → optimisation continue

ÉTAPE 1 — DIAGNOSTIC STRATÉGIQUE
Déterminer :
- Impact court terme (cash / leads)
- Impact long terme (autorité / SEO)
- Niveau : stratégique / production / optimisation
- Position dans Authority Domination (Fondation / Accélération / Scaling)

ÉTAPE 2 — ACTIVATION INTELLIGENTE
Activer automatiquement le module adapté.
Si pertinent, combiner maximum 2 modules.
Toujours prioriser ROI + effet cumulé.

ÉTAPE 3 — EXÉCUTION STRUCTURÉE
Répondre avec :
1) Objectif stratégique
2) Module activé (sans explication théorique)
3) Plan d'action priorisé (P1 / P2 / P3)
4) KPI impacté
5) Effet court terme vs long terme
6) Prochaine action concrète sous 48h

RÈGLES
- Ton direct, clair, sans blabla.
- Vision systémique, pas tactique isolée.
- Toujours relier à autorité + monétisation.
- Si données manquantes : maximum 3 questions.
- Sinon : exécuter immédiatement.
```

**Ce que ça couvre automatiquement :**

| Demande                                 | Modules activés                 |
| --------------------------------------- | ------------------------------- |
| Lancer page pilier FluentCRM            | Architecture + Strategic Engine |
| CTR baisse sur une page                 | Growth Loop + Performance Loop  |
| Transformer article en contenu LinkedIn | Omnichannel Engine              |
| Arbitrer entre 2 sujets                 | Decision Engine                 |
| Optimiser funnel consulting             | Strategic + Performance         |

---

### Niveau 3 — MINI OS (10 lignes — à garder en favori)

```
schoolsWP OS – MINI MODE

Tu es le cerveau stratégique interne de schoolsWP.
Analyse ma demande et active automatiquement le bon module :
Architecture / Decision / Strategic / Omnichannel / Growth / Performance.

1) Clarifie l'objectif business réel.
2) Identifie l'impact court vs long terme.
3) Active le module le plus pertinent (max 2 combinés).
4) Priorise selon ROI et effet cumulé.
5) Propose un plan d'action P1 / P2 / P3.
6) Indique le KPI impacté.
7) Donne une action concrète à exécuter sous 48h.
8) Supprime tout blabla inutile.
9) Si info manquante : max 3 questions.
10) Sinon : exécute immédiatement.
```

**Usage** : `schoolsWP OS : [ta demande]`

---

### Récapitulatif des 3 niveaux

| Niveau          | Longueur  | Quand l'utiliser                          |
| --------------- | --------- | ----------------------------------------- |
| AUTO MODE       | Moyen     | Demandes variées, besoin de structure     |
| STRATEGIC BRAIN | Long      | Décisions importantes, alignement méthode |
| MINI OS         | 10 lignes | Quotidien, réponse rapide, contexte clair |

---

### Règle d'or

> Tu n'utilises plus le framework. **Le système le fait pour toi.**

---

## DAILY EXECUTION CHECKLIST — schoolsWP OS

But : avancer chaque jour sur autorité + trafic + revenus. Sans dispersion.

---

### 1) THINK (5–10 min)

- [ ] Objectif clair aujourd'hui ?
- [ ] Impact court terme (cash / leads) identifié ?
- [ ] Impact long terme (SEO / autorité) identifié ?
- [ ] Aligné avec Authority Domination 24 mois ?
- [ ] Module OS à activer aujourd'hui ?

> Si flou → activer **Decision Engine**.

---

### 2) BUILD (60–120 min deep work)

- [ ] Je travaille sur UNE seule priorité P1
- [ ] Page pilier / landing / séquence en cours ?
- [ ] Structure validée via Architecture Blueprint
- [ ] Production via Strategic Engine
- [ ] CTA et monétisation intégrés
- [ ] SEO IA (FAQ, structure, snippet) optimisé

> Règle : pas de micro-tâches inutiles.

---

### 3) SCALE (30 min)

- [ ] Le contenu produit est-il décliné ?

| Canal              | Format                 |
| ------------------ | ---------------------- |
| LinkedIn           | Post carrousel / texte |
| Newsletter         | Note 5 lignes          |
| Email              | Séquence evergreen     |
| Ressource affiliée | CTA intégré            |

> Si non → activer **Omnichannel Engine**. Jamais 1 contenu = 1 canal.

---

### 4) OPTIMIZE (30 min data)

Ouvrir GSC :

- [ ] CTR faible (< 3 %) identifié ?
- [ ] Position 5–15 exploitable ?
- [ ] Requêtes secondaires non intégrées ?
- [ ] Opportunité snippet / FAQ ?

> Si oui → activer **Growth Loop** (test ciblé).

---

### 5) IMPROVE (15 min)

- [ ] Un test en cours ?
- [ ] KPI suivi ?
- [ ] Hypothèse validée ou à ajuster ?
- [ ] Une amélioration concrète appliquée aujourd'hui ?

> Sinon → activer **Performance Loop**.

---

### Règle d'or quotidienne

Chaque jour doit produire au moins :

- 1 actif long terme
- ou 1 optimisation mesurable
- ou 1 amélioration conversion

> Sinon → journée non stratégique.

---

### Rythme minimal viable (journée chargée)

| Bloc         | Durée      |
| ------------ | ---------- |
| Production   | 30 min     |
| Data         | 15 min     |
| Optimisation | 15 min     |
| **Total**    | **60 min** |

---

### Effet cumulé sur 90 jours

| Levier                   | Volume |
| ------------------------ | ------ |
| Contenus structurés      | 20+    |
| Optimisations CTR        | 20+    |
| Déclinaisons omnicanales | 20+    |
| Autorité cumulative      | —      |
| Trafic exponentiel       | —      |

---

## DIAGRAMMES STRATÉGIQUES — schoolsWP OS

Trois vues complémentaires du système. À utiliser comme référence lors de l'activation des modules.

---

### Diagramme 1 — Vue globale OS (flux décisionnel)

```
Input : idée / problème / demande
              ↓
        ┌─────────────┐
        │ Diagnostic  │ ◄────────────────────────────────────────┐
        │     OS      │                                          │
        └──────┬──────┘                                          │
               │                                                 │
    ┌──────────┼──────────────────────┐                          │
    │          │          │           │           │              │
 Cadrer    Décider    Produire    Transformer   Tester       Optimiser
    │          │          │           │           │              │
    ▼          ▼          │           │           │              │
 SPECS      COT           │           │           │              │
 Architecture  Decision   │           │           │              │
 Blueprint     Engine     │           │           │              │
    │          │          │           │           │              │
    └────┬─────┘          │           │           │              │
         │                │           │           │              │
         ▼                ▼           │           │              │
      CREDO ─────────────►            │           │              │
      Strategic Engine                │           │              │
              │                       │           │              │
              ▼                       ▼           │              │
           DITO ──────────────────────►           │              │
           Omnichannel Engine                     │              │
                   │                              ▼              │
                   ▼                           PACT              │
                PACT ─────────────────────────► Growth Loop      │
                Growth Loop                       │              │
                        │                         ▼              │
                        ▼                      TDD               │
                     TDD ─────────────────────► Performance Loop │
                     Performance Loop             │              │
                             │                    │              │
                             ▼                    │              │
                     Playbook / Templates          │              │
                     Automations ─────────────────┴──────────────┘
                                        Nouveau cycle
```

**Règle mémo :**

| Situation                    | Module                         |
| ---------------------------- | ------------------------------ |
| Nouveau chantier             | SPECS — Architecture Blueprint |
| Hésitation / arbitrage       | COT — Decision Engine          |
| Création de contenu          | CREDO — Strategic Engine       |
| Déclinaison multi-canal      | DITO — Omnichannel Engine      |
| Test (title, CTA, hook)      | PACT — Growth Loop             |
| Amélioration continue        | TDD — Performance Loop         |
| Ce qui marche → standardiser | Playbook + Automation          |

---

### Diagramme 2 — Authority Domination 24 mois (3 phases)

```
Phase 1 — Fondation          Phase 2 — Accélération       Phase 3 — Scaling
─────────────────────        ──────────────────────        ──────────────────────
SPECS                   →    DITO                    →    TDD
cadrage + architecture       repurposing omnicanal        optimisation continue
SEO + offres                                              CTR / conversion
     ↓                            ↓                            ↓
CREDO                        PACT                        Playbooks +
pages piliers +              tests hooks /               Automations
pages offres                 title / CTA                 FluentCRM
```

**Tempo recommandé :**

- Phase 1 (M1–M8) : poser l'architecture, créer les pages fondamentales, structurer les offres
- Phase 2 (M9–M16) : activer l'omnicanal, tester ce qui convertit
- Phase 3 (M17–M24) : optimiser, standardiser, automatiser → revenus récurrents

---

### Diagramme 3 — Pipeline CSOA + monétisation (contenu → revenus)

```
Keyword / Question IA
        ↓
SPECS : scope + purpose + success
        ↓
CREDO : page pilier / guide / ressource
        ↓
   ┌────┴────────────────┬──────────────────────┐
   ↓                     ↓                      ↓
Encarts              FAQ + Snippets         DITO
monétisation         Schémas                LinkedIn + Newsletter
Affiliation /        Citabilité IA          Emails + Vidéo
Consulting /                                     ↓
Formation                                   Lead capture
                                            Fluent Forms
                                                 ↓
                                            FluentCRM
                                            tags + scoring + segments
                                                 ↓
                                            Offre
                                            consulting / formation / pack
                                                 ↓
                                            PACT
                                            test titres / CTA / offre
                                                 ↓
                                            TDD
                                            optimisation CTR / conv
                                                 ↓
                                            Templates + SOP + Automations
                                                 ↓
                                     ┌───────────┘
                                     ↓
                            Keyword / Question IA
                            (nouveau cycle)
```

**Ce que ce pipeline garantit :**

Chaque contenu produit alimente simultanément :

1. Le SEO (page pilier + citabilité IA)
2. La monétisation directe (affiliation + consulting + formation)
3. La base email (FluentCRM via Fluent Forms)
4. L'optimisation continue (PACT → TDD)

Aucun contenu ne reste isolé. Tout rentre dans le système.

---

## WORKFLOW N8N — schoolsWP OS Multi-Agent

Architecture modulaire en 3 workflows séparés (plus stable, plus facile à débugger).

```
Entrée → Orchestrateur → [Architect → Builder → Critic → Data → Loop] → Sorties
```

---

### Variables d'environnement (n8n Credentials)

| Variable        | Valeur                              |
| --------------- | ----------------------------------- |
| `LLM_PROVIDER`  | `anthropic` \| `google` \| `openai` |
| `MODEL_FAST`    | routeur / orchestrateur             |
| `MODEL_BUILD`   | builder (Claude recommandé)         |
| `MODEL_CRITIC`  | critic                              |
| `MODEL_DATA`    | data analyst (GPT recommandé)       |
| `NOTION_DB_ID`  | ID base Notion destination          |
| `GDRIVE_FOLDER` | ID dossier Google Drive             |
| `SLACK_WEBHOOK` | URL webhook Slack                   |

---

### Workflow 1 — OS Intake + Router

**Trigger : Webhook POST** `/-/schoolswp-os`

Body attendu :

```json
{
  "request": "texte libre",
  "assets": ["url1", "note1"],
  "url": "https://...",
  "goal": "optionnel",
  "kpis": "optionnel",
  "data": "export GSC/GA4 optionnel"
}
```

**Node 2 — Normalize (Set)**

Crée un objet `ctx` standard :

```
ctx.request_raw    = body.request
ctx.url            = body.url
ctx.assets         = body.assets
ctx.stack          = [RankMath, FluentCRM, FluentForms, TutorLMS]
ctx.constraints    = [ton schoolsWP, zéro blabla, max 3 questions]
```

**Node 3 — Orchestrator LLM (modèle rapide)**

Prompt → sortie JSON obligatoire :

```json
{
  "intent": "architecture|decision|production|transformation|test|optimisation",
  "primary_module": "SPECS|COT|CREDO|DITO|PACT|TDD",
  "secondary_module": "optionnel",
  "required_inputs": [],
  "plan": [],
  "risk_flags": []
}
```

**Node 4 — Switch** sur `intent` → branche vers Workflow 2 (production) ou Workflow 3 (data).

---

### Workflow 2 — Multi-Agent Production

**Agent 1 — ARCHITECT** (Gemini recommandé)

- Input : `ctx` + `router.plan`
- Output JSON :

```json
{
  "structure": "plan H2/H3 ou architecture système",
  "scope_exclusions": [],
  "seo_targets": { "intent": "", "angles": [], "entities": [] },
  "monetization_slots": [],
  "next_steps": []
}
```

---

**Agent 2 — BUILDER** (Claude recommandé)

- Input : `Architect.structure` + `ctx`
- Output Markdown :
  - Contenu final prêt à publier
  - FAQ
  - CTA
  - Blocs réutilisables

---

**Agent 3 — CRITIC** (Claude ou GPT)

- Input : `Builder.output`
- Output diff + checklist :

```json
{
  "issues": [],
  "patches": [],
  "final": "version améliorée"
}
```

Vérifie : clarté, structure, SEO, citabilité IA, fluff.

---

**Agent 4 — DATA ANALYST** (GPT recommandé)

- Input : `ctx.data` (GSC/GA4) + contenu final
- Output JSON :

```json
{
  "kpi_primary": "",
  "baseline": "",
  "hypotheses": [],
  "tests": [],
  "measurement_plan": {}
}
```

---

**Agent 5 — LOOP CONTROLLER** (IF node, sans LLM)

```
IF baseline absent    → "need_data" (max 3 questions)
IF expected_lift élevé → "scale"
ELSE                  → "iterate"
```

Output :

```json
{
  "decision": "iterate|scale|pivot|need_data",
  "actions_next_48h": []
}
```

---

### Workflow 3 — Data & Iteration Loop

**Trigger** : upload CSV (Drive) ou webhook file

1. Parse CSV (Spreadsheet File node)
2. Normalize metrics
3. Inject dans Agent 4
4. Output : plan de test + priorités CTR

---

### Sorties automatisées

**A) Notion**

Créer une page avec :

- Résumé
- Module(s) activé(s)
- Version finale
- Plan de test
- Next 48h

**B) Tickets P1/P2/P3** (Trello / Jira / GitHub Issues)

3 cartes :

- checklist quick wins
- checklist version complète
- KPI + date de mesure

**C) Slack / Discord**

TL;DR + lien Notion

**D) Logs** (Airtable / Google Sheets / Postgres)

| Champ    | Valeur  |
| -------- | ------- |
| date     | —       |
| type     | demande |
| url      | —       |
| modules  | activés |
| résultat | —       |
| KPI      | choisi  |

---

### Garde-fous indispensables

| Problème           | Solution n8n                      |
| ------------------ | --------------------------------- |
| Rate limit LLM     | Wait / Throttle node entre appels |
| Timeout API        | Retry sur HTTP Request (3x)       |
| JSON invalide      | IF + "Parse JSON" + fallback      |
| Agent 2 échoue     | Relance avec prompt plus strict   |
| Contexte trop long | Truncate Function avant injection |

---

### Architecture recommandée (3 workflows séparés)

```
Workflow 1 : OS Intake + Router
             → classe l'intent, fixe le mode

Workflow 2 : Multi-Agent Production
             → Architect → Builder → Critic

Workflow 3 : Data & Iteration Loop
             → Data Analyst → Loop Controller → sorties
```

> 1 workflow monolithique = impossible à débugger. 3 workflows = chacun testable indépendamment.

---

## GSC CSV → Strategic Brain — Pipeline Data

Connecter les exports GSC directement au système multi-agent pour générer diagnostics, quick wins et plans de tests.

---

### Format CSV recommandé

**Export GSC → Performances → Résultats de recherche**

| Export           | Dimension    | Utilité           |
| ---------------- | ------------ | ----------------- |
| Pages            | Page         | Vue macro par URL |
| Requêtes         | Query        | Vue par mot-clé   |
| Pages + Requêtes | Page + Query | Le plus puissant  |

**Colonnes standard attendues :**
`page`, `query` (optionnel), `clicks`, `impressions`, `ctr`, `position`

**Optionnel (comparaison MoM) :**
`clicks_prev`, `impressions_prev`, `ctr_prev`, `position_prev`

Période recommandée : 28 jours (baseline) + 28 jours précédents.

---

### Calculs à faire AVANT le LLM (Function node)

**A) Quick wins CTR (P1)**

Cible : position 3–12 + impressions élevées + CTR sous-performant

```js
opportunity = impressions * Math.max(0, expected_ctr(position) - ctr);
```

CTR attendu par position :

| Position | CTR attendu |
| -------- | ----------- |
| 1        | 0.28        |
| 2        | 0.15        |
| 3        | 0.10        |
| 4        | 0.07        |
| 5        | 0.05        |
| 6–10     | 0.03        |
| 11–20    | 0.015       |

Actions : title + meta + FAQ + snippet.

**B) Striking distance (P2)**

Position 8–20 + impressions > seuil (ex : 200/mois)

Actions : enrichissement contenu, entités, maillage, FAQ.

**C) Cannibalisation (P3)**

Même query sur plusieurs pages distinctes

Actions : consolidation, canonicals, reframing, maillage.

**D) Décrochage MoM (P3)**

Impressions down + clicks down + position down vs période précédente

Actions : diagnostic SERP, intent drift, title/fragment.

---

### Prompt Data Agent — prêt à coller

```
AGENT DATA – GSC CSV ANALYSIS (schoolsWP)

Input: tableau CSV parsé avec colonnes:
page, query (optionnel), clicks, impressions, ctr, position,
(optionnel) clicks_prev, impressions_prev, ctr_prev, position_prev

Tâche:
1) Nettoyer (URL normalisée, ctr en décimal, position float)
2) Calculer 4 listes:
   A) Quick wins CTR : position 3-12 + impressions élevées + ctr sous-performant
   B) Striking distance : position 8-20 + impressions élevées
   C) Cannibalisation : même query sur plusieurs pages
   D) Décrochage : plus forte baisse clicks/impressions vs période précédente

3) Pour chaque item, donner:
   - priorité (P1/P2/P3)
   - why (1 phrase)
   - action recommandée (title/meta/FAQ/maillage/contenu)
   - KPI à surveiller + délai

Sortie:
- 4 tableaux (Top 20)
- 10 recommandations globales (règles de titres, snippets, maillage)

Ton: direct, concret. Zéro blabla.
```

---

### Pipeline n8n — 6 blocs (no-code)

```
1) Trigger (Manual / Cron / Webhook)
        ↓
2) Read Binary File (CSV)
        ↓
3) Spreadsheet File node (CSV → JSON)
        ↓
4) Function node JS (calcule scores + sort top 20)
        ↓
5) LLM node (envoie uniquement les top tables aux agents)
        ↓
6) Output (Notion / Google Doc / Slack / Airtable / Markdown)
```

> Le LLM ne reçoit jamais le CSV brut — seulement les tables filtrées (top 20 max par catégorie). Cela maintient le contexte court et les réponses stables.

---

### Function node JS — score CTR (à coller dans n8n)

```js
const EXPECTED_CTR = {
  1: 0.28,
  2: 0.15,
  3: 0.1,
  4: 0.07,
  5: 0.05,
  6: 0.03,
  7: 0.03,
  8: 0.03,
  9: 0.03,
  10: 0.03,
};
function expectedCtr(pos) {
  const p = Math.round(pos);
  if (p <= 10) return EXPECTED_CTR[p] || 0.03;
  if (p <= 20) return 0.015;
  return 0.005;
}

const items = $input.all().map((item) => {
  const d = item.json;
  const pos = parseFloat(d.position);
  const ctr = parseFloat(d.ctr) / (d.ctr > 1 ? 100 : 1); // normalise %
  const impr = parseInt(d.impressions);
  const opportunity = impr * Math.max(0, expectedCtr(pos) - ctr);
  return { ...d, pos, ctr, impr, opportunity: Math.round(opportunity) };
});

// Quick wins CTR : pos 3-12, impr > 100
const quickWins = items
  .filter((d) => d.pos >= 3 && d.pos <= 12 && d.impr > 100)
  .sort((a, b) => b.opportunity - a.opportunity)
  .slice(0, 20);

// Striking distance : pos 8-20, impr > 200
const striking = items
  .filter((d) => d.pos >= 8 && d.pos <= 20 && d.impr > 200)
  .sort((a, b) => b.impr - a.impr)
  .slice(0, 20);

return [{ json: { quickWins, striking } }];
```

---

### Rôle de chaque agent sur les données GSC

| Agent     | Input            | Output                                    |
| --------- | ---------------- | ----------------------------------------- |
| DATA      | CSV brut         | 4 tableaux scorés                         |
| ARCHITECT | Tableaux + CSOA  | Mapping vers piliers + priorités business |
| BUILDER   | Architect output | Titles / meta / FAQ / briefs              |
| CRITIC    | Builder output   | Vérification intent + fluff               |
| LOOP      | Tout             | Plan de tests + séquence itération        |

---

## AFFILIATE EVERGREEN LOOP™ — schoolsWP

Système autonome : Trafic → Lead → Confiance → Recommandation → Commission → Relance → Upsell. Sans lancement.

---

### Architecture globale (6 phases)

```
SEO Attraction
      ↓
Capture Lead Magnet (Fluent Forms → FluentCRM)
      ↓
Séquence Evergreen 7–12 emails
      ↓
Conversion intelligente (CTA + bonus + promo)
      ↓
Optimisation continue (Growth Loop + Performance Loop)
      ↓
Scaling omnicanal (DITO Engine)
      ↓ (retour boucle)
SEO Attraction
```

---

### Phase 1 — Attraction (SEO intention forte)

Pages sources :

- Page pilier (ex : FluentCRM, hébergement, plugin SEO)
- Comparatif structuré
- Article "meilleur outil pour…"
- FAQ optimisée IA
- Page ressource centrale

**Optimisations clés :**

| Élément                     | Objectif        |
| --------------------------- | --------------- |
| Position "outil recommandé" | Ancre autorité  |
| Bloc comparatif clair       | Décision rapide |
| Cas d'usage précis          | Confiance       |
| Bonus exclusif schoolsWP    | Différenciation |

---

### Phase 2 — Capture (lead magnet ciblé)

Exemples de lead magnets :

- Checklist PDF
- Template CRM
- Guide "config idéale"
- Bonus exclusif affilié

**Stack** : Fluent Forms → FluentCRM

**Segmentation à l'entrée :**

| Tag             | Segment   |
| --------------- | --------- |
| `lvl_debutant`  | Débutant  |
| `lvl_freelance` | Freelance |
| `lvl_agence`    | Agence    |

---

### Phase 3 — Séquence Evergreen (7–12 emails)

Structure type :

| Email | Contenu                                       |
| ----- | --------------------------------------------- |
| J0    | Confirmation + accès lead magnet              |
| J1    | Problème réel (validation douleur)            |
| J2    | Erreurs fréquentes                            |
| J3    | Solution structurée                           |
| J4    | Démo concrète (captures / vidéo)              |
| J5    | Cas réel (résultat chiffré)                   |
| J6    | Comparatif (outil recommandé vs alternatives) |
| J7    | Recommandation claire + lien affilié          |
| J8    | Rappel bonus exclusif                         |
| J9    | Réponse à l'objection principale              |
| J10   | Dernier push (urgence douce)                  |
| J14   | Nurturing long terme (contenu pilier)         |

> Règle : **Valeur > pression.** Le ratio contenu/vente = 8/2 minimum.

---

### Phase 4 — Conversion intelligente

Intégrer sur la page et dans les emails :

- CTA contextualisés (résultat, pas l'outil)
- Code promo exclusif schoolsWP
- Bonus privé (template, config, guide)
- Mini audit offert (pour l'offre consulting)

> Ne jamais vendre l'outil. **Vendre le résultat.**

---

### Phase 5 — Optimisation continue

**Growth Loop (tests) :**

- Hook email (A/B objet)
- CTA (texte + couleur + position)
- Position bloc affilié dans l'article
- Angle comparatif (feature vs ROI vs simplicité)

**Performance Loop (KPI à suivre) :**

| KPI                   | Définition              |
| --------------------- | ----------------------- |
| CTR page              | Clics affilié / visites |
| EPC                   | Gains / 100 clics       |
| Taux inscription      | Leads / visiteurs       |
| Taux conversion email | Ventes / leads          |
| LTV par segment       | CA moyen par type       |

---

### Phase 6 — Scaling omnicanal (DITO Engine)

| Source         | Destination         |
| -------------- | ------------------- |
| Article pilier | Post LinkedIn       |
| Article pilier | Newsletter          |
| Vidéo tuto     | Article enrichi     |
| Étude de cas   | Nouveau lead magnet |

Chaque contenu alimente la boucle. Aucun actif ne reste isolé.

---

### Prompt activable — Affiliate Evergreen Loop Mode

```
schoolsWP AFFILIATE EVERGREEN LOOP MODE

Objectif :
Construire ou optimiser une boucle affiliée evergreen complète.

Tu dois :
1) Identifier la page source principale (SEO intention forte)
2) Définir le lead magnet cohérent
3) Structurer la séquence email evergreen (7–12 emails)
4) Intégrer bonus différenciant
5) Proposer segmentation FluentCRM
6) Définir KPI clés
7) Identifier opportunités scaling

Toujours intégrer :
- Logique autorité long terme
- Revenu durable sans lancement
- Optimisation continue (Growth Loop + Performance Loop)

Ton: direct, concret. Zéro blabla.
```

---

### Projection réaliste (par page pilier)

| Étape              | Taux | Volume    |
| ------------------ | ---- | --------- |
| Visiteurs / mois   | —    | 2 000     |
| Capture email      | 3%   | 60 leads  |
| Conversion affilié | 8%   | ~5 ventes |
| Commission moyenne | —    | 150€      |
| **CA mensuel**     |      | **750€**  |

**× 5 pages piliers stratégiques = ~3 750€ / mois**

Avec séquences email optimisées + upsells consulting → objectif 5 000€ affiliation atteint.

---

### Ce que ce système produit

Pas une page affiliée. **Un actif récurrent.**

| Composante         | Rôle                               |
| ------------------ | ---------------------------------- |
| Pages SEO          | Trafic permanent                   |
| Lead magnets       | Capture sans pub                   |
| Séquences email    | Conversion automatique             |
| FluentCRM segments | Personnalisation offres            |
| DITO Engine        | Multiplication des points d'entrée |
| Growth Loop        | Amélioration continue du EPC       |

---

## MULTI-AGENT ORCHESTRATION COMPLÈTE — 7 agents

Architecture schoolsWP Strategic Brain. Sépare stratégie / production / vérification / monétisation / projection / décision.

```
Architect → Builder → Critic → Data → Monetization → Financial Projection → Loop Controller
```

---

### Agent 1 — ARCHITECT (Gemini recommandé)

**Rôle** : Vision long terme, structure CSOA, cohérence Authority 24 mois.

Mission :

- Définir structure et cluster
- Identifier opportunités SEO
- Prioriser ROI
- Valider cohérence globale

> Il ne rédige pas. Il structure.

---

### Agent 2 — BUILDER (Claude recommandé)

**Rôle** : Production premium selon le plan validé.

Mission :

- Produire article / landing / email
- Structurer H2/H3
- Intégrer CTA
- Générer FAQ IA

> Il exécute le plan.

---

### Agent 3 — CRITIC (Claude ou GPT)

**Rôle** : Challenger, détecteur de failles.

Mission :

- Identifier faiblesses SEO
- Détecter manque d'angle
- Vérifier citabilité IA
- Supprimer fluff, améliorer clarté

> Il améliore la qualité.

---

### Agent 4 — DATA ANALYST (GPT)

**Rôle** : Lire GSC, analyser CTR, identifier quick wins.

Mission :

- Définir hypothèse
- Proposer A/B
- Mesurer impact
- Prioriser itérations

> Il connecte au réel.

---

### Agent 5 — MONETIZATION ENGINE

**Rôle** : Transformer chaque action en opportunité de revenu.

Mission — pour chaque production ou optimisation :

- Identifier le levier monétisable (affiliation / consulting / lead magnet / upsell)
- Proposer point d'entrée (CTA stratégique)
- Définir le parcours (funnel / automation FluentCRM)
- Intégrer affiliation si pertinente
- Estimer potentiel court terme / long terme

**Format de sortie obligatoire :**

- Opportunités identifiées
- CTA recommandé
- Parcours utilisateur
- Automatisation associée
- Estimation potentiel (faible / moyen / fort)
- Impact court terme vs long terme

**Exemple — page pilier FluentCRM :**

- Bloc comparatif + code promo exclusif
- Séquence email evergreen
- CTA audit CRM
- Bonus affilié exclusif
- Segmentation `lvl_freelance` / `lvl_agence`

> Il pense revenu structurel. Toujours.

---

### Agent 6 — FINANCIAL PROJECTION ENGINE

**Rôle** : Modéliser les revenus sur 12 et 24 mois.

Mission :

- Identifier sources de revenu (affiliation, consulting, formation, evergreen, upsell)
- Définir variables clés (trafic, CTR, conversion, panier moyen, LTV)
- Construire 3 scénarios (conservateur / réaliste / ambitieux)
- Identifier le levier prioritaire

**Format de sortie obligatoire :**

```
FINANCIAL PROJECTION

1) Hypothèses utilisées
2) Variables critiques
3) Scénario conservateur (12m / 24m)
4) Scénario réaliste (12m / 24m)
5) Scénario ambitieux (12m / 24m)
6) Levier prioritaire à activer
7) Risque principal
8) Action à fort ROI immédiat
```

**Exemple — page pilier affiliation :**

| Variable           | Valeur             |
| ------------------ | ------------------ |
| Trafic 12 mois     | 1 500 visites/mois |
| CTR affiliation    | 4%                 |
| Taux conversion    | 8%                 |
| Commission moyenne | 120€               |

→ Réaliste : ~4 600€ an 1 / ~12 000€ cumulé an 2

**Levier identifié** : CTR 4% → 6% = +50% revenu sans trafic supplémentaire.

---

### Agent 7 — LOOP CONTROLLER

**Rôle** : Chef d'orchestre — décide si on scale, itère ou pivote.

```
IF KPI > seuil    → SCALE
IF KPI < seuil    → ITERATE
IF stagnation     → REPOSITION
```

Output :

- `decision = scale | iterate | pivot`
- `actions_next_48h`

---

### Prompt orchestration FULL — prêt à coller

```
schoolsWP STRATEGIC BRAIN – FULL MULTI AGENT MODE

AGENT 1 – ARCHITECT
Structure stratégique (CSOA + ROI long terme).

AGENT 2 – BUILDER
Production premium.

AGENT 3 – CRITIC
Amélioration qualité & citabilité IA.

AGENT 4 – DATA ANALYST
KPI + hypothèses de test.

AGENT 5 – MONETIZATION ENGINE
Identifier, intégrer et structurer les leviers de revenu
(affiliation, consulting, evergreen, lead magnet, upsell).

AGENT 6 – FINANCIAL PROJECTION ENGINE
Projection 12–24 mois + 3 scénarios + levier prioritaire.

AGENT 7 – LOOP CONTROLLER
Décision : scaler / itérer / pivoter.

Règles :
- Chaque initiative doit avoir un potentiel chiffré.
- Priorité revenu cumulatif.
- Vision 24 mois minimum.
- Chaque contenu doit avoir une logique monétisable.
- Réponses structurées par agent.
- Zéro redondance.
```

---

## MODÈLE FINANCIER GOOGLE SHEETS — schoolsWP

Projection affiliation + consulting + offre digitale sur 12 et 24 mois.

---

### Feuille 1 — HYPOTHÈSES

| Cellule | Variable                        | Valeur par défaut |
| ------- | ------------------------------- | ----------------- |
| B1      | `TRAFIC_MENSUEL_INITIAL`        | 800               |
| B2      | `CROISSANCE_MENSUELLE_%`        | 0.05              |
| B3      | `CTR_AFFILIATION_%`             | 0.04              |
| B4      | `TAUX_CONVERSION_AFFILIATION_%` | 0.08              |
| B5      | `COMMISSION_MOYENNE_€`          | 120               |
| B6      | `TAUX_CONVERSION_CONSULTING_%`  | 0.02              |
| B7      | `PANIER_MOYEN_CONSULTING_€`     | 800               |
| B8      | `TAUX_CONVERSION_PRODUIT_%`     | 0.03              |
| B9      | `PANIER_MOYEN_PRODUIT_€`        | 97                |
| B10     | `TAUX_CAPTURE_EMAIL_%`          | 0.03              |
| B11     | `TAUX_CONVERSION_EMAIL_%`       | 0.08              |
| B12     | `OBJECTIF_MENSUEL_€`            | 5000              |

---

### Feuille 2 — PROJECTION MENSUELLE

| Col | Champ              | Formule (ligne 2)                             |
| --- | ------------------ | --------------------------------------------- |
| A   | Mois               | 1, 2, 3…                                      |
| B   | Trafic estimé      | `=HYPOTHÈSES!B1` puis `=B2*(1+HYPOTHÈSES!B2)` |
| C   | Clics affiliés     | `=B2*HYPOTHÈSES!B3`                           |
| D   | Ventes affiliées   | `=C2*HYPOTHÈSES!B4`                           |
| E   | Revenu affiliation | `=D2*HYPOTHÈSES!B5`                           |
| F   | Leads capturés     | `=B2*HYPOTHÈSES!B10`                          |
| G   | Ventes consulting  | `=F2*HYPOTHÈSES!B6`                           |
| H   | Revenu consulting  | `=G2*HYPOTHÈSES!B7`                           |
| I   | Ventes produit     | `=F2*HYPOTHÈSES!B8`                           |
| J   | Revenu produit     | `=I2*HYPOTHÈSES!B9`                           |
| K   | **Revenu total**   | `=E2+H2+J2`                                   |

Copier lignes 3–25 pour 24 mois.

---

### Feuille 3 — SYNTHÈSE

```
Revenu total 12 mois   = SOMME(K2:K13)
Revenu total 24 mois   = SOMME(K2:K25)
Revenu moyen 12 mois   = MOYENNE(K2:K13)
Revenu moyen 24 mois   = MOYENNE(K2:K25)
Écart objectif         = HYPOTHÈSES!B12 - MOYENNE(K2:K13)
```

> Si **Écart objectif** > 0 : identifier le levier prioritaire à améliorer (CTR ? conversion email ? consulting ?).

---

### 3 scénarios (cloner la feuille)

| Scénario     | Croissance mensuelle | Trafic M12 estimé |
| ------------ | -------------------- | ----------------- |
| Conservateur | +2%/mois             | ~980              |
| Réaliste     | +5%/mois             | ~1 300            |
| Ambitieux    | +8–10%/mois          | ~1 800+           |

**Lecture stratégique :** le levier principal est presque toujours conversion email + consulting — pas le volume de trafic.

---

## MODÈLE OBJECTIF 5 000€/MOIS AFFILIATION

### Variables de base

| Variable                                  | Symbole | Valeur exemple |
| ----------------------------------------- | ------- | -------------- |
| Commission moyenne par vente              | C       | 120€           |
| Taux clic affilié (depuis article)        | T1      | 4%             |
| Taux conversion affilié (chez partenaire) | T2      | 8%             |
| Trafic mensuel qualifié                   | V       | à définir      |

**Formule clé :**

```
Revenu mensuel = V × T1 × T2 × C
```

---

### Exemple réaliste schoolsWP

Hypothèses de base :

```
Commission moyenne = 120€
T1 = 4%
T2 = 8%

Revenu = V × 0.04 × 0.08 × 120
Revenu = V × 0.4608

→ Chaque visiteur vaut ≈ 0,46€
→ Trafic nécessaire pour 5 000€ : 5 000 / 0.4608 ≈ 10 850 visiteurs/mois
```

---

### 3 scénarios comparés

| Scénario     | Commission | T1  | T2  | EPC (€/visiteur) | Trafic nécessaire |
| ------------ | ---------- | --- | --- | ---------------- | ----------------- |
| Conservateur | 100€       | 3%  | 6%  | 0,18€            | ~28 000           |
| Réaliste     | 120€       | 4%  | 8%  | 0,38€            | ~13 000           |
| Optimisé     | 150€       | 5%  | 10% | 0,75€            | ~6 700            |

**Règle clé :** EPC (€ par visiteur) est le multiplicateur. Doubler l'EPC = couper le trafic nécessaire de moitié.

---

### Google Sheets — Modèle objectif 5 000€

**Paramètres (cellules fixes) :**

```
B1 = Commission moyenne (ex: 120)
B2 = Taux clic affilié (ex: 0.04)
B3 = Taux conversion (ex: 0.08)
B4 = EPC calculé automatiquement : =B1*B2*B3
B5 = Trafic nécessaire : =5000/B4
```

**Revenu mensuel depuis un volume connu :**

```
=B1*B2*B3*A1   (A1 = trafic mensuel actuel)
```

---

## SIMULATION CROISSANCE SEO PROGRESSIVE 12–24 MOIS

### Modèle de croissance composée

```
V(m) = V0 × (1 + g)^m

V0 = trafic qualifié initial (depuis GSC)
g  = taux de croissance mensuel (ex: 6%, 8%, 12%)
m  = mois écoulés

R(m) = V(m) × EPC
```

---

### Google Sheets — Simulation progressive

**Paramètres (cellules de référence) :**

```
B1 = V0 (trafic qualifié actuel, ex: 2000)
B2 = g  (croissance mensuelle, ex: 0.08)
B3 = EPC (€/visiteur, ex: 0.46 ou 0.75)
B4 = Objectif revenu (ex: 5000)
```

**Table (à partir de A7) :**

| Colonne | Contenu     | Formule                     |
| ------- | ----------- | --------------------------- |
| A8      | Mois 0      | `0`                         |
| A9:A32  | Mois 1 → 24 | `=A8+1` (tirer vers le bas) |
| B8      | Trafic M0   | `=$B$1*(1+$B$2)^A8`         |
| C8      | Revenu M0   | `=B8*$B$3`                  |

**Mois où tu passes l'objectif :**

```
=MATCH(TRUE, C8:C100>=$B$4, 0)-1
```

---

### Exemple concret — Scénario réaliste

```
V0 = 2 000 visites qualifiées/mois
g  = 8%/mois
EPC = 0,46€/visite

Mois 12 : V ≈ 5 000 → R ≈ 2 300€/mois
Mois 18 : V ≈ 8 000 → R ≈ 3 700€/mois
Mois 21 : V ≈ 9 800 → R ≈ 4 500€/mois
Mois 23 : V ≈ 11 400 → R ≈ 5 250€/mois  ✓ objectif
```

Avec EPC optimisé à 0,75€ (meilleurs CTA + comparatifs) :

```
Mois 12 : R ≈ 3 750€/mois
Mois 15 : R ≈ 4 700€/mois
Mois 17 : R ≈ 5 500€/mois  ✓ objectif
```

→ **Optimiser l'EPC gagne 6 mois sur l'objectif.**

---

### 3 scénarios de croissance SEO (colonnes parallèles)

| Mois | Prudent (g=4%) | Réaliste (g=8%) | Ambitieux (g=12%) |
| ---- | -------------- | --------------- | ----------------- |
| 0    | 2 000          | 2 000           | 2 000             |
| 6    | 2 530          | 3 173           | 3 948             |
| 12   | 3 202          | 5 036           | 7 795             |
| 18   | 4 052          | 7 988           | 15 398            |
| 24   | 5 129          | 12 676          | 30 415            |

Revenus mensuels à EPC = 0,46€ :

| Mois | Prudent | Réaliste | Ambitieux |
| ---- | ------- | -------- | --------- |
| 12   | 1 473€  | 2 317€   | 3 586€    |
| 18   | 1 864€  | 3 675€   | 7 083€    |
| 24   | 2 359€  | 5 831€   | 13 991€   |

---

### Les 2 accélérateurs > trafic seul

```
1. Monter l'EPC (CTA, placement, comparatifs, bonus, séquences email)
   → +50% EPC = objectif atteint 6–8 mois plus tôt

2. Monter CTR GSC sur pages positions 4–12
   → sans attendre de nouveau contenu, trafic +20–40% immédiat
```

---

### Intégration dans l'OS multi-agent

```
Agent Data        → identifie pages positions 4–12 (GSC)
Agent Growth      → teste CTA affiliés (A/B)
Agent Monetization → optimise blocs comparatifs
Agent Financial   → recalcule projection EPC × V(m)
Loop Controller   → boucle mensuelle automatique
```

---

### Feuille Google Sheets complète — 3 scénarios en colonnes

**Structure recommandée :**

```
Colonne A  : Mois (0 → 24)
Colonne B  : Trafic Prudent  = $B$1*(1+0.04)^A
Colonne C  : Revenu Prudent  = B*EPC
Colonne D  : Trafic Réaliste = $B$1*(1+0.08)^A
Colonne E  : Revenu Réaliste = D*EPC
Colonne F  : Trafic Ambitieux= $B$1*(1+0.12)^A
Colonne G  : Revenu Ambitieux= F*EPC
Colonne H  : Ligne objectif  = 5000 (constante, pour graphique)
```

**Graphique recommandé :** courbes C, E, G + ligne droite H → visualise quand chaque scénario croise l'objectif.

---

### Authority Domination — chemin réaliste vers 5 000€/mois

```
3 pages piliers affiliation forte    → 400–600 visites/page/mois
10 pages satellites ciblées          → 150–300 visites/page/mois
1 comparatif central                 → 800–1 200 visites/mois
1 séquence email evergreen           → +15–25% revenu sur trafic email
1 bonus exclusif affilié             → CTR +1–2% supplémentaire

Total trafic qualifié estimé : 6 000–12 000 visites/mois
→ 5 000€/mois cohérent avec EPC optimisé (0,65–0,75€)
```

---

### Lecture stratégique finale

> Tu as 4 leviers actionnables, par ordre d'impact immédiat :
>
> 1. **Commission moyenne** — choisir partenaires à commission >100€ (SaaS, formations, hébergement premium)
> 2. **CTR affilié** — CTA contextuels, blocs comparatifs, bonus exclusifs
> 3. **Conversion partenaire** — qualifier le trafic avant le clic (articles intent fort)
> 4. **Volume de trafic** — le plus lent, mais le plus durable
>
> **Le trafic seul ne suffit pas. L'EPC décide.**

---

## WORKFLOW N8N — GSC API QUERY-BASED (ROI-DRIVEN)

### Architecture complète

```
Cron (hebdo / bi-mensuel)
  ↓
Google Search Console – Search Analytics
  dimensions: query | date range: last 90 days | row limit: 5 000
  ↓
Function – Filtre opportunités
  ↓
Function – Simulation CTR & gain clics
  ↓
Function – Projection financière
  ↓
LLM Node (optionnel) → recommandations SEO
  ↓
Google Sheets / Notion  +  Slack / Email résumé
```

---

### Règles de détection (Query-based)

Cibles prioritaires :

| Critère     | Valeur |
| ----------- | ------ |
| Position    | 4 → 12 |
| Impressions | ≥ 300  |
| CTR         | < 4%   |

**Pourquoi cette zone ?** Google te montre déjà, tu es proche du top 3, le gain CTR peut exploser sans nouveau contenu.

---

### Logique de calcul

**Variables :**

```js
CTR_TARGET_1 = 0.05; // scénario conservateur
CTR_TARGET_2 = 0.07; // scénario ambitieux
AFF_CLICK_RATE = 0.04; // taux clic affilié depuis l'article
AFF_CONV_RATE = 0.08; // taux conversion chez le partenaire
COMMISSION = 120; // commission moyenne par vente (€)
```

**Gain de clics :**

```js
clicks_current = impressions * ctr_current;
clicks_target = impressions * CTR_TARGET;
clicks_gain = clicks_target - clicks_current;
```

**Revenu affiliation :**

```js
aff_clicks = clicks_gain * AFF_CLICK_RATE;
sales = aff_clicks * AFF_CONV_RATE;
revenue_monthly = sales * COMMISSION;
```

**Projection 12 / 24 mois (rampe SEO) :**

```js
// Mois 1 = 30%, Mois 2 = 60%, Mois 3+ = 100%
rev_12m = revenue_monthly * (0.3 + 0.6 + 10); // ≈ 10,9 mois plein
rev_24m = revenue_monthly * (0.3 + 0.6 + 22); // ≈ 22,9 mois plein
```

---

### Function Node — Core Logic n8n

```js
const CTR_TARGETS = [0.05, 0.07];
const MIN_IMPRESSIONS = 300;
const POS_MIN = 4;
const POS_MAX = 12;

const AFF_CLICK_RATE = 0.04;
const AFF_CONV_RATE = 0.08;
const COMMISSION = 120;

function weight(pos) {
  if (pos <= 6) return 1.2;
  if (pos <= 9) return 1.0;
  return 0.8;
}

const enriched = items
  .map((i) => {
    const impressions = i.json.impressions;
    const clicks = i.json.clicks;
    const ctr = impressions ? clicks / impressions : 0;
    const position = i.json.position;
    const query = i.json.keys[0];

    if (
      impressions < MIN_IMPRESSIONS ||
      position < POS_MIN ||
      position > POS_MAX ||
      ctr > 0.04
    )
      return null;

    const sims = CTR_TARGETS.map((t) => {
      const gain = impressions * t - clicks;
      const affClicks = gain * AFF_CLICK_RATE;
      const sales = affClicks * AFF_CONV_RATE;
      const revenueMonthly = sales * COMMISSION;
      const rev12 = revenueMonthly * (0.3 + 0.6 + 10);
      const rev24 = revenueMonthly * (0.3 + 0.6 + 22);

      return {
        ctr_target: t,
        clicks_gain: Math.round(gain),
        revenue_monthly: +revenueMonthly.toFixed(2),
        revenue_12m: +rev12.toFixed(2),
        revenue_24m: +rev24.toFixed(2),
      };
    });

    const score = sims[0].clicks_gain * weight(position);

    return {
      query,
      impressions,
      clicks,
      ctr: +(ctr * 100).toFixed(2) + "%",
      position: +position.toFixed(1),
      score: +score.toFixed(1),
      sim_5: sims[0],
      sim_7: sims[1],
    };
  })
  .filter(Boolean)
  .sort((a, b) => b.score - a.score)
  .slice(0, 15);

return enriched.map((e) => ({ json: e }));
```

---

### Output par requête

| Champ                   | Description                                |
| ----------------------- | ------------------------------------------ |
| `query`                 | Requête GSC                                |
| `impressions`           | Impressions 90j                            |
| `ctr`                   | CTR actuel                                 |
| `position`              | Position moyenne                           |
| `score`                 | Score priorisation (gain × poids position) |
| `sim_5.clicks_gain`     | Gain clics si CTR → 5%                     |
| `sim_5.revenue_monthly` | Revenu mensuel estimé                      |
| `sim_5.revenue_12m`     | Projection 12 mois                         |
| `sim_5.revenue_24m`     | Projection 24 mois                         |
| `sim_7.*`               | Mêmes métriques pour CTR → 7%              |

---

### LLM Node — Prompt recommandations SEO

À coller après le Function Node :

```
Pour chaque requête fournie :

1) Propose un nouveau Title SEO optimisé CTR
2) Propose une meta description persuasive (155 car. max)
3) Indique si la requête mérite :
   - Une nouvelle page dédiée
   - Une optimisation de la page existante
   - Un cluster complet (pilier + satellites)
4) Donne 3 actions concrètes pour gagner 2 points de CTR

Format de sortie :
---
Requête : [query]
Title proposé : [...]
Meta : [...]
Action recommandée : [nouvelle page / optimisation / cluster]
Actions CTR :
- [action 1]
- [action 2]
- [action 3]
```

---

### Lecture stratégique — Ce que ça change

**Avant :** "Je vais écrire un article sur X"

**Après :** "Cette requête peut générer +3 200€ sur 24 mois si je gagne 2 points de CTR"

C'est une allocation de capital, pas une décision éditoriale.

**Priorité d'action (par ordre de ROI) :**

1. Requêtes score > 200 → optimisation immédiate title/meta
2. Requêtes score 100–200 → A/B test CTA affilié
3. Requêtes score < 100 → surveiller, pas d'action urgente

**Intégration OS :**

```
Agent Data        → identifie les 15 requêtes top score
Agent Growth      → génère titles/metas optimisés CTR
Agent Monetization → priorise blocs affiliés sur pages cibles
Agent Financial   → consolide rev_12m + rev_24m → tableau de bord
```

---

## FUNNEL CONSULTING + AFFILIATION — INTÉGRATION FLUENTCRM

### Architecture globale

```
SEO (page pilier / comparatif / guide)
        ↓
┌───────────────────────────────┐
│         Double sortie         │
├───────────────────┬───────────┤
│  Affiliation      │ Consulting │
│  directe          │ (via LM)  │
│  → commission     │ → call    │
└───────────────────┴───────────┘
```

---

### Structure page pilier (ex : FluentCRM)

| Bloc   | Contenu                                                      | Objectif             |
| ------ | ------------------------------------------------------------ | -------------------- |
| Bloc 1 | Guide complet + FAQ IA                                       | Valeur gratuite, SEO |
| Bloc 2 | Comparatif + cas d'usage + code promo + CTA affilié          | Commission directe   |
| Bloc 3 | "Vous voulez aller plus loin ?" + audit CRM + CTA LM/booking | Lead consulting      |

---

### Funnel affiliation (silencieux)

```
Visiteur → Clic affilié → Conversion partenaire → Commission
```

Simple. Scalable. Passif.

---

### Funnel consulting (FluentCRM intégré)

**Étape 1 — Lead Magnet**

Exemple : "Checklist CRM WordPress rentable"

Tags à l'opt-in :

```
TAG : LM_CRM
SOURCE : SRC_SEO_FluentCRM
TAG : PIPE_NewLead
```

**Étape 2 — Séquence email 7 jours**

Voir section EMAIL ci-dessous.

**Tags comportementaux :**

```
ENG_Open_Sequence   → ouverture email
ENG_Click_Audit     → clic lien audit
INT_Consulting      → basculement séquence hot
SCORE_HOT           → score ≥ 40
PIPE_CallBooked     → réservation confirmée
```

---

### Nomenclature tags FluentCRM (namespace propre)

| Namespace | Exemples                                                                                | Usage                     |
| --------- | --------------------------------------------------------------------------------------- | ------------------------- |
| `SRC_`    | `SRC_SEO_FluentCRM`, `SRC_LinkedIn`                                                     | Origine du lead           |
| `LM_`     | `LM_CRM`, `LM_Maintenance`                                                              | Lead magnet téléchargé    |
| `INT_`    | `INT_Affiliation`, `INT_Consulting`, `INT_HighTicket`                                   | Intention détectée        |
| `ENG_`    | `ENG_Open_Sequence`, `ENG_Click_Audit`, `ENG_Click_Pricing`                             | Engagement                |
| `SCORE_`  | `SCORE_HOT` (≥ 40)                                                                      | Qualification automatique |
| `PIPE_`   | `PIPE_NewLead`, `PIPE_Qualified`, `PIPE_CallBooked`, `PIPE_ProposalSent`, `PIPE_Client` | Étape pipeline            |
| `CLI_`    | `CLI_Consulting`                                                                        | Client confirmé           |

---

### Scoring dynamique

| Action            | Points |
| ----------------- | ------ |
| Ouverture email   | +5     |
| Clic lien audit   | +10    |
| Clic page pricing | +20    |

**Seuils :**

```
0–20  → Lead froid
20–40 → Tiède
40+   → SCORE_HOT → tâche "Contacter sous 48h"
```

---

### Automations FluentCRM

**Automation principale — Trigger : TAG = LM_CRM**

```
→ Ajouter SRC_xxx
→ Ajouter PIPE_NewLead
→ Démarrer séquence CRM_Consulting_7j
```

**Branche consultation (si ENG_Click_Audit) :**

```
→ Ajouter INT_Consulting
→ +15 points score
→ Envoyer email "Cas client + offre"
```

**Branche affiliation (si ENG_Click_Affiliate) :**

```
→ Ajouter INT_Affiliation
→ Basculer vers séquence Evergreen_Affiliate
```

**Si Score ≥ 40 :**

```
→ Ajouter SCORE_HOT
→ Créer tâche "Contacter sous 48h"
→ Envoyer email personnalisé
```

**Automation post-call — Trigger : TAG = PIPE_CallBooked**

```
→ Pause séquence marketing
→ Envoyer séquence pré-call
→ Après call : PIPE_ProposalSent ou PIPE_Client
```

**Automation client — Trigger : TAG = PIPE_Client**

```
→ Retirer tags lead
→ Ajouter CLI_Consulting
→ Lancer séquence onboarding
→ J+30 : upsell offre premium
```

**Séquence evergreen affiliation — Trigger : TAG = INT_Affiliation**

```
Email 1 → Guide avancé
Email 2 → Comparatif
Email 3 → Étude de cas
Email 4 → Bonus exclusif
Email 5 → Rappel
```

---

### Pipeline consulting

```
Landing audit → Calendly / FluentBooking → Call 30 min → Offre :

Audit          750€
Accompagnement 1 500€
Mission        3 000€
```

---

### Projection sur 1 000 visiteurs

| Canal       | Métriques                                                 | Revenu       |
| ----------- | --------------------------------------------------------- | ------------ |
| Affiliation | 4% clic → 40 / 8% conv → 3 ventes / ×120€                 | **360€**     |
| Consulting  | 5% opt-in → 50 leads / 3% conv → 1,5 client / ×1 000€ moy | **1 500€**   |
| **Total**   |                                                           | **≈ 1 860€** |

---

## SÉQUENCE EMAIL 7 JOURS — CRM CONSULTING

Trigger : TAG = LM_CRM

---

**EMAIL 1 — Livraison + Positionnement**

```
Objet : Voici votre checklist CRM

Salut,

Voici la checklist promise.

Télécharge-la ici → [Lien]

Important :

90% des sites WordPress utilisent un CRM.
5% l'utilisent correctement.

Un CRM mal configuré =
- leads perdus
- automatisations bancales
- argent laissé sur la table

Demain, je te montre l'erreur n°1 que je vois partout.

À demain.
— Michaël

[Tag : ENG_Open_Sequence]
```

---

**EMAIL 2 — Erreur structurelle**

```
Objet : L'erreur CRM qui coûte cher

La plupart font ça :

Installer → créer 3 tags → envoyer 2 emails.

Ce n'est pas un système.
C'est du bricolage.

Un CRM rentable repose sur :
- segmentation claire
- logique d'intention
- scoring
- automatisations conditionnelles

Si ton CRM n'a pas ça, il te freine.

Tu utilises quoi actuellement ?

PS : si tu veux comparer FluentCRM proprement → [Lien affilié]

[Tag si clic affilié : ENG_Click_Affiliate → INT_Affiliation]
```

---

**EMAIL 3 — Mini étude de cas**

```
Objet : +38% de conversion avec cette structure

Un freelance WordPress.

Même trafic.
Même offre.

On a juste :
- restructuré les tags
- ajouté le scoring
- optimisé la séquence
- clarifié les CTA

Résultat : +38% conversion.

La différence ? Architecture.

Si tu veux que je regarde ton setup →
Audit stratégique ici → [Lien call]

[Tag si clic audit : ENG_Click_Audit → INT_Consulting + 15 pts]
```

---

**EMAIL 4 — Quick win**

```
Objet : À faire en 20 minutes

Action rapide :

Crée 3 segments :
1. Prospect froid
2. Prospect engagé
3. Prospect intention forte

Puis adapte tes emails selon segment.
Rien que ça change tout.

Tu veux que je te montre comment je structure ça ?
→ Réserve un audit → [Lien call]
```

---

**EMAIL 5 — Différenciation**

```
Objet : Ce que la plupart ne comprennent pas

Un CRM n'est pas un outil.
C'est une machine à décision.

Si tu ne sais pas :
- qui est chaud
- qui est prêt
- qui est dormant

Tu navigues à l'aveugle.

Un audit stratégique permet de voir clair en 45 minutes.

Lien ici → [Call]
```

---

**EMAIL 6 — Autorité + affiliation subtile**

```
Objet : FluentCRM ou autre ?

On me demande souvent :
"Quel CRM choisir ?"

La réponse :
Celui que tu sais structurer.

Personnellement, j'utilise FluentCRM pour :
- flexibilité
- intégration WordPress native
- coût maîtrisé

Si tu veux le tester → [Lien affilié + bonus]

Mais si tu veux qu'il soit rentable,
c'est l'architecture qui compte.

[Tag si clic affilié : ENG_Click_Affiliate]
```

---

**EMAIL 7 — Rappel + urgence douce**

```
Objet : Dernier message (promis)

Si tu as téléchargé la checklist,
c'est que ton CRM t'intéresse.

Deux options :

1️⃣ Tester seul (outil recommandé ici → [Lien affilié])
2️⃣ Accélérer avec un audit stratégique personnalisé

Je ferme les créneaux cette semaine.

Si tu veux avancer sérieusement →
Réserve ici → [Lien call]

À toi de décider.
— Michaël
```

---

### Logique cachée de la séquence

| Email | Rôle                            |
| ----- | ------------------------------- |
| 1     | Livraison + confiance           |
| 2     | Problème + affilié discret      |
| 3     | Preuve + CTA consulting         |
| 4     | Quick win + CTA consulting      |
| 5     | Autorité + CTA consulting       |
| 6     | Affilié + renforcement autorité |
| 7     | Urgence douce + double CTA      |

**Emails 2 & 6** → renforcent affiliation
**Emails 3, 4, 5, 7** → poussent consulting
**Tous** → renforcent autorité

---

### Règle clé — Jamais un seul CTA

```
Toujours deux sorties sur chaque page :

CTA affilié  → autonomie   → commission passive
CTA consulting → accélération → revenu premium
```

Même trafic → génère commission + construit liste + produit clients premium + nourrit evergreen.

---

## PLAN STRATÉGIQUE — OBJECTIF 5 000€/MOIS AFFILIATION

### Décomposer la cible

```
5 000€ / mois
Commission moyenne = 70€
→ ≈ 72 ventes / mois
→ ≈ 2,4 ventes / jour
```

Atteignable avec un système structuré.

---

### Sélection des 5 piliers affiliation

Ne pas promouvoir 20 outils. Choisir 5 catégories à fort intent transactionnel :

| Catégorie           | Critères clés                                  |
| ------------------- | ---------------------------------------------- |
| Hébergement premium | Commission élevée, récurrente ou one-shot fort |
| Plugin SEO          | Marché actif, intent achat clair               |
| Outil performance   | Décision rapide, taux conv. élevé              |
| CRM / Email         | Abonnement = commission récurrente             |
| LMS / Formation     | Panier moyen élevé                             |

---

### Répartition réaliste des revenus

| Catégorie   | Commission | Ventes/mois | Total      |
| ----------- | ---------- | ----------- | ---------- |
| Hébergement | 120€       | 15          | 1 800€     |
| Plugin SEO  | 60€        | 20          | 1 200€     |
| CRM         | 80€        | 10          | 800€       |
| LMS         | 90€        | 8           | 720€       |
| Performance | 50€        | 10          | 500€       |
| **Total**   |            | **63**      | **5 020€** |

→ Pas un seul outil. Un portefeuille équilibré.

---

### Machine d'acquisition — 3 canaux

**SEO (base stable)**

```
10 articles transactionnels
5 comparatifs
5 "avis complet"
5 alternatives
→ Objectif : 3 000–5 000 visiteurs transactionnels/mois
```

**LinkedIn (amplificateur)**

```
2 carrousels stack/mois
→ Objectif : 1 000 visiteurs supplémentaires/mois + DM qualifiés
```

**Email (conversion)**

```
Séquence affiliée evergreen
→ Objectif : 5–10 ventes/mois uniquement via email
```

---

### Optimisation conversion

**Page ressource premium : "Ma stack WordPress 2026"**

```
Contenu :
- Tableau comparatif complet
- Cas d'usage par profil
- Pour qui / pour qui pas
- Bonus si achat via ton lien
```

**Bonus exclusifs (peuvent doubler le taux de conversion) :**

```
- Checklist offerte
- Template prêt à l'emploi
- Mini formation
- Audit express
```

---

### Mécanique de trafic → ventes

```
10 000 visiteurs/mois
  × 5%  consultent page affiliée       = 500
  × 15% cliquent                       = 75
  × 5%  achètent                       = 3–4 ventes

→ Sur 1 page forte

Avec 10 pages fortes :
  → 30–40 ventes/mois

+ Email + LinkedIn :
  → 72 ventes atteignables
```

---

### Plan sur 6 mois

| Phase        | Actions                                                                  | Objectif revenu   |
| ------------ | ------------------------------------------------------------------------ | ----------------- |
| **Mois 1–2** | Page ressource + 5 articles clés + séquence email evergreen              | 1 000€/mois       |
| **Mois 3–4** | +5 articles transactionnels + 2 carrousels/mois + segmentation email     | 2 500–3 000€/mois |
| **Mois 5–6** | Bonus exclusifs + comparatifs optimisés + guide stack + internal linking | 4 000–5 000€/mois |

---

### KPI à surveiller

```
CTR affilié (depuis articles)
Conversion post-clic (chez partenaire)
Pages les plus rentables (rev/page)
Emails les plus cliqués
Stack la plus performante (rev par outil)

→ Optimiser ce qui vend. Supprimer ce qui ne vend pas.
```

---

### Levier différenciant schoolsWP

Ne pas vendre "le meilleur plugin". Expliquer :

```
Pourquoi ce choix
Pour quel profil
Dans quel contexte exact
Quel ROI attendu
Quelle alternative si budget différent
```

**Autorité = conversion.** La recommandation experte convertit 2–3× mieux que la liste générique.

---

### Objectif final 12 mois

```
L'affiliation doit :
→ Couvrir les charges fixes (mois 4–6)
→ Stabiliser le cashflow (mois 7–9)
→ Financer le développement formation & consulting (mois 10–12)
```

---

### Tableau prévisionnel 12 mois — Structure Google Sheets

**Feuille INPUTS (cellules jaunes modifiables) :**

```
B1  : Trafic SEO M1 (ex: 2 000)
B2  : Trafic LinkedIn M1 (ex: 300)
B3  : Trafic Email M1 (ex: 500)
B4  : Croissance mensuelle trafic (ex: 0.08)
B5  : % visiteurs page affiliée (ex: 0.05)
B6  : CTR sortant affilié (ex: 0.15)
B7  : Taux conversion partenaire (ex: 0.05)
B8  : Commission Hébergement (ex: 120)
B9  : Commission SEO (ex: 60)
B10 : Commission CRM (ex: 80)
B11 : Commission LMS (ex: 90)
B12 : Commission Performance (ex: 50)
B13 : Mix Hébergement (ex: 0.24)
B14 : Mix SEO (ex: 0.32)
B15 : Mix CRM (ex: 0.16)
B16 : Mix LMS (ex: 0.13)
B17 : Mix Performance (ex: 0.16)
B18 : Objectif mensuel (ex: 5000)
```

**Feuille FORECAST — Colonnes A→K :**

```
A : Mois (1→12)
B : Trafic total = (INPUTS!B1+INPUTS!B2+INPUTS!B3) × (1+INPUTS!B4)^(A-1)
C : Visiteurs page affiliée = B × INPUTS!B5
D : Clics affiliés = C × INPUTS!B6
E : Ventes totales = D × INPUTS!B7
F : Rev Hébergement = E × INPUTS!B13 × INPUTS!B8
G : Rev SEO = E × INPUTS!B14 × INPUTS!B9
H : Rev CRM = E × INPUTS!B15 × INPUTS!B10
I : Rev LMS = E × INPUTS!B16 × INPUTS!B11
J : Rev Performance = E × INPUTS!B17 × INPUTS!B12
K : Revenu total = SOMME(F:J)
L : Écart vs objectif = K - INPUTS!B18
```

**Feuille DASHBOARD :**

```
KPI affiché :
- Revenu M12 projeté
- Mois de franchissement objectif : =MATCH(TRUE, FORECAST!K:K>=INPUTS!B18, 0)
- Revenu cumulé 12 mois : =SOMME(FORECAST!K2:K13)
- Ventes totales 12 mois : =SOMME(FORECAST!E2:E13)
- Meilleure catégorie : MAX(F12,G12,H12,I12,J12)

Graphiques recommandés :
- Courbe revenu mensuel + ligne objectif
- Barres empilées par catégorie (mois 1→12)
- Jauge ou indicateur M12 vs objectif
```

---

## SIMULATION PROGRESSIVE 24 MOIS — AFFILIATION + CONSULTING

### Hypothèses de base (schoolsWP réaliste)

**SEO**

```
3 pages piliers affiliées fortes au départ
+2 nouvelles pages/mois pendant 6 mois
Croissance organique : +8%/mois (effet cumulé contenu + maillage)
```

**Affiliation**

```
Commission moyenne : 120€
Taux clic affilié   : 4%
Taux conv. partenaire : 8%
Valeur par visiteur (EPC) ≈ 0,46€
```

**Consulting**

```
Opt-in lead magnet : 5%
Conversion lead → client : 3%
Panier moyen : 800€ (M1–12) → 1 500€ (M13–24, premium sélectif)
Cap clients : 4/mois max (contrainte temps)
```

---

### Phase 1 — Mois 1–6 : Foundation

```
Trafic M1 = 1 500 visiteurs/mois
Croissance 8%/mois

M1   : 1 500 → Aff = 690€   | Consulting = 1 800€ | Total = 2 490€
M2   : 1 620 → Aff = 745€   | Consulting = 1 944€ | Total = 2 689€
M3   : 1 750 → Aff = 805€   | Consulting = 2 100€ | Total = 2 905€
M4   : 1 890 → Aff = 869€   | Consulting = 2 268€ | Total = 3 137€
M5   : 2 040 → Aff = 938€   | Consulting = 2 448€ | Total = 3 386€
M6   : 2 203 → Aff = 1 013€ | Consulting = 2 644€ | Total = 3 657€
```

**Lecture M6** : le consulting porte le cash. L'affiliation représente ~28% du revenu.

---

### Phase 2 — Mois 7–12 : Acceleration

```
M7   : 2 380 → Aff = 1 095€ | Consulting = 2 856€ | Total = 3 951€
M8   : 2 570 → Aff = 1 182€ | Consulting = 3 084€ | Total = 4 266€
M9   : 2 775 → Aff = 1 277€ | Consulting = 3 330€ | Total = 4 607€
M10  : 2 997 → Aff = 1 379€ | Consulting = 3 597€ | Total = 4 976€
M11  : 3 237 → Aff = 1 489€ | Consulting = 3 885€ | Total = 5 374€  ✓ 5k franchi
M12  : 3 496 → Aff = 1 608€ | Consulting = 4 196€ | Total = 5 804€
```

**Lecture M12** : le seuil 5k est franchi en mois 11. Mix équilibré : affiliation ~28%, consulting ~72%.

---

### Phase 3 — Mois 13–18 : Scaling

```
M13  : 3 776 → Aff = 1 737€ | Consulting = 4 532€ | Total = 6 269€
M14  : 4 078 → Aff = 1 876€ | Consulting = 4 894€ | Total = 6 770€
M15  : 4 404 → Aff = 2 026€ | Consulting = 5 285€ | Total = 7 311€
M16  : 4 756 → Aff = 2 188€ | Consulting = 5 708€ | Total = 7 896€
M17  : 5 137 → Aff = 2 363€ | Consulting = 6 165€ | Total = 8 528€
M18  : 5 548 → Aff = 2 552€ | Consulting = 6 658€ | Total = 9 210€
```

**Alerte M13–18** : le consulting commence à saturer en temps. C'est le moment de monter le panier moyen (800€ → 1 500€) et de limiter à 4 clients/mois maximum.

---

### Phase 4 — Mois 19–24 : Stabilisation intelligente

```
Panier consulting = 1 500€ (clients premium)
Cap = 4 clients/mois

M19  : 5 992 → Aff = 2 756€ | Consulting = 3 595€ (cap 4 cl. × 899€ moy.) | Total = 6 351€
M20  : 6 472 → Aff = 2 977€ | Consulting = 4 200€ (4 cl. × 1 050€ moy.)   | Total = 7 177€
M21  : 6 990 → Aff = 3 215€ | Consulting = 4 800€ (4 cl. × 1 200€)         | Total = 8 015€
M22  : 7 549 → Aff = 3 473€ | Consulting = 5 400€ (4 cl. × 1 350€)         | Total = 8 873€
M23  : 8 153 → Aff = 3 750€ | Consulting = 6 000€ (4 cl. × 1 500€)         | Total = 9 750€
M24  : 8 805 → Aff = 4 050€ | Consulting = 6 000€ (cap atteint)             | Total = 10 050€
```

**Lecture M24** : affiliation ≈ 40% du revenu, consulting ≈ 60% mais plafonné volontairement. L'affiliation devient socle stable et croissant sans effort supplémentaire.

---

### Tableau synthèse 24 mois

| Phase         | Période | Trafic      | Rev. Affiliation | Rev. Consulting | Total mensuel |
| ------------- | ------- | ----------- | ---------------- | --------------- | ------------- |
| Foundation    | M1–M6   | 1 500–2 200 | 690–1 013€       | 1 800–2 644€    | 2 490–3 657€  |
| Acceleration  | M7–M12  | 2 380–3 500 | 1 095–1 608€     | 2 856–4 196€    | 3 951–5 804€  |
| Scaling       | M13–M18 | 3 780–5 550 | 1 737–2 552€     | 4 532–6 658€    | 6 269–9 210€  |
| Stabilisation | M19–M24 | 6 000–8 800 | 2 756–4 050€     | 3 600–6 000€    | 6 350–10 050€ |

**Seuil 5 000€ franchi : mois 11**

---

### Lecture stratégique

```
M0–6   : Consulting = cash immédiat (72% du revenu)
M6–12  : Mix équilibré — l'affiliation monte progressivement
M12–24 : Affiliation = socle stable + croissant
         Consulting = premium sélectif (qualité > volume)
```

**Ce que ça montre** : tu n'as pas besoin de 20 000 visiteurs. Avec 8–10k visiteurs qualifiés + double CTA + séquence evergreen, 5k/mois est structurellement atteignable.

---

### Les 3 vrais leviers (plus puissants que la croissance brute)

| Levier                            | Impact                                           |
| --------------------------------- | ------------------------------------------------ |
| CTR affilié 4% → 6%               | +50% revenus affiliation sans 1 visiteur de plus |
| Panier consulting 800€ → 1 500€   | +87% revenu consulting à volume constant         |
| Meilleure qualification des leads | Moins de clients, plus de CA, moins de temps     |

**Chaque amélioration d'un levier impacte tout le modèle.**

---

### Google Sheets — Structure simulation 24 mois

**Onglet INPUTS (cellules modifiables) :**

```
B1  : Trafic M1 (ex: 1500)
B2  : Croissance mensuelle (ex: 0.08)
B3  : EPC affiliation (ex: 0.46)
B4  : Opt-in consulting (ex: 0.05)
B5  : Conv. lead→client (ex: 0.03)
B6  : Panier M1–12 (ex: 800)
B7  : Panier M13–24 (ex: 1500)
B8  : Cap clients/mois (ex: 4)
B9  : Objectif mensuel (ex: 5000)
```

**Onglet PROJECTION_24M — Colonnes :**

```
A : Mois (1→24)
B : Trafic = INPUTS!B1 × (1+INPUTS!B2)^(A-1)
C : Rev. Affiliation = B × INPUTS!B3
D : Leads générés = B × INPUTS!B4
E : Clients consulting = MIN(D × INPUTS!B5, INPUTS!B8)
F : Panier appliqué = SI(A<=12, INPUTS!B6, INPUTS!B7)
G : Rev. Consulting = E × F
H : Total mensuel = C + G
I : Cumul = SOMME(H$2:H2)
J : Écart objectif = H - INPUTS!B9
```

**Formule mois de franchissement 5k :**

```
=MATCH(TRUE, H2:H25>=INPUTS!B9, 0)
```

**Onglet DASHBOARD :**

```
- KPI : Total M12, Total M24, Mois franchissement 5k, Cumul 24 mois
- Graphique 1 : Courbe Rev. Affiliation + Rev. Consulting + Total + ligne objectif
- Graphique 2 : Barres empilées (Aff vs Consulting) sur 24 mois
- Graphique 3 : Trafic cumulatif M1→M24
```

---

## MODÈLE 5 000€ MINIMUM GARANTI STRUCTUREL

### Principe

Un revenu est "garanti structurel" non pas par magie, mais parce qu'il repose sur **3 couches indépendantes** : si l'une baisse, les deux autres compensent.

```
5 000€/mois =
  Couche 1 : Consulting récurrent   → 2 500€ (50%)
  Couche 2 : Missions ponctuelles   → 1 500€ (30%)
  Couche 3 : Affiliation stable     → 1 000€ (20%)
```

---

### Couche 1 — Socle sécurité (consulting récurrent)

**Cible : 2 500€/mois fixes**

Options :

```
Option A : 5 clients récurrents × 500€/mois (maintenance + suivi)
Option B : 3 clients × 850€/mois (accompagnement mensuel)
Option C : 2 clients × 1 250€/mois (suivi stratégique premium)
```

**Ce que cette couche garantit :** 50% de l'objectif sans dépendre du trafic, des algorithmes ou des conversions d'affiliation.

**Condition** : minimum 3 contrats actifs. En dessous, le modèle n'est plus structurel.

---

### Couche 2 — Missions premium (semi-scalable)

**Cible : 1 500€/mois en moyenne annuelle**

Options :

```
Option A : 1 mission audit stratégique × 1 500€
Option B : 2 audits SEO/CRM × 750€
Option C : 1 mission consulting + 1 audit × 1 000€ + 500€
```

Pas obligatoire chaque mois — mais la **moyenne annuelle** doit tenir.

**Offres recommandées schoolsWP :**

- Audit CRM WordPress → 750€
- Architecture SEO → 1 200€
- Accompagnement Autorité → 1 500€

---

### Couche 3 — Affiliation stable (scalable)

**Cible : 1 000€/mois minimum**

**Hypothèses prudentes :**

```
Commission moyenne    = 120€
CTR affilié          = 3%
Taux conversion      = 7%
EPC (€/visiteur)     ≈ 0,25–0,30€

Trafic nécessaire    = 1 000 / 0.30 ≈ 3 300 visiteurs qualifiés
```

→ 3 300 visiteurs/mois est beaucoup plus atteignable que 10 000.

**Condition** : minimum 1 page pilier affiliée forte + 1 tunnel evergreen email actif.

---

### Tableau de répartition cible

| Source               | Cible mensuelle | % du total | Levier principal    |
| -------------------- | --------------- | ---------- | ------------------- |
| Consulting récurrent | 2 500€          | 50%        | Contrats actifs     |
| Missions ponctuelles | 1 500€          | 30%        | Qualification leads |
| Affiliation          | 1 000€          | 20%        | Trafic × EPC        |
| **Total**            | **5 000€**      | **100%**   |                     |

---

### Les 3 conditions du modèle structurel

```
1. Minimum 3 clients récurrents actifs
   → Sans eux, la couche 1 s'effondre

2. Minimum 1 page pilier affiliée forte
   → Sans elle, la couche 3 reste aléatoire

3. Minimum 1 tunnel evergreen email actif
   → Sans lui, l'affiliation dépend uniquement du trafic direct
```

Sans ces 3 éléments → le modèle n'est pas structurel. Il est espéré.

---

### Évolution des couches sur 24 mois

| Phase  | Consulting | Affiliation | Logique                         |
| ------ | ---------- | ----------- | ------------------------------- |
| M0–6   | 80%        | 20%         | Consulting = cash immédiat      |
| M6–18  | 60%        | 40%         | Montée en puissance affiliation |
| M18–24 | 40%        | 60%         | Affiliation = moteur stable     |

À terme, l'affiliation remplace progressivement la **pression consulting**. Moins de clients requis pour le même revenu total.

---

### Formule globale

```
Revenu total = Récurrent + Missions + (V × T1 × T2 × C)

Avec :
V   = visiteurs qualifiés/mois
T1  = taux clic affilié (ex: 0.03)
T2  = taux conversion partenaire (ex: 0.07)
C   = commission moyenne (ex: 120€)
```

---

### Google Sheets — Structure modèle hybride 5k garanti

**Onglet INPUTS :**

```
B1  : Clients récurrents (ex: 3)
B2  : Panier récurrent moyen (ex: 850)
B3  : Missions/mois moyenne annuelle (ex: 1.5)
B4  : Panier mission moyen (ex: 1000)
B5  : Trafic qualifié M1 (ex: 2000)
B6  : Croissance mensuelle trafic (ex: 0.08)
B7  : CTR affilié (ex: 0.03)
B8  : Taux conversion partenaire (ex: 0.07)
B9  : Commission moyenne (ex: 120)
B10 : Objectif mensuel (ex: 5000)
```

**Onglet TARGETS — Calcul structure :**

```
Rev. Récurrent   = B1 × B2
Rev. Missions    = B3 × B4
EPC              = B7 × B8 × B9
Trafic nécessaire aff. 1k€ = 1000 / EPC

Rev. Affiliation M1 = B5 × EPC
Total M1         = Rev.Récurrent + Rev.Missions + Rev.Affiliation

Écart vs 5k      = Total M1 - B10
Couverture (%)   = Total M1 / B10
```

**Onglet PROJECTION_24M :**

```
A : Mois
B : Trafic = B5 × (1+B6)^(A-1)
C : Rev. Affiliation = B × EPC
D : Rev. Récurrent = INPUTS!B1 × INPUTS!B2 (stable)
E : Rev. Missions = INPUTS!B3 × INPUTS!B4 (stable)
F : Total = C + D + E
G : Cumul
H : Écart vs 5k = F - INPUTS!B10
```

**Onglet GSC (connexion optionnelle) :**

```
Colonnes A→E : export GSC (query, clicks, impressions, ctr, position)
Colonne F    : Monétisation (Affiliate / Consulting / Mixed / Content)
Colonne G    : Gain clics si CTR → 5%
Colonne H    : Opportunité €/mois = G × EPC
Colonne I    : Potentiel consulting = G × 0.05 × 0.03 × 1000
Colonne J    : Opportunité totale = H + I
Tri par J    → quick wins priorisés
```

**Onglet DASHBOARD :**

```
KPI clés :
- Total M1 / M12 / M24
- Mois franchissement 5k structurel
- % couverture par couche (Récurrent / Missions / Affiliation)
- Trafic nécessaire pour 1k€ affiliation seul

Graphiques :
1. Barres empilées 3 couches sur 24 mois
2. Courbe total + ligne 5k objectif
3. Donut part des revenus M12 vs M24
```

---

### Vision schoolsWP (positionnement optimisé)

```
Consulting récurrent :
  → 3 clients "Accompagnement Autorité" × 850€/mois = 2 550€

Missions :
  → 1 Audit CRM WordPress (750€) + 1 Architecture SEO (1 200€)/mois en alternance
  → Moyenne : ~975€ → arrondi 1 000€

Affiliation :
  → 3 pages piliers (FluentCRM, hébergement, LMS)
  → 3 500 visiteurs qualifiés × 0.30€ = 1 050€

Total structurel : 2 550 + 1 000 + 1 050 = 4 600€ → ~5 000€ avec marge
```

→ **Ce modèle est atteignable sans audience massive et sans dépendre d'un seul canal.**

---

## GSC CONNECTED MODE — DATA ENGINE SCHOOLSWP

### Principe

Passer de "je vais optimiser cette page" à "cette page peut générer +1 380€/an si j'augmente le CTR à 5%". Ce n'est plus du SEO. C'est de l'allocation de capital.

---

### Format attendu — Export GSC CSV

```
Colonnes nécessaires :
  A : Query (ou Page)
  B : Clicks
  C : Impressions
  D : CTR
  E : Position

Période : 3 mois minimum (idéal 6 mois)
Export : GSC → Performance → Télécharger → CSV
```

---

### Prompt multi-agent — GSC Connected Mode

À coller dans Claude avec le CSV joint :

```
schoolsWP STRATEGIC BRAIN – GSC CONNECTED MODE

AGENT DATA ANALYST
À partir du CSV GSC fourni :

1) Identifier requêtes/pages avec :
   - Impressions élevées
   - CTR faible (< 4%)
   - Position 4 à 12 (zone opportunité)

2) Classer par potentiel de gain trafic si :
   - CTR passe à 5%
   - CTR passe à 7%

3) Estimer gain de clics mensuels potentiel par ligne.

---

AGENT MONETIZATION
À partir des gains estimés :
- Appliquer : taux clic affilié = 4%, conversion = 8%, commission = 120€
- Calculer revenu potentiel mensuel par requête/page

---

AGENT FINANCIAL PROJECTION
Projeter :
- 12 mois cumulés (avec rampe SEO : M1=30%, M2=60%, M3+=100%)
- 24 mois cumulés
- Effet cumulé croissance SEO +8%/mois

---

AGENT LOOP CONTROLLER
Prioriser :
- Top 3 pages à optimiser (score ROI)
- Action concrète à faire sous 7 jours
- Effet ROI estimé en €/an
```

---

### Logique de calcul (exemple)

```
Requête X :
  Impressions : 10 000
  CTR actuel  : 2%  → 200 clics
  CTR cible   : 5%  → 500 clics
  Gain         = +300 clics/mois

Monétisation :
  300 × 4% clic affilié = 12 clics affiliés
  12 × 8% conversion    = 0,96 vente
  0,96 × 120€           ≈ 115€/mois

Sur 12 mois (avec rampe) ≈ 1 150€/an

→ Une seule page optimisée.
→ 10 pages : +11 500€/an potentiel.
```

---

### Google Sheets — Structure modèle GSC connecté

**Onglet INPUTS (cellules bleues) :**

```
B1  : CTR cible scénario 1 (ex: 0.05)
B2  : CTR cible scénario 2 (ex: 0.07)
B3  : Taux clic affilié (ex: 0.04)
B4  : Taux conversion (ex: 0.08)
B5  : Commission moyenne (ex: 120)
B6  : Croissance SEO mensuelle (ex: 0.08)
B7  : Filtre position min (ex: 4)
B8  : Filtre position max (ex: 12)
B9  : Filtre impressions min (ex: 300)
B10 : Objectif revenu mensuel (ex: 5000)
```

**Onglet GSC_DATA — Coller l'export CSV :**

```
A : Query / Page
B : Clicks
C : Impressions
D : CTR (décimal, ex: 0.02)
E : Position
```

**Onglet OPPORTUNITIES — Calculs automatiques :**

```
F  : Éligible (OUI si position B7–B8, impr ≥ B9, CTR < 0.04)
G  : Gain clics scén. 1 = (C × INPUTS!B1) - B
H  : Rev. mensuel scén. 1 = G × B3 × B4 × B5
I  : Rev. 12 mois scén. 1 = H × (0.3 + 0.6 + 10)
J  : Rev. 24 mois scén. 1 = H × (0.3 + 0.6 + 22)
K  : Gain clics scén. 2 = (C × INPUTS!B2) - B
L  : Rev. mensuel scén. 2 = K × B3 × B4 × B5
M  : Score priorisation = G × (poids position)
N  : Include (1/0) — filtre manuel pour Dashboard
```

**Poids position (colonne cachée) :**

```
Position 4–6  → ×1.2
Position 7–9  → ×1.0
Position 10–12 → ×0.8
```

**Onglet PROJECTION — Cumul 24 mois :**

```
A : Mois (1→24)
B : Uplift trafic inclus (rampe + croissance)
C : Rev. affiliation total (scén. 1) cumulé
D : Rev. affiliation total (scén. 2) cumulé
E : Écart vs objectif
```

**Formule rampe + croissance :**

```
= SOMME(Opp. H:H[Include=1])
  × CHOISIR(mois, 0.3, 0.6, 1, 1, ...)
  × (1 + INPUTS!B6)^(mois-3)
```

**Onglet HOW_TO :**

```
1. Exporter GSC (Performance → 6 mois → CSV)
2. Coller A:E dans GSC_DATA à partir de la ligne 6
3. Ajuster INPUTS (cellules bleues)
4. Onglet OPPORTUNITIES : trier par colonne M (score) décroissant
5. Mettre Include=1 sur top 10–15 lignes
6. Lire PROJECTION pour revenu cumulé 12/24 mois
7. Copier top 3 dans plan d'action hebdo
```

---

### Versions avancées activables

| Option                           | Description                                            |
| -------------------------------- | ------------------------------------------------------ |
| Simulation amélioration position | Position 8 → 5 : modéliser l'effet CTR attendu         |
| Simulation cluster complet       | Agréger requêtes d'une même page → potentiel global    |
| Détection cannibalisation        | 2+ pages sur la même requête → signal de consolidation |
| Requêtes IA-friendly             | Identifier celles avec intent Q&A / comparatif → GEO   |
| Priorisation consulting          | Requêtes intent forte → potentiel lead consulting      |

---

### Résultat attendu

```
Avant : "Je vais optimiser cette page"
Après : "Cette page peut générer +1 380€/an si CTR passe à 5%"

Avant : "Mon SEO progresse"
Après : "Mes 8 pages en zone 4–12 représentent +6 400€/an de potentiel non capturé"
```

**Connexion avec l'OS multi-agent :**

```
Agent Data        → analyse GSC, score opportunités
Agent Growth      → génère titles/metas optimisés CTR
Agent Monetization → calcule revenu par page + priorité
Agent Financial   → projette M12/M24 avec rampe
Loop Controller   → plan d'action top 3 sous 7 jours
```

---

## 5 PAGES LES PLUS RENTABLES À PRODUIRE EN PREMIER

### Critères de sélection

- Intent transactionnelle forte
- Commission affiliée élevée ou consulting direct
- Volume de recherche réaliste FR
- Capacité à ranker avec un cocon bien structuré
- Potentiel de cluster autour

---

### Classement stratégique

#### 🥇 1. Meilleur hébergement WordPress (Pillar)

**Pourquoi #1 :**

- Intent d'achat claire
- Commissions élevées (hosting = recurring + high ticket)
- Sujet pilier structurant

**Potentiel business :**

```
2 000 visiteurs/mois ciblés
3–6% clic affilié
2–4% conversion
→ 800€ à 3 000€/mois possible à terme
```

> Page qui peut générer du revenu avant même que le reste du site soit mature.

---

#### 🥈 2. Meilleur plugin SEO WordPress (Pillar)

**Pourquoi :**

- Sujet ultra recherché
- Intent semi-transactionnelle
- Affiliations plugins premium

**Potentiel :**

```
1 500 visiteurs/mois ciblés
Conversion affiliée régulière
Upsell consulting SEO possible
```

> Permet de construire tout le cocon SEO derrière.

---

#### 🥉 3. Rank Math avis (Cluster BOFU)

**Pourquoi :**

- Intent décisionnelle
- Moins concurrentiel que le mot-clé générique
- Conversion très forte

**Potentiel :**

```
500–1 000 visiteurs/mois
5–10% clic affilié
Page ultra rentable long terme
```

> Les pages "avis" convertissent souvent mieux que les comparatifs généraux.

---

#### 🏅 4. Créer une formation en ligne avec WordPress (Pillar)

**Pourquoi :**

- Positionnement business différenciant
- Lead magnet puissant
- Lien direct vers future formation premium

**Potentiel :**

```
1 000–2 000 visiteurs/mois
Conversion email forte
Opportunité consulting + formation signature
```

> Page stratégique moyen terme, gros impact autorité.

---

#### 🎖 5. Meilleur plugin LMS WordPress (Cluster BOFU)

**Pourquoi :**

- Intent commerciale forte
- Affiliations LMS
- Relie directement au Pillar formation

**Potentiel :**

```
400–800 visiteurs/mois
Conversion élevée
Tunnel formation derrière
```

---

### Couverture stratégique

Ces 5 pages couvrent :

| Axe                     | Page                         |
| ----------------------- | ---------------------------- |
| Cash flow rapide        | Hébergement WordPress        |
| Autorité + trafic       | Plugin SEO WordPress         |
| Positionnement business | Formation en ligne WordPress |
| Conversion forte        | Rank Math avis               |
| Funnel long terme       | Plugin LMS WordPress         |

---

### Ordre de production recommandé (6–8 semaines)

```
Semaine 1–2 : Meilleur hébergement WordPress
Semaine 2–3 : Hébergement WordPress rapide (cluster support)
Semaine 3–4 : Meilleur plugin SEO WordPress
Semaine 4–5 : Rank Math avis
Semaine 5–6 : Créer une formation en ligne WordPress
Semaine 7–8 : Meilleur plugin LMS WordPress
```

---

### Projection réaliste à 12 mois (si bien exécuté)

```
Trafic mensuel ciblé : 6k–10k
Affiliation / mois   : 2k–5k€
Premiers clients consulting
Emails qualifiés     : 3k–5k
```

---

## STRATÉGIE D'ATTAQUE — RANKER PLUS VITE

### 4 leviers simultanés

1. Intent ultra ciblée
2. Structure sémantique chirurgicale
3. Autorité interne agressive
4. Backlinks intelligents

---

### Étape 1 — Attaque par la longue traîne stratégique

**Ne pas viser d'abord :**

- "meilleur hébergement WordPress" (trop compétitif)
- "plugin SEO WordPress" (trop compétitif)

**Commencer par :**

```
Hébergement :
- meilleur hébergement WordPress pour freelance
- hébergement WordPress rapide pas cher
- hébergement WordPress pour WooCommerce
- avis [marque spécifique]

Plugin SEO :
- Rank Math avis complet
- configurer Rank Math 2026
- Rank Math vs Yoast 2026
- schema WordPress Rank Math

LMS :
- Tutor LMS avis 2026
- Tutor LMS vs LearnDash
- vendre formation WordPress sans plugin externe
```

> Longue traîne = positions rapides = trafic initial = signal positif.

---

### Étape 2 — Structure sémantique optimisée dès le départ

Chaque page doit contenir :

```
- 1 H1 clair
- 6–10 H2
- FAQ optimisée
- Tableaux comparatifs
- Données concrètes
- Screenshots réels
- Section "Verdict final"
```

Google doit voir : contenu expert + contenu testé + contenu structuré.

---

### Étape 3 — Maillage interne agressif dès semaine 1

Dès que 5 pages publiées :

- Chaque nouvelle page reçoit 3–5 liens internes
- Chaque ancienne page est mise à jour pour inclure les nouvelles
- **Règle : aucune page isolée**

---

### Étape 4 — Backlinks intelligents (pas massifs)

**Objectif : 5–10 backlinks de qualité dans les 3 premiers mois**

```
- Articles invités WordPress FR
- Interviews croisées
- Mention dans newsletters WP
- Commentaires experts sur sites WP
- Partenariats plugins (témoignages utilisateurs)
```

> 5 bons liens peuvent suffire pour une niche FR.

---

### Étape 5 — Mise à jour stratégique (tous les 60 jours)

```
- Ajouter FAQ supplémentaires
- Ajouter captures écran actualisées
- Ajouter comparatif actualisé
- Ajouter section "Nouveautés 2026"
```

> Google favorise les pages vivantes.

---

### Étape 6 — Optimisation CTR

Après premières impressions, optimiser :

```
- Title plus direct
- Année 2026
- "Test réel"
- "Verdict"
- "Comparatif complet"
```

**Exemple :**

```
❌ "Rank Math avis"
✅ "Rank Math avis 2026 : test réel, avantages, limites et verdict"
```

---

### Étape 7 — Activer le trafic externe pour accélérer

200 visites ciblées LinkedIn/YouTube peuvent :

- Accélérer indexation
- Donner signaux comportementaux
- Améliorer vitesse montée SERP

**Vecteurs :** LinkedIn carrousel / Newsletter / YouTube court

---

### Timeline réaliste si exécuté proprement

```
30 jours :
  - Indexation complète
  - Premières positions longue traîne (top 20–40)

60 jours :
  - Top 10 sur mots-clés secondaires
  - Premiers clics affiliés

90 jours :
  - Top 5 sur longue traîne forte
  - Trafic 500–1 500/mois sur cluster prioritaire
```

---

### Ce qui fait la différence

```
✓ Contenu vraiment testé
✓ Screenshots réels
✓ Comparatifs clairs
✓ Angle business (pas juste technique)
✓ Maillage interne cohérent
✓ Mise à jour régulière
```

### Ce qui ralentit 90% des sites

```
✗ Trop généraliste
✗ Pas de maillage
✗ Pas d'intention commerciale claire
✗ Aucun backlink
✗ Pas de mise à jour
```

---

### Accélérateurs optionnels (x2 vitesse)

```
- Mini campagne netlinking ciblée
- Digital PR WordPress FR
- Page "Ressources recommandées" très stratégique
- Études de cas chiffrées
- Lead magnet ultra spécifique (conversion forte)
```

---

## ARCHITECTURE SCALABLE — 50+ PAGES

### Vision

Pas 50 articles. 50 actifs stratégiques.

---

### 5 super piliers (colonne vertébrale)

1. Hébergement WordPress
2. Plugin SEO WordPress
3. Formation en ligne WordPress
4. Vitesse & Performance WordPress
5. Monétisation & Funnel WordPress

---

### Répartition cible

| Type                     | Nombre cible |
| ------------------------ | ------------ |
| Pillars                  | 5            |
| Clusters BOFU            | 20           |
| Clusters MOFU            | 15           |
| Supports techniques      | 10           |
| Pages ponts stratégiques | 5            |
| **Total**                | **55 pages** |

---

### Pilier 1 — Hébergement WordPress (12 pages)

```
- Meilleur hébergement WordPress
- Hébergement WordPress rapide
- Hébergement pas cher
- Hébergement WooCommerce
- Hébergement pour freelance
- VPS vs mutualisé
- Migration WordPress
- Comparatif hébergement premium
- Sécurité serveur WordPress
- Sauvegarde WordPress
- CDN WordPress
- Optimiser serveur WordPress
```

### Pilier 2 — Plugin SEO WordPress (12 pages)

```
- Meilleur plugin SEO WordPress
- Rank Math avis
- Rank Math Pro avis
- Yoast avis
- SEOPress avis
- Rank Math vs Yoast
- Configurer Rank Math
- Sitemap WordPress
- Schema WordPress
- Maillage interne WordPress
- Redirections 301 WordPress
- Erreurs SEO WordPress
```

### Pilier 3 — Formation en ligne (12 pages)

```
- Créer formation en ligne WordPress
- Meilleur plugin LMS WordPress
- Tutor LMS avis
- LearnDash avis
- Tutor vs LearnDash
- Stripe WordPress
- Espace membre WordPress
- Tunnel evergreen formation
- Automatisation email WordPress
- Plan de cours formation
- Page de vente formation
- Hébergement vidéo formation
```

### Pilier 4 — Performance & Vitesse (10 pages)

```
- Optimiser vitesse WordPress
- Core Web Vitals WordPress
- WP Rocket avis
- Cache WordPress
- Lazy loading WordPress
- Optimiser images WordPress
- Base de données WordPress
- Hébergement rapide WordPress
- GTmetrix / PageSpeed guide
- Erreurs performance WordPress
```

### Pilier 5 — Monétisation & Funnel (9 pages)

```
- Monétiser son site WordPress
- Tunnel de vente WordPress
- Affiliation WordPress
- Vendre services WordPress
- Pack maintenance WordPress
- CRM WordPress
- FluentCRM avis
- Automatisation WordPress
- Gagner de l'argent avec WordPress
```

---

### Règle de maillage scalable

Chaque page doit :

- Lier son Pillar
- Lier 2 pages horizontales (même cluster)
- Lier 1 page pont
- Lier 1 page support

**Exemple :**

```
Rank Math avis
  → Meilleur plugin SEO WordPress (Pillar)
  → Configurer Rank Math (horizontal)
  → Erreurs SEO WordPress (horizontal)
  → Tunnel WordPress (pont)
```

---

### Cadence de production

| Option        | Rythme | Total pages | Durée   |
| ------------- | ------ | ----------- | ------- |
| Conservatrice | 2/mois | 55 pages    | 24 mois |
| Accélérée     | 3/mois | 55 pages    | 18 mois |

---

### Effet SEO cumulatif à 50+ pages

```
✓ Google comprend la thématique dominante
✓ Autorité cluster forte
✓ Moins besoin de backlinks externes
✓ Pages BOFU poussent naturellement
```

---

### Projection réaliste à 50+ pages

```
Trafic organique/mois  : 20k–35k
Affiliation/mois       : 5k–12k€
Leads consulting/mois  : 5–10
Base email             : 10k+
```

---

## 15 PREMIÈRES PAGES À PRODUIRE — PRIORISATION ROI

### Méthode de scoring

Chaque page scorée sur :

- Potentiel monétisation direct
- Intent transactionnelle
- Capacité à ranker en longue traîne
- Importance structurelle dans le cocon
- Capacité de maillage

---

### Niveau 1 — Priorité absolue (Pages Money + Structure)

| #   | Page                                   | Rôle                                       |
| --- | -------------------------------------- | ------------------------------------------ |
| 1   | Meilleur hébergement WordPress         | Cash flow principal + Hub                  |
| 2   | Hébergement WordPress rapide           | Longue traîne accessible + renforce Pillar |
| 3   | Meilleur plugin SEO WordPress          | Autorité SEO + BOFU fort                   |
| 4   | Rank Math avis                         | Conversion élevée + moins concurrentiel    |
| 5   | Créer une formation en ligne WordPress | Positionnement business + lead magnet      |

### Niveau 2 — Priorité stratégique (Conversion + Maillage)

| #   | Page                           | Rôle                                      |
| --- | ------------------------------ | ----------------------------------------- |
| 6   | Meilleur plugin LMS WordPress  | BOFU formation + forte intention          |
| 7   | Tutor LMS avis                 | Conversion LMS                            |
| 8   | Optimiser la vitesse WordPress | Page pont stratégique (hébergement + SEO) |
| 9   | Configurer Rank Math           | Intent opérationnelle + pousse affilié    |
| 10  | Tunnel de vente WordPress      | BOFU consulting + pont business           |

### Niveau 3 — Priorité structurelle (Renforcer l'autorité)

| #   | Page                           | Rôle                                             |
| --- | ------------------------------ | ------------------------------------------------ |
| 11  | Migration WordPress            | Support hébergement + longue traîne rentable     |
| 12  | Erreurs SEO WordPress          | TOFU large + pousse plugin SEO                   |
| 13  | Automatisation email WordPress | Connecte LMS + Funnel                            |
| 14  | Monétiser son site WordPress   | Vision business globale + pont consulting        |
| 15  | WP Rocket avis                 | Conversion performance + renforce pilier vitesse |

---

### Cadence recommandée (2 articles/mois)

```
Mois 1 → Pages 1 & 2
Mois 2 → Pages 3 & 4
Mois 3 → Pages 5 & 6
Mois 4 → Pages 7 & 8
Mois 5 → Pages 9 & 10
Mois 6 → Pages 11 & 12
Mois 7 → Pages 13 & 14
Mois 8 → Page 15
```

---

### Projection réaliste après 12 mois (15 pages)

```
Trafic organique/mois : 5k–10k
Affiliation/mois      : 2k–5k€
Leads consulting      : réguliers
Base email            : 3k–5k
```

---

### Pourquoi cette priorisation est intelligente

```
✓ L'argent est construit avant le branding massif
✓ Les hubs posés avant les clusters secondaires
✓ Longue traîne optimisée avant les requêtes ultra concurrentielles
✓ Business + SEO connectés dès le départ
```

---

## STRATÉGIE SPEED TO TOPICAL AUTHORITY — 90 JOURS

### Principe fondamental

Ne pas "publier beaucoup". Publier dans le bon ordre, avec preuves, maillage, CTR et liens ciblés.

**Raccourci fiable :**

```
1. BOFU longue traîne (positions rapides + conversion forte)
2. Pages support preuves (signal qualité Google)
3. Pillar (remonte grâce au maillage + signaux)
```

> Le Pillar arrive APRÈS que les satellites existent. Seul, il est lent.

---

### Séquence de publication par cocon

#### A. 2 pages BOFU "faciles" en premier

```
- Rank Math avis
- Tutor LMS avis
- Hébergement WordPress rapide
```

#### B. 1 page "preuve / méthode"

```
- Protocole de test, checklists, benchmarks
- Comparatifs tabulaires, FAQs structurées
```

#### C. 1 Pillar "définitif"

```
- Gros guide + tableau + choix par profils + FAQ
```

---

### Format qui ranke plus vite

**Sur chaque page BOFU :**

```
- Intro ultra courte (promesse + verdict)
- Tableau comparatif au-dessus de la ligne de flottaison
- Verdict explicite ("Mon choix si tu es freelance / e-commerce / formation")
- Section "Pour qui / pas pour qui"
- FAQ (5–10 questions vraies)
- Blocs preuve : captures, config, métriques, étapes
```

**Sur les Pillars :**

```
- Tableau + filtres par profil
- Sections décisionnelles (convertissent et font rester)
- Maillage vers clusters "avis" + "how-to"
- Lead magnet lié pile au sujet
```

---

### Maillage interne — minimum par page

```
- 1 lien → Pillar
- 2 liens → clusters voisins
- 1 lien → support preuve
- 1 lien → page pont (vitesse / tunnel / automatisation)
```

**Blocs éditoriaux récurrents :**

```
"À lire ensuite"          → 3 liens contextualisés
"Si tu veux aller plus loin" → 3 liens plus BOFU
```

---

### CTR boost — levier sous-estimé

**Title :** année + bénéfice + verdict

```
✅ "Meilleur hébergement WordPress (2026) : rapide, fiable, mon top 3"
```

**Meta :** promesse + preuve + profil

```
✅ "Tests TTFB + CWV, recommandations par usage (blog, WooCommerce, formation)."
```

**Éléments schema à ajouter :**

- FAQ schema quand pertinent
- Pros/Cons structurés
- Sommaire cliquable

---

### "Proof Content" — l'arme anti-comparatifs génériques

```
✓ Protocole de test clair (même simple)
✓ Captures et settings réels
✓ Mesures : TTFB, CWV, temps de chargement
✓ Checklists téléchargeables
✓ "Mon setup exact" (stack WP)
```

> C'est ce qui fait battre les gros sites qui ne testent pas vraiment.

---

### Backlinks — petit volume, maximum impact

**Cibles de liens (priorité) :**

```
1. Pages ponts (Optimiser vitesse / Tunnel / Automatisation)
2. Pillars (hébergement / plugin SEO / formation)
3. 1–2 pages BOFU forte conversion (Rank Math avis, Meilleur LMS)
```

**Méthodes rapides (propres) :**

```
- Articles invités : 3–5 sites WP / freelances / communautés
- Interviews croisées YouTube/Blog avec lien retour
- Ressource "référence" (checklist / template) citée naturellement
- Pages "stack recommandée"
```

---

### SOP — Publication → Indexation → Push

#### Jour 0

```
- Publier article
- Ajouter 3 liens internes entrants depuis pages existantes
- Ajouter dans sitemap
- Inspecter URL dans GSC
```

#### Jours 3–5

```
- Ajouter 1 FAQ supplémentaire
- Ajouter 1 tableau comparatif
- Ajouter 2 liens internes supplémentaires
```

#### Jour 14

```
- Vérifier impressions GSC
- Ajuster Title si CTR faible
- Ajouter section "Pour qui / pas pour qui"
```

#### Mois 2–3

```
- Obtenir 1 backlink contextuel vers page
- Ajouter bloc "Alternatives"
- Mettre à jour année si nécessaire
```

---

### Plan 30 / 60 / 90 jours

**Jours 1–30 : prise de terrain**

```
- Publier 6 pages BOFU (2 par cocon)
- Publier 2 pages preuve/ponts (vitesse + tunnel)
- Maillage complet
```

**Jours 31–60 : verrouillage**

```
- Publier les 3 Pillars (un par cocon)
- Ajouter tableaux + FAQ + "choix par profils"
- Optimiser titles/metas selon premières impressions GSC
```

**Jours 61–90 : accélération**

```
- Publier 6 supports (schema, sitemap, migration, page de vente, etc.)
- Lancer 5–10 backlinks ciblés
- Itérer sur les pages à impressions mais CTR faible
```

---

### Résultat attendu à 90 jours

```
- 6–10 pages positionnées top 20
- 3–5 pages proches top 10 longue traîne
- Premiers clics affiliés récurrents
- Premiers leads consulting organiques
```

---

## PLAN D'EXÉCUTION — 15 PAGES EN MODE TERRAIN

### Phase 1 — Cash + Position rapide (Semaines 1–4)

| #   | Page                          | Intent          | Raison                                              |
| --- | ----------------------------- | --------------- | --------------------------------------------------- |
| 1   | Rank Math avis                | BOFU pur        | Concurrence faible, premières conversions affiliées |
| 2   | Hébergement WordPress rapide  | BOFU            | Accessible, relie vitesse + hosting                 |
| 3   | Tutor LMS avis                | BOFU            | Niche spécifique, concurrence faible                |
| 4   | Rank Math vs Yoast            | BOFU comparatif | Requête décisionnelle forte                         |
| 5   | Meilleur plugin LMS WordPress | BOFU            | Cluster formation solide                            |

### Phase 2 — Hubs centraux (Semaines 5–8)

| #   | Page                                                 | Rôle                                  |
| --- | ---------------------------------------------------- | ------------------------------------- |
| 6   | Meilleur plugin SEO WordPress (Pillar)               | S'appuie sur pages déjà publiées      |
| 7   | Meilleur hébergement WordPress (Pillar)              | Appuyé par "rapide" + futurs supports |
| 8   | Créer une formation en ligne avec WordPress (Pillar) | Hub formation                         |
| 9   | Optimiser la vitesse WordPress                       | Page pont stratégique                 |
| 10  | Tunnel de vente WordPress                            | Page pont business                    |

### Phase 3 — Renforts stratégiques (Semaines 9–12)

| #   | Page                                      | Rôle                  |
| --- | ----------------------------------------- | --------------------- |
| 11  | Configurer Rank Math                      | Support BOFU SEO      |
| 12  | Migration WordPress vers nouvel hébergeur | Support hébergement   |
| 13  | Automatisation email WordPress            | Pont LMS + Funnel     |
| 14  | Schema WordPress guide                    | Support technique SEO |
| 15  | Page de vente formation WordPress         | BOFU formation        |

---

### Titles & Meta optimisés

**Rank Math avis**

```
Title : Rank Math avis (2026) : test complet, avantages, limites et verdict
Meta  : Analyse détaillée de Rank Math : fonctionnalités, version Pro, performances
        SEO, comparatif et pour qui il est réellement adapté.
```

**Hébergement WordPress rapide**

```
Title : Hébergement WordPress rapide (2026) : lequel choisir pour des Core Web Vitals verts ?
Meta  : Comparatif des hébergements WordPress les plus rapides avec tests TTFB,
        performances réelles et recommandations selon votre profil.
```

**Meilleur plugin SEO WordPress**

```
Title : Meilleur plugin SEO WordPress (2026) : Rank Math vs Yoast vs SEOPress
Meta  : Comparatif complet des meilleurs plugins SEO WordPress : fonctionnalités,
        prix, performances et choix selon votre stratégie.
```

---

### Maillage exact — exemple Rank Math avis

```
→ Meilleur plugin SEO WordPress    ancre : "meilleur plugin SEO WordPress"
→ Configurer Rank Math             ancre : "configurer Rank Math"
→ Schema WordPress                 ancre : "schema WordPress"
→ Tunnel de vente WordPress        ancre : "automatiser son site WordPress"
→ Hébergement WordPress rapide     ancre : "optimiser la vitesse WordPress"
```

---

### Vision stratégique finale

```
Tu ne publies pas 15 pages isolées.
Tu publies 15 pages connectées.

Google doit comprendre :
schoolsWP = WordPress + SEO + hébergement + formation + monétisation
```

---

## SIMULATION CA POTENTIEL — 50+ PAGES (3 SCÉNARIOS)

### Hypothèses de base (site mature 18–24 mois)

```
- 50–55 pages bien maillées
- 15 pages BOFU
- 20 pages MOFU
- 15 pages TOFU / supports
- Trafic organique majoritaire
- Funnel email actif
```

---

### Scénario 1 — Prudent

**Trafic mensuel : 20 000 visiteurs**

```
Répartition :
- 40% BOFU  = 8 000 visiteurs
- 35% MOFU  = 7 000 visiteurs
- 25% TOFU  = 5 000 visiteurs
```

**Affiliation :**

```
8 000 × 4% clic × 3% conversion × 60€ commission
= 576 clics × 3% = 17 ventes × 60€
≈ 5 760€/mois
```

**Consulting :**

```
7 000 MOFU × 1% leads = 70 leads
70 × 5% closing = 3–4 clients/mois
Ticket moyen : 1 200€
≈ 3 600–4 800€/mois
```

**Formation (2 lancements/an, lissé) :**

```
8 000 emails actifs × 2% = 160 ventes
160 × 297€ = 47 520€ par lancement
2 lancements → 95 040€/an lissé
≈ 8 000€/mois
```

| Source            | /mois              |
| ----------------- | ------------------ |
| Affiliation       | 5 700€             |
| Consulting        | 4 000€             |
| Formation (lissé) | 8 000€             |
| **Total**         | **≈ 17 700€/mois** |
| **Annuel**        | **≈ 212 000€/an**  |

---

### Scénario 2 — Réaliste

**Trafic mensuel : 30 000 visiteurs**

**Affiliation :**

```
12 000 BOFU × 5% clic × 4% conv × 70€
≈ 16 800€/mois
```

**Consulting :**

```
10 clients/mois × 1 500€
= 15 000€/mois
```

**Formation (lissé) :**

```
10 000 emails × 3% = 300 ventes × 297€
= 89 100€ / lancement × 2
≈ 15 000€/mois lissé
```

| Source            | /mois              |
| ----------------- | ------------------ |
| Affiliation       | 16 800€            |
| Consulting        | 15 000€            |
| Formation (lissé) | 15 000€            |
| **Total**         | **≈ 46 800€/mois** |
| **Annuel**        | **≈ 562 000€/an**  |

---

### Scénario 3 — Ambitieux

**Trafic mensuel : 45 000 visiteurs**

| Source                 | /mois              |
| ---------------------- | ------------------ |
| Affiliation            | 25 000€            |
| Consulting premium     | 20 000€            |
| Formation + communauté | 25 000€            |
| **Total**              | **≈ 70 000€/mois** |
| **Annuel**             | **≈ 840 000€/an**  |

---

### Récapitulatif 3 scénarios

| Scénario  | Trafic/mois | CA mensuel | CA annuel |
| --------- | ----------- | ---------- | --------- |
| Prudent   | 20 000      | 17 700€    | 212 000€  |
| Réaliste  | 30 000      | 46 800€    | 562 000€  |
| Ambitieux | 45 000      | 70 000€    | 840 000€  |

---

### Ce qui rend ces chiffres crédibles

```
✓ Niche WordPress = forte intent d'achat
✓ Produits SaaS = commissions élevées
✓ Positionnement business = consulting premium
✓ Cocon structuré = autorité durable
✓ Funnel email = levier multiplicateur
```

### Conclusion stratégique

```
200k€/an = réaliste (scénario prudent bien exécuté)
500k€/an = possible (trafic + funnel actifs)
800k€/an = exigeant mais cohérent avec autorité forte
```

### Ce qui fera la différence

```
- Qualité rédactionnelle (contenu testé, preuves réelles)
- Positionnement business clair (pas juste technique)
- Maillage rigoureux (chaque page connectée)
- Lead magnet performant (entrée funnel forte)
- Autorité LinkedIn en parallèle (amplificateur)
```

---

## AUTHORITY FLYWHEEL — MATRICE COMPLÈTE schoolsWP

### Principe fondamental

Un flywheel fonctionne si :

- Chaque action renforce la suivante
- Le coût marginal diminue avec le temps
- L'autorité devient cumulative
- Les revenus financent la croissance

### Vue macro

```
SEO Content → Trafic → Email → Confiance → Vente
     ↑                                        ↓
     ← ← ← ← Autorité + Preuve + Études ← ← ←
```

---

### Phase 1 — Attraction (SEO + Social)

**Inputs :**

```
- Pillar pages
- Clusters BOFU
- Comparatifs
- Avis produits
- Contenu LinkedIn pédagogique
- Vidéos YouTube tutos
```

**Output :** Trafic organique / Visibilité LinkedIn / Autorité thématique / Premiers backlinks

**KPI :** Trafic organique / Temps passé / CTR / Abonnés LinkedIn

---

### Phase 2 — Capture (Email)

**Inputs — Lead magnets ultra ciblés :**

```
- Checklist hébergement
- Pack SEO Rank Math
- Plan formation en ligne
```

**Output :** Liste email qualifiée + segmentation (SEO / Hébergement / Formation / Funnel)

**KPI :** Taux conversion page → email / Open rate / CTR email

---

### Phase 3 — Activation (Confiance)

**Inputs :**

```
- Séquence email pédagogique
- Études de cas réelles
- Comparatifs approfondis
- Vidéos démonstration
```

**Output :** Confiance / Autorité / Positionnement expert business WP

**KPI :** Réponses email / Engagement LinkedIn / Temps moyen YouTube

---

### Phase 4 — Monétisation (4 flux)

```
1. Affiliation (hosting, SEO, LMS)
2. Consulting
3. Formation signature
4. Templates & ressources premium
```

**KPI :** CA affilié mensuel / Leads consulting / Ventes formation / LTV client

---

### Phase 5 — Amplification

Les ventes génèrent :

```
- Études de cas
- Témoignages
- Preuves sociales
- Backlinks naturels
- Contenu dérivé
```

> Retour à Phase 1 avec autorité renforcée.

---

### Boucle complète

```
Content SEO
   ↓
Trafic qualifié
   ↓
Lead magnet
   ↓
Email nurturing
   ↓
Affiliation / Formation / Consulting
   ↓
Études de cas / Témoignages
   ↓
Autorité renforcée
   ↓
Meilleur ranking SEO
   ↓
Plus de trafic (← boucle)
```

---

### 5 moteurs clés

| Moteur     | Composants                                                         |
| ---------- | ------------------------------------------------------------------ |
| SEO        | 50+ pages clusterisées / maillage interne fort / BOFU prioritaire  |
| Conversion | CTA contextuels / lead magnets spécialisés / landing pages simples |
| Email      | Segmentation / séquence evergreen / upsell progressif              |
| Autorité   | LinkedIn régulier / interviews experts / masterclass live          |
| Preuve     | Études de cas / résultats clients / screenshots GSC / témoignages  |

---

### Matrice synthétique

| Étape         | Actif clé              | Effet sur le système |
| ------------- | ---------------------- | -------------------- |
| SEO           | Pillars + Clusters     | Trafic               |
| Capture       | Lead magnets           | Base email           |
| Activation    | Email + contenu expert | Confiance            |
| Vente         | Offres                 | Cash flow            |
| Amplification | Preuve sociale         | Autorité SEO         |

---

### Pourquoi le Flywheel s'accélère seul

```
Début (M0–M12) :
  Effort élevé → Résultat modéré

Maturité (M12–M24) :
  Effort stable → Résultat exponentiel

Raisons :
  - Google comprend le topic authority
  - L'email convertit mieux avec la confiance
  - Les comparatifs deviennent références
  - Les backlinks arrivent naturellement
```

---

### Projection à maturité (24 mois)

```
Trafic/mois       : 25–35k
Base email        : 10–20k
Affiliation/mois  : 5–15k€
Lancement formation: 20–40k€
Consulting premium: inbound
```

---

## ROADMAP DOMINATION FR WORDPRESS BUSINESS (24 MOIS)

### Positionnement à verrouiller

> "WordPress, mais version business."
> Pas "tutos WordPress". Systèmes : acquisition → conversion → rétention → revenu.

**3 promesses à répéter partout :**

```
1. Un site WordPress plus rapide
2. Un site WordPress qui attire (SEO)
3. Un site WordPress qui vend (funnel + automatisation)
```

---

### Phase 1 — Prise de terrain (M1–M3)

**Objectif :** Planter son drapeau. Avoir 3 piliers qui convertissent.

**Livrables :**

```
- 3 Pillars BOFU : Hébergement / Plugin SEO / Formation en ligne
- 6 pages "avis" à conversion (Rank Math, WP Rocket, Tutor LMS...)
- 2 lead magnets : Checklist Hébergement + Pack SEO Rank Math
```

**Distribution :**

```
- 2 articles SEO / mois
- 2 vidéos YouTube / mois (tuto + démo)
- 2 posts LinkedIn / semaine (pédagogie + opinion)
```

**KPI :**

```
- 1 000 visites/mois organiques
- 300 emails
- 1–3 ventes affiliées/semaine
- 1 lead consulting/mois
```

---

### Phase 2 — Accélération SEO + preuve (M4–M6)

**Objectif :** Faire monter le cocon. Créer la crédibilité "terrain".

**Livrables :**

```
- 15–20 pages cocon (clusters + supports)
- 3 études de cas : vitesse, SEO, conversion
- 1 page "Stack recommandée schoolsWP" (outil-référence)
```

**Systèmes :**

```
- Bloc "Recommandations schoolsWP" standardisé en bas de chaque page BOFU
- Section "Mon protocole de test" sur chaque comparatif
```

**KPI :**

```
- 2 500–4 000 visites/mois
- 1 000 emails
- 500–1 500€/mois affiliation
- 2–3 leads consulting/mois
```

---

### Phase 3 — Autorité externe (M7–M9)

**Objectif :** Sortir du site. Se faire citer. Obtenir des backlinks naturels.

**Livrables :**

```
- 10 interviews (agences, devs perf, SEO, formateurs)
- 6 articles invités (médias/communautés WP FR)
- 1 "State of WordPress Business (FR)" (article annuel massif)
```

**Distribution :**

```
- YouTube : série "Stack business WordPress"
- LinkedIn : carrousels "playbook" (checklists, frameworks)
```

**KPI :**

```
- 6 000–8 000 visites/mois
- 2 500 emails
- 10 backlinks qualifiés
- 3–5 leads consulting/mois
```

---

### Phase 4 — Produit signature (M10–M12)

**Objectif :** Passer de média rentable → marque qui vend.

**Produit signature recommandé — "WordPress Business System" :**

```
Module 1 : SEO & cocon rentable
Module 2 : Performance & stack
Module 3 : Funnel + automatisation (FluentCRM, paiements, séquences)
```

**Livrables :**

```
- 1 masterclass / trimestre (live)
- 1 mini-offre d'entrée (templates + checklist)
- 1 séquence email evergreen (7–10 mails) par pilier
```

**KPI :**

```
- 10 000 visites/mois
- 5 000 emails
- 3 000–6 000€/mois affiliation
- 1er lancement : 5k–20k€ (selon audience)
```

---

### Phase 5 — Domination thématique (M13–M18)

**Objectif :** Devenir "la référence" sur 5 catégories business.

**5 catégories à verrouiller :**

```
1. Hébergement & perf
2. SEO WordPress
3. LMS & formation
4. CRM & automatisation
5. Funnel & monétisation
```

**Livrables :**

```
- 5 super-pillars (10k mots, MAJ trimestrielle)
- 50+ pages cocon
- 1 outil gratuit : calculateur / checklist interactive (lead magnet killer)
```

**KPI :**

```
- 15k–22k visites/mois
- 10k emails
- 5–10k€/mois affiliation
- 6–10 leads consulting/mois
```

---

### Phase 6 — Empire (M19–M24)

**Objectif :** Industrialiser. Partenariats. Communauté. Moat.

**Livrables :**

```
- Communauté premium (petite, chère, utile)
- Partenariats marques WP (codes exclusifs, contenus co-brandés)
- "Playbooks schoolsWP" (bundle templates + SOP)
- 2 lancements/an de la formation signature
```

**KPI :**

```
- 25k–35k visites/mois
- 15k–20k emails
- 10k€/mois affiliation (stable)
- 20k–40k€ par lancement formation
- Consulting premium inbound : 5–10k€/mois
```

---

### 7 leviers qui construisent le moat

```
1. Protocole de test (tu n'es plus un blog, tu es un labo)
2. Pages "stack" (tu deviens la référence outil)
3. Comparatifs ultra concrets (tableaux + cas d'usage)
4. Cocon + maillage (effet cumulatif)
5. Email segmenté (SEO → email → vente)
6. Preuves (GSC, CWV, résultats clients)
7. Partenariats (backlinks + codes + visibilité)
```

---

### Cadence hebdo d'exécution

```
1 contenu SEO (ou 1 MAJ majeure) / semaine
2 posts LinkedIn / semaine
1 vidéo YouTube / semaine (ou 2/mois)
1 newsletter / semaine
1 action autorité / semaine (interview, outreach, partenariat)
```

---

## schoolsWP OS™ — SYSTÈME DE PROMPT ENGINEERING INTERNE

### Vue d'ensemble

6 frameworks de prompt engineering organisés en 3 niveaux :

```
THINKING LAYER  → Architecture Blueprint (SPECS) + Decision Engine (COT)
BUILD LAYER     → Strategic Engine (CREDO) + Omnichannel Engine (DITO)
GROWTH LAYER    → Growth Loop (PACT) + Performance Loop (TDD)
```

### Diagramme opérationnel

```
┌──────────────────────────┐
│   1. ARCHITECTURE        │
│   Blueprint (SPECS)      │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│   2. DECISION            │
│   Engine (COT)           │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│   3. PRODUCTION          │
│   Strategic Engine       │
│   (CREDO)                │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│   4. TRANSFORMATION      │
│   Omnichannel Engine     │
│   (DITO)                 │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│   5. EXPERIMENTATION     │
│   Growth Loop (PACT)     │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│   6. OPTIMISATION        │
│   Performance Loop       │
│   (TDD)                  │
└─────────────┬────────────┘
              │
              ▼
       ┌─────────────┐
       │   SCALE     │
       │   ou        │
       │   ITERATE   │
       └─────────────┘
```

### Règles fondamentales

```
✓ Rien sans cadre.
✓ Rien sans KPI.
✓ Rien sans test.
✓ Rien sans optimisation.
✓ Chaque contenu doit scaler.
```

---

### Module 1 — Architecture Blueprint (SPECS)

**Nom complet :** schoolsWP Architecture Blueprint
**Framework :** SPECS = Scope · Purpose · Environment · Constraint · Success criteria
**Quand l'utiliser :** nouvelle page pilier / nouvelle offre / nouvelle formation / nouveau cluster / nouveau tunnel

```
[S] SCOPE
- Périmètre inclus :
- Périmètre exclu :
- Niveau de profondeur attendu :
- Livrables concernés :

[P] PURPOSE
- Problème à résoudre :
- Résultat business recherché :
- Impact principal (trafic / autorité / leads / conversion / rétention) :
- KPI cible :

[E] ENVIRONMENT
- Site : schoolsWP.com
- Audience : freelances / créateurs / entrepreneurs WordPress
- Stack : (Rank Math, Fluent Suite, etc.)
- Sources de données : (GSC, GA4, DataForSEO…)
- Ressources disponibles :
- Contraintes techniques existantes :

[C] CONSTRAINT
- Temps disponible :
- Complexité acceptable :
- Budget si applicable :
- Ton : direct, actionnable, sans jargon inutile
- Interdictions : théorie vague, fluff, généralités

[S] SUCCESS CRITERIA
- Indicateurs mesurables :
- Délai d'évaluation :
- Seuil de validation :
- Signal d'échec :
- Prochaine itération prévue :

FORMAT DE RÉPONSE ATTENDU
1) Résumé exécutif
2) Diagnostic
3) Plan d'action priorisé
4) Version rapide
5) Version complète
6) Méthode de mesure selon les Success criteria
7) Étape suivante logique
```

---

### Module 2 — Decision Engine (COT structuré)

**Nom complet :** schoolsWP Decision Engine
**Framework :** COT = Chain Of Thought structuré
**Quand l'utiliser :** choisir un outil / prioriser un chantier / arbitrer entre 2 stratégies / décider d'un pivot

```
INSTRUCTION

Avant de répondre :
1) Clarifie le problème exact
2) Identifie les variables clés
3) Analyse les options possibles
4) Évalue les impacts SEO / business / technique
5) Priorise selon ROI et faisabilité
6) Produis une réponse structurée et actionnable

FORMAT DE RÉPONSE ATTENDU
1) Diagnostic clair
2) Facteurs clés identifiés
3) Options stratégiques comparées
4) Recommandation priorisée
5) Justification synthétique
6) Plan d'exécution concret
```

---

### Module 3 — Strategic Engine (CREDO)

**Nom complet :** schoolsWP Strategic Engine
**Framework :** CREDO = Context · Role · Example · Deliverable · Outcome
**Quand l'utiliser :** article pilier / landing / lead magnet / séquence email / module formation

```
[C] CONTEXT
Tu interviens pour schoolsWP.com, média et écosystème dédié à WordPress.
Audience : freelances, créateurs, formateurs, entrepreneurs WordPress.
Objectif : contenu à forte valeur stratégique, exploitable immédiatement,
optimisé SEO + IA (Google SGE, ChatGPT, Perplexity).
Contrainte : ton direct, clair, concret. Zéro blabla.

[R] ROLE
Tu es un expert WordPress senior + consultant SEO stratégique + architecte automation.
Tu raisonnes en priorité business : trafic qualifié, autorité, conversion, scalabilité.
Tu proposes uniquement des recommandations actionnables.

[E] EXAMPLE (STYLE ATTENDU)
Structure claire. Titres hiérarchisés. Checklist priorisée.
Blocs prêts à intégrer. Toujours orienté mise en œuvre immédiate.

[D] DELIVERABLE
1) Résumé stratégique en 5 lignes maximum
2) Analyse structurée
3) Checklist d'actions priorisées (P1 / P2 / P3)
4) Version "quick wins" (30 min)
5) Version "optimisation complète"
6) Si SEO contenu : plan H2/H3 + FAQ optimisée IA
7) Si technique : réglages précis
8) Comment mesurer dans Google Search Console

[O] OUTCOME
- Augmenter la clarté stratégique
- Améliorer la performance SEO
- Renforcer la citabilité IA
- Favoriser la conversion
- Être directement exploitable sans retravail

Si des informations manquent, poser maximum 3 questions.
Sinon, exécuter immédiatement.
```

---

### Module 4 — Omnichannel Engine (DITO)

**Nom complet :** schoolsWP Omnichannel Engine
**Framework :** DITO = Define · Input · Transformation · Output
**Quand l'utiliser :** article → LinkedIn / vidéo → SEO / transcript → cluster / repurposing massif

```
[D] DEFINE
- Objectif principal :
- Canal cible : (Article / LinkedIn / Newsletter / Email / YouTube / Lead magnet…)
- Intention SEO cible :
- Niveau de profondeur : (court / stratégique / expert)
- Résultat business attendu :

[I] INPUT
- Type d'input : (article / transcript / notes / données SEO / capture / CSV…)
- Contenu brut :
- Mots-clés principaux :
- Angle stratégique existant :
- Contraintes spécifiques :

[T] TRANSFORMATION
- Type : (résumer / structurer / optimiser SEO / convertir en carrousel / extraire FAQ…)
- Niveau d'optimisation IA : (citabilité / featured snippet / SGE / FAQ)
- Structure attendue :
- Éléments à inclure :
- Éléments à exclure :

[O] OUTPUT
- Format : (Markdown / prêt à publier / script vidéo…)
- Longueur cible :
- Ton : direct, clair, actionnable (style schoolsWP)
- Structure obligatoire :
- Blocs spécifiques : (H2/H3, FAQ, métadonnées, CTA…)

FORMAT DE RÉPONSE ATTENDU
1) Résultat final directement exploitable
2) Optimisation SEO intégrée naturellement
3) Structure hiérarchisée claire
4) Aucun blabla inutile
5) CTA cohérent avec l'objectif

Si l'input est insuffisant, poser maximum 3 questions.
Sinon, transformer immédiatement.
```

---

### Module 5 — Growth Loop (PACT)

**Nom complet :** schoolsWP Growth Loop
**Framework :** PACT = Problem · Approach · Constraint · Test
**Quand l'utiliser :** tester un title / un CTA / un angle / un hook / une landing

```
[P] PROBLEM
- Symptôme observé :
- Problème structurel supposé :
- Impact business actuel :
- Page / tunnel / cluster concerné :
- Données disponibles (GSC, GA4, CTR…) :

[A] APPROACH
- Hypothèse principale :
- Angle stratégique choisi :
- Action prioritaire à tester :
- Levier principal (SEO contenu / technique / UX / offre / automation / CTA) :
- Étapes concrètes d'exécution :

[C] CONSTRAINT
- Temps disponible :
- Complexité acceptable :
- Stack WordPress utilisée :
- Ressources disponibles :
- Interdictions : jargon inutile, refonte complète si non nécessaire

[T] TEST
- KPI principal à mesurer :
- KPI secondaire :
- Seuil de réussite :
- Délai d'observation :
- Signal d'échec :
- Plan si échec :

FORMAT DE RÉPONSE ATTENDU
1) Résumé du problème réel
2) Hypothèse stratégique
3) Plan d'action concret
4) Implémentation rapide (≤ 30 min si possible)
5) Méthode de test précise
6) Prochaine itération logique
```

---

### Module 6 — Performance Loop (TDD)

**Nom complet :** schoolsWP Performance Loop
**Framework :** TDD = Test · Develop · Debug
**Quand l'utiliser :** optimiser CTR / conversion / open rate / position SEO

```
[T] TEST
- Objectif exact :
- KPI principal :
- KPI secondaire :
- Seuil de réussite :
- Délai d'évaluation :
- Données de référence (baseline) :

[D] DEVELOP
- Action principale :
- Ajustements secondaires :
- Stack utilisée :
- Ressources nécessaires :
- Temps estimé :

Exécuter uniquement ce qui influence directement le KPI défini.

[D] DEBUG
- Résultat observé :
- Écart vs objectif :
- Cause probable :
- Ajustement à tester :
- Décision : itérer / pivoter / scaler

FORMAT DE RÉPONSE ATTENDU
1) Définition claire du test
2) Plan d'implémentation
3) Méthode de mesure
4) Analyse des résultats
5) Prochaine itération recommandée
```

---

### Tableau de sélection rapide

| Situation                     | Module à utiliser              |
| ----------------------------- | ------------------------------ |
| Démarrer un nouveau projet    | Architecture Blueprint (SPECS) |
| Hésiter entre 2 options       | Decision Engine (COT)          |
| Produire un contenu clé       | Strategic Engine (CREDO)       |
| Décliner sur plusieurs canaux | Omnichannel Engine (DITO)      |
| Tester une hypothèse          | Growth Loop (PACT)             |
| Optimiser un actif existant   | Performance Loop (TDD)         |

---

### Comparatif des frameworks

| Framework                      | Orientation                      |
| ------------------------------ | -------------------------------- |
| RACE                           | Exécution rapide                 |
| CREDO (Strategic Engine)       | Production stratégique premium   |
| SPECS (Architecture Blueprint) | Cadrage produit / architecture   |
| PACT (Growth Loop)             | Résolution + expérimentation     |
| DITO (Omnichannel Engine)      | Transformation & automatisation  |
| COT (Decision Engine)          | Décision structurée              |
| TDD (Performance Loop)         | Amélioration continue rigoureuse |

---

### Prompt RACE (référence)

**Framework :** RACE = Role · Action · Context · Expectation
**Nom :** AI Strategic Engine schoolsWP (version rapide)

```
[R] ROLE
Tu es un expert WordPress senior spécialisé en SEO (Google + Bing), performance,
sécurité, automatisation (FluentCRM / Fluent Forms / TutorLMS / FluentBooking)
et conversion. Tu réponds en français, style schoolsWP : direct, concret,
phrases courtes. Zéro blabla. Tu proposes des actions applicables immédiatement.

[A] ACTION
Ta mission : produire une recommandation opérationnelle et priorisée sur : [SUJET].
Tu dois :
1) Diagnostiquer rapidement la situation
2) Proposer des actions concrètes (checklist) avec ordre de priorité
3) Donner une version "quick wins (30 min)" + une version "propre (2–3 h)"
4) Fournir si utile : snippets, réglages plugin, ou structure de page

[C] CONTEXT
- Site : schoolsWP.com
- Audience : freelances / créateurs / entrepreneurs WordPress
- Objectif business : trafic qualifié + citabilité IA + conversion
- Contrainte : pas de jargon marketing, pas de théorie inutile
- URL : [URL]
- Intention cible : [INTENTION]
- Mot-clé principal : [KW_MAIN]
- Mots-clés secondaires : [KW_SECONDARY]
- Outils : Rank Math Pro, GSC, GA4
- Input : [CONTENU / CAPTURE]

[E] EXPECTATION (FORMAT DE SORTIE)
1) Résumé en 5 lignes (ce qui bloque / ce qui manque)
2) Priorités (P1 / P2 / P3) + effort estimé (S/M/L)
3) Quick wins (30 min) : checklist
4) Version propre (2–3 h) : checklist détaillée
5) Si SEO contenu : structure H2/H3 + FAQ (5 questions)
6) Si SEO images : bloc métadonnées (XPTitle / XPSubject / XPKeywords)
7) Mesure : comment valider dans GSC
8) Next step : 3 questions max si info manquante

Si c'est OK, exécuter directement sans demander d'autorisation.
```

---

### Version Notion — schoolsWP OS Command Center

**Propriétés (colonnes) :**

```
Nom          : Titre de la tâche / projet / contenu
Module OS    : Architecture Blueprint / Decision Engine / Strategic Engine /
               Omnichannel Engine / Growth Loop / Performance Loop
Type d'actif : Article pilier / Landing / Lead magnet / Séquence email /
               Post LinkedIn / Vidéo / Formation / Offre / Automation
Statut       : Blueprint → Décision → Production → Transformation →
               Test → Optimisation → Scale → Terminé
Priorité     : P1 stratégique / P2 important / P3 opportunité
Objectif     : Trafic / Leads / Conversion / Autorité
KPI principal: (ex: CTR / Position SEO / Leads)
Baseline     : (ex: CTR 2.1%)
Objectif KPI : (ex: CTR 4%)
Canaux       : SEO / LinkedIn / Newsletter / Email / YouTube / Formation
Résultat     : (post-test)
Décision     : Scale / Optimiser / Pivoter / Abandonner
```

**Vues recommandées :**

```
1. Pipeline OS       → Board par Statut
2. Growth Experiments → Filtre : Module OS = Growth Loop
3. Optimisation      → Filtre : Module OS = Performance Loop
4. Production        → Filtre : Module OS = Strategic Engine
```

**Règle systémique :**

```
Chaque actif DOIT passer par :
Blueprint → Production → Transformation → Test → Optimisation
```

---

## CHECKLIST QUOTIDIENNE — schoolsWP OS

### Étape 1 — Vérifier les signaux (5 min)

- GSC → CTR / impressions / position
- Trafic page pilier principale
- Conversions / leads / clics affiliés
- **Question clé** : Où est le levier aujourd'hui ?

### Étape 2 — Décider l'action du jour (2 min)

Choisir **UNE seule priorité** : créer / transformer / tester / optimiser

> Règle : 1 action principale / jour

### Étape 3 — Produire ou transformer (temps principal)

- **Cas A — Production** → Strategic Engine (SPECS → COT → DITO → article / page)
- **Cas B — Transformation** → Omnichannel Engine (article → thread / newsletter / vidéo / lead magnet)

### Étape 4 — Lancer un micro-test (5 min)

Growth Loop — 1 variable seulement (titre / CTA / angle / format)

### Étape 5 — Optimiser un actif existant (5–10 min)

Performance Loop — 1 page à améliorer (maillage / meta / structure / CTA)

### Règle fondamentale

```
✔ 1 création ou transformation / jour
✔ 1 test / jour
✔ 1 optimisation / jour
```

### Raccourci mental

```
Signal → Décision → Créer ou Transformer → Tester → Optimiser
```

### Version ultra simple

1. Quel est le levier aujourd'hui ?
2. Quel contenu je crée ou transforme ?
3. Qu'est-ce que j'améliore ?

---

## schoolsWP OS™ — AUTO-ROUTER (Prompt système unique)

### Prompt maître

```
Tu es l'AI Operating System interne de schoolsWP.
Tu réponds en français, style schoolsWP : direct, concret, phrases courtes.
Objectif : activer automatiquement le bon module (SPECS / COT / CREDO / DITO / PACT / TDD) selon mon besoin, sans me poser 15 questions.

RÈGLE D'OR
1 seul module principal par réponse (max 2 si indispensable).
Tu commences par annoncer : "Module activé : ____".
Puis tu exécutes immédiatement.

ENTRÉE (ce que je te donne)
- Besoin / demande : [MON BESOIN]
- Contexte : [OPTIONNEL]
- Données : [OPTIONNEL] (URL, extrait, GSC, notes, capture, CSV, etc.)
- Contraintes : [OPTIONNEL] (temps, stack WP, objectif…)

ÉTAPE 1 — ROUTING (diagnostic rapide)
Détecte l'intention et choisis le module :

A) Cadrer / définir / architecturer (offre, page pilier, formation, tunnel, cluster, système)
→ Module = SPECS (Architecture Blueprint)

B) Trancher / prioriser / choisir entre options / décider
→ Module = COT (Decision Engine)

C) Produire un livrable premium final (article, landing, séquence, plan, contenu complet)
→ Module = CREDO (Strategic Engine)

D) Transformer / recycler / décliner un contenu (article → LinkedIn, vidéo → SEO, notes → email)
→ Module = DITO (Omnichannel Engine)

E) Tester une hypothèse (title, CTA, angle, hook, structure) avec logique d'expérimentation
→ Module = PACT (Growth Loop)

F) Optimiser en boucle à partir de résultats (CTR, conversion, positions, open rate) et itérer
→ Module = TDD (Performance Loop)

Si plusieurs intentions : choisir la plus bloquante (le "goulot").
Si flou : mini COT (30 secondes) et choisir quand même un module.

ÉTAPE 2 — EXÉCUTION (format standard)

1) Module activé : [MODULE]
2) Résumé (2–5 lignes) : ce que je vais faire + pourquoi
3) Livraison principale : le livrable attendu
4) Next step : 1 action concrète + max 3 questions ciblées si bloquant

FORMATS PAR MODULE

SPECS (Architecture Blueprint)
- Scope / Purpose / Environment / Constraints / Success criteria
- Plan d'action P1/P2/P3

COT (Decision Engine)
- Options (2–4) + critères + recommandation
- Décision + plan d'exécution

CREDO (Strategic Engine)
- Livrable final prêt à publier
- Structure claire + blocs (H2/H3, FAQ, CTA) si pertinent

DITO (Omnichannel Engine)
- Output final + déclinaisons
- Templates prêts à coller (LinkedIn, email, newsletter, etc.)

PACT (Growth Loop)
- Hypothèse → action → test → seuil → délai
- Un test à la fois + plan si échec

TDD (Performance Loop)
- Baseline → changement → mesure → debug → itération suivante
- Priorité ROI + effort (S/M/L)

CONTRAINTES DE STYLE
- Zéro blabla. Zéro théorie.
- Toujours actionnable.
- Si tu proposes un outil WordPress, donne le réglage précis ou l'étape exacte.
- Si tu dois poser des questions : max 3, uniquement si ça bloque l'exécution.
```

### Table de routing rapide

| Besoin                           | Module |
| -------------------------------- | ------ |
| Créer une page pilier            | SPECS  |
| Choisir entre FluentCRM et Brevo | COT    |
| Écrire la page prête à publier   | CREDO  |
| Transformer article → carrousel  | DITO   |
| Tester 2 titles CTR              | PACT   |
| Le CTR a bougé, on itère         | TDD    |

### Exemple de sortie — SPECS (page pilier)

**Module activé : SPECS (Architecture Blueprint)**

**S — Scope**

- Sujet : [SUJET]
- Type : Guide pilier evergreen
- Inclus : guide complet, tutoriel, FAQ, ressources, maillage satellites
- Exclus : actualités, comparatifs hors sujet

**P — Purpose**

- Problème : L'utilisateur veut comprendre [SUJET] et l'appliquer sur WordPress
- Impact : trafic SEO qualifié + autorité + captation emails + conversion formation
- KPI principal : Top 3 sur mot-clé principal

**E — Environment**

- Site : schoolsWP.com
- Audience : freelances WP, créateurs, entrepreneurs web (débutant → intermédiaire)
- Stack : Rank Math, FluentCRM, FluentForms, Gutenberg

**C — Constraints**

- Ton : pédagogique, clair, actionnable, sans jargon
- Structure : H2 logiques + étapes numérotées + exemples + FAQ
- Longueur cible : 2 000 → 4 000 mots

**S — Success Criteria**

- Top 10 en 3 mois / Top 3 en 9–12 mois
- Temps moyen > 3 min
- Citations IA naturelles

**Structure recommandée**

```
H1 — Guide complet : [SUJET]
H2 — Qu'est-ce que [SUJET]
H2 — Pourquoi c'est important
H2 — Comment mettre en place [SUJET] (étapes)
H2 — Outils recommandés
H2 — Erreurs à éviter
H2 — Cas pratique
H2 — FAQ
```

**Maillage interne** : 4–6 articles satellites à pointer depuis la pilier

**Next step** : Donne-moi `SUJET = ?` → je génère structure SEO complète + cluster + maillage exact.

---

### Exemple de sortie — COT (FluentCRM vs Brevo)

**Module activé : COT (Decision Engine)**

**Les 2 options**

| Critère         | FluentCRM                              | Brevo                         |
| --------------- | -------------------------------------- | ----------------------------- |
| Hébergement     | Self-hosted WordPress                  | SaaS externe                  |
| Données         | Sur ton serveur                        | Chez Brevo                    |
| Contacts        | Illimités                              | Selon plan                    |
| Tarification    | Annuelle fixe (~129 $/an)              | Volume d'envois mensuel       |
| Intégrations WP | Natives (LearnDash, WooCommerce, etc.) | Via plugin + API              |
| Multicanal      | Email uniquement                       | Email + SMS + WhatsApp + chat |
| Délivrabilité   | Dépend de ton SMTP                     | Infrastructure gérée          |
| Transactionnel  | Via SMTP tiers                         | Inclus dans tous les plans    |

**Critères de décision**

1. Centre de gravité WordPress → FluentCRM
2. Centre de gravité multicanal SaaS → Brevo
3. Maîtrise des coûts long terme → FluentCRM
4. Simplicité délégable / délivrabilité gérée → Brevo

**Recommandation nette pour schoolsWP**

> **FluentCRM** = choix stratégique — écosystème WordPress cohérent, propriétaire, données maîtrisées.
> **Brevo** = choix opérationnel uniquement si besoin multicanal fort ou stack moins WordPress-centric.

**Plan d'exécution (FluentCRM)**

1. FluentCRM comme CRM principal dans WordPress
2. SMTP sérieux pour les envois (Postmark / Amazon SES / Brevo SMTP)
3. Tags + listes + scoring + automations dans FluentCRM
4. Brevo en complément éventuel pour transactionnel ou multicanal

**Next step** : comparatif 10 critères FluentCRM vs Brevo (coût / délivrabilité / WP / LMS / WooCommerce / automatisations / données / maintenance / scalabilité / simplicité)

---

### Exemple de sortie — CREDO (page pilier schoolsWP OS)

**Module activé : CREDO (Strategic Engine)**

---

# schoolsWP OS : la méthode pour penser, créer et optimiser un site WordPress avec l'IA

Créer du contenu ne suffit plus.

Pour qu'un site WordPress devienne un véritable levier de croissance, il faut un système. Un système pour réfléchir avant de produire, produire du contenu utile, transformer chaque contenu en actif, tester ce qui fonctionne, optimiser en continu.

C'est exactement ce que permet schoolsWP OS. Une méthode simple basée sur 6 modules complémentaires.

## Pourquoi créer un OS pour WordPress ?

La plupart des créateurs fonctionnent comme ça : 1 contenu → publié → oublié.

Résultat : peu de trafic durable, peu d'autorité, peu de conversion.

Le problème n'est pas le contenu. Le problème est l'absence de système.

schoolsWP OS transforme ton site en machine d'autorité, machine SEO, machine de conversion.

## La structure du schoolsWP OS

La méthode repose sur 6 modules. Ils correspondent à 6 étapes logiques :

```
Architecture → Décision → Production → Transformation → Test → Optimisation
```

### 1. Architecture Blueprint (SPECS)

Avant de produire quoi que ce soit, il faut définir le cadre.

Il sert à structurer : une page pilier, un cluster SEO, une formation, une offre, un tunnel.

Le framework SPECS :

- **S**cope — le périmètre
- **P**urpose — l'objectif
- **E**nvironment — le contexte
- **C**onstraints — les contraintes
- **S**uccess Criteria — les critères de réussite

### 2. Decision Engine (COT)

Dans WordPress, les décisions sont constantes : quel plugin choisir, quelle stratégie SEO adopter, quel angle éditorial utiliser.

Le module Decision Engine utilise un raisonnement structuré (Chain Of Thought) pour analyser les options, comparer les impacts, prioriser selon le ROI.

Résultat : moins d'hésitation, plus de clarté.

### 3. Strategic Engine (CREDO)

Le module de production principale. On l'utilise pour créer un article SEO, une page pilier, une landing page, un lead magnet, une séquence email, un module de formation.

Le framework CREDO :

- **C**ontext
- **R**ole
- **E**xample
- **D**eliverable
- **O**utcome

Ce module garantit que chaque contenu répond à un objectif, apporte une vraie valeur et est directement exploitable.

### 4. Omnichannel Engine (DITO)

Un contenu ne doit jamais rester isolé. Ce module transforme un contenu en plusieurs formats.

Exemples : Article → LinkedIn, Article → newsletter, Vidéo → article SEO, Transcript → cluster d'articles.

Le framework DITO :

- **D**efine
- **I**nput
- **T**ransformation
- **O**utput

C'est la clé pour scaler ton contenu sans repartir de zéro.

### 5. Growth Loop (PACT)

Une fois le contenu publié, il faut tester. Exemples : tester un nouveau title SEO, tester un CTA, tester un hook, tester une structure d'article.

Le framework PACT :

- **P**roblem
- **A**pproach
- **C**onstraint
- **T**est

Chaque expérimentation doit mesurer un seul élément.

### 6. Performance Loop (TDD)

Le module Performance Loop permet d'améliorer ce qui existe : augmenter le CTR, améliorer une landing, optimiser une séquence email, renforcer un cluster SEO.

Le framework TDD :

- **T**est
- **D**evelop
- **D**ebug

C'est une boucle continue : mesurer → ajuster → améliorer.

## Le workflow complet

```
1. Architecture Blueprint  →  cadrer
2. Decision Engine         →  décider
3. Strategic Engine        →  produire
4. Omnichannel Engine      →  transformer
5. Growth Loop             →  tester
6. Performance Loop        →  optimiser
```

Ce processus transforme chaque contenu en actif cumulatif.

## Exemple concret — page pilier maintenance WordPress

- Étape 1 (SPECS) → définir la structure SEO
- Étape 2 (CREDO) → écrire l'article complet
- Étape 3 (DITO) → transformer en carrousel LinkedIn + newsletter + vidéo
- Étape 4 (PACT) → tester plusieurs titles
- Étape 5 (TDD) → optimiser le CTR dans Google

Résultat : un contenu qui continue à produire du trafic.

## Pourquoi cette méthode fonctionne

1. **Penser avant de produire** — beaucoup de contenu échoue car il n'est pas structuré.
2. **Transformer chaque contenu** — un contenu doit vivre sur plusieurs canaux.
3. **Optimiser en continu** — le SEO est une boucle, pas une action unique.

## Conclusion

La différence entre un blog qui stagne et un site qui grandit n'est pas la motivation. C'est le système.

schoolsWP OS est conçu pour transformer WordPress en véritable levier de croissance.

---

### Exemple de sortie — DITO (Article → Carrousel LinkedIn)

**Module activé : DITO (Omnichannel Engine)**

#### Prompt de transformation

```
INPUT
- Article source : [COLLER L'ARTICLE]
- Objectif du post : [autorité / trafic / leads / engagement]
- CTA final : [commentaire / message privé / lien / newsletter]
- Audience cible : [freelances / créateurs / entrepreneurs WordPress]

TRANSFORMATION
À partir de l'article :
1) Extraire l'idée centrale
2) Identifier les 5 à 10 points les plus utiles
3) Reformuler chaque point pour un format slide LinkedIn
4) Simplifier sans appauvrir
5) Garder un ton direct, concret, pédagogique, style schoolsWP
6) Créer une progression logique slide par slide
7) Ajouter une slide finale avec CTA naturel

OUTPUT ATTENDU
1) Titre de carrousel fort
2) Structure complète slide par slide :
   - numéro de slide
   - titre court
   - texte à afficher
3) Légende LinkedIn d'accompagnement
4) 3 hooks alternatifs
5) 5 hashtags maximum, pertinents

CONTRAINTES
- Français
- Ton schoolsWP : direct, utile, concret
- Phrases courtes
- Pas de jargon inutile
- Pas de blabla motivationnel
- Chaque slide apporte une vraie valeur
- Prêt à designer dans Canva
```

#### Format de sortie obligatoire

```
Slide 1   = hook fort
Slides 2–7/8 = idées clés
Avant-dernière = synthèse ou erreur à éviter
Dernière  = CTA simple
```

#### Autres transformations DITO disponibles

| Input              | Output                       |
| ------------------ | ---------------------------- |
| Article SEO        | Carrousel LinkedIn           |
| Article SEO        | Thread X                     |
| Article SEO        | Newsletter (intro + 3 blocs) |
| Article SEO        | Script vidéo YouTube         |
| Vidéo / transcript | Article SEO                  |
| Notes / bullets    | Article structuré            |
| Article            | Lead magnet PDF (plan)       |
| Article            | Séquence email 3 jours       |

**Règle DITO** : 1 contenu source → N formats. Ne jamais repartir de zéro.

---

### Exemple de sortie — DITO (Carrousel LinkedIn Fluent Forms)

**Module activé : DITO (Omnichannel Engine)**
**Angle** : Le gratuit te rassure. Le Pro te rapporte.
**Format** : 10 slides — ton tranchant, polarisant

#### Structure des slides

**Slide 1 — Hook**

> Label : COMPARATIF 2026
> Titre : Fluent Forms gratuit peut te faire perdre de l'argent
> Sous-texte : Oui, il est gratuit à l'entrée. Non, il n'est pas toujours rentable à la sortie.
> Micro-copy : _Le "gratuit" peut coûter plus cher._

**Slide 2 — Remise en place**

> Titre : Le gratuit n'est pas mauvais
> Sous-texte : Pour un formulaire de contact, il fait très bien le boulot.
> Micro-copy : _Pour commencer : oui. Pour scaler : non._

**Slide 3 — Le coup caché**

> Label : PROBLÈME
> Titre : Le piège, c'est le +1,9 %
> Sous-texte : En version gratuite, Stripe te coûte plus cher à chaque transaction.
> Micro-copy : _Chaque vente te rapporte moins._

**Slide 4 — La phrase qui fait mal**

> Label : RÉALITÉ BUSINESS
> Titre : Plus tu vends, plus le gratuit te pénalise
> Micro-copy : _Tu ne paies pas la licence. Tu paies en silence._

**Slide 5 — Le switch**

> Label : VERSION PRO
> Titre : Pro arrête l'hémorragie
> Sous-texte : Zéro surcoût Stripe. Plus de liberté. Plus de rentabilité.
> Micro-copy : _Tu reprends le contrôle de ta marge._

**Slide 6 — Le vrai game changer**

> Label : CONVERSION
> Titre : Pro ne fait pas juste "plus"
> Sous-texte : devis auto, calculs dynamiques, remises conditionnelles, parcours fluides.
> Micro-copy : _On passe de formulaire à tunnel._

**Slide 7 — Impact utilisateur**

> Label : EXPÉRIENCE
> Titre : Les formulaires longs ne font pas fuir… les mauvais formulaires si
> Micro-copy : _Moins d'abandon. Plus de complétions._

**Slide 8 — Impact business**

> Label : AUTOMATISATION
> Titre : Le vrai luxe : ne plus faire les tâches à la main
> Micro-copy : _Moins d'admin. Plus d'exécution._

**Slide 9 — Verdict**

> Label : VERDICT
> Titre : Gratuit pour tester. Pro pour construire quelque chose de sérieux
> Free : contact simple, zéro vente, zéro automatisation
> Pro : paiements, devis, CRM, croissance
> Micro-copy : _Le gratuit aide à démarrer. Le Pro aide à gagner._

**Slide 10 — CTA**

> Label : À FAIRE
> Titre : Arrête de choisir "gratuit" par réflexe
> CTA principal : Lis le comparatif complet sur schoolsWP
> CTA secondaire : Code promo schoolsWP20
> Micro-copy : _Le bon choix n'est pas le moins cher. C'est le plus rentable._

#### Légende LinkedIn

```
Fluent Forms gratuit peut te coûter plus cher que la version Pro.

Oui, tu as bien lu.

Le gratuit est très bon pour démarrer.
Mais dès que tu encaisses avec Stripe, il ajoute 1,9 % de surcoût.

La vraie question n'est pas :
"Est-ce que le gratuit suffit ?"

La vraie question, c'est :
"À partir de quand il commence à me faire perdre de l'argent ?"

Tu choisis encore tes plugins pour économiser…
ou pour construire un vrai système rentable ?
```

#### 5 hooks alternatifs

```
A — Le plus gros piège de Fluent Forms Free ? Il s'appelle "gratuit".
B — Tu n'économises pas avec Fluent Forms Free. Tu repousses juste la facture.
C — Le gratuit est séduisant. Ta marge, beaucoup moins.
D — Fluent Forms Free est parfait… jusqu'à ce qu'il commence à te coûter trop cher.
E — Ce n'est pas parce qu'un plugin est gratuit qu'il est rentable.
```

---

## WORDPRESS MATURITY MODEL — Les 5 niveaux

Framework WordCamp — slide deck pédagogique.

### Vue d'ensemble

```
1️⃣  Blog amateur        → contenu sans stratégie
2️⃣  Site vitrine        → présence sans acquisition
3️⃣  Site SEO            → trafic sans système
4️⃣  Système d'acquisition → leads sans boucle
5️⃣  Machine de croissance → infrastructure complète
```

**Accroche slide** : _"À quel niveau est votre site ?"_ — déclic immédiat dans la salle.

---

### Niveau 2 — Site vitrine

**Titre slide** : Niveau 2 — Site vitrine

Le site existe. Mais il ne travaille pas vraiment.

**Diagramme** :

```
Entreprise → WordPress → Information
```

**Caractéristiques** :

- Page d'accueil, À propos, Services, Contact, parfois blog
- Pas de stratégie SEO, pas de capture, pas d'automatisation, pas de logique de conversion
- Dépend du bouche-à-oreille, du réseau, des plateformes externes

**Message clé** : Un site vitrine est utile pour exister. Il ne suffit pas pour générer une croissance durable.

**Pour passer au niveau 3** : architecture de contenu + stratégie SEO + pages ciblant des intentions + maillage interne.

---

### Niveau 5 — Machine de croissance automatisée

**Titre slide** : Niveau 5 — WordPress Growth Machine

Le site devient un système qui travaille en continu. Infrastructure digitale complète.

**Boucle de croissance** :

```
SEO → Trafic qualifié → Contenu → Capture email
→ Segmentation CRM → Automatisation → Offres
→ Revenus → Autorité → Plus de trafic
```

**Caractéristiques** :

- Génère du trafic SEO
- Capture des leads automatiquement
- Segmente et score les contacts
- Envoie des séquences automatisées
- Propose des offres adaptées — sans intervention manuelle

**Exemple de parcours visiteur** :

```
1. Arrive via Google (article SEO)
2. Télécharge une ressource
3. Entre dans une séquence email
4. Découvre une formation
5. Devient client
→ Tout est automatisé
```

**Briques du système** :

| Couche         | Outils / actions               |
| -------------- | ------------------------------ |
| Acquisition    | SEO, contenu stratégique       |
| Capture        | Formulaires, lead magnets      |
| CRM            | Segmentation, scoring          |
| Automatisation | Séquences email, nurturing     |
| Monétisation   | Formations, services, produits |

**Diagramme WordCamp** :

```
Traffic → Content → WordPress → Automation → Leads → Customers
```

**Message final** : Un site WordPress peut être un blog, une vitrine, ou une machine de croissance. Le choix est une décision stratégique.

---

## WORDCAMP TALK SIGNATURE — schoolsWP

### Pitch 30 secondes (versions)

**Version standard**

> Je suis Michaël KIHL, fondateur de schoolsWP. schoolsWP aide les freelances, créateurs et entrepreneurs à transformer leur site WordPress en véritable levier de croissance. La plupart des ressources expliquent comment utiliser WordPress. Nous expliquons comment construire un système complet avec WordPress : SEO, automatisation, contenu, CRM et monétisation.

**Version ultra punch (20 sec)**

> Je suis Michaël KIHL, fondateur de schoolsWP. J'aide les freelances et entrepreneurs à transformer WordPress en véritable moteur de croissance. Pas seulement un site. Un système complet qui combine SEO, automatisation et contenu pour générer du trafic, des leads et du business.

**Version vision**

> schoolsWP est un média et une communauté qui aide les indépendants à reprendre le contrôle de leur présence digitale grâce à WordPress. Notre objectif : transformer les sites WordPress en systèmes autonomes capables de générer trafic, autorité et business sur le long terme.

**Structure du pitch** : Qui tu es → À qui tu aides → Le problème → La différence → Le résultat

---

### Talk WordCamp 20 min — Structure complète

**Titre** : _WordPress n'est pas qu'un CMS : comment transformer un site en moteur de croissance_

**Plan** :

```
2 min  → Hook
5 min  → Le problème
7 min  → La solution
4 min  → La méthode
2 min  → Conclusion
```

#### Slide 1 — Hook

> _La plupart des sites WordPress ne génèrent aucun business._

Script : "Quand on crée un site WordPress, on pense souvent à un blog ou à une vitrine. Pourtant, la majorité des sites ne génèrent ni trafic durable, ni leads, ni clients. Et pourtant… WordPress peut faire beaucoup plus."

#### Slide 2 — La croyance

> WordPress est vu comme : un CMS / un blog / un site vitrine

#### Slide 3 — La réalité

> _Le problème n'est pas WordPress. Le problème est la manière dont on construit les sites._

#### Slide 4 — Les 5 erreurs classiques

> Pourquoi les sites WordPress échouent : pas de stratégie SEO / contenu au hasard / aucune automatisation / aucune capture de leads / aucune structure

#### Slide 5 — Le potentiel

> WordPress peut connecter : SEO / contenu / email / CRM / formation / automatisation

#### Slide 6 — Le modèle

> WordPress comme système : moteur SEO + système d'acquisition + plateforme d'automatisation

#### Slide 7 — La méthode schoolsWP

> 4 piliers : Architecture SEO / Contenu stratégique / Automatisation / Autorité

#### Slide 8 — Le résultat

> Le site ne devient plus une vitrine, mais un moteur.

#### Slide 9 — La vision

> WordPress permet de : posséder son audience / automatiser son acquisition / construire une autorité

#### Slide 10 — Conclusion (slide mémorable)

> WordPress peut être un site. Ou un système.

---

### Punchlines tweetables

```
"Si vous construisez un site WordPress comme une vitrine, vous obtenez une vitrine.
 Si vous le construisez comme un système, vous obtenez un moteur."

"WordPress n'est pas un site. C'est un système qui peut travailler pour vous."

"Le problème de WordPress n'est presque jamais WordPress.
 C'est la façon dont on construit les sites."

"WordPress is not the website. WordPress is the system."
```

---

### Slides visuelles signature

#### WordPress Growth Engine

```
          TRAFIC
            ↑
        SEO / CONTENT
            │
LEADS ← WORDPRESS → AUTOMATION
            │
        AUTHORITY
            ↓
          BUSINESS
```

#### WordPress System Map

```
               TRAFFIC
                  ↑
              SEO / CONTENT
                  │
SOCIAL → AUTHORITY → WORDPRESS ← COMMUNITY
                  │
          CRM / EMAIL / AUTOMATION
                  │
               PRODUCTS
                  ↓
               BUSINESS
```

**Script (40 sec)** : "Le SEO et le contenu attirent le trafic. Les réseaux sociaux renforcent l'autorité. Le CRM transforme les visiteurs en leads. Les produits transforment ces leads en business. Quand tout est connecté, le site devient le cœur d'un système de croissance."

**Astuce conférence** : Arrête de parler 2 secondes sur cette slide. Les gens prennent une photo.

---

### Niveau 1 — Blog amateur

Le site existe. Mais il ne travaille pas.

**Caractéristiques** :

- Articles publiés au hasard
- Pas de stratégie SEO, pas de structure, pas de capture, pas d'automatisation
- Chaque article est isolé, aucun maillage

**Architecture typique** :

```
Accueil → Article / Article / Article / Article
```

**Message clé** : Le problème n'est pas le volume de contenu. C'est l'absence d'architecture.

**Pour passer au niveau 2** : ajouter une structure SEO.

---

## POSITIONNEMENT OFFICIEL — schoolsWP vs les autres médias WordPress

### La différence fondamentale

| Les autres médias WordPress | schoolsWP                                             |
| --------------------------- | ----------------------------------------------------- |
| Comment utiliser WordPress  | Comment transformer WordPress en levier de croissance |
| CMS, tutoriels, plugins     | Architecture, systèmes, autorité digitale             |
| Aider à utiliser WP         | Aider à construire un système rentable avec WP        |

**Approche concurrents** : news / tutoriels / astuces / plugins / comparatifs
**Approche schoolsWP** : architecture SEO / automatisation / systèmes / autorité digitale

### La métaphore signature

> Les autres médias WordPress expliquent **comment conduire une voiture**.
> schoolsWP explique **comment construire un moteur qui roule tout seul**.

### Ce que fait schoolsWP

schoolsWP ne parle pas seulement de WordPress. schoolsWP parle de :

- Stratégie
- Architecture
- Systèmes
- Automatisation
- Autorité digitale

WordPress est le socle. Le sujet est le **business digital**.

### Positionnement en une phrase

> schoolsWP est un guide pour construire un système digital autonome avec WordPress.

Utilisable pour : page About / pitch conférence / présentation partenaire / LinkedIn / presse.

---

## TAGLINES OFFICIELLES — schoolsWP

### Classement stratégique

**1 — Tagline principale (la plus puissante)**

> _Transformer WordPress en levier de croissance._

Ultra simple, ultra mémorisable. Idéale pour : header site / bio LinkedIn / signature email / bannière.

**2 — Tagline pédagogique**

> _WordPress pour construire des systèmes qui travaillent pour vous._

Claire, différenciante, business-oriented. Positionne WordPress comme un système, pas un site.

**3 — Tagline marque long terme**

> _Construire des actifs digitaux avec WordPress._

Alignée avec le manifeste. Parle long terme, indépendance, business.

**Baseline longue (variante bonus)**

> _Apprendre WordPress. Construire des systèmes. Créer des actifs._

### Intégration site recommandée

```
schoolsWP

Transformer WordPress en levier de croissance.

Apprendre WordPress.
Construire des systèmes.
Créer des actifs.
```

---

## CATEGORY SENTENCE — schoolsWP

Une Category Sentence positionne schoolsWP comme une nouvelle catégorie mentale dans l'écosystème WordPress.

### Version principale (recommandée)

> _schoolsWP est le média qui aide les créateurs et entrepreneurs à transformer WordPress en véritable système de croissance._

Coche tout : claire, positionnement unique, mémorisable, scalable.

### Version "catégorie" (positionnement niche)

> _schoolsWP est le premier média francophone dédié au WordPress business et aux systèmes de croissance construits avec WordPress._

Positionne une niche + une autorité + une catégorie.

### Version courte (bio, conférences, réseaux)

> _schoolsWP aide les entrepreneurs à transformer WordPress en système de croissance._

### Version "category design" (la plus forte)

> _schoolsWP est un média dédié au WordPress business : comment transformer un site WordPress en moteur d'acquisition, d'automatisation et de revenus._

Ouvre clairement la catégorie : **WordPress Business**

### Intégration branding complète

```
schoolsWP

Transformer WordPress en levier de croissance.

schoolsWP aide les créateurs et entrepreneurs à transformer WordPress
en véritable système de croissance.

Apprendre WordPress.
Construire des systèmes.
Créer des actifs.
```

### Catégorie créée

> **WordPress Business Systems**

Les médias WordPress parlent de plugins, thèmes, news.
schoolsWP parle de business, systèmes, automatisation, autorité.

---

## WORDPRESS GROWTH ENGINE™ — Framework officiel schoolsWP

Le WordPress Growth Engine™ est le modèle en 5 piliers qui transforme un site WordPress en système de croissance autonome. Chaque pilier construit un actif durable.

### Les 5 piliers

**1. Foundation — La base technique**

Un système WordPress solide commence par une base propre.

- Stack minimale
- Hébergement performant
- Sécurité solide
- Maintenance simple

> Sans fondation solide, rien ne scale.

---

**2. Structure — L'architecture SEO**

Avant de publier, il faut structurer.

- Mapping des intentions
- Cocon sémantique
- Maillage interne
- Pages piliers

> Le SEO devient une architecture, pas une série d'articles.

---

**3. Authority — La production d'actifs**

Chaque contenu doit renforcer l'autorité.

- Contenus pédagogiques
- Guides complets
- Ressources citables
- Contenus evergreen

> On construit des actifs digitaux durables.

---

**4. Automation — Le système invisible**

Un site performant automatise.

- Capture d'email
- Segmentation CRM
- Séquences automatisées
- Nurturing intelligent

> Le site devient un système relationnel.

---

**5. Monetization — La création de valeur**

Le trafic seul ne suffit pas.

- Produits digitaux
- Affiliation
- Formations
- Services

> Un site devient un actif économique.

### Le cycle complet

```
Foundation
    ↓
Structure
    ↓
Authority
    ↓
Automation
    ↓
Monetization
    ↓
(recommence avec plus de données et d'autorité)
```

### Ce que change ce framework

La plupart des sites WordPress font :

> contenu → trafic

Le WordPress Growth Engine crée :

> système → autorité → audience → revenus

### La phrase signature

> _Le WordPress Growth Engine est le modèle schoolsWP pour transformer un site WordPress en système de croissance autonome._

### Résultat final

Avec les 5 piliers en place, le site WordPress devient :

- Un moteur SEO
- Un système d'acquisition
- Une plateforme d'autorité
- Un actif business

---

## AUTHORITY FLYWHEEL™ — schoolsWP

Le moteur d'autorité qui fait grandir un site WordPress en continu.

Un site WordPress ne devient pas une référence grâce à un article viral. Il devient une référence grâce à un système qui renforce son autorité en continu.

### Le principe

Au lieu de produire du contenu isolé, on construit un moteur d'autorité.

Chaque contenu :

- Attire du trafic
- Renforce la crédibilité
- Nourrit l'écosystème
- Améliore les contenus existants

> Résultat : le site devient de plus en plus puissant avec le temps.

### Le cycle en 6 étapes

**1. Expertise**

Répondre aux questions importantes du domaine avec des guides structurés, tutoriels détaillés, explications pédagogiques.

> L'objectif : devenir utile.

---

**2. Contenu**

Transformer l'expertise en ressources : articles, guides, tutoriels — conçus pour répondre à une intention précise, être clairs et actionnables, pouvoir être cités.

---

**3. SEO**

Organiser les contenus en architecture : cocon sémantique, maillage interne, pages piliers.

> Le site devient progressivement une ressource complète sur son sujet.

---

**4. Trafic**

La structure attire naturellement : recherches Google, partages, citations.

> Le site devient visible.

---

**5. Audience**

Une partie du trafic devient une audience capturée via newsletters, ressources, formations, communautés.

> On ne parle plus de visiteurs. On parle d'audience.

---

**6. Autorité**

Le site est cité, les contenus partagés, la crédibilité augmente. Google comprend que le site est une référence.

> L'autorité se renforce.

### La roue continue

```
Expertise
    → Contenu
    → SEO
    → Trafic
    → Audience
    → Autorité
    → (recommence avec plus de données et de crédibilité)
```

Plus d'autorité → plus de visibilité → plus de trafic → plus d'audience → plus de contenu.

### L'erreur classique à éviter

Publier sans stratégie → contenus isolés → trafic fragile → autorité faible.

Sans système, la croissance est limitée.

### Ce que fait la méthode schoolsWP

Transforme un site WordPress en :

- Moteur SEO
- Hub de contenu
- Système d'acquisition
- Plateforme d'autorité

> Un site qui grandit même quand on publie moins.

### La vision

Le but n'est pas seulement d'avoir du trafic.

Le but est de construire un site qui devient une référence — un actif qui prend de la valeur avec le temps.

---

## TDD — schoolsWP Performance Loop

Module activé quand : le CTR a bougé, une modification SEO a été effectuée, on est en boucle d'optimisation post-résultat.

**Logique TDD :**

- Test : un changement a déjà eu lieu
- Develop : on identifie ce qui a été modifié
- Debug : on analyse l'impact réel sur le CTR
- Next iteration : on décide quoi ajuster ensuite

### Prompt TDD — Performance Loop (standard)

```
TDD – schoolsWP Performance Loop

Contexte :
Le CTR a bougé après une modification SEO ou éditoriale. Je veux analyser le résultat
proprement, comprendre ce qui a influencé la variation, puis définir la prochaine
itération la plus pertinente.

Ta mission : Travaille en mode TDD (Test · Develop · Debug).

1) TEST
- Rappelle l'objectif initial
- Identifie le KPI principal : CTR
- Précise la baseline avant changement
- Compare avec la nouvelle valeur observée
- Indique si le test est concluant, neutre ou négatif

2) DEVELOP
- Liste exactement les changements effectués
- Identifie le changement le plus susceptible d'avoir influencé le CTR
- Distingue les changements principaux des changements secondaires
- Évalue l'effort vs impact potentiel

3) DEBUG
- Analyse pourquoi le CTR a monté, stagné ou baissé
- Identifie les causes probables
- Signale les biais possibles : faible volume, saisonnalité, position moyenne,
  variation d'impressions, requêtes différentes
- Dis ce qu'il faut conserver, annuler ou ajuster

4) ITERATION SUIVANTE
- Propose UNE seule prochaine itération prioritaire
- Donne l'hypothèse associée
- Donne le changement exact à tester
- Donne le délai d'observation recommandé
- Donne le seuil de validation

Format de réponse attendu :
1) Verdict du test
2) Analyse des changements
3) Debug stratégique
4) Prochaine itération recommandée
5) Action concrète à exécuter maintenant

Style : Réponse en français. Ton schoolsWP : direct, concret, utile. Pas de blabla.
Priorise le ROI et la simplicité d'exécution.
```

**Version ultra courte :**

> Analyse ce mouvement de CTR en mode TDD : baseline, changement, debug, prochaine itération.

**Quand utiliser TDD :**

- Changé un title / meta description / H1 / snippet / angle éditorial
- Observé une variation après update
- En boucle d'optimisation post-publication

---

## TDD — schoolsWP Performance Loop (GSC Edition)

Version spécialisée Google Search Console.

### Prompt TDD — GSC Edition

```
TDD – schoolsWP Performance Loop (Google Search Console)

Contexte :
Je constate une variation du CTR dans Google Search Console après une modification SEO
(title, meta description, structure, angle éditorial ou snippet).
Je veux analyser cette variation de manière rigoureuse et définir la prochaine itération SEO.

Travaille en mode TDD : Test → Develop → Debug.

Données disponibles :
- URL analysée : [URL]
- Période avant modification : [DATES]
- Période après modification : [DATES]

Metrics GSC :
- CTR avant : [CTR]  — CTR après : [CTR]
- Position moyenne avant : [POS]  — Position moyenne après : [POS]
- Impressions avant : [IMP]  — Impressions après : [IMP]

1) TEST
Analyse le résultat du test.
- Compare CTR avant / après
- Vérifie si la position moyenne a changé
- Vérifie si le volume d'impressions a changé
- Identifie si la variation est statistiquement crédible
Verdict : Test concluant / neutre / négatif

2) DEVELOP
Identifie les changements réalisés : title / meta description / H1 / FAQ /
angle éditorial / snippet. Classe par impact potentiel.

3) DEBUG
Analyse les causes possibles de la variation CTR :
- changement d'intention de requête
- variation de position moyenne
- concurrence dans la SERP
- snippet concurrent plus attractif
- mismatch entre title et intention
Signale les biais possibles : faible volume, saisonnalité, changement d'impressions

4) ITERATION SUIVANTE
Propose UNE seule itération prioritaire.
Donne : l'hypothèse / le changement précis / le nouveau title ou snippet proposé /
le délai d'observation / le seuil de validation

FORMAT DE RÉPONSE :
1) Verdict du test
2) Analyse GSC
3) Cause probable
4) Prochaine itération
5) Action immédiate
```

**Règle fondamentale :** toujours isoler la variable — tester 1 seule chose à la fois (title OU description, jamais les deux).

---

## CTR DOMINATION FRAMEWORK — schoolsWP

Pipeline : Détection → Priorisation → Optimisation → Test → Itération

### 1. Détection — pages à potentiel

Dans GSC → Performance → Pages, exporter : URL / Impressions / CTR / Position / Clicks — période 90 jours.

**Critère Quick Win :**

- Position : 3 → 12
- Impressions : > 500
- CTR : < 3 %

### 2. Score d'opportunité

```
Score = Impressions × (CTR cible − CTR actuel)
```

| Position | CTR cible |
| -------- | --------- |
| 3        | 15 %      |
| 4        | 12 %      |
| 5        | 10 %      |
| 6        | 8 %       |
| 7        | 6 %       |
| 8–10     | 5 %       |

Exemple : 5000 impressions × (8 % − 2 %) = **300 clics/mois** sans nouveau contenu.

### 3. Diagnostic SERP

Pour chaque page prioritaire : title actuel / meta description / 5 premiers résultats.
Analyser : angle dominant / promesse / mots déclencheurs / longueur du title / chiffres.

### 4. Déclencheurs CTR — schoolsWP

| Catégorie   | Mots                               |
| ----------- | ---------------------------------- |
| Performance | rapide, performant, optimisé       |
| Gain        | guide, méthode, checklist          |
| Curiosité   | erreurs, pièges, secrets           |
| Concret     | étape par étape, complet, débutant |

### 5. Boucle TDD

- Changer 1 variable (title ou description)
- Observer 14 à 21 jours
- Comparer CTR / impressions / position
- Décider : conserver / itérer / revenir

### Routine hebdomadaire (30 min)

1. Ouvrir GSC
2. Repérer 1 page sous-optimisée
3. Optimiser le title
4. Lancer test
5. Noter résultat

> Impact réel possible : +3 % CTR sur 80 000 impressions = +2400 clics sans écrire un seul article.

---

## CTR HUNTER — Système interne schoolsWP

Pipeline complet : Extraction GSC → Détection → Scoring → Priorisation → Génération de titles → Test TDD

### Étapes

**1. Extraction GSC** — colonnes : URL / Impressions / CTR / Position / Clicks — 90 jours

**2. Filtres Quick Win** — Position 3→12, Impressions >500, CTR <3 %

**3. Score** — `Impressions × (CTR cible − CTR actuel)`

**4. Analyse SERP** — title / meta / concurrents — identifier angle et promesse

**5. Génération variantes titles (exemple)**

Page : `maintenance wordpress` — Title actuel : `Maintenance WordPress : guide complet`

Variantes :

- Maintenance WordPress : guide complet (+ checklist)
- Maintenance WordPress : la checklist indispensable
- Maintenance WordPress : 7 erreurs à éviter
- Maintenance WordPress : méthode simple pour sécuriser ton site
- Maintenance WordPress : le guide pratique pour débuter

**6. Test TDD** — 1 variable / 14-21 jours d'observation

**7. Décision** — CTR monte : conserver | stable : nouvel angle | baisse : revenir

### Template Google Sheets CTR Hunter

4 onglets :

- **Dashboard** — vue synthèse des opportunités
- **CTR_Hunter** — scoring et suivi des tests (colonnes : URL / Impressions / CTR actuel / Position / Score / Title testé / CTR après / Statut)
- **Title_Ideas** — génération rapide de variantes de titles
- **Import_GSC** — mode d'emploi import depuis GSC / Settings seuils

---

## PROMPT — Générateur de 20 Titles SEO (CTR Optimisation)

```
Tu es un expert SEO spécialisé dans l'optimisation du CTR dans Google.

Ta mission est de générer 20 titles SEO optimisés pour maximiser le taux de clic dans les SERP.

CONTEXTE

Mot-clé principal : [KEYWORD]
URL de la page : [URL]
Intentions de recherche : [INTENTION]
Title actuel : [TITLE ACTUEL]
Position moyenne Google : [POSITION]
CTR actuel : [CTR]
Audience : freelances, créateurs et entrepreneurs WordPress.
Objectif : Augmenter le CTR tout en restant pertinent et crédible.

RÈGLES

Les titles doivent :
• rester naturels et crédibles
• inclure le mot-clé principal
• faire entre 50 et 60 caractères environ
• maximiser la curiosité ou la promesse
• varier les angles (guide, erreurs, méthode, checklist, etc.)

Leviers à utiliser : bénéfice clair / curiosité / chiffres / erreurs à éviter /
méthode ou guide / gain de temps / angle débutant ou pratique

Ne jamais produire de clickbait trompeur.

FORMAT DE SORTIE

Génère exactement 20 titles SEO numérotés.
Chaque title doit être différent.
Ne donne aucune explication. Seulement la liste.

Commence maintenant.
```

**Conseil d'usage :** tester 1 seul title à la fois / observer 14-21 jours / puis TDD → Debug → Iteration.

---

## PROMPT — SERP Reverse Engineering + 20 Titles SEO CTR

Version plus puissante : l'IA analyse la SERP en premier, puis génère des variantes différenciantes.

```
Tu es un expert SEO spécialisé dans l'optimisation du CTR organique dans Google.

Ta mission est d'analyser la SERP cible, d'identifier les patterns de titles les plus
performants, puis de générer 20 titles SEO optimisés pour maximiser le taux de clic.

## CONTEXTE

Mot-clé principal : [KEYWORD]
URL de la page à optimiser : [URL]
Title actuel : [TITLE ACTUEL]
Meta description actuelle : [META ACTUELLE]
Position moyenne Google : [POSITION]
CTR actuel : [CTR]
Audience cible : freelances, créateurs, formateurs, entrepreneurs WordPress
Objectif : Augmenter le CTR sans clickbait, en restant cohérent avec l'intention de recherche.

## ÉTAPE 1 — ANALYSE DE LA SERP

Analyse les 10 premiers résultats Google sur le mot-clé principal.

Pour chaque résultat, identifie :
- l'angle dominant
- la promesse principale
- les mots déclencheurs utilisés
- présence de chiffres, d'année, bénéfice clair
- format : guide / méthode / checklist / erreurs / comparatif
- longueur approximative du title
- ce qui semble faible ou répétitif

Puis résume :
1. Les patterns dominants dans la SERP
2. Les opportunités de différenciation
3. Les angles sous-exploités
4. Les erreurs à éviter

## ÉTAPE 2 — DIAGNOSTIC DU TITLE ACTUEL

Analyse le title actuel : points forts, faiblesses, niveau d'attractivité face à la SERP,
pourquoi il peut sous-performer en CTR.

## ÉTAPE 3 — GÉNÉRATION DE 20 TITLES

Génère exactement 20 titles SEO optimisés — contraintes : mot-clé inclus, crédible,
50-60 car., angles variés. Répartis en 5 familles de 4 variantes :

### Famille A — Clarté / Guide
### Famille B — Checklist / Action
### Famille C — Erreurs / Pièges
### Famille D — Bénéfice / Résultat
### Famille E — Différenciation SERP

## ÉTAPE 4 — SÉLECTION PRIORITAIRE

Sélectionne les 3 meilleurs titles pour un test CTR. Pour chacun : 1 phrase d'explication.
Identifie aussi : le title le plus safe / le plus agressif / le plus différenciant.

FORMAT DE SORTIE :
### 1) Analyse SERP
### 2) Diagnostic du title actuel
### 3) 20 titles classés par familles
### 4) Top 3 à tester en priorité
```

---

## PROMPT ULTIME — CTR SEO + Meta + TDD

Version complète : 20 titles + 10 metas + sélection prioritaire + plan TDD intégré.

```
Tu es un expert SEO spécialisé dans l'optimisation du CTR organique, l'analyse SERP,
le copywriting SEO et les boucles d'itération basées sur Google Search Console.

Ta mission : optimiser le snippet SEO d'une page existante pour augmenter son CTR.
Travaille comme un consultant SEO senior orienté performance.

## CONTEXTE

Mot-clé principal : [KEYWORD]
Mots-clés secondaires : [KEYWORDS_SECONDAIRES]
URL de la page : [URL]
Title actuel : [TITLE ACTUEL]
Meta description actuelle : [META ACTUELLE]
H1 actuel : [H1 ACTUEL]
Position moyenne Google : [POSITION]
CTR actuel : [CTR]
Impressions : [IMPRESSIONS]
Audience cible : freelances, créateurs, formateurs, entrepreneurs WordPress
Intention de recherche : [INTENTION]

Ton attendu : français, style schoolsWP — direct, concret, utile, zéro blabla.

## ÉTAPE 1 — ANALYSE SERP
[Cf. prompt SERP Reverse Engineering — mêmes critères]
Produire : patterns dominants / angles sur-utilisés / angles sous-exploités /
meilleur axe de différenciation.

## ÉTAPE 2 — DIAGNOSTIC DU SNIPPET ACTUEL
Points forts / faibles / ce qui freine le clic / verdict : correct / moyen / faible /
à retravailler en priorité.

## ÉTAPE 3 — 20 TITLES SEO
[Mêmes 5 familles : Guide / Checklist / Erreurs / Bénéfice / Différenciation]

## ÉTAPE 4 — 10 META DESCRIPTIONS
Contraintes : cohérentes avec les meilleurs titles / claires et concrètes /
140-160 caractères / varier : guide, action, bénéfice, réassurance, curiosité utile.

## ÉTAPE 5 — SÉLECTION PRIORITAIRE
- 3 meilleurs titles à tester
- 2 meilleures metas à tester
- Combo le plus "safe"
- Combo le plus différenciant
- Combo le plus agressif mais crédible
Pour chaque sélection : 1 phrase d'explication.

## ÉTAPE 6 — PLAN TDD

### TEST
- Baseline (CTR, position, impressions)
- KPI principal + seuil de validation

### DEVELOP
- Changement exact à faire
- Variable qui doit rester stable
- Title ou meta en premier ?

### DEBUG
- Causes possibles si le test échoue
- Biais à surveiller : position, impressions, saisonnalité, volume, requêtes

### ITERATION
Prochaine itération si CTR monte / stagne / baisse.

## FORMAT DE SORTIE OBLIGATOIRE
### 1) Analyse SERP
### 2) Diagnostic du snippet actuel
### 3) 20 titles classés par familles
### 4) 10 meta descriptions
### 5) Top sélections à tester
### 6) Plan TDD complet
### 7) Recommandation finale : quoi tester en premier
```

**Version courte :**

> Optimise le CTR SEO de cette page avec une logique GSC + SERP + TDD.
> Keyword : ... | URL : ... | Title actuel : ... | Meta actuelle : ... | Position : ... | CTR : ... | Impressions : ...

---

## TEMPLATE GOOGLE SHEETS — CTR TDD Tracker schoolsWP

4 onglets : README / GSC_Pages / Tests_CTR / Title_Variants

### Onglet Tests_CTR

| Colonne             | Description                              |
| ------------------- | ---------------------------------------- |
| Date test           | Date de départ du test                   |
| URL                 | Page testée                              |
| Keyword principal   | Mot-clé ciblé                            |
| Position (avant)    | Position moyenne GSC avant changement    |
| CTR (avant)         | CTR GSC avant changement                 |
| Impressions (avant) | Impressions GSC avant changement         |
| Title initial       | Title avant test                         |
| Meta initiale       | Meta avant test                          |
| Variable testée     | Title ou Meta (jamais les deux)          |
| Nouvelle version    | Contenu testé                            |
| Position (après)    | Position après 14-21 jours               |
| CTR (après)         | CTR après 14-21 jours                    |
| Impressions (après) | Impressions après 14-21 jours            |
| Verdict             | Concluant / Neutre / Négatif             |
| Prochaine action    | Conserver / Tester autre angle / Revenir |

### Onglet GSC_Pages (Quick Wins)

| URL | Keyword | Position | Impressions | CTR | CTR cible | Score opportunité | Priorité |

**Formule Score :**

```
=E2*(F2-D2)
```

_(colonnes : E = Impressions, F = CTR cible, D = CTR actuel — valeurs en %)_

### Onglet Title_Variants

| URL | Keyword | Title A | Title B | Title C | Title D | Title E | Title testé |

### Règles fondamentales

- Variable testée : Title ou Meta — **jamais les deux**
- Observation : **14 à 21 jours minimum**
- Toujours comparer les 3 métriques ensemble : CTR + Position + Impressions

### Interprétation rapide

| Situation                | Action                     |
| ------------------------ | -------------------------- |
| CTR ↑ et position stable | Conserver le title         |
| CTR ↑ et position ↑      | Très bon signal            |
| CTR stable               | Tester autre angle         |
| CTR ↓                    | Revenir au title précédent |

---

## FRAMEWORKS DE PROMPT ENGINEERING — schoolsWP

### RACE — Role · Action · Context · Expectation

Framework de base pour structurer une instruction IA.

| Composante      | Rôle                                          |
| --------------- | --------------------------------------------- |
| **Role**        | Définir qui doit être l'IA (expertise, ton)   |
| **Action**      | Préciser ce que l'IA doit faire (verbe clair) |
| **Context**     | Donner les infos nécessaires                  |
| **Expectation** | Définir le format et le résultat attendu      |

**Quand utiliser RACE :** exécution rapide, tâches simples, agents, API, automation.

### RACE — Version officielle schoolsWP

```
[R] ROLE
Tu es un expert WordPress senior spécialisé en SEO (Google + Bing), performance,
sécurité, automatisation (FluentCRM / Fluent Forms / TutorLMS / FluentBooking) et
conversion. Tu réponds en français, style schoolsWP : direct, concret, phrases courtes.
Zéro blabla. Tu proposes des actions applicables immédiatement.

[A] ACTION
Ta mission : produire une recommandation opérationnelle et priorisée sur : [SUJET].
Tu dois :
1) Diagnostiquer rapidement la situation à partir des éléments fournis.
2) Proposer des actions concrètes (checklist) avec un ordre de priorité.
3) Donner une version "quick wins (30 min)" + une version "propre (2–3 h)".
4) Fournir si utile : snippets (Rank Math, WP, .htaccess, SQL, CSS), réglages plugin,
   ou structure de page.

[C] CONTEXT
- Site : schoolsWP.com
- Audience : freelances / créateurs / entrepreneurs WordPress, niveau technique variable
- Objectif business : trafic qualifié + citabilité IA + conversion
- Contrainte : pas de jargon marketing, pas de théorie inutile
- Données disponibles (selon le cas) :
  • URL / page : [URL]
  • Intention cible : [INTENTION]
  • Mot-clé principal : [KW_MAIN]
  • Mots-clés secondaires : [KW_SECONDARY]
  • Outils : Rank Math Pro, GSC, GA4, (optionnel) DataForSEO, Fluent Suite
  • Extraits / captures / contenu : [INPUT]

[E] EXPECTATION (FORMAT DE SORTIE)
Tu réponds avec ce format EXACT :

1) Résumé en 5 lignes (ce qui bloque / ce qui manque)
2) Priorités (P1 / P2 / P3) + effort estimé (S/M/L)
3) Quick wins (30 min) : checklist
4) Version propre (2–3 h) : checklist détaillée
5) Si SEO contenu : structure H2/H3 + FAQ (5 questions)
6) Si SEO images : bloc métadonnées (XPTitle / XPSubject / XPKeywords)
7) Mesure : comment valider dans GSC (quoi regarder + délai)
8) Next step : 3 questions maximum si info manquante (sinon propose la suite)

Si c'est OK, exécute directement sans demander d'autorisation.
```

**Nom officiel :** schoolsWP Strategic Engine (RACE edition)

---

### CREDO — Context · Role · Example · Deliverable · Outcome

Framework plus stratégique que RACE, orienté qualité du livrable final.

| Composante      | Rôle                                           |
| --------------- | ---------------------------------------------- |
| **Context**     | Situation précise, pourquoi, environnement     |
| **Role**        | Expertise attendue (profondeur)                |
| **Example**     | Style/format attendu — l'IA imite les patterns |
| **Deliverable** | Ce qui doit être produit exactement            |
| **Outcome**     | Résultat business attendu                      |

| Framework | Idéal pour                     |
| --------- | ------------------------------ |
| RACE      | Exécution rapide               |
| CREDO     | Production stratégique premium |

**Quand utiliser CREDO :** article pilier, landing, lead magnet, séquence email, module formation.

### CREDO — Version officielle schoolsWP

```
[C] CONTEXT
Tu interviens pour schoolsWP.com, média et écosystème dédié à WordPress (SEO,
automatisation, performance, monétisation, maintenance).
Audience : freelances, créateurs, formateurs, entrepreneurs WordPress.
Objectif : produire un contenu/action à forte valeur stratégique, exploitable
immédiatement, optimisé SEO + IA (Google SGE, ChatGPT, Perplexity).
Contrainte : ton direct, clair, concret. Zéro blabla. Pas de jargon marketing inutile.

[R] ROLE
Tu es un expert WordPress senior + consultant SEO stratégique + architecte automation.
Tu raisonnes en priorité business : trafic qualifié, autorité, conversion, scalabilité.
Tu proposes uniquement des recommandations actionnables.

[E] EXAMPLE (STYLE ATTENDU)
Structure claire. Titres hiérarchisés (H2/H3 si contenu). Checklist priorisée.
Blocs prêts à intégrer (FAQ, snippets, tableaux si nécessaire).
Toujours orienté mise en œuvre immédiate.

[D] DELIVERABLE
Tu dois produire :
1) Un résumé stratégique en 5 lignes maximum
2) Une analyse structurée
3) Une checklist d'actions priorisées (P1 / P2 / P3)
4) Une version "quick wins" (30 min)
5) Une version "optimisation complète"
6) Si SEO contenu : plan H2/H3 + FAQ optimisée IA
7) Si technique : réglages précis (plugin / snippet / paramétrage)
8) Comment mesurer le résultat dans Google Search Console

[O] OUTCOME
Le résultat doit :
- Augmenter la clarté stratégique
- Améliorer la performance SEO
- Renforcer la citabilité IA
- Favoriser la conversion
- Être directement exploitable sans retravail

Si des informations manquent, pose maximum 3 questions stratégiques.
Sinon, exécute immédiatement.
```

**Nom officiel :** schoolsWP Strategic Engine

---

### SPECS — Scope · Purpose · Environment · Constraint · Success criteria

Framework orienté produit / ingénierie / architecture. Le plus "cadrage" de tous.

| Composante           | Rôle                                         |
| -------------------- | -------------------------------------------- |
| **Scope**            | Périmètre exact (inclus / exclu)             |
| **Purpose**          | Pourquoi, quel problème, quel objectif       |
| **Environment**      | Stack, outils, audience, niveau              |
| **Constraint**       | Limites (temps, budget, ton, complexité)     |
| **Success criteria** | Définition concrète de réussite (KPI, délai) |

**Quand utiliser SPECS :** conception offre, architecture SEO, formation, automation, produit digital.

### SPECS — Version officielle schoolsWP v2

```
[S] SCOPE
- Périmètre inclus :
- Périmètre exclu :
- Niveau de profondeur attendu :
- Livrables concernés :

[P] PURPOSE
- Problème à résoudre :
- Résultat business recherché :
- Impact principal (trafic / autorité / leads / conversion / rétention) :
- KPI cible :

[E] ENVIRONMENT
- Site : schoolsWP.com
- Audience : freelances / créateurs / entrepreneurs WordPress
- Stack : (Rank Math, Fluent Suite, etc.)
- Sources de données : (GSC, GA4, DataForSEO…)
- Ressources disponibles :
- Contraintes techniques existantes :

[C] CONSTRAINT
- Temps disponible :
- Complexité acceptable :
- Budget si applicable :
- Ton : direct, actionnable, sans jargon inutile
- Interdictions : théorie vague, fluff, généralités

[S] SUCCESS CRITERIA
Définis comment on sait que c'est réussi :
- Indicateurs mesurables :
- Délai d'évaluation :
- Seuil de validation :
- Signal d'échec :
- Prochaine itération prévue :

FORMAT DE RÉPONSE ATTENDU :
1) Résumé exécutif
2) Diagnostic
3) Plan d'action priorisé
4) Version rapide
5) Version complète
6) Méthode de mesure selon les Success criteria
7) Étape suivante logique
```

**Nom officiel :** schoolsWP Architecture Blueprint

---

### PACT — Problem · Approach · Constraint · Test

Framework lean orienté résolution de problème + validation expérimentale.

| Composante     | Rôle                                           |
| -------------- | ---------------------------------------------- |
| **Problem**    | Le vrai problème structurel (pas le symptôme)  |
| **Approach**   | Stratégie, angle, logique d'exécution          |
| **Constraint** | Limites à respecter (temps, stack, ressources) |
| **Test**       | Comment valider — KPI, seuil, signal d'échec   |

**Quand utiliser PACT :** tester un angle SEO, valider une landing, optimiser un email, lancer une mini-offre.

### PACT — Version officielle schoolsWP (Growth Loop)

```
[P] PROBLEM
Définis le problème réel (pas le symptôme).
- Symptôme observé :
- Problème structurel supposé :
- Impact business actuel :
- Page / tunnel / cluster concerné :
- Données disponibles (GSC, GA4, taux conversion, CTR…) :

[A] APPROACH
Décris la stratégie d'intervention.
- Hypothèse principale :
- Angle stratégique choisi :
- Action prioritaire à tester :
- Levier principal (SEO contenu / technique / UX / offre / automation / CTA) :
- Étapes concrètes d'exécution :

[C] CONSTRAINT
Cadre les limites opérationnelles.
- Temps disponible :
- Complexité acceptable :
- Stack WordPress utilisée (Rank Math, Fluent Suite, etc.) :
- Ressources disponibles :
- Interdictions : jargon inutile, refonte complète si non nécessaire, théorie vague

[T] TEST
Définis comment on valide l'expérimentation.
- KPI principal à mesurer :
- KPI secondaire :
- Seuil de réussite :
- Délai d'observation :
- Signal d'échec :
- Plan si échec :

FORMAT DE RÉPONSE ATTENDU :
1) Résumé du problème réel
2) Hypothèse stratégique
3) Plan d'action concret
4) Implémentation rapide (≤ 30 min si possible)
5) Méthode de test précise
6) Prochaine itération logique
```

**Nom officiel :** schoolsWP Growth Loop

---

### DITO — Define · Input · Transformation · Output

Framework pipeline / transformation de contenu / automatisation.

| Composante         | Rôle                                                 |
| ------------------ | ---------------------------------------------------- |
| **Define**         | Objectif exact, type de transformation, format final |
| **Input**          | Matière brute (article, transcript, CSV, notes)      |
| **Transformation** | Ce que l'IA doit faire avec l'input                  |
| **Output**         | Format exact, longueur, ton, contraintes             |

**Quand utiliser DITO :** repurposing omnicanal, FAQ IA, métadonnées SEO, multi-agents, pipeline.

### DITO — Version officielle schoolsWP (Omnichannel Engine)

```
[D] DEFINE
Définis précisément l'objectif de transformation.
- Objectif principal :
- Canal cible : (Article / LinkedIn / Newsletter / Email / YouTube / Lead magnet…)
- Intention SEO cible :
- Niveau de profondeur : (court / stratégique / expert)
- Résultat business attendu : (trafic / leads / autorité / conversion)

[I] INPUT
Fournis la matière brute à transformer.
- Type d'input : (article / transcript / notes / données SEO / capture / CSV…)
- Contenu brut :
- Mots-clés principaux :
- Angle stratégique existant :
- Contraintes spécifiques :

[T] TRANSFORMATION
Décris ce que l'IA doit faire.
- Type de transformation : (résumer / structurer / optimiser SEO / reformuler /
  convertir en carrousel / extraire FAQ / créer métadonnées…)
- Niveau d'optimisation IA : (citabilité / featured snippet / SGE / structuration FAQ)
- Structure attendue :
- Éléments à inclure : (CTA / FAQ / hook / storytelling / tableau…)
- Éléments à exclure :

[O] OUTPUT
Spécifie le format final exact.
- Format : (Markdown / prêt à publier / prêt à coller dans WordPress / script vidéo…)
- Longueur cible :
- Ton : direct, clair, actionnable (style schoolsWP)
- Structure obligatoire :
- Blocs spécifiques : (H2/H3, FAQ, métadonnées, CTA…)

FORMAT DE RÉPONSE ATTENDU :
1) Résultat final directement exploitable
2) Optimisation SEO intégrée naturellement
3) Structure hiérarchisée claire
4) CTA cohérent avec l'objectif
```

**Nom officiel :** schoolsWP Omnichannel Engine

---

### COT — Chain Of Thought (mode structuré schoolsWP)

Technique de raisonnement interne — forcer l'IA à analyser étape par étape avant de répondre.

**Attention :** l'objectif n'est pas "montre ton raisonnement" mais "structure ton analyse en étapes claires".

**Quand utiliser COT :** arbitrage stratégique, choix d'outil, décision produit, architecture SEO.

### COT — Version officielle schoolsWP (Decision Engine)

```
COT – schoolsWP Structured Reasoning Mode

Objectif : produire une analyse stratégique structurée, logique et progressive,
sans exposer de raisonnement interne inutile.

INSTRUCTION

Avant de répondre :
1) Clarifie le problème exact
2) Identifie les variables clés
3) Analyse les options possibles
4) Évalue les impacts SEO / business / technique
5) Priorise selon ROI et faisabilité
6) Produis une réponse structurée et actionnable

FORMAT DE RÉPONSE ATTENDU :
1) Diagnostic clair
2) Facteurs clés identifiés
3) Options stratégiques comparées
4) Recommandation priorisée
5) Justification synthétique
6) Plan d'exécution concret
```

**Nom officiel :** schoolsWP Decision Engine

---

## schoolsWP INTELLIGENCE SUITE™ — Architecture complète

### Tableau comparatif des frameworks

| Framework | Nom officiel           | Utilité principale              |
| --------- | ---------------------- | ------------------------------- |
| SPECS     | Architecture Blueprint | Cadrage stratégique / produit   |
| COT       | Decision Engine        | Arbitrage / décision structurée |
| CREDO     | Strategic Engine       | Production premium              |
| DITO      | Omnichannel Engine     | Transformation / repurposing    |
| PACT      | Growth Loop            | Hypothèse / expérimentation     |
| TDD       | Performance Loop       | Optimisation continue / data    |

### Architecture hiérarchique

**NIVEAU 1 — THINKING LAYER (penser)**

1. **Architecture Blueprint (SPECS)** — point de départ obligatoire
   - Créer une offre, structurer une formation, concevoir une page pilier, définir architecture SEO
   - Règle : jamais de production sans Blueprint

2. **Decision Engine (COT)** — quand tu hésites
   - Choisir entre 2 plugins, prioriser un chantier, arbitrer un angle éditorial
   - Règle : pas d'intuition floue — décision structurée

**NIVEAU 2 — BUILD LAYER (créer)**

3. **Strategic Engine (CREDO)** — production principale
   - Article pilier, landing, lead magnet, séquence email, module formation
   - Règle : toujours produire avec objectif + KPI

4. **Omnichannel Engine (DITO)** — scaling contenu
   - Article → LinkedIn / Newsletter / Email / Cluster / Vidéo → SEO
   - Règle : jamais 1 contenu = 1 canal

**NIVEAU 3 — GROWTH LAYER (améliorer)**

5. **Growth Loop (PACT)** — hypothèse & test
   - Nouveau title, CTA, angle, hook — 1 test à la fois

6. **Performance Loop (TDD)** — optimisation continue
   - CTR, conversion, open rate, position SEO

### Workflow complet (exemple page pilier)

```
Architecture Blueprint → définir structure
        ↓
Strategic Engine → produire
        ↓
Omnichannel Engine → décliner
        ↓
Growth Loop → tester angle / title
        ↓
Performance Loop → optimiser CTR
        ↓
SCALE ou ITERATE
```

### Règles fondamentales de l'OS

- Rien sans cadre
- Rien sans KPI
- Rien sans test
- Rien sans optimisation
- Chaque contenu doit scaler

### Diagramme opérationnel

```
┌──────────────────────────┐
│   1. ARCHITECTURE        │
│   Blueprint (SPECS)      │
└─────────────┬────────────┘
              ↓
┌──────────────────────────┐
│   2. DECISION            │
│   Engine (COT)           │
└─────────────┬────────────┘
              ↓
┌──────────────────────────┐
│   3. PRODUCTION          │
│   Strategic Engine       │
│   (CREDO)                │
└─────────────┬────────────┘
              ↓
┌──────────────────────────┐
│   4. TRANSFORMATION      │
│   Omnichannel Engine     │
│   (DITO)                 │
└─────────────┬────────────┘
              ↓
┌──────────────────────────┐
│   5. EXPERIMENTATION     │
│   Growth Loop (PACT)     │
└─────────────┬────────────┘
              ↓
┌──────────────────────────┐
│   6. OPTIMISATION        │
│   Performance Loop (TDD) │
└─────────────┬────────────┘
              ↓
       ┌─────────────┐
       │   SCALE     │
       │   ou        │
       │   ITERATE   │
       └─────────────┘
```

Version ultra synthétique :

> Architecture → Create → Repurpose → Test → Optimize → Scale

---

## schoolsWP AUTHORITY SYSTEM™ — Méthode signature

Transformer la suite de frameworks en méthode stratégique enseignable, vendable et différenciante.

**Sous-titre :** Concevoir, produire et optimiser un écosystème WordPress orienté trafic, IA et conversion.

### Architecture en 6 phases

**Phase 1 — Foundation : Architecture Blueprint (SPECS)**

- Cadrer le système : positionnement, structure SEO, offre cohérente, tunnel logique
- Livrable : plan d'architecture stratégique complet

**Phase 2 — Clarity : Decision Engine (COT)**

- Prioriser, éviter la dispersion, maximiser le ROI
- Livrable : plan d'action priorisé

**Phase 3 — Authority : Strategic Engine (CREDO)**

- Produire du contenu premium citable IA, page pilier massive, autorité thématique
- Livrable : contenu structuré prêt à ranker

**Phase 4 — Scale : Omnichannel Engine (DITO)**

- Article → LinkedIn → Newsletter → Email — réutilisation intelligente, amplification
- Livrable : kit omnicanal complet

**Phase 5 — Optimize : Growth Loop (PACT)**

- Tester intelligemment : CTR, conversion, angles — 1 test à la fois
- Livrable : plan d'expérimentation clair

**Phase 6 — Dominate : Performance Loop (TDD)**

- Optimisation continue, itération structurée, scalabilité
- Livrable : système d'optimisation durable

### Positionnement

Ce n'est pas "une méthode IA". C'est un système stratégique WordPress orienté performance, SEO IA et autorité.

**Promesse centrale :** En appliquant la méthode, tu ne publies plus au hasard, tu ne testes plus à l'aveugle, tu construis un écosystème cohérent.

**Slogan :** `schoolsWP Authority System™ — Structure. Autorité. Performance.`

---

## AI STRATEGIC BRAIN schoolsWP™ — Prompt système global

Méta-système orchestrateur qui cadre, décide, produit, transforme, teste et optimise automatiquement.

### 6 modes d'activation

| Mode        | Framework     | Déclenché quand                                  |
| ----------- | ------------- | ------------------------------------------------ |
| ARCHITECT   | SPECS         | Nouveau projet, page pilier, offre, formation    |
| STRATEGIST  | COT structuré | Arbitrage, priorisation, choix SEO/outil/angle   |
| PRODUCER    | CREDO         | Rédaction page pilier, landing, séquence email   |
| TRANSFORMER | DITO          | Article → LinkedIn, vidéo → article, repurposing |
| EXPERIMENT  | PACT          | CTR faible, conversion faible, nouveau test      |
| OPTIMIZER   | TDD           | Itération, amélioration continue, scaling        |

### Prompt Système Global

```
Tu es AI Strategic Brain schoolsWP™.

Tu combines :
- Architecture Blueprint (cadrage stratégique)
- Decision Engine (arbitrage priorisé)
- Strategic Engine (production premium SEO IA)
- Omnichannel Engine (transformation multi-canal)
- Growth Loop (expérimentation)
- Performance Loop (optimisation continue)

Ta mission :
Analyser la demande et activer automatiquement le mode le plus pertinent.

Toujours :
1) Clarifier l'objectif business
2) Identifier la phase concernée
3) Produire une réponse structurée
4) Prioriser selon ROI
5) Proposer la prochaine étape logique

Style : Direct. Concret. Actionnable. Zéro blabla.

Si la phase n'est pas claire, demander maximum 3 questions.
Sinon, exécuter immédiatement.
```

---

## AI STRATEGIC BRAIN — Module formation schoolsWP

Position dans la formation : module final qui relie tout.

```
1️⃣ Fondations WordPress Business
2️⃣ SEO stratégique
3️⃣ Autorité & contenu
4️⃣ Automatisation
5️⃣ Conversion
6️⃣ AI Strategic Brain schoolsWP™  ← cerveau qui relie tout
```

### Objectif pédagogique

À la fin du module, l'élève sait : cadrer un projet WordPress, prendre des décisions stratégiques, produire du contenu qui rank, transformer un contenu en machine omnicanale, tester et optimiser.

Résultat : passer de "site WordPress" → "système de croissance".

### Structure du module (6 exercices)

| Étape | Framework              | Exercice concret                               |
| ----- | ---------------------- | ---------------------------------------------- |
| 1     | Architecture Blueprint | Concevoir l'architecture d'un site WP rentable |
| 2     | Decision Engine        | Prioriser 10 actions SEO                       |
| 3     | Strategic Engine       | Créer une page pilier complète                 |
| 4     | Omnichannel Engine     | Transformer un article en 5 formats            |
| 5     | Growth Loop            | Plan de test SEO (title/CTA)                   |
| 6     | Performance Loop       | Optimiser une page existante via GSC           |

**Différenciation :** la plupart des formations parlent d'outils et de plugins. Ici on enseigne un système de pensée.

---

## PROMESSE MARKETING — Formation schoolsWP

### Versions de la promesse principale

**Version équilibrée :**

> Transforme ton site WordPress en machine de croissance.

**Version système :**

> Construis un WordPress qui travaille pour toi.

**Version résultat :**

> Passe de "site WordPress" à "système de croissance".

**Version différenciante (très schoolsWP) :**

> Arrête de bricoler WordPress. Construis un système.

**Version page de vente (courte) :**

> Crée un WordPress qui attire, convertit et évolue avec ton business.

### Formule signature

**WordPress Growth System™**

> La méthode pour transformer WordPress en levier de croissance.

### Angle marketing stratégique

Ce que tu vends vraiment : pas WordPress, pas du SEO.

> La capacité à construire un actif digital rentable.

La plupart des formations vendent des plugins, des hacks, des astuces.
schoolsWP vend un système de pensée stratégique.

---

## TUNNEL DE VENTE — Formation schoolsWP

### Objectif

Transformer un visiteur WordPress curieux en élève de la formation.
Logique : Éducation → Confiance → Méthode → Offre.

---

### Étape 1 — Aimant à trafic (SEO + LinkedIn + Newsletter)

Point d'entrée : contenu utile.

**Exemples :**

- Article SEO : "Pourquoi 90 % des sites WordPress ne génèrent aucun client"
- Carrousel LinkedIn : "Le système WordPress en 6 étapes pour générer des leads"
- Newsletter : "Comment transformer WordPress en machine de croissance"

**CTA :** Télécharger le blueprint WordPress rentable.

---

### Étape 2 — Lead Magnet

**Blueprint WordPress rentable (PDF)**

Contenu :

- Architecture d'un site qui génère des clients
- Les 6 briques du système schoolsWP
- Erreurs fréquentes
- Checklist rapide

Objectif : montrer l'expertise, préparer la formation.

---

### Étape 3 — Page d'inscription

**Promesse claire :** Transformer WordPress en système de croissance.

**Sous-promesse :** Construire un site WordPress qui attire du trafic, génère des leads et crée de l'autorité.

**Sections :**

1. Problème du marché
2. Présentation du système schoolsWP
3. Ce que l'élève va apprendre
4. Aperçu du module AI Strategic Brain
5. Témoignages / crédibilité
6. CTA : Rejoindre la formation

---

### Étape 4 — Séquence email (5 emails)

**Email 1 – Livraison du blueprint**
Sujet : Voici le blueprint WordPress rentable
Objectif : valeur immédiate.

**Email 2 – Erreurs WordPress**
Sujet : Pourquoi la plupart des sites WordPress ne convertissent pas
Objectif : prise de conscience.

**Email 3 – Le système schoolsWP**
Sujet : Le système en 6 briques qui change tout
Objectif : présenter la méthode.

**Email 4 – Étude de cas**
Sujet : Comment structurer un site WordPress rentable
Objectif : crédibilité.

**Email 5 – Offre**
Sujet : La formation schoolsWP est ouverte
Objectif : conversion.

---

### Étape 5 — Page de vente

**Promesse :** Créer un site WordPress qui génère trafic, autorité et clients.

**Structure :**

**Section 1 – Le problème**
Les sites WordPress échouent car :

- Pas de stratégie
- Pas de système
- Contenu isolé

**Section 2 – La solution**
La méthode schoolsWP — Les 6 briques :

- Architecture Blueprint
- Decision Engine
- Strategic Engine
- Omnichannel Engine
- Growth Loop
- Performance Loop

**Section 3 – Ce que tu vas construire**

- Un site structuré
- Un système de contenu
- Un tunnel de conversion

**Section 4 – Programme**
Modules détaillés.

**Section 5 – Résultats attendus**

- Trafic qualifié
- Autorité thématique
- Génération de leads

**Section 6 – Bonus**

- Templates SEO
- Prompts schoolsWP
- Checklists WordPress

**Section 7 – Garantie**
Garantie 14 ou 30 jours.

**Section 8 – CTA**
Rejoindre la formation.

---

### Étape 6 — Upsell post-achat

**Pack templates schoolsWP**

- Prompts IA
- Templates SEO
- Checklists WordPress

---

## ROADMAP PÉDAGOGIQUE — Formation schoolsWP (12 semaines)

**Objectif :** Former quelqu'un à construire un site WordPress qui génère trafic, autorité et revenus.

### Semaine 1 — Le modèle WordPress rentable

Objectif : comprendre le système.

Contenu :

- Pourquoi 90 % des sites WordPress échouent
- Le modèle site vitrine vs machine de croissance
- Présentation du schoolsWP Authority System™

Livrable : vision stratégique du projet
Exercice : définir l'objectif business du site.

---

### Semaine 2 — Positionnement & niche

Objectif : éviter le contenu générique.

Contenu :

- Choisir une niche rentable
- Identifier un problème réel
- Créer un positionnement clair

Livrable : positionnement du site
Exercice : définir une promesse claire.

---

### Semaine 3 — Architecture stratégique

Framework : Architecture Blueprint (SPECS)

Contenu :

- Architecture d'un site qui rank
- Structure pages piliers
- Logique de cocon sémantique

Livrable : plan complet du site
Exercice : créer l'architecture de son site.

---

### Semaine 4 — Recherche SEO intelligente

Contenu :

- Identifier les mots-clés qui convertissent
- Comprendre l'intention de recherche
- Trouver les pages à fort ROI

Livrable : liste de mots-clés prioritaires
Exercice : définir les 10 premières pages stratégiques.

---

### Semaine 5 — Créer une page pilier

Framework : Strategic Engine (CREDO)

Contenu :

- Structure d'une page qui rank
- SEO + IA
- Optimisation featured snippets

Livrable : première page pilier
Exercice : écrire une page pilier complète.

---

### Semaine 6 — Autorité & contenu

Contenu :

- Créer un cluster de contenu
- Maillage interne stratégique
- Stratégie autorité

Livrable : plan de contenu sur 3 mois
Exercice : définir 10 articles complémentaires.

---

### Semaine 7 — WordPress qui convertit

Contenu :

- Structure d'une page efficace
- UX simple
- CTA intelligents

Livrable : structure conversion du site
Exercice : optimiser une page existante.

---

### Semaine 8 — Automatisation

Stack recommandée : FluentCRM + Fluent Forms + WordPress

Contenu :

- Capture de leads
- Séquences email
- Segmentation

Livrable : tunnel email simple
Exercice : créer une séquence de 5 emails.

---

### Semaine 9 — Machine omnicanale

Framework : Omnichannel Engine (DITO)

Contenu :

- Transformer 1 contenu en 5 formats
- LinkedIn, newsletter, email

Livrable : plan de diffusion omnicanal
Exercice : transformer un article en 3 formats.

---

### Semaine 10 — Tester et optimiser

Framework : Growth Loop (PACT)

Contenu :

- Tester un title SEO
- Tester un CTA
- Tester un angle contenu

Livrable : plan d'expérimentation
Exercice : définir 3 tests SEO.

---

### Semaine 11 — Optimisation continue

Framework : Performance Loop (TDD)

Contenu :

- Analyser GSC
- Améliorer CTR
- Améliorer conversion

Livrable : plan d'optimisation
Exercice : optimiser une page existante.

---

### Semaine 12 — Le cerveau stratégique

Module final : AI Strategic Brain schoolsWP™

Contenu :

- Penser comme un stratège
- Utiliser les frameworks
- Construire un système durable

Livrable : stratégie complète du site
Exercice : créer son plan de croissance 12 mois.

**Résultat final :** un site structuré + stratégie SEO + système contenu + tunnel email + plan de croissance.

---

## POSITIONNEMENT PREMIUM — Formation 900€ à 2000€

### Angle différenciant

La plupart des formations WordPress vendent des tutoriels, plugins, outils.
schoolsWP vend un système pour transformer WordPress en machine de croissance.

**Promesse centrale :** Construire un site WordPress qui génère trafic, autorité et revenus.

**Promesse premium :** Concevoir un écosystème WordPress capable d'attirer trafic, leads et clients.

### Facteur différenciant

Méthode propriétaire schoolsWP Authority System™ avec ses 6 frameworks :
Architecture Blueprint · Decision Engine · Strategic Engine · Omnichannel Engine · Growth Loop · Performance Loop

Cela transforme la formation en méthode structurée, pas en cours.

### Structure de l'offre

**Version Core — 900 €**

- Formation complète
- Frameworks
- Templates

**Version Pro — 1500 €**

- Formation + templates
- Bonus AI Strategic Brain
- Études de cas

**Version Premium — 2000 €**

- Formation + bonus
- Audit site
- Session stratégique

### Pourquoi ce prix est crédible

La promesse est claire : créer un site WordPress rentable.
Un site bien structuré peut générer 500 à 3000 €/mois.
La formation se rembourse en 1 à 3 mois.

---

## TUNNEL "AUTORITÉ SEO" — schoolsWP

Principe : Google → contenu autorité → capture → séquence → vente.
Simple. Stable. Scalable. Pas de publicité.

### Flux

1. **Page pilier SEO** → attirer trafic qualifié à intention forte
2. **Capture de lead** → blueprint PDF au milieu de la page pilier
3. **Séquence email 5 messages** → valeur → méthode → offre
4. **Page de vente** → conversion

### Métriques réalistes

- 1 page pilier = 1000 visiteurs/mois
- Conversion lead : 5 % → 50 leads
- Conversion formation : 3 % → 1-2 ventes
- À 1500 € → 1500 à 3000 €/mois par page pilier

Avec 5 pages piliers stratégiques : effet levier maximal.

---

## 5 PAGES SEO À FORT LEVIER — schoolsWP

Pages piliers prioritaires pour alimenter le tunnel formation.

### Page 1 — Créer un site WordPress rentable

Mot-clé : `site wordpress rentable`
Variantes : créer un site wordpress rentable / comment gagner de l'argent avec wordpress / blog wordpress rentable
Audience : gens qui veulent monétiser → idéal pour vendre la formation.
CTA : Télécharger le plan pour transformer WordPress en machine de croissance.

### Page 2 — Trouver des clients avec WordPress

Mot-clé : `trouver des clients wordpress`
Variantes : trouver des clients avec son site / marketing wordpress
Audience : freelances, agences, indépendants → ton audience cible.
Angle : transformer son site en machine à prospects.

### Page 3 — Créer une page pilier SEO

Mot-clé : `page pilier seo`
Variantes : pillar page seo / cocon sémantique page pilier
Audience : trafic expert → crédibilité forte + autorité.
Objectif : montrer la méthode.

### Page 4 — Automatiser WordPress

Mot-clé : `automatisation wordpress`
Variantes : automatiser un site wordpress / marketing automation wordpress
Contenu : FluentCRM, formulaires, tunnels, séquences.
Angle : transformer WordPress en machine automatisée.

### Page 5 — Monétiser un site WordPress

Mot-clé : `monetiser wordpress`
Variantes : gagner de l'argent wordpress / revenus wordpress / business wordpress
Audience : intention forte → gens qui veulent gagner de l'argent.
Conversion naturelle vers la formation.

---

## STRUCTURE PAGE PILIER TOP 3 GOOGLE

Longueur idéale : 2500 à 3500 mots. Structure claire > volume brut.

### Section 1 — Hook + promesse (100-150 mots)

Problème clair → promesse → aperçu solutions.

Exemple :

> La plupart des sites WordPress ne génèrent ni trafic ni clients. Dans ce guide, vous allez découvrir comment transformer WordPress en véritable système de croissance.

### Section 2 — Comprendre le problème

H2 : Pourquoi la plupart des sites WordPress ne génèrent aucun résultat
Contenu : erreurs courantes, confusion, mauvais modèles.
Objectif : identification + tension.

### Section 3 — Présenter le modèle

H2 : Le modèle pour transformer WordPress en machine de croissance
Présenter schoolsWP Authority System™.

Schéma : Architecture → Contenu → Autorité → Trafic → Conversion

### Section 4 — Étapes concrètes (H2 par étape)

- Étape 1 : construire une architecture solide
- Étape 2 : créer une page pilier
- Étape 3 : développer l'autorité thématique
- Étape 4 : capter les leads
- Étape 5 : automatiser la conversion

Chaque étape : explication simple + checklist + exemple.

### Section 5 — Exemple concret

H2 : Exemple d'un site WordPress structuré pour générer du trafic
Contenu : architecture réelle, plan de contenu, logique SEO.

### Section 6 — Erreurs à éviter

H2 : Les erreurs qui empêchent un site WordPress de décoller
Format liste courte : publier sans stratégie / ignorer le SEO / absence de capture email.

### Section 7 — FAQ optimisée IA

H2 : Questions fréquentes

- Comment créer une page pilier ?
- Combien d'articles faut-il pour ranker ?
- Comment monétiser un site WordPress ?
- Combien de temps pour obtenir du trafic ?

Réponses courtes et claires. Format apprécié des IA.

### Section 8 — Conclusion stratégique

H2 : Comment passer d'un site WordPress simple à un système de croissance
Résumé : architecture + contenu + automatisation + optimisation.

### Section 9 — CTA principal

> Télécharger le plan pour transformer WordPress en machine de croissance

### Checklist SEO page pilier

- H1 clair
- H2 structurés
- Table des matières
- FAQ
- Maillage interne
- Schema FAQ
- Images optimisées

### 3 facteurs de ranking

1. Structure claire
2. Profondeur réelle
3. Autorité du site

Pour schoolsWP : chaque page pilier doit montrer la méthode, prouver l'expertise, introduire le funnel.

---

## PROMESSE MARKETING IRRÉSISTIBLE — Formation schoolsWP

### Versions de la promesse principale

**Version forte :**

> Transformez votre site WordPress en système de croissance capable d'attirer trafic, leads et clients.

**Version impactante :**

> Construisez un site WordPress qui travaille pour vous : trafic, autorité et clients.

**Version orientée résultat :**

> Passez d'un simple site WordPress à une machine de croissance.

**Version premium :**

> Apprenez à concevoir un écosystème WordPress capable d'attirer trafic qualifié, générer des leads et convertir des clients.

**Version ultra simple (souvent la meilleure) :**

> Créez un site WordPress qui génère trafic et clients.

### Formule complète recommandée

**Résultat + système + délai crédible :**

> En 12 semaines, transformez votre site WordPress en système de croissance capable d'attirer trafic, leads et clients.

**Sous-promesse (juste en dessous) :**

> Sans publier au hasard.
> Sans dépendre de la publicité.
> Et sans complexité technique inutile.

### Levier psychologique

La formation ne vend pas "WordPress". Elle vend indépendance et croissance.

---

## PAGE DE VENTE COMPLÈTE — Formation schoolsWP

### HERO

**Titre :** Transformez votre site WordPress en système de croissance.

**Sous-titre :** En 12 semaines, construisez un site capable d'attirer trafic qualifié, générer des leads et convertir des clients.

Sans publier au hasard. Sans dépendre de la publicité. Sans complexité technique inutile.

**CTA :** Découvrir le programme

---

### Le problème

Aujourd'hui, la plupart des sites WordPress :

- publient du contenu sans stratégie
- n'attirent presque aucun trafic
- ne génèrent aucun client

Résultat : WordPress devient un simple site vitrine. Alors qu'il pourrait devenir un moteur de croissance.

---

### La promesse

La formation schoolsWP apprend à :

- structurer son site intelligemment
- attirer du trafic qualifié
- créer du contenu qui rank
- transformer ce trafic en leads
- construire un système durable

**Autrement dit :** Créer un site WordPress qui travaille pour vous.

---

### La méthode — schoolsWP Authority System™

**1 — Architecture Blueprint**
Structurer le site pour qu'il puisse grandir.

**2 — Decision Engine**
Prioriser les actions qui ont un impact réel.

**3 — Strategic Engine**
Créer du contenu qui attire trafic et autorité.

**4 — Omnichannel Engine**
Transformer un contenu en machine de diffusion.

**5 — Growth Loop**
Tester ce qui fonctionne vraiment.

**6 — Performance Loop**
Optimiser et améliorer en continu.

---

### Le programme (12 semaines)

- S1 : Le modèle WordPress rentable
- S2 : Positionnement
- S3 : Architecture SEO
- S4 : Recherche SEO
- S5 : Page pilier
- S6 : Autorité
- S7 : Conversion
- S8 : Automatisation
- S9 : Omnicanal
- S10 : Expérimentation
- S11 : Optimisation
- S12 : Stratégie long terme

---

### Ce qu'on obtient à la fin

Un système complet : site structuré + stratégie SEO + plan de contenu + tunnel email + méthode d'optimisation.

---

### Bonus

**AI Strategic Brain schoolsWP™** — système de prompts et frameworks pour prendre les bonnes décisions stratégiques.

**Templates opérationnels** — architecture SEO, structure page pilier, plan de contenu, checklists optimisation.

---

### À qui s'adresse cette formation

- freelance, créateur de contenu, formateur, entrepreneur, utilisateur WordPress
- Qui veut construire un site qui génère de vrais résultats

**Pas pour :** ceux qui cherchent un résultat magique, qui ne veulent pas produire de contenu, ou qui cherchent un simple tutoriel.

---

### Prix et garantie

**900 € — paiement unique — accès à vie**

Garantie 14 jours satisfait ou remboursé.

---

### Dernier message

WordPress peut être un simple site vitrine ou un système de croissance.
La différence ne vient pas des plugins. Elle vient de la stratégie.

**CTA :** Rejoindre la formation schoolsWP

---

## 5 BLOCS PSYCHOLOGIQUES DE CONVERSION

### Bloc 1 — Prise de conscience

Objectif : faire réaliser au lecteur qu'il a un problème.

Ce que les gens pensent faire : publier des articles / installer des plugins / améliorer le design.

La réalité : le problème n'est pas WordPress. C'est l'absence de stratégie.

> La plupart des sites WordPress échouent pour une raison simple : ils publient du contenu sans système.

---

### Bloc 2 — Nouvelle perspective

Objectif : montrer qu'il existe une autre façon de faire.

> Les sites WordPress qui réussissent ne publient pas plus. Ils publient mieux et de manière structurée.

Fonctionnent comme un système : architecture claire + contenu stratégique + diffusion intelligente + optimisation continue.

---

### Bloc 3 — Méthode

Objectif : montrer que la solution est structurée, logique, reproductible.

Introduire schoolsWP Authority System™.

**Règle :** Les gens achètent des systèmes, pas des cours.

---

### Bloc 4 — Projection

Objectif : faire imaginer le résultat.

> Imaginez votre site dans 6 mois : vos articles attirent du trafic, votre site capte des leads, vos contenus deviennent des ressources citées.
> Votre site n'est plus un simple blog. C'est un actif digital.

---

### Bloc 5 — Friction finale (objections)

**"Je ne suis pas technique"** → La formation est conçue pour rester simple et accessible.

**"Je n'ai pas beaucoup de temps"** → Le programme est structuré sur 12 semaines avec des actions concrètes.

**"Le SEO prend du temps"** → Oui. Mais c'est aussi le canal d'acquisition le plus durable.

---

### Structure de page optimale (ordre des blocs)

1. Hero
2. Problème
3. Nouvelle perspective
4. Méthode
5. Programme
6. Projection
7. Bonus
8. Objections
9. Prix
10. CTA final

**Règle d'or :** La page ne vend pas une formation WordPress. Elle vend un système de croissance WordPress. C'est ce qui justifie le prix premium.

---

## PAGE DE VENTE LONGUE — schoolsWP (version complète 14 sections)

### HERO

**Titre :** Transforme ton site WordPress en machine de croissance

**Sous-titre :**
Arrête de publier au hasard, bricoler ton SEO et empiler des plugins sans logique.
Avec la méthode schoolsWP, tu construis un système WordPress clair, rapide, automatisé et rentable.

**CTA :** Je veux construire mon système WordPress rentable

**Preuve courte :** Formation complète sur 12 semaines pour créer un site qui attire du trafic, génère des leads et soutient ton activité.

---

### Section 1 — Le vrai problème

**Titre :** Le problème n'est pas WordPress

WordPress n'est pas le problème. Le problème, c'est tout le reste :

- un site sans vraie structure
- du contenu publié sans stratégie
- un SEO mal priorisé
- des plugins empilés sans logique
- aucune automatisation claire
- un trafic qui ne convertit pas

Tu passes du temps. Tu fais "plein de choses". Mais ton site ne devient pas un levier de croissance.

> Tu as un site. Pas un système.

---

### Section 2 — La promesse

**Titre :** Ce que cette formation va changer

Cette formation t'aide à construire un écosystème WordPress capable de :

- attirer un trafic qualifié
- renforcer ton autorité
- capter des leads
- automatiser une partie de ton marketing
- convertir plus intelligemment

Tu ne vas pas juste apprendre WordPress. Tu vas apprendre à penser, structurer et optimiser ton site comme un vrai actif business.

---

### Section 3 — Pour qui

**Titre :** Cette formation est faite pour toi si…

**Tu es freelance** — et tu veux un site qui te rapporte autre chose que quelques visites.

**Tu es créateur ou formateur** — et tu veux transformer ton contenu en levier d'acquisition.

**Tu es entrepreneur** — et tu veux un WordPress plus simple, plus stratégique et plus rentable.

**Tu es déjà lancé** — mais ton site reste flou, mal structuré ou sous-exploité.

---

### Section 4 — Ce que tu vas obtenir

**Titre :** Ce que tu vas construire concrètement

À la fin du programme, tu repars avec :

- un positionnement plus clair
- une architecture de site cohérente
- une stratégie SEO priorisée
- une page pilier prête à performer
- un système de contenu plus intelligent
- une logique omnicanale claire
- un tunnel email simple
- un plan d'optimisation concret

> Tu ne repars pas avec de la théorie. Tu repars avec une structure.

---

### Section 5 — La méthode signature

**Titre :** La méthode schoolsWP Authority System™

Toute la formation repose sur une méthode claire. Pas sur des hacks. Pas sur des recettes TikTok. Pas sur du blabla.

**1. Architecture Blueprint** — Tu cadres ton projet. Tu poses la structure. Tu arrêtes la dispersion.

**2. Decision Engine** — Tu apprends à prioriser. Tu sais quoi faire maintenant, quoi repousser, quoi ignorer.

**3. Strategic Engine** — Tu crées du contenu solide, utile, structuré pour le SEO et les IA.

**4. Omnichannel Engine** — Tu transformes un contenu en plusieurs formats. Tu cesses de repartir de zéro à chaque fois.

**5. Growth Loop** — Tu testes ce qui mérite vraiment d'être testé.

**6. Performance Loop** — Tu analyses. Tu corriges. Tu améliores en continu.

> Tu passes d'un site WordPress "présent en ligne" à un système WordPress piloté.

---

### Section 6 — Le programme (12 semaines)

- **S1** — Le modèle WordPress rentable : comprendre pourquoi la majorité des sites stagnent
- **S2** — Positionnement & niche : clarifier ta cible, ton angle et ta promesse
- **S3** — Architecture stratégique : construire un site logique, lisible, orienté SEO et conversion
- **S4** — Recherche SEO intelligente : trouver les mots-clés utiles et prioriser
- **S5** — Créer une page pilier : contenu fort, citables IA, prêt à performer
- **S6** — Autorité & contenu : cluster, maillage, profondeur, cohérence
- **S7** — WordPress qui convertit : CTA, parcours, clarté
- **S8** — Automatisation : WordPress + formulaires + email
- **S9** — Machine omnicanale : recycler intelligemment le contenu
- **S10** — Tester et optimiser : logique d'expérimentation simple
- **S11** — Optimisation continue : lire les bons signaux, améliorer ce qui compte
- **S12** — AI Strategic Brain schoolsWP™ : assembler la méthode pour piloter comme un actif stratégique

---

### Section 7 — Le module différenciant

**Titre :** Le cerveau stratégique intégré : AI Strategic Brain schoolsWP™

C'est la brique qui rend la formation différente. Tu ne reçois pas juste des vidéos. Tu apprends à utiliser un vrai système de réflexion pour :

- cadrer un projet
- décider plus vite
- produire plus proprement
- transformer ton contenu
- tester intelligemment
- optimiser en continu

C'est ce qui relie toute la formation. Et c'est ce qui évite de retomber dans le chaos après 3 semaines.

---

### Section 8 — Les bonus

**Bonus 1 — Templates schoolsWP** : checklist, structures de pages, frameworks, matrices de décision, modèles de contenu.

**Bonus 2 — Prompts opérationnels** : prompts prêts à utiliser pour SEO, contenu, structuration et automatisation.

**Bonus 3 — Stack recommandée** : les bons outils, les bons réglages, la bonne logique.

**Bonus 4 — Plans d'action rapides** : versions "quick wins" pour avancer même quand tu manques de temps.

---

### Section 9 — Pourquoi schoolsWP est différente

La plupart des formations t'apprennent : installer des plugins / suivre des tutoriels / reproduire des actions.

schoolsWP t'apprend : structurer / prioriser / produire / automatiser / convertir / optimiser.

> Tu n'apprends pas seulement à utiliser WordPress. Tu apprends à t'en servir comme d'un levier.

---

### Section 10 — Résultats attendus

Cette formation peut t'aider à : rendre ton site plus clair / publier avec une vraie logique / gagner du temps / améliorer ton SEO / mieux capter les leads / structurer un système durable.

Ce n'est pas une promesse miracle. C'est une méthode sérieuse. Elle demande du travail. Mais elle t'évite des mois d'errance.

---

### Section 11 — Objections

**"Je ne suis pas très technique."** → La formation est pensée pour rester claire, progressive et actionnable.

**"J'ai déjà suivi des formations."** → Souvent elles sont fragmentées. Ici, tout est relié par une logique système.

**"Je manque de temps."** → La méthode t'aide justement à arrêter de perdre du temps sur les mauvais chantiers.

**"Mon site existe déjà."** → Encore mieux. Tu pourras l'optimiser avec une approche plus mature.

---

### Section 12 — Offre

Ce que tu reçois :

- 12 semaines de formation structurée
- La méthode schoolsWP Authority System™
- Le module AI Strategic Brain schoolsWP™
- Les templates opérationnels
- Les frameworks de décision
- Les modèles de structuration SEO / contenu / conversion
- Les bonus outils et stack recommandée

**Tarifs :** Core 900 € · Pro 1500 € · Premium 2000 €

---

### Section 13 — CTA final

**Titre :** Ton site peut rester une vitrine ou devenir un vrai système de croissance

Tu peux continuer à publier sans cadre, tester sans méthode et empiler des outils.
Ou tu peux construire quelque chose de plus propre. Plus clair. Plus rentable.

**CTA :** Je rejoins la formation schoolsWP

---

### Section 14 — FAQ

**Mon site existe déjà, c'est utile ?** — Oui. Autant pour structurer un nouveau projet que pour remettre de l'ordre dans un site existant.

**Faut-il être expert en WordPress ?** — Non. Il faut surtout être prêt à appliquer une méthode claire.

**C'est seulement du SEO ?** — Non. Architecture, contenu, conversion, automatisation et optimisation.

**C'est orienté théorie ?** — Non. L'objectif est l'application directe.

**Quels outils sont utilisés ?** — WordPress, une stack claire et des outils utiles. Pas une usine à gaz.

---

### Recommandation design

Structure visuelle : hero sobre / bloc problème / bloc transformation / méthode signature / programme / bonus / objections / offre / FAQ / CTA final.

Fond clair. Beaucoup d'air. Typo propre. Accent couleur chaleureux pour les CTA. Aligné avec le branding schoolsWP.

---

## PLAN COMPLET FORMATION — schoolsWP Authority System™

**Sous-titre :** Transformer un site WordPress en machine de trafic, d'autorité et de revenus.
**Public :** freelances · créateurs · entrepreneurs · formateurs
**Logique :** Architecture → Autorité → Système → Croissance

### Module 1 — Les fondations WordPress business

Objectif : comprendre ce qui fait un site WordPress rentable.

Contenu :

- WordPress comme système de croissance
- Les 5 erreurs qui empêchent un site de décoller
- Positionnement : niche, angle, différenciation
- Structure minimale d'un site rentable
- Stack WordPress recommandée

Résultat : un projet WordPress clair et viable.

---

### Module 2 — Architecture SEO intelligente

Objectif : créer un site qui peut réellement ranker.

Contenu :

- Comprendre l'intention de recherche
- Construire un cocon sémantique simple
- Page pilier vs article satellite
- Maillage interne stratégique
- Structurer pour Google et l'IA

Exercice : créer l'architecture SEO complète du site.

---

### Module 3 — Contenu qui crée l'autorité

Objectif : produire du contenu qui rank, est cité par l'IA, et convertit.

Contenu :

- La structure d'une page pilier
- Écriture SEO moderne (IA + SGE)
- FAQ stratégiques
- Snippets et citabilité
- CTA intelligents

Exercice : créer une page pilier complète.

---

### Module 4 — Automatisation WordPress

Objectif : transformer le site en machine automatisée.

Contenu :

- CRM WordPress (FluentCRM)
- Capture de leads
- Séquences email simples
- Automatisation marketing
- Segmentation intelligente

Exercice : créer un tunnel simple automatisé.

---

### Module 5 — Monétisation WordPress

Objectif : transformer le trafic en revenus.

Contenu :

- Affiliation stratégique
- Produits digitaux
- Services premium
- Tunnel de conversion
- Pages qui vendent

Exercice : créer une offre claire.

---

### Module 6 — AI Strategic Brain schoolsWP™ (module signature)

Objectif : apprendre le système de pensée derrière les sites performants.

Les 6 moteurs :

1. Architecture Blueprint
2. Decision Engine
3. Strategic Engine
4. Omnichannel Engine
5. Growth Loop
6. Performance Loop

Exercice : appliquer le système complet à son site.

---

### Module 7 — Growth & domination

Objectif : passer de site actif à machine de croissance.

Contenu :

- Stratégie contenu long terme
- Autorité thématique
- Amplification omnicanale
- Partenariats & backlinks
- Optimisation continue

**Résultat final :** site structuré + architecture SEO + contenu pilier + tunnel simple + système de croissance = un actif digital.

---

## FORMATION 10× — Version Premium schoolsWP

**Formation signature** : schoolsWP Authority System™
**Sous-titre :** Construire un site WordPress qui génère trafic, autorité et revenus.
**Durée :** 10 à 12 semaines

---

### PHASE 1 — FOUNDATION (construire la base stratégique)

**Module 1 — WordPress Business**

- WordPress comme actif digital
- Différence site vitrine / machine de croissance
- Les 5 modèles économiques WordPress
- Choisir son positionnement

Livrable → Blueprint du projet

**Module 2 — Architecture SEO**

- Intention de recherche
- Cluster sémantique
- Page pilier + maillage interne stratégique
- Architecture scalable

Livrable → Architecture SEO complète

---

### PHASE 2 — AUTHORITY (construire l'autorité)

**Module 3 — Page pilier**

- Structure pilier
- SEO moderne + citabilité IA
- FAQ stratégiques + CTA intelligents

Livrable → 1 page pilier premium

**Module 4 — Strategic Content Engine**

- Stratégie éditoriale
- Clusters + contenu evergreen
- Plan éditorial 90 jours

Livrable → Roadmap contenu

---

### PHASE 3 — SYSTEM (transformer le site en machine)

**Module 5 — Automatisation**

- CRM WordPress, capture de leads, segmentation
- Séquences email + automatisation marketing

Livrable → Tunnel automatisé

**Module 6 — Monétisation**

- Affiliation stratégique, produits digitaux, consulting
- Pages de conversion

Livrable → Offre claire + page de vente

---

### PHASE 4 — AI STRATEGIC BRAIN (le cerveau du système)

Module signature — les élèves apprennent à utiliser :

- Architecture Blueprint (cadrage stratégique)
- Decision Engine (priorisation)
- Strategic Engine (production premium)
- Omnichannel Engine (repurposing contenu)
- Growth Loop (expérimentation)
- Performance Loop (optimisation continue)

Livrable → Système de pilotage complet

---

### PHASE 5 — GROWTH (passer à l'échelle)

**Module 8 — Amplification**

- Omnicanal : LinkedIn, newsletter, SEO long terme, partenariats

Livrable → Plan de croissance 12 mois

---

### Positionnement marché

Ce n'est pas une formation WordPress / SEO / marketing.
C'est **un système complet pour créer un business WordPress**.

### Pricing formation 10×

| Version     | Prix          |
| ----------- | ------------- |
| Solo        | 997 – 1497 €  |
| Accompagnée | 2497 – 3997 € |
| Mastermind  | 5000 €+       |

---

## PRODUIT PREMIUM CLIENT — schoolsWP Strategic Brain™

**Sous-titre :** Le cerveau stratégique qui pilote ton site WordPress pour générer trafic, autorité et clients.

**Cible :** freelances WordPress, créateurs, agences, entrepreneurs.

### Ce que le client obtient

Un assistant stratégique structuré qui sait :

1. Cadrer un projet
2. Prioriser les actions
3. Produire du contenu SEO IA
4. Transformer un contenu en machine omnicanale
5. Tester des optimisations
6. Améliorer les performances

### Les 6 modules du Strategic Brain

**ARCHITECT** — créer l'architecture SEO du site → pages piliers, clusters, plan de contenu.

**STRATEGIST** — décider quoi faire en priorité → roadmap claire, priorités ROI.

**PRODUCER** — produire du contenu premium → plan SEO, structure IA, FAQ, CTA.

**TRANSFORMER** — créer la machine omnicanale → carrousel, newsletter, email.

**EXPERIMENT** — tester des optimisations → hypothèse + test concret.

**OPTIMIZER** — améliorer les performances → plan d'optimisation + priorités.

### Comment le vendre

**Option 1 — Accès Premium standalone** : 97 – 297 €
Prompts structurés + guide d'utilisation + templates.

**Option 2 — Bonus formation** : valeur perçue 297 €+
Inclus dans le programme WordPress Business Engine.

**Option 3 — Bonus consulting** : valeur perçue 500 €+
Offert dans un accompagnement — fort effet de valeur.

### Positionnement marketing

Ne jamais dire "prompt IA". Dire : "Cerveau stratégique WordPress".

> Tu n'utilises plus l'IA au hasard. Tu pilotes ton site WordPress avec un système stratégique.

---

## PROMPT MAÎTRE CLIENT — schoolsWP Strategic Brain™

Prompt à copier-coller par le client dans son IA :

```
Tu es le schoolsWP Strategic Brain™.

Tu es un expert WordPress stratégique spécialisé en :
SEO, architecture de site, contenu qui génère des clients,
automatisation et croissance.

Ta mission : m'aider à développer mon site WordPress
de manière stratégique.

Avant de répondre :

1. Comprends mon objectif business
2. Identifie la phase stratégique
3. Donne uniquement des recommandations concrètes
4. Priorise selon impact et facilité
5. Structure clairement la réponse

Modes disponibles :

ARCHITECT → structurer un site ou une stratégie SEO
STRATEGIST → prioriser les actions
PRODUCER → produire un contenu SEO puissant
TRANSFORMER → transformer un contenu en multi-formats
EXPERIMENT → tester une optimisation
OPTIMIZER → améliorer les performances

Règles :
- réponses claires
- actions concrètes
- style simple
- zéro jargon inutile

Si mon objectif n'est pas clair,
pose maximum 3 questions.

Sinon, aide-moi immédiatement.

Ma demande :

[ÉCRIS TON BESOIN]
```

### Ce qui rend le produit fort

Le client ne voit qu'un seul prompt.
Mais derrière il utilise : SPECS · CREDO · PACT · DITO · COT · TDD — sans le savoir.

---

## PACK COMPLET CLIENT — schoolsWP Strategic Brain™

### Contenu du pack

1. Prompt maître
2. Guide d'utilisation
3. Templates pratiques
4. Format de livraison

---

### Guide d'utilisation (PDF)

**Étape 1** — Coller le prompt dans ton IA.

**Étape 2** — Décrire ton besoin :

- "Créer la structure SEO de mon site WordPress."
- "Améliorer le CTR de mon article."
- "Créer une page pilier maintenance WordPress."
- "Transformer cet article en contenu LinkedIn."

**Étape 3** — Appliquer les recommandations.

---

### Template 1 — Architecture de site

```
Je crée un site WordPress pour [activité].
Public cible : [persona]
Objectif business : [générer des leads / vendre formation / service]

Peux-tu structurer :
- l'architecture du site
- les pages piliers
- les clusters SEO
- les premières actions prioritaires
```

### Template 2 — Création d'article SEO

```
Sujet : [mot clé]
Public cible : [persona]
Objectif : [trafic / leads / autorité]

Peux-tu créer :
- plan SEO complet
- structure H2 H3
- FAQ optimisée IA
- CTA logique
```

### Template 3 — Optimisation d'article

```
Voici mon article : [colle ton contenu]
Objectif : améliorer SEO / CTR / conversion

Peux-tu analyser et proposer :
- optimisations prioritaires
- quick wins
- améliorations structurelles
```

### Template 4 — Transformation omnicanale

```
Voici mon contenu : [colle article / transcript]

Peux-tu transformer ce contenu en :
- post LinkedIn
- carrousel
- newsletter
- email
```

---

### Format de livraison

**Option simple** : Google Doc ou PDF (prompt + guide + templates)

**Option premium** : Notion workspace (Strategic Brain / Templates / Guides / Cas d'usage)

**Option bonus** : Mini-vidéo Loom "Comment utiliser le Strategic Brain" — fort effet valeur perçue.

### Pricing produit seul

| Format         | Prix          |
| -------------- | ------------- |
| Standalone     | 97 – 197 €    |
| Avec formation | valeur 297 €+ |
| Avec accomp.   | valeur 500 €+ |

---

## VISUEL CONCEPT — schoolsWP Strategic Brain™

Critères : rendre le concept compréhensible en 3 secondes. Évoquer intelligence, système, pilotage, WordPress, stratégie.

### Concept 1 — The Strategic Brain (recommandé)

**Idée :** un cerveau digital composé de connexions. Chaque zone = un module.

**Modules :** Architect · Strategist · Producer · Transformer · Experiment · Optimizer

**Message transmis :** "Un cerveau stratégique qui pilote ton site."

**Utilisations :** hero section landing / slide conférence / couverture PDF / visuel LinkedIn.

**Pourquoi c'est le meilleur :** simple à comprendre, mémorable, premium, iconique. Peut devenir le symbole du produit.

---

### Concept 2 — The Strategic Control Center

**Idée :** un centre de contrôle, comme un cockpit. Chaque écran = une fonction (SEO / contenu / conversion / optimisation).

**Message transmis :** "Tu pilotes ton business WordPress."

**Utilisations :** page de vente, visuel produit, publicité LinkedIn.

---

### Concept 3 — The Strategic System

**Idée :** un système modulaire connecté. Chaque module = une brique de la méthode.

**Modules :** Architecture → Decision → Production → Transformation → Test → Optimisation

**Message transmis :** "Ce n'est pas un prompt. C'est un système."

---

### Visuel idéal schoolsWP

```
         ARCHITECT
        /
OPTIMIZER          STRATEGIST
    |                   |
EXPERIMENT         PRODUCER
        \
         TRANSFORMER

      [ schoolsWP Strategic Brain™ ]
```

Cerveau digital minimal + 6 nœuds autour avec les 6 modules. Centre : `schoolsWP Strategic Brain™`.

---

## Frameworks de Prompt Engineering — schoolsWP Intelligence Suite™

### RACE — Framework exécution rapide

**RACE = Role · Action · Context · Expectation**

1. **Role** — Définit qui doit être l'IA (niveau d'expertise + ton)
2. **Action** — Ce que l'IA doit faire (verbe d'action clair)
3. **Context** — Informations nécessaires (audience, site, outils)
4. **Expectation** — Format et résultat attendu

**Utilité :** réduire l'ambiguïté, améliorer la précision, rendre les réponses reproductibles, faciliter l'intégration dans des workflows (agents, API, automation)

---

### RACE — Version officielle schoolsWP

```
[R] ROLE
Tu es un expert WordPress senior spécialisé en SEO (Google + Bing), performance, sécurité, automatisation (FluentCRM / Fluent Forms / TutorLMS / FluentBooking) et conversion.
Tu réponds en français, style schoolsWP : direct, concret, phrases courtes. Zéro blabla. Tu proposes des actions applicables immédiatement.

[A] ACTION
Ta mission : produire une recommandation opérationnelle et priorisée sur : [SUJET].
Tu dois :
1) Diagnostiquer rapidement la situation à partir des éléments fournis.
2) Proposer des actions concrètes (checklist) avec un ordre de priorité.
3) Donner une version "quick wins (30 min)" + une version "propre (2–3 h)".
4) Fournir si utile : snippets (Rank Math, WP, .htaccess, SQL, CSS), réglages plugin, ou structure de page.

[C] CONTEXT
- Site : schoolsWP.com
- Audience : freelances / créateurs / entrepreneurs WordPress, niveau technique variable
- Objectif business : trafic qualifié + citabilité IA + conversion
- Contrainte : pas de jargon marketing, pas de théorie inutile
- Données disponibles (selon le cas) :
  • URL / page : [URL]
  • Intention cible : [INTENTION]
  • Mot-clé principal : [KW_MAIN]
  • Mots-clés secondaires : [KW_SECONDARY]
  • Outils : Rank Math Pro, GSC, GA4, (optionnel) DataForSEO, Fluent Suite
  • Extraits / captures / contenu : [INPUT]

[E] EXPECTATION (FORMAT DE SORTIE)
Tu réponds avec ce format EXACT :

1) Résumé en 5 lignes (ce qui bloque / ce qui manque)
2) Priorités (P1 / P2 / P3) + effort estimé (S/M/L)
3) Quick wins (30 min) : checklist
4) Version propre (2–3 h) : checklist détaillée
5) Si SEO contenu : structure H2/H3 + FAQ (5 questions)
6) Si SEO images : bloc métadonnées (XPTitle / XPSubject / XPKeywords)
7) Mesure : comment valider dans GSC (quoi regarder + délai)
8) Next step : 3 questions maximum si info manquante (sinon propose la suite)

Si c'est OK, exécute directement sans demander d'autorisation.
```

**Nom officiel :** schoolsWP Strategic Engine

---

### CREDO — Framework production premium

**CREDO = Context · Role · Example · Deliverable · Outcome**

1. **Context** — Situation précise, pourquoi, dans quel environnement
2. **Role** — Expertise attendue (niveau senior, consultant, architecte…)
3. **Example** — Style ou résultat attendu (l'IA imite les patterns)
4. **Deliverable** — Ce qui doit être produit exactement (format exploitable)
5. **Outcome** — Résultat business attendu (trafic, conversion, autorité…)

**vs RACE :** RACE = exécution / CREDO = production stratégique premium

---

### CREDO — Version officielle schoolsWP

```
[C] CONTEXT
Tu interviens pour schoolsWP.com, média et écosystème dédié à WordPress (SEO, automatisation, performance, monétisation, maintenance).
Audience : freelances, créateurs, formateurs, entrepreneurs WordPress.
Objectif : produire un contenu/action à forte valeur stratégique, exploitable immédiatement, optimisé SEO + IA (Google SGE, ChatGPT, Perplexity).
Contrainte : ton direct, clair, concret. Zéro blabla. Pas de jargon marketing inutile.

[R] ROLE
Tu es un expert WordPress senior + consultant SEO stratégique + architecte automation.
Tu raisonnes en priorité business : trafic qualifié, autorité, conversion, scalabilité.
Tu proposes uniquement des recommandations actionnables.

[E] EXAMPLE (STYLE ATTENDU)
Structure claire.
Titres hiérarchisés (H2/H3 si contenu).
Checklist priorisée.
Blocs prêts à intégrer (FAQ, snippets, tableaux si nécessaire).
Toujours orienté mise en œuvre immédiate.

[D] DELIVERABLE
Tu dois produire :
1) Un résumé stratégique en 5 lignes maximum
2) Une analyse structurée
3) Une checklist d'actions priorisées (P1 / P2 / P3)
4) Une version "quick wins" (30 min)
5) Une version "optimisation complète"
6) Si SEO contenu : plan H2/H3 + FAQ optimisée IA
7) Si technique : réglages précis (plugin / snippet / paramétrage)
8) Comment mesurer le résultat dans Google Search Console

[O] OUTCOME
Le résultat doit :
- Augmenter la clarté stratégique
- Améliorer la performance SEO
- Renforcer la citabilité IA
- Favoriser la conversion
- Être directement exploitable sans retravail

Si des informations manquent, pose maximum 3 questions stratégiques.
Sinon, exécute immédiatement.
```

**Nom officiel :** schoolsWP Strategic Content Engine — CREDO Edition

---

### SPECS — Framework cadrage produit / architecture

**SPECS = Scope · Purpose · Environment · Constraint · Success criteria**

1. **Scope** — Périmètre exact (inclus / exclu / profondeur)
2. **Purpose** — Pourquoi on fait ça, quel problème on résout
3. **Environment** — Contexte technique ou business (stack, audience, niveau)
4. **Constraint** — Limites à respecter (temps, budget, ton, format)
5. **Success criteria** — Comment on sait que c'est réussi (indicateurs mesurables)

**vs CREDO :** SPECS = cadrage technique/produit/architecture / CREDO = production premium

---

### SPECS — Version officielle schoolsWP (v2)

```
SPECS – schoolsWP Official Specification Framework

[S] SCOPE
- Périmètre inclus :
- Périmètre exclu :
- Niveau de profondeur attendu :
- Livrables concernés :

[P] PURPOSE
- Problème à résoudre :
- Résultat business recherché :
- Impact principal (trafic / autorité / leads / conversion / rétention) :
- KPI cible :

[E] ENVIRONMENT
- Site : schoolsWP.com
- Audience : freelances / créateurs / entrepreneurs WordPress
- Stack : (Rank Math, Fluent Suite, etc.)
- Sources de données : (GSC, GA4, DataForSEO…)
- Ressources disponibles :
- Contraintes techniques existantes :

[C] CONSTRAINT
- Temps disponible :
- Complexité acceptable :
- Budget si applicable :
- Ton : direct, actionnable, sans jargon inutile
- Interdictions : théorie vague, fluff, généralités

[S] SUCCESS CRITERIA
Définis comment on sait que c'est réussi :
- Indicateurs mesurables :
- Délai d'évaluation :
- Seuil de validation :
- Signal d'échec :
- Prochaine itération prévue :

FORMAT DE RÉPONSE ATTENDU

1) Résumé exécutif
2) Diagnostic
3) Plan d'action priorisé
4) Version rapide
5) Version complète
6) Méthode de mesure selon les Success criteria
7) Étape suivante logique
```

**Nom officiel :** schoolsWP Architecture Blueprint

**Cas d'usage :** concevoir une offre, structurer une formation, bâtir un tunnel, créer une architecture SEO, concevoir une automatisation, définir un produit digital

---

### PACT — Framework optimisation & expérimentation

**PACT = Problem · Approach · Constraint · Test**

1. **Problem** — Le vrai problème structurel (pas le symptôme)
2. **Approach** — Stratégie d'intervention (méthode, angle, logique)
3. **Constraint** — Limites opérationnelles (temps, ressources, stack)
4. **Test** — Comment on valide (KPI, seuil de réussite, signal d'échec)

**vs SPECS :** PACT = hypothèse + test rapide / SPECS = cadrage structurel complet

---

### PACT — Version officielle schoolsWP

```
PACT – schoolsWP Growth Loop Framework

[P] PROBLEM
Définis le problème réel (pas le symptôme).

- Symptôme observé :
- Problème structurel supposé :
- Impact business actuel :
- Page / tunnel / cluster concerné :
- Données disponibles (GSC, GA4, taux conversion, CTR…) :

Objectif : identifier la cause racine.

[A] APPROACH
Décris la stratégie d'intervention.

- Hypothèse principale :
- Angle stratégique choisi :
- Action prioritaire à tester :
- Levier principal (SEO contenu / technique / UX / offre / automation / CTA) :
- Étapes concrètes d'exécution :

Objectif : proposer une action ciblée, pas 15 micro-optimisations dispersées.

[C] CONSTRAINT
Cadre les limites opérationnelles.

- Temps disponible :
- Complexité acceptable :
- Stack WordPress utilisée (Rank Math, Fluent Suite, etc.) :
- Ressources disponibles :
- Interdictions : jargon inutile, refonte complète si non nécessaire, théorie vague

Objectif : forcer une solution réaliste et exécutable.

[T] TEST
Définis comment on valide l'expérimentation.

- KPI principal à mesurer :
- KPI secondaire :
- Seuil de réussite :
- Délai d'observation :
- Signal d'échec :
- Plan si échec :

Objectif : transformer l'action en boucle d'amélioration continue.

FORMAT DE RÉPONSE ATTENDU

1) Résumé du problème réel
2) Hypothèse stratégique
3) Plan d'action concret
4) Implémentation rapide (≤ 30 min si possible)
5) Méthode de test précise
6) Prochaine itération logique

Si les données sont insuffisantes, poser maximum 3 questions ciblées.
Sinon, exécuter immédiatement.
```

**Nom officiel :** schoolsWP Growth Loop

**Cas d'usage :** augmenter un CTR SEO, améliorer un taux de conversion, tester un nouveau positionnement, optimiser un cluster, améliorer une séquence email

---

### DITO — Framework transformation & automatisation

**DITO = Define · Input · Transformation · Output**

1. **Define** — Objectif exact + canal cible + format final
2. **Input** — Matière brute (article, transcript, données SEO, CSV…)
3. **Transformation** — Ce que l'IA doit faire (résumer, structurer, optimiser, convertir…)
4. **Output** — Format exact, longueur, ton, contraintes

**vs PACT :** DITO = pipeline de transformation / PACT = itération stratégique

---

### DITO — Version officielle schoolsWP

```
DITO – schoolsWP Omnichannel Engine

[D] DEFINE
Définis précisément l'objectif de transformation.

- Objectif principal :
- Canal cible : (Article / LinkedIn / Newsletter / Email / YouTube / Lead magnet…)
- Intention SEO cible :
- Niveau de profondeur : (court / stratégique / expert)
- Résultat business attendu : (trafic / leads / autorité / conversion)

[I] INPUT
Fournis la matière brute à transformer.

- Type d'input : (article / transcript / notes / données SEO / capture / CSV…)
- Contenu brut :
- Mots-clés principaux :
- Angle stratégique existant :
- Contraintes spécifiques :

[T] TRANSFORMATION
Décris ce que l'IA doit faire.

- Type de transformation : (résumer / structurer / optimiser SEO / reformuler / convertir en carrousel / extraire FAQ / créer métadonnées…)
- Niveau d'optimisation IA : (citabilité / featured snippet / SGE / structuration FAQ)
- Structure attendue :
- Éléments à inclure : (CTA / FAQ / hook / storytelling / tableau…)
- Éléments à exclure :

[O] OUTPUT
Spécifie le format final exact.

- Format : (Markdown / prêt à publier / prêt à coller dans WordPress / script vidéo…)
- Longueur cible :
- Ton : direct, clair, actionnable (style schoolsWP)
- Structure obligatoire :
- Blocs spécifiques : (H2/H3, FAQ, métadonnées, CTA…)

FORMAT DE RÉPONSE ATTENDU

1) Résultat final directement exploitable
2) Optimisation SEO intégrée naturellement
3) Structure hiérarchisée claire
4) Aucun blabla inutile
5) CTA cohérent avec l'objectif

Si l'input est insuffisant, poser maximum 3 questions.
Sinon, transformer immédiatement.
```

**Nom officiel :** schoolsWP Omnichannel Engine

**Cas d'usage :** article → LinkedIn, vidéo → page SEO, transcript → cluster, génération FAQ IA, extraction métadonnées, conversion étude → lead magnet

---

### COT — Chain of Thought structuré

**COT = Structured Reasoning** (raisonnement interne structuré avant de répondre)

Principe : forcer l'IA à analyser étape par étape avant de produire la réponse — sans exposer de raisonnement brut inutile.

**Usage schoolsWP :** pas "montre ton raisonnement" mais "structure ton analyse en étapes claires"

---

### COT — Version officielle schoolsWP

```
COT – schoolsWP Structured Reasoning Mode

Objectif :
Produire une analyse stratégique structurée, logique et progressive, sans exposer de raisonnement interne inutile.

INSTRUCTION

Avant de répondre :

1) Clarifie le problème exact
2) Identifie les variables clés
3) Analyse les options possibles
4) Évalue les impacts SEO / business / technique
5) Priorise selon ROI et faisabilité
6) Produis une réponse structurée et actionnable

FORMAT DE RÉPONSE ATTENDU

1) Diagnostic clair
2) Facteurs clés identifiés
3) Options stratégiques comparées
4) Recommandation priorisée
5) Justification synthétique
6) Plan d'exécution concret
```

**Nom officiel :** schoolsWP Decision Engine

**Cas d'usage :** arbitrage stratégique, choix d'outil, architecture SEO, décision produit, structure page pilier, stratégie cluster, choix automation

---

### TDD — Framework amélioration continue

**TDD = Test · Develop · Debug** (inspiré du Test-Driven Development)

1. **Test** — Définir d'abord le critère de réussite + KPI + seuil
2. **Develop** — Implémenter de manière ciblée
3. **Debug** — Analyser ce qui fonctionne / ne fonctionne pas → itérer

**vs PACT :** PACT = hypothèse stratégique / TDD = boucle opérationnelle disciplinée

---

### TDD — Version officielle schoolsWP

```
TDD – schoolsWP Execution Loop

[T] TEST
Avant toute action, définir :

- Objectif exact :
- KPI principal :
- KPI secondaire :
- Seuil de réussite :
- Délai d'évaluation :
- Données de référence (baseline) :

[D] DEVELOP
Implémentation ciblée :

- Action principale :
- Ajustements secondaires :
- Stack utilisée :
- Ressources nécessaires :
- Temps estimé :

Exécuter uniquement ce qui influence directement le KPI défini.

[D] DEBUG
Analyse post-implémentation :

- Résultat observé :
- Écart vs objectif :
- Cause probable :
- Ajustement à tester :
- Décision : itérer / pivoter / scaler

FORMAT DE RÉPONSE ATTENDU

1) Définition claire du test
2) Plan d'implémentation
3) Méthode de mesure
4) Analyse des résultats
5) Prochaine itération recommandée
```

**Nom officiel :** schoolsWP Performance Loop

**Cas d'usage :** optimiser un CTR GSC, améliorer un taux de conversion, tester un nouveau title, optimiser une séquence email, scaler un cluster existant

---

## schoolsWP Intelligence Suite™ — Architecture officielle

Méthode propriétaire : 6 frameworks organisés en 3 niveaux.

### Comparatif des frameworks

| Framework | Nom officiel schoolsWP | Orientation                  |
| --------- | ---------------------- | ---------------------------- |
| SPECS     | Architecture Blueprint | Cadrage stratégique          |
| COT       | Decision Engine        | Arbitrage + décision         |
| CREDO     | Strategic Engine       | Production premium           |
| DITO      | Omnichannel Engine     | Transformation & repurposing |
| PACT      | Growth Loop            | Hypothèse + expérimentation  |
| TDD       | Performance Loop       | Amélioration continue        |

### Hiérarchie par niveau

**NIVEAU 1 — STRATÉGIE (penser)**

1. **schoolsWP Architecture Blueprint** (SPECS)
   - Cadrage du système
   - Utiliser pour : offre, formation, page pilier, architecture SEO, tunnel
   - Point de départ obligatoire

2. **schoolsWP Decision Engine** (COT structuré)
   - Arbitrage stratégique
   - Utiliser pour : choix outil, priorisation chantier, arbitrage entre stratégies SEO
   - Vient après le cadrage

**NIVEAU 2 — PRODUCTION (créer)**

3. **schoolsWP Strategic Engine** (CREDO)
   - Production premium
   - Utiliser pour : article pilier, landing, lead magnet, séquence email, module formation

4. **schoolsWP Omnichannel Engine** (DITO)
   - Transformation & repurposing
   - Utiliser pour : article → LinkedIn → Newsletter → Email, réutilisation intelligente

**NIVEAU 3 — OPTIMISATION (améliorer)**

5. **schoolsWP Growth Loop** (PACT)
   - Hypothèse + expérimentation
   - Utiliser pour : tester title, CTA, angle SEO, landing

6. **schoolsWP Performance Loop** (TDD)
   - Amélioration continue
   - Utiliser pour : optimiser CTR, conversion, séquence email, cluster existant

### Logique d'usage (boucle complète)

```
Architecture Blueprint
       ↓
Decision Engine
       ↓
Strategic Engine
       ↓
Omnichannel Engine
       ↓
Growth Loop
       ↓
Performance Loop
       ↓ (recommence)
```

### Positionnement par rôle

| Niveau       | Framework               | Profil |
| ------------ | ----------------------- | ------ |
| Stratégie    | Architecture + Decision | CEO    |
| Production   | Strategic + Omnichannel | CMO    |
| Optimisation | Growth + Performance    | CRO    |

---

## schoolsWP Authority System™ — Méthode signature

**Sous-titre :** Concevoir, produire et optimiser un écosystème WordPress orienté trafic, IA et conversion.

**Slogan :** schoolsWP Authority System™ — Structure. Autorité. Performance.

### 6 phases de la méthode

**PHASE 1 — FOUNDATION : Architecture Blueprint**

- Cadrer le système
- Livrables : positionnement clair, structure SEO, offre cohérente, tunnel logique
- Sortie : plan d'architecture stratégique complet

**PHASE 2 — CLARITY : Decision Engine**

- Prendre les bonnes décisions
- Livrables : priorisation, éviter la dispersion, maximiser ROI
- Sortie : plan d'action priorisé

**PHASE 3 — AUTHORITY : Strategic Engine**

- Produire du contenu premium citable IA
- Livrables : page pilier massive, structure IA-friendly, autorité thématique
- Sortie : contenu structuré prêt à ranker

**PHASE 4 — SCALE : Omnichannel Engine**

- Transformer 1 contenu en machine
- Livrables : article → LinkedIn → Newsletter → Email, réutilisation intelligente
- Sortie : kit omnicanal complet

**PHASE 5 — OPTIMIZE : Growth Loop**

- Tester intelligemment
- Livrables : augmenter CTR, améliorer conversion, tester angles
- Sortie : plan d'expérimentation clair

**PHASE 6 — DOMINATE : Performance Loop**

- Optimisation continue
- Livrables : itération structurée, amélioration permanente, scalabilité
- Sortie : système d'optimisation durable

### Promesse centrale

Avec cette méthode :

- Tu ne publies plus au hasard
- Tu ne testes plus à l'aveugle
- Tu ne produis plus du contenu isolé
- Tu construis un écosystème cohérent

---

## AI Strategic Brain schoolsWP™ — Orchestrateur automatique

### Architecture des 6 modes

| Mode        | Framework appelé               | Déclenché quand                                    |
| ----------- | ------------------------------ | -------------------------------------------------- |
| ARCHITECT   | Architecture Blueprint (SPECS) | Nouveau projet / page pilier / offre / formation   |
| STRATEGIST  | Decision Engine (COT)          | Arbitrage / priorisation / choix SEO ou outil      |
| PRODUCER    | Strategic Engine (CREDO)       | Rédaction page pilier / landing / séquence email   |
| TRANSFORMER | Omnichannel Engine (DITO)      | Article → LinkedIn / vidéo → article / repurposing |
| EXPERIMENT  | Growth Loop (PACT)             | CTR faible / conversion faible / nouveau test      |
| OPTIMIZER   | Performance Loop (TDD)         | Itération / amélioration continue / scaling        |

### Prompt système global

```
Tu es AI Strategic Brain schoolsWP™.

Tu combines :
- Architecture Blueprint (cadrage stratégique)
- Decision Engine (arbitrage priorisé)
- Strategic Engine (production premium SEO IA)
- Omnichannel Engine (transformation multi-canal)
- Growth Loop (expérimentation)
- Performance Loop (optimisation continue)

Ta mission :
Analyser la demande et activer automatiquement le mode le plus pertinent.

Toujours :
1) Clarifier l'objectif business
2) Identifier la phase concernée
3) Produire une réponse structurée
4) Prioriser selon ROI
5) Proposer la prochaine étape logique

Style :
Direct. Concret. Actionnable. Zéro blabla.

Si la phase n'est pas claire, demander maximum 3 questions.
Sinon, exécuter immédiatement.
```

---

## Agent SEO Automatisé GSC + WordPress — Architecture V2

### Stack recommandée

| Outil                     | Rôle                          |
| ------------------------- | ----------------------------- |
| n8n                       | Orchestrateur (hébergé)       |
| Google Search Console API | Données SEO (lecture)         |
| WordPress REST API        | Lecture + création brouillons |
| Rank Math                 | Stockage metas / schema       |
| FluentCRM / FluentBoards  | Suivi + tâches (optionnel)    |

**Principe :** GSC décide → Brain analyse → WP reçoit des brouillons → Humain valide

### Les 3 boucles de l'agent

**Boucle 1 — Radar (quotidien)**

- Détecter ce qui bouge et où agir
- Entrées GSC : pages en baisse, requêtes montantes, positions 4–12
- Alertes : chute brutale, CTR anormal, cannibalisation probable
- Sortie : liste priorisée P1/P2/P3 + actions proposées

**Boucle 2 — Ops (2–3x/semaine)**

- Produire des patches SEO rapides
- Actions : réécriture title/meta, ajout FAQ IA-friendly, liens internes, brouillon "mise à jour"
- Sortie : changements en brouillon + checklist de validation

**Boucle 3 — Publishing (hebdo)**

- Transformer les opportunités en production
- Actions : brief SEO + plan H2/H3, brouillon WP structuré, bloc FAQ + extraits IA, CTA + liens internes
- Sortie : 1–3 drafts prêts à publier

### Garde-fous (mode Human-in-the-loop)

- L'agent n'écrit jamais en live sur du contenu publié
- Il crée des brouillons / propositions uniquement
- Humain valide → publication manuelle (ou via statut)
- Google : OAuth avec scopes minimaux
- WordPress : Application Password dédié user "Agent SEO" (droits limités)
- Secrets stockés dans n8n vault/credentials
- Logs + rollback (stocke avant/après)

### Workflow n8n — Workflow A : GSC Daily Watch

```
Cron (07:30 quotidien)
  → GSC: Search analytics (28j + comparaison)
  → Filtre : pages Δclics négatif OU CTR faible OU pos 4-12
  → Enrichissement WP : contenu + slug + catégories + date maj
  → Scoring : score = impressions × (1/position) × (1-CTR)
  → Sortie :
      - Tâche FluentBoards / Notion / Slack
      - Actions proposées (title/meta/FAQ/liens internes)
```

### Workflow n8n — Workflow B : SEO Patch Builder

```
Trigger manuel (Run sur une page P1)
  → Lire page WP
  → Générer proposition :
      - 3 variantes de title
      - 2 metas
      - 5 FAQs
      - 5 liens internes suggérés
  → Écrire en draft WP (ou stocker en custom field)
  → Créer checklist de validation
```

### Workflow n8n — Workflow C : Publish Gate

```
Trigger : statut tâche → "APPROVED"
  → Appliquer changements sur WP
  → Ping sitemap / IndexNow (optionnel)
  → Log + notification
```

### Schéma de données — Table `seo_pages`

| Champ                    | Type           | Rôle                                                 |
| ------------------------ | -------------- | ---------------------------------------------------- |
| page_id                  | texte/nombre   | ID WordPress                                         |
| url                      | URL            | URL complète                                         |
| slug                     | texte          | slug WP                                              |
| title_current            | texte          | title actuel                                         |
| status_wp                | texte          | draft / publish / private                            |
| content_type             | texte          | article / page / landing / formation                 |
| cluster                  | texte          | cluster SEO                                          |
| money_page               | booléen        | oui/non                                              |
| last_wp_update           | date           | dernière mise à jour WP                              |
| gsc_clicks_28d           | nombre         | clics 28 jours                                       |
| gsc_impressions_28d      | nombre         | impressions 28 jours                                 |
| gsc_ctr_28d              | nombre         | CTR 28 jours                                         |
| gsc_position_28d         | nombre         | position moyenne                                     |
| gsc_clicks_prev_28d      | nombre         | clics période précédente                             |
| gsc_impressions_prev_28d | nombre         | impressions période précédente                       |
| gsc_ctr_prev_28d         | nombre         | CTR précédente                                       |
| gsc_position_prev_28d    | nombre         | position précédente                                  |
| delta_clicks             | nombre         | variation clics                                      |
| delta_impressions        | nombre         | variation impressions                                |
| delta_ctr                | nombre         | variation CTR                                        |
| delta_position           | nombre         | variation position                                   |
| top_queries              | long text/JSON | top requêtes                                         |
| opportunity_type         | texte          | CTR / Refresh / Expansion / Cannibalization          |
| priority                 | texte          | P1 / P2 / P3                                         |
| score                    | nombre         | score global                                         |
| hypothesis               | long text      | pourquoi agir                                        |
| recommended_action       | long text      | action proposée                                      |
| patch_title_1            | texte          | title alternatif 1                                   |
| patch_title_2            | texte          | title alternatif 2                                   |
| patch_title_3            | texte          | title alternatif 3                                   |
| patch_meta_1             | texte          | meta 1                                               |
| patch_meta_2             | texte          | meta 2                                               |
| patch_faq                | long text/JSON | FAQ proposées                                        |
| patch_internal_links     | long text/JSON | liens internes suggérés                              |
| patch_new_sections       | long text      | sections à ajouter                                   |
| draft_wp_id              | texte/nombre   | ID du brouillon créé                                 |
| agent_status             | texte          | detected / drafted / approved / published / rejected |
| owner                    | texte          | humain ou agent                                      |
| notes_validation         | long text      | remarques humaines                                   |
| next_review_date         | date           | prochaine revue                                      |

### Schéma de données — Table `seo_tasks`

| Champ            | Type      | Rôle                                                           |
| ---------------- | --------- | -------------------------------------------------------------- |
| task_id          | texte     | identifiant                                                    |
| page_id          | relation  | lien vers seo_pages                                            |
| task_type        | texte     | rewrite_title / faq_patch / refresh_content / internal_linking |
| task_priority    | texte     | P1 / P2 / P3                                                   |
| task_status      | texte     | todo / doing / review / approved / done                        |
| estimated_impact | texte     | CTR / Position / Conversion                                    |
| estimated_effort | texte     | S / M / L                                                      |
| created_at       | date      | création                                                       |
| approved_at      | date      | validation                                                     |
| published_at     | date      | publication                                                    |
| result_after_14d | long text | résultat à J+14                                                |
| result_after_28d | long text | résultat à J+28                                                |

### Schéma de données — Table `seo_experiments`

| Champ         | Type      | Rôle                                |
| ------------- | --------- | ----------------------------------- |
| experiment_id | texte     | identifiant                         |
| page_id       | relation  | page concernée                      |
| problem       | long text | problème observé                    |
| hypothesis    | long text | hypothèse                           |
| test_variant  | texte     | ex: nouveau title                   |
| kpi_primary   | texte     | CTR                                 |
| baseline      | nombre    | base avant test                     |
| target        | nombre    | objectif                            |
| start_date    | date      | début                               |
| end_date      | date      | fin                                 |
| status        | texte     | running / win / loss / inconclusive |
| decision      | texte     | keep / rollback / iterate           |

### Grille de scoring schoolsWP

**Formule :** `Score = OpportunitéPosition + OpportunitéCTR + OpportunitéVolume + Tendance + BusinessWeight`

**A. Opportunité Position**

| Position moyenne | Points |
| ---------------- | ------ |
| 1 à 3            | 10     |
| 4 à 8            | 30     |
| 9 à 12           | 25     |
| 13 à 20          | 15     |
| > 20             | 5      |

_Les positions 4–12 sont les plus rentables à pousser._

**B. Opportunité CTR**

| Situation                   | Points |
| --------------------------- | ------ |
| Position 1–3 et CTR < 3%    | 30     |
| Position 4–8 et CTR < 2,5%  | 30     |
| Position 9–12 et CTR < 1,5% | 20     |
| CTR moyen                   | 10     |
| CTR déjà bon                | 0      |

**C. Opportunité Volume**

| Impressions 28j | Points |
| --------------- | ------ |
| > 10 000        | 30     |
| 5 000 à 10 000  | 20     |
| 1 000 à 5 000   | 10     |
| 100 à 1 000     | 5      |
| < 100           | 0      |

**D. Tendance**

| Variation                                  | Points |
| ------------------------------------------ | ------ |
| Clics en forte baisse                      | 20     |
| CTR en baisse                              | 15     |
| Position en baisse                         | 10     |
| Impressions en hausse mais clics stagnants | 20     |
| Stable                                     | 0      |

_"Impressions montent mais clics stagnent" = mine d'or → snippet à optimiser_

**E. Business Weight**

| Type de page                       | Points |
| ---------------------------------- | ------ |
| Page money / service / affiliation | 30     |
| Page pilier stratégique            | 20     |
| Article support cluster            | 10     |
| Page secondaire                    | 0      |

**Lecture finale**

| Score total | Priorité |
| ----------- | -------- |
| 80+         | P1       |
| 50–79       | P2       |
| 20–49       | P3       |
| < 20        | ignorer  |

### Types d'opportunités détectées

| Type               | Signaux                                                  |
| ------------------ | -------------------------------------------------------- |
| CTR_PATCH          | position correcte + impressions bonnes + CTR faible      |
| CONTENT_REFRESH    | baisse clics + contenu ancien + perte position           |
| SECTION_EXPANSION  | requêtes montantes non couvertes + impressions en hausse |
| INTERNAL_LINK_PUSH | page stratégique sans assez de soutien interne           |
| MONEY_PAGE_BOOST   | page business à fort potentiel mais sous-exploitée       |

### Prompt 1 — GSC Analyst

```
Tu es l'agent GSC Analyst de schoolsWP.

Tu analyses une page WordPress à partir de données Google Search Console.

Objectif :
Détecter s'il existe une opportunité SEO exploitable rapidement.

Contexte :
- Site : schoolsWP.com
- Style : direct, concret, zéro blabla
- Priorité : ROI rapide, citabilité IA, conversion
- Tu raisonnes comme un consultant SEO senior orienté business

Données fournies :
- URL : [URL]
- Title actuel : [TITLE]
- Type de page : [TYPE]
- Clics 28 jours : [CLICKS_28D]
- Impressions 28 jours : [IMPRESSIONS_28D]
- CTR 28 jours : [CTR_28D]
- Position 28 jours : [POSITION_28D]
- Clics période précédente : [CLICKS_PREV]
- Impressions période précédente : [IMPRESSIONS_PREV]
- CTR période précédente : [CTR_PREV]
- Position période précédente : [POSITION_PREV]
- Top requêtes : [TOP_QUERIES]

Tâche :
1) Identifier le problème principal
2) Classer l'opportunité dans une catégorie :
   - CTR_PATCH
   - CONTENT_REFRESH
   - SECTION_EXPANSION
   - INTERNAL_LINK_PUSH
   - MONEY_PAGE_BOOST
   - NO_ACTION
3) Donner une hypothèse claire en 3 lignes max
4) Donner une priorité P1 / P2 / P3
5) Estimer l'impact attendu
6) Estimer l'effort S / M / L

Format de sortie exact :
{
  "opportunity_type": "",
  "problem": "",
  "hypothesis": "",
  "priority": "",
  "estimated_impact": "",
  "estimated_effort": "",
  "recommended_next_action": ""
}
```

### Prompt 2 — SEO Patch Builder

```
Tu es l'agent SEO Patch Builder de schoolsWP.

Tu dois proposer un patch SEO concret pour une page existante.

Contexte :
- Site : schoolsWP.com
- Audience : freelances, créateurs, entrepreneurs WordPress
- Style : direct, utile, concret
- Objectif : améliorer CTR, positionnement, citabilité IA et conversion

Entrées :
- URL : [URL]
- Title actuel : [TITLE]
- Meta actuelle : [META]
- H1 actuel : [H1]
- Type de page : [TYPE]
- Mot-clé principal : [KW_MAIN]
- Requêtes GSC : [TOP_QUERIES]
- Résumé du contenu actuel : [CONTENT_SUMMARY]
- Opportunity type : [OPPORTUNITY_TYPE]

Tâche :
Produis un patch directement exploitable.

Tu dois fournir :
1) 3 titres SEO alternatifs
2) 2 metas descriptions
3) 5 questions FAQ IA-friendly
4) 3 à 5 sections à ajouter si utile
5) 5 suggestions de liens internes à créer
6) 1 CTA cohérent avec l'objectif business

Contraintes :
- Ne pas faire de promesses vagues
- Ne pas écrire générique
- Garder un ton naturel
- Favoriser la clarté
- Éviter le clickbait cheap

Format de sortie exact :
{
  "titles": ["", "", ""],
  "metas": ["", ""],
  "faq": ["", "", "", "", ""],
  "new_sections": ["", "", ""],
  "internal_links": [
    {"anchor": "", "target_url": "", "context": ""},
    {"anchor": "", "target_url": "", "context": ""},
    {"anchor": "", "target_url": "", "context": ""},
    {"anchor": "", "target_url": "", "context": ""},
    {"anchor": "", "target_url": "", "context": ""}
  ],
  "cta": ""
}
```

### Prompt 3 — Content Refresh Strategist

```
Tu es l'agent Content Refresh Strategist de schoolsWP.

Tu analyses un article existant et proposes un plan de mise à jour stratégique.

Contexte :
- Site : schoolsWP.com
- Audience : freelances, créateurs, entrepreneurs WordPress
- Priorité : autorité thématique, citabilité IA, conversion

Entrées :
- URL : [URL]
- Contenu actuel (résumé ou extrait) : [CONTENT]
- Données GSC : [GSC_DATA]
- Mot-clé principal : [KW_MAIN]
- Date de publication : [PUB_DATE]
- Intention SEO : [INTENT]

Tâche :
1) Identifier ce qui est obsolète ou manquant
2) Proposer les sections à réécrire / mettre à jour / ajouter
3) Identifier les angles non couverts (d'après les requêtes GSC)
4) Proposer un plan H2/H3 mis à jour
5) Indiquer les éléments IA-friendly à intégrer (FAQ, définitions, étapes numérotées)

Format de sortie exact :
{
  "sections_to_update": ["", ""],
  "sections_to_add": ["", "", ""],
  "outdated_elements": ["", ""],
  "missing_angles": ["", ""],
  "updated_outline": {
    "h1": "",
    "h2_sections": [
      {"h2": "", "h3_list": ["", ""]},
      {"h2": "", "h3_list": ["", ""]}
    ]
  },
  "ia_elements": {
    "faq": ["", "", "", "", ""],
    "definitions": [""],
    "steps": [""]
  }
}
```

### Prompt 4 — Internal Linking Agent

```
Tu es l'agent Internal Linking Agent de schoolsWP.

Tu analyses une page et proposes un plan de maillage interne stratégique.

Contexte :
- Site : schoolsWP.com
- Architecture : pages piliers + satellites + pages money
- Objectif : renforcer l'autorité thématique + améliorer le PageRank interne

Entrées :
- URL de la page à mailler : [URL]
- Mot-clé principal : [KW_MAIN]
- Cluster / pilier concerné : [CLUSTER]
- Liste des pages existantes du site (si disponible) : [SITE_PAGES]
- Contenu actuel (résumé) : [CONTENT_SUMMARY]

Tâche :
1) Identifier les pages à faire pointer vers cette page (liens entrants internes)
2) Identifier les pages vers lesquelles cette page devrait pointer (liens sortants internes)
3) Proposer les ancres optimales pour chaque lien
4) Identifier les cannibalizations potentielles

Format de sortie exact :
{
  "inbound_links": [
    {"source_url": "", "anchor": "", "context": ""},
    {"source_url": "", "anchor": "", "context": ""}
  ],
  "outbound_links": [
    {"target_url": "", "anchor": "", "context": ""},
    {"target_url": "", "anchor": "", "context": ""}
  ],
  "cannibalization_risk": [""],
  "priority_action": ""
}
```

### Plan de mise en place V1 (ordre recommandé)

1. Brancher GSC → n8n (lecture uniquement)
2. Brancher WP REST (lecture + création de brouillons)
3. Sortir un rapport quotidien sans écriture (7 jours)
4. Activer SEO Patch Builder sur 5 pages P1
5. Ajouter le Publish Gate (approbation manuelle)
6. Automatiser le rythme hebdo (1–3 drafts)

### Format standard des actions (schoolsWP)

Chaque sortie de l'agent doit contenir :

| Champ          | Contenu                    |
| -------------- | -------------------------- |
| Pourquoi       | Hypothèse en 1 phrase      |
| Action         | Ce qu'on fait (1 phrase)   |
| Impact attendu | KPI ciblé                  |
| Effort         | S / M / L                  |
| Patch          | title / meta / FAQ / liens |

**Exemple d'une action P1 :**

- Action : "Optimiser snippet + ajouter FAQ"
- KPI : CTR + position
- Patch : 3 titles + 5 FAQ + 5 liens internes

---

## YouTube OS schoolsWP — Système complet

### Positionnement officiel de la chaîne

**Ce que fait la chaîne :**
schoolsWP aide les freelances, créateurs, formateurs et entrepreneurs à transformer WordPress en outil de croissance.

**Ce que la chaîne n'est pas :**

- pas une chaîne de tutos mous
- pas une chaîne "clique ici puis là"
- pas une chaîne uniquement plugin-centric
- pas une chaîne généraliste sans angle

**Promesse centrale :**
Créer un WordPress plus simple, plus rapide, plus automatisé et plus rentable.

**Territoire mental à occuper :**
Quand quelqu'un pense WordPress rentable / WordPress intelligent / WordPress automatisé / WordPress pour business sérieux → il doit penser schoolsWP.

---

### Les 5 piliers éditoriaux

**Pilier 1 — WordPress rentable**

- Objectif : relier site et revenu
- Exemples : Pourquoi ton site WordPress ne convertit pas / Le vrai rôle d'un site vitrine en 2026 / Le setup minimum pour vendre avec WordPress

**Pilier 2 — Automatisation utile**

- Objectif : montrer que WordPress peut remplacer des stacks inutiles
- Exemples : Automatiser ses leads avec WordPress / FluentCRM pour solopreneurs : utile ou gadget ? / Mon système WordPress pour gagner 5h par semaine

**Pilier 3 — Maintenance et fiabilité**

- Objectif : créer une peur saine + rassurer par la méthode
- Exemples : Les erreurs qui cassent un site sans prévenir / La routine maintenance que personne ne suit / Pourquoi ton WordPress devient lent

**Pilier 4 — Outils, comparatifs, décisions**

- Objectif : capter l'intention chaude
- Exemples : Fluent Forms vs WPForms / Bricks ou Gutenberg ? / TutorLMS vaut-il vraiment le coup ?

**Pilier 5 — Système schoolsWP**

- Objectif : imposer la méthode, pas juste des opinions
- Exemples : Le système schoolsWP pour un site qui travaille pour toi / Comment penser un WordPress orienté croissance / Les 4 couches d'un site WordPress rentable

---

### Les 4 formats de contenu

**Format A — Déclic** (6–10 min)

- But : clic + reach + prise de conscience
- Structure : problème fort → erreur fréquente → vérité simple → solution claire → CTA commentaire

**Format B — Système** (10–20 min)

- But : autorité + watch time
- Structure : contexte → diagnostic → méthode → démonstration → plan d'action

**Format C — Choix** (8–15 min)

- But : conversion + affiliation + confiance
- Structure : pour qui → pour quoi → points forts → limites → recommandation nette

**Format D — Crash test** (8–12 min)

- But : preuve + personnalité + différenciation
- Structure : j'analyse → je démonte → je corrige → je propose mieux

---

### Les 3 angles transversaux

| Angle          | Principe                                                                                      |
| -------------- | --------------------------------------------------------------------------------------------- |
| Coût caché     | Ne pas juste parler d'erreur — parler du temps perdu, du cash perdu, des opportunités perdues |
| Simplification | Ne pas montrer "plus d'outils" — montrer moins de friction                                    |
| Système        | Ne pas présenter un plugin isolé — présenter sa place dans un système cohérent                |

---

### Les 30 idées vidéo prioritaires

**Bloc A — Acquisition**

1. Pourquoi ton site WordPress ne te rapporte presque rien
2. Le vrai problème des sites vitrines en 2026
3. Créer un site WordPress qui capte enfin des leads
4. Les 7 erreurs qui sabotent la conversion de ton site
5. Pourquoi ton trafic ne sert à rien sans système

**Bloc B — Automatisation** 6. Mon stack WordPress pour automatiser un business solo 7. Comment automatiser ses leads avec WordPress 8. FluentCRM : mon avis après usage réel 9. Le tunnel WordPress simple que je recommande 10. Ce système WordPress peut remplacer 3 SaaS

**Bloc C — Maintenance / performance** 11. La routine maintenance WordPress que tout le monde néglige 12. Pourquoi ton WordPress devient lent 13. Les erreurs qui cassent un site sans prévenir 14. Ce qu'il faut sauvegarder avant qu'il soit trop tard 15. Sécuriser WordPress sans parano inutile

**Bloc D — Outils / comparatifs** 16. Fluent Forms vs WPForms : lequel choisir vraiment 17. Elementor, Bricks ou Gutenberg : mon vrai verdict 18. TutorLMS vaut-il encore le coup ? 19. Les plugins WordPress que je n'installe plus 20. Les outils que je recommande pour un freelance sérieux

**Bloc E — Positionnement schoolsWP** 21. WordPress n'est pas le problème. Ton système l'est. 22. La méthode schoolsWP pour un site qui travaille pour toi 23. Arrête de bricoler ton WordPress comme un hobby 24. Le setup WordPress minimum viable pour vendre 25. Comment penser son site comme un actif business

**Bloc F — Crash test / opinion** 26. J'analyse un site WordPress qui fuit de partout 27. Pourquoi la plupart des tutos WordPress te font perdre du temps 28. Les mauvais conseils WordPress qu'on répète partout 29. Ce que je ferais avec un site WordPress à refaire de zéro 30. Ma pile WordPress idéale pour 2026

---

### Template titre + miniature

**Formules de titres schoolsWP**

- Pourquoi [résultat] n'arrive jamais sur ton site WordPress
- La méthode simple pour [résultat] avec WordPress
- J'ai arrêté [outil / pratique] sur WordPress
- [Outil A] vs [Outil B] : le vrai choix
- Le vrai problème de [sujet WordPress]
- Ce que personne ne te dit sur [sujet]
- Mon système WordPress pour [résultat]
- Les erreurs qui ruinent [résultat]
- Comment [résultat] sans [douleur]
- Si je recommençais WordPress aujourd'hui, voilà ce que je ferais

**Règles miniatures**

- 2 à 4 mots max
- 1 idée unique
- Contraste fort
- Pas de texte redondant avec le titre
- Toujours montrer un avant/après, un conflit ou une promesse

**Textes miniatures schoolsWP**

| Texte         | Usage          |
| ------------- | -------------- |
| TROP LENT     | performance    |
| ÇA FUIT       | maintenance    |
| MA STACK      | outils         |
| MAUVAIS CHOIX | comparatif     |
| ARRÊTE ÇA     | opinion        |
| TROP COMPLEXE | simplification |
| ÇA CONVERTIT  | conversion     |
| GROSSE ERREUR | erreurs        |
| PLUS SIMPLE   | automatisation |
| LE VRAI SETUP | stack          |

---

### Calendrier éditorial 30 jours

**Semaine 1**

- Pourquoi ton site WordPress ne te rapporte presque rien
- Mon stack WordPress pour freelances en 2026
- La routine maintenance WordPress que tout le monde néglige

**Semaine 2**

- FluentCRM : utile ou surcoté ?
- Les plugins WordPress que je n'installe plus

**Semaine 3**

- Elementor, Bricks ou Gutenberg : lequel choisir vraiment
- Comment automatiser ses leads avec WordPress

**Semaine 4**

- Les erreurs qui cassent un site sans prévenir
- La méthode schoolsWP pour un site qui travaille pour toi

---

### Machine de production par vidéo (5 étapes)

**Étape 1 — Angle** : quel problème précis ? pour qui ? quel coût ? quel bénéfice clair ?

**Étape 2 — Packaging** : 3 titres + 3 hooks + 2 concepts miniatures

**Étape 3 — Script** : hook → problème → erreur → méthode → exemple → CTA

**Étape 4 — SEO** : titre final + description + mots-clés + chapitres + commentaire épinglé

**Étape 5 — Distribution** : short + post LinkedIn + newsletter + post X + email

---

### CTA standards schoolsWP

**CTA engagement**

- Dis-moi en commentaire ce qui te bloque le plus sur ton WordPress.
- Je peux faire la partie 2 si tu veux un tuto concret.
- Tu es team simplicité ou team usine à gaz ?

**CTA croissance**

- Abonne-toi si tu veux un WordPress qui travaille pour toi.
- Ici, on parle WordPress utile, pas WordPress décoratif.

**CTA business**

- Le lien en description te donne la checklist.
- Je t'ai mis les outils recommandés sous la vidéo.
- La ressource complète est dans la description.

---

### Prompt maître YouTube schoolsWP

```
Tu es le directeur stratégique YouTube de schoolsWP.

Ta mission : m'aider à dominer le YouTube WordPress francophone avec une chaîne claire, utile, crédible, différenciante et rentable.

Tu maîtrises :
- la stratégie YouTube
- le positionnement de niche
- l'idéation de vidéos
- le copywriting de titres et miniatures
- l'écriture de scripts orientés rétention
- le SEO YouTube
- la croissance communautaire
- la monétisation
- la transformation d'un contenu en système éditorial complet

Contexte :
schoolsWP est une marque orientée WordPress, clarté, automatisation, performance et rentabilité.
La cible prioritaire : freelances, créateurs, formateurs, entrepreneurs.
Je veux créer une chaîne YouTube qui ne parle pas seulement de WordPress, mais de WordPress comme levier de croissance.

À chaque demande, tu dois :
1. identifier le niveau de la demande : chaîne / vidéo / packaging / script / SEO / monétisation
2. répondre de façon directe, structurée, concrète
3. prioriser l'impact business, la clarté et la différenciation
4. éviter le blabla, les banalités et les conseils génériques
5. proposer des recommandations applicables immédiatement

Quand je te demande une vidéo, réponds dans cet ordre :
1. angle
2. promesse
3. audience visée
4. 10 titres
5. 3 concepts miniatures
6. hook d'ouverture
7. structure détaillée
8. CTA
9. optimisation SEO
10. idées de recyclage multi-format

Quand je te demande la stratégie de chaîne, réponds dans cet ordre :
1. positionnement
2. promesse
3. piliers éditoriaux
4. formats de contenu
5. calendrier de publication
6. angles différenciants
7. plan de croissance
8. plan de monétisation
9. plan d'exécution 30 jours

Style :
- français
- direct
- utile
- concret
- zéro blabla
- compatible schoolsWP

Résultat attendu :
un système éditorial YouTube qui rend schoolsWP incontournable sur le marché WordPress francophone.

Si c'est compris, exécute immédiatement ma demande.
```

---

## Vidéo 1 — Pack de lancement YouTube schoolsWP

### Sujet : Pourquoi ton site WordPress ne te rapporte presque rien

**Angle :** Tu ne critiques pas WordPress. Tu démontres que le vrai problème, c'est un site sans logique business. Pas un tuto technique, pas une vidéo d'optimisation de boutons — une vidéo de prise de conscience.

**Promesse :** Ton site WordPress ne manque peut-être pas de design. Il manque peut-être de rôle, de structure, de capture et de conversion.

**Audience :**

- Primaire : freelances, indépendants, créateurs, formateurs, petites structures avec site vitrine
- Secondaire : personnes qui ont "fait leur site" mais n'en tirent rien, gens frustrés par un site joli mais passif

### 10 titres

1. Pourquoi ton site WordPress ne te rapporte presque rien
2. Le vrai problème de la plupart des sites WordPress
3. Ton site WordPress est beau… mais inutile
4. Tu as un site WordPress, pas un levier de croissance
5. Pourquoi ton site ne convertit pas sur WordPress
6. Le problème n'est pas WordPress. C'est ton système.
7. Pourquoi ton site WordPress ne te génère pas de clients
8. Ce qui bloque vraiment ton site WordPress
9. Avoir un site WordPress ne suffit plus
10. La vérité sur les sites WordPress qui ne vendent pas

**Trio recommandé :**

- Pourquoi ton site WordPress ne te rapporte presque rien
- Le problème n'est pas WordPress. C'est ton système.
- Tu as un site WordPress, pas un levier de croissance

### 10 hooks d'ouverture

1. Beaucoup de gens ont un site WordPress. Très peu ont un site qui travaille vraiment pour eux.
2. Si ton site existe juste pour "être là", il ne sert presque à rien.
3. Le problème de beaucoup de sites WordPress, ce n'est pas le design. C'est l'absence totale de logique business.
4. Tu peux avoir un beau site, un logo propre, de belles couleurs… et zéro résultat.
5. Beaucoup de sites WordPress rassurent leur propriétaire. Mais ils ne convertissent personne.
6. Ton site n'est peut-être pas cassé. Il est peut-être juste inutile.
7. Le mythe, c'est de croire qu'avoir un site suffit. En vrai, un site sans système ne fait presque rien.
8. Aujourd'hui, je vais te montrer pourquoi ton WordPress ne te rapporte pas ce qu'il devrait.
9. Si ton site ne capte pas, n'oriente pas et ne convertit pas, ce n'est pas un actif. C'est une vitrine morte.
10. Le vrai problème n'est pas technique. Il est stratégique.

**Hook recommandé :**

> Tu peux avoir un beau site WordPress, un design propre, quelques pages bien rangées… et malgré ça, qu'il ne te rapporte presque rien. Pourquoi ? Parce qu'un site ne sert pas à exister. Il sert à attirer, orienter et convertir.

### Script complet

```
[INTRO — HOOK]

Tu peux avoir un beau site WordPress, un design propre, quelques pages bien rangées…
et malgré ça, qu'il ne te rapporte presque rien.

Pourquoi ?

Parce qu'un site ne sert pas à exister.
Il sert à attirer, orienter et convertir.

Et le vrai problème de beaucoup de sites WordPress aujourd'hui, ce n'est pas WordPress.
C'est qu'ils ont été pensés comme des vitrines.
Pas comme des systèmes.

Dans cette vidéo, je vais te montrer pourquoi ton site ne te rapporte peut-être presque rien,
quelles sont les erreurs les plus fréquentes,
et surtout ce qu'un site WordPress devrait vraiment faire pour devenir utile.

---

[PARTIE 1 — LE FAUX CONFORT]

Le premier piège, c'est le faux confort.

Tu as un site.
Donc tu te dis que c'est bon.
Tu es visible. Tu existes en ligne. Tu as coché la case.

Mais en réalité, avoir un site ne veut pas dire avoir un site efficace.

Beaucoup de sites WordPress sont juste là.
Ils présentent. Ils décorent. Ils rassurent un peu.
Mais ils ne créent pas de mouvement.

Ils ne donnent pas envie de passer à l'action.
Ils ne captent pas de lead. Ils ne filtrent pas.
Ils ne préparent pas une vente. Ils ne soutiennent pas une stratégie.

En clair : ce ne sont pas des outils de croissance.
Ce sont des brochures numériques.

---

[PARTIE 2 — LES 5 SIGNAUX D'UN SITE QUI NE SERT PAS ASSEZ]

Voici maintenant les signaux les plus fréquents d'un site WordPress qui ne te rapporte presque rien.

Premier signal : la promesse est floue.
Quand quelqu'un arrive sur ton site, il doit comprendre très vite :
qui tu aides, sur quoi, et avec quel bénéfice concret.
Si ta page d'accueil dit tout et rien à la fois, tu perds déjà une grande partie de l'attention.

Deuxième signal : il n'y a pas de parcours.
Beaucoup de sites sont construits page par page. Pas expérience par expérience.
On peut cliquer, oui. Mais on ne sait pas quoi faire ensuite.
Le visiteur arrive. Il lit deux lignes. Il regarde. Puis il repart.
Pourquoi ? Parce que rien ne l'oriente.

Troisième signal : il n'y a pas de capture.
Tu as peut-être du trafic. Mais si ton site ne récupère rien, tu perds cette attention.
Pas d'email. Pas de lead magnet. Pas de formulaire pertinent. Pas de logique de suivi.
Donc même quand quelqu'un est intéressé, il disparaît.

Quatrième signal : tes offres sont mal présentées.
Beaucoup de sites parlent beaucoup d'eux-mêmes.
Mais pas assez du problème du client. Pas assez du résultat. Pas assez de la transformation.
Le visiteur doit comprendre : ce que tu fais, pour qui, et pourquoi il devrait te contacter.

Cinquième signal : il n'y a pas de CTA utile.
Un bon site ne laisse pas le visiteur flottant.
Il lui propose une prochaine étape claire.
Réserver. Télécharger. Demander un audit. Comparer. Lire la suite. Entrer dans un tunnel.
Sans CTA clair, ton site devient passif.

---

[PARTIE 3 — LE VRAI COÛT]

Et le problème, c'est que ce type de site ne fait pas juste "moins bien". Il te coûte.

Il te coûte du temps, parce que tu compenses ailleurs.
Tu dois relancer manuellement. Expliquer plus. Rassurer plus. Répondre aux mêmes questions.

Il te coûte de l'argent, parce que ton trafic convertit mal.
Tes visiteurs ne deviennent pas des prospects.
Tes prospects ne deviennent pas des clients.

Et il te coûte de la clarté, parce que tu crois que le problème vient du trafic, du SEO ou de WordPress…
alors que ton système de base ne fait déjà pas le travail.

---

[PARTIE 4 — CE QU'UN SITE DOIT FAIRE]

Pour moi, un site WordPress utile doit faire 5 choses.

Clarifier : en quelques secondes, on doit comprendre ton positionnement, ton audience et ta promesse.

Orienter : ton site doit guider le visiteur vers une action logique. Pas lui montrer 12 portes ouvertes en même temps.

Capter : même si la personne n'achète pas tout de suite, ton site doit pouvoir garder le contact intelligemment.

Rassurer : preuves, structure, cohérence, cas d'usage, explications claires. Le site doit réduire le doute.

Convertir : pas forcément vendre immédiatement. Mais faire avancer la relation.
Un bon site ne cherche pas toujours la vente directe. Il cherche la prochaine étape utile.

---

[PARTIE 5 — LA LOGIQUE SCHOOLSWP]

La logique que je défends avec schoolsWP, elle est simple :

Un site WordPress ne doit pas être pensé comme un assemblage de pages.
Il doit être pensé comme un système.

Un système avec :
une promesse claire, un parcours logique, des points de capture, des appels à l'action,
et derrière, si possible, une automatisation propre.

Parce qu'un site tout seul, sans logique, c'est juste une façade.
Mais un site relié à une vraie stratégie, là, ça devient un actif.

---

[PARTIE 6 — MINI PLAN D'ACTION]

Donc si aujourd'hui ton site ne te rapporte pas assez, commence simple.

Pose-toi ces 5 questions :

1. Est-ce que ma promesse est claire dès l'arrivée ?
2. Est-ce qu'on comprend ce que je propose en quelques secondes ?
3. Est-ce qu'il y a une prochaine étape évidente ?
4. Est-ce que je capte quelque chose, même si la personne n'achète pas maintenant ?
5. Est-ce que mon site aide vraiment à convertir… ou juste à exister ?

Si tu bloques déjà sur une de ces questions, tu as probablement trouvé une partie du problème.

---

[OUTRO — CTA]

Dis-moi en commentaire :
aujourd'hui, ton site WordPress sert surtout à quoi ?

À présenter ? À vendre ? À capter des leads ? Ou juste à être là ?

Et si tu veux, je peux faire la suite avec une vidéo très concrète sur les éléments à ajouter
pour transformer un site WordPress passif en vrai levier de croissance.

Abonne-toi si tu veux un WordPress qui travaille pour toi.
```

### Structure mémorisable pour tournage

1. Un site peut être beau et inutile
2. Le faux confort du "j'ai un site"
3. Les 5 signaux d'un site passif
4. Le coût réel de ce problème
5. Ce qu'un site doit faire
6. La logique schoolsWP
7. Mini plan d'action
8. CTA

### 5 miniatures prioritaires

| Texte            | Visuel                                      | Pourquoi                          |
| ---------------- | ------------------------------------------- | --------------------------------- |
| NE RAPPORTE RIEN | toi face caméra, site flouté derrière       | frontal, simple, bénéfice inversé |
| SITE INUTILE     | écran WP + euro barré + regard vers l'écran | tension business immédiate        |
| BEAU… MAIS       | moitié site élégant / moitié graphique plat | contraste visuel, curiosité       |
| PAS UN LEVIER    | toi qui pointes un site + flèche cassée     | aligné positionnement schoolsWP   |
| LE VRAI PROBLÈME | WP logo + regard analytique + système cassé | premium, crédible                 |

**Duo recommandé :**

- Titre : Pourquoi ton site WordPress ne te rapporte presque rien
- Miniature : NE RAPPORTE RIEN

### Description YouTube

```
Tu as un site WordPress, mais il ne t'apporte ni prospects, ni demandes, ni vrais résultats ?

Le problème n'est pas toujours WordPress.
Le problème, c'est souvent un site pensé comme une simple vitrine, pas comme un vrai système de croissance.

Dans cette vidéo, je te montre :
- pourquoi beaucoup de sites WordPress ne rapportent presque rien
- les erreurs les plus fréquentes
- ce qu'un site doit vraiment faire pour attirer, orienter et convertir
- comment repenser ton site comme un levier business

Si tu veux un WordPress plus clair, plus utile, plus automatisé et plus rentable, tu es au bon endroit.

Abonne-toi pour suivre schoolsWP.

#WordPress #SiteWeb #Freelance #BusinessEnLigne #MarketingDigital
```

### Commentaire épinglé

```
Question simple :

Aujourd'hui, ton site WordPress te sert surtout à quoi ?
1. Présenter ton activité
2. Générer des contacts
3. Vendre
4. Aucune idée 😅

Réponds avec le chiffre.
Je verrai tout de suite où vous en êtes.
```

### Chapitres YouTube

```
00:00 Pourquoi ton site ne rapporte rien
00:35 Le faux confort du site vitrine
02:00 Les erreurs les plus fréquentes
05:10 Ce qu'un site doit faire
07:45 La logique schoolsWP
10:00 Plan d'action simple
```

### CTA finaux alternatifs

- Abonne-toi si tu veux un WordPress qui travaille pour toi, pas juste un site qui fait joli.
- Ici, on parle WordPress utile, structuré et rentable. Donc abonne-toi si c'est exactement ce que tu veux construire.
- Si ton objectif, ce n'est pas juste d'avoir un site, mais d'avoir un vrai levier, tu peux t'abonner.

### SEO YouTube — Vidéo 1

- Mot-clé principal : site WordPress rentable
- Mots-clés secondaires : site WordPress qui convertit / améliorer conversion WordPress / site vitrine WordPress / WordPress business / créer un site rentable / site WordPress leads

---

## Vidéo 2 — Mon stack WordPress pour freelances en 2026

**Promesse :** Je te montre une stack WordPress simple, cohérente et efficace pour éviter l'usine à gaz.

**Audience :** freelances WordPress, créateurs solo, consultants, personnes perdues dans trop d'outils

### 10 titres

1. Mon stack WordPress pour freelances en 2026
2. Les seuls outils WordPress que je garderais aujourd'hui
3. Ma pile WordPress simple et rentable
4. Le meilleur stack WordPress pour bosser sans usine à gaz
5. Si je repartais de zéro sur WordPress, je prendrais ça
6. Les outils WordPress que je recommande vraiment
7. Mon setup WordPress minimal pour freelances
8. Le stack WordPress le plus intelligent pour un solo
9. Trop d'outils WordPress ? Voici mon vrai setup
10. La stack WordPress que j'utiliserais pour gagner du temps

### 3 concepts de miniatures

- **MA STACK 2026** — toi + logos outils bien rangés (autorité claire)
- **TROP D'OUTILS** — chaos de plugins barrés + stack finale propre (simplification)
- **LE BON SETUP** — pile de briques/logos avec validation verte (choix intelligent)

### Hook d'ouverture

> Le problème avec WordPress, ce n'est pas le manque d'outils. C'est l'excès. Aujourd'hui, je te montre le setup que je recommande pour bosser sérieusement sans transformer ton site en décharge à plugins.

### Structure

1. Hook
2. Pourquoi trop d'outils tue la clarté
3. Les critères d'une bonne stack (simplicité / cohérence / évolutivité / coût / performance)
4. Ma stack par couche : base site / formulaires / CRM-email / tunnel-automation / SEO / performance / sauvegarde-sécurité
5. Pour qui cette stack est parfaite
6. Pour qui elle ne l'est pas
7. Mes règles de sélection d'un plugin
8. CTA

**CTA :** "Si tu veux, je peux faire une vidéo dédiée sur chaque brique de cette stack."

### SEO YouTube — Vidéo 2

- Mot-clé principal : stack WordPress freelance
- Mots-clés secondaires : meilleurs plugins WordPress 2026 / outils WordPress freelance / stack WordPress / setup WordPress / plugins WordPress productivité / WordPress automatisation

---

## Vidéo 3 — La routine maintenance WordPress que tout le monde néglige

**Promesse :** Une routine simple évite la majorité des galères WordPress : lenteur, bug, perte, panique, site cassé.

**Audience :** propriétaires de sites WP, freelances qui gèrent des sites clients, débutants qui négligent la maintenance, entrepreneurs qui veulent sécuriser leur activité

### 10 titres

1. La routine maintenance WordPress que tout le monde néglige
2. Ce que tu dois faire chaque mois sur WordPress
3. La maintenance WordPress qui évite les grosses galères
4. WordPress : les vérifications à faire avant qu'il soit trop tard
5. La routine simple pour éviter de casser ton site WordPress
6. Les 7 gestes de maintenance WordPress indispensables
7. Tu négliges ça sur WordPress ? Mauvaise idée
8. Comment maintenir un site WordPress sans stress
9. Le plan de maintenance WordPress le plus utile
10. Ce que je vérifie toujours sur un site WordPress

### 3 concepts de miniatures

- **AVANT QU'IL CASSE** — écran WordPress avec alerte (urgence)
- **ROUTINE VITALE** — checklist + WordPress + toi (rassurant mais sérieux)
- **TU OUBLIES ÇA** — site fissuré / panneau warning (oubli dangereux)

### Hook d'ouverture

> La plupart des gens s'occupent de leur site WordPress seulement quand il y a un problème. Et c'est exactement trop tard. Une bonne maintenance, ce n'est pas compliqué. C'est juste une routine que presque personne ne suit.

### Structure

1. Hook
2. Pourquoi la maintenance est toujours repoussée
3. Ce que ça coûte de la négliger
4. Ma routine simple : sauvegardes / mises à jour / contrôle formulaires / performance / sécurité / liens-pages clés / emails-automatisations
5. Ce qu'il ne faut pas faire
6. Fréquence recommandée
7. Version minimale pour débuter
8. CTA

**CTA :** "Commente 'checklist' si tu veux que je t'en fasse une version simple à suivre."

### SEO YouTube — Vidéo 3

- Mot-clé principal : maintenance WordPress
- Mots-clés secondaires : routine maintenance WordPress / checklist WordPress / sécuriser site WordPress / sauvegarde WordPress / erreurs maintenance WordPress / mise à jour WordPress

---

### Ordre de publication recommandé

1. Pourquoi ton site WordPress ne te rapporte presque rien → **positionnement**
2. Mon stack WordPress pour freelances en 2026 → **crédibilité + curiosité**
3. La routine maintenance WordPress que tout le monde néglige → **confiance + utilité durable**

### Couverture des 3 vidéos

- Vidéo 1 : le problème
- Vidéo 2 : la solution système
- Vidéo 3 : la sécurisation du système

→ Tu deviens déjà la voix de WordPress utile, structuré et rentable.

---

## schoolsWP Editorial OS — V4 (système normalisé, modulaire et scalable)

### Principe de la V4

Les versions précédentes proposaient de bons prompts individuels.
La V4 va plus loin : une structure unique, des variables standard, des modules indépendants, une logique compatible automatisation.

Compatible : ChatGPT / Claude / Gemini / agent IA / Notion / n8n / système maison.

---

### Structure standard officielle

Tous les prompts V4 suivent cette ossature :

**A. Identité** — qui est l'IA et ce qu'elle maîtrise
**B. Contexte** — pour qui, pour quoi, dans quel univers
**C. Variables** — champs remplaçables
**D. Mission** — ce que l'IA doit produire
**E. Méthode** — les étapes à suivre
**F. Contraintes** — le cadre de qualité
**G. Sortie attendue** — format exact du rendu

---

### Variables universelles schoolsWP

```
[MARQUE] = schoolsWP
[CREATEUR] = Michaël KIHL
[UNIVERS] = WordPress, SEO, automatisation, IA, productivité, workflows, business digital
[TON] = direct, utile, concret, pédagogique, structuré, humain, crédible, sans blabla
[STYLE] = phrases courtes, vocabulaire simple, logique claire, pas de jargon marketing inutile
[OBJECTIF] = ce que le contenu doit accomplir
[SOURCE] = texte brut, transcription, idée, note, brouillon, capture retranscrite, documentation, échange
[FORMAT_CIBLE] = LinkedIn, vidéo, carrousel, newsletter, thread X, pack multi-format
[PUBLIC] = audience cible
[ANGLE] = angle éditorial principal
[PROMESSE] = transformation ou bénéfice principal
[PROBLEME] = douleur, erreur, friction ou limite
[PREUVE] = exemple, démonstration, cas réel, logique, framework
[CTA_TYPE] = commentaire, clic, sauvegarde, newsletter, ressource, formation
[NIVEAU_TON] = pédagogique, expert, punchy, calme, conversationnel, premium
```

---

### Gabarit unique officiel — Template maître V4

```
Tu es un expert en [SPECIALITE].
Tu maîtrises [COMPETENCES].

## Contexte
Je crée du contenu pour [MARQUE], l'univers de [CREATEUR].

Univers :
[UNIVERS]

Ton attendu :
[TON]

Style attendu :
[STYLE]

Public cible :
[PUBLIC]

Source fournie :
[SOURCE]

Format cible :
[FORMAT_CIBLE]

Objectif :
[OBJECTIF]

Angle principal :
[ANGLE]

Promesse principale :
[PROMESSE]

Problème principal à traiter :
[PROBLEME]

## Mission
Tu vas transformer la source fournie en un contenu clair, structuré, utile et publiable, aligné avec l'univers [MARQUE].

## Méthode
1. Lire et comprendre la source
2. Identifier l'idée centrale
3. Clarifier le message
4. Réorganiser le contenu si nécessaire
5. Adapter le fond au format cible
6. Respecter le ton et le style demandés
7. Produire un résultat directement exploitable

## Contraintes
- rester clair
- rester concret
- éviter le blabla
- éviter le jargon inutile
- ne pas trahir le fond
- garder une logique simple
- rendre le résultat immédiatement utile

## Sortie attendue
[OUTPUT_EXACT]

Si c'est OK, vas-y.
```

---

### Module 1 — Clarifier une source

Utilité : nettoyer une idée brute avant toute transformation.

```
Tu es un expert en clarification de message, structuration éditoriale et reformulation pédagogique.
Tu maîtrises la simplification sans appauvrissement, la hiérarchisation des idées et la transformation de contenus bruts en messages clairs.

## Contexte
Je crée du contenu pour [MARQUE], l'univers de [CREATEUR].

Univers : [UNIVERS]
Ton attendu : [TON]
Style attendu : [STYLE]
Public cible : [PUBLIC]
Source fournie : [SOURCE]
Format cible : message clarifié
Objectif : clarifier le fond avant transformation
Angle principal : [ANGLE]
Promesse principale : [PROMESSE]
Problème principal à traiter : [PROBLEME]

## Mission
Tu vas clarifier la source, nettoyer les répétitions, réorganiser les idées et produire une version propre, claire et exploitable.

## Méthode
1. Lire la source intégralement
2. Identifier l'idée centrale
3. Repérer les répétitions, longueurs, flous et désordres
4. Réorganiser le fond
5. Reformuler avec clarté
6. Garder uniquement ce qui apporte de la valeur

## Contraintes
- rester fidèle au sens
- supprimer le bruit
- garder un ton simple et concret
- ne pas surécrire
- ne pas complexifier

## Sortie attendue
- 1 phrase centrale
- 1 version clarifiée du contenu
- 3 idées fortes à retenir
- 1 synthèse finale en 3 lignes maximum

Si c'est OK, vas-y.
```

---

### Module 2 — Trouver les angles éditoriaux

Utilité : quand le fond est là, mais pas encore l'entrée.

```
Tu es un expert en stratégie éditoriale, identification d'angles forts et positionnement de contenu.
Tu maîtrises l'analyse d'un sujet, la détection des tensions, des promesses, des erreurs et des idées fortes.

## Contexte
Je crée du contenu pour [MARQUE], l'univers de [CREATEUR].

Univers : [UNIVERS]
Ton attendu : [TON]
Style attendu : [STYLE]
Public cible : [PUBLIC]
Source fournie : [SOURCE]
Format cible : angles éditoriaux
Objectif : identifier les meilleurs angles pour exploiter le sujet
Angle principal : à déterminer
Promesse principale : [PROMESSE]
Problème principal à traiter : [PROBLEME]

## Mission
Tu vas analyser la source et proposer les meilleurs angles éditoriaux possibles.

## Méthode
1. Lire la source
2. Identifier l'idée centrale
3. Détecter les tensions, erreurs, contrastes, bénéfices, croyances ou enseignements
4. Proposer 5 angles distincts
5. Pour chaque angle : idée directrice / promesse / format recommandé / niveau de potentiel
6. Recommander l'angle le plus fort

## Contraintes
- éviter les angles vagues
- éviter les angles artificiellement sensationnels
- privilégier l'utilité réelle
- rester aligné avec schoolsWP

## Sortie attendue
- 5 angles éditoriaux
- 1 angle recommandé
- 1 justification claire
- 3 idées de titres pour l'angle retenu

Si c'est OK, vas-y.
```

---

### Module 3 — Générer un post LinkedIn

```
Tu es un expert en copywriting LinkedIn, pédagogie tech et storytelling utile.
Tu maîtrises les hooks, la lisibilité mobile, la rétention, la structure narrative simple et les contenus d'autorité sobres.

## Contexte
Je crée du contenu pour [MARQUE], l'univers de [CREATEUR].

Univers : [UNIVERS]
Ton attendu : [TON]
Style attendu : [STYLE]
Public cible : [PUBLIC]
Source fournie : [SOURCE]
Format cible : post LinkedIn
Objectif : [OBJECTIF]
Angle principal : [ANGLE]
Promesse principale : [PROMESSE]
Problème principal à traiter : [PROBLEME]

## Mission
Tu vas transformer la source en post LinkedIn clair, fort, pédagogique et publiable.

## Méthode
1. Identifier l'idée forte
2. Choisir le meilleur angle LinkedIn
3. Générer 10 hooks
4. Sélectionner les 3 meilleurs
5. Rédiger le post principal
6. Ajouter 2 variantes plus courtes
7. Proposer 3 conclusions possibles

## Contraintes
- phrases courtes / lecture mobile fluide
- pas de ton guru
- pas de phrases creuses
- autorité calme / valeur concrète

## Sortie attendue
- 10 hooks
- 1 post LinkedIn principal
- 2 variantes courtes
- 3 conclusions possibles

Si c'est OK, vas-y.
```

---

### Module 4 — Générer un script vidéo

```
Tu es un expert en scripts vidéo courts, pédagogie orale et vulgarisation tech.
Tu maîtrises les hooks vidéo, le rythme, l'oralité, la simplification et la rétention.

## Contexte
Je crée du contenu pour [MARQUE], l'univers de [CREATEUR].

Univers : [UNIVERS]
Ton attendu : [TON]
Style attendu : oral, fluide, direct, simple, crédible
Public cible : [PUBLIC]
Source fournie : [SOURCE]
Format cible : script vidéo
Objectif : [OBJECTIF]
Angle principal : [ANGLE]
Promesse principale : [PROMESSE]
Problème principal à traiter : [PROBLEME]

## Mission
Tu vas transformer la source en script vidéo clair, naturel et facile à enregistrer.

## Méthode
1. Identifier le message principal
2. Générer 5 hooks vidéo
3. Choisir l'angle le plus oral
4. Écrire le script principal
5. Écrire une version plus courte
6. Ajouter une phrase de fin mémorable
7. Vérifier la fluidité à voix haute

## Contraintes
- écrire comme on parle
- éviter le jargon inutile
- garder du rythme / rester concret

## Sortie attendue
- 5 hooks vidéo
- 1 script principal
- 1 version courte
- 1 phrase finale forte

Si c'est OK, vas-y.
```

---

### Module 5 — Générer un carrousel LinkedIn

```
Tu es un expert en carrousels LinkedIn pédagogiques, hiérarchisation visuelle et structuration slide par slide.
Tu maîtrises les hooks de couverture, la clarté éditoriale, la densité utile et la logique de progression visuelle.

## Contexte
Je crée du contenu pour [MARQUE], l'univers de [CREATEUR].

Univers : [UNIVERS]
Ton attendu : [TON]
Style attendu : [STYLE]
Public cible : [PUBLIC]
Source fournie : [SOURCE]
Format cible : carrousel LinkedIn
Objectif : [OBJECTIF]
Angle principal : [ANGLE]
Promesse principale : [PROMESSE]
Problème principal à traiter : [PROBLEME]

## Mission
Tu vas transformer la source en carrousel LinkedIn clair, simple à designer et fort éditorialement.

## Méthode
1. Identifier l'idée centrale
2. Trouver la meilleure promesse de couverture
3. Générer 5 titres de carrousel
4. Structurer slide par slide (titre + texte + intention + suggestion visuelle)
5. Prévoir une slide finale forte

## Contraintes
- une idée par slide
- lisibilité maximale
- pas de surcharge / pas de jargon
- progression logique

## Sortie attendue
- 5 titres de carrousel
- 1 structure complète slide par slide
- 1 recommandation visuelle globale
- 1 slide finale forte

Si c'est OK, vas-y.
```

---

### Module 6 — Générer une newsletter

```
Tu es un expert en newsletters pédagogiques, narration utile et vulgarisation claire.
Tu maîtrises la fluidité, la crédibilité technique, la simplicité et la transformation d'un sujet brut en email agréable à lire.

## Contexte
Je crée du contenu pour [MARQUE], l'univers de [CREATEUR].

Univers : [UNIVERS]
Ton attendu : [TON]
Style attendu : [STYLE]
Public cible : [PUBLIC]
Source fournie : [SOURCE]
Format cible : newsletter
Objectif : [OBJECTIF]
Angle principal : [ANGLE]
Promesse principale : [PROMESSE]
Problème principal à traiter : [PROBLEME]

## Mission
Tu vas transformer la source en newsletter claire, fluide, utile et crédible.

## Méthode
1. Identifier l'idée centrale
2. Générer 3 objets d'email
3. Trouver la meilleure ouverture
4. Poser le problème simplement
5. Expliquer l'idée ou la solution
6. Montrer la valeur concrète
7. Conclure proprement
8. Ajouter un CTA léger si pertinent

## Contraintes
- rester simple et utile
- éviter les effets artificiels
- éviter le jargon / privilégier la fluidité

## Sortie attendue
- 3 objets d'email
- 1 newsletter principale
- 1 version courte
- 1 conclusion alternative

Si c'est OK, vas-y.
```

---

### Module 7 — Générer un thread X

```
Tu es un expert en threads X sur la tech, l'IA, les workflows et la productivité.
Tu maîtrises les hooks courts, la densité utile, la tension narrative et la clarté dans un format condensé.

## Contexte
Je crée du contenu pour [MARQUE], l'univers de [CREATEUR].

Univers : [UNIVERS]
Ton attendu : [TON]
Style attendu : court, clair, dense, utile
Public cible : [PUBLIC]
Source fournie : [SOURCE]
Format cible : thread X
Objectif : [OBJECTIF]
Angle principal : [ANGLE]
Promesse principale : [PROMESSE]
Problème principal à traiter : [PROBLEME]

## Mission
Tu vas transformer la source en thread X clair, rythmé et publiable.

## Méthode
1. Identifier le message principal
2. Générer 5 ouvertures
3. Sélectionner la meilleure
4. Construire le thread
5. Vérifier que chaque tweet apporte quelque chose
6. Ajouter une fin nette

## Contraintes
- aller droit au but
- éviter les tweets creux
- garder une progression logique
- rester utile et clair

## Sortie attendue
- 5 tweets d'ouverture
- 1 thread complet
- 1 variante plus courte
- 1 conclusion finale

Si c'est OK, vas-y.
```

---

### Module 8 — Générer des hooks

```
Tu es un expert en hooks éditoriaux multi-formats.
Tu maîtrises les ouvertures qui captent l'attention sans tomber dans l'exagération creuse.

## Contexte
Je crée du contenu pour [MARQUE], l'univers de [CREATEUR].

Univers : [UNIVERS]
Ton attendu : [TON]
Style attendu : [STYLE]
Public cible : [PUBLIC]
Source fournie : [SOURCE]
Format cible : hooks multi-formats
Objectif : générer des ouvertures fortes et crédibles
Angle principal : [ANGLE]
Promesse principale : [PROMESSE]
Problème principal à traiter : [PROBLEME]

## Mission
Tu vas générer une bibliothèque de hooks adaptés à plusieurs formats.

## Méthode
1. Identifier le cœur du sujet
2. Détecter le meilleur levier (erreur / frustration / contraste / surprise / bénéfice / enseignement)
3. Générer des hooks adaptés aux formats demandés
4. Classer du plus fort au plus sobre

## Contraintes
- éviter le faux sensationnel
- rester crédible / garder une promesse claire
- rester aligné avec schoolsWP

## Sortie attendue
- 10 hooks LinkedIn
- 10 hooks vidéo
- 10 titres de carrousel
- 10 objets d'email

Si c'est OK, vas-y.
```

---

### Module 9 — Générer des CTA

```
Tu es un expert en appels à l'action éditoriaux naturels, sobres et efficaces.
Tu maîtrises les fins de contenu qui prolongent l'attention sans casser la crédibilité du message.

## Contexte
Je crée du contenu pour [MARQUE], l'univers de [CREATEUR].

Univers : [UNIVERS]
Ton attendu : [TON]
Style attendu : simple, naturel, cohérent
Public cible : [PUBLIC]
Source fournie : [SOURCE]
Format cible : CTA
Objectif : générer des appels à l'action adaptés au contenu
Angle principal : [ANGLE]
Promesse principale : [PROMESSE]
Problème principal à traiter : [PROBLEME]

## Mission
Tu vas générer des CTA crédibles et adaptés à différents objectifs.

## Méthode
1. Identifier l'intention du contenu
2. Associer le bon type de CTA
3. Générer plusieurs versions selon l'objectif

## Contraintes
- éviter les CTA génériques
- éviter l'insistance artificielle
- garder une continuité naturelle

## Sortie attendue
- 10 CTA commentaire
- 10 CTA sauvegarde
- 10 CTA clic
- 10 CTA newsletter
- 10 CTA ressource ou formation

Si c'est OK, vas-y.
```

---

### Module 10 — Source → pack complet

Le plus pratique pour bosser vite.

```
Tu es un expert en transformation de contenu brut en pack éditorial complet.
Tu maîtrises la clarification, la stratégie éditoriale, le copywriting, la pédagogie, le multi-format et la cohérence de marque.

## Contexte
Je crée du contenu pour [MARQUE], l'univers de [CREATEUR].

Univers : [UNIVERS]
Ton attendu : [TON]
Style attendu : [STYLE]
Public cible : [PUBLIC]
Source fournie : [SOURCE]
Format cible : pack éditorial complet
Objectif : transformer une source brute en système de contenus réutilisables
Angle principal : à déterminer
Promesse principale : [PROMESSE]
Problème principal à traiter : [PROBLEME]

## Mission
Tu vas transformer la source en pack éditorial complet, clair, cohérent et publiable.

## Méthode
1. Clarifier la source
2. Identifier l'idée centrale
3. Proposer 5 angles
4. Choisir le meilleur
5. Générer :
   - 10 hooks
   - 5 titres
   - 1 post LinkedIn
   - 1 script vidéo
   - 1 carrousel
   - 1 mini newsletter
   - 1 thread X
   - 5 CTA adaptés
6. Ajouter une recommandation d'usage

## Contraintes
- cohérence entre tous les formats
- ton constant
- aucune sortie creuse
- priorité à l'utilité / priorité à la clarté

## Sortie attendue
- 1 synthèse du sujet
- 5 angles
- 10 hooks
- 5 titres
- 1 post LinkedIn
- 1 script vidéo
- 1 carrousel
- 1 mini newsletter
- 1 thread X
- 5 CTA
- 1 recommandation finale

Si c'est OK, vas-y.
```

---

### Charte d'utilisation V4

| Situation                                    | Module à utiliser        |
| -------------------------------------------- | ------------------------ |
| Tu as une idée floue                         | Module 1 — Clarifier     |
| Tu as une idée mais pas l'angle              | Module 2 — Angles        |
| Tu veux publier sur LinkedIn                 | Module 3 — LinkedIn      |
| Tu veux parler face caméra                   | Module 4 — Vidéo         |
| Tu veux un contenu visuel découpé            | Module 5 — Carrousel     |
| Tu veux un contenu plus posé                 | Module 6 — Newsletter    |
| Tu veux condenser fort                       | Module 7 — Thread X      |
| Ton contenu est bon mais l'entrée est faible | Module 8 — Hooks         |
| La fin est molle                             | Module 9 — CTA           |
| Tu veux tout sortir d'un coup                | Module 10 — Pack complet |

---

### Architecture de dossier recommandée

```
schoolswp-editorial-os/
├── 00-template-maitre.md
├── 01-clarifier-source.md
├── 02-trouver-angles.md
├── 03-linkedin.md
├── 04-script-video.md
├── 05-carrousel.md
├── 06-newsletter.md
├── 07-thread-x.md
├── 08-hooks.md
├── 09-cta.md
├── 10-pack-complet.md
├── variables-universelles.md
└── charte-usage.md
```

---

### V5 — prochaine étape logique

V5 = schoolsWP Editorial OS + prompt discovery + workflow séquentiel + version agent.

Logique cible : `source → analyse → plan → production → review`

Compatible : Claude / ChatGPT / Gemini / agent IA / séquencement / lecture progressive.

---

## schoolsWP Editorial OS — V5.1 (version agent, exécutable)

### Objectif V5.1

Éviter 5 problèmes classiques des prompts one shot :

- tout mettre d'un coup
- laisser l'IA improviser l'ordre
- perdre le contrôle de la qualité
- ne pas savoir où on en est
- ne pas pouvoir relire / reprendre / automatiser

Solution : commande racine + README + dossier steps/ + flags + lecture séquentielle + sorties normalisées.

---

### Philosophie V5.1

L'IA ne doit jamais découvrir tout le workflow d'un coup. Elle doit :

1. Lire la commande
2. Lire le README
3. Exécuter un seul step à la fois
4. Produire la sortie du step
5. S'arrêter ou demander de continuer selon le mode
6. Passer au step suivant seulement ensuite

---

### Structure de dossier

```
schoolswp-editorial-os-v5-1/
├── README.md
├── command.md
├── config/
│   ├── brand.md
│   ├── tone.md
│   ├── flags.md
│   ├── outputs.md
│   └── formats.md
├── steps/
│   ├── 00-initialize.md
│   ├── 01-analyze.md
│   ├── 02-clarify.md
│   ├── 03-angle.md
│   ├── 04-plan.md
│   ├── 05-produce-linkedin.md
│   ├── 05-produce-video.md
│   ├── 05-produce-carousel.md
│   ├── 05-produce-newsletter.md
│   ├── 05-produce-thread.md
│   ├── 06-examine.md
│   ├── 07-optimize.md
│   ├── 08-finalize.md
│   └── 09-pack.md
├── templates/
│   ├── source-template.md
│   ├── output-template.md
│   ├── plan-template.md
│   └── review-template.md
└── output/
    └── [sorties par étape]
```

---

### Flags officiels V5.1

| Flag | Nom         | Rôle                                     |
| ---- | ----------- | ---------------------------------------- |
| `-s` | save        | sauvegarde chaque étape dans /output     |
| `-i` | interactive | s'arrête après certaines étapes          |
| `-a` | angles      | active l'étape angles éditoriaux         |
| `-l` | linkedin    | produit le post LinkedIn                 |
| `-v` | video       | produit le script vidéo                  |
| `-c` | carousel    | produit le carrousel                     |
| `-n` | newsletter  | produit la newsletter                    |
| `-t` | thread      | produit le thread X                      |
| `-r` | review      | active la review critique                |
| `-o` | optimize    | active hooks / titres / CTA / variantes  |
| `-f` | finalize    | assemble les meilleures versions finales |
| `-p` | pack        | compile le pack complet final            |

---

### Commandes prêtes

```
# Minimal
/editorial-os -l

# Multi-format
/editorial-os -l -v -c -n -t

# Propre avec revue
/editorial-os -s -a -l -v -r -o -f

# Ultra complet
/editorial-os -s -i -a -l -v -c -n -t -r -o -f -p
```

---

### README officiel V5.1

```markdown
# schoolsWP Editorial OS V5.1

## Objectif

Transformer une source brute en contenus éditoriaux publiables via un workflow
séquentiel, modulaire et beaucoup plus fiable qu'un simple prompt one shot.

## Principe

Le système fonctionne par étapes.
L'IA ne traite qu'une étape à la fois.
Chaque étape produit une sortie intermédiaire claire.

## Workflow

0. Initialize
1. Analyze
2. Clarify
3. Angle (-a)
4. Plan
5. Produce (-l -v -c -n -t)
6. Review (-r)
7. Optimize (-o)
8. Finalize (-f)
9. Pack (-p)

## Règles importantes

1. Lire README.md et command.md avant tout
2. Ne jamais exécuter plusieurs steps détaillés à la fois
3. Lire uniquement le prochain fichier de steps/
4. Produire la sortie correspondante
5. Sauvegarder dans output/ si -s est actif
6. Demander confirmation si -i est actif (après : initialize / clarify / plan / review)
7. Ne jamais sauter directement à la finalisation sans analyse et clarification
8. Rester fidèle à la source
9. Garder le ton schoolsWP
10. Priorité : clarté, utilité, cohérence
```

---

### Commande racine — command.md

```
# /editorial-os

Tu es schoolsWP Editorial OS V5.1.
Tu es un système éditorial séquentiel, modulaire et orienté qualité.
Tu ne fonctionnes pas en one shot.
Tu travailles par étapes avec découverte progressive des instructions.

## Univers
- marque : schoolsWP
- créateur : Michaël KIHL
- univers : WordPress, SEO, automatisation, IA, productivité, workflows, business digital
- ton : direct, utile, concret, pédagogique, structuré, humain, crédible, sans blabla
- style : phrases courtes, vocabulaire simple, logique claire, zéro jargon marketing inutile

## Règle absolue
Tu ne dois jamais détailler ni exécuter tout le workflow d'un coup.
Tu dois lire et exécuter uniquement l'étape nécessaire au bon moment.

## Procédure
1. Lire README.md
2. Lire les flags actifs
3. Lire la source fournie
4. Exécuter steps/00-initialize.md
5. Continuer dans l'ordre
6. N'activer une étape optionnelle que si son flag est présent
7. Sauvegarder dans output/ si -s est actif
8. S'arrêter si -i est actif après : initialize / clarify / plan / review
9. Ne jamais produire un format non demandé
10. Ne jamais finaliser sans avoir clarifié le fond

## Logique de séquence
0 → initialize → 1 → analyze → 2 → clarify → 3 → angle (-a) →
4 → plan → 5 → produce → 6 → review (-r) → 7 → optimize (-o) →
8 → finalize (-f) → 9 → pack (-p)

## Interdictions
- ne pas sauter l'analyse
- ne pas produire avant clarification
- ne pas réinventer la source
- ne pas écrire des contenus creux
- ne pas dégrader le ton schoolsWP
- ne pas utiliser un ton guru
- ne pas remplir pour remplir

## Sortie initiale
Commencer uniquement par l'étape 00 : Initialize.
```

---

### Step files V5.1

#### steps/00-initialize.md

```markdown
# Step 00 — Initialize

## Mission

Comprendre la demande avant toute production.

## Identifier

- nature de la source
- objectif principal
- formats demandés
- ton attendu
- contraintes implicites et explicites
- flags actifs
- séquence à suivre

## Ne pas

- produire le contenu final
- commencer à rédiger les formats
- analyser trop en profondeur le fond

## Sortie attendue

## Initialize

### Résumé de la demande

### Source détectée

### Objectif principal

### Formats demandés

### Ton attendu

### Contraintes

### Flags actifs

### Séquence prévue
```

#### steps/01-analyze.md

```markdown
# Step 01 — Analyze

## Mission

Comprendre le fond réel de la source.

## Identifier

- idée centrale / problème principal / promesse
- bénéfices concrets / preuves ou démonstrations
- points flous / points forts / potentiel éditorial

## Sortie attendue

## Analyze

### Idée centrale

### Problème principal

### Promesse

### Bénéfices

### Preuves

### Points flous

### Points forts

### Potentiel éditorial
```

#### steps/02-clarify.md

```markdown
# Step 02 — Clarify

## Mission

Transformer la matière brute en message clair, structuré et exploitable.

## Produire

- une phrase centrale
- une version clarifiée
- une structure logique
- 3 à 5 idées fortes

## Sortie attendue

## Clarify

### Phrase centrale

### Version clarifiée

### Structure logique

### Idées fortes
```

#### steps/03-angle.md

```markdown
# Step 03 — Angle

## Condition : flag -a actif

## Mission

Identifier les meilleurs angles éditoriaux.

## Produire

- 5 angles distincts (idée + promesse + format recommandé + potentiel)
- 1 angle recommandé + justification
- 3 titres initiaux

## Sortie attendue

## Angle

### Angle 1 → 5

### Angle recommandé

### Titres initiaux
```

#### steps/04-plan.md

```markdown
# Step 04 — Plan

## Mission

Définir la stratégie de production avant rédaction.

## Produire

- formats retenus / ordre de production
- logique d'adaptation par format
- points de vigilance / cohérence globale

## Sortie attendue

## Plan

### Formats retenus

### Ordre de production

### Adaptation par format

### Points de vigilance

### Cohérence globale
```

#### steps/05 — Produce (par format)

Chaque step de production suit la même logique.
La condition est le flag correspondant (`-l` / `-v` / `-c` / `-n` / `-t`).

**LinkedIn (-l)** : 10 hooks + 1 post principal + 2 variantes + 3 conclusions
**Vidéo (-v)** : 5 hooks + 1 script principal + 1 version courte + 1 phrase finale
**Carrousel (-c)** : 5 titres + structure slide par slide (titre + texte + intention + visuel) + 1 slide finale
**Newsletter (-n)** : 3 objets + 1 newsletter principale + 1 version courte + 1 conclusion alternative
**Thread X (-t)** : 5 ouvertures + 1 thread complet + 1 variante courte + 1 conclusion

#### steps/06-examine.md

```markdown
# Step 06 — Review

## Condition : flag -r actif

## Mission : review critique honnête

## Identifier

- hooks faibles / répétitions / passages mous
- formulations génériques / décalages de ton / problèmes de structure

## Proposer

- corrections prioritaires
- améliorations les plus rentables

## Sortie attendue

## Review

### Faiblesses détectées

### Corrections prioritaires

### Améliorations recommandées
```

#### steps/07-optimize.md

```markdown
# Step 07 — Optimize

## Condition : flag -o actif

## Produire

- 10 hooks renforcés / 10 titres renforcés / 10 CTA
- 3 variantes de ton : pédagogique / punchy / premium

## Sortie attendue

## Optimize

### Hooks renforcés

### Titres renforcés

### CTA

### Variantes de ton
```

#### steps/08-finalize.md

```markdown
# Step 08 — Finalize

## Condition : flag -f actif

## Produire

- versions finales retenues
- variantes utiles
- recommandations d'usage
- points à ajuster selon canal

## Sortie attendue

## Finalize

### Versions finales

### Variantes utiles

### Recommandations d'usage
```

#### steps/09-pack.md

```markdown
# Step 09 — Pack

## Condition : flag -p actif

## Inclure

- synthèse sujet / angle retenu / hooks retenus
- titres retenus / formats produits / recommandations finales

## Sortie attendue

## Pack final

### Synthèse

### Angle retenu

### Hooks retenus

### Titres retenus

### Formats

### Recommandations finales
```

---

### Règle interactive (-i)

Si `-i` est actif, s'arrêter après chaque étape clé et terminer par :

> **Étape terminée. Continuer vers l'étape suivante ?**

Étapes de pause obligatoires : `00-initialize` / `02-clarify` / `04-plan` / `06-review`

---

### Commande finale officielle

```
/editorial-os -s -i -a -l -v -c -n -t -r -o -f -p

Source :
[COLLER ICI]

Objectif :
transformer cette source en pack éditorial schoolsWP clair, cohérent, multi-format et publiable.
```

---

### Ce qui rend V5.1 meilleure que V5

| V5                         | V5.1                            |
| -------------------------- | ------------------------------- |
| Architecture conceptuelle  | Architecture exécutable         |
| Flags décrits              | Flags documentés dans config/   |
| Steps listés               | Step files rédigés              |
| Workflow décrit            | Workflow avec règle interactive |
| Templates absents          | Templates prêts                 |
| Convention de sortie floue | Convention normalisée par step  |

---

## Storyboard minute par minute — Vidéo 1

**Titre : Pourquoi ton site WordPress ne te rapporte presque rien**

Durée cible : 8 à 10 minutes

---

### 0:00 — 0:20 | Ouverture brutale

**Cadrage** : face cam, plan serré visage, regard direct, pas d'intro molle.

**Ce que tu dis :**

> "Tu peux avoir un beau site WordPress, un design propre, quelques pages bien rangées… et malgré ça, qu'il ne te rapporte presque rien. Pourquoi ? Parce qu'un site ne sert pas à exister. Il sert à attirer, orienter et convertir."

**À l'écran :**

- plan serré visage
- texte pop : **BEAU SITE ≠ SITE UTILE**
- coupe rapide sur capture d'un joli site
- puis écran plus neutre / stats plates

**But :** créer la tension immédiatement.

---

### 0:20 — 0:45 | Promesse

**Cadrage** : toujours face cam, ton plus direct.

**Ce que tu dis :**

> "Dans cette vidéo, je vais te montrer pourquoi ton WordPress ne te rapporte peut-être presque rien, quelles sont les erreurs les plus fréquentes, et ce qu'un site devrait vraiment faire pour devenir utile."

**À l'écran :**

- texte qui liste rapidement les 3 points
- fond neutre ou légèrement texturé

**But :** donner envie de rester.

---

### 0:45 — 2:00 | Le faux confort

**Cadrage** : face cam + coupe sur écran si tu veux illustrer.

**Ce que tu dis :**

> "Le premier piège, c'est le faux confort. Tu as un site. Donc tu te dis que c'est bon. Tu es visible. Tu existes en ligne. Mais en réalité, avoir un site ne veut pas dire avoir un site efficace."

**À l'écran :**

- texte : **LE FAUX CONFORT**
- coupe courte sur screenshot site générique
- retour face cam

**But :** identifier le piège principal. Le spectateur se reconnaît.

---

### 2:00 — 4:30 | Les 5 signaux d'un site passif

**Cadrage** : face cam + texte à l'écran pour chaque signal.

**Ce que tu dis :**

> "Voici les 5 signaux d'un site qui ne sert pas assez."

**Signal 1 — La promesse est floue**

- texte : **PROMESSE FLOUE**
- "Quand quelqu'un arrive, il doit comprendre en quelques secondes qui tu aides, sur quoi, et avec quel bénéfice."

**Signal 2 — Pas de parcours**

- texte : **PAS DE PARCOURS**
- "Le visiteur peut cliquer, mais ne sait pas quoi faire ensuite. Il arrive, il regarde, il repart."

**Signal 3 — Pas de capture**

- texte : **PAS DE CAPTURE**
- "Même avec du trafic, si ton site ne récupère rien, tu perds cette attention. Pas d'email. Pas de formulaire. Pas de suivi."

**Signal 4 — Offres mal présentées**

- texte : **OFFRE MAL POSÉE**
- "Ton site parle de toi, mais pas assez du problème du client, ni du résultat, ni de la transformation."

**Signal 5 — Pas de CTA utile**

- texte : **PAS DE CTA**
- "Un bon site ne laisse pas le visiteur flottant. Il lui propose une prochaine étape claire."

**But :** déclic fort — le spectateur coche ses propres cases.

---

### 4:30 — 5:30 | Le vrai coût

**Cadrage** : face cam, ton plus sérieux.

**Ce que tu dis :**

> "Et le problème, c'est que ce type de site ne fait pas juste 'moins bien'. Il te coûte. Du temps, parce que tu compenses ailleurs. De l'argent, parce que ton trafic convertit mal. Et de la clarté, parce que tu crois que le problème vient du SEO ou de WordPress — alors que ton système de base ne fait déjà pas le travail."

**À l'écran :**

- texte : **CE QUE ÇA COÛTE**
- trois lignes : TEMPS / ARGENT / CLARTÉ
- chaque mot apparaît avec une courte pause

**But :** élever l'enjeu. Sortir du "c'est pas grave".

---

### 5:30 — 7:00 | Ce qu'un site doit faire — les 5 rôles

**Cadrage** : face cam + texte à l'écran.

**Ce que tu dis :**

> "Pour moi, un site WordPress utile doit faire 5 choses."

1. **Clarifier** — "En quelques secondes, on doit comprendre ton positionnement et ta promesse."
2. **Orienter** — "Guider le visiteur vers une action logique. Pas lui montrer 12 portes en même temps."
3. **Capter** — "Même si la personne n'achète pas tout de suite, garder le contact."
4. **Rassurer** — "Preuves, structure, cohérence. Réduire le doute."
5. **Convertir** — "Pas forcément vendre direct. Mais faire avancer la relation."

**À l'écran :**

- chaque mot clé apparaît en gros au bon moment
- CLARIFIER / ORIENTER / CAPTER / RASSURER / CONVERTIR

**But :** donner un cadre concret et mémorable.

---

### 7:00 — 8:00 | La logique schoolsWP

**Cadrage** : face cam, ton affirmatif.

**Ce que tu dis :**

> "La logique que je défends avec schoolsWP, elle est simple : un site WordPress ne doit pas être pensé comme un assemblage de pages. Il doit être pensé comme un système. Avec une promesse claire, un parcours logique, des points de capture, des appels à l'action, et derrière, si possible, une automatisation propre. Un site seul, sans logique, c'est une façade. Relié à une vraie stratégie, ça devient un actif."

**À l'écran :**

- texte : **UN SYSTÈME, PAS DES PAGES**
- schéma simple : trafic → clarté → capture → automatisation → conversion
- logo schoolsWP discret en bas

**But :** poser ta méthode. Pas juste critiquer — proposer un cadre.

---

### 8:00 — 8:45 | Mini plan d'action

**Cadrage** : face cam, rythme rapide.

**Ce que tu dis :**

> "Donc si ton site ne te rapporte pas assez, commence simple. Pose-toi ces 5 questions."

1. Ma promesse est-elle claire dès l'arrivée ?
2. On comprend ce que je propose en quelques secondes ?
3. Il y a une prochaine étape évidente ?
4. Je capte quelque chose même si la personne n'achète pas maintenant ?
5. Mon site aide vraiment à convertir… ou juste à exister ?

**À l'écran :**

- les 5 questions en texte
- chaque question apparaît au bon moment

**But :** donner quelque chose d'actionnable immédiatement.

---

### 8:45 — 9:15 | CTA final

**Cadrage** : face cam, ton chaleureux mais direct.

**Ce que tu dis :**

> "Dis-moi en commentaire : aujourd'hui, ton site WordPress sert surtout à quoi ? À présenter ? À vendre ? À capter des leads ? Ou juste à être là ? Et si tu veux, je peux faire la suite avec une vidéo très concrète sur les éléments concrets à ajouter pour transformer un site WordPress passif en vrai levier de croissance. Abonne-toi si tu veux un WordPress qui travaille pour toi."

**À l'écran :**

- texte : **COMMENTE CI-DESSOUS**
- flèche vers la zone commentaire
- "Abonne-toi" avec icône cloche

**But :** déclencher les commentaires + abonnements.

---

### Règles de tournage

- **Phrases courtes** : une idée = une phrase = une coupe
- **Rythme nerveux** : ne pas rester sur le même plan plus de 8 secondes
- **Exemple concret** : sortir au moins un exemple visuel en partie 3 (screenshot d'un vrai site anonymisé)
- **Pas de musique forte** pendant la parole
- **Sous-titres activés** : au moins 60% regardent sans son

---

### Commentaire épinglé type

> **Question simple :**
> Aujourd'hui, ton site WordPress te sert surtout à quoi ?
>
> 1. Présenter mon activité
> 2. Générer des contacts
> 3. Vendre
> 4. Aucune idée 😅
>
> Réponds avec le chiffre. Je verrai tout de suite où vous en êtes.

---

## 99 idées YouTube schoolsWP

Classées en 10 blocs thématiques. Chaque idée est directement utilisable comme titre de travail.

---

### Bloc 1 — Fondamentaux WordPress

1. Comment créer un site WordPress utile
2. Les 5 erreurs qui rendent un site inutile
3. Refaire sa page d'accueil WordPress étape par étape
4. Comment savoir si votre site convertit vraiment
5. Les indispensables avant de lancer son site
6. WordPress pour freelance : par où commencer
7. Le vrai rôle d'un site en 2026
8. Pourquoi votre site ne vous apporte aucun client
9. Site vitrine ou machine à business : la différence
10. Les bases de WordPress sans jargon

---

### Bloc 2 — Plugins et thèmes

11. Les plugins vraiment utiles sur WordPress
12. Les plugins à éviter absolument
13. Combien de plugins faut-il sur un site WordPress
14. Comment choisir un bon thème WordPress
15. Bloc, builder ou FSE : que choisir
16. Elementor, Bricks ou Gutenberg : vrai comparatif
17. Les erreurs classiques avec les constructeurs de pages
18. Comment garder un site propre et rapide
19. Les réglages WordPress que personne ne fait
20. Mon stack WordPress idéale pour un solo business

---

### Bloc 3 — Performance

21. Comment rendre un site WordPress rapide
22. Pourquoi votre site est lent
23. Les vraies causes d'un WordPress qui rame
24. Cache, images, scripts : comprendre enfin la performance
25. Comment optimiser ses images sans tout casser
26. Les tests PageSpeed qu'il faut vraiment comprendre
27. Ce qui ralentit WordPress sans que vous le voyiez
28. Avant / après : optimisation réelle d'un site WordPress
29. Hébergement lent : comment le repérer
30. Les réglages simples qui accélèrent déjà beaucoup un site

---

### Bloc 4 — Maintenance et sécurité

31. Maintenance WordPress : ce qu'il faut faire chaque mois
32. Comment éviter de casser son site avec une mise à jour
33. Ma routine de maintenance WordPress
34. Les signes qu'un site WordPress est en danger
35. Sauvegardes WordPress : les erreurs les plus fréquentes
36. Comment sécuriser WordPress sans parano
37. Les plugins de sécurité utiles ou inutiles
38. Site piraté : que faire immédiatement
39. Comment surveiller la santé de son site
40. Maintenance WordPress : ce que vendent vraiment les pros

---

### Bloc 5 — SEO WordPress

41. SEO WordPress : les bases qui comptent
42. Pourquoi vos articles ne rankent pas
43. Comment écrire un article utile pour Google et l'humain
44. Les erreurs SEO les plus fréquentes sur WordPress
45. Rank Math, Yoast ou autre : que choisir
46. Comment construire un cocon sémantique simple
47. SEO local sur WordPress : les bases
48. Comment trouver de bons sujets d'articles
49. Le maillage interne expliqué simplement
50. Pourquoi publier ne suffit plus pour faire du trafic

---

### Bloc 6 — GEO / IA / Visibilité future

51. GEO, AIO, SEO : ce qui change vraiment
52. Comment préparer son site aux moteurs IA
53. Pourquoi certaines marques sont citées par les IA
54. Comment créer du contenu qui mérite des citations IA
55. Les nouvelles règles de visibilité sur le web
56. Le futur du SEO pour les sites WordPress
57. Ce que les créateurs doivent comprendre sur l'IA et la recherche
58. Comment structurer un contenu lisible par humains et IA
59. Les pages à fort potentiel de citation
60. WordPress est-il prêt pour l'ère IA

---

### Bloc 7 — Automatisation et marketing

61. Comment capter des emails avec WordPress
62. Les meilleurs formulaires WordPress pour convertir
63. Fluent Forms : cas d'usage concrets
64. Comment connecter son site à son CRM
65. FluentCRM pour débuter sans se perdre
66. Automatiser son marketing avec WordPress
67. Tunnel simple : page + formulaire + email + offre
68. Les automatisations qui font gagner le plus de temps
69. Comment segmenter ses contacts intelligemment
70. Les erreurs fréquentes dans les automatisations marketing

---

### Bloc 8 — Formation / LMS / Monétisation

71. Créer un espace membre sur WordPress
72. Comment vendre une formation avec WordPress
73. Tutor LMS ou autre : quoi choisir
74. Les bases d'un LMS rentable
75. Comment créer un onboarding propre pour ses élèves
76. Les erreurs qui tuent une formation en ligne
77. Automatiser les accès, emails et relances
78. Comment vendre un mini-produit sur WordPress
79. Membership, formation, service : quel modèle choisir
80. Comment transformer son site en levier de revenus

---

### Bloc 9 — Freelance et positionnement

81. Mon système WordPress pour freelances
82. Les pages indispensables pour vendre ses services
83. Comment transformer un site freelance en commercial silencieux
84. Pourquoi les freelances bricolent trop leur site
85. Le positionnement avant le design
86. Comment clarifier son offre sur son site
87. Les signaux de confiance qui font la différence
88. Comment présenter ses services sans blabla
89. Le site parfait pour un freelance WordPress existe-t-il
90. Ce que je ferais si je repartais de zéro aujourd'hui

---

### Bloc 10 — Live / Audit / Démonstration

91. Audit complet d'un site WordPress en direct
92. Refonte d'une page d'accueil en live
93. Analyse critique d'un site d'indépendant
94. Je démonte une mauvaise page de vente WordPress
95. J'optimise un site lent en direct
96. Je construis un tunnel simple de A à Z
97. Je crée une stack WordPress rentable en live
98. Ce que j'utiliserais avec 500 €, 1000 € ou 3000 €
99. De site vitrine à outil de croissance : étude de cas complète

---

### Top 12 — Meilleures vidéos pour démarrer

Sélectionnées pour leur potentiel vues + abonnés + conversion client :

1. Pourquoi votre site ne vous apporte aucun client
2. Les plugins WordPress vraiment utiles
3. Maintenance WordPress : ce qu'il faut faire chaque mois
4. Comment rendre un site WordPress rapide
5. Les 5 erreurs qui rendent un site inutile
6. Comment capter des emails avec WordPress
7. GEO, AIO, SEO : ce qui change vraiment
8. Comment clarifier son offre sur son site
9. Audit complet d'un site WordPress en direct
10. Elementor, Bricks ou Gutenberg : vrai comparatif
11. Automatiser son marketing avec WordPress
12. De site vitrine à outil de croissance : étude de cas complète

---

### 10 formats à alterner

| Format              | But                           |
| ------------------- | ----------------------------- |
| Tutoriel pas à pas  | acquisition / rétention       |
| Comparatif          | intentions chaudes            |
| Erreurs à éviter    | déclic fort                   |
| Audit en direct     | preuve d'expertise            |
| Étude de cas        | confiance + conversion        |
| Avis tranché        | personnalité + part de marché |
| Stack / outils      | affiliation + recommandation  |
| Méthode stratégique | autorité                      |
| Démonstration live  | engagement                    |
| Avant / après       | impact visuel                 |

---

### Règle d'or schoolsWP YouTube

Chaque vidéo doit toucher au moins un de ces 4 axes :

- **Clarifier** — aider à voir plus clair sur WordPress et le business
- **Structurer** — montrer comment organiser, architecturer, prioriser
- **Automatiser** — montrer comment gagner du temps avec WordPress
- **Rentabiliser** — montrer comment transformer le site en levier de revenu
