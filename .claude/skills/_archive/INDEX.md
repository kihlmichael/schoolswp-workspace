# Skills archivés — INDEX

Skills mis hors auto-déclenchement. Invocation manuelle uniquement (le YAML a été gutté : pas de `description`, ou `user-invocable: false`, selon le cas). Ré-activation possible en restaurant le frontmatter original.

Source de vérité pour ce qui était auto-déclenché avant l'archivage.

## Archivés le 2026-04-16

| Skill | Raison |
|---|---|
| `brain` | 10 modes trop larges, intention ambiguë |
| `content-factory-autonome` | Fusionné dans `brain-autonome` |
| `topical-authority-map` | Fusionné dans `cocon-map-schoolswp` |
| `lms-cocon-roi-prioritization` | Généralisé en `cocon-roi-prioritization` |
| `seo-pipeline` | Pipeline 10 tâches trop lourd, réouverture possible en cluster séparé |
| `m1m3-urls-internal-linking` | Plan M1-M3 révolu |
| `youtube` | Espace métier fourre-tout (déjà `user-invocable: false`), remplacé par les skills YouTube spécialisés |
| `youtube-thumbnails` | Doublonnait `thumbnail-strategist`, fusionné |
| `social-content` | Doublonnait `social-media-manager` + collisions avec skills plateforme |
| `instagram-strategy` (workspace) | Doublonné par la version project |
| `reddit` | Pas de priorité canal 2026, mis en veille — ré-activable en restaurant le YAML |
| `schoolswp-branding-studio` (workspace) | Doublonné par `branding` project + modes de création redondants avec skills spécialisés |

## À supprimer manuellement

| Chemin | Raison |
|---|---|
| `projects/schoolswp/.claude/skills/thumbnail-strategist/` | Dossier orphelin (sans SKILL.md, vide) — résidu de réorganisation 2026-04-16 |

Pour la procédure de suppression, voir `feedback_skill_archival.md` en mémoire (gut YAML + bandeau + Explorer).

## Règle de mise à jour

Chaque nouvelle archive = ligne ajoutée ici avec date + raison. Ne pas réinjecter la liste dans le CLAUDE.md racine projet : il pointe simplement vers ce fichier.
