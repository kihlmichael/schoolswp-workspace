---
name: gemini
description: |
  CLI Gemini pour Q&A one-shot, résumés rapides, génération texte/JSON. Mode positionnel (`gemini "prompt"`) avec --model et --output-format json, gestion d'extensions via `gemini extensions`.
  Utilise ce skill quand l'utilisateur dit : "lance le CLI Gemini", "gemini en ligne de commande", "one-shot Gemini", "résume avec gemini CLI", "gemini --model", ou veut un appel rapide sans coder de SDK.
  NE PAS utiliser pour : intégrer Gemini dans une app via SDK (utiliser `gemini-api-dev`), streaming temps réel WebSocket (utiliser `gemini-live-api-dev`), API Interactions stateful (utiliser `gemini-interactions-api`).
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
