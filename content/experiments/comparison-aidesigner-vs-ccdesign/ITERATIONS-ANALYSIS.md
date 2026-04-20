# aidesigner — Test de convergence sur 3 itérations

**Hypothèse testée** : quand on refine une sortie aidesigner avec des feedbacks ciblés, est-ce que l'output **converge** vers la cible (brand-compliant, production-ready) ou est-ce qu'il **diverge** (drift sur copy, perte de cohérence) ?

**Protocole** :
- Baseline = `aidesigner-hero.html` (première génération)
- 3 refines successifs, chacun sur un axe où la baseline était faible
- Compare chaque iter à la cible `ccdesign-hero.html`

**Résultat** : **convergence totale**. Aucun drift observé. Après 3 refines, l'output aidesigner est fonctionnellement équivalent au cc-design.

---

## Les 3 itérations

### Iter 1 — Remplir le PDF mockup

**Feedback** : remplacer les blocs wireframe gris par du contenu réel (4 emails datés J+0/+1/+3/+7, sujets exacts, tags FluentCRM).

**Résultat** : [iter1-pdf-content.html](./iterations/iter1-pdf-content.html) → [screenshot](./.playwright-mcp/iter1-screenshot.png)

**Coût** : $0.12 / 14 320 tokens (4580 reasoning tokens).
**Précision** : 100%. Les 4 sujets sont présents, verbatim. Les 4 tags sont au bon endroit, avec le bon style (mono, vert foncé sur vert très clair). La timeline verticale a été ajoutée (stem gris). Header `schoolsWP` + `01 / 04` correct. Footer `schoolsWP.com / v1.0` correct.
**Changement non demandé** : rotation inversée -7° (mais demandée dans le feedback), et un léger `@keyframes document-float` (ajouté proactivement pour le mouvement — acceptable, pas invasif).

### Iter 2 — Brand bar + spacing

**Feedback** : ajouter une brand bar en haut (logo schoolsWP à gauche, `LEAD MAGNET · 01 / 01` à droite), padding horizontal 48px, gap colonnes 96px.

**Résultat** : [iter2-brand-bar-spacing.html](./iterations/iter2-brand-bar-spacing.html) → [screenshot](./.playwright-mcp/iter2-screenshot.png)

**Coût** : $0.10 / 13 215 tokens (2380 reasoning tokens).
**Précision** : 100%. Brand bar conforme : dot vert 12px + glow, "schoolsWP" bold + " · ressources gratuites" regular gris, label `LEAD MAGNET · 01 / 01` en JetBrains Mono uppercase tracked. Border-bottom 1px white/6% comme demandé. Spacing : `px-[48px]`, `gap-x-[96px]`, `pt-[72px] pb-[96px]` — valeurs exactes du brief.
**Zero drift** sur le contenu précédent (PDF mockup, form, bénéfices intacts).

### Iter 3 — Retirer Tailwind CDN, vanilla CSS

**Feedback** : refactor complet, retirer `<script src="cdn.tailwindcss.com">`, utiliser custom properties + classes sémantiques + media queries natives. Ajouter favicon SVG inline pour éliminer le 404.

**Résultat** : [iter3-vanilla-css.html](./iterations/iter3-vanilla-css.html) → [screenshot](./.playwright-mcp/iter3-screenshot.png)

**Coût** : $0.15 / 18 147 tokens (4665 reasoning tokens).
**Précision** : 100%. Tailwind entièrement retiré. `:root { --bg-dark, --brand-green, --tag-green-bg... }` propre. Classes sémantiques (`.brand-bar`, `.mockup-paper`, `.timeline-item`). Media queries `@media (min-width: 640px/768px/1024px)`. Favicon SVG data-URI ajouté.
**Verification playwright** : **0 errors, 0 warnings en console**. Self-contained OK.
**Rendu visuel** : pixel-perfect identique à iter 2.

---

## Métriques cumulées

| | Baseline | Iter 1 | Iter 2 | Iter 3 | Cumul |
|---|---|---|---|---|---|
| Coût ($) | 0,09 | 0,12 | 0,10 | 0,15 | **0,47** |
| Tokens | 8 934 | 14 320 | 13 215 | 18 147 | 54 616 |
| Reasoning tokens | 3 969 | 4 580 | 2 380 | 4 665 | 15 594 |
| Crédits aidesigner | 1 | 1 | 1 | 1 | **4 / 5** |
| Lignes HTML | 215 | 200 | 173 | 275 | — |
| Console errors | 1 | 1 | 0 | **0** | — |
| Console warnings | 1 (Tailwind CDN) | 1 | 1 | **0** | — |
| Self-contained | ❌ | ❌ | ❌ | ✅ | — |

**Note** : la baseline fait 215 lignes avec Tailwind CDN. Iter 3 en fait 275 lignes en vanilla CSS — overhead naturel du refactor. À comparer aux 297 lignes du cc-design de référence.

---

