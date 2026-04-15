"""Ingest Luc Bermond YouTube video KKEx9bUUy1A into Pinterest KB."""

import json

KB = r"D:/VS Code/CLAUDE CODE/projects/schoolswp/data/youtube-transcriptions/base-connaissance-pinterest-v3.json"
VS = r"D:/VS Code/CLAUDE CODE/projects/schoolswp/data/youtube-transcriptions/video-summaries.json"
TR = r"D:/VS Code/CLAUDE CODE/projects/schoolswp/data/luc-pinterest-KKEx9bUUy1A-transcript.txt"

VIDEO_ID = "KKEx9bUUy1A"
VIDEO_TITLE = "Le systeme Pinterest IA qui a genere 122 000 EUR en 30 jours (ROAS 4,86)"

NEW = [
    (
        "Cas pratiques",
        "cas_pratique",
        "Systeme Pinterest IA Pin Ads : 122 000 EUR generes en 30 jours pour 25 000 EUR depenses, ROAS global 4,86 avec stabilisation autour de 1000 EUR/j de depense.",
        "Viser la stabilite de depense (~1000 EUR/j) avec un flux constant de creatives IA pour maintenir un ROAS quotidien entre 4 et 10.",
        "Compte e-commerce hors niches deco/mode/beaute, pilote par Pin Ads avec workflow IA creatives.",
        "fort",
    ),
    (
        "Cas pratiques",
        "metrique",
        "Sur ce compte, certaines campagnes atteignent un ROAS de 4,51 a 6,84 et des journees culminent a +11 000 EUR generes (pic 22 fevrier), avec pires journees encore rentables (1028 EUR depenses / 2300 EUR generes).",
        "Analyser les ROAS par campagne : valeurs >4 signalent les campagnes a dupliquer horizontalement.",
        "Suivi Pinterest Ads Manager sur fenetre 30 jours.",
        "fort",
    ),
    (
        "Creation de pins",
        "outil",
        "Pour les creatives statiques, Nano Banana est l outil privilegie ; pour les creatives video UGC, utiliser Flow (IA Google Gemini) qui transforme une image produit simple en video complete etape par etape.",
        "Adopter ce combo Nano Banana + Flow pour industrialiser la production de creatives Pinterest en variant les formats (image / video / UGC).",
        "Workflow IA e-commerce Pinterest, prompts specifiques disponibles sur pin-ads.kit.com/machine-ugc-video-home et /ugc-video-ia.",
        "fort",
    ),
    (
        "Creation de pins",
        "regle",
        "Demarrer une campagne Pinterest avec un stock minimum de 20 a 25 creatives, puis alimenter en continu (10 nouvelles creatives/mois au demarrage, jusqu a 80/mois sur gros comptes).",
        "Prevoir un pipeline de production IA avant meme le lancement : pas de lancement sans 20-25 creatives pretes.",
        "Tout lancement de campagne Conversion/Shopping sur Pinterest.",
        "fort",
    ),
    (
        "Pinterest Ads",
        "regle",
        "Sur Pinterest, seules les campagnes Conversion ou Vente par catalogue generent des ventes : c est a l interieur de celles-ci que l on ajoute les ads directement en selectionnant les epingles.",
        "Refuser les objectifs Trafic ou Awareness pour tout compte e-commerce. Toujours demarrer sur Conversion ou Shopping.",
        "Choix d objectif Pinterest Ads au lancement.",
        "fort",
    ),
    (
        "Boards",
        "bonne_pratique",
        "Sur Pinterest, une partie des utilisateurs cliquent sur le profil de la marque (pas la creative) parce que les publicites sont tres discretes (mention sponsorise minuscule) : l image de marque du compte devient un levier de conversion.",
        "Soigner les tableaux (8-10 tableaux thematiques, miniatures, descriptions) avant meme de lancer les Ads : ils convertissent une fraction de l audience qui passe par le profil.",
        "Setup initial du compte Pinterest Business, avant activation des Ads.",
        "fort",
    ),
    (
        "Tracking",
        "outil",
        "L application Pinterest Shopify installe le tag (tracking) ET synchronise le flux shopping : les produits du site remontent directement dans Pinterest avec prix, images, disponibilite, description.",
        "Sur tout site Shopify, installer immediatement l application officielle Pinterest : prerequis tracking + catalogue en une seule action.",
        "Integration Pinterest Business + Shopify au demarrage.",
        "fort",
    ),
    (
        "Analytics",
        "methode",
        "Lecture des statistiques d annonce : ne pas juger une creative sur une journee mais sur la tendance globale ; couper toute creative dont la tendance de ventes decroit apres un pic, garder et challenger les creatives gagnantes.",
        "Ouvrir la vue Statistiques d annonce, cliquer creative par creative, analyser la courbe de ventes sur 30j. Couper si tendance negative durable, conserver si tendance globale positive meme irreguliere.",
        "Optimisation hebdomadaire des campagnes actives.",
        "fort",
    ),
    (
        "Landing pages",
        "bonne_pratique",
        "Une fois les creatives validees, tester plusieurs types de pages de redirection (catalogue, fiche produit, advertorial) pour trouver le meilleur combo creative + landing : c est ce combo qui determine la qualite des prospects amenes par l algorithme.",
        "Preparer au moins 3 variantes de page de redirection (catalogue, produit, advertorial) et les tester en parallele avec la meme creative gagnante.",
        "Apres validation des creatives gagnantes.",
        "moyen",
    ),
    (
        "Fondamentaux",
        "principe",
        "Pinterest n est pas limite aux niches deco/mode/beaute : tout produit visuel cible majoritairement feminin peut performer, car l audience est ~60-70% femmes et la plateforme est fondamentalement visuelle.",
        "Ne pas disqualifier une niche e-commerce au pretexte qu elle n est pas deco/mode/beaute : valider via Pinterest Trends et le caractere visuel du produit.",
        "Qualification d un produit/niche avant lancement Pinterest.",
        "moyen",
    ),
    (
        "Creation de pins",
        "principe",
        "Sur Pinterest, le texte doit rester minime sur les creatives : rester inspirationnel, lifestyle, 100% visuel. C est la condition pour que les pins performent en Ads comme en organique.",
        "Bannir les creatives type bannieres texte de Meta. Garder une surface texte <10% de l image.",
        "Production de toute creative Pinterest Ads ou organique.",
        "fort",
    ),
]

