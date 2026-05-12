# Etape 2 - Inventaire WP schoolswp.com

> Audit lecture seule via WP REST API. Date : 2026-05-12.
> Auth : Application Password de Michael KIHL (admin).
> Aucune valeur secrete dans ce rapport.

---

## Resume executif

- **55 plugins** au total (54 actifs, 1 inactif). Stack tres riche, surface d attaque importante.
- **1 user privilegie** (administrator + tutor_instructor), 7 users au total. 598 capabilities sur l admin (poids Fluent + TutorLMS + Kadence).
- **7 Application Passwords** actifs, dont 2 candidats a suppression (SEOpital non-utilise depuis 16 mois, ClaudeAPI jamais utilise).
- **60 namespaces REST**, **1886 routes** exposees. Surface API tres large.
- **Aucun security header HTTP** sauf X-Content-Type-Options sur /?rest_route=/. HSTS, CSP, X-Frame-Options absents.
- **/wp-login.php et /wp-admin/ retournent HTTP 500** sans session : probable artefact SecuPress move-login, a verifier.
- **timezone vide** dans settings WordPress.
- xmlrpc.php = 404 (confirme blocage EasyHoster server-level, conforme memoire).

## 1. Identite du site

- **Nom** : 'schoolsWP'
- **URL** : https://schoolswp.com
- **Description** : 'Formations WordPress pour tous niveaux'
- **Langue** : fr_FR
- **Timezone** : '' (vide = a configurer)
- **Admin email** : contact@michaelkihl.fr
- **Page d accueil** : page (id page = 6)
- **Posts per page** : 9
- **REST authentication exposee** : application-passwords (endpoint declared)

## 2. Utilisateurs (users)

**Total users (tous roles)** : 7
**Privilegies (admin/editor/shop_manager/instructor/fluentcrm_admin/fluent_boards_admin)** : 1

### user id=2

- **username** : `Michael KIHL` (note : valeur litterale, espace inclus)
- **email** : contact@michaelkihl.fr
- **roles** : administrator, tutor_instructor
- **capabilities** : 598 (mosaique Fluent + TutorLMS + Kadence + WP core)
- **extra_capabilities** : 3 (capabilities individuelles, a auditer)
- **inscrit** : 2020-05-18T12:18:18+00:00
- **url profil** : https://schoolswp.com/

## 3. Application Passwords

| Nom | Cree | Last used | Last IP | Statut |
|---|---|---|---|---|
| Skoatch | 2024-06-05 | 2026-05-11 | 67.207.92.92 | ACTIF |
| SEOpital | 2024-06-26 | 2025-01-10 | 13.37.128.122 | DORMANT (> 6 mois) |
| Wisewand | 2026-02-26 | 2026-05-11 | 34.76.27.167 | ACTIF |
| ClaudeAPI | 2026-04-23 | - | - | JAMAIS UTILISE |
| Novamira | 2026-04-27 | 2026-05-12 | 85.95.197.29 | ACTIF |
| routine-plugins-snapshot-weekly | 2026-05-05 | 2026-05-12 | 35.192.191.42 | ACTIF |
| Novamira — Novamira - Gemini | 2026-05-05 | 2026-05-12 | 85.95.197.29 | ACTIF |

**Verdict Application Passwords** :

- `SEOpital` : last_used = 2025-01-10. Inutilise depuis 16 mois. **SUPPRIMER**.
- `ClaudeAPI` : never used depuis creation le 2026-04-23. **SUPPRIMER** ou identifier le process qui devrait l utiliser.
- 5 autres password actifs avec usage recent, repartition par IP :
    - 85.95.197.29 (probable IP residentielle Michael) : Novamira x2
    - 67.207.92.92 (DigitalOcean) : Skoatch
    - 34.76.27.167 (Google Cloud) : Wisewand
    - 35.192.191.42 (Google Cloud) : routine-plugins-snapshot-weekly (n8n probable)

## 4. Plugins (55 total)

### Actifs (54)

