"""Generate the two markdown WP inventory reports from the audit JSONs."""
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).parent


def fmt_plugins_table(plugins_list):
    rows = []
    for pl in plugins_list:
        name = pl.get("name")
        if isinstance(name, dict):
            name = name.get("raw") or name.get("rendered") or "?"
        rows.append(f"| {name} | {pl.get('version')} | {pl.get('status')} |")
    return "\n".join(rows)


def build_report_schoolswp(r):
    parts = []
    parts.append("# Etape 2 - Inventaire WP schoolswp.com\n\n")
    parts.append("> Audit lecture seule via WP REST API. Date : 2026-05-12.\n")
    parts.append("> Auth : Application Password de Michael KIHL (admin).\n")
    parts.append("> Aucune valeur secrete dans ce rapport.\n\n")
    parts.append("---\n\n")

    parts.append("## Resume executif\n\n")
    parts.append("- **55 plugins** au total (54 actifs, 1 inactif). Stack tres riche, surface d attaque importante.\n")
    parts.append("- **1 user privilegie** (administrator + tutor_instructor), 7 users au total. 598 capabilities sur l admin (poids Fluent + TutorLMS + Kadence).\n")
    parts.append("- **7 Application Passwords** actifs, dont 2 candidats a suppression (SEOpital non-utilise depuis 16 mois, ClaudeAPI jamais utilise).\n")
    parts.append("- **60 namespaces REST**, **1886 routes** exposees. Surface API tres large.\n")
    parts.append("- **Aucun security header HTTP** sauf X-Content-Type-Options sur /?rest_route=/. HSTS, CSP, X-Frame-Options absents.\n")
    parts.append("- **/wp-login.php et /wp-admin/ retournent HTTP 500** sans session : probable artefact SecuPress move-login, a verifier.\n")
    parts.append("- **timezone vide** dans settings WordPress.\n")
    parts.append("- xmlrpc.php = 404 (confirme blocage EasyHoster server-level, conforme memoire).\n\n")

    d = r["checks"]["discovery"]
    s = r["checks"].get("settings", {})
    parts.append("## 1. Identite du site\n\n")
    parts.append(f"- **Nom** : {d.get('name')!r}\n")
    parts.append(f"- **URL** : {d.get('url')}\n")
    parts.append(f"- **Description** : {s.get('description', '?')!r}\n")
    parts.append(f"- **Langue** : {s.get('language', '?')}\n")
    parts.append(f"- **Timezone** : {s.get('timezone', '?')!r} (vide = a configurer)\n")
    parts.append(f"- **Admin email** : {s.get('admin_email', '?')}\n")
    parts.append(f"- **Page d accueil** : {s.get('show_on_front')} (id page = {s.get('page_on_front')})\n")
    parts.append(f"- **Posts per page** : {s.get('posts_per_page')}\n")
    parts.append(f"- **REST authentication exposee** : application-passwords (endpoint declared)\n\n")

    parts.append("## 2. Utilisateurs (users)\n\n")
    u = r["checks"].get("users_privileged", {})
    total = r["checks"].get("users_total", {}).get("total_count", "?")
    parts.append(f"**Total users (tous roles)** : {total}\n")
    parts.append(f"**Privilegies (admin/editor/shop_manager/instructor/fluentcrm_admin/fluent_boards_admin)** : {u.get('count')}\n\n")
    for usr in u.get("users", []):
        parts.append(f"### user id={usr['id']}\n\n")
        parts.append(f"- **username** : `{usr['username']}` (note : valeur litterale, espace inclus)\n")
        parts.append(f"- **email** : {usr['email']}\n")
        parts.append(f"- **roles** : {', '.join(usr['roles'])}\n")
        parts.append(f"- **capabilities** : {usr['capabilities_count']} (mosaique Fluent + TutorLMS + Kadence + WP core)\n")
        parts.append(f"- **extra_capabilities** : {usr['extra_capabilities_count']} (capabilities individuelles, a auditer)\n")
        parts.append(f"- **inscrit** : {usr['registered_date']}\n")
        parts.append(f"- **url profil** : {usr.get('url', '-')}\n\n")

    parts.append("## 3. Application Passwords\n\n")
    ap = r["checks"].get("application_passwords", {})
    if ap.get("users"):
        parts.append("| Nom | Cree | Last used | Last IP | Statut |\n|---|---|---|---|---|\n")
        for entry in ap["users"]:
            for p in entry.get("names", []):
                status = "ACTIF" if p["last_used"] else "JAMAIS UTILISE"
                if p["last_used"] and p["last_used"] < "2025-06-01":
                    status = "DORMANT (> 6 mois)"
                parts.append(f"| {p['name']} | {p['created'][:10]} | {(p['last_used'] or '-')[:10]} | {p['last_ip'] or '-'} | {status} |\n")
        parts.append("\n")

    parts.append("**Verdict Application Passwords** :\n\n")
    parts.append("- `SEOpital` : last_used = 2025-01-10. Inutilise depuis 16 mois. **SUPPRIMER**.\n")
    parts.append("- `ClaudeAPI` : never used depuis creation le 2026-04-23. **SUPPRIMER** ou identifier le process qui devrait l utiliser.\n")
    parts.append("- 5 autres password actifs avec usage recent, repartition par IP :\n")
    parts.append("    - 85.95.197.29 (probable IP residentielle Michael) : Novamira x2\n")
    parts.append("    - 67.207.92.92 (DigitalOcean) : Skoatch\n")
    parts.append("    - 34.76.27.167 (Google Cloud) : Wisewand\n")
    parts.append("    - 35.192.191.42 (Google Cloud) : routine-plugins-snapshot-weekly (n8n probable)\n\n")

    parts.append("## 4. Plugins (55 total)\n\n")
    pl = r["checks"].get("plugins", {})
    actives = pl.get("active", [])
    inactives = pl.get("inactive", [])
    parts.append(f"### Actifs ({len(actives)})\n\n")
    parts.append("| Nom | Version | Author |\n|---|---|---|\n")
    for p in actives:
        name = p.get("name")
        if isinstance(name, dict):
            name = name.get("raw") or name.get("rendered") or "?"
        author = p.get("author")
        if isinstance(author, dict):
            author = author.get("raw") or author.get("rendered") or "?"
        parts.append(f"| {name} | {p.get('version')} | {author} |\n")
    parts.append("\n")

    parts.append(f"### Inactifs ({len(inactives)})\n\n")
    for p in inactives:
        name = p.get("name")
        if isinstance(name, dict):
            name = name.get("raw") or name.get("rendered") or "?"
        parts.append(f"- {name} v{p.get('version')}\n")
    parts.append("\n")

    parts.append("### Observations plugins\n\n")
    parts.append("- Stack Fluent complet (Affiliate, Boards, Booking, Cart, CRM, Forms, PDF, Roadmap, SMTP, Support) en versions free + Pro coexistentes (normal cf memoire reference_wp_plugin_patterns).\n")
    parts.append("- TutorLMS 3.9.10 + Pro 3.9.9 = mismatch versions, ecart 1 patch tolerable.\n")
    parts.append("- SecuPress Pro 2.6.1 : version qui avait corrompu wp-config.php (cf memoire project_secupress_activation_fix). DCTS JS bug documente (cf memoire reference_secupress_dcts_js_bug).\n")
    parts.append("- Novamira v1.1.2 + Novamira Pro v1.0.0 = le plugin MCP REST proxy. La connexion MCP n etait pas active dans la session courante.\n")
    parts.append("- 2 plugins backup co-actifs : WP Umbrella v2.23.0 + WPvivid v0.9.126. Coherent (WP Umbrella = monitoring + backup chaud, WPvivid = backup local).\n")
    parts.append("- ClickWhale Pro v2.5.3.5 = cloak des liens affilies (schoolswp.com/<plugin>).\n")
    parts.append("- Make Connector v1.6.6 (Celonis/Integromat ex) : verifier si encore utilise sinon desactiver.\n")
    parts.append("- FreshRank AI Pro v1.0.0 : a auditer (v1.0.0 = potentiellement instable).\n\n")
    parts.append("**Vulns plugins** : skipped dans cette session (classifier a bloque l appel direct a l API WP Umbrella). Pour les obtenir : lance `/umbrella:health` toi-meme dans une session interactive, ou ouvre app.wp-umbrella.com.\n\n")

    parts.append("## 5. Themes\n\n")
    parts.append("| stylesheet | version | status | parent |\n|---|---|---|---|\n")
    for th in r["checks"].get("themes", {}).get("themes", []):
        parts.append(f"| {th['stylesheet']} | {th['version']} | {th['status']} | {th['parent_theme'] or '-'} |\n")
    parts.append("\nHygiene : 2 themes presents (1 actif child + 1 parent inactif). Pas de twentytwenty* legacy. Bon point.\n\n")

    parts.append("## 6. Post types (28)\n\n")
    pt = r["checks"].get("post_types", {})
    parts.append(f"`{', '.join(pt.get('types', []))}`\n\n")
    parts.append("Standard WP + lots Kadence (10) + Fluent (2) + Presto Player (2) + Tutor (1: courses) + Rank Math (2).\n\n")

    parts.append("## 7. REST API namespaces exposes\n\n")
    ns = r["checks"]["discovery"].get("namespaces", [])
    parts.append(f"**{len(ns)} namespaces, {r['checks']['discovery'].get('routes_count')} routes**.\n\n")
    parts.append("Namespaces detectes :\n\n")
    for n in ns:
        parts.append(f"- `{n}`\n")
    parts.append("\n**A investiguer** :\n\n")
    parts.append("- `mcp` namespace : declaration WP-MCP du plugin Novamira (a verifier que les endpoints sont auth-only).\n")
    parts.append("- `wp-abilities/v1` : namespace WP Abilities (introduit par WP 6.6+). Verifier que les capabilities exposees sont publiques par design.\n")
    parts.append("- `liquidweb/harbor/v1` : namespace inconnu, vient de quel plugin ? Investiguer.\n")
    parts.append("- `rankmath/v1/setupWizard` : wizard de config. Devrait etre accessible uniquement par admin.\n\n")

    parts.append("## 8. Headers HTTP et exposure\n\n")
    exp = r["checks"].get("exposure", {})
    parts.append("| Path | HTTP status | HSTS | X-Frame | X-CT | CSP | Referrer | Permissions |\n|---|---|---|---|---|---|---|---|\n")
    for path, info in exp.items():
        sh = info.get("security_headers", {})
        flags = []
        for h in ["Strict-Transport-Security", "X-Frame-Options", "X-Content-Type-Options", "Content-Security-Policy", "Referrer-Policy", "Permissions-Policy"]:
            flags.append("OK" if sh.get(h) else "MISS")
        parts.append(f"| `{path}` | {info.get('status')} | {flags[0]} | {flags[1]} | {flags[2]} | {flags[3]} | {flags[4]} | {flags[5]} |\n")
    parts.append("\n")
    parts.append("**Anomalies** :\n\n")
    parts.append("- /wp-login.php = HTTP 500 : probable artefact SecuPress move-login (URL reelle de login differente, /wp-login.php direct casse). **A verifier**.\n")
    parts.append("- /wp-admin/ = HTTP 500 : meme cause probable. Verifier.\n")
    parts.append("- xmlrpc.php = HTTP 404 (et pas 403) : EasyHoster a sans doute redirige xmlrpc -> 127.0.0.1 server-level (cf memoire reference_hosting_easyhoster).\n")
    parts.append("- Server header expose : `nginx` (sans version, OK). X-Powered-By absent (bon).\n")
    parts.append("- **Aucun HSTS, aucun CSP, aucun X-Frame-Options**. C est le finding **CRITIQUE** de cette etape. Cloudflare peut injecter ces headers via Page Rules / Transform Rules.\n\n")

    parts.append("## 9. Findings classes\n\n")
    parts.append("### CRITIQUE\n\n")
    parts.append("1. **Aucun security header HTTP serveur-level**\n")
    parts.append("   HSTS, CSP, X-Frame-Options, Referrer-Policy, Permissions-Policy tous absents. Pour un site qui touche du paiement FluentCart + collecte des PII FluentCRM, c est un gap reglementaire (RGPD) et un risque clickjacking + downgrade TLS. **Fix prioritaire** : injecter les headers via Cloudflare Transform Rules ou via SecuPress (module headers).\n\n")
    parts.append("2. **2 Application Passwords orphelins**\n")
    parts.append("   `SEOpital` (inutilise depuis janvier 2025) + `ClaudeAPI` (jamais utilise). Surface d acces ouverte sans contrepartie. **Supprimer immediatement** via WP Admin > Profils > Mots de passe d application.\n\n")
    parts.append("3. **/wp-login.php et /wp-admin/ retournent 500 sans session**\n")
    parts.append("   Inconsistant. Soit SecuPress move-login + ferme l acces direct, soit erreur PHP/configuration. A diagnostiquer : si tu peux toujours te connecter via l URL move-login, c est OK. Sinon, anomalie a fixer.\n\n")
    parts.append("4. **598 capabilities sur le seul admin**\n")
    parts.append("   Concentration de pouvoir + difficulte d audit des capabilities heritees. La perte de ce compte = perte totale. Mitigations : durcir le password + Application Password unique par usage (deja en place) + activer 2FA sur le login admin via SecuPress.\n\n")

    parts.append("### ELEVE\n\n")
    parts.append("5. **60 namespaces REST + 1886 routes**\n")
    parts.append("   Surface d API tres large. Chaque plugin (Fluent suite + Kadence + Rank Math + Presto Player + TutorLMS + etc.) ajoute le sien. Audit specifique de `wp-abilities/v1`, `mcp`, `liquidweb/harbor/v1`, `rankmath/v1/setupWizard` requis : confirmer que les endpoints qui mutent l etat exigent une capability admin.\n\n")
    parts.append("6. **Mu-plugins, wp-config.php constantes et SecuPress submodules NON inspectes**\n")
    parts.append("   Le REST API ne donne pas acces a ces points. Sans Novamira MCP execute-php cette session, ils restent un trou dans l audit. A combler quand Novamira sera reconnecte ou en sondant via WP-CLI (xCloud / EasyHoster panel).\n\n")
    parts.append("7. **timezone WordPress vide**\n")
    parts.append("   Les operations FluentCart (factures), FluentCRM (envois email programmes), TutorLMS (deadlines) utilisent par defaut UTC. Mettre `Europe/Paris` dans WP Admin > Reglages.\n\n")
    parts.append("8. **2 plugins backup co-actifs**\n")
    parts.append("   WP Umbrella + WPvivid. Le risque : si l un cron-overlap l autre, charge serveur + corruption potentielle. Verifier que les fenetres de backup ne se croisent pas.\n\n")
    parts.append("9. **Make Connector v1.6.6 actif**\n")
    parts.append("   Successeur d Integromat. Verifier qu il est encore utilise (sinon desactiver, surface d attaque pour rien).\n\n")
    parts.append("10. **FreshRank AI Pro v1.0.0**\n")
    parts.append("    Version 1.0.0 d un plugin Themeisle utilisant l IA. Auditer la maturite + le scope des appels reseau.\n\n")

    parts.append("### MOYEN\n\n")
    parts.append("11. **MCP namespace `mcp` expose**\n")
    parts.append("    Verifier les endpoints exposes et que l authentification est obligatoire pour toute mutation.\n\n")
    parts.append("12. **Plugin Novamira (v1.1.2 + Pro v1.0.0)**\n")
    parts.append("    Source de verite des audits Claude Code. Verifier nb d Application Passwords actifs (Novamira + Novamira-Gemini = 2), et que l IP 85.95.197.29 est bien residentielle Michael (sinon = compromission).\n\n")
    parts.append("13. **Bit Social v1.13.10 + Pro v1.13.10**\n")
    parts.append("    Plugin garde (memoire project_plugin_strategic_decisions), mais a auditer pour eviter token-leak vers les reseaux sociaux.\n\n")
    parts.append("14. **3 extra_capabilities individuelles sur l admin**\n")
    parts.append("    En plus des 598 capacites de role, 3 capabilities propres a ce user. Liste a obtenir via WP-CLI ou Novamira.\n\n")

    parts.append("### FAIBLE\n\n")
    parts.append("15. **WP Umbrella plugin v2.23.0 actif**\n")
    parts.append("    Bon. Verifier qu il pointe vers le bon team plan et que la routine plugins-snapshot-weekly tourne (cf memoire reference_routine_plugins_snapshot).\n\n")
    parts.append("16. **6 users non-administrators**\n")
    parts.append("    Probable abonnes newsletter/FluentCRM ou customers FluentCart. A verifier qu aucun n a un role inattendu.\n\n")

    parts.append("---\n\n## Recommandations\n\n")
    parts.append("| Finding | Etape briefing | Priorite |\n|---|---|---|\n")
    parts.append("| #1 (headers) | Etape 7 (Cloudflare) | P0, semaine 2 |\n")
    parts.append("| #2 (app passwords orphelins) | Manuel WP Admin, immediat | P0, aujourd hui |\n")
    parts.append("| #3 (500 sur login/admin) | Manuel, verifier move-login SecuPress | P0, aujourd hui |\n")
    parts.append("| #4 (concentration admin) | Etape 6 (WP users) + Etape 8 (2FA) | P1 |\n")
    parts.append("| #5 (REST namespaces) | Etape 7 + audit Novamira reconnecte | P1 |\n")
    parts.append("| #6 (mu-plugins/wp-config inspection) | Repeat etape 2 quand Novamira reconnecte | P1 |\n")
    parts.append("| #7 (timezone) | WP Admin > Reglages, immediat | P2 |\n")
    parts.append("| #8 (backup overlap) | Audit cron, manuel | P2 |\n")
    parts.append("| #9, #10 (plugins a auditer) | Etape 6 elargi | P2 |\n")
    parts.append("| #11, #12, #13 (REST plugin namespaces) | Etape 7 | P2 |\n")
    parts.append("| #14 (extra_caps) | Quand Novamira reconnecte | P2 |\n")
    parts.append("\n")
    parts.append("**Bloqueurs sans Novamira MCP** :\n\n")
    parts.append("- Inspection wp-config.php (DISALLOW_FILE_EDIT, FORCE_SSL_ADMIN, SECUPRESS_*, WP_DEBUG).\n")
    parts.append("- Liste mu-plugins (schoolswp-person-schema, schoolswp-ai-summary-buttons, FluentCampaign tag_based_redirect, etc.).\n")
    parts.append("- Liste SecuPress modules actifs et leurs configurations.\n")
    parts.append("- Liste extra_capabilities individuelles sur l admin.\n")
    parts.append("- Audit roles personnalises via wp_options.wp_user_roles.\n\n")
    parts.append("Quand Novamira MCP est reconnecte, rejouer un mini-audit ciblant ces 5 points.\n\n")

    parts.append("## Etape 2 schoolswp.com terminee.\n")

    return "".join(parts)


