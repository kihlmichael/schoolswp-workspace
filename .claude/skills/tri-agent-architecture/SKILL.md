---
name: tri-agent-architecture
description: Architecture a 3 agents (Planner, Executor, Verifier) pour des workflows deterministes et audites. Utiliser quand l'utilisateur veut concevoir un système multi-agents fiable avec séparation planification/exécution/vérification, éviter les boucles infinies et garantir un gate humain final avant toute modification critique.
---

# Tri-Agent Architecture (Planner, Executor, Verifier)

Tu operes un modele distribue qui separe planification, execution et verification.
Objectif: fiabilite, scope controle, verification avant approbation humaine.

## Dev definition

Le modele Tri-Agent decouple le cycle d ingenierie en roles specialises:
- Planner: scope et plan
- Executor: implementation
- Verifier: validation et tests

## Implementation pattern (Claude Code + MCP)


1) Planner agent (context high, read-only)
- Inspecte repo via MCP (read/list/search)
- Produit un plan deterministe (plan.md)
- Donne criteres d acceptation

2) Executor agent (context low, write)
- Lit plan.md
- Modifie les fichiers cibles uniquement
- Utilise edit_block/write_file

3) Verifier agent (context medium, execute/read)
- Lit plan.md et criteres
- Lance tests via start_process
- Produit un rapport de verification
- Escalade au humain si echec

## Failure modes / optimization

- Infinite loop: limiter retries (ex: 3), puis escalade humaine
- Planner scope creep: max 3 fichiers sans approval
- Context rot: agents stateless, lisent plan.md + logs

## Schema (texte)

Human Engineer
  -> Planner (plan.md)
  -> Executor (edits)
  -> Verifier (tests)
  -> Human approval

## Exemple entree / sortie


Entree (exemple):
- Demande: ajouter un agent Verifier + pipeline de tests

Sortie (exemple):
- Dev definition: roles separes + plan.md
- Impact: dossiers plans/reports
- Pattern: inspect -> plan -> execute -> verify
- Failures: loop / scope creep
- Next actions: definir gates, creer prompts, tester

## Checklist (5 points)

1) Roles et limites definis
2) Plan.md + criteres d acceptation
3) Tools scopes par agent
4) Tests executes par Verifier
5) Gate humain final

## Architectural impact

- Repository: dossiers explicites (tasks/, plans/, reports/)
- Tool exposure: scope par role
- Prompt design: une phase par prompt
- Context management: tokens limites
- Reliability: verif avant validation humaine
