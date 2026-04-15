# Apps schoolsWP — Inventaire

Applications actives dans `apps/`. Chaque app est un sous-projet autonome avec son propre package.json ou venv.

## Apps actives

| App | Stack | Rôle |
|---|---|---|
| **video-marketing** | Remotion (Node.js) | Génération de vidéos marketing programmatiques. `theme.ts` + `texts.ts` = source de vérité. CLAUDE.md dédié. |
| **vscode-agent-visual** | VS Code extension (TypeScript + esbuild + Canvas) | Avatars animés pilotés par Claude Code dans VS Code. postMessage IPC. CLAUDE.md dédié. |
| **brand-reveal** | Node.js | App de brand reveal schoolsWP. |
| **claude-md-generator** | HTML/CSS/JS statique | Générateur de fichiers CLAUDE.md. |
| **claude-telegram-poc** | Python (venv) | POC d'intégration Telegram + Claude. |
| **telegram-bot** | Node.js | Bot Telegram opérationnel. |

## Archivé

- `apps/_archive/` — versions legacy
- `apps/_prototypes/` — expérimentations

## Apps avec CLAUDE.md dédié (sous-règles auto-chargées)

- `apps/video-marketing/CLAUDE.md` — governance theme.ts/texts.ts, protocole QA
- `apps/vscode-agent-visual/CLAUDE.md` — architecture extension, postMessage, Canvas

## Commandes type

```bash
# video-marketing
cd apps/video-marketing && npm install && npm run build

# vscode-agent-visual
cd apps/vscode-agent-visual && npm install && npm run compile
```

## À savoir

- Chaque app active peut avoir son propre package.json et ses propres déps npm
- Les CLAUDE.md par app sont auto-chargés quand tu édites dedans
- Les apps `_archive/` et `_prototypes/` sont masquées du workspace VS Code
