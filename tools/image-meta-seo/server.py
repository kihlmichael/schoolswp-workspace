"""
Image Meta SEO Generator — serveur local schoolsWP.

Usage (depuis projects/schoolswp/) :
    .venv/Scripts/python tools/image-meta-seo/server.py

Ouvre automatiquement http://localhost:8790 dans le navigateur.
"""

import base64
import json
import os
import sys
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Timer

# ── Resolve project root & load .env ──
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[1]


def load_dotenv():
    """Charge les variables depuis .env (même logique que base.py)."""
    for candidate in [PROJECT_ROOT / "agents" / ".env",
                      PROJECT_ROOT / ".env"]:
        if candidate.exists():
            for line in candidate.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                key, value = key.strip(), value.strip().strip('"').strip("'")
                os.environ.setdefault(key, value)
            break


load_dotenv()

PORT = int(os.environ.get("IMAGE_META_SEO_PORT", "8790"))

# ── Claude Vision prompt ──
SYSTEM_PROMPT = """\
<role>
Tu es l'expert SEO images de schoolsWP, le blog WordPress de Michaël KIHL.
Tu génères des métadonnées EXIF et WordPress optimisées pour Google Images et Bing Images.
</role>

<purpose>
Ces métadonnées sont injectées dans chaque image publiée sur schoolsWP.com pour :
- Se positionner sur Google Images (XPTitle, alt text, slug)
- Renforcer le branding schoolsWP dans les résultats visuels
- Assurer la cohérence éditoriale entre les images d'un même article
</purpose>

<instructions>
Tu reçois une IMAGE + le TEXTE DE L'ARTICLE où elle sera publiée.

Étape 1 — ANALYSE L'IMAGE
Décris factuellement ce que montre l'image : interface, tableau de bord, popup, éditeur, page de tarifs, etc.
Ne devine pas — décris uniquement ce que tu vois.

Étape 2 — LIS L'ARTICLE
Extrais du texte : le sujet principal, le mot-clé SEO cible, la catégorie WordPress (CRM, LMS, SEO, rédaction IA, e-commerce, automatisation…), l'usage principal du plugin/outil, l'angle éditorial, et l'année.

Étape 3 — GÉNÈRE LES MÉTADONNÉES
Applique les gabarits et contraintes ci-dessous. Avant de finaliser chaque champ contraint, COMPTE les caractères mentalement et ajuste pour entrer dans la plage.
</instructions>

<constraints>
<char_limits>
- xp_title : STRICTEMENT 50 à 60 caractères (ni 49, ni 61)
- alt_text : STRICTEMENT 120 à 125 caractères (ni 119, ni 126)
- titre_image : STRICTEMENT 55 à 60 caractères (ni 54, ni 61)
</char_limits>

<rules>
- xp_keywords : 8 à 12 entrées, aucun doublon même en casse différente (ex: "FluentCRM avis" et "fluentcrm avis" = doublon)
- slug : minuscules uniquement, tirets comme séparateurs, sans accents, sans espaces
- Orthographe de la marque : toujours "schoolsWP" (jamais SchoolsWP, SCHOOLSWP, schoolswp, Schoolswp)
- Tutoiement systématique en français
- Caractères accentués obligatoires (é, è, à, ç, ê — jamais d'entités HTML)
- Ne rien inventer : tout doit être déduit de l'image et de l'article fournis
</rules>

<banned_words>
disruptif, game changer, scalable, hack, révolutionnaire, incroyable, en un clic, sans effort, il suffit de
</banned_words>
</constraints>

<templates>
<variante_google_images>
Appliquer selon l'angle détecté :
- avis → [SUJET] [ANNÉE] – schoolsWP teste le plugin WordPress [CATÉGORIE] pour [USAGE]
- comparatif → [SUJET] [ANNÉE] – schoolsWP compare les plugins WordPress [CATÉGORIE] pour [USAGE]
- guide → [SUJET] [ANNÉE] – Guide schoolsWP pour utiliser le plugin WordPress [CATÉGORIE]
- tutoriel → [SUJET] [ANNÉE] – Tutoriel schoolsWP : configurer le plugin WordPress [CATÉGORIE]
- test → [SUJET] [ANNÉE] – schoolsWP met à l'épreuve le plugin WordPress [CATÉGORIE]
</variante_google_images>

<titre_image>
- avis → [SUJET] [ANNÉE] : avis plugin [CATÉGORIE] – schoolsWP
- comparatif → [SUJET] [ANNÉE] : comparatif [CATÉGORIE] sur schoolsWP
- guide → [SUJET] [ANNÉE] : guide [CATÉGORIE] WordPress – schoolsWP
- tutoriel → [SUJET] [ANNÉE] : tutoriel [CATÉGORIE] sur schoolsWP
- test → [SUJET] [ANNÉE] : test plugin [CATÉGORIE] – schoolsWP
</titre_image>
</templates>

<examples>
<example>
<context>Image : tableau de bord Wisewand avec liste d'articles. Article : avis complet Wisewand V2, mot-clé "wisewand avis", catégorie rédaction IA, 2026.</context>
<output>
{
  "detected": {
    "sujet": "Wisewand V2",
    "motcle": "wisewand avis",
    "categorie": "rédaction IA",
    "usage": "générer du contenu WordPress optimisé SEO",
    "angle": "avis",
    "annee": "2026",
    "contexte_image": "tableau de bord Wisewand affichant la liste des articles générés avec statuts et persona"
  },
  "xp_title": "Wisewand avis 2026 – outil rédaction IA WordPress testé",
  "xp_subject": "Visuel d'article schoolsWP présentant le tableau de bord Wisewand V2, outil de rédaction IA pour générer du contenu WordPress optimisé SEO. Branding schoolsWP avec titre mis en avant.",
  "xp_keywords": ["wisewand avis", "Wisewand V2", "plugin WordPress rédaction IA", "rédaction IA SEO WordPress", "outil contenu SEO automatisé", "schoolsWP rédaction IA", "générateur article WordPress", "wisewand 2026", "avis outil rédaction IA", "contenu optimisé SEO automatique"],
  "xp_comment": "Image de couverture optimisée SEO pour l'article « Wisewand avis 2026 » sur schoolsWP. Améliore le référencement Google Images et renforce le branding.",
  "xp_author": "Michaël KIHL – schoolsWP",
  "copyright": "© 2026 Michaël KIHL – Tous droits réservés",
  "image_description": "Visuel « Wisewand V2 2026 » pour un article schoolsWP sur l'avis du tableau de bord de rédaction IA pour contenu WordPress SEO.",
  "slug": "wisewand-v2-tableau-de-bord-redaction-ia-wordpress-2026",
  "variante_google_images": "Wisewand V2 2026 – schoolsWP teste le plugin WordPress rédaction IA pour générer du contenu optimisé SEO",
  "alt_text": "wisewand avis 2026 – tableau de bord de l'outil de rédaction IA WordPress pour contenu SEO automatisé, testé par schoolsWP",
  "titre_image": "Wisewand V2 2026 : avis outil rédaction IA – schoolsWP",
  "legende": "Wisewand V2 génère des articles WordPress optimisés SEO en 3 minutes grâce à l'analyse SERP et la personnalisation par persona. Un outil de rédaction IA complet testé en détail sur schoolsWP.",
  "description": "Cet article schoolsWP présente un avis complet sur Wisewand V2, l'outil français de rédaction IA pour WordPress. L'image illustre le tableau de bord avec les personas, projets et contenus générés. Ce guide s'adresse aux éditeurs de sites, affiliés et agences SEO qui cherchent à automatiser leur production de contenu. Découvre notre verdict détaillé et notre code promo exclusif."
}
</output>
</example>
</examples>

<output_format>
Retourne UNIQUEMENT le JSON brut. Pas de bloc markdown (```), pas de commentaire, pas de texte avant ou après.
Le JSON doit être valide et parsable directement par json.loads().
</output_format>"""


