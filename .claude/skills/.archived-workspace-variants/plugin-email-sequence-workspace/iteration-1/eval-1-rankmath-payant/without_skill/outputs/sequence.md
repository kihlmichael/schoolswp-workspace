# Sequence email -- Decouverte RankMath Pro

**Objectif** : convertir les abonnes schoolsWP en utilisateurs RankMath Pro via le lien affilie.
**Lien affilie** : [schoolswp.com/recommande/rankmath](https://schoolswp.com/recommande/rankmath)
**Nombre d'emails** : 7
**Duree totale** : 14 jours
**Segmentation entree** : abonnes actifs (ouvert au moins 1 email dans les 90 derniers jours)

---

## Logique d'automation (FluentCRM / n8n)

```
[Declencheur] Abonne entre dans la sequence
    |
    v
Email 1 (J0) -- Le probleme SEO silencieux
    |
    v
[Delai 2 jours]
    |
    v
Email 2 (J2) -- Mon avant/apres avec RankMath
    |
    v
[Condition] A clique sur le lien affilie ?
    |--- OUI --> Tag "rankmath-interesse" + Email 5 (avance vers offre directe)
    |--- NON --> Continue
    |
    v
[Delai 2 jours]
    |
    v
Email 3 (J4) -- La fonctionnalite qui change tout
    |
    v
[Delai 2 jours]
    |
    v
Email 4 (J6) -- Objections honnetes
    |
    v
[Condition] A clique sur le lien affilie (cumul) ?
    |--- OUI --> Tag "rankmath-interesse" + saute a Email 6
    |--- NON --> Continue
    |
    v
[Delai 3 jours]
    |
    v
Email 5 (J9) -- Le cout reel de ne rien faire
    |
    v
[Delai 3 jours]
    |
    v
Email 6 (J12) -- Recapitulatif + decision
    |
    v
[Delai 2 jours]
    |
    v
Email 7 (J14) -- Dernier mot
    |
    v
[Fin de sequence]
    |
    v
[Post-sequence]
    Tag "rankmath-sequence-terminee"
    Si tag "rankmath-interesse" ET pas d'achat --> relance dans 30 jours
    Si aucun clic sur la sequence --> tag "rankmath-pas-interesse" (exclure des futures promos RankMath)
```

### Tags FluentCRM utilises

| Tag | Declencheur | Utilite |
|-----|-------------|---------|
| `rankmath-sequence-active` | Entree dans la sequence | Eviter les doublons |
| `rankmath-interesse` | Clic sur lien affilie | Segmentation future |
| `rankmath-sequence-terminee` | Fin de sequence | Tracking |
| `rankmath-pas-interesse` | 0 clic apres 7 emails | Exclusion futures campagnes |
| `rankmath-client` | Achat confirme (webhook) | Sortie immediate de sequence |

### Regle de sortie globale

Si l'abonne recoit le tag `rankmath-client` (achat confirme via webhook d'affiliation), il sort immediatement de la sequence et recoit un email de bienvenue/onboarding separe.

---

## Email 1 -- Le probleme SEO silencieux

**Jour** : J0
**Objet** : Ton site WordPress perd du trafic sans que tu le saches
**Preview text** : Et tu n'as probablement aucun outil pour le detecter.

---

Salut {prenom},

Je vais etre direct : la plupart des sites WordPress perdent du trafic organique chaque mois. Pas a cause d'une penalite Google. Pas a cause d'un mauvais contenu.

A cause de problemes techniques SEO que personne ne surveille.

Des balises title mal optimisees. Des redirections cassees. Des schemas markup absents. Des meta descriptions en doublon.

Le pire ? Ces erreurs sont invisibles a l'oeil nu. Ton site a l'air normal. Mais Google, lui, voit tout.

Pendant 2 ans, j'ai gere le SEO de schoolsWP "a la main". Je verifiais mes articles un par un. Je corrigeais les erreurs quand je les trouvais -- c'est-a-dire rarement.

Mon score SEO moyen : 60/100.

Pas catastrophique. Mais largement insuffisant pour ranker sur des requetes concurrentielles.

