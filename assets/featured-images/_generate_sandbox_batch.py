"""Generate heros for the WP sandbox/site-creation batch (verdict-block)."""

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

I_BROWSER = '<rect x="2" y="4" width="20" height="16" rx="2" ry="2"></rect><path d="M2 9h20"></path><circle cx="5.5" cy="6.5" r="0.6"></circle><circle cx="8" cy="6.5" r="0.6"></circle>'
I_STOPWATCH = '<circle cx="12" cy="13" r="8"></circle><path d="M12 9v4l2.5 2"></path><path d="M9 2h6"></path><path d="M12 2v2"></path>'
I_MONITOR = '<rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line>'
I_CURSOR = '<path d="M3 3l7.07 16.97 2.51-7.39 7.39-2.51L3 3z"></path><path d="M13 13l6 6"></path>'
I_SPARK = '<path d="M12 2l1.8 5.2L19 9l-5.2 1.8L12 16l-1.8-5.2L7 9l5.2-1.8L12 2z"></path><path d="M19 15l.6 1.8L21.5 17.4l-1.9.7L19 20l-.7-1.9L16.5 18.1l1.8-.7L19 15z"></path>'

V = [
    # WordPress Playground FR / EN / DE -- WP in the browser, no server
    dict(id=56148, lang="fr", htmllang="fr", pt="WordPress Playground - Hero FR", tf=72, vf=68,
        p1="WP Playground", p2="Guide", icon=I_BROWSER, vh="L'essentiel",
        lines=["WordPress dans", "ton <em>navigateur</em>"],
        base="Lance une instance WordPress complète directement dans ton navigateur, sans serveur ni installation, pour tester, apprendre et développer.",
        vn="Navigateur", vs="WordPress sans serveur ni installation",
        stats=[("Type", "Bac à sable"), ("Force", "Zéro installation"), ("Atout", "Instantané"), ("Idéal pour", "Tester &amp; apprendre")],
        foot="Teste WordPress en un instant"),
    dict(id=58229, lang="en", htmllang="en", pt="WordPress Playground - Hero EN", tf=80, vf=68,
        p1="WP Playground", p2="Guide", icon=I_BROWSER, vh="The essentials",
        lines=["WordPress in", "your <em>browser</em>"],
        base="Spin up a full WordPress instance right in your browser, with no server and no install, to test, learn and develop.",
        vn="In-browser", vs="WordPress with no server, no install",
        stats=[("Type", "Sandbox"), ("Strength", "Zero install"), ("Plus", "Instant"), ("Best for", "Testing &amp; learning")],
        foot="Try WordPress in an instant"),
    dict(id=56793, lang="de", htmllang="de", pt="WordPress Playground - Hero DE", tf=88, vf=76,
        p1="WP Playground", p2="Guide", icon=I_BROWSER, vh="Das Wichtigste",
        lines=["WordPress im", "<em>Browser</em>"],
        base="Starte eine komplette WordPress-Instanz direkt im Browser, ohne Server und ohne Installation, zum Testen, Lernen und Entwickeln.",
        vn="Im Browser", vs="WordPress ohne Server, ohne Installation",
        stats=[("Typ", "Sandkasten"), ("Stärke", "Keine Installation"), ("Plus", "Sofort startklar"), ("Ideal für", "Testen &amp; Lernen")],
        foot="WordPress sofort ausprobieren"),
    # TasteWP FR / EN / DE -- instant temporary test sites
    dict(id=54820, lang="fr", htmllang="fr", pt="TasteWP - Hero FR", tf=92, vf=68,
        p1="TasteWP", p2="Avis", icon=I_STOPWATCH, vh="L'essentiel",
        lines=["Un site WP", "en <em>test</em>"],
        base="Crée un site WordPress temporaire et gratuit en quelques secondes, pour tester un plugin, un thème ou une idée sans rien installer.",
        vn="Test minute", vs="un site WordPress temporaire en secondes",
        stats=[("Type", "Site temporaire"), ("Force", "Prêt en secondes"), ("Atout", "Gratuit"), ("Idéal pour", "Tester un plugin")],
        foot="Teste sans rien installer"),
    dict(id=55955, lang="en", htmllang="en", pt="TasteWP - Hero EN", tf=92, vf=76,
        p1="TasteWP", p2="Review", icon=I_STOPWATCH, vh="The essentials",
        lines=["A WP site", "to <em>test</em>"],
        base="Create a free, temporary WordPress site in seconds to try out a plugin, a theme or an idea without installing anything.",
        vn="Quick test", vs="a temporary WordPress site in seconds",
        stats=[("Type", "Temporary site"), ("Strength", "Ready in seconds"), ("Plus", "Free"), ("Best for", "Testing a plugin")],
        foot="Test without installing a thing"),
    dict(id=55956, lang="de", htmllang="de", pt="TasteWP - Hero DE", tf=84, vf=72,
        p1="TasteWP", p2="Meinung", icon=I_STOPWATCH, vh="Das Wichtigste",
        lines=["Eine WP-Site", "zum <em>Testen</em>"],
        base="Erstelle in Sekunden eine kostenlose, temporäre WordPress-Site, um ein Plugin, ein Theme oder eine Idee ohne Installation zu testen.",
        vn="Schnelltest", vs="eine temporäre WordPress-Site in Sekunden",
        stats=[("Typ", "Temporäre Site"), ("Stärke", "In Sekunden bereit"), ("Plus", "Kostenlos"), ("Ideal für", "Plugin testen")],
        foot="Testen ohne Installation"),
    # Local WP FR / EN / DE -- local dev environment
    dict(id=54821, lang="fr", htmllang="fr", pt="Local WP - Hero FR", tf=92, vf=84,
        p1="Local WP", p2="Avis", icon=I_MONITOR, vh="L'essentiel",
        lines=["WordPress", "en <em>local</em>"],
        base="L'environnement de développement WordPress sur ta machine : monte un site en local pour développer et tester avant la mise en ligne.",
        vn="En local", vs="développer WordPress sur ta machine",
        stats=[("Type", "Dev local"), ("Force", "Sur ta machine"), ("Comparé à", "XAMPP"), ("Idéal pour", "Développeurs")],
        foot="Développe avant de publier"),
    dict(id=58239, lang="en", htmllang="en", pt="Local WP - Hero EN", tf=88, vf=80,
        p1="Local WP", p2="Review", icon=I_MONITOR, vh="The essentials",
        lines=["WordPress", "run <em>locally</em>"],
        base="The WordPress development environment on your machine: build a site locally to develop and test before going live.",
        vn="Local dev", vs="develop WordPress on your own machine",
        stats=[("Type", "Local dev"), ("Strength", "On your machine"), ("Vs", "XAMPP"), ("Best for", "Developers")],
        foot="Develop before you publish"),
    dict(id=58235, lang="de", htmllang="de", pt="Local WP - Hero DE", tf=88, vf=96,
        p1="Local WP", p2="Meinung", icon=I_MONITOR, vh="Das Wichtigste",
        lines=["WordPress", "ganz <em>lokal</em>"],
        base="Die WordPress-Entwicklungsumgebung auf deinem Rechner: baue eine Site lokal, um vor dem Livegang zu entwickeln und zu testen.",
        vn="Lokal", vs="WordPress lokal auf deinem Rechner",
        stats=[("Typ", "Lokale Dev"), ("Stärke", "Auf deinem Rechner"), ("Vs", "XAMPP"), ("Ideal für", "Entwickler")],
        foot="Entwickeln vor dem Livegang"),
    # InstaWP FR / EN -- instant cloud sandbox, one click
    dict(id=53100, lang="fr", htmllang="fr", pt="InstaWP - Hero FR", tf=88, vf=76,
        p1="InstaWP", p2="Avis", icon=I_CURSOR, vh="L'essentiel",
        lines=["Un site WP", "en un <em>clic</em>"],
        base="Crée un site WordPress sandbox dans le cloud en un clic : idéal pour tester, prototyper, partager et migrer en production.",
        vn="En un clic", vs="un site WordPress sandbox dans le cloud",
        stats=[("Type", "Sandbox cloud"), ("Force", "Un seul clic"), ("Atout", "Partage &amp; migration"), ("Idéal pour", "Prototyper")],
        foot="Du sandbox à la production"),
    dict(id=1295032, lang="en", htmllang="en", pt="InstaWP - Hero EN", tf=84, vf=80,
        p1="InstaWP", p2="Review", icon=I_CURSOR, vh="The essentials",
        lines=["A WP site", "in one <em>click</em>"],
        base="Spin up a cloud WordPress sandbox in one click: perfect to test, prototype, share and migrate to production.",
        vn="One click", vs="a cloud WordPress sandbox, instantly",
        stats=[("Type", "Cloud sandbox"), ("Strength", "A single click"), ("Plus", "Share &amp; migrate"), ("Best for", "Prototyping")],
        foot="From sandbox to production"),
    # ZipWP FR / EN / DE -- AI-built WordPress site
    dict(id=52615, lang="fr", htmllang="fr", pt="ZipWP - Hero FR", tf=80, vf=64,
        p1="ZipWP", p2="Avis", icon=I_SPARK, vh="L'essentiel",
        lines=["Ton site WP,", "créé par <em>l'IA</em>"],
        base="L'IA génère un site WordPress complet en quelques minutes : pages, contenu et images, prêts à personnaliser et publier.",
        vn="Créé par l'IA", vs="un site WordPress complet généré par IA",
        stats=[("Type", "Création IA"), ("Force", "Site en minutes"), ("Atout", "Pages &amp; contenu inclus"), ("Idéal pour", "Démarrer vite")],
        foot="De l'idée au site, en IA"),
    dict(id=57053, lang="en", htmllang="en", pt="ZipWP - Hero EN", tf=80, vf=84,
        p1="ZipWP", p2="Review", icon=I_SPARK, vh="The essentials",
        lines=["Your WP site,", "built by <em>AI</em>"],
        base="AI generates a full WordPress site in minutes: pages, content and images, ready to customize and publish.",
        vn="AI-built", vs="a full WordPress site, AI-generated",
        stats=[("Type", "AI builder"), ("Strength", "A site in minutes"), ("Plus", "Pages &amp; content included"), ("Best for", "Starting fast")],
        foot="From idea to site, with AI"),
    dict(id=57052, lang="de", htmllang="de", pt="ZipWP - Hero DE", tf=84, vf=92,
        p1="ZipWP", p2="Meinung", icon=I_SPARK, vh="Das Wichtigste",
        lines=["Deine WP-Site,", "per <em>KI</em>"],
        base="Die KI erstellt in Minuten eine komplette WordPress-Site: Seiten, Inhalte und Bilder, bereit zum Anpassen und Veröffentlichen.",
        vn="Per KI", vs="eine komplette WordPress-Site per KI",
        stats=[("Typ", "KI-Erstellung"), ("Stärke", "Site in Minuten"), ("Plus", "Seiten &amp; Inhalte inklusive"), ("Ideal für", "Schnell starten")],
        foot="Von der Idee zur Site, per KI"),
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
