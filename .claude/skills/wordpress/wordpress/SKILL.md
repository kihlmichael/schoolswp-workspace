---
name: wordpress
description: Espace métier WordPress - sites, blogs, WooCommerce et maintenance. Utiliser pour toute tâche liée à WordPress (articles, pages, plugins, thèmes, e-commerce).
user-invocable: false
---

# WordPress Workspace

Espace métier dédié à la gestion des sites WordPress pour schoolsWP.

## Périmètre

- **Contenu** : Articles, pages, médias
- **SEO** : Optimisation on-page, sitemap, schema
- **E-commerce** : WooCommerce, produits, commandes
- **Maintenance** : Mises à jour, sécurité, backups
- **Performance** : Cache, optimisation, CDN

## Structure

```
04_WordPress/
├── SKILL.md          # Ce fichier
├── references/        # Workflows n8n
├── references/       # SOP et checklists
└── assets/        # Templates de contenu
```

## Workflows disponibles

_À créer selon les besoins :_

| Workflow | Description | Status |
|----------|-------------|--------|
| `publish-article.json` | Publication d'article | Placeholder |
| `backup-site.json` | Backup automatisé | Placeholder |
| `update-plugins.json` | Mise à jour plugins | Placeholder |
| `woo-order-notify.json` | Notification commande | Placeholder |

## Procédures

_À documenter :_

- [ ] Checklist publication article
- [ ] Process de maintenance hebdomadaire
- [ ] Guidelines SEO on-page
- [ ] Procédure de déploiement

## Templates

_À créer :_

- [ ] Template article blog
- [ ] Template page landing
- [ ] Template fiche produit

## Dépendances

Ce workspace utilise les skills socle :
- `n8n-code-javascript` pour le scripting
- `n8n-workflow-patterns` pour l'architecture
- `n8n-mcp-tools-expert` pour les intégrations API

## Sites gérés

_À compléter :_

| Site | Type | URL |
|------|------|-----|
| schoolsWP | Principal | _à renseigner_ |

## Prochaines étapes

1. Inventorier les sites WordPress
2. Documenter les process de publication
3. Mettre en place les backups automatisés
