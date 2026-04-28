---
name: claude-config-backup
description: |
  Sauvegarde et restaure la configuration Claude Code (skills, agents, commands, hooks, settings) entre
  machines Windows via git privé ou archive .tar.gz. Gère workspace (`D:/VS Code/CLAUDE CODE/.claude/`)
  et global user (`C:/Users/<user>/.claude/`), exclut automatiquement les secrets (.env, .mcp.json,
  settings.local.json, *.key). Déclenche pour "backup mes skills", "sauvegarder config Claude",
  "restore sur nouvelle machine", "sync claude config", "setup nouveau PC", "migrer skills", "transférer
  config Claude Code", "exporter skills", "importer skills".
---

# Claude Config Backup

Skill d'outillage pour sauvegarder et restaurer la config Claude Code (skills, agents, commands, hooks,
settings) entre machines. Pensé pour Michael KIHL qui travaille sur plusieurs PC Windows.

## Périmètre

Deux emplacements sont sauvegardés :

1. **Workspace** : `D:/VS Code/CLAUDE CODE/.claude/`
   - `skills/`, `agents/`, `commands/`, `hooks/`, `settings.json`
2. **Global user** : `C:/Users/<username>/.claude/`
   - `skills/`, `agents/`, `commands/`, `CLAUDE.md`, `settings.json`

**Hors périmètre** : `projects/schoolswp/.claude/` (déjà versionné dans le repo git du projet) et
`.agents/skills/` (source library, rarement modifiée — à archiver à part si besoin).

## Secrets exclus automatiquement

Le skill refuse d'inclure ces fichiers (pattern matching sur le chemin) :

- `.env`, `.env.local`, `.env.*`
- `.mcp.json` (contient les clés API MCP)
- `settings.local.json`
- `*.key`, `*.pem`, `credentials.json`, `*.token`
- `projects/` (sous-projets ont leur propre git)

Un fichier `.backupignore` peut être placé à la racine de chaque emplacement pour exclusions
supplémentaires (syntaxe glob, une règle par ligne).

## Commandes

Les scripts sont dans `scripts/` à côté de ce SKILL.md. Toujours invoquer depuis bash (Git Bash sur
Windows) — pas depuis PowerShell.

### Setup initial (une fois, sur la machine principale)

```bash
bash scripts/init.sh <github-user> <repo-name>
# Exemple : bash scripts/init.sh michaelkihl claude-config-private
```

Ce qu'il fait :
1. Crée un dossier de travail `~/claude-config-sync/`
2. Initialise un repo git avec `.gitignore` sécurisé (exclusions secrets)
3. Copie les deux emplacements dedans (workspace/ et user/)
4. Crée le repo GitHub privé via `gh repo create` (nécessite `gh` CLI authentifié)
5. Push initial

### Backup

```bash
# Mode git : commit + push vers le repo privé
bash scripts/backup.sh --git

# Mode archive : .tar.gz horodaté (pour OneDrive/Dropbox/transfert manuel)
bash scripts/backup.sh --archive [--out <dir>]
# Défaut out : ~/claude-config-backups/

# Les deux (recommandé pour sécurité max)
bash scripts/backup.sh --git --archive
```

### Restore (sur la nouvelle machine)

```bash
# Depuis git
bash scripts/restore.sh --git <repo-url>
# Exemple : bash scripts/restore.sh --git git@github.com:michaelkihl/claude-config-private.git

# Depuis archive
bash scripts/restore.sh --archive <path/to/file.tar.gz>

# Dry-run pour voir ce qui sera copié sans rien écrire
bash scripts/restore.sh --git <url> --dry-run
```

Le restore vérifie les chemins de destination et demande confirmation avant d'écraser du contenu
existant.

## Workflow multi-machines (branche par machine)

Pour éviter l'écrasement croisé, chaque machine push sur sa propre branche. `main` est réservée à
l'état fusionné canonique.

```
main                 ← état fusionné après review manuelle
├── pc-maison        ← cette machine
└── pc-ancien        ← autre machine
```

**Sur cette machine (pc-maison, défaut)** :
```bash
bash scripts/backup.sh --git                      # push sur pc-maison
```

**Sur l'autre machine (pc-ancien)** :
```bash
# 1. Clone le repo (une fois)
git clone https://github.com/kihlmichael/claude-config-private.git ~/claude-config-sync

# 2. Backup en overridant la branche
bash scripts/backup.sh --git --branch pc-ancien
# Ou via env var : CLAUDE_BACKUP_BRANCH=pc-ancien bash scripts/backup.sh --git
```

**Restore depuis la branche canonique `main` (après merge)** :
```bash
bash scripts/restore.sh --git https://github.com/... --branch main
```

**Restore directement depuis une branche machine** (si pas encore mergée) :
```bash
bash scripts/restore.sh --git https://github.com/... --branch pc-ancien --dry-run
```

## Compare & merge (étape manuelle, à faire depuis VS Code)

Tant que `compare.sh` n'est pas implémenté, la procédure manuelle est :

1. Clone le repo dans un dossier de review : `git clone <url> ~/claude-merge && cd ~/claude-merge`
2. Liste les fichiers qui diffèrent : `git diff --name-status pc-ancien..pc-maison`
3. Ouvre VS Code sur le dossier : `code .`
4. Utilise l'extension GitLens ou la vue "Source Control" → comparaison de branches
5. Crée une branche `main` fusionnée manuellement :
   ```bash
   git checkout main
   # Pour chaque fichier à garder depuis pc-ancien :
   git checkout pc-ancien -- path/to/file
   # Pour chaque fichier à garder depuis pc-maison :
   git checkout pc-maison -- path/to/file
   git commit -m "chore: merge pc-maison + pc-ancien"
   git push origin main
   ```
6. Les deux machines peuvent ensuite `restore.sh --branch main`

## Pourquoi ces choix

- **Git privé** : versionné, audit trail, diff entre versions, reverse possible. L'approche la plus
  robuste pour un usage long terme.
- **Archive en parallèle** : fallback sans dépendance GitHub, transport possible via clé USB ou cloud,
  utile pour les machines sans accès réseau initial.
- **Exclusions strictes de secrets** : même avec un repo privé, les clés API ne doivent jamais y
  atterrir — elles vivent dans `.env` / `.mcp.json` qui restent locaux à chaque machine.
- **Bash sur Windows** : cohérent avec le reste du workspace schoolsWP (le CLAUDE.md du workspace
  précise bash).

## Tests manuels

Avant de publier une nouvelle version du skill, vérifier :

1. `bash scripts/backup.sh --archive --out /tmp/test` produit un `.tar.gz` sans secrets
2. `tar -tzf /tmp/test/claude-config-*.tar.gz | grep -E '(\.env|\.mcp\.json|settings\.local)'` ne
   retourne rien
3. `bash scripts/restore.sh --archive /tmp/test/claude-config-*.tar.gz --dry-run` liste les
   destinations attendues sans rien copier

## Limites

- Windows-only (chemins codés en dur : `D:/VS Code/CLAUDE CODE/` et `C:/Users/`)
- Ne gère pas la synchro auto (pas de watcher) — à lancer manuellement ou via tâche planifiée
- Ne résout pas les conflits git automatiquement (si backup sur deux machines sans pull intermédiaire)
