---
name: gws-modelarmor-create-template
version: 1.0.0
description: |
  Helper gws modelarmor +create-template : crée un nouveau template Model Armor sur GCP (project + location + template-id) avec les filters de sécurité voulus (contournement, PII, malicious URLs, etc.). Pré-requis avant tout sanitize prompt ou response.
  Utilise ce skill quand l'utilisateur dit : "crée un template Model Armor", "setup Model Armor", "configure Model Armor pour mon projet GCP", "init template Model Armor", ou pour bootstraper une stack safety LLM côté Google Cloud.
  NE PAS utiliser pour : utiliser un template existant pour sanitize un prompt (utiliser gws-modelarmor-sanitize-prompt), sanitize une réponse modèle (utiliser gws-modelarmor-sanitize-response), ou opérations CRUD générales sur les templates (utiliser gws-modelarmor).
metadata:
  openclaw:
    category: "security"
    requires:
      bins: ["gws"]
    cliHelp: "gws modelarmor +create-template --help"
---

# modelarmor +create-template

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Create a new Model Armor template

## Usage

```bash
gws modelarmor +create-template --project <PROJECT> --location <LOCATION> --template-id <ID>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--project` | ✓ | — | GCP project ID |
| `--location` | ✓ | — | GCP location (e.g. us-central1) |
| `--template-id` | ✓ | — | Template ID to create |
| `--preset` | — | — | Use a preset template: jailbreak |
| `--json` | — | — | JSON body for the template configuration (overrides --preset) |

## Examples

```bash
gws modelarmor +create-template --project P --location us-central1 --template-id my-tmpl --preset jailbreak
gws modelarmor +create-template --project P --location us-central1 --template-id my-tmpl --json '{...}'
```

## Tips

- Defaults to the jailbreak preset if neither --preset nor --json is given.
- Use the resulting template name with +sanitize-prompt and +sanitize-response.

> [!CAUTION]
> This is a **write** command — confirm with the user before executing.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-modelarmor](../gws-modelarmor/SKILL.md) — All filter user-generated content for safety commands