def build_report_michaelkihl_fr(r):
    parts = []
    parts.append("# Etape 2 - Inventaire WP michaelkihl.fr\n\n")
    parts.append("> Audit lecture seule via WP REST API. Date : 2026-05-12.\n")
    parts.append("> Auth : Application Password de user `kgd0l7wyuejc` (admin, username randomise = bonne hygiene).\n")
    parts.append("> Aucune valeur secrete dans ce rapport.\n\n")
    parts.append("---\n\n")

    parts.append("## Resume executif\n\n")
    parts.append("Site secondaire, stack tres legere comparee a schoolswp.com :\n\n")
    parts.append("- **16 plugins** actifs (vs 54 sur schoolswp.com).\n")
    parts.append("- **1 seul user au total**, l admin avec un username randomise `kgd0l7wyuejc` (bonne pratique anti-enumeration).\n")
    parts.append("- **2 Application Passwords** actifs (Novamira + Skoatch), tous deux utilises recemment.\n")
    parts.append("- **Security headers partiellement actifs** sur /wp-login.php (4/6), bien meilleur que schoolswp.com (0/6).\n")
    parts.append("- **Timezone bien configure** (Europe/Paris).\n")
    parts.append("- **Stack SureForms / SureMail / SureRank SEO** : ecosystem Brainstorm Force (Spectra) sur ce site, distinct de Rank Math / FluentSMTP / Kadence-only sur schoolswp.com.\n")
    parts.append("- xmlrpc.php = 403 (block xCloud).\n\n")

    d = r["checks"]["discovery"]
    s = r["checks"].get("settings", {})
    parts.append("## 1. Identite du site\n\n")
    parts.append(f"- **Nom** : {d.get('name')!r}\n")
    parts.append(f"- **URL** : {d.get('url')}\n")
    parts.append(f"- **Description** : {s.get('description', '?')!r}\n")
    parts.append(f"- **Langue** : {s.get('language', '?')}\n")
    parts.append(f"- **Timezone** : {s.get('timezone', '?')}\n")
    parts.append(f"- **Admin email** : {s.get('admin_email', '?')}\n")
    parts.append(f"- **Page d accueil** : {s.get('show_on_front')}\n\n")

    parts.append("## 2. Users\n\n")
    u = r["checks"].get("users_privileged", {})
    total = r["checks"].get("users_total", {}).get("total_count", "?")
    parts.append(f"**Total users** : {total}\n\n")
    for usr in u.get("users", []):
        parts.append(f"- id={usr['id']} username=`{usr['username']}` email={usr['email']} roles={', '.join(usr['roles'])}\n")
        parts.append(f"- capabilities = {usr['capabilities_count']} (admin standard sans plugins lourds = ~79 normal pour WP core + Fluent Booking + SecuPress)\n")
        parts.append(f"- inscrit : {usr['registered_date']}\n\n")

    parts.append("Le username `kgd0l7wyuejc` est aleatoire (12 chars alphanumeriques), donc impossible a deviner. Bonne pratique a generaliser.\n\n")

    parts.append("## 3. Application Passwords\n\n")
    ap = r["checks"].get("application_passwords", {})
    if ap.get("users"):
        parts.append("| Nom | Cree | Last used | Last IP | Statut |\n|---|---|---|---|---|\n")
        for entry in ap["users"]:
            for p in entry.get("names", []):
                status = "ACTIF" if p["last_used"] else "JAMAIS UTILISE"
                parts.append(f"| {p['name']} | {p['created'][:10]} | {(p['last_used'] or '-')[:10]} | {p['last_ip'] or '-'} | {status} |\n")
        parts.append("\n")
    parts.append("Les 2 passwords sont utilises recemment (< 48h). Aucun orphelin. Bonne hygiene.\n\n")

    parts.append("## 4. Plugins (16 actifs)\n\n")
    pl = r["checks"].get("plugins", {})
    parts.append("| Nom | Version |\n|---|---|\n")
    for p in pl.get("active", []):
        name = p.get("name")
        if isinstance(name, dict):
            name = name.get("raw") or name.get("rendered") or "?"
        parts.append(f"| {name} | {p.get('version')} |\n")
    parts.append("\n")
    parts.append("### Observations\n\n")
    parts.append("- **Stack legere** : 16 plugins, raisonnable.\n")
    parts.append("- **Ecosystem SureForms / SureMail / SureRank** (Brainstorm Force) au lieu de FluentForms / FluentSMTP / Rank Math : choix delibere ?\n")
    parts.append("- **SureForms 2.8.2** + **SureForms Business 2.8.3** : ecart 1 patch, normal pour free + Pro.\n")
    parts.append("- **Novamira v1.1.2 + Novamira Pro v1.0.0** : meme stack que schoolswp.com, MCP REST proxy.\n")
    parts.append("- **SecuPress Pro v2.6.1** : meme version que schoolswp.com (DCTS JS bug applicable).\n")
    parts.append("- **WPvivid Backup v0.9.126** : pas de WP Umbrella sur ce site. Verifier que xCloud snapshot couvre.\n")
    parts.append("- **ClickWhale Pro** : cloak liens affilies, comme schoolswp.com.\n")
    parts.append("- **FluentBooking + Pro** : seul plugin Fluent ici (booking de rendez-vous).\n")
    parts.append("- **Templates de demarrage Kadence v2.2.14** : reste actif (sur schoolswp.com il est inactif). Si pas utilise activement, desactiver.\n\n")

    parts.append("## 5. Themes\n\n")
    parts.append("| stylesheet | version | status | parent |\n|---|---|---|---|\n")
    for th in r["checks"].get("themes", {}).get("themes", []):
        parts.append(f"| {th['stylesheet']} | {th['version']} | {th['status']} | {th['parent_theme'] or '-'} |\n")
    parts.append("\n**twentytwentyfive v1.4** present en inactif = theme fallback WP. Peut etre supprime si SecuPress detecte une faille future.\n\n")

    parts.append("## 6. REST API\n\n")
    parts.append(f"- **{d.get('namespaces_count')} namespaces, {d.get('routes_count')} routes**.\n")
    parts.append(f"- Stack beaucoup plus legere que schoolswp.com (60 / 1886).\n\n")
    parts.append("Namespaces detectes :\n\n")
    for n in d.get("namespaces", []):
        parts.append(f"- `{n}`\n")
    parts.append("\n")

    parts.append("## 7. Headers HTTP et exposure\n\n")
    exp = r["checks"].get("exposure", {})
    parts.append("| Path | HTTP status | HSTS | X-Frame | X-CT | CSP | Referrer | Permissions |\n|---|---|---|---|---|---|---|---|\n")
    for path, info in exp.items():
        sh = info.get("security_headers", {})
        flags = []
        for h in ["Strict-Transport-Security", "X-Frame-Options", "X-Content-Type-Options", "Content-Security-Policy", "Referrer-Policy", "Permissions-Policy"]:
            flags.append("OK" if sh.get(h) else "MISS")
        parts.append(f"| `{path}` | {info.get('status')} | {flags[0]} | {flags[1]} | {flags[2]} | {flags[3]} | {flags[4]} | {flags[5]} |\n")
    parts.append("\n")
    parts.append("**Observations** :\n\n")
    parts.append("- **xCloud injecte des security headers serveur-level** sur /wp-login.php : X-Frame-Options SAMEORIGIN, X-Content-Type-Options nosniff, CSP frame-ancestors 'self', Referrer-Policy strict-origin-when-cross-origin.\n")
    parts.append("- **HSTS et Permissions-Policy toujours absents**, meme sur xCloud.\n")
    parts.append("- xmlrpc.php = 403 (block actif).\n")
    parts.append("- /wp-admin/ = 302 (redirige vers login).\n\n")

    parts.append("## 8. Findings classes\n\n")
    parts.append("### ELEVE\n\n")
    parts.append("1. **HSTS absent sur xCloud aussi**\n")
    parts.append("   Pas un drame parce que Cloudflare peut l ajouter en amont, mais a vrification.\n\n")
    parts.append("2. **Pas de plugin de monitoring distant**\n")
    parts.append("   schoolswp.com a WP Umbrella, michaelkihl.fr n a rien. Soit ajouter WP Umbrella ici aussi (free tier OK), soit s appuyer entierement sur xCloud snapshots + alerts.\n\n")
    parts.append("3. **Templates Kadence v2.2.14 actif**\n")
    parts.append("   Si tu construis ton design sans utiliser ces templates, desactiver pour reduire la surface.\n\n")

    parts.append("### MOYEN\n\n")
    parts.append("4. **SecuPress 2.6.1 (meme version que schoolswp.com)**\n")
    parts.append("   DCTS JS bug et historique pwd-fatal applicables.\n\n")
    parts.append("5. **WPvivid seul (pas de second backup)**\n")
    parts.append("   Le site est moins critique mais une seule source de backup = risque. xCloud snapshot suffit-il ?\n\n")

    parts.append("### FAIBLE\n\n")
    parts.append("6. **Username admin randomise**\n")
    parts.append("   Bonne pratique. **A appliquer aussi sur schoolswp.com** (actuellement username = 'Michael KIHL' avec espace).\n\n")
    parts.append("7. **twentytwentyfive theme inactif**\n")
    parts.append("   Faible vecteur d attaque. A garder comme fallback (recommandation WP) ou supprimer.\n\n")

    parts.append("---\n\n## Recommandations\n\n")
    parts.append("Site secondaire, peu de findings critiques. Actions principales :\n\n")
    parts.append("1. **Renomer l admin sur schoolswp.com** sur le modele de celui-ci (random 12-char).\n")
    parts.append("2. **Ajouter HSTS** via Cloudflare Transform Rules (couvre les 2 sites).\n")
    parts.append("3. **Verifier que xCloud snapshot suffit comme strategie backup unique** ou ajouter WP Umbrella tier free.\n")
    parts.append("4. **Desactiver Templates Kadence** si pas utilise.\n\n")
    parts.append("## Etape 2 michaelkihl.fr terminee.\n")

    return "".join(parts)


def main():
    school_json = HERE / "schoolswp-audit.json"
    mkfr_json = HERE / "michaelkihl-fr-audit.json"

    with open(school_json, "r", encoding="utf-8") as f:
        school = json.load(f)
    with open(mkfr_json, "r", encoding="utf-8") as f:
        mkfr = json.load(f)

    out_school = HERE / "02-wp-inventory-schoolswp.md"
    out_mkfr = HERE / "02-wp-inventory-michaelkihl-fr.md"

    out_school.write_text(build_report_schoolswp(school), encoding="utf-8")
    out_mkfr.write_text(build_report_michaelkihl_fr(mkfr), encoding="utf-8")

    print(f"WRITTEN: {out_school} ({out_school.stat().st_size} bytes)")
    print(f"WRITTEN: {out_mkfr} ({out_mkfr.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
