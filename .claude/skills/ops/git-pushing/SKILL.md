---
name: git-pushing
description: |
  Pousse les changements vers le remote via le script smart commit (message conventional commit, footer Claude, flag upstream). Pattern fixe — ne jamais relancer les commandes git manuellement quand ce skill est invoqué.
  Utilise ce skill quand l'utilisateur dit : "save to github", "pousser sur le remote", "sauvegarde les changements", "let's push this up", "smart commit", ou termine une feature et veut la partager.
  NE PAS utiliser pour : créer un nouveau repo GitHub (utiliser publish-repo), ouvrir une pull request (utiliser le skill superpowers requesting-code-review), versioning atomique multi-fichiers structuré (utiliser git-workflow-and-versioning), ou résolution de conflits ou rebase interactif (workflow manuel).
risk: unknown
source: community
date_added: "2026-02-27"
---

# Git Push Workflow

Stage all changes, create a conventional commit, and push to the remote branch.

## When to Use

Automatically activate when the user:

- Explicitly asks to push changes ("push this", "commit and push")
- Mentions saving work to remote ("save to github", "push to remote")
- Completes a feature and wants to share it
- Says phrases like "let's push this up" or "commit these changes"

## Workflow

**ALWAYS use the script** - do NOT use manual git commands:

```bash
bash skills/git-pushing/scripts/smart_commit.sh
```

With custom message:

```bash
bash skills/git-pushing/scripts/smart_commit.sh "feat: add feature"
```

Script handles: staging, conventional commit message, Claude footer, push with -u flag.
