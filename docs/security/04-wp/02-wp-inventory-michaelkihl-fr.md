# Etape 2 - Inventaire WP michaelkihl.fr

> Audit lecture seule via WP REST API. Date : 2026-05-12.
> Auth : Application Password de user `kgd0l7wyuejc` (admin, username randomise = bonne hygiene).
> Aucune valeur secrete dans ce rapport.

---

## Resume executif

Site secondaire, stack tres legere comparee a schoolswp.com :

- **16 plugins** actifs (vs 54 sur schoolswp.com).
- **1 seul user au total**, l admin avec un username randomise `kgd0l7wyuejc` (bonne pratique anti-enumeration).
- **2 Application Passwords** actifs (Novamira + Skoatch), tous deux utilises recemment.
- **Security headers partiellement actifs** sur /wp-login.php (4/6), bien meilleur que schoolswp.com (0/6).
- **Timezone bien configure** (Europe/Paris).
- **Stack SureForms / SureMail / SureRank SEO** : ecosystem Brainstorm Force (Spectra) sur ce site, distinct de Rank Math / FluentSMTP / Kadence-only sur schoolswp.com.
- xmlrpc.php = 403 (block xCloud).

## 1. Identite du site

- **Nom** : 'Michaël KIHL'
- **URL** : https://michaelkihl.fr
- **Description** : 'Création de Sites Internet &amp; Conception Web sur WordPress'
- **Langue** : fr_FR
- **Timezone** : Europe/Paris
- **Admin email** : contact@michaelkihl.fr
- **Page d accueil** : page

## 2. Users

**Total users** : 1

- id=1 username=`kgd0l7wyuejc` email=contact@michaelkihl.fr roles=administrator
- capabilities = 79 (admin standard sans plugins lourds = ~79 normal pour WP core + Fluent Booking + SecuPress)
- inscrit : 2024-10-11T17:35:49+00:00

Le username `kgd0l7wyuejc` est aleatoire (12 chars alphanumeriques), donc impossible a deviner. Bonne pratique a generaliser.

## 3. Application Passwords

| Nom | Cree | Last used | Last IP | Statut |
|---|---|---|---|---|
| Novamira | 2026-04-27 | 2026-05-12 | 85.95.197.29 | ACTIF |
| Skoatch | 2026-05-11 | 2026-05-11 | 67.207.92.92 | ACTIF |

Les 2 passwords sont utilises recemment (< 48h). Aucun orphelin. Bonne hygiene.

## 4. Plugins (16 actifs)

| Nom | Version |
|---|---|
| ClickWhale (Pro) | 2.5.3.5 |
| FluentBooking - Solution de prise de rendez-vous et de réservation | 2.0.05 |
| Fluent Booking Pro | 2.0.05 |
| Kadence Blocks - PRO Extension | 2.8.14 |
| Kadence Blocks — Page Builder Toolkit for Gutenberg Editor | 3.6.7 |
| Kadence Theme Kit Pro - Premium addon for the Kadence Theme | 1.1.19 |
| Novamira | 1.1.2 |
| Novamira Pro | 1.0.0 |
| Safe SVG | 2.4.0 |
| SecuPress Pro with Simple SSL – Simple and Performant Security | 2.6.1 |
| Modèles de démarrage par Kadence WP | 2.2.14 |
| SureForms | 2.8.2 |
| SureForms Business | 2.8.3 |
| SureMail | 1.9.5 |
| SureRank SEO | 1.7.3 |
| WPvivid Backup Plugin | 0.9.126 |

### Observations

- **Stack legere** : 16 plugins, raisonnable.
- **Ecosystem SureForms / SureMail / SureRank** (Brainstorm Force) au lieu de FluentForms / FluentSMTP / Rank Math : choix delibere ?
- **SureForms 2.8.2** + **SureForms Business 2.8.3** : ecart 1 patch, normal pour free + Pro.
- **Novamira v1.1.2 + Novamira Pro v1.0.0** : meme stack que schoolswp.com, MCP REST proxy.
- **SecuPress Pro v2.6.1** : meme version que schoolswp.com (DCTS JS bug applicable).
- **WPvivid Backup v0.9.126** : pas de WP Umbrella sur ce site. Verifier que xCloud snapshot couvre.
- **ClickWhale Pro** : cloak liens affilies, comme schoolswp.com.
- **FluentBooking + Pro** : seul plugin Fluent ici (booking de rendez-vous).
- **Templates de demarrage Kadence v2.2.14** : reste actif (sur schoolswp.com il est inactif). Si pas utilise activement, desactiver.

