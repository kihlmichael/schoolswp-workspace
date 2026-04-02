# Script video — Module 3, Lecon 4 : Upload fichiers et images

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 3 — Formulaires avances
**Lecon** : 4/8 — Upload fichiers et images
**Duree** : 6 min (~900 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast configuration upload
**Objectif** : Configurer l'upload de fichiers de maniere securisee et fonctionnelle

---

**[INTRO — face camera]**

Formulaire de candidature avec CV. Formulaire de reclamation avec photo du defaut. Formulaire de soumission d'article avec images. Des que tu as besoin que le visiteur t'envoie un fichier, il te faut l'upload.

FluentForms Pro offre un upload de fichiers avance. On configure ca.

**[ECRAN — screencast "Champ File Upload"]**

Ajoute un champ "File Upload" depuis la sidebar. Ouvre ses settings.

Les options cles :

Max File Size : la taille maximale par fichier. Par defaut c'est 1 Mo — souvent insuffisant pour un PDF ou une image haute resolution. Monte a 5 ou 10 Mo selon le besoin. Attention : ta configuration serveur WordPress a aussi une limite (upload_max_filesize dans php.ini). FluentForms ne peut pas depasser cette limite serveur.

Max Files : le nombre de fichiers que le visiteur peut envoyer. 1 pour un CV unique, 5 pour un portfolio, 10 pour un dossier complet.

Allowed File Types : les extensions autorisees. C'est LA configuration de securite.

Pour un CV : .pdf, .doc, .docx.

Pour des images : .jpg, .jpeg, .png, .webp.

Pour des documents generaux : .pdf, .doc, .docx, .xls, .xlsx.

N'autorise JAMAIS les extensions executables : .exe, .php, .js, .bat, .sh. Un visiteur malveillant pourrait uploader un script qui s'execute sur ton serveur. Limite toujours les types a ce dont tu as besoin.

**[ECRAN — screencast "Champ Image Upload"]**

Le champ Image Upload est une variante specialisee. Il accepte uniquement les images et affiche une preview avant l'envoi.

Le visiteur voit une miniature de son image apres l'avoir selectionnee. Il peut la supprimer et en choisir une autre avant de soumettre le formulaire.

C'est ideal pour les photos de profil, les logos, les captures d'ecran. Le visiteur verifie visuellement qu'il a selectionne le bon fichier.

Les memes options de taille et de nombre s'appliquent.

**[ECRAN — screencast "Ou sont stockes les fichiers"]**

Les fichiers uploades sont stockes dans wp-content/uploads/fluentform/ sur ton serveur WordPress.

Chaque soumission a son propre sous-dossier. Les fichiers sont renommes avec un identifiant unique pour eviter les conflits de noms.

Les fichiers sont accessibles depuis le dashboard WordPress dans Fluent Forms → Entries. Tu cliques sur une soumission, tu vois les fichiers attaches, tu peux les telecharger.

Les fichiers ne sont pas publiquement accessibles par defaut — ils ne sont pas indexes et l'URL contient un hash aleatoire. Mais ce n'est pas du chiffrement. Si tu geres des documents sensibles (pieces d'identite, donnees medicales), ajoute une couche de securite supplementaire au niveau serveur.

**[ECRAN — screencast "Securite — les bonnes pratiques"]**

Quatre regles de securite pour l'upload.

Regle 1 : limite les types de fichiers. Toujours. Jamais de wildcard (*.*). Definis explicitement chaque extension autorisee.

Regle 2 : limite la taille. Un fichier de 100 Mo sur un hebergement mutualise, ca bloque tout. 5 a 10 Mo par fichier est raisonnable pour la plupart des usages.

Regle 3 : limite le nombre. Un visiteur qui uploade 50 fichiers d'un coup, c'est soit un bug, soit une attaque. 5 a 10 fichiers maximum par champ.

Regle 4 : surveille le dossier uploads. De temps en temps, verifie que le dossier fluentform/ ne grossit pas demesurement. Les fichiers s'accumulent — pense a archiver ou nettoyer les anciennes soumissions.

**[ECRAN — screencast "Cas pratique — formulaire candidature"]**

Cas pratique rapide. Formulaire de candidature avec deux uploads.

Champ 1 : "CV" — File Upload, max 1 fichier, max 5 Mo, types .pdf .doc .docx. Required.

Champ 2 : "Portfolio ou travaux" — Image Upload, max 5 fichiers, max 10 Mo chacun, types .jpg .png .pdf. Optionnel.

Dans la notification au recruteur, les fichiers sont automatiquement inclus en pieces jointes ou en liens de telechargement dans l'email.

En preview : je selectionne un PDF pour le CV. Le nom du fichier apparait. Je selectionne 3 images pour le portfolio — les miniatures s'affichent. Je soumets. Le recruteur recoit tout.

**[OUTRO — face camera]**

L'upload de fichiers, c'est simple a configurer mais critique a securiser. Limite les types, limite la taille, et surveille ton espace disque.

Prochaine lecon : Save and Resume. Le visiteur peut sauvegarder son formulaire a mi-chemin et le reprendre plus tard. Indispensable pour les formulaires longs. A tout de suite.

---

**Points cles** :
- File Upload : types autorises, taille max, nombre max de fichiers
- Image Upload : preview avant envoi, specialise images
- Stockage : wp-content/uploads/fluentform/ (sous-dossier par soumission)
- Securite : jamais d'extensions executables (.exe, .php, .js)
- Notifications : fichiers en pieces jointes ou liens de telechargement

**Mots cles SEO** : FluentForms upload fichiers, FluentForms image upload, upload securise formulaire WordPress, FluentForms file upload configuration

---

**Notes de production** :
- Face camera : intro (15 sec) + outro (10 sec)
- Screencast : configuration complete des deux types d'upload
- Montrer la preview image avant envoi
- Insister visuellement sur la configuration des types autorises (zoomer)
- Ton : securite en priorite — insister sur les limites
