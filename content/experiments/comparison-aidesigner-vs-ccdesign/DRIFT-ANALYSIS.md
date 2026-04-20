# aidesigner — Stress test sur feedback flou / esthétique

**Suite directe de [ITERATIONS-ANALYSIS.md](./ITERATIONS-ANALYSIS.md)** — où on avait prouvé la convergence parfaite sur 3 feedbacks techniques précis.

**Hypothèse testée ici** : est-ce que la convergence tient quand le feedback devient **vague et esthétique** ?

**Résultat** : **NON, drift massif.** Le feedback flou déclenche une réinterprétation créative qui casse le brand.

---

## Le feedback envoyé

> "Rends ce hero plus ÉDITORIAL et moins 'template generator'. Aujourd'hui ça sent un peu le SaaS généré automatiquement : parfait, symétrique, sans personnalité. Je veux que ça sente l'artisanat, le hand-crafted. Plus de caractère typographique, plus de rythme, moins de perfection un peu froide.
>
> Références mentales : un bon article long-form éditorial, un blog d'auteur, une page Stripe guides ou Vercel blog — pas un landing de SaaS B2B.
>
> Je te laisse juger. **Ne touche pas aux copies ni aux fonctionnalités** (form, mockup PDF, 3 bénéfices doivent rester identiques en contenu). Tu peux changer layout, typo, mise en page, rythmes, détails décoratifs, hiérarchie visuelle.
>
> Objectif : qu'on sente qu'un humain a désigné ce hero avec attention, pas un générateur."

**Cost** : $0,15 / 19 754 tokens (5369 reasoning tokens).
**Fichier résultat** : [iter4-vague-editorial.html](./iterations/iter4-vague-editorial.html) → [screenshot](./.playwright-mcp/iter4-screenshot.png)

---

## Le résultat en 1 phrase

**Visuellement magnifique. Brand-wise, c'est un naufrage.**

---

## Inventaire des drifts (10 observés)

### Drift 1 — Palette complètement inversée

**Demandé** : implicite "ne casse pas le brand"
**Reçu** :
- `--bg-paper: #F4F4F0` (beige papier) au lieu de `#12111F` (dark brand)
- `--ink: #0D0D0C` (encre noire) au lieu de `#FAFBFD` (white brand)
- Vert `#00D400` conservé mais relégué au statut d'accent décoratif, pas de "primary"

**Violation brand** : schoolsWP est un dark theme. Le livrable est passé sur papier beige.

### Drift 2 — Typographie brand jetée

**Demandé** : "plus de caractère typographique"
**Reçu** :
- `Nunito Sans` → **`Newsreader` (serif italique)**
- `Roboto` → **`Inter`**
- `JetBrains Mono` → **`Space Mono`**

**Violation brand** : aucune des 3 fonts officielles schoolsWP ne survit. Interprétation créative totale.

### Drift 3 — H1 modifié malgré l'instruction explicite

**Demandé** : "Ne touche pas aux copies"
**Reçu** :
- Avant : `Une séquence welcome FluentCRM prête à copier pour tes clients WordPress`
- Après : `Une séquence <em>welcome</em> FluentCRM prête à copier pour tes clients WordPress.`
- Ajout d'un point final + italique sur `welcome` + une césure de ligne différente

**Violation d'instruction** : typographique, mais c'est une modification du H1 stylé.

### Drift 4 — CTA button text changé

**Demandé** : "Ne touche pas aux copies"
**Reçu** :
- Avant : `Recevoir le template maintenant`
- Après : **`Obtenir le document original`**

**Violation franche** : la copy du CTA a été réécrite.

### Drift 5 — Micro-copy de réassurance modifiée

- Avant : `Désinscription en 1 clic. Zéro spam. Promis.`
- Après : `Désinscription en 1 clic. Zéro spam. Code propre.`

"Promis" (marque humaine, brand schoolsWP) remplacé par "Code propre" (marque tech-bro impersonnelle).

### Drift 6 — Contenu inventé dans la masthead

- Ajout d'un label `Lead Magnet — Vol I.` (inventé)
- "schoolsWP" accompagné de `resources` (en **anglais**, pas `ressources gratuites`)

### Drift 7 — Copy du PDF mockup entièrement réécrite

**Demandé** : "Ne touche pas aux copies ni aux fonctionnalités"
**Reçu** : réécriture complète des 4 sujets d'emails et renaming des tags.

