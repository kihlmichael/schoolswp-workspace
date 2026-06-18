# Standard Operating Procedure (SOP) - Claude + Novamira WordPress Builds (schoolsWP Edition)

---

## Document Control & Changelog

- **Date de version** : 2026-06-04
- **Version** : 1.1.0
- **Auteur** : schoolsWP team

### Changelog :
- `1.1.0` (2026-06-04) : Addition of decision matrix, concrete examples, anti-patterns list, naming conventions, test protocol, logging rules, and pattern granularity recommendations.
- `1.0.0` (2026-06-04) : Initial consolidated release.

---

## Part 1: Technical Build Guidelines (Gutenberg & TT5 Theme)

You are Claude Code working with the Novamira MCP adapter to build native WordPress websites.

### 1. Priority Order
When rules conflict, follow this priority order:
1. **Editor friendliness** : The site must remain fully editable by a non-technical user in the WordPress block editor.
2. **Native WordPress & Gutenberg first** : Use default features, Core blocks, and official methods first.
3. **Maintainability** : Structures must be simple and clean.
4. **Performance** : Keep DOM trees flat, omit heavy scripts, and optimize assets.
5. **Accessibility** : Follow basic standards (contrast, semantic hierarchy, alt texts).
6. **Reusability** : Prefer patterns and template parts over duplicated code.
7. **Visual polish** : Respect design systems without custom overhead.
8. **Custom code only as a last resort**.

### 2. Hard Constraints
Do not create:
- Custom PHP (unless writing sandbox utility scripts)
- Custom JavaScript or React components
- Custom Gutenberg blocks
- Complex custom HTML
- External font loading scripts (use Font Library)
- CSS that replaces what `theme.json` or Global Styles can already handle

### 3. Template & Template Parts Strategy
- **Templates** : Create custom templates only when structurally necessary or reusable (e.g., *Home, Default Page, Landing Page, Blog Archive, Single Post*). Avoid creating one-off templates like *About, Contact, Services*.
- **Template Parts** : Use only for repeated global areas like *Header, Footer, Navigation, Sidebar*.

### 4. theme.json & Global Styles Strategy
`theme.json` is the source of truth for:
- Color palette
- Typography (fonts, sizes, fluid typography)
- Spacing scale
- Layout width (content, wide)
- Border radius and shadow presets
- Button, heading, and link styles
- Default block spacing

*Do not hardcode global design decisions inside individual blocks. Put them in theme.json or Global Styles.*

### 5. Font & CSS Rules
- **Fonts** : Always use the native WordPress Font Library. Do not import fonts via CSS imports or external scripts.
- **CSS** : Custom CSS is allowed only for micro-spacing adjustments, responsive fixes not possible natively, utility classes, and minor visual effects unavailable through core block controls. Keep it minimal and scoped.

---

## Part 2: schoolsWP Adaptation Layer (Règles Éditoriales & Graphiques)

This section details the brand rules, copywriting constraints, and tone requirements for **schoolsWP** projects.

### 1. schoolsWP Core Intent
schoolsWP helps creators, freelancers, trainers, and small businesses make WordPress clearer, more structured, and more useful.
- **From**: "WordPress feels complex, scattered, and hard to manage."
- **To**: "WordPress becomes clear, structured, useful, and easier to run."

*Do not build decorative pages. Build useful, clear, structured WordPress experiences.*

### 2. schoolsWP Brand Principles
- **Clarity before style** : Design must feel calm, structured, readable, and generous in spacing.
- **Pedagogy before persuasion** : Human explanations, no buzzwords or hype marketing.
- **Autonomy before dependency** : Clean block structure inside Gutenberg so the user doesn't need a developer to make simple edits.

### 3. Tone and Language Rules (Français)
- **Tutoiement** : For French content, always use **"tu"** (tutoiement).
- **Style direct** : Use **"je"** or **"sur schoolsWP"** / **"dans mon cas"** / **"l'objectif est simple"**.
- **Avoid** : *"nous", "notre", "nos", "chez schoolsWP, nous", "on vous accompagne"*, vague marketing language, and exaggerated promises.

### 4. Brand Naming Rules
Always write the brand name exactly as:
**schoolsWP**
*(Never write: SchoolsWP, schoolswp, Schools WP, schools wp, schoolWP, or Schoolswp).*
*Even at the beginning of a sentence, keep the lowercase "s".*

### 5. Typographic Restriction
Do not use em dashes or en dashes. Never use `—` or `–`.
Use instead:
- simple hyphen: `-`
- colon: `:`
- period: `.`
- parentheses: `()`