| Nom | Version | Author |
|---|---|---|
| Admin and Site Enhancements (ASE) Pro | 8.7.3 | wpase.com |
| Bit Social | 1.13.10 | Bit Social Auto Poster &amp; Scheduler - by Bit Apps |
| Bit Social Pro | 1.13.10 | Bit Apps |
| ClickWhale (Pro) | 2.5.3.5 | ClickWhale |
| CookieYes | GDPR Cookie Consent | 3.4.2 | CookieYes |
| Custom Feed for TikTok | 1.2.3 | Social Feed - WP Social Ninja Team |
| Easy Content Linker (Premium) | 2.14.2 | Baptiste Guiraud |
| FluentAffiliate | 1.4.0 | WPManageNinja |
| FluentAffiliate Pro | 1.4.0 | WPManageNinja LLC |
| Fluent Boards - Outil de gestion de projet | 1.91.3 | WPManageNinja |
| Fluent Boards Pro | 1.91.2 | WPManageNinja |
| FluentBooking - Solution de prise de rendez-vous et de réservation | 2.0.05 | Équipe de solutions pour les rendez-vous et les réservations - WPManageNinja |
| Fluent Booking Pro | 2.0.05 | WPManageNinja LLC |
| FluentCart | 1.3.27 | FluentCart Team |
| FluentCart Pro | 1.3.27 | FluentCart Team |
| FluentCRM - Marketing Automation For WordPress | 2.9.87 | WP Email Newsletter Team - FluentCRM |
| FluentCRM Pro | 2.9.86 | Fluent CRM |
| Fluent Forms | 6.2.2 | Contact Form - WPManageNinja LLC |
| Pack complémentaire Fluent Forms Pro | 6.2.2 | Fluent Forms |
| Fluent PDF Generator | 2.1.1 | WPManageNinja LLC |
| Fluent Roadmap | 1.80 | Fluent Boards |
| FluentSMTP | 2.2.95 | Équipes FluentSMTP &amp; WPManageNinja |
| Fluent Support | 2.1.2 | WPManageNinja LLC |
| Fluent Support Pro | 2.1.1 | WPManageNinja LLC |
| FlyingPress | 5.4.5 | FlyingWeb |
| FreshRank AI Pro | 1.0.0 | Themeisle |
| Indexation instantanée | 1.1.22 | Rank Math |
| Kadence Blocks - PRO Extension | 2.8.14 | Kadence WP |
| Kadence Blocks — Page Builder Toolkit for Gutenberg Editor | 3.7.0 | Kadence WP |
| Kadence Theme Kit Pro - Premium addon for the Kadence Theme | 1.2.0 | Kadence WP |
| Linksgarden | 1.2.2 | Linksgarden |
| Link Whisper Premium | 2.8.9 | Link Whisper |
| Loco Translate | 2.8.4 | Tim Whitlock |
| Make Connector | 1.6.6 | Celonis s.r.o. |
| Ninja Tables Pro | 5.2.8 | WPManageNinja |
| Ninja Tables – Easy Data Table Builder | 5.2.8 | WPManageNinja LLC |
| Novamira | 1.1.2 | Dynamic.ooo |
| Novamira Pro | 1.0.0 | Dynamic.ooo |
| OttoKit | 1.1.27 | OttoKit |
| Polylang | 3.8.3 | WP SYNTEX |
| Presto Player | 4.1.3 | Presto Made, Inc |
| Presto Player Pro | 3.1.4 | Presto Player |
| Rank Math SEO | 1.0.269 | Rank Math SEO |
| Rank Math SEO PRO | 3.0.112 | Rank Math SEO |
| Safe SVG | 2.4.0 | 10up |
| SecuPress Pro with Simple SSL – Simple and Performant Security | 2.6.1 | SecuPress |
| Traduire Sans Migraine | 2.4.33 | Otter Corp |
| Tutor LMS | 3.9.10 | Themeum |
| Tutor LMS Pro | 3.9.9 | Themeum |
| WP Social Ninja | 4.2.1 | WPManageNinja LLC |
| WP Social Ninja Pro | 4.2.1 | WPManageNinja LLC |
| WP Umbrella | 2.23.0 | WP Umbrella - Backup &amp; Manage WordPress |
| WPvivid Backup Plugin | 0.9.126 | WPvivid Backup &amp; Migration |
| WP Webhooks | 3.4.2 | Cozmoslabs |

