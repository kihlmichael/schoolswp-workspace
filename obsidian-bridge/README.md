---
name: Passerelle Obsidian Claude Code
owner: Michaël KIHL
project: schoolsWP
version: 1.1
date_creation: 2026-05-04
phase: 1
---

# Passerelle Obsidian - Claude Code

## 1. Rôle

Canal contrôlé entre le projet Claude Code schoolsWP et le vault Obsidian schoolsWP.

- Projet : `d:\VS Code\CLAUDE CODE\projects\schoolswp\`
- Vault : `D:\MES SITES\📋 SCHOOLSWP.COM\12_Obsidian\schoolsWP\`

Cette passerelle n'est pas une synchronisation. C'est un canal de transit explicite, journalisé, validé manuellement.

## 2. Asymétrie

- Le vault Obsidian reste **autorité finale** de la mémoire longue.
- Le projet Claude Code reste **autorité finale** de l'opérationnel.
- La mémoire interne Claude Code (`C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory\`) est technique. Elle ne remplace pas le wiki et n'a pas autorité sur lui.

## 3. Structure

```text
obsidian-bridge/
├── README.md                       (versionné)
├── bridge-config.md                (versionné)
├── SOP-claude-obsidian-bridge.md   (versionné)
├── SOP-memory-lint.md              (versionné)
├── promote-to-vault.ps1            (versionné, promotion assistée L0)
├── sync-outbox-to-vault.ps1        (versionné, synchro auto outbox -> vault + index)
├── register-sync-task.ps1          (versionné, enregistre la tâche planifiée)
├── INDEX-memos-techniques.md       (versionné, index généré auto - ne pas éditer)
├── .gitignore                      (versionné)
├── templates/                      (versionné)
│   ├── synthese.md
│   ├── decision.md
│   └── log-entry.md
├── inbox-from-obsidian/            (gitignored sauf .gitkeep)
├── outbox-to-obsidian/             (gitignored sauf .gitkeep)
└── logs/                           (gitignored sauf .gitkeep)
```

## 4. Sens de circulation

| De                            | Vers                   | Contenu                                |
| ----------------------------- | ---------------------- | -------------------------------------- |
| Vault                         | `inbox-from-obsidian/` | Notes que Michaël expose à Claude Code |
| `outbox-to-obsidian/`         | Vault                  | Drafts produits par Claude Code        |
| Vault `outbox-depuis-claude/` | Zones stables vault    | Promotion validée par L0 + log.md      |

## 5. Règles essentielles

1. Claude Code n'écrit jamais directement dans le vault sans validation explicite.
2. Toute action significative est journalisée (côté projet : `logs/`, côté vault : `log.md`).
3. Les contenus de transit sont gitignorés. La structure est versionnée.
4. Aucune mémoire durable n'est créée automatiquement par cette passerelle.
5. Toute stabilisation reste soumise à validation Michaël.

## 6. Documentation associée

- Procédure complète : [SOP-claude-obsidian-bridge.md](SOP-claude-obsidian-bridge.md)
- Procédure de lint mémoire : [SOP-memory-lint.md](SOP-memory-lint.md)
- Configuration humaine : [bridge-config.md](bridge-config.md)
- Promotion assistée vers zone stable (validation L0 requise, backup + verif intégrés) : [promote-to-vault.ps1](promote-to-vault.ps1)
- Templates : [templates/](templates/)
- Charte vault (autorité) : `claude.md` à la racine du vault Obsidian
- SOP côté vault : `00_systeme/claude-code-bridge/SOP-utilisation.md`

## 7. Phase 2 - synchronisation automatisée (active depuis 2026-06-11)

La passerelle sert de **mémo technique** : les drafts produits par Claude Code sont synchronisés vers le vault et indexés pour être retrouvés facilement, côté repo et côté vault.

Automatisation en place :

- `sync-outbox-to-vault.ps1` : transport one-way `outbox-to-obsidian/` -> vault `outbox-depuis-claude/`, idempotent, conserve une copie locale (miroir `_archive/deja-transportes/`, gardée indéfiniment et ré-indexée), régénère les index. Journal : `logs/sync.log`. Option `-DryRun`.
- `register-sync-task.ps1` : enregistre la tâche planifiée `schoolsWP Obsidian Sync` (au logon + quotidien 13:00, compte courant, sans élévation). `-Remove` pour la désactiver.
- Index : `INDEX-memos-techniques.md` (versionné, repo, findable via git) + `MOC-memos-techniques.md` (vault, navigable Obsidian). Générés automatiquement, ne pas éditer à la main.

Toujours **hors périmètre** :

- synchronisation bidirectionnelle automatique (l'inbox vault -> projet reste manuelle)
- promotion automatique vers les zones stables du wiki (reste validée par L0 via `promote-to-vault.ps1`)

Règle inchangée : le vault reste l'**autorité finale** ; la synchro n'écrase jamais une note déjà présente dans le vault et ne supprime jamais un draft (déplacé vers le miroir).
