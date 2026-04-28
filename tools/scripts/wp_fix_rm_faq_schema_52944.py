#!/usr/bin/env python3
"""
Rewrite Rank Math FAQPage schema attached to post 52944 so it matches the
3 new body questions (post-v4).
Target meta key: rank_math_schema_FAQPage (serialized array payload).
"""
import json, urllib.request, urllib.error, base64, sys, re, time, gzip, io
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
POST_ID = 52944

NEW_FAQ = {
    "@type": "FAQPage",
    "metadata": {
        "title": "FAQ",
        "type": "template",
        "isPrimary": "",
        "reviewLocationShortcode": "[rank_math_rich_snippet]",
    },
    "mainEntity": [
        {
            "@type": "Question",
            "name": "Quel plugin LMS choisir pour WordPress ?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": (
                    "Le choix d'un plugin LMS dépend de vos besoins spécifiques. "
                    "LearnDash est le plus complet et populaire, idéal pour les projets ambitieux. "
                    "Tutor LMS offre un excellent rapport qualité-prix avec une version gratuite généreuse. "
                    "Lifter LMS est une solution freemium intuitive avec des options de gamification. "
                    "Pour débuter avec un budget limité, LearnPress et Sensei LMS sont des solutions légères et gratuites."
                ),
            },
        },
        {
            "@type": "Question",
            "name": "Comment vendre des formations en ligne avec WordPress ?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": (
                    "Pour vendre des formations en ligne avec WordPress, installez d'abord un plugin LMS "
                    "performant comme Tutor LMS, LearnDash ou Lifter LMS. Structurez votre contenu pédagogique "
                    "en cours, leçons et quiz. Intégrez une solution de paiement sécurisée comme WooCommerce "
                    "avec Stripe ou PayPal pour gérer les transactions. Créez une page de vente persuasive avec "
                    "vidéo, témoignages et appel à l'action. Automatisez les communications avec FluentCRM ou "
                    "SureTriggers, puis optimisez votre SEO et lancez des campagnes d'emailing."
                ),
            },
        },
        {
            "@type": "Question",
            "name": "Quel budget pour créer une plateforme de formation WordPress ?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": (
                    "Le budget varie selon le niveau. Option économique : 500 à 1 500 euros "
                    "(hébergement annuel, thème gratuit ou premium, plugin LMS gratuit comme LearnPress ou Tutor LMS). "
                    "Option intermédiaire : 1 500 à 5 000 euros (hébergement performant, thème premium Kadence, "
                    "plugin LMS premium, extensions additionnelles). Option professionnelle : 5 000 à 15 000 euros "
                    "ou plus (développement sur mesure, services de design, outils avancés). WordPress reste "
                    "économique comparé aux plateformes SaaS propriétaires."
                ),
            },
        },
    ],
}

def creds():
    env = json.loads(SETTINGS.read_text(encoding="utf-8")).get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]

def auth(u, p):
    return "Basic " + base64.b64encode(f"{u}:{p}".encode()).decode()

def rm_update(u, p, meta):
    req = urllib.request.Request(
        "https://schoolswp.com/wp-json/rankmath/v1/updateMeta",
        data=json.dumps({"objectID": POST_ID, "objectType": "post", "meta": meta}).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": auth(u, p),
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")

def public_faq_check():
    url = f"https://schoolswp.com/creer-plateforme-formation-wordpress/?nocache={int(time.time())}"
    req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0","Cache-Control":"no-cache"})
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            raw = gzip.decompress(raw)
    data = raw.decode("utf-8", errors="replace")
    qs = re.findall(r'"@type"\s*:\s*"Question"[^{]*"name"\s*:\s*"([^"]+)"', data)
    return qs

def main():
    u, p = creds()

    # Try multiple possible meta keys under which Rank Math stores per-post schema
    candidates = [
        "rank_math_schema_FAQPage",
        "rank_math_schema_2099769",
        "rank_math_schemas",
    ]

    for key in candidates:
        print(f"\n[try] writing to {key}")
        status, resp = rm_update(u, p, {key: NEW_FAQ})
        print(f"   HTTP {status} resp[:200]: {resp[:200]}")
        time.sleep(1)
        qs = public_faq_check()
        print(f"   Live questions now ({len(qs)}):")
        for q in qs[:5]:
            print(f"     - {q}")
        if qs and any("plugin LMS choisir" in q for q in qs):
            print(f"\n[SUCCESS] FAQPage updated via key '{key}'")
            return

    print("\n[FAIL] All key candidates ignored by /updateMeta")
    sys.exit(1)

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
