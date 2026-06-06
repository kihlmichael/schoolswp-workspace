"""Fetch FluentCart YouTube transcripts via DataForSEO API and save markdown files locally.

Pipeline:
1. POST /v3/serp/youtube/video_subtitles/live/advanced for each video
2. Dedupe rolling caption overlaps (YouTube auto-captions overlap by design)
3. Build markdown with header + paragraphs
4. Save under .tmp-fluentcart-transcripts/<priority>-<id>.md

Run from project root with .venv/Scripts/python.
"""

from __future__ import annotations

import base64
import concurrent.futures as cf
import json
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

USER = "contact@michaelkihl.fr"
PWD = "9619f3f5c61f8fbb"
ENDPOINT = "https://api.dataforseo.com/v3/serp/youtube/video_subtitles/live/advanced"

OUT_DIR = Path(__file__).parent
EXTRACTION_DATE = "2026-05-19"

# (priority_prefix, seq, video_id, title, duration, slug)
VIDEOS = [
    # --- Top 1 - Officiels WPManageNinja ---
    ("A", 1, "-GmuODJXObk", "FluentCart: The FASTEST WooCommerce Alternative (Complete Tutorial)", "1:02:40", "fluentcart-fastest-woo-alternative"),
    ("A", 2, "uLuLzBWYTa0", "FluentCart LIVE Demo with Shahjahan Jewel", "1:40:38", "fluentcart-live-demo-shahjahan-jewel"),
    ("A", 3, "iCH91AKiRq0", "FluentCart Shipping New Features Daily — Everything That's New", "10:38", "fluentcart-shipping-new-features"),
    ("A", 4, "qPevG01umgo", "Sell More Using FluentCart Integration with FluentCRM", "9:20", "fluentcart-fluentcrm-integration"),
    ("A", 5, "wgITkJhkosc", "How to Add Products in Your Store with FluentCart", "9:25", "add-products-fluentcart"),
    ("A", 6, "mCqa7Dt__S8", "How to Sell Products with Multiple Variations", "9:14", "sell-products-variations"),
    ("A", 7, "95k2Y3Ly0yI", "FluentCart Elementor Blocks Are Here", "9:48", "fluentcart-elementor-blocks"),
    ("A", 8, "KWFfzjSUcZk", "How to Create a Digital Product with License Using FluentCart", "8:35", "digital-product-license"),
    ("A", 9, "LtxeoOn92nE", "How to Manage Orders in WordPress with FluentCart", "8:13", "manage-orders-fluentcart"),
    ("A", 10, "IUHpC-wLMuk", "Build a Membership System for FREE in WordPress", "8:02", "membership-system-free-wordpress"),
    ("A", 11, "Y60NtDrbo8E", "How to Configure Taxes for Your Online Store", "7:37", "configure-taxes-store"),
    ("A", 12, "EKcQbn_diKQ", "eCommerce Features You Need in 2026", "7:31", "ecommerce-features-2026"),
    ("A", 13, "JLBQNRXfADU", "How to Manage Your Online Store in WordPress | FluentCart", "7:04", "manage-online-store-fluentcart"),
    ("A", 14, "civx2FRQp1o", "How To Create And Manage Coupons in WordPress with FluentCart", "6:59", "coupons-fluentcart"),
    ("A", 15, "z_QaFONgsNo", "Set Up Your Online Store in WordPress with FluentCart", "6:31", "setup-online-store-fluentcart"),
    ("A", 16, "uBOIQXh0yDo", "How to Ship Products Worldwide In WordPress With FluentCart", "6:31", "ship-worldwide-fluentcart"),
    ("A", 17, "oPlvPk7BmME", "Start Your Online Business for FREE", "6:30", "start-online-business-free"),
    ("A", 18, "4bPYqLefPP8", "How to Connect Multiple Payment Gateways in FluentCart", "6:19", "multiple-payment-gateways"),
    ("A", 19, "jlen1WvJDI8", "How to Customize Your Online Store with WordPress Gutenberg Editor", "6:04", "customize-store-gutenberg"),
    ("A", 20, "QyF-0-MWbR8", "This Simple Packaging Fix Can Save You Thousands", "5:46", "packaging-fix-save-thousands"),
    ("A", 21, "fft6fB48ZmY", "Advanced Inventory Management in FluentCart", "5:54", "advanced-inventory-management"),
    ("A", 22, "yJ2n9mAQ3rs", "Boost Store Conversions with Page Browsing History", "5:54", "boost-conversions-browsing-history"),
    ("A", 23, "LhurGHdf67s", "FluentCart is Getting Better Every Day", "5:39", "fluentcart-getting-better"),
    ("A", 24, "nVmVE-RbyZ4", "How to Sell Physical & Digital Products Together", "5:21", "sell-physical-digital-together"),
    ("A", 25, "vZkQ3LvGW7s", "Get Paid for Every Booking", "5:24", "paid-every-booking"),
    ("A", 26, "rYURYzXRf9A", "Free Plugins Don't Scale", "5:25", "free-plugins-dont-scale"),
    ("A", 27, "HToxE5YtHQM", "Make Money Selling Online Courses for FREE", "5:06", "sell-online-courses-free"),
    ("A", 28, "V5nALtJLXnY", "How to Create New Orders + Custom Payments", "4:50", "new-orders-custom-payments"),
    ("A", 29, "ElyoIlUfpjg", "How to Manage Customers in Your Online Store", "5:11", "manage-customers-store"),
    ("A", 30, "R4kbP5Cwmo0", "How to Collect Display Product Reviews + WPSocialNinja", "5:50", "product-reviews-wpsocialninja"),
    # --- Top 2 - Reviews / walkthroughs tiers ---
    ("B", 1, "2DwAN1Ft6HA", "FluentCart Review: The Truth Nobody Is Telling You!", "34:01", "fluentcart-review-truth"),
    ("B", 2, "wRjdmQDQ6ns", "FluentCart Review - Everything You Need To Know!", "31:15", "fluentcart-review-everything"),
    ("B", 3, "M3xfbtFhrSI", "FluentCart is FEATURE packed for FREE!", "22:56", "fluentcart-feature-packed-free"),
    ("B", 4, "fwDWCXtj5W0", "FluentCart First Impressions - Complete Walkthrough", "29:09", "fluentcart-first-impressions-walkthrough"),
    ("B", 5, "6jb4eURVy9M", "Is FluentCart the Next Big Thing?", "19:06", "fluentcart-next-big-thing"),
    ("B", 6, "G2TqzwWB8Qw", "Fluent Cart Overview - Fast, Lightweight, and Powerful!", "15:59", "fluentcart-overview-fast-lightweight"),
    ("B", 7, "jy0TbM1Rzp8", "Fluent Cart FREE - So Much For Zero Cost!", "25:14", "fluentcart-free-zero-cost"),
    ("B", 8, "nuLIXt7qHDk", "Is FluentCart the WooCommerce Killer?", "25:02", "fluentcart-woocommerce-killer"),
    ("B", 9, "5lj0OyNtRlY", "Finally, a Cart Plugin That Gets It", "26:23", "cart-plugin-that-gets-it"),
    ("B", 10, "g2F-nLK6cRc", "FluentCart Prerelease - WooCommerce Killer?", "33:34", "fluentcart-prerelease-woo-killer"),
    ("B", 11, "qLZbwltWfCY", "New FluentCart First Look!", "33:07", "fluentcart-first-look"),
    ("B", 12, "GqaPwbH-l_A", "How To Sell Products Online - Getting Started With FluentCart", "35:02", "sell-products-online-getting-started"),
    ("B", 13, "4JjOBe5mvr0", "Bye Bye WooCommerce? My First Look at FluentCart", "17:00", "bye-bye-woo-first-look"),
    ("B", 14, "bcKAXsqo_O8", "Fluent Cart in Bricks: The Good, The Bad & What's Missing", "14:47", "fluentcart-bricks-good-bad"),
    ("B", 15, "kNapzJq-Jyw", "FluentCart Pro Setup Made Easy", "15:20", "fluentcart-pro-setup-easy"),
    ("B", 16, "obWMvgQO7jA", "How I Am Using FluentCart For My Online Business", "13:24", "using-fluentcart-online-business"),
    ("B", 17, "dgpxnDtwbaQ", "FluentCart Plugin Hands-on Overview", "13:48", "fluentcart-hands-on-overview"),
    ("B", 18, "ytYhMP2J09s", "Genius WordPress Automation (FluentCart + MailerPress)", "20:02", "wordpress-automation-mailerpress"),
    ("B", 19, "zd8ogjvdSO4", "How To Sell an Online Course with FluentCart (LifterLMS)", "9:57", "sell-online-course-lifterlms"),
    ("B", 20, "laudt9M4sYk", "FluentCart vs SureCart - Which is Better?", "11:27", "fluentcart-vs-surecart"),
    ("B", 21, "WsCXQPBsJOQ", "How FluentCart Saved My Online Business!", "10:28", "fluentcart-saved-online-business"),
]


