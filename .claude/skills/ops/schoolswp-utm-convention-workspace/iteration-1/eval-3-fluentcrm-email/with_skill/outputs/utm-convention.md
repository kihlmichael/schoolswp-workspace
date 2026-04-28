# Convention UTM schoolsWP — Email FluentCRM — v1.0 (mars 2026)

Périmètre : 3 types d'emails FluentCRM — newsletter hebdomadaire, séquences automatisées lead magnet, relances abandon page de vente.

---

## 1. Règles de base

1. **Tout en minuscules, tirets uniquement, sans accents** — jamais d'underscores, jamais d'espaces, jamais de majuscules.
2. **utm_source = fluentcrm** pour tous les emails schoolsWP sans exception — la source c'est l'outil d'envoi.
3. **utm_medium = email** pour tous les emails — le canal est toujours email, quel que soit le type.
4. **utm_campaign = identifiant unique de la campagne** — distingue la newsletter, la séquence et la relance.
5. **utm_content = identifiant du lien dans l'email** — obligatoire dès qu'un email contient plus d'un lien cliquable.
6. **Cohérence absolue** — une valeur = un sens. Ne jamais utiliser deux graphies pour la même chose (ex: `wp-insights` et `wpinsights` sont deux campagnes différentes aux yeux de GA4).
7. **Ne jamais taguer les liens internes de navigation** (menu, footer du site) — seuls les liens distribués depuis l'extérieur reçoivent des UTMs.

---

## 2. Paramètres UTM — rôle et valeurs pour les emails FluentCRM

### utm_source

**Rôle** : identifie qui envoie le trafic — ici, toujours l'outil d'envoi email.

| Valeur      | Contexte                                                                 |
| ----------- | ------------------------------------------------------------------------ |
| `fluentcrm` | Tous les emails envoyés via FluentCRM (newsletters, séquences, relances) |

Règle tranchée : ne pas utiliser `newsletter` comme source — newsletter est une campagne, pas une source. La source c'est FluentCRM.

---

### utm_medium

**Rôle** : identifie le canal de diffusion.

| Valeur  | Contexte                       |
| ------- | ------------------------------ |
| `email` | Tous les emails sans exception |

---

### utm_campaign

**Rôle** : identifie la campagne spécifique — distingue les 3 types d'emails entre eux et les distingue dans le temps.

Format recommandé :

- Newsletter : `wp-insights-[semaine ou date]` — ex: `wp-insights-sem11-2026`
- Séquence lead magnet : `seq-[nom-lead-magnet]-[etape]` — ex: `seq-guide-lms-j1`
- Relance abandon : `relance-[nom-page]-[etape]` — ex: `relance-authority-system-j3`

| Valeur                        | Type d'email                         | Explication                                      |
| ----------------------------- | ------------------------------------ | ------------------------------------------------ |
| `wp-insights-sem11-2026`      | Newsletter hebdo                     | Identifie l'édition précise (semaine + année)    |
| `wp-insights-lundi`           | Newsletter hebdo (si cadence stable) | Variante si la date n'est pas utile dans GA4     |
| `seq-guide-lms-j1`            | Séquence lead magnet, email J+1      | `j1` = premier email de la séquence              |
| `seq-guide-lms-j3`            | Séquence lead magnet, email J+3      | Permet de comparer les taux de clic par étape    |
| `seq-guide-lms-j7`            | Séquence lead magnet, email J+7      |                                                  |
| `relance-authority-system-j1` | Relance abandon, 1er email           | 1er email de relance après abandon page de vente |
| `relance-authority-system-j3` | Relance abandon, 2ème email          | Relance 3 jours après                            |
| `relance-authority-system-j7` | Relance abandon, 3ème email          | Dernière relance de la séquence                  |

---

### utm_content

**Rôle** : différencie plusieurs liens dans le même email — c'est le seul paramètre qui permet de savoir quel lien précis a été cliqué dans une même campagne.

Règle : **utm_content est obligatoire dès qu'un email contient plus d'un lien cliquable vers une même destination.**

Convention de nommage :

