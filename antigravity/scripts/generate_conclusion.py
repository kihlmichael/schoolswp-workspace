import json
import time
import urllib.request
import urllib.error

def generate_conclusion():
    url = "http://127.0.0.1:11434/api/generate"
    
    # Prompt système et utilisateur avec Few-Shot Prompting pour la conclusion
    prompt = """Tu es un rédacteur web expert et pédagogue senior pour le média schoolsWP fondé par Michaël KIHL.
schoolsWP est un média francophone destiné aux freelances, créateurs de contenu, formateurs et solopreneurs WordPress.

Sujet de l'article : "Pourquoi installer un CRM local sur WordPress ?"
Tâche : Rédige uniquement la CONCLUSION de cet article (la synthèse philosophique et le passage à l'action).

Règles de style absolues et non négociables ( schoolsWP ) :
1. TUTOIEMENT SYSTÉMATIQUE OBLIGATOIRE : Utilise exclusivement "tu", "toi", "ton", "tes", "tu peux". Le vouvoiement ("vous", "votre", "vos") est STRICTEMENT INTERDIT.
2. PAS DE SAAS FLUFF / PAS DE JARGON CREUX : Reste factuel, technique mais accessible. Pas de mots comme "disruptif", "game changer", "scalable", "hack", "révolutionnaire", "incroyable", "en un clic", "sans effort", "il suffit de".
3. LONGUEUR : Entre 150 et 250 mots. Développe bien tes paragraphes pour atteindre cette longueur.
4. STRUCTURE : Rédige en paragraphes fluides. Évite les listes à puces. Utilise un titre de niveau 2 (H2) court et incitatif à l'action.
5. FIN : Termine l'article sur une note forte et inspirante sur la liberté et la souveraineté numérique.

---
EXEMPLE DE TON ET DE STYLE ATTENDU (Observe le tutoiement, le rythme et le ton pédagogue) :
"Tu passes des heures à configurer ton site WordPress pour qu'il soit rapide, sécurisé et agréable pour tes visiteurs. C'est parfait. Mais as-tu pensé à ton infrastructure de messagerie ? Chaque jour, des dizaines d'emails transactionnels partent de ton site : confirmations de commande WooCommerce, liens de réinitialisation de mot de passe, ou notifications de cours Tutor LMS. Pourtant, si tu te reposes sur le serveur SMTP par défaut de ton hébergeur, tu joues avec le feu. La plupart de ces messages critiques finissent directement dans le dossier spam de tes clients. Reprendre le contrôle de tes envois n'est pas une option, c'est une nécessité business absolue pour protéger ta délivrabilité et tes ventes."
---

Consignes de contenu pour cette partie (La Conclusion) :
- Titre H2 : Trouve un titre court et inspirant (ex: "Prends le contrôle de tes données dès aujourd'hui").
- Contenu :
  * Fais une synthèse rapide : le CRM local n'est pas juste une économie financière, c'est une décision philosophique pour reprendre possession de ton actif le plus précieux.
  * Rappelle que ton site WordPress est une plateforme ouverte capable de rivaliser avec les meilleurs outils propriétaires si tu l'équipes des bonnes extensions.
  * Incite le lecteur à faire le premier pas : installer la version gratuite de FluentCRM et créer ses premières listes de contacts.
  * Note de fin : La liberté numérique commence par les outils que tu possèdes réellement.

Rédige maintenant la conclusion de l'article (respecte scrupuleusement la limite de 150-250 mots et le TUTOIEMENT) :"""

    payload = {
        "model": "qwen2.5:7b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "num_predict": 1000,
            "top_p": 0.9
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
            print("ARTICLE DE RÉFÉRENCE schoolsWP — CONCLUSION GÉNÉRÉE")
            print("="*50 + "\n")
            print(text)
            print("\n" + "="*50)
            print("MÉTRIQUES DE GÉNÉRATION GPU")
            print("="*50)
            print(f"Nombre de mots            : environ {word_count} mots")
            print(f"Modèle utilisé            : {res_data.get('model', 'qwen2.5:7b')}")
            print(f"Paramètres de génération  : temperature=0.7, top_p=0.9, num_predict=1000")
            print(f"Tokens générés (eval_count): {eval_count} tokens")
            print(f"Raison de fin (done_reason): '{done_reason}'")
            print(f"Temps de génération total : {elapsed_time:.2f} secondes (moteur Ollama : {total_duration_ns / 1e9:.2f}s)")
            print("="*50)
            
            # Save the result in drafts for safety
            draft_path = r"d:\ANTIGRAVITY\drafts\generated_conclusion.txt"
            with open(draft_path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"[OK] Saved to {draft_path}")
            
    except urllib.error.URLError as e:
        print(f"\n[Erreur] Impossible de se connecter à Ollama : {e}")
        print("Vérifie qu'Ollama est bien lancé sur http://127.0.0.1:11434")

if __name__ == "__main__":
    generate_conclusion()
