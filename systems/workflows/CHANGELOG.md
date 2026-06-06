# Changelog - schoolsWP Workflows

## v0.2 Baseline - validée (2026-06-01)

- **Moteur d'état résilient** : Ajout d'un aiguillage d'état robuste (`baseline`, `unchanged`, `changed`, `error`).
- **Normalisation anti-bruit** : Normalisation fine des chaînes de caractères avant hachage (retrait des cookies, footers et timestamps).
- **Hachage SHA-256** : Intégration d'un nœud crypto natif résolvant le hachage de manière robuste.
- **LLM uniquement sur changed** : Économie de bande passante et réduction des coûts d'IA en limitant l'utilisation de Gemini 2.5 Flash uniquement pour l'état `changed`.
- **Snapshot intelligent** : Enregistrement de snapshots uniquement pour les états `baseline`, `changed` et `error`.
- **Alertes filtrées** : Génération d'alertes uniquement si le score IA diff est >= 6.
- **Notifications exclusives** : Transmission sur Discord et Email uniquement si le score IA diff est >= 8.
- **Validation empirique** : Réussite des 3 cycles de validation complets (baseline, unchanged silencieux, changed simulé avec score 5/10 bypassant les notifications).
