# Lecon 2.7 - Optimisation mobile : ce que la plupart oublient

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : 2 - Optimisation et conversion
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Identifier et corriger les 5 erreurs mobiles les plus courantes sur les pages de funnel, maitriser les controles responsive de Kadence Blocks, et adopter l'approche mobile-first pour maximiser les conversions.

---

## Script narration

**[INTRO - face camera]**

Entre 60 et 75% du trafic sur un site WordPress vient du mobile. Pas 20%, pas 30% - la majorite. Et pourtant, la plupart des funnels que je vois sont concus sur un ecran 27 pouces, et personne ne verifie ce que ca donne sur un iPhone.

Le resultat : des pages qui ont l'air pro sur desktop et qui sont inutilisables sur mobile. Des boutons qu'on ne voit pas, des formulaires penibles a remplir, des temps de chargement qui font fuir. Tu perds la majorite de tes visiteurs avant meme qu'ils voient ton offre.

Dans cette lecon, on va corriger ca. Je vais te montrer les 5 erreurs mobiles les plus courantes sur les pages de funnel, comment les regler avec Kadence Blocks, et pourquoi tu devrais designer pour mobile d'abord.

---

**[SECTION 1 - Les 5 erreurs mobiles les plus courantes]**

**[ECRAN - slide "5 erreurs mobiles"]**

Premiere erreur : les titres trop longs. Un H1 de 15 mots qui tient sur une ligne en desktop, ca prend trois ecrans sur mobile. Ton visiteur doit scroller juste pour voir le debut de ton contenu. C'est un tueur de conversions. La regle : ton titre principal doit tenir sur 2 lignes maximum en vue mobile. Si c'est plus long, raccourcis-le ou reduis la taille de police sur mobile.

**[ECRAN - comparaison avant/apres titre mobile]**

Deuxieme erreur : les images trop lourdes. Une image hero de 2 Mo, sur desktop avec une connexion fibre, ca passe. Sur mobile en 4G dans le metro, c'est 3 a 5 secondes de chargement. Google mesure ca - et tes visiteurs aussi. Chaque seconde de chargement en plus, c'est environ 7% de conversions en moins. On en reparle dans la section performance.

Troisieme erreur : les boutons trop petits ou trop bas dans la page. Sur mobile, ton call-to-action doit etre visible sans scroller. Et il doit etre assez grand pour qu'on puisse taper dessus avec le pouce sans viser. Un bouton de 30 pixels de haut, c'est trop petit. Vise au minimum 48 pixels, idealement 56. Et place-le haut dans la page - au-dessus de la ligne de flottaison.

**[ECRAN - exemple bouton trop petit vs bouton correct]**

Quatrieme erreur : les formulaires penibles a remplir. Des champs trop petits, un clavier qui masque le champ actif, des labels qui disparaissent quand tu tapes. Sur desktop, on tolere un formulaire moyen. Sur mobile, c'est l'abandon garanti. Chaque champ inutile que tu ajoutes reduit ton taux de completion. Limite-toi au strict necessaire : email, nom, et c'est souvent suffisant pour un opt-in.

Cinquieme erreur : le padding excessif. Des sections avec 80 pixels de marge en haut et en bas, ca donne de l'air sur desktop. Sur mobile, ca allonge ta page de facon absurde. Ton visiteur scrolle pendant 10 secondes sans voir de contenu. Reduis systematiquement les espacements sur mobile - 20 a 30 pixels suffisent generalement.

---

**[SECTION 2 - Les controles responsive de Kadence Blocks]**

**[ECRAN - editeur Gutenberg, panneau Kadence Blocks]**

La bonne nouvelle : Kadence Blocks te donne le controle total sur l'affichage par appareil. Chaque bloc a des reglages separes pour Desktop, Tablette et Mobile. Tu vois les trois icones en haut du panneau de reglages - clique sur celle que tu veux pour ajuster les valeurs independamment.

**[ECRAN - demonstration taille de police responsive]**

Premiere chose a regler : la taille de police. Un titre en 48px sur desktop, c'est impactant. Sur mobile, c'est enorme et ca prend trop de place. Passe a 28 ou 32px sur mobile. Pour le corps de texte, 16px minimum - en dessous, c'est illisible sans zoomer.

**[ECRAN - demonstration padding/margin responsive]**

Deuxieme reglage : le padding et les marges. Pour chaque section, chaque row, chaque bloc, tu peux definir des valeurs differentes. Desktop : 60px de padding vertical. Tablette : 40px. Mobile : 20px. C'est ce genre de detail qui fait la difference entre une page pro et une page amateur.

**[ECRAN - option "masquer sur mobile"]**

Troisieme reglage : masquer un bloc sur mobile. Dans les reglages avances de chaque bloc Kadence, tu as l'option de visibilite par appareil. Cette image decorative qui fait joli sur desktop mais qui ralentit le chargement mobile ? Masque-la. Cette deuxieme colonne qui passe mal en empile ? Masque-la et cree une version mobile dediee.

Attention : ne masque pas du contenu important. Google indexe le contenu mobile. Si tu masques ton H1 ou tes arguments de vente sur mobile, tu te tires une balle dans le pied cote SEO.

---

