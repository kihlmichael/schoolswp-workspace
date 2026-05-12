# Setup manuel FluentCRM : étapes UI

Suite aux limites de l'API REST FluentCRM (templates et création d'automations non scriptables via MCP), voici les étapes manuelles à faire dans WP Admin.

> **Diagnostic complet 2026-05-08 (RESOLU + EXECUTE)** : le 500 venait d un payload mal forme. Le controller TemplateController.php ligne 124 attend un body JSON imbrique sous une cle template. Le MCP fluentcrm_template_create envoyait les champs au top level, ce qui produisait null puis fatal Arr::only(). Solution : REST POST direct avec imbrication. Etape 1 effectuee en autonome le 2026-05-08, les 9 templates ont les IDs 2866640 a 2866649 (verifiables dans WP Admin > FluentCRM > E-mails > Modeles d e-mail). Methode debug WP_DEBUG via Novamira execute-php documentee dans sandbox-workspace/wp-debug-toggle/. Voir memory/reference_fluentcrm_mcp_template_create_broken.md.

## Déjà fait par API (ne pas refaire)

Les 5 tags ont été créés automatiquement le 2026-04-16 via MCP. Vérification : FluentCRM → Contacts → Étiquettes.

| ID | Tag slug | Rôle |
| --- | --- | --- |
| 746 | `freebie_welcome_template_fluentcrm` | Source lead magnet |
| 747 | `freebie_welcome_template_delivered` | Email 1 envoyé |
| 748 | `freebie_welcome_template_story_delivered` | Email 2 envoyé |
| 749 | `freebie_welcome_template_tip_delivered` | Email 3 envoyé |
| 750 | `freebie_welcome_template_completed` | Fin séquence welcome |

Tags existants réutilisés :

- `sequence_fluentcrm_onboarding` (id 688) - déclencheur séquence affiliation
- `plugin_fluentcrm` (id 606) - appliqué à la conversion
- Tag de conversion à créer si besoin : `sequence_fluentcrm_converti` (via UI)

## Étape 1 : Créer les 9 modèles d'e-mail [FAIT 2026-05-08 via REST direct]

> Les 9 templates ont les IDs 2866640 à 2866649. Vérifiables dans WP Admin > FluentCRM > E-mails > Modèles d'e-mail. Lien PDF placeholder #REMPLACER_PAR_LIEN_PDF# présent dans le template E1, à remplacer au moment de la config du Funnel 1 (étape 4) via override per-funnel.

FluentCRM → E-mails → **Modèles d'e-mail** → `Créer un nouveau modèle`

Pour chacun des 9 emails :

1. Titre du template = `LM Welcome Template FluentCRM · E1 · Livraison` (etc., voir ci-dessous)
2. Sujet = celui listé ci-dessous
3. Corps HTML = copier-coller le bloc correspondant depuis les fichiers sources
4. Enregistrer

### Séquence welcome (fichier source : [03-welcome-sequence.md](03-welcome-sequence.md))

| Nom template | Sujet | Source |
| --- | --- | --- |
| LM Welcome Template FluentCRM · E1 · Livraison | Ton template est juste ici | Email 1 du fichier |
| LM Welcome Template FluentCRM · E2 · Contexte | Pourquoi j'ai créé ce template | Email 2 |
| LM Welcome Template FluentCRM · E3 · Astuce | L'astuce que j'ajoute à chaque compte client | Email 3 |
| LM Welcome Template FluentCRM · E4 · Transition | Ce que tu vas recevoir ensuite | Email 4 |

### Séquence affiliation (fichier source : [04-affiliate-sequence.md](04-affiliate-sequence.md))

| Nom template | Sujet | Source |
| --- | --- | --- |
| SEQ FluentCRM Pro · E1 · Le coût | Combien tu paies Mailchimp ce mois-ci ? | Email 1 du fichier |
| SEQ FluentCRM Pro · E2 · La découverte | Ce que tes contacts font vraiment dans WordPress | Email 2 |
| SEQ FluentCRM Pro · E3 · La preuve | 3 ans avec FluentCRM chez mes clients | Email 3 |
| SEQ FluentCRM Pro · E4 · Gratuit vs Pro | Gratuit vs Pro : quand ça vaut vraiment le coup | Email 4 |
| SEQ FluentCRM Pro · E5 · La décision | Dernière chose sur FluentCRM | Email 5 |

