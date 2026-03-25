# Tax Settings eCommerce
> Source : https://docs.themeum.com/tutor-lms/ecommerce/tax/

## Prerequis

Activer le eCommerce natif : **Tutor LMS > Settings > Monetization** > selectionner **Native**. L'option Taxes apparait sous Monetization.

## Regional Tax Rates

### Ajouter une region

Cliquer **Add tax region** pour etablir des taux pour des zones geographiques specifiques :
- Selectionner un pays entier
- Ou selectionner des provinces individuelles

> Consulter les autorites fiscales locales pour s'assurer d'appliquer les bons taux.

### Modifier les pourcentages

1. Cliquer le bouton edit pour la region
2. Saisir le pourcentage souhaite (defaut : 0%)
3. Choisir entre un taux uniforme ou des taux par province

**Taux unique :** activer "Apply single tax rate for the entire country" pour un pourcentage uniforme sur toutes les provinces.

**Configuration par province :** desactiver l'option ci-dessus pour definir des taux individuels par province.

## Global Tax Settings

### Tax Inclusion in Prices

**"Tax is already included in my prices"** — indique que les prix incluent deja les taxes. Les prix doivent etre definis manuellement comme tax-inclusive lors de la creation du cours.

### Tax at Checkout

**"Tax calculated and displayed on the checkout page"** — la taxe apparait uniquement lors du processus de checkout.

### Display Preference

**"Display prices inclusive of tax"** — affiche le prix total apres calcul de la taxe au checkout.

## Advanced Settings

### Display Tax-Inclusive Prices Site-Wide

Quand active, les prix des cours affichent les montants TTC sur :
- Les listings de cours
- Les pages de detail des cours
- Les pages de checkout

Recommande pour les regions exigeant legalement l'affichage TTC (EU, Australie, etc.).

### Enable Tax Configuration per Course & Membership Plan

Quand active, controle individuel des taxes pour chaque cours et bundle lors de la creation/edition :
- Definir si les taxes s'appliquent a des cours specifiques
- Gerer les offres taxables et exonerees
- Supporter les ventes globales avec des exigences variables

### Appliquer la taxe dans le Course Builder

1. Aller dans **Tutor LMS > Courses**
2. Creer ou editer un cours
3. Localiser la section **Pricing** dans le panneau droit
4. Sous "Tax Collection", cocher :
   - Tax sur l'achat unique du cours
   - Tax sur l'abonnement/paiement recurrent

> Les options de taxe n'apparaissent que pour les cours payants ; les cours gratuits excluent les parametres de taxe.
