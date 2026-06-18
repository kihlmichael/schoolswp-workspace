# gemini.md - Antigravity Pilot for schoolsWP

Ce fichier dicte le comportement de l'agent Antigravity (Gemini) lorsqu'il travaille sur le projet schoolsWP. Il ne remplace pas `CLAUDE.md`, mais fonctionne de pair avec lui en tant que référentiel spécifique pour Gemini.

## 1. Rôle et Objectifs
Le dossier `D:\VS Code\CLAUDE CODE\projects\schoolswp\antigravity` (ou le dossier `antigravity/` à la racine du projet principal) est le workspace dédié à Gemini/Antigravity. Il sert de "tour de contrôle" pour :
- Préparer les plans de travail
- Rédiger les tâches
- Produire des brouillons
- Générer des scripts temporaires
- Documenter les actions
- Tester des approches avant application au projet principal schoolsWP

Il ne doit **en aucun cas** être considéré comme une refonte de `schoolswp-agents`.

## 2. Règles de Sécurité Inflexibles (Data Safety)
- **Aucune suppression massive** sans validation explicite de l'utilisateur.
- **Aucune modification du Vault Obsidian** (situé dans `D:\🌐 MES SITES\📋 SCHOOLSWP.COM\12_Obsidian\schoolsWP`) sans accord préalable.
- **Aucun déplacement ou renommage risqué** de fichiers/dossiers sans plan structuré.
- **Validation avant impact** : Toute action nécessitant de modifier le projet principal doit d'abord faire l'objet d'un plan approuvé (brouillon ou diff).

## 3. Workflow Opérationnel (Comportement Attendu)
À chaque nouvelle demande concernant schoolsWP, Gemini DOIT respecter cet ordre :
1. **Lire ce fichier (`gemini.md`)**.
2. **Identifier le périmètre** de la tâche.
3. **Vérifier l'impact** : Est-ce que cela touche le site WordPress, le Vault Obsidian, les agents Claude, les automatisations ou les contenus éditoriaux ?
4. **Proposer un plan** (via `implementation_plan.md`).
5. **Produire les livrables** dans les dossiers `outputs/` ou `drafts/` de ce workspace.
6. **Application stricte** : Ne modifier le projet principal qu'après validation.
7. **Documenter** le travail effectué (via `walkthrough.md` et `changelog.md`).

## 4. Relation avec l'Écosystème Claude Code
- **Cohabitation** : L'écosystème Claude (`D:\VS Code\CLAUDE CODE\projects\schoolswp`) et ses agents (schoolswp-agents) restent la référence historique et la base du système.
- **Inspiration, pas duplication** : S'inspirer des skills Claude et comprendre leur rôle, mais utiliser des méthodes propres à Gemini plutôt que d'imiter aveuglément des hooks, commandes spécifiques ou sous-agents propres à l'architecture Claude.
- **Documentation de référence** : Consulter le dossier `references/` pour les pointeurs vers les règles Claude et le Vault Obsidian.

## 5. Architecture de l'Espace ANTIGRAVITY
L'espace vit désormais sous le dossier `antigravity/` à la racine de schoolsWP :
- `gemini.md` : Les règles (ce fichier).
- `task.md` / `implementation_plan.md` / `walkthrough.md` : Les fichiers de gestion de tâche et d'itération de Gemini.
- `changelog.md` : Historique des modifications majeures apportées au système ou au projet.
- `logs/` : Traces d'exécution et logs divers.
- `outputs/` : Livrables finaux prêts à être déployés.
- `drafts/` : Brouillons de code ou de texte (sandbox).
- `scripts/` : Scripts temporaires ou outils de diagnostic propres à Gemini.
- `references/` : Pointeurs de contexte (règles Claude, architecture, Obsidian).

## 6. Outils et Intégrations
Gemini utilise ses propres capacités natives tout en respectant l'esprit du projet :
- **Serveurs MCP** : Utilisation des serveurs disponibles (notamment `novamira-schoolswp-com` pour interagir avec le blog WordPress en direct).
- **Mode Planning & Artifacts** : Utilisation obligatoire des artéfacts pour valider les étapes structurantes avec l'utilisateur.
