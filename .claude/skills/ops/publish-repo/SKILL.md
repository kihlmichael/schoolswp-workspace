---
name: publish-repo
description: |
  Crée un nouveau repo GitHub privé via gh CLI, initie git si besoin, commit les changements puis push avec flag upstream. Usage : /publish-repo <repo-name> [commit message]. Toujours privé, demande confirmation avant création et push.
  Utilise ce skill quand l'utilisateur dit : "publish repo", "crée repo GitHub", "push sur GitHub", "/publish-repo nom-repo", ou veut publier un nouveau projet sur le compte GitHub.
  NE PAS utiliser pour : push sur un repo déjà créé (utiliser `git-pushing`), créer un repo public (skill force `--private`), créer une pull request (utiliser le skill `superpowers:requesting-code-review`), ou fork d'un repo existant (utiliser MCP `github` ou gh CLI direct).
---

# /publish-repo

Purpose: Create a GitHub repo, commit current changes, and push.
Run only inside this repo: D:\VS Code\CLAUDE CODE\projects\schoolswp.

Usage: `$ARGUMENTS` → `<repo-name> [commit message]`

Always create private repos. Ask only for repo name and commit message.

## Pre-checks

- Verify git is available.
- Verify gh is available; if not, ask to open a new terminal and retry.
- Verify gh auth status; if not logged in, run: gh auth login.

## Steps

1. Confirm working directory is the repo root.
2. If not a git repo, run: git init.
3. Show git status and ask for confirmation to proceed.
4. git add -A
5. If there are staged changes, run: git commit -m "<message>"
6. If origin remote exists, skip repo creation and push.
7. Else create repo with gh: `gh repo create <repo-name> --source . --remote origin --private`
8. Push current branch: git push -u origin HEAD

## Safety rules

- Never use rm. Use trash for deletions.
- Always ask before creating the GitHub repo or pushing.
- If no changes to commit, skip commit and just push.
