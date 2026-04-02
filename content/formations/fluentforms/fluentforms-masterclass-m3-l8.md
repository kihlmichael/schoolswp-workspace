# Script video — Module 3, Lecon 8 : AI Form Builder

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 3 — Formulaires avances
**Lecon** : 8/8 — AI Form Builder
**Duree** : 6 min (~900 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast demonstration AI builder
**Objectif** : Utiliser l'IA pour generer des formulaires et comprendre ses limites

---

**[INTRO — face camera]**

FluentForms a integre un generateur de formulaires par intelligence artificielle. Tu decris ce que tu veux en langage naturel, et l'IA genere les champs, la structure, et parfois meme la logique conditionnelle.

C'est seduisant. Mais est-ce que ca fonctionne vraiment ? On teste ensemble avec des cas concrets, et on voit les limites.

**[ECRAN — screencast "Acceder a l'AI Form Builder"]**

Dans le dashboard FluentForms, quand tu crees un nouveau formulaire, tu as trois options : Blank Form, Template, et AI Form Builder.

Clique sur AI Form Builder. Un champ de texte s'ouvre. C'est ton prompt — tu decris le formulaire que tu veux, et l'IA fait le reste.

**[ECRAN — screencast "Test 1 : formulaire de contact restaurant"]**

Premier test. Je tape : "Formulaire de contact pour un restaurant avec option de reservation. Champs : nom, email, telephone, date et heure de reservation, nombre de personnes, demandes speciales."

L'IA reflechit quelques secondes et genere le formulaire.

Resultat : un formulaire avec les champs Name, Email, Phone, Date Picker, Number (nombre de personnes), et Textarea (demandes speciales). Les labels sont corrects, les champs sont dans le bon ordre, le champ nombre a un minimum de 1.

C'est propre. Pour un formulaire simple, l'IA fait gagner une a deux minutes de configuration manuelle.

**[ECRAN — screencast "Test 2 : formulaire de devis photographe"]**

Deuxieme test, plus complexe. "Formulaire de devis pour un photographe. Type de prestation : portrait, mariage, evenement, corporate. Pour mariage, afficher un champ nombre d'invites et lieu. Calcul du prix : portrait 150 euros, mariage 800 euros, evenement 500 euros, corporate 400 euros. Notification au photographe et confirmation au client."

L'IA genere un formulaire avec les champs type de prestation (select), nombre d'invites, lieu, et les champs de contact.

Ce qui fonctionne : les champs sont crees, le select a les bonnes options, le formulaire est structure.

Ce qui manque : la logique conditionnelle pour afficher "nombre d'invites" et "lieu" uniquement pour le mariage n'est pas toujours configuree. Le calcul dynamique du prix n'est pas genere. Les notifications sont basiques.

L'IA cree la structure. La logique metier, c'est toi qui l'ajoutes.

**[ECRAN — screencast "Test 3 : formulaire d'inscription formation"]**

Troisieme test. "Formulaire d'inscription pour une formation en ligne. Nom, email, mot de passe, niveau actuel (debutant, intermediaire, avance), objectifs (checkboxes : maitriser WordPress, vendre des formations, automatiser son site), conditions d'utilisation a accepter."

Resultat : le formulaire est genere avec les bons types de champs. Le select pour le niveau, les checkboxes pour les objectifs, la case a cocher pour les conditions. C'est coherent.

Ce qui manque : pas de User Registration Feed configure (normal — ca necessite une configuration specifique). Pas de logique conditionnelle.

Mais la base est la en 10 secondes.

**[ECRAN — slide "Ce que l'IA fait bien"]**

Recapitulons ce que l'AI Form Builder fait bien.

La selection des types de champs. Si tu decris "email", l'IA met un champ Email. Si tu decris "date", elle met un Date Picker. Si tu decris "plusieurs options possibles", elle met des Checkbox. Le mapping type de besoin → type de champ est fiable.

La structure du formulaire. L'ordre des champs est logique. Les labels sont clairs. Les champs obligatoires sont generalement bien identifies.

La rapidite. Un formulaire de 8 champs est genere en 10 secondes. En configuration manuelle, ca prend 2 a 5 minutes.

**[ECRAN — slide "Ce que l'IA ne fait pas (encore)"]**

Maintenant, les limites.

La logique conditionnelle complexe. L'IA genere rarement des conditions afficher/masquer. Tu dois les configurer manuellement.

Les calculs dynamiques. Les formules de calcul ne sont pas generees. Tu ajoutes les champs calcules toi-meme.

Les notifications avancees. L'IA cree une notification basique, mais pas de notifications conditionnelles, pas de merge tags personnalises.

Les integrations. Pas de Post Feed, pas de User Registration, pas de connexion CRM. Tout ce qui est post-soumission est a configurer manuellement.

Le styling. Le formulaire est genere en style par defaut. La personnalisation visuelle est a faire apres.

**[ECRAN — screencast "La bonne facon d'utiliser l'AI Builder"]**

Voici comment en tirer le maximum.

Etape 1 : decris le formulaire a l'IA. Sois precis sur les champs et les options, mais n'attends pas de miracles sur la logique.

Etape 2 : l'IA genere la base. En 10 secondes, tu as 80% de la structure.

Etape 3 : tu peaufines. Tu ajoutes la logique conditionnelle, les calculs, les notifications avancees, le styling. C'est 2 a 5 minutes de configuration.

Au total : 3 minutes au lieu de 7. L'IA ne remplace pas ta competence — elle accelere la partie mecanique.

**[ECRAN — slide "Conseils pour de meilleurs prompts"]**

Pour de meilleurs resultats avec l'AI Builder :

Sois explicite sur les types de champs. "Un select avec les options A, B, C" donne un meilleur resultat que "le visiteur choisit entre A, B et C".

Nomme tes champs. "Champ email de contact" est plus precis que "il faut un email".

Decris le contexte. "Formulaire pour un photographe freelance" aide l'IA a choisir des labels et des options pertinents.

Ne surcharge pas le prompt. Un formulaire de 5 a 10 champs donne de bons resultats. Un formulaire de 25 champs avec des conditions complexes va depasser les capacites de l'IA.

**[OUTRO — face camera]**

L'AI Form Builder cree la base en 10 secondes. Toi tu peaufines en 2 minutes. C'est un accelerateur, pas un remplacement.

Et voila, le Module 3 est termine. Tu maitrises maintenant les formulaires avances : multi-step, conversationnel, calculs, upload, save and resume, creation de posts, inscription utilisateur, et l'IA.

Tu as toutes les briques pour construire n'importe quel formulaire WordPress professionnel.

---

**Points cles** :
- AI Form Builder : decrire le formulaire en langage naturel → generation automatique
- Bien fait : selection des types de champs, structure, rapidite (10 sec)
- Limites : pas de logique conditionnelle, pas de calculs, pas de notifications avancees
- Methode : IA genere 80% de la structure, tu peaufines les 20% restants
- Prompts efficaces : types de champs explicites, contexte, 5-10 champs max

**Mots cles SEO** : FluentForms AI form builder, FluentForms intelligence artificielle, creer formulaire IA WordPress, FluentForms generateur automatique

---

**Notes de production** :
- Face camera : intro (15 sec) + outro (20 sec, conclusion Module 3)
- Screencast : 3 tests en temps reel avec l'AI Builder
- Montrer ce qui est genere vs ce qui manque pour chaque test
- Montrer la correction manuelle apres generation
- Ton : honnete sur les limites, positif sur l'acceleration
