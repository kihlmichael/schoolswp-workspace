---
name: gws-docs
version: 1.0.0
description: |
  Lit, cree et met a jour des Google Docs via le CLI `gws`. Operations natives : ouvrir un Doc, extraire son contenu, ajouter du texte, partager. Sous-skills helpers `gws-docs-write` (append) et intégration avec Sheets/Drive/Gmail via les recipes correspondantes.
  Utilise ce skill quand l'utilisateur dit : "lis ce Google Doc", "cree un Doc", "mets a jour le Doc", "partage ce Doc", "extrait le contenu de ce Doc", "ajoute du texte au Doc", ou colle un lien `docs.google.com/document/`.
  NE PAS utiliser pour : draft email depuis Doc (utiliser `recipe-draft-email-from-doc`), rapport Sheets vers Doc (utiliser `recipe-generate-report-from-sheet`), redaction de contenu schoolsWP (utiliser le skill plateforme : `schoolswp-content-studio`, `schoolswp-article-workflow`).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws docs --help"
---

# docs (v1)

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

```bash
gws docs <resource> <method> [flags]
```

## Helper Commands

| Command | Description |
|---------|-------------|
| [`+write`](../gws-docs-write/SKILL.md) | Append text to a document |

## API Resources

### documents

  - `batchUpdate` — Applies one or more updates to the document. Each request is validated before being applied. If any request is not valid, then the entire request will fail and nothing will be applied. Some requests have replies to give you some information about how they are applied. Other requests do not need to return information; these each return an empty reply. The order of replies matches that of the requests.
  - `create` — Creates a blank document using the title given in the request. Other fields in the request, including any provided content, are ignored. Returns the created document.
  - `get` — Gets the latest version of the specified document.

## Discovering Commands

Before calling any API method, inspect it:

```bash
# Browse resources and methods
gws docs --help

# Inspect a method's required params, types, and defaults
gws schema docs.<resource>.<method>
```

Use `gws schema` output to build your `--params` and `--json` flags.

