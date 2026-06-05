---
name: Configuration de la passerelle Obsidian Claude Code
owner: Michaël KIHL
project: schoolsWP
version: 1.0
date_creation: 2026-05-04
---

# Configuration passerelle Obsidian - Claude Code

## 1. Chemins

| Repère                   | Chemin absolu                                                                        |
| ------------------------ | ------------------------------------------------------------------------------------ |
| Projet Claude Code       | `d:\VS Code\CLAUDE CODE\projects\schoolswp\`                                         |
| Passerelle projet        | `d:\VS Code\CLAUDE CODE\projects\schoolswp\obsidian-bridge\`                         |
| Vault Obsidian           | `D:\MES SITES\📋 SCHOOLSWP.COM\12_Obsidian\schoolsWP\`                               |
| Passerelle vault         | `D:\MES SITES\📋 SCHOOLSWP.COM\12_Obsidian\schoolsWP\00_systeme\claude-code-bridge\` |
| Mémoire auto Claude Code | `C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory\`  |

> Le chemin du vault contient des espaces, accents et emojis. Tout script doit utiliser `-LiteralPath` côté PowerShell (quand le cmdlet le supporte) ou `-Path` avec guillemets stricts à défaut. Côté Bash, toujours guillemets doubles autour de la variable.

## 2. Mapping des dossiers

| Côté projet                            | Côté vault                                            | Sens            |
| -------------------------------------- | ----------------------------------------------------- | --------------- |
| `obsidian-bridge/inbox-from-obsidian/` | `00_systeme/claude-code-bridge/inbox-vers-claude/`    | Vault -> projet |
| `obsidian-bridge/outbox-to-obsidian/`  | `00_systeme/claude-code-bridge/outbox-depuis-claude/` | Projet -> vault |
| `obsidian-bridge/logs/`                | `00_systeme/claude-code-bridge/logs/`                 | Miroir          |

## 3. Conventions de nommage

Inspirées de la charte du vault :

- kebab-case minuscule
- préfixe date `YYYY-MM-DD_` pour les éléments datés
- pas d'em-dash (`—`) ni d'en-dash (`–`)
- marque toujours écrite **schoolsWP** (s minuscule, WP majuscule)
- dossiers en minuscules

Format recommandé :

```text
YYYY-MM-DD_type_titre-court.md
```

Exemples :

- `2026-05-04_synthese_audit-pinterest.md`
- `2026-05-04_decision_choix-stack-formation.md`

## 4. Frontmatter standard

Tout fichier transitant par la passerelle doit porter un frontmatter explicite :

```yaml
---
source: claude-code | obsidian | michael
status: brouillon | a-arbitrer | synthese-stabilisee | memoire-durable
date_creation: YYYY-MM-DD
date_validation: YYYY-MM-DD (optionnel)
validated_by: Michaël KIHL (optionnel)
type: synthese | decision | sop | rapport | note | log
---
```

## 5. Règles Git

Versionné :

- structure de `obsidian-bridge/`
- README, SOP, templates, scripts éventuels
- conventions et documentation

Gitignoré :

- `inbox-from-obsidian/*` (sauf `.gitkeep`)
- `outbox-to-obsidian/*` (sauf `.gitkeep`)
- `logs/*` (sauf `.gitkeep`)
- exports intermédiaires
- contenus de transition

Détail dans `.gitignore`.

## 6. Hygiène d'écriture

- Toujours préférer `Edit` à `Write` pour modifier un fichier existant.
- Toujours `Read` avant `Edit`.
- Pas de réécriture totale de fichier sans accord.
- Pas de modification de structure d'un fichier sans le signaler.

## 7. Liens externes

- Charte du vault : `claude.md` à la racine du vault Obsidian.
- Règle absolue du wiki : aucune modification durable du wiki sans entrée dans `log.md` du vault.
- SOP projet : [SOP-claude-obsidian-bridge.md](SOP-claude-obsidian-bridge.md)
- SOP vault : `00_systeme/claude-code-bridge/SOP-utilisation.md`
