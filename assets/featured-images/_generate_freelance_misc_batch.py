"""Generate heros for the freelance/marketplace/misc-tools/portraits batch (verdict-block)."""

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

I_TAG = '<path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path><line x1="7" y1="7" x2="7.01" y2="7"></line>'
I_BRIEFCASE = '<rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>'
I_GLOBE = '<circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>'
I_BARCHART = '<line x1="12" y1="20" x2="12" y2="10"></line><line x1="18" y1="20" x2="18" y2="4"></line><line x1="6" y1="20" x2="6" y2="16"></line>'
I_IMAGE = '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline>'
I_LAYERS = '<polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline>'
I_CHAT = '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path>'
I_PACKAGE = '<line x1="16.5" y1="9.4" x2="7.5" y2="4.21"></line><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line>'
I_USER = '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle>'
I_AWARD = '<circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline>'
I_TRENDING = '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline>'

V = [
    # ComeUp FR / EN (draft) -- French micro-services marketplace
    dict(id=2506216, lang="fr", htmllang="fr", pt="ComeUp - Hero FR", tf=92, vf=60,
        p1="ComeUp", p2="Avis", icon=I_TAG, vh="L'essentiel",
        lines=["Vendre tes", "<em>services</em>"],
        base="La place de marché française pour acheter et vendre des micro-services en ligne, des centaines de prestations dans tous les domaines.",
        vn="Micro-services", vs="acheter et vendre des micro-services en ligne",
        stats=[("Type", "Place de marché"), ("Origine", "Française"), ("Force", "Micro-services"), ("Idéal pour", "Acheter &amp; vendre")],
        foot="La marketplace made in France"),
    dict(id=2888491, lang="en", htmllang="en", pt="ComeUp - Hero EN", tf=92, vf=60,
        p1="ComeUp", p2="Review", icon=I_TAG, vh="The essentials",
        lines=["Sell your", "<em>services</em>"],
        base="The French marketplace to buy and sell micro-services online, with hundreds of gigs across every field.",
        vn="Micro-services", vs="buy and sell micro-services online",
        stats=[("Type", "Marketplace"), ("Origin", "French"), ("Strength", "Micro-services"), ("Best for", "Buy &amp; sell")],
        foot="The French gig marketplace"),
    # Metricool FR / EN -- social media management (schedule + analytics)
    dict(id=1599511, lang="fr", htmllang="fr", pt="Metricool - Hero FR", tf=84, vf=72,
        p1="Metricool", p2="Avis", icon=I_BARCHART, vh="L'essentiel",
        lines=["Tes réseaux,", "<em>pilotés</em>"],
        base="L'outil tout-en-un pour planifier, analyser et piloter tes réseaux sociaux depuis un seul tableau de bord.",
        vn="Le pilotage", vs="planifier et analyser tes réseaux sociaux",
        stats=[("Type", "Gestion sociale"), ("Force", "Planif &amp; analytics"), ("Atout", "Tout-en-un"), ("Idéal pour", "Community managers")],
        foot="Tes réseaux, sous contrôle"),
    dict(id=1946752, lang="en", htmllang="en", pt="Metricool - Hero EN", tf=80, vf=76,
        p1="Metricool", p2="Review", icon=I_BARCHART, vh="The essentials",
        lines=["Your socials,", "<em>managed</em>"],
        base="The all-in-one tool to schedule, analyze and steer your social media from a single dashboard.",
        vn="Social hub", vs="schedule and analyze your social media",
        stats=[("Type", "Social mgmt"), ("Strength", "Scheduling &amp; analytics"), ("Plus", "All-in-one"), ("Best for", "Community managers")],
        foot="Your socials, under control"),
    # Canva for WordPress -- design guide
    dict(id=48485, lang="fr", htmllang="fr", pt="Canva site WP - Hero FR", tf=80, vf=80,
        p1="Canva", p2="Guide", icon=I_IMAGE, vh="L'essentiel",
        lines=["Un beau site", "avec <em>Canva</em>"],
        base="Comment créer des visuels et un site WordPress soignés avec Canva, même sans la moindre compétence en design.",
        vn="Le design", vs="des visuels pros, sans être designer",
        stats=[("Type", "Guide"), ("Objectif", "Visuels soignés"), ("Niveau", "Débutant"), ("Idéal pour", "Sites &amp; réseaux")],
        foot="Le design à la portée de tous"),
    # Webflow -- no-code website builder
    dict(id=48487, lang="fr", htmllang="fr", pt="Webflow - Hero FR", tf=76, vf=76,
        p1="Webflow", p2="Guide", icon=I_LAYERS, vh="L'essentiel",
        lines=["Créer un site", "sans <em>code</em>"],
        base="Le constructeur de sites no-code qui combine design visuel et puissance d'un CMS, une vraie alternative à WordPress.",
        vn="Le no-code", vs="créer un site web sans écrire de code",
        stats=[("Type", "Constructeur no-code"), ("Force", "Design visuel"), ("Comparé à", "WordPress"), ("Idéal pour", "Designers")],
        foot="Le web, sans une ligne de code"),
    # ManyChat -- Messenger chatbot
    dict(id=46119, lang="fr", htmllang="fr", pt="ManyChat - Hero FR", tf=80, vf=76,
        p1="ManyChat", p2="Guide", icon=I_CHAT, vh="L'essentiel",
        lines=["Ton chatbot", "<em>Messenger</em>"],
        base="L'outil pour créer un chatbot Messenger et automatiser tes conversations, tes ventes et ton support sur Facebook et Instagram.",
        vn="Le chatbot", vs="automatiser tes conversations Messenger",
        stats=[("Type", "Chatbot"), ("Force", "Messenger &amp; Insta"), ("Atout", "Automatisation"), ("Idéal pour", "Vente &amp; support")],
        foot="Tes conversations, automatisées"),
    # BeFreelancr -- French freelance marketplace
    dict(id=45812, lang="fr", htmllang="fr", pt="BeFreelancr - Hero FR", tf=88, vf=60,
        p1="BeFreelancr", p2="Avis", icon=I_BRIEFCASE, vh="L'essentiel",
        lines=["Trouve ton", "<em>freelance</em>"],
        base="La plateforme française pour acheter et vendre des services freelance en ligne, de la rédaction au design en passant par le web.",
        vn="Les freelances", vs="acheter et vendre des services freelance",
        stats=[("Type", "Place de marché"), ("Origine", "Française"), ("Force", "Services freelance"), ("Idéal pour", "Trouver un pro")],
        foot="Ton freelance en quelques clics"),
    # CodeaProd -- turnkey affiliate blog
    dict(id=45640, lang="fr", htmllang="fr", pt="CodeaProd - Hero FR", tf=84, vf=72,
        p1="CodeaProd", p2="Avis", icon=I_PACKAGE, vh="L'essentiel",
        lines=["Ton blog,", "clé en <em>main</em>"],
        base="Le service qui te livre un blog d'affiliation clé en main, déjà construit et optimisé, sans avoir à le créer toi-même.",
        vn="Clé en main", vs="un blog d'affiliation prêt à l'emploi",
        stats=[("Type", "Service"), ("Force", "Blog clé en main"), ("Atout", "Gain de temps"), ("Idéal pour", "Se lancer vite")],
        foot="Ton blog d'affiliation, livré prêt"),
    # Pierre-Eliott Lallemant -- portrait (creator of Skeall)
    dict(id=4821, lang="fr", htmllang="fr", pt="Pierre-Eliott Lallemant - Hero FR", tf=84, vf=72,
        p1="Pierre-Eliott L.", p2="Portrait", icon=I_USER, vh="Le portrait",
        lines=["Le créateur", "de <em>Skeall</em>"],
        base="Portrait de Pierre-Eliott Lallemant, formateur français en business en ligne et fondateur de Skeall : parcours et méthode.",
        vn="Le créateur", vs="formateur et fondateur de Skeall",
        stats=[("Activité", "Formateur"), ("Spécialité", "Business en ligne"), ("Connu pour", "Skeall"), ("Profil", "Entrepreneur FR")],
        foot="Le parcours derrière Skeall"),
    # Frank Houbré -- portrait
    dict(id=4530, lang="fr", htmllang="fr", pt="Frank Houbre - Hero FR", tf=80, vf=68,
        p1="Frank Houbré", p2="Portrait", icon=I_AWARD, vh="Le portrait",
        lines=["Qui est", "Frank <em>Houbré</em>"],
        base="Portrait de Frank Houbré, formateur français en business en ligne : son parcours, sa crédibilité et ce qu'il propose.",
        vn="Le formateur", vs="formateur français en business en ligne",
        stats=[("Activité", "Formateur"), ("Spécialité", "Business en ligne"), ("Format", "Formations"), ("Profil", "Entrepreneur FR")],
        foot="Le parcours et la méthode"),
    # Jungle Scout -- Amazon FBA product research
    dict(id=3554, lang="fr", htmllang="fr", pt="Jungle Scout - Hero FR", tf=76, vf=50,
        p1="Jungle Scout", p2="Avis", icon=I_TRENDING, vh="L'essentiel",
        lines=["Booste tes", "ventes <em>Amazon</em>"],
        base="L'outil de recherche produit pour les vendeurs Amazon : repère les produits porteurs et analyse la concurrence et la demande.",
        vn="Vendre sur Amazon", vs="trouver les produits qui se vendent sur Amazon",
        stats=[("Type", "Recherche produit"), ("Force", "Données Amazon"), ("Atout", "Analyse concurrence"), ("Idéal pour", "Vendeurs FBA")],
        foot="Les bons produits, avant les autres"),
    # Fiverr -- global freelance marketplace
    dict(id=927, lang="fr", htmllang="fr", pt="Fiverr - Hero FR", tf=72, vf=88,
        p1="Fiverr", p2="Avis", icon=I_GLOBE, vh="L'essentiel",
        lines=["Des freelances", "du <em>monde</em>"],
        base="La marketplace mondiale pour trouver des freelances dans tous les domaines, du logo à la vidéo en passant par la rédaction.",
        vn="Le géant", vs="trouver des freelances du monde entier",
        stats=[("Type", "Place de marché"), ("Portée", "Mondiale"), ("Force", "Tous les domaines"), ("Idéal pour", "Trouver un freelance")],
        foot="Le freelance, à l'échelle mondiale"),
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
