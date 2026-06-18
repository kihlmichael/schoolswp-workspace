"""Generate brand-grade featured-image heros (1920x1080) for the page-builders batch.

Two layouts: verdict-block (v) and compare-head (c). Output: post-<ID>/slide-00-hero-<lang>.html
Run from assets/featured-images/. Reproducible, versionnable, zero AI credits.
"""

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
@@EXTRACSS@@
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
@@BODY@@
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

VCSS = """      .visual-inner { padding: 64px 56px 52px 56px; display: flex; flex-direction: column; gap: 30px; height: 100%; }
      .verdict-block { display: flex; flex-direction: column; align-items: center; gap: 6px; padding: 6px 0 2px; text-align: center; }
      .verdict-num { font-weight: 900; font-size: @@VERDICTFONT@@px; line-height: 1; letter-spacing: -3px; color: var(--green); white-space: nowrap; }
      .verdict-sub { font-size: 22px; font-weight: 600; color: var(--grey-text); line-height: 1.3; max-width: 470px; }
      .stats { display: flex; flex-direction: column; gap: 10px; width: 100%; flex: 1; justify-content: center; }
      .stat { display: flex; justify-content: space-between; align-items: baseline; padding: 13px 4px; border-bottom: 1px dashed var(--line); font-size: 21px; }
      .stat:last-child { border-bottom: none; }
      .stat-key { color: var(--grey-text); font-weight: 500; }
      .stat-val { color: var(--black); font-weight: 800; }"""

CCSS = """      .visual-inner { padding: 56px 50px 46px 50px; display: flex; flex-direction: column; gap: 24px; height: 100%; }
      .cmp { flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 26px; }
      .compare-head { display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; gap: 8px; padding: 4px 0 2px; }
      .ch-col { display: flex; flex-direction: column; align-items: center; gap: 2px; text-align: center; }
      .ch-name { font-size: 23px; font-weight: 800; color: var(--black); line-height: 1.05; letter-spacing: -0.5px; }
      .ch-tag { font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: var(--green); }
      .ch-vs { font-size: 20px; font-weight: 900; color: var(--grey-text); width: 56px; text-align: center; }
      .compare { display: flex; flex-direction: column; gap: 0; }
      .crow { display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; gap: 10px; padding: 13px 0; border-bottom: 1px dashed var(--line); }
      .crow:last-child { border-bottom: none; }
      .cv { font-size: 18px; font-weight: 700; color: var(--black); text-align: center; line-height: 1.2; }
      .caxis { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; color: var(--grey-text); text-align: center; width: 116px; }"""


def vbody(verdict_font, verdict_num, verdict_sub, stats):
    rows = "\n".join(
        f'            <div class="stat"><span class="stat-key">{k}</span><span class="stat-val">{v}</span></div>'
        for k, v in stats
    )
    return (
        '          <div class="verdict-block">\n'
        f'            <div class="verdict-num">{verdict_num}</div>\n'
        f'            <div class="verdict-sub">{verdict_sub}</div>\n'
        "          </div>\n"
        '          <div class="stats">\n'
        f"{rows}\n"
        "          </div>"
    )


def cbody(chl_name, chl_tag, chr_name, chr_tag, crows):
    rows = "\n".join(
        f'              <div class="crow"><div class="cv">{l}</div><div class="caxis">{a}</div><div class="cv">{r}</div></div>'
        for l, a, r in crows
    )
    return (
        '          <div class="cmp">\n'
        '            <div class="compare-head">\n'
        f'              <div class="ch-col"><div class="ch-name">{chl_name}</div><div class="ch-tag">{chl_tag}</div></div>\n'
        '              <div class="ch-vs">vs</div>\n'
        f'              <div class="ch-col"><div class="ch-name">{chr_name}</div><div class="ch-tag">{chr_tag}</div></div>\n'
        "            </div>\n"
        '            <div class="compare">\n'
        f"{rows}\n"
        "            </div>\n"
        "          </div>"
    )


def tlines(lines):
    return "".join(f"<span>{x}</span>" for x in lines)


