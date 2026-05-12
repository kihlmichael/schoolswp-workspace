---
name: Passerelle Obsidian Claude Code
owner: Michaël KIHL
project: schoolsWP
version: 1.0
date_creation: 2026-05-04
phase: 1
---

# Passerelle Obsidian - Claude Code

## 1. Rôle

Canal contrôlé entre le projet Claude Code schoolsWP et le vault Obsidian schoolsWP.

- Projet : `d:\VS Code\CLAUDE CODE\projects\schoolswp\`
- Vault : `D:\🌐 MES SITES\📋 SCHOOLSWP.COM\12_Obsidian\schoolsWP\`

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

| De | Vers | Contenu |
|----|------|---------|
| Vault | `inbox-from-obsidian/` | Notes que Michaël expose à Claude Code |
| `outbox-to-obsidian/` | Vault | Drafts produits par Claude Code |
| Vault `outbox-depuis-claude/` | Zones stables vault | Promotion validée par L0 + log.md |

## 5. Règles essentielles

1. Claude Code n'écrit jamais directement dans le vault sans validation explicite.
2. Toute action significative est journalisée (côté projet : `logs/`, côté vault : `log.md`).
3. Les contenus de transit sont gitignorés. La structure est versionnée.
4. Aucune mémoire durable n'est créée automatiquement par cette passerelle.
5. Toute stabilisation reste soumise à validation Michaël.

## 6. Documentation associée

- Procédure complète : [SOP-claude-obsidian-bridge.md](SOP-claude-obsidian-bridge.md)
- Configuration humaine : [bridge-config.md](bridge-config.md)
- Templates : [templates/](templates/)
- Charte vault (autorité) : `claude.md` à la racine du vault Obsidian
- SOP côté vault : `00_systeme/claude-code-bridge/SOP-utilisation.md`

## 7. Phase 1 - périmètre actuel

Cette phase inclut **uniquement** :

- arborescence côté projet et côté vault
- README, SOP, templates
- règles Git
- entrées dans `log.md` du vault
- documentation dans `CLAUDE.md` du projet

Cette phase **n'inclut pas** :

- automatisation
- synchronisation bidirectionnelle
- sous-skill de verrouillage durci
- promotion automatique d'information vers le wiki

Une phase 2 sera évaluée si un besoin réel apparaît.
