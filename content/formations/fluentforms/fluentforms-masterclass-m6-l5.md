# Script video — Module 6, Lecon 5 : PDF Generator

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 6 — Quiz, surveys et analytics
**Lecon** : 5/6 — PDF Generator
**Duree** : 8 min (~1100 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast PDF feed config, slide cas d'usage
**Objectif** : Generer des PDF automatiques a partir des soumissions et les envoyer par email

---

**[INTRO — face camera]**

Chaque soumission de formulaire peut automatiquement generer un PDF professionnel. Un devis, une confirmation d'inscription, une attestation, un bon de commande. Le visiteur soumet, le PDF est cree et envoye par email — sans intervention manuelle.

FluentForms Pro inclut un generateur de PDF natif. On le configure ensemble.

**[SECTION 1 — screencast "Activer les PDF feeds"]**

Ouvre ton formulaire. Va dans Settings, PDF Feeds. Clique sur "Add PDF Feed".

Un PDF Feed, c'est une regle qui dit : "Quand ce formulaire est soumis, genere un PDF avec ce template et ces donnees."

Tu peux avoir plusieurs PDF Feeds par formulaire. Par exemple : un PDF pour le client (confirmation) et un PDF pour l'admin (fiche interne).

**[SECTION 2 — screencast "Configurer le template"]**

Le premier ecran te demande le template.

FluentForms propose des templates de base. Tu en choisis un et tu le personnalises.

Les elements configurables :

Header. Le logo de ton entreprise, le nom, les coordonnees. Ce header apparait en haut de chaque PDF.

Body. C'est le contenu du PDF. Tu selectionnes quels champs du formulaire inclure. Tu peux tous les inclure, ou en selectionner certains.

Pour un devis, tu veux : nom du client, email, type de prestation, options selectionnees, montant total.

Pour une confirmation d'inscription, tu veux : nom, email, evenement, date, creneau, montant paye.

Pour une attestation, tu veux : nom, date de la formation, mention "a suivi la formation X".

Footer. Mentions legales, conditions generales, numero de SIRET — ce qui doit apparaitre en bas du document.

**[SECTION 3 — screencast "Personnaliser le design"]**

Tu peux ajuster le design du PDF.

Police de caracteres. Choisis une police professionnelle et lisible.

Couleurs. Adapte les couleurs a ta charte graphique. Header en couleur, titres en couleur, texte en noir.

Mise en page. Format A4 ou Letter. Orientation portrait ou paysage. Marges.

Si le template de base ne te suffit pas, tu peux utiliser du HTML/CSS custom pour un design sur mesure. C'est plus avance, mais ca te donne un controle total sur le rendu.

Pour la plupart des cas, les templates par defaut avec une personnalisation basique font le travail.

**[SECTION 4 — screencast "Envoyer le PDF par email"]**

Le PDF genere, il faut l'envoyer. Deux options.

Option 1 — Piece jointe de la notification. Va dans Settings, Notifications. Dans la notification client, active l'option "Attach PDF". Selectionne le PDF Feed concerne. Le PDF sera joint a l'email de notification.

Option 2 — Lien de telechargement. Au lieu de joindre le PDF, inclus un lien de telechargement dans le corps de l'email. Le shortcode {pdf_download_link} insere le lien automatiquement.

La piece jointe est plus directe — le client recoit le PDF sans cliquer. Le lien est plus leger — l'email arrive plus vite et evite les problemes de taille de piece jointe.

Mon choix : la piece jointe pour les documents importants (devis, confirmation), le lien pour les documents complementaires.

**[SECTION 5 — slide "Cas d'usage"]**

Voici les cas ou le PDF Generator est le plus utile.

Devis automatique. Le client remplit un formulaire de devis avec ses options. Le PDF genere le recapitulatif avec les prix. Tu peux meme inclure des conditions de vente en bas du document.

Confirmation d'inscription. Le client s'inscrit a un evenement. Le PDF lui sert de billet ou de justificatif.

Attestation de formation. Apres une formation, genere un certificat avec le nom du participant, la date et l'intitule. Utile pour les formations professionnelles.

Bon de commande. Pour les achats via formulaire de paiement. Le PDF recapitule la commande — produits, quantites, montant, coordonnees.

Contrat ou engagement. Un formulaire d'adhesion genere un document PDF avec les termes acceptes et la date de signature electronique.

**[SECTION 6 — screencast "PDF conditionnel"]**

Tu peux conditionner la generation du PDF.

Exemple : tu as un formulaire de devis avec deux options — "Site vitrine" et "Site e-commerce". Tu veux generer un PDF different pour chaque option. Des templates, des textes et des conditions differents.

Cree deux PDF Feeds. Le premier avec la condition "Type de site IS Site vitrine" — template adapte au devis site vitrine. Le deuxieme avec la condition "Type de site IS Site e-commerce" — template adapte au devis e-commerce.

Seul le PDF correspondant a l'option selectionnee est genere et envoye.

**[SECTION 7 — screencast "Tester"]**

Soumets le formulaire en mode test. Verifie que le PDF est genere. Ouvre-le — les champs sont-ils correctement remplis ? Le design est-il propre ? Le logo apparait-il ?

Verifie aussi que le PDF est bien joint a l'email de notification. Ouvre la piece jointe. Tout est la ?

Si le PDF est vide ou mal formate, verifie le mapping des champs dans le PDF Feed. L'erreur la plus courante : un champ du formulaire qui n'est pas correctement reference dans le template.

**[OUTRO — face camera]**

Tu generes des PDF professionnels automatiquement. Dans la derniere lecon du module, on s'attaque aux partial entries — les soumissions partielles, l'equivalent du cart abandonment pour les formulaires.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- PDF Feed : regle de generation automatique de PDF par formulaire (Pro)
- Template : header (logo) + body (champs selectionnes) + footer (mentions legales)
- Envoi : piece jointe ou lien de telechargement dans la notification email
- PDF conditionnel : template different selon les reponses
- Cas d'usage : devis, confirmation, attestation, bon de commande, contrat
- Tester le PDF genere et l'email avant mise en production

**Mots cles SEO** : FluentForms PDF, generer PDF formulaire WordPress, PDF automatique WordPress, FluentForms PDF generator

---

**Notes de production** :
- Face camera : intro (pitch automatisation PDF) + outro (transition partial entries)
- Screencast : config PDF feed + envoi email + test (~6 min)
- Slide : 1 slide cas d'usage
- Ton : pratique, oriente resultat — montrer le PDF genere a l'ecran
