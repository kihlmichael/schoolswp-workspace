# Playbook AEO (GEO) : Optimiser les Articles d'Avis pour les Moteurs de Réponse IA

Ce playbook définit les standards de structuration sémantique et technique à appliquer sur **schoolswp.com** pour maximiser la visibilité de nos pages d'avis dans les moteurs de réponse à intelligence artificielle (Perplexity, Google Gemini, OpenAI Search, Bing Copilot). 

L'optimisation pour les moteurs de recherche génératifs (GEO - *Generative Engine Optimization* ou AEO - *Answer Engine Optimization*) exige une rigueur extrême dans l'exposition des faits, l'architecture sémantique et la modélisation des données.

---

## 1. Clarté sémantique et Entités Nommées

Les LLM (Large Language Models) n'indexent pas seulement des mots-clés, ils extraient des **entités** (sujet, produit, marque, concept) et cartographient leurs relations.

### Bonnes Pratiques :
*   **Identification claire du sujet dès l'introduction** : Le produit testé doit être défini formellement dès le premier paragraphe (ex. *"Amelia WP est une extension WordPress de gestion de réservations et de rendez-vous en ligne développée par TMS-Plugins"*).
*   **Utilisation de termes sans équivoque** : Éviter les pronoms vagues ("il", "cet outil") et répéter de manière fluide le nom du produit associé à ses attributs.
*   **Hiérarchie H2/H3 logique** : Les titres doivent contenir des entités claires. Éviter les titres mystérieux ou uniquement axés sur le clic, préférer des titres descriptifs (ex. *"Les fonctionnalités de réservation de Kadence Pro"* au lieu de *"Ce que vous allez adorer"*).

---

## 2. Structuration Factuelle (Bullet Points "Sentence-Level")

Les modèles de langage excellent dans l'extraction de synthèses factuelles présentées sous forme de listes. C'est le format idéal pour nourrir les fenêtres de contexte des moteurs GEO.

### Directives d'écriture :
*   **Format "Phrase-Clé" complète** : Chaque puce d'une liste d'avantages/inconvénients ou de caractéristiques doit être rédigée sous forme de phrase complète et explicite. Éviter les puces d'un seul mot.
    *   *Incorrect* : `- Vitesse`
    *   *Correct* : `- **Temps de chargement réduits** : L'extension génère un code HTML épuré qui améliore les Core Web Vitals sur mobile.`
*   **Tableaux de comparaison Pro/Cons** : Présenter systématiquement un tableau ou des colonnes séparant clairement les avantages (Pros) et inconvénients (Cons). Les IA recherchent activement ces oppositions pour formuler leurs jugements de valeur.

---

## 3. Données Structurées Riches (JSON-LD)

Le schéma JSON-LD est la passerelle de confiance entre notre base de données et les parsers d'IA. Il apporte une confirmation formelle et typée des données de la page.

### Spécifications requises pour chaque page d'avis :
Chaque article de test ou d'avis doit obligatoirement embarquer :
1.  **Un schéma `Review`** : Avec une note globale claire (`ratingValue`), une note maximale (`bestRating` = 5) et un décompte de votes réaliste (`ratingCount` / `reviewCount`).
2.  **Un schéma `SoftwareApplication` (ou `Product`)** : Spécifiant la catégorie de l'application (`applicationCategory`), le système d'exploitation (`operatingSystem` = "All" ou "WordPress"), et l'URL officielle du produit.
3.  **Des offres de prix (`offers`)** : Un tableau contenant les différents plans de prix (ex. Free Plan, Pro Plan) typés avec leur prix (`price`) et leur devise (`priceCurrency`), pour apparaître dans les comparaisons tarifaires des IA.

---

## 4. Formatage des Questions/Réponses (FAQ & Q&A)

Les moteurs GEO formulent souvent leurs réponses à partir de blocs Questions/Réponses explicites trouvés sur les sites de confiance.

### Méthodologie d'implémentation :
*   **Intégration d'un accordéon de FAQ** : En fin d'article, ajouter 3 à 5 questions récurrentes que se posent les utilisateurs sur le produit (ex. *"TasteWP est-il vraiment gratuit ?"*, *"Comment migrer un site de TasteWP vers mon hébergeur ?"*).
*   **Réponse directe à la première phrase** : La première phrase de chaque réponse de FAQ doit répondre directement et de manière concise à la question posée (ex. *"Oui, TasteWP propose un plan 100 % gratuit sans inscription..."*), suivie de détails explicatifs.

---

## 5. Preuve d'Expérience et de Fiabilité (EEAT)

L'algorithme de Google et les critères de sélection des IA favorisent les créateurs de contenu qui démontrent une expérience vécue directe (*Experience*).

### Éléments requis dans la rédaction :
*   **Contextualisation du test** : Préciser le protocole de test (ex. *"Nous avons testé SureForms pendant 3 semaines sur un serveur de staging local en y installant 15 extensions tierces pour mesurer la compatibilité..."*).
*   **Captures d'écran et mesures techniques** : Inclure des chiffres précis issus de tests de performance (temps de chargement GTmetrix, requêtes SQL évitées) plutôt que de simples affirmations génériques.
*   **Signature de l'auteur** : Associer chaque article à son auteur légitime doté d'une biographie d'expert dans l'écosystème WordPress (EEAT).
