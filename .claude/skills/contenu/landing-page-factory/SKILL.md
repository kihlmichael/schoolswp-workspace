---
name: landing-page-factory
description: |
  Pipeline complet qui transforme une URL (plugin WP, theme WP, SaaS WordPress) en pages de destination
  HTML responsive multi-angles avec contenu de conversion et visuels de marque.
  7 etapes : scrape site → strategie → profil marque → copywriting → visuels → build HTML → QA gate.
  Utilise Firecrawl pour le scrape et OpenAI DALL-E pour les visuels.
  Declencheur : "landing page", "page de destination", "creer une page pour [produit]",
  "variations de landing", "page de vente HTML", "lander pour [plugin]", "page conversion".
  Utilise ce skill meme si l'utilisateur dit simplement "fais-moi une page pour X" ou
  "je veux promouvoir ce plugin" — des qu'il y a un produit WordPress/SaaS a mettre en avant.
allowed-tools:
  - Bash(firecrawl *)
  - Bash(npx firecrawl *)
  - Bash(python *)
  - Bash(node *)
  - Write
  - Read
  - Edit
  - Glob
  - Grep
  - WebFetch
  - WebSearch
metadata:
  version: 1.1.0
  brand: schoolsWP
---

# Landing Page Factory

Pipeline en 7 etapes qui transforme une URL produit en pages de destination pretes a deployer.
Chaque etape produit un livrable intermediaire qui alimente la suivante.

## Identite visuelle schoolsWP (obligatoire)

Toutes les pages generees DOIVENT utiliser l'identite visuelle schoolsWP. Ne jamais inventer de palette ou de typographie.

**Couleurs** :
- Primaire : `#00D400` (vert schoolsWP)
- Secondaire : `#00A100` (vert fonce)
- Accent : `#E668D4` (rose/magenta)
- Fond sombre : `#12111F`
- Fond moyen : `#212121`
- Texte subtil : `#57556D`
- Texte secondaire : `#8F8DA5`
- Fond section clair : `#EDF0F8`
- Fond clair : `#F4F6FB`
- Fond blanc : `#FAFBFD`
- Succes : `#13612E` / Info : `#1159AF` / Alerte : `#B82105` / Warning : `#F7630C`

**Typographie** :
- Titres : `Nunito Sans` — bold 700
- Body : `Roboto` — regular 400, 1.2rem
- Sizes : H1 2rem / H2 1.75rem / H3 1.5rem

**Style** : epure, aere, lisible, professionnel sans etre froid, structuré avec des espaces genereux. **Fond blanc** (fond principal `#FAFBFD`, sections alternees `#F4F6FB` et `#EDF0F8`, texte `#212121`).

**Logo** : inclure la version sombre du logo schoolsWP dans le header. URL par defaut : `https://schoolswp.com/wp-content/uploads/2022/06/cropped-cropped-logo-schoolsWP-nom-white-sans-contour.png` — si l'utilisateur fournit un logo adapte au fond clair, l'utiliser a la place. Le logo blanc sur fond blanc ne fonctionne PAS — toujours verifier le contraste.

**CTA buttons** : fond `#00D400`, texte `#12111F` (bold), border-radius 8px, hover → `#00A100`.

## Modele funnel affiliation

Ces pages sont des tunnels de vente affilies schoolsWP. Le modele :

1. **L'utilisateur decouvre** le produit via la page (copy de conversion)
2. **Il achete via le lien affilie** schoolsWP (CTA principal)
3. **En echange**, il recoit une formation gratuite schoolsWP pour bien demarrer avec le produit

**Structure CTA obligatoire** :
- CTA primaire : "Acheter [Produit] et recevoir la formation gratuite" (lien affilie)
- Si un **code promo** est fourni, l'afficher en evidence : banniere au-dessus du CTA avec "Code promo : [CODE] — [reduction]%" et le repeter dans le bouton CTA ("Acheter avec -XX% + formation gratuite")
- Sous le CTA : mention transparente "Lien affilié — je recommande uniquement les outils que j'utilise au quotidien sur schoolsWP."
- Section bonus avant le CTA final : presenter la formation offerte (contenu, duree, valeur)

**Section "Ton bonus schoolsWP"** (a inserer avant le CTA final) :
```
En achetant [Produit] via schoolsWP, tu recois :
- La formation "[Nom formation]" (valeur XX EUR) — GRATUITE
- [Nombre] modules pas a pas pour maitriser [Produit]
- Acces a la communaute schoolsWP
[Si code promo fourni] + Le code [CODE] pour -XX% sur ton achat
```

