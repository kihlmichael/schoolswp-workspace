---
title: SureCart - Après la vente : espace client, emails, CRM, analytics, affiliation et connexions (Module 7)
version: 1.0
last_updated: 2026-06-05
---

# Checklist "Outils connectés + 1er affilié"

Garde cette fiche à côté de toi pendant le Module 7. Coche chaque ligne quand c'est fait : à la fin, ton espace client est soigné, tes emails sont à ton image, tes outils sont reliés et tu as un premier affilié en place.

## Espace client

- [ ] **Page Dashboard accessible** : la page Dashboard créée automatiquement par SureCart est visible dans Pages. Elle contient les blocs abonnements, commandes et téléchargements. _(Leçon 7.1)_
- [ ] **Lien dans le menu** : Apparence, Menus, toutes les pages, Dashboard sélectionné et ajouté au menu. Tes clients s'y connectent depuis ta navigation. _(Leçon 7.1)_
- [ ] **Présentation adaptée** : les blocs sont réorganisés selon ton catalogue (retirer Téléchargements si tu n'en vends pas). Template choisi : SureCart autonome ou template par défaut (intégré à ton thème). _(Leçon 7.1)_

## Emails et notifications

- [ ] **Emails clients activés/désactivés** : SureCart, Settings, Notifications. Seuls les emails pertinents pour ton catalogue sont actifs. _(Leçon 7.2)_
- [ ] **Email de confirmation de commande personnalisé** : sujet et corps modifiés sur la plateforme (Email, Customer Emails), variables Liquid conservées, Preview et Send Test effectués. _(Leçon 7.2)_
- [ ] **Alertes propriétaire réglées** : plateforme app.surecart.com, ton nom, Notifications. Tu reçois (ou non) la notification de nouvelle commande selon ton choix. _(Leçon 7.2)_

## CRM et automatisations

- [ ] **Clients synchronisés en utilisateurs WordPress** : les intégrations (cours, CRM) nécessitent des utilisateurs WordPress. Pour des clients importés, synchronisation effectuée via Settings, Advanced, Syncing, Sync Customers. _(Leçon 7.3)_
- [ ] **Intégration CRM branchée sur le produit** : section Integrations de la fiche produit configurée. Une vente ajoute le contact dans FluentCRM avec le bon tag, qui déclenche ta séquence de bienvenue. _(Leçon 7.3)_

## Suivi analytics

- [ ] **Google Site Kit installé et actif** : plugin officiel activé, tes ventes (ajout au panier, achat) remontent dans Google Analytics. _(Leçon 7.4)_

## Affiliation

- [ ] **Programme d'affiliation activé** : Settings, Affiliates, candidatures activées, description du programme rédigée, approbation manuelle choisie, commission fixée. URL d'inscription récupérée. _(Leçons 7.5 et 7.6)_
- [ ] **Premier affilié approuvé** : SureCart, Affiliates, Requests, demande approuvée. L'affilié a reçu son email de finalisation et accède à son portail. _(Leçon 7.6)_
- [ ] **Coupon d'apporteur créé** : SureCart, Coupons, Add New, remise définie, affilié lié via Link to Affiliate. _(Leçon 7.6)_

## Abilities (optionnel)

- [ ] **Permissions MCP réglées** : Settings, MCP. Interrupteur principal configuré. Autorisation de suppression désactivée sauf besoin avéré. _(Leçon 7.7)_

---

## Mémo technique

### Deux familles d'emails à bien distinguer

| Famille              | Destinataire | Où les régler                                                                      |
| -------------------- | ------------ | ---------------------------------------------------------------------------------- |
| Emails clients       | Ton acheteur | SureCart, Settings, Notifications (activer/désactiver) puis Edit sur la plateforme |
| Alertes propriétaire | Toi          | app.surecart.com, ton nom, Notifications                                           |

> Règle d'or : la langue des emails se règle dans Store Settings, Store Language. Vérifie-la si tes emails partent en anglais alors que ta boutique est en français. _(Leçon 1.6)_

### Variables Liquid dans les emails

Les variables entre doubles accolades insèrent du contenu dynamique. Exemples courants :

```
{{ order.first_name }}          → prénom de l'acheteur
{{ product.name }}              → nom du produit acheté
{{ store.name }}                → nom de ta boutique
{{ order.first_name | capitalize }} → prénom avec majuscule
```

Trois boutons à connaître dans l'éditeur d'email sur la plateforme :

- **Preview** : voir le rendu avant envoi
- **Send Test** : t'envoyer un email d'essai avec de vraies données
- **Revert to Default** : revenir au modèle d'origine si tu t'es trompé

### Le modèle headless de SureCart

SureCart est headless : les données clients vivent dans le cloud SureCart, pas dans ta base WordPress. C'est ce qui garde ton site léger. Mais pour que tes intégrations fonctionnent (donner accès à un cours, pousser un contact dans ton CRM), tes clients doivent exister comme utilisateurs WordPress.

À l'achat, l'utilisateur WordPress est créé automatiquement. Pour des clients importés depuis un autre outil, synchronise manuellement via Settings, Advanced, Syncing, Sync Customers.

### Schéma vente vers séquence CRM

```
Vente (ou produit gratuit)
  └─> Contact créé dans FluentCRM
        └─> Tag ajouté (ex. "acheteur-formation-x")
              └─> Séquence de bienvenue déclenchée
```

SureCart encaisse et enregistre. Ton CRM prend le relais sur la relation.

### Suivi analytics : commence simple

| Besoin                                        | Outil                                     |
| --------------------------------------------- | ----------------------------------------- |
| Voir tes ventes dans GA (ajout panier, achat) | Google Site Kit                           |
| Suivre la vue produit, le début de checkout   | Google Tag Manager + balise GA4           |
| Pixel Facebook, outils tiers                  | Tag Manager ou code sur événement d'achat |

> N'ajoute Tag Manager et le Pixel que si tu fais de la publicité ou que tu as besoin d'un suivi précis. Commence simple.

### Affiliation : les deux limites honnêtes

> Deux points à connaître avant de promettre quoi que ce soit à tes affiliés.
>
> 1. Les paiements sont manuels : SureCart prépare la liste (Payouts), mais tu règles tes affiliés toi-même, en dehors de la plateforme.
> 2. Seules les vraies ventes sont suivies : tes achats de test ne sont pas comptés en affiliation. Pense-y quand tu valides ton installation.

### Garde-fous des Abilities (pilotage IA)

Trois permissions dans Settings, MCP :

1. **Interrupteur principal** : autorise ou non l'accès de l'IA à ta boutique.
2. **Créer et modifier** : l'IA peut créer des coupons, des factures, prolonger des abonnements.
3. **Supprimer** : la permission la plus sensible. N'active-la que si tu en as vraiment besoin, et demande toujours confirmation à l'IA avant toute action destructive.

```
Exemple de demande précise à l'IA :
"Trouve l'abonnement actif de contact@exemple.fr
et repousse son renouvellement de 7 jours.
Confirme avant d'agir."
```

> Règle d'or : sois précis (email du client, nom exact du produit, dates au bon format). Décris le but, pas chaque étape. Pour toute action sensible, demande confirmation avant qu'elle s'exécute.

---

## Quatre voies pour connecter SureCart à tes outils

| Voie                                        | Pour qui                            | Sans code ?      |
| ------------------------------------------- | ----------------------------------- | ---------------- |
| Intégrations produit (section Integrations) | Inscription cours, alimentation CRM | Oui              |
| Événements (signaux émis à chaque action)   | Écouter depuis un outil tiers       | Généralement non |
| Webhooks (données vers une adresse externe) | Relier un service tiers             | Non              |
| API (sur-mesure)                            | Développements custom               | Non              |

Pour démarrer, les intégrations produit suffisent. Les trois autres voies sont utiles quand tu as des besoins spécifiques, et relèvent souvent d'un développeur.
