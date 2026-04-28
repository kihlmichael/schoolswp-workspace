---
name: content-factory-autonome
description: (fusionné dans brain-autonome - archivé - ne pas auto-déclencher)
---

> **Statut : fusionné dans `brain-autonome` le 2026-04-16.**
> Ce skill ne se déclenche plus automatiquement. Toute sa logique (détection d'opportunités, seuils de décision chiffrés, boucle d'amélioration, auto-audit) a été absorbée dans `brain-autonome`.
> Pour tout arbitrage éditorial / priorisation / décision publier-optimiser-abandonner : utiliser `brain-autonome`.
> Conservation temporaire de ce fichier uniquement pour référence. Suppression manuelle à faire via l'explorateur Windows après période d'observation.

# Content Factory Autonome — schoolsWP

Tu actives une usine de contenu pilotee par score. Tu identifies quoi produire, tu priorises, tu fais produire, tu auto-audites, tu optimises et tu decides publier ou iterer. Style schoolsWP : direct, concret, phrases courtes.

## Regles de redaction

- Phrases courtes
- Bullets
- Zero blabla
- Si info manque : “Hypothese : …”

## Checklist (5 points)

1) Objectif defini en 1 phrase
2) Entrees clairement listees
3) Sorties obligatoires explicites
4) Exemple entree/sortie present
5) Actions suivantes listees

## Sortie obligatoire


Toujours produire ces sections :

1) Logique globale
2) Etape 1 — Detection d’opportunites (prompt + grille)
3) Etape 2 — Production controlee
4) Etape 3 — Auto-audit (prompt)
5) Etape 4 — Decision editoriale (regles)
6) Etape 5 — Boucle d’amelioration
7) Resultat attendu
8) Actions suivantes (3 max)

## Logique globale


Entree -> Analyse -> Priorisation -> Production -> Audit -> Optimisation -> Decision

## Etape 1 — Detection d’opportunites


### Inputs possibles
- Mot-cle cible
- Thematique (ex : CRM WordPress)
- Plugin specifique
- URL concurrent
- Cluster a developper

### Analyse obligatoire
- Intent principale
- Niveau concurrence estimee
- Opportunite business
- Complexite production
- Potentiel monetisation
- Alignement schoolsWP

### Sortie
- Score Opportunite /10
- Statut : Prioritaire / Opportunite / Secondaire / A ignorer

### Prompt — Detection opportunite

Tu es le moteur strategique schoolsWP.

Analyse l’opportunite suivante :
{SUJET}

Evalue :
- Intent principale
- Difficulté estimee
- Potentiel SEO
- Potentiel business
- Alignement avec schoolsWP
- Risque

Donne :
- Score Opportunite /10
- Recommandation claire

## Etape 2 — Production controlee


Utiliser un template adapte : Article / Comparatif / Tutoriel.
La production doit rester orientee intention + valeur business.

## Etape 3 — Auto-Audit integre


Appliquer :
1) Quick Wins SEO
2) Intent Gap Detector
3) Scoring strategique
4) Differenciation concurrentielle

### Prompt — Auto-Audit obligatoire

Analyse le contenu produit.

Applique :
1. Quick Wins SEO
2. Intent Gap Detector
3. Scoring strategique
4. Capacite de surclassement

Donne :
- Score final /10
- Corrections prioritaires
- Decision : Publier / Optimiser / Revoir angle / Abandonner

## Etape 4 — Decision editoriale


Regles :
- Score >= 8 : Publier
- Score 6 a 7,9 : Optimiser
- Score 4 a 5,9 : Revoir angle
- Score < 4 : Abandon

## Etape 5 — Boucle d’amelioration


Si Optimiser :
- Corriger gaps majeurs
- Ajouter angle differenciant
- Renforcer decisionnel
- Reevaluer score

## Resultat attendu


- Systeme editorial pilote par score
- Production priorisee
- SEO + business alignes
- Moins d’articles, plus d’impact
- Decisions rationnelles
