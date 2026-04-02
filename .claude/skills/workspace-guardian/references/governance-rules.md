# Règles de gouvernance — schoolsWP Workspace

## Principes fondamentaux

1. **main = stable** : aucun commit direct, uniquement des merges via PR
2. **Un skill, un chemin** : `.claude/skills/` est le seul emplacement autorisé
3. **Conventional commits** : `type(scope): description`
4. **Tags sémantiques** : `vMAJEUR.MINEUR.PATCH` sur chaque merge main
5. **Zéro fichier orphelin** : pas de `patch_*`, `temp_*`, `backup_*` à la racine

## Nommage

| Élément | Convention | Exemple |
|---------|------------|---------|
| Branches | kebab-case avec préfixe | `feature/sync-wordpress` |
| Skills | kebab-case | `workspace-guardian` |
| Fichiers Python | snake_case | `sync_agent.py` |
| Fichiers JS/TS | camelCase ou kebab-case | `syncAgent.js` |
| Dossiers | kebab-case | `data-exports/` |

## Arborescence cible

```
schoolswp/
├── .claude/
│   ├── skills/
│   └── settings.json
├── agents/
├── apps/
├── data/
│   ├── raw/
│   ├── processed/
│   └── exports/
├── docs/
│   ├── lessons.md
│   ├── agents-registry.md
│   ├── deploy-to-wordpress.md
│   └── CHANGELOG.md
├── scripts/
│   └── patches/
├── tests/
├── _archive/
├── .pre-commit-config.yaml
├── .github/
│   └── workflows/
└── README.md
```

## Processus de merge

1. Créer une branche `feature/`, `fix/` ou `chore/`
2. Développer et commiter avec conventional commits
3. Vérifier que les tests passent
4. Créer une PR vers `main`
5. Relire le diff
6. Merger et taguer

## Processus d'archivage

1. Identifier le contenu à archiver
2. Déplacer dans `_archive/` avec préfixe date : `2026-03-24_nom-du-dossier/`
3. Ajouter une entrée dans le CHANGELOG
4. Commiter : `chore(archive): archiver [description]`
