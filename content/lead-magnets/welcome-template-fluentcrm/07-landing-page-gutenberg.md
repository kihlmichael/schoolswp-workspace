# Landing Page Gutenberg : `template-welcome-fluentcrm`

Code Gutenberg pret a coller dans une page WP. Construit en blocs core WordPress (Group, Columns, Heading, Paragraph, List, Image, Media-Text) + shortcode Fluent Forms. Aucun bloc Kadence custom : Michael repassera derriere pour ajuster le styling avec les blocs Pro si besoin.

---

## Meta WordPress

| Champ | Valeur |
|---|---|
| Type | Page (pas Post) |
| Slug | `template-welcome-fluentcrm` |
| Titre WP | `Sequence welcome FluentCRM : template pret a copier` |
| Statut | Draft (publier apres test du formulaire) |
| Meta title (Rank Math) | `Sequence welcome FluentCRM : template pret a copier \| schoolsWP` |
| Meta description (Rank Math) | `Telecharge la sequence de bienvenue FluentCRM que j'installe chez mes clients WordPress. 4 emails, 7 jours, tags et conditions. Gratuit.` |
| Indexable Rank Math | Oui (la landing peut etre indexee, c'est une page de capture publique) |

---

## Procedure (ordre)

1. **Formulaire Fluent Forms : DEJA EXISTANT** (id `15`, confirme par Michael le 2026-05-09).
   - Si tu veux re-verifier ses settings : Fluent Forms > Forms > id 15
   - Champs attendus : `prenom` (optionnel) + `email` (requis)
   - Bouton submit : `Recevoir le template maintenant`
   - Confirmation : Redirect vers `https://schoolswp.com/merci-template-welcome-fluentcrm/`
   - Integration FluentCRM : Lists 26 (FREEBIES schoolsWP) + Tag 746 (freebie_welcome_template_fluentcrm)
   - Si un de ces points manque, l'ajuster avant publication de la landing.

2. **Uploader le mockup PDF** dans la mediatheque WP :
   - Image PNG ou JPG, dimension recommandee 1200x900 ou ratio 4:3
   - Alt text : `Mockup du PDF Sequence welcome FluentCRM`
   - Note l'URL de l'upload.

3. **Verifier que la photo ronde Michael 80x80** existe deja, sinon en uploader une :
   - Format JPG ou PNG, ratio 1:1, recommandation 160x160 (retina sur 80x80)
   - Alt text : `Michael Kihl, fondateur schoolsWP`

4. **Creer la page WP** (Pages > Add New) :
   - Titre : `Sequence welcome FluentCRM : template pret a copier`
   - Slug : `template-welcome-fluentcrm` (verifier dans Permalink)
   - Mode editeur : passer en Code Editor (raccourci Ctrl+Shift+Alt+M ou via le menu trois-points en haut a droite > Code editor)
   - Coller le bloc de code ci-dessous

5. **Remplacer les 2 placeholders restants** dans le code colle :
   - `REPLACE_AVEC_URL_MOCKUP_PDF` : URL du mockup uploadee etape 2
   - `REPLACE_AVEC_URL_PHOTO_MICHAEL` : URL de la photo ronde etape 3
   - (Le shortcode formulaire est deja figé sur `id="15"`, formulaire pre-existant confirme par Michael le 2026-05-09)

6. Repasser en Visual Editor pour visualiser le rendu et ajuster.

7. Garder en Draft, tester le formulaire en mode preview, valider la redirection vers `/merci-template-welcome-fluentcrm/`, valider l'application du tag dans FluentCRM > Contacts apres soumission test, **puis publier**.

---

## Code Gutenberg complet

A coller tel quel en mode Code Editor :

```html
<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"5rem","bottom":"5rem","right":"2rem","left":"2rem"}}},"layout":{"type":"constrained","contentSize":"1140px"}} -->
<div class="wp-block-group alignfull" style="padding-top:5rem;padding-right:2rem;padding-bottom:5rem;padding-left:2rem">

<!-- wp:columns {"verticalAlignment":"center"} -->
<div class="wp-block-columns are-vertically-aligned-center">

<!-- wp:column {"verticalAlignment":"center","width":"58%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:58%">

<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"2.75rem","lineHeight":"1.15"}}} -->
<h1 class="wp-block-heading" style="font-size:2.75rem;line-height:1.15">Une sequence welcome FluentCRM prete a copier pour tes clients WordPress</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"style":{"typography":{"fontSize":"1.125rem","lineHeight":"1.6"}}} -->
<p style="font-size:1.125rem;line-height:1.6">4 emails, 7 jours, tags et conditions inclus. Installe-la en 45 minutes sur n'importe quel compte client, sans repartir d'une page blanche.</p>
<!-- /wp:paragraph -->

<!-- wp:shortcode -->
[fluentform id="15"]
<!-- /wp:shortcode -->

<!-- wp:paragraph {"style":{"typography":{"fontSize":"0.875rem"},"color":{"text":"#6b7280"}}} -->
<p class="has-text-color" style="color:#6b7280;font-size:0.875rem">Desinscription en 1 clic. Zero spam. Promis.</p>
<!-- /wp:paragraph -->

</div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center","width":"42%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:42%">

<!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="REPLACE_AVEC_URL_MOCKUP_PDF" alt="Mockup du PDF Sequence welcome FluentCRM"/></figure>
<!-- /wp:image -->

</div>
<!-- /wp:column -->

</div>
<!-- /wp:columns -->

</div>
<!-- /wp:group -->

<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"4rem","bottom":"4rem","right":"2rem","left":"2rem"}},"color":{"background":"#f4f5f7"}},"layout":{"type":"constrained","contentSize":"840px"}} -->
<div class="wp-block-group alignfull has-background" style="background-color:#f4f5f7;padding-top:4rem;padding-right:2rem;padding-bottom:4rem;padding-left:2rem">

<!-- wp:heading {"textAlign":"center","level":2,"style":{"typography":{"fontSize":"2rem","lineHeight":"1.2"}}} -->
<h2 class="wp-block-heading has-text-align-center" style="font-size:2rem;line-height:1.2">Ce que tu trouves dans le template</h2>
<!-- /wp:heading -->

<!-- wp:list {"style":{"typography":{"fontSize":"1.125rem","lineHeight":"1.7"},"spacing":{"padding":{"top":"1rem","bottom":"0","right":"0","left":"0"}}}} -->
<ul class="wp-block-list" style="padding-top:1rem;padding-right:0;padding-bottom:0;padding-left:0;font-size:1.125rem;line-height:1.7"><!-- wp:list-item -->
<li>Les <strong>4 objets d'emails</strong> testes qui tiennent au-dessus de 45 % d'ouverture</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Le <strong>planning exact</strong> (delais en jours + tags + conditions FluentCRM)</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>La <strong>bascule vers la newsletter</strong> sans perdre l'engagement acquis</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

</div>
<!-- /wp:group -->

<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"4rem","bottom":"4rem","right":"2rem","left":"2rem"}}},"layout":{"type":"constrained","contentSize":"720px"}} -->
<div class="wp-block-group alignfull" style="padding-top:4rem;padding-right:2rem;padding-bottom:4rem;padding-left:2rem">

<!-- wp:media-text {"align":"none","mediaPosition":"left","mediaWidth":20,"mediaSizeSlug":"thumbnail","verticalAlignment":"center","imageFill":false} -->
<div class="wp-block-media-text is-stacked-on-mobile is-vertically-aligned-center" style="grid-template-columns:20% auto"><figure class="wp-block-media-text__media"><img src="REPLACE_AVEC_URL_PHOTO_MICHAEL" alt="Michael Kihl, fondateur schoolsWP" class="size-thumbnail" style="border-radius:50%"/></figure><div class="wp-block-media-text__content">
<!-- wp:paragraph {"style":{"typography":{"fontSize":"1rem","lineHeight":"1.6"},"color":{"text":"#374151"}}} -->
<p class="has-text-color" style="color:#374151;font-size:1rem;line-height:1.6"><strong>Michael Kihl</strong>, je construis schoolsWP pour aider les freelances WordPress a livrer mieux que les agences. J'installe FluentCRM chez mes clients depuis 3 ans, voici ce qui marche.</p>
<!-- /wp:paragraph -->
</div></div>
<!-- /wp:media-text -->

</div>
<!-- /wp:group -->
```

---

## Notes design

- **Hero (section 1)** : 2 colonnes desktop (58% texte, 42% mockup), stack automatique mobile (Gutenberg core columns). H1 + sous-titre + formulaire FF + reassurance, mockup PDF a droite.
- **Bloc valeur (section 2)** : fond gris clair `#F4F5F7` (token schoolsWP), 3 puces avec gras sur les keywords. H2 centre.
- **Signature (section 3)** : photo ronde 20% largeur a gauche + bio Michael a droite. Alignement vertical centre. Stack mobile auto.
- **Aucun separateur horizontal** (regle schoolsWP : pas de wp:separator). La respiration vient des paddings 4 a 5 rem entre sections.
- **Aucun em-dash ni en-dash** dans le texte (regle branding).
- **Tutoiement** systematique.
- **Pas de Kadence Advanced Button ici** : le CTA est le submit Fluent Forms, ce qui simplifie la cohabitation. Pour styler le bouton submit FF en vert `#00D400` avec hover, ca se fait dans Fluent Forms > Form Settings > Style ou via Custom CSS du formulaire, pas dans la page Gutenberg.

## Ajustements possibles (Michael)

- Remplacer les valeurs `2.75rem`, `2rem`, `1.125rem` par du fluide (`clamp()`) si le theme Kadence l'autorise. Pour l'instant, valeurs fixes safe.
- Ajouter en hero un badge "Gratuit" superpose sur le mockup (cf 02-landing-page.md spec : badge vert `#00D400` en haut-droite, rotation 8 deg). Faisable avec un wp:image overlay et CSS inline ou un bloc Kadence Info Box.
- Convertir la liste 3 puces en `wp:kadence/iconlist` avec icones fleches vertes (`#00D400`) pour matcher la spec 02 ("3 points fleches vertes").
- Ajouter sticky CTA mobile en bas (Kadence Sticky Container ou JS custom) si conversion mobile faible.

---

## Verifications post-creation

- [ ] Page WP creee en draft, slug = `template-welcome-fluentcrm`
- [ ] Meta title et description Rank Math remplis
- [ ] Formulaire FF cree avec id note
- [ ] Mockup PDF uploade et URL collee
- [ ] Photo Michael uploadee et URL collee
- [ ] Apercu de la page : 3 sections rendues, formulaire visible, image mockup affichee
- [ ] Test soumission formulaire avec email perso : redirection vers `/merci-template-welcome-fluentcrm/` OK
- [ ] Dans FluentCRM > Contacts, le contact test a :
  - Liste : FREEBIES schoolsWP (id 26)
  - Tag : freebie_welcome_template_fluentcrm (id 746)
- [ ] Si Funnel 1 publie : verifier que le contact test a recu l'email 1 dans les 5 minutes
- [ ] Publier la page

---

## Lien interne optionnel (post-publication)

Quand le pilier money page FluentCRM sera live, ajouter en pied de landing un petit "Tu veux aller plus loin ?" qui pointe vers `/fluentcrm/`. Pas urgent, n'allonge pas la page de capture inutilement.
