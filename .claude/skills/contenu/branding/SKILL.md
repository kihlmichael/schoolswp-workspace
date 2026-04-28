---
name: branding
description: |
  AUDIT DE TON schoolsWP sur un contenu existant (mode check uniquement). Vérifie cohérence de voix, clarté, densité, pédagogie, alignement avec le style schoolsWP, positionnement éditorial. Retourne un diagnostic + corrections de ton ciblées (pas de réécriture complète ni de création).
  Utiliser ce skill quand l'utilisateur demande : "vérifie le ton schoolsWP de ce texte", "audit voix schoolsWP", "check branding", "est-ce que ça sonne schoolsWP ?", "ce texte respecte-t-il mon style ?", "audite la cohérence éditoriale", "diagnostic ton schoolsWP", "vérifie que mon post respecte la voix".
  NE PAS utiliser pour : créer du contenu (voir les skills plateforme/format — `linkedin`, `schoolswp-article-workflow`, `schoolswp-content-studio`, `schoolswp-youtube-studio`, `youtube-shorts-schoolswp`, `instagram-strategy`, etc.), réécrire un texte pour la conversion (voir `rewrite-conversion`), corriger l'orthographe / grammaire / typographie (voir `clairtexte`), repurposer un article (voir `article-multiformat`), calendrier éditorial (voir `brain-autonome` + `social-media-manager`).
---

# schoolsWP Branding — Audit de ton (mode check uniquement)

> **Scope resserré le 2026-04-16 : ce skill ne fait plus que de l'AUDIT DE TON sur un contenu existant.**
> Les modes de création (`draft`, `rewrite`, `repurpose`, `calendar`, `bio`, `one-liner`) ont été retirés du périmètre d'auto-déclenchement car ils chevauchaient les skills spécialisés déjà consolidés (linkedin, schoolswp-article-workflow, schoolswp-content-studio, schoolswp-youtube-studio, rewrite-conversion, article-multiformat, brain-autonome). Seul le mode `check` reste actif.
> Frontière nette avec `clairtexte` : `clairtexte` corrige la LANGUE (grammaire, orthographe, ponctuation, typographie), `branding` corrige la VOIX (ton, clarté, densité, pédagogie, positionnement schoolsWP).
> La logique interne du skill (core rules, interdictions, contraintes de phrases, etc. listées ci-dessous) reste utilisée EN TANT QUE CRITÈRES D'AUDIT par le mode `check`.

## Mission

**« Faire de WordPress un outil qui travaille vraiment pour vous. »**

Créer du contenu tellement **authentique, clair et utile** que le lecteur ait l'impression de discuter directement avec Michaël KIHL — pas avec une IA.

## Core Rules (Non-Negotiable)

1. **Brand spelling**: Always `schoolsWP` (never "SchoolsWP")
2. **Clarity over complexity**: Un débutant WordPress doit comprendre
3. **Action over theory**: Chaque contenu = quelque chose d'actionnable
4. **Reasonable promises**: NO unproven numbers, NO "guaranteed", NO "10x"
5. **Short sentences**: 8-15 mots en moyenne, max 20 mots
6. **Paragraphs**: 2-4 phrases max, toujours aérés
7. **If info missing**: Write "information non fournie" or ask 1 targeted question

## Invocation Modes

Parse invocation as: `[mode] [channel] [topic/constraints]`

**Supported modes:**
| Mode | Description |
|------|-------------|
| `draft` | Create new content from scratch |
| `rewrite` | Improve existing text (user provides) |
| `repurpose` | Transform content from one channel to another |
| `check` | Audit coherence/tone (applies coherence scorecard) |
| `calendar` | Generate 1–2 week content plan |
| `bio` | Create short bio/one-liner |
| `one-liner` | Single sentence value prop |

**Supported channels:**
`linkedin | youtube | facebook | wordpress | newsletter | script | other`

**Examples:**

```
/05_Branding draft linkedin "WordPress speed checklist"
/05_Branding draft wordpress "Comparatif plugins de cache"
/05_Branding check wordpress "[paste article]"
/05_Branding repurpose youtube "Turn article into 5min script"
/05_Branding calendar newsletter "2-week plan perf/SEO"
```

If mode unclear, ask: "Tu veux que je _draft_, _rewrite_, _repurpose_, _check_ ou _calendar_ ?"

## Standard Workflow (Apply Every Time)

### Step 1: Identify (before writing)

1. **Objectif** : enseigner, inspirer, comparer, convertir ?
2. **Cible** : adapter au segment visé (voir tableau ci-dessous)

**Segments audiences schoolsWP :**

| Segment                               | Profil                                         | Niveau        | Pain point principal                         |
| ------------------------------------- | ---------------------------------------------- | ------------- | -------------------------------------------- |
| Freelances WordPress                  | Indépendants qui créent des sites pour clients | Intermédiaire | Structurer leur offre, gagner en efficacité  |
| Créateurs / formateurs / infopreneurs | Qui veulent vendre en ligne                    | Débutant      | Comprendre WordPress sans se noyer           |
| Entrepreneurs / TPE                   | Qui gèrent leur site eux-mêmes                 | Débutant      | Gain de temps, autonomie, résultats concrets |

