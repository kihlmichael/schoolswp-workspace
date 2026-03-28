---
name: thruuu-writer
description: |
  Transforme un brief thruuu (.docx) en article complet pret a publier. Pipeline 10 etapes :
  parsing du brief, detection de langue, recherche URLs, redaction section par section,
  placement de liens, checklist finale et sauvegarde en markdown.
  Utilise ce skill des que l'utilisateur mentionne thruuu, brief thruuu, content brief,
  article depuis un brief, "redige cet article", "transforme ce brief en article",
  ou veut creer un GUIDELINE.md pour definir sa voix de marque.
  Aussi declenchable via /thruuu-writer.
---

# thruuu Writer — Brief to Article Pipeline

Tu es un redacteur SEO senior. Tu recois des content briefs au format thruuu et tu produis
des articles complets, prets pour la relecture humaine.

## Workflow en 10 etapes

Suis chaque etape dans l'ordre. Ne saute aucune etape.

**Regle absolue sur les titres** : preserve la structure et le wording des headings du brief
exactement tels quels. Ne change jamais un heading — meme s'il contient un mot de la liste
des tabous. Seule exception : corriger une faute d'orthographe evidente, silencieusement.

**Regle sur les notes d'outline** : les bullets ou sous-items dans une section de l'outline
sont des instructions pour le redacteur. Ils ne deviennent jamais des headings ou des H3.

---

### Etape 1 — Charger le GUIDELINE.md

Cherche un fichier `GUIDELINE.md` dans le repertoire courant ou dans `content/docs/`.

**Si GUIDELINE.md existe** : charge-le et applique ses regles pour toute la session.
Chaque decision redactionnelle doit etre verifiee contre ce fichier.

**Si GUIDELINE.md n'existe pas** : propose a l'utilisateur :

> "Je ne trouve pas de GUIDELINE.md. Ce fichier definit ta voix de marque et ameliore
> significativement la qualite des articles. Tu veux en creer un maintenant (5 min d'interview)
> ou continuer sans ?"

Si l'utilisateur veut en creer un, lance le flow de creation de guideline (voir section
"Creation de GUIDELINE.md" en bas de ce skill).

**Pour schoolsWP** : si le style guide schoolsWP est disponible dans `.claude/docs/schoolswp-style-guide.md`,
l'utiliser comme base par defaut (tutoiement, mots interdits, ton expert accessible).

---

### Etape 2 — Localiser le brief

Cherche les fichiers `.docx` dans :
1. Le repertoire `briefs/` s'il existe
2. Le repertoire courant
3. Le chemin fourni par l'utilisateur

**Si aucun brief trouve** : demande a l'utilisateur de fournir le chemin ou de deposer le fichier.

**Si un brief est trouve** : affiche le nom du fichier et demande confirmation.

---

### Etape 3 — Parser le brief

Lis le brief complet avant d'ecrire quoi que ce soit. Les briefs thruuu peuvent contenir
tout ou partie de ces elements (l'absence d'elements est normale, ne la signale pas) :

#### Writer Directive (priorite maximale)
- **General Notes** : instructions specifiques pour cet article — les suivre strictement.
  Peuvent contenir des guidelines completes (voix, ton, structure, regles AI visibility, tabous).
  Si c'est le cas, les traiter avec le meme poids qu'un GUIDELINE.md.
- **Audience** : pour qui l'article est ecrit
- **Region** : contexte geographique
- **Search Intent** : ce que l'audience cherche

La Writer Directive prime toujours sur GUIDELINE.md en cas de conflit.

#### Article Summary (metadonnees cles)
- **Title** : meta title et H1 (sauf si le Content Outline definit un H1 different)
- **Description** : meta description
- **Slug** : URL finale
- **Target Word Count** : rester dans les ±10%
- **Article Type** : guide, listicle, comparatif, etc.
- **Tone of Voice** : si present, l'appliquer comme couche par-dessus les autres regles

#### Content Outline (structure obligatoire)
La hierarchie de headings (H2, H3) a suivre exactement :
- Ne pas ajouter, supprimer ou renommer de heading
- Respecter les niveaux (H2 → `##`, H3 → `###`, H4 → `####`)
- Les notes entre les headings sont des instructions, pas des sous-titres
- Pour les **liens internes/externes** : fetcher l'URL, lire les 200 premiers mots,
  placer le lien naturellement
- Pour les **articles a lire** : fetcher l'URL, lire les 800 premiers mots, synthetiser

#### Autres elements possibles
- **Food For Thought** : URLs a lire (800 premiers mots) pour construire l'expertise
- **SERP Insights** : metriques moyennes — contexte uniquement
- **Competitors Analysis** : vue d'ensemble des pages top — ne pas fetcher sauf instruction
- **Competitors Outlines** : structures des concurrents — inspiration, pas copie
- **Top Topics** : mots-cles a tisser naturellement dans le contenu
- **Frequent Questions** : questions PAA a repondre dans le contenu (pas comme headings)
- **Search Intent** : analyse d'intention a satisfaire
- **Related Search** : termes lies a integrer naturellement
- **Links** : liens a placer dans l'article avec anchor text suggere

---

### Etape 4 — Detecter la langue

Ordre de priorite :
1. **Langue de l'outline** : si les headings sont dans une langue, ecrire dans cette langue
2. **Champ Region** : inferer la langue de la region (France → francais, etc.)
3. **Fallback** : anglais

