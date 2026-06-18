# Scripts vidéo - Module 14 : Content Bank & Shortcodes

**Formation** : Maîtriser TutorLMS
**Module** : M14 - Content Bank & Shortcodes (Premium)
**Leçons** : 6 vidéos + 1 quiz
**Durée totale** : ~30 min
**Date** : 2026-03-23

---

### Leçon 14.1 : Content Bank

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS admin
**Source** : Vidéo #38 + doc content-bank

---

**[INTRO - face caméra]**

Tu crées plusieurs cours et tu te retrouves à refaire les mêmes leçons à chaque fois ? La Content Bank de TutorLMS résout ce problème. C'est une bibliothèque centralisée où tu stockes des leçons réutilisables - une seule version, utilisable dans autant de cours que tu veux. Dans cette leçon, on met ça en place.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Settings > Content Bank]

Première étape : active la Content Bank. Va dans Tutor LMS, Settings, puis cherche l'option Content Bank. Active-la. À partir de maintenant, un nouveau menu "Content Bank" apparaît dans le menu latéral de TutorLMS.

**[ÉCRAN - screencast Content Bank]**

[Navigation vers Tutor LMS > Content Bank]

Clique sur Content Bank dans le menu. Tu arrives sur une liste vide pour l'instant. C'est ici que tu vas stocker toutes tes leçons réutilisables.

Clique sur "Add New". Tu retrouves l'éditeur classique de leçon TutorLMS - titre, contenu, vidéo, pièces jointes. La seule différence : cette leçon n'est rattachée à aucun cours. Elle existe de manière autonome dans ta bibliothèque.

Remplis ta leçon comme d'habitude. Titre, contenu texte, vidéo si besoin. Puis sauvegarde.

**[ÉCRAN - screencast Course Builder]**

[Navigation vers un cours > Course Builder > ajout de leçon depuis la Content Bank]

Maintenant, ouvre le Course Builder d'un cours. Quand tu ajoutes une nouvelle leçon à un topic, tu vois un bouton "Import from Content Bank" à côté du bouton classique "Add Lesson".

Clique dessus. La liste de tes leçons Content Bank s'affiche. Sélectionne celle que tu veux, confirme. La leçon est importée dans ton cours.

**[ÉCRAN - screencast montrant la leçon dans deux cours]**

[Ouvre deux cours différents qui partagent la même leçon]

Point important : la leçon importée est une copie indépendante. Si tu modifies la version dans le cours, ça ne change pas la version dans la Content Bank. Et inversement. C'est une copie à l'import, pas un lien dynamique.

Ça veut dire : si tu corriges une erreur dans la leçon source, tu dois réimporter dans les cours concernés. Garde ça en tête.

**[TRANSITION - face caméra]**

La Content Bank prend tout son sens quand tu as des leçons communes entre plusieurs formations. Par exemple, une leçon "Comment naviguer dans l'interface" ou "Les bases de WordPress" - tu la crées une fois, et tu l'importes partout. Pour un formateur qui gère 5 ou 10 cours, c'est un gain de temps énorme.

---

**Points clés** :
- Content Bank = bibliothèque centralisée de leçons réutilisables
- Activation dans Tutor LMS > Settings
- Création de leçons autonomes (pas rattachées à un cours)
- Import dans n'importe quel cours via le Course Builder
- L'import crée une copie indépendante (pas un lien dynamique)
- Idéal pour les leçons communes à plusieurs formations

**Mots clés SEO** : TutorLMS Content Bank, leçons réutilisables TutorLMS, bibliothèque de contenu LMS WordPress, Content Bank Tutor LMS

---

### Leçon 14.2 : Shortcodes Tutor LMS

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast WordPress + TutorLMS
**Source** : doc shortcodes

---

**[INTRO - face caméra]**

TutorLMS génère ses pages automatiquement - tableau de bord, liste de cours, panier. Mais parfois, tu veux afficher ces éléments ailleurs. Sur ta page d'accueil, dans un article, ou dans une landing page. C'est exactement le rôle des shortcodes. Dans cette leçon, on passe en revue les shortcodes TutorLMS et on les intègre dans des pages WordPress.

**[ÉCRAN - screencast WordPress éditeur]**

