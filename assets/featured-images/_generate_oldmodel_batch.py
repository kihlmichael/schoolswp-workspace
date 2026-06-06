"""Generate heros to replace the legacy dark-background featured images (verdict-block)."""

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

I_TABLE = '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="3" y1="15" x2="21" y2="15"></line><line x1="9" y1="3" x2="9" y2="21"></line>'
I_DATABASE = '<ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>'
I_PEN = '<path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>'
I_CURSOR = '<path d="M3 3l7.07 16.97 2.51-7.39 7.39-2.51L3 3z"></path><path d="M13 13l6 6"></path>'
I_CALCHECK = '<rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line><path d="M9 16l2 2 4-4"></path>'
I_LINK = '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>'

V = [
    # Family A -- Ninja Tables review (general best table plugin)
    dict(id=1946756, lang="en", htmllang="en", pt="Ninja Tables review - Hero EN", tf=92, vf=84,
        p1="Ninja Tables", p2="Review", icon=I_TABLE, vh="The essentials",
        lines=["Beautiful", "<em>tables</em>"],
        base="Ninja Tables lets you build responsive, sortable WordPress tables without writing a line of code: the best table plugin, reviewed.",
        vn="No-code", vs="build WordPress tables without code",
        stats=[("Type", "Table plugin"), ("Strength", "Responsive"), ("Plus", "Sortable &amp; filterable"), ("Best for", "Any content")],
        foot="The best table plugin"),
    dict(id=50326, lang="fr", htmllang="fr", pt="Ninja Tables avis - Hero FR", tf=92, vf=80,
        p1="Ninja Tables", p2="Avis", icon=I_TABLE, vh="L'essentiel",
        lines=["De beaux", "<em>tableaux</em>"],
        base="Ninja Tables permet de créer des tableaux WordPress responsives et triables sans écrire une ligne de code : le meilleur plugin de tableaux, testé.",
        vn="Sans code", vs="créer tes tableaux WordPress sans code",
        stats=[("Type", "Plugin de tableaux"), ("Force", "Responsive"), ("Atout", "Triable &amp; filtrable"), ("Idéal pour", "Tout contenu")],
        foot="Le meilleur plugin de tableaux"),
    # Family B -- Ninja Tables DataTables (large datasets / performance)
    dict(id=2865114, lang="en", htmllang="en", pt="Ninja Tables DataTables - Hero EN", tf=84, vf=76,
        p1="Ninja Tables", p2="DataTables", icon=I_DATABASE, vh="The essentials",
        lines=["Big tables,", "<em>handled</em>"],
        base="Ninja Tables DataTables handles thousands of rows with search, sorting and pagination: manage your large datasets without slowing down.",
        vn="Big tables", vs="manage large datasets without lag",
        stats=[("Type", "DataTables"), ("Strength", "Thousands of rows"), ("Plus", "Search &amp; pagination"), ("Best for", "Large datasets")],
        foot="Huge tables, no slowdown"),
    dict(id=2592793, lang="fr", htmllang="fr", pt="Ninja Tables DataTables - Hero FR", tf=80, vf=64,
        p1="Ninja Tables", p2="DataTables", icon=I_DATABASE, vh="L'essentiel",
        lines=["Tes données", "<em>volumineuses</em>"],
        base="Ninja Tables DataTables gère des milliers de lignes avec recherche, tri et pagination : affiche tes données volumineuses sans ralentir.",
        vn="Grandes tables", vs="gérer des milliers de lignes sans ralentir",
        stats=[("Type", "DataTables"), ("Force", "Milliers de lignes"), ("Atout", "Recherche &amp; pagination"), ("Idéal pour", "Gros volumes")],
        foot="De grosses tables, sans ralentir"),
    dict(id=2888497, lang="de", htmllang="de", pt="Ninja Tables DataTables - Hero DE", tf=88, vf=60,
        p1="Ninja Tables", p2="DataTables", icon=I_DATABASE, vh="Das Wichtigste",
        lines=["Große", "<em>Datensätze</em>"],
        base="Ninja Tables DataTables verwaltet Tausende Zeilen mit Suche, Sortierung und Pagination: zeige große Datensätze ohne Verzögerung.",
        vn="Große Tabellen", vs="Tausende Zeilen ohne Verzögerung",
        stats=[("Typ", "DataTables"), ("Stärke", "Tausende Zeilen"), ("Plus", "Suche &amp; Pagination"), ("Ideal für", "Große Datenmengen")],
        foot="Große Tabellen, kein Ruckeln"),
    # Family C -- Create a blog post (DE only; FR/EN already branded)
    dict(id=1136071, lang="de", htmllang="de", pt="Blogbeitrag erstellen - Hero DE", tf=80, vf=76,
        p1="WordPress", p2="Tutorial", icon=I_PEN, vh="In diesem Guide",
        lines=["Blogbeitrag", "in <em>WordPress</em>"],
        base="Mehr als nur ein Textfeld ausfüllen: der komplette Workflow, um einen Beitrag zu schreiben, zu strukturieren, zu veröffentlichen und zu optimieren.",
        vn="6 Schritte", vs="vom leeren Entwurf zum optimierten Beitrag",
        stats=[("Schreiben", "Gutenberg-Blöcke"), ("Struktur", "Überschriften &amp; Listen"), ("Medien", "Bilder &amp; Alt"), ("Publizieren", "Live o. geplant")],
        foot="Der komplette Veröffentlichungs-Workflow"),
    # Family D -- Elementor (match FR 895: verdict "Le builder", cursor icon)
    dict(id=1944479, lang="en", htmllang="en", pt="Elementor - Hero EN", tf=84, vf=72,
        p1="Elementor", p2="Guide", icon=I_CURSOR, vh="The essentials",
        lines=["Elementor,", "the <em>builder</em>"],
        base="The most popular WordPress page builder: everything you need to know to build your pages by drag and drop.",
        vn="The builder", vs="the most popular WordPress page builder",
        stats=[("Type", "Page builder"), ("Strength", "Drag &amp; drop"), ("Community", "The largest"), ("Best for", "Any site")],
        foot="Build your pages, no code needed"),
    dict(id=1944485, lang="de", htmllang="de", pt="Elementor - Hero DE", tf=84, vf=72,
        p1="Elementor", p2="Guide", icon=I_CURSOR, vh="Das Wichtigste",
        lines=["Elementor,", "der <em>Builder</em>"],
        base="Der beliebteste Page-Builder für WordPress: alles, was du wissen musst, um deine Seiten per Drag and Drop zu bauen.",
        vn="Der Builder", vs="der beliebteste WordPress-Page-Builder",
        stats=[("Typ", "Page Builder"), ("Stärke", "Drag &amp; Drop"), ("Community", "Die größte"), ("Ideal für", "Jede Site")],
        foot="Seiten bauen, ganz ohne Code"),
    # Family E -- Amelia (DE only) -- booking
    dict(id=1351611, lang="de", htmllang="de", pt="Amelia - Hero DE", tf=84, vf=80,
        p1="Amelia", p2="Meinung", icon=I_CALCHECK, vh="Das Wichtigste",
        lines=["Amelia,", "die <em>Termine</em>"],
        base="Amelia ist das Buchungs-Plugin für WordPress: Termine, Events und Online-Zahlungen in einer modernen Oberfläche.",
        vn="Buchungen", vs="Termine und Events in WordPress",
        stats=[("Typ", "Buchungen"), ("Stärke", "Termine &amp; Events"), ("Plus", "Online-Zahlungen"), ("Ideal für", "Dienstleister")],
        foot="Termine, automatisch verwaltet"),
    # Family F -- Linkuma (match FR 54381: score 7,5/10, netlinking)
    dict(id=56041, lang="en", htmllang="en", pt="Linkuma - Hero EN", tf=84, vf=80,
        p1="Linkuma", p2="Review", icon=I_LINK, vh="My verdict",
        lines=["Linkuma,", "the <em>verdict</em>"],
        base="French netlinking platform with dofollow backlinks, full delegation and responsive support: my honest take for WordPress freelancers and SEO agencies.",
        vn="7,5/10", vs="French netlinking, tested for months",
        stats=[("Type", "Netlinking"), ("Origin", "French"), ("Network", "45,000 sites"), ("Best for", "Freelancers &amp; agencies")],
        foot="Backlinks, fully delegated"),
    dict(id=56040, lang="de", htmllang="de", pt="Linkuma - Hero DE", tf=84, vf=80,
        p1="Linkuma", p2="Meinung", icon=I_LINK, vh="Mein Urteil",
        lines=["Linkuma,", "das <em>Urteil</em>"],
        base="Französische Netlinking-Plattform mit Dofollow-Backlinks, voller Delegation und reaktivem Support: mein ehrliches Fazit für WordPress-Freelancer und SEO-Agenturen.",
        vn="7,5/10", vs="französisches Netlinking, monatelang getestet",
        stats=[("Typ", "Netlinking"), ("Herkunft", "Französisch"), ("Netzwerk", "45.000 Sites"), ("Ideal für", "Freelancer &amp; Agenturen")],
        foot="Backlinks, komplett delegiert"),
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
