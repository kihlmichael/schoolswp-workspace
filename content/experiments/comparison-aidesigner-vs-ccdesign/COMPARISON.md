# Head-to-head : aidesigner vs cc-design

**Test** : hero section pour landing lead magnet "Séquence welcome FluentCRM prête à copier".
**Date** : 2026-04-20
**Brief** : identique pour les deux (H1, sous-titre, form, PDF mockup rotation 8°, badge Gratuit, 3 bénéfices, dark theme #12111F + green #00D400, typo Nunito Sans + Roboto, tutoiement, self-contained).
**Viewport** : desktop 1440×900.

Artefacts :
- [aidesigner-hero.html](./aidesigner-hero.html) → [screenshot](./.playwright-mcp/aidesigner-hero-desktop.png)
- [ccdesign-hero.html](./ccdesign-hero.html) → [screenshot](./.playwright-mcp/ccdesign-hero-desktop.png)

---

## Résumé exécutif

| | aidesigner | cc-design |
|---|---|---|
| Temps de production | ~60s (1 appel MCP) | ~15 min (workflow 6 étapes) |
| Coût direct | 1 crédit ≈ 0,09 $ | 0 $ (tokens conversation) |
| Lignes HTML | 215 | 297 |
| Taille fichier | 11 KB | 13 KB |
| Console errors | 1 error + 1 warning | 0 |
| Dépendances externes | Tailwind CDN + Google Fonts | Google Fonts uniquement |
| Self-contained vrai | ❌ (Tailwind CDN) | ✅ |
| Brand compliance | Partielle | Totale |
| Maillage avec le repo | Aucun | Direct (BRAND_KIT.json, specs lead magnet) |

**Verdict court** : `aidesigner` livre un résultat propre en 1 minute mais reste **générique et dépendant du CDN**. `cc-design` demande **15× plus de temps** mais produit un artefact **aligné brand, self-contained, sans erreur console, avec du contenu métier réel dans le mockup**.

---

## Analyse sur 7 axes

### 1. Scope & entrée

| Axe | aidesigner | cc-design |
|---|---|---|
| Types de sorties | HTML seulement (output unique par run) | HTML + PDF + PPTX + HTML inline (4 scripts) |
| Clarifying questions | Aucune (one-shot) | Question protocol intégré via `AskUserQuestion` |
| Auto-détection brand | Aucune (reformule le prompt avec son propre jugement) | Charge `BRAND_RULES.md` explicitement via étape 3 (Acquire Context) |
| Mode "clone/enhance/inspire" depuis URL | Oui (mode + url) | Oui via `getdesign-loader.md` |
| Entrée typique | Prompt long + repo_context compact | Brief conversationnel + routing vers 2-3 références |

**Winner scope** : cc-design (HTML + export PDF/PPTX, clarification pre-build).
**Winner friction** : aidesigner (un seul tool call, pas de workflow).

### 2. Boucle & coût

| Axe | aidesigner | cc-design |
|---|---|---|
| Call duration | ~45-60s par génération | Variable, ~10-20 min de workflow |
| Tokens consommés | ~9k tokens (3969 reasoning + 7512 completion + 1422 prompt) | ~30-50k tokens (routing + référence + build + verify) dans la conversation |
| $ direct | 0,09 $ (1 crédit sur le compte aidesigner) | 0 $ côté service, mais charge la conversation Claude Code |
| Itération | `refine_design` (run_id + feedback) → 1 crédit | Edit direct sur le fichier HTML |
| Granularité fine | Medium (feedback textuel) | Haute (Edit ciblé ligne par ligne) |
| Reproductibilité | Faible (stochastique remote) | Haute (même skill, mêmes références, même brief) |

**Winner coût direct** : cc-design (pas de facture externe) — à condition d'avoir déjà une subscription Claude Code active.
**Winner time-to-first-draft** : aidesigner (1 min vs 15 min).
**Winner iteration** : cc-design (Edit permet du pixel-perfect, refine_design reste global).

### 3. Qualité visuelle

**aidesigner :**
- ✅ Hero correct, hiérarchie typo claire (H1 3.5rem, sub 1.25rem)
- ✅ Form clean, CTA green bien visible
- ⚠️ PDF mockup **abstrait** : grid pattern + blocs gris génériques. Pas de contenu réel, pas de sujets d'emails, pas de badges tags. Un wireframe, pas un preview.
- ⚠️ Badge "Gratuit" petit, placé en absolute en haut-droite, rotation légère
- ⚠️ Reassurance icône cadenas correct mais standard
- ⚠️ Pas d'eyebrow, pas de brand bar, pas de structure de page (démarre direct au H1)

**cc-design :**
- ✅ Hero avec brand bar en haut (schoolsWP · ressources gratuites + Lead magnet 01/01)
- ✅ Eyebrow vert "TEMPLATE FLUENTCRM · PDF" qui positionne le contenu
- ✅ H1 avec accent green sur "prête à copier" (pattern brand)
- ✅ **PDF mockup avec contenu réel** : 4 emails datés (J+0, J+1, J+3, J+7), sujets, tags (`lm_fluentcrm`, `open_lm`, `if_not_open`, `welcome_done`), header "schoolsWP" + "01/04", footer versionné
- ✅ Badge "Gratuit" avec glow vert + rotation + shadow élaborée
- ✅ Background fixe avec 2 radial gradients verts subtils (tension visuelle)
- ✅ Hover states sur button (translateY + shadow)

**Verdict** : le livrable cc-design raconte une histoire (ce qui est dans le PDF). Celui d'aidesigner promet un contenu sans le montrer.

### 4. Brand compliance schoolsWP

| Critère | aidesigner | cc-design |
|---|---|---|
| Tutoiement FR | ✅ | ✅ |
| Phrases 8-15 mots | ✅ | ✅ |
| Mots interdits | ✅ aucun | ✅ aucun |
| Couleurs brand (#00D400, #12111F, #FAFBFD) | ✅ | ✅ |
| Typo brand (Nunito Sans + Roboto) | ✅ | ✅ |
| Nom "schoolsWP" exact | ❌ absent du rendu | ✅ présent brand bar + mockup |
| Style "espaces généreux" | ⚠️ serré à 1440px | ✅ padding 56-96px |
| Anti-slop : pas de gradient agressif | ✅ | ✅ (gradients très subtils, cohérent) |
| Anti-slop : pas d'emoji | ✅ | ✅ |
| Anti-slop : pas de carte rounded + left-border | ✅ | ✅ |
| "Placeholder > bad asset" (mockup) | ⚠️ placeholder abstrait | ✅ placeholder enrichi avec data réaliste |

**Winner brand** : cc-design, nettement. Il n'y a pas de "schoolsWP" mentionné par aidesigner alors que c'est l'auteur du lead magnet.

### 5. Output technique

| Point | aidesigner | cc-design |
|---|---|---|
| Console errors | ❌ 1 error (favicon 404) + 1 warning (Tailwind CDN prod) | ✅ 0 error, 0 warning |
| Self-contained | ❌ depends on cdn.tailwindcss.com | ✅ tout CSS inline |
| Robustesse offline | ❌ | ✅ (sauf fonts Google — à packager si besoin) |
| CSS approach | Tailwind utility-first + tailwind.config inline | CSS vanilla avec custom properties (tokens) |
| A11y de base | ✅ label sr-only, `required`, focus rings Tailwind | ✅ `required`, aria-label mockup, focus rings custom |
| Responsive | ✅ breakpoint `lg:` Tailwind | ✅ `@media (max-width: 980px)` natif |
| Adoption dans un theme WP | ⚠️ doit extraire les classes Tailwind ou compiler | ✅ copier-coller direct (pas de build step) |

**Winner tech** : cc-design — respecte le contrat "no console errors" du skill, portable direct dans WordPress sans build step.

### 6. Dépendances & infra

| | aidesigner | cc-design |
|---|---|---|
| MCP actif requis | ✅ `mcp__aidesigner__*` | ❌ skill local |
| Browser requis | Non (generation remote) | Oui pour verify (Playwright MCP) |
| Compte externe | Oui (OAuth) | Non |
| Quota / crédits | 5 gratuits + payant au-delà | Limité par le pricing Claude Code |
| Fallback hors-ligne | Non | Partiel (build oui, verify non) |

### 7. Use case fit (schoolsWP)

**aidesigner brille pour :**
- Exploration rapide d'options visuelles en amont d'un brief détaillé ("voir à quoi ça pourrait ressembler")
- Prototypes quick-and-dirty pour rendez-vous client
- Situations où tu n'as pas le contexte brand encore cristallisé
- Quand tu veux 3 variantes en 3 crédits

**cc-design brille pour :**
- Production d'assets schoolsWP finaux (landing, slide deck, mockup WordPress)
- Tout artefact qui doit respecter BRAND_RULES à la lettre
- Tout ce qui demande export PDF/PPTX propre
- Tout ce qui doit atterrir dans le repo (composant théorique portable)
- Itération pixel-perfect avec Edit direct
- Artefacts où la cohérence brand > la vitesse

---

## Recommandation pour schoolsWP

**Garde les deux. Router selon l'intent :**

```
Demande utilisateur "design X"
├─ Exploration amont, pas de contexte brand arrêté, besoin de 2-3 pistes
│   → aidesigner (generate_design + url optionnel)
│   → Livrable : 2-3 HTML candidats, crédits faibles (~0,30 $)
│
├─ Production finale brand-compliant, export multi-format, adoption repo
│   → cc-design (workflow 6 étapes, starter-components)
│   → Livrable : HTML + PDF + PPTX, self-contained, 0 erreur console
│
└─ Itération sur un candidat aidesigner
    → refine_design (1 crédit) si modif globale
    → cc-design Edit si modif ciblée
```

**Intégration pipeline possible :** utiliser aidesigner comme **générateur de pistes** (T0), puis passer en cc-design pour **polish + adoption** (T1). Cas d'usage : pitch client → aidesigner pour 3 versions rapides → cc-design sur la version retenue pour brand compliance.

---

## Notes opérationnelles

- `aidesigner` a retourné "empty HTML artifact" au premier appel (sans consommer de crédit) — retry avec prompt légèrement plus court a réussi. **Transport MCP peut aussi drop** (c'est arrivé une fois aussi).
- `cc-design` a demandé un fix upstream (sélecteur `deck-stage > section` cassé après init JS) — corrigé dans le repo.
- Les deux outils respectent les Google Fonts externes ; pour un vrai offline, packager les woff2 localement.

## À tester plus tard

- Un même prompt au format "clone URL" : aidesigner.com VS cc-design getdesign-loader.md sur une URL schoolsWP.com
- Slide deck 8 slides head-to-head (là où cc-design est structurellement avantagé via deck_stage.js)
- Landing page complète (pas juste hero) pour voir si aidesigner tient la charge en densité d'info
- Mode "refine" sur 3 itérations : est-ce que aidesigner diverge ou converge ?