| Valeur               | Signification                                                                                |
| -------------------- | -------------------------------------------------------------------------------------------- |
| `cta-principal`      | Bouton ou lien CTA principal de l'email (1er appel à l'action)                               |
| `cta-secondaire`     | Deuxième CTA (si présent)                                                                    |
| `lien-texte`         | Lien inséré dans le corps du texte, pas un bouton                                            |
| `lien-texte-2`       | Deuxième lien texte dans le corps                                                            |
| `cta-footer`         | CTA ou lien dans le bas de l'email (avant signature)                                         |
| `ps-lien`            | Lien dans un PS en fin d'email                                                               |
| `image`              | Image cliquable                                                                              |
| `bouton-decouvrir`   | Bouton dont le libellé est "Découvrir" — utile si plusieurs boutons avec libellés différents |
| `bouton-telecharger` | Bouton "Télécharger"                                                                         |
| `bouton-rejoindre`   | Bouton "Rejoindre"                                                                           |

Règle de différenciation liens principaux vs liens secondaires :

- **Lien principal** = CTA prioritaire, celui que tu veux que le lecteur clique en premier. Toujours `cta-principal`.
- **Lien secondaire** = tout autre lien dans l'email (lien texte contextuel, CTA de rappel en footer, PS). Utiliser `lien-texte`, `cta-footer`, `ps-lien` selon la position.
- Si deux liens pointent vers des destinations différentes dans le même email, chacun a ses propres UTMs (campaign différente si la destination est différente).
- Si deux liens pointent vers la même destination, seul utm_content les distingue dans GA4.

---

### utm_term

**Rôle** : réservé aux campagnes payantes (Google Ads, Meta Ads). Ne pas utiliser pour les emails FluentCRM.

---

## 3. Convention officielle recommandée

Format standard schoolsWP pour tous les emails FluentCRM :

```
?utm_source=fluentcrm&utm_medium=email&utm_campaign=[campaign]&utm_content=[content]
```

Tableau de référence rapide :

| Type d'email             | utm_source  | utm_medium | utm_campaign                  | utm_content                                   |
| ------------------------ | ----------- | ---------- | ----------------------------- | --------------------------------------------- |
| Newsletter hebdo         | `fluentcrm` | `email`    | `wp-insights-sem11-2026`      | `cta-principal` / `lien-texte` / `cta-footer` |
| Séquence lead magnet J+1 | `fluentcrm` | `email`    | `seq-guide-lms-j1`            | `cta-principal` / `lien-texte` / `ps-lien`    |
| Relance abandon J+1      | `fluentcrm` | `email`    | `relance-authority-system-j1` | `cta-principal` / `cta-footer` / `ps-lien`    |

---

## 4. Cas concrets — les 3 scénarios complets

---

### Scénario 1 — Newsletter hebdomadaire "WP Insights" (lundi)

Contexte : newsletter édition semaine 11 2026, envoyée chaque lundi. L'email contient un article phare sur TutorLMS, un lien texte contextuel vers une ressource gratuite, et un CTA footer vers la formation Authority System.

**Lien principal — article TutorLMS (CTA du bloc principal) :**

```
Contexte : Bouton CTA principal "Lire l'article complet" dans le bloc éditorial principal
URL complète : https://schoolswp.com/tutor-lms-avis/?utm_source=fluentcrm&utm_medium=email&utm_campaign=wp-insights-sem11-2026&utm_content=cta-principal
Explication : cta-principal identifie le lien prioritaire de l'email — c'est celui que GA4 te montrera en premier dans les rapports de campagne
```

**Lien secondaire — ressource gratuite dans le texte :**

```
Contexte : Lien texte dans le corps de l'email vers un guide gratuit
URL complète : https://schoolswp.com/guide-lms-wordpress/?utm_source=fluentcrm&utm_medium=email&utm_campaign=wp-insights-sem11-2026&utm_content=lien-texte
Explication : lien-texte différencie ce clic du CTA principal dans GA4 — tu verras lequel convertit le mieux
```

**Lien secondaire — CTA footer vers Authority System :**

```
Contexte : Bouton "Découvrir Authority System" en bas de l'email avant signature
URL complète : https://schoolswp.com/authority-system/?utm_source=fluentcrm&utm_medium=email&utm_campaign=wp-insights-sem11-2026&utm_content=cta-footer
Explication : cta-footer identifie les clics du bas de l'email — compare avec cta-principal pour voir si le placement impacte le taux de clic
```

---

### Scénario 2 — Séquence automatisée lead magnet "Guide LMS WordPress"

Contexte : séquence déclenchée après téléchargement du lead magnet. Email J+1 (premier email de nurturing), J+3 (approfondissement), J+7 (invitation à découvrir Authority System).

