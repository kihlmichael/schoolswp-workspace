import os
import re
import sys
from datetime import datetime

import requests

# Force l'encodage UTF-8 de la console sous Windows pour éviter tout UnicodeEncodeError
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Importer le chargeur d'environnement existant
sys.path.append(os.path.dirname(__file__))
from run_pipeline import load_env_variables


def get_obsidian_outbox_path():
    """
    Returns the absolute path to the Obsidian Outbox directory.
    Falls back to a local 'output/' directory inside the project if not accessible.
    """
    path = r"D:\🌐 MES SITES\📋 SCHOOLSWP.COM\12_Obsidian\schoolsWP\00_systeme\claude-code-bridge\outbox-depuis-claude"
    if os.path.exists(path):
        return path

    # Fallback local
    local_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))), "output"
    )
    os.makedirs(local_path, exist_ok=True)
    return local_path


def call_ollama_completion(prompt, model_name="qwen2.5:7b"):
    """
    Calls local Ollama server using OpenAI compatible endpoint.
    """
    ollama_url = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434/v1").rstrip("/") + "/chat/completions"

    payload = {"model": model_name, "messages": [{"role": "user", "content": prompt}], "temperature": 0.7}

    try:
        response = requests.post(ollama_url, json=payload, timeout=600)
        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()
        else:
            raise RuntimeError(f"Ollama a retourné une erreur HTTP {response.status_code}: {response.text}")
    except Exception as e:
        raise RuntimeError(f"Échec de l'appel local Ollama : {e}")


def read_prompt_template(filename):
    """
    Reads prompt template from prompts folder.
    """
    script_dir = os.path.dirname(os.path.dirname(__file__))
    prompt_path = os.path.join(script_dir, "prompts", filename)
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()


def generate_voiceover_tts(text, output_path, api_key, voice_id):
    """
    Calls ElevenLabs Text-to-Speech API to synthesize the voiceover MP3 file.
    """
    print("[INFO] Lancement de la synthèse vocale via ElevenLabs...")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"xi-api-key": api_key, "Content-Type": "application/json"}

    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=300)
        if response.status_code == 200:
            with open(output_path, "wb") as f:
                f.write(response.content)
            print(f"[SUCCESS] Voix off synthétisée avec succès : {output_path}")
            return True
        else:
            raise RuntimeError(f"ElevenLabs TTS a retourné une erreur HTTP {response.status_code}: {response.text}")
    except Exception as e:
        print(f"[ERROR] Échec de la synthèse vocale ElevenLabs : {e}")
        return False


def extract_dialogue_from_script(script_markdown):
    """
    Parses the generated script markdown and extracts dialogue.
    Tries regex for 'Dialogue exact: "..."' first (highly robust against column swapping),
    then falls back to column-based parsing.
    """
    # 1. Tentative d'extraction par regex ciblant "Dialogue exact: ..." ou similaire
    dialogue_matches = re.findall(
        r'(?:Dialogue exact|dialogue exact|Dialogue|dialogue)\s*:\s*["«]([^"»]*?)["»]', script_markdown
    )
    if dialogue_matches:
        clean_text = " ".join([d.strip() for d in dialogue_matches if d.strip()])
        if len(clean_text) > 20:
            return clean_text

    # 2. Fallback 1 : Analyse des lignes de tableau (colonne gauche ou droite selon le contenu)
    lines = script_markdown.split("\n")
    dialogue_lines = []

    for line in lines:
        line = line.strip()
        if line.startswith("|") and line.endswith("|"):
            # Ignorer les en-têtes et les séparateurs
            if "---" in line or "notes visuelles" in line.lower() or "rythme" in line.lower():
                continue

            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 1:
                # Si la colonne de droite contient "Dialogue exact", on extrait depuis celle-ci
                target_col = parts[0]
                if len(parts) > 1 and "dialogue exact" in parts[1].lower():
                    # Tente d'extraire la partie dialogue exact dans la colonne de droite
                    match = re.search(r'["«]([^"»]*?)["»]', parts[1])
                    if match:
                        target_col = match.group(1)

                # Nettoyage
                spoken_text = re.sub(r"\[.*?\]", "", target_col)
                spoken_text = re.sub(r"SEG-\d+", "", spoken_text)
                spoken_text = spoken_text.strip("**").strip()
                if spoken_text and len(spoken_text) > 3 and spoken_text.lower() not in ("hook", "payoff", "cta"):
                    dialogue_lines.append(spoken_text)

    if dialogue_lines:
        return " ".join(dialogue_lines)

    # 3. Fallback 2 : Renvoyer le texte nettoyé sans les blocs d'annotations
    clean_lines = []
    for line in lines:
        if not line.startswith("[") and not line.startswith("|"):
            clean_lines.append(line)
    return " ".join(clean_lines)