### 6. Affiliate and Recommendation Rules
- Include the canonical French disclosure at the top of pages containing affiliate links:
  > ℹ️ **Lien affilié** - Je recommande uniquement les outils que j'utilise au quotidien. Si vous achetez via ce lien, je peux recevoir une commission sans surcoût pour vous.
- List at least 2 real limitations or weaknesses for every recommended tool.
- Respect the exact casing of verified promo codes. Never invent codes.

### 7. design-system-schoolswp
Visual tokens to use:
- **Primary Color** : `#0f172a` (Slate 900)
- **Secondary Color** : `#1e293b` (Slate 800)
- **Brand Accent** : `#0ea5e9` (Sky 500) - For buttons, links, highlights
- **Green Recommend** : `#10b981` (Emerald 500) - For positive verdicts
- **Calm Background** : `#f8fafc` (Slate 50) - For content cards and areas
- **Radius** : `12px` rounded corners
- **Fonts** : `Outfit` for headings, `Inter` for body copy

---

## Part 3: Novamira, Security, and Environment Protocols

### 1. Novamira MCP Capabilities
- **Read & List** : `novamira/read-file`, `novamira/list-directory`.
- **Write & Edit** : `novamira/write-file`, `novamira/edit-file` (PHP files can only be written to sandbox directory `wp-content/novamira-sandbox/`).
- **Post management** : `novamira/create-post`, `novamira/update-post`, `novamira/delete-post`.
- **Shell & PHP execution** : `novamira/run-wp-cli` (Run WP-CLI commands) and `novamira/execute-php` (executes PHP within the full WP lifecycle).

### 2. Staging vs Production & Backups
- **No direct production edits** : All complex/structure updates must be performed on Staging/Local or as a draft.
- **Mandatory Backup (Niveau 3)** : Before any Level 3 modification (e.g. editing `theme.json`, template files), execute:
  1. Export `theme.json` / target file to a backup file under `wp-content/novamira-sandbox/backups/`.
  2. Create a rollback plan (original block markup snippet).

### 3. Risk Control Grid
- **Niveau 1 - Autorisé sans validation** : Draft pages, simple copy edits, auditing layout options.
- **Niveau 2 - Validation recommandée** : Adjusting local responsive styling, creating a new pattern.
- **Niveau 3 - Validation obligatoire** : theme.json edits, template / header / footer edits, page url/slug edits.

---

## Part 4: Report Formats

Use the appropriate template depending on the changes made:

### A. Format Court (Petites modifications)
```markdown
### 1. Modifications réalisées
- [Détail court de ce qui a changé]

### 2. Justification
- [Pourquoi ce changement est nécessaire]

### 3. À vérifier
- [Lien/Élément à valider par l'utilisateur]
```

### B. Format Complet (Changements structurels - Obligatoire pour Niveau 3)
```markdown
### 1. Fichiers & Éléments modifiés
- **Fichiers** : [Liste des chemins]
- **Templates** : [Nom des templates]
- **Patterns** : [Patterns créés/modifiés]

### 2. Décisions techniques & theme.json
- [Détail des clés modifiées dans theme.json ou Global Styles]

### 3. Risques & Rollback
- **Risques** : [Usabilité, responsive, etc.]
- **Rollback** : [Chemin de la sauvegarde créée]

### 4. Checklist de validation QA
- [ ] Responsive Desktop/Tablet/Mobile vérifié
- [ ] Accessibilité respectée
```

---

## Part 5: Bibliothèque de Patterns & QA final

### 1. Bibliothèque de 10 Patterns Prioritaires
1. **Hero pédagogique** : Grande bannière claire, titre principal H1 Outfit, courte phrase d'intention décrivant le bénéfice.
2. **Problème / Solution** : Structure double colonne listant le problème ("Le constat") et la solution apportée.
3. **Ce que tu vas comprendre** : Carte grise (Slate 50) avec une liste à puces décrivant l'objectif de la page.
4. **Méthode en étapes** : Liste numérotée stylisée en blocs verticaux avec des pas de numéros Sky 500.
5. **Checklist actionnable** : Blocs à cocher pour guider l'utilisateur dans son autonomie.
6. **CTA Guide** : Section d'appel à l'action invitant à télécharger ou lire un guide pratique.
7. **Recommandation plugin** : Bloc de mise en valeur d'une extension validée par schoolsWP.
8. **Limites à connaître** : Bloc d'honnêteté listant au moins 2 faiblesses d'un outil.
9. **Verdict personnel** : Encadré bordure verte Emerald 500 donnant la conclusion du test.
10. **FAQ pédagogique** : Bloc de questions-réponses structuré pour le SEO evergreen.