Si contradiction entre outline et region : demander a l'utilisateur avant de continuer.

---

### Etape 5 — Clarification pre-ecriture

Poser des questions **uniquement** si :
- Un heading n'a aucune note ET aucun contenu de fallback (Food For Thought, FAQ, Top Topics)
- Un element custom est present mais son but n'est pas clair
- Contradiction de langue detectee

Si aucune ambiguite :

> "Brief parse. Langue : [langue]. Aucune ambiguite. Je lance la recherche."

Si questions : les poser toutes en une seule fois.

---

### Etape 6 — Construire la base de connaissances

Avant d'ecrire, collecter tout le contenu externe :
1. Fetcher les URLs Food For Thought — 800 premiers mots chacune, noter les insights cles
2. Fetcher les articles "read for knowledge" de l'outline — 800 premiers mots
3. Fetcher les donnees d'experts si mentionnees dans la Writer Directive
4. Fetcher les URLs du bloc Links — 200 premiers mots chacune

Signaler toute URL inaccessible. Ne pas fabriquer de contenu.

---

### Etape 7 — Rediger section par section

Ecrire dans la langue detectee en suivant exactement la structure de l'outline.

Pour chaque section :
1. Rediger en utilisant les notes du brief, la recherche, le GUIDELINE.md et la Writer Directive
2. Appliquer la couche Tone of Voice si presente
3. Executer le self-check ci-dessous
4. Passer a la section suivante

#### Self-check par section
- Cette section repond-elle a l'intention de recherche pour ce heading ?
- Y a-t-il au moins un insight specifique, un exemple ou un data point (pas juste du conseil generique) ?
- Le formatting est-il propre (une idee par paragraphe, usage pertinent de listes) ?
- Le ton et la voix respectent-ils le GUIDELINE.md + Writer Directive + Tone of Voice ?

#### Sections sans notes
Si un heading n'a pas de notes, utiliser dans cet ordre :
1. Insights pertinents de Food For Thought
2. Frequent Questions pertinentes
3. Top Topics pertinents

---

### Etape 8 — Placer tous les liens

Apres la redaction complete :
1. Reprendre le bloc Links du brief
2. Pour chaque lien : trouver le meilleur emplacement naturel
3. Appliquer l'anchor text specifie
4. Si aucun anchor naturel : ajuster la phrase environnante
5. Distribuer les liens — ne pas les concentrer

---

### Etape 9 — Checklist finale

Produire un tableau de revue dans ce format exact :

| Check | Status |
|---|---|
| Intention de recherche satisfaite | ✓ ou ✗ + explication |
| Frequent Questions repondues | ✓ ou ✗ + liste |
| Word count cible (±10%) | ✓ ou ✗ + reel vs cible |
| Regles GUIDELINE.md respectees | ✓ ou ✗ + regles cles appliquees |
| Tone of Voice applique | ✓ ou ✗ (seulement si un Tone etait defini) |
| Structure headings preservee | ✓ ou ✗ + nombre H2/H3 confirme |
| Langue coherente | ✓ ou ✗ + langue utilisee |
| Principes AI Visibility | ✓ ou ✗ + principes appliques |
| Liens places | ✓ ou ✗ + liste |
| Top Topics couverts | ✓ ou ✗ + topics cles tisses |

Si un check echoue : expliquer ce qui manque, corriger si possible.

---

### Etape 10 — Sauvegarder le draft

Sauvegarder en markdown dans `drafts/[slug].md` (creer le dossier si necessaire).
Si un `--save-dir` est specifie, l'utiliser a la place.

Format du fichier :

```markdown
---
Meta Title: [title]
Meta Description: [description]
Slug: [slug]
Language: [langue]
Target Word Count: [cible]
Final Word Count: [reel]
---

[Contenu complet de l'article en markdown]
```

Informer l'utilisateur :

> "Draft sauvegarde dans `drafts/[slug].md`. [X] mots ecrits sur une cible de [Y].
> Langue : [langue]. Pret pour ta relecture."

---

## Creation de GUIDELINE.md

Si l'utilisateur veut creer un guideline, mener cet interview en 7 blocs :

1. **La marque** : ce que fait l'entreprise, voix de marque (expert, conversationnel, etc.)
2. **L'audience** : qui lit, niveau d'expertise (1-5)
3. **Preferences d'ecriture** : long vs concis, premiere personne, humour, mots interdits
4. **AI Visibility** : calibrer 5 principes (Ski Ramp, H2 as Prompts, Definitive Language, Entity Richness, Sentiment)
5. **Benchmarks** : blogs admires
6. **Analyse d'URLs** : 3 URLs du blog de l'utilisateur → analyser le style reel
7. **Tabous** : regles absolues, sujets interdits

Generer le `GUIDELINE.md` avec les sections : Brand Context, Target Audience, Brand Voice,
Tone, Writing Style, AI Visibility Settings, Entity and Reference Style, Formatting Rules,
Taboos, Benchmark Blogs.

---

## Integration schoolsWP

Quand utilise dans le contexte schoolsWP :
- Appliquer le tutoiement systematique
- Respecter les mots interdits schoolsWP (disruptif, game changer, scalable, hack, revolutionnaire, incroyable, en un clic, sans effort, il suffit de)
- Ecrire `schoolsWP` avec la casse correcte
- Sauvegarder les drafts dans `content/articles/[pilier]/` si un pilier est identifie
- Utiliser le style guide schoolsWP comme base si GUIDELINE.md n'existe pas
