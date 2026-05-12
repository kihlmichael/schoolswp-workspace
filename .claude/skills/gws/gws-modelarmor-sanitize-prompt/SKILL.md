---
name: gws-modelarmor-sanitize-prompt
version: 1.0.0
description: |
  Helper gws modelarmor +sanitize-prompt : passe un prompt utilisateur dans un template Model Armor existant et retourne le verdict safety (allow/block) + détails de matchs (PII, contournement, toxique). Idéal en pre-check avant d'envoyer le prompt à un LLM.
  Utilise ce skill quand l'utilisateur dit : "sanitize ce prompt", "check ce prompt Model Armor", "filtre prompt avant LLM", "verdict safety prompt", ou pour brancher Model Armor en garde-corps amont sur un agent LLM en prod.
  NE PAS utiliser pour : sanitize la réponse retournée par le modèle (utiliser gws-modelarmor-sanitize-response), créer le template Model Armor (utiliser gws-modelarmor-create-template), ou modération texte hors GCP.
metadata:
  openclaw:
    category: "security"
    requires:
      bins: ["gws"]
    cliHelp: "gws modelarmor +sanitize-prompt --help"
---

# modelarmor +sanitize-prompt

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Sanitize a user prompt through a Model Armor template

## Usage

```bash
gws modelarmor +sanitize-prompt --template <NAME>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--template` | ✓ | — | Full template resource name (projects/PROJECT/locations/LOCATION/templates/TEMPLATE) |
| `--text` | — | — | Text content to sanitize |
| `--json` | — | — | Full JSON request body (overrides --text) |

## Examples

```bash
gws modelarmor +sanitize-prompt --template projects/P/locations/L/templates/T --text 'user input'
echo 'prompt' | gws modelarmor +sanitize-prompt --template ...
```

## Tips

- If neither --text nor --json is given, reads from stdin.
- For outbound safety, use +sanitize-response instead.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-modelarmor](../gws-modelarmor/SKILL.md) — All filter user-generated content for safety commands
