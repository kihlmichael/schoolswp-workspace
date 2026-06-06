# Script video - Module 3, Lecon 7 : Enregistrement utilisateur

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 3 - Formulaires avances
**Lecon** : 7/8 - Enregistrement utilisateur
**Duree** : 8 min (~1100 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast configuration User Registration Feed
**Objectif** : Creer des comptes WordPress automatiquement a la soumission d'un formulaire

---

**[INTRO - face camera]**

Tu veux que les visiteurs puissent s'inscrire sur ton site ? Creer un compte, acceder a un espace membre, suivre des cours sur TutorLMS ?

Le formulaire d'inscription par defaut de WordPress est minimaliste : username, email, mot de passe. Pas de champs personnalises, pas de design, pas de logique.

FluentForms Pro te permet de creer un formulaire d'inscription complet qui genere un compte WordPress a la soumission. Avec les champs que tu veux, le design que tu veux, et le role que tu veux.

**[ECRAN - screencast "Configurer le User Registration Feed"]**

Ouvre ton formulaire dans le builder. Va dans Form Settings → User Registration Feed.

Clique sur "Add User Registration Feed".

Un panneau de configuration s'ouvre. C'est ici que tu relies les champs du formulaire aux donnees du compte WordPress.

**[ECRAN - screencast "Mapper les champs utilisateur"]**

Les champs obligatoires :

Username : mappe vers un champ Text Input "Nom d'utilisateur" ou vers le champ Email (l'email comme identifiant, c'est plus simple pour les utilisateurs).

Email : mappe vers le champ Email du formulaire.

Password : mappe vers un champ Password du formulaire. FluentForms a un champ Password dedie avec confirmation (le visiteur tape deux fois son mot de passe). Utilise-le.

Les champs optionnels :

First Name : mappe vers le champ prenom.

Last Name : mappe vers le champ nom.

Website : si pertinent, mappe vers un champ URL.

**[ECRAN - screencast "Role et options"]**

User Role : le role WordPress attribue au nouveau compte.

"Subscriber" : le role par defaut. Acces au profil, lecture du contenu restreint. C'est le role adapte pour un espace membre ou un LMS.

"Contributor" : peut ecrire des brouillons d'articles mais pas les publier. Pour un blog collaboratif.

"Author" : peut ecrire et publier. A utiliser avec precaution - donner la publication directe a un nouveau venu est risque.

N'attribue JAMAIS les roles Editor ou Administrator via un formulaire public. C'est une faille de securite majeure.

Options supplementaires :

"Login After Registration" : le visiteur est automatiquement connecte apres la soumission. Experience fluide - il s'inscrit et il est immediatement dans son espace.

"Send Default WordPress Registration Email" : envoie l'email standard WordPress avec les identifiants. Combine avec ta propre notification FluentForms pour un double filet.

"Enable User Activation" : le compte est cree mais inactif tant que le visiteur n'a pas clique sur un lien de confirmation dans l'email. Anti-spam et anti-comptes fantomes.

**[ECRAN - screencast "Cas pratique - inscription espace membre"]**

Construisons un formulaire d'inscription pour un espace membre.

Champs :

Name (prenom + nom).

Email.

Password (avec confirmation).

Select "Comment as-tu entendu parler de nous ?" : Google, Reseaux sociaux, Bouche a oreille, Autre.

Checkbox "J'accepte les conditions d'utilisation et la politique de confidentialite" - obligatoire. Avec un lien vers les pages correspondantes dans le label (via Custom HTML ou help text).

User Registration Feed :

Username : mappe vers Email (l'email comme identifiant).

Email : mappe vers Email.

Password : mappe vers Password.

First Name : mappe vers le prenom du champ Name.

Last Name : mappe vers le nom du champ Name.

Role : Subscriber.

Login After Registration : active.

User Activation : active.

Notification au visiteur : "Bienvenue sur schoolsWP. Clique sur le lien ci-dessous pour activer ton compte et acceder a ton espace membre."

Notification admin : "Nouvel utilisateur inscrit : {inputs.name} - {inputs.email}."

**[ECRAN - screencast "Connecter avec TutorLMS"]**

Si tu utilises TutorLMS pour vendre des formations, la connexion est directe.

TutorLMS utilise le systeme de comptes WordPress. Quand FluentForms cree un compte avec le role "Subscriber", TutorLMS le reconnait automatiquement comme un etudiant potentiel.

Le parcours :

1. Le visiteur remplit le formulaire d'inscription FluentForms.
2. Un compte WordPress est cree (role Subscriber).
3. Le visiteur est connecte automatiquement.
4. Il accede au catalogue TutorLMS et peut s'inscrire a des cours.

Si tu veux aller plus loin, tu peux ajouter un champ de paiement dans le formulaire et declencher l'inscription automatique a un cours specifique apres paiement. Ca demande un webhook ou une integration supplementaire, mais le systeme de base fonctionne nativement.

**[ECRAN - slide "Securite de l'inscription"]**

L'inscription utilisateur est un point sensible. Quelques regles.

Toujours activer l'User Activation. Sans validation par email, les bots creent des centaines de faux comptes.

Ajouter Cloudflare Turnstile ou un captcha. Double protection anti-bot.

Ne jamais proposer un role superieur a Subscriber sur un formulaire public. Les roles avec des privileges d'ecriture ou d'administration sont attribues manuellement par un admin.

Limiter les soumissions par IP. Meme regle que pour l'anti-spam : 2 ou 3 inscriptions par IP par jour, maximum.

Surveiller les inscriptions. Regarde regulierement la liste des nouveaux comptes. Des inscriptions massives avec des emails suspects (sequences aleatoires, domaines jetables) sont un signe de spam. Nettoie rapidement.

**[OUTRO - face camera]**

Le formulaire d'inscription FluentForms remplace le formulaire WordPress natif par quelque chose de professionnel, personalise et securise. Combine avec TutorLMS, c'est le point d'entree de tout ton systeme de formation.

Derniere lecon du Module 3 : l'AI Form Builder. Tu decris ton formulaire en langage naturel, et l'IA le genere pour toi. On voit ce que ca vaut en pratique. A tout de suite.

---

**Points cles** :
- User Registration Feed : cree un compte WordPress a la soumission
- Mapping : username, email, password, first/last name, role
- Role Subscriber pour les formulaires publics - jamais Editor ou Admin
- Login After Registration + User Activation = experience fluide et securisee
- Integration native TutorLMS via le systeme de comptes WordPress
- Anti-spam : captcha + limitation IP + activation par email

**Mots cles SEO** : FluentForms inscription utilisateur, FluentForms user registration, formulaire inscription WordPress, FluentForms TutorLMS integration

---

**Notes de production** :
- Face camera : intro (15 sec) + outro (15 sec)
- Screencast : configuration complete du User Registration Feed
- Montrer le compte cree dans le dashboard WordPress apres soumission
- Montrer la connexion avec TutorLMS (acces au catalogue de cours)
- Ton : securite en priorite - insister sur les bonnes pratiques
