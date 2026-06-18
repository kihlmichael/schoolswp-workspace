# Lecon 6.4 - Lire les resultats : signification statistique

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : 6 - A/B Testing et Analytics
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Comprendre la signification statistique sans mathematiques. Savoir quand un test est conclusif, eviter les deux erreurs classiques (conclure trop tot, ne jamais conclure), et appliquer la regle pratique des 200 visiteurs par variante.

---

## Script narration

**[INTRO - face camera]**

Ton test tourne depuis une semaine. Tu ouvres CartFlows et tu vois : variante A 3.2%, variante B 4.1%. La variante B a l'air meilleure. Tu es tente de la declarer gagnante tout de suite.

Stop. Avant de prendre une decision, tu dois comprendre un concept essentiel : la signification statistique. C'est ce qui fait la difference entre une decision basee sur des donnees et une decision basee sur du hasard.

Pas de panique. On ne va pas faire de maths. On va raisonner simplement.

---

**[SECTION 1 - La signification statistique, en clair]**

**[ECRAN - analogie piece de monnaie]**

Imagine que tu lances une piece de monnaie 10 fois. Tu obtiens 7 fois face et 3 fois pile. Est-ce que la piece est truquee ? Probablement pas. Avec 10 lancers, un ecart de 70/30 peut arriver par pur hasard.

Maintenant, lance-la 1000 fois. Si tu obtiens 700 fois face et 300 fois pile, la c'est different. L'ecart est le meme en pourcentage, mais avec 1000 lancers, il est extremement improbable que ce soit du hasard. La piece est probablement truquee.

C'est exactement le meme principe avec l'A/B testing. Quand ta variante B convertit a 4.1% contre 3.2% pour la variante A, la question est : est-ce que cet ecart est reel, ou est-ce du hasard lie a la taille de ton echantillon ?

La signification statistique repond a cette question. Elle te dit : "avec le volume de donnees que tu as, il y a X% de chances que cet ecart soit reel et pas du bruit."

En A/B testing, on considere qu'un resultat est significatif quand il y a au moins 95% de chances que l'ecart soit reel. En dessous de 95%, on ne conclut pas.

---

**[SECTION 2 - L'indicateur CartFlows]**

**[ECRAN - tableau de bord A/B Test avec indicateur couleur]**

CartFlows simplifie tout ca avec un indicateur visuel. Pas besoin de calculer quoi que ce soit.

Vert : le test est statistiquement significatif. L'ecart entre les variantes est reel. Tu peux declarer un gagnant en confiance.

Orange : le test n'est pas encore conclusif. L'ecart existe, mais il pourrait etre du au hasard. Il faut plus de donnees. Continue de faire tourner le test.

C'est tout. Vert = decision. Orange = patience.

---

**[SECTION 3 - Erreur numero 1 : conclure trop tot]**

**[ECRAN - graphique de convergence des resultats dans le temps]**

C'est l'erreur la plus frequente. Tu as lance ton test il y a trois jours. Tu as 47 visiteurs sur la variante A et 52 sur la variante B. La variante B convertit a 5.8% contre 2.1% pour A. L'ecart est enorme. Tu veux declarer B gagnante.

Ne le fais pas.

Avec 50 visiteurs par variante, un seul achat de plus ou de moins change completement les pourcentages. Si 3 personnes achevent sur B au lieu de 2, le taux passe de 3.8% a 5.8%. Un seul achat supplementaire cree l'illusion d'un ecart massif.

C'est du bruit statistique. L'indicateur CartFlows sera orange. Respecte-le.

Regle pratique : ne regarde meme pas les resultats avant d'avoir au moins 100 visiteurs par variante. Avant ca, les chiffres ne veulent rien dire.

---

**[SECTION 4 - Erreur numero 2 : ne jamais conclure]**

**[ECRAN - test qui tourne depuis 6 mois sans decision]**

L'erreur inverse existe aussi. Tu lances un test, les resultats sont serres, l'indicateur reste orange, et tu laisses tourner. Des semaines passent. Des mois. Le test tourne toujours. Tu ne prends aucune decision.

Le probleme : pendant que ce test tourne, tu ne peux pas en lancer un autre sur la meme page. Tu bloques ton processus d'optimisation. Et plus un test dure longtemps, plus il est expose a des facteurs externes qui polluent les resultats - changement de saison, promotion concurrente, mise a jour de Google.

Fixe une limite de temps. Si apres 4 a 6 semaines (ou 500 visiteurs par variante), l'indicateur est toujours orange, arrete le test. Les deux variantes sont equivalentes. Garde l'originale et passe au test suivant.

Un test qui ne conclut pas est une information utile : ce levier n'a pas d'impact mesurable sur tes conversions. Tu le sais maintenant. Tu peux investir ton temps ailleurs.

---

**[SECTION 5 - La regle pratique : 200 visiteurs, indicateur vert]**

**[ECRAN - checklist de decision]**

Voici la regle que tu vas appliquer a chaque test :

Minimum 200 visiteurs par variante. C'est le seuil plancher. En dessous, tu ne regardes meme pas les resultats.

Attends l'indicateur vert de CartFlows. C'est lui qui te dit que le volume est suffisant et que l'ecart est reel.

Si apres 500 visiteurs par variante l'indicateur est toujours orange, arrete le test. Les variantes sont equivalentes.

Et la derniere question : que faire si pas de difference significative ? C'est simple. Tu gardes la version originale. Elle fonctionne. Elle est en place. Elle est testee. Il n'y a aucune raison de la remplacer par une version qui ne fait pas mieux.

Note le resultat ("Test titre checkout : pas de difference significative - 520 visiteurs total, 4 semaines") et passe au test suivant dans ta hierarchie : CTA, prix, ou design.

---

**[OUTRO - face camera]**

La signification statistique n'est pas un concept abstrait. C'est ton garde-fou. Elle t'empeche de prendre des decisions sur du bruit et de confondre le hasard avec une amelioration reelle.

Retiens la regle : 200 visiteurs par variante, indicateur vert, et une limite de temps. Avec ca, chaque test que tu fais produit une decision fiable.

Dans la prochaine lecon, on va explorer le tableau de bord Analytics de CartFlows pour avoir une vue d'ensemble de la performance de tes funnels.

---

## Notes de production

- **Visuels** : analogie piece de monnaie (schema), indicateur couleur CartFlows (capture), graphique de convergence, checklist de decision
- **Captures d'ecran** : CartFlows Pro - tableau de bord A/B Test avec indicateurs vert et orange (3 captures minimum)
- **Ton** : pedagogique, desacralise les stats sans simplifier a l'exces
- **Duree estimee** : ~8 min a debit normal
- **Transition** : enchaine directement sur L6.5 (tableau de bord Analytics)
