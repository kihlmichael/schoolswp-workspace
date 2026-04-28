# Brief visuel + prompt visuel — contenu Instagram schoolsWP

> Template et règles pour produire des briefs visuels et des prompts exploitables en production graphique (Nano Banana par défaut, Midjourney / DALL-E / Canva possibles).

---

## Identité visuelle schoolsWP (rappel — règles non négociables)

1. **Fond clair** apaisant (`#FAFBFD`) — jamais de fond sombre par défaut
2. **Style propre** et épuré — pas de surcharge graphique
3. **Lisibilité forte** — typo nette, contraste suffisant
4. **Structure nette** — grilles propres, alignements, espaces généreux
5. **Rendu premium utile** — pro sans être froid
6. **Sobriété** — zéro effet tape-à-l'œil
7. **Accents de couleur** uniquement sur éléments d'action (CTA, chiffres clés, mots d'action)
8. **Typographie** — Nunito Sans Bold 700 pour titres, Roboto Regular 400 pour body
9. **Contrastes maîtrisés** — `#12111F` sur fond clair, contraste AA minimum

**Couleurs officielles** :
- `#00D400` — Primary (vert schoolsWP, réservé aux actions)
- `#00A100` — Secondary (vert foncé)
- `#E668D4` — Accent (rose, rare, pour les moments forts)
- `#12111F` — Darkest (textes)
- `#FAFBFD` — White bg (fond par défaut)

---

## Partie C — Template Brief visuel

Chaque post doit avoir un brief visuel structuré ainsi :

```markdown
### Brief visuel — Post [N] — [Titre interne]

- **Intention visuelle** : [l'émotion / le signal à provoquer en 1 phrase]
  Exemple : "Stopper le scroll par un gros chiffre d'alerte + faire ressentir le coût caché."

- **Type de composition** :
  [une option parmi : slide texte sur fond uni | carrousel fond uni + typographie forte | mockup produit + texte | photo + overlay texte | data-viz simple | illustration vectorielle minimale | capture d'écran annotée]

- **Hiérarchie de texte** :
  - Titre / slide 1 : [taille dominante, 4–7 mots max]
  - Sous-titre : [accompagnement, 6–10 mots]
  - Accent : [chiffre clé ou mot d'action, en couleur primary]

- **Ambiance** :
  [calme / affirmée / alerte / chaleureuse / technique]

- **Niveau de contraste** :
  AA minimum — texte `#12111F` sur fond `#FAFBFD`, accent `#00D400` réservé aux actions

- **Élément à mettre en avant** :
  [chiffre clé / icône / logo outil / screenshot / flèche / pictogramme / mockup]

- **Recommandation visuelle** :
  [recommandation précise — illustration, photo, mockup, data-viz, annotation]

- **À éviter visuellement** :
  - emojis en cascade
  - dégradés criards
  - effets 3D marketing
  - photos stock génériques "équipe souriante"
  - icônes Apple emoji sur fond coloré
  - templates Canva reconnaissables
  - typographies décoratives / scriptes