[Montre l'éditeur de page WordPress avec le bloc Shortcode]

Un shortcode, c'est un bout de texte entre crochets que WordPress remplace par du contenu dynamique. TutorLMS en fournit plusieurs. Pour les utiliser, ouvre n'importe quelle page dans l'éditeur WordPress, ajoute un bloc "Shortcode" et colle le code.

Premier shortcode - la liste des cours :

```
[tutor_course]
```

Ça affiche la grille de tous tes cours publiés, avec les miniatures, les titres et les prix. Tu peux l'ajouter sur ta page d'accueil pour mettre tes formations en avant.

**[ÉCRAN - screencast front-end]**

[Montre le rendu du shortcode sur la page]

Voilà le rendu. La grille de cours s'affiche exactement comme sur la page catalogue native de TutorLMS.

**[ÉCRAN - screencast WordPress éditeur]**

[Retour à l'éditeur, ajout d'autres shortcodes]

Deuxième shortcode - le tableau de bord élève :

```
[tutor_dashboard]
```

Ça affiche le dashboard complet de l'élève - cours en cours, progression, certificats. Utile si tu veux intégrer le dashboard dans une page personnalisée plutôt que la page par défaut.

Troisième shortcode - le formulaire d'inscription instructeur :

```
[tutor_instructor_registration_form]
```

Si tu acceptes les instructeurs externes, ce shortcode affiche le formulaire d'inscription. Tu peux le placer sur une page dédiée "Devenir formateur".

**[ÉCRAN - screencast avec paramètres]**

[Montre l'ajout de paramètres au shortcode]

Certains shortcodes acceptent des paramètres. Par exemple, pour afficher uniquement les cours d'une catégorie :

```
[tutor_course category="wordpress"]
```

Ou pour limiter le nombre de cours affichés :

```
[tutor_course count="6"]
```

Tu peux combiner les paramètres :

```
[tutor_course category="wordpress" count="3" orderby="date"]
```

**[ÉCRAN - screencast liste complète des shortcodes]**

[Montre la documentation TutorLMS avec la liste des shortcodes]

Voici les principaux shortcodes disponibles :

- `[tutor_course]` - grille de cours
- `[tutor_dashboard]` - tableau de bord élève
- `[tutor_instructor_registration_form]` - inscription instructeur
- `[tutor_student_registration_form]` - inscription élève
- `[tutor_instructor_list]` - liste des instructeurs
- `[tutor_course_search]` - barre de recherche de cours

La documentation TutorLMS les liste tous avec leurs paramètres.

**[TRANSITION - face caméra]**

Les shortcodes te donnent une flexibilité totale pour intégrer TutorLMS dans tes pages WordPress. La recommandation schoolsWP : utilise `[tutor_course]` sur ta page d'accueil pour afficher tes formations, et `[tutor_dashboard]` sur une page personnalisée si le design par défaut ne te convient pas. Pour tout le reste, les pages natives TutorLMS font le travail.

---

**Points clés** :
- Shortcodes = blocs dynamiques TutorLMS à insérer dans n'importe quelle page WordPress
- `[tutor_course]` - grille de cours (paramètres : category, count, orderby)
- `[tutor_dashboard]` - tableau de bord élève complet
- `[tutor_instructor_registration_form]` - formulaire inscription instructeur
- `[tutor_student_registration_form]` - formulaire inscription élève
- `[tutor_instructor_list]` - liste des instructeurs
- Utiliser le bloc "Shortcode" dans l'éditeur WordPress

**Mots clés SEO** : shortcodes TutorLMS, intégrer TutorLMS page WordPress, tutor_course shortcode, afficher cours TutorLMS page accueil

---

### Leçon 14.3 : LaTeX dans les cours

**Durée** : 4 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS éditeur
**Source** : doc tutorials/tutor-lms-latex

---

**[INTRO - face caméra]**

Tu enseignes les maths, la physique, la chimie, ou n'importe quelle matière avec des formules ? TutorLMS supporte LaTeX - le standard pour écrire des équations mathématiques propres. Dans cette leçon, on active LaTeX et on l'utilise dans les leçons et les quiz.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Settings]

Première étape : vérifie que le support LaTeX est activé. Va dans Tutor LMS, Settings, puis cherche l'option liée à LaTeX ou MathJax. TutorLMS utilise MathJax pour le rendu - c'est la bibliothèque standard qui transforme le code LaTeX en formules visuelles.

Active l'option si elle n'est pas déjà cochée.

**[ÉCRAN - screencast éditeur de leçon]**

[Navigation vers une leçon > éditeur de contenu]

Maintenant, ouvre l'éditeur d'une leçon. Pour écrire une formule LaTeX, tu utilises la syntaxe standard : entoure ta formule de doubles dollars pour un bloc centré, ou de simples dollars pour une formule en ligne.

Exemple - formule en ligne dans un paragraphe :

```
L'aire d'un cercle est $A = \pi r^2$ ou r est le rayon.
```

Exemple - formule en bloc, centrée :

```
$$E = mc^2$$
```

**[ÉCRAN - screencast front-end]**

[Montre le rendu de la formule côté élève]

Côté élève, MathJax prend le relais et affiche la formule avec un rendu typographique propre. Les fractions, les racines carrées, les intégrales - tout est supporté.

Quelques formules courantes :

- Fraction : `$\frac{a}{b}$`
- Racine carrée : `$\sqrt{x}$`
- Somme : `$\sum_{i=1}^{n} x_i$`
- Intégrale : `$\int_{0}^{1} f(x) dx$`

**[ÉCRAN - screencast éditeur de quiz]**

[Navigation vers un quiz > éditeur de question]

LaTeX fonctionne aussi dans les quiz. Quand tu crées une question, tu peux insérer des formules dans l'énoncé et dans les choix de réponse. Même syntaxe : dollars simples ou doubles.

Par exemple, pour une question de maths :

Énoncé : "Quelle est la dérivée de $f(x) = x^3$ ?"
- Choix A : $f'(x) = 3x^2$ (bonne réponse)
- Choix B : $f'(x) = 2x^2$
- Choix C : $f'(x) = x^2$

Le rendu est propre dans le quiz côté élève.

**[TRANSITION - face caméra]**

LaTeX dans TutorLMS, c'est indispensable pour les formations scientifiques. Le rendu est professionnel, la syntaxe est standard. Si tu ne connais pas LaTeX, il existe des éditeurs visuels en ligne - tape "LaTeX equation editor" dans Google, compose ta formule visuellement, et copie le code généré dans TutorLMS.

---

**Points clés** :
- TutorLMS utilise MathJax pour le rendu LaTeX
- Activation dans Tutor LMS > Settings
- Syntaxe : `$formule$` (en ligne) ou `$$formule$$` (bloc centré)
- Fonctionne dans les leçons ET dans les quiz (énoncés + réponses)
- Supporte fractions, racines, sommes, intégrales, matrices
- Éditeurs visuels en ligne disponibles pour les débutants LaTeX

**Mots clés SEO** : LaTeX TutorLMS, formules mathématiques LMS WordPress, MathJax TutorLMS, équations cours en ligne WordPress

---

### Leçon 14.4 : Embed PDF dans les leçons

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS + WordPress
**Source** : doc tutorials/embed-pdf

---

**[INTRO - face caméra]**

Tu as des supports de cours en PDF - fiches de révision, exercices, documents de référence ? Plutôt que de mettre un simple lien de téléchargement, tu peux intégrer le PDF directement dans la leçon. L'élève le consulte sans quitter la page. Dans cette leçon, on voit comment faire.

**[ÉCRAN - screencast TutorLMS éditeur de leçon]**

[Navigation vers une leçon > éditeur de contenu]

Ouvre l'éditeur d'une leçon. On a deux approches pour intégrer un PDF.

**Approche 1 : pièce jointe TutorLMS**

La plus simple. En bas de l'éditeur de leçon, tu as une section "Attachments". Clique sur "Upload", sélectionne ton PDF. L'élève verra un bouton de téléchargement en bas de la leçon.

C'est fonctionnel, mais l'élève doit télécharger le fichier pour le lire. On peut faire mieux.

**Approche 2 : embed dans le contenu**

[Montre l'ajout d'un bloc dans l'éditeur]

Pour afficher le PDF directement dans la leçon, utilise un bloc "File" dans l'éditeur WordPress. Ajoute un bloc, cherche "File", sélectionne-le. Upload ton PDF ou choisis-le depuis la médiathèque.

Dans les options du bloc, active "Inline Embed". Ça affiche un viewer PDF directement dans la page. L'élève peut faire défiler les pages, zoomer, et télécharger si besoin.

**[ÉCRAN - screencast front-end]**

[Montre le rendu côté élève avec le PDF intégré]

Voilà le rendu. Le PDF s'affiche dans un cadre intégré à la leçon. L'élève navigue entre les pages sans quitter le cours. Le bouton de téléchargement reste disponible en haut du viewer.

**[ÉCRAN - screencast éditeur]**

[Retour à l'éditeur, ajustement de la taille]

Tu peux ajuster la hauteur du viewer PDF dans les options du bloc. Par défaut, c'est souvent trop petit. Monte à 600 ou 800 pixels pour un confort de lecture correct.

**[ÉCRAN - screencast avec un plugin PDF]**

[Montre l'alternative plugin PDF Embedder]

Si le bloc natif ne te convient pas, il existe des plugins dédiés comme PDF Embedder. L'avantage : un rendu plus propre avec pagination, zoom, et un mode plein écran. L'inconvénient : un plugin supplémentaire à maintenir.

La recommandation schoolsWP : commence avec le bloc File natif. Si tu as beaucoup de PDF et que le rendu compte pour tes élèves, passe sur PDF Embedder.

**[TRANSITION - face caméra]**

L'embed PDF transforme tes leçons en vrais supports de cours. Au lieu d'un lien que personne ne clique, le document est là, visible, consultable immédiatement. C'est particulièrement utile pour les fiches de synthèse, les exercices à remplir, et les documents de référence.

---

**Points clés** :
- Approche 1 : pièce jointe TutorLMS (section Attachments) - téléchargement uniquement
- Approche 2 : bloc "File" WordPress avec "Inline Embed" activé - viewer PDF dans la page
- Ajuster la hauteur du viewer (600-800px recommandé)
- Alternative plugin : PDF Embedder (rendu supérieur, plugin supplémentaire)
- Recommandation schoolsWP : bloc File natif d'abord, plugin si besoin
- Idéal pour fiches de révision, exercices, documents de référence

**Mots clés SEO** : embed PDF TutorLMS, intégrer PDF cours en ligne, PDF dans leçon WordPress, viewer PDF LMS

---

### Leçon 14.5 : Sous-titres vidéo

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS
**Source** : doc tutorials/video-captions

---

**[INTRO - face caméra]**

Les sous-titres, c'est à la fois une question d'accessibilité et de confort. Certains élèves apprennent mieux en lisant, d'autres sont dans un environnement bruyant, et d'autres encore ne parlent pas ta langue maternelle. TutorLMS supporte les sous-titres sur les vidéos de cours. Dans cette leçon, on les ajoute.

**[ÉCRAN - screencast préparation du fichier]**

[Montre un fichier .vtt dans un éditeur de texte]

Les sous-titres utilisent le format WebVTT - un fichier texte avec l'extension `.vtt`. Voici à quoi ça ressemble :

```
WEBVTT

00:00:00.000 --> 00:00:03.000
Bienvenue dans cette leçon sur TutorLMS.

00:00:03.500 --> 00:00:07.000
Aujourd'hui, on configure les certificats.
```

Chaque bloc contient un timecode de début, un timecode de fin, et le texte à afficher. C'est simple à éditer manuellement, mais pour une vidéo de 10 minutes, ça prend du temps.

**[ÉCRAN - screencast outil de sous-titrage]**

[Montre un outil de génération de sous-titres]

La méthode rapide : utilise un outil de transcription automatique. Des services comme Whisper (gratuit, open source) ou des outils en ligne génèrent le fichier `.vtt` à partir de ta vidéo. Tu uploades ta vidéo, tu récupères le fichier de sous-titres, tu corriges les erreurs éventuelles.

Pour les vidéos HeyGen, le script que tu as rédigé pour la voix off est déjà ta transcription. Tu n'as qu'à le convertir en format `.vtt` avec les timecodes.

**[ÉCRAN - screencast TutorLMS éditeur de leçon]**

[Navigation vers une leçon avec vidéo > section sous-titres]

Dans l'éditeur de leçon TutorLMS, ouvre une leçon qui contient une vidéo. Tu trouves une section "Video Source" avec les options de la vidéo. Cherche l'option pour ajouter des sous-titres ou captions.

Upload ton fichier `.vtt`. Si tu as des sous-titres dans plusieurs langues, tu peux en ajouter plusieurs - un par langue. Donne un label à chaque fichier : "Français", "English", etc.

**[ÉCRAN - screencast front-end]**

[Montre la vidéo côté élève avec le bouton CC]

Côté élève, un bouton "CC" (closed captions) apparaît dans le lecteur vidéo. L'élève clique dessus, choisit la langue, et les sous-titres s'affichent en surimpression sur la vidéo.

Si tu as uploadé plusieurs langues, l'élève peut basculer entre elles.

**[TRANSITION - face caméra]**

Les sous-titres, c'est un effort initial qui bénéficie à tous tes élèves. La recommandation schoolsWP : génère tes sous-titres automatiquement avec Whisper ou un service équivalent, corrige les erreurs, et uploade le fichier `.vtt`. Compte 15-20 minutes de travail par vidéo de 10 minutes. Pour les formations multilingues, c'est aussi la porte d'entrée vers un public international.

---

**Points clés** :
- Format : WebVTT (.vtt) - fichier texte avec timecodes
- Génération automatique : Whisper (gratuit) ou services de transcription en ligne
- Upload dans l'éditeur de leçon TutorLMS, section vidéo
- Support multi-langues (un fichier .vtt par langue)
- Côté élève : bouton CC dans le lecteur vidéo
- Conseil : corriger toujours les sous-titres auto-générés avant publication

**Mots clés SEO** : sous-titres TutorLMS, vidéo captions LMS WordPress, fichier VTT TutorLMS, accessibilité vidéo cours en ligne

---

### Leçon 14.6 : Sidebar sticky

**Durée** : 4 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast WordPress + TutorLMS
**Source** : doc tutorials/sticky-sidebar

---

**[INTRO - face caméra]**

Quand un élève fait défiler une longue leçon, la sidebar disparaît vers le haut. Le curriculum du cours, le bouton "leçon suivante", la progression - tout ça devient inaccessible. La sidebar sticky résout ce problème : elle reste visible en permanence pendant le scroll. Dans cette leçon, on l'active.

**[ÉCRAN - screencast front-end sans sticky]**

[Montre une leçon longue, scroll vers le bas - la sidebar disparaît]

Voici le problème en action. On est sur une leçon avec beaucoup de contenu. Quand on scroll, la sidebar avec le curriculum disparaît. L'élève doit remonter tout en haut pour naviguer vers la leçon suivante ou voir sa progression. C'est une mauvaise expérience.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Settings > Design]

TutorLMS propose une option native pour rendre la sidebar sticky. Va dans Tutor LMS, Settings, puis la section Design ou Course. Cherche l'option "Sticky Sidebar" ou "Sidebar Position". Active-la.

**[ÉCRAN - screencast front-end avec sticky]**

[Montre la même leçon après activation - la sidebar suit le scroll]

Maintenant, regarde la différence. Quand tu scrolles, la sidebar reste fixée en haut de la zone visible. Le curriculum, la progression, le bouton "leçon suivante" - tout reste accessible en permanence.

**[ÉCRAN - screencast CSS personnalisé]**

[Montre l'éditeur de CSS additionnel dans WordPress]

Si l'option native n'est pas disponible dans ta version, ou si le rendu ne te convient pas, tu peux le faire en CSS. Va dans Apparence, Personnaliser, CSS additionnel. Ajoute :

```css
.tutor-course-sidebar {
    position: sticky;
    top: 80px;
}
```

La valeur `top: 80px` correspond à la marge avec le haut de la page. Ajuste-la selon la hauteur de ton header. Si ton menu fixe fait 60px, mets `top: 70px`.

**[ÉCRAN - screencast test responsive]**

[Montre le rendu sur mobile et tablette]

Point important : vérifie le rendu sur mobile. Sur les petits écrans, la sidebar passe généralement sous le contenu (pas à côté). Le sticky ne s'applique donc que sur desktop et tablette en mode paysage. C'est le comportement attendu - sur mobile, l'élève scroll naturellement.

**[TRANSITION - face caméra]**

La sidebar sticky, c'est un petit ajustement qui améliore la navigation dans tes cours. C'est particulièrement utile pour les leçons longues avec beaucoup de texte ou de contenu multimédia. Active-le une fois, et tous tes cours en bénéficient.

---

**Points clés** :
- Sidebar sticky = la sidebar reste visible pendant le scroll
- Option native dans Tutor LMS > Settings > Design (ou Course)
- Alternative CSS : `position: sticky; top: 80px;` sur `.tutor-course-sidebar`
- Ajuster la valeur `top` selon la hauteur du header
- Fonctionne sur desktop et tablette - sur mobile, la sidebar passe sous le contenu
- Améliore la navigation pour les leçons longues

**Mots clés SEO** : sidebar sticky TutorLMS, navigation cours TutorLMS, sidebar fixe LMS WordPress, UX cours en ligne TutorLMS

---

### Leçon 14.7 : Quiz Module 14

**Durée** : ~3 min
**Type** : Quiz TutorLMS (8 QCM)
**Passage** : 75% (6/8)

---

**Question 1** - Qu'est-ce que la Content Bank de TutorLMS ?

- A) Un système de paiement intégré
- B) Une bibliothèque centralisée de leçons réutilisables entre cours **[BONNE REPONSE]**
- C) Un outil de création de quiz automatisé
- D) Un gestionnaire de fichiers multimédia

