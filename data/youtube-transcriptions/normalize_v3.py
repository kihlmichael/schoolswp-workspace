import json, re, unicodedata
from collections import Counter

data = json.load(open("data/youtube-transcriptions/v3-knowledge-deduped.json", encoding="utf-8"))

CANONICAL = [
    "Fondamentaux",
    "Pinterest Ads",
    "Pinterest SEO",
    "Creation de pins",
    "Design",
    "Copywriting",
    "Landing pages",
    "Boards",
    "Distribution",
    "E-commerce",
    "Tracking",
    "Ciblage",
    "Budget",
    "Tests",
    "Optimisation",
    "Analytics",
    "Tunnel",
    "Erreurs",
    "Tendances",
    "Cas pratiques",
    "Outils",
    "Scaling",
    "Retargeting",
    "Shopping",
    "Performance Plus",
    "Saisonnalite",
    "International",
    "Trafic",
    "Conversion",
    "Mythes",
]

KEYWORDS = {
    "Fondamentaux": [
        "fondament",
        "plateforme",
        "audience pinterest",
        "nature",
        "positionn",
        "introduction",
        "mission",
        "decouverte",
        "compreh",
        "avantage concurr",
        "ocean bleu",
        "concurrence",
        "stabilit",
        "long terme",
        "mindset",
    ],
    "Pinterest Ads": [
        "pinterest ads",
        "campagne",
        "objectif campagne",
        "encheres",
        "enchere",
        "cpc",
        "cpm",
        "structure campagne",
        "compte publicitaire",
        "deblocage",
        "type de campagne",
        "paiement natif",
        "lead ads",
        "phase apprentissage",
        "internal trigger",
    ],
    "Pinterest SEO": [
        "seo pinterest",
        "pinterest seo",
        "mots-cles pinterest",
        "hashtag",
        "organique pinterest",
        "pin suggest",
        "score de page",
        "revendication site",
        "rich pins",
        "flux organique",
        "publication pinterest",
        "frequence publication",
    ],
    "Creation de pins": [
        "creat",
        "epingle",
        "pin ",
        "pins ",
        "ugc",
        "statique",
        "video pinterest",
        "format creat",
        "format vertical",
        "format video",
        "hook video",
        "nano banana",
        "gemini",
        "flows",
        "ia creat",
        "chatgpt",
        "templates canva",
        "profils feminins",
    ],
    "Design": [
        "design",
        "visuel",
        "image produit",
        "photo produit",
        "couleur",
        "lumiere",
        "lifestyle",
        "fond blanc",
        "4k ",
        "vertical",
    ],
    "Copywriting": [
        "copywriting",
        "texte epingle",
        "titre epingle",
        "description epingle",
        "cta",
        "appel action",
        "inspirationnel",
    ],
    "Landing pages": [
        "landing page",
        "page produit",
        "page collection",
        "page redirection",
        "cro",
        "hotjar",
        "taux rebond",
        "parcours simpl",
    ],
    "Boards": ["tableau", "board", "miniature tableau", "couverture tableau", "structure tableau"],
    "E-commerce": [
        "e-commerce",
        "ecommerce",
        "shopify",
        "woocommerce",
        "prestashop",
        "panier moyen",
        "catalogue produit",
        "flux shopping",
        "produit gagnant",
        "dropship",
        "affiliation",
        "niche",
        "bijoux",
        "decoration",
        "beaute",
        "mariage",
        "jardin",
        "complement alimentaire",
        "etsy",
    ],
    "Tracking": [
        "tracking",
        "pixel",
        "api conversion",
        "attribution",
        "utm",
        "correspondance avancee",
        "scoring interne",
        "evenement conversion",
    ],
    "Ciblage": [
        "ciblage",
        "audience",
        "demographi",
        "centres interet",
        "femme",
        "non precise",
        "broad",
        "exact match",
        "lookalike",
        "langue ciblage",
        "geographi",
        "pays ciblage",
    ],
    "Budget": ["budget", "cout publicitaire", "depense", "investir", "petit budget", "quotidien vs", "palier budget"],
    "Scaling": [
        "scaling",
        "scaler",
        "dupliquer campagne",
        "horizontal",
        "escalier",
        "palier spend",
        "augmenter budget",
    ],
    "Retargeting": ["retargeting", "reciblage", "audience chaude", "dynamique", "retargetin"],
    "Shopping": [
        "shopping",
        "catalogue shopping",
        "commercant verifie",
        "flux produit",
        "channable",
        "multifeed",
        "vente par catalogue",
    ],
    "Performance Plus": ["performance plus", "performance+"],
    "Saisonnalite": [
        "saisonnal",
        "q4",
        "q5",
        "noel",
        "saint-valentin",
        "black friday",
        "ete pinterest",
        "printemps",
        "rentree",
        "janvier",
        "fete des meres",
    ],
    "Outils": ["outil", "tailwind", "minea", "pin spy", "canva", "exploding topics", "dropship.io"],
    "Erreurs": [
        "erreur",
        "piege",
        "croyance",
        "mythe",
        "ne pas faire",
        "eviter",
        "bloqu",
        "suspendu",
        "ban ",
        "strike",
        "fausse",
    ],
    "Cas pratiques": [
        "cas pratique",
        "etude de cas",
        "resultat client",
        "thomas",
        "dorian",
        "julie",
        "quentin",
        "la fourche",
        "asphal",
        "decathlon",
        "lego",
        "sephora",
        "tiffany",
        "la redoute",
        "expedia",
        "cuur",
        "spring",
        "omads",
    ],
    "Tendances": [
        "tendance",
        "evolution",
        "nouveaute",
        "predict",
        "generation z",
        "2025",
        "2026",
        "futur",
        "nouveau pinterest",
        "croissance",
    ],
    "Tests": ["test ab", "a/b test", "tester", "test creatif"],
    "Optimisation": ["optimisation", "ameliorer", "diagnostic", "analyse resultat", "kpi", "metriques surveiller"],
    "Analytics": ["analytics", "statistique", "reporting", "dashboard", "analyse post"],
    "International": [
        "international",
        "marche us",
        "usa",
        "canada",
        "europe",
        "scandinave",
        "mexique",
        "bresil",
        "marche amerique",
    ],
    "Trafic": ["trafic", "visiteur", "impression", "clic sortant", "ctr pinterest"],
    "Conversion": ["conversion", "achat", "vente", "roi", "roas", "taux conversion"],
    "Tunnel": ["tunnel", "funnel", "parcours achat", "cycle achat"],
    "Distribution": ["distribution", "horaire publication", "planifier epingle"],
    "Mythes": ["mythe", "idee recue", "fausse croyance"],
}


