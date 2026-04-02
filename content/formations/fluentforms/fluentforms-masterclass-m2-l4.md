# Script video — Module 2, Lecon 4 : Messages de confirmation conditionnels

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 2 — Logique conditionnelle
**Lecon** : 4/7 — Messages de confirmation conditionnels
**Duree** : 6 min (~900 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast configuration confirmations
**Objectif** : Afficher un message ou rediriger vers une page differente selon les reponses

---

**[INTRO — face camera]**

Le visiteur remplit ton formulaire, clique sur "Envoyer". Que voit-il ensuite ? La plupart du temps, un message generique : "Merci, votre message a ete envoye." Pareil pour tout le monde, quelle que soit la reponse.

Avec les confirmations conditionnelles, tu personnalises ce qui se passe apres la soumission. Un message different, une redirection vers une page differente — tout depend de ce que le visiteur a repondu.

**[ECRAN — screencast "Confirmation par defaut"]**

Voyons d'abord la confirmation standard.

Dans le builder, va dans Form Settings → Confirmation Settings.

Tu as trois types de confirmation :

"Same Page" : un message s'affiche sur la meme page, a la place du formulaire. C'est le defaut.

"To a Page" : le visiteur est redirige vers une page WordPress de ton choix. Une page de remerciement, une page d'offre, un espace membre.

"To a Custom URL" : redirection vers n'importe quelle URL. Un lien Calendly, un site externe, un dashboard.

Par defaut, c'est "Same Page" avec le message "Merci pour votre soumission." On va rendre ca plus intelligent.

**[ECRAN — screencast "Cas pratique : confirmation selon le budget"]**

Prenons un formulaire de demande de devis avec un champ Radio "Budget" : moins de 5000 euros, entre 5000 et 15000 euros, plus de 15000 euros.

On veut deux comportements differents.

Si le budget est "plus de 15000 euros" : rediriger vers une page de prise de rendez-vous Calendly. Ce prospect est chaud, on veut qu'il reserve un creneau immediatement.

Si le budget est inferieur : afficher un message de remerciement classique. "Merci pour ta demande. On te recontacte sous 48h avec une proposition."

**[ECRAN — screencast "Configurer la confirmation conditionnelle"]**

Dans Form Settings → Confirmation Settings, tu vas voir un bouton "Add Confirmation" ou "Other Confirmations".

Cree une nouvelle confirmation.

Name : "Redirect gros budget".

Type : "To a Custom URL".

URL : colle ton lien Calendly.

Active la logique conditionnelle : "Budget" Equal "Plus de 15 000 euros".

Cette confirmation ne s'applique que pour les prospects a gros budget. Tous les autres voient la confirmation par defaut.

**[ECRAN — screencast "Message conditionnel sur la meme page"]**

Autre scenario. Formulaire d'inscription a un evenement. Le visiteur choisit entre "Presentiel" et "En ligne".

Confirmation 1 (defaut) : message "Same Page" — "Inscription confirmee. Tu recevras les informations d'acces par email."

Confirmation 2 (conditionnelle) : "Presentiel" → message different — "Inscription confirmee. L'evenement a lieu au 15 rue des Lilas, Paris 11e. Plan d'acces en piece jointe dans l'email de confirmation."

Meme page, mais le message change. Le participant en presentiel recoit l'adresse immediatement. Le participant en ligne recoit le lien d'acces par email.

**[ECRAN — screencast "Redirection vers des pages differentes"]**

Tu peux aussi rediriger vers des pages WordPress differentes.

Exemple : un quiz avec un champ Select "Niveau" : Debutant, Intermediaire, Expert.

Confirmation 1 : si "Niveau" = "Debutant" → redirect vers /formation-debutant/.

Confirmation 2 : si "Niveau" = "Intermediaire" → redirect vers /formation-intermediaire/.

Confirmation 3 : si "Niveau" = "Expert" → redirect vers /formation-expert/.

Chaque repondant est redirige vers le contenu adapte a son profil. C'est un entonnoir de qualification automatique.

**[ECRAN — slide "Combinaisons puissantes"]**

Les confirmations conditionnelles prennent tout leur sens quand tu les combines avec les notifications conditionnelles.

Le visiteur repond "Budget > 15 000 euros" :
- Notification : email au directeur commercial avec tous les details
- Confirmation : redirection vers Calendly pour prise de RDV

Le visiteur repond "Budget < 5 000 euros" :
- Notification : email au commercial standard
- Confirmation : message de remerciement avec delai de reponse

Deux parcours completement differents, geres par un seul formulaire. Le visiteur a l'impression d'une experience sur mesure. Toi, tu n'as rien a faire manuellement.

**[ECRAN — slide "Idees d'utilisation"]**

Quelques cas d'usage courants.

Formulaire de contact : redirection vers une FAQ si la demande est classique, vers un formulaire detaille si la demande est complexe.

Formulaire de devis : redirection vers une page de prise de RDV pour les gros budgets.

Quiz : redirection vers le contenu adapte au score ou au profil.

Inscription evenement : message avec les informations pratiques specifiques au format choisi (presentiel vs en ligne).

Enquete de satisfaction : message de remerciement avec un coupon de reduction si la note est basse (retention client).

**[OUTRO — face camera]**

La confirmation, c'est le dernier point de contact avec le visiteur. C'est ta derniere chance de l'impressionner, de le diriger vers la bonne ressource, ou de le convertir.

Ne gaspille pas ce moment avec un "Merci" generique.

Prochaine lecon : les groupes de conditions avances en version Pro. On monte en complexite. A tout de suite.

---

**Points cles** :
- Trois types de confirmation : Same Page, To a Page, To a Custom URL
- Confirmations conditionnelles : message ou redirection differente selon les reponses
- Combiner notifications conditionnelles + confirmations conditionnelles = parcours sur mesure
- Cas d'usage : devis (Calendly si gros budget), quiz (contenu adapte), evenement (infos pratiques)

**Mots cles SEO** : FluentForms confirmation conditionnelle, FluentForms redirection apres soumission, message personnalise formulaire WordPress, FluentForms conditional confirmation

---

**Notes de production** :
- Face camera : intro (15 sec) + outro (15 sec)
- Screencast : configuration des confirmations conditionnelles
- Montrer le test en preview (deux soumissions avec des reponses differentes)
- Ton : strategic — montrer la valeur business de la personnalisation
