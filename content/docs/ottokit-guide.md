# Guide Conceptuel : OttoKit dans l'écosystème schoolsWP

OttoKit (anciennement SureTriggers) est notre outil privilégié pour orchestrer et automatiser les flux de travail complexes.

## 1. Philosophie d'utilisation

La philosophie d'OttoKit est l'**intégration native sans coût d'infrastructure externe** :

*   **Remplacement de Zapier/Make** : Zapier facture au nombre d'exécutions (tâches) avec des abonnements de départ autour de 20 $/mois. OttoKit permet de réaliser la quasi-totalité des automatisations internes à l'écosystème WordPress de manière gratuite ou à un coût extrêmement compétitif.
*   **Simplicité de configuration** : Conçu spécifiquement pour l'univers WordPress, il comprend nativement les déclencheurs (triggers) et actions des plugins leaders du marché.
*   **Décharge de n8n** : Bien que schoolsWP possède une instance n8n autonome pour des scripts avancés de scraping ou d'IA, OttoKit est préféré pour toutes les intégrations simples et orientées plugins WordPress (ex: relier FluentForms à un outil externe).

## 2. Rôle dans l'écosystème

Dans notre architecture, OttoKit sert de passerelle entre les différents plugins de notre stack :

1.  **Synchronisation inter-outils** : Par exemple, lorsqu'un formulaire d'audit est soumis via FluentForms, OttoKit peut notifier l'équipe ou envoyer des données vers des outils externes de reporting.
2.  **Gestion des rôles et accès** : Automatiser l'octroi d'accès à des ressources ou services externes en fonction des actions d'un utilisateur sur le site.
3.  **Relais de Webhooks** : Capturer les signaux webhooks de services tiers pour déclencher des actions dans WordPress sans surcharger le serveur avec des requêtes PHP lourdes.

## 3. Directives d'usage pour les agents IA

*   **Privilégier OttoKit pour le simple** : Si un workflow ne concerne que des plugins WordPress (FluentForms, FluentCRM, TutorLMS), utilisez toujours les intégrations natives ou OttoKit.
*   **Réserver n8n pour le complexe** : N'utilisez l'instance n8n externe que pour les tâches nécessitant du code Python/JS complexe, de l'appel d'APIs tierces complexes (DataForSEO, etc.), ou du traitement asynchrone lourd.

*(Dernière mise à jour : 24 mai 2026)*
