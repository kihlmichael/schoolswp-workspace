"""Generate heros for the hosting/domain batch (verdict-block + compare-head)."""

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

I_GLOBE = '<circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>'
I_SERVER = '<rect x="2" y="2" width="20" height="8" rx="2"></rect><rect x="2" y="14" width="20" height="8" rx="2"></rect><line x1="6" y1="6" x2="6.01" y2="6"></line><line x1="6" y1="18" x2="6.01" y2="18"></line>'
I_TAG = '<path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path><line x1="7" y1="7" x2="7.01" y2="7"></line>'
I_BOX = '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line>'
I_CLOUD = '<path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"></path>'
I_ZAP = '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>'
I_SWAP = '<path d="M16 3l4 4-4 4"></path><path d="M20 7H4"></path><path d="M8 21l-4-4 4-4"></path><path d="M4 17h16"></path>'
I_LIFEBUOY = '<circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="4"></circle><line x1="4.93" y1="4.93" x2="9.17" y2="9.17"></line><line x1="14.83" y1="14.83" x2="19.07" y2="19.07"></line><line x1="14.83" y1="9.17" x2="19.07" y2="4.93"></line><line x1="4.93" y1="19.07" x2="9.17" y2="14.83"></line>'

V = []
C = []

# Netim FR
V.append(dict(id=2289949, lang="fr", htmllang="fr", pt="Netim - Hero FR", tf=88, vf=80,
    p1="Netim", p2="Avis", icon=I_GLOBE, vh="L'essentiel",
    lines=["Netim,", "le <em>domaine</em>"],
    base="Le registrar français pour gérer tes noms de domaine : extensions variées, interface pro et support expert.",
    vn="Le domaine", vs="ton nom de domaine chez un registrar FR",
    stats=[("Type", "Registrar"), ("Origine", "Français"), ("Force", "Expertise domaine"), ("Idéal pour", "Gérer tes domaines")],
    foot="Tes noms de domaine entre de bonnes mains"))

# LWS FR
V.append(dict(id=2289791, lang="fr", htmllang="fr", pt="LWS - Hero FR", tf=88, vf=84,
    p1="LWS", p2="Avis", icon=I_SERVER, vh="L'essentiel",
    lines=["LWS,", "<em>accessible</em>"],
    base="L'hébergeur web français au tarif abordable : nom de domaine, e-mails et hébergement WordPress pour bien démarrer.",
    vn="Accessible", vs="l'hébergement web français abordable",
    stats=[("Type", "Hébergeur web"), ("Origine", "Français"), ("Force", "Bon rapport prix"), ("Idéal pour", "Petits budgets")],
    foot="Démarrer sans se ruiner"))

# Rapyd promo FR / EN / DE -- evergreen (no %, no code, no date)
V.append(dict(id=59494, lang="fr", htmllang="fr", pt="Code promo Rapyd Cloud - Hero FR", tf=80, vf=84,
    p1="Rapyd Cloud", p2="Code promo", icon=I_TAG, vh="L'essentiel",
    lines=["Rapyd Cloud,", "la <em>remise</em>"],
    base="Mon code promo pour Rapyd Cloud : profite de l'hébergement WordPress infogéré à prix réduit, en quelques clics.",
    vn="La remise", vs="économiser sur Rapyd Cloud",
    stats=[("Type", "Code promo"), ("Pour", "Rapyd Cloud"), ("Avantage", "Prix réduit"), ("Idéal pour", "Te lancer malin")],
    foot="L'hébergement perf, moins cher"))
V.append(dict(id=59551, lang="en", htmllang="en", pt="Rapyd Cloud coupon - Hero EN", tf=80, vf=72,
    p1="Rapyd Cloud", p2="Coupon", icon=I_TAG, vh="The essentials",
    lines=["Rapyd Cloud,", "the <em>discount</em>"],
    base="My coupon code for Rapyd Cloud: get managed WordPress cloud hosting at a lower price, in a few clicks.",
    vn="The discount", vs="save on Rapyd Cloud",
    stats=[("Type", "Coupon code"), ("For", "Rapyd Cloud"), ("Perk", "Lower price"), ("Best for", "Starting smart")],
    foot="Performance hosting, for less"))
V.append(dict(id=59570, lang="de", htmllang="de", pt="Rapyd Cloud Gutschein - Hero DE", tf=80, vf=84,
    p1="Rapyd Cloud", p2="Gutschein", icon=I_TAG, vh="Das Wichtigste",
    lines=["Rapyd Cloud,", "der <em>Rabatt</em>"],
    base="Mein Gutscheincode für Rapyd Cloud: hol dir managed WordPress-Cloud-Hosting zum besten Preis, in wenigen Klicks.",
    vn="Der Rabatt", vs="bei Rapyd Cloud sparen",
    stats=[("Typ", "Gutscheincode"), ("Für", "Rapyd Cloud"), ("Vorteil", "Günstiger Preis"), ("Ideal für", "Clever starten")],
    foot="Performance-Hosting, günstiger"))

