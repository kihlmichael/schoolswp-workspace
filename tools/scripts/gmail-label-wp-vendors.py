"""Applique le label '📰 Newsletters' sur les emails des fabricants WP.

Usage :
  python tools/scripts/gmail-label-wp-vendors.py           # dry-run (liste sans modifier)
  python tools/scripts/gmail-label-wp-vendors.py --apply   # applique le label
  python tools/scripts/gmail-label-wp-vendors.py --apply --days 365  # elargit la fenetre

Le label cible = Label_5722837123959833844 (📰 Newsletters).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
_spec = importlib.util.spec_from_file_location("gc", SCRIPT_DIR / "gmail-common.py")
_gc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_gc)

LABEL_ID = "Label_5722837123959833844"  # 📰 Newsletters

# Fabricants WordPress + outils ecosysteme (derive de l'export ClickWhale + sources seed)
# Gmail 'from:' fait du substring match, donc inutile de lister les sous-domaines mail./news./etc.
# -- sauf pour les cas ou le fabricant envoie UNIQUEMENT depuis un sous-domaine specifique
VENDORS = [
    # --- WPManageNinja (Fluent*) ---
    "fluentcrm.com", "fluentsupport.com", "fluentboards.com", "fluentbooking.com",
    "fluentforms.com", "fluentcart.com", "fluentcommunity.co",
    "wpmanageninja.com", "ninjatables.com",
    # --- Page builders + themes ---
    "kadencewp.com", "kadenceblocks.com", "elementor.com", "generateblocks.com",
    "generatepress.com", "bricksbuilder.io", "elegantthemes.com", "beaverbuilder.com",
    "wpbeaverbuilder.com", "wpastra.com", "wpspectra.com", "breakdance.com",
    "crocoblock.com", "droip.com", "jpthemes.com", "jpblocks.com",
    "divi-pixel.com", "diviengine.com", "divilover.com",
    # --- Automattic / WordPress core ---
    "automattic.com", "wordpress.com", "woo.com", "woocommerce.com", "jetpack.com",
    # --- SEO ---
    "rankmath.com", "yoast.com", "aioseo.com", "seopress.org", "surerank.com",
    "link-whisper.com", "linkwhisper.com", "seo-key.fr", "seo-sans-migraine.fr",
    "seopital.co", "skoatch.com", "getgenie.ai", "wisewand.ai", "wpwand.com",
    "thruuu.com", "thot-seo.fr", "chatseo.app", "pageradar.io", "seranking.com",
    "semrush.com",
    # --- Hebergeurs + perf ---
    "kinsta.com", "wpengine.com", "wp-rocket.me", "flyingpress.com", "cloudways.com",
    "siteground.com", "hostinger.fr", "rapyd.cloud", "xcloud.host", "planethoster.com",
    "copilhost.fr", "o2switch.fr", "nitropack.io", "fastpixel.io", "perfmatters.io",
    "infiniteuploads.com", "novashare.io",
    # --- Securite / backup ---
    "wordfence.com", "sucuri.net", "ithemes.com", "solidwp.com",
    "updraftplus.com", "wpvivid.com", "duplicator.com", "wp-umbrella.com",
    # --- E-commerce + tunnels ---
    "surecart.com", "cartflows.com", "funnelkit.com", "getwpfunnels.com",
    "launchflows.com", "b2bking.com", "kingsplugins.com",
    # --- CRM / email / marketing ---
    "surecontact.com", "mailerpress.com", "groundhogg.io", "convertkit.com",
    "mailpoet.com", "systeme.io", "manychat.com",
    # --- Automation / integration ---
    "suretriggers.com", "ottokit.com", "make.com", "pabbly.com",
    "automatorwp.com", "bitapps.pro",
    # --- LMS / formation ---
    "tutorlms.com", "learndash.com", "lifterlms.com", "masteriyo.com",
    "buddyboss.com", "wishlistmember.com", "suremembers.com",
    # --- Forms / booking ---
    "sureforms.com", "latepoint.com",
    # --- Video / media ---
    "prestoplayer.com", "submagic.co", "elevenlabs.io",
    # --- IA / content ---
    "bertha.ai", "mydropai.com",
    # --- Site builders / no-code ---
    "instawp.com", "zipwp.com", "webflow.com",
    # --- Links / redirects / affiliate ---
    "clickwhale.com", "presstools.com", "solidaffiliate.com",
    "affiliatepressplugin.com", "armemberplugin.com",
    # --- Analytics / social ---
    "wpsocialninja.com", "metricool.com", "bit-social.com",
    # --- Community / misc ---
    "wpbeginner.com", "wpmudev.com", "freshrank.ai", "wporigami.com",
    "multicollab.com", "themeover.com", "wpgridbuilder.com",
    "gamipress.com", "exclusiveaddons.com", "piotnet.com",
    "wpmet.com", "coolplugins.net", "bdthemes.com", "surelywp.com",
    "pulse-pro.app", "arraytics.com", "junglescout.com",
    "alidropship.com", "netim.com",
    # --- Send-only subdomains (bypass parent domain match) ---
    "news.ottokit.com", "news.zipwp.com", "mail.tutorlms.com",
]


def build_query(domains: list[str], days: int) -> str:
    from_clause = " OR ".join(f"from:*@{d}" for d in domains)
    return f"({from_clause}) newer_than:{days}d -label:{LABEL_ID}"


def search_messages(svc, query: str, max_results: int = 500) -> list[dict]:
    results = []
    page_token = None
    while True:
        resp = svc.users().messages().list(
            userId="me", q=query, maxResults=min(100, max_results - len(results)),
            pageToken=page_token
        ).execute()
        results.extend(resp.get("messages", []))
        page_token = resp.get("nextPageToken")
        if not page_token or len(results) >= max_results:
            break
    return results


def get_subject_and_from(svc, msg_id: str) -> tuple[str, str]:
    msg = svc.users().messages().get(
        userId="me", id=msg_id, format="metadata",
        metadataHeaders=["Subject", "From"]
    ).execute()
    headers = msg.get("payload", {}).get("headers", [])
    h = {x["name"].lower(): x["value"] for x in headers}
    return h.get("subject", "(no subject)"), h.get("from", "(no from)")


def apply_label(svc, msg_ids: list[str]) -> int:
    # Gmail API batchModify : max 1000 par appel
    count = 0
    for i in range(0, len(msg_ids), 500):
        chunk = msg_ids[i : i + 500]
        svc.users().messages().batchModify(
            userId="me",
            body={"ids": chunk, "addLabelIds": [LABEL_ID]},
        ).execute()
        count += len(chunk)
    return count


def main():
    days = 180
    apply = "--apply" in sys.argv
    if "--days" in sys.argv:
        days = int(sys.argv[sys.argv.index("--days") + 1])

    svc = _gc.get_service()
    query = build_query(VENDORS, days)
    print(f"Fenetre : {days} jours")
    print(f"Domaines scrutes : {len(VENDORS)}\n")

    msgs = search_messages(svc, query, max_results=1000)
    print(f"Emails trouves (non deja labelises) : {len(msgs)}\n")

    if not msgs:
        print("Rien a faire.")
        return

    # Echantillon pour preview
    print("Echantillon (20 premiers) :")
    for m in msgs[:20]:
        subj, frm = get_subject_and_from(svc, m["id"])
        print(f"  [{m['id'][:12]}]  {frm[:45]:45s}  |  {subj[:80]}")

    if len(msgs) > 20:
        print(f"  ... + {len(msgs) - 20} autres")

    if not apply:
        print(f"\n[DRY-RUN] Ajoute --apply pour labeliser ces {len(msgs)} emails.")
        return

    print(f"\nApplication du label sur {len(msgs)} emails...")
    count = apply_label(svc, [m["id"] for m in msgs])
    print(f"[OK] {count} emails labelises avec '📰 Newsletters'")


if __name__ == "__main__":
    main()
