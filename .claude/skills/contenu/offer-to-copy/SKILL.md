---
name: offer-to-copy
description: |
  Transforme une offre technique schoolsWP (produit, compétence, feature, formation, playbook) en
  positionnement marketing B2B complet et prêt à publier : promesse de transformation, problème
  prospect, bénéfices business, crédibilité, post LinkedIn, landing page courte et pitch produit.
  Utilise ce skill dès que l'utilisateur mentionne : transformer une offre en message, écrire le
  marketing d'un produit, positionner une feature, rédiger un pitch, créer un post de lancement,
  vendre une compétence ou une formation, copywriting d'offre, message de vente, ou fournit une
  description technique à transformer en argumentaire commercial.
  Ne pas utiliser pour : rédiger un article de blog (→ content-studio), réécrire un texte existant
  dans le ton schoolsWP (→ branding-studio), ou faire un audit SEO.
---

# offer-to-copy

Transforme une offre technique schoolsWP en positionnement marketing crédible + 3 messages prêts à publier.

## Philosophie

Ce skill vend une **transformation business**, pas une fonctionnalité.

La différence fondamentale :
- Feature-led : "Dashboard Google Ads en 30 secondes"
- Offer-led : "Tu passes moins de temps à produire le rapport, et plus de temps à défendre tes décisions médias"

Chaque sortie de ce skill doit répondre à la question du prospect : **"Qu'est-ce que ça change dans mon business ?"** — pas seulement "Qu'est-ce que ça fait ?"

## Positionnement

Ce skill fait du **copywriting de positionnement B2B**, pas de la rédaction de contenu. La différence :

- **content-studio** structure du contenu éditorial (articles, newsletters)
- **branding-studio** applique la voix schoolsWP à n'importe quel texte
- **offer-to-copy** extrait la valeur commerciale d'une offre technique et la traduit en messages qui donnent envie d'acheter ou d'essayer — avec crédibilité

Le livrable final est un document de positionnement marketing complet, directement exploitable pour LinkedIn, une landing page ou un pitch.

## Input accepté

L'utilisateur fournit :