```

---

## Partie D — Template Prompt visuel

### Structure obligatoire du prompt

Chaque prompt doit contenir ces 7 blocs, dans cet ordre :

```
1. [SUJET] — qu'est-ce qu'on voit ?
2. [COMPOSITION] — cadrage, structure, grille
3. [STYLE] — style propre / minimaliste / éditorial / data-viz
4. [TYPOGRAPHIE] — Nunito Sans Bold 700 (titres), Roboto Regular 400 (body)
5. [PALETTE] — fond clair #FAFBFD, texte #12111F, accent #00D400 sur éléments d'action uniquement
6. [AMBIANCE] — calme / affirmée / technique / chaleureuse
7. [NÉGATIFS] — ce qu'il NE faut PAS (voir liste ci-dessous)
```

### Négatifs à inclure systématiquement

À appendre à la fin de chaque prompt :

```
--no emojis en cascade, dégradés saturés, effets 3D, glow, néon, photos stock génériques, icônes Apple emoji, templates Canva reconnaissables, typographie scripte, lens flare, bokeh excessif, surcharge graphique
```

### Exemples de prompts prêts à l'emploi

**Exemple 1 — Slide 1 carrousel "erreur FluentCRM"**

```
Slide Instagram carrée 1080x1080, fond clair #FAFBFD avec grain fin quasi invisible.
Grande typographie Nunito Sans Bold 700 centrée : "La faute que 9 utilisateurs sur 10 font avec FluentCRM" en #12111F.
Le mot "faute" surligné en vert #00D400 en bandeau discret.
Aucun autre élément visuel. Composition ultra épurée, marges généreuses.
Style : éditorial minimaliste, premium utile, lisible au pouce.
Ambiance affirmée, calme.
--no emojis, dégradés, effets 3D, photos, icônes, surcharge.
```

**Exemple 2 — Slide comparatif FluentCRM vs Mailchimp**

```
Slide Instagram carrée 1080x1080, fond clair #FAFBFD.
Composition en 2 colonnes verticales séparées par une ligne fine #12111F à 20% opacité.
Colonne gauche : logo FluentCRM (placeholder texte), titre "FluentCRM" en Nunito Sans Bold 700 #12111F, 3 points clés en Roboto Regular 400.
Colonne droite : logo Mailchimp (placeholder texte), titre "Mailchimp", 3 points clés.
En haut, bandeau fin avec le critère comparé : "Automatisation" en majuscules espacées, #12111F.
En bas, petit verdict "→ FluentCRM" en #00D400 Nunito Sans Bold 700.
Style éditorial, aéré, ambiance technique calme.
--no dégradés, 3D, glow, emojis, icônes Apple, surcharge.
```

**Exemple 3 — Post simple "retour d'expérience chiffré"**

```
Post Instagram carré 1080x1080, fond clair #FAFBFD.
Au centre, un très grand chiffre "−43 %" en Nunito Sans Bold 700, #00D400, taille dominante.
En dessous, en Roboto Regular 400 #12111F : "de temps passé sur la gestion des emails, depuis que j'utilise FluentCRM + OttoKit."
En bas, petite signature "schoolsWP" discrète en gris #12111F 40%.
Style : data-viz éditoriale, minimaliste, premium utile.
Ambiance affirmée, crédible.
--no dégradés, 3D, emojis, photos, icônes Apple, effets néon.
```

**Exemple 4 — Slide Reels "hook 0–3s"**

```
Vignette verticale Instagram Reels 1080x1920, fond clair #FAFBFD.
Texte principal occupant les 2/3 supérieurs : "Je n'utilise plus Yoast en 2026." en Nunito Sans Bold 700 #12111F, taille massive.
En bas du cadre, petit encart en rose #E668D4 20% opacité avec "Swipe →" en Roboto 400 #12111F.
Composition ultra épurée, zones mortes hautes et basses respectées (safe zones Reels).
Style : éditorial vertical, minimaliste.
Ambiance contrariante, calme.
--no dégradés, 3D, emojis, photos stock, glow, néon, surcharge.
```

**Exemple 5 — Mini-checklist slide**

```
Slide Instagram carrée 1080x1080, fond clair #FAFBFD.
Titre en haut : "Checklist — Activer OttoKit" en Nunito Sans Bold 700 #12111F.
5 items alignés à gauche, chaque ligne : carré case à cocher fine #12111F + texte en Roboto Regular 400 #12111F.
Les 5 items : espacement vertical généreux (24-32px entre items).
Les cases à cocher peuvent être remplies en #00D400 si l'item est "fait par défaut".
En bas à droite, logo schoolsWP discret.
Style : propre, structuré, éditorial technique.
Ambiance calme, pédagogique.
--no emojis, dégradés, 3D, photos, icônes Apple, fioritures.
```

**Exemple 6 — Post "opinion tranchée"**

```
Post Instagram carré 1080x1080, fond clair #FAFBFD.
Grande citation centrée : "Payer Yoast Premium en 2026, c'est payer pour rien." en Nunito Sans Bold 700 #12111F, 3 lignes max.
Les mots "pour rien" soulignés en rose #E668D4 (trait fin, pas un fluo).
Guillemets stylisés fins en haut et en bas de la citation, #12111F 30% opacité.
Aucun autre élément.
Style : éditorial fort, citation assumée, typographie dominante.
Ambiance contrariante, affirmée.
--no dégradés, 3D, emojis, photos, glow, surcharge.
```

---

## Règles générales pour rédiger un prompt visuel schoolsWP

1. **Mentionne toujours le fond** `#FAFBFD` (évite Midjourney de partir sur un fond sombre par défaut)
2. **Mentionne toujours la typographie** (Nunito Sans Bold 700 pour titres, Roboto 400 pour body) même si l'outil ne supporte pas le texte vectoriel — ça oriente le rendu
3. **Mentionne la couleur accent** `#00D400` **uniquement sur l'élément d'action** (CTA, chiffre clé, verdict) — jamais en fond, jamais en bordure large
4. **Précise le format** : 1080x1080 (post carré / carrousel IG), 1080x1920 (Reels / Stories)
5. **Écris en français ou en anglais selon l'outil** — pour Nano Banana (Gemini), le français fonctionne ; pour Midjourney, préfère l'anglais
6. **Négatifs systématiques** : la liste `--no` doit toujours être présente en fin de prompt
7. **Ne jamais surcharger** : 1 idée visuelle principale par image. Si le prompt dépasse 8 lignes, c'est probablement trop
8. **Signature schoolsWP** : accepter / suggérer un petit logo discret en bas à droite, en gris 40% opacité

---

## Mapping format → type de visuel

| Format post            | Type visuel recommandé                                                      |
| ---------------------- | --------------------------------------------------------------------------- |
| Carrousel tutoriel     | Slides fond uni + typo forte + 1 chiffre ou pictogramme par slide           |
| Carrousel comparatif   | Slides 2 colonnes + verdict coloré en bas                                   |
| Carrousel opinion      | Slides citation dominante + typo massive                                    |
| Post simple            | Chiffre / citation / verdict dominant sur fond uni                          |
| Mini-checklist         | Slide structurée avec items + cases à cocher                                |
| Mini-comparatif        | Tableau visuel simple 2 colonnes                                            |
| Reels hook             | Format vertical, texte massif, safe zones respectées                        |
| Stories                | Format vertical, texte + un élément interactif (poll, question, lien)       |

---

## Outils de génération — préférences schoolsWP

1. **Nano Banana** (`gemini-2.5-flash-image`) — par défaut, validé A/B le 2026-04-16 (voir `memory/feedback_image_gen.md`)
2. **Canva** — pour les carrousels avec contrôle précis du texte
3. **Midjourney** — pour les visuels éditoriaux / illustrations (prompts en anglais)
4. **DALL-E / gpt-image-1** — fallback si Nano Banana indispo

---

## Anti-prompts (ne jamais écrire)

- "Vibrant colors" (tire vers le saturé)
- "Eye-catching" (tire vers le gimmicky)
- "Trendy" (tire vers le générique instagrammable)
- "Flat design with bright colors" (tire vers le plat saturé)
- "With emojis" (ne jamais demander d'emojis dans un visuel schoolsWP)
- "3D rendering" (hors scope identité visuelle)
- "Gradient background" (hors identité schoolsWP)
- "Bokeh / lens flare" (trop marketing, pas lisible)
