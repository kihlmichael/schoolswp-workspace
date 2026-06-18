"""Generate heros for the draft posts that lack a featured image (verdict-block)."""

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

I_GAUGE = '<path d="M12 14l4-4"></path><path d="M3.34 19a10 10 0 1 1 17.32 0"></path>'
I_SHUFFLE = '<polyline points="16 3 21 3 21 8"></polyline><line x1="4" y1="20" x2="21" y2="3"></line><polyline points="21 16 21 21 16 21"></polyline><line x1="15" y1="15" x2="21" y2="21"></line><line x1="4" y1="4" x2="9" y2="9"></line>'
I_GRID = '<rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect>'
I_TRUCK = '<rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle>'
I_COMPARE = '<circle cx="18" cy="18" r="3"></circle><circle cx="6" cy="6" r="3"></circle><path d="M13 6h3a2 2 0 0 1 2 2v7"></path><path d="M11 18H8a2 2 0 0 1-2-2V9"></path>'
I_GIFT = '<polyline points="20 12 20 22 4 22 4 12"></polyline><rect x="2" y="7" width="20" height="5"></rect><line x1="12" y1="22" x2="12" y2="7"></line><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"></path><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"></path>'
I_SCALE = '<path d="M12 3v18"></path><path d="M5 7h14"></path><path d="M5 7l-3 6a3 3 0 0 0 6 0z"></path><path d="M19 7l-3 6a3 3 0 0 0 6 0z"></path><path d="M8 21h8"></path>'
I_COMPASS = '<circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon>'
I_SLIDERS = '<line x1="4" y1="21" x2="4" y2="14"></line><line x1="4" y1="10" x2="4" y2="3"></line><line x1="12" y1="21" x2="12" y2="12"></line><line x1="12" y1="8" x2="12" y2="3"></line><line x1="20" y1="21" x2="20" y2="16"></line><line x1="20" y1="12" x2="20" y2="3"></line><line x1="1" y1="14" x2="7" y2="14"></line><line x1="9" y1="8" x2="15" y2="8"></line><line x1="17" y1="16" x2="23" y2="16"></line>'
I_ZAP = '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>'
I_CLIPBOARD = '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect><path d="M9 14l2 2 4-4"></path>'
I_SHARE = '<circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line>'
I_LIST = '<line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line>'
I_LINK = '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>'
I_MSG = '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>'
I_CARD = '<rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line>'

