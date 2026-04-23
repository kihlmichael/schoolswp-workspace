---
name: refresh-site-md
description: Rafraîchit le fichier `shared/SITE.md` (snapshot WordPress schoolswp.com) via le MCP novamira. Utilise ce skill quand l'utilisateur demande de mettre à jour SITE.md, de vérifier les plugins actifs, ou après une installation/désactivation de plugin sur schoolswp.com.
---

# refresh-site-md — Rafraîchir SITE.md

Met à jour le snapshot `shared/SITE.md` en lecture seule via le MCP `novamira-schoolswp-com`.

## Quand l'utiliser

- L'utilisateur demande un refresh : "mets à jour SITE.md", "check les plugins".
- Après installation, désactivation ou update d'un plugin sur schoolswp.com.
- Avant une session de travail importante si le fichier a > 7 jours.

## Sécurité

- **Lecture seule** strictement. Jamais d'écriture côté WordPress.
- Pas de modification de config, de post, ou d'option.
- Écriture locale uniquement dans `shared/SITE.md`.

## Procédure

### Étape 1 — Découvrir les abilities disponibles

```
mcp__novamira-schoolswp-com__mcp-adapter-discover-abilities
```

Identifier les abilities en lecture :
- Liste des plugins actifs (ex: `list-plugins`, `get-plugins`)
- Version WordPress / PHP (ex: `get-environment`, `site-info`)
- Thème actif (ex: `get-theme`)

### Étape 2 — Exécuter uniquement les abilities lecture

Pour chaque ability identifiée :

```
mcp__novamira-schoolswp-com__mcp-adapter-execute-ability
```

**Ne jamais exécuter** une ability contenant `create`, `update`, `delete`, `write`, `set`, `install`, `activate`, `deactivate`.

### Étape 3 — Comparer avec le SITE.md actuel

1. Lire `shared/SITE.md`.
2. Identifier les différences avec la sortie MCP :
   - Nouveaux plugins actifs
   - Plugins désactivés / supprimés
   - Versions mises à jour
   - Changement de thème / version WP / PHP

### Étape 4 — Écrire le nouveau SITE.md

Conserver la structure existante :
- Environnement (WP, PHP, locale, multilingue, hébergement, thème)
- Plugins actifs groupés par catégorie (SEO, Fluent, Automation, Multilingue, Contenu, Sécurité, Admin, Infrastructure)
- Doublons détectés
- Ressources critiques
- Stack technique

Mettre à jour la date : `**Dernière mise à jour** : YYYY-MM-DD`.

### Étape 5 — Rapport à l'utilisateur

Format concis :

```
SITE.md refresh — YYYY-MM-DD

Changements :
- +1 plugin : <nom> v<version>
- -1 plugin : <nom> désactivé
- ~3 updates : <plugin> v<old> → v<new>
- Doublons : <liste si nouveaux>

Action recommandée : <si applicable>
```

## Ne pas faire

- Jamais d'écriture côté WordPress (modifier un post, activer un plugin, changer une option).
- Jamais de commit automatique — laisser l'utilisateur valider les changements de SITE.md.
- Jamais de `git push` — écriture locale uniquement.
- Pas de refresh si l'utilisateur n'a pas demandé explicitement ou si SITE.md a < 24h.

## Exemple d'invocation utilisateur

- "Refresh SITE.md"
- "Check les plugins actifs sur schoolswp.com"
- "Update le snapshot WP"
- "SITE.md est à jour ?"