1. **Description de l'offre** — texte libre décrivant ce que fait le produit/la compétence/la feature (fonctionnalités, mécanisme, stack)
2. **Audience cible** — qui sont les prospects (rôles, contexte, taille d'entreprise)
3. **Problème résolu** — ce que le prospect fait aujourd'hui sans la solution (optionnel — le skill peut le déduire)

L'input peut être :
- du texte libre dans le prompt
- un fichier markdown (`--file chemin/vers/brief.md`)
- un mix des deux

Si l'audience ou le problème manquent, les déduire de la description technique. Ne poser qu'une seule question de clarification si vraiment nécessaire — sinon, avancer.

## Process en 9 étapes

Suivre ces étapes dans l'ordre exact. Chaque étape produit un bloc du livrable final.

### Étape 1 — Promesse centrale (transformation, pas feature)

Identifier la promesse marketing la plus forte de l'offre.

Critères :
- Compréhensible en moins de 5 secondes par un décideur
- **Orientée transformation business** — pas juste un gain de temps ou une suppression de tâche, mais ce que ce gain permet de faire en plus (mieux analyser, mieux servir ses clients, standardiser, scaler, facturer)
- Concrète et crédible — pas de superlatif non prouvable
- Une seule phrase

Mauvais (feature-led) : "Ton rapport Google Ads en 30 secondes."
Bon (offer-led) : "Ton reporting Google Ads standardisé et client-ready, sans export ni mise en forme."

La promesse doit répondre à : "Qu'est-ce que ça change dans mon business ?" — pas seulement dans ma semaine.

### Étape 2 — Cible précise

Avant de décrire le problème, affiner la cible. "Agences et consultants" est trop vague.

Préciser :
- **Rôle exact** — freelance SEA, petite agence paid media, consultant acquisition, blogueur affilié, formateur WordPress...
- **Contexte** — taille d'équipe, nombre de clients/comptes, niveau technique
- **Moment de douleur** — quand exactement cette personne ressent le problème (chaque lundi matin, à chaque nouveau client, en début de trimestre...)

Format : 2-3 lignes descriptives, pas une liste abstraite.

### Étape 3 — Problème prospect reformulé

Décrire le problème actuel du prospect de manière concrète et visuelle. Le lecteur doit se reconnaître immédiatement.

Technique : décrire une scène du quotidien, pas un concept abstrait. Montrer les gestes, les outils, les frustrations.

Mauvais : "Les équipes marketing manquent de visibilité sur leurs performances publicitaires."
Bon : "Chaque lundi, tu ouvres Google Ads, tu exportes un CSV, tu l'importes dans Sheets, tu crées un tableau croisé, tu fais 3 graphiques, tu mets en forme. Deux heures plus tard, tu as un rapport que ton client mettra 90 secondes à parcourir."

Court paragraphe — 3 à 5 phrases max.

### Étape 4 — Pourquoi le workflow actuel ne fonctionne plus

Lister 3 à 5 points expliquant pourquoi la méthode actuelle est problématique.

Chaque point couvre un angle différent parmi :
- **Temps perdu** — quantifier avec prudence ("environ X heures", "entre X et Y")
- **Répétition** — même travail chaque semaine/mois
- **Fragilité** — erreurs manuelles, formules cassées
- **Fatigue mentale** — charge cognitive inutile
- **Lenteur de décision** — le temps entre la donnée et l'action
- **Coût d'opportunité** — ce que ce temps empêche de faire (analyser, optimiser, prospecter)

Inclure aussi : **quelles alternatives le prospect a déjà envisagées** (Looker Studio, AgencyAnalytics, Sheets templates, etc.) et pourquoi elles ne résolvent pas tout.

Format : liste à puces, une phrase par point, directe.

### Étape 5 — Présentation simple de la solution

Présenter la solution en un court paragraphe (3-4 phrases).

Règles :
- Commencer par ce que l'utilisateur fait (l'action)
- Puis ce qu'il obtient (le résultat business, pas technique)
- **Zéro jargon technique dans le message commercial** — les noms de protocoles (MCP, API, SDK), de frameworks ou de stack n'ont rien à faire dans l'argumentaire principal. Le prospect veut savoir si c'est fiable, simple et utile — pas comment c'est branché
- Donner l'impression que c'est simple et fiable, sans promettre la magie

Le lecteur doit se dire : "Ça a l'air sérieux et faisable."

**Formulations interdites dans cette section :**
- "en X secondes" (sauf si mesuré et prouvable)
- "sans aucune compétence technique"
- "compatible avec tous les X"
- "c'est terminé" / "c'est fini"
- Tout absolu non démontré

### Étape 6 — Fonctionnalités → Bénéfices → Impact business

Transformer chaque fonctionnalité importante en bénéfice concret, puis en impact business.

Présenter sous forme de tableau markdown à 3 colonnes :

| Fonctionnalité | Bénéfice immédiat | Impact business |
| --- | --- | --- |
| Connexion données live | Tu travailles avec les vrais chiffres, pas un export d'hier | Tes recommandations sont basées sur des données fraîches — plus crédibles côté client |
| Dashboard HTML interactif | Tu envoies un lien, pas un fichier Sheets | Le client perçoit un reporting plus pro — meilleure rétention |

Règles de transformation :
- La colonne "Bénéfice" parle de temps gagné, lisibilité, confort
- La colonne "Impact business" parle de revenus, crédibilité, scalabilité, facturation, rétention client
- Utiliser "tu" — pas "l'utilisateur" ou "les équipes"
- Chaque ligne doit être vérifiable — pas de "meilleure expérience"
- 5 à 7 lignes max

### Étape 7 — Différenciants clés (vs alternatives réelles)

