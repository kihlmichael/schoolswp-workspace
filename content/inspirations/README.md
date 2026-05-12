# Inspirations - bibliotheque de patterns

Ce dossier collecte des fiches d'analyse de contenus externes (newsletters, posts LinkedIn, videos YouTube, articles) qui inspirent la production schoolsWP. Chaque fiche extrait les **patterns reutilisables** (hook, structure, CTA, mecaniques) sans copier le contenu source.

## A quoi ca sert

- Construire une bibliotheque de **mecaniques qui marchent** dans la niche WordPress / SEO / IA / SaaS / creator economy.
- Disposer d'un input concret pour les skills de production (`schoolswp-content-studio`, `linkedin`, etc.) : "ecris-moi un post inspire de la fiche X".
- Reperer des angles editoriaux non encore exploites par schoolsWP.
- Garder une trace des contenus marquants pour s'en reinspirer plus tard.

## Comment c'est rempli

Le skill `capture-inspiration` (`.claude/skills/contenu/capture-inspiration/`) cree les fiches automatiquement quand Michael dit :

- "analyse cette newsletter de X"
- "capture les patterns de Y"
- "decortique ce post"
- "ajoute Z a mes inspirations"

Le skill range chaque fiche dans `content/inspirations/<createur>/<YYYY-MM-DD>-<format>-<sujet>.md`.

## Structure du dossier

```
content/inspirations/
├── README.md                              <- ce fichier
├── <createur>/
│   ├── _index.md                          <- profil createur + liste des captures
│   └── <YYYY-MM-DD>-<format>-<sujet>.md   <- fiches individuelles
└── ...
```

### Conventions

| Element | Format | Exemple |
| --- | --- | --- |
| Createur (slug) | kebab-case `prenom-nom` | `nathan-fenina` |
| Format | kebab-case | `newsletter`, `post-linkedin`, `video-youtube`, `carousel-instagram` |
| Sujet | kebab-case 2-4 mots | `assistant-marketing`, `seo-prompts-ai` |
| Slug fichier | `<YYYY-MM-DD>-<format>-<sujet>.md` | `2026-05-05-newsletter-assistant-marketing.md` |

La date dans le slug est celle de **publication** du contenu original. Si elle n'est pas trouvable, utiliser la date de capture.

## Frontmatter standard

Chaque fiche commence par :

```yaml
---
createur: <slug>
format: <format>
sujet: <sujet-kebab>
date_publication: <YYYY-MM-DD ou null>
date_capture: <YYYY-MM-DD>
source_url: <URL ou null>
tags: [<niche>, <mecanique>, <format>]
---
```

## Index par createur

(automaintenu par le skill - ajout de chaque createur ici a la creation du premier `_index.md`)

<!-- index-start -->
<!-- index-end -->

## Regles d'or

1. **Pas de copier-coller integral** d'un contenu paywall. Extrait court uniquement.
2. **La fiche reste en voix schoolsWP** (tutoiement, "je", pas d'em-dash). On analyse, on mime pas.
3. **Toujours remplir la section "Transposition schoolsWP"** sinon la fiche est inutile.
4. **Ne pas juger le createur.** Decrire les mecaniques, pas etoiler.
5. **Tags obligatoires** (3-5) pour pouvoir chercher dans la bibliotheque plus tard.

## Liens

- Skill : `.claude/skills/contenu/capture-inspiration/SKILL.md`
- Outil d'extraction URL : skill `defuddle` (`.claude/skills/external-obsidian/defuddle/`)
- Voix schoolsWP : `content/docs/BRAND_RULES.md`
