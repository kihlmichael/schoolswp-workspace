# Lecon 1.6 - Connecter ton page builder : Gutenberg + Kadence Blocks

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : M1 - Installation et configuration
- **Lecon** : 1.6 - Connecter ton page builder
- **Duree cible** : 6 min (~900 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Configurer Gutenberg comme page builder dans CartFlows, installer Kadence Blocks, et connaitre les blocs essentiels pour designer des pages de funnel performantes.

---

## Script narration

**[INTRO - face camera]**

CartFlows gere la logique de ton funnel - les etapes, les redirections, les order bumps, les upsells. Mais le design de chaque page, c'est ton page builder qui s'en charge. C'est lui qui controle ce que ton visiteur voit : la mise en page, les titres, les boutons, les temoignages. Si ton page builder est mal configure ou limite, tes pages de funnel seront mediocres, peu importe la qualite de ta strategie de vente.

Dans cette lecon, on configure Gutenberg comme page builder pour CartFlows, on installe Kadence Blocks, et je te montre les blocs concrets que tu vas utiliser sur chaque page de funnel.

---

**[SECTION 1 - Pourquoi le choix du page builder compte]**

**[ECRAN - slide "Page builder = design de ton funnel"]**

Quand tu edites un step dans CartFlows - une landing page, un checkout, une page de remerciement - tu ne travailles pas dans une interface CartFlows. Tu travailles dans ton editeur WordPress habituel. CartFlows ouvre la page dans Gutenberg, et c'est la que tu construis le contenu.

Le page builder que tu choisis determine trois choses. Premierement, les composants disponibles : est-ce que tu as des blocs de temoignages, des compteurs d'urgence, des mises en page flexibles ? Deuxiemement, le controle responsive : est-ce que tu peux ajuster le rendu sur desktop, tablette et mobile separement ? Troisiemement, la performance : est-ce que tes pages chargent vite ou est-ce que le page builder ajoute du code inutile qui alourdit tout ?

C'est pour ca qu'on utilise Gutenberg avec Kadence Blocks dans cette formation. Et je t'explique pourquoi.

---

**[SECTION 2 - Gutenberg : compatibilite native avec CartFlows]**

**[ECRAN - WordPress admin > CartFlows]**

Gutenberg, c'est l'editeur natif de WordPress. Il est deja installe - tu n'as rien a ajouter. CartFlows le supporte nativement, sans plugin supplementaire. Quand tu ouvres un step de ton flow pour l'editer, Gutenberg se lance automatiquement.

L'avantage principal : zero conflit. Pas de plugin intermediaire, pas de couche supplementaire entre CartFlows et ton editeur. Le rendu que tu vois dans l'editeur, c'est le rendu final. Et les mises a jour WordPress n'introduisent jamais de probleme de compatibilite avec Gutenberg puisque c'est le meme logiciel.

Mais Gutenberg seul a une limite : ses blocs de base sont fonctionnels, mais basiques. Un titre, un paragraphe, une image, un bouton - c'est bien pour un article de blog, mais insuffisant pour une page de vente qui doit convertir. C'est la que Kadence Blocks entre en jeu.

---

**[SECTION 3 - Pourquoi Kadence Blocks]**

**[ECRAN - slide "Kadence Blocks : l'arsenal funnel"]**

Kadence Blocks, c'est une extension gratuite qui ajoute des blocs avances a Gutenberg. Et ce n'est pas un gadget - c'est le compagnon ideal pour CartFlows. Trois raisons.

Premiere raison : les blocs avances. Row Layout pour structurer tes sections, Advanced Heading pour controler la typographie de tes titres, Advanced Button pour des CTA stylises, Icon List pour des listes de benefices avec des icones, Tabs et Accordion pour organiser de l'information, et un bloc Form si tu as besoin de formulaires. Ce sont exactement les composants dont tu as besoin sur une page de vente.

Deuxieme raison : le controle responsive par appareil. Chaque bloc Kadence te permet d'ajuster les tailles, les marges, la visibilite pour desktop, tablette et mobile separement. Sur une page de funnel, c'est indispensable. Ton titre peut faire 48px sur desktop et 28px sur mobile. Ton bouton CTA peut avoir un padding different selon l'ecran. Tu ne devines pas - tu controles.

Troisieme raison : les performances. Kadence Blocks ne genere pas de DOM bloat. Contrairement a d'autres solutions qui injectent des dizaines de div imbriquees et des fichiers CSS/JS massifs, Kadence produit un code leger. Tes pages de funnel chargent vite, et la vitesse de chargement impacte directement ton taux de conversion.

---

**[SECTION 4 - Verifier la configuration CartFlows]**

**[ECRAN - CartFlows > Settings > General]**

Premiere etape : verifie que CartFlows utilise bien Gutenberg. Va dans CartFlows, puis Settings, puis l'onglet General. Tu vas trouver un parametre "Page Builder". Selectionne Gutenberg. Si c'est deja le cas, parfait - tu n'as rien a changer.

Ce reglage indique a CartFlows quel editeur ouvrir quand tu cliques sur "Editer" dans un step. Si tu as un autre page builder installe sur ton site - Elementor, Divi, ou autre - CartFlows pourrait l'avoir detecte automatiquement. Verifie et corrige si necessaire. On veut Gutenberg.

---

**[SECTION 5 - Installer Kadence Blocks]**

**[ECRAN - WordPress > Extensions > Ajouter]**

Si Kadence Blocks n'est pas encore installe, c'est le moment. Va dans Extensions, puis Ajouter. Tape "kadence blocks" dans la barre de recherche. C'est l'extension developpee par Kadence WP - verifie que c'est bien le bon editeur, avec plus de 400 000 installations actives.

Clique sur Installer, puis Activer. C'est fait. Kadence Blocks ajoute automatiquement ses blocs dans l'editeur Gutenberg. Tu n'as rien d'autre a configurer.

Note : on utilise la version gratuite de Kadence Blocks. Elle contient tous les blocs dont tu as besoin pour les funnels de cette formation. La version Pro existe, elle ajoute des blocs supplementaires, mais elle n'est pas necessaire pour suivre ce qu'on fait ici.

---

**[SECTION 6 - Les blocs Kadence essentiels pour tes funnels]**

**[ECRAN - Gutenberg avec panneau de blocs Kadence ouvert]**

Voyons les six blocs que tu vas utiliser le plus souvent dans tes pages de funnel.

**Row Layout** - c'est le bloc de structure. Il te permet de creer des sections avec une ou plusieurs colonnes. Chaque section de ta page de vente - hero, benefices, temoignages, CTA - commence par un Row Layout. Tu controles la couleur de fond, les marges, et la largeur maximale.

**Advanced Heading** - pour tes titres et sous-titres. Tu choisis la police, la taille, la couleur, l'espacement des lettres, le tout par appareil. Un bon titre accrocheur avec la bonne typographie, ca change la perception de toute la page.

**Advanced Button** - tes boutons d'appel a l'action. Couleur, taille, icone, bordure, ombre, animation au survol. Sur un funnel, le bouton CTA est l'element le plus important apres le titre. Kadence te donne le controle total.

**Icon List** - les listes avec des icones a gauche de chaque item. Parfait pour presenter les benefices d'un produit ou les fonctionnalites incluses dans une offre. Visuellement, c'est beaucoup plus efficace qu'une liste a puces standard.

**Countdown Timer** - un compteur a rebours. Quand tu as une offre limitee dans le temps, ce bloc ajoute de l'urgence visuelle. Tu definis une date de fin, et le compteur decompte les jours, heures, minutes et secondes. A utiliser avec parcimonie - mais sur une offre de lancement ou une promo flash, ca fonctionne.

**Testimonials** - un bloc dedie aux temoignages clients. Photo, nom, texte, etoiles. La preuve sociale est un des leviers de conversion les plus puissants. Ce bloc te permet de l'integrer proprement sans bricoler avec des images et du texte brut.

---

**[SECTION 7 - Tester sur un step existant]**

**[ECRAN - CartFlows > Flow > editer un step]**

Pour verifier que tout fonctionne, ouvre un de tes flows dans CartFlows. Clique sur un step - ta landing page par exemple - et clique sur "Editer". Gutenberg s'ouvre.

Dans l'editeur, clique sur le "+" pour ajouter un bloc. Cherche "kadence". Tu dois voir apparaitre tous les blocs Kadence : Row Layout, Advanced Heading, Advanced Button, et les autres. Si c'est le cas, tout est en place. Tu es pret a designer tes pages de funnel.

Ajoute un bloc Row Layout pour tester. Choisis une mise en page a deux colonnes. Tu vois comment ca s'integre directement dans la page. C'est exactement comme ca qu'on va construire chaque section dans les prochaines lecons.

---

**[OUTRO - face camera]**

Ton environnement est maintenant complet. CartFlows gere la logique du funnel. Gutenberg est ton editeur. Kadence Blocks te donne les composants avances pour creer des pages qui convertissent. Et tout ca fonctionne ensemble nativement, sans usine a gaz.

Si tu utilises un autre page builder comme Elementor ou Divi, CartFlows les supporte aussi - tu peux adapter les concepts. Mais dans cette formation, toutes les demos et tous les exemples sont faits avec Gutenberg et Kadence Blocks. C'est la stack la plus legere et la plus performante pour des funnels WordPress.

Dans la prochaine lecon, on passe a la pratique : on construit la landing page de vente de ton funnel, section par section. A tout de suite.

---

## Notes de production

### Visuels

| Timecode approx. | Type | Contenu |
|---|---|---|
| 0:00-0:30 | Face camera | Intro - pourquoi le page builder compte |
| 0:30-1:15 | Slide | Schema "CartFlows = logique / Page builder = design" |
| 1:15-2:00 | Screencast | WordPress admin > CartFlows, navigation dans un flow |
| 2:00-2:45 | Slide | Kadence Blocks - 3 raisons (blocs, responsive, perf) |
| 2:45-3:15 | Screencast | CartFlows > Settings > General > Page Builder = Gutenberg |
| 3:15-3:50 | Screencast | Extensions > Ajouter > "kadence blocks" > Installer > Activer |
| 3:50-5:15 | Screencast | Gutenberg - tour des 6 blocs Kadence avec demo rapide |
| 5:15-5:45 | Screencast | Ouvrir un step > ajouter un Row Layout > verifier |
| 5:45-6:00 | Face camera | Outro - recapitulatif + teaser prochaine lecon |

### Points techniques

- Montrer le panneau de blocs Kadence en gros plan pour que les noms soient lisibles
- Pour chaque bloc presente, montrer un apercu en 5-10 secondes (pas besoin de configurer entierement)
- Sur le Countdown Timer, preciser visuellement "a utiliser sur les offres limitees"
- Le screencast de la section 7 (test) doit montrer le flow CartFlows PUIS l'editeur Gutenberg - pour ancrer visuellement le lien entre les deux

### Ton et rythme

- Rythme soutenu mais pas presse - le public est en mode apprentissage
- Pas de jargon technique inutile (pas de "DOM", "markup" - sauf "DOM bloat" en section 3 qui est contextualise)
- Tutoiement constant, ton direct