# o2switch FR / EN / DE
V.append(dict(id=59256, lang="fr", htmllang="fr", pt="o2switch - Hero FR", tf=84, vf=78,
    p1="o2switch", p2="Avis", icon=I_BOX, vh="L'essentiel",
    lines=["o2switch,", "<em>tout</em> compris"],
    base="L'hébergeur français connu pour son offre unique tout illimité : ressources, sites et accompagnement, sans surcouche.",
    vn="Tout compris", vs="l'offre unique tout illimité",
    stats=[("Type", "Hébergeur web"), ("Origine", "Français"), ("Force", "Offre illimitée"), ("Idéal pour", "Sites multiples")],
    foot="Une seule offre, tout dedans"))
V.append(dict(id=59434, lang="en", htmllang="en", pt="o2switch - Hero EN", tf=88, vf=92,
    p1="o2switch", p2="Review", icon=I_BOX, vh="The essentials",
    lines=["o2switch,", "<em>all</em>-in"],
    base="The French host known for its single unlimited plan: resources, sites and support, all included.",
    vn="All-in", vs="one unlimited all-in plan",
    stats=[("Type", "Web host"), ("Origin", "French"), ("Strength", "Unlimited plan"), ("Best for", "Multiple sites")],
    foot="One plan, everything in it"))
V.append(dict(id=59420, lang="de", htmllang="de", pt="o2switch - Hero DE", tf=84, vf=84,
    p1="o2switch", p2="Test", icon=I_BOX, vh="Das Wichtigste",
    lines=["o2switch,", "<em>alles</em> drin"],
    base="Der französische Host mit seinem einzigen unbegrenzten Tarif: Ressourcen, Sites und Support, alles inklusive.",
    vn="Alles drin", vs="ein unbegrenzter Tarif, alles drin",
    stats=[("Typ", "Webhost"), ("Herkunft", "Französisch"), ("Stärke", "Unbegrenzter Tarif"), ("Ideal für", "Mehrere Sites")],
    foot="Ein Tarif, alles dabei"))

# Rapyd Cloud avis FR / EN / DE
V.append(dict(id=57810, lang="fr", htmllang="fr", pt="Rapyd Cloud - Hero FR", tf=84, vf=88,
    p1="Rapyd Cloud", p2="Avis", icon=I_CLOUD, vh="L'essentiel",
    lines=["Rapyd Cloud,", "le <em>cloud</em>"],
    base="L'hébergement WordPress infogéré sur cloud haute performance : vitesse, scalabilité et zéro maintenance serveur.",
    vn="Le cloud", vs="l'hébergement WordPress infogéré",
    stats=[("Type", "Cloud infogéré"), ("Force", "Performance"), ("Atout", "Zéro maintenance"), ("Idéal pour", "Sites exigeants")],
    foot="La vitesse, sans gérer le serveur"))
V.append(dict(id=58610, lang="en", htmllang="en", pt="Rapyd Cloud - Hero EN", tf=84, vf=92,
    p1="Rapyd Cloud", p2="Review", icon=I_CLOUD, vh="The essentials",
    lines=["Rapyd Cloud,", "the <em>cloud</em>"],
    base="Managed WordPress hosting on high-performance cloud: speed, scalability and zero server maintenance.",
    vn="Cloud", vs="managed high-performance WordPress hosting",
    stats=[("Type", "Managed cloud"), ("Strength", "Performance"), ("Plus", "Zero maintenance"), ("Best for", "Demanding sites")],
    foot="Speed, without managing the server"))
V.append(dict(id=58598, lang="de", htmllang="de", pt="Rapyd Cloud - Hero DE", tf=84, vf=92,
    p1="Rapyd Cloud", p2="Test", icon=I_CLOUD, vh="Das Wichtigste",
    lines=["Rapyd Cloud,", "die <em>Cloud</em>"],
    base="Managed WordPress-Hosting auf Hochleistungs-Cloud: Geschwindigkeit, Skalierbarkeit und null Server-Wartung.",
    vn="Cloud", vs="managed WordPress-Hosting in der Cloud",
    stats=[("Typ", "Managed Cloud"), ("Stärke", "Performance"), ("Plus", "Null Wartung"), ("Ideal für", "Anspruchsvolle Sites")],
    foot="Speed, ohne Server-Verwaltung"))

