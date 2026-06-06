import json
import time
import urllib.request
import urllib.error

def generate_part2():
    url = "http://127.0.0.1:11434/api/generate"
    
    # Prompt système et utilisateur avec Few-Shot Prompting pour la partie 2
    prompt = """Tu es un rédacteur web expert et pédagogue senior pour le média schoolsWP fondé par Michaël KIHL.
schoolsWP est un média francophone destiné aux freelances, créateurs de contenu, formateurs et solopreneurs WordPress.

Sujet de l'article : "Pourquoi installer un CRM local sur WordPress ?"
Tâche : Rédige uniquement la DEUXIÈME GRANDE PARTIE (la problématique des CRM SaaS cloud et les bénéfices du stockage local).

Règles de style absolues et non négociables ( schoolsWP ) :
1. TUTOIEMENT SYSTÉMATIQUE OBLIGATOIRE : Utilise exclusivement "tu", "toi", "ton", "tes", "tu peux". Le vouvoiement ("vous", "votre", "vos") est STRICTEMENT INTERDIT.
2. PAS DE SAAS FLUFF / PAS DE JARGON CREUX : Reste factuel, technique mais accessible. Pas de mots comme "disruptif", "game changer", "scalable", "hack", "révolutionnaire", "incroyable", "en un clic", "sans effort", "il suffit de".
3. LONGUEUR : Entre 250 et 350 mots. Développe bien tes paragraphes pour atteindre cette longueur.
4. STRUCTURE : Rédige en paragraphes fluides. Évite les listes à puces (bullet points) sauf si nécessaire. Utilise un titre de niveau 2 (H2) accrocheur et court pour commencer cette partie.
5. TRANSITION : Termine cette partie par une phrase de transition naturelle vers la partie suivante (la sélection pratique des plugins et l'installation).

---
EXEMPLE DE TON ET DE STYLE ATTENDU (Observe le tutoiement, le rythme et le ton pédagogue) :
"Tu passes des heures à configurer ton site WordPress pour qu'il soit rapide, sécurisé et agréable pour tes visiteurs. C'est parfait. Mais as-tu pensé à ton infrastructure de messagerie ? Chaque jour, des dizaines d'emails transactionnels partent de ton site : confirmations de commande WooCommerce, liens de réinitialisation de mot de passe, ou notifications de cours Tutor LMS. Pourtant, si tu te reposes sur le serveur SMTP par défaut de ton hébergeur, tu joues avec le feu. La plupart de ces messages critiques finissent directement dans le dossier spam de tes clients. Reprendre le contrôle de tes envois n'est pas une option, c'est une nécessité business absolue pour protéger ta délivrabilité et tes ventes."
---

Consignes de contenu pour cette partie (Les frictions cloud et les bénéfices du local) :
- Titre H2 : Trouve un titre court et percutant dans le style schoolsWP (ex: "La cage dorée des CRM SaaS (et comment WordPress t'en libère)").
- Contenu :
  * Le piège financier des CRM cloud (HubSpot, ActiveCampaign, etc.) : plus ta liste de contacts grandit, plus la facture explose, parfois pour des contacts inactifs ou de simples curieux.
  * La perte de souveraineté : tes données clients les plus précieuses sont stockées sur des serveurs américains. Si les tarifs augmentent ou si le service ferme ton compte, tu perds ton actif le plus précieux.
  * La complexité technique : connecter ton site WordPress à ces CRM requiert des usines à gaz d'intégration (Zapier, Make, webhooks complexes) qui ajoutent des coûts et créent des pannes régulières.
  * L'alternative locale : WordPress dispose déjà d'une base de données SQL robuste sous ton contrôle. Stocker ses données clients chez soi, c'est s'assurer une conformité RGPD native, une sécurité totale et 0€ d'abonnement tiers.
  * Transition : Annonce que pour passer de la théorie à la pratique, nous allons voir quels outils et plugins concrets installer directement sur ton site WordPress.

Rédige maintenant cette deuxième partie de l'article (respecte scrupuleusement la limite de 250-350 mots et le TUTOIEMENT) :"""

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
            print("ARTICLE DE RÉFÉRENCE schoolsWP — DEUXIÈME PARTIE GÉNÉRÉE")
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
            
    except urllib.error.URLError as e:
        print(f"\n[Erreur] Impossible de se connecter à Ollama : {e}")
        print("Vérifie qu'Ollama est bien lancé sur http://127.0.0.1:11434")

if __name__ == "__main__":
    generate_part2()
