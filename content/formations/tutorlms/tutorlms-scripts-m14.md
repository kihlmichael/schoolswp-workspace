# Scripts video — Module 14 : Content Bank & Shortcodes

**Formation** : Maitriser TutorLMS
**Module** : M14 — Content Bank & Shortcodes (Premium)
**Lecons** : 6 videos + 1 quiz
**Duree totale** : ~30 min
**Date** : 2026-03-23

---

### Lecon 14.1 — Content Bank

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS admin
**Source** : Video #38 + doc content-bank

---

**[INTRO — face camera]**

Tu crees plusieurs cours et tu te retrouves a refaire les memes lecons a chaque fois ? La Content Bank de TutorLMS resout ce probleme. C'est une bibliotheque centralisee ou tu stockes des lecons reutilisables — une seule version, utilisable dans autant de cours que tu veux. Dans cette lecon, on met ca en place.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Settings > Content Bank]

Premiere etape : active la Content Bank. Va dans Tutor LMS, Settings, puis cherche l'option Content Bank. Active-la. A partir de maintenant, un nouveau menu "Content Bank" apparait dans le menu lateral de TutorLMS.

**[ECRAN — screencast Content Bank]**

[Navigation vers Tutor LMS > Content Bank]

Clique sur Content Bank dans le menu. Tu arrives sur une liste vide pour l'instant. C'est ici que tu vas stocker toutes tes lecons reutilisables.

Clique sur "Add New". Tu retrouves l'editeur classique de lecon TutorLMS — titre, contenu, video, pieces jointes. La seule difference : cette lecon n'est rattachee a aucun cours. Elle existe de maniere autonome dans ta bibliotheque.

Remplis ta lecon comme d'habitude. Titre, contenu texte, video si besoin. Puis sauvegarde.

**[ECRAN — screencast Course Builder]**

[Navigation vers un cours > Course Builder > ajout de lecon depuis la Content Bank]

Maintenant, ouvre le Course Builder d'un cours. Quand tu ajoutes une nouvelle lecon a un topic, tu vois un bouton "Import from Content Bank" a cote du bouton classique "Add Lesson".

Clique dessus. La liste de tes lecons Content Bank s'affiche. Selectionne celle que tu veux, confirme. La lecon est importee dans ton cours.

**[ECRAN — screencast montrant la lecon dans deux cours]**

[Ouvre deux cours differents qui partagent la meme lecon]

Point important : la lecon importee est une copie independante. Si tu modifies la version dans le cours, ca ne change pas la version dans la Content Bank. Et inversement. C'est une copie a l'import, pas un lien dynamique.

Ca veut dire : si tu corriges une erreur dans la lecon source, tu dois reimporter dans les cours concernes. Garde ca en tete.

**[TRANSITION — face camera]**

La Content Bank prend tout son sens quand tu as des lecons communes entre plusieurs formations. Par exemple, une lecon "Comment naviguer dans l'interface" ou "Les bases de WordPress" — tu la crees une fois, et tu l'importes partout. Pour un formateur qui gere 5 ou 10 cours, c'est un gain de temps enorme.

---

**Points cles** :
- Content Bank = bibliotheque centralisee de lecons reutilisables
- Activation dans Tutor LMS > Settings
- Creation de lecons autonomes (pas rattachees a un cours)
- Import dans n'importe quel cours via le Course Builder
- L'import cree une copie independante (pas un lien dynamique)
- Ideal pour les lecons communes a plusieurs formations

**Mots cles SEO** : TutorLMS Content Bank, lecons reutilisables TutorLMS, bibliotheque de contenu LMS WordPress, Content Bank Tutor LMS

---

### Lecon 14.2 — Shortcodes Tutor LMS

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast WordPress + TutorLMS
**Source** : doc shortcodes

---

**[INTRO — face camera]**

TutorLMS genere ses pages automatiquement — tableau de bord, liste de cours, panier. Mais parfois, tu veux afficher ces elements ailleurs. Sur ta page d'accueil, dans un article, ou dans une landing page. C'est exactement le role des shortcodes. Dans cette lecon, on passe en revue les shortcodes TutorLMS et on les integre dans des pages WordPress.

**[ECRAN — screencast WordPress editeur]**