### Inactifs (1)

- Modèles de démarrage par Kadence WP v2.3.0

### Observations plugins

- Stack Fluent complet (Affiliate, Boards, Booking, Cart, CRM, Forms, PDF, Roadmap, SMTP, Support) en versions free + Pro coexistentes (normal cf memoire reference_wp_plugin_patterns).
- TutorLMS 3.9.10 + Pro 3.9.9 = mismatch versions, ecart 1 patch tolerable.
- SecuPress Pro 2.6.1 : version qui avait corrompu wp-config.php (cf memoire project_secupress_activation_fix). DCTS JS bug documente (cf memoire reference_secupress_dcts_js_bug).
- Novamira v1.1.2 + Novamira Pro v1.0.0 = le plugin MCP REST proxy. La connexion MCP n etait pas active dans la session courante.
- 2 plugins backup co-actifs : WP Umbrella v2.23.0 + WPvivid v0.9.126. Coherent (WP Umbrella = monitoring + backup chaud, WPvivid = backup local).
- ClickWhale Pro v2.5.3.5 = cloak des liens affilies (schoolswp.com/<plugin>).
- Make Connector v1.6.6 (Celonis/Integromat ex) : verifier si encore utilise sinon desactiver.
- FreshRank AI Pro v1.0.0 : a auditer (v1.0.0 = potentiellement instable).

**Vulns plugins** : skipped dans cette session (classifier a bloque l appel direct a l API WP Umbrella). Pour les obtenir : lance `/umbrella:health` toi-meme dans une session interactive, ou ouvre app.wp-umbrella.com.

## 5. Themes

| stylesheet | version | status | parent |
|---|---|---|---|
| discover-kadence | 1.2.0 | active | kadence |
| kadence | 1.5.0 | inactive | kadence |

Hygiene : 2 themes presents (1 actif child + 1 parent inactif). Pas de twentytwenty* legacy. Bon point.

## 6. Post types (28)

`post, page, attachment, nav_menu_item, wp_block, wp_template, wp_template_part, wp_global_styles, wp_navigation, wp_font_family, wp_font_face, kadence_element, kadence_form, kadence_navigation, kadence_header, kadence_custom_svg, kadence_query, kadence_query_card, fct-dummy, fluent-products, pp_video_block, courses, kadence_lottie, kadence_vector, kb_icon, rm_content_editor, rank_math_schema, pp_email_submission`

Standard WP + lots Kadence (10) + Fluent (2) + Presto Player (2) + Tutor (1: courses) + Rank Math (2).

## 7. REST API namespaces exposes

**60 namespaces, 1886 routes**.

Namespaces detectes :

- `bit-social`
- `cky/v1`
- `clickwhale/v1`
- `cookieyes/v1`
- `fluent-affiliate/v2`
- `fluent-boards/v2`
- `fluent-booking/v2`
- `fluent-cart/v1`
- `fluent-cart/v2`
- `fluent-crm/v2`
- `fluent-smtp`
- `fluent-support/v2`
- `fluentform/v1`
- `kb-activecampaign/v1`
- `kb-convertkit/v1`
- `kb-custom-svg/v1`
- `kb-design-library/v1`
- `kb-fluentcrm/v1`
- `kb-getresponse/v1`
- `kb-image-picker/v1`
- `kb-lottieanimation/v1`
- `kb-mailchimp/v1`
- `kb-mailerlite/v1`
- `kb-sendinblue/v1`
- `kb-vector/v1`
- `kbp-dynamic/v1`
- `kbp/v1`
- `kbpp/v1`
- `ktp/v1`
- `lg/v1`
- `link-whisper`
- `liquidweb/harbor/v1`
- `mcp`
- `ninjatables/v2`
- `nps-survey/v1`
- `oembed/1.0`
- `pll/v1`
- `presto-player/v1`
- `presto-player/v1/activecampaign`
- `presto-player/v1/analytics`
- `presto-player/v1/email`
- `presto-player/v1/fluentcrm`
- `presto-player/v1/mailchimp`
- `presto-player/v1/mailerlite`
- `rankmath/v1`
- `rankmath/v1/an`
- `rankmath/v1/ca`
- `rankmath/v1/in`
- `rankmath/v1/link-genius`
- `rankmath/v1/setupWizard`
- `rankmath/v1/status`
- `seo-sans-migraine`
- `sure-triggers/v1`
- `tutor/v1`
- `wp-abilities/v1`
- `wp-block-editor/v1`
- `wp-site-health/v1`
- `wp-umbrella/v1`
- `wp/v2`
- `wpsocialreviews/v2`

