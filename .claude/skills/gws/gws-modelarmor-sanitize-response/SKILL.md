---
name: gws-modelarmor-sanitize-response
version: 1.0.0
description: |
  Helper gws modelarmor +sanitize-response : passe une réponse de modèle LLM dans un template Model Armor et retourne le verdict safety (allow/block) + détails de matchs. Idéal en post-check avant d'afficher la réponse à l'utilisateur.
  Utilise ce skill quand l'utilisateur dit : "sanitize la réponse LLM", "filtre réponse avant affichage", "Model Armor sur output modèle", "verdict safety output", ou pour brancher Model Armor en garde-corps aval sur un agent LLM en prod.
  NE PAS utiliser pour : sanitize le prompt utilisateur en amont (utiliser gws-modelarmor-sanitize-prompt), créer le template (utiliser gws-modelarmor-create-template), ou logique de fallback côté agent (à coder dans le wrapper qui appelle ce sanitize).
metadata:
  openclaw:
    category: "security"
    requires:
      bins: ["gws"]
    cliHelp: "gws modelarmor +sanitize-response --help"
---

# modelarmor +sanitize-response

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Sanitize a model response through a Model Armor template

## Usage

```bash
gws modelarmor +sanitize-response --template <NAME>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--template` | ✓ | — | Full template resource name (projects/PROJECT/locations/LOCATION/templates/TEMPLATE) |
| `--text` | — | — | Text content to sanitize |
| `--json` | — | — | Full JSON request body (overrides --text) |

## Examples

```bash
gws modelarmor +sanitize-response --template projects/P/locations/L/templates/T --text 'model output'
model_cmd | gws modelarmor +sanitize-response --template ...
```

## Tips

- Use for outbound safety (model -> user).
- For inbound safety (user -> model), use +sanitize-prompt.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-modelarmor](../gws-modelarmor/SKILL.md) — All filter user-generated content for safety commands