Les corps HTML prêts sont dans les blocs ` ``` ` des fichiers sources. Tu peux les copier-coller en passant l'éditeur en mode HTML (ou garder le texte et laisser FluentCRM convertir).

## Étape 2 : Créer le formulaire Fluent Forms [FAIT 2026-05-08 via Novamira execute-php]

> **Form id=15** créé via INSERT direct dans `yym2fb_fluentform_forms` + 5 metas (`formSettings`, `notifications`, `fluentcrm_feeds`, `_primary_email_field`, `step_data_persistency_status`). Shortcode à insérer dans la landing : `[fluentform id="15"]`. Vérifiable dans WP Admin > Fluent Forms > All Forms.
>
> Configuration validée : 2 champs (`first_name` optionnel + `email` requis), submit "Recevoir le template maintenant", intégration FluentCRM (list 26 FREEBIES schoolsWP + tag 746 freebie_welcome_template_fluentcrm, single opt-in, skip si déjà inscrit), redirect customUrl `/merci-template-welcome-fluentcrm/`.

Fluent Forms → `Nouveau formulaire` → **Formulaire vierge**

Nom : `Lead Magnet - Welcome Template FluentCRM`

Champs :

- `prenom` (Prénom, optionnel)
- `email` (Email, requis, validation email)

Bouton submit : `Recevoir le template maintenant` (texte exact)

**Intégration FluentCRM** → Settings → Integrations → `Add New Integration` → FluentCRM :

- Add to list : `FREEBIES schoolsWP` (id 26)
- Apply tags : `freebie_welcome_template_fluentcrm`

**Redirection** après submit : URL personnalisée → `/merci-template-welcome-fluentcrm/`

## Étape 2bis : Créer la landing page [FAIT 2026-05-09]

> **Page id=2867562** creee. Slug : template-welcome-fluentcrm. Status draft (a publier manuellement apres relecture). Edit : <https://schoolswp.com/wp-admin/post.php?post=2867562&action=edit>. Une fois publiee, URL : <https://schoolswp.com/template-welcome-fluentcrm/>.
>
> Contenu : H1 + sous-titre, formulaire Fluent Forms id 15 embed dans un encart vert clair + micro-copy de reassurance, H2 "Ce que tu recois" avec 3 puces, H2 "Pour qui c'est utile" avec 2 paragraphes, H2 "Pourquoi je donne ca" avec 1 paragraphe, bloc signature Michael (avatar MK + bio courte) + mention RGPD avec lien /privacy/. Fonts brand inline : Nunito Sans 700 sur H1/H2, Roboto 400 sur body 1.1-1.2rem. Pas de separateurs Gutenberg.
>
> **A faire avant publication** : verifier le rendu du formulaire embed apres publication, Rank Math : option index par defaut, mettre noindex si tu veux eviter une duplication d'intention avec d'autres landing magnets, optionnel ajouter image hero (mockup PDF).

WP Admin > Pages > Nouvelle page

Slug : template-welcome-fluentcrm
Titre : Une sequence welcome FluentCRM prete a copier pour tes clients WordPress

Contenu :

- H1 + sous-titre (hero)
- Encart formulaire avec shortcode Fluent Forms id 15
- Micro-copy : Desinscription en 1 clic. Zero spam. Promis.
- H2 "Ce que tu recois" + 3 puces (4 objets, planning, bascule newsletter)
- H2 "Pour qui c'est utile" + 2 paragraphes (freelance WP, soi-meme)
- H2 "Pourquoi je donne ca" + 1 paragraphe (3 ans d'usage chez clients)
- Bloc signature Michael + bio
- Mention RGPD + lien vers /privacy/

## Étape 3 : Créer la page de remerciement [FAIT 2026-05-08 via Novamira execute-php]

> **Page id=2866761** créée. URL : <https://schoolswp.com/merci-template-welcome-fluentcrm/> (HTTP 200 confirmé). Edit : <https://schoolswp.com/wp-admin/post.php?post=2866761&action=edit>. Status `publish`, `noindex` set via Rank Math meta.
>
> **PDF v1 généré et linké 2026-05-08** : reportlab depuis `01-pdf-content.md` (1 page A4, vert #00D400, table actionnable centrale, ~3.7 KB). Uploadé en médiathèque (attachment id 2866893), URL : <https://schoolswp.com/wp-content/uploads/2026/05/welcome-template-fluentcrm.pdf>. Placeholders `#REMPLACER_PAR_URL_PDF#` (page 2866761) et `#REMPLACER_PAR_LIEN_PDF#` (template FluentCRM E1 id 2866640) remplacés automatiquement. Le bouton CTA actuel sur la page utilise un style inline temporaire, à remplacer par un Kadence advancedbtn quand tu mets en page la version finale (pattern `feedback_kadence_cta_template.md`).
>
> **Page densifiée 2026-05-08** : post_title réécrit en "C'est dans la boîte. Ton template FluentCRM arrive." (sert de H1 unique via le thème Kadence). Contenu = paragraphe rassurance + CTA vert sticky + 2 sections H2 ("Ce que tu trouves dans le template" 3 puces + "Et la suite ?" récap 4 emails à venir J+0/J+1/J+3/J+7) + section H3 "En attendant" avec lien interne vers `/fluentcrm-automations-indispensables/` + signature Michaël. Fonts brand appliqués via inline styles (Nunito Sans 700 sur titres, Roboto 400 sur body 1.1-1.2rem). Vérifié front : 1 H1, 2 H2, 1 H3, structure SEO propre.

WP Admin → Pages → Nouvelle page

Slug : `merci-template-welcome-fluentcrm`
Titre : `Ton template arrive`

Contenu :