Lister les 4 à 6 éléments qui rendent cette offre différente **des alternatives que le prospect connaît déjà** (pas juste "faire à la main").

Pour chaque différenciant, nommer implicitement ou explicitement l'alternative battue.

Format : liste à puces, une phrase par point.

**Formulations interdites :**
- "le seul" / "la seule" (sauf si vérifiable à 100%)
- "le premier" (idem)
- "aucun autre" (idem)

Préférer : "contrairement à X, ici tu..." ou "là où X demande Y, ici tu..."

### Étape 8 — Crédibilité et limites honnêtes

Cette section est ce qui sépare une bonne offre d'une offre crédible. Elle contient :

**Éléments de confiance** (au moins 2 parmi) :
- Un scénario d'usage concret avec des chiffres réalistes (pas un claim absolu)
- Ce que l'outil ne remplace PAS (le jugement humain, la stratégie, la personnalisation)
- Ce qui reste à faire côté utilisateur après utilisation
- Les pré-requis réels (compte actif, config minimale, compétences de base)

**Limites honnêtes** (au moins 1) :
- Ce que l'offre ne fait pas encore
- Les cas où elle n'est pas adaptée
- Les conditions pour que ça fonctionne vraiment

Le ton n'est pas défensif — c'est de la transparence qui renforce la crédibilité. Un prospect qui voit les limites fait davantage confiance aux promesses.

### Étape 9 — 3 messages finaux

Rédiger 3 versions distinctes du message marketing. Chaque version doit **intégrer la couche crédibilité** — pas seulement la promesse et les bénéfices.

#### A. Post LinkedIn

Structure :
1. **Accroche** — une phrase choc qui arrête le scroll (question, constat, chiffre)
2. **Problème** — 2-3 phrases qui décrivent la douleur
3. **Solution** — 2-3 phrases qui présentent l'offre (sans jargon technique)
4. **Preuve / crédibilité** — 1 détail concret qui inspire confiance (scénario réel, chiffre mesuré, limite honnête)
5. **CTA** — une action simple (commenter, DM, lien)

Longueur : 150-250 mots. Tutoiement. Pas de hashtags dans le corps du texte — les mettre à la fin si pertinents (3 max).

#### B. Landing page courte

Structure :
1. **Headline** — promesse de transformation en une phrase
2. **Sous-titre** — pour qui + contexte en une phrase
3. **Problème** — 3-4 lignes
4. **Solution** — 3-4 lignes (sans noms techniques)
5. **Bénéfices** — 3-4 puces orientées impact business
6. **Comment ça marche** — 3 étapes numérotées (ultra-simples)
7. **Ce que ça ne remplace pas** — 1 phrase de transparence qui renforce la confiance
8. **CTA principal** — bouton + micro-texte de réassurance

Longueur : 200-350 mots total. Style direct, aéré, scannable.

#### C. Pitch produit court

Un paragraphe de 4-6 phrases qui résume : ce que c'est, pour qui exactement, la transformation business, et une limite honnête qui crédibilise.

Utilisable en DM, en intro d'email, en description de playbook. Doit fonctionner seul, sans contexte.

## Contraintes de style (non négociables)

1. **Phrases courtes** — 8 à 15 mots en moyenne, jamais plus de 20
2. **Vocabulaire simple** — si un mot de 3 syllabes fait le travail, ne pas en utiliser un de 5
3. **Ton confiant mais honnête** — affirmer ce qui est vrai, nuancer ce qui dépend du contexte. Jamais arrogant, jamais timide
4. **Transformation avant technique** — toujours expliquer ce que ça change dans le business avant d'expliquer comment ça marche
5. **Zéro remplissage** — chaque phrase doit aider à vendre ou à comprendre. Si elle ne fait ni l'un ni l'autre, la supprimer
6. **Pas de hype IA** — ne pas écrire "powered by AI", "IA révolutionnaire", "magie de l'IA". L'IA est le mécanisme, pas l'argument de vente
7. **Pas de sur-promesses** — les absolus non prouvés détruisent la crédibilité. Voir la liste des formulations interdites ci-dessous
8. **Tutoiement** — systématique, naturel
9. **Orthographe** — toujours "schoolsWP" (jamais SchoolsWP, Schools WP, etc.)
10. **Jargon technique en coulisse** — les noms de protocoles, SDK, API, frameworks ne doivent jamais apparaître dans les messages commerciaux. Ils peuvent figurer dans une note technique à part si demandé

