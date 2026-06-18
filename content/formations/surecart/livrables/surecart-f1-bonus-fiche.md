---
title: SureCart - Cas pratiques et dépannage (Bonus)
version: 1.0
last_updated: 2026-06-05
---

# Cas pratiques et dépannage SureCart

Garde cette fiche comme aide-mémoire de référence rapide. Elle couvre les deux montages types du Bonus et la méthode de dépannage pas à pas.

---

## Montage type 1 : vendre une prestation de service (B.1)

- [ ] Créer le produit (SureCart, Products, Add New) : type service, sans stock ni expédition, description concrète incluant ce qui est livré et la durée.
- [ ] Fixer le prix en paiement unique (ou ajouter des frais de mise en place / un échéancier si la prestation est lourde - voir M5).
- [ ] Choisir la page de paiement : formulaire soigné (deux colonnes) ou Instant Checkout pour un lien direct (M3).
- [ ] Ajouter un champ personnalisé utile (ex. : URL du site à auditer) et la case CGV (M3).
- [ ] Personnaliser l'email de confirmation : cadrer la relation, indiquer le délai de retour et ce que le client doit transmettre (M7).
- [ ] Si client professionnel : créer une facture payable plutôt qu'un lien classique (M4).
- [ ] Tester en navigation privée : achat test, vérifier l'email reçu et le champ URL dans la commande (M1, M4).
- [ ] Nettoyer les données de test, désactiver le mode test, partager le lien.

---

## Montage type 2 : vendre un ebook ou un template numérique (B.2)

- [ ] Créer le produit : soigner la description et l'image de couverture (M2).
- [ ] Attacher le fichier en stockage sécurisé dans la section Downloads (M2). La livraison est automatique : espace client + email après l'achat.
- [ ] Activer l'Instant Checkout pour un lien direct partageable sur les réseaux et par email (M3).
- [ ] Ajouter un order bump si le produit est à petit prix (ex. : pack complémentaire à prix réduit au moment du paiement) - plan Pro requis (M6).
- [ ] Créer une page de remerciement qui explique comment accéder au fichier (M3).
- [ ] Proposer un extrait gratuit (produit à zéro euro) pour capter des leads : la séquence email pousse ensuite vers le produit payant (M2).
- [ ] Tester la livraison du fichier : téléchargement depuis l'espace client et depuis l'email de confirmation.
- [ ] Nettoyer, désactiver le mode test, partager.

---

## Dépannage : symptôme - cause probable - solution (B.3)

| Symptôme                                         | Cause probable                                    | Solution                                                                                                                                  |
| ------------------------------------------------ | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Affichage bizarre ou checkout cassé              | Cache mal configuré                               | Vider les 3 caches (navigateur, plugin de cache, Clear Account Cache dans SureCart, Settings), exclure les pages dynamiques et l'API REST |
| Boutique déconnectée (statut "disconnected")     | Plugin de sécurité a régénéré les salts WordPress | Recoller le jeton dans Settings, Connection ; ou le définir dans wp-config.php pour qu'il survive aux régénérations                       |
| Paiement qui échoue                              | Processeur mal connecté ou mauvais compte         | Settings, Payments : rafraîchir ou reconnecter le processeur, vérifier le bon compte et la bonne boutique                                 |
| Webhooks en erreur                               | Désynchronisation technique                       | Settings, Connection, Advanced Options, bouton Resync Webhooks                                                                            |
| Order bumps invisibles                           | Plan gratuit                                      | Ces leviers (M6) nécessitent le plan Pro ou Business                                                                                      |
| Apple Pay invisible                              | Mauvais navigateur, domaine ou pays               | Tester uniquement sur Safari, avec le domaine exact tel que les visiteurs le voient, dans un pays compatible                              |
| Pages Boutique/Paiement/Espace client manquantes | Suppression ou corbeille par erreur               | Vérifier la corbeille WordPress et restaurer les pages essentielles                                                                       |

### Méthode de dépannage (ordre à respecter)

1. Mettre SureCart à jour.
2. Vider les 3 caches : navigateur, plugin de cache du site, et Clear Account Cache (SureCart, Settings, bouton en haut à droite).
3. Tester sur un autre navigateur ou appareil.
4. Désactiver les autres plugins un par un, en vérifiant après chaque désactivation.
5. Si le problème touche un thème : tester avec le thème par défaut.
6. Pour un problème de paiement : reconnecter le processeur et utiliser Resync Webhooks si nécessaire.

> Règle d'or du dépannage : un changement à la fois. Tu modifies une chose, tu vérifies, puis tu passes à la suivante. C'est ainsi que tu isoles la cause sans créer de nouveaux problèmes.

---

## FAQ de départ (B.4)

| Question                                                 | Réponse courte                                                                                                                                                                      |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SureCart est-il gratuit ?                                | Oui, plan Launch gratuit avec 1,9 % de commission par transaction. Le plan Pro (abonnement) supprime cette commission. Les frais Stripe/PayPal s'appliquent dans tous les cas (M0). |
| Suis-je enfermé chez SureCart ?                          | Non. Tes données sont exportables. Si ton jeton est dans wp-config.php, une migration de site est même facilitée.                                                                   |
| Pourquoi je ne vois pas les order bumps ni les upsells ? | Ces fonctions (M6) sont réservées aux plans Pro et Business. Sur le plan gratuit, elles n'apparaissent pas. Ce n'est pas un bug.                                                    |
| Apple Pay ne s'affiche pas, pourquoi ?                   | Trois causes : pas sur Safari, domaine non validé exactement comme il s'affiche dans Stripe, ou pays non compatible.                                                                |
| Comment gérer ma TVA ?                                   | SureCart donne les outils (M4). Pour ta situation fiscale précise, consulte ton comptable.                                                                                          |

---

## La suite selon ton activité (B.5)

Le socle F1 couvre la grande majorité des besoins : prestations, produits numériques, abonnements simples. N'ajoute pas de complexité si tu n'en as pas besoin.

- **Parcours Créateurs (F2)** : si tu vends du contenu premium, un espace membre, des licences, ou si tu veux des outils de rétention avancés (Subscription Saver, dunning, montées de gamme automatiques).
- **Parcours Boutique (F3)** : si tu vends des produits physiques avec un catalogue, des variations nombreuses, de la gestion de stock, des zones d'expédition et du suivi de colis.

Tu choisis selon ce que tu vends, pas par envie de tout collecter.
