# Script video — Module 1, Lecon 3 : Les 35+ types de champs

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 1 — Fondations
**Lecon** : 3/6 — Les 35+ types de champs
**Duree** : 10 min (~1400 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast avec tour des champs par categorie
**Objectif** : Connaitre l'existence de chaque type de champ pour savoir quoi utiliser selon le besoin

---

**[INTRO — face camera]**

FluentForms propose plus de 35 types de champs. Tu n'utiliseras jamais les 35 dans un seul formulaire. Mais connaitre leur existence, ca te donne des idees. Ca t'evite de bricoler un workaround quand un champ natif fait exactement ce dont tu as besoin.

On va les passer en revue par categorie. Je ne vais pas m'attarder sur chaque champ — je vais te montrer ce qu'il fait et quand l'utiliser.

**[ECRAN — screencast "Categorie General"]**

Commencons par les champs General. C'est ta base quotidienne.

Name : champ nom prenom. Deux sous-champs par defaut (prenom et nom), tu peux en ajouter d'autres comme un titre ou un second prenom.

Email : champ email avec validation automatique. FluentForms verifie que le format est correct — pas besoin d'ajouter un regex a la main.

Text Input : champ texte simple, une seule ligne. Pour un numero de commande, un sujet, un code promo — tout ce qui est court.

Textarea : champ texte multi-lignes. Pour les messages, les descriptions, les commentaires. Tu peux definir le nombre de lignes visibles et une limite de caracteres.

Select : menu deroulant. Le visiteur choisit une option parmi une liste. Ideal pour un type de projet, un departement, une categorie.

Radio Button : choix unique avec boutons visibles. La difference avec le select : toutes les options sont affichees d'un coup. Utilise le radio quand tu as 2 a 5 options.

Checkbox : choix multiples. Le visiteur peut cocher plusieurs cases. Pour des fonctionnalites souhaitees, des centres d'interet, des services complementaires.

Number : champ numerique. Accepte uniquement des chiffres. Tu peux definir un minimum, un maximum, et un pas d'incrementation.

Date Picker : selecteur de date. Calendrier integre. Tu configures le format (jour/mois/annee ou mois/jour/annee), les dates min et max.

File Upload : upload de fichier. En gratuit, c'est basique — un fichier a la fois. En Pro, tu as l'upload multiple, le controle des types de fichiers, et la preview.

**[ECRAN — screencast "Categorie Advanced"]**

Les champs Advanced. C'est la que FluentForms se demarque.

Hidden Field : champ invisible pour le visiteur. Tu y mets des donnees automatiques : URL de la page, source UTM, ID utilisateur, IP. C'est essentiel pour le tracking sans rien demander au visiteur.

Section Break : separateur visuel entre deux sections du formulaire. Un titre et une description optionnelle. Ca structure les formulaires longs.

Custom HTML : tu inseres du HTML libre dans le formulaire. Un bandeau d'information, un avertissement, une image, un lien — tout ce que les champs standard ne couvrent pas.

Rich Text Editor : un editeur de texte complet avec mise en forme — gras, italique, listes. Le visiteur peut formater sa reponse. Utile pour les soumissions d'articles ou les descriptions detaillees.

Ratings : etoiles de notation. 1 a 5 etoiles par defaut, configurable. Pour les avis, les evaluations, les enquetes de satisfaction.

Net Promoter Score : le classique NPS de 0 a 10. "Recommanderiez-vous ce service ?" Un champ dedie avec l'echelle standard.

Repeat Field : un groupe de champs que le visiteur peut dupliquer. Par exemple, ajouter plusieurs participants a un evenement, plusieurs produits a une commande. Il clique sur "Ajouter" et un nouveau jeu de champs apparait.

Range Slider : un curseur que le visiteur fait glisser. Pour un budget, une note, un niveau. Plus visuel qu'un champ numerique.

Color Picker : selecteur de couleur. Cas d'usage rare mais utile : commande personnalisee, choix de theme, preferences visuelles.

Phone : champ telephone avec code pays automatique et masque de saisie. Le visiteur choisit son pays, le prefixe s'adapte.

**[ECRAN — screencast "Categorie Payment"]**

Les champs Payment. Disponibles en Pro pour l'experience complete.

Payment Item : un produit ou service avec un prix. Tu definis le nom, le montant, et le type (fixe, select, checkbox). C'est la base de tout formulaire de paiement.

Subscription : paiement recurrent. Mensuel, annuel, personnalise. Connecte a Stripe, le visiteur souscrit un abonnement directement depuis le formulaire.

Coupon : champ code promo. Le visiteur entre un code, la remise s'applique automatiquement au total. Tu crees les codes dans les settings du formulaire.

Quantity : selecteur de quantite. Le visiteur choisit combien d'unites il veut. Le prix total se recalcule automatiquement.

**[ECRAN — screencast "Categorie Container"]**

Les champs Container. Ils structurent le formulaire.

Multi-Column : tu organises tes champs en colonnes. Deux colonnes, trois colonnes — tu decides. Ca permet de mettre le prenom a gauche et le nom a droite, par exemple. Le formulaire prend moins de place verticale.

Step Break : le separateur de page pour les formulaires multi-etapes. Tu places un Step Break, et tout ce qui est en dessous passe a l'etape suivante. Tu personnalises le label de chaque etape et la barre de progression.

**[ECRAN — slide "Recapitulatif par usage"]**

Recapitulons autrement — par besoin concret.

Tu veux un formulaire de contact : Name + Email + Select (sujet) + Textarea + Submit. Cinq champs, c'est fait.

Tu veux un formulaire de devis : Name + Email + Select (type de projet) + Checkbox (options) + Range Slider (budget) + Textarea + Payment Item. Avec de la logique conditionnelle par-dessus.

Tu veux un sondage : Radio + Checkbox + Ratings + NPS + Textarea. Tout en multi-step pour ne pas noyer le visiteur.

Tu veux un formulaire d'inscription evenement : Name + Email + Number (places) + Select (menu) + Date + Payment + Coupon.

Les champs sont des briques. A toi de les assembler selon ton objectif.

**[OUTRO — face camera]**

Tu as maintenant une vue d'ensemble complete de ce que FluentForms met a ta disposition. Tu n'as pas besoin de tout retenir — cette lecon est la pour que tu puisses y revenir quand tu te demandes "est-ce qu'il existe un champ pour ca ?"

La reponse est presque toujours oui.

Dans la prochaine lecon, on configure les notifications email. Parce qu'un formulaire sans email de confirmation, c'est un lead perdu. A tout de suite.

---

**Points cles** :
- General : Name, Email, Text, Textarea, Select, Radio, Checkbox, Number, Date, File Upload
- Advanced : Hidden Field, Section Break, Custom HTML, Rich Text, Ratings, NPS, Repeat Field, Range Slider, Color Picker, Phone
- Payment : Payment Item, Subscription, Coupon, Quantity
- Container : Multi-Column, Step Break
- Penser par besoin concret, pas par liste de champs

**Mots cles SEO** : FluentForms types de champs, FluentForms champs avances, FluentForms payment fields, formulaire WordPress champs

---

**Notes de production** :
- Face camera : intro (20 sec) + outro (20 sec)
- Screencast : montrer chaque champ rapidement dans le builder (2-3 sec par champ)
- Zoomer sur les champs moins connus (NPS, Repeat Field, Hidden Field)
- Rythme soutenu — c'est un tour d'horizon, pas un tutoriel detaille par champ