**[SECTION 3 - Tester sur un vrai telephone]**

**[FACE CAMERA]**

Le preview responsive de ton navigateur - celui que tu actives avec F12 ou les DevTools - c'est un debut. Mais ce n'est pas la realite. Il ne simule pas la latence reseau, il ne reproduit pas le comportement tactile, et il ne montre pas les problemes de clavier mobile.

Prends ton telephone. Ouvre ta page de funnel. Et fais le parcours complet : lis le titre, scrolle, clique sur le bouton, remplis le formulaire, valide le paiement. Fais-le en conditions reelles - pas sur ton WiFi, mais en 4G. Demande a quelqu'un d'autre de le faire aussi. Tu vas decouvrir des problemes que tu n'aurais jamais vus autrement.

Un test de 3 minutes sur un vrai telephone vaut plus qu'une heure d'ajustements dans le preview navigateur.

---

**[SECTION 4 - Performance mobile]**

**[ECRAN - PageSpeed Insights]**

La performance sur mobile, c'est principalement une question d'images. Les images representent en moyenne 50 a 70% du poids d'une page. Deux actions concretes.

Premiere action : compresse tes images avec un plugin dedie. Imagify ou ShortPixel - les deux fonctionnent bien. Ils convertissent automatiquement en WebP, un format plus leger que JPEG, et ils compressent sans perte visible de qualite. Un setup de 5 minutes qui allegera toutes tes images existantes et futures.

Deuxieme action : active le lazy loading. Depuis WordPress 5.5, le lazy loading est natif - les images en bas de page ne se chargent que quand le visiteur scrolle vers elles. Verifie que ton theme ne le desactive pas. Dans Kadence, c'est actif par defaut.

**[ECRAN - score PageSpeed avant/apres]**

Avec ces deux actions - compression d'images et lazy loading - tu gagnes facilement 15 a 30 points sur ton score PageSpeed mobile. Et surtout, tes visiteurs voient ta page plus vite.

---

**[SECTION 5 - L'approche mobile-first]**

**[FACE CAMERA]**

Le conseil le plus important de cette lecon : designe pour mobile d'abord, ajuste pour desktop ensuite.

C'est l'inverse de ce que tout le monde fait. La plupart des gens creent leur page sur un grand ecran, avec des colonnes, des images pleine largeur, des effets visuels - et ensuite ils essaient de faire rentrer tout ca sur mobile. Le resultat est toujours un compromis bancal.

Si tu pars du mobile, tu es force d'aller a l'essentiel. Un titre court. Un argument clair. Un bouton visible. Et quand tu passes sur desktop, tu as de la place pour enrichir - ajouter une deuxieme colonne, une image, plus d'espace. C'est beaucoup plus facile d'enrichir que de simplifier.

Dans Kadence, tu peux travailler directement en vue mobile dans l'editeur. Clique sur l'icone mobile dans la barre responsive, et construis ta page dans cette vue. Ensuite, passe en desktop pour ajuster les details.

---

**[OUTRO - face camera]**

Resume : verifie tes titres, tes boutons, tes formulaires et tes espacements sur mobile. Utilise les controles responsive de Kadence. Teste sur un vrai telephone. Compresse tes images. Et pense mobile d'abord.

Ce sont des ajustements simples, mais ils font la difference entre un funnel qui convertit et un funnel qui perd la majorite de son trafic.

Dans la prochaine lecon, on aborde un sujet que personne ne traite dans les formations CartFlows : le SEO de tes pages funnel. Faut-il les indexer ou les mettre en noindex ? La reponse n'est pas celle que tu crois.

---

## Notes de production

### Captures d'ecran suggerees

- Slide "5 erreurs mobiles" avec icones numerotees (section 1)
- Comparaison avant/apres titre mobile - screenshot reel d'un funnel (section 1)
- Exemple bouton trop petit (30px) vs bouton correct (56px) cote a cote (section 1)
- Editeur Gutenberg avec panneau Kadence Blocks - icones Desktop/Tablette/Mobile encadrees (section 2)
- Demonstration taille de police responsive - valeurs differentes par appareil (section 2)
- Demonstration padding responsive - 60/40/20px (section 2)
- Option "masquer sur mobile" dans les reglages avances Kadence (section 2)
- PageSpeed Insights - score avant/apres compression (section 4)

### Transitions

- Intro : face camera, ton direct, fond neutre schoolsWP
- Section 1 : slides + captures comparatives (avant/apres)
- Section 2 : screencast editeur Kadence Blocks - demonstrations en direct
- Section 3 : face camera - ton personnel, conseil pratique
- Section 4 : screencast PageSpeed Insights + plugins
- Section 5 : face camera - conseil strategique
- Outro : face camera, CTA vers lecon 2.8

### Duree estimee par section

| Section | Duree |
| --- | --- |
| Intro | 0:45 |
| Section 1 - 5 erreurs mobiles | 2:30 |
| Section 2 - Controles Kadence | 2:00 |
| Section 3 - Tester sur vrai telephone | 0:45 |
| Section 4 - Performance mobile | 1:15 |
| Section 5 - Approche mobile-first | 0:30 |
| Outro | 0:15 |
| **Total** | **~8:00** |
