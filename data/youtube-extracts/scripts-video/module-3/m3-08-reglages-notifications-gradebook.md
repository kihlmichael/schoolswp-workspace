# Module 3 — Lecon 8 : Reglages Notifications et Gradebook
> Duree estimee : 3 min | Type : Adapte du transcript video #11

## Script de narration

[INTRO]

Dans cette lecon, on configure deux fonctionnalites complementaires : les notifications en temps reel et le carnet de notes. Deux outils qui ameliorent l'engagement de tes eleves et te donnent plus de controle sur l'evaluation.

[CONTENU]

Avant de toucher aux notifications, il faut activer l'add-on. Va dans Tutor LMS, Add-ons, et active le toggle "Notifications".

[CAPTURE ECRAN : Page Add-ons avec le toggle Notifications]

Attention : en survolant l'infobulle a cote du toggle, tu verras deux prerequis techniques. Ton site doit avoir un certificat SSL valide et l'extension PHP GMP doit etre activee sur ton hebergement. Ces deux points se configurent depuis le cPanel de ton hebergeur. Si tu ne sais pas comment faire, une recherche rapide avec le nom de ton hebergeur te donnera la procedure.

[CAPTURE ECRAN : Infobulle avec les deux prerequis (SSL + PHP GMP)]

Une fois l'add-on active, rends-toi dans Tutor LMS, Reglages, onglet Notifications.

[CAPTURE ECRAN : Menu Settings > Notifications]

Tu retrouves une liste d'evenements, chacun avec des options de notification. Pour chaque evenement, tu peux choisir entre trois modes : notification sur le site, notification push, ou les deux.

[CAPTURE ECRAN : Liste des evenements avec les selecteurs de type de notification]

Prenons un exemple concret. Active "notification sur le site" et "notification push" pour l'evenement "Inscription a un cours".

[CAPTURE ECRAN : Evenement "Course Enrolled" avec les deux options cochees]

Cote front-end, quand un eleve s'inscrit a un cours, une notification push apparait sur son ecran. Et toutes les notifications du site sont accessibles depuis l'icone en forme de cloche dans le tableau de bord.

[CAPTURE ECRAN : Notification push sur l'ecran + icone cloche dans le dashboard front-end]

Le principe est identique pour tous les autres evenements. Les notifications peuvent cibler les eleves, les instructeurs ou les administrateurs, selon l'evenement.

Passons au carnet de notes — Gradebook.

Comme pour les notifications, tu dois d'abord activer l'add-on Gradebook depuis la page Add-ons de Tutor LMS.

[CAPTURE ECRAN : Page Add-ons avec le toggle Gradebook active]

Une fois active, l'onglet Gradebook apparait dans tes reglages.

[CAPTURE ECRAN : Menu Settings > Gradebook]

Premiere option : utiliser un systeme de points au lieu de lettres pour afficher les performances des eleves. Si tu preferes voir "85/100" plutot que "B+", active ce toggle.

[CAPTURE ECRAN : Toggle systeme de points]

Tu peux activer la limite du bareme GPA. Quand c'est active, les eleves voient leur note sous la forme "3.0 sur 4.0" — ca donne un repere clair sur l'echelle de notation.

[CAPTURE ECRAN : Toggle GPA Scale Limit]

L'option suivante te permet de choisir le separateur utilise pour afficher les scores. Un detail cosmique, mais qui contribue a la lisibilite.

[CAPTURE ECRAN : Selection du type de separateur]

Et enfin, tu definis la valeur du bareme GPA. Si tu la mets a 4.0, tes eleves seront notes sur une echelle de 4. Ajuste selon le systeme de notation que tu veux utiliser.

[CAPTURE ECRAN : Champ valeur du bareme GPA]

[RECAP]

Notifications en temps reel pour garder tes eleves informes et engages, carnet de notes pour structurer l'evaluation — deux modules optionnels mais fortement recommandes des que tu as plusieurs eleves. N'oublie pas les prerequis techniques pour les notifications. Derniere lecon du module : l'authentification.

## Notes de production
- Captures ecran necessaires : activation des deux add-ons, prerequis techniques (infobulle), liste des evenements de notification, demo notification push + cloche, chaque option du Gradebook
- Points d'attention : bien insister sur les prerequis techniques (SSL + PHP GMP) — c'est la ou beaucoup d'utilisateurs bloquent
