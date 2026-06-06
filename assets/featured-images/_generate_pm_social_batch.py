"""Generate heros for the PM/social/tracking batch (verdict-block)."""

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

I_KANBAN = '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line><line x1="15" y1="3" x2="15" y2="21"></line>'
I_STAR = '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>'
I_REPEAT = '<polyline points="17 1 21 5 17 9"></polyline><path d="M3 11V9a4 4 0 0 1 4-4h14"></path><polyline points="7 23 3 19 7 15"></polyline><path d="M21 13v2a4 4 0 0 1-4 4H3"></path>'
I_TARGET = '<circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle>'

V = [
    # FluentBoards FR / EN / DE -- project management (Fluent suite, singular voice in footer)
    dict(id=53571, lang="fr", htmllang="fr", pt="FluentBoards - Hero FR", tf=84, vf=80,
        p1="FluentBoards", p2="Avis", icon=I_KANBAN, vh="L'essentiel",
        lines=["FluentBoards,", "tes <em>projets</em>"],
        base="Le plugin de gestion de projet pour WordPress : tableaux kanban, tâches, échéances et collaboration, sans quitter ton tableau de bord.",
        vn="Le kanban", vs="la gestion de projet intégrée à WordPress",
        stats=[("Type", "Gestion de projet"), ("Force", "Kanban &amp; tâches"), ("Atout", "Tout dans WP"), ("Idéal pour", "Équipes &amp; freelances")],
        foot="Mes projets, dans WordPress"),
    dict(id=53804, lang="en", htmllang="en", pt="FluentBoards - Hero EN", tf=84, vf=92,
        p1="FluentBoards", p2="Review", icon=I_KANBAN, vh="The essentials",
        lines=["FluentBoards,", "your <em>projects</em>"],
        base="The project management plugin for WordPress: kanban boards, tasks, deadlines and collaboration, without leaving your dashboard.",
        vn="Kanban", vs="project management inside WordPress",
        stats=[("Type", "Project mgmt"), ("Strength", "Kanban &amp; tasks"), ("Plus", "All inside WP"), ("Best for", "Teams &amp; freelancers")],
        foot="My projects, inside WordPress"),
    dict(id=53803, lang="de", htmllang="de", pt="FluentBoards - Hero DE", tf=80, vf=92,
        p1="FluentBoards", p2="Meinung", icon=I_KANBAN, vh="Das Wichtigste",
        lines=["FluentBoards,", "deine <em>Projekte</em>"],
        base="Das Projektmanagement-Plugin für WordPress: Kanban-Boards, Aufgaben, Fristen und Zusammenarbeit, ohne dein Dashboard zu verlassen.",
        vn="Kanban", vs="Projektmanagement direkt in WordPress",
        stats=[("Typ", "Projektmanagement"), ("Stärke", "Kanban &amp; Aufgaben"), ("Plus", "Alles in WP"), ("Ideal für", "Teams &amp; Freelancer")],
        foot="Meine Projekte, in WordPress"),
    # WP Social Ninja FR / EN -- social proof (reviews, feeds, chat)
    dict(id=48489, lang="fr", htmllang="fr", pt="WP Social Ninja - Hero FR", tf=72, vf=60,
        p1="WP Social Ninja", p2="Avis", icon=I_STAR, vh="L'essentiel",
        lines=["Avis &amp; réseaux,", "sur ton <em>site</em>"],
        base="Affiche tes avis clients, tes flux de réseaux sociaux et un chat sur ton site WordPress, pour rassurer et convertir tes visiteurs.",
        vn="Preuve sociale", vs="avis, flux sociaux et chat sur ton site",
        stats=[("Type", "Preuve sociale"), ("Force", "Avis &amp; flux sociaux"), ("Atout", "Widgets de chat"), ("Idéal pour", "Rassurer &amp; convertir")],
        foot="Tes visiteurs, mis en confiance"),
    dict(id=97456, lang="en", htmllang="en", pt="WP Social Ninja - Hero EN", tf=68, vf=68,
        p1="WP Social Ninja", p2="Review", icon=I_STAR, vh="The essentials",
        lines=["Reviews &amp; feeds,", "on your <em>site</em>"],
        base="Show your customer reviews, your social media feeds and a chat widget on your WordPress site, to reassure and convert your visitors.",
        vn="Social proof", vs="reviews, social feeds and chat on your site",
        stats=[("Type", "Social proof"), ("Strength", "Reviews &amp; feeds"), ("Plus", "Chat widgets"), ("Best for", "Trust &amp; conversion")],
        foot="Turn visitors into trust"),
    # Missinglettr FR -- social media automation (drip)
    dict(id=44066, lang="fr", htmllang="fr", pt="Missinglettr - Hero FR", tf=84, vf=60,
        p1="Missinglettr", p2="Avis", icon=I_REPEAT, vh="L'essentiel",
        lines=["Ton social,", "en <em>automatique</em>"],
        base="L'outil qui transforme chaque article de blog en une campagne de posts sociaux étalée sur un an, générée et programmée pour toi.",
        vn="Le pilote auto", vs="tes réseaux sociaux en pilote automatique",
        stats=[("Type", "Automation sociale"), ("Force", "Drip sur 12 mois"), ("Atout", "Posts générés pour toi"), ("Idéal pour", "Gagner du temps")],
        foot="L'outil qui bosse à ta place"),
    # Facebook Pixel FR -- tracking guide
    dict(id=3161, lang="fr", htmllang="fr", pt="Pixel Facebook - Hero FR", tf=72, vf=84,
        p1="Pixel Facebook", p2="Guide", icon=I_TARGET, vh="L'essentiel",
        lines=["Le pixel", "Facebook <em>installé</em>"],
        base="Comprends ce qu'est le pixel Facebook et installe-le pas à pas sur ton site WordPress pour mesurer tes conversions et faire du retargeting.",
        vn="Le suivi", vs="mesurer tes conversions et retargeter",
        stats=[("Type", "Guide"), ("Objectif", "Suivi des conversions"), ("Niveau", "Débutant"), ("Idéal pour", "Pubs &amp; retargeting")],
        foot="Sache ce que tes pubs rapportent"),
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
