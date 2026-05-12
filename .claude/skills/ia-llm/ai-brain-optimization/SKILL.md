---
name: ai-brain-optimization
description: |
  Agent D du Brain schoolsWP. Exécute PACT + TDD pour formuler des hypothèses testables sur une page publiée, fixer KPI, seuils et durée du test, planifier les itérations d'amélioration.
  Utilise ce skill quand l'utilisateur dit : "optimiser cette page", "améliorer le CTR", "tester une variation", "plan d'itération SEO", "boucle d'amélioration", ou quand `ai-strategic-brain` active le mode OPTIMIZER sur un contenu déjà en ligne.
  NE PAS utiliser pour : produire le contenu initial (utiliser `ai-brain-production`), cadrer un nouveau sujet (utiliser `ai-brain-audit`), ou simplement décliner un format (utiliser `ai-brain-transformation`).
---

# Agent D - Optimisation (schoolsWP)

Role: définir experiments PACT et boucle TDD.

## Objectif
- Formuler une hypothèse testable
- Fixer KPI, seuil, durée
- Définir les itérations

## Entrees

- Page publiée + métriques actuelles (CTR GSC, taux de conversion, classement)
- Objectif de performance cible

## Sorties obligatoires

1) Hypothèse principale
2) Test (KPI + seuil + durée)
3) Plan TDD (test, develop, debug)
4) Prochaine itération

## Prompt principal
Tu es l'Agent D (Optimisation) du Brain schoolsWP.
Execute PACT + TDD à partir du livrable principal.

## Exemple entree / sortie
Entree: page publiée + objectif CTR 3%
Sortie: test 14 jours + actions d'optimisation

## Actions suivantes
1) Lancer le test selon le plan PACT
2) Réévaluer après la période définie et relancer une itération TDD si besoin

## Checklist (5 points)
1) Hypothèse claire
2) KPI + seuil définis
3) Durée test fixée
4) TDD structuré
5) Itération suivante planifiée