**A investiguer** :

- `mcp` namespace : declaration WP-MCP du plugin Novamira (a verifier que les endpoints sont auth-only).
- `wp-abilities/v1` : namespace WP Abilities (introduit par WP 6.6+). Verifier que les capabilities exposees sont publiques par design.
- `liquidweb/harbor/v1` : namespace inconnu, vient de quel plugin ? Investiguer.
- `rankmath/v1/setupWizard` : wizard de config. Devrait etre accessible uniquement par admin.

## 8. Headers HTTP et exposure

| Path | HTTP status | HSTS | X-Frame | X-CT | CSP | Referrer | Permissions |
|---|---|---|---|---|---|---|---|
| `/xmlrpc.php` | 404 | MISS | MISS | MISS | MISS | MISS | MISS |
| `/wp-login.php` | 500 | MISS | MISS | MISS | MISS | MISS | MISS |
| `/wp-admin/` | 500 | MISS | MISS | MISS | MISS | MISS | MISS |
| `/?rest_route=/` | 200 | MISS | MISS | OK | MISS | MISS | MISS |

**Anomalies** :

- /wp-login.php = HTTP 500 : probable artefact SecuPress move-login (URL reelle de login differente, /wp-login.php direct casse). **A verifier**.
- /wp-admin/ = HTTP 500 : meme cause probable. Verifier.
- xmlrpc.php = HTTP 404 (et pas 403) : EasyHoster a sans doute redirige xmlrpc -> 127.0.0.1 server-level (cf memoire reference_hosting_easyhoster).
- Server header expose : `nginx` (sans version, OK). X-Powered-By absent (bon).
- **Aucun HSTS, aucun CSP, aucun X-Frame-Options**. C est le finding **CRITIQUE** de cette etape. Cloudflare peut injecter ces headers via Page Rules / Transform Rules.

## 9. Findings classes

### CRITIQUE

1. **Aucun security header HTTP serveur-level**
   HSTS, CSP, X-Frame-Options, Referrer-Policy, Permissions-Policy tous absents. Pour un site qui touche du paiement FluentCart + collecte des PII FluentCRM, c est un gap reglementaire (RGPD) et un risque clickjacking + downgrade TLS. **Fix prioritaire** : injecter les headers via Cloudflare Transform Rules ou via SecuPress (module headers).

2. **2 Application Passwords orphelins**
   `SEOpital` (inutilise depuis janvier 2025) + `ClaudeAPI` (jamais utilise). Surface d acces ouverte sans contrepartie. **Supprimer immediatement** via WP Admin > Profils > Mots de passe d application.

3. **/wp-login.php et /wp-admin/ retournent 500 sans session**
   Inconsistant. Soit SecuPress move-login + ferme l acces direct, soit erreur PHP/configuration. A diagnostiquer : si tu peux toujours te connecter via l URL move-login, c est OK. Sinon, anomalie a fixer.

4. **598 capabilities sur le seul admin**
   Concentration de pouvoir + difficulte d audit des capabilities heritees. La perte de ce compte = perte totale. Mitigations : durcir le password + Application Password unique par usage (deja en place) + activer 2FA sur le login admin via SecuPress.

### ELEVE

5. **60 namespaces REST + 1886 routes**
   Surface d API tres large. Chaque plugin (Fluent suite + Kadence + Rank Math + Presto Player + TutorLMS + etc.) ajoute le sien. Audit specifique de `wp-abilities/v1`, `mcp`, `liquidweb/harbor/v1`, `rankmath/v1/setupWizard` requis : confirmer que les endpoints qui mutent l etat exigent une capability admin.

