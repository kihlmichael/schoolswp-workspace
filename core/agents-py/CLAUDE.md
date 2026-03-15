# CLAUDE.md — core/agents-py/

Conventions spécifiques aux agents Python schoolsWP. Ce répertoire est le namespace `agents.*` (importable depuis `projects/schoolswp/`).

## Architecture d'un agent

Chaque agent = un sous-dossier avec exactement :
```
mon_agent/
├── agent.py   # classe principale héritant de BaseContentAgent
└── cli.py     # point d'entrée CLI argparse
```

Tous les agents héritent de `BaseContentAgent` (`base.py`) :
- Async — `run(**kwargs)` retourne `str` (markdown), jamais JSON
- Modèle auto-résolu : `MODEL_WRITER` env var → `claude-sonnet-4-6`
- `ANTHROPIC_API_KEY` chargé automatiquement depuis `.env` (cherche dans : `agents/.env` → `.env` → `multi-agent-system/.env`)

## Créer un nouvel agent

```python
from agents.base import BaseContentAgent

class MonAgent(BaseContentAgent):
    name = "mon-agent"
    system_prompt = "..."

    async def run(self, *, param: str, **kwargs) -> str:
        response = await self._client.messages.create(
            model=self.model,
            max_tokens=8000,
            system=self.system_prompt,
            messages=[{"role": "user", "content": param}],
        )
        return response.content[0].text
```

## Conventions CLI (cli.py)

- `argparse` uniquement — pas de `click`
- Toujours exposer `--model` et `--output`
- Sortie : `print()` vers stdout ou écriture dans `--output`
- Métadonnées après `---meta---` dans la sortie (title, description, slug)

## Agents multi-étapes (pipelines)

- Parallélisme via `asyncio.gather` pour les étapes indépendantes
- Résultats dans un `dataclass` (`PipelineResult`, `WorkflowResult`, etc.)
- Fichiers intermédiaires via `--save-dir` : nommage `v1.md`, `audit.md`, `v2.md`...

## Règle branding

Tout contenu éditorial généré doit respecter `content/docs/BRAND_RULES.md`. Le branding schoolsWP s'applique dans les system prompts, pas dans le code Python.
