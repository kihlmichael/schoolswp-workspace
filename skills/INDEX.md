# schoolsWP Skills - Project Reference

**Statut** : Skills migres vers global le 2026-02-10

---

## Tous les skills sont maintenant globaux

**Emplacement** : `~/.claude/skills/`
**Portee** : Disponibles dans tous les projets Claude Code

Les 19 skills metier (ex 01_LinkedIn a 19_Remotion) ont ete migres
vers `~/.claude/skills/` avec un nommage a plat (sans prefixe numerique).

Voir l'index complet : `~/.claude/skills/INDEX.md`

---

## Mapping ancien -> nouveau

| Ancien (projet) | Nouveau (global) |
|------------------|------------------|
| `01_LinkedIn` | `linkedin` |
| `02_YouTube` | `youtube` |
| `03_Facebook` | `facebook` |
| `04_WordPress` | `wordpress` |
| `05_Branding` | `branding` |
| `06_Dev` | `dev-wordpress` |
| `07_Marketing` | `marketing` |
| `08_GoogleDrive` | `googledrive` |
| `09_Discord` | `discord` |
| `10_Slack` | `slack` |
| `11_WhatsApp` | `whatsapp` |
| `12_Notion` | `notion` |
| `13_Gemini` | `gemini` |
| `14_OpenAI-ImageGen` | `openai-imagegen` |
| `15_OpenAI-Whisper` | `openai-whisper` |
| `16_OpenAI-Whisper-API` | `openai-whisper-api` |
| `17_CodeAudit` | `code-audit` |
| `18_Firecrawl` | `firecrawl` |
| `19_Remotion` | `remotion` |

---

## Ajouter un skill project-only

Si besoin d'un skill specifique a ce projet, creer un dossier ici :

```
.claude/skills/
├── INDEX.md         # Ce fichier
└── mon-skill/       # Skill local au projet
    └── SKILL.md
```

---

## Rollback

Backup pre-migration : `~/.claude/skills-backup-2026-02-10/`

---

**schoolsWP** - Espace de travail digital organise
