"""Generate heros for the FluentSMTP / FluentCRM promo batch (verdict-block)."""

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

I_MAILCHECK = '<path d="M22 13V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h8"></path><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path><path d="m16 19 2 2 4-4"></path>'
I_TAG = '<path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path><line x1="7" y1="7" x2="7.01" y2="7"></line>'

V = [
    # FluentSMTP FR / EN / DE(draft) -- free SMTP, deliverability
    dict(id=377897, lang="fr", htmllang="fr", pt="FluentSMTP - Hero FR", tf=84, vf=84,
        p1="FluentSMTP", p2="Avis", icon=I_MAILCHECK, vh="L'essentiel",
        lines=["FluentSMTP,", "bien <em>livré</em>"],
        base="Le plugin SMTP gratuit qui fiabilise l'envoi de tes e-mails WordPress : connexion à n'importe quel service, suivi des envois.",
        vn="Bien livré", vs="tes e-mails arrivent à destination",
        stats=[("Type", "Plugin SMTP"), ("Prix", "Gratuit"), ("Force", "Délivrabilité"), ("Idéal pour", "Tous les sites")],
        foot="Fini les e-mails qui finissent en spam"),
    dict(id=722591, lang="en", htmllang="en", pt="FluentSMTP - Hero EN", tf=84, vf=88,
        p1="FluentSMTP", p2="Review", icon=I_MAILCHECK, vh="The essentials",
        lines=["FluentSMTP,", "<em>delivered</em>"],
        base="The free SMTP plugin that makes your WordPress emails reliable: connect any service, track every send.",
        vn="Delivered", vs="your emails actually reach the inbox",
        stats=[("Type", "SMTP plugin"), ("Price", "Free"), ("Strength", "Deliverability"), ("Best for", "Every site")],
        foot="No more emails landing in spam"),
    dict(id=1168409, lang="de", htmllang="de", pt="FluentSMTP - Hero DE", tf=84, vf=84,
        p1="FluentSMTP", p2="Test", icon=I_MAILCHECK, vh="Das Wichtigste",
        lines=["FluentSMTP,", "<em>zugestellt</em>"],
        base="Das kostenlose SMTP-Plugin, das deine WordPress-E-Mails zuverlässig macht: jeder Dienst, jeder Versand im Blick.",
        vn="Zugestellt", vs="deine E-Mails landen im Posteingang",
        stats=[("Typ", "SMTP-Plugin"), ("Preis", "Kostenlos"), ("Stärke", "Zustellbarkeit"), ("Ideal für", "Jede Site")],
        foot="Schluss mit E-Mails im Spam"),
    # FluentCRM promo FR / EN / DE -- evergreen: no %, no code, no date
    dict(id=59328, lang="fr", htmllang="fr", pt="Code promo FluentCRM - Hero FR", tf=88, vf=76,
        p1="FluentCRM", p2="Code promo", icon=I_TAG, vh="L'essentiel",
        lines=["FluentCRM,", "le <em>bon plan</em>"],
        base="Mon code promo pour FluentCRM : profite de mon CRM WordPress préféré au meilleur prix, en quelques clics.",
        vn="Le bon plan", vs="économiser sur FluentCRM",
        stats=[("Type", "Code promo"), ("Pour", "FluentCRM Pro"), ("Avantage", "Prix réduit"), ("Idéal pour", "Te lancer malin")],
        foot="Mon CRM WordPress préféré, moins cher"),
    dict(id=59402, lang="en", htmllang="en", pt="Coupon code FluentCRM - Hero EN", tf=88, vf=88,
        p1="FluentCRM", p2="Coupon", icon=I_TAG, vh="The essentials",
        lines=["FluentCRM,", "the <em>deal</em>"],
        base="My coupon code for FluentCRM: get my favorite WordPress CRM at the best price, in just a few clicks.",
        vn="The deal", vs="save on FluentCRM",
        stats=[("Type", "Coupon code"), ("For", "FluentCRM Pro"), ("Perk", "Lower price"), ("Best for", "Starting smart")],
        foot="My favorite WordPress CRM, for less"),
    dict(id=59391, lang="de", htmllang="de", pt="Gutscheincode FluentCRM - Hero DE", tf=88, vf=88,
        p1="FluentCRM", p2="Gutschein", icon=I_TAG, vh="Das Wichtigste",
        lines=["FluentCRM,", "der <em>Deal</em>"],
        base="Mein Gutscheincode für FluentCRM: hol dir mein liebstes WordPress-CRM zum besten Preis, in wenigen Klicks.",
        vn="Der Deal", vs="bei FluentCRM sparen",
        stats=[("Typ", "Gutscheincode"), ("Für", "FluentCRM Pro"), ("Vorteil", "Günstiger Preis"), ("Ideal für", "Clever starten")],
        foot="Mein liebstes WordPress-CRM, günstiger"),
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