# Copilhost FR / EN / DE
V.append(dict(id=53666, lang="fr", htmllang="fr", pt="Copilhost - Hero FR", tf=88, vf=88,
    p1="Copilhost", p2="Avis", icon=I_ZAP, vh="L'essentiel",
    lines=["Copilhost,", "<em>rapide</em>"],
    base="L'hébergeur WordPress français qui mise sur la vitesse et la sécurité : serveurs optimisés et protection incluse.",
    vn="Rapide", vs="hébergement WordPress rapide et sûr",
    stats=[("Type", "Hébergeur WP"), ("Origine", "Français"), ("Force", "Vitesse &amp; sécurité"), ("Idéal pour", "Sites WordPress")],
    foot="Rapide et protégé, par défaut"))
V.append(dict(id=53811, lang="en", htmllang="en", pt="Copilhost - Hero EN", tf=88, vf=96,
    p1="Copilhost", p2="Review", icon=I_ZAP, vh="The essentials",
    lines=["Copilhost,", "<em>fast</em>"],
    base="The French WordPress host built around speed and security: optimized servers and protection included.",
    vn="Fast", vs="fast and secure WordPress hosting",
    stats=[("Type", "WP host"), ("Origin", "French"), ("Strength", "Speed &amp; security"), ("Best for", "WordPress sites")],
    foot="Fast and protected, by default"))
V.append(dict(id=53810, lang="de", htmllang="de", pt="Copilhost - Hero DE", tf=88, vf=92,
    p1="Copilhost", p2="Test", icon=I_ZAP, vh="Das Wichtigste",
    lines=["Copilhost,", "<em>schnell</em>"],
    base="Der französische WordPress-Host mit Fokus auf Tempo und Sicherheit: optimierte Server und Schutz inklusive.",
    vn="Schnell", vs="schnelles und sicheres WordPress-Hosting",
    stats=[("Typ", "WP-Host"), ("Herkunft", "Französisch"), ("Stärke", "Tempo &amp; Sicherheit"), ("Ideal für", "WordPress-Sites")],
    foot="Schnell und geschützt, von Haus aus"))

# EasyHoster FR / EN / DE -- hosts schoolswp.com
V.append(dict(id=4854, lang="fr", htmllang="fr", pt="EasyHoster - Hero FR", tf=84, vf=84,
    p1="EasyHoster", p2="Avis", icon=I_LIFEBUOY, vh="L'essentiel",
    lines=["EasyHoster,", "le <em>support</em>"],
    base="L'hébergement WordPress français reconnu pour son accompagnement : sauvegardes, sécurité et un support qui répond.",
    vn="Le support", vs="l'hébergeur français qui t'accompagne",
    stats=[("Type", "Hébergeur WP"), ("Origine", "Français"), ("Force", "Accompagnement"), ("Idéal pour", "Être bien suivi")],
    foot="Un vrai support, en français"))
V.append(dict(id=739366, lang="en", htmllang="en", pt="EasyHoster - Hero EN", tf=80, vf=92,
    p1="EasyHoster", p2="Review", icon=I_LIFEBUOY, vh="The essentials",
    lines=["EasyHoster,", "the <em>support</em>"],
    base="The French WordPress host known for its hands-on support: backups, security and a team that actually answers.",
    vn="Support", vs="the French host that supports you",
    stats=[("Type", "WP host"), ("Origin", "French"), ("Strength", "Hands-on support"), ("Best for", "Being well supported")],
    foot="Real support, that answers"))
V.append(dict(id=739385, lang="de", htmllang="de", pt="EasyHoster - Hero DE", tf=80, vf=92,
    p1="EasyHoster", p2="Test", icon=I_LIFEBUOY, vh="Das Wichtigste",
    lines=["EasyHoster,", "der <em>Support</em>"],
    base="Der französische WordPress-Host, bekannt für seinen Support: Backups, Sicherheit und ein Team, das wirklich antwortet.",
    vn="Support", vs="der französische Host, der dich begleitet",
    stats=[("Typ", "WP-Host"), ("Herkunft", "Französisch"), ("Stärke", "Persönlicher Support"), ("Ideal für", "Gut betreut sein")],
    foot="Echter Support, der antwortet"))

# WordPress.com vs .org compare FR / EN / DE
C.append(dict(id=53488, lang="fr", htmllang="fr", pt="WordPress.com vs .org - Hero FR", tf=118,
    p1="WordPress.com vs .org", p2="Comparatif", icon=I_SWAP, vh="Le comparatif",
    lines=[".com ou", "<em>.org</em>&nbsp;?"],
    base="WordPress.com clé en main ou WordPress.org en autonomie totale ? Le comparatif pour faire le bon choix.",
    chl=("WordPress.com", "Clé en main"), chr=("WordPress.org", "Liberté totale"),
    crows=[("Inclus", "Hébergement", "À toi de gérer"), ("Simplicité", "Force", "Contrôle total"),
           ("Limitée", "Personnalisation", "Illimitée"), ("Débutants", "Idéal pour", "Pros &amp; makers")],
    foot="Clé en main ou liberté totale ? Au cas par cas"))
