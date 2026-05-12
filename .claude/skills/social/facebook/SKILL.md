---
name: facebook
description: |
  Espace métier Facebook schoolsWP : pages, groupes, publicité, Messenger, analytics. Hub de référence pour publication, modération, ads et insights cross-platform — workflows et SOP en cours de constitution.
  Utilise ce skill quand l'utilisateur dit : "publie sur la page Facebook schoolsWP", "modère le groupe", "configure une campagne ads Facebook", "rapport publicitaire FB", "automatise Messenger", ou demande une action métier sur l'écosystème Facebook.
  NE PAS utiliser pour : adaptation et publication multi-plateformes orchestrée (utiliser `social-media-manager` via Blotato), création copy LinkedIn/Instagram/Pinterest (utiliser le skill plateforme dédié), ou stratégie social globale sans canal Facebook (utiliser `pulse` agent).
user-invocable: false
---

# Facebook Workspace

Espace métier dédié à la gestion de présence Facebook pour schoolsWP.

## Périmètre

- **Pages** : Publication, modération, insights
- **Groupes** : Animation, engagement, modération
- **Publicité** : Création, gestion, reporting
- **Messenger** : Automatisation, chatbots
- **Analytics** : Performances cross-platform

## Structure

```
03_Facebook/
├── SKILL.md          # Ce fichier
├── references/        # Workflows n8n
├── references/       # SOP et checklists
└── assets/        # Templates de contenu
```

## Workflows disponibles

_À créer selon les besoins :_

| Workflow | Description | Status |
|----------|-------------|--------|
| `publish-page-post.json` | Publication sur page | Placeholder |
| `group-moderation.json` | Modération automatisée | Placeholder |
| `ads-reporting.json` | Rapport publicitaire | Placeholder |

## Procédures

_À documenter :_

- [ ] Checklist de publication page
- [ ] Process de modération groupe
- [ ] Guidelines publicité

## Templates

_À créer :_

- [ ] Template post page
- [ ] Template post groupe
- [ ] Template réponse messenger

## Dépendances

Ce workspace utilise les skills socle :
- `n8n-code-javascript` pour le scripting
- `n8n-workflow-patterns` pour l'architecture
- `n8n-validation-expert` pour le debug

## Prochaines étapes

1. Inventorier les pages/groupes gérés
2. Documenter les process actuels
3. Identifier les automatisations prioritaires