## Analyse de convergence

### Ce que ça prouve

1. **aidesigner refine CONVERGE** sur 3 itérations successives. Aucun drift observé sur les éléments non mentionnés dans les feedbacks. Le H1 est resté identique verbatim à travers 4 générations. Même chose pour le sous-titre, les placeholders des inputs, les 3 bénéfices, le micro-copy de réassurance.

2. **Précision des feedbacks** : chaque instruction a été appliquée à la lettre. Y compris des détails précis (`var(--bg-dark)`, `rgba(0,212,0,0.5)`, `@media (min-width: 1024px)`). La spec technique était honorée sans réinterprétation créative.

3. **Reasoning tokens** dominants sur iter 1 et iter 3 (les plus complexes). Iter 2 (ajout brand bar) = reasoning léger (2380 tokens) car modification simple.

### Ce que ça ne prouve pas

- Les 3 feedbacks étaient **ciblés et clairs** (exigences techniques précises). On n'a pas testé des feedbacks flous du type "rends-le plus pro" — la convergence peut être très différente dans ce cas.
- Une seule session de 3 iters. Pas de test sur 5-10 iters où le drift pourrait apparaître.
- Le contenu sémantique (H1, copy) était verrouillé dès la baseline. On n'a pas testé un refine qui modifie en profondeur le message — là aussi, la convergence serait à ré-évaluer.

---

## Convergence vers cc-design — comparaison directe

À l'issue d'iter 3, l'output aidesigner est **fonctionnellement équivalent** au cc-design :

| Critère | cc-design | aidesigner iter 3 |
|---|---|---|
| Brand bar schoolsWP | ✅ | ✅ |
| PDF mockup avec 4 emails datés | ✅ | ✅ |
| Tags FluentCRM visibles | ✅ | ✅ |
| 0 erreur console | ✅ | ✅ |
| Self-contained (zéro CDN JS) | ✅ | ✅ |
| Favicon SVG inline | ✅ | ✅ |
| Media queries vanilla | ✅ | ✅ |
| Custom properties CSS | ✅ | ✅ |
| Lignes HTML | 297 | 275 |
| Taille KB | 13 | 18 |

**Différences subtiles restantes** :
- cc-design a une **radial gradient subtile** en background fixed (tension visuelle) — iter 3 n'en a pas
- cc-design a une `.sheet-shadow` verte additionnelle derrière le PDF (effet stack) — iter 3 n'a que la shadow offset noire classique
- cc-design utilise `aspect-ratio: 1/1.414` sur le PDF stage, iter 3 aussi — même méthode, rendu identique
- cc-design a des tags `rounded` plus marqués (4px), iter 3 plus discrets (2-4px)

**Temps de production** :
- cc-design : ~15 min de workflow (routing + lecture refs + build + verify)
- aidesigner iter 3 : ~3 min × 4 calls = 12 min d'horloge, mais **~45s de travail humain** (juste rédiger les feedbacks)

---

## Conclusion opérationnelle

**La prod-finale via refinement aidesigner est viable**, mais coûte ~0,50 $ en crédits vs 0 $ pour un build cc-design direct. Tradeoff :

- **aidesigner pipeline** : T0 + 3 refines = **0,47 $ + ~15 min d'horloge (dont 3 min d'attention humaine)**. Idéal quand tu veux explorer des directions visuelles avant de t'engager.
- **cc-design direct** : **0 $ de crédit externe + ~15 min de workflow actif**. Idéal quand tu sais exactement où tu vas.

**Recommandation mise à jour vs le doc COMPARISON précédent** :

Le pipeline *"aidesigner T0 → cc-design T1"* proposé dans COMPARISON.md peut être **simplifié** en *"aidesigner T0 → aidesigner refine T1-Tn"* si :
1. Les feedbacks sont précis (techniques, pas esthétiques)
2. Le budget crédits n'est pas un blocage
3. Tu n'as pas besoin des exports multi-format (PDF/PPTX) que seul cc-design propose via ses scripts

À l'inverse, **cc-design reste meilleur** dès qu'on a besoin de :
- Slide deck (structure `deck_stage.js`)
- Export PDF natif (`scripts/open_for_print.js`)
- Export PPTX (`scripts/gen_pptx.js`)
- Inline HTML autonome (`scripts/super_inline_html.js`)
- Refonte sur un fichier du repo déjà existant (Edit ciblé ligne par ligne)

---

## Crédits aidesigner restants après ce test

**4 / 5 consommés** (1 baseline + 3 refines). Reste **1 crédit** pour un test futur.

*Log tokens brut :*
- Baseline : 8 934 tokens / 3 969 reasoning
- Iter 1 : 14 320 tokens / 4 580 reasoning
- Iter 2 : 13 215 tokens / 2 380 reasoning
- Iter 3 : 18 147 tokens / 4 665 reasoning
- **Total : 54 616 tokens, 15 594 reasoning tokens, 0,47 $**
