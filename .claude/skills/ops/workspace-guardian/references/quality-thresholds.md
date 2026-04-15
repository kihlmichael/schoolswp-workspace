# Seuils de qualité — schoolsWP Workspace

## Tests

| Métrique | Seuil minimum | Cible | Critique |
|----------|---------------|-------|----------|
| Couverture globale | 20% | 50% | Non |
| Couverture code critique | 30% | 60% | Oui |
| Tests par agent | 1 | 3+ | Oui |
| Tests d'intégration | 1 par workflow | 2+ | Non |
| Temps d'exécution tests | < 60s | < 30s | Non |

## Définition de "code critique"

Le code critique inclut :
- Tout agent qui interagit avec une API externe
- Tout module qui manipule des données utilisateur
- Tout script de déploiement
- Tout code de synchronisation WordPress

## Pre-commit hooks

### Obligatoires

1. **Linting Python** : `flake8` ou `ruff`
2. **Linting JS** : `eslint`
3. **Formatage** : `black` (Python), `prettier` (JS)
4. **Tests** : exécution des tests unitaires

### Recommandés

5. **Détection de secrets** : `detect-secrets`
6. **Vérification types** : `mypy` (Python)

## Configuration `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.4.0
    hooks:
      - id: detect-secrets
```

## Revue de code — Checklist

Avant chaque merge sur `main` :

- [ ] Au moins un test nouveau ou mis à jour
- [ ] Pas de `TODO` sans ticket associé
- [ ] Pas de credentials ou secrets dans le code
- [ ] Le CHANGELOG est mis à jour
- [ ] La documentation est à jour si nécessaire
- [ ] Le code suit les conventions de nommage
