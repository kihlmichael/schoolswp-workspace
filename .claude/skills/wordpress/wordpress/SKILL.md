---
name: wordpress
description: |
  Espace métier WordPress schoolsWP : index de l'espace de travail (contenu, SEO, e-commerce, maintenance, performance). Pas un skill exécutable, c'est un dossier-parapluie qui organise les workflows et SOPs liés aux sites WP de l'écosystème schoolsWP.
  Utilise ce skill quand l'utilisateur dit : "espace WordPress", "structure dossier WP", "où sont les workflows WP", ou pour naviguer dans l'organisation interne de cet espace métier.
  NE PAS utiliser pour : développement WP réel (utiliser `dev-wordpress` ou skills dédiés `wp-block-development`/`wp-plugin-development`/etc.), router de repo (utiliser `wordpress-router`), production de contenu schoolsWP (utiliser `schoolswp-article-workflow`), ou opérations WP-CLI (utiliser `wp-wpcli-and-ops`).
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
