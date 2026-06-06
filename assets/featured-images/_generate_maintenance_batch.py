"""Generate heros for the WP maintenance/management batch (verdict-block)."""

import os

HEAD = """<!doctype html>
<html lang="@@HTMLLANG@@">
  <head>
    <meta charset="UTF-8" />
    <title>@@PAGETITLE@@</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap"
      rel="stylesheet"
    />
    <style>
      :root {
        --bg: #f4f5f7;
        --card-bg: #ffffff;
        --green: #00d400;
        --green-soft: #d4f7d4;
        --black: #0f1419;
        --grey-text: #5a6470;
        --line: #d8dce3;
      }
      * { box-sizing: border-box; margin: 0; padding: 0; }
      html, body { font-family: "Inter", -apple-system, sans-serif; background: var(--bg); }
      .slide {
        width: 1920px; height: 1080px; background: var(--bg);
        display: grid; grid-template-columns: 1080px 1fr;
        align-items: center; padding: 0 110px; gap: 80px;
        position: relative; overflow: hidden;
      }
      .text-block { display: flex; flex-direction: column; gap: 38px; }
      .pill {
        display: inline-flex; align-items: center; gap: 14px; align-self: flex-start;
        padding: 12px 22px 12px 18px; border-radius: 999px; background: #ffffff;
        border: 1.5px solid var(--line); font-size: 18px; font-weight: 700;
        letter-spacing: 2px; text-transform: uppercase; color: var(--black);
      }
      .pill .dot { width: 10px; height: 10px; border-radius: 50%; background: var(--green); box-shadow: 0 0 0 4px rgba(0, 212, 0, 0.18); }
      .pill .sep { color: var(--line); font-weight: 400; }
      .title { font-family: "Inter", sans-serif; font-weight: 900; font-size: @@TITLEFONT@@px; line-height: 0.98; letter-spacing: -4px; color: var(--black); }
      .title span { display: block; }
      .title em { font-style: normal; color: var(--green); }
      .baseline { font-size: 30px; font-weight: 500; color: var(--grey-text); line-height: 1.4; max-width: 920px; }
      .signature { font-size: 20px; font-weight: 600; color: var(--black); letter-spacing: 0.3px; margin-top: 18px; }
      .signature .sep { color: var(--line); margin: 0 14px; }
      .signature .schools { color: var(--black); }
      .signature .wp { color: var(--green); }
      .visual {
        width: 620px; height: 720px; background: var(--card-bg); border-radius: 32px;
        box-shadow: 0 32px 70px -20px rgba(15, 20, 25, 0.18), 0 4px 12px -4px rgba(15, 20, 25, 0.06);
        position: relative; overflow: hidden; display: flex; flex-direction: column;
      }
      .visual::before {
        content: ""; position: absolute; top: 0; left: 0; right: 0; height: 8px;
        background: linear-gradient(90deg, var(--green) 0%, var(--green) 35%, transparent 35%, transparent 100%);
      }
      .v-header { display: flex; align-items: center; gap: 14px; font-size: 20px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; color: var(--grey-text); }
      .v-header .icon-circle { width: 36px; height: 36px; border-radius: 50%; background: var(--green-soft); display: inline-flex; align-items: center; justify-content: center; color: var(--green); }
      .v-header .icon-circle svg { width: 20px; height: 20px; display: block; }
      .visual-footer { display: flex; align-items: center; justify-content: center; gap: 10px; font-size: 17px; font-weight: 600; color: var(--grey-text); margin-top: 2px; text-align: center; }
      .visual-footer .dot { width: 6px; height: 6px; border-radius: 50%; background: var(--green); flex-shrink: 0; }
      .visual-inner { padding: 64px 56px 52px 56px; display: flex; flex-direction: column; gap: 30px; height: 100%; }
      .verdict-block { display: flex; flex-direction: column; align-items: center; gap: 6px; padding: 6px 0 2px; text-align: center; }
      .verdict-num { font-weight: 900; font-size: @@VERDICTFONT@@px; line-height: 1; letter-spacing: -3px; color: var(--green); white-space: nowrap; }
      .verdict-sub { font-size: 22px; font-weight: 600; color: var(--grey-text); line-height: 1.3; max-width: 470px; }
      .stats { display: flex; flex-direction: column; gap: 10px; width: 100%; flex: 1; justify-content: center; }
      .stat { display: flex; justify-content: space-between; align-items: baseline; padding: 13px 4px; border-bottom: 1px dashed var(--line); font-size: 21px; }
      .stat:last-child { border-bottom: none; }
      .stat-key { color: var(--grey-text); font-weight: 500; }
      .stat-val { color: var(--black); font-weight: 800; }
    </style>
  </head>
  <body>
    <div class="slide">
      <div class="text-block">
        <div class="pill">
          <span class="dot"></span>
          <span>@@PILL1@@</span>
          <span class="sep">|</span>
          <span>@@PILL2@@</span>
        </div>
        <div class="title">@@TITLELINES@@</div>
        <div class="baseline">@@BASELINE@@</div>
        <div class="signature">
          Micha&euml;l KIHL <span class="sep">|</span>
          <span class="schools">schools</span><span class="wp">WP</span>.com
        </div>
      </div>
      <div class="visual">
        <div class="visual-inner">
          <div class="v-header">
            <span class="icon-circle">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">@@ICON@@</svg>
            </span>
            <span>@@VHEADER@@</span>
          </div>
          <div class="verdict-block">
            <div class="verdict-num">@@VN@@</div>
            <div class="verdict-sub">@@VS@@</div>
          </div>
          <div class="stats">
@@STATS@@
          </div>
          <div class="visual-footer">
            <span class="dot"></span>
            <span>@@FOOTER@@</span>
          </div>
        </div>
      </div>
    </div>
  </body>
</html>
"""