**Email J+1 — CTA principal vers un article de blog :**

```
Contexte : Premier email de la séquence, CTA principal "Commence par là" vers un article
URL complète : https://schoolswp.com/lms-wordpress-comparatif/?utm_source=fluentcrm&utm_medium=email&utm_campaign=seq-guide-lms-j1&utm_content=cta-principal
Explication : seq-guide-lms-j1 identifie cet email dans la séquence — tu peux comparer les taux de clic entre j1, j3, j7
```

**Email J+1 — lien texte secondaire dans le corps :**

```
Contexte : Lien dans le texte du J+1 vers une page de ressources
URL complète : https://schoolswp.com/ressources-lms/?utm_source=fluentcrm&utm_medium=email&utm_campaign=seq-guide-lms-j1&utm_content=lien-texte
Explication : même campaign que le CTA principal (même email), utm_content différent pour suivre quel lien est cliqué
```

**Email J+3 — CTA principal :**

```
Contexte : Email J+3, approfondissement, CTA vers un article comparatif
URL complète : https://schoolswp.com/tutor-lms-vs-learndash/?utm_source=fluentcrm&utm_medium=email&utm_campaign=seq-guide-lms-j3&utm_content=cta-principal
Explication : campaign change (j3 vs j1) — permet de voir à quelle étape de la séquence les leads s'engagent le plus
```

**Email J+7 — CTA principal vers page de vente :**

```
Contexte : Email J+7, invitation à découvrir Authority System
URL complète : https://schoolswp.com/authority-system/?utm_source=fluentcrm&utm_medium=email&utm_campaign=seq-guide-lms-j7&utm_content=cta-principal
Explication : j7 marque la transition nurturing → conversion dans ta séquence — isole ces clics dans GA4
```

**Email J+7 — lien PS en fin d'email :**

```
Contexte : PS en bas de l'email J+7, lien alternatif "ou commence par ce guide gratuit"
URL complète : https://schoolswp.com/guide-lms-gratuit/?utm_source=fluentcrm&utm_medium=email&utm_campaign=seq-guide-lms-j7&utm_content=ps-lien
Explication : ps-lien identifie les clics sur le PS — utile pour mesurer l'impact de cette technique copywriting
```

---

### Scénario 3 — Emails de relance abandonnistes page de vente Authority System

Contexte : séquence relance pour les visiteurs qui ont visité la page de vente sans acheter. 3 emails : J+1 (rappel bénéfices), J+3 (objection fréquente), J+7 (dernière chance ou pivot).

**Email J+1 — CTA principal (retour page de vente) :**

```
Contexte : Premier email de relance, CTA principal "Reprendre où tu t'es arrêté"
URL complète : https://schoolswp.com/authority-system/?utm_source=fluentcrm&utm_medium=email&utm_campaign=relance-authority-system-j1&utm_content=cta-principal
Explication : relance-authority-system-j1 identifie ce premier email de relance — tu pourras voir quel email de relance génère le plus de retours sur la page
```

**Email J+1 — lien texte secondaire (témoignage ou preuve) :**

```
Contexte : Lien dans le texte vers une page de témoignages ou étude de cas
URL complète : https://schoolswp.com/temoignages-authority-system/?utm_source=fluentcrm&utm_medium=email&utm_campaign=relance-authority-system-j1&utm_content=lien-texte
Explication : mesure si les preuves sociales dans le texte convertissent mieux que le CTA direct
```

**Email J+3 — CTA principal (objection) :**

```
Contexte : Email J+3, traitement objection "trop cher", lien vers FAQ tarifs
URL complète : https://schoolswp.com/authority-system/#faq?utm_source=fluentcrm&utm_medium=email&utm_campaign=relance-authority-system-j3&utm_content=cta-principal
Explication : campaign j3 distingue cet email du j1 dans GA4 — tu vois si les abandonnistes réengagent à j3
```

**Email J+7 — CTA principal (dernière chance) :**

```
Contexte : Dernier email de relance, offre limitée ou pivot vers une alternative
URL complète : https://schoolswp.com/authority-system/?utm_source=fluentcrm&utm_medium=email&utm_campaign=relance-authority-system-j7&utm_content=cta-principal
Explication : j7 est le dernier email — si les conversions viennent de là, ta relance longue a de la valeur
```

**Email J+7 — CTA footer (offre alternative) :**

