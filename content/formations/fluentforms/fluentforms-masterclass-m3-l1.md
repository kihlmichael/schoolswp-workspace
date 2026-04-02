# Script video — Module 3, Lecon 1 : Multi-step forms

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 3 — Formulaires avances
**Lecon** : 1/8 — Multi-step forms
**Duree** : 10 min (~1300 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast construction multi-step complet
**Objectif** : Creer un formulaire multi-etapes avec barre de progression et navigation

---

**[INTRO — face camera]**

Un formulaire de 15 champs sur une seule page, ca fait fuir. Le visiteur arrive, voit le mur de champs, et ferme l'onglet. Taux d'abandon : catastrophique.

La solution : decouper le formulaire en etapes. Le visiteur voit 4 ou 5 champs, repond, clique sur "Suivant", et decouvre la suite. Chaque etape est digeste. L'engagement est progressif. Et une fois qu'il a rempli la premiere etape, il a investi du temps — il va jusqu'au bout.

C'est ce qu'on construit dans cette lecon.

**[ECRAN — slide "Pourquoi le multi-step fonctionne"]**

Les donnees sont claires. Un formulaire multi-etapes obtient un taux de completion significativement superieur a un formulaire long sur une seule page. La raison psychologique : l'engagement progressif. A chaque etape completee, le visiteur s'est investi un peu plus. Abandonner apres l'etape 2 sur 3, ca lui coute psychologiquement.

C'est aussi meilleur en termes d'experience. Le visiteur ne voit que ce qui est pertinent a chaque moment. Pas de surcharge cognitive.

FluentForms Pro rend ca simple a implementer.

**[ECRAN — screencast "Creer le formulaire multi-step"]**

On va construire un formulaire de candidature emploi en 3 etapes.

Etape 1 : Informations personnelles. Etape 2 : Experience professionnelle. Etape 3 : Motivation.

Nouveau formulaire vierge : "Candidature — Poste Developeur WordPress".

J'ajoute les champs de l'etape 1 : Name, Email, Phone, Date Picker "Date de naissance".

Maintenant, le point cle. J'ajoute un champ "Step Break" depuis la sidebar — categorie Container. Ce champ cree la separation entre l'etape 1 et l'etape 2. Tout ce qui est au-dessus du Step Break = etape 1. Tout ce qui est en dessous = etape 2.

**[ECRAN — screencast "Ajouter les etapes"]**

Apres le premier Step Break, j'ajoute les champs de l'etape 2.

Select "Niveau d'experience" : Junior (0-2 ans), Confirme (3-5 ans), Senior (6+ ans).

Textarea "Experiences pertinentes" : decris tes experiences en lien avec le poste.

Checkbox "Technologies maitrisees" : PHP, JavaScript, WordPress, React, MySQL, Docker.

J'ajoute un deuxieme Step Break.

Apres, les champs de l'etape 3.

Textarea "Pourquoi ce poste t'interesse" — champ obligatoire.

File Upload "CV" — types autorises : PDF, DOC, DOCX. Taille max : 5 Mo.

File Upload "Lettre de motivation" — optionnel. Memes types.

Checkbox "J'accepte que mes donnees soient traitees dans le cadre de ce recrutement" — obligatoire. RGPD.

**[ECRAN — screencast "Configurer la barre de progression"]**

Cliquons sur le premier Step Break pour le configurer.

Tu vois les options :

Progress Bar Style : plusieurs styles disponibles.

"Progress Bar" : une barre qui se remplit progressivement. Classique et efficace.

"Steps" : des pastilles numerotees 1, 2, 3. Plus visuel.

"None" : pas d'indicateur de progression. A eviter — le visiteur a besoin de savoir ou il en est.

Je choisis "Steps" avec les labels personnalises.

Step 1 Label : "Informations". Step 2 Label : "Experience". Step 3 Label : "Motivation".

Ces labels s'affichent au-dessus du formulaire. Le visiteur sait exactement ou il en est et ce qui l'attend.

**[ECRAN — screencast "Navigation — boutons Suivant/Precedent"]**

Chaque Step Break genere automatiquement un bouton "Suivant" et un bouton "Precedent".

Tu peux personnaliser le texte des boutons. Au lieu de "Next" et "Previous", mets "Continuer" et "Retour". Ou "Etape suivante" et "Revenir".

Option importante : "Enable auto-scroll to top". Quand le visiteur clique sur Suivant, la page scroll automatiquement vers le haut du formulaire. Active-le — sinon le visiteur se retrouve au milieu de la page et ne voit pas les champs de l'etape suivante.

**[ECRAN — screencast "Validation par etape"]**

Un point crucial : la validation par etape.

Quand le visiteur clique sur "Suivant", FluentForms valide les champs de l'etape courante. Si un champ obligatoire est vide, le formulaire ne passe pas a l'etape suivante. Le visiteur voit un message d'erreur.

Ca evite que le visiteur arrive a l'etape 3 et doive revenir corriger un champ de l'etape 1.

Verifie que tes champs obligatoires sont bien marques comme "Required" dans chaque etape.

**[ECRAN — screencast "Design des indicateurs"]**

Le design de la barre de progression est personnalisable dans Input Customization.

Couleur de l'etape active, couleur de l'etape completee, couleur de l'etape a venir. Taille des pastilles, epaisseur de la barre, police des labels.

Mon conseil : utilise les couleurs de ton site. L'etape active en couleur principale, les etapes completees en vert ou en gris fonce, les etapes a venir en gris clair.

**[ECRAN — screencast "Test complet"]**

Testons le formulaire.

Etape 1 : je remplis nom, email, telephone, date de naissance. Je clique "Continuer". Le formulaire passe a l'etape 2. L'indicateur montre que l'etape 1 est completee.

Etape 2 : je choisis "Confirme", je decris mes experiences, je coche PHP et WordPress. "Continuer". Etape 3.

Etape 3 : je redige ma motivation, j'uploade mon CV en PDF. Je coche la case RGPD. "Envoyer ma candidature".

Confirmation : "Merci pour ta candidature. On te recontacte sous une semaine."

Le parcours est fluide. Trois etapes courtes au lieu d'un formulaire interminable.

**[ECRAN — screencast "Cas pratique — candidature emploi"]**

En recap : voici le formulaire complet.

3 etapes, 11 champs, une barre de progression avec labels. Validation a chaque etape. Upload de fichiers a la derniere etape. Notification au recruteur avec tous les fichiers en piece jointe. Confirmation au candidat.

Ce meme schema fonctionne pour n'importe quel formulaire long : inscription a un programme, demande de financement, onboarding client, questionnaire medical.

**[OUTRO — face camera]**

Le multi-step, c'est la difference entre un formulaire que les gens remplissent et un formulaire que les gens abandonnent. Chaque fois que ton formulaire depasse 6 ou 7 champs, pose-toi la question : est-ce que je devrais le decouper en etapes ?

Prochaine lecon : les conversational forms. L'alternative Typeform, integree dans FluentForms, pour des taux de completion encore plus eleves. A tout de suite.

---

**Points cles** :
- Multi-step : decouper un formulaire long en etapes pour reduire l'abandon
- Step Break : champ Container qui cree la separation entre les etapes
- Barre de progression : Progress Bar ou Steps avec labels personnalises
- Validation par etape : les champs obligatoires sont verifies avant de passer a la suite
- Navigation : boutons Suivant/Precedent personnalisables + auto-scroll

**Mots cles SEO** : FluentForms multi-step, formulaire multi-etapes WordPress, FluentForms barre de progression, formulaire candidature WordPress

---

**Notes de production** :
- Face camera : intro (20 sec) + outro (15 sec)
- Screencast : construction complete du formulaire 3 etapes
- Montrer la barre de progression en action (etapes qui changent de couleur)
- Montrer la validation qui bloque le passage si champ obligatoire vide
- Rythme : moderement rapide — le viewer peut suivre en parallele
