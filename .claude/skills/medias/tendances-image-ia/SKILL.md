---
name: tendances-image-ia
description: >
  Transforme une photo existante en visuel viral selon un trend image IA du moment (ChatGPT / Gemini),
  puis fournit la legende et les hashtags prets a poster. Le premier trend disponible est la
  "miniature chibi" (personnage grosse tete / petit corps assis sur une paume ouverte).
  Utilise ce skill des que l'utilisateur veut appliquer un trend image a une photo : "transforme
  cette photo en chibi", "fais-moi le trend chibi miniature", "version miniature de cette photo",
  "le trend ChatGPT du moment", "rends ma photo trop mim's", "tendance image IA", meme si le mot
  "skill" n'est pas prononce et meme si seul le mot "trend" est mentionne avec une photo.
  NE PAS utiliser pour : generer une image from scratch sans photo source (utiliser nano-banana
  directement), une video motion schoolsWP (skill schoolswp-motion), une miniature YouTube (skills
  thumbnail), ou la production complete d'une influenceuse OFM (agent ofm-bot).
---

# Tendances Image IA

Applique un **trend image viral** (ChatGPT / Gemini) a une photo fournie par l'utilisateur, puis livre
le visuel **plus** sa legende et ses hashtags, prets a publier.

Le skill est une **bibliotheque de trends** : chaque trend a sa fiche dans `references/`. Le workflow
ci-dessous est commun a tous les trends ; les details creatifs (prompt master, cadrage, legende type)
vivent dans la fiche du trend.

## Moteur

L'outil de generation est **nano-banana** (Gemini image), deja configure (token `GEMINI_API_KEY`).

- `mcp__nano-banana__edit_image` — transforme une photo **existante** a partir d'un prompt. C'est l'outil
  principal : tous les trends partent d'une photo source.
- `mcp__nano-banana__continue_editing` — retouche la **derniere** image generee, sans repasser le chemin.
  A utiliser pour les ajustements iteratifs (expression, format, cadrage) apres une premiere passe.
- `mcp__nano-banana__generate_image` — generation from scratch. **A eviter ici** : un trend part toujours
  d'une photo, sinon on perd la ressemblance du sujet.

Avant la premiere generation d'une session, verifie la config si tu as un doute :
`mcp__nano-banana__get_configuration_status`.

## Trends disponibles

| Trend                | Fiche                              | En une ligne                                                       |
| -------------------- | ---------------------------------- | ------------------------------------------------------------------ |
| Miniature chibi      | `references/chibi-miniature.md`    | Personnage chibi (grosse tete) assis sur une paume ouverte, boudeur |

Quand l'utilisateur ne nomme pas explicitement de trend mais parle de "chibi", "miniature", "mim's"
ou "trend du moment" avec une photo, prends **miniature chibi** par defaut (c'est le trend phare).

## Workflow

Suis ces etapes dans l'ordre. C'est court par design : la valeur est dans le prompt master de la fiche,
pas dans une procedure lourde.

### 1. Identifier le trend et lire sa fiche

Determine le trend demande, puis **lis la fiche correspondante** dans `references/`. Ne reconstruis jamais
le prompt de memoire : la fiche contient le prompt master calibre, les details qui font le rendu viral, et
le modele de legende. Travailler sans la fiche donne un rendu generique et rate le trend.

### 2. Recuperer la photo source

Il faut un **chemin de fichier local** vers la photo. Si l'utilisateur n'a pas fourni de chemin (juste une
description ou un copier-coller), demande-le : sans photo source, le trend ne peut pas s'appliquer (on ne
genere pas from scratch, on transforme).

Regarde rapidement la photo (Read) pour adapter le prompt au sujet reel : genre apparent (il / elle),
tenue, cheveux, accessoires marquants. L'objectif est de **preserver l'identite et le visage** du sujet
tout en appliquant le style du trend.

### 3. Construire le prompt final

Pars du prompt master de la fiche et adapte uniquement ce qui depend du sujet (genre, tenue, details
notables). Garde intacts les elements qui font le trend (pose, echelle, expression, style, format). Le
format de sortie demande par les trends actuels est **vertical 4:5** — ne le change pas sans raison.

### 4. Generer

Appelle `mcp__nano-banana__edit_image` avec :

- `imagePath` : le chemin de la photo source
- `prompt` : le prompt final construit a l'etape 3

Recupere le **chemin du fichier produit** renvoye par l'outil (souvent sous `Documents/nano-banana-images/`).

### 5. Recadrer en 4:5 (etape deterministe, obligatoire)

Le moteur Gemini **n'honore pas** le ratio demande dans le prompt : il rend souvent en ~9:16 ou ~3:4,
jamais en 4:5 fiable. On corrige donc le format en post-traitement, sans relancer `edit_image` (pas de
regeneration, pas de degradation du rendu, resultat reproductible) :

