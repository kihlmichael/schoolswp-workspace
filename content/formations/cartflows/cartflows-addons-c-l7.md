# Lecon C.7 - Programme de fidelite et credits

## Metadata

- **Formation** : CartFlows Add-ons (premium - FRM-008)
- **Module** : C - Power Coupons
- **Duree cible** : 10 min (~1400 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Configurer un programme de fidelite par points avec Power Coupons, definir les regles de gain et de conversion, et comprendre l'impact sur la LTV et la retention client.

---

## Script narration

**[INTRO - face camera]**

Acquerir un nouveau client coute cinq a sept fois plus cher que de faire racheter un client existant. C'est une statistique classique du marketing, et elle reste vraie pour les boutiques WooCommerce.

Le probleme : WooCommerce n'a aucun mecanisme natif pour inciter un client a revenir. Chaque commande est traitee comme une transaction isolee. Le client achete, il recoit son produit, et tu n'as aucun levier pour le faire revenir - a part envoyer des emails promotionnels.

Power Coupons propose un systeme de points et de credits qui change la donne. Le client accumule des points a chaque achat et les convertit en remise. On va le configurer ensemble.

---

**[SECTION 1 - Le concept : points par achat]**

**[ECRAN - slide schema points → credits → remise]**

Le principe est simple. A chaque commande, le client gagne des points proportionnels au montant depense. Quand il atteint un certain seuil de points, il peut les convertir en un coupon de remise.

Exemple concret : 1 point par euro depense. Le client passe une commande de 80€, il gagne 80 points. Il passe une deuxieme commande de 45€, il gagne 45 points. Total : 125 points.

Tu as defini un seuil de conversion : 100 points = 10€ de remise. Le client a 125 points, il peut convertir 100 points en un coupon de 10€. Il lui reste 25 points pour la prochaine fois.

C'est un cercle vertueux. Plus le client achete, plus il accumule. Plus il accumule, plus il a une raison de revenir.

---

**[SECTION 2 - Configurer le programme dans Power Coupons]**

**[ECRAN - WordPress admin → Power Coupons → Loyalty Settings]**

Dans les reglages Power Coupons, va dans la section "Loyalty" ou "Fidelite".

Premiere etape : definir le taux de gain. Combien de points par euro depense ? Les valeurs courantes : 1 point par euro (simple), 2 points par euro (genereux), 0.5 point par euro (conservateur).

Commence par 1 point par euro. C'est facile a comprendre pour le client et facile a calculer pour toi.

Deuxieme etape : definir le seuil de conversion. Combien de points pour combien d'euros de remise ? Exemple : 100 points = 10€. Ca signifie que le client recoit 10% de ses achats en credit fidelite. C'est genereux mais maitrise.

Tu peux aussi definir un minimum de points pour convertir. Si tu mets 100, le client doit attendre d'avoir au moins 100 points avant de pouvoir convertir. Ca l'incite a faire plusieurs achats pour atteindre le seuil.

Troisieme etape : definir l'expiration. Les points expirent-ils ? Tu peux definir une duree - par exemple 12 mois apres le dernier achat. Ca cree de l'urgence : "Utilise tes points avant qu'ils expirent."

---

**[SECTION 3 - Affichage dans le compte client]**

**[ECRAN - front-end, page "Mon compte" WooCommerce]**

Le client voit ses points directement dans son espace "Mon compte" WooCommerce. Power Coupons ajoute une section dediee.

Il voit son solde de points actuel. L'historique de ses gains : "+80 points - commande #1234 du 15 mars". Le seuil de conversion : "100 points = 10€ de remise". Et un bouton pour convertir ses points quand le seuil est atteint.

La transparence est cle. Le client doit voir a tout moment ou il en est et combien il lui manque pour la prochaine remise. Un client qui voit "85 points sur 100" sait qu'une commande de 15€ lui suffit pour debloquer 10€ de credit.

---

**[SECTION 4 - Emails automatiques]**

**[ECRAN - reglages notifications]**

Power Coupons peut envoyer des emails automatiques a des moments cles.

Email de bienvenue : quand le client rejoint le programme de fidelite. "Tu gagnes desormais 1 point par euro depense. Accumule 100 points et recois 10€ de remise."

Email de seuil atteint : quand le client a assez de points pour convertir. "Tu as 105 points ! Convertis-les maintenant en 10€ de remise sur ta prochaine commande." Ce mail est un declencheur d'achat direct.

Email de rappel : quand les points vont expirer. "Tes 85 points expirent dans 30 jours. Passe une commande pour les utiliser." L'urgence motive l'action.

Ces emails sont configures dans les reglages de notification Power Coupons. Tu personnalises le contenu, le design, et les conditions d'envoi.

---

**[SECTION 5 - Le calcul economique]**

**[ECRAN - slide calcul LTV]**

Reprenons notre exemple. 1 point par euro, 100 points = 10€ de remise. Ca represente un retour de 10% au client.

Un client qui depense 200€ recoit 20€ de credit fidelite. Ce credit, c'est ton cout. Mais ce client est revenu pour une deuxieme, une troisieme, une quatrieme commande. Sans le programme de fidelite, il serait peut-etre reste a une seule commande.

Le calcul a faire : quel est le cout supplementaire du programme (les remises fidelite) versus le revenu supplementaire genere par les achats repetitifs ?

Si un client moyen fait 1.5 commandes sans programme de fidelite et 3 commandes avec, tu as double ta LTV. Meme en offrant 10% en credit, tu gagnes plus.

Cas pratique complet. Client sans programme : 1 commande de 80€ = 80€ de CA. Client avec programme : 3 commandes de 80€ = 240€ de CA, moins 24€ de credit fidelite utilise = 216€ de CA net. La difference est claire.

---

**[SECTION 6 - Points d'attention]**

**[ECRAN - slide conseils]**

Ne sois pas trop genereux au depart. 1 point par euro et 100 points = 10€, c'est un bon equilibre. Tu peux toujours augmenter la generosite plus tard - baisser est plus difficile sans frustrer les clients.

Communique clairement le programme. Un lien visible dans le header "Programme fidelite", une mention sur les pages produits "Gagne X points avec cet achat", une section dans les emails de confirmation de commande.

Surveille les metriques. Taux de conversion des points, frequence de retour des clients inscrits au programme, AOV des clients fidelite vs clients standards. Ces donnees te disent si le programme fonctionne.

---

**[CONCLUSION - face camera]**

Le programme de fidelite Power Coupons transforme des acheteurs ponctuels en clients reguliers. Points, credits, emails automatiques - le systeme travaille pour toi entre les commandes.

Dans la derniere lecon du module, on va configurer les remises par quantite - les paliers degressifs qui incitent le client a acheter plus en une seule commande.

---

## Notes de production

- **Visuels** : schema points → credits → remise, captures reglages Loyalty Power Coupons, page "Mon compte" avec solde de points, slide calcul LTV, slide emails automatiques
- **Donnees** : cout acquisition client vs retention (ratio 5-7x), exemple calcul LTV avec et sans programme
- **Transition** : enchaine sur LC.8 (remises par quantite)
