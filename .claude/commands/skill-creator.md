# /skill-creator

Crée ou améliore un skill Claude Code pour schoolsWP.

## Usage

```
/skill-creator <description ou arguments>
```

## Ce que fait cette commande

Invoque le skill `skill-creator` avec les arguments fournis.
Le skill-creator gère le cycle complet : draft SKILL.md → test cases → runs parallèles (with/without skill) → grading → benchmark → viewer → itération.

## Comportement

1. Lire le skill à : `d:/VS Code/CLAUDE CODE/.claude/skills/skill-creator/SKILL.md`
2. Suivre les instructions du skill-creator avec les arguments fournis
3. Si un skill existant est mentionné → mode amélioration (snapshot + baseline = ancienne version)
4. Si nouveau skill → mode création (baseline = without_skill)
5. Workspace de test : `.claude/skills/<nom-skill>-workspace/`
6. Sync registre après validation : `python .claude/skills/.registry/skills_registry.py --sync`

## Étapes standard

1. **Capture intent** — clarifier nom, trigger, sortie attendue, cas de test
2. **SKILL.md** — écrire ou améliorer dans `.claude/skills/<nom>/SKILL.md`
3. **Evals** — 2-3 prompts réalistes dans `evals/evals.json`
4. **Runs parallèles** — with_skill + without_skill (ou old_skill) simultanément
5. **Grading + benchmark** — assertions, `aggregate_benchmark.py`, `generate_review.py --static`
6. **Review** — ouvrir le viewer, attendre feedback utilisateur
7. **Itération** — améliorer si nécessaire, re-runner
8. **Sync** — `skills_registry.py --sync` une fois le skill validé

## Règles

- Workspace des skills : `d:/VS Code/CLAUDE CODE/.claude/skills/`
- Script d'agrégation : `d:/VS Code/CLAUDE CODE/.claude/skills/skill-creator/scripts/aggregate_benchmark.py`
- Viewer : `d:/VS Code/CLAUDE CODE/.claude/skills/skill-creator/eval-viewer/generate_review.py`
- Toujours utiliser `--static` pour le viewer (environnement Windows sans serveur)
- Toujours patcher PYTHONUTF8=1 pour les scripts Python sur Windows
- Ne jamais utiliser `rm` — utiliser `trash`
