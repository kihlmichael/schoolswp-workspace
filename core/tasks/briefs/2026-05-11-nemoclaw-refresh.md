# Brief nemoclaw-workspace-refresh — 2026-05-11

Routine lundi 9h. Mode : read-only par défaut, écriture uniquement sur artefacts reproductibles, jamais de suppressions destructives ni de sudo. Confirmation Michael avant toute suppression de fichier unique ou contenu.

## Contexte shell

Tu peux opérer depuis PowerShell ou depuis WSL. Attention au piège venv.

**PowerShell Windows** : activer le venv via Activate.ps1, ou invoquer le binaire interpréteur du venv directement.

~~~
.venv\Scripts\Activate.ps1
.venv\Scripts\python.exe -m <module>
~~~

**WSL** : le venv Windows ne s'active pas via la commande source. Invoquer le binaire Windows par chemin complet.

~~~
/mnt/d/VS\ Code/CLAUDE\ CODE/projects/schoolswp/.venv/Scripts/python.exe -m <module>
~~~

**Ne PAS** tenter d'activer le venv depuis WSL, ça échoue silencieusement (incident 2026-05-11 09h17).

## 1. Intégrité CLAUDE.md + skills

### Fichiers à valider (présence + lecture + pas tronqués)

- `D:\VS Code\CLAUDE CODE\CLAUDE.md` (workspace racine)
- `D:\VS Code\CLAUDE CODE\projects\schoolswp\CLAUDE.md` (projet)
- `D:\VS Code\CLAUDE CODE\projects\schoolswp\CLAUDE.local.md` (overrides, peut être vide)
- Sub-CLAUDE.md auto-chargés :
  - `core/agents-py/CLAUDE.md`
  - `systems/n8n/CLAUDE.md`
  - `apps/video-marketing/CLAUDE.md`
  - `apps/vscode-agent-visual/CLAUDE.md`

### Checks

- [ ] Chaque fichier > 0 octets, pas de marker de conflit git (chevrons sept fois)
- [ ] Frontmatter (si présent) parsable
- [ ] Pas de lien cassé vers `.claude/docs/*.md` (les 3 chargés en auto)

### Skills registry

Commande à lancer depuis la racine projet :

~~~
.venv\Scripts\python .claude\skills\.registry\skills_registry.py --sync
~~~

- [ ] Sortie : 0 frontmatter invalide
- [ ] `_to-delete/` toujours exclu du scan (voir `skills_registry.py`)
- [ ] Sync Google Sheets OK (sinon noter le code retour)
- [ ] Diff `INDEX.md` vs registre (juste lister les écarts, pas patcher)

## 2. Logs + Telegram @schoolswp_brain_bot

### Logs agents

Inventaire avant action :

~~~
Get-ChildItem "D:\VS Code\CLAUDE CODE\projects\schoolswp\logs\agents.log*"
~~~

- [ ] Rotation effective (max 5 fichiers, < 10 MB chacun)
- [ ] Pas de fichier > 10 MB qui aurait raté la rotation
- [ ] Dernière ligne datée < 7 jours (sinon flag : pipeline silencieux)

### Bot @schoolswp_brain_bot

- [ ] Health check ping : envoyer 1 message test au bot, attendre echo
- [ ] Vérifier `agents/telegram-claude/server.js` tourne (process node, port attendu)
- [ ] Pas d'erreur récente dans les logs PM2 si déployé via xCloud

### Channel Discord (canal alerts)

- [ ] Webhook schoolsWP-Routines répond 204 sur ping minimal. Utiliser Invoke-RestMethod en PowerShell (Method POST, ContentType application/json, body JSON minimal du genre {"content":"ping nemoclaw 2026-05-11"}). Webhook URL dans `.claude/settings.local.json`, jamais en clair dans ce brief.

## 3. Caches temporaires Claude Code

### Inventaire avant action (read-only)

~~~
Get-ChildItem -Recurse -Directory -Filter "__pycache__" "D:\VS Code\CLAUDE CODE\projects\schoolswp" | Measure-Object
Get-ChildItem -Recurse -Directory -Filter ".pytest_cache" "D:\VS Code\CLAUDE CODE\projects\schoolswp" | Measure-Object
Get-ChildItem "D:\VS Code\CLAUDE CODE\projects\schoolswp\.coverage" -ErrorAction SilentlyContinue
~~~

### Suppression (uniquement après feu vert Michael)

Cibles reproductibles uniquement :

- `**/__pycache__/`
- `**/.pytest_cache/`
- `.coverage` à la racine (vérifier qu'il est gitignored avant)
- `.mypy_cache/` si présent

Méthode : Remove-Item -Recurse -Force après confirmation explicite. Jamais d'opérateur destructif POSIX. Jamais en root.

Ne PAS toucher :

- `node_modules/`
- `.venv/`
- `tools/wp-media-upload/.cache/` (peut contenir des backups d'images)
- `apps/hyperframes/node_modules/` (lourd à réinstaller)

## Bonus — hygiène workspace (signaler, ne pas agir)

Anomalies connues à laisser tranquilles sans investigation, à juste lister + tailler :

- [ ] Dossier `{agents,hooks,commands}/` (résidu brace expansion)
- [ ] `systems/multi-agent-system/multi-agent-system/` (sous-dossier dupliqué imbriqué)
- [ ] `content/articles/articles/lms-*/` (doublons à fusionner)
- [ ] 3 backups MCP racine : `.mcp.json.bak`, `.mcp.json.fluent`, `.mcp.backup.json`
- [ ] Pollution racine : `.tmp-vm-*`, `tmp-*.py`, fichiers debug `*.txt`, `slide-*.png`, `iter*-screenshot.png`, transcripts `2026-03-28_youtube_*.md`

## Rapport attendu

Format markdown court, 1 section par bloc (1, 2, 3, bonus). Pour chaque check :

- OK / flag / fail + détail 1 ligne
- Toute action écriture/suppression effectuée : citer commande exacte + sortie

Poster le rapport :

- Dans `core/tasks/lessons.md` si quelque chose a été appris ou corrigé
- Sinon append dans Discord webhook schoolsWP-Routines (1 message résumé)
