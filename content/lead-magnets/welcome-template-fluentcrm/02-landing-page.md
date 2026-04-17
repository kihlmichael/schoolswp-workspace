# Landing Page — Template Séquence Welcome FluentCRM

## Meta HTML

**Meta title**
Séquence welcome FluentCRM — template prêt à copier | schoolsWP

**Meta description**
Télécharge la séquence de bienvenue FluentCRM que j'installe chez mes clients WordPress. 4 emails, 7 jours, tags et conditions. Gratuit.

---

## Copywriting

**H1**
Une séquence welcome FluentCRM prête à copier pour tes clients WordPress

**Sous-titre (H2 léger)**
4 emails, 7 jours, tags et conditions inclus — installe-la en 45 minutes sur n'importe quel compte client, sans repartir d'une page blanche.

**Visuel** : mockup du PDF A4 (vue de face + légère rotation 8°), badge "Gratuit" vert `#00D400` en haut-droite.

**Bloc valeur — 3 points (flèches vertes)**

→ Les **4 objets d'emails** testés qui tiennent au-dessus de 45 % d'ouverture
→ Le **planning exact** (délais en jours + tags + conditions FluentCRM)
→ La **bascule vers la newsletter** sans perdre l'engagement acquis

**Formulaire Fluent Forms**

- Champ `prenom` — label "Ton prénom (optionnel)" — non requis
- Champ `email` — label "Ton email" — requis, validation email
- Bouton CTA : **"Recevoir le template maintenant"** — fond vert `#00D400`, texte blanc, Kadence Advanced Button

**Réassurance (sous bouton)**
Désinscription en 1 clic. Zéro spam. Promis.

**Signature Michaël**
Photo ronde 80×80 +

> Michaël Kihl — je construis schoolsWP pour aider les freelances WordPress à livrer mieux que les agences. J'installe FluentCRM chez mes clients depuis 3 ans, voici ce qui marche.

---

## Specs de structure (mobile-first)

1. H1 + sous-titre (hero plein écran, centré)
2. Visuel mockup PDF (à droite desktop, sous H1 mobile)
3. Formulaire + CTA (au-dessus de la ligne de flottaison mobile)
4. Réassurance (micro-copy gris)
5. Bloc valeur 3 points (flèches vertes)
6. Signature Michaël (ancrage confiance)
7. Footer minimal (mentions légales + politique de confidentialité)

---

## Specs Fluent Forms

- **Form name** : `lead-magnet-welcome-template-fluentcrm`
- **Champs** : `prenom` (optional), `email` (required, email validation)
- **Intégration FluentCRM** : Add to list `lead_magnet_welcome_template` + Apply tag `source_lm_fluentcrm`
- **Confirmation type** : Redirect to `/merci-template-welcome-fluentcrm/`
- **Page de remerciement** : lien de téléchargement direct du PDF (bouton Kadence) + message "Le PDF est aussi dans ta boîte mail"
- **Failsafe email** : envoi automatique FluentCRM de l'email 1 (séquence) qui contient le lien PDF
- **Double opt-in** : désactivé (single opt-in, confirmation implicite par ouverture email 1)
- **Liens externes** : `target="_blank" rel="noopener"`
