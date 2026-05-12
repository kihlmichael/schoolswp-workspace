# Photo System — Briques élémentaires Alexya Amateur Photos

Ce fichier est le **kit complet** de génération de prompts photo amateur. À charger au premier appel du skill.

## Table des matières

1. [Les 4 types de plans](#les-4-types-de-plans)
2. [Structures de prompts par type](#structures-de-prompts-par-type)
3. [Mots-clés "amateur iPhone" obligatoires](#mots-clés-amateur-iphone-obligatoires)
4. [Mots-clés interdits](#mots-clés-interdits)
5. [Émotions girly mappées](#émotions-girly-mappées)
6. [Imperfections obligatoires par type](#imperfections-obligatoires-par-type)
7. [Banque de contextes par catégorie](#banque-de-contextes-par-catégorie)
8. [Tenues plausibles](#tenues-plausibles)
9. [Lumières amateur](#lumières-amateur)
10. [Exemples Gold Standard](#exemples-gold-standard)

---

## Les 4 types de plans

| Type | Description | Caractéristiques visuelles | Quand l'utiliser |
|------|-------------|----------------------------|------------------|
| **SELFIE** | Elle se prend en photo elle-même, bras tendu | Bras visible/coupé bas du cadre, angle plongeant léger possible, regard caméra direct, cadrage épaules ou mi-corps | C1 (intimiste) et C5 (action) — le plus fréquent |
| **SELFIE MIROIR** | Elle se photographie dans un miroir | Téléphone visible devant le corps, reflet, full body ou mi-corps possible, miroir = environnement | C1 (chambre/sdb) et C3 (fit check) |
| **TIERCE** | Photo prise par "quelqu'un d'autre" (ami fictif) | Pas de téléphone, deux mains libres, cadrage extérieur, possibilités cinématiques mais reste amateur | C2, C3, C4, C5 — la plus polyvalente |
| **POV** | Vue subjective : ses mains, ses pieds, son repas, son écran — pas son visage (ou très partiellement) | Top-down, à hauteur des mains, perspective subjective | C2 (lifestyle) et C5 (action) |

**Règle de cohérence** : un selfie ou selfie miroir suppose que **elle** prenait la photo. Donc pas de "candid moment" où elle aurait l'air de ne pas savoir qu'on la photographie. Si le prompt demande un moment "catch sur le vif", c'est forcément une TIERCE ou un POV.

---

## Structures de prompts par type

### SELFIE

```
Amateur iPhone [12/14] selfie, [angle], [expression émotionnelle], [tenue/élément visible], [environnement], [lumière]. [1-2 imperfections]. Raw, unedited, spontaneous. Slightly imperfect framing, arm partially visible at bottom edge. Use the reference image to accurately reproduce her facial features, body shape, proportions, and curves.
```

**Variations d'angle :**
- `straight-on selfie` — classique, regard direct
- `slightly high angle selfie` — angle plongeant, flatteur
- `side angle selfie, 3/4 view` — profil 3/4
- `close-up selfie, face fills the frame` — très intime
- `arm extended selfie, mid-body framing` — mi-corps inclus

### SELFIE MIROIR

```
Mirror selfie taken with iPhone [12/14], [pose], [tenue complète], [décor du miroir/pièce], [lumière]. Phone held at [chest/waist] level, [expression]. [Cadrage : full body / mid-body] visible in mirror reflection. [1-2 imperfections miroir]. Raw, unedited, authentic social media mirror selfie aesthetic. Use the reference image to accurately reproduce her facial features, body shape, proportions, and curves.
```

**Pièces classiques :**
- Salle de bain (tiles, lavabo, douche en arrière-plan)
- Chambre (lit fait/défait, vêtements qui traînent, fenêtre)
- Dressing / placard ouvert
- Ascenseur (cliché iconique du selfie miroir)
- Vestiaire de salle de sport
- Cabine d'essayage de magasin

### TIERCE

```
Candid photo taken with iPhone [12/14], [angle/distance], [pose/action], [expression], [tenue], [environnement détaillé], [lumière]. [1-2 imperfections]. Raw, unedited, spontaneous. [Si plein air / décor] Background slightly blurred. Use the reference image to accurately reproduce her facial features, body shape, proportions, and curves.
```

**Cadrages classiques :**
- `medium shot` — mi-corps
- `full body shot` — plein pied
- `wide shot` — elle dans son décor (C4 surtout)
- `close-up` — gros plan visage/épaules

### POV

```
POV amateur photo taken with iPhone [12/14], [angle : top-down / first-person hand], [élément central : ses mains tenant X / son écran / son repas], [environnement secondaire], [lumière]. [1-2 imperfections]. Raw, unedited, spontaneous. [Si mains visibles] The visible hands belong to a [âge]-year-old woman matching the reference image. Same skin tone. [Détail : manucure / bracelet / etc. cohérent avec l'identité].
```

**POV iconiques :**
- Mains tenant un café/matcha
- Mains tenant un livre / téléphone / écran
- Mains qui tapent sur clavier
- Mains qui appliquent skincare
- Pieds dans le sable / dans l'eau / dans des baskets neuves
- Repas top-down vu d'au-dessus

---

## Mots-clés "amateur iPhone" obligatoires

À insérer dans CHAQUE prompt (pioche selon le contexte) :

**Pour qualifier la prise de vue :**
- `amateur iPhone [12/14] photo`
- `candid iPhone selfie`
- `mirror selfie taken with iPhone`
- `shot on iPhone, authentic social media aesthetic`

**Pour qualifier la qualité brute :**
- `raw, unedited, spontaneous`
- `slightly imperfect framing`
- `casual composition`
- `subtle film grain`
- `slight motion blur` (occasionnel, sur 1-2 photos par pack max)
- `light JPEG compression artifacts` (occasionnel)
- `slightly overexposed tones` ou `slightly underexposed`

**À varier dans le pack** : ne pas mettre exactement les mêmes mots-clés sur les N prompts. Mélanger.

---

## Mots-clés interdits

Si un de ces termes apparaît dans un prompt, il est à supprimer :

- `professional photography`, `professional shoot`
- `studio lighting`, `softbox`, `ring light` (sauf si vraiment justifié contextuellement)
- `DSLR`, `mirrorless camera`, `camera body`
- `editorial`, `magazine quality`, `cover shoot`
- `high fashion`, `runway`, `couture`
- `glamour shot`, `boudoir photography`
- `perfectly composed`, `cinematographic composition`
- `model pose`, `pose for the camera`
- `serious gaze`, `fierce expression`, `intense stare` (sauf si vraiment intentionnel pour 1 photo)
- `bokeh`, `shallow depth of field`, `creamy background blur`

---

## Émotions girly mappées

| Émotion | Descripteur anglais à insérer dans le prompt |
|---------|-----------------------------------------------|
| **Cute / espiègle** | `playful pout, slight nose scrunch, eyes slightly squinted with a smile` |
| **Joues gonflées** | `cheeks puffed out playfully, eyes wide and amused` |
| **Langue tirée** | `tongue stuck out to the side, playful wink, eyes crinkled` |
| **Bouche en cœur** | `exaggerated kissy face, lips pursed forward, eyes laughing` |
| **Clin d'œil** | `playful wink, half-smile, head tilted slightly` |
| **Rire franc** | `head tilted back slightly, eyes crinkled in genuine laughter, mouth open mid-laugh` |
| **Sourire en coin** | `subtle smirk, one corner of the mouth lifted, knowing eyes` |
| **Lip bite séducteur** | `slight lower lip bite, lingering gaze, half-smile` |
| **Regard intense / charmeuse** | `intense soft gaze into camera, slightly parted lips, head tilted` |
| **Regard taquin** | `one eyebrow slightly raised, playful eyes, mischievous half-smile` |
| **Surprise / "oh"** | `wide eyes, mouth slightly open in a soft "oh", eyebrows raised` |
| **Réflexion / rêveuse** | `gaze slightly off-camera, soft pensive half-smile, hand near chin` |
| **Complicité** | `warm genuine smile, leaning slightly toward the camera, conspiratorial expression` |
| **Autodérision** | `exaggerated eye roll, amused smirk, hand on forehead` |
| **Bored chic** | `relaxed neutral expression, slightly bored, hand propping chin or playing with hair` |
| **Confiance / boss** | `confident calm gaze, subtle smile, chin slightly lifted` |
| **Fatigue mignonne (matin)** | `sleepy soft eyes, gentle smile, slightly tousled hair, hand near face` |

**Règle de variété** : dans un pack de N photos, utiliser au moins **8 émotions différentes** pour N≥20, au moins **5 différentes** pour N entre 10 et 20.

---

## Imperfections obligatoires par type

Chaque prompt doit contenir **AU MOINS 1 imperfection** de la liste ci-dessous, choisie selon le type de plan.

### Selfie miroir

- `subtle toothpaste streaks on the mirror`
- `faint fingerprints on the glass`
- `clutter on the bathroom counter (skincare bottles, hair tie, mascara)`
- `unmade bed visible in the reflection`
- `clothes piled on a chair in the background`
- `phone case slightly worn or with a sticker`
- `slight smudge on the camera lens`

### Selfie bras tendu

- `strand of hair crossing the frame`
- `fingertip slightly visible at the edge of the lens`
- `slightly tilted framing, not perfectly straight`
- `partially blurred edge from arm motion`
- `light flare from a window catching the lens`

### Lifestyle / Tierce

- `mismatched cushions on the couch`
- `dishes left on the counter in the background`
- `harsh tungsten or warm bulb light, not flattering`
- `slight overhead fluorescent light cast`
- `wrinkled bedsheets, clothes draped over chair`
- `uneven natural light, half shadow on face`
- `passersby slightly blurred in background`
- `mundane urban elements visible (trash bin, sign, parked car)`

### POV

- `slight finger over the lens edge`
- `crumbs or stains on the table surface`
- `slightly tilted angle, not symmetrical`
- `motion blur on the hand`
- `reflection of the iPhone in a glossy surface`

### Toutes catégories — texture peau/cheveux

- `natural skin texture with light grain, not airbrushed`
- `flyaway hair strands, not perfectly styled`
- `slightly chapped lips` (occasionnel)
- `light circles under eyes` (occasionnel, pour le côté humain)

---

## Banque de contextes par catégorie

### C1 — MIRROR SELFIES & SELFIES INTIMISTES

- Salle de bain matin (skincare visible, peignoir)
- Chambre lit défait fin de journée
- Dressing ouvert avant de sortir
- Cabine d'essayage magasin
- Ascenseur immeuble / hôtel
- Vestiaire salle de sport
- Selfie au lit (drap, chevet)
- Selfie sur le canapé sous plaid
- Selfie devant petit miroir mural

### C2 — LIFESTYLE & QUOTIDIEN

- Petit déj seule au comptoir
- Café terrasse, latte devant elle
- Brunch entre amis (amis flous)
- Métro / bus — coup d'œil par la fenêtre
- Voiture passager, ceinture visible, paysage flou
- Marché / supermarché chariot
- Lecture sur la plage / dans un parc / sur un rooftop
- Cuisine — elle prépare un truc
- Apéro avec amies (verres flous au premier plan)
- Promenade chien (laisse visible)
- Dans un Uber, regard par la fenêtre

### C3 — OUTFIT CHECK & MODE

- Plein pied en pied de mur urbain
- Devant porte d'immeuble parisienne / vintage
- Devant un mur graffé / brique / texture
- Sur une terrasse en hauteur
- Devant un magasin
- Dans un dressing / vestiaire (mais pas forcément miroir, juste plein pied)
- Dans une rue de jour calme
- Dans une chambre d'hôtel chic mais simple
- Devant une voiture (sa voiture / une voiture cool)

### C4 — ENVIRONNEMENT & DÉCOR

**Ici la contradiction de l'identité peut s'exprimer.** C'est la catégorie où on peut placer 1-2 photos liées à l'activité signature (sport, art, etc.).

- Plan large dans son lieu signature (gym, atelier, studio, fac, etc.)
- Petit village / port / quartier qui matche son lore
- Plage / forêt / montagne (cohérent avec son lifestyle)
- Concert / festival (foule floue)
- Rooftop avec ville en fond
- Restaurant / bar ambiance
- Aéroport (terminal, valise)
- Dans son lit, plan plus large avec pièce visible

### C5 — ACTION & MOMENTS CATCH

- Elle rigole en marchant (TIERCE, motion blur léger)
- Elle se brosse les cheveux dans la chambre
- Elle danse seule dans sa chambre / cuisine
- Elle cuisine, en pleine action (coupe un truc, mélange)
- Elle écrit / dessine / tape sur son ordi
- Elle stretche / s'étire au réveil
- Elle joue avec un chien / chat
- Elle court pour attraper le métro (un peu floue)
- Elle se maquille (POV ou TIERCE)
- Elle plie ou range des fringues
- Elle pratique son activité signature (1-2 photos max — règle des 20%)

---

## Tenues plausibles

À adapter selon l'identité de l'influenceuse. Quelques familles :

**Quotidien décontracté :**
- Jean droit / mom jean + t-shirt blanc + baskets
- Legging + crop top + sweat oversize
- Jogging + tee oversize + sneakers
- Pyjama (tee + short cotton, ou ensemble en satin si vibe sexy soft)

**Sortie / fit check :**
- Jean + chemise blanche oversize + bottes
- Robe simple + baskets ou sandales
- Ensemble blazer + jean + escarpins (chic décontracté)
- Jupe en jean / mini + crop top + bottines

**Sport / activité :**
- Brassière + legging assorti
- Short de boxe + crop top (si MMA / boxe)
- Tenue de yoga
- Maillot de bain / 2-pièces (été, plage)

**Cocooning / intimiste :**
- Peignoir blanc / nude
- T-shirt oversize + short
- Sweat à capuche + jogging cozy

**Règle** : la tenue doit être **cohérente avec le moment de la photo** (pas de robe de soirée pour un selfie matin) et avec l'archétype (pas de tailleur si l'identité est "étudiante chill").

---

## Lumières amateur

À varier dans le pack pour éviter l'effet "même heure de la journée 20 fois".

| Lumière | Mots-clés |
|---------|-----------|
| Matin doux | `soft morning light from a window`, `gentle natural light, slightly diffused` |
| Plein jour | `bright daylight`, `overcast diffuse light`, `flat midday light` |
| Golden hour | `warm golden hour light`, `late afternoon sunlight casting long shadows` |
| Crépuscule | `soft dusk light, blue hour tones` |
| Nuit intérieur | `warm indoor lamp light`, `harsh tungsten ceiling light`, `mixed lighting from TV and lamp` |
| Nuit extérieur | `street lamp glow, ambient city light`, `neon sign glow on the face` |
| Flash iPhone | `iPhone flash, harsh direct flash lighting, slight grain`, `night flash with red-eye reduction artifact` |
| Salle de bain | `harsh bathroom overhead light`, `mixed natural and artificial light from frosted window` |

**Quotas dans un pack de 20+** :
- Max 5 prompts en `bright daylight`
- Max 3 prompts en `golden hour` (sinon ça devient un cliché Instagram pro)
- Au moins 2-3 prompts en lumière "moche" (tungstène, néon, flash) — c'est ça qui fait amateur

---

## Exemples Gold Standard

### Exemple 1 — Identité MMA, C1 selfie miroir salle de bain

```
Mirror selfie taken with iPhone 14, casually standing in front of a small bathroom mirror, wearing an oversized white t-shirt and black cotton shorts, hair tied in a messy low ponytail, faint bruise on collarbone barely visible. Phone held at chest level, playful pout with slight nose scrunch. Mid-body framing visible in mirror reflection. Subtle toothpaste streaks on the mirror, cluttered counter with skincare bottles and a hair tie, harsh bathroom overhead light. Raw, unedited, authentic social media mirror selfie aesthetic. Use the reference image to accurately reproduce her facial features, body shape, proportions, and curves.
```

**Pourquoi ça marche :**
- Détail de l'identité subtil (faint bruise on collarbone) sans en faire le sujet
- Tenue cohérente "étudiante chill" — pas de tenue MMA
- Imperfections multiples (toothpaste streaks, counter clutter, harsh light)
- Émotion girly cute (playful pout, nose scrunch) — pas de "fierce fighter"
- Aucun mot-clé pro

### Exemple 2 — Identité MMA, C2 lifestyle café

```
Candid photo taken with iPhone 12, medium shot, sitting at a small café table near a window, wearing a beige hoodie with sleeves slightly pulled over hands, holding a latte in both hands close to her face, warm genuine smile leaning slightly toward camera with conspiratorial expression. Cluttered café table with a half-eaten croissant on a small plate, paper napkin, phone face-down. Soft morning light from the window, slight overexposure on the highlights. Background slightly blurred showing other patrons. Slight finger smudge on the lens edge. Raw, unedited, spontaneous. Use the reference image to accurately reproduce her facial features, body shape, proportions, and curves.
```

**Pourquoi ça marche :**
- TIERCE plausible (un ami photographie)
- Tenue casual étudiante (hoodie)
- Émotion complicité (warm smile, leaning, conspiratorial) — relation parasociale
- Détail "sleeves over hands" = micro-détail girly
- Imperfections (clutter, lens smudge, slight overexposure)
- Aucun lien avec le MMA — variation pure

### Exemple 3 — Identité MMA, C4 décor (avec contradiction)

```
Wide shot candid photo taken with iPhone 14, walking out of a boxing gym at dusk, wearing a plain black hoodie and fitted joggers, gym bag slung over one shoulder, sneakers, hand wraps still visible peeking out of the bag, hair damp and pulled back, exhausted satisfied half-smile, gaze ahead not at camera. Industrial street with the gym sign visible behind her, parked cars, harsh street lamp glow. Slight motion blur from her step. Raw, unedited, spontaneous. Background slightly blurred. Use the reference image to accurately reproduce her facial features, body shape, proportions, and curves.
```

**Pourquoi ça marche :**
- C'est UNE des photos liées à l'activité signature (rentrer dans les 20%)
- Pas dans la cage / pas en plein training — moment "après", plus humain
- Tenue cohérente
- Détail unique (cicatrice) implicite mais pas mentionné — l'image de référence fera le job
- Lumière "moche" (street lamp dusk) = très amateur

### Exemple 4 — Identité MMA, C5 action

```
Amateur iPhone 12 selfie, slightly high angle, lying on her back on the gym mat after training, hair stuck to forehead with sweat, hand wraps still on, exhausted but glowing smile with one eyebrow slightly raised, playful eyes. Padded mat texture visible, water bottle and phone case beside her on the mat, mid-body framing. Harsh gym fluorescent lighting, slightly overexposed. Strand of hair crossing the frame. Raw, unedited, spontaneous. Slightly imperfect framing, arm partially visible at bottom edge. Use the reference image to accurately reproduce her facial features, body shape, proportions, and curves.
```

**Pourquoi ça marche :**
- L'autre photo "liée au signature" — moment d'humanité, pas de pose combat
- Émotion "exhausted glowing smile + raised eyebrow" = girly malgré le contexte
- Imperfections multiples (sweat, hair stuck, fluorescent harsh, hair crossing frame)
- Tout ce qu'on EVITE : un cliché "fighter pose with fists up"

---

## Process de génération en batch — récap

Pour chaque prompt généré :

1. **Choisir la catégorie** (selon la répartition prescrite)
2. **Choisir le type de plan** (varier dans la catégorie)
3. **Choisir le contexte** (dans la banque de la catégorie, varier au max)
4. **Choisir la tenue** (cohérente avec contexte + identité)
5. **Choisir la lumière** (varier le moment de la journée)
6. **Choisir l'émotion** (varier dans le pack, min 5-8 différentes)
7. **Sélectionner 1-2 imperfections** (cohérentes avec le type de plan)
8. **Assembler selon la structure** du type de plan
9. **Vérifier** : aucun mot-clé interdit, image de référence mentionnée si visage visible, pas de redondance avec les prompts précédents

**Anti-redondance** : si tu as déjà fait un selfie miroir salle de bain, le prochain selfie miroir doit être ailleurs (chambre, ascenseur, dressing, etc.).