def _auth_header() -> str:
    raw = f"{USER}:{PWD}".encode("utf-8")
    return "Basic " + base64.b64encode(raw).decode("ascii")


def _post(payload: list[dict]) -> dict:
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT,
        data=body,
        method="POST",
        headers={
            "Authorization": _auth_header(),
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _fetch_subtitles(video_id: str, translate: bool = False) -> list[dict] | None:
    """Return list of subtitle items or None on hard failure."""
    task = {
        "video_id": video_id,
        "location_name": "United States",
        "language_code": "en",
        "subtitles_language": "en",
    }
    if translate:
        task["subtitles_translate_language"] = "en"
    try:
        data = _post([task])
    except urllib.error.HTTPError as e:
        print(f"  [HTTP {e.code}] {video_id}: {e.reason}", flush=True)
        return None
    except Exception as e:  # noqa: BLE001
        print(f"  [ERR] {video_id}: {e}", flush=True)
        return None

    if data.get("status_code") != 20000:
        print(f"  [API] {video_id}: {data.get('status_message')}", flush=True)
        return None

    tasks = data.get("tasks") or []
    if not tasks:
        return None
    t0 = tasks[0]
    if t0.get("status_code") != 20000:
        print(f"  [TASK] {video_id}: {t0.get('status_message')}", flush=True)
        return None
    results = t0.get("result") or []
    if not results:
        return None
    items = results[0].get("items") or []
    return items


def _dedupe_rolling(items: list[dict]) -> list[str]:
    """YouTube auto-captions overlap (rolling 2-line display). Each new caption
    contains the tail of the previous one. We compute the longest suffix of
    prev_combined that matches the prefix of current text, and only append the
    non-overlapping part.
    """
    if not items:
        return []
    items_sorted = sorted(items, key=lambda x: x.get("start_time") or 0.0)
    out: list[str] = []
    prev = ""
    for it in items_sorted:
        cur = (it.get("text") or "").strip()
        if not cur:
            continue
        # Find longest k such that prev endswith first k chars of cur.
        max_k = min(len(prev), len(cur))
        k = 0
        for size in range(max_k, 0, -1):
            if prev.endswith(cur[:size]):
                k = size
                break
        new_part = cur[k:].strip()
        if new_part:
            out.append(new_part)
        # prev tracks the last ~200 chars to keep overlap comparison cheap
        prev = (prev + " " + new_part).strip()[-300:]
    return out


def _to_paragraphs(tokens: list[str]) -> str:
    """Join tokens into sentences. Each '. ', '? ', '! ' triggers a soft wrap.
    Paragraphs every ~5 sentences for readability.
    """
    if not tokens:
        return ""
    text = " ".join(tokens)
    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()
    # Insert newline after sentence terminators
    text = re.sub(r"([.!?])\s+", r"\1\n", text)
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    # Group every 5 sentences into a paragraph
    paragraphs = []
    chunk: list[str] = []
    for s in lines:
        chunk.append(s)
        if len(chunk) >= 5:
            paragraphs.append(" ".join(chunk))
            chunk = []
    if chunk:
        paragraphs.append(" ".join(chunk))
    return "\n\n".join(paragraphs)


def _process_one(entry):
    prefix, seq, vid, title, duration, slug = entry
    print(f"[{prefix}{seq:02d}] {vid} — {title[:60]}", flush=True)
    items = _fetch_subtitles(vid, translate=False)
    if not items:
        # try translate fallback
        items = _fetch_subtitles(vid, translate=True)
    if not items:
        return {"ok": False, "prefix": prefix, "seq": seq, "video_id": vid, "title": title, "reason": "no subtitles available"}

    tokens = _dedupe_rolling(items)
    body = _to_paragraphs(tokens)
    word_count = len(body.split())

    md = (
        f"# {title}\n\n"
        f"- YouTube ID : {vid}\n"
        f"- URL : https://www.youtube.com/watch?v={vid}\n"
        f"- Durée : {duration}\n"
        f"- Chaîne : \n"
        f"- Date extraction : {EXTRACTION_DATE}\n"
        f"- Mots : {word_count}\n\n"
        f"---\n\n"
        f"{body}\n"
    )

    fname = f"T{prefix}{seq:02d}-{vid}-{slug}.md"
    fpath = OUT_DIR / fname
    fpath.write_text(md, encoding="utf-8")
    return {
        "ok": True,
        "prefix": prefix,
        "seq": seq,
        "video_id": vid,
        "title": title,
        "duration": duration,
        "slug": slug,
        "filename": fname,
        "word_count": word_count,
        "segments": len(items),
    }


def main():
    # Optional filter: python fetch_transcripts.py A     -> only Top 1
    #                  python fetch_transcripts.py B     -> only Top 2
    #                  python fetch_transcripts.py vid1 vid2 ... -> specific
    flt = sys.argv[1:]
    todo = list(VIDEOS)
    if flt:
        keep_letters = {x for x in flt if len(x) == 1}
        keep_vids = {x for x in flt if len(x) > 1}
        todo = [e for e in todo if e[0] in keep_letters or e[2] in keep_vids]

    print(f"Processing {len(todo)} videos in parallel (max 6 workers)...", flush=True)
    t_start = time.time()
    results = []
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        for r in ex.map(_process_one, todo):
            results.append(r)

    elapsed = time.time() - t_start
    ok = [r for r in results if r["ok"]]
    ko = [r for r in results if not r["ok"]]

    manifest = {
        "extraction_date": EXTRACTION_DATE,
        "elapsed_sec": round(elapsed, 1),
        "total": len(results),
        "ok": len(ok),
        "ko": len(ko),
        "ok_items": ok,
        "ko_items": ko,
    }
    (OUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(f"\nDone in {elapsed:.1f}s — ok={len(ok)} ko={len(ko)}", flush=True)
    print(f"Manifest: {OUT_DIR / 'manifest.json'}", flush=True)


if __name__ == "__main__":
    main()
