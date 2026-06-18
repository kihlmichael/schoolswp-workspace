# Script video - Lecon 3 : Creer un formulaire de contact pro

**Formation** : FluentForms Quick Start
**Code** : FRM-011
**Lecon** : 3/5 - Creer un formulaire de contact pro
**Duree** : 8 min (~1100 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera pour intro/conclusion, screencast complet de la creation du formulaire
**Objectif** : Creer un formulaire de contact complet (champs, anti-spam, notifications, confirmation, insertion page)

---

**[INTRO - face camera]**

On cree ton premier formulaire. Un formulaire de contact professionnel - celui que chaque site WordPress devrait avoir. A la fin de cette lecon, il sera en ligne sur ton site, avec anti-spam, notifications et message de confirmation.

**[ECRAN - screencast FluentForms → Nouveau formulaire]**

Dans FluentForms, clique sur Nouveau formulaire. On va utiliser le template "Contact Form" comme base. Selectionne-le.

Le builder s'ouvre avec un formulaire pre-rempli : nom, email, sujet, message. C'est un bon point de depart, mais on va l'ameliorer.

**[SECTION 1 - Les champs]**

**[ECRAN - screencast du builder]**

Regardons les champs un par un.

Le champ Nom. Clique dessus. Dans les options, tu vois qu'il est configure en champ simple - un seul champ pour le nom complet. C'est bien. Evite de separer prenom et nom de famille pour un formulaire de contact. Un seul champ, moins de friction.

Le champ Email. Clique dessus. Verifie que "Obligatoire" est coche. C'est le champ le plus important - sans email, tu ne peux pas repondre. FluentForms valide automatiquement le format de l'adresse email.

Le champ Sujet. Le template utilise un champ texte simple. On va le remplacer par un champ Select - un menu deroulant. Pourquoi ? Parce que ca te permet de categoriser les demandes automatiquement.

Supprime le champ sujet actuel. Dans la liste des champs a gauche, glisse un champ "Dropdown" a la place. Clique dessus pour le configurer.

Label : "Sujet de ta demande". Options : ajoute quatre choix. "Question generale", "Demande de devis", "Support technique", "Partenariat". Coche "Obligatoire".

L'avantage du dropdown : tu peux ensuite creer des notifications differentes selon le choix. Une demande de devis va a ton email commercial, un support technique va a ton email technique. On configure ca juste apres.

Le champ Message. C'est un textarea - un champ texte long. Verifie que le placeholder dit quelque chose d'utile, par exemple "Decris ta demande en quelques lignes...". Coche "Obligatoire".

**[ECRAN - screencast de l'ajout d'un champ]**

Facultatif : ajoute un champ Telephone entre l'email et le sujet. Glisse le champ "Phone" depuis la liste. Laisse-le en non obligatoire - certains visiteurs n'aiment pas donner leur numero. Mais ceux qui le font te facilitent le suivi.

Ton formulaire a maintenant cinq champs : Nom, Email, Telephone (facultatif), Sujet (dropdown), Message. C'est complet sans etre lourd.

**[SECTION 2 - Anti-spam]**

**[ECRAN - screencast des reglages anti-spam]**

Passons a la protection anti-spam. Tu as deja active le Honeypot dans les reglages globaux a la lecon precedente. C'est la premiere couche de defense - invisible pour les visiteurs, elle bloque les robots basiques.

Pour renforcer la protection, on va ajouter Cloudflare Turnstile. C'est l'alternative moderne a reCAPTCHA - plus rapide, plus respectueux de la vie privee, et gratuit.

Va dans Reglages de FluentForms, puis reCAPTCHA / hCaptcha / Turnstile. Selectionne Turnstile. Tu auras besoin d'une cle de site et d'une cle secrete - tu les obtiens sur le dashboard Cloudflare en 30 secondes. Colle les cles, enregistre.

Retourne dans ton formulaire. Ajoute le champ "Turnstile" depuis la liste des champs. Glisse-le juste avant le bouton d'envoi.

Deux couches de protection - Honeypot plus Turnstile - ca bloque 99% du spam sans embeter tes visiteurs avec un "cliquez sur tous les feux de circulation".

**[SECTION 3 - Notifications email]**

**[ECRAN - screencast de l'onglet Reglages → Notifications]**

Clique sur l'onglet Reglages en haut du builder, puis sur Notifications par email.

FluentForms a cree une notification par defaut. C'est l'email que tu recois quand quelqu'un soumet le formulaire. Verifions la configuration.

Destinataire : mets ton adresse email. Si tu veux envoyer a plusieurs personnes, separe les adresses par des virgules.

Objet : utilise les shortcodes de FluentForms pour personnaliser. Par exemple : "Nouveau message - {inputs.dropdown}" - ca affichera le sujet choisi dans le dropdown directement dans l'objet de l'email.

Corps du message : FluentForms inclut tous les champs par defaut avec le shortcode {all_data}. C'est bien pour commencer. Tu pourras personnaliser plus tard.

Expediteur : configure un "Reply-To" avec {inputs.email} - comme ca, quand tu reponds a l'email de notification, ta reponse part directement au visiteur.

**[SECTION 4 - Message de confirmation]**

**[ECRAN - screencast Reglages → Confirmation]**

Toujours dans l'onglet Reglages, va dans Confirmation. C'est ce que le visiteur voit apres avoir soumis le formulaire.

Trois options : afficher un message, rediriger vers une URL, ou les deux.

Pour un formulaire de contact, le message suffit. Ecris quelque chose de clair et rassurant : "Merci pour ton message. Je te reponds sous 24 heures.". Pas besoin de redirection.

Si tu veux aller plus loin, tu peux rediriger vers une page de remerciement dediee. L'avantage : tu peux tracker les conversions dans Google Analytics en utilisant l'URL de cette page comme objectif.

**[SECTION 5 - Inserer dans une page]**

**[ECRAN - screencast insertion bloc Gutenberg]**

Le formulaire est pret. Il faut l'inserer dans une page.

Methode recommandee : le bloc Gutenberg. Va dans Pages, ouvre ta page de contact - ou crees-en une. Dans l'editeur Gutenberg, ajoute un bloc. Cherche "Fluent Forms". Selectionne le bloc, puis choisis ton formulaire dans le menu deroulant.

C'est tout. Le formulaire s'affiche dans l'editeur et sur la page publiee.

Methode alternative : le shortcode. Dans la liste des formulaires de FluentForms, tu vois un shortcode a cote de chaque formulaire. Copie-le et colle-le dans n'importe quel bloc "Shortcode" de Gutenberg, ou dans un widget. Le shortcode ressemble a ceci : [fluentform id="1"].

Je recommande le bloc Gutenberg - c'est plus propre et tu vois l'apercu directement dans l'editeur.

**[OUTRO - face camera]**

Ton formulaire de contact est en ligne. Cinq champs, anti-spam, notification email, message de confirmation. Fais un test toi-meme - remplis le formulaire et verifie que tu recois bien l'email.

Dans la prochaine lecon, on cree le deuxieme formulaire : la capture d'email. Plus court, plus cible, et connecte a FluentCRM.

---

**Points cles** :
- 5 champs : nom, email, telephone (facultatif), sujet (dropdown), message
- Anti-spam : Honeypot (global) + Turnstile (champ dans le formulaire)
- Notification : Reply-To avec {inputs.email}, shortcode {inputs.dropdown} dans l'objet
- Confirmation : message texte clair, option redirection pour tracking
- Insertion : bloc Gutenberg (recommande) ou shortcode [fluentform id="X"]
- Tester soi-meme apres publication

**Mots cles SEO** : creer formulaire contact WordPress, FluentForms formulaire contact, anti-spam formulaire WordPress, Turnstile WordPress

---

**Notes de production** :
- Face camera : intro (15 sec) + outro (15 sec)
- Screencast principal : tout le reste (7 min 30)
- Annoter chaque clic et chaque champ avec des cercles/fleches
- Montrer le resultat final (formulaire publie sur une page) en fin de screencast
- Couper les temps morts (chargement de page, etc.)
