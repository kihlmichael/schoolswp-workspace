"""Generate heros for the SureForms / MailerPress batch (verdict-block, FR+EN+DE)."""

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

I_DB = '<ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>'
I_MAIL = '<rect x="2" y="4" width="20" height="16" rx="2"></rect><path d="m22 7-10 5L2 7"></path>'
I_REFRESH = '<path d="M23 4v6h-6"></path><path d="M1 20v-6h6"></path><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10"></path><path d="M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path>'

V = [
    # SureForms FR / EN / DE -- local storage
    dict(id=2228904, lang="fr", htmllang="fr", pt="SureForms - Hero FR", tf=84, vf=88,
        p1="SureForms", p2="Formulaires", icon=I_DB, vh="L'essentiel",
        lines=["SureForms,", "en <em>local</em>"],
        base="Le plugin de formulaires qui stocke 100% des réponses sur ton propre site, sans passer par un service externe.",
        vn="En local", vs="stocker les réponses sur ton site",
        stats=[("Type", "Formulaires"), ("Force", "Stockage local"), ("Atout", "Respect des données"), ("Idéal pour", "Données sensibles")],
        foot="Tes formulaires, tes données, ton serveur"),
    dict(id=2289526, lang="en", htmllang="en", pt="SureForms - Hero EN", tf=84, vf=92,
        p1="SureForms", p2="Forms", icon=I_DB, vh="The essentials",
        lines=["SureForms,", "stays <em>local</em>"],
        base="The form plugin that stores 100% of your entries on your own site, with no external service in the loop.",
        vn="Local", vs="store form entries on your own site",
        stats=[("Type", "Forms"), ("Strength", "Local storage"), ("Plus", "Privacy-friendly"), ("Best for", "Sensitive data")],
        foot="Your forms, your data, your server"),
    dict(id=2289527, lang="de", htmllang="de", pt="SureForms - Hero DE", tf=80, vf=88,
        p1="SureForms", p2="Formulare", icon=I_DB, vh="Das Wichtigste",
        lines=["SureForms,", "<em>lokal</em> gespeichert"],
        base="Das Formular-Plugin, das 100% deiner Einträge auf deiner eigenen Site speichert, ganz ohne externen Dienst.",
        vn="Lokal", vs="Formulardaten auf deiner Site speichern",
        stats=[("Typ", "Formulare"), ("Stärke", "Lokale Speicherung"), ("Plus", "Datenschutzfreundlich"), ("Ideal für", "Sensible Daten")],
        foot="Deine Formulare, deine Daten, dein Server"),
    # MailerPress FR / EN / DE -- newsletter plugin
    dict(id=2084435, lang="fr", htmllang="fr", pt="MailerPress - Hero FR", tf=80, vf=80,
        p1="MailerPress", p2="Avis", icon=I_MAIL, vh="L'essentiel",
        lines=["MailerPress,", "l'<em>emailing</em> WP"],
        base="La solution d'emailing intégrée à WordPress : crée et envoie tes newsletters sans quitter ton tableau de bord.",
        vn="L'emailing", vs="la newsletter intégrée à WordPress",
        stats=[("Type", "Emailing"), ("Force", "Tout dans WP"), ("Atout", "Envois illimités"), ("Idéal pour", "Newsletters")],
        foot="Ta newsletter, sans quitter WordPress"),
    dict(id=2289539, lang="en", htmllang="en", pt="MailerPress - Hero EN", tf=84, vf=92,
        p1="MailerPress", p2="Review", icon=I_MAIL, vh="The essentials",
        lines=["MailerPress,", "WP <em>email</em>"],
        base="The email marketing solution built into WordPress: create and send your newsletters without leaving your dashboard.",
        vn="Email", vs="built-in newsletters for WordPress",
        stats=[("Type", "Email marketing"), ("Strength", "All inside WP"), ("Plus", "Unlimited sends"), ("Best for", "Newsletters")],
        foot="Your newsletter, right inside WordPress"),
    dict(id=2289538, lang="de", htmllang="de", pt="MailerPress - Hero DE", tf=80, vf=84,
        p1="MailerPress", p2="Test", icon=I_MAIL, vh="Das Wichtigste",
        lines=["MailerPress,", "<em>E-Mails</em> in WP"],
        base="Die E-Mail-Marketing-Lösung direkt in WordPress: erstelle und versende deine Newsletter ohne dein Dashboard zu verlassen.",
        vn="E-Mails", vs="Newsletter direkt in WordPress",
        stats=[("Typ", "E-Mail-Marketing"), ("Stärke", "Alles in WP"), ("Plus", "Unbegrenzte Sends"), ("Ideal für", "Newsletter")],
        foot="Dein Newsletter, direkt in WordPress"),
    # MailerPress update FR / EN / DE -- evergreen, NO version number
    dict(id=1796449, lang="fr", htmllang="fr", pt="MailerPress update - Hero FR", tf=80, vf=88,
        p1="MailerPress", p2="Mise à jour", icon=I_REFRESH, vh="L'essentiel",
        lines=["MailerPress,", "les <em>nouveautés</em>"],
        base="La mise à jour qui repense l'interface et ajoute les champs personnalisés : MailerPress passe un cap.",
        vn="Du neuf", vs="interface repensée et champs perso",
        stats=[("Type", "Mise à jour"), ("Au menu", "Nouvelle interface"), ("Aussi", "Champs perso"), ("Idéal pour", "Aller plus loin")],
        foot="Une nouvelle version, plus puissante"),
    dict(id=2085071, lang="en", htmllang="en", pt="MailerPress update - Hero EN", tf=80, vf=76,
        p1="MailerPress", p2="Update", icon=I_REFRESH, vh="The essentials",
        lines=["MailerPress,", "what's <em>new</em>"],
        base="The update that redesigns the interface and adds custom fields: MailerPress steps up its game.",
        vn="What's new", vs="redesigned interface and custom fields",
        stats=[("Type", "Update"), ("Highlight", "New interface"), ("Also", "Custom fields"), ("Best for", "Going further")],
        foot="A new version, more powerful"),
    dict(id=2085544, lang="de", htmllang="de", pt="MailerPress update - Hero DE", tf=80, vf=92,
        p1="MailerPress", p2="Update", icon=I_REFRESH, vh="Das Wichtigste",
        lines=["MailerPress,", "das <em>Update</em>"],
        base="Das Update mit neu gestalteter Oberfläche und eigenen Feldern: MailerPress legt nochmal zu.",
        vn="Neu", vs="neue Oberfläche und eigene Felder",
        stats=[("Typ", "Update"), ("Highlight", "Neue Oberfläche"), ("Auch", "Eigene Felder"), ("Ideal für", "Mehr rausholen")],
        foot="Eine neue Version, noch stärker"),
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
