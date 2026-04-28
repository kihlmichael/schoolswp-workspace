---
name: plugin-email-sequence
description: |
  Génère une séquence email complète (3 à 7 emails) pour faire découvrir un plugin ou outil
  WordPress via affiliation, plus la logique d'automation FluentCRM (tags, conditions, tracking).
  Style schoolsWP : éducation → valeur → conversion, zéro hype.
  Déclenche ce skill dès que l'utilisateur veut créer une séquence email pour un plugin WordPress,
  promouvoir un outil par email, construire un drip campaign affilié, rédiger des emails de
  découverte produit, ou monter l'automation FluentCRM associée — même s'il ne dit pas
  explicitement "séquence" (ex: "je veux présenter RankMath à ma liste", "envoyer des emails
  pour ClickWhale", "faire découvrir TutorLMS par email").
  Couvre aussi les outils payants seuls (sans version gratuite) et les outils 100% gratuits.
  NE PAS utiliser pour : séquence de bienvenue newsletter / welcome sequence post-inscription à un lead magnet (voir lead-magnet-schoolswp), recyclage d'un email reçu en contenus dérivés (voir email-to-content), copy de page de vente d'offre propre (voir mini-offre-page-de-vente), landing page d'affiliation tiers (voir landing-page-factory).
---

# Plugin Email Sequence — schoolsWP

Produis une séquence email pour faire découvrir un plugin ou outil WordPress à une audience
existante, avec la logique d'automation FluentCRM prête à implémenter.

Le principe : éduquer d'abord, vendre ensuite. Chaque email a un rôle précis dans la progression
du lecteur — de "je ne connais pas cet outil" à "je l'installe et je l'utilise".

---

## Entrées attendues

| Entrée | Obligatoire | Exemple |
|---|---|---|
| Nom du plugin/outil | oui | ClickWhale |
| Problème résolu | oui | Liens affiliés impossibles à traquer |
| URL affilié ou lien officiel | oui | schoolswp.com/recommande/clickwhale |
| Modèle économique | oui | Freemium / Payant seul / 100% gratuit |
| Fonctionnalités clés (3-5) | oui | Cloaking, tracking clics, centralisation |
| Fonctionnalités Pro (si freemium) | non | Groupes, UTM auto, stats géo |
| Prix (si payant) | non | 49€/an |
| Expérience perso avec l'outil | non | "Utilisé 30 jours, mes 3 liens les plus cliqués n'étaient pas ceux que je pensais" |
| Audience cible | non (défaut : abonnés newsletter schoolsWP) | Freelances WordPress |
| Nombre d'emails souhaité | non (défaut : 5) | 3, 5 ou 7 |

Si une info obligatoire manque, demander avant de produire. Ne jamais inventer de fonctionnalités
ou de résultats.

---

## Structure de la séquence

### Séquence standard (5 emails — défaut)

| Email | Jour | Angle | Rôle | CTA |
|---|---|---|---|---|
| 1 | J0 | Le problème | Créer la prise de conscience | Teaser email suivant |
| 2 | J2 | La découverte | Éduquer sur l'outil | Lien vers article/tuto |
| 3 | J4 | La preuve | Cas concret, résultats réels | Lien installation/essai |
| 4 | J7 | Gratuit vs Pro / Approfondissement | Qualifier vers l'offre | Lien vers comparatif |
| 5 | J10 | La décision | Convertir sans pression | Lien affilié direct |

### Séquence courte (3 emails — outils simples)

| Email | Jour | Angle |
|---|---|---|
| 1 | J0 | Problème + découverte (fusionné) |
| 2 | J3 | Preuve + approfondissement |
| 3 | J7 | Décision |

### Séquence longue (7 emails — outils complexes type LMS)

Ajouter entre Email 3 et 4 :
- **Email 3bis (J5)** — Tuto pas à pas (configuration concrète)
- **Email 3ter (J6)** — Objection courante démontée

### Espacement — pourquoi ces délais

- J0→J2 (2j) : le problème est frais, on enchaîne vite
- J2→J4 (2j) : laisser le temps de regarder/tester
- J4→J7 (3j) : digérer l'expérience avant de parler d'achat
- J7→J10 (3j) : laisser mûrir la décision

---

## Adaptation par modèle économique

Le skill s'adapte au modèle de l'outil. L'arc narratif reste le même, seuls les angles de
l'email 4 et les CTA changent.

### Freemium (gratuit + Pro)

- Emails 1-2 : valeur pure, zéro lien commercial
- Email 3 : lien vers installation gratuite
- Email 4 : angle "Gratuit vs Pro" — présenter le Pro comme upgrade logique, pas nécessité
- Email 5 : lien affilié vers la version Pro

### Payant seul (pas de version gratuite)

- Emails 1-2 : valeur pure, zéro lien commercial
- Email 3 : lien vers démo/essai gratuit ou article détaillé
- Email 4 : angle "Ce que ça change concrètement" — ROI, gain de temps, témoignage
- Email 5 : lien affilié avec mention du prix + ce qu'on obtient

### 100% gratuit (pas de version payante)

- Pas de conversion monétaire — l'objectif est la confiance et l'autorité
- Email 4 : angle "Astuce avancée" — usage pro de l'outil
- Email 5 : angle "Et maintenant ?" — lien vers un article complémentaire ou un outil compagnon
- Le tag de conversion traque l'installation, pas l'achat

---

## Règles de rédaction

### Ton — exemples concrets

Le ton est celui d'un pair qui a trouvé un bon outil et le partage. Ni commercial, ni distant.

**Bon :**
> Tu as des liens d'affiliation sur ton site ? Alors tu as peut-être ce problème sans le savoir.

> Après 30 jours d'utilisation, voici ce que j'ai appris. Mes 3 liens les plus cliqués n'étaient
> pas ceux que je pensais.

> Je ne vais pas te relancer 15 fois. Mais voici la question directe.

**Mauvais :**
> Découvrez l'outil révolutionnaire qui va transformer votre business en ligne !

> ClickWhale est la solution n°1 pour les marketeurs WordPress. Ne ratez pas cette opportunité
> incroyable !

> Cher abonné, nous avons le plaisir de vous présenter notre sélection du mois.

### Règles

- Tutoiement systématique — sans exception
- Direct, pédagogique, concret
- Mots interdits : révolutionnaire, game changer, incroyable, scalable, en un clic, sans effort
- Longueur : 150-250 mots par email (lu en 90 secondes max)
- Un seul CTA par email — jamais deux directions
- Chaque objet < 50 caractères

### Structure de chaque email

```
Objet : [Accroche courte — curiosité ou bénéfice concret]
Objet alternatif : [Variante A/B — angle différent]

[Prénom],

[2-3 lignes de contexte — le problème ou la situation]

[Corps — 3-5 paragraphes courts, bullets si utile]

[CTA naturel — une seule action claire]

[Signature — Michaël]

P.S. : [Élément de réassurance ou teaser]
```

Toujours fournir **deux objets par email** (principal + alternatif) pour permettre l'A/B testing
dans FluentCRM. Les deux objets doivent avoir des angles différents (pas juste une reformulation).

---

## Règles d'affiliation schoolsWP

- L'outil est recommandé parce qu'il est testé et utile, pas parce qu'il paie
- Mentionner au moins une limite réelle de l'outil dans la séquence
- Ne jamais promettre de résultats ("tu vas gagner X€")
- Si version gratuite existe, toujours la recommander en premier
- La version Pro est présentée comme un upgrade logique, pas comme une nécessité
- Mention "(lien affilié)" au moins une fois dans la séquence (transparence)

---

## Logique d'automation FluentCRM

### Tags à créer

| Tag | Rôle | Appliqué quand |
|---|---|---|
| `{slug}-sequence` | Marque l'entrée | Début de la séquence |
| `{slug}-converti` | Marque la conversion | Clic sur lien affilié (email 3, 4 ou 5) |
| `{slug}-termine` | Marque la fin naturelle | Email final envoyé, pas converti |

`{slug}` = nom du plugin en kebab-case (ex : `clickwhale`, `tutor-lms`, `rankmath`).

### Nommage de l'automation

Format : `SEQ — {Nom Plugin} Discovery`
Exemple : `SEQ — ClickWhale Discovery`

### Schéma de l'automation

```
[TRIGGER] Tag "{slug}-sequence" appliqué
    ↓
[CONDITION] Tag "{slug}-converti" OU "{slug}-termine" présent ?
    ↓ Non                         ↓ Oui
    ↓                          [FIN — anti-doublon]
    ↓
[ENVOYER] Email 1
    ↓
[ATTENTE] 2 jours
    ↓
[CONDITION] Tag "{slug}-converti" ?
    ↓ Non                         ↓ Oui
[ENVOYER] Email 2              [FIN — sortie propre]
    ↓
[ATTENTE] 2 jours
    ↓
[CONDITION] Tag "{slug}-converti" ?
    ↓ Non                         ↓ Oui
[ENVOYER] Email 3              [FIN — sortie propre]
    ↓
[ATTENTE] 3 jours
    ↓
[CONDITION] Tag "{slug}-converti" ?
    ↓ Non                         ↓ Oui
[ENVOYER] Email 4              [FIN — sortie propre]
    ↓
[ATTENTE] 3 jours
    ↓
[CONDITION] Tag "{slug}-converti" ?
    ↓ Non                         ↓ Oui
[ENVOYER] Email 5              [FIN — sortie propre]
    ↓
[APPLIQUER TAG] {slug}-termine
[RETIRER TAG] {slug}-sequence
    ↓
[FIN]
```

Pour les séquences 3 ou 7 emails, adapter le nombre de blocs (même pattern conditionnel).

### Condition anti-doublon (entrée)

Avant d'entrer dans la séquence, vérifier :
- Le contact n'a PAS le tag `{slug}-termine` (déjà passé)
- Le contact n'a PAS le tag `{slug}-converti` (déjà converti)
- Le contact est en statut "Abonné" dans FluentCRM

### Tracking de conversion

**Option A — FluentCRM Pro (natif)**
- Trigger : clic sur lien dans email
- Action : appliquer tag `{slug}-converti`

**Option B — Page de redirection + webhook (version gratuite)**
- Page WordPress `/recommande/{slug}` avec redirection vers lien affilié
- Webhook FluentCRM via OttoKit pour appliquer le tag au passage

Recommander l'option B si FluentCRM gratuit. Toujours mentionner les deux options.

### Stratégie post-séquence

Les contacts tagués `{slug}-termine` (non convertis) ne sont pas perdus. Proposer :

1. **Relance douce (J+30)** — Un seul email "Au fait, {plugin} a été mis à jour" si mise à jour
   récente — tag temporaire `{slug}-relance-30`
2. **Inclusion dans une séquence thématique** — Si le plugin appartient à un cluster (ex: "outils
   affiliation"), inclure le contact dans la séquence du cluster
3. **Ne rien faire** — Parfois le meilleur choix. Ne pas harceler.

---

## Sortie obligatoire

Produire exactement ces sections, dans cet ordre :

1. **Récapitulatif** — Tableau des emails (jour, objet principal, objet alternatif, angle, rôle)
2. **Emails 1 à N** — Texte complet de chaque email, prêt à coller, avec les deux objets
3. **Automation FluentCRM** — Tags, nommage, schéma, conditions, tracking, stratégie post-séquence
4. **Checklist pré-lancement** — Les vérifications à faire avant d'activer
5. **KPI de suivi** — Métriques à surveiller

Ne pas ajouter d'intro ni de conclusion hors de ces sections.

---

## Checklist pré-lancement

Toujours inclure cette checklist dans la sortie :

- [ ] Les 3 tags sont créés dans FluentCRM
- [ ] L'automation est configurée et en mode "brouillon"
- [ ] Chaque email a été relu (aucune fonctionnalité inventée)
- [ ] Les liens (affiliés et articles) sont testés et fonctionnels
- [ ] La page `/recommande/{slug}` redirige correctement (si option B)
- [ ] Un contact test a reçu la séquence complète
- [ ] Le statut du contact test passe bien de `{slug}-sequence` à `{slug}-termine`
- [ ] Le clic sur le lien affilié applique bien `{slug}-converti`

---

## KPI de suivi

Inclure ces métriques dans la sortie avec les seuils schoolsWP :

| KPI | Seuil acceptable | Seuil bon | Action si en dessous |
|---|---|---|---|
| Taux d'ouverture moyen | > 25% | > 40% | Revoir les objets (tester les variantes A/B) |
| Taux de clic Email 3 | > 3% | > 6% | Revoir le CTA ou l'angle de preuve |
| Taux de clic Email 5 | > 2% | > 5% | Revoir l'urgence ou la proposition de valeur |
| Taux de conversion séquence | > 1% | > 3% | Revoir l'alignement audience/outil |
| Taux de désabonnement | < 2% | < 0.5% | Revoir la fréquence ou la pertinence |

---

## Exemple entrée/sortie

### Entrée

```
Plugin : ClickWhale
Problème : liens affiliés impossibles à traquer, URLs moches, pas de centralisation
URL affilié : schoolswp.com/recommande/clickwhale
Modèle : Freemium
Fonctionnalités clés : cloaking de liens, tracking des clics, centralisation
Fonctionnalités Pro : groupes de liens, UTM automatiques, stats géolocalisation, intégration WooCommerce
Expérience : utilisé 30 jours, découvert que mes 3 liens les plus cliqués n'étaient pas ceux que je pensais
```

### Sortie attendue (extraits)

**Email 1 :**

```
Objet : Tes liens WordPress te font perdre de l'argent
Objet alternatif : Ce que tu ne sais pas sur tes liens d'affiliation

[Prénom],

Tu as des liens d'affiliation sur ton site WordPress ?

Alors tu as peut-être ce problème sans le savoir :
- Des liens impossibles à mémoriser
- Des liens qui cassent quand tu changes d'hébergeur
- Des liens que tu ne peux pas traquer

En clair : tu laisses de l'argent sur la table à chaque clic.

J'ai cherché une solution simple, native WordPress, sans abonnement.
J'ai trouvé ClickWhale.

Dans le prochain email, je te montre exactement comment il fonctionne.

Michaël

P.S. : ClickWhale est gratuit. Pas d'excuse pour ne pas tester.
```

**Email 3 :**

```
Objet : Ce que j'ai découvert après 30 jours avec ClickWhale
Objet alternatif : Mes 3 liens les plus cliqués n'étaient pas ceux que je pensais

[Prénom],

Après 30 jours d'utilisation, voici ce que j'ai appris.

Mes 3 liens les plus cliqués n'étaient pas ceux que je pensais.

Sans ClickWhale, je continuais à pousser les mauvais contenus. Avec les stats de clics,
j'ai réorganisé mes priorités.

Résultat : j'ai mis en avant les liens qui convertissaient vraiment.

Un outil sans données, c'est un outil à moitié utilisé.

Tu n'as pas encore installé ClickWhale ?
→ C'est gratuit et ça prend 2 minutes : [lien vers le plugin WordPress]

Michaël

P.S. : Une limite honnête — l'interface est fonctionnelle mais pas la plus belle.
Ça fait le job, c'est ce qui compte.
```

**Email 5 :**

```
Objet : Dernière chose sur ClickWhale
Objet alternatif : Un outil simple pour tes liens (et je te laisse décider)

[Prénom],

Je ne vais pas te relancer 15 fois.

Mais voici la question directe : est-ce que tu gères des liens d'affiliation sur ton site ?

Si oui, tu as besoin d'un gestionnaire de liens. Pas demain. Maintenant.

ClickWhale est celui que j'utilise sur schoolsWP. Pas parce que c'est parfait.
Parce que c'est simple, efficace, et natif WordPress.

Version gratuite → déjà suffisante pour démarrer.
Version Pro → si tu veux les UTM automatiques et les stats avancées.

→ Installer ClickWhale : schoolswp.com/recommande/clickwhale (lien affilié)

Michaël

P.S. : Si tu as des questions sur la config, réponds à cet email. Je te file un coup de main.
```

---

## Actions suivantes

Après production de la séquence :

1. **Relire chaque email** — vérifier qu'aucune fonctionnalité n'est inventée
2. **Configurer FluentCRM** — créer les tags, l'automation, tester le tracking
3. **Passer la checklist pré-lancement** — tout cocher avant activation
4. **Activer en mode test** — envoyer la séquence à 2-3 contacts réels avant ouverture complète
5. **Suivre les KPI** — vérifier les métriques après 1 semaine et après la fin du premier cycle
