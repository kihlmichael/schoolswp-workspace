# Landing de capture — Checklist FluentCart Setup

Page de capture newsletter pour le lead magnet "Checklist FluentCart Setup en 1 demi-journée".
Stack : Fluent Forms (capture) + FluentCRM (séquence). Pattern répliqué du tunnel welcome-template-fluentcrm.

Statut : COPY PRÊTE. Build WP en attente des gates (voir 03-fluentcrm-blueprint.md).

---

## Meta SEO

- **Meta title** : Checklist FluentCart Setup gratuite | Ouvre ta boutique en 1 demi-journée
- **Meta description** : La checklist en 7 phases pour ouvrir ta boutique FluentCart sans rien oublier. Install, paiements, première vente test. Gratuite, à télécharger.
- **Slug** : `/checklist-fluentcart-setup/`
- **Indexation** : la landing est indexable. La page de remerciement reste en noindex.

---

## Structure de la page (ordre des blocs)

1. Hero (H1 + sous-titre + visuel PDF)
2. Bloc valeur (3 points)
3. Formulaire Fluent Forms
4. Réassurance
5. Signature Michaël

---

## Hero

**H1**
Ouvre ta boutique FluentCart en une demi-journée, sans rien oublier

**Sous-titre**
La checklist exacte que je suis à chaque installation. Pour les créateurs WordPress qui veulent vendre sans passer par WooCommerce.

**Visuel**
Mockup du PDF (couverture + une page intérieure visible). Vert #00D400 en accent.

---

## Bloc valeur

Ce que tu vas recevoir :

- → Les **7 phases** de A à Z : installation, configuration du store, premier produit, paiements, vente test, emails, contrôle final.
- → La ligne **Vérification** à chaque étape, pour ne jamais avancer tant que la précédente n'est pas validée.
- → Les **5 pièges** qui font perdre des heures, et comment les éviter dès le départ.

Temps pour tout appliquer : une demi-journée. Niveau requis : aucun.

---

## Formulaire Fluent Forms

Champs :
- **Prénom** (optionnel)
- **Email** (obligatoire)

**Bouton CTA** : Recevoir la checklist FluentCart

**Texte sous le bouton (réassurance)** :
Désinscription en 1 clic. Zéro spam. Promis.

### Specs techniques Fluent Forms

- Nouveau formulaire Fluent Forms : "Lead Magnet - Checklist FluentCart Setup"
- Feed FluentCRM (`fluentcrm_feeds`) :
  - Liste : **FREEBIES schoolsWP** (id 26)
  - Tags appliqués : `freebie_fluentcart_setup_fr` (trigger, à créer) + `lang_fr` (768)
  - Opt-in : single opt-in
  - `skip_if_exists` : activé (ne pas réécraser un contact existant)
- Redirection post-inscription : page de remerciement dédiée `/merci-checklist-fluentcart/` (publish, noindex)
- La page de remerciement porte le lien de téléchargement du PDF sur son URL stable WP (à publier, voir gate G1 du blueprint).

---

## Signature Michaël

Moi c'est Michaël. J'aide les créateurs WordPress à vendre en ligne sans usine à gaz.
J'ai installé FluentCart assez de fois pour t'éviter les détours. Cette checklist, c'est ma méthode, condensée.

---

## Cohérence funnel

Promesse landing = promesse PDF = objet email 1 : **ouvrir ta boutique FluentCart en une demi-journée sans rien oublier**.
Le visiteur s'inscrit, reçoit l'email 1 avec le lien du PDF, télécharge la checklist, l'applique. Aucune friction, aucune promesse non tenue.