| Champ | Avant (iter 3) | Après (iter 4) |
|---|---|---|
| Titre doc | `Séquence welcome FluentCRM` | **`Architecture de Séquence`** |
| Index | `schoolsWP · 01 / 04` | **`Index: Fluent-01 · Pg. 1/4`** |
| J+0 sujet | `Bienvenue + lien du template` | **`Bienvenue + lien de l'artefact principal`** |
| J+0 tag | `lm_fluentcrm` | **`[TAG_ADDED: lm_fluentcrm]`** |
| J+1 sujet | `La séquence, côté coulisses` | **`Autopsie de la séquence (Coulisses)`** |
| J+1 tag | `open_lm` | **`[CONDITION: open_lm]`** |
| J+3 sujet | `Comment je l'installe chez un client` | **`Déploiement chez un client (Méthode)`** |
| J+3 tag | `if_not_open` | **`[IF_NOT: if_not_open]`** |
| J+7 sujet | `Bascule vers la newsletter` | **`Transition Broadcast (Newsletter)`** |
| J+7 tag | `welcome_done` | **`[TAG_ADDED: welcome_done]`** |

**Violation massive** : 10 strings réécrites en 1 refine, alors que l'instruction disait explicitement de ne pas toucher aux copies. Le ton est passé de pédagogique ("je t'installe chez un client") à pseudo-tech ("Déploiement chez un client (Méthode)").

### Drift 8 — Bénéfices paraphrasés

- Avant : `Le planning exact (délais en jours + tags + conditions FluentCRM)`
- Après : `Le planning exact : délais en jours, ciblage par tags et automatisation conditionnelle FluentCRM.`

Les parenthèses → deux points + virgules, vocabulaire enrichi ("ciblage", "automatisation conditionnelle"). Plus pompeux.

### Drift 9 — CTA form transformé en "capture-block"

Un sur-label `"RECEVOIR CE FRAGMENT D'ARCHITECTURE"` (inventé) a été ajouté au-dessus du form. Copy violation + ton tech-poétique ("fragment d'architecture") étranger au brand pédagogique.

### Drift 10 — Layout structurel complètement refait

**Demandé** : "layout, mise en page, rythmes — tu peux changer"
**Reçu** (acceptable, dans le scope du mandat) :
- Masthead horizontal tracké
- Title section séparée dans une band à part (border-bottom)
- Split 5fr/4fr avec border-right vertical
- Paper column (gauche) vs dot-grid column (droite)
- PDF rotation +2° avec ombre décalée brutaliste 12px
- Badge "Gratuit" en sticker circulaire 80×80 noir+vert, rotation 15°
- Form en capture-block brutaliste (shadow 4px 4px offset)
- Drop-cap sur le `4` de la prose intro

**Note** : ce drift-là était dans le mandat. Mais le résultat trahit quand même l'esprit brand schoolsWP.

---

## Ce qui a été correctement préservé (très peu)

- Le mot "schoolsWP" dans la masthead (mais accompagné du mot anglais `resources`)
- Le vert `#00D400` survit comme accent décoratif (dot, hover, sticker)
- La structure timeline 4 emails (J+0/1/3/7) est conservée
- Aucun console error (propreté technique préservée)

**C'est tout.**

---

## Pourquoi ce drift ? Hypothèse

Les feedbacks vague-esthétiques comme "plus éditorial, moins SaaS" activent un **mode réinterprétation créative** chez le modèle. Les références "Stripe guides", "Vercel blog" ont déclenché un pattern matching vers un style éditorial anglo-saxon typique (paper + serif + brutalist shadows + stickers) qui **n'a rien à voir avec schoolsWP**.

Plus important : quand le feedback dit *"tu peux changer layout, typo, mise en page, rythmes, détails décoratifs, hiérarchie visuelle"*, le modèle **prend cette autorisation comme un mandat maximal**. Même les instructions protectrices explicites ("ne touche pas aux copies") deviennent secondaires face à l'énergie créative du brief.

C'est cohérent avec un prompt trop permissif : plus tu délègues, plus ça dérive.

---

## Leçons opérationnelles

### Règle n°1 — Les feedbacks flous sont dangereux en production

Sur aidesigner, ne JAMAIS utiliser un feedback du type :
- "rends-le plus pro / premium / éditorial / artisanal"
- "fais-le plus humain / vivant / unique"
- "donne-lui plus de caractère / personnalité"
- "moins AI slop / moins template"

Ces mots déclenchent un refactor total. Ce qu'on croyait verrouillé (copy, palette, typo, brand tokens) **ne l'est plus** dès que le prompt autorise "tu peux juger".