[Montre l'editeur de page WordPress avec le bloc Shortcode]

Un shortcode, c'est un bout de texte entre crochets que WordPress remplace par du contenu dynamique. TutorLMS en fournit plusieurs. Pour les utiliser, ouvre n'importe quelle page dans l'editeur WordPress, ajoute un bloc "Shortcode" et colle le code.

Premier shortcode — la liste des cours :

```
[tutor_course]
```

Ca affiche la grille de tous tes cours publies, avec les miniatures, les titres et les prix. Tu peux l'ajouter sur ta page d'accueil pour mettre tes formations en avant.

**[ECRAN — screencast front-end]**

[Montre le rendu du shortcode sur la page]

Voila le rendu. La grille de cours s'affiche exactement comme sur la page catalogue native de TutorLMS.

**[ECRAN — screencast WordPress editeur]**

[Retour a l'editeur, ajout d'autres shortcodes]

Deuxieme shortcode — le tableau de bord eleve :

```
[tutor_dashboard]
```

Ca affiche le dashboard complet de l'eleve — cours en cours, progression, certificats. Utile si tu veux integrer le dashboard dans une page personnalisee plutot que la page par defaut.

Troisieme shortcode — le formulaire d'inscription instructeur :

```
[tutor_instructor_registration_form]
```

Si tu acceptes les instructeurs externes, ce shortcode affiche le formulaire d'inscription. Tu peux le placer sur une page dediee "Devenir formateur".

**[ECRAN — screencast avec parametres]**

[Montre l'ajout de parametres au shortcode]

Certains shortcodes acceptent des parametres. Par exemple, pour afficher uniquement les cours d'une categorie :

```
[tutor_course category="wordpress"]
```

Ou pour limiter le nombre de cours affiches :

```
[tutor_course count="6"]
```

Tu peux combiner les parametres :

```
[tutor_course category="wordpress" count="3" orderby="date"]
```

**[ECRAN — screencast liste complete des shortcodes]**

[Montre la documentation TutorLMS avec la liste des shortcodes]

Voici les principaux shortcodes disponibles :

- `[tutor_course]` — grille de cours
- `[tutor_dashboard]` — tableau de bord eleve
- `[tutor_instructor_registration_form]` — inscription instructeur
- `[tutor_student_registration_form]` — inscription eleve
- `[tutor_instructor_list]` — liste des instructeurs
- `[tutor_course_search]` — barre de recherche de cours

La documentation TutorLMS les liste tous avec leurs parametres.

**[TRANSITION — face camera]**

Les shortcodes te donnent une flexibilite totale pour integrer TutorLMS dans tes pages WordPress. La recommandation schoolsWP : utilise `[tutor_course]` sur ta page d'accueil pour afficher tes formations, et `[tutor_dashboard]` sur une page personnalisee si le design par defaut ne te convient pas. Pour tout le reste, les pages natives TutorLMS font le travail.

---

**Points cles** :
- Shortcodes = blocs dynamiques TutorLMS a inserer dans n'importe quelle page WordPress
- `[tutor_course]` — grille de cours (parametres : category, count, orderby)
- `[tutor_dashboard]` — tableau de bord eleve complet
- `[tutor_instructor_registration_form]` — formulaire inscription instructeur
- `[tutor_student_registration_form]` — formulaire inscription eleve
- `[tutor_instructor_list]` — liste des instructeurs
- Utiliser le bloc "Shortcode" dans l'editeur WordPress

**Mots cles SEO** : shortcodes TutorLMS, integrer TutorLMS page WordPress, tutor_course shortcode, afficher cours TutorLMS page accueil

---

### Lecon 14.3 — LaTeX dans les cours

**Duree** : 4 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS editeur
**Source** : doc tutorials/tutor-lms-latex

---

**[INTRO — face camera]**

Tu enseignes les maths, la physique, la chimie, ou n'importe quelle matiere avec des formules ? TutorLMS supporte LaTeX — le standard pour ecrire des equations mathematiques propres. Dans cette lecon, on active LaTeX et on l'utilise dans les lecons et les quiz.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Settings]

Premiere etape : verifie que le support LaTeX est active. Va dans Tutor LMS, Settings, puis cherche l'option liee a LaTeX ou MathJax. TutorLMS utilise MathJax pour le rendu — c'est la bibliotheque standard qui transforme le code LaTeX en formules visuelles.

Active l'option si elle n'est pas deja cochee.

**[ECRAN — screencast editeur de lecon]**

[Navigation vers une lecon > editeur de contenu]

Maintenant, ouvre l'editeur d'une lecon. Pour ecrire une formule LaTeX, tu utilises la syntaxe standard : entoure ta formule de doubles dollars pour un bloc centre, ou de simples dollars pour une formule en ligne.

Exemple — formule en ligne dans un paragraphe :

```
L'aire d'un cercle est $A = \pi r^2$ ou r est le rayon.
```

Exemple — formule en bloc, centree :

```
$$E = mc^2$$
```

**[ECRAN — screencast front-end]**

[Montre le rendu de la formule cote eleve]

Cote eleve, MathJax prend le relais et affiche la formule avec un rendu typographique propre. Les fractions, les racines carrees, les integrales — tout est supporte.

Quelques formules courantes :

- Fraction : `$\frac{a}{b}$`
- Racine carree : `$\sqrt{x}$`
- Somme : `$\sum_{i=1}^{n} x_i$`
- Integrale : `$\int_{0}^{1} f(x) dx$`

**[ECRAN — screencast editeur de quiz]**

[Navigation vers un quiz > editeur de question]

LaTeX fonctionne aussi dans les quiz. Quand tu crees une question, tu peux inserer des formules dans l'enonce et dans les choix de reponse. Meme syntaxe : dollars simples ou doubles.

Par exemple, pour une question de maths :

Enonce : "Quelle est la derivee de $f(x) = x^3$ ?"
- Choix A : $f'(x) = 3x^2$ (bonne reponse)
- Choix B : $f'(x) = 2x^2$
- Choix C : $f'(x) = x^2$

Le rendu est propre dans le quiz cote eleve.

**[TRANSITION — face camera]**

LaTeX dans TutorLMS, c'est indispensable pour les formations scientifiques. Le rendu est professionnel, la syntaxe est standard. Si tu ne connais pas LaTeX, il existe des editeurs visuels en ligne — tape "LaTeX equation editor" dans Google, compose ta formule visuellement, et copie le code genere dans TutorLMS.

---

**Points cles** :
- TutorLMS utilise MathJax pour le rendu LaTeX
- Activation dans Tutor LMS > Settings
- Syntaxe : `$formule$` (en ligne) ou `$$formule$$` (bloc centre)
- Fonctionne dans les lecons ET dans les quiz (enonces + reponses)
- Supporte fractions, racines, sommes, integrales, matrices
- Editeurs visuels en ligne disponibles pour les debutants LaTeX

**Mots cles SEO** : LaTeX TutorLMS, formules mathematiques LMS WordPress, MathJax TutorLMS, equations cours en ligne WordPress

---

### Lecon 14.4 — Embed PDF dans les lecons

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS + WordPress
**Source** : doc tutorials/embed-pdf

---

**[INTRO — face camera]**

Tu as des supports de cours en PDF — fiches de revision, exercices, documents de reference ? Plutot que de mettre un simple lien de telechargement, tu peux integrer le PDF directement dans la lecon. L'eleve le consulte sans quitter la page. Dans cette lecon, on voit comment faire.

**[ECRAN — screencast TutorLMS editeur de lecon]**

[Navigation vers une lecon > editeur de contenu]

Ouvre l'editeur d'une lecon. On a deux approches pour integrer un PDF.

**Approche 1 : piece jointe TutorLMS**

La plus simple. En bas de l'editeur de lecon, tu as une section "Attachments". Clique sur "Upload", selectionne ton PDF. L'eleve verra un bouton de telechargement en bas de la lecon.

C'est fonctionnel, mais l'eleve doit telecharger le fichier pour le lire. On peut faire mieux.

**Approche 2 : embed dans le contenu**

[Montre l'ajout d'un bloc dans l'editeur]

Pour afficher le PDF directement dans la lecon, utilise un bloc "File" dans l'editeur WordPress. Ajoute un bloc, cherche "File", selectionne-le. Upload ton PDF ou choisis-le depuis la mediatheque.

Dans les options du bloc, active "Inline Embed". Ca affiche un viewer PDF directement dans la page. L'eleve peut faire defiler les pages, zoomer, et telecharger si besoin.

**[ECRAN — screencast front-end]**

[Montre le rendu cote eleve avec le PDF integre]

Voila le rendu. Le PDF s'affiche dans un cadre integre a la lecon. L'eleve navigue entre les pages sans quitter le cours. Le bouton de telechargement reste disponible en haut du viewer.

**[ECRAN — screencast editeur]**

[Retour a l'editeur, ajustement de la taille]

Tu peux ajuster la hauteur du viewer PDF dans les options du bloc. Par defaut, c'est souvent trop petit. Monte a 600 ou 800 pixels pour un confort de lecture correct.

**[ECRAN — screencast avec un plugin PDF]**

[Montre l'alternative plugin PDF Embedder]

Si le bloc natif ne te convient pas, il existe des plugins dedies comme PDF Embedder. L'avantage : un rendu plus propre avec pagination, zoom, et un mode plein ecran. L'inconvenient : un plugin supplementaire a maintenir.

La recommandation schoolsWP : commence avec le bloc File natif. Si tu as beaucoup de PDF et que le rendu compte pour tes eleves, passe sur PDF Embedder.

**[TRANSITION — face camera]**

L'embed PDF transforme tes lecons en vrais supports de cours. Au lieu d'un lien que personne ne clique, le document est la, visible, consultable immediatement. C'est particulierement utile pour les fiches de synthese, les exercices a remplir, et les documents de reference.

---

**Points cles** :
- Approche 1 : piece jointe TutorLMS (section Attachments) — telechargement uniquement
- Approche 2 : bloc "File" WordPress avec "Inline Embed" active — viewer PDF dans la page
- Ajuster la hauteur du viewer (600-800px recommande)
- Alternative plugin : PDF Embedder (rendu superieur, plugin supplementaire)
- Recommandation schoolsWP : bloc File natif d'abord, plugin si besoin
- Ideal pour fiches de revision, exercices, documents de reference

**Mots cles SEO** : embed PDF TutorLMS, integrer PDF cours en ligne, PDF dans lecon WordPress, viewer PDF LMS

---

### Lecon 14.5 — Sous-titres video

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS
**Source** : doc tutorials/video-captions

---

**[INTRO — face camera]**

Les sous-titres, c'est a la fois une question d'accessibilite et de confort. Certains eleves apprennent mieux en lisant, d'autres sont dans un environnement bruyant, et d'autres encore ne parlent pas ta langue maternelle. TutorLMS supporte les sous-titres sur les videos de cours. Dans cette lecon, on les ajoute.

**[ECRAN — screencast preparation du fichier]**

[Montre un fichier .vtt dans un editeur de texte]

Les sous-titres utilisent le format WebVTT — un fichier texte avec l'extension `.vtt`. Voici a quoi ca ressemble :

```
WEBVTT

00:00:00.000 --> 00:00:03.000
Bienvenue dans cette lecon sur TutorLMS.

00:00:03.500 --> 00:00:07.000
Aujourd'hui, on configure les certificats.
```

Chaque bloc contient un timecode de debut, un timecode de fin, et le texte a afficher. C'est simple a editer manuellement, mais pour une video de 10 minutes, ca prend du temps.

**[ECRAN — screencast outil de sous-titrage]**

[Montre un outil de generation de sous-titres]

La methode rapide : utilise un outil de transcription automatique. Des services comme Whisper (gratuit, open source) ou des outils en ligne generent le fichier `.vtt` a partir de ta video. Tu uploades ta video, tu recuperes le fichier de sous-titres, tu corriges les erreurs eventuelles.

Pour les videos HeyGen, le script que tu as redige pour la voix off est deja ta transcription. Tu n'as qu'a le convertir en format `.vtt` avec les timecodes.

**[ECRAN — screencast TutorLMS editeur de lecon]**

[Navigation vers une lecon avec video > section sous-titres]

Dans l'editeur de lecon TutorLMS, ouvre une lecon qui contient une video. Tu trouves une section "Video Source" avec les options de la video. Cherche l'option pour ajouter des sous-titres ou captions.

Upload ton fichier `.vtt`. Si tu as des sous-titres dans plusieurs langues, tu peux en ajouter plusieurs — un par langue. Donne un label a chaque fichier : "Francais", "English", etc.

**[ECRAN — screencast front-end]**

[Montre la video cote eleve avec le bouton CC]

Cote eleve, un bouton "CC" (closed captions) apparait dans le lecteur video. L'eleve clique dessus, choisit la langue, et les sous-titres s'affichent en surimpression sur la video.

Si tu as uploade plusieurs langues, l'eleve peut basculer entre elles.

**[TRANSITION — face camera]**

Les sous-titres, c'est un effort initial qui beneficie a tous tes eleves. La recommandation schoolsWP : genere tes sous-titres automatiquement avec Whisper ou un service equivalent, corrige les erreurs, et uploade le fichier `.vtt`. Compte 15-20 minutes de travail par video de 10 minutes. Pour les formations multilingues, c'est aussi la porte d'entree vers un public international.

---

**Points cles** :
- Format : WebVTT (.vtt) — fichier texte avec timecodes
- Generation automatique : Whisper (gratuit) ou services de transcription en ligne
- Upload dans l'editeur de lecon TutorLMS, section video
- Support multi-langues (un fichier .vtt par langue)
- Cote eleve : bouton CC dans le lecteur video
- Conseil : corriger toujours les sous-titres auto-generes avant publication

**Mots cles SEO** : sous-titres TutorLMS, video captions LMS WordPress, fichier VTT TutorLMS, accessibilite video cours en ligne

---

### Lecon 14.6 — Sidebar sticky

**Duree** : 4 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast WordPress + TutorLMS
**Source** : doc tutorials/sticky-sidebar

---

**[INTRO — face camera]**

Quand un eleve fait defiler une longue lecon, la sidebar disparait vers le haut. Le curriculum du cours, le bouton "lecon suivante", la progression — tout ca devient inaccessible. La sidebar sticky resout ce probleme : elle reste visible en permanence pendant le scroll. Dans cette lecon, on l'active.

**[ECRAN — screencast front-end sans sticky]**

[Montre une lecon longue, scroll vers le bas — la sidebar disparait]

Voici le probleme en action. On est sur une lecon avec beaucoup de contenu. Quand on scroll, la sidebar avec le curriculum disparait. L'eleve doit remonter tout en haut pour naviguer vers la lecon suivante ou voir sa progression. C'est une mauvaise experience.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Settings > Design]

TutorLMS propose une option native pour rendre la sidebar sticky. Va dans Tutor LMS, Settings, puis la section Design ou Course. Cherche l'option "Sticky Sidebar" ou "Sidebar Position". Active-la.

**[ECRAN — screencast front-end avec sticky]**

[Montre la meme lecon apres activation — la sidebar suit le scroll]

Maintenant, regarde la difference. Quand tu scrolles, la sidebar reste fixee en haut de la zone visible. Le curriculum, la progression, le bouton "lecon suivante" — tout reste accessible en permanence.

**[ECRAN — screencast CSS personnalise]**

[Montre l'editeur de CSS additionnel dans WordPress]

Si l'option native n'est pas disponible dans ta version, ou si le rendu ne te convient pas, tu peux le faire en CSS. Va dans Apparence, Personnaliser, CSS additionnel. Ajoute :

```css
.tutor-course-sidebar {
    position: sticky;
    top: 80px;
}
```

La valeur `top: 80px` correspond a la marge avec le haut de la page. Ajuste-la selon la hauteur de ton header. Si ton menu fixe fait 60px, mets `top: 70px`.

**[ECRAN — screencast test responsive]**

[Montre le rendu sur mobile et tablette]

Point important : verifie le rendu sur mobile. Sur les petits ecrans, la sidebar passe generalement sous le contenu (pas a cote). Le sticky ne s'applique donc que sur desktop et tablette en mode paysage. C'est le comportement attendu — sur mobile, l'eleve scroll naturellement.

**[TRANSITION — face camera]**

La sidebar sticky, c'est un petit ajustement qui ameliore la navigation dans tes cours. C'est particulierement utile pour les lecons longues avec beaucoup de texte ou de contenu multimedia. Active-le une fois, et tous tes cours en beneficient.

---

**Points cles** :
- Sidebar sticky = la sidebar reste visible pendant le scroll
- Option native dans Tutor LMS > Settings > Design (ou Course)
- Alternative CSS : `position: sticky; top: 80px;` sur `.tutor-course-sidebar`
- Ajuster la valeur `top` selon la hauteur du header
- Fonctionne sur desktop et tablette — sur mobile, la sidebar passe sous le contenu
- Ameliore la navigation pour les lecons longues

**Mots cles SEO** : sidebar sticky TutorLMS, navigation cours TutorLMS, sidebar fixe LMS WordPress, UX cours en ligne TutorLMS

---

### Lecon 14.7 — Quiz Module 14

**Duree** : ~3 min
**Type** : Quiz TutorLMS (8 QCM)
**Passage** : 75% (6/8)

---

**Question 1** — Qu'est-ce que la Content Bank de TutorLMS ?

- A) Un systeme de paiement integre
- B) Une bibliotheque centralisee de lecons reutilisables entre cours **[BONNE REPONSE]**
- C) Un outil de creation de quiz automatise
- D) Un gestionnaire de fichiers multimedia