# Icons (feather-style inner SVG)
I_PLAY_CIRCLE = '<circle cx="12" cy="12" r="10"></circle><polygon points="10 8 16 12 10 16 10 8"></polygon>'
I_BLOCKS = '<rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect>'
I_LAYOUT = '<rect x="3" y="3" width="18" height="18" rx="2"></rect><path d="M3 9h18"></path><path d="M9 21V9"></path>'
I_LAYERS = '<polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline>'
I_SWAP = '<path d="M16 3l4 4-4 4"></path><path d="M20 7H4"></path><path d="M8 21l-4-4 4-4"></path><path d="M4 17h16"></path>'
I_CODE = '<polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline>'
I_PLAY = '<polygon points="5 3 19 12 5 21 5 3"></polygon>'
I_BOLT = '<path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path>'
I_TROPHY = '<path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path><path d="M4 22h16"></path><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"></path>'
I_GEAR = '<circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"></path>'
I_WRENCH = '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>'
I_FEATHER = '<path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"></path><line x1="16" y1="8" x2="2" y2="22"></line><line x1="17.5" y1="15" x2="9" y2="15"></line>'
I_BOX = '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line>'

V = []  # verdict-block heros
C = []  # compare heros

# 1. FluentPlayer FR
V.append(dict(id=2289921, lang="fr", htmllang="fr", pt="FluentPlayer - Hero FR", tf=80, vf=76,
    p1="FluentPlayer", p2="Lecteur vid&eacute;o", icon=I_PLAY_CIRCLE, vh="L'essentiel",
    lines=["FluentPlayer,", "vid&eacute;o <em>interactive</em>"],
    base="Le lecteur vid&eacute;o de WPManageNinja : chapitres, fiches, appels &agrave; l'action et suivi des vues, directement dans WordPress.",
    vn="Interactif", vs="le lecteur vid&eacute;o sign&eacute; WPManageNinja",
    stats=[("Type", "Lecteur vid&eacute;o"), ("Force", "Vid&eacute;o interactive"), ("&Eacute;cosyst&egrave;me", "Fluent"), ("Id&eacute;al pour", "Cours &amp; marketing")],
    foot="La vid&eacute;o qui engage tes visiteurs"))

# 2. Gutenberg FR / EN / DE
V.append(dict(id=57155, lang="fr", htmllang="fr", pt="Gutenberg - Hero FR", tf=88, vf=80,
    p1="Gutenberg", p2="Guide", icon=I_BLOCKS, vh="L'essentiel",
    lines=["Gutenberg,", "l'<em>&eacute;diteur</em> WP"],
    base="L'&eacute;diteur de blocs natif de WordPress : comment &ccedil;a marche, ce qu'il change, et comment en tirer parti.",
    vn="L'&eacute;diteur", vs="l'&eacute;diteur de blocs natif de WordPress",
    stats=[("Type", "&Eacute;diteur natif"), ("Principe", "Blocs"), ("Niveau", "D&eacute;butant"), ("Id&eacute;al pour", "Cr&eacute;er ses pages")],
    foot="Le c&oelig;ur de WordPress moderne"))
V.append(dict(id=57235, lang="en", htmllang="en", pt="Gutenberg - Hero EN", tf=88, vf=80,
    p1="Gutenberg", p2="Guide", icon=I_BLOCKS, vh="The essentials",
    lines=["Gutenberg,", "the WP <em>editor</em>"],
    base="WordPress' native block editor: how it works, what it changes, and how to get the most out of it.",
    vn="The editor", vs="WordPress' native block editor",
    stats=[("Type", "Native editor"), ("Principle", "Blocks"), ("Level", "Beginner"), ("Best for", "Building pages")],
    foot="The heart of modern WordPress"))
V.append(dict(id=57236, lang="de", htmllang="de", pt="Gutenberg - Hero DE", tf=86, vf=80,
    p1="Gutenberg", p2="Guide", icon=I_BLOCKS, vh="Das Wichtigste",
    lines=["Gutenberg,", "der WP-<em>Editor</em>"],
    base="Der native Block-Editor von WordPress: wie er funktioniert, was er ver&auml;ndert und wie du ihn optimal nutzt.",
    vn="Der Editor", vs="der native Block-Editor von WordPress",
    stats=[("Typ", "Nativer Editor"), ("Prinzip", "Bl&ouml;cke"), ("Niveau", "Einsteiger"), ("Ideal f&uuml;r", "Seiten bauen")],
    foot="Das Herz von modernem WordPress"))

