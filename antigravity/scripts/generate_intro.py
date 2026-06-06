import json
import time
import urllib.request
import urllib.error

def generate_introduction():
    url = "http://127.0.0.1:11434/api/generate"
    
    # Prompt système et utilisateur combinés pour le modèle local
    prompt = """Tu es un rédacteur web expert et pédagogue senior pour le média schoolsWP.
schoolsWP est un média francophone destiné aux freelances, créateurs de contenu, formateurs et solopreneurs WordPress.

Mission : Rédige uniquement l'INTRODUCTION d'un article de blog de référence.
Sujet : "Pourquoi installer un CRM local sur WordPress ?"

Règles de style impératives ( schoolsWP ) :
- TUTOIEMENT SYSTÉMATIQUE obligatoire. Ne jamais vouvoyer le lecteur.
- Ton : Humain, accessible, pédagogue, structuré, orienté business et pragmatisme.
- Style : Écris comme un artisan du web qui parle à un autre indépendant. Pas de jargon marketing creux.
- Explique le POURQUOI avant le COMMENT. Relie le sujet à la rentabilité et à l'autonomie.
- Phrases courtes (8 à 15 mots maximum). Direct au but.
- Pas de plan de texte, pas de puces (bullet points) ou de listes dans cette introduction. Rédige uniquement des paragraphes fluides.
- MOTS INTERDITS : disruptif, game changer, scalable, hack, révolutionnaire, incroyable, en un clic, sans effort, il suffit de.
- Longueur attendue : Entre 250 et 350 mots.
- Conclusion de l'introduction : Fais une transition naturelle vers la première partie sans utiliser de titre intermédiaire.

Contenu à aborder dans l'introduction :
- Accroche : Le piège des CRM SaaS (SaaS fatigue, abonnement mensuel lourd, perte de contrôle des données).
- Promesse : L'alternative d'installer un CRM local autonome directement dans WordPress pour reprendre le contrôle de ses données clients, réduire ses charges récurrentes à zéro et automatiser ses ventes.
- Transition fluide vers la suite.

Rédige l'introduction maintenant :"""

    payload = {
        "model": "qwen2.5:7b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "num_predict": 1000
        }
    }
    
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
    
    print("[Ollama] Connexion à l'instance locale...")
    start_time = time.time()
    
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            elapsed_time = time.time() - start_time
            
            text = res_data.get("response", "").strip()
            eval_count = res_data.get("eval_count", 0)
            done_reason = res_data.get("done_reason", "inconnu")
            total_duration_ns = res_data.get("total_duration", 0)
            
            # Calcul du nombre de mots
            word_count = len(text.split())
            
            print("\n" + "="*50)
            print("ARTICLE DE RÉFÉRENCE schoolsWP — INTRODUCTION GÉNÉRÉE")
            print("="*50 + "\n")
            print(text)
            print("\n" + "="*50)
            print("MÉTRIQUES DE GÉNÉRATION GPU")
            print("="*50)
            print(f"Nombre de mots            : environ {word_count} mots")
            print(f"Modèle utilisé            : {res_data.get('model', 'qwen2.5:7b')}")
            print(f"Paramètres de génération  : temperature=0.7, num_predict=1000")
            print(f"Tokens générés (eval_count): {eval_count} tokens")
            print(f"Raison de fin (done_reason): '{done_reason}'")
            print(f"Temps de génération total : {elapsed_time:.2f} secondes (moteur Ollama : {total_duration_ns / 1e9:.2f}s)")
            print("="*50)
            
    except urllib.error.URLError as e:
        print(f"\n[Erreur] Impossible de se connecter à Ollama : {e}")
        print("Vérifie qu'Ollama est bien lancé sur http://127.0.0.1:11434")

if __name__ == "__main__":
    generate_introduction()
