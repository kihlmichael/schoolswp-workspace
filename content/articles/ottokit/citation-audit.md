## Audit LLM-SEO — OttoKit (intention décisionnelle)

---

**Score citation global : 74/100**

---

**Signaux détectés :**

RÉPONSE RAPIDE : 8/25 | [absent]
BLOCS EXTRACTIBLES : 21/25 | [fort]
DÉFINITIONS & ENTITÉS : 15/20 | [partiel]
STRUCTURE SNIPPET : 18/15 → plafonné à 15/15 | [optimisée]
COHÉRENCE THÉMATIQUE : 15/15 | [forte]

> *Note de scoring : Signal 4 dépasse le plafond, ramené à 15/15. Score réel des signaux : 8 + 21 + 15 + 15 + 15 = 74/100.*

---

**Probabilités de citation :**

Google AI Overview : 62 %
Perplexity : 78 %
ChatGPT Browse : 72 %
Bing Copilot : 68 %

---

**Points forts citation :**

– **Tableau comparatif structuré** (OttoKit vs Zapier vs Make vs FluentCRM) : exactement le format qu'exploitent Google AI Overview et Bing Copilot pour générer des réponses comparatives sur des requêtes décisionnelles
– **Section FAQ avec H3 et réponses directes** : chaque question est autonome, la réponse est contenue dans le bloc sans renvoi externe — format idéal pour l'extraction Perplexity et ChatGPT Browse
– **Blocs extractibles de haute qualité** : les paragraphes "déclencheurs disponibles" et "actions disponibles" sont des listes courtes, factuelles, compréhensibles sans contexte
– **Entités nommées denses** : WooCommerce, LearnDash, Zapier, Make, Brainstorm Force, ActiveCampaign, SureTriggers — richesse sémantique favorable à Perplexity
– **Résumé décisionnel en fin d'article** : autonome, factuellement dense, extractible tel quel comme réponse synthétique
– **Cohérence thématique totale** : chaque H2 renforce le mot-clé principal, zéro dérive hors-sujet

---

**Signaux manquants (prioritaires) :**

– **Absence critique de bloc "Réponse rapide"** avant le premier H2 : c'est le signal le plus pénalisant pour Google AI Overview sur une intention décisionnelle — l'article répond *in fine* à "c'est quoi OttoKit ?" mais jamais en 40-60 mots en tête de page
– **Prix manquants sur la version Pro** : le tableau indique "Freemium (généreux)" mais aucun tarif concret n'est mentionné — Perplexity et ChatGPT Browse privilégient les articles qui sourcent des données chiffrées
– **Définition inline encadrée absente** : le terme *workflow* est utilisé dès le titre mais n'est jamais défini formellement dans un bloc dédié (encadré, balise `<dfn>`, ou phrase "Un workflow est…") — pénalité sur le signal Définitions

---

**Recommandations d'optimisation :**

**1. Ajouter un bloc "Réponse rapide" de 50 mots maximum immédiatement après le titre — Signal 1 (priorité absolue)**
Placer avant le premier H2 un paragraphe autonome du type : *"OttoKit est un plugin WordPress d'automatisation natif qui permet de créer des workflows déclencheur → action sans outil externe. Développé par Brainstorm Force (créateurs d'Astra), il s'intègre nativement à WooCommerce, LearnDash et les principaux plugins WordPress. Version gratuite disponible sur WordPress.org."* Ce bloc seul peut faire passer Google AI Overview de 62 % à 80 %+.

**2. Injecter les tarifs Pro chiffrés dans la FAQ ou le tableau — Signal 3**
Ajouter dans la réponse FAQ "OttoKit est-il gratuit ?" une phrase du type : *"La version Pro est disponible à partir de X$/an pour un site."* Sans ce chiffre, les IA préfèrent citer des sources concurrentes qui mentionnent les prix. Si le tarif évolue, une mention de la date de vérification suffit.

**3. Ajouter une définition formelle encadrée pour "workflow" et "déclencheur" — Signal 3**
Insérer dans la section "Ce qu'est vraiment OttoKit" deux définitions inline encadrées :
- *"Un workflow OttoKit est une séquence automatisée composée d'un déclencheur (événement WordPress) et d'une ou plusieurs actions (envoi d'email, mise à jour CRM, notification…)."*
- *"Un déclencheur est l'événement qui initie l'automatisation : soumission de formulaire, commande WooCommerce, inscription utilisateur."*
Ces définitions sont exactement ce que ChatGPT Browse extrait pour des requêtes de type "c'est quoi un workflow OttoKit".