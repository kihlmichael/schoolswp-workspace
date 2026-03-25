# Sequence Email FluentCRM — 5 emails

**Plugin** : FluentCRM
**Modele** : Freemium (gratuit + Pro a 129$/an)
**Lien affilie** : schoolswp.com/recommande/fluentcrm
**Objectif** : Presenter FluentCRM, demontrer la valeur, convertir via lien affilie
**Duree totale** : 12 jours

---

## Logique d'automation FluentCRM

### Declencheur

- **Tag applique** : `sequence-fluentcrm` (ajoute manuellement ou via formulaire/automation existante)

### Funnel de tags

| Tag | Moment | Usage |
|-----|--------|-------|
| `sequence-fluentcrm` | Entree dans la sequence | Declencheur |
| `fluentcrm-email-1-ouvert` | Ouverture email 1 | Scoring engagement |
| `fluentcrm-clic-decouverte` | Clic lien affilie (emails 1-3) | Identifie les curieux |
| `fluentcrm-clic-achat` | Clic lien affilie (emails 4-5) | Identifie les acheteurs potentiels |
| `fluentcrm-converti` | Achat confirme | Retire de la sequence |

### Regles d'automation

1. **Sortie anticipee** : Si le tag `fluentcrm-converti` est applique, retirer de la sequence immediatement.
2. **Relance conditionnelle** : Si email 3 non ouvert, ajouter un delai de 24h avant email 4 avec objet alternatif.
3. **Scoring** : Chaque ouverture +1 point, chaque clic +3 points. Score >= 7 au moment de l'email 4 = envoyer la version "push" de l'email 5.

### Schema d'automation FluentCRM

```
[Tag: sequence-fluentcrm]
    |
    v
[Email 1 — J0]
    |
    |- Attendre 3 jours
    v
[Email 2 — J3]
    |
    |- Attendre 3 jours
    v
[Email 3 — J6]
    |
    |- Condition : email 3 ouvert ?
    |   OUI → Attendre 2 jours → Email 4
    |   NON → Attendre 3 jours → Email 4 (objet alternatif)
    v
[Email 4 — J8 ou J9]
    |
    |- Attendre 3 jours
    v
[Email 5 — J11 ou J12]
    |
    v
[Retirer tag sequence-fluentcrm]
[Appliquer tag: sequence-fluentcrm-terminee]
```

---

## Email 1 — La decouverte (J0)

**Objet** : Le CRM que j'utilise tous les jours (il est gratuit)
**Pre-header** : Pas besoin de Mailchimp. Tout se passe dans WordPress.

---

Salut {{contact.first_name}},

Tu utilises quoi pour gerer tes contacts et envoyer tes emails ?

Mailchimp ? Brevo ? ConvertKit ?

Pendant longtemps, j'ai jongle entre WordPress d'un cote et un outil email de l'autre. Deux interfaces, deux logiques, des donnees qui ne se parlent pas.

Et puis j'ai installe FluentCRM.

**FluentCRM, c'est un CRM directement dans WordPress.** Pas un service externe. Pas d'abonnement mensuel qui grimpe avec ta liste. Un plugin.

Ce que tu as dans la version gratuite (celle que tu peux installer maintenant) :

- **Gestion des contacts** avec tags et listes
- **Automations basiques** : quand quelqu'un s'inscrit, tu peux declencher une sequence
- **Emails illimites** — tu paies ton hebergeur SMTP, pas FluentCRM
- **Tableau de bord** dans WordPress, au meme endroit que ton contenu

J'utilise FluentCRM depuis un an pour toutes les automations schoolsWP. C'est devenu le centre nerveux de mon business WordPress.