**Explication** : La Content Bank permet de creer des lecons autonomes, stockees dans une bibliotheque centrale, et de les importer dans n'importe quel cours.

---

**Question 2** — Quand tu importes une lecon de la Content Bank dans un cours, que se passe-t-il ?

- A) Un lien dynamique est cree — toute modification se propage automatiquement
- B) La lecon originale est deplacee dans le cours
- C) Une copie independante est creee dans le cours **[BONNE REPONSE]**
- D) La lecon est partagee en temps reel entre tous les cours

**Explication** : L'import cree une copie independante. Les modifications dans le cours ne modifient pas la version dans la Content Bank, et inversement.

---

**Question 3** — Quel shortcode affiche la grille de cours TutorLMS sur une page WordPress ?

- A) `[tutor_dashboard]`
- B) `[tutor_course]` **[BONNE REPONSE]**
- C) `[tutor_instructor_list]`
- D) `[tutor_course_search]`

**Explication** : `[tutor_course]` affiche la grille de cours avec miniatures, titres et prix. Il accepte des parametres comme `category`, `count` et `orderby`.

---

**Question 4** — Quelle syntaxe LaTeX utiliser pour afficher une formule centree en bloc dans TutorLMS ?

- A) `$formule$`
- B) `\[formule\]`
- C) `$$formule$$` **[BONNE REPONSE]**
- D) `{formule}`