C.append(dict(id=722922, lang="en", htmllang="en", pt="WordPress.com vs .org - Hero EN", tf=118,
    p1="WordPress.com vs .org", p2="Comparison", icon=I_SWAP, vh="The comparison",
    lines=[".com or", "<em>.org</em>?"],
    base="WordPress.com turnkey or WordPress.org in full autonomy? The comparison to make the right call.",
    chl=("WordPress.com", "Turnkey"), chr=("WordPress.org", "Full freedom"),
    crows=[("Included", "Hosting", "You manage it"), ("Simplicity", "Strength", "Full control"),
           ("Limited", "Customization", "Unlimited"), ("Beginners", "Best for", "Pros &amp; makers")],
    foot="Turnkey or full freedom? Case by case"))
C.append(dict(id=739173, lang="de", htmllang="de", pt="WordPress.org vs .com - Hero DE", tf=110,
    p1="WordPress.org vs .com", p2="Vergleich", icon=I_SWAP, vh="Der Vergleich",
    lines=[".org oder", "<em>.com</em>?"],
    base="WordPress.org in voller Autonomie oder WordPress.com schlüsselfertig? Der Vergleich für die richtige Wahl.",
    chl=("WordPress.org", "Volle Freiheit"), chr=("WordPress.com", "Schlüsselfertig"),
    crows=[("Du verwaltest", "Hosting", "Inklusive"), ("Volle Kontrolle", "Stärke", "Einfachheit"),
           ("Unbegrenzt", "Anpassung", "Begrenzt"), ("Profis &amp; Maker", "Ideal für", "Einsteiger")],
    foot="Schlüsselfertig oder volle Freiheit? Je nachdem"))


def vbody(h):
    rows = "\n".join(
        f'            <div class="stat"><span class="stat-key">{k}</span><span class="stat-val">{v}</span></div>'
        for k, v in h["stats"]
    )
    return (
        '          <div class="verdict-block">\n'
        f'            <div class="verdict-num">{h["vn"]}</div>\n'
        f'            <div class="verdict-sub">{h["vs"]}</div>\n'
        "          </div>\n"
        '          <div class="stats">\n'
        f"{rows}\n"
        "          </div>"
    )


def cbody(h):
    rows = "\n".join(
        f'              <div class="crow"><div class="cv">{l}</div><div class="caxis">{a}</div><div class="cv">{r}</div></div>'
        for l, a, r in h["crows"]
    )
    return (
        '          <div class="cmp">\n'
        '            <div class="compare-head">\n'
        f'              <div class="ch-col"><div class="ch-name">{h["chl"][0]}</div><div class="ch-tag">{h["chl"][1]}</div></div>\n'
        '              <div class="ch-vs">vs</div>\n'
        f'              <div class="ch-col"><div class="ch-name">{h["chr"][0]}</div><div class="ch-tag">{h["chr"][1]}</div></div>\n'
        "            </div>\n"
        '            <div class="compare">\n'
        f"{rows}\n"
        "            </div>\n"
        "          </div>"
    )


def fill(html, h):
    html = html.replace("@@HTMLLANG@@", h["htmllang"])
    html = html.replace("@@PAGETITLE@@", h["pt"])
    html = html.replace("@@TITLEFONT@@", str(h["tf"]))
    html = html.replace("@@PILL1@@", h["p1"])
    html = html.replace("@@PILL2@@", h["p2"])
    html = html.replace("@@TITLELINES@@", "".join(f"<span>{x}</span>" for x in h["lines"]))
    html = html.replace("@@BASELINE@@", h["base"])
    html = html.replace("@@ICON@@", h["icon"])
    html = html.replace("@@VHEADER@@", h["vh"])
    html = html.replace("@@FOOTER@@", h["foot"])
    return html


def render_v(h):
    html = HEAD.replace("@@EXTRACSS@@", VCSS.replace("@@VERDICTFONT@@", str(h["vf"])))
    html = html.replace("@@BODY@@", vbody(h))
    return fill(html, h)


def render_c(h):
    html = HEAD.replace("@@EXTRACSS@@", CCSS)
    html = html.replace("@@BODY@@", cbody(h))
    return fill(html, h)


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
print("Generated", count, "hero HTML files")
for h in V + C:
    print(f"  post-{h['id']}/slide-00-hero-{h['lang']}.html")
