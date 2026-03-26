# Module 3 — Lecon 6 : Reglages Email
> Duree estimee : 3 min 30 | Type : Adapte du transcript video #09

## Script de narration

[INTRO]

Les emails automatiques sont essentiels pour ta plateforme de formation. Inscription confirmee, cours termine, devoir note — chaque evenement peut declencher un email. Dans cette lecon, on configure les templates et les regles d'envoi.

[CONTENU]

Rends-toi dans Tutor LMS, Reglages, onglet Email.

[CAPTURE ECRAN : Menu Settings > Email]

On commence par la configuration globale. Tu peux uploader un logo qui apparaitra en haut a gauche de chaque email envoye par Tutor LMS. Par defaut, c'est le logo Tutor LMS — remplace-le par le logo de ta plateforme.

[CAPTURE ECRAN : Upload du logo email et apercu dans un template]

Tu regles la hauteur du logo en pixels. Ajuste pour que ca reste proportionnel.

[CAPTURE ECRAN : Champ hauteur du logo]

Tu peux desactiver la banniere qui accompagne chaque email. Si tu veux un email plus sobre, desactive-la.

[CAPTURE ECRAN : Toggle banniere email]

Ensuite, tu definis le nom de l'expediteur — c'est ce que tes eleves verront dans leur boite de reception — et l'adresse email d'envoi. Utilise une adresse professionnelle, pas une adresse generique.

[CAPTURE ECRAN : Champs nom d'expediteur et adresse email]

Le texte du pied de page est personnalisable. Ajoute tes informations legales ou un message de contact.

[CAPTURE ECRAN : Champ footer email]

Passons aux notifications par email. Tu trouves une longue liste de toggles organises en trois categories : emails pour les eleves, emails pour les instructeurs, et emails pour les administrateurs.

[CAPTURE ECRAN : Vue d'ensemble des trois categories de toggles]

Chaque toggle correspond a un evenement precis. Par exemple : "Devoir note" — en l'activant, l'eleve recoit un email quand son devoir est corrige. "Cours publie" — l'admin est notifie quand un instructeur publie un cours. Active ceux qui sont pertinents pour ton fonctionnement.

[CAPTURE ECRAN : Exemples de toggles actives dans chaque categorie]

Le vrai point fort, c'est l'editeur de templates email. Clique sur n'importe quel template pour le personnaliser.

[CAPTURE ECRAN : Clic sur le template "Course Enrolled"]

L'editeur se presente en deux parties. A gauche, tu modifies le contenu. A droite, tu vois en temps reel a quoi ressemblera l'email. C'est dynamique — chaque modification se repercute instantanement.

[CAPTURE ECRAN : Editeur de template avec volet gauche (edition) et volet droit (apercu)]

Tu peux modifier le sujet de l'email, le titre, et le corps du message. Le contenu pre-rempli utilise des variables dynamiques — par exemple, le nom du cours s'insere automatiquement. Tu peux reformuler le texte tout en conservant ces variables.

[CAPTURE ECRAN : Modification du heading avec apercu en temps reel]

Une fois satisfait, clique sur Enregistrer les modifications. Cet email sera envoye a chaque fois qu'un eleve s'inscrit a un cours.

[CAPTURE ECRAN : Bouton Save Changes]

Derniere section : le cron WordPress pour les envois en masse. Si tu as beaucoup d'eleves et que tu veux envoyer des emails par lots, active cette option.

[CAPTURE ECRAN : Section WP Cron pour bulk email]

Tu configures la frequence en secondes — par defaut, 300 secondes, soit 5 minutes. Et tu definis combien d'emails sont envoyes a chaque execution. Par exemple, si tu as 50 emails a envoyer avec 10 emails par execution toutes les 5 minutes, le tout sera traite en 25 minutes.

[CAPTURE ECRAN : Champs frequence et emails par execution]

[RECAP]

Les reglages email couvrent l'identite visuelle de tes messages, les notifications automatiques par evenement, et un editeur de templates tres intuitif. Prends le temps de personnaliser au moins les emails les plus courants : inscription, fin de cours, devoir note. Prochaine lecon : les certificats.

## Notes de production
- Captures ecran necessaires : configuration globale (logo, nom, adresse), liste des toggles par categorie, editeur de template en split view, modification en temps reel, section WP Cron
- Points d'attention : montrer l'editeur de template en action avec la modification en direct — c'est le moment le plus parlant de cette lecon