### 2. schoolsWP Brand QA Scorecard
Rate from 1 to 5 at the end of your execution response:
- **Tone** (tutoiement, pedagogic tone, direct)
- **Clarity** (clear in under 10 seconds)
- **Usefulness** (practical intent)
- **Editorial consistency** (capitalization schoolsWP, simple hyphen, no en/em dashes)
- **Technical sobriety** (flat block structure, no custom overhead)
- **Editor friendliness** (admin editability)
- **Performance awareness** (no excessive scripting)
- **WordPress-native alignment** (TT5 compatibility)
*If any score is below 4, explain what must be corrected.*

---

## Part 6: Éléments Complémentaires schoolsWP

### 1. Matrice de Décision Rapide
Utiliser ce barème de décision avant de commencer une intégration :
- **Section unique sur une page** -> Écrire directement dans le contenu de la page.
- **Section réutilisable sur plusieurs pages** -> Créer un **Pattern** Gutenberg.
- **Structure de page globale commune** -> Créer un **Template** (Modèle).
- **Règles graphiques et styles globaux** -> Modifier le fichier **theme.json**.
- **Besoin d'ajustement local introuvable dans Gutenberg** -> CSS minimal ciblé (via classe CSS).

### 2. Exemples Concrets de Structures schoolsWP
- **Page Guide** : Hero pédagogique -> Bloc "Ce que tu vas comprendre" -> Étapes de la méthode -> Checklist actionnable -> Conclusion & CTA vers ressource.
- **Page Comparatif** : Hero -> Tableau comparatif -> Plugin 1 (Détails + Limites + Verdict) -> Plugin 2 (Détails + Limites + Verdict) -> Synthèse & Recommandation finale.
- **Page Outil Affilié** : Affiliate Disclosure -> Hero -> Description de l'outil -> Pour qui c'est utile -> Limites -> Verdict et CTA Affilié.
- **Landing Page Service** : Hero clair -> Problème / Solution -> Avantages du service -> Témoignages ou cas d'usage -> FAQ pédagogique -> Formulaire ou CTA.

### 3. Anti-patterns à Éviter
- Créer un modèle (Template) WordPress pour chaque page (About, Contact, etc.).
- Utiliser du CSS personnalisé pour des espacements ou des couleurs déjà gérés par theme.json.
- Empiler de multiples conteneurs (Group blocks) imbriqués ralentissant l'éditeur.
- Intégrer des animations JavaScript ou CSS lourdes sans réelle valeur pédagogique.
- Modifier le theme.json global pour satisfaire un besoin esthétique localisé sur une seule page.

### 4. Convention de Nommage
- **Patterns** : `schoolswp-[categorie]-[nom]` (ex: `schoolswp-hero-guide`, `schoolswp-cta-resource`).
- **Templates** : `schoolswp-[nom]` (ex: `schoolswp-landing`, `schoolswp-single-course`).
- **Classes CSS** : `is-style-schoolswp-[effet]` (ex: `is-style-schoolswp-border-accent`).
- **Fichiers SOP** : `SOP-schoolswp-[domaine].md`.

### 5. Protocole de Test Réel
1. Déployer les modifications sur une **page de staging**.
2. Demander un audit initial de la page et de l'existant à Claude.
3. Exposer le plan de modification technique.
4. Appliquer les modifications en mode brouillon.
5. Valider l'éditabilité et la structure Gutenberg dans l'admin.
6. Tester le responsive sur Mobile/Tablet.
7. Effectuer la validation finale avec le score Brand QA.

### 6. Règles de Journalisation (Changelog local)
Toute modification sur le site doit faire l'objet d'une entrée simple dans un fichier `log.md` ou en fin de rapport :
- **Date** : [Date]
- **Action** : [Titre de l'action]
- **Zones touchées** : [Templates / Pages / Fichiers]
- **Raison** : [Pourquoi]
- **Risque** : [Risque identifié]
- **Rollback** : [Méthode de retour à l'état initial]

### 7. Granularité des Patterns
- **Patterns recommandés** : Privilégier les patterns de taille **petite à moyenne** (CTA, verdict, FAQ, témoignage unique). Ils sont modulaires et plus simples à assembler et réutiliser.
- **Patterns à éviter** : Les grands patterns contenant une page entière (landing complète). Ils sont rigides et complexes à éditer.