6. **Mu-plugins, wp-config.php constantes et SecuPress submodules NON inspectes**
   Le REST API ne donne pas acces a ces points. Sans Novamira MCP execute-php cette session, ils restent un trou dans l audit. A combler quand Novamira sera reconnecte ou en sondant via WP-CLI (xCloud / EasyHoster panel).

7. **timezone WordPress vide**
   Les operations FluentCart (factures), FluentCRM (envois email programmes), TutorLMS (deadlines) utilisent par defaut UTC. Mettre `Europe/Paris` dans WP Admin > Reglages.

8. **2 plugins backup co-actifs**
   WP Umbrella + WPvivid. Le risque : si l un cron-overlap l autre, charge serveur + corruption potentielle. Verifier que les fenetres de backup ne se croisent pas.

9. **Make Connector v1.6.6 actif**
   Successeur d Integromat. Verifier qu il est encore utilise (sinon desactiver, surface d attaque pour rien).

10. **FreshRank AI Pro v1.0.0**
    Version 1.0.0 d un plugin Themeisle utilisant l IA. Auditer la maturite + le scope des appels reseau.

### MOYEN

11. **MCP namespace `mcp` expose**
    Verifier les endpoints exposes et que l authentification est obligatoire pour toute mutation.

12. **Plugin Novamira (v1.1.2 + Pro v1.0.0)**
    Source de verite des audits Claude Code. Verifier nb d Application Passwords actifs (Novamira + Novamira-Gemini = 2), et que l IP 85.95.197.29 est bien residentielle Michael (sinon = compromission).

13. **Bit Social v1.13.10 + Pro v1.13.10**
    Plugin garde (memoire project_plugin_strategic_decisions), mais a auditer pour eviter token-leak vers les reseaux sociaux.

14. **3 extra_capabilities individuelles sur l admin**
    En plus des 598 capacites de role, 3 capabilities propres a ce user. Liste a obtenir via WP-CLI ou Novamira.

### FAIBLE

15. **WP Umbrella plugin v2.23.0 actif**
    Bon. Verifier qu il pointe vers le bon team plan et que la routine plugins-snapshot-weekly tourne (cf memoire reference_routine_plugins_snapshot).

16. **6 users non-administrators**
    Probable abonnes newsletter/FluentCRM ou customers FluentCart. A verifier qu aucun n a un role inattendu.

---

## Recommandations

| Finding | Etape briefing | Priorite |
|---|---|---|
| #1 (headers) | Etape 7 (Cloudflare) | P0, semaine 2 |
| #2 (app passwords orphelins) | Manuel WP Admin, immediat | P0, aujourd hui |
| #3 (500 sur login/admin) | Manuel, verifier move-login SecuPress | P0, aujourd hui |
| #4 (concentration admin) | Etape 6 (WP users) + Etape 8 (2FA) | P1 |
| #5 (REST namespaces) | Etape 7 + audit Novamira reconnecte | P1 |
| #6 (mu-plugins/wp-config inspection) | Repeat etape 2 quand Novamira reconnecte | P1 |
| #7 (timezone) | WP Admin > Reglages, immediat | P2 |
| #8 (backup overlap) | Audit cron, manuel | P2 |
| #9, #10 (plugins a auditer) | Etape 6 elargi | P2 |
| #11, #12, #13 (REST plugin namespaces) | Etape 7 | P2 |
| #14 (extra_caps) | Quand Novamira reconnecte | P2 |

**Bloqueurs sans Novamira MCP** :

- Inspection wp-config.php (DISALLOW_FILE_EDIT, FORCE_SSL_ADMIN, SECUPRESS_*, WP_DEBUG).
- Liste mu-plugins (schoolswp-person-schema, schoolswp-ai-summary-buttons, FluentCampaign tag_based_redirect, etc.).
- Liste SecuPress modules actifs et leurs configurations.
- Liste extra_capabilities individuelles sur l admin.
- Audit roles personnalises via wp_options.wp_user_roles.

Quand Novamira MCP est reconnecte, rejouer un mini-audit ciblant ces 5 points.

## Etape 2 schoolswp.com terminee.
