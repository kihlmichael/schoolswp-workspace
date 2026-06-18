# 08 - Brouillons de promotion (lead magnet welcome FluentCRM)

> STATUT : BROUILLONS. Rien n'est publié ni envoyé. Relecture obligatoire avant diffusion.
> Date : 2026-05-28
> Destination commune : `https://schoolswp.com/template-welcome-fluentcrm/`
> Contexte : maillage interne déjà posé (articles 2871653, 2779, 2511708). Cette étape couvre social + e-mail.

---

## 1. Post LinkedIn (FR)

**Visuel suggéré** : capture de la séquence dans FluentCRM (vue funnel) ou la couverture du template. Format 1200x1500 (portrait) ou 1200x628.

**Corps du post :**

```
La plupart des sites WordPress n'envoient jamais le premier e-mail au bon moment.

Quelqu'un s'inscrit, reçoit (au mieux) un « merci », et plus rien. Le moment où l'attention est la plus forte passe à la trappe.

J'ai donc préparé une séquence welcome FluentCRM prête à copier sur ton site, pensée pour tes clients WordPress :

- la structure complète des e-mails d'accueil, dans l'ordre
- les délais entre chaque envoi
- les textes que tu peux adapter en quelques minutes
- la logique de tags pour segmenter dès l'inscription

Tu importes, tu ajustes ton ton, tu actives. Pas besoin de partir d'une page blanche.

C'est gratuit, c'est ici : https://schoolswp.com/template-welcome-fluentcrm/

Dis-moi en commentaire comment tu gères ton accueil aujourd'hui, je suis curieux.

#WordPress #FluentCRM #EmailMarketing #Automatisation
```

**Notes** : 1 seul lien (dans le corps, pas en commentaire pour ce draft). Ton « je », pas de promesse absolue. Adapter le premier mot si tu reposts.

---

## 2. Épingle Pinterest

**Destination** : `https://schoolswp.com/template-welcome-fluentcrm/`
**Board suggéré** : WordPress / Email marketing / FluentCRM

**Titre (max ~100 caractères)** :

```
Séquence welcome FluentCRM prête à copier (gratuit)
```

**Description (mots-clés naturels)** :

```
Une séquence d'e-mails de bienvenue FluentCRM prête à importer sur ton site WordPress. Structure des e-mails, délais, textes à adapter et logique de tags pour bien accueillir chaque nouveau contact dès son inscription. À récupérer gratuitement sur schoolsWP.
```

**Texte sur le visuel (overlay)** :

```
Ta séquence welcome
FluentCRM, prête à copier
```

**Alt de l'image** :

```
Aperçu d'une séquence welcome FluentCRM prête à copier pour WordPress, proposée par schoolsWP
```

---

## 3. E-mail broadcast (newsletter)

> NE PAS ENVOYER sans validation. À construire en broadcast FluentCRM.
> Segment cible suggéré : abonnés newsletter francophones (tag `lang_fr` / liste newsletter FR). Exclure les contacts déjà taggés `freebie_welcome_template_*` pour ne pas redonder avec ceux qui l'ont déjà.
> Envoi unique, pas d'automatisation.

**Objet (à tester en A/B)** :

```
A. La séquence welcome que je fais tourner, prête à copier
B. Ton accueil par e-mail mérite mieux qu'un simple « merci »
```

**Texte de préheader** :

```
Importe-la dans FluentCRM, adapte ton ton, active. C'est gratuit.
```

**Corps :**

```
Salut [prénom],

Le premier e-mail après une inscription, c'est souvent là que tout se joue. Et c'est souvent là que rien ne part.

J'ai mis au propre la séquence welcome FluentCRM que j'utilise pour accueillir un nouveau contact : l'ordre des e-mails, les délais, les textes à adapter, et la logique de tags pour segmenter dès le départ.

Tu l'importes, tu ajustes deux ou trois phrases à ta voix, tu actives. Tu pars d'une base solide plutôt que d'une page blanche.

Je te l'offre ici :

[BOUTON : Récupérer ma séquence welcome FluentCRM]
-> https://schoolswp.com/template-welcome-fluentcrm/

Si tu la mets en place, réponds-moi pour me dire ce que tu en as fait. Je lis tout.

À bientôt,
Michael
```

**Bouton** : à construire en bloc Kadence email-safe (table HTML inline, cf. mémoire `reference_kadence_email_button_pattern`), couleur accent vert schoolsWP, lien vers la landing.

**Garde-fou** : un seul CTA, lien direct vers la landing (pas de cloak nécessaire, c'est une page interne).

---

## Checklist diffusion (à cocher au moment voulu)

- [ ] Relire les 3 brouillons (ton, fautes via clairtexte si besoin)
- [ ] LinkedIn : publier + épingler le lien en 1er commentaire si tu préfères ce format
- [ ] Pinterest : générer le visuel (overlay ci-dessus) puis créer l'épingle vers la landing
- [ ] E-mail : construire le broadcast FluentCRM, choisir l'objet, vérifier le segment FR + exclusion `freebie_welcome_template_*`, envoyer un test, puis programmer
- [ ] Après diffusion : suivre clics landing + inscriptions form 15 (funnel 32)
