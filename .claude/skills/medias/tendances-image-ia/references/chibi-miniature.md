# Trend : Miniature chibi

Le trend viral "mim's" : a partir d'une photo, on cree une **version chibi miniature** du sujet (grosse
tete, petit corps) **assise sur une paume de main ouverte**, pour une echelle realiste et attendrissante.
Expression boudeuse / contrariee. Style pastel, ultra-detaille, format vertical 4:5.

## Prompt master

Pars de ce prompt et adapte uniquement le genre et les details du sujet (`elle` / `il`, tenue, cheveux).
Garde intacts : la pose (assis dans la paume), l'echelle (chibi qui tient dans la main), l'expression
boudeuse, le style chibi pastel, et le format 4:5.

> A partir de la photo, cree une version chibi miniature du personnage, avec une grosse tete et un petit
> corps. Le personnage est assis sur la paume gauche ouverte d'une main realiste (echelle realiste : le
> personnage est minuscule et tient dans la paume), la main droite de la grande personne pressant
> delicatement la joue du chibi avec l'index. Le chibi a l'air boudeur et contrarie : joues gonflees,
> leger froncement de sourcils, yeux plisses. Style chibi ultra-detaille, couleurs pastel douces, texture
> lisse, eclairage net, faible profondeur de champ, accentuation de l'expression du visage et du contact
> des mains. Preserve la ressemblance et les traits du visage du sujet d'origine (coiffure, couleur de
> cheveux, tenue). Composition verticale, format 4:5.

Variante anglaise (Gemini repond bien aux deux ; utilise l'anglais si le rendu FR derape) :

> From the photo, create a chibi miniature version of the character, with a big head and a small body.
> The character sits on an open left palm of a realistic hand (realistic scale: the character is tiny and
> fits in the palm), while the right hand's index finger gently presses the chibi's cheek. The chibi looks
> pouty and annoyed: puffed cheeks, slight frown, squinted eyes. Ultra-detailed chibi style, soft pastel
> colors, smooth texture, crisp lighting, shallow depth of field, emphasis on the facial expression and
> the hand contact. Preserve the original subject's face and likeness (hairstyle, hair color, outfit).
> Vertical composition, 4:5 aspect ratio.

## Ce qui fait le rendu (ne pas zapper)

Ces details ne sont pas optionnels : ils font la difference entre un chibi generique et le trend viral.

- **Grosse tete / petit corps** : la signature chibi. Si la tete n'est pas exageree, ce n'est pas le trend.
- **Assis dans la paume ouverte** : l'echelle main / personnage est le ressort emotionnel ("trop mim's").
  Le personnage doit clairement tenir dans la main, pas etre a cote.
- **Index qui presse la joue** : le contact tactile renforce le cote attendrissant. Doigt sur la joue du chibi.
- **Expression boudeuse** : joues gonflees + sourcils legerement fronces + yeux plisses. C'est l'emotion
  qui rend la photo partageable.
- **Pastel doux + texture lisse + faible profondeur de champ** : look "rendu 3D mignon", arriere-plan flou.
- **Ressemblance preservee** : le visage doit rester reconnaissable comme le sujet de la photo source.
- **Format 4:5 vertical** : optimise pour les feeds mobiles (Instagram, TikTok).

## Adaptations selon le sujet

- Genre apparent : accorde "assis / assise", pronoms et tenue au sujet de la photo.
- Tenue / cheveux : reprends les elements marquants (couleur de cheveux, lunettes, casquette) pour que le
  chibi reste identifiable.
- Si la photo source est en plan large : recadre mentalement sur le visage / buste pour que le chibi en
  herite des traits nets.

## Criteres QA

- [ ] Tete nettement plus grosse que le corps (proportions chibi)
- [ ] Personnage minuscule, assis dans la paume ouverte (echelle coherente)
- [ ] Index pressant la joue visible
- [ ] Expression boudeuse lisible (joues gonflees, sourcils fronces, yeux plisses)
- [ ] Visage / ressemblance du sujet d'origine preserve
- [ ] Palette pastel, arriere-plan en faible profondeur de champ
- [ ] Format 4:5 : garanti par l'etape de crop (`scripts/crop-to-4-5.py`), pas par le moteur. Verifier que
      le crop n'a pas ampute la tete, les mains ou un accessoire (sinon relancer le crop avec un autre anchor).

Si un critere **creatif** cle manque (proportions, paume, expression), corrige par un nouvel `edit_image`
sur le chemin produit (ex. "make the head bigger and the body smaller, keep the same face", "accentue les
joues gonflees et le froncement de sourcils"). Le ratio, lui, est gere par le crop, pas par regeneration.

## Legende et hashtags

La legende est du texte **user-facing** : francais correct, **tous les accents** (`tête`, `même`, `vélo`,
`Légende`...). Pas de chemin de fichier local dedans. Livre **2 variantes** (le meme visuel ne se legende
pas pareil selon le reseau).

**Version courte / fun** (Instagram, TikTok, Pinterest) - accroche + concept + question/CTA, 1-3 emojis :

> Le trend ChatGPT du moment, version trop mim's ! 🙌🏻
> Moi en chibi minuscule, coincé dans une main et clairement pas d'accord 😤
> Je te fais la tienne ? Dis-moi en commentaire 🫶🏻

Hashtags : **5 a 8**, porteurs du trend + 2-4 de niche :

> #chibi #trend #chatgpt #miniature #figurine #aiart

**Version sobre** (LinkedIn) - ton pose, angle "trend IA teste", peu/pas d'emojis, question ouverte :

> J'ai teste le trend IA du moment : transformer une photo en version chibi miniature.
> Le rendu est bluffant de ressemblance, et un peu trop a mon gout sur la mine boudeuse.
> Vous l'utiliseriez pour quoi, vous, ce genre de visuel ?

Hashtags : **3 a 5** sobres :

> #IA #GenAI #chibi #ContenuVisuel

Adapte au sujet (ex. casque velo : `#vélo` / `#cyclisme` ; jardin : un tag lifestyle). Evite les listes de
15+ tags disperses : elles diluent la portee.

**Garde-fou marques** : ne mets jamais de nom de marque ou de studio dans le **prompt image** ni dans les
hashtags (pas de "Pixar", "Disney", "Funko Pop"...). Pour le style, reste sur du neutre : "stylized 3D",
"glossy vinyl toy look", "kawaii". Cela evite toute dependance a un style protege.
