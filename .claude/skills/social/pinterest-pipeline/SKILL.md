---
name: pinterest-pipeline
description: |
  Pipeline automatisé d'EXÉCUTION Pinterest schoolsWP (pas stratégie) : orchestration brief → Canva → export → Pinterest API → analytics. Gestion de la file de production pins (20-50 pins/semaine) et sync des analytics.
  Utiliser ce skill quand l'utilisateur demande : "génère des pins", "publie des pins", "pipeline Pinterest", "brief pins", "analytics Pinterest", "file de production Pinterest", "batch pins Pinterest", "sync Pinterest", "exécuter production Pinterest".
  NE PAS utiliser pour : stratégie / pilotage / organisation Pinterest (voir `pinterest-strategy`), publication multi-plateformes (voir `social-media-manager`), autres plateformes sociales.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
  - WebFetch
  - mcp__claude_ai_Canva__generate-design
  - mcp__claude_ai_Canva__generate-design-structured
  - mcp__claude_ai_Canva__export-design
  - mcp__claude_ai_Canva__get-design
  - mcp__claude_ai_Canva__get-design-thumbnail
  - mcp__claude_ai_Canva__search-designs
  - mcp__claude_ai_Canva__get-export-formats
  - mcp__claude_ai_Canva__start-editing-transaction
  - mcp__claude_ai_Canva__perform-editing-operations
  - mcp__claude_ai_Canva__commit-editing-transaction
last_reviewed: 2026-04-23
review_interval_days: 90
---

# Pinterest Pipeline — schoolsWP

Tu es l'orchestrateur du pipeline Pinterest schoolsWP. Tu geres le cycle complet : brief → visuel Canva → export → publication Pinterest → analytics.

## SOP

Source de verite : `systems/pinterest-pipeline/SOP.md`. Lis-la avant toute action.

## Regles absolues

1. **Machine d'etat stricte** : idea → brief_generated → brief_approved → design_generated → design_approved → exported → publish_approved → published → analytics_synced → archived. Jamais sauter un etat.
2. **3 validations humaines** obligatoires (brief, design, publication). Demander explicitement a l'utilisateur.
3. **Anti-doublon** : verifier `published_pin_id` + `content_hash` avant publication.
4. **Export local** : telecharger l'image dans `systems/pinterest-pipeline/exports/` AVANT publication.
5. **Dry-run par defaut** : toujours proposer `--dry-run` avant la premiere execution reelle.

## Modes d'utilisation

### Mode 1 : Generer des briefs

Input : URL d'article(s) schoolsWP ou mot-cle
Output : brief JSON dans `systems/pinterest-pipeline/briefs/`

```
/pinterest-pipeline brief --url https://schoolswp.com/article-slug --board-key seo-wordpress
```

Actions :
1. Lire l'article (WebFetch ou fichier local)
2. Generer 1-5 variations de pin (title, description, alt_text, overlay_text, keywords)
3. Ecrire le brief JSON dans `/briefs/YYYY-MM-DD-pin-XXX.json`
4. Ajouter l'entree dans `pins_queue.json` avec status `brief_generated`
5. Demander validation humaine → passer a `brief_approved`

### Mode 2 : Creer le visuel Canva

Input : pin-id d'un pin en status `brief_approved`
Output : design Canva genere + design_id stocke

Actions :
1. Lire le brief du pin
2. Generer le design via Canva MCP (`generate-design-structured` avec les specs brand)
3. Stocker le `canva_design_id` dans `pins_queue.json`
4. Passer a `design_generated`
5. Montrer un apercu (thumbnail) → demander validation humaine → `design_approved`

### Mode 3 : Exporter et publier

Input : pin-id d'un pin en status `design_approved`
Output : image PNG exportee + pin publie sur Pinterest

Actions :
1. Exporter le design Canva (PNG 1000x1500)
2. Telecharger l'image dans `/exports/pin-XXX.png`
3. Passer a `exported`
4. Afficher le recapitulatif complet (titre, description, board, image)
5. Demander validation humaine finale → `publish_approved`
6. Upload media Pinterest → create pin → stocker `published_pin_id`
7. Passer a `published`

### Mode 4 : Sync analytics

Input : aucun ou pin-id specifique
Output : snapshot analytics dans `/analytics/YYYY-MM-DD.json`

Actions :
1. Pour chaque pin `published` : fetch analytics Pinterest
2. Sauvegarder le snapshot quotidien
3. Passer les pins synces a `analytics_synced`
4. Afficher les top performers

### Mode 5 : Dashboard

Input : aucun
Output : resume de la file de production

Actions :
1. Lire `pins_queue.json`
2. Compter par status
3. Afficher les pins bloques (en attente de validation)
4. Afficher les prochains a traiter

## Design specs Pinterest schoolsWP

| Spec | Valeur |
| --- | --- |
| Format | 1000x1500 px (ratio 2:3) |
| Marge | 50 px |
| Zone texte | Tiers superieur |
| Couleur accent | `#00D400` (barres, CTA, soulignements) |
| Fond sombre | `#12111F` |
| Fond clair | `#FAFBFD` |
| Typo titres | Montserrat Bold, 30pt minimum |
| Typo corps | Open Sans |
| Headline | 3-7 mots, chiffres boostent le CTR |

## Boards

| board_key | Pilier |
| --- | --- |
| `wordpress-guides` | WordPress |
| `seo-wordpress` | SEO |
| `lms-wordpress` | LMS |
| `crm-email` | CRM |
| `automatisation` | Automatisation |
| `plugins` | Plugins |
| `ecommerce` | Ecommerce |
| `freelance` | Freelance |
| `strategie-contenu` | Formation |
| `coulisses` | Coulisses |

## Branding Pinterest

- Nom : toujours `schoolsWP` (jamais SchoolsWP, schoolswp)
- Tutoiement systematique dans les descriptions
- Mots interdits : disruptif, game changer, scalable, hack, revolutionnaire, en un clic, sans effort
- CTA utile : "Decouvre le guide complet", "Teste par toi-meme"
- Disclosure affilie : "Lien affilie — je recommande uniquement les outils que j'utilise au quotidien."

## Fichiers cles

```
systems/pinterest-pipeline/
  SOP.md                    ← source de verite
  CLAUDE.md                 ← regles techniques
  data/pins_queue.json      ← file de production
  data/boards.json          ← mapping board_key → board_id
  data/templates.json       ← mapping template_key → canva_id
  schemas/pin.schema.json   ← validation JSON
  briefs/                   ← briefs JSON par pin
  exports/                  ← images PNG exportees
  analytics/                ← snapshots quotidiens
  logs/                     ← transitions + publications
  src/                      ← scripts Python
```

## Erreurs a ne jamais faire

- Publier un pin sans `publish_approved = true`
- Sauter un etat dans la machine d'etat
- Oublier de verifier le doublon avant publication
- Ne pas telecharger l'export avant publication (URL expire 24h)
- Utiliser `rm` au lieu de `trash`
- Ecrire des secrets dans un fichier versionne