# 3. FSE FR / EN / DE
V.append(dict(id=55007, lang="fr", htmllang="fr", pt="FSE - Hero FR", tf=92, vf=88,
    p1="Full Site Editing", p2="Guide", icon=I_LAYOUT, vh="L'essentiel",
    lines=["Le FSE,", "le <em>futur</em> de WP"],
    base="Le Full Site Editing : &eacute;diter tout ton site (en-t&ecirc;te, pied de page, mod&egrave;les) au bloc, sans toucher au code.",
    vn="Le futur", vs="&eacute;diter tout ton site au bloc",
    stats=[("Type", "&Eacute;dition de site"), ("Principe", "Th&egrave;mes &agrave; blocs"), ("Niveau", "Interm&eacute;diaire"), ("Id&eacute;al pour", "Sites sans code")],
    foot="Tout ton site &eacute;ditable au bloc"))
V.append(dict(id=55420, lang="en", htmllang="en", pt="FSE - Hero EN", tf=88, vf=84,
    p1="Full Site Editing", p2="Guide", icon=I_LAYOUT, vh="The essentials",
    lines=["FSE,", "the <em>future</em> of WP"],
    base="Full Site Editing: edit your entire site (header, footer, templates) with blocks, without touching code.",
    vn="The future", vs="edit your whole site with blocks",
    stats=[("Type", "Site editing"), ("Principle", "Block themes"), ("Level", "Intermediate"), ("Best for", "No-code sites")],
    foot="Your entire site, block-editable"))
V.append(dict(id=55419, lang="de", htmllang="de", pt="FSE - Hero DE", tf=92, vf=84,
    p1="Full Site Editing", p2="Guide", icon=I_LAYOUT, vh="Das Wichtigste",
    lines=["FSE,", "die <em>Zukunft</em>"],
    base="Full Site Editing: Bearbeite deine ganze Website (Header, Footer, Templates) mit Bl&ouml;cken, ganz ohne Code.",
    vn="Die Zukunft", vs="deine ganze Website mit Bl&ouml;cken bauen",
    stats=[("Typ", "Site-Editing"), ("Prinzip", "Block-Themes"), ("Niveau", "Mittel"), ("Ideal f&uuml;r", "Seiten ohne Code")],
    foot="Deine ganze Website per Block"))

# 4. ElementsKit FR / EN / DE
V.append(dict(id=53976, lang="fr", htmllang="fr", pt="ElementsKit - Hero FR", tf=78, vf=78,
    p1="ElementsKit", p2="Addons Elementor", icon=I_LAYERS, vh="L'essentiel",
    lines=["ElementsKit,", "le <em>tout-en-un</em>"],
    base="L'add-on tout-en-un pour Elementor : des dizaines de widgets, un constructeur d'en-t&ecirc;te et un mega menu r&eacute;unis.",
    vn="Tout-en-un", vs="des dizaines de widgets pour Elementor",
    stats=[("Type", "Add-on Elementor"), ("Contenu", "90+ widgets"), ("Force", "En-t&ecirc;te &amp; menu"), ("Id&eacute;al pour", "&Eacute;tendre Elementor")],
    foot="Elementor boost&eacute;, sans empiler les plugins"))
V.append(dict(id=679464, lang="en", htmllang="en", pt="ElementsKit - Hero EN", tf=78, vf=80,
    p1="ElementsKit", p2="Elementor addons", icon=I_LAYERS, vh="The essentials",
    lines=["ElementsKit,", "the <em>all-in-one</em>"],
    base="The all-in-one add-on for Elementor: dozens of widgets, a header builder and a mega menu in one pack.",
    vn="All-in-one", vs="dozens of widgets for Elementor",
    stats=[("Type", "Elementor add-on"), ("Content", "90+ widgets"), ("Strength", "Header &amp; menu"), ("Best for", "Extending Elementor")],
    foot="Elementor supercharged, fewer plugins"))
V.append(dict(id=679476, lang="de", htmllang="de", pt="ElementsKit - Hero DE", tf=78, vf=80,
    p1="ElementsKit", p2="Elementor-Addons", icon=I_LAYERS, vh="Das Wichtigste",
    lines=["ElementsKit,", "das <em>All-in-one</em>"],
    base="Das All-in-one-Addon f&uuml;r Elementor: dutzende Widgets, ein Header-Builder und ein Mega-Men&uuml; in einem Paket.",
    vn="All-in-one", vs="dutzende Widgets f&uuml;r Elementor",
    stats=[("Typ", "Elementor-Addon"), ("Inhalt", "90+ Widgets"), ("St&auml;rke", "Header &amp; Men&uuml;"), ("Ideal f&uuml;r", "Elementor erweitern")],
    foot="Elementor aufgebohrt, weniger Plugins"))

