---
name: note-to-sop
description: >
  Transforme une note brute, une idee vague ou un process informel en SOP claire et exploitable
  pour schoolsWP. Utilise ce skill des que l'utilisateur veut structurer un process, creer une SOP,
  documenter une procedure, transformer des notes en etapes, ou dit "SOP", "procedure", "process",
  "etapes a suivre", "documente ce workflow", "comment faire", "transforme en SOP",
  "standardise ce process", "checklist". Aussi utilisable depuis Dispatch mobile pour produire
  une SOP rapide a partir d'une note vocale ou d'un memo court.
allowed-tools:
  - Read
  - Write
---

# Note brute → SOP — schoolsWP

Tu transformes des notes brutes, des idees informelles ou des process non documentes
en SOP (Standard Operating Procedure) claires, sequentielles et directement implementables.

---

## Pourquoi ce skill existe

Les process schoolsWP (redaction, SEO, publication, prospection, formations) sont souvent
dans la tete de Michael ou eparpilles en notes. Ce skill les capture dans un format
reproductible par n'importe qui (humain ou agent IA).

---

## Entree attendue

| Entree | Comment la traiter |
|---|---|
| **Note brute** | Texte colle en vrac — extraire le process implicite |
| **Idee orale** | Description informelle — structurer en etapes |
| **Fichier** | Lire avec Read, puis structurer |
| **Process existant** | Reorganiser et standardiser |
| **Conversation** | Extraire les etapes d'un echange |

Si la note est trop vague pour en deduire un process, poser 1-2 questions maximum
avant de produire une premiere version.

---

## Structure d'une SOP schoolsWP

Toute SOP produite doit suivre cette structure exacte :

```markdown
# [Nom de la SOP]

## Objectif

[1-2 phrases : ce que cette SOP permet d'accomplir]

## Prerequis

- [Ce qu'il faut avoir/savoir avant de commencer]
- [Outils, acces, fichiers necessaires]

## Etapes

### 1. [Action en verbe imperatif]

[Instructions claires, 1-3 phrases max]

**Sortie attendue** : [ce qui doit exister apres cette etape]

### 2. [Action suivante]

[...]

### N. [Derniere action]

[...]

## Points de vigilance

- [Erreur courante a eviter]
- [Piege connu]

## Resultat attendu

[Description concrete de ce qui est produit a la fin de la SOP]

## Prochaine action

[Ce qu'on fait apres avoir termine cette SOP]
```

---

## Regles de redaction

- **Verbe imperatif** pour chaque etape ("Ouvre", "Configure", "Verifie" — pas "Il faut ouvrir")
- **Sequentiel** : chaque etape depend de la precedente
- **Concret** : pas de "penser a" ou "envisager" — des actions
- **Sortie attendue** pour chaque etape importante (ce qui doit exister apres)
- **Points de vigilance** : erreurs courantes, pas des mises en garde generiques
- **Pas de theorie** : une SOP n'est pas un guide pedagogique
- **Granularite adaptee** : ni trop haut niveau ("Fais le SEO") ni trop micro ("Clique sur le bouton bleu a droite")

---

## Adaptation par contexte

| Contexte | Adaptation |
|---|---|
| **SOP redaction** | Inclure les outils (Claude, thruuu, publish_ready), les formats de sortie |
| **SOP SEO** | Inclure les metriques cibles, les outils d'audit |
| **SOP publication** | Inclure les checklist pre-publication, les canaux de diffusion |
| **SOP technique** | Inclure les commandes exactes, les chemins de fichiers |
| **SOP prospection** | Inclure les criteres de qualification, les templates de message |
| **SOP formation** | Inclure les livrables par module, les validations |

---

## Format de sortie

```
## SOP generee

[SOP complete au format standard ci-dessus]

## Hypotheses

[Si des informations manquaient dans la note et que des hypotheses ont ete faites,
les lister ici pour validation]

## Suggestions

[1-2 ameliorations possibles de la SOP — automatisation, outil, simplification]
```

---

## Mode Dispatch Mobile

Quand le skill est invoque depuis Dispatch (mobile), produire directement la SOP
sans les sections Hypotheses et Suggestions :

```
## SOP : [Nom]

**Objectif** : [1 ligne]

**Prerequis** : [bullets]

**Etapes** :
1. [Action] → [sortie]
2. [Action] → [sortie]
3. [Action] → [sortie]

**Vigilance** : [1-2 points]

**Resultat** : [ce qui est produit]
```

Contraintes mobile : SOP lisible en 1 ecran, pas de section longue, ultra-sequentiel.
