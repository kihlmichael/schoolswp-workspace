# Calendrier editorial schoolsWP

Source de verite Markdown du **planning editorial multi-canal** schoolsWP. Versionne dans git, lu/ecrit par Claude Code via le skill `calendrier-edito-schoolswp`.

## Pourquoi Markdown et pas Sheets ?

- **Coherence** : tout le contenu schoolsWP vit en `.md` versionne (`content/articles/`, `audits/`, `decisions/`, `inspirations/`).
- **Diff git** : on voit l'evolution du planning sur chaque commit / PR.
- **Lecture/ecriture native par Claude** : pas besoin de MCP cloud a chaque interaction.
- **Pas de dependance** : si Sheets/Drive tombe, le calendrier reste consultable en local.

**Export Sheets** : disponible a la demande via `tools/calendrier-export-sheets.py` (a creer si besoin) pour vue tableau partageable. La source reste Markdown.

## Structure du dossier

```
content/calendrier-edito/
├── README.md           <- ce fichier
├── _backlog.md         <- idees non datees, en attente de slot
├── _legende.md         <- legende statuts + canaux
├── 2026-05.md          <- mois courant
├── 2026-06.md
└── ...
```

Un fichier par mois (format `YYYY-MM.md`). Ajout d'un nouveau mois quand le precedent se termine ou quand on planifie a 4+ semaines.

## Format d'une entree

Chaque publication = une section `##` avec format strict :

```markdown
## YYYY-MM-DD - <canal> - <sujet court>
- **Statut** : idea | draft | scheduled | published | killed
- **Canal** : newsletter | linkedin | bluesky | pinterest | youtube | youtube-shorts | blog | instagram | reddit | discord | email-promo
- **Pilier** : LMS | CRM | SEO | automatisation | ecommerce | freelance | formation | meta
- **Sujet** : phrase courte (max 12 mots)
- **Lien output** : `content/<chemin>` ou null si pas encore drafte
- **Inspiration** : lien fiche `content/inspirations/...` ou null
- **CTA** : produit/lead magnet/article cible (URL cloak schoolswp.com/<slug>/)
- **Notes** : optionnel, contraintes ou idees
```

### Exemple

```markdown
## 2026-05-12 - newsletter - Pinterest pipeline pas a pas
- **Statut** : draft
- **Canal** : newsletter
- **Pilier** : automatisation
- **Sujet** : Comment Claude pilote ma generation de pins via n8n + Placid
- **Lien output** : content/newsletters/2026-05-12-pinterest-pipeline.md
- **Inspiration** : null
- **CTA** : schoolswp.com/pinterest-strategy/
- **Notes** : capture d'ecran workflow n8n a inclure
```

## Conventions

| Element | Regle |
| --- | --- |
| Date | `YYYY-MM-DD` toujours, jamais relatif ("la semaine prochaine") |
| Canal | un seul canal par entree. Si publication multi-canal le meme jour, creer une entree par canal |
| Sujet | impersonnel, pas de "je vais ecrire" - directement l'angle |
| Pilier | obligatoire, choisir parmi la liste fermee |
| Lien output | path relatif au repo, prefixe `content/` |
| Slot | une entree par jour par canal. Pas 2 newsletters le meme jour |

## Statuts

| Statut | Sens | Action attendue |
| --- | --- | --- |
| `idea` | concept attribue a une date, pas encore drafte | a transformer en draft a J-7 |
| `draft` | brouillon en cours dans `content/<chemin>` | relire, finaliser |
| `scheduled` | drafte, valide, programme dans l'outil de pub (Buffer, Blotato, FluentCRM) | rien, attendre l'envoi |
| `published` | publie | ajouter URL live + metriques en notes |
| `killed` | abandonne (deprio, sujet invalide, refait) | conserver pour historique, ne pas supprimer |

## Canaux suivis

| Canal | Cadence cible | Skill associe |
| --- | --- | --- |
| `newsletter` | 1/semaine (dimanche) | `schoolswp-content-studio` |
| `linkedin` | 2-3/semaine | `linkedin` |
| `bluesky` | 2-3/semaine | `linkedin` (meme structure) |
| `pinterest` | 5-10 pins/semaine | `pinterest-pipeline` |
| `youtube` | 1-2/mois | `schoolswp-youtube-studio` |
| `youtube-shorts` | 1-3/semaine | `youtube-shorts-schoolswp` |
| `blog` | 1-2 articles longs/mois (pilier ou cluster) | `schoolswp-article-workflow` |
| `instagram` | 1-2 carrousels/semaine | `instagram-strategy` + `social/contenu-reseaux-sociaux-schoolswp` |
| `reddit` | 1/semaine | `reddit-strategist` |
| `discord` | au fil de l'eau | `discord` |
| `email-promo` | adhoc (lancement, news plugin) | `lead-magnet-schoolswp` ou `plugin-email-sequence` |

## Backlog `_backlog.md`

Idees sans date attribuee. Format identique mais sans `## YYYY-MM-DD`, juste `## idea-<slug>`. Le skill `calendrier-edito-schoolswp` peut proposer des slots pour les idees du backlog.

## Audit / queries supportees par le skill

- "qu'est-ce que je publie cette semaine ?" → liste les entrees J vers J+7
- "audit calendrier mai" → lit `2026-05.md`, signale gaps (jours sans pub) et incoherences
- "prochaines newsletters" → filtre canal `newsletter` ordre date
- "ajoute [sujet] au calendrier le [date] sur [canal]" → cree l'entree
- "marque [entree] comme published avec URL [...]" → MAJ statut
- "deplace l'entree du [date1] au [date2]" → reschedule
- "quelles idees du backlog peuvent etre planifiees ?" → propose slots

Detail dans `.claude/skills/engines/calendrier-edito-schoolswp/SKILL.md`.

## Liens

- Skill : `.claude/skills/engines/calendrier-edito-schoolswp/SKILL.md`
- Production newsletter : skill `schoolswp-content-studio`
- Inspirations : `content/inspirations/`
- Tasks projet (different) : `core/tasks/todo.md` (taches dev/audit, pas publications)