Il y a 8 mois, j'ai change un seul element dans mon workflow. Un seul.

Je t'en parle dans le prochain email.

A bientot,
Michael

P.S. Si tu veux deja savoir de quoi il s'agit, c'est ici : [schoolswp.com/recommande/rankmath](https://schoolswp.com/recommande/rankmath)

---

## Email 2 -- Mon avant/apres avec RankMath Pro

**Jour** : J2
**Objet** : De 60 a 85/100 en SEO -- voici ce que j'ai change
**Preview text** : 8 mois de donnees reelles sur schoolsWP.

---

Salut {prenom},

Dans le dernier email, je te disais qu'un seul changement avait transforme mes resultats SEO.

Ce changement, c'est RankMath Pro.

Pas un cours. Pas une strategie secrete. Un outil.

Voici mes chiffres reels sur 8 mois :

- **Score SEO moyen** : 60 --> 85/100
- **Erreurs techniques detectees au premier mois** : 47 (dont 12 critiques que je ne soupconnais pas)
- **Temps passe sur l'optimisation on-page** : divise par 3

Ce qui a change concretement :

**1. L'audit SEO on-page en temps reel**
Chaque article que je publie passe par un scoring automatique. RankMath me dit exactement quoi corriger -- titre, meta, densite de mot-cle, lisibilite, liens internes. Plus besoin de deviner.

**2. Le suivi de positions integre**
Avant, j'utilisais un outil separe (payant) pour tracker mes positions Google. RankMath Pro le fait directement dans WordPress. Je vois mes progressions sans quitter mon dashboard.

**3. Les schemas markup automatiques**
FAQ, HowTo, Article, Product -- RankMath genere le balisage structure sans toucher une ligne de code. Resultat : des rich snippets qui augmentent mon CTR.

**4. Les redirections**
Chaque fois que je modifie un slug, RankMath cree automatiquement une redirection 301. Plus de liens casses, plus de 404 inutiles.

Le tout pour 59 $/an. Pour un seul site.

Pour mettre ca en perspective : un outil de suivi de positions seul coute souvent plus cher.

Si tu veux voir par toi-meme : [schoolswp.com/recommande/rankmath](https://schoolswp.com/recommande/rankmath)

A bientot,
Michael

---

## Email 3 -- La fonctionnalite qui change tout

**Jour** : J4
**Objet** : La fonctionnalite RankMath que j'utilise tous les jours
**Preview text** : Ce n'est pas celle que tu crois.

---

Salut {prenom},

Si je devais garder une seule fonctionnalite de RankMath Pro, ce ne serait pas l'audit SEO. Ce ne serait pas le suivi de positions.

Ce serait le **Content AI + Schema Markup automatique**.

Pourquoi ? Parce que c'est la fonctionnalite qui genere des resultats visibles dans Google sans effort supplementaire.

Voici comment ca marche en pratique :

1. Tu rediges ton article normalement dans WordPress
2. RankMath detecte le type de contenu (tutoriel, comparatif, FAQ, produit...)
3. Il genere automatiquement le schema markup adapte
4. Google affiche des rich snippets -- etoiles, FAQ deroulantes, etapes numerotees

Le resultat concret sur schoolsWP :

- 3 articles avec FAQ schema ont vu leur **CTR augmenter de 15 a 25 %** en 6 semaines
- 1 article tutoriel avec HowTo schema est passe de la **position 7 a la position 3** (le rich snippet attire plus de clics, ce qui ameliore le ranking)

Et tout ca sans avoir ecrit une seule ligne de JSON-LD.

Les plugins SEO gratuits proposent des schemas basiques. RankMath Pro va plus loin avec 20+ types de schemas, la detection automatique, et la validation en temps reel.

C'est ce genre de detail qui fait la difference entre "avoir un plugin SEO" et "avoir un avantage SEO reel".

Decouvre RankMath Pro ici : [schoolswp.com/recommande/rankmath](https://schoolswp.com/recommande/rankmath)

A bientot,
Michael

---

## Email 4 -- Objections honnetes

**Jour** : J6
**Objet** : Les 3 raisons de NE PAS prendre RankMath Pro
**Preview text** : Je joue cartes sur table.

---

Salut {prenom},

Je pourrais te dire que RankMath Pro est parfait. Ce serait plus simple pour moi.

Mais ce n'est pas mon style. Voici les vraies limites que j'ai constatees en 8 mois d'utilisation.

**Objection 1 : "59 $/an, c'est un cout supplementaire"**

C'est vrai. Et je ne vais pas te dire que c'est "rien". Pour un site qui ne genere pas encore de revenus, chaque dollar compte.

Mais voici mon calcul : avant RankMath Pro, j'utilisais un outil de suivi de positions a 29 $/mois (348 $/an). Plus un plugin SEO gratuit qui ne faisait que la moitie du travail.

RankMath Pro a 59 $/an remplace les deux. J'economise 289 $/an.

**Objection 2 : "Yoast / All-in-One SEO font la meme chose"**

En surface, oui. En pratique, non.

Yoast Premium coute 99 $/an et n'inclut pas le suivi de positions. All-in-One SEO Pro demarre a 49 $/an mais le schema markup avance est reserve aux plans superieurs (199 $/an).

RankMath Pro a 59 $/an inclut tout : audit, positions, schemas, redirections.

**Objection 3 : "Je n'ai pas le temps de configurer un nouvel outil"**

L'assistant de configuration de RankMath prend 10 minutes. Il importe automatiquement les reglages de Yoast ou AIOSEO si tu migres.

J'ai fait la migration sur schoolsWP un samedi matin. En 15 minutes, tout etait en place.

**Alors, pour qui RankMath Pro n'est PAS fait ?**

- Si tu publies moins d'un article par mois et que le SEO n'est pas ta priorite
- Si tu es satisfait de tes resultats actuels et que tu ne cherches pas a progresser
- Si tu geres 50+ sites (la licence Business a 199 $/an serait plus adaptee)

Pour tous les autres cas -- et surtout si tu crees du contenu regulierement sur WordPress -- c'est l'investissement SEO le plus rentable que je connaisse.

A toi de voir : [schoolswp.com/recommande/rankmath](https://schoolswp.com/recommande/rankmath)

Michael

---

## Email 5 -- Le cout reel de ne rien faire

**Jour** : J9
**Objet** : Combien te coute ton SEO "gratuit" ?
**Preview text** : Le calcul que personne ne fait.

---

Salut {prenom},

Faisons un calcul rapide.

Disons que ton site recoit 1 000 visiteurs/mois via Google. C'est un chiffre modeste.

Si tu ameliores ton SEO technique et que ton trafic augmente de 20 % (ce qui est conservateur avec un audit systematique), tu passes a 1 200 visiteurs/mois.

200 visiteurs supplementaires par mois. 2 400 par an.

Maintenant, combien vaut un visiteur pour toi ?

- Si tu vends une formation a 297 EUR avec un taux de conversion de 1 % : 2 400 visiteurs = 24 ventes = **7 128 EUR**
- Si tu fais de l'affiliation avec un revenu moyen de 2 EUR/visiteur : **4 800 EUR**
- Si tu vends des services freelance et que 1 visiteur sur 200 devient client a 1 500 EUR : **18 000 EUR**

Dans tous les cas, le retour sur investissement de 59 $/an est absurde.

Mais voici ce que ce calcul ne montre pas :

**Le cout compose de l'inaction.**

Chaque mois ou ton SEO technique reste a 60/100, tu accumules de la dette technique. Des erreurs non corrigees. Des opportunites de rich snippets manquees. Des positions qui stagnent ou reculent.

Et pendant ce temps, tes concurrents qui utilisent un outil d'audit SEO voient leurs scores monter. Chaque article qu'ils publient est mieux optimise que le precedent.

L'ecart se creuse. Et il est de plus en plus difficile a rattraper.

Je ne te dis pas de prendre RankMath Pro aujourd'hui. Je te dis de prendre une decision. N'importe laquelle.

- Utilise RankMath Pro : [schoolswp.com/recommande/rankmath](https://schoolswp.com/recommande/rankmath)
- Utilise un autre outil payant qui fait le meme travail
- Ou decide consciemment que le SEO n'est pas ta priorite

Mais ne reste pas dans le flou. C'est la pire option.

Michael

---

## Email 6 -- Recapitulatif + decision

**Jour** : J12
**Objet** : RankMath Pro -- tout ce que tu dois savoir pour decider
**Preview text** : Le recapitulatif complet en 2 minutes.

---

Salut {prenom},

On arrive a la fin de cette serie. Voici un recapitulatif clair pour que tu puisses decider en connaissance de cause.

### Ce qu'est RankMath Pro

Un plugin SEO WordPress premium qui regroupe 4 outils en 1 :

| Fonctionnalite | Ce que ca fait | Alternative separee |
|----------------|----------------|---------------------|
| Audit SEO on-page | Score en temps reel + recommandations par article | Surfer SEO (59 $/mois) |
| Suivi de positions | Tracking de mots-cles directement dans WP | SE Ranking (39 $/mois) |
| Schema markup | 20+ types generes automatiquement | Schema Pro (79 $/an) |
| Redirections | 301 automatiques + gestionnaire | Redirection plugin (gratuit mais basique) |

### Prix

**59 $/an pour 1 site.** Pas de version mensuelle. Pas de frais caches.

Pour comparaison :
- Yoast Premium : 99 $/an (sans suivi de positions)
- AIOSEO Pro : 49 $/an (schemas avances en option a 199 $/an)
- SEMrush : 129 $/mois (complet mais 25x plus cher)

### Mes resultats sur schoolsWP (8 mois)

- Score SEO moyen : 60 --> 85/100
- Temps d'optimisation on-page : divise par 3
- 47 erreurs techniques detectees au premier mois

### Pour qui c'est fait

- Createurs de contenu WordPress qui publient regulierement
- Freelances et formateurs qui dependent du trafic organique
- Sites de niche et blogs d'autorite

### Pour qui ce n'est PAS fait

- Sites qui ne publient presque jamais
- Projets ou le SEO n'est pas un levier de croissance
- Multi-sites (50+) -- la licence Business est plus adaptee

### Ma recommandation

Si tu publies au moins 2 articles par mois et que le SEO est un canal important pour toi, RankMath Pro est le meilleur rapport qualite/prix du marche. C'est l'outil que j'utilise chaque jour.

Prends-le ici (lien affilie -- transparence totale) : [schoolswp.com/recommande/rankmath](https://schoolswp.com/recommande/rankmath)

Si tu as des questions, reponds a cet email. Je lis tout.

Michael

---

## Email 7 -- Dernier mot

**Jour** : J14
**Objet** : Derniere chose sur RankMath (et apres, on passe a autre chose)
**Preview text** : Un conseil, que tu prennes RankMath ou non.

---

Salut {prenom},

Dernier email de cette serie sur RankMath Pro. Promis.

Que tu decides de le prendre ou non, voici mon conseil :

**Arrete de faire du SEO a l'aveugle.**

Publier du contenu sans verifier l'optimisation on-page, c'est comme envoyer des emails sans verifier le taux d'ouverture. Tu travailles, mais tu ne sais pas si ca marche.

Utilise un outil. N'importe lequel. Mais utilise-en un.

RankMath Pro est celui que j'utilise et que je recommande parce qu'il m'a donne des resultats mesurables pour un prix raisonnable. Mais c'est ton choix.

Si tu veux essayer : [schoolswp.com/recommande/rankmath](https://schoolswp.com/recommande/rankmath)

A partir du prochain email, on revient au contenu habituel -- WordPress, automation, et strategies pour developper ton activite en ligne.

A bientot,
Michael

---

## Configuration FluentCRM

### Sequence

```
Nom : [Affiliation] RankMath Pro -- Decouverte
Tag d'entree : rankmath-sequence-active
Condition d'entree : abonne actif (ouverture 90j) ET PAS tag "rankmath-client" ET PAS tag "rankmath-sequence-terminee"
```

### Workflow d'automation detaille

```
1. DECLENCHEUR : Tag ajoute "rankmath-sequence-active"
   |
2. ATTENDRE : 0 min
   |
3. ENVOYER : Email 1 -- Le probleme SEO silencieux
   |
4. ATTENDRE : 2 jours
   |
5. CONDITION : Tag "rankmath-client" present ?
   |-- OUI --> FIN (email de bienvenue separe)
   |-- NON --> continuer
   |
6. ENVOYER : Email 2 -- Mon avant/apres
   |
7. ATTENDRE : 1 jour
   |
8. CONDITION : A clique sur schoolswp.com/recommande/rankmath (emails 1 ou 2) ?
   |-- OUI --> Ajouter tag "rankmath-interesse" --> sauter a etape 16 (Email 5)
   |-- NON --> continuer
   |
9. ATTENDRE : 1 jour (total J4)
   |
10. ENVOYER : Email 3 -- Schema markup
    |
11. ATTENDRE : 2 jours
    |
12. ENVOYER : Email 4 -- Objections
    |
13. ATTENDRE : 1 jour
    |
14. CONDITION : A clique sur le lien affilie (cumul emails 1-4) ?
    |-- OUI --> Ajouter tag "rankmath-interesse" --> sauter a etape 18 (Email 6)
    |-- NON --> continuer
    |
15. ATTENDRE : 2 jours (total J9)
    |
16. ENVOYER : Email 5 -- Cout de l'inaction
    |
17. ATTENDRE : 3 jours (total J12)
    |
18. ENVOYER : Email 6 -- Recapitulatif
    |
19. ATTENDRE : 2 jours (total J14)
    |
20. ENVOYER : Email 7 -- Dernier mot
    |
21. RETIRER tag : rankmath-sequence-active
22. AJOUTER tag : rankmath-sequence-terminee
23. CONDITION : tag "rankmath-interesse" present ET PAS tag "rankmath-client" ?
    |-- OUI --> Ajouter tag "rankmath-relance-30j" (sequence de relance dans 30 jours)
    |-- NON --> CONDITION : 0 clic total sur la sequence ?
        |-- OUI --> Ajouter tag "rankmath-pas-interesse"
        |-- NON --> fin
    |
24. FIN
```

### Webhook d'achat (sortie anticipee)

Configurer un webhook sur la plateforme d'affiliation RankMath pour recevoir les conversions :

```
URL : https://schoolswp-n8n.wp1.host/webhook/rankmath-conversion
Methode : POST
Payload attendu : { "email": "...", "product": "rankmath-pro", "amount": 59 }
```

Workflow n8n associe :

```
[Webhook] --> [FluentCRM API : ajouter tag "rankmath-client"]
          --> [FluentCRM API : retirer de la sequence active]
          --> [Envoyer email de bienvenue/onboarding]
```

---

## Metriques a suivre

| Metrique | Objectif | Outil |
|----------|----------|-------|
| Taux d'ouverture moyen | > 35 % | FluentCRM |
| Taux de clic sur lien affilie | > 8 % | FluentCRM + UTM |
| Taux de conversion (clic --> achat) | > 3 % | Dashboard affiliation RankMath |
| Taux de desabonnement sur la sequence | < 1 % | FluentCRM |
| Revenu genere | Tracking mensuel | Dashboard affiliation |

### UTM recommandes

```
https://schoolswp.com/recommande/rankmath?utm_source=fluentcrm&utm_medium=email&utm_campaign=rankmath-discovery&utm_content=email-{numero}
```

Remplacer `{numero}` par 1 a 7 pour tracker quel email convertit le mieux.

---

## Notes d'implementation

1. **Test A/B** : tester les objets des emails 1 et 5 (les plus critiques -- entree de sequence et relance mid-sequence)
2. **Timing d'envoi** : programmer les envois a 9h00 heure locale du destinataire (mardi-jeudi de preference)
3. **Repondeur** : surveiller les reponses aux emails 4 et 6 -- les objections non traitees sont des opportunites de contenu
4. **Exclusions** : exclure de la sequence les abonnes deja tagges `rankmath-client` ou `rankmath-sequence-terminee`
5. **Conformite** : chaque email contient un lien de desabonnement (automatique FluentCRM) et la mention "lien affilie" est explicite dans l'email 6