## 5. Themes

| stylesheet | version | status | parent |
|---|---|---|---|
| discover-kadence | 1.1.1 | active | kadence |
| kadence | 1.4.5 | inactive | kadence |
| twentytwentyfive | 1.4 | inactive | twentytwentyfive |

**twentytwentyfive v1.4** present en inactif = theme fallback WP. Peut etre supprime si SecuPress detecte une faille future.

## 6. REST API

- **33 namespaces, 561 routes**.
- Stack beaucoup plus legere que schoolswp.com (60 / 1886).

Namespaces detectes :

- `clickwhale/v1`
- `fluent-booking/v2`
- `kadence-starter-library/v1`
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
- `mcp`
- `nps-survey/v1`
- `oembed/1.0`
- `sureforms`
- `sureforms-pro`
- `sureforms-pro/v1`
- `sureforms/v1`
- `suremails/v1`
- `surerank/v1`
- `wp-abilities/v1`
- `wp-block-editor/v1`
- `wp-site-health/v1`
- `wp/v2`
- `xcloud-magic-login/v1`

## 7. Headers HTTP et exposure

| Path | HTTP status | HSTS | X-Frame | X-CT | CSP | Referrer | Permissions |
|---|---|---|---|---|---|---|---|
| `/xmlrpc.php` | 403 | MISS | MISS | MISS | MISS | MISS | MISS |
| `/wp-login.php` | 200 | MISS | OK | OK | OK | OK | MISS |
| `/wp-admin/` | 302 | MISS | OK | OK | MISS | MISS | MISS |
| `/?rest_route=/` | 200 | MISS | OK | OK | MISS | MISS | MISS |

**Observations** :

- **xCloud injecte des security headers serveur-level** sur /wp-login.php : X-Frame-Options SAMEORIGIN, X-Content-Type-Options nosniff, CSP frame-ancestors 'self', Referrer-Policy strict-origin-when-cross-origin.
- **HSTS et Permissions-Policy toujours absents**, meme sur xCloud.
- xmlrpc.php = 403 (block actif).
- /wp-admin/ = 302 (redirige vers login).

## 8. Findings classes

### ELEVE

1. **HSTS absent sur xCloud aussi**
   Pas un drame parce que Cloudflare peut l ajouter en amont, mais a vrification.

2. **Pas de plugin de monitoring distant**
   schoolswp.com a WP Umbrella, michaelkihl.fr n a rien. Soit ajouter WP Umbrella ici aussi (free tier OK), soit s appuyer entierement sur xCloud snapshots + alerts.

3. **Templates Kadence v2.2.14 actif**
   Si tu construis ton design sans utiliser ces templates, desactiver pour reduire la surface.

### MOYEN

4. **SecuPress 2.6.1 (meme version que schoolswp.com)**
   DCTS JS bug et historique pwd-fatal applicables.

5. **WPvivid seul (pas de second backup)**
   Le site est moins critique mais une seule source de backup = risque. xCloud snapshot suffit-il ?

### FAIBLE

6. **Username admin randomise**
   Bonne pratique. **A appliquer aussi sur schoolswp.com** (actuellement username = 'Michael KIHL' avec espace).

7. **twentytwentyfive theme inactif**
   Faible vecteur d attaque. A garder comme fallback (recommandation WP) ou supprimer.

---

## Recommandations

Site secondaire, peu de findings critiques. Actions principales :

1. **Renomer l admin sur schoolswp.com** sur le modele de celui-ci (random 12-char).
2. **Ajouter HSTS** via Cloudflare Transform Rules (couvre les 2 sites).
3. **Verifier que xCloud snapshot suffit comme strategie backup unique** ou ajouter WP Umbrella tier free.
4. **Desactiver Templates Kadence** si pas utilise.

## Etape 2 michaelkihl.fr terminee.
