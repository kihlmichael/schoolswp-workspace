# Plugins Claude Code — Inventaire

Plugins installés dans l'environnement Claude Code (distinct des agents et skills).

## Plugins actifs

| Plugin | Source | Rôle | Commandes clés |
|---|---|---|---|
| **codex** | `openai/codex-plugin-cc` | Review de code et délégation de tâches à Codex (OpenAI) | `/codex:review`, `/codex:adversarial-review`, `/codex:rescue`, `/codex:status`, `/codex:result`, `/codex:cancel` |

Fiche détaillée Codex : voir doc dédiée.

## Gestion des plugins

```
/plugin marketplace add <owner/repo>    Ajouter une marketplace
/plugin install <plugin@marketplace>    Installer un plugin
/plugin list                            Lister les plugins installés
/reload-plugins                         Recharger après install/update
```

## Scopes d'installation

- **User scope** — dispo dans tous les projets Claude Code (perso)
- **Project scope** — commité dans le repo, partagé équipe
- **Local scope** — juste ce repo, juste toi

## À suivre

Cette liste évoluera. Mettre à jour à chaque nouvelle installation via `/plugin install`.