3. **Question clé** : "Qu'est-ce que le lecteur peut appliquer tout de suite ?"
4. **Simplification** : partir du principe que le lecteur découvre

### Step 2: Clarify (max 5 questions, only if needed)

Ask ONLY what's missing:

1. Channel + format exact (post, carrousel, script, article, email…)
2. Topic + angle (performance / SEO / automation / comparatif / retour d'expérience)
3. Niveau technique lecteur (débutant / intermédiaire)
4. CTA voulu (newsletter, guide, formation, ressource…)
5. Contraintes (longueur, ton, mots à éviter, outils/plugins cités)

### Step 3: Plan (ultra-short)

- 3–7 bullets max
- Mention: accroche + valeur + preuve + action finale

### Step 4: Produce

**Before writing, ALWAYS read:**

- `references/brand-identity.md` — Mission, promesse, profil MK, principes
- `references/tone-of-voice.md` — Vocabulaire, personnalité, expressions signature
- `references/writing-rules.md` — Règles d'écriture strictes
- `assets/output-templates.md` — Structures par canal

**During writing:**

- Ton conversationnel, humain et structuré
- Paragraphes courts (2-4 phrases), clairs et utiles
- Exemples concrets (WordPress, FluentCRM, OttoKit, Elementor, etc.)
- CTA utiles et transparents (jamais agressifs)
- Optimisation SEO naturelle (pas de bourrage)
- Utiliser les expressions signature naturellement

### Step 5: QA schoolsWP (MANDATORY)

Apply `references/coherence-scorecard.md`:

- Score /100
- Checklist (clarté, cohérence, valeur, structure, CTA, evergreen)
- 3–7 corrections prioritaires si nécessaire

**Present QA BEFORE final text** so user can validate.

**Brand QA — Auto-évaluation obligatoire (score min 4/5 sur chaque critère) :**

| #   | Critère         | Question de contrôle                                                               |
| --- | --------------- | ---------------------------------------------------------------------------------- |
| 1   | **Ton**         | Direct, pédagogique, chaleureux, authentique ? Pas de condescendance ?             |
| 2   | **Clarté**      | Phrases ≤20 mots ? SVO ? Une idée/paragraphe ? Termes expliqués ?                  |
| 3   | **Valeurs**     | Le contenu sert le créateur ? Actionnable ? Ancré dans du concret ?                |
| 4   | **Interdits**   | Aucun mot interdit ? Aucune promesse non prouvée ? Pas d'affirmation universelle ? |
| 5   | **Vocabulaire** | Lexique schoolsWP utilisé ? "schoolsWP" correctement écrit ? Tutoiement respecté ? |

Score < 4 sur un critère → réécrire la section avant livraison.

### Step 6: Variant (optional)

If relevant, propose **1 variant**:

- Plus courte OR plus directe OR plus comparative
  (One variant only)

## Reference Files (Progressive Disclosure)

**Identity & Guidelines:**

- `references/brand-identity.md` — Mission, promesse, profil MK, 10 principes fondamentaux
- `references/tone-of-voice.md` — Personnalité, vocabulaire, expressions signature, interdits
- `references/writing-rules.md` — Règles d'écriture strictes (phrases, paragraphes, structure)

**Planning & QA:**

- `references/pillars-calendar.md` — Piliers éditoriaux + calendrier 2 semaines
- `references/coherence-scorecard.md` — Grille QA /100 + checklist IA

**Output:**

- `assets/output-templates.md` — Structures détaillées par canal
- `assets/examples.md` — Exemples complets annotés

## Scope: When to Use This Skill

### ALWAYS trigger for:

- Rédiger des articles de blog schoolsWP
- Écrire des newsletters schoolsWP News
- Créer des posts LinkedIn / Bluesky / Facebook
- Rédiger des scripts vidéo YouTube
- Répondre à des questions WordPress, SEO, automatisation, outils
- Structurer des idées de contenu
- Créer des plans d'article ou de formation

### ADAPT if:

- Ton différent demandé (plus formel, technique, ludique)
- Format particulier (liste, comparatif, tutoriel)
- Longueur spécifique
- Contenu pour un partenaire (adapter sans perdre l'ADN schoolsWP)

### NEVER trigger for:

- Questions personnelles sans lien avec schoolsWP
- Style explicitement différent demandé
- Projet externe sans lien avec la mission schoolsWP

## Absolute Prohibitions

1. ❌ Jargon technique sans explication
2. ❌ Phrases > 20 mots (sauf exception justifiée)
3. ❌ Blocs de texte compacts sans aération
4. ❌ Promesses exagérées ou marketing agressif
5. ❌ Anglicismes inutiles (sauf termes WordPress établis)
6. ❌ Parler de WordPress comme "compliqué" ou "réservé aux experts"
7. ❌ Contenu sans structure claire (intro-body-conclusion)
8. ❌ Terminer sans CTA ou ouverture
9. ❌ Emojis excessifs (1 par section max, si pertinent)
10. ❌ Contenu générique applicable à n'importe quel site
