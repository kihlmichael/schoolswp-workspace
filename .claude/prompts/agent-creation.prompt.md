# Création Agent Python schoolsWP

Guide de création d'un nouvel agent Python dans core/agents-py/.

## Input
Nom de l'agent : $ARGUMENTS

## Checklist de création

### 1. Structure fichiers
```
core/agents-py/{agent-name}/
├── __init__.py
├── agent.py      # Classe héritant de BaseContentAgent
└── cli.py        # Entry point argparse
```

### 2. agent.py — Template
- Hériter de `BaseContentAgent`
- Définir `name`, `system_prompt`, `max_tokens`
- Implémenter `async def run(self, **kwargs) -> str`
- Retourner du markdown

### 3. cli.py — Template
- `safe_read_path()` / `safe_write_path()` pour tout chemin
- Logger : `logging.getLogger("agents.{agent-name}")`
- `asyncio.run(main())` en entry point

### 4. Tests
- Créer `tests/test_{agent_name}_contract.py`
- Tester le contrat : héritage, signature run(), retour markdown
- Utiliser `mock_anthropic_client` fixture

### 5. Documentation
- Ajouter dans la table des modules de `.claude/rules/python-agents.md`
- Ajouter le system prompt dans `core/agents-md/`

## Lancer après création
```bash
.venv/Scripts/python -m ruff check core/agents-py/{agent-name}/
.venv/Scripts/python -m pytest tests/test_{agent_name}_contract.py -v
```