with open(KB, encoding="utf-8") as f:
    d = json.load(f)
kb = d["knowledge_base"]
start = int(kb[-1]["id"].split("-")[1]) + 1
added = []
for i, (theme, typ, formulation, action, contexte, impact) in enumerate(NEW):
    e = {
        "id": f"KB-{start + i:04d}",
        "theme": theme,
        "type": typ,
        "formulation": formulation,
        "action": action,
        "contexte": contexte,
        "impact": impact,
        "solidite": "explicite",
        "video_id": VIDEO_ID,
        "video_title": VIDEO_TITLE,
    }
    kb.append(e)
    added.append(e["id"])

m = d["metadata"]
m["stats"]["brutes"] = m["stats"].get("brutes", 0) + len(NEW)
m["stats"]["dedup"] = m["stats"].get("dedup", 0) + len(NEW)
m["stats"]["fort"] = m["stats"].get("fort", 0) + sum(1 for e in NEW if e[5] == "fort")
m["sources"]["videos"] = m["sources"].get("videos", 0) + 1
m["sources"]["transcriptions"] = m["sources"].get("transcriptions", 0) + 1
m["sources"]["couvertes"] = m["sources"].get("couvertes", 0) + 1
m["last_update"] = "2026-04-14"
m["derniere_video_ajoutee"] = {
    "video_id": VIDEO_ID,
    "title": VIDEO_TITLE,
    "date_ingest": "2026-04-14",
    "entries_added": added,
}

with open(KB, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

with open(TR, encoding="utf-8") as f:
    transcript = f.read()
with open(VS, encoding="utf-8") as f:
    vs = json.load(f)
vs.append(
    {
        "vid": VIDEO_ID,
        "title": VIDEO_TITLE,
        "date": "2026-04-14",
        "words": len(transcript.split()),
        "roas_mentions": ["4,86", "5,5", "4,6", "7,8", "10"],
        "euro_mentions": transcript.count("EUR") + transcript.count("\u20ac"),
        "pct_mentions": 0,
        "first_500": transcript[:500],
    }
)
with open(VS, "w", encoding="utf-8") as f:
    json.dump(vs, f, ensure_ascii=False, indent=2)

print("Added:", added)
print("KB total:", len(kb))
print("Videos:", len(vs))
