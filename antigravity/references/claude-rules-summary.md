# Résumé des règles Claude Code

Ce fichier sert de référence à Gemini pour s'aligner sur la rigueur de l'environnement Claude.

## Règles fondamentales à respecter
1. **Sécurité (Data Safety)** : Pas de suppressions destructrices (`rm -rf` etc.), aucune suppression de fichier sans l'accord de l'utilisateur.
2. **Planification** : Toujours produire un plan avant une action structurante. Privilégier les brouillons (diffs) et les validations intermédiaires.
3. **Logique SOP** : Travailler selon des Standard Operating Procedures et documenter tout changement de fond.

## Adaptation pour Gemini
- Gemini doit comprendre les intentions des "Skills" situés dans `D:\VS Code\CLAUDE CODE\projects\schoolswp\.claude\skills\` mais doit employer **ses propres capacités** (outils, serveurs MCP comme `novamira-schoolswp-com`, artifacts) sans tenter d'imiter les hooks internes ou les commandes propres à la CLI Claude Code.