# 6. Microthemer FR / EN
V.append(dict(id=50952, lang="fr", htmllang="fr", pt="Microthemer - Hero FR", tf=84, vf=78,
    p1="Microthemer", p2="Avis", icon=I_CODE, vh="L'essentiel",
    lines=["Microthemer,", "le <em>CSS</em> visuel"],
    base="Un &eacute;diteur CSS visuel pour WordPress : personnalise n'importe quel &eacute;l&eacute;ment &agrave; la souris, sans &eacute;crire de code.",
    vn="CSS visuel", vs="personnaliser ton site sans coder",
    stats=[("Type", "&Eacute;diteur CSS"), ("Force", "Sans code"), ("Cible", "N'importe quel th&egrave;me"), ("Id&eacute;al pour", "Designers &amp; no-code")],
    foot="Le CSS sur-mesure, &agrave; la souris"))
V.append(dict(id=97482, lang="en", htmllang="en", pt="Microthemer - Hero EN", tf=88, vf=80,
    p1="Microthemer", p2="Review", icon=I_CODE, vh="The essentials",
    lines=["Microthemer,", "<em>visual</em> CSS"],
    base="A visual CSS editor for WordPress: style any element with your mouse, without writing a single line of code.",
    vn="Visual CSS", vs="style your site without coding",
    stats=[("Type", "CSS editor"), ("Strength", "No code"), ("Target", "Any theme"), ("Best for", "Designers &amp; no-code")],
    foot="Custom CSS, point and click"))

# 7. Presto Player FR
V.append(dict(id=46176, lang="fr", htmllang="fr", pt="Presto Player - Hero FR", tf=84, vf=84,
    p1="Presto Player", p2="Avis", icon=I_PLAY, vh="L'essentiel",
    lines=["Presto Player,", "le <em>lecteur</em>"],
    base="Le lecteur vid&eacute;o de r&eacute;f&eacute;rence pour WordPress : design soign&eacute;, chapitres, capture d'e-mails et compatibilit&eacute; LMS.",
    vn="Le lecteur", vs="la vid&eacute;o pro pour WordPress",
    stats=[("Type", "Lecteur vid&eacute;o"), ("Force", "Design &amp; LMS"), ("Sources", "YouTube, Vimeo, Bunny"), ("Id&eacute;al pour", "Cours &amp; contenus")],
    foot="Tes vid&eacute;os, version professionnelle"))

# 8. Crocoblock FR / EN / DE
V.append(dict(id=44121, lang="fr", htmllang="fr", pt="Crocoblock - Hero FR", tf=78, vf=80,
    p1="Crocoblock", p2="Avis", icon=I_BOLT, vh="L'essentiel",
    lines=["Crocoblock,", "le site <em>dynamique</em>"],
    base="La suite JetPlugins pour Elementor : contenus dynamiques, annuaires, filtres et sites sur-mesure sans coder.",
    vn="Dynamique", vs="des sites dynamiques avec Elementor",
    stats=[("Type", "Suite Elementor"), ("Star", "JetEngine"), ("Force", "Contenu dynamique"), ("Id&eacute;al pour", "Sites complexes")],
    foot="Elementor passe au niveau pro"))
V.append(dict(id=58540, lang="en", htmllang="en", pt="Crocoblock - Hero EN", tf=84, vf=88,
    p1="Crocoblock", p2="Review", icon=I_BOLT, vh="The essentials",
    lines=["Crocoblock,", "<em>dynamic</em> sites"],
    base="The JetPlugins suite for Elementor: dynamic content, directories, filters and custom sites without code.",
    vn="Dynamic", vs="dynamic sites with Elementor",
    stats=[("Type", "Elementor suite"), ("Star", "JetEngine"), ("Strength", "Dynamic content"), ("Best for", "Complex sites")],
    foot="Elementor goes pro"))
V.append(dict(id=58545, lang="de", htmllang="de", pt="Crocoblock - Hero DE", tf=76, vf=84,
    p1="Crocoblock", p2="Test", icon=I_BOLT, vh="Das Wichtigste",
    lines=["Crocoblock,", "<em>dynamische</em> Sites"],
    base="Die JetPlugins-Suite f&uuml;r Elementor: dynamische Inhalte, Verzeichnisse, Filter und individuelle Sites ohne Code.",
    vn="Dynamisch", vs="dynamische Sites mit Elementor",
    stats=[("Typ", "Elementor-Suite"), ("Star", "JetEngine"), ("St&auml;rke", "Dynamische Inhalte"), ("Ideal f&uuml;r", "Komplexe Sites")],
    foot="Elementor wird professionell"))

