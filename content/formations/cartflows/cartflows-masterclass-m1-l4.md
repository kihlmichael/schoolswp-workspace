# Lecon 1.4 - Installer et configurer CartFlows Pro

## Metadata
- Formation : CartFlows Masterclass Vente (FRM-007, premium)
- Module : 1 - Fondations
- Duree cible : 8 min
- Objectif pedagogique : Acheter, installer et activer CartFlows Pro, puis identifier les nouvelles features disponibles (Order Bumps, Upsells, A/B Testing, Canvas Mode)
- Prerequis : CartFlows gratuit installe (vu dans le Quick Start), WooCommerce actif

## Script narration

[INTRO]

Dans les lecons precedentes, tu as decouvert la difference entre Free et Pro, tu connais l'architecture d'un funnel performant, et tu as vu les cinq types de funnels que tu vas pouvoir construire. Maintenant, on passe a l'action : on installe CartFlows Pro sur ton site.

Si tu as suivi le Quick Start, tu as deja la version gratuite de CartFlows et WooCommerce. C'est exactement ce qu'il faut. CartFlows Pro s'installe par-dessus la version gratuite - il ne la remplace pas, il l'enrichit. Les deux fonctionnent ensemble.

---

[SECTION 1 - Choisir et acheter le bon plan]

Ouvre cartflows.com dans un nouvel onglet et clique sur "Pricing". Tu vas voir plusieurs plans. Je te recommande de commencer avec le plan Starter. Il te donne acces a toutes les features de vente qu'on va utiliser dans cette formation : Order Bumps, One-Click Upsells, A/B Split Testing, et le Canvas Mode.

Les plans superieurs ajoutent des features avancees - funnels illimites, support prioritaire, licences multi-sites. Tu pourras upgrader plus tard si tu en as besoin. Pour l'instant, le Starter couvre tout ce qu'il faut.

Choisis ton plan, cree ton compte ou connecte-toi si tu en as deja un, et termine le paiement. Une fois la commande confirmee, tu arrives sur ton espace client CartFlows. C'est la que tu vas recuperer deux choses : le fichier d'installation et ta cle de licence.

---

[SECTION 2 - Telecharger le fichier .zip]

Dans ton espace client CartFlows, cherche la section "Downloads". Tu vas y trouver un fichier nomme quelque chose comme `cartflows-pro.zip`. Telecharge-le sur ton ordinateur. Ne decompresse pas le fichier - WordPress a besoin du .zip tel quel.

Petit rappel si c'est la premiere fois que tu installes un plugin premium : les plugins payants ne sont pas disponibles depuis le repertoire officiel WordPress.org. Tu dois les installer manuellement via un fichier .zip que l'editeur te fournit. C'est ce qu'on fait maintenant.

---

[SECTION 3 - Installer le plugin sur WordPress]

Retourne sur ton dashboard WordPress. Va dans Extensions, puis clique sur "Ajouter". En haut de la page, tu vois le bouton "Televerser une extension". Clique dessus.

Selectionne le fichier `cartflows-pro.zip` que tu viens de telecharger. Clique sur "Installer maintenant". WordPress decompresse le fichier et installe le plugin. Ca prend quelques secondes.

Une fois l'installation terminee, clique sur "Activer l'extension". Tu devrais voir CartFlows Pro apparaitre dans ta liste d'extensions, juste en dessous de CartFlows (la version gratuite). Les deux doivent etre actifs - c'est normal, Pro est un add-on qui s'appuie sur la base gratuite.

Si tu vois un message d'erreur a cette etape, verifie deux choses : que CartFlows gratuit est bien active, et que ta version de WooCommerce est a jour. CartFlows Pro a besoin des deux pour fonctionner.

---

[SECTION 4 - Activer la licence]

Le plugin est installe, mais il n'est pas encore active cote licence. Sans la licence, tu n'auras pas acces aux mises a jour automatiques, et certaines features Pro resteront verrouillees.

Va dans CartFlows, puis Settings, puis l'onglet License. Tu vois un champ "License Key". Retourne sur ton espace client cartflows.com, copie ta cle de licence - c'est une longue chaine de caracteres, souvent visible dans la section "License" ou dans l'email de confirmation.

Colle la cle dans le champ, puis clique sur "Activate". Si tout va bien, tu vois un message de confirmation en vert : "License activated successfully". Le statut passe a "Active".

Garde cette cle quelque part - dans un gestionnaire de mots de passe, dans un doc prive. Tu en auras besoin si tu reinstalles le plugin ou si tu migres ton site.

---

[SECTION 5 - Verifier que les features Pro sont actives]

Maintenant, verifions que tout fonctionne. Va dans CartFlows et ouvre un flow existant - celui du Quick Start par exemple. Clique sur "Edit" a cote du step Checkout.

