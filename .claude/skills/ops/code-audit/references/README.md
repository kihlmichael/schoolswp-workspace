# Code Audit Procedures

Procédures détaillées pour chaque type d'analyse de l'audit de code.

## Procédures disponibles

| Procédure | Description |
|-----------|-------------|
| [duplication-analysis.md](duplication-analysis.md) | Détection du code dupliqué |
| [todo-detection.md](todo-detection.md) | Scanner et classifier les TODO/FIXME |
| [pattern-consistency.md](pattern-consistency.md) | Détecter les incohérences de patterns |
| [dependency-audit.md](dependency-audit.md) | Identifier les dépendances inutilisées |

## Workflow complet

```
1. Préparation
   ├── Détecter langage
   ├── Identifier structure
   └── Configurer exclusions

2. Analyses (parallèles)
   ├── duplication-analysis.md
   ├── todo-detection.md
   ├── pattern-consistency.md
   └── dependency-audit.md

3. Consolidation
   ├── Regrouper findings
   ├── Calculer sévérités
   └── Estimer efforts

4. Rapport
   └── Générer MD + JSON
```

## Usage

Chaque procédure peut être exécutée indépendamment ou comme partie de l'audit complet.

### Audit complet

```
/code-audit .
```

### Audit ciblé

```
/code-audit . --only duplication
/code-audit . --only todo
/code-audit . --only patterns
/code-audit . --only dependencies
```

---

Retour à [SKILL.md](../SKILL.md)