**Ton** : voix schoolsWP (tutoiement, direct, pedagogique, chaleureux). Lire `references/ban-list.md` ET respecter les expressions signature :
- "En clair :"
- "Teste et approuve."
- "Pas de blabla, juste du concret."
- "WordPress peut vraiment travailler pour toi."

## Scope

**Produits supportes** : plugins WordPress, themes WordPress, SaaS proches de l'ecosysteme schoolsWP (LMS, CRM, automatisation, SEO, ecommerce, formulaires, page builders).

**Ce skill n'est PAS pour** : des produits sans rapport avec WordPress/SaaS, des pages institutionnelles generiques, du contenu editorial (utiliser `branding` ou `ai-brain-production` pour ca).

## Entrees

L'utilisateur fournit au minimum :
- **URL du produit** : page officielle du plugin/theme/SaaS a promouvoir
- **Nombre d'angles** (optionnel, defaut : 3) : combien de variations de landing page generer

Entrees optionnelles :
- **Public cible** : freelance, createur, entrepreneur, agence (defaut : detection auto depuis le site)
- **Objectif conversion** : email capture, essai gratuit, achat, demo, affiliation (defaut : detection auto)
- **Brand assets partenaire** : logo du produit, screenshots, visuels officiels (fichiers fournis par l'utilisateur). Si fournis, les integrer dans les pages HTML.
- **Code promo** : code de reduction a afficher dans le CTA (ex: "SCHOOLSWP20" pour -20%). Si fourni, l'integrer dans le CTA et dans une banniere dediee.
- **Lien affilie** : URL exacte du lien affilie a utiliser dans les CTA (defaut : `#` en placeholder)
- **Langue** : francais (defaut) ou anglais

## Pipeline — 7 etapes sequentielles

### Etape 1 : Site Extract (ADN de marque)

**Objectif** : Extraire les donnees brutes du site produit pour tout fonder sur du reel, pas de l'hallucination.

**Actions** :
1. Scraper l'URL fournie avec Firecrawl :
   ```bash
   firecrawl scrape "<url>" -o .firecrawl/<slug>-main.md
   ```
2. Si le site a une page pricing, about, ou features — scraper aussi :
   ```bash
   firecrawl scrape "<url>/pricing" -o .firecrawl/<slug>-pricing.md
   firecrawl scrape "<url>/features" -o .firecrawl/<slug>-features.md
   ```
3. Extraire et structurer dans un fichier `01-site-extract.md` :

```markdown
# Site Extract — [Nom Produit]

## Identite visuelle
- Couleurs principales : [hex codes]
- Typographies : [fonts detectees]
- Style general : [minimal/corporate/playful/technique...]

## Signaux de confiance
- Nombre d'utilisateurs / installations actives
- Temoignages clients (verbatim)
- Logos partenaires / integrations
- Notes / avis (WordPress.org, G2, Trustpilot...)
- Certifications, badges, garanties

## Proposition de valeur
- Headline principale du site
- Sous-headline
- Benefices mis en avant (liste)

## Fonctionnalites cles
- [Feature 1] — [description courte]
- [Feature 2] — ...

## Pricing
- Plans et tarifs
- Modele (freemium, trial, one-time, subscription)

## Integrations / Ecosysteme
- Plugins/outils compatibles mentionnes
```

**Livrable** : `01-site-extract.md`

---

### Etape 2 : Page Strategy (cartographie des claims)

**Objectif** : Comprendre POURQUOI quelqu'un devrait acheter/essayer ce produit — pas lister les features.

**Actions** :
1. Lire `01-site-extract.md`
2. Pour chaque angle de landing page demande, definir :

```markdown
# Page Strategy — [Nom Produit]

## Analyse du probleme
- Quel probleme resout ce produit ?
- Pour qui exactement ? (persona concret, pas abstrait)
- Quelle est l'alternative actuelle ? (et pourquoi elle est insuffisante)

## Cartographie des claims
| Claim | Prouvable ? | Source de preuve |
|-------|-------------|-----------------|
| "Gain de 2h/semaine" | Oui | Temoignage client X |
| "Le plus rapide du marche" | Non | Aucune donnee comparative |
| ... | ... | ... |

Regle : ne JAMAIS utiliser un claim non prouvable dans le copy.

## Angles proposes
### Angle 1 : [Nom de l'angle]
- Hook : [phrase d'accroche]
- Cible : [persona specifique]
- Emotion dominante : [frustration/aspiration/curiosite/urgence]
- CTA principal : [action attendue]
- Mecanisme de preuve : [temoignage/stat/demo/comparatif]

### Angle 2 : [...]
### Angle N : [...]
```

Le choix du nombre d'angles depend du produit :
- Produit simple (1 feature cle) → 2-3 angles suffisent
- Produit riche (multi-features, multi-audiences) → 4-6 angles
- Si l'utilisateur a specifie un nombre, le respecter

**Livrable** : `02-page-strategy.md`

---

### Etape 3 : Brand Profile (voix de marque)

**Objectif** : Capturer la voix exacte du produit pour que le copy sonne authentique, pas generique.

**Actions** :
1. Relire `01-site-extract.md` — se concentrer sur le LANGAGE utilise
2. Produire :

```markdown
# Brand Profile — [Nom Produit]

## Personnalite de marque
- Ton : [technique/accessible/premium/decontracte/autorite...]
- Registre : [tutoiement/vouvoiement/neutre]
- Niveau technique : [debutant/intermediaire/expert]

## Patterns linguistiques detectes
- Phrases signatures : ["...", "...", "..."]
- Mots recurrents : [liste]
- Structure argumentaire : [probleme→solution / avant→apres / feature→benefice]

## Adaptation schoolsWP
Le copy final doit fusionner la voix du produit avec les regles schoolsWP :
- Tutoiement systematique
- Phrases courtes (8-15 mots en moyenne, max 20)
- Paragraphes aeres (2-4 phrases)
- Pas de jargon sans explication
- Actionnable : chaque section = quelque chose a faire

## Ban List
Lire `references/ban-list.md` — ces mots sont interdits dans tout le copy.
```

**Livrable** : `03-brand-profile.md`

---

### Etape 4 : Page Copy (redaction conversion)

**Objectif** : Rediger le contenu de chaque variation de landing page. Chaque ligne doit meriter sa place.

**Actions** :
1. Lire `02-page-strategy.md` + `03-brand-profile.md` + `references/ban-list.md`
2. Pour CHAQUE angle, rediger une landing page complete :

```markdown
# Landing Page Copy — [Nom Produit] — Angle [N] : [Nom]

## Hero Section
- Headline : [max 10 mots, percutant]
- Sous-headline : [1-2 phrases, clarifie la promesse]
- CTA primaire : [texte du bouton]
- Preuve immediate : [stat, temoignage court, badge]

## Section Probleme
[2-3 paragraphes qui decrivent la douleur du persona — avec des mots qu'il utiliserait lui-meme]

## Section Solution
[Comment le produit resout le probleme — benefices, pas features]

## Section Preuve
- Temoignages (verbatim du site, entre guillemets, avec source)
- Chiffres (uniquement prouvables)
- Logos / integrations

## Section Features (optionnel)
[3-5 features principales avec icone suggeree + benefice en 1 phrase]

## Section Pricing / CTA final
- Recap de la valeur
- Objection principale → reponse
- CTA final + garantie si disponible

## FAQ (3-5 questions)
[Questions reelles que le persona se pose]
```

**Regle des 20%** : apres la premiere redaction, relire et SUPPRIMER 20% du texte. Si une phrase ne fait pas avancer la decision d'achat, elle degage.

**Livrable** : `04-copy-angle-1.md`, `04-copy-angle-2.md`, etc.

---

### Etape 5 : Page Visuals (generation d'images)

**Objectif** : Generer des visuels alignes sur la marque pour chaque landing page.

**Actions** :
1. Lire `01-site-extract.md` (palette, style) + `03-brand-profile.md`
2. Pour chaque angle, definir les visuels necessaires :
   - Hero image (illustration ou mockup produit)
   - 1-2 images de section (preuve sociale, feature highlight)
   - Favicon / icone si pertinent
3. Generer via OpenAI :

```bash
python "{baseDir}/../openai-imagegen/scripts/gen.py" \
  --prompt "[prompt detaille avec style, couleurs, composition]" \
  --model gpt-image-1 \
  --size 1536x1024 \
  --quality high \
  --count 1 \
  --out-dir landing-pages/<slug>/images/angle-<N>/
```

**Directives pour les prompts image** :
- Toujours inclure les couleurs hex de la marque dans le prompt
- Style coherent entre toutes les images d'un meme angle
- Pas de photos stock generiques (pas de "businessman shaking hands")
- Pas de degradres violets IA
- Privilegier : illustrations flat/isometriques, mockups produit, schemas, screenshots stylises

**Livrable** : images dans `landing-pages/<slug>/images/angle-<N>/`

---

### Etape 6 : Page Build (HTML responsive)

**Objectif** : Assembler copy + visuels en fichier(s) HTML single-file, prets a deployer.

**Actions** :
1. Lire le copy (etape 4), les visuels (etape 5), le brand profile (etape 3)
2. Pour chaque angle, generer un fichier HTML autonome :

**Structure HTML obligatoire** :
- Single file (CSS inline ou `<style>` dans le `<head>`)
- Images en base64 embedees OU references locales
- Responsive (mobile-first, breakpoints 768px / 1024px)
- Font loading via Google Fonts ou font-stack systeme
- Meta tags SEO (title, description, og:image)
- Schema markup Product ou SoftwareApplication

**Adapter le layout selon le type de produit** — lire `references/page-types.md` :
- Plugin WP → layout feature-grid + demo CTA
- Theme WP → layout visual-first + live preview CTA
- SaaS → layout problem-solution + trial CTA
- Formation/cours → layout curriculum + inscription CTA

**Principes design** (herites de `frontend-design`) :
- Typographie distinctive (pas Inter, pas Roboto, pas Arial)
- Palette derivee des couleurs de marque (etape 1)
- Animations CSS subtiles (fade-in au scroll, hover states)
- Composition spatiale intentionnelle (pas de layout generique)
- Contraste fort pour les CTAs

**Livrable** : `landing-pages/<slug>/angle-<N>.html`

---

### Etape 7 : QA Gate (validation)

**Objectif** : Rien ne sort sans validation. Chaque page est evaluee sur 5 axes.

**Actions** :
1. Pour chaque page HTML generee, evaluer selon `references/qa-scorecard.md` :

```markdown
# QA Report — [Nom Produit] — Angle [N]

## Scores (/20 chaque, total /100)

| Axe | Score | Commentaire |
|-----|-------|-------------|
| Preuve | /20 | Claims prouvables ? Sources citees ? |
| Confiance | /20 | Temoignages reels ? Garanties ? Signaux de confiance ? |
| Contenu | /20 | Clair ? Actionnable ? Phrases courtes ? Ban list respectee ? |
| Visuels | /20 | Coherents avec la marque ? Pas generiques ? Responsive ? |
| Anti-charabia | /20 | Aucun mot de la ban list ? Pas de fluff IA ? Chaque phrase utile ? |

## Verdict
- >= 80 : LIVRABLE — pret a deployer
- 60-79 : BROUILLON — corrections mineures listees ci-dessous
- < 60 : BLOQUE — rewrite necessaire, problemes critiques

## Corrections requises
1. [...]
2. [...]
```

2. Si verdict = BROUILLON → appliquer les corrections et re-evaluer
3. Si verdict = BLOQUE → remonter a l'etape problematique et refaire

**Livrable** : `landing-pages/<slug>/qa-angle-<N>.md` + pages corrigees si necessaire

---

## Sortie finale

A la fin du pipeline, le dossier `landing-pages/<slug>/` contient :

```
landing-pages/<slug>/
├── 01-site-extract.md          # ADN marque
├── 02-page-strategy.md         # Strategie + angles
├── 03-brand-profile.md         # Voix de marque
├── 04-copy-angle-1.md          # Copy angle 1
├── 04-copy-angle-2.md          # Copy angle 2
├── 04-copy-angle-N.md          # ...
├── images/
│   ├── angle-1/                # Visuels angle 1
│   └── angle-2/                # Visuels angle 2
├── angle-1.html                # Page HTML finale
├── angle-2.html                # Page HTML finale
├── qa-angle-1.md               # Rapport QA
└── qa-angle-2.md               # Rapport QA
```

Presenter a l'utilisateur :
1. Le resume strategique (angles choisis + pourquoi)
2. Les scores QA de chaque page
3. Les chemins vers les fichiers HTML pour preview
4. Les corrections appliquees si verdict etait BROUILLON

## Reference Files

- `references/ban-list.md` — Mots et expressions interdits dans tout le copy
- `references/page-types.md` — Layouts adaptes par type de produit
- `references/qa-scorecard.md` — Grille d'evaluation detaillee des 5 axes QA