I_CAL = '<rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line>'
I_ACTIVITY = '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>'
I_UMBRELLA = '<path d="M23 12a11.05 11.05 0 0 0-22 0zm-5 7a3 3 0 0 1-6 0v-7"></path>'
I_DB = '<ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>'
I_INBOX = '<polyline points="22 12 16 12 14 15 10 15 8 12 2 12"></polyline><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"></path>'

V = [
    # Booknetic FR (draft) -- booking
    dict(id=2969996, lang="fr", htmllang="fr", pt="Booknetic - Hero FR", tf=76, vf=76,
        p1="Booknetic", p2="Avis", icon=I_CAL, vh="L'essentiel",
        lines=["Booknetic,", "la <em>réservation</em>"],
        base="Le plugin de prise de rendez-vous pour WordPress : agenda, paiements en ligne et notifications, dans une interface moderne.",
        vn="Réservation", vs="la prise de rendez-vous sur WordPress",
        stats=[("Type", "Réservation"), ("Force", "Agenda &amp; paiements"), ("Atout", "Interface moderne"), ("Idéal pour", "Rendez-vous clients")],
        foot="Tes rendez-vous, en pilote automatique"),
    # WPMissionControl FR / EN / DE -- monitoring (concept-led title, long name in pill)
    dict(id=1380389, lang="fr", htmllang="fr", pt="WPMissionControl - Hero FR", tf=84, vf=80,
        p1="WPMissionControl", p2="Avis", icon=I_ACTIVITY, vh="L'essentiel",
        lines=["Le site sous", "<em>surveillance</em>"],
        base="Le plugin qui surveille ton site WordPress en continu : disponibilité, performances et alertes en temps réel.",
        vn="Monitoring", vs="surveiller ton site WordPress 24/7",
        stats=[("Type", "Monitoring"), ("Force", "Uptime &amp; perfs"), ("Atout", "Alertes temps réel"), ("Idéal pour", "Sites critiques")],
        foot="Sois prévenu avant tes visiteurs"),
    dict(id=1638614, lang="en", htmllang="en", pt="WPMissionControl - Hero EN", tf=92, vf=80,
        p1="WPMissionControl", p2="Review", icon=I_ACTIVITY, vh="The essentials",
        lines=["Your site", "under <em>watch</em>"],
        base="The plugin that monitors your WordPress site around the clock: uptime, performance and real-time alerts.",
        vn="Monitoring", vs="monitor your WordPress site 24/7",
        stats=[("Type", "Monitoring"), ("Strength", "Uptime &amp; perf"), ("Plus", "Real-time alerts"), ("Best for", "Critical sites")],
        foot="Know before your visitors do"),
    dict(id=1638632, lang="de", htmllang="de", pt="WPMissionControl - Hero DE", tf=88, vf=80,
        p1="WPMissionControl", p2="Test", icon=I_ACTIVITY, vh="Das Wichtigste",
        lines=["Site unter", "<em>Aufsicht</em>"],
        base="Das Plugin, das deine WordPress-Site rund um die Uhr überwacht: Verfügbarkeit, Performance und Echtzeit-Alarme.",
        vn="Monitoring", vs="deine WordPress-Site rund um die Uhr",
        stats=[("Typ", "Monitoring"), ("Stärke", "Uptime &amp; Performance"), ("Plus", "Echtzeit-Alarme"), ("Ideal für", "Kritische Sites")],
        foot="Wissen, bevor die Besucher es merken"),
    # WP Umbrella FR / EN / DE -- maintenance for agencies
    dict(id=57383, lang="fr", htmllang="fr", pt="WP Umbrella - Hero FR", tf=80, vf=72,
        p1="WP Umbrella", p2="Avis", icon=I_UMBRELLA, vh="L'essentiel",
        lines=["WP Umbrella,", "la <em>maintenance</em>"],
        base="L'outil de maintenance WordPress pensé pour les agences : sauvegardes, monitoring, mises à jour et rapports clients.",
        vn="La maintenance", vs="la maintenance WordPress des pros",
        stats=[("Type", "Maintenance"), ("Force", "Sauvegardes &amp; updates"), ("Atout", "Rapports clients"), ("Idéal pour", "Agences &amp; freelances")],
        foot="Tes sites clients sous contrôle"),
    dict(id=57412, lang="en", htmllang="en", pt="WP Umbrella - Hero EN", tf=80, vf=80,
        p1="WP Umbrella", p2="Review", icon=I_UMBRELLA, vh="The essentials",
        lines=["WP Umbrella,", "<em>maintenance</em>"],
        base="The WordPress maintenance tool built for agencies: backups, monitoring, updates and client reports.",
        vn="Maintenance", vs="WordPress maintenance for pros",
        stats=[("Type", "Maintenance"), ("Strength", "Backups &amp; updates"), ("Plus", "Client reports"), ("Best for", "Agencies &amp; freelancers")],
        foot="Your client sites under control"),
    dict(id=57413, lang="de", htmllang="de", pt="WP Umbrella - Hero DE", tf=80, vf=88,
        p1="WP Umbrella", p2="Meinung", icon=I_UMBRELLA, vh="Das Wichtigste",
        lines=["WP Umbrella,", "die <em>Wartung</em>"],
        base="Das WordPress-Wartungstool für Agenturen: Backups, Monitoring, Updates und Kundenreports.",
        vn="Wartung", vs="WordPress-Wartung für Profis",
        stats=[("Typ", "Wartung"), ("Stärke", "Backups &amp; Updates"), ("Plus", "Kundenreports"), ("Ideal für", "Agenturen &amp; Freelancer")],
        foot="Deine Kundensites im Griff"),
    # Clean WordPress database FR / EN / DE -- guide
    dict(id=53653, lang="fr", htmllang="fr", pt="Nettoyer base de donnees - Hero FR", tf=80, vf=84,
        p1="Base de données", p2="Guide", icon=I_DB, vh="L'essentiel",
        lines=["Base de données,", "au <em>propre</em>"],
        base="Comment alléger et nettoyer la base de données de ton site WordPress : révisions, transients, tables orphelines et plugins.",
        vn="Nettoyer", vs="alléger ta base de données WordPress",
        stats=[("Type", "Guide"), ("Objectif", "Base allégée"), ("Niveau", "Débutant"), ("Idéal pour", "Accélérer ton site")],
        foot="Une base propre, un site plus rapide"),
    dict(id=57351, lang="en", htmllang="en", pt="Clean WordPress database - Hero EN", tf=80, vf=84,
        p1="WordPress database", p2="Guide", icon=I_DB, vh="The essentials",
        lines=["Your database,", "<em>cleaned</em> up"],
        base="How to lighten and clean your WordPress database: revisions, transients, orphan tables and plugins.",
        vn="Clean it", vs="lighten your WordPress database",
        stats=[("Type", "Guide"), ("Goal", "Lighter database"), ("Level", "Beginner"), ("Best for", "Speeding up your site")],
        foot="A clean database, a faster site"),
    dict(id=57295, lang="de", htmllang="de", pt="WordPress-Datenbank reinigen - Hero DE", tf=76, vf=84,
        p1="WordPress-Datenbank", p2="Guide", icon=I_DB, vh="Das Wichtigste",
        lines=["Deine Datenbank,", "<em>aufgeräumt</em>"],
        base="So machst du deine WordPress-Datenbank schlank und sauber: Revisionen, Transients, verwaiste Tabellen und Plugins.",
        vn="Aufräumen", vs="deine WordPress-Datenbank entschlacken",
        stats=[("Typ", "Guide"), ("Ziel", "Schlanke Datenbank"), ("Niveau", "Einsteiger"), ("Ideal für", "Site beschleunigen")],
        foot="Saubere Datenbank, schnellere Site"),
    # Fluent Support FR / EN / DE -- helpdesk
    dict(id=50687, lang="fr", htmllang="fr", pt="Fluent Support - Hero FR", tf=80, vf=76,
        p1="Fluent Support", p2="Avis", icon=I_INBOX, vh="L'essentiel",
        lines=["Fluent Support,", "tes <em>tickets</em>"],
        base="Le helpdesk auto-hébergé pour WordPress : gère tous tes tickets de support client directement depuis ton tableau de bord.",
        vn="Tes tickets", vs="le support client intégré à WordPress",
        stats=[("Type", "Helpdesk"), ("Force", "Tout dans WP"), ("Atout", "Tickets illimités"), ("Idéal pour", "Support client")],
        foot="Ton SAV, sans quitter WordPress"),
    dict(id=54889, lang="en", htmllang="en", pt="Fluent Support - Hero EN", tf=80, vf=92,
        p1="Fluent Support", p2="Review", icon=I_INBOX, vh="The essentials",
        lines=["Fluent Support,", "your <em>tickets</em>"],
        base="The self-hosted helpdesk for WordPress: manage all your customer support tickets right from your dashboard.",
        vn="Tickets", vs="built-in customer support for WordPress",
        stats=[("Type", "Helpdesk"), ("Strength", "All inside WP"), ("Plus", "Unlimited tickets"), ("Best for", "Customer support")],
        foot="Your support desk, inside WordPress"),
    dict(id=54888, lang="de", htmllang="de", pt="Fluent Support - Hero DE", tf=80, vf=92,
        p1="Fluent Support", p2="Meinung", icon=I_INBOX, vh="Das Wichtigste",
        lines=["Fluent Support,", "deine <em>Tickets</em>"],
        base="Das selbstgehostete Helpdesk für WordPress: verwalte alle deine Support-Tickets direkt im Dashboard.",
        vn="Tickets", vs="Kundensupport direkt in WordPress",
        stats=[("Typ", "Helpdesk"), ("Stärke", "Alles in WP"), ("Plus", "Unbegrenzte Tickets"), ("Ideal für", "Kundensupport")],
        foot="Dein Support, direkt in WordPress"),
]