**Explication** : La Content Bank permet de créer des leçons autonomes, stockées dans une bibliothèque centrale, et de les importer dans n'importe quel cours.

---

**Question 2** - Quand tu importes une leçon de la Content Bank dans un cours, que se passe-t-il ?

- A) Un lien dynamique est créé - toute modification se propage automatiquement
- B) La leçon originale est déplacée dans le cours
- C) Une copie indépendante est créée dans le cours **[BONNE REPONSE]**
- D) La leçon est partagée en temps réel entre tous les cours

**Explication** : L'import crée une copie indépendante. Les modifications dans le cours ne modifient pas la version dans la Content Bank, et inversement.

---

**Question 3** - Quel shortcode affiche la grille de cours TutorLMS sur une page WordPress ?

- A) `[tutor_dashboard]`
- B) `[tutor_course]` **[BONNE REPONSE]**
- C) `[tutor_instructor_list]`
- D) `[tutor_course_search]`

**Explication** : `[tutor_course]` affiche la grille de cours avec miniatures, titres et prix. Il accepte des paramètres comme `category`, `count` et `orderby`.

---

**Question 4** - Quelle syntaxe LaTeX utiliser pour afficher une formule centrée en bloc dans TutorLMS ?

- A) `$formule$`
- B) `\[formule\]`
- C) `$$formule$$` **[BONNE REPONSE]**
- D) `{formule}`