Si tu veux voir a quoi ca ressemble :
**[Decouvrir FluentCRM (version gratuite)](https://schoolswp.com/recommande/fluentcrm)**

Dans le prochain email, je te montre concretement ce que j'ai mis en place avec — et pourquoi ca change la donne quand tout est dans WordPress.

A bientot,
Michael

*P.S. — Oui, c'est un lien affilie. Je ne recommande que les outils que j'utilise reellement. FluentCRM tourne sur schoolswp.com depuis plus d'un an.*

---

**Parametres FluentCRM :**
- Delai avant email 2 : 3 jours
- Tag sur clic lien : `fluentcrm-clic-decouverte`

---

## Email 2 — Le cas concret (J3)

**Objet** : Mon automation FluentCRM preferee (5 min a creer)
**Pre-header** : Un nouveau contact s'inscrit → voici ce qui se passe automatiquement.

---

Salut {{contact.first_name}},

La derniere fois, je te presentais FluentCRM. Aujourd'hui, je te montre ce que ca donne en vrai.

**Mon automation numero 1 : l'accueil des nouveaux inscrits.**

Voici ce qui se passe quand quelqu'un s'inscrit sur schoolswp.com :

1. FluentCRM lui ajoute le tag `nouvel-inscrit`
2. Une sequence de 3 emails se declenche automatiquement
3. Selon les liens sur lesquels il clique, un tag de centre d'interet est ajoute (LMS, CRM, SEO...)
4. Au bout de 7 jours, il recoit du contenu personnalise en fonction de ses interets

**Tout ca se configure en quelques clics dans l'interface FluentCRM, directement dans WordPress.**

Pas de Zapier. Pas de webhook a configurer. Pas de code.

Tu crees un "Funnel" (c'est le nom de leur editeur d'automations), tu choisis un declencheur, tu enchaines les actions. C'est visuel et logique.

Ce qui m'a convaincu par rapport aux solutions externes :

- **Mes donnees restent chez moi** — pas sur les serveurs de Mailchimp
- **Pas de limite de contacts** — la version gratuite ne bride pas ta liste
- **L'integration WordPress est native** — formulaires, pages, WooCommerce, tout communique

Et honnement ? La version gratuite suffit pour 80% des besoins. J'ai commence avec, et je suis passe en Pro seulement quand j'ai eu besoin des sequences email avancees.

**[Tester FluentCRM sur ton WordPress](https://schoolswp.com/recommande/fluentcrm)**

Demain... non, dans 3 jours — je te parle du moment ou la version gratuite ne suffit plus. Et de ce que le Pro debloque.

Michael

---

**Parametres FluentCRM :**
- Delai avant email 3 : 3 jours
- Tag sur clic lien : `fluentcrm-clic-decouverte`

---

## Email 3 — La limite du gratuit (J6)

**Objet** : A quel moment FluentCRM gratuit ne suffit plus
**Pre-header** : Spoiler : ca depend de ce que tu vends.

---

Salut {{contact.first_name}},

Tu te demandes peut-etre : "Si la version gratuite est si bien, pourquoi payer ?"

Bonne question. Voici ma reponse honnete.

**La version gratuite de FluentCRM suffit si :**

- Tu geres une liste de contacts avec des tags
- Tu envoies des newsletters ponctuelles
- Tu as des automations simples (inscription → email de bienvenue)
- Tu ne vends pas (encore) de produits en ligne

**La version Pro devient necessaire quand :**

- Tu veux des **sequences email avancees** — par exemple, une sequence de vente en 5 emails declenchee par un comportement precis
- Tu utilises **WooCommerce** et tu veux segmenter tes clients par produit achete, panier abandonne, montant depense
- Tu as besoin de **rapports detailles** — taux d'ouverture par sequence, revenus generes par automation
- Tu veux de l'**A/B testing** sur tes objets d'email

Pour schoolsWP, le declencheur a ete WooCommerce. Le jour ou j'ai commence a vendre des formations, j'avais besoin de :

- Taguer automatiquement les acheteurs par produit
- Declencher des sequences post-achat personnalisees
- Suivre le revenu genere par chaque automation

**Sans FluentCRM Pro, j'aurais du utiliser un outil externe + des webhooks + du code custom.** Avec, tout est dans WordPress.

Le prix : **129$/an**. Pour un CRM complet avec automations avancees et integration ecommerce. Compare a ActiveCampaign (228$/an minimum), Mailchimp (156$/an pour des fonctions similaires), ou ConvertKit (300$/an) — le calcul est vite fait.

Je ne te dis pas de passer en Pro maintenant. Installe la version gratuite, teste pendant 2-3 semaines. Tu verras naturellement si tu as besoin du Pro.

**[Commencer avec FluentCRM](https://schoolswp.com/recommande/fluentcrm)**

Dans mon prochain email, je te donne ma configuration exacte — les tags, les automations, la structure que j'utilise pour schoolsWP.

Michael

---

**Parametres FluentCRM :**
- Delai avant email 4 : 2 jours (si ouvert) / 3 jours (si non ouvert)
- Tag sur clic lien : `fluentcrm-clic-decouverte`
- Condition : verifier ouverture email 3

---

## Email 4 — La preuve par l'usage (J8 ou J9)

**Objet** : Ma config FluentCRM exacte (tags, automations, resultats)
**Objet alternatif** (si email 3 non ouvert) : Ce que FluentCRM a change dans mon business WordPress
**Pre-header** : 12 mois de recul. Voici les chiffres.

---

Salut {{contact.first_name}},

Ca fait un an que FluentCRM gere l'integralite de mes contacts et automations sur schoolsWP. Voici exactement comment c'est organise.

### Ma structure de tags

```
Interets :     lms | crm | seo | automatisation | ecommerce
Statut :       prospect | client | vip
Source :       blog | formation | webinar | partenaire
Comportement : actif-30j | inactif-60j | clic-affiliation
```

### Mes 5 automations principales

| Automation | Declencheur | Actions |
|-----------|------------|---------|
| Accueil | Inscription formulaire | 3 emails + tag interet selon clics |
| Nurturing | Tag `prospect` + interet | Contenu cible hebdo pendant 4 semaines |
| Post-achat | Achat WooCommerce | Sequence onboarding 5 emails |
| Reactivation | Tag `inactif-60j` | 2 emails + nettoyage si pas de reaction |
| Affiliation | Clic lien affilie | Tag produit + sequence avis |

### Les resultats apres 12 mois

- **Taux d'ouverture moyen** : 42% (contre 28% quand j'etais sur Mailchimp)
- **Temps de gestion** : 30 min/semaine max — les automations font le travail
- **Cout** : 129$/an au lieu de ~300$/an sur une plateforme externe

La difference de taux d'ouverture vient d'un truc simple : comme FluentCRM est dans WordPress, je peux segmenter beaucoup plus finement. Je sais exactement quelles pages un contact a visitees, quels produits il a regardes, quels emails il a ouverts. Et je personnalise en consequence.

**Le vrai avantage, c'est pas le prix. C'est le controle.** Tes donnees, tes regles, ta logique.

**[Obtenir FluentCRM Pro a 129$/an](https://schoolswp.com/recommande/fluentcrm)**

Dernier email demain — je reponds aux 3 objections que j'entends le plus souvent.

Michael

---

**Parametres FluentCRM :**
- Delai avant email 5 : 3 jours
- Tag sur clic lien : `fluentcrm-clic-achat`

---

## Email 5 — La decision (J11 ou J12)

**Objet** : FluentCRM — les 3 questions qu'on me pose toujours
**Pre-header** : Delivrabilite, support, migration. Reponses franches.

---

Salut {{contact.first_name}},

Dernier email de cette serie sur FluentCRM. Je reponds aux 3 objections que j'entends le plus souvent.

---

**"La delivrabilite n'est pas un probleme avec un CRM WordPress ?"**

FluentCRM ne gere pas l'envoi lui-meme. Il utilise ton service SMTP (Amazon SES, SendGrid, ou meme le SMTP de ton hebergeur). La delivrabilite depend donc de ton SMTP, pas de FluentCRM.

Mon setup : FluentCRM + FluentSMTP (gratuit, du meme editeur) + Amazon SES. Cout d'envoi : ~0.10$ pour 1 000 emails. Delivrabilite : excellente.

**"Et si j'ai un probleme, le support est bon ?"**

En un an, j'ai contacte le support 3 fois. Reponse en moins de 24h a chaque fois, avec des solutions concretes. L'equipe derriere FluentCRM (WPManageNinja) maintient aussi FluentForms et Ninja Tables — c'est un editeur serieux, pas un side-project.

La communaute Facebook est aussi active — beaucoup de cas d'usage partages par d'autres utilisateurs WordPress.

**"Je suis deja sur Mailchimp/ConvertKit, la migration est penible ?"**

FluentCRM a un importateur CSV integre. Tu exportes tes contacts depuis ton outil actuel, tu importes dans FluentCRM avec les tags. Les automations, par contre, tu dois les recreer — mais c'est l'occasion de les simplifier.

J'ai migre depuis Mailchimp en une apres-midi. Le plus long : reconfigurer mes formulaires pour pointer vers FluentCRM (30 minutes).

---

### En resume

| | Gratuit | Pro (129$/an) |
|--|---------|---------------|
| Contacts illimites | Oui | Oui |
| Tags et listes | Oui | Oui |
| Automations basiques | Oui | Oui |
| Sequences email avancees | Non | **Oui** |
| Integration WooCommerce | Non | **Oui** |
| Rapports detailles | Non | **Oui** |
| A/B testing | Non | **Oui** |

Mon conseil : **installe la version gratuite aujourd'hui, teste pendant 2 semaines.** Si tu as besoin du Pro, le lien ci-dessous te donne acces a la licence annuelle.

**[Installer FluentCRM maintenant](https://schoolswp.com/recommande/fluentcrm)**

Si tu as des questions sur la configuration ou la migration, reponds a cet email. Je t'aide.

Michael

*P.S. — Les liens vers FluentCRM dans cette serie sont des liens affilies. Si tu passes par la, je recois une commission — sans surcout pour toi. C'est une facon de soutenir schoolsWP tout en accedant a un outil que je recommande sincerement.*

---

**Parametres FluentCRM :**
- Tag sur clic lien : `fluentcrm-clic-achat`
- Action finale : retirer tag `sequence-fluentcrm`, appliquer tag `sequence-fluentcrm-terminee`
- Si aucun clic sur les 5 emails : appliquer tag `fluentcrm-non-interesse`

---

## Recapitulatif de la sequence

| # | Jour | Objet | Angle | CTA |
|---|------|-------|-------|-----|
| 1 | J0 | Le CRM que j'utilise tous les jours (il est gratuit) | Decouverte + probleme resolu | Decouvrir (gratuit) |
| 2 | J3 | Mon automation FluentCRM preferee (5 min a creer) | Cas concret + demo | Tester |
| 3 | J6 | A quel moment FluentCRM gratuit ne suffit plus | Gratuit vs Pro + prix | Commencer (gratuit) |
| 4 | J8-9 | Ma config FluentCRM exacte | Preuve + resultats 12 mois | Obtenir Pro |
| 5 | J11-12 | Les 3 questions qu'on me pose toujours | Objections + tableau comparatif | Installer |

## KPIs a suivre dans FluentCRM

- **Taux d'ouverture par email** — objectif : > 35%
- **Taux de clic sur le lien affilie** — objectif : > 5%
- **Taux de conversion globale** (clic → achat) — objectif : > 2%
- **Taux de desabonnement** — alerte si > 1% par email
- **Score d'engagement moyen** en fin de sequence
