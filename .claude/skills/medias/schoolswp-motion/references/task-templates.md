# Task Templates — schoolsWP Video System

> 4 templates couvrent les workflows principaux du projet video.
> Utilise le template correspondant a la tache demandee par l'utilisateur.
> Si la tache ne correspond a aucun template, suis quand meme le workflow
> obligatoire du SKILL.md (Diagnostic → Plan → Execution → QA → Suite).

---

## Template 1 — Creer une composition

### Informations a collecter

Avant de commencer, obtenir ou deduire :

- Nom souhaite de la composition
- Objectif de la video
- Duree cible
- Format (1920x1080 par defaut)
- FPS (THEME.fps par defaut)
- Ambiance
- Elements a afficher
- Texte exact a afficher
- Assets a utiliser
- Presence audio (oui / non)
- Dossier de sortie vise (previews / finals)
- Contraintes specifiques

### Methode de travail

1. Analyser l'existant (compositions, composants, assets)
2. Verifier les assets et composants reutilisables
3. Proposer la structure de la composition
4. Creer ou modifier les fichiers necessaires
5. Declarer la composition dans Root.tsx
6. Preparer la commande de rendu
7. Faire une QA de premier niveau

### Regles specifiques

- Respecter l'univers schoolsWP (calme, premium, lisible)
- Reutiliser les composants existants si pertinent
- Centraliser les constantes dans theme.ts
- Centraliser les textes dans texts.ts
- Eviter les duplications inutiles
- Privilegier une animation sobre et premium

### Format de reponse

```
## Diagnostic
- ce qui existe deja
- ce qui peut etre reutilise
- ce qui manque
- risques eventuels

## Plan d'action
- etapes de creation
- ordre d'execution

## Fichiers impactes
- crees
- modifies
- laisses intacts

## Commandes executees
- commandes reellement lancees
- ou indiquer explicitement si aucune

## Resultat
- composition creee ou non
- rendu lance ou non
- limites eventuelles

## QA
- branding
- lisibilite
- timing
- structure
- export

## Suite recommandee
- prochaine etape prioritaire
```

---

## Template 2 — Ameliorer une composition existante

### Informations a collecter

- Composition concernee
- Objectif de l'amelioration
- Ce qui doit progresser (rythme, lisibilite, hierarchie, impact, branding, fluidite)
- Contraintes a respecter
- Niveau de modification autorise (leger / moyen / refonte partielle)

### Obligations d'analyse

Avant de modifier, preciser :

- l'intention actuelle de la composition
- ce qui fonctionne deja
- ce qui ne fonctionne pas
- ce qui doit rester intact
- ce qui peut etre simplifie ou extrait

### Pour chaque amelioration proposee, preciser

- l'intention
- ce qui change visuellement
- l'impact sur la lisibilite
- l'impact sur le rythme
- l'impact sur la coherence de marque
- le risque eventuel

### Regles specifiques

- Ne pas casser la structure existante
- Justifier chaque changement visuel
- Eviter les effets gadgets
- Garder une logique maintenable
- Verifier la lisibilite sur le fond utilise
- Signaler clairement tout risque introduit

### Format de reponse

```
## Diagnostic
- etat actuel
- points forts
- points faibles
- elements a preserver

## Ce qui ne va pas actuellement
- problemes concrets observes
- priorisation des defauts

## Plan d'action
- corrections prevues
- ordre logique
- justification

## Fichiers impactes
- crees / modifies / deplaces / renommes / laisses intacts

## Commandes executees
- commandes reellement lancees ou indiquer si aucune

## Resultat
- ce qui a ete ameliore
- ce qui reste a verifier
- rendu genere ou non

## QA
- branding, lisibilite, timing, structure, export, risques residuels

## Suite recommandee
- prochaine action utile
```

---

## Template 3 — Organiser le workflow

### Mission

Structurer le workflow video schoolsWP : securiser les inputs, clarifier l'arborescence,
faciliter les rendus et fiabiliser la QA.

### Ce que tu dois faire

- Analyser l'arborescence actuelle
- Reperer le flou, les duplications, les risques
- Proposer une structure cible simple et maintenable
- Recommander les renommages utiles
- Creer les dossiers manquants si pertinent
- Proposer une logique de rendu et d'archivage
- Proposer une logique de QA
- Documenter les conventions de nommage
- Signaler les zones de risque

### Priorites

1. clarte
2. stabilite
3. maintenabilite
4. tracabilite
5. vitesse d'execution en production

### Contraintes

- Ne pas renommer inutilement
- Ne pas complexifier le projet
- Conserver une structure exploitable rapidement par un humain
- Eviter les dossiers ambigus

### Format de reponse

```
## Etat actuel
- structure observee, logique existante, points deja propres

## Problemes reperes
- flou, duplication, risques, incoherences, fragilites

## Structure cible
- arborescence recommandee
- logique de rangement
- responsabilites de chaque dossier

## Changements proposes
- a creer / renommer / deplacer / laisser tel quel

## Fichiers / dossiers impactes
- creations, modifications, deplacements, renommages

## Scripts utiles
- scripts proposes, role, usage recommande

## Convention de nommage
- assets, compositions, exports, logs

## Checklist QA
- branding, technique, motion, son, export

## Suite recommandee
- prochaine action structurante prioritaire
```

---

## Template 4 — Rendu, QA et export

### Informations a collecter

- Composition a rendre
- Nom de sortie souhaite
- Type de sortie (preview / final)
- Version souhaitee
- Audio present (oui / non)
- Dossier cible
- Contraintes specifiques

### Verifications pre-rendu

- Assets reellement presents
- Textes affiches
- Casse exacte de schoolsWP
- Dimensions, fps, duree
- Lisibilite du logo et de l'URL
- Coherence des couleurs
- Coherence du nom de fichier

### Ce que tu dois faire

- Verifier le pre-rendu
- Proposer la commande correcte
- Lancer le rendu si necessaire
- Signaler tout probleme technique
- Faire une QA post-rendu
- Recommander le nom de fichier final
- Recommander l'emplacement de sortie
- Indiquer si logguer dans render-log.md

### Format de reponse

```
## Verifications pre-rendu
- assets, textes, branding, parametres techniques, points de risque

## Commandes executees
- commandes reellement lancees ou indiquer si aucune

## Resultat
- rendu genere ou non, emplacement, erreurs, statut global

## QA post-rendu
- branding, lisibilite, timing, structure, export, son si applicable

## Nom de fichier final recommande
- nom exact, justification rapide

## Emplacement recommande
- preview / final / archive, justification rapide

## Suite recommandee
- prochaine action la plus logique
```

---

## Rappel global

Dans toutes les taches :

- toujours ecrire **schoolsWP** avec WP en majuscules
- ne jamais supposer un asset correct sans verification
- ne jamais annoncer un rendu comme valide sans QA minimale
- toujours distinguer **Confirme** / **A verifier** / **Recommande** / **Bloquant**
- toujours privilegier la lisibilite, la coherence et la maintenabilite
- toujours recommander une seule prochaine etape prioritaire
