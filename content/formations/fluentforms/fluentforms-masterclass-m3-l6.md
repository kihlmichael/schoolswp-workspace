# Script video — Module 3, Lecon 6 : Creation de posts WordPress

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 3 — Formulaires avances
**Lecon** : 6/8 — Creation de posts WordPress
**Duree** : 8 min (~1100 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast configuration Post Feed
**Objectif** : Transformer une soumission de formulaire en post, page ou CPT WordPress

---

**[INTRO — face camera]**

Et si tes visiteurs pouvaient publier du contenu directement depuis un formulaire ? Un article pour un blog collaboratif, un temoignage client, une annonce pour un repertoire, une fiche produit pour un catalogue.

FluentForms Pro permet de transformer chaque soumission en post WordPress. Le visiteur remplit le formulaire, et un article, une page ou un custom post type se cree automatiquement.

**[ECRAN — screencast "Configurer le Post Feed"]**

Ouvre un formulaire dans le builder. Va dans Form Settings → Post/CPT Feed.

Clique sur "Add Post Feed". C'est ici que tu relies les champs du formulaire aux elements d'un post WordPress.

Premiere option : "Post Type". Tu choisis le type de contenu a creer.

"Post" : un article WordPress classique.

"Page" : une page WordPress.

Ou n'importe quel Custom Post Type enregistre sur ton site. Si tu as un CPT "Temoignage", "Annonce", "Recette", "Bien immobilier" — il apparait dans la liste.

**[ECRAN — screencast "Mapper les champs"]**

Le mapping, c'est la correspondance entre les champs du formulaire et les elements du post.

Post Title : mappe vers le champ du formulaire qui contient le titre. Par exemple, le champ Text Input "Titre de l'article".

Post Content : mappe vers le champ Textarea ou Rich Text qui contient le corps du contenu. Si le visiteur utilise un champ Rich Text, le formatage (gras, listes, liens) est conserve dans le post.

Featured Image : mappe vers le champ Image Upload. L'image uploadee par le visiteur devient l'image mise en avant du post.

Post Excerpt : optionnel. Mappe vers un champ Textarea "Resume" si tu en as un.

Post Status : tu decides si le post est publie immediatement ou place en brouillon.

"Draft" : le post est cree en brouillon. Tu le relis, tu le valides, tu le publies manuellement. C'est la configuration recommandee pour un blog collaboratif — tu gardes le controle editorial.

"Pending Review" : le post est en attente de relecture. Le contributeur voit son statut, l'editeur recoit une notification.

"Publish" : le post est publie immediatement. A utiliser uniquement si tu fais confiance aux contributeurs ou si le contenu ne necessite pas de validation.

**[ECRAN — screencast "Taxonomies et meta"]**

Tu peux aussi mapper des taxonomies.

Category : mappe vers un champ Select ou Radio du formulaire. Si le visiteur choisit "Tutoriel" dans le formulaire, le post est automatiquement classe dans la categorie "Tutoriel" de WordPress.

Tags : mappe vers un champ Text Input ou Checkbox. Les tags du visiteur deviennent les tags du post.

Custom Fields (meta) : si ton CPT a des champs personnalises (via ACF, MetaBox ou natif), tu peux les mapper aussi. Le champ "Prix" du formulaire remplit le custom field "prix" du CPT.

**[ECRAN — screencast "Cas pratique — blog collaboratif"]**

Construisons un formulaire de soumission d'article pour un blog collaboratif.

Champs du formulaire :

Name "Ton nom" — sera affiche comme auteur.

Email "Ton email".

Text Input "Titre de l'article".

Select "Categorie" : Tutoriel, Avis, Guide, Actualite.

Rich Text Editor "Contenu de l'article" — le visiteur peut formater son texte.

Image Upload "Image mise en avant" — optionnel.

Textarea "Bio courte" — 2-3 lignes sur l'auteur.

Checkbox "J'autorise la publication et la modification editoriale de mon article" — obligatoire.

Post Feed configuration :

Post Type : Post.

Post Title : mappe vers "Titre de l'article".

Post Content : mappe vers "Contenu de l'article".

Featured Image : mappe vers "Image mise en avant".

Category : mappe vers "Categorie".

Post Status : Draft.

Le visiteur soumet. Un brouillon d'article est cree dans WordPress avec le titre, le contenu formate, l'image, et la categorie. L'editeur du site n'a plus qu'a relire et publier.

**[ECRAN — screencast "Notification et workflow"]**

Pour completer le workflow :

Notification au visiteur : "Merci pour ta soumission. Notre equipe va relire ton article et te tiendra informe de sa publication."

Notification a l'editeur : "Nouvel article soumis par {inputs.name}. Titre : {inputs.titre}. Connecte-toi pour le relire et le publier."

Tu peux meme ajouter un lien direct vers le brouillon dans la notification si tu utilises le merge tag {post.edit_link}.

**[ECRAN — slide "Autres cas d'usage"]**

Ce meme mecanisme fonctionne pour bien d'autres usages.

Repertoire d'entreprises : le visiteur soumet une fiche, un CPT "Entreprise" est cree avec nom, description, logo, categorie de metier.

Temoignages clients : formulaire court → CPT "Temoignage" en brouillon → tu valides et publies.

Annonces immobilieres : formulaire avec adresse, prix, photos → CPT "Bien" avec custom fields ACF.

Recettes de cuisine : formulaire avec ingredients, etapes, photo → CPT "Recette".

La cle : ton formulaire devient une interface de saisie pour tes contributeurs. Ils n'ont pas besoin d'acceder au back-office WordPress.

**[OUTRO — face camera]**

Transformer un formulaire en interface de publication, c'est ouvrir ton site aux contributions sans donner acces au dashboard. Le visiteur soumet, tu controles.

Prochaine lecon : l'enregistrement d'utilisateur. On va creer des comptes WordPress a la soumission d'un formulaire — avec connexion a TutorLMS pour l'acces aux cours. A tout de suite.

---

**Points cles** :
- Post Feed : transformer une soumission en Post, Page ou CPT
- Mapping : titre, contenu, image, categories, tags, custom fields
- Post Status : Draft (recommande), Pending Review, ou Publish
- Cas d'usage : blog collaboratif, repertoire, temoignages, annonces
- Le visiteur n'a pas besoin d'acceder au back-office WordPress

**Mots cles SEO** : FluentForms creer post WordPress, FluentForms post feed, formulaire publication article WordPress, FluentForms CPT custom post type

---

**Notes de production** :
- Face camera : intro (15 sec) + outro (15 sec)
- Screencast : configuration complete du Post Feed + cas pratique blog collaboratif
- Montrer le brouillon cree dans WordPress apres soumission
- Montrer le mapping des champs visuellement (formulaire → post)
- Ton : pratique, montrer la puissance du mecanisme