**Explication** : Les doubles dollars `$$...$$` affichent la formule en bloc centré. Les simples dollars `$...$` insèrent une formule en ligne dans le texte.

---

**Question 5** - Quelle est la méthode recommandée par schoolsWP pour intégrer un PDF dans une leçon ?

- A) Ajouter un lien externe vers le PDF
- B) Utiliser la section Attachments uniquement
- C) Utiliser le bloc "File" WordPress avec l'option "Inline Embed" activé **[BONNE REPONSE]**
- D) Convertir le PDF en images et les insérer une par une

**Explication** : Le bloc File avec Inline Embed affiche un viewer PDF directement dans la leçon. L'élève consulte le document sans quitter la page.

---

**Question 6** - Quel format de fichier est utilisé pour les sous-titres vidéo dans TutorLMS ?

- A) .srt
- B) .txt
- C) .vtt (WebVTT) **[BONNE REPONSE]**
- D) .sub

**Explication** : TutorLMS utilise le format WebVTT (.vtt), un fichier texte contenant des timecodes et le texte des sous-titres.

---

**Question 7** - Quel outil gratuit et open source peut générer automatiquement des fichiers de sous-titres ?

- A) Adobe Premiere
- B) Whisper **[BONNE REPONSE]**
- C) Canva
- D) HeyGen

**Explication** : Whisper (par OpenAI) est un outil gratuit et open source de transcription automatique qui génère des fichiers de sous-titres à partir de fichiers audio ou vidéo.

---

**Question 8** - Que fait la propriété CSS `position: sticky` appliquée à la sidebar TutorLMS ?

- A) Elle cache la sidebar sur mobile
- B) Elle fixe la sidebar en haut de la page en permanence
- C) Elle garde la sidebar visible pendant le scroll dans sa zone parente **[BONNE REPONSE]**
- D) Elle déplace la sidebar à gauche du contenu

**Explication** : `position: sticky` maintient la sidebar visible dans la zone d'affichage pendant que l'élève scroll le contenu de la leçon, sans la fixer de manière absolue.

---

**Seuil de passage** : 6/8 (75%)
**Message de réussite** : Module 14 validé. Tu maîtrises les outils de contenu avancé de TutorLMS - Content Bank, shortcodes, LaTeX, PDF, sous-titres et sidebar sticky.
**Message d'échec** : Relis les leçons 14.1 à 14.6 avant de retenter le quiz. Concentre-toi sur les fonctionnalités de la Content Bank et les shortcodes.