```bash
python .claude/skills/medias/tendances-image-ia/scripts/crop-to-4-5.py <chemin_retourne> <chemin_final_4-5>
```

Le script fait un crop centre vers 4:5. Si le sujet a un element haut a proteger (tete, casque) et que le
crop centre risque de le rogner, passe un anchor vertical plus bas en 3e argument (ex. `0.35` garde le haut).
Le `<chemin_final_4-5>` est le livrable que tu communiques.

### 6. QA visuel

Regarde le rendu final (Read sur l'image 4:5) et verifie les criteres de la fiche du trend, typiquement :

- la ressemblance / le visage du sujet est preserve
- l'echelle est coherente (ex. chibi : le personnage tient dans la paume)
- l'expression et la pose demandees sont presentes
- le crop 4:5 n'a ampute aucun element cle (tete, mains, accessoire) ; sinon, relance le crop avec un anchor
  different plutot que de regenerer

Si un critere creatif cle echoue (pas le ratio, lui c'est le crop qui gere), corrige avec un nouvel
`edit_image` sur le chemin produit (un seul ajustement cible : "accentue les joues boudeuses", "preserve
mieux le visage"). N'enchaine pas dix retouches.

### 7. Legende et hashtags (2 variantes)

La legende est destinee a etre **postee telle quelle** : francais correct **avec tous les accents**
(`Légende`, `tête`, `même`, `vélo`), et **jamais** de chemin de fichier local ni d'info technique dedans
(ca, c'est pour toi, pas pour le post). Un meme visuel ne se legende pas pareil selon le reseau, donc livre
**deux variantes** :

- **Version courte / fun** (Instagram, TikTok, Pinterest) : accroche punchy + ligne concept (le perso
  minuscule, boudeur, coince dans une main) + **question / CTA** ("Je te fais la tienne ?"), 1-3 emojis.
  Hashtags : **5 a 8**, porteurs du trend (`#chibi`, `#trend`, `#chatgpt`) + 2-4 de niche.
- **Version sobre** (LinkedIn) : ton pose, angle "j'ai teste le trend IA du moment", peu ou pas d'emojis,
  une reflexion ou une question ouverte. Hashtags : **3 a 5** sobres (`#IA`, `#GenAI`, `#chibi`...).

Adapte au sujet (ex. casque velo : `#vélo` ; jardin : un tag lifestyle). Evite les listes de 15+ tags
disperses (elles diluent la portee). Le modele de legende vit dans la fiche du trend ; adapte-le.

Typographie : pas de tirets longs (em / en dash) dans la legende ; un trait d'union simple suffit. Pas de
noms de marques ni de studios dans le style de l'image ni dans les hashtags (voir la fiche).

## Format de sortie

Reponds toujours selon ce gabarit, pour que l'utilisateur ait tout au meme endroit, pret a poster :

```
## Trend applique : <nom du trend>

**Image** : <chemin du livrable final 4:5> (recadre en 4:5 via crop-to-4-5.py ; ce chemin est pour toi, pas
pour le post)

**Legende - courte / fun (Instagram, TikTok, Pinterest)**
<accroche + ligne concept + question/CTA, accents corrects, 1-3 emojis>
<5 a 8 hashtags : porteurs du trend + niche>

**Legende - sobre (LinkedIn)**
<ton pose, angle "trend IA teste", question ouverte, peu/pas d'emojis>
<3 a 5 hashtags sobres>

**QA**
- Visage / ressemblance preserve : oui / a verifier
- Echelle coherente : oui / a verifier
- Crop 4:5 sans amputation d'element cle : oui / a verifier
- Retouches appliquees : <aucune | description>
```

Si tu n'as pas pu valider un point visuellement, ecris "a verifier" plutot que d'affirmer.

## Ajouter un nouveau trend

La bibliotheque est faite pour grandir. Pour ajouter un trend :

1. Cree `references/<nom-du-trend>.md` (kebab-case) en suivant la structure de `chibi-miniature.md` :
   prompt master, details qui font le rendu, adaptations selon le sujet, criteres QA, legende + hashtags.
2. Ajoute une ligne dans le tableau **Trends disponibles** ci-dessus.
3. Si le nouveau trend introduit des declencheurs nouveaux (mots-cles), ajoute-les dans la `description`
   du frontmatter pour que le skill se declenche bien.

Le workflow commun (etapes 1 a 6) reste le meme : seule la fiche change.

## References

- `references/chibi-miniature.md` — Trend miniature chibi : prompt master, details, QA, legende.
- `scripts/crop-to-4-5.py` — Recadrage deterministe 4:5 en post-traitement (Pillow), appele a l'etape 5.
