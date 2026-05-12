---
name: schoolswp-content-studio
description: |
  Met en forme du texte brut schoolsWP (notes, transcript, voice note, brouillon, idées en vrac) en contenu court ou intermédiaire prêt à publier. Formats couverts UNIQUEMENT : post LinkedIn/Bluesky, newsletter schoolsWP News (avec PS et bloc offres), script vidéo YouTube.
  Utilise ce skill quand l'utilisateur dit : "écris un post", "rédige la newsletter", "draft newsletter", "newsletter schoolsWP", "newsletter du dimanche", "newsletter de la semaine", "script vidéo", "transforme mes notes", "restructure ce brouillon", "mets en forme ce transcript", "nettoie ce texte", ou fournit du texte brut à structurer.
  NE PAS utiliser pour : article de blog SEO long (voir schoolswp-article-workflow ou thruuu-writer selon input), recyclage d'un article déjà publié (article-multiformat), arbitrage éditorial / priorisation de roadmap (brain-autonome), ou contenu sans lien avec schoolsWP.
---

# schoolsWP Content Studio

## Vue d'ensemble

Ce skill transforme n'importe quel input brut (notes, idees, brief, transcript, texte non structure) en contenu schoolsWP pret a publier, au format Markdown.

Il applique automatiquement les regles d'ecriture, le ton, la structure et l'identite schoolsWP a chaque contenu produit.

## Workflow en 5 etapes

Suivre ces etapes dans l'ordre pour chaque contenu :

### Etape 1 — Identifier le format cible

Determiner le format demande parmi les 4 formats schoolsWP :

| Format                    | Fichier de reference              | Longueur type       |
| ------------------------- | --------------------------------- | ------------------- |
| Article de blog           | `references/format-article.md`    | 1200-2500 mots      |
| Post LinkedIn / Bluesky   | `references/format-post.md`       | 100-200 mots        |
| Newsletter schoolsWP News | `references/format-newsletter.md` | 300-600 mots        |
| Script video YouTube      | `references/format-video.md`      | 5-15 min de lecture |

Si le format n'est pas explicite, le deduire du contexte :

- Texte long + technique → article de blog
- Idee courte + opinion → post LinkedIn/Bluesky
- Anecdote + lecon → newsletter
- Tutoriel visuel → script video

**Action** : lire le fichier de reference du format cible AVANT de commencer a ecrire.

### Etape 2 — Analyser le texte brut

Extraire du texte brut :

1. L'idee centrale (en une phrase)
2. Le probleme que ca resout
3. Les points cles (3-5 max)
4. Les exemples concrets mentionnes
5. Le CTA naturel possible

Si des elements manquent, les inferer du contexte ou demander a l'utilisateur.

### Etape 3 — Charger les regles d'ecriture

**Action** : lire `references/writing-rules.md` pour appliquer les regles schoolsWP.

Ce fichier contient toutes les regles de ton, structure de phrase, mise en forme et interdits. Chaque contenu produit doit passer ces regles.

### Etape 4 — Rediger le contenu

Appliquer simultanement :

- La structure du format cible (etape 1)
- Les regles d'ecriture schoolsWP (etape 3)
- Les elements extraits du texte brut (etape 2)

Principes de redaction :

- Commencer par l'accroche. Toujours.
- Une idee par paragraphe. 2-4 phrases max.
- Phrases de 8-15 mots en moyenne. Jamais plus de 20.
- Zero jargon non explique. Zero blabla marketing.
- CTA doux et contextualise en fin de contenu. Un seul.
- Utiliser les expressions signature schoolsWP naturellement.

### Etape 5 — Produire le fichier .md

Creer le fichier Markdown final.

Convention de nommage : `{format}-{sujet-en-kebab-case}.md`

Exemples :

- `article-workflow-ia-code.md`
- `post-seo-wordpress-erreurs.md`
- `newsletter-fluentcrm-automatisation.md`
- `script-elementor-debutant.md`

---

## Regles critiques

1. **Toujours lire le fichier de reference du format** avant d'ecrire. Chaque format a sa structure propre.
2. **Toujours lire writing-rules.md** avant d'ecrire. Les regles d'ecriture sont non negociables.
3. **Ne jamais produire de contenu generique.** Tout doit etre ancre dans l'univers schoolsWP (WordPress, outils, cas concrets).
4. **Ne jamais depasser 20 mots par phrase** sauf exception rare et justifiee.
5. **Toujours finir par un CTA doux** — jamais agressif, toujours utile.
6. **Orthographe invariable** : "schoolsWP" s'ecrit toujours ainsi, meme en debut de phrase.
7. **Tagline officielle** : "WordPress. Clair. Structure. Utile."

## Formats speciaux

### Contenu SEO / LMS

Pour les articles orientes SEO ou destines au LMS, ajouter obligatoirement :

- **Reponse rapide** : resume en 2-3 phrases sous le H1
- **Points cles** : liste de 3-5 points apres la reponse rapide
- **En resume** : section de synthese avant la conclusion

### Contenu multi-format

Si l'utilisateur demande de decliner un contenu sur plusieurs formats (ex: article → post + newsletter), lire tous les fichiers de reference concernes et produire chaque format dans un fichier .md separe.

---

## Structure des fichiers de reference

```
schoolswp-content-studio/
├── SKILL.md                          <- ce fichier
└── references/
    ├── writing-rules.md              <- regles d'ecriture schoolsWP
    ├── format-article.md             <- template article de blog
    ├── format-post.md                <- template post LinkedIn/Bluesky
    ├── format-newsletter.md          <- template newsletter
    └── format-video.md               <- template script video YouTube
```
