# Script video - Lecon 5 : Personnaliser et publier

**Formation** : FluentForms Quick Start
**Code** : FRM-011
**Lecon** : 5/5 - Personnaliser le design et publier
**Duree** : 4 min (~850 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera pour intro/conclusion/recap, screencast pour le design
**Objectif** : Styler les formulaires, verifier le rendu mobile, recapituler, teaser la Masterclass

---

**[INTRO - face camera]**

Derniere lecon. Tes deux formulaires fonctionnent - maintenant on les rend beaux. On va ajuster les couleurs, les bordures et les boutons pour que les formulaires s'integrent parfaitement a ton site. Ensuite, on fait le bilan et je te montre ce qui t'attend dans la Masterclass.

**[SECTION 1 - Styler le formulaire]**

**[ECRAN - screencast du styler FluentForms]**

Ouvre un de tes formulaires dans le builder. En haut, clique sur l'icone "Preview & Design" - c'est l'outil de personnalisation visuelle de FluentForms.

Tu arrives sur un ecran avec ton formulaire a droite et les options de style a gauche. Tout se fait visuellement, pas besoin de CSS.

Premiere option : le style general. Tu choisis entre plusieurs presets - Flat, Material, Bootstrap, ou Custom. Le preset "Flat" est clean et moderne, c'est un bon point de depart. Selectionne-le.

Deuxieme option : les couleurs. Tu peux changer la couleur de fond du formulaire, la couleur des bordures des champs, la couleur du texte des labels, et la couleur du texte placeholder. Reprends les couleurs de ta charte graphique. Si ton site utilise Kadence avec un bleu principal et un gris fonce pour les textes, utilise les memes codes couleurs ici.

Troisieme option : les bordures. Tu controles le rayon des coins - arrondi ou carre - et l'epaisseur de la bordure. Un rayon de 4 a 8 pixels donne un rendu moderne sans exagerer.

Quatrieme option : le bouton d'envoi. C'est l'element le plus important visuellement. Change la couleur de fond pour qu'elle ressorte - un bouton de la meme couleur que le reste du formulaire est invisible. Utilise ta couleur d'accent. Ajuste la taille du texte, le padding, et le rayon des coins.

**[ECRAN - screencast avant/apres]**

Regarde la difference. Avant : un formulaire avec les styles par defaut, generique, qui ne correspond a rien sur le site. Apres : les couleurs de ta marque, un bouton visible, des bordures coherentes. Ca prend deux minutes et ca change tout.

**[SECTION 2 - CSS custom basique]**

**[ECRAN - screencast de l'ajout de CSS]**

Si tu veux aller plus loin, FluentForms permet d'ajouter du CSS custom par formulaire. Dans les reglages du formulaire, onglet "Customization", tu peux ajouter une classe CSS au conteneur du formulaire.

Un exemple concret : tu veux que le formulaire de capture d'email ait un fond colore pour ressortir sur la page. Ajoute une classe "ff-capture-bg" au formulaire, puis dans le Customizer de WordPress ou dans le CSS additionnel de Kadence, ajoute :

```css
.ff-capture-bg {
  background: #f0f4ff;
  padding: 24px;
  border-radius: 8px;
}
```

C'est facultatif. Le styler integre suffit pour la majorite des cas. Le CSS custom, c'est pour les details.

**[SECTION 3 - Preview mobile]**

**[ECRAN - screencast du preview mobile]**

Avant de publier, verifie le rendu sur mobile. Plus de 60% du trafic web est mobile - si ton formulaire est cassé sur telephone, tu perds des leads.

Dans le preview de FluentForms, tu peux basculer entre desktop et mobile. Verifie trois choses.

Les champs sont-ils assez grands pour etre tapes au doigt ? Un champ de 40 pixels de hauteur est trop petit sur mobile. FluentForms gere ca correctement par defaut, mais verifie.

Le bouton prend-il toute la largeur ? Sur mobile, un bouton pleine largeur est plus facile a cliquer qu'un petit bouton centre.

Le layout inline passe-t-il en vertical sur mobile ? Si tu as utilise un container en colonnes pour le formulaire de capture, verifie qu'il s'empile correctement sur petit ecran. FluentForms est responsive par defaut, mais un test rapide evite les surprises.

**[SECTION 4 - Recap]**

**[ECRAN - slide "Ce que tu as construit"]**

Recapitulons ce que tu as fait en 30 minutes.

Tu as installe FluentForms et configure l'anti-spam. Tu as cree un formulaire de contact professionnel avec cinq champs, des notifications email, et un message de confirmation. Tu as cree un formulaire de capture d'email minimaliste connecte a FluentCRM. Tu as personnalise le design pour coller a ta charte graphique. Et tu as verifie le rendu mobile.

Deux formulaires en production. Pas des maquettes - des formulaires qui captent des leads sur ton site en ce moment.

**[SECTION 5 - Teaser Masterclass]**

**[ECRAN - slide "FluentForms Masterclass"]**

Ce que tu as appris ici, c'est le Quick Start. Ca couvre les fondamentaux. Mais FluentForms va beaucoup plus loin.

Dans la Masterclass FluentForms, on explore tout.

La logique conditionnelle avancee : des formulaires qui s'adaptent en temps reel aux reponses. Un formulaire de devis qui calcule un prix, un formulaire d'inscription qui affiche des options selon le profil.

Les formulaires multi-etapes : au lieu d'un long formulaire, tu le decoupes en etapes avec une barre de progression. Le taux de completion explose.

Les paiements : Stripe, PayPal, integres directement dans le formulaire. Vente de produits, prises de reservation avec acompte, dons.

L'integration FluentCRM avancee : segmentation automatique, sequences email declenchees par une soumission, lead scoring.

Les quiz et sondages : champs note, champs calcul, resultats conditionnels. Pour la formation, l'evaluation, ou la generation de leads qualifies.

Si tu veux maitriser les formulaires WordPress, la Masterclass est la suite logique.

**[OUTRO - face camera]**

Merci d'avoir suivi ce Quick Start. Tu as maintenant deux formulaires professionnels sur ton site. Utilise-les, regarde les soumissions arriver dans le dashboard, et quand tu seras pret pour la suite - la Masterclass t'attend.

A bientot sur schoolsWP.

---

**Points cles** :
- Styler : presets (Flat recommande), couleurs de marque, bordures, bouton d'accent
- CSS custom facultatif : classe sur le conteneur + CSS additionnel
- Preview mobile : taille des champs, bouton pleine largeur, layout responsive
- Recap : 2 formulaires pro, anti-spam, notifications, FluentCRM, design personnalise
- Teaser Masterclass : logique conditionnelle, multi-step, paiements, FluentCRM avance, quiz

**Mots cles SEO** : personnaliser formulaire FluentForms, design formulaire WordPress, FluentForms CSS, formulaire WordPress mobile responsive

---

**Notes de production** :
- Face camera : intro (10 sec), recap (transition), outro (15 sec)
- Screencast : styler (90 sec), CSS custom (30 sec), preview mobile (45 sec)
- Slides : 2 slides (recap, Masterclass)
- Avant/apres : montrer cote a cote le formulaire default vs personnalise
- Fin : ecran de fin schoolsWP avec lien Masterclass
