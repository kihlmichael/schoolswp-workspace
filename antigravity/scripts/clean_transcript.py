#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script pédagogique de nettoyage de transcription YouTube en local.
Utilise Ollama avec le modèle Qwen2.5:7b pour formater et polir 
les textes gratuitement sur ta carte graphique RTX 5070 Ti.

Usage :
    .venv/Scripts/python scripts/clean_transcript.py
"""

import os
import sys
import json
import urllib.request
import urllib.error

# Config locale
OLLAMA_HOST = "http://127.0.0.1:11434"
MODEL_NAME = "qwen2.5:7b"

# Exemple de transcription YouTube brute et désordonnée
DUMMY_TRANSCRIPT = """
alors bonjour à tous aujourd'hui on va voir comment installer tutor lms et en fait
c'est super simple mais y a des pièges à éviter du coup genre faut faire attention
à la configuration et tout d'abord vous devez aller dans les extensions de wordpress
et puis chercher tutor lms et cliquer sur installer puis activer mais attendez y a
un assistant de configuration et faut pas tout valider par défaut parce que sinon
votre site va ressembler à une usine à gaz et on veut pas ça chez nous on veut faire
un truc propre et carré
"""

def check_ollama_running() -> bool:
    """Vérifie si le service Ollama est actif sur le port 11434."""
    try:
        with urllib.request.urlopen(f"{OLLAMA_HOST}/api/tags", timeout=2) as response:
            return response.status == 200
    except (urllib.error.URLError, ConnectionRefusedError):
        return False

def check_model_installed(model_name: str) -> bool:
    """Vérifie si le modèle spécifié est déjà téléchargé dans Ollama."""
    try:
        with urllib.request.urlopen(f"{OLLAMA_HOST}/api/tags") as response:
            data = json.loads(response.read().decode("utf-8"))
            models = [m["name"] for m in data.get("models", [])]
            # Ollama ajoute souvent :latest ou des tags, on vérifie la correspondance
            return any(model_name in m for m in models)
    except Exception:
        return False

def call_local_llm(system_prompt: str, user_prompt: str) -> str:
    """Effectue un appel direct à l'API locale d'Ollama sans dépendances externes."""
    url = f"{OLLAMA_HOST}/api/chat"
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "stream": False,
        "options": {
            "temperature": 0.3
        }
    }
    
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
    
    try:
        print(f"-> Envoi de la requête à Ollama ({MODEL_NAME})...")
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            return res_data["message"]["content"]
    except Exception as e:
        return f"Erreur lors de l'appel LLM : {e}"

def main():
    print("=== PIPELINE DE NETTOYAGE IA LOCALE ===")
    
    # 1. Vérifications initiales
    if not check_ollama_running():
        print(f"[ERREUR] Ollama ne semble pas démarré sur {OLLAMA_HOST}.")
        print("-> Action requise : Lance l'application Ollama dans Windows.")
        sys.exit(1)
        
    print("[OK] Ollama est bien en cours d'exécution.")
    
    if not check_model_installed(MODEL_NAME):
        print(f"[ALERTE] Le modèle '{MODEL_NAME}' n'est pas détecté dans ton instance Ollama.")
        print(f"-> Action requise : Lance la commande suivante dans PowerShell :")
        print(f"   ollama pull {MODEL_NAME}")
        sys.exit(1)
        
    print(f"[OK] Le modèle '{MODEL_NAME}' est disponible.")
    
    # 2. Définition des prompts (Alignés sur ton style direct et directifs)
    system_prompt = (
        "Tu es un assistant éditorial ultra-précis pour le média schoolsWP.\n"
        "Ton rôle est de nettoyer et structurer des transcriptions audio brutes en français.\n"
        "Règles strictes :\n"
        "- Supprime les tics de langage (genre, alors, du coup, en fait, etc.).\n"
        "- Utilise le tutoiement systématique.\n"
        "- N'utilise JAMAIS 'nous', 'notre' ou 'on vous'. Écris au 'je' ou utilise des tournures directes.\n"
        "- Structure le texte avec des listes à puces et des titres clairs (Markdown).\n"
        "- Reste concis, direct et pragmatique.\n"
        "- N'invente pas d'informations qui ne sont pas dans le texte d'origine.\n"
        "- Rends le texte fluide et agréable à lire."
    )
    
    user_prompt = f"Voici la transcription brute à nettoyer :\n---\n{DUMMY_TRANSCRIPT}\n---"
    
    # 3. Traitement
    print("\n--- Transcription brute reçue ---")
    print(DUMMY_TRANSCRIPT.strip())
    print("---------------------------------\n")
    
    cleaned_text = call_local_llm(system_prompt, user_prompt)
    
    print("--- Résultat nettoyé et formaté par ton GPU (Gratuit !) ---")
    print(cleaned_text)
    print("----------------------------------------------------------\n")
    
    print("Félicitations ! Tu viens d'exécuter ta première tâche d'agent local.")

if __name__ == "__main__":
    main()
