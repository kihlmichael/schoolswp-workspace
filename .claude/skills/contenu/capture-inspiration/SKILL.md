---
name: capture-inspiration
description: |
  Analyse un contenu externe (newsletter, post LinkedIn, video YouTube, article) pour en extraire les patterns réutilisables (hook, structure, CTA, mecaniques, voix, format), puis range la fiche dans `content/inspirations/<createur>/<date>-<format>-<sujet>.md`. Source : URL (utilise defuddle pour extraire), texte colle, ou capture d'ecran.
  Utilise ce skill quand l'utilisateur dit : "analyse cette newsletter", "capture les patterns de", "inspire-toi de", "decortique ce post", "decompose le hook de", "capture inspiration", "ajoute [X] a mes inspirations", "comment [createur] structure ses [format]", ou colle une URL/texte d'un createur a etudier.
  NE PAS utiliser pour : extraire le texte brut d'une page web sans analyse (utiliser `defuddle` directement), faire un audit concurrentiel SEO (utiliser `radar` agent ou `niche-detector-reachable`), recycler son propre contenu schoolsWP (utiliser `article-multiformat`), ecrire un post inspire d'un autre createur (utiliser le skill plateforme `linkedin` / `instagram-strategy` / `schoolswp-content-studio` avec la fiche d'inspiration en input).
---

# capture-inspiration

## Vue d'ensemble

Ce skill transforme un contenu externe inspirant en **fiche pattern reutilisable** rangee dans `content/inspirations/`. La fiche extrait :

- Le hook (3 premieres phrases, mecanique d'accroche)
- La structure (sections, transitions, CTA)
- La voix (ton, registre, signatures verbales)
- Les mecaniques d'engagement (commenter MOT, lien direct, PS, etc.)
- Le format (longueur, mise en forme, visuels)
- Ce qui est transposable a schoolsWP, ce qui ne l'est pas

Objectif : construire une bibliotheque de patterns pour s'inspirer **sans copier**, et identifier les mecaniques qui marchent dans la niche WordPress / SEO / IA / SaaS.

## Inputs acceptes

1. **URL** (newsletter Substack, article Medium, post LinkedIn public, video YouTube avec subs) - extraction via defuddle ou WebFetch.
2. **Texte colle** dans le message - analyse directe.
3. **Capture d'ecran** (Telegram avec image_path) - Read l'image.
4. **Nom de createur** + format vise - chercher dans `content/inspirations/<createur>/` si deja capture, sinon demander URL.

Si la source est ambigue, demander une seule fois :
- "Tu colles le texte, tu donnes l'URL, ou je cherche dans tes inspirations existantes ?"

## Workflow

### Etape 1 - Recuperer le contenu source

| Source | Methode |
| --- | --- |
| URL Substack / blog / Medium | invoquer skill `defuddle` (rapide, propre) |
| URL LinkedIn (post public) | WebFetch puis nettoyage manuel |
| URL YouTube | utiliser MCP `dataforseo__serp_youtube_video_subtitles_live_advanced` ou demander a l'utilisateur de coller la transcription |
| Texte colle | passer directement a l'etape 2 |
| Capture | Read le fichier image |

### Etape 2 - Identifier le createur et le format

Determiner :
- **Createur** : prenom + nom, ou pseudo (ex: nathan-fenina, justin-welsh, dan-koe)
- **Format** : newsletter, post-linkedin, post-twitter, video-youtube, video-shorts, podcast, article-blog, carousel-linkedin, carousel-instagram
- **Date publication** (si trouvable) ou date de capture
- **Sujet** : 2-4 mots en kebab-case

Slug fichier : `<YYYY-MM-DD>-<format>-<sujet-kebab>.md` (la date est celle de publication de l'original si connue, sinon du jour de capture).

### Etape 3 - Extraire les 7 patterns

Pour chaque contenu, remplir cette grille :

#### 1. Hook (les 3 premieres phrases)

- Citation litterale du hook
- Mecanique identifiee (claque, contre-intuitif, anecdote, chiffre, question, declaration audacieuse)
- Ce qui le rend efficace (1 phrase)

#### 2. Structure narrative

- Liste des sections / beats narratifs (ex: hook → probleme → tentative ratee → solution → resultat → CTA)
- Longueur de chaque beat (en phrases ou paragraphes)
- Transition entre les beats (mots-cles, sauts de ligne, sous-titres)

#### 3. Voix et ton

- Tutoiement / vouvoiement
- "Je" / "nous" / impersonnel
- Registre : pro, decontracte, intime, technique
- Signatures verbales (expressions repetees, tics positifs)

#### 4. Mecaniques d'engagement

- CTA principal (texte exact + position dans le contenu)
- Mecaniques secondaires : commenter MOT, repondre a l'email, liker, partager, lien direct
- Format des CTA : phrase imperative, question, lien nu, bouton
- PS / postscriptum : combien, fonction de chacun

#### 5. Mise en forme

- Longueur totale (mots ou minutes)
- Densite (paragraphes courts ou longs)
- Usage de listes, citations, separateurs (`---`)
- Emojis (lesquels, frequence, fonction)
- Format visuel (carrousel : nombre de slides, cover, hierarchie texte)

#### 6. Offre / monetisation visible

- Y a-t-il une offre dans le contenu ? Laquelle ?
- Position de l'offre (debut, fin, PS)
- Format : lien direct, bloc encadre, mention soft, call to action
- Type : formation, lead magnet, produit, service, affiliation

#### 7. Transposition schoolsWP

- **A garder** : ce qui est universellement applicable (mecanique, structure, hook)
- **A adapter** : ce qui marche dans leur niche mais doit etre traduit pour WordPress/SEO
- **A NE PAS reprendre** : ce qui colle a leur persona et trahirait la voix schoolsWP

### Etape 4 - Produire la fiche Markdown

Format de sortie obligatoire :

```markdown
---
createur: <slug-prenom-nom>
format: <format>
sujet: <kebab-case-sujet>
date_publication: <YYYY-MM-DD ou null>
date_capture: <YYYY-MM-DD>
source_url: <URL ou null si capture/colle>
tags: [<niche>, <mecanique>, <format>]
---

# [Titre original du contenu]

> Source : [URL ou "texte colle" / "capture"]
> Createur : [Nom]
> Format : [format]
> Capture : [date]

## Hook

> [citation litterale]

**Mecanique** : [type]
**Pourquoi ca marche** : [1 phrase]

## Structure narrative

1. [beat 1] - [longueur]
2. [beat 2] - [longueur]
3. ...

## Voix et ton

- [bullets]

## Mecaniques d'engagement

- **CTA principal** : "[texte]" ([position])
- **Mecaniques secondaires** : [...]
- **PS** : [nombre + fonction]

## Mise en forme

- Longueur : [...]
- Densite : [...]
- Emojis : [...]

## Offre / monetisation

[bloc ou "absent"]

## Transposition schoolsWP

### A garder
- [...]

### A adapter
- [...]

### A NE PAS reprendre
- [...]

---

## Texte source (extrait nettoye)

> [extrait pertinent ou texte complet si court]
```

### Etape 5 - Ranger le fichier

Chemin de sortie : `content/inspirations/<createur>/<YYYY-MM-DD>-<format>-<sujet>.md`

Si le dossier `content/inspirations/<createur>/` n'existe pas, le creer.

Si une fiche existe deja avec le meme slug, ajouter `-v2` au slug et signaler a l'utilisateur.

### Etape 6 - Mettre a jour l'index createur

Si le dossier `<createur>/` n'a pas de `_index.md`, le creer avec :

```markdown
# Inspirations : [Nom]

> Slug : <createur>
> Niche : [...]
> Pourquoi je suis : [1-2 phrases - angle, mecaniques signature]
> Profil principal : [URL]

## Captures

- [YYYY-MM-DD] [format] [sujet] - [lien fichier]
- ...
```

Si l'index existe, ajouter une ligne dans la section "Captures" en respectant l'ordre antichronologique (plus recent en haut).

## Regles critiques

1. **Toujours nettoyer le texte source.** Pas de pub, pas de footer, pas de "subscribe" en plein milieu.
2. **Ne jamais inventer les patterns.** Si une grille n'est pas observable dans le contenu, ecrire "non observable" plutot que halluciner.
3. **Citer litteralement le hook.** C'est ce qui sera reutilise comme reference, donc precision exacte.
4. **Ne pas juger le createur.** La fiche est un outil, pas une critique. Pas de "c'est nul" ou "c'est genial". Decrire les mecaniques, point.
5. **Toujours remplir la section "transposition schoolsWP".** C'est le coeur de la fiche : sans cette section, c'est juste un resume.
6. **Respecter la voix schoolsWP dans la fiche.** Tutoiement, "je", pas d'em-dash. La fiche elle-meme suit les regles BRAND_RULES.md.
7. **Pas de copier-coller integral d'un contenu paywall ou prive.** Si l'URL est derriere paywall ou demande de connexion, demander a l'utilisateur de coller un extrait court (fair use).

## Convention de nommage

| Element | Format | Exemple |
| --- | --- | --- |
| Createur (slug) | kebab-case prenom-nom | `nathan-fenina` |
| Format | kebab-case | `newsletter`, `post-linkedin`, `video-youtube`, `carousel-instagram` |
| Sujet | kebab-case 2-4 mots | `assistant-marketing`, `seo-prompts-ai` |
| Slug fichier | `<YYYY-MM-DD>-<format>-<sujet>.md` | `2026-05-05-newsletter-assistant-marketing.md` |
| Index createur | `<createur>/_index.md` | `nathan-fenina/_index.md` |

## Anti-patterns

- **Capture sans transposition** : si tu rends la fiche sans la section "Transposition schoolsWP", elle est inutile. Refais.
- **Copier le ton du createur** : tu analyses, tu ne mimes pas. La fiche reste en voix schoolsWP.
- **Trop de patterns** : 7 sections suffisent. N'en ajoute pas.
- **Resume au lieu d'analyse** : un resume du contenu n'est pas une fiche pattern. Si tu as ecrit "il dit que..." plus de 2 fois, recommence.
- **Fiche sans tags** : les tags servent a chercher dans la bibliotheque. Toujours en mettre 3-5.

## Integration avec d'autres skills

- **defuddle** : utilise pour extraire un article/newsletter propre depuis une URL.
- **schoolswp-content-studio** : la fiche d'inspiration est un input ideal - Michael peut dire "ecris-moi un post LinkedIn inspire de la fiche `nathan-fenina/2026-05-05-newsletter-assistant-marketing.md`".
- **brain-autonome** : peut utiliser les fiches comme contexte strategique pour choisir des angles editoriaux.