- H1 : "Merci, ton template est en route"
- Paragraphe : "Un email avec le lien de téléchargement vient de partir. Si tu ne le reçois pas dans 2 minutes, vérifie tes spams."
- Bouton Kadence : `Télécharger le PDF maintenant` → URL directe du PDF (lien vers l'upload media WP)

## Étape 4 : Créer le Funnel 1 (séquence welcome) [FAIT 2026-05-08 via Novamira execute-php]

> **Funnel id=32** "SEQ - LM Welcome Template FluentCRM" en `draft`. Trigger : tag 746 (freebie_welcome_template_fluentcrm) appliqué + subscription_status=subscribed. 4 campaigns créées (ids 183-186, type funnel_email_campaign, status published, design_template raw_html, parent_id=32) clonées des templates 2866640-2866643. 13 sequences (ids 130-142) :
>
> 1. add_contact_to_tag → 747
> 2. send_custom_email → campaign 183 (E1 Livraison)
> 3. wait 1 day
> 4. add_contact_to_tag → 748
> 5. send_custom_email → 184 (E2 Contexte)
> 6. wait 2 days
> 7. add_contact_to_tag → 749
> 8. send_custom_email → 185 (E3 Astuce)
> 9. wait 4 days
> 10. add_contact_to_tag → 750
> 11. send_custom_email → 186 (E4 Transition)
> 12. add_contact_to_tag → 688 (déclenche Funnel 2)
> 13. end_this_funnel
>
> Test funnel 31 "TEST API : SEQ LM Welcome" supprimé en pre-cleanup (résidu d'une session antérieure). Pour activer le funnel après tests : flip status à `published` via UI ou DB.

FluentCRM → Automations → `Nouveau funnel` → **"When a Contact is Added to a Tag"**

Nom : `SEQ - LM Welcome Template FluentCRM`

Trigger settings :

- Tag : `freebie_welcome_template_fluentcrm`
- Run once per contact : Yes
- Subscription status : Subscribed

Blocks dans l'ordre :

1. **Send Email** → template `LM Welcome Template FluentCRM · E1 · Livraison` → remplacer `#REMPLACER_PAR_LIEN_PDF#` dans le body par l'URL réelle du PDF
2. **Apply Tag** → `freebie_welcome_template_delivered`
3. **Wait** → 1 day
4. **Conditional Check** (Benchmark) : "Is Unsubscribed?" → Yes path = End funnel, No path = continue
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

## Étape 5 : Créer le Funnel 2 (séquence affiliation) [FAIT 2026-05-08 V1]

> Funnel id=33 SEQ - FluentCRM Pro Discovery en draft. Trigger tag 688 (sequence_fluentcrm_onboarding) appliqué, subscription subscribed. Le tag est cascadé automatiquement depuis Funnel 1 step 12. 5 campaigns ids 187-191 clonées des templates 2866644 a 2866647 et 2866649. 10 sequences ids 143-152 en flux lineaire :
>
> 1. send_custom_email vers 187 E1 Le coût
> 2. wait 2 days
> 3. send_custom_email vers 188 E2 La découverte
> 4. wait 2 days
> 5. send_custom_email vers 189 E3 La preuve
> 6. wait 3 days
> 7. send_custom_email vers 190 E4 Gratuit vs Pro
> 8. wait 3 days
> 9. send_custom_email vers 191 E5 La décision
> 10. end_this_funnel
>
> Goal tracking pas implémenté en V1. Le brief 04-affiliate-sequence.md prévoit un block Benchmark sur clic vers fluentcrm.com qui applique tag 606 (plugin_fluentcrm) et coupe le funnel pour les convertis. A ajouter via UI Gutenberg quand tu testeras le funnel.

FluentCRM → Automations → `Nouveau funnel` → **"When a Contact is Added to a Tag"**

Nom : `SEQ - FluentCRM Pro Discovery`

Trigger settings :

- Tag : `sequence_fluentcrm_onboarding`
- Run once per contact : Yes

Goal tracking (à placer en début de funnel) :

- Block **Benchmark / Goal** → "Link Clicked" → URL contains `fluentcrm.com`
- Action on goal : Apply tag `plugin_fluentcrm` + End funnel (conversion réussie, sortie propre)

Blocks dans l'ordre :

1. **Send Email** → template `SEQ FluentCRM Pro · E1 · Le coût`
2. **Wait** → 2 days
3. **Conditional Check** : a-t-il déjà le tag `plugin_fluentcrm` ? Yes = End funnel
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

## Étape 6 : Tests avant activation

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
- [ ] Landing page publiée (relue + Rank Math configuré)
- [ ] Page de remerciement créée avec lien PDF
- [ ] PDF uploadé dans la médiathèque WP
- [ ] Funnel 1 créé en brouillon
- [ ] Funnel 2 créé en brouillon
- [ ] Lien `#REMPLACER_PAR_LIEN_PDF#` remplacé dans l'email 1
- [ ] Tests passés avec contact test
- [ ] Goal tracking E3 affiliation testé (clic sur fluentcrm.com applique `plugin_fluentcrm`)
- [ ] Délais remis aux valeurs réelles
- [ ] Les 2 funnels publiés
