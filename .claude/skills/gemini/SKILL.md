---
name: gemini
description: CLI Gemini pour Q&A en one-shot, résumés et génération.
homepage: https://ai.google.dev/
metadata: {"openclaw":{"emoji":"♊️","requires":{"bins":["gemini"]},"install":[{"id":"brew","kind":"brew","formula":"gemini-cli","bins":["gemini"],"label":"Installer Gemini CLI (brew)"}]}}
---

# Gemini CLI

Utilisez Gemini en mode one-shot avec un prompt positionnel (éviter le mode interactif).

## Démarrage rapide

- `gemini "Réponds à cette question..."`
- `gemini --model <nom> "Prompt..."`
- `gemini --output-format json "Retourne du JSON"`

## Extensions

- Lister : `gemini --list-extensions`
- Gérer : `gemini extensions <commande>`

## Notes

- Si l'authentification est requise, exécuter `gemini` une fois de manière interactive et suivre le flow de connexion.
- Éviter `--yolo` pour la sécurité.
