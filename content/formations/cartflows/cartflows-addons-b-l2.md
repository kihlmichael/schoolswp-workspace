# Lecon B.2 - Installer Cart Abandonment Recovery

## Metadata

- **Formation** : CartFlows Add-ons (premium - FRM-008)
- **Module** : B - Cart Abandonment Recovery
- **Duree cible** : 6 min (~900 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Installer et activer Cart Abandonment Recovery, comprendre son fonctionnement technique (capture d'email avant finalisation) et verifier son integration avec CartFlows.

---

## Script narration

**[INTRO - face camera]**

Cart Abandonment Recovery est gratuit, disponible sur WordPress.org, et s'installe en deux minutes. Mais avant de cliquer sur "Activer", il faut comprendre comment le plugin fonctionne techniquement - parce que c'est la que reside toute sa valeur.

---

**[SECTION 1 - Installation du plugin]**

**[ECRAN - tableau de bord WordPress]**

Dans ton tableau de bord WordPress, va dans Extensions → Ajouter. Dans la barre de recherche, tape "cart abandonment recovery".

Le premier resultat devrait etre "WooCommerce Cart Abandonment Recovery" par Starter Templates (c'est le nom commercial de Brainstorm Force sur WordPress.org). Tu le reconnais a l'icone verte avec un panier.

Clique sur "Installer maintenant" puis "Activer".

C'est tout. Pas de cle de licence, pas de configuration complexe a l'installation. Le plugin est actif.

---

**[SECTION 2 - Le wizard de configuration rapide]**

**[ECRAN - wizard Cart Abandonment Recovery]**

A l'activation, le plugin te propose un assistant de configuration rapide. Trois etapes.

Premiere etape : tes informations d'envoi. Le nom et l'email qui apparaitront comme expediteur des emails de relance. Utilise le meme email que tes emails WooCommerce pour la coherence - en general ton email de boutique.

Deuxieme etape : activer ou desactiver les emails par defaut. Le plugin cree automatiquement une sequence de 3 emails de relance. Tu peux les personnaliser plus tard - pour l'instant, laisse-les actifs. On les retravaillera en detail dans la lecon 3.

Troisieme etape : activer les coupons automatiques. Le plugin peut generer un coupon unique pour l'email de relance numero 3. Active cette option - on configurera le montant dans la lecon 5.

Valide le wizard. Le plugin est pret.

---

**[SECTION 3 - Comment ca fonctionne techniquement]**

**[ECRAN - schema flux capture email]**

Voici ce qui se passe en coulisses, et c'est la que ca devient interessant.

Quand un visiteur arrive sur ta page de checkout - que ce soit le checkout WooCommerce standard ou un checkout CartFlows - il commence a remplir le formulaire. Le premier champ, c'est en general l'adresse email.

Le moment ou le visiteur tape son email et passe au champ suivant, Cart Abandonment Recovery capture cette adresse. Avant que la commande soit finalisee. Avant meme que le client ait rempli son adresse de livraison.

Le plugin surveille le champ email avec du JavaScript. Des que le curseur quitte le champ, l'email est enregistre en base de donnees avec l'etat "abandon en cours".

Si le client finalise sa commande, le statut passe a "termine" et aucun email de relance ne part. Si le client quitte la page sans payer, le plugin attend le delai configure (15 minutes par defaut) puis declenche la sequence de relance.

C'est pour ca que le plugin est si efficace : il n'a pas besoin que le client ait un compte. Il n'a pas besoin qu'il soit connecte. Il lui faut juste l'email - et le client le donne naturellement en remplissant le checkout.

---

**[SECTION 4 - Integration native avec CartFlows]**

**[ECRAN - checkout CartFlows avec champ email]**

Cart Abandonment Recovery et CartFlows sont developpes par la meme equipe. L'integration est native - aucune configuration supplementaire.

Si tu utilises un checkout CartFlows (et tu devrais, vu ce qu'on a vu dans les modules precedents), la capture d'email fonctionne automatiquement. Le plugin detecte le champ email du checkout CartFlows exactement comme il detecte celui de WooCommerce.

L'avantage avec CartFlows : ton checkout est deja optimise pour la conversion. Moins de champs, meilleur design, moins de friction. Cart Abandonment Recovery vient recuperer ceux qui abandonnent malgre cette optimisation. Les deux plugins sont complementaires.

---

**[SECTION 5 - Verifier que tout fonctionne]**

**[ECRAN - WooCommerce → Cart Abandonment]**

Pour verifier que le plugin est bien actif, va dans WooCommerce → Cart Abandonment. Tu dois voir le tableau de bord du plugin avec les onglets : Reports, Settings, Follow-Up Emails.

Fais un test simple : ouvre ta boutique en navigation privee, ajoute un produit au panier, va au checkout, tape une adresse email de test, puis ferme la page sans finaliser.

Attends 15 minutes (le delai par defaut du premier email). Si tout est bien configure, tu recevras un email de relance a l'adresse que tu as saisie.

Si l'email n'arrive pas, verifie deux choses : que tes emails WordPress fonctionnent (installe un plugin SMTP si ce n'est pas deja fait) et que l'email de test n'est pas dans les spams.

---

**[CONCLUSION - face camera]**

Le plugin est installe, actif, et il capture deja les emails de tes visiteurs qui commencent le checkout sans finir. A partir de maintenant, chaque abandon est enregistre.

Dans la prochaine lecon, on configure la sequence de relance : quel email, a quel moment, avec quel message. C'est la que la recuperation commence vraiment.

---

## Notes de production

- **Visuels** : capture ecran Extensions → Ajouter, wizard du plugin, schema technique capture email, menu WooCommerce → Cart Abandonment
- **Donnees** : plugin gratuit, 800K+ installs, meme editeur que CartFlows (Brainstorm Force)
- **Transition** : enchaine sur LB.3 (configurer la sequence de relance)