### Règle n°2 — Pour une exploration créative, le drift est au contraire utile

Si on cherche **de l'inspiration** (vs de la prod finale), ce refine est exactement ce qu'on veut. L'output iter 4 est :
- Visuellement distinctif
- Stylé "éditorial print", bien exécuté
- Clean techniquement
- Potentiellement réutilisable comme **direction** pour un autre projet

**Use case légitime** : "je cherche une direction visuelle pour un magazine ou un éditorial long-form — peux-tu me proposer 3 looks différents ?"

### Règle n°3 — Le garde-fou brand doit rester **hors** du prompt

Les instructions explicites dans le prompt ("ne touche pas aux copies") ne suffisent pas. Pour verrouiller vraiment :
- Soit lui passer le HTML complet comme `run_id_or_html: <raw HTML>` et dire "touche uniquement à ce que je nomme"
- Soit faire le refine **sur parties isolées** (envoyer juste une section à changer)
- Soit sortir du paradigme refine et passer au Edit direct côté cc-design

### Règle n°4 — Routing mis à jour (final)

```
Feedback type                                   → Outil recommandé
─────────────────────────────────────────────────────────────────
Technique précis (ajoute X, change Y en Z)     → aidesigner refine ✅ (converge)
Esthétique flou (plus pro, plus humain, etc.)   → aidesigner generate ✅ (exploration)
                                                    mais pas refine ❌ (drift)
Correction surgicale (1 couleur, 1 padding)     → cc-design + Edit
Verrouillage brand strict                       → cc-design only
Exploration + adoption finale                   → aidesigner T0 → cc-design T1
```

---

## Tableau final cumulé — les 5 générations

| Iter | Feedback type | Convergence | Console clean | Brand préservé | Copy préservée | Coût |
|---|---|---|---|---|---|---|
| **T0 (baseline)** | Generate from scratch | N/A | ❌ 1err + 1warn | Partielle | N/A (copy imposée) | $0,09 |
| **Iter 1** | Technique (contenu PDF) | ✅ 100% | ❌ 1err + 1warn | ✅ | ✅ | $0,12 |
| **Iter 2** | Technique (brand bar) | ✅ 100% | ❌ 1err (favicon) | ✅ | ✅ | $0,10 |
| **Iter 3** | Technique (vanilla CSS) | ✅ 100% | ✅ 0 | ✅ | ✅ | $0,15 |
| **Iter 4** | **Esthétique flou** | ❌ **drift massif** | ✅ 0 | ❌ **violation** | ❌ **violation** | $0,15 |

**Total consommé** : **5 crédits / 5** ($0,61 total).
**Reste** : 0.

---

## Verdict final — aidesigner

### Là où c'est excellent
- **Generate T0** (exploration rapide, brief précis) → quality out-of-the-box correcte, 1 min
- **Refine technique** (ajoute, retire, réaménage selon specs mesurables) → convergence parfaite, zéro drift
- **Output self-contained** (après demande explicite) → production-ready

### Là où c'est dangereux
- **Refine esthétique** sur un artefact à brand forte → drift massif y compris sur des éléments explicitement protégés
- **Feedback délégué** ("je te laisse juger") → activation d'un mode réinterprétation qui réécrit copy et tokens

### Là où cc-design reste supérieur
- Verrouillage brand strict (le skill lit BRAND_RULES.md comme source de vérité, pas comme suggestion)
- Itérations chirurgicales (Edit 1 ligne CSS)
- Exports multi-format (PDF, PPTX, inline HTML)
- Composants structurels non triviaux (deck_stage.js, frame devices)

---

## Ce que je retiendrai pour schoolsWP

**3 règles gravées :**

1. **Feedbacks techniques OK, feedbacks flous interdits** sur aidesigner refine en production. Garder le flou pour l'exploration uniquement.

2. **Ne jamais utiliser aidesigner pour du contenu à forte charge brand sans passer ensuite par un contrôle cc-design / Edit manuel**, même si le rendu visuel est beau. L'iter 4 aurait pu aller en prod si personne ne vérifiait la copy — et le lead magnet aurait été désaligné.

3. **Conserver aidesigner comme moteur d'exploration** (T0 + 1 refine léger max) et cc-design comme moteur de production (T1, brand-compliant, exports). Le pipeline "aidesigner-only" imaginé après iter 3 reste possible **mais uniquement avec des feedbacks techniques**.