def run_interactive_planner(dry_run=False):
    """
    Main interactive loop for the 7-step SOP video planner.
    """
    print("=" * 80)
    print("      ASSISTANT DE PRODUCTION VIDÉO INTERACTIF - METHOD SOP (schoolswp)")
    print("=" * 80)

    # 1. Charger l'environnement
    load_env_variables()

    elevenlabs_key = os.getenv("ELEVENLABS_API_KEY")
    elevenlabs_voice_id = os.getenv("ELEVENLABS_VOICE_ID", "r8Nv8JDxL3hOIt4MZtwT")

    obsidian_dir = get_obsidian_outbox_path()
    display_dir = obsidian_dir.replace("🌐", "[SITE]").replace("📋", "[DOCS]")
    print(f"[INFO] Dossier de sortie Obsidian : {display_dir}\n")

    # --- ETAPE 1 : GENERATION DE CONCEPTS ---
    print("-" * 80)
    print(" ETAPE 1 : Génération de Concepts")
    print("-" * 80)

    if dry_run:
        print("[DRY-RUN] Simulation de l'étape 1...")
        niche = "WordPress, IA, LMS, n8n"
        audience = "Créateurs de formations, indépendants, agences WordPress"
        objectifs = "Notoriété, autorité pédagogique, engagement"
        performants = "Aucune donnée"
        contraintes = "Solo, matériel minimal, format YouTube long, durée visée 10 minutes"
    else:
        niche = input("Niche du contenu [WordPress, IA, LMS, n8n] : ") or "WordPress, IA, LMS, n8n"
        audience = (
            input("Audience cible [Créateurs de formations, indépendants, agences WordPress] : ")
            or "Créateurs de formations, indépendants, agences WordPress"
        )
        objectifs = (
            input("Objectifs [Notoriété, autorité pédagogique, engagement] : ")
            or "Notoriété, autorité pédagogique, engagement"
        )
        performants = input("Vidéos les plus performantes [Aucune donnée] : ") or "Aucune donnée"
        contraintes = (
            input("Contraintes [Solo, matériel minimal, format YouTube long, durée visée 10 minutes] : ")
            or "Solo, matériel minimal, format YouTube long, durée visée 10 minutes"
        )

    print("\n[INFO] Génération des 7 concepts via Ollama local (qwen2.5:7b)...")
    concept_template = read_prompt_template("write_concept_ollama.txt")
    concept_prompt = concept_template.format(
        niche=niche, audience=audience, objectifs=objectifs, performants=performants, contraintes=contraintes
    )

    if dry_run:
        concepts_out = "### CONCEPT-01: Titre de simulation\nAngle de simulation.\n\n<!-- slide -->\nBLOC DE PASSAGE POUR L'ÉTAPE SUIVANTE\n- Promesse centrale: test"
    else:
        concepts_out = call_ollama_completion(concept_prompt)

    print("\n" + "=" * 40 + " CONCEPTS GÉNÉRÉS " + "=" * 40)
    print(concepts_out[:2000] + "\n... (Tronqué pour affichage) ...\n")

    concepts_file = os.path.join(obsidian_dir, "01_concepts.md")
    with open(concepts_file, "w", encoding="utf-8") as f:
        f.write(concepts_out)
    print(f"[SUCCESS] Les 7 concepts ont été sauvegardés dans : {concepts_file}")

    # --- ETAPE 2 : ARCHITECTURE DE SCRIPT ---
    print("\n" + "-" * 80)
    print(" ETAPE 2 : Architecture du Script Rétention")
    print("-" * 80)

    if dry_run:
        print("[DRY-RUN] Simulation de l'étape 2...")
        chosen_concept = "CONCEPT-01: Titre de simulation\nPromesse centrale: test"
        style_parole = "Pédagogique, direct, tutoiement"
        longueur = "10 minutes"
        plateforme = "YouTube long"
        tournage_contraintes = "Solo, enregistrement d'écran + voix off ElevenLabs"
    else:
        print("Veuillez sélectionner le meilleur concept recommandé et copier/coller son bloc de passage.")
        chosen_concept = input("Entrez/collez le concept choisi ou son bloc de passage : ")
        if not chosen_concept.strip():
            # Essayer d'extraire automatiquement le premier concept du fichier généré
            match = re.search(r"(CONCEPT-01.*?)CONCEPT-02", concepts_out, re.DOTALL)
            if match:
                chosen_concept = match.group(1).strip()
                print("[INFO] Utilisation automatique du CONCEPT-01 détecté.")
            else:
                chosen_concept = "CONCEPT-01 extrait de 01_concepts.md"

        style_parole = (
            input("Style de parole [Pédagogique, direct, tutoiement] : ") or "Pédagogique, direct, tutoiement"
        )
        longueur = input("Longueur cible [10 minutes] : ") or "10 minutes"
        plateforme = input("Plateforme [YouTube long] : ") or "YouTube long"
        tournage_contraintes = (
            input("Contraintes de tournage [Solo, enregistrement d'écran + voix off ElevenLabs] : ")
            or "Solo, enregistrement d'écran + voix off ElevenLabs"
        )

    print("\n[INFO] Génération du script de rétention ultra-précis via Ollama local (qwen2.5:7b)...")
    script_template = read_prompt_template("write_script_ollama.txt")
    script_prompt = script_template.format(
        concept_choisi=chosen_concept,
        style_parole=style_parole,
        longueur=longueur,
        plateforme=plateforme,
        contraintes=tournage_contraintes,
    )

    if dry_run:
        script_out = (
            "| Dialogue exact | Notes visuelles |\n"
            "| [HOOK] Salut c'est Michael, aujourd'hui on va brancher Claude en local. | Capture d'écran |\n"
            "| SEG-01 Dans un premier temps on configure le fichier JSON. | Plan de détail |\n"
            "\nBLOC DE PASSAGE POUR L'ÉTAPE SUIVANTE\n- Promesse centrale: test"
        )
    else:
        script_out = call_ollama_completion(script_prompt)

    print("\n" + "=" * 40 + " SCRIPT GÉNÉRÉ " + "=" * 40)
    print(script_out[:2000] + "\n... (Tronqué pour affichage) ...\n")

    script_file = os.path.join(obsidian_dir, "02_script.md")
    with open(script_file, "w", encoding="utf-8") as f:
        f.write(script_out)
    print(f"[SUCCESS] Le script complet a été sauvegardé dans : {script_file}")

    # --- ETAPE 3 : SYNTHESE ELEVENLABS ---
    print("\n" + "-" * 80)
    print(" ETAPE 3 : Synthèse vocale de secours ElevenLabs")
    print("-" * 80)

    # Extraire les répliques parlées
    spoken_text = extract_dialogue_from_script(script_out)
    print("\n[INFO] Texte extrait pour la voix off :")
    print(spoken_text[:500] + "\n...")

    if dry_run:
        print("[DRY-RUN] Simulation de la synthèse vocale ElevenLabs...")
        print("[SUCCESS] Fichier audio fictif simulé avec succès.")
    else:
        generate_audio = input("\nVoulez-vous générer le fichier MP3 de la voix off ElevenLabs maintenant ? (o/n) : ")
        if generate_audio.lower() == "o":
            if not elevenlabs_key or elevenlabs_key.startswith("__"):
                print("[ERROR] Clé ELEVENLABS_API_KEY non configurée ou placeholder dans le .env.")
                return

            output_audio_name = f"voiceover_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
            output_audio_path = os.path.join(obsidian_dir, output_audio_name)

            synthesis_success = generate_voiceover_tts(
                text=spoken_text, output_path=output_audio_path, api_key=elevenlabs_key, voice_id=elevenlabs_voice_id
            )
            if synthesis_success:
                print(
                    f"\n[INFO] Étape 3 terminée avec succès. Votre voix off est stockée dans Obsidian Outbox : {output_audio_path}"
                )
        else:
            print("[INFO] Synthèse vocale ignorée pour l'instant. Vous pourrez la lancer plus tard.")

    print("\n" + "=" * 80)
    print(" WORKFLOW INTERACTIF TERMINE AVEC SUCCÈS")
    print(" Les livrables sont prêts dans Obsidian Outbox.")
    print("=" * 80)


if __name__ == "__main__":
    is_dry = "--dry-run" in sys.argv
    run_interactive_planner(dry_run=is_dry)
