# apps/ — Classification des sous-applications schoolsWP

Derniere classification : 2026-03-25

## Structure

```
apps/
├── vscode-agent-visual/    # ACTIF — seule app en developpement
├── brand-reveal/           # PROTOTYPE LOURD — Remotion + React Three Fiber (2.6 GB deps)
├── video-marketing/        # PROTOTYPE LOURD — Remotion 7 scenes (2.0 GB deps)
├── telegram-bot/           # ARCHIVE — config VPS seulement (non tracke)
└── _archive/               # ARCHIVE — squelettes inactifs, code preserve
    ├── claude-telegram-poc/    # Python — POC Telegram + Claude CLI
    ├── elearning/              # Node.js — Pipeline ElevenLabs + HeyGen (squelette)
    └── thruuu-claude-writer/   # Markdown — Guidelines redaction (migre dans .claude/docs/)
```

## Classification

| App | Statut | Stack | Fichiers git | Action |
|-----|--------|-------|-------------|--------|
| **vscode-agent-visual** | Actif | TypeScript + esbuild (VS Code ext) | 18 | Maintenu |
| claude-telegram-poc | Archive | Python (telegram + claude) | 5 | `_archive/` |
| elearning | Archive | Node.js (ElevenLabs + HeyGen) | 5 | `_archive/` |
| thruuu-claude-writer | Archive | Markdown/guidelines | 2 | `_archive/` |
| telegram-bot | Archive | Node.js (pm2/ccpa) | 0 (non tracke) | A deplacer dans `_archive/` |
| brand-reveal | Prototype lourd | Remotion + React Three Fiber + Three.js | 17 | node_modules gitignore |
| video-marketing | Prototype lourd | Remotion + React | 22 | node_modules gitignore |

## Criteres

- **Actif** : en developpement, modifie recemment, necessaire au workflow
- **Archive** (`_archive/`) : squelette <10 fichiers, inactif >30j, pas de deps lourdes
- **Prototype lourd** : node_modules lourdes (Remotion/Three.js), source trackee, deps non committees — `npm install` pour reactiver

## Prototypes Remotion — comment utiliser

```bash
cd apps/brand-reveal/brand-reveal && npm install && npm run studio
cd apps/video-marketing/video-marketing && npm install && npm run studio
```

## Impact

- **Avant** : 7 apps, ~5.6 GB de deps locales (node_modules + venv), bruit dans IDE
- **Apres** : 1 app active (311 MB deps), 3 archivees (0 deps), 1 a archiver, 2 prototypes (4.6 GB deps gitignores)
- Reduction surface active : **7 → 1 app**
