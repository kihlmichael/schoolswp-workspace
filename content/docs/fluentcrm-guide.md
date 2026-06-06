# Guide Conceptuel : FluentCRM dans l'écosystème schoolsWP

FluentCRM est le moteur central de notre marketing relationnel et de l'automatisation de nos emails.

## 1. Philosophie d'utilisation

La philosophie fondamentale derrière le choix de FluentCRM sur schoolsWP repose sur l'**indépendance** et la **souveraineté des données** :

*   **Pas de taxe SaaS** : Contrairement aux plateformes comme Mailchimp, ConvertKit ou ActiveCampaign, dont le coût augmente de manière exponentielle avec le nombre d'abonnés (parfois 50 à 150 €/mois pour quelques milliers de contacts), FluentCRM fonctionne sur notre propre hébergement WordPress sans surcoût par abonné.
*   **Centralisation des données** : Toutes les informations clients (achats FluentCart, progression de cours TutorLMS, formulaires FluentForms) résident dans la même base de données. Il n'y a pas besoin de synchronisations API complexes et fragiles.
*   **Sécurité et conformité** : Vos données clients ne quittent pas votre serveur WordPress, ce qui simplifie grandement la conformité RGPD.

## 2. Rôle dans l'écosystème

FluentCRM agit comme le système nerveux de schoolsWP :

1.  **Séquences d'accueil (Welcome sequences)** : Après chaque achat sur FluentCart, une séquence automatisée s'enclenche immédiatement pour accueillir le client, lui expliquer comment accéder à TutorLMS et lui délivrer ses bonus.
2.  **Newsletter hebdomadaire** : Notre principal canal de communication avec notre communauté.
3.  **Tags et segmentation** : Les contacts sont taggués dynamiquement selon leurs intérêts (par exemple : `intérêt-seo`, `intérêt-lms`, `acheteur-novamira`) afin de leur envoyer des communications ultra-ciblées.

## 3. Stack technique associée

Pour fonctionner de manière optimale, FluentCRM est couplé à :
*   **FluentSMTP** : Pour router les emails de manière fiable vers des services externes (comme Amazon SES, Mailgun ou Postmark) afin de garantir une délivrabilité maximale (évite que nos emails finissent dans les spams).
*   **FluentCart** : Déclenche les webhooks et les tags après un achat.
*   **TutorLMS** : Permet de suivre si un utilisateur a commencé un cours et de lui envoyer des relances s'il stagne.

*(Dernière mise à jour : 24 mai 2026)*
