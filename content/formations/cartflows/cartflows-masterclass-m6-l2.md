# Lecon 6.2 - Creer un split test sur une page checkout

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : 6 - A/B Testing et Analytics
- **Duree cible** : 10 min (~1400 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Savoir creer un A/B test sur une page checkout dans CartFlows Pro. Configurer la repartition du trafic, lancer le test, lire les premiers resultats et declarer un gagnant.

---

## Script narration

**[INTRO - face camera]**

Tu connais maintenant la theorie : une variable a la fois, volume suffisant, et commencer par le titre du checkout. Maintenant, on va le faire pour de vrai dans CartFlows.

Dans cette lecon, tu vas creer ton premier split test. On va cloner ta page checkout, modifier un seul element, configurer la repartition du trafic, et lancer le test. A la fin, tu sauras exactement comment CartFlows gere l'A/B testing.

---

**[SECTION 1 - Acceder a la fonction A/B Test]**

**[ECRAN - CartFlows > Flows > ton flow > step Checkout]**

Ouvre ton tableau de bord WordPress. Va dans CartFlows, puis Flows. Ouvre le flow que tu veux tester - par exemple ton funnel de vente principal.

Clique sur le step Checkout. C'est la page de paiement de ton funnel. En haut de la page, tu vois un onglet ou un bouton "A/B Test". C'est la que tout se passe.

Clique dessus. CartFlows t'affiche ton checkout actuel comme "Variante A" - c'est ta version de reference, celle qui est deja en ligne.

---

**[SECTION 2 - Creer la variante B]**

**[ECRAN - interface de creation de variante]**

Clique sur "Add New Variation" ou "Ajouter une variante". CartFlows clone ta page checkout existante. Tu obtiens une copie exacte : meme design, meme contenu, meme formulaire.

C'est le point de depart. Ta variante B est identique a la variante A. Maintenant, tu vas modifier un seul element.

Ouvre la variante B dans l'editeur. On va changer le titre de la page. Remplace le titre actuel par une alternative que tu veux tester. Par exemple, si ton titre A est "Formation WooCommerce Complete", ton titre B pourrait etre "Lance ta boutique en ligne en 7 jours".

Enregistre et ferme l'editeur. Tu as maintenant deux versions de ta page checkout qui different uniquement par le titre. C'est exactement ce qu'on veut.

---

**[SECTION 3 - Configurer la repartition du trafic]**

**[ECRAN - reglages de repartition du trafic]**

De retour dans les reglages A/B Test, tu vois les deux variantes avec un curseur de repartition du trafic.

La recommandation : 50/50. La moitie des visiteurs voit la variante A, l'autre moitie voit la variante B. C'est la repartition la plus equilibree et celle qui donne des resultats fiables le plus rapidement.

CartFlows utilise un systeme de cookies pour s'assurer qu'un meme visiteur voit toujours la meme variante. Si un client visite ta page checkout lundi et revient mercredi, il verra la meme version les deux fois. C'est important pour la fiabilite des resultats.

Tu peux ajuster la repartition - 70/30 par exemple - si tu veux limiter le risque en exposant moins de visiteurs a la nouvelle variante. Mais sauf raison specifique, reste sur 50/50. C'est le standard.

---

**[SECTION 4 - Lancer le test]**

**[ECRAN - activation du test]**

Une fois la repartition configuree, active le test. CartFlows commence immediatement a distribuer le trafic entre les deux variantes.

A partir de ce moment, ne touche a rien. Pas de modification du design. Pas de changement de prix. Pas de nouvelle campagne publicitaire qui enverrait un type de trafic different. Toute modification externe pendant le test pollue les resultats.

Le test tourne. Les visiteurs arrivent. CartFlows enregistre les conversions de chaque variante. Tu peux suivre les resultats en temps reel depuis le tableau de bord A/B Test.

---

**[SECTION 5 - Combien de temps attendre ?]**

**[ECRAN - tableau de resultats en cours avec indicateur de confiance]**

La tentation est forte de regarder les resultats au bout de 24 heures. Resiste. Les premiers resultats sont du bruit statistique. Avec 15 visiteurs par variante, un ecart de 20% ne signifie rien.

Attends d'avoir au minimum 100 visiteurs par variante. Idealement 200. CartFlows affiche un indicateur de signification statistique - un code couleur. Tant que l'indicateur n'est pas vert, les resultats ne sont pas conclusifs.

En pratique, selon ton volume de trafic, un test dure entre 1 et 4 semaines. Si tu as 50 visiteurs par jour sur ton checkout, le test sera conclusif en une semaine. Si tu en as 10 par jour, compte un mois.

---

**[SECTION 6 - Declarer le gagnant et archiver]**

**[ECRAN - declaration du gagnant dans CartFlows]**

L'indicateur est vert. La variante B convertit a 4.2% contre 3.1% pour la variante A. L'ecart est statistiquement significatif. Tu as ton gagnant.

Dans CartFlows, clique sur "Declare Winner" sur la variante B. CartFlows desactive la variante A et redirige 100% du trafic vers la variante gagnante. Le test est termine.

La variante perdante est archivee. Tu peux la retrouver si besoin, mais elle n'est plus servie aux visiteurs.

Note ce que tu as teste et le resultat. "Titre checkout : variante B (+35% conversion). Test du 15 au 29 mars, 412 visiteurs total." Ce journal de tests est precieux. Il t'evitera de retester des choses deja tranchees.

---

**[SECTION 7 - Et si les resultats sont similaires ?]**

**[ECRAN - resultats serres sans vainqueur clair]**

Ca arrive. Variante A : 3.5%. Variante B : 3.6%. L'indicateur reste orange meme apres 400 visiteurs. La difference n'est pas significative.

Dans ce cas, garde la variante originale. Si deux versions produisent des resultats equivalents, il n'y a aucune raison de changer. Tu passes au test suivant : le CTA, le prix, ou un autre element de ta hierarchie.

Un test sans vainqueur n'est pas un echec. C'est une information : ce levier specifique n'a pas d'impact mesurable. Tu elimines une hypothese et tu avances.

---

**[OUTRO - face camera]**

Tu sais maintenant creer un split test complet dans CartFlows : cloner le checkout, modifier une variable, repartir le trafic, attendre la signification statistique, et declarer le gagnant. C'est un processus que tu vas repeter a chaque optimisation.

Dans la prochaine lecon, on applique la meme methode aux order bumps et aux upsells. Parce que le checkout n'est pas la seule etape qu'on peut tester.

---

## Notes de production

- **Visuels** : captures d'ecran CartFlows (onglet A/B Test, creation variante, repartition trafic, indicateur statistique, declaration gagnant)
- **Captures d'ecran** : CartFlows Pro interface - flow > step Checkout > A/B Test (6 captures minimum)
- **Ton** : pratique et pas-a-pas, oriente action
- **Duree estimee** : ~10 min a debit normal
- **Transition** : enchaine directement sur L6.3 (tester bumps et upsells)
