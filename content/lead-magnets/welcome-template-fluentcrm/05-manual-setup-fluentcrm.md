# Setup manuel FluentCRM — étapes UI

Suite aux limites de l'API REST FluentCRM (templates et création d'automations non scriptables via MCP), voici les étapes manuelles à faire dans WP Admin.

## Déjà fait par API (ne pas refaire)

Les 5 tags ont été créés automatiquement le 2026-04-16 via MCP. Vérification : FluentCRM → Contacts → Étiquettes.

| ID | Tag slug | Rôle |
|---|---|---|
| 746 | `freebie_welcome_template_fluentcrm` | Source lead magnet |
| 747 | `freebie_welcome_template_delivered` | Email 1 envoyé |
| 748 | `freebie_welcome_template_story_delivered` | Email 2 envoyé |
| 749 | `freebie_welcome_template_tip_delivered` | Email 3 envoyé |
| 750 | `freebie_welcome_template_completed` | Fin séquence welcome |

Tags existants réutilisés :
- `sequence_fluentcrm_onboarding` (id 688) — déclencheur séquence affiliation
- `plugin_fluentcrm` (id 606) — appliqué à la conversion
- Tag de conversion à créer si besoin : `sequence_fluentcrm_converti` (via UI)

## Étape 1 — Créer les 9 modèles d'e-mail

FluentCRM → E-mails → **Modèles d'e-mail** → `Créer un nouveau modèle`

Pour chacun des 9 emails :

1. Titre du template = `LM Welcome Template FluentCRM · E1 · Livraison` (etc. — voir ci-dessous)
2. Sujet = celui listé ci-dessous
3. Corps HTML = copier-coller le bloc correspondant depuis les fichiers sources
4. Enregistrer

### Séquence welcome (fichier source : [03-welcome-sequence.md](03-welcome-sequence.md))

| Nom template | Sujet | Source |
|---|---|---|
| LM Welcome Template FluentCRM · E1 · Livraison | Ton template est juste ici | Email 1 du fichier |
| LM Welcome Template FluentCRM · E2 · Contexte | Pourquoi j'ai créé ce template | Email 2 |
| LM Welcome Template FluentCRM · E3 · Astuce | L'astuce que j'ajoute à chaque compte client | Email 3 |
| LM Welcome Template FluentCRM · E4 · Transition | Ce que tu vas recevoir ensuite | Email 4 |

### Séquence affiliation (fichier source : [04-affiliate-sequence.md](04-affiliate-sequence.md))

| Nom template | Sujet | Source |
|---|---|---|
| SEQ FluentCRM Pro · E1 · Le coût | Combien tu paies Mailchimp ce mois-ci ? | Email 1 du fichier |
| SEQ FluentCRM Pro · E2 · La découverte | Ce que tes contacts font vraiment dans WordPress | Email 2 |
| SEQ FluentCRM Pro · E3 · La preuve | 3 ans avec FluentCRM chez mes clients | Email 3 |
| SEQ FluentCRM Pro · E4 · Gratuit vs Pro | Gratuit vs Pro : quand ça vaut vraiment le coup | Email 4 |
| SEQ FluentCRM Pro · E5 · La décision | Dernière chose sur FluentCRM | Email 5 |