```
Contexte : Si l'achat ne se fait pas, lien vers une ressource gratuite en bas de l'email
URL complète : https://schoolswp.com/guide-lms-wordpress/?utm_source=fluentcrm&utm_medium=email&utm_campaign=relance-authority-system-j7&utm_content=cta-footer
Explication : mesure combien d'abandonnistes non-acheteurs restent engagés via le contenu gratuit
```

---

## 5. Liens principaux vs liens secondaires — règle définitive

**La question n'est pas "principal ou secondaire" au sens hiérarchique — la question est : que veux-tu mesurer séparément dans GA4 ?**

Règle opérationnelle :

| Position du lien dans l'email                         | utm_content recommandé                    |
| ----------------------------------------------------- | ----------------------------------------- |
| CTA principal (bloc hero ou section principale)       | `cta-principal`                           |
| CTA en bas de l'email (avant signature)               | `cta-footer`                              |
| Lien inséré dans le corps du texte (inline)           | `lien-texte`                              |
| Deuxième lien inline dans le texte                    | `lien-texte-2`                            |
| PS en toute fin d'email                               | `ps-lien`                                 |
| Image cliquable                                       | `image`                                   |
| Bouton avec libellé spécifique (si plusieurs boutons) | `bouton-[libelle]` ex: `bouton-rejoindre` |

Conclusion tranchée : **toujours mettre utm_content dès qu'un email a plus d'un lien.** Si tu ne mets utm_content que sur le lien principal, GA4 agrège tous les autres clics sans étiquette et tu perds l'information.

---

## 6. Quand mettre des UTMs dans les emails

- Tous les liens qui pointent vers ton site depuis un email FluentCRM
- Liens vers des articles, pages de vente, pages de ressources, pages de téléchargement
- Liens vers des pages tierces (partenaires, outils recommandés) si tu veux les tracker
- Liens dans les emails transactionnels si tu veux mesurer l'engagement post-achat

---

## 7. Quand NE PAS mettre des UTMs dans les emails

- **Lien de désabonnement** — lien système FluentCRM, ne pas toucher
- **Lien de gestion des préférences** — idem
- **Lien de confirmation de commande vers une page tierce de paiement** — casse le tracking e-commerce, GA4 perd la source originelle
- **Liens vers des ancres internes de la même page** (ex: `#faq`) — ajouter les UTMs sur l'URL de base mais pas sur l'ancre seule
- **Redirections techniques ou liens de tracking FluentCRM natifs** — FluentCRM a son propre tracking de clics ; les UTMs s'ajoutent en plus pour GA4, pas à la place

---

## 8. Erreurs à éviter

1. **Utiliser `newsletter` comme utm_source** — newsletter est une campagne, pas une source. Source = fluentcrm (l'outil). Erreur classique qui fragmente les données dans GA4.
2. **Oublier utm_content quand l'email a plusieurs liens** — GA4 ne peut pas distinguer d'où vient le clic ; tu perds toute donnée de placement.
3. **Changer la graphie d'une valeur entre deux envois** — `wp-insights-sem11` et `wp-insights-s11` créent deux campagnes distinctes dans GA4. Choisir une convention et ne plus en bouger.
4. **Utiliser des majuscules** — GA4 est sensible à la casse. `WP-Insights` ≠ `wp-insights`. Toujours minuscules.
5. **Mettre des accents ou caractères spéciaux** — `relance-séquence` devient `relance-s%C3%A9quence` dans l'URL. Toujours écrire `relance-sequence`.
6. **Copier-coller un UTM d'un email vers un autre sans changer utm_campaign** — deux emails différents avec la même campaign, GA4 les fusionne. Toujours mettre à jour utm_campaign pour chaque email de séquence.
7. **Taguer les liens de désabonnement** — risque de casser le système de compliance email, ne jamais toucher ces liens.
8. **Oublier de tester les liens avant envoi** — coller l'URL complète dans un navigateur pour vérifier que les UTMs passent bien et que la page se charge correctement.

---

## 9. Recommandation simple à retenir

> Source = FluentCRM (l'outil qui envoie). Medium = email (le canal). Campaign = quel email précis (newsletter semaine X, séquence J+1, relance J+3). Content = quel lien dans cet email (principal, texte, footer, PS).
>
> Si un email a plusieurs liens et que tu ne mets utm_content que sur le premier, tu travailles dans l'obscurité sur tous les autres. Tague tout ou ne tague rien — l'entre-deux ne sert à personne.