### Formulations interdites

Ces patterns cassent la crédibilité. Ne jamais les utiliser :

- "en X secondes" / "en moins de X minutes" (sauf si mesuré et prouvable — préférer "en quelques minutes" ou "rapidement")
- "le seul" / "la seule" / "le premier" (sauf monopole vérifiable)
- "sans aucune compétence" / "aucun prérequis"
- "compatible avec tous les X"
- "c'est terminé" / "c'est fini" / "tu n'auras plus jamais à"
- "révolutionnaire" / "game-changer" / "disruptif"
- "powered by AI" / "magie de l'IA"
- "100% automatique" / "entièrement automatisé"
- "copy de qualité à chaque fois" (qualité subjective + absolu)

Préférer les formulations calibrées :
- "en quelques minutes" au lieu de "en 30 secondes"
- "une base solide à personnaliser" au lieu de "prêt à publier tel quel"
- "accélère fortement la production" au lieu de "100% automatisé"
- "pensé pour les comptes standards" au lieu de "compatible avec tous"
- "la seule formation FR structurée à ce jour" au lieu de "la seule" tout court

## Auto-vérification avant livraison

Avant de produire le livrable final, vérifier silencieusement ces 8 points :

1. La promesse vend une transformation business, pas juste un gain de temps
2. La cible est précise — on voit la personne, pas une catégorie abstraite
3. Les bénéfices sont plus visibles que la technique dans chaque section
4. Le problème prospect semble réel, spécifique et douloureux — pas générique
5. Les différenciants se comparent à de vraies alternatives, pas juste au "faire à la main"
6. **Il y a au moins un élément de crédibilité / limite honnête** dans le livrable
7. **Aucune formulation interdite** n'apparaît dans les messages finaux
8. Chaque version message (LinkedIn, landing, pitch) est directement publiable et crédible

Si un point échoue, corriger avant de livrer.

## Structure du livrable final

Produire un seul document markdown avec exactement cette structure :

```
# [Nom de l'offre] — Positionnement marketing

## 1. Promesse centrale
[une phrase — transformation business]

## 2. Cible
[2-3 lignes — profil précis + moment de douleur]

## 3. Problème prospect
[paragraphe court — scène du quotidien]

## 4. Pourquoi le workflow actuel ne fonctionne plus
- [point 1]
- [point 2]
- [...]
- Alternatives envisagées : [X, Y] — et pourquoi elles ne suffisent pas

## 5. La solution
[paragraphe court — sans jargon technique]

## 6. Fonctionnalités → Bénéfices → Impact business
| Fonctionnalité | Bénéfice immédiat | Impact business |
| --- | --- | --- |
| ... | ... | ... |

## 7. Différenciants clés
- [vs alternative X : ...]
- [...]

## 8. Crédibilité et limites
- Scénario type : [...]
- Ce que ça ne remplace pas : [...]
- Pré-requis : [...]

## 9. Messages finaux

### A. Post LinkedIn
[texte complet]

### B. Landing page courte
[texte complet]

### C. Pitch produit court
[texte complet]
```

## Ce que ce skill ne fait PAS

- Il ne rédige pas d'article de blog → utiliser `content-studio`
- Il ne corrige pas le ton d'un texte existant → utiliser `branding-studio`
- Il ne fait pas d'audit SEO → utiliser `seo-audit`
- Il ne crée pas de séquence email → utiliser le skill `marketing`
- Il ne traduit pas en anglais — tout le livrable est en français