Les corps HTML prêts sont dans les blocs ` ``` ` des fichiers sources — tu peux les copier-coller en passant l'éditeur en mode HTML (ou garder le texte et laisser FluentCRM convertir).

## Étape 2 — Créer le formulaire Fluent Forms

Fluent Forms → `Nouveau formulaire` → **Formulaire vierge**

Nom : `Lead Magnet — Welcome Template FluentCRM`

Champs :
- `prenom` (Prénom, optionnel)
- `email` (Email, requis, validation email)

Bouton submit : `Recevoir le template maintenant` (texte exact)

**Intégration FluentCRM** → Settings → Integrations → `Add New Integration` → FluentCRM :
- Add to list : `FREEBIES schoolsWP` (id 26)
- Apply tags : `freebie_welcome_template_fluentcrm`

**Redirection** après submit : URL personnalisée → `/merci-template-welcome-fluentcrm/`

## Étape 3 — Créer la page de remerciement

WP Admin → Pages → Nouvelle page

Slug : `merci-template-welcome-fluentcrm`
Titre : `Ton template arrive`

Contenu :
- H1 : "Merci — ton template est en route"
- Paragraphe : "Un email avec le lien de téléchargement vient de partir. Si tu ne le reçois pas dans 2 minutes, vérifie tes spams."
- Bouton Kadence : `Télécharger le PDF maintenant` → URL directe du PDF (lien vers l'upload media WP)

## Étape 4 — Créer le Funnel 1 (séquence welcome)

FluentCRM → Automations → `Nouveau funnel` → **"When a Contact is Added to a Tag"**

Nom : `SEQ — LM Welcome Template FluentCRM`

Trigger settings :
- Tag : `freebie_welcome_template_fluentcrm`
- Run once per contact : Yes
- Subscription status : Subscribed

Blocks dans l'ordre :

1. **Send Email** → template `LM Welcome Template FluentCRM · E1 · Livraison` → remplacer `#REMPLACER_PAR_LIEN_PDF#` dans le body par l'URL réelle du PDF
2. **Apply Tag** → `freebie_welcome_template_delivered`
3. **Wait** → 1 day
4. **Conditional Check** (Benchmark) — "Is Unsubscribed?" → Yes path = End funnel, No path = continue
5. **Send Email** → template E2 Contexte
6. **Apply Tag** → `freebie_welcome_template_story_delivered`
7. **Wait** → 2 days
8. **Send Email** → template E3 Astuce
9. **Apply Tag** → `freebie_welcome_template_tip_delivered`
10. **Wait** → 4 days
11. **Send Email** → template E4 Transition
12. **Apply Tag** → `freebie_welcome_template_completed`
13. **Apply Tag** → `sequence_fluentcrm_onboarding` (déclenche le Funnel 2)

Statut final : **Draft** (ne pas publier avant tests)

## Étape 5 — Créer le Funnel 2 (séquence affiliation)

FluentCRM → Automations → `Nouveau funnel` → **"When a Contact is Added to a Tag"**

Nom : `SEQ — FluentCRM Pro Discovery`

Trigger settings :
- Tag : `sequence_fluentcrm_onboarding`
- Run once per contact : Yes

Goal tracking (à placer en début de funnel) :
- Block **Benchmark / Goal** → "Link Clicked" → URL contains `fluentcrm.com`
- Action on goal : Apply tag `plugin_fluentcrm` + End funnel (conversion réussie, sortie propre)

Blocks dans l'ordre :

1. **Send Email** → template `SEQ FluentCRM Pro · E1 · Le coût`
2. **Wait** → 2 days
3. **Conditional Check** — a-t-il déjà le tag `plugin_fluentcrm` ? Yes = End funnel
4. **Send Email** → template E2 La découverte
5. **Wait** → 2 days
6. **Conditional Check** idem
7. **Send Email** → template E3 La preuve
8. **Wait** → 3 days
9. **Conditional Check** idem
10. **Send Email** → template E4 Gratuit vs Pro
11. **Wait** → 3 days
12. **Conditional Check** idem
13. **Send Email** → template E5 La décision
14. **Apply Tag** → `sequence_fluentcrm_termine` (à créer via UI si tu veux tracker les non-convertis)

Statut final : **Draft**

## Étape 6 — Tests avant activation

Pour chaque funnel :

1. Active en mode brouillon
2. Crée un contact test avec ton email personnel (pas l'email principal)
3. Applique le tag déclencheur manuellement via le profil du contact
4. Vérifie que l'email 1 arrive dans les 5 minutes
5. Raccourcis temporairement les délais des wait steps à 1 minute pour tester la séquence complète
6. Vérifie les bascules de tags dans FluentCRM → Contacts → [ton contact test] → onglet Tags
7. Remets les délais réels (1/2/4 jours et 2/2/3/3 jours) avant publication
8. Publie les funnels

## Checklist finale

- [ ] 9 modèles d'e-mail créés
- [ ] Formulaire Fluent Forms créé avec intégration FluentCRM
- [ ] Page de remerciement créée avec lien PDF
- [ ] PDF uploadé dans la médiathèque WP
- [ ] Funnel 1 créé en brouillon
- [ ] Funnel 2 créé en brouillon
- [ ] Lien `#REMPLACER_PAR_LIEN_PDF#` remplacé dans l'email 1
- [ ] Tests passés avec contact test
- [ ] Goal tracking E3 affiliation testé (clic sur fluentcrm.com applique `plugin_fluentcrm`)
- [ ] Délais remis aux valeurs réelles
- [ ] Les 2 funnels publiés
