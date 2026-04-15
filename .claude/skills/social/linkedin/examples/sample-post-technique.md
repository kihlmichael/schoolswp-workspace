# Exemple — Post LinkedIn technique WordPress

**Auteur** : Michael KIHL
**Ton** : vouvoiement, professionnel, technique accessible
**Sujet** : optimisation des performances WordPress

---

## Post LinkedIn

74 % des sites WordPress chargent en plus de 3 secondes. Le votre aussi, probablement.

J'ai reduit le temps de chargement d'un site e-commerce WordPress de 4.8s a 1.2s. Sans changer d'hebergeur. Sans plugin de cache premium.

Voici les 3 actions qui ont fait 80 % du resultat :

1. Desactiver les scripts inutiles sur les pages ou ils ne servent pas. WooCommerce charge ses assets JavaScript sur toutes les pages — meme celles sans produit. Un simple `wp_dequeue_script` conditionnel a retire 340 Ko de JS inutile du chargement initial.

2. Passer les images en WebP avec chargement differe. WordPress 6.9 gere nativement le format WebP a l'upload. Combiné avec `loading="lazy"` sur les images below-the-fold (deja actif par defaut depuis WP 5.5), le LCP est passe de 3.1s a 1.4s.

3. Precharger la police principale. Une seule ligne dans le `<head>` — `<link rel="preload" href="police.woff2" as="font" crossorigin>` — a supprime le flash de texte invisible (FOIT) et gagne 200ms sur le First Contentful Paint.

Le point commun de ces 3 actions : elles ne coutent rien, ne cassent rien, et se font en moins d'une heure.

La performance n'est pas une question de budget. C'est une question de methode.

Si vous voulez aller plus loin, j'ai documente le processus complet avec les mesures avant/apres sur schoolsWP.com.

---

## Notes de conformite

- **Vouvoiement** : oui (LinkedIn = formel)
- **Accroche** : chiffre concret (74 %), interpellation directe
- **Structure** : probleme > solution > 3 points > synthese > CTA soft
- **Longueur** : ~250 mots (format LinkedIn optimal)
- **Casing** : schoolsWP (correct)
- **CTA** : une seule ligne en fin de post, pas de lien direct
- **Pas de surcharge** : zero emoji, zero hashtag dans le corps