**Explication** : Les doubles dollars `$$...$$` affichent la formule en bloc centre. Les simples dollars `$...$` inserent une formule en ligne dans le texte.

---

**Question 5** — Quelle est la methode recommandee par schoolsWP pour integrer un PDF dans une lecon ?

- A) Ajouter un lien externe vers le PDF
- B) Utiliser la section Attachments uniquement
- C) Utiliser le bloc "File" WordPress avec l'option "Inline Embed" active **[BONNE REPONSE]**
- D) Convertir le PDF en images et les inserer une par une

**Explication** : Le bloc File avec Inline Embed affiche un viewer PDF directement dans la lecon. L'eleve consulte le document sans quitter la page.

---

**Question 6** — Quel format de fichier est utilise pour les sous-titres video dans TutorLMS ?

- A) .srt
- B) .txt
- C) .vtt (WebVTT) **[BONNE REPONSE]**
- D) .sub

**Explication** : TutorLMS utilise le format WebVTT (.vtt), un fichier texte contenant des timecodes et le texte des sous-titres.

---

**Question 7** — Quel outil gratuit et open source peut generer automatiquement des fichiers de sous-titres ?

- A) Adobe Premiere
- B) Whisper **[BONNE REPONSE]**
- C) Canva
- D) HeyGen

**Explication** : Whisper (par OpenAI) est un outil gratuit et open source de transcription automatique qui genere des fichiers de sous-titres a partir de fichiers audio ou video.

---

**Question 8** — Que fait la propriete CSS `position: sticky` appliquee a la sidebar TutorLMS ?

- A) Elle cache la sidebar sur mobile
- B) Elle fixe la sidebar en haut de la page en permanence
- C) Elle garde la sidebar visible pendant le scroll dans sa zone parente **[BONNE REPONSE]**
- D) Elle deplace la sidebar a gauche du contenu

**Explication** : `position: sticky` maintient la sidebar visible dans la zone d'affichage pendant que l'eleve scroll le contenu de la lecon, sans la fixer de maniere absolue.

---

**Seuil de passage** : 6/8 (75%)
**Message de reussite** : Module 14 valide. Tu maitrises les outils de contenu avance de TutorLMS — Content Bank, shortcodes, LaTeX, PDF, sous-titres et sidebar sticky.
**Message d'echec** : Relis les lecons 14.1 a 14.6 avant de retenter le quiz. Concentre-toi sur les fonctionnalites de la Content Bank et les shortcodes.