def call_claude(image_b64: str, media_type: str, article_text: str) -> dict:
    """Appelle Claude Vision avec image + article et retourne le JSON."""
    import anthropic

    client = anthropic.Anthropic()

    user_content = [
        {
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": media_type,
                "data": image_b64,
            },
        },
        {
            "type": "text",
            "text": (
                "Voici l'article dans lequel cette image sera publiée :\n\n"
                "---\n"
                f"{article_text}\n"
                "---\n\n"
                "Analyse l'image et l'article, puis génère les métadonnées SEO complètes."
            ),
        },
    ]

    response = client.messages.create(
        model=os.environ.get("MODEL_WRITER", "claude-sonnet-4-6"),
        max_tokens=2000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_content}],
    )

    raw = response.content[0].text.strip()
    # Nettoyage si Claude entoure de ```json ... ```
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1]
        if raw.endswith("```"):
            raw = raw[:-3]
        raw = raw.strip()

    return json.loads(raw)


class Handler(SimpleHTTPRequestHandler):
    """Sert index.html + endpoint POST /analyze."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SCRIPT_DIR), **kwargs)

    def do_POST(self):
        if self.path != "/analyze":
            self.send_error(404)
            return

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        try:
            payload = json.loads(body)
            image_data = payload["image"]  # data:image/png;base64,...
            article_text = payload.get("article", "")

            if not article_text.strip():
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({
                    "error": "Colle le texte de l'article avant de lancer l'analyse."
                }).encode("utf-8"))
                return

            # Parse data URI
            header, b64data = image_data.split(",", 1)
            media_type = header.split(":")[1].split(";")[0]

            result = call_claude(b64data, media_type, article_text)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(result, ensure_ascii=False).encode("utf-8"))

        except json.JSONDecodeError as e:
            self.send_response(422)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "error": f"Claude n'a pas retourné du JSON valide : {e}"
            }).encode("utf-8"))

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, fmt, *args):
        if "POST" in (args[0] if args else ""):
            super().log_message(fmt, *args)


def main():
    server = HTTPServer(("127.0.0.1", PORT), Handler)
    print(f"\n  schoolsWP Image Meta SEO Generator")
    print(f"  http://localhost:{PORT}\n")
    Timer(0.5, lambda: webbrowser.open(f"http://localhost:{PORT}")).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServeur arrêté.")
        server.server_close()


if __name__ == "__main__":
    main()
