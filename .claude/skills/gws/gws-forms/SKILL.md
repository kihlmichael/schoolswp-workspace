---
name: gws-forms
version: 1.0.0
description: |
  Lit et cree des Google Forms via le CLI `gws`. Operations : créer un formulaire, ajouter des questions (texte, choix multiple, échelle), récupérer les reponses, modifier la structure d'un Form existant.
  Utilise ce skill quand l'utilisateur dit : "cree un Google Form", "ajoute une question au Form", "récupère les reponses du Form", "modifie le Form", ou colle un lien `docs.google.com/forms/`.
  NE PAS utiliser pour : créer un Form de feedback partage par Gmail (utiliser `recipe-create-feedback-form`), récupérer specifiquement les reponses dans un workflow (utiliser `recipe-collect-form-responses`), ou créer un formulaire WordPress (utiliser Fluent Forms - voir `flow` agent).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws forms --help"
---

# forms (v1)

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

```bash
gws forms <resource> <method> [flags]
```

## API Resources

### forms

  - `batchUpdate` — Change the form with a batch of updates.
  - `create` — Create a new form using the title given in the provided form message in the request. *Important:* Only the form.info.title and form.info.document_title fields are copied to the new form. All other fields including the form description, items and settings are disallowed. To create a new form and add items, you must first call forms.create to create an empty form with a title and (optional) document title, and then call forms.update to add the items.
  - `get` — Get a form.
  - `setPublishSettings` — Updates the publish settings of a form. Legacy forms aren't supported because they don't have the `publish_settings` field.
  - `responses` — Operations on the 'responses' resource
  - `watches` — Operations on the 'watches' resource

## Discovering Commands

Before calling any API method, inspect it:

```bash
# Browse resources and methods
gws forms --help

# Inspect a method's required params, types, and defaults
gws schema forms.<resource>.<method>
```

Use `gws schema` output to build your `--params` and `--json` flags.