def strip_a(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def classify_theme(unit):
    theme_raw = strip_a(unit.get("theme", "")).lower().strip()
    formulation = strip_a(unit.get("formulation", "")).lower()
    combined = theme_raw + " " + formulation

    for canon in CANONICAL:
        if strip_a(canon).lower() == theme_raw:
            return canon

    best = None
    best_score = 0
    for canon, kws in KEYWORDS.items():
        score = sum(1 for kw in kws if kw in combined)
        if score > best_score:
            best_score = score
            best = canon

    return best if best_score > 0 else "Fondamentaux"


for u in data:
    u["theme"] = classify_theme(u)

themes = Counter(u["theme"] for u in data)
vids = set(u.get("video_id", "") for u in data if u.get("video_id"))

print(f"Unites: {len(data)}, Videos: {len(vids)}, Themes: {len(themes)}")
for t, c in themes.most_common():
    print(f"  {t}: {c}")

json.dump(
    data,
    open("data/youtube-transcriptions/v3-knowledge-deduped.json", "w", encoding="utf-8"),
    ensure_ascii=False,
    indent=2,
)

output = {
    "metadata": {
        "titre": "Base de Connaissance Pinterest - Luc Bermond",
        "date": "2026-04-05",
        "version": "3.0",
        "sources": {
            "videos": 215,
            "transcriptions": 215,
            "couvertes": len(vids),
            "mots": 683719,
            "chars_analyses": 3652839,
        },
        "stats": {
            "brutes": 1612,
            "dedup": len(data),
            "fort": sum(1 for u in data if u.get("impact") == "fort"),
            "themes": len(themes),
            "types": len(Counter(u["type"] for u in data)),
        },
        "comparaison": {
            "v1": {"unites": 135, "videos": 13},
            "v2": {"unites": 523, "videos": 204},
            "v3": {"unites": len(data), "videos": len(vids)},
        },
    },
    "taxonomie": {t: [u["id"] for u in data if u["theme"] == t] for t in sorted(themes)},
    "knowledge_base": data,
}
json.dump(
    output,
    open("data/youtube-transcriptions/base-connaissance-pinterest-v3.json", "w", encoding="utf-8"),
    ensure_ascii=False,
    indent=2,
)
print("V3 JSON final OK")
