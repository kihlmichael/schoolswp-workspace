# SITE.md — Snapshot WordPress schoolswp.com

Source : MCP `novamira-schoolswp-com` via `novamira/execute-php` (fonctions WP lecture seule).
Mis à jour via `shared/skills/refresh-site-md.md`.

**Dernière mise à jour** : 2026-04-17 (refresh complet via MCP)

---

## Environnement

- **WordPress** : 6.9.4
- **PHP** : 8.3.30
- **Locale** : fr_FR
- **Site URL** : <https://schoolswp.com>
- **Hébergement** : EasyHoster
- **Thème actif** : **Discover v1.2.0** (enfant de Kadence — thème parent)
- **Multilingue** : Polylang v3.8.2 + Traduire Sans Migraine v2.4.33 (traduction auto AI)

**Total plugins** : 54 installés, 53 actifs (1 inactif : SecuPress Pro, erreur fatale)

---

## Plugins actifs

### SEO & Performance (8)

- Rank Math SEO PRO v3.0.111
- Rank Math SEO v1.0.268 (requis par Pro)
- FlyingPress v5.4.1
- FreshRank AI Pro v1.0.0
- Instant Indexing v1.1.22
- Link Whisper Premium v2.8.8
- Easy Content Linker (Premium) v2.14.0
- Linksgarden v1.2.2

### Fluent Suite (17)

- FluentCRM v2.9.87 + FluentCRM Pro v2.9.86 (Pro à jour — addon séparé, pas de 2.9.87 Pro publié)
- FluentCart v1.3.18 + FluentCart Pro v1.3.18
- FluentBooking v2.0.05 + FluentBooking Pro v2.0.05
- Fluent Support v2.1.1 + Fluent Support Pro v2.1.1
- FluentAffiliate v1.4.0 + FluentAffiliate Pro v1.4.0
- Fluent Boards v1.91.3 + Fluent Boards Pro v1.91.2 (Pro à jour — addon séparé)
- Fluent Forms v6.2.1 + Fluent Forms Pro Add On Pack v6.2.1
- FluentSMTP v2.2.95
- Fluent PDF Generator v2.1.1
- Fluent Roadmap v1.80

### LMS (2)

- Tutor LMS v3.9.9
- Tutor LMS Pro v3.9.9
- Utilisé pour schoolsWP Academy

### Automation & Intégrations (4)

- OttoKit v1.1.25 (ex SureTriggers)
- Make Connector v1.6.6
- WP Webhooks v3.4.0
- Bit Social v1.13.6 + Bit Social Pro v1.13.6

### Multilingue & Traduction (3)

- Polylang v3.8.2 (plugin multilingue principal)
- Traduire Sans Migraine v2.4.33 (extension Polylang — traduction auto AI)
- Loco Translate v2.8.3

### Contenu & Média (9)

- Kadence Blocks v3.6.7 + Kadence Blocks Pro v2.8.14
- Kadence Theme Kit Pro v1.1.19
- Starter Templates by Kadence WP v2.2.14
- Presto Player v4.1.3 + Presto Player Pro v3.1.4
- Ninja Tables v5.2.8 + Ninja Tables Pro v5.2.8
- Safe SVG v2.4.0
- Custom Feed for TikTok v1.2.1

### Social (2)

- WP Social Ninja v4.1.0 + WP Social Ninja Pro v4.1.0

### Backup & Monitoring (2)

- WPvivid Backup Plugin v0.9.125
- WP Umbrella v2.22.4 (monitoring santé site)

### Sécurité & RGPD (2)

- CookieYes | GDPR Cookie Consent v3.4.2
- ⚠️ **SecuPress Pro v2.6.1** — **INACTIF**, erreur fatale à l'activation. À débuguer (compatibilité PHP 8.3 probable, ou conflit plugin).

### Admin (2)

- Admin and Site Enhancements (ASE) Pro v8.6.2
- ClickWhale Pro v2.5.3.5

### Infrastructure Claude (1)

- **Novamira v1.0.3** — bridge MCP ↔ WordPress

---

## Changements vs snapshot précédent (2026-04-17 initial → refresh)

**+9 plugins découverts** (liste tronquée au premier snapshot) :

- Traduire Sans Migraine v2.4.33
- Tutor LMS v3.9.9 + Tutor LMS Pro v3.9.9
- WP Social Ninja v4.1.0 + Pro v4.1.0
- WP Umbrella v2.22.4
- WPvivid Backup v0.9.125
- Starter Templates by Kadence WP v2.2.14
- WP Webhooks v3.4.0

**Corrections** :

- Thème réel : **Discover v1.2.0** (enfant de Kadence), pas "Kadence + Blocks + Theme Kit" directs
- CookieYes : v3.4.1 → **v3.4.2** (update silencieux)
- "Site Assist" (menu sidebar) = pas un plugin séparé, item d'un autre plugin

## Doublons détectés (à auditer)

Aucun à ce jour.

## Points d'attention

1. ⚠️ **SecuPress Pro** : erreur fatale à l'activation. Debug prioritaire ou désinstallation.
2. ✅ **FluentCRM Pro** (v2.9.86) et **Fluent Boards Pro** (v1.91.2) : OK. Les Pro sont des addons séparés avec leur propre versioning. Confirmé via query serveur WPFluent 2026-04-18 : aucune MAJ disponible.
3. **Polylang + Traduire Sans Migraine** : combo de traduction auto AI. Pas un conflit — extension officielle.

## Patterns normaux (ne pas flagger)

- **Rank Math** : free + PRO → Pro requiert free pour fonctionner.
- **Fluent Suite** : chaque plugin Fluent en binôme free + Pro.
- **Kadence** : Blocks + Blocks Pro + Theme Kit Pro + Starter Templates + thème enfant Discover → architecture modulaire.
- **WP Social Ninja** : free + Pro.
- **Bit Social** : free + Pro.
- **Presto Player** : free + Pro.
- **Ninja Tables** : free + Pro.

---

## Ressources critiques

- **URL prod** : <https://schoolswp.com>
- **URL admin** : <https://schoolswp.com/wp-admin>
- **URL n8n** : <https://schoolswp-n8n.wp1.host>
- **MCP novamira** : contrôle complet (lecture libre, écriture confirmation humaine obligatoire — voir `RULES.md` §6)

## Stack technique schoolsWP (source : `shared/skills/wordpress-stack.md`)

- LMS : Tutor LMS + Tutor LMS Pro (schoolsWP Academy)
- SEO ops : Thruuu + GSC + DataForSEO
- Automation : n8n + OttoKit + WP Webhooks + Make
- CRM : FluentCRM Pro
- Email SMTP : FluentSMTP
- Backup : WPvivid
- Monitoring : WP Umbrella