V = [
    dict(id=2969994, lang="fr", htmllang="fr", pt="WP Grid Builder perf - Hero FR", tf=84, vf=84,
        p1="WP Grid Builder", p2="Guide", icon=I_GAUGE, vh="L'essentiel",
        lines=["Grid Builder", "et la <em>perf</em>"],
        base="Comment optimiser WP Grid Builder pour soigner tes Core Web Vitals : chargement, requêtes et rendu, sans sacrifier le design.",
        vn="La perf", vs="WP Grid Builder et les Core Web Vitals",
        stats=[("Type", "Guide"), ("Objectif", "Core Web Vitals"), ("Niveau", "Intermédiaire"), ("Idéal pour", "Sites rapides")],
        foot="Du design, sans ralentir ton site"),
    dict(id=2969990, lang="fr", htmllang="fr", pt="Alternative WP Grid Builder - Hero FR", tf=72, vf=64,
        p1="WP Grid Builder", p2="Alternatives", icon=I_SHUFFLE, vh="L'essentiel",
        lines=["L'alternative", "à <em>Grid Builder</em>"],
        base="Quelle alternative à WP Grid Builder choisir pour afficher tes contenus en grilles et en filtres : les meilleures options comparées.",
        vn="L'alternative", vs="remplacer WP Grid Builder sereinement",
        stats=[("Type", "Comparatif"), ("Sujet", "Grilles &amp; filtres"), ("Critère", "Perf &amp; prix"), ("Idéal pour", "Changer d'outil")],
        foot="Le bon outil de grilles pour ton site"),
    dict(id=2969989, lang="fr", htmllang="fr", pt="FluentKit - Hero FR", tf=84, vf=92,
        p1="FluentKit", p2="Avis", icon=I_GRID, vh="L'essentiel",
        lines=["FluentKit,", "le <em>hub</em>"],
        base="Le hub central pour gérer et connecter tes plugins WordPress depuis un seul tableau de bord, signé l'écosystème Fluent.",
        vn="Le hub", vs="gérer tes plugins depuis un seul endroit",
        stats=[("Type", "Hub plugins"), ("Force", "Tout centralisé"), ("Atout", "Tableau de bord unique"), ("Idéal pour", "Power users")],
        foot="Tes plugins, réunis au même endroit"),
    dict(id=2969501, lang="fr", htmllang="fr", pt="Dropshipping WooCommerce - Hero FR", tf=80, vf=56,
        p1="WooCommerce", p2="Guide", icon=I_TRUCK, vh="L'essentiel",
        lines=["Réussir ton", "<em>dropshipping</em>"],
        base="Le guide expert pour lancer et réussir ton activité de dropshipping avec WooCommerce : fournisseurs, automatisation et marges.",
        vn="Le dropshipping", vs="lancer ta boutique dropshipping sur WooCommerce",
        stats=[("Type", "Guide expert"), ("Plateforme", "WooCommerce"), ("Sujet", "Fournisseurs &amp; marges"), ("Idéal pour", "E-commerçants")],
        foot="Ta boutique sans gérer de stock"),
    dict(id=2969375, lang="fr", htmllang="fr", pt="SureDash vs Fluent Community - Hero FR", tf=66, vf=72,
        p1="SureDash vs FC", p2="Comparatif", icon=I_COMPARE, vh="L'essentiel",
        lines=["SureDash vs", "Fluent <em>Community</em>"],
        base="SureDash ou Fluent Community : le comparatif pour choisir la meilleure plateforme communautaire et de cours pour ton site WordPress.",
        vn="Face à face", vs="choisir ta plateforme communautaire WP",
        stats=[("Type", "Comparatif"), ("Catégorie", "Communauté &amp; cours"), ("Face à face", "2 plugins"), ("Idéal pour", "Créateurs")],
        foot="La bonne plateforme communautaire"),
    dict(id=2968090, lang="en", htmllang="en", pt="Tutor LMS Coupon - Hero EN", tf=88, vf=84,
        p1="Tutor LMS", p2="Coupon", icon=I_GIFT, vh="The essentials",
        lines=["Tutor LMS,", "the <em>deal</em>"],
        base="Get Tutor LMS at a reduced price with the schoolsWP coupon, and launch your online school on WordPress for less.",
        vn="The deal", vs="Tutor LMS at a better price",
        stats=[("Type", "Coupon"), ("Product", "Tutor LMS"), ("Goal", "Online school"), ("Best for", "Course creators")],
        foot="Launch your online school for less"),
    dict(id=2967212, lang="fr", htmllang="fr", pt="FluentCart vs WooCommerce - Hero FR", tf=68, vf=60,
        p1="FluentCart vs Woo", p2="Comparatif", icon=I_SCALE, vh="L'essentiel",
        lines=["FluentCart vs", "<em>WooCommerce</em>"],
        base="FluentCart ou WooCommerce pour vendre sur WordPress : le comparatif des deux solutions e-commerce pour faire le bon choix.",
        vn="Lequel choisir", vs="vendre sur WordPress, le bon choix",
        stats=[("Type", "Comparatif"), ("Catégorie", "E-commerce"), ("Face à face", "2 solutions"), ("Idéal pour", "Vendre sur WP")],
        foot="La bonne solution pour vendre en ligne"),
    dict(id=2967654, lang="fr", htmllang="fr", pt="Rigueur SEO - Hero FR", tf=80, vf=76,
        p1="SEO", p2="Méthode", icon=I_COMPASS, vh="L'essentiel",
        lines=["La rigueur,", "clé du <em>SEO</em>"],
        base="Pourquoi la rigueur et la régularité font la différence en SEO : la méthode qui paie vraiment pour grimper durablement.",
        vn="La rigueur", vs="la méthode SEO qui paie vraiment",
        stats=[("Type", "Méthode"), ("Sujet", "SEO durable"), ("Clé", "Régularité"), ("Idéal pour", "Le long terme")],
        foot="Le SEO récompense la constance"),
    dict(id=2967240, lang="fr", htmllang="fr", pt="Code promo Tutor LMS - Hero FR", tf=80, vf=72,
        p1="Tutor LMS", p2="Code promo", icon=I_GIFT, vh="L'essentiel",
        lines=["Tutor LMS,", "le <em>bon plan</em>"],
        base="Profite de Tutor LMS à prix réduit avec le code promo schoolsWP, et lance ton école en ligne sur WordPress pour moins cher.",
        vn="Le bon plan", vs="Tutor LMS à prix réduit",
        stats=[("Type", "Code promo"), ("Produit", "Tutor LMS"), ("Objectif", "École en ligne"), ("Idéal pour", "Formateurs")],
        foot="Lance ton école en ligne, moins cher"),
    dict(id=2592792, lang="fr", htmllang="fr", pt="Divi Pixel - Hero FR", tf=84, vf=80,
        p1="Divi Pixel", p2="Avis", icon=I_SLIDERS, vh="L'essentiel",
        lines=["Divi Pixel,", "le <em>design</em>"],
        base="Divi Pixel ajoute des dizaines de modules et d'options de design à Divi, pour pousser ton thème encore plus loin.",
        vn="Pour Divi", vs="des modules de design en plus pour Divi",
        stats=[("Type", "Addon Divi"), ("Force", "Modules de design"), ("Atout", "Sans coder"), ("Idéal pour", "Utilisateurs Divi")],
        foot="Ton thème Divi, sans limites"),
    dict(id=2592797, lang="fr", htmllang="fr", pt="OttoKit automation - Hero FR", tf=76, vf=52,
        p1="OttoKit", p2="Guide", icon=I_ZAP, vh="L'essentiel",
        lines=["OttoKit,", "l'<em>automatisation</em>"],
        base="Comment connecter tes applications et automatiser tes tâches WordPress avec OttoKit, l'outil no-code ex-SureTriggers.",
        vn="L'automatisation", vs="connecter tes apps sans coder",
        stats=[("Type", "Automatisation"), ("Force", "No-code"), ("Atout", "Multi-apps"), ("Idéal pour", "Gagner du temps")],
        foot="Tes tâches tournent toutes seules"),
    dict(id=2592796, lang="fr", htmllang="fr", pt="GemBoards - Hero FR", tf=84, vf=72,
        p1="GemBoards", p2="Avis", icon=I_CLIPBOARD, vh="L'essentiel",
        lines=["GemBoards,", "tes <em>projets</em>"],
        base="Gère tes projets WordPress directement dans ton tableau de bord avec GemBoards : tableaux, tâches et suivi d'équipe.",
        vn="Tes projets", vs="la gestion de projet dans WordPress",
        stats=[("Type", "Gestion de projet"), ("Force", "Tableaux &amp; tâches"), ("Atout", "Dans WordPress"), ("Idéal pour", "Équipes")],
        foot="Tes projets, pilotés dans WordPress"),
    dict(id=2289922, lang="fr", htmllang="fr", pt="FluentAffiliate - Hero FR", tf=68, vf=64,
        p1="FluentAffiliate", p2="Avis", icon=I_SHARE, vh="L'essentiel",
        lines=["FluentAffiliate,", "ton <em>affiliation</em>"],
        base="Gère ton propre programme d'affiliation directement dans WordPress avec FluentAffiliate : affiliés, commissions et suivi.",
        vn="L'affiliation", vs="ton programme d'affiliation dans WordPress",
        stats=[("Type", "Affiliation"), ("Force", "Affiliés &amp; commissions"), ("Atout", "Tout dans WP"), ("Idéal pour", "Vendeurs &amp; SaaS")],
        foot="Ton programme d'affiliation maison"),
    dict(id=2538716, lang="fr", htmllang="fr", pt="FluentCRM vs SureContact - Hero FR", tf=88, vf=68,
        p1="4 outils, 0 confusion", p2="Guide", icon=I_LIST, vh="L'essentiel",
        lines=["4 outils,", "<em>démêlés</em>"],
        base="FluentCRM, SureContact, SureCart, FluentCart : le guide clair pour ne plus confondre ces 4 outils et choisir le bon.",
        vn="Les 4 outils", vs="ne plus confondre CRM, mailing et e-commerce",
        stats=[("Type", "Guide"), ("Sujet", "CRM &amp; e-commerce"), ("Outils", "4 comparés"), ("Idéal pour", "Y voir clair")],
        foot="Le bon outil, sans confusion"),
    dict(id=2289944, lang="fr", htmllang="fr", pt="AI Link Genius - Hero FR", tf=72, vf=72,
        p1="AI Link Genius", p2="Avis", icon=I_LINK, vh="L'essentiel",
        lines=["Le maillage", "interne par <em>IA</em>"],
        base="Automatise ton maillage interne WordPress avec AI Link Genius : l'IA suggère et pose les liens pour booster ton SEO.",
        vn="Le maillage", vs="tes liens internes générés par IA",
        stats=[("Type", "Maillage interne"), ("Force", "Liens par IA"), ("Atout", "Gain de temps SEO"), ("Idéal pour", "Blogs &amp; contenus")],
        foot="Tes liens internes, sans effort"),
    dict(id=2289936, lang="fr", htmllang="fr", pt="Reclamations clients - Hero FR", tf=76, vf=52,
        p1="Service client", p2="Guide", icon=I_MSG, vh="L'essentiel",
        lines=["Gérer les", "<em>réclamations</em>"],
        base="Comment organiser la gestion des réclamations clients sur WordPress : centraliser, suivre et résoudre sans rien laisser passer.",
        vn="Les réclamations", vs="traiter les plaintes clients sur WordPress",
        stats=[("Type", "Guide"), ("Objectif", "SAV maîtrisé"), ("Sujet", "Réclamations"), ("Idéal pour", "Boutiques &amp; services")],
        foot="Aucun client laissé sans réponse"),
    dict(id=2289935, lang="fr", htmllang="fr", pt="Paystack FluentCart - Hero FR", tf=76, vf=84,
        p1="FluentCart + Paystack", p2="Guide", icon=I_CARD, vh="L'essentiel",
        lines=["Paystack sur", "<em>FluentCart</em>"],
        base="Comment installer Paystack sur FluentCart pour encaisser tes paiements dans WordPress, idéal pour vendre en Afrique.",
        vn="Paystack", vs="encaisser en Afrique avec FluentCart",
        stats=[("Type", "Guide"), ("Sujet", "Paiements Paystack"), ("Plateforme", "FluentCart"), ("Idéal pour", "Vendre en Afrique")],
        foot="Encaisse tes clients en Afrique"),
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
