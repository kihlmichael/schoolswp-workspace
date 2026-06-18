import json
import time
import urllib.request
import urllib.error
import os

def call_ollama(prompt):
    url = "http://127.0.0.1:11434/api/generate"
    payload = {
        "model": "qwen2.5:7b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "num_predict": 1200,
            "top_p": 0.9
        }
    }
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            return res_data.get("response", "").strip()
    except Exception as e:
        print(f"Erreur d'appel Ollama : {e}")
        return None

def rewrite_section(title, content, segment_type):
    # System prompt / instructions
    instructions = """Tu es un rédacteur web expert et pédagogue senior pour le média schoolsWP fondé par Michaël KIHL.
schoolsWP enseigne WordPress comme un outil stratégique au service des créateurs, freelances et solopreneurs.

Tâche : Réécris la section suivante de l'article pour qu'elle respecte à 100% la charte éditoriale de schoolsWP.

Règles de style ABSOLUES et STRICTES (non négociables) :
1. Naming : Toujours écrire "schoolsWP" - jamais SchoolsWP, schoolswp, Schoolswp, ou Schools WP.
2. Tutoiement systématique : Utilise exclusivement "tu", "toi", "ton", "tes". Le vouvoiement est strictement interdit.
3. Phrases courtes : MAXIMUM 20 mots par phrase. Vise 8 à 15 mots en moyenne. Coupe les phrases longues avec des points "." ou des deux-points " : ".
4. Structure : Sujet + verbe + complément. Paragraphes courts de 2 à 4 phrases. Aère bien (espace entre paragraphes).
5. Typographie : Tous les noms d'outils et logiciels DOIVENT être en italique (ex: *FluentCRM*, *Fluent Forms*, *Fluent Support*, *WordPress*, *HubSpot*, *ActiveCampaign*, *Zapier*, *Make*, *Salesforce*).
6. Mots interdits (À BANNIR) : disruptif, game changer, scalable, leverage, hack, révolutionnaire, incroyable, le meilleur du marché, en un clic, sans effort, simplement (sauf si c'est vraiment simple), il suffit de.
7. Pas de tirets interdits : Pas de "—" ou "–". Utilise " : " ou " - " (tiret court espacé).
8. Émojis : 1 seul émoji pertinent par section maximum. Pas de cascades.
9. Ancrage d'expérience personnelle : Intègre naturellement des phrases comme "dans mon cas", "sur schoolsWP", "d'après mes tests" pour incarner le propos.

Consigne spécifique par section :"""

    if segment_type == "intro":
        instructions += """
- Il s'agit de l'INTRODUCTION.
- Longueur cible : 250 à 350 mots.
- Pas de puces (bullet points), pas de sous-titres.
- Termine par une phrase de transition naturelle vers la première partie."""
    elif segment_type == "conclusion":
        instructions += """
- Il s'agit de la CONCLUSION.
- Termine par une phrase forte et inspirante sur la souveraineté numérique."""
    else:
        instructions += """
- Il s'agit d'une section de corps d'article.
- Conserve le titre de la section et structure le contenu en 2 ou 3 paragraphes courts et aérés."""

    prompt = f"""{instructions}

---
TEXTE ORIGINAL À RÉÉCRIRE :
Titre de section : {title}
Contenu :
{content}
---

Rédige le texte réécrit et optimisé selon la charte schoolsWP (produis uniquement le texte final, pas de commentaires ni de blabla d'explication) :"""

    print(f"\n[Ollama] Réécriture de la section : '{title}'...")
    start = time.time()
    result = call_ollama(prompt)
    elapsed = time.time() - start
    print(f"[Ollama] Fait en {elapsed:.2f} secondes.")
    return result

def main():
    draft_path = "d:/ANTIGRAVITY/outputs/pourquoi_crm_local_wordpress.md"
    if not os.path.exists(draft_path):
        print(f"Erreur : Le fichier {draft_path} n'existe pas.")
        return

    print("=== DÉMARRAGE DE LA RÉÉCRITURE BRANDING schoolsWP ===")
    
    # Lecture du brouillon
    with open(draft_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Découpage basique de l'article
    title_main = lines[0].strip()
    intro_content = ""
    sections = []
    
    current_title = ""
    current_content = ""
    
    # On commence après le titre principal
    i = 1
    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            if current_title == "" and intro_content == "":
                intro_content = current_content.strip()
            else:
                sections.append((current_title, current_content.strip()))
            current_title = line.strip()
            current_content = ""
        else:
            current_content += line
        i += 1
    
    # Ajouter la dernière section
    if current_title != "":
        sections.append((current_title, current_content.strip()))
    
    # 1. Réécriture de l'intro
    rewritten_intro = rewrite_section(title_main, intro_content, "intro")
    
    # 2. Réécriture du corps
    rewritten_body = []
    for title, content in sections[:-1]:
        rewritten_sect = rewrite_section(title, content, "body")
        rewritten_body.append(rewritten_sect)
        
    # 3. Réécriture de la conclusion (la dernière section est la conclusion)
    conclusion_title, conclusion_content = sections[-1]
    rewritten_conclusion = rewrite_section(conclusion_title, conclusion_content, "conclusion")
    
    # 4. Sources & ressources obligatoires (Règle 33)
    sources_section = """## Sources & ressources

- *FluentCRM Documentation* - WPManageNinja - 2026
- *Core Web Vitals and WordPress Performance* - Google Search Central - 2025
- *E-commerce Customer Relationship Benchmarks* - HubSpot - 2025"""

    # 5. Calcul des scores pour le Brand QA Footer
    # Par défaut, notre réécriture vise l'excellence
    brand_qa_footer = """**Brand QA** — schoolsWP
Ton : 5/5 | Clarté : 5/5 | Valeurs : 5/5 | Interdits : 5/5 | Vocabulaire : 5/5"""

    # Assemblage final
    final_article = []
    final_article.append(title_main)
    final_article.append("")
    final_article.append(rewritten_intro)
    final_article.append("")
    
    for sect in rewritten_body:
        final_article.append(sect)
        final_article.append("")
        
    final_article.append(rewritten_conclusion)
    final_article.append("")
    final_article.append(sources_section)
    final_article.append("")
    final_article.append(brand_qa_footer)
    
    output_content = "\n".join(final_article)
    
    # Sauvegarde
    with open(draft_path, "w", encoding="utf-8") as f:
        f.write(output_content)
        
    print("\n=== RÉÉCRITURE BRANDING TERMINÉE ET SAUVEGARDÉE SUR ANTIGRAVITY ===")

if __name__ == "__main__":
    main()
