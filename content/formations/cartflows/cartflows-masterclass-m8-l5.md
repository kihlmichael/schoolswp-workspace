# Lecon 8.5 - Import/Export de funnels entre sites

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : 8 - Ecosysteme et automatisation
- **Duree cible** : 6 min (~900 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Exporter un flow CartFlows complet et l'importer sur un autre site WordPress. Comprendre ce qui est exporte et ce qui ne l'est pas pour eviter les mauvaises surprises.

---

## Script narration

**[INTRO - face camera]**

Tu as construit un funnel qui convertit. Les chiffres sont bons, le parcours est rode. Et maintenant, un client te demande de reproduire exactement le meme funnel sur son site. Ou bien tu lances un deuxieme site et tu veux repartir de la meme base.

Tout reconstruire a la main ? Non. CartFlows permet d'exporter un flow complet en un clic et de l'importer sur un autre site. Voyons comment ca marche et surtout, ce qu'il faut verifier apres l'import.

---

**[SECTION 1 - Exporter un flow]**

**[ECRAN - CartFlows > Flows > Export]**

L'export se fait depuis l'interface CartFlows. Va dans CartFlows > Flows. Survole le flow que tu veux exporter et clique sur "Export". CartFlows genere un fichier JSON qui contient toute la structure du flow.

Ce fichier JSON inclut :
- La structure du flow : les steps (landing, checkout, upsell, downsell, thank you) et leur ordre
- Le design des pages : les blocs Gutenberg ou le layout Kadence
- La configuration de chaque step : les parametres CartFlows (bump, upsell, regles de redirection)
- Les parametres de style : couleurs, polices, espacements

L'export est instantane. Le fichier pese generalement entre 100 Ko et 1 Mo selon la complexite du design.

---

**[SECTION 2 - Importer un flow]**

**[ECRAN - CartFlows > Flows > Import]**

Sur le site de destination, va dans CartFlows > Flows et clique sur "Import". Selectionne le fichier JSON exporte. CartFlows reconstruit le flow complet avec tous ses steps.

Apres l'import, tu retrouves exactement la meme structure : memes pages, meme design, memes parametres de steps. Les pages sont creees automatiquement dans WordPress avec le bon contenu.

L'import cree de nouvelles pages - il n'ecrase rien d'existant. Si tu importes le meme flow deux fois, tu auras deux copies independantes.

---

**[SECTION 3 - Ce qui est exporte vs ce qui ne l'est PAS]**

**[ECRAN - tableau comparatif exporte / non exporte]**

C'est la partie critique. Voici ce que tu dois savoir :

Ce qui EST exporte :
- Structure du flow et des steps
- Design des pages (blocs, layout, styles)
- Configuration CartFlows (bump text, upsell settings, redirection rules)
- Textes, titres, descriptions

Ce qui N'EST PAS exporte :
- Les produits WooCommerce. Le checkout fait reference a un produit (par exemple "Formation SEO - 97 euros"). Ce produit n'existe pas sur le nouveau site. Tu dois le recreer dans WooCommerce et le reassocier au checkout.
- Les images uploadees. Si tes pages contiennent des images, les URLs pointent vers l'ancien site. Il faut re-uploader les images sur le nouveau site et mettre a jour les liens.
- Les integrations externes. Les connexions Stripe, PayPal, FluentCRM, OttoKit - tout ca est specifique a chaque site. A reconfigurer.
- Les coupons WooCommerce. Si ton funnel utilise des coupons, ils doivent etre recrees.

---

**[SECTION 4 - Checklist post-import]**

**[ECRAN - checklist a cocher]**

Voici ta checklist apres chaque import de flow :

1. Verifier que toutes les pages sont creees et accessibles
2. Creer les produits WooCommerce correspondants sur le nouveau site
3. Associer chaque checkout step au bon produit WooCommerce
4. Re-configurer les order bumps avec les bons produits
5. Re-configurer les upsells et downsells avec les bons produits
6. Re-uploader les images et mettre a jour les URLs dans les pages
7. Verifier la passerelle de paiement (Stripe/PayPal)
8. Tester une commande complete de bout en bout
9. Verifier les redirections post-achat (surtout si tu rediriges vers TutorLMS)

Cette checklist prend 15 a 30 minutes selon la complexite du funnel. C'est toujours plus rapide que de tout reconstruire - mais ne saute pas l'etape de test.

---

**[OUTRO - face camera]**

L'import/export CartFlows, c'est un gain de temps enorme quand tu geres plusieurs sites ou quand tu travailles pour des clients. Exporte ton meilleur funnel, importe-le, adapte les produits et les visuels, et tu es operationnel en moins d'une heure.

Dans la prochaine lecon, on parle des redirections post-achat - ou envoyer ton client apres le paiement pour maximiser l'engagement.

---

## Notes de production

- **Visuels** : bouton export CartFlows, interface import, tableau exporte/non-exporte, checklist post-import
- **Captures d'ecran** : menu export flow, fichier JSON, interface import, flow importe
- **Ton** : pratique et direct, focus sur les pieges a eviter
- **Duree estimee** : ~6 min a debit normal
- **Transition** : enchaine sur L8.6 (Redirections post-achat)