def render(h):
    html = HEAD
    html = html.replace("@@HTMLLANG@@", h["htmllang"])
    html = html.replace("@@PAGETITLE@@", h["pt"])
    html = html.replace("@@TITLEFONT@@", str(h["tf"]))
    html = html.replace("@@VERDICTFONT@@", str(h["vf"]))
    html = html.replace("@@PILL1@@", h["p1"])
    html = html.replace("@@PILL2@@", h["p2"])
    html = html.replace("@@TITLELINES@@", "".join(f"<span>{x}</span>" for x in h["lines"]))
    html = html.replace("@@BASELINE@@", h["base"])
    html = html.replace("@@ICON@@", h["icon"])
    html = html.replace("@@VHEADER@@", h["vh"])
    html = html.replace("@@VN@@", h["vn"])
    html = html.replace("@@VS@@", h["vs"])
    html = html.replace("@@FOOTER@@", h["foot"])
    rows = "\n".join(
        f'            <div class="stat"><span class="stat-key">{k}</span><span class="stat-val">{v}</span></div>'
        for k, v in h["stats"]
    )
    html = html.replace("@@STATS@@", rows)
    return html


for h in V:
    d = f"post-{h['id']}"
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, f"slide-00-hero-{h['lang']}.html"), "w", encoding="utf-8") as f:
        f.write(render(h))
    print(f"  post-{h['id']}/slide-00-hero-{h['lang']}.html")
print("Generated", len(V), "hero HTML files")
