#!/usr/bin/env python3
"""Cartographie des mails reçus via le forward kidkihl@gmail.com.

Liste les expéditeurs, fréquence, date dernier mail, et suggère une priorité
de bascule (🔴 CRITIQUE / 🟡 IMPORTANT / ⚪ OPTIONNEL / 🔵 NEWSLETTER).

Usage:
    python gmail-kidkihl-cartography.py --output data/kidkihl-cartography.csv [--days 90]
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import re
import sys
from collections import defaultdict
from email.utils import parseaddr, parsedate_to_datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
spec = importlib.util.spec_from_file_location("gmail_common", SCRIPT_DIR / "gmail-common.py")
gc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gc)


# Classification par domaine/mot-clé
CRITICAL_PATTERNS = [
    # Domaines & registrars
    r"ovh\.",
    r"gandi\.",
    r"namecheap\.",
    r"godaddy\.",
    r"cloudflare\.",
    r"hostinger\.",
    r"o2switch\.",
    r"infomaniak\.",
    # Hébergement
    r"wp1\.host",
    r"kinsta\.",
    r"wpengine\.",
    # Paiements & banques
    r"stripe\.",
    r"paypal\.",
    r"shine\.",
    r"qonto\.",
    r"revolut\.",
    r"banque",
    r"credit",
    r"boursorama",
    # Administratif
    r"impots\.gouv",
    r"urssaf\.",
    r"ameli\.",
    r"caf\.",
    r"laposte\.net",
    r"service-public",
    r"ants\.gouv",
    # Google/Apple/Microsoft security
    r"accounts\.google",
    r"no-reply@accounts",
    r"appleid\.",
    r"microsoft\.com",
    r"security",
    r"sécurité",
]

IMPORTANT_PATTERNS = [
    # SaaS métier payants
    r"anthropic\.",
    r"claude\.",
    r"openai\.",
    r"perplexity",
    r"firecrawl",
    r"rapidapi",
    r"dataforseo",
    r"ahrefs",
    r"semrush",
    r"gumroad",
    r"lemonsqueezy",
    r"polar\.sh",
    # Réseaux sociaux actifs
    r"linkedin\.",
    r"github\.",
    r"twitter\.",
    r"x\.com",
    r"pinterest",
    # Affiliation
    r"impact\.com",
    r"awin\.",
    r"affilae",
    r"partnerstack",
    # WordPress écosystème
    r"wordpress\.",
    r"woocommerce",
    r"elementor",
    r"kadence",
    r"fluentcrm",
    r"ottokit",
    r"suretriggers",
]

NEWSLETTER_PATTERNS = [
    r"newsletter",
    r"mailchimp",
    r"substack",
    r"beehiiv",
    r"convertkit",
    r"sendinblue",
    r"brevo",
    r"mailerlite",
    r"no-?reply.*news",
]


def classify(sender_email: str, subject: str = "") -> str:
    haystack = (sender_email + " " + subject).lower()
    for pat in CRITICAL_PATTERNS:
        if re.search(pat, haystack):
            return "🔴 CRITIQUE"
    for pat in IMPORTANT_PATTERNS:
        if re.search(pat, haystack):
            return "🟡 IMPORTANT"
    for pat in NEWSLETTER_PATTERNS:
        if re.search(pat, haystack):
            return "🔵 NEWSLETTER"
    return "⚪ OPTIONNEL"


def get_header(headers: list[dict], name: str) -> str:
    for h in headers:
        if h["name"].lower() == name.lower():
            return h["value"]
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, help="Chemin CSV de sortie")
    parser.add_argument("--days", type=int, default=90, help="Fenêtre en jours (défaut: 90)")
    parser.add_argument(
        "--query",
        default="deliveredto:kidkihl@gmail.com",
        help="Requête Gmail (défaut: deliveredto:kidkihl@gmail.com)",
    )
    args = parser.parse_args()

    service = gc.get_service()
    query = f"{args.query} newer_than:{args.days}d"
    print(f"Requête: {query}", file=sys.stderr)

    # Liste des message IDs
    ids, token = [], None
    while True:
        resp = service.users().messages().list(userId="me", q=query, maxResults=500, pageToken=token).execute()
        ids.extend(m["id"] for m in resp.get("messages", []))
        token = resp.get("nextPageToken")
        if not token:
            break
    print(f"{len(ids)} messages trouvés", file=sys.stderr)

    # Agrégation par expéditeur
    by_sender: dict[str, dict] = defaultdict(
        lambda: {
            "count": 0,
            "last_date": None,
            "last_subject": "",
            "sample_subjects": [],
        }
    )

    for i, msg_id in enumerate(ids, 1):
        if i % 50 == 0:
            print(f"  [{i}/{len(ids)}]", file=sys.stderr)
        msg = (
            service.users()
            .messages()
            .get(
                userId="me",
                id=msg_id,
                format="metadata",
                metadataHeaders=["From", "Subject", "Date"],
            )
            .execute()
        )
        headers = msg.get("payload", {}).get("headers", [])
        from_raw = get_header(headers, "From")
        _, email = parseaddr(from_raw)
        email = email.lower().strip()
        if not email:
            continue
        subject = get_header(headers, "Subject")
        date_raw = get_header(headers, "Date")
        try:
            date = parsedate_to_datetime(date_raw) if date_raw else None
        except Exception:
            date = None

        entry = by_sender[email]
        entry["count"] += 1
        if date and (entry["last_date"] is None or date > entry["last_date"]):
            entry["last_date"] = date
            entry["last_subject"] = subject
        if len(entry["sample_subjects"]) < 3:
            entry["sample_subjects"].append(subject)

    # Tri par fréquence décroissante
    rows = []
    for email, data in by_sender.items():
        rows.append(
            {
                "priorite": classify(email, " ".join(data["sample_subjects"])),
                "expediteur": email,
                "nb_mails": data["count"],
                "dernier_mail": data["last_date"].strftime("%Y-%m-%d") if data["last_date"] else "",
                "dernier_sujet": data["last_subject"][:80],
                "action_suggeree": "",
            }
        )

    # Sort: priorité (rouge > jaune > bleu > blanc) puis nb_mails desc
    priority_order = {"🔴 CRITIQUE": 0, "🟡 IMPORTANT": 1, "🔵 NEWSLETTER": 2, "⚪ OPTIONNEL": 3}
    rows.sort(key=lambda r: (priority_order.get(r["priorite"], 9), -r["nb_mails"]))

    # Action suggérée par priorité
    for r in rows:
        if r["priorite"] == "🔴 CRITIQUE":
            r["action_suggeree"] = "Changer email du compte → michaelkihlpro@gmail.com"
        elif r["priorite"] == "🟡 IMPORTANT":
            r["action_suggeree"] = "Changer email sous 3 mois"
        elif r["priorite"] == "🔵 NEWSLETTER":
            r["action_suggeree"] = "Unsubscribe"
        else:
            r["action_suggeree"] = "Laisser (forward fait le job) ou fermer compte"

    # Export CSV
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["priorite", "expediteur", "nb_mails", "dernier_mail", "dernier_sujet", "action_suggeree"],
            delimiter=";",
        )
        writer.writeheader()
        writer.writerows(rows)

    # Résumé console
    summary: dict[str, int] = defaultdict(int)
    for r in rows:
        summary[r["priorite"]] += 1
    print(f"\nCSV écrit: {output_path}  ({len(rows)} expéditeurs uniques)", file=sys.stderr)
    print("\nRépartition par priorité:", file=sys.stderr)
    for prio in ["🔴 CRITIQUE", "🟡 IMPORTANT", "🔵 NEWSLETTER", "⚪ OPTIONNEL"]:
        print(f"  {prio}: {summary.get(prio, 0)} expéditeurs", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