# 9. Top 3 addons Elementor FR
V.append(dict(id=7862, lang="fr", htmllang="fr", pt="Top 3 addons Elementor - Hero FR", tf=84, vf=84,
    p1="Addons Elementor", p2="Comparatif", icon=I_TROPHY, vh="L'essentiel",
    lines=["Addons Elementor,", "le <em>top 3</em>"],
    base="ElementsKit, Piotnet et Exclusive Addons compar&eacute;s : lequel choisir pour &eacute;tendre Elementor sans alourdir ton site ?",
    vn="Le top 3", vs="ElementsKit, Piotnet, Exclusive",
    stats=[("Type", "Comparatif"), ("En lice", "3 add-ons"), ("Crit&egrave;res", "Widgets &amp; prix"), ("Id&eacute;al pour", "Bien choisir")],
    foot="Trois add-ons, un seul gagnant pour toi"))

# 10. Divi Machine FR
V.append(dict(id=6184, lang="fr", htmllang="fr", pt="Divi Machine - Hero FR", tf=78, vf=78,
    p1="Divi Machine", p2="Avis", icon=I_GEAR, vh="L'essentiel",
    lines=["Divi Machine,", "le <em>sur-mesure</em>"],
    base="Le plugin qui transforme Divi en machine &agrave; contenus dynamiques : annuaires, fiches, filtres et boutiques.",
    vn="Sur-mesure", vs="des contenus dynamiques pour Divi",
    stats=[("Type", "Add-on Divi"), ("Force", "Contenu dynamique"), ("Cible", "Divi / WooCommerce"), ("Id&eacute;al pour", "Sites avanc&eacute;s")],
    foot="Divi passe au dynamique"))

# 11. Beaver Builder FR
V.append(dict(id=2471, lang="fr", htmllang="fr", pt="Beaver Builder - Hero FR", tf=80, vf=88,
    p1="Beaver Builder", p2="Avis", icon=I_WRENCH, vh="L'essentiel",
    lines=["Beaver Builder,", "le <em>fiable</em>"],
    base="Le constructeur de pages r&eacute;put&eacute; pour sa stabilit&eacute; : un code propre, z&eacute;ro d&eacute;pendance forc&eacute;e, des bases solides.",
    vn="Fiable", vs="le page builder propre et stable",
    stats=[("Type", "Page builder"), ("Force", "Stabilit&eacute;"), ("Atout", "Code propre"), ("Id&eacute;al pour", "Sites pros durables")],
    foot="Le builder qui ne te l&acirc;che pas"))

# 12. Kadence WP FR (schoolsWP stack theme, singular voice)
V.append(dict(id=3087, lang="fr", htmllang="fr", pt="Kadence WP - Hero FR", tf=84, vf=92,
    p1="Kadence", p2="Avis", icon=I_FEATHER, vh="L'essentiel",
    lines=["Kadence,", "le th&egrave;me <em>l&eacute;ger</em>"],
    base="Mon th&egrave;me WordPress pr&eacute;f&eacute;r&eacute; : ultra l&eacute;ger, rapide et personnalisable, avec un constructeur d'en-t&ecirc;te au top.",
    vn="L&eacute;ger", vs="mon th&egrave;me WordPress pr&eacute;f&eacute;r&eacute;",
    stats=[("Type", "Th&egrave;me"), ("Force", "Vitesse"), ("Atout", "Personnalisable"), ("Id&eacute;al pour", "Tous les sites")],
    foot="Rapide, l&eacute;ger, mon choix par d&eacute;faut"))

# 13. Zoom sur Divi FR
V.append(dict(id=898, lang="fr", htmllang="fr", pt="Divi - Hero FR", tf=88, vf=80,
    p1="Divi", p2="Avis", icon=I_BOX, vh="L'essentiel",
    lines=["Divi,", "le <em>polyvalent</em>"],
    base="Th&egrave;me et constructeur visuel tout-en-un : Divi te laisse tout designer &agrave; la souris, avec une licence &agrave; vie.",
    vn="Polyvalent", vs="le th&egrave;me et builder tout-en-un",
    stats=[("Type", "Th&egrave;me + builder"), ("Force", "Tout visuel"), ("Licence", "&Agrave; vie"), ("Id&eacute;al pour", "Designers complets")],
    foot="Tout designer, sans &eacute;crire de code"))