Premiere verification : tu dois voir un nouvel onglet "Order Bump" dans les reglages du step. Avant, cet onglet n'existait pas. C'est la que tu vas configurer les offres complementaires qui s'affichent directement sur la page de paiement - on les verra en detail dans le module 3.

Deuxieme verification : cree un nouveau step de type "Upsell" dans ton flow. Quand tu ouvres ses reglages, tu vois un onglet "Offer" avec les options de One-Click Upsell. Le client pourra accepter ou refuser l'offre en un clic, sans ressaisir ses informations de paiement. On configure ca dans le module 4.

Troisieme verification : dans n'importe quel step, cherche la section "A/B Testing". Tu dois voir un bouton ou un lien pour creer une variante. Le A/B Testing te permet de tester deux versions d'une meme page pour identifier celle qui convertit le mieux. On mettra ca en place dans le module 7.

Si tu vois ces trois elements - Order Bump, Upsell/Downsell, A/B Testing - c'est bon, CartFlows Pro est correctement installe et active.

---

[SECTION 6 - Tour rapide des nouveaux menus Pro]

Avant de terminer, faisons un tour rapide pour que tu saches ou tout se trouve. On ne configure rien maintenant - on repere juste les outils.

Premier point : l'onglet "Order Bump" dans chaque step Checkout. C'est ici que tu ajouteras un produit complementaire affiche juste avant le bouton de paiement. Pense "coque de telephone a la caisse" - simple, contextuel, impulsif.

Deuxieme point : les steps de type "Upsell" et "Downsell" dans l'editeur de flow. Quand tu ajoutes un nouveau step, tu peux maintenant choisir "Upsell" ou "Downsell" comme type. Chacun a ses propres reglages d'offre. L'upsell propose une montee en gamme apres le paiement. Le downsell est l'alternative proposee si le client refuse l'upsell.

Troisieme point : le Canvas Mode. Va dans un flow et cherche le bouton "Canvas" en haut. Le Canvas Mode te donne une vue visuelle de ton funnel - tu vois chaque step, les connexions entre eux, et tu peux reorganiser le parcours par glisser-deposer. C'est beaucoup plus lisible qu'une simple liste quand ton funnel a plus de trois ou quatre steps.

Quatrieme point : dans CartFlows → Settings, explore les nouveaux onglets. Tu verras des sections pour les reglages globaux des Order Bumps, les options de paiement pour les Upsells, et les parametres du A/B Testing. On reviendra sur chacun de ces reglages quand on les utilisera concretement.

---

[CONCLUSION]

CartFlows Pro est installe, la licence est active, et tu as repere ou se trouvent les features qu'on va utiliser dans les prochains modules. Ne touche a rien pour l'instant - on va configurer chaque feature en detail dans les modules suivants. L'ordre est important : d'abord les fondations, ensuite les techniques de vente.

Dans la prochaine lecon, on explore le Canvas Mode en profondeur - l'outil qui te permet de visualiser et d'organiser tes funnels de maniere intuitive.

---

## Notes de production

### Captures d'ecran / screencasts necessaires
1. Page pricing cartflows.com - mettre en surbrillance le plan Starter
2. Espace client CartFlows - section Downloads avec le fichier .zip
3. WordPress → Extensions → Ajouter → Televerser une extension (etapes)
4. CartFlows → Settings → License → champ vide, puis champ rempli + message "Active"
5. Step Checkout : onglet "Order Bump" visible (encadrer en rouge)
6. Nouveau step de type "Upsell" : onglet "Offer" visible
7. Section A/B Testing dans un step (encadrer en rouge)
8. Canvas Mode : vue d'ensemble d'un flow avec 4-5 steps

### Annotations texte (overlays HeyGen)
- "cartflows.com → Pricing → Starter" (SECTION 1)
- "Downloads → cartflows-pro.zip" (SECTION 2)
- "Extensions → Ajouter → Televerser" (SECTION 3)
- "CartFlows → Settings → License" (SECTION 4)
- Checklist visuelle : "Order Bump / Upsell / A/B Testing" (SECTION 5)

### Rythme et ton
- Ton direct, rythme soutenu - pas de temps mort
- Chaque section = une action concrete terminee
- Sections 1-4 : technique pure, rester factuel
- Sections 5-6 : plus exploratoire, donner un apercu sans entrer dans le detail
- Conclusion : rassurer ("ne touche a rien") et teaser la suite

### Duree estimee par section
| Section | Duree |
|---|---|
| Intro | 0:30 |
| Section 1 - Choisir le plan | 1:15 |
| Section 2 - Telecharger le .zip | 0:45 |
| Section 3 - Installer le plugin | 1:30 |
| Section 4 - Activer la licence | 1:15 |
| Section 5 - Verifier les features | 1:30 |
| Section 6 - Tour des menus Pro | 1:30 |
| Conclusion | 0:15 |
| **Total** | **~8:30** |