# 5. Divi vs Elementor (compare) FR / EN / DE
C.append(dict(id=53915, lang="fr", htmllang="fr", pt="Divi vs Elementor - Hero FR", tf=118,
    p1="Divi vs Elementor", p2="Comparatif", icon=I_SWAP, vh="Le comparatif",
    lines=["Divi ou", "<em>Elementor</em>&nbsp;?"],
    base="Divi Builder et Elementor Pro se disputent le titre de meilleur constructeur de pages. Lequel pour ton site ?",
    chl=("Divi Builder", "Le pack"), chr=("Elementor Pro", "Le standard"),
    crows=[("Licence &agrave; vie", "Tarif", "Abonnement"), ("Sites illimit&eacute;s", "Force", "&Eacute;cosyst&egrave;me"),
           ("Tout inclus", "Approche", "Widgets + add-ons"), ("Fans de Divi", "Id&eacute;al pour", "Le plus populaire")],
    foot="Pack &agrave; vie ou &eacute;cosyst&egrave;me roi ? Au cas par cas"))
C.append(dict(id=58089, lang="en", htmllang="en", pt="Divi vs Elementor - Hero EN", tf=118,
    p1="Divi vs Elementor", p2="Comparison", icon=I_SWAP, vh="The comparison",
    lines=["Divi or", "<em>Elementor</em>?"],
    base="Divi Builder and Elementor Pro both claim the best page builder crown. Which one fits your site?",
    chl=("Divi Builder", "The bundle"), chr=("Elementor Pro", "The standard"),
    crows=[("Lifetime license", "Pricing", "Subscription"), ("Unlimited sites", "Strength", "Ecosystem"),
           ("All included", "Approach", "Widgets + add-ons"), ("Divi fans", "Best for", "Most popular")],
    foot="Lifetime bundle or top ecosystem? Case by case"))
C.append(dict(id=58095, lang="de", htmllang="de", pt="Divi vs Elementor - Hero DE", tf=110,
    p1="Divi vs Elementor", p2="Vergleich", icon=I_SWAP, vh="Der Vergleich",
    lines=["Divi oder", "<em>Elementor</em>?"],
    base="Divi Builder und Elementor Pro k&auml;mpfen um den Titel als bester Page-Builder. Welcher passt zu deiner Website?",
    chl=("Divi Builder", "Das Paket"), chr=("Elementor Pro", "Der Standard"),
    crows=[("Lifetime-Lizenz", "Preis", "Abo"), ("Unbegrenzte Sites", "St&auml;rke", "&Ouml;kosystem"),
           ("Alles dabei", "Ansatz", "Widgets + Addons"), ("Divi-Fans", "Ideal f&uuml;r", "Am beliebtesten")],
    foot="Lifetime-Paket oder Top-&Ouml;kosystem? Je nachdem"))


def render_v(h):
    html = HEAD
    html = html.replace("@@EXTRACSS@@", VCSS.replace("@@VERDICTFONT@@", str(h["vf"])))
    html = html.replace("@@BODY@@", vbody(h["vf"], h["vn"], h["vs"], h["stats"]))
    return fill(html, h)


def render_c(h):
    html = HEAD
    html = html.replace("@@EXTRACSS@@", CCSS)
    html = html.replace("@@BODY@@", cbody(h["chl"][0], h["chl"][1], h["chr"][0], h["chr"][1], h["crows"]))
    return fill(html, h)


def fill(html, h):
    html = html.replace("@@HTMLLANG@@", h["htmllang"])
    html = html.replace("@@PAGETITLE@@", h["pt"])
    html = html.replace("@@TITLEFONT@@", str(h["tf"]))
    html = html.replace("@@PILL1@@", h["p1"])
    html = html.replace("@@PILL2@@", h["p2"])
    html = html.replace("@@TITLELINES@@", tlines(h["lines"]))
    html = html.replace("@@BASELINE@@", h["base"])
    html = html.replace("@@ICON@@", h["icon"])
    html = html.replace("@@VHEADER@@", h["vh"])
    html = html.replace("@@FOOTER@@", h["foot"])
    return html


count = 0
for h in V:
    d = f"post-{h['id']}"
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, f"slide-00-hero-{h['lang']}.html"), "w", encoding="utf-8") as f:
        f.write(render_v(h))
    count += 1
for h in C:
    d = f"post-{h['id']}"
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, f"slide-00-hero-{h['lang']}.html"), "w", encoding="utf-8") as f:
        f.write(render_c(h))
    count += 1

print(f"Generated {count} hero HTML files")
for h in V + C:
    print(f"  post-{h['id']}/slide-00-hero-{h['lang']}.html")
