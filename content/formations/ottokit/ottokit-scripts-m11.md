# Scripts vidéo - Module 11 : AI Agents et MCP : l'automatisation intelligente

**Formation** : Maîtriser OttoKit
**Module** : M11 - AI Agents et MCP : l'automatisation intelligente
**Leçons** : 8 vidéos + 1 quiz
**Durée totale** : ~55 min de vidéo
**Date** : 2026-03-30

---

## Leçon 11.1 - AI Agents : qu'est-ce que c'est et pourquoi c'est different

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides comparatifs

---

**[INTRO - face caméra]**

Depuis le debut de cette formation, tu construis des workflows. Des étapes fixes, dans un ordre précis, avec des conditions prévisibles. Ça fonctionne. Mais certaines situations ne rentrent pas dans un schéma fixe. C'est là que les AI Agents entrent en jeu.

**[ÉCRAN - slide "Workflow vs Agent - la difference fondamentale"]**

Un **workflow**, c'est une recette de cuisine. Tu suis les étapes dans l'ordre. Si l'étape 3 échoue, tout s'arrete. Les décisions sont binaires : oui ou non, vrai ou faux.

Un **AI Agent**, c'est un assistant qui reçoit un objectif et décide seul comment l'atteindre. Il choisit quels outils utiliser, dans quel ordre, et s'adapte en fonction de ce qu'il trouve.

| | Workflow | AI Agent |
|---|---|---|
| Fonctionnement | Étapes fixes, ordre prédéfini | Objectif défini, exécution flexible |
| Decisions | Conditions binaires (if/else) | Raisonnement contextuel |
| Adaptatif | Non - même chemin à chaque fois | Oui - s'adapte aux données reçues |
| Previsibilite | Très haute | Modérée |
| Cout en tasks | Faible (1 task par étape) | Plus élevé (1 task par action de l'agent) |

**[ÉCRAN - slide "Exemple concret"]**

Imagine un étudiant qui envoie un email avec cette question : "Je n'arrive pas a acceder a mon cours, mon paiement est passe mais rien ne s'affiche."

Avec un **workflow**, tu pourrais :
- Verifier si le mot "paiement" est present → envoyer une réponse type
- Verifier si le mot "cours" est present → envoyer une autre reponse type

Le probleme : la question contient les deux. Le workflow ne sait pas quoi faire - ou envoie la mauvaise reponse.

Avec un **AI Agent** :
- L'agent lit la question, comprend le contexte
- Il vérifie le statut du paiement dans Stripe
- Il vérifie l'inscription dans TutorLMS
- Il rédige une réponse adaptée au probleme specifique

L'agent raisonne. Le workflow execute.

**[ÉCRAN - slide "Quand utiliser un agent"]**

Utilise un AI Agent quand :
- Les inputs sont imprévisibles (emails, questions libres, messages varies)
- La réponse dépend du contexte (pas de chemin unique)
- Plusieurs outils doivent être interrogés avant de décider

Garde un workflow classique quand :
- Le processus est prévisible (nouvelle commande → email de confirmation)
- Les etapes sont toujours les memes
- Tu veux un coût en tasks minimal

**[TRANSITION - face caméra]**

Tu vois la différence. Un workflow est un automate. Un agent est un assistant. Dans la prochaine lecon, tu vas créer ton premier agent directement dans OttoKit.

---

**Points cles**
- Un workflow exécute des étapes fixes ; un agent décide comment atteindre un objectif
- L'agent s'adapte au contexte, le workflow suit toujours le même chemin
- Les agents consomment plus de tasks que les workflows classiques
- Utilise un agent quand les inputs sont imprévisibles et le contexte variable

**Mots-cles SEO**
- OttoKit AI Agent
- différence workflow agent IA
- AI Agent WordPress automatisation
- OttoKit agent intelligent

---

## Leçon 11.2 - Crée ton premier AI Agent dans OttoKit

**Durée** : 8 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit interface agent

---

**[INTRO - face caméra]**

Tu sais ce qu'est un agent. Maintenant, tu en crees un. OttoKit integre les AI Agents directement dans son interface. Pas besoin de code, pas besoin d'un outil externe. Tout se fait depuis le dashboard.

**[ÉCRAN - screencast OttoKit dashboard]**

[Ouvre OttoKit - app.ottokit.com]
[Dans la barre laterale, clique sur "AI Agents"]

La section AI Agents est separee des workflows. C'est un espace dedie. Tu y retrouves tes agents crees, leur historique et leurs parametres.

**[ÉCRAN - screencast creation de l'agent]**

[Clique sur "Create Agent" ou "New Agent"]
[Un formulaire s'ouvre avec plusieurs champs]

Voici les elements a configurer :

**[ÉCRAN - screencast champ "Name"]**

[Tape le nom : "Assistant Support Formation"]

Le nom identifie ton agent dans le dashboard. Choisis quelque chose de clair.

**[ÉCRAN - screencast champ "Objective" / "Instructions"]**

[Dans le champ objectif ou instructions, tape :]

```
Tu es l'assistant support de schoolsWP. Quand un etudiant pose une question :
1. Identifie le sujet (acces cours, paiement, technique, contenu)
2. Cherche la reponse dans la FAQ
3. Si la reponse n'est pas dans la FAQ, propose une reponse basee sur le contexte
4. Reponds toujours en francais, avec le tutoiement
```

L'objectif, c'est le prompt de ton agent. C'est ici que tu lui dis ce qu'il doit faire, comment raisonner, et dans quel cadre. Sois precis : plus les instructions sont claires, meilleur sera le resultat.

**[ÉCRAN - screencast champ "Model"]**

[Selectionne le modele : GPT-4o, Claude, ou le modele disponible]
[Pointe les options disponibles]

Tu choisis le modele de langage. OttoKit supporte plusieurs fournisseurs. Le choix depend de ta cle API et de ton budget. GPT-4o et Claude sont les plus performants pour le raisonnement.

**[ÉCRAN - screencast section "Tools" / "Actions"]**

[Montre la section ou l'on ajoute les outils de l'agent]
[Pour l'instant, ne connecte aucun outil - on le fait dans la lecon suivante]

Les outils, c'est ce que l'agent peut faire. Pour l'instant, on ne connecte rien. L'agent fonctionnera en mode "reponse uniquement". On ajoutera les outils dans la lecon 11.3.

**[ÉCRAN - screencast bouton "Save" ou "Create"]**

[Clique sur "Save" ou "Create"]
[Montre l'agent cree dans la liste]

Ton agent est cree. Il apparait dans la liste.

**[ÉCRAN - screencast test de l'agent]**

[Clique sur l'agent pour l'ouvrir]
[Montre l'interface de test / chat]
[Tape : "Je n'arrive pas a acceder a mon cours, j'ai paye hier"]
[Montre la reponse de l'agent]

OttoKit fournit une interface de test. Tu peux discuter avec ton agent pour verifier qu'il repond correctement. Ici, l'agent identifie le probleme et propose une reponse adaptee.

[Tape une deuxieme question : "Comment telecharger mon certificat ?"]
[Montre la reponse]

Deuxieme test. L'agent comprend le contexte et adapte sa reponse. C'est ca la difference avec un workflow : chaque reponse est differente.

**[ÉCRAN - slide "Bonnes pratiques pour le prompt"]**

- Definis clairement le role de l'agent (support, redacteur, analyste)
- Liste les etapes de raisonnement (1. Identifie, 2. Cherche, 3. Reponds)
- Precise le ton et la langue (francais, tutoiement)
- Indique ce que l'agent ne doit pas faire (pas de promesse de remboursement, pas de donnees personnelles)

**[TRANSITION - face caméra]**

Ton agent existe et il repond. Mais pour l'instant, il ne peut que parler. Dans la prochaine lecon, on lui donne des outils pour qu'il puisse agir : envoyer des emails, consulter des sheets, creer des taches.

---

**Points cles**
- Les AI Agents se creent depuis la section "AI Agents" du dashboard OttoKit
- Le prompt (objectif/instructions) determine le comportement de l'agent
- L'interface de test permet de valider les reponses avant la mise en production
- Un bon prompt est precis, structure et definit les limites de l'agent

**Mots-cles SEO**
- creer AI Agent OttoKit
- OttoKit agent IA configuration
- AI Agent WordPress support
- configurer agent intelligent OttoKit

---

## Leçon 11.3 - Donne des outils a ton agent : actions et integrations

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit interface agent

---

**[INTRO - face caméra]**

Un agent sans outils, c'est un consultant qui donne des conseils mais ne peut rien faire. Pour que ton agent passe a l'action, tu dois lui donner acces a des outils : envoyer un email, lire un Google Sheet, creer un article WordPress. C'est ce qu'on fait maintenant.

**[ÉCRAN - slide "Agent + Outils = Action"]**

L'agent recoit une question ou une demande. Avec ses outils, il peut :

1. **Chercher** une information (lire un Google Sheet, consulter une base FAQ)
2. **Agir** (envoyer un email, creer une tache, mettre a jour un contact)
3. **Combiner** plusieurs actions selon le contexte

Sans outils, il ne fait que repondre. Avec des outils, il agit.

**[ÉCRAN - screencast OttoKit - ouvrir l'agent]**

[Ouvre l'agent "Assistant Support Formation" cree dans la lecon 11.2]
[Clique sur "Edit" ou accede aux parametres]
[Navigue vers la section "Tools" / "Actions" / "Integrations"]

On reprend l'agent de la lecon precedente. Dans la section outils, tu vois la liste des integrations que tu peux connecter.

**[ÉCRAN - screencast ajout de Gmail]**

[Clique sur "Add Tool" ou "Add Integration"]
[Tape "Gmail" dans la recherche]
[Selectionne "Gmail"]
[Selectionne l'action "Send Email"]
[Selectionne la connexion Gmail existante]
[Configure les permissions - l'agent peut envoyer des emails]

Premier outil : Gmail. On donne a l'agent la capacite d'envoyer des emails. Quand il decidera qu'un email est necessaire, il pourra le faire.

**[ÉCRAN - screencast ajout de Google Sheets]**

[Clique sur "Add Tool"]
[Tape "Google Sheets" dans la recherche]
[Selectionne "Google Sheets"]
[Selectionne l'action "Read Row" ou "Get Data"]
[Selectionne la connexion Google existante]
[Selectionne le spreadsheet FAQ - montre les colonnes : Question, Reponse, Categorie]

Deuxieme outil : Google Sheets en lecture. L'agent pourra consulter ta FAQ. Tu pointes vers le spreadsheet qui contient les questions et reponses frequentes.

**[ÉCRAN - screencast resume des outils]**

[Montre la liste des outils ajoutes a l'agent : Gmail (Send Email) + Google Sheets (Read Row)]
[Clique sur "Save"]

L'agent a maintenant deux outils. Il peut lire la FAQ dans Google Sheets et envoyer un email si necessaire. Le choix d'utiliser tel ou tel outil, c'est l'agent qui le fait - pas toi.

**[ÉCRAN - screencast test de l'agent avec outils]**

[Ouvre l'interface de test]
[Tape : "Je n'arrive pas a acceder a mon cours WordPress, j'ai paye hier"]
[Montre la reponse de l'agent]
[Pointe les etapes visibles : "Searching FAQ..." → "Found matching answer" → "Drafting response"]

Cette fois, l'agent ne se contente pas d'inventer une reponse. Il consulte d'abord la FAQ dans Google Sheets. S'il trouve une reponse correspondante, il l'utilise. Tu vois les etapes dans le log : recherche, resultat, reponse.

[Tape : "Envoie-moi un recapitulatif par email a jean@test.com"]
[Montre l'agent qui prepare l'envoi d'email]

Et si tu lui demandes d'envoyer un email, il utilise Gmail. L'agent choisit l'outil adapte a la demande.

**[ÉCRAN - slide "Gerer les permissions"]**

Quelques regles importantes :

- Ne donne a l'agent que les outils dont il a besoin. Pas plus.
- Un agent support n'a pas besoin d'acceder a WooCommerce.
- Si un outil est sensible (suppression, modification), active le Human-in-the-Loop (lecon suivante).
- Chaque outil consomme des tasks quand l'agent l'utilise.

**[TRANSITION - face caméra]**

Ton agent sait maintenant chercher et agir. Mais lui faire confiance les yeux fermes, c'est risque. Dans la prochaine lecon, on met en place un garde-fou : l'approbation humaine avant chaque action sensible.

---

**Points cles**
- Les outils donnent a l'agent la capacite d'agir (email, lecture de donnees, actions WP)
- L'agent choisit quel outil utiliser en fonction du contexte
- Ne connecte que les outils strictement necessaires
- Chaque utilisation d'outil consomme des tasks

**Mots-cles SEO**
- OttoKit agent outils integrations
- AI Agent Gmail Google Sheets OttoKit
- donner actions agent IA OttoKit
- agent WordPress outils automatisation

---

## Leçon 11.4 - Human-in-the-Loop : garde le controle sur ton agent

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit interface agent

---

**[INTRO - face caméra]**

Un agent qui envoie des emails tout seul, ca peut etre utile. Ca peut aussi etre dangereux. Imagine qu'il reponde a un client avec des informations erronees, ou qu'il supprime un contact par erreur. Le Human-in-the-Loop, c'est ton filet de securite : l'agent propose, tu approuves.

**[ÉCRAN - slide "Le principe"]**

Sans Human-in-the-Loop :
1. L'etudiant pose une question
2. L'agent decide de la reponse
3. L'agent envoie l'email directement
4. Tu decouvres l'email apres coup

Avec Human-in-the-Loop :
1. L'etudiant pose une question
2. L'agent decide de la reponse
3. L'agent te soumet la reponse pour approbation
4. Tu approuves (ou modifies) → l'email part

La difference : tu restes dans la boucle. L'agent fait le travail, tu valides le resultat.

**[ÉCRAN - screencast OttoKit - activer le Human-in-the-Loop]**

[Ouvre l'agent "Assistant Support Formation"]
[Navigue vers les parametres / Settings]
[Trouve l'option "Human-in-the-Loop" ou "Require Approval"]
[Active l'option]

L'activation est simple. Tu coches une case dans les parametres de l'agent. A partir de maintenant, chaque action de l'agent sera soumise a ton approbation.

**[ÉCRAN - screencast configuration de la notification]**

[Montre les options de notification : email, dashboard, webhook]
[Selectionne "Email notification" - tape ton adresse email]
[Clique sur "Save"]

Tu choisis comment etre notifie. Par email, c'est le plus courant. Tu recois un message avec la proposition de l'agent et un lien pour approuver ou rejeter.

**[ÉCRAN - screencast test avec approbation]**

[Ouvre l'interface de test de l'agent]
[Tape : "Envoie un email de bienvenue a nouvel-eleve@test.com"]
[Montre que l'agent prepare l'action mais ne l'execute pas]
[Montre le message "Awaiting approval" ou "Pending review"]

L'agent a prepare l'email. Mais au lieu de l'envoyer, il attend ton approbation. Tu vois le statut "En attente" dans l'interface.

**[ÉCRAN - screencast approbation dans le dashboard]**

[Montre la notification dans le dashboard OttoKit - ou dans l'email recu]
[Montre le detail de l'action proposee : destinataire, objet, contenu de l'email]
[Clique sur "Approve" / "Approuver"]
[Montre que l'action s'execute apres approbation]

Tu vois exactement ce que l'agent veut faire avant qu'il le fasse. Tu peux approuver, rejeter, ou modifier. C'est toi qui as le dernier mot.

[Montre aussi le bouton "Reject" / "Rejeter"]

Si tu rejetes, l'action est annulee. L'agent ne fait rien.

**[ÉCRAN - slide "Quand activer le Human-in-the-Loop"]**

| Scenario | Human-in-the-Loop |
|---|---|
| Agent de support qui repond aux etudiants | Oui - les premieres semaines au minimum |
| Agent qui lit des donnees sans modifier | Non - pas de risque |
| Agent qui envoie des emails de relance | Oui - jusqu'a ce que tu aies confiance |
| Agent qui cree des articles WordPress | Oui - toujours relire avant publication |
| Agent qui ajoute des lignes dans un Sheet | Non - impact faible |

La regle : si l'action est visible par tes clients ou modifie des donnees sensibles, active l'approbation. Tu pourras la desactiver plus tard quand tu seras confiant.

**[ÉCRAN - slide "L'agent apprend de tes corrections"]**

Chaque fois que tu approuves ou rejetes une action, tu donnes un signal a l'agent. Avec le temps :

- Les reponses s'ameliorent
- Tu gagnes en confiance
- Tu peux desactiver l'approbation sur certaines actions

C'est une montee en competence progressive. Tu ne passes pas de "controle total" a "confiance aveugle". Tu augmentes la liberte de l'agent graduellement.

**[TRANSITION - face caméra]**

Ton agent est sous controle. Tu sais exactement ce qu'il fait avant qu'il le fasse. Dans la prochaine lecon, on passe a un sujet different : le MCP, le protocole qui permet a Claude ou ChatGPT de piloter OttoKit directement.

---

**Points cles**
- Human-in-the-Loop = l'agent propose, tu approuves avant execution
- Active l'approbation pour toute action visible par tes clients
- La notification peut etre par email ou dans le dashboard
- Desactive progressivement quand tu as confiance dans l'agent

**Mots-cles SEO**
- OttoKit Human-in-the-Loop
- approbation agent IA OttoKit
- controler AI Agent WordPress
- securite agent automatisation OttoKit

---

## Leçon 11.5 - MCP (Model Context Protocol) : connecte Claude et ChatGPT

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides explicatifs, schema d'architecture

---

**[INTRO - face caméra]**

Tu utilises peut-etre Claude, ChatGPT ou Cursor pour travailler. Et tu utilises OttoKit pour automatiser ton WordPress. Jusqu'ici, ce sont deux mondes separes. Le MCP - Model Context Protocol - cree un pont entre les deux. Ton LLM peut appeler OttoKit directement.

**[ÉCRAN - slide "Le probleme actuel"]**

Aujourd'hui, si tu veux publier un article sur WordPress depuis Claude :

1. Tu generes le texte dans Claude
2. Tu copies le texte
3. Tu ouvres WordPress
4. Tu colles le texte
5. Tu configures la categorie, le slug, l'image
6. Tu cliques sur "Publier"

Six etapes manuelles. Le MCP reduit ca a une seule commande.

**[ÉCRAN - slide "MCP - le protocole universel"]**

MCP signifie **Model Context Protocol**. C'est un standard ouvert cree par Anthropic. Son role : permettre a un LLM (Claude, ChatGPT, Cursor) de communiquer avec des outils externes.

Concretement, MCP definit :
- **Quels outils** le LLM peut utiliser (ex: "creer un article WordPress")
- **Comment** les appeler (parametres, format)
- **Ce qu'il recoit** en retour (confirmation, erreur, donnees)

C'est un langage commun entre les IA et les outils.

**[ÉCRAN - schema d'architecture MCP]**

```
  Claude / ChatGPT / Cursor
           |
           | (requete MCP)
           v
     Serveur MCP OttoKit
           |
           | (actions)
           v
   WordPress  Google  Slack  Email  ...
```

Le LLM envoie une requete au serveur MCP d'OttoKit. Le serveur MCP traduit cette requete en actions OttoKit. OttoKit execute les actions sur tes apps connectees.

**[ÉCRAN - slide "Ce que ca change"]**

Avec MCP, tu peux dire a Claude :

- "Publie cet article en brouillon sur le blog schoolsWP dans la categorie LMS"
- "Envoie un email de bienvenue a marie@test.com via Gmail"
- "Ajoute cette ligne dans le Google Sheet des inscriptions"

Et Claude le fait. Pas en copiant-collant. En appelant directement OttoKit.

**[ÉCRAN - slide "OttoKit comme serveur MCP"]**

OttoKit propose un serveur MCP natif. Ca signifie :

- Tu actives le mode developpeur dans OttoKit
- Tu generes une URL de serveur MCP
- Tu connectes cette URL a Claude Desktop, ChatGPT, Cursor ou Claude Code
- Ton LLM voit les actions OttoKit comme des outils disponibles

Les 1 300+ integrations d'OttoKit deviennent accessibles depuis ton LLM.

**[ÉCRAN - slide "Qui supporte MCP ?"]**

| Outil | Support MCP |
|---|---|
| Claude Desktop | Oui (natif) |
| Claude Code | Oui (natif) |
| ChatGPT (plugins/actions) | Via adaptateur |
| Cursor | Oui (natif) |
| VS Code + Copilot | Via extension |

Le support s'elargit rapidement. Anthropic a cree MCP comme un standard ouvert - tout le monde peut l'adopter.

**[TRANSITION - face caméra]**

Tu comprends ce que MCP apporte : ton IA pilote tes outils directement. Dans la prochaine lecon, on configure le serveur MCP dans OttoKit et on connecte un LLM.

---

**Points cles**
- MCP (Model Context Protocol) permet aux LLM d'appeler des outils externes
- OttoKit propose un serveur MCP natif avec ses 1 300+ integrations
- Claude, Cursor et ChatGPT supportent MCP
- MCP elimine le copier-coller entre l'IA et les outils

**Mots-cles SEO**
- OttoKit MCP Model Context Protocol
- connecter Claude OttoKit
- MCP WordPress automatisation
- ChatGPT OttoKit integration

---

## Leçon 11.6 - Configure un MCP server OttoKit

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit + Claude Desktop

---

**[INTRO - face caméra]**

On passe a la pratique. Tu vas activer le serveur MCP dans OttoKit, recuperer l'URL de connexion, et la brancher sur Claude Desktop. A la fin de cette lecon, tu pourras publier sur WordPress directement depuis Claude.

**[ÉCRAN - screencast OttoKit - activer le Developer Mode]**

[Ouvre OttoKit - app.ottokit.com]
[Va dans Settings / Reglages]
[Cherche l'option "Developer Mode" ou "MCP"]
[Active le Developer Mode]

Premiere etape : active le mode developpeur. C'est necessaire pour acceder aux fonctionnalites MCP. Le mode developpeur ne change rien a tes workflows existants - il ajoute des options supplementaires.

**[ÉCRAN - screencast OttoKit - creation du serveur MCP]**

[Navigue vers la section "MCP" ou "MCP Servers"]
[Clique sur "Create MCP Server" ou "New Server"]
[Donne un nom : "schoolsWP MCP Server"]

On cree un serveur MCP. C'est ce serveur qui exposera tes actions OttoKit aux LLM.

**[ÉCRAN - screencast OttoKit - selection des outils]**

[Montre la liste des outils/actions que tu peux exposer via MCP]
[Selectionne : "WordPress - Create Post"]
[Selectionne : "Gmail - Send Email"]
[Selectionne : "Google Sheets - Add Row"]
[Clique sur "Save"]

Tu choisis quels outils rendre accessibles. Ne coche pas tout - selectionne uniquement ce que tu veux que le LLM puisse faire. C'est le meme principe que les permissions d'un agent : le minimum necessaire.

**[ÉCRAN - screencast OttoKit - copie de l'URL MCP]**

[Montre l'URL du serveur MCP generee par OttoKit]
[Copie l'URL - format : https://app.ottokit.com/mcp/xxx-xxx-xxx]

OttoKit te donne une URL unique. C'est l'adresse de ton serveur MCP. Tu vas la coller dans ton LLM.

**[ÉCRAN - screencast Claude Desktop - configuration]**

[Ouvre Claude Desktop]
[Va dans Settings > MCP Servers (ou le fichier de configuration)]
[Montre le fichier de configuration MCP :]

```json
{
  "mcpServers": {
    "ottokit": {
      "url": "https://app.ottokit.com/mcp/xxx-xxx-xxx"
    }
  }
}
```

[Enregistre et redemarre Claude Desktop]

Dans Claude Desktop, tu ajoutes le serveur MCP dans la configuration. Le format est simple : un nom et une URL. Apres redemarrage, Claude voit les outils OttoKit.

**[ÉCRAN - screencast Claude Desktop - verification]**

[Ouvre une nouvelle conversation dans Claude]
[Montre l'icone ou l'indicateur MCP qui confirme la connexion]
[Montre la liste des outils disponibles : WordPress Create Post, Gmail Send Email, Google Sheets Add Row]

Claude affiche les outils connectes. Tu vois les trois actions qu'on a configurees. Tout est pret.

**[ÉCRAN - screencast Claude Desktop - test reel]**

[Tape dans Claude : "Cree un brouillon d'article WordPress avec le titre 'Les 5 meilleurs plugins LMS en 2026' dans la categorie LMS"]
[Montre Claude qui appelle l'outil OttoKit]
[Montre la confirmation : article cree en brouillon]

Claude envoie la commande au serveur MCP. OttoKit cree l'article en brouillon sur WordPress. Tu n'as pas quitte Claude. Pas de copier-coller, pas d'onglet WordPress ouvert.

[Ouvre WordPress admin - montre le brouillon dans la liste des articles]

Et voila le brouillon dans WordPress. Titre, categorie, tout est la.

**[ÉCRAN - slide "MCP + Claude Code"]**

Pour les utilisateurs techniques : Claude Code supporte aussi MCP. Tu peux ajouter le serveur OttoKit dans ton fichier `.mcp.json` :

```json
{
  "ottokit": {
    "url": "https://app.ottokit.com/mcp/xxx-xxx-xxx"
  }
}
```

Depuis le terminal, tu peux alors dire a Claude Code : "Publie cet article sur WordPress" - et il le fait via OttoKit. C'est exactement ce qu'on utilise chez schoolsWP pour automatiser la publication.

**[TRANSITION - face caméra]**

Ton serveur MCP est en place. Claude peut maintenant piloter OttoKit. Dans la prochaine lecon, on explore trois cas d'usage concrets d'AI Agents pour ton business WordPress.

---

**Points cles**
- Le Developer Mode est necessaire pour activer MCP dans OttoKit
- Tu choisis quels outils exposer via le serveur MCP (principe du moindre privilege)
- La connexion se fait via une URL dans la configuration du LLM
- Claude Desktop et Claude Code supportent MCP nativement

**Mots-cles SEO**
- configurer MCP OttoKit
- OttoKit serveur MCP Claude
- MCP server WordPress
- connecter Claude Desktop OttoKit MCP

---

## Leçon 11.7 - Cas d'usage AI : agent support, agent contenu, agent SEO

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides cas d'usage, screencast rapide

---

**[INTRO - face caméra]**

Tu sais creer un agent et configurer MCP. Maintenant la question qui compte : qu'est-ce que tu en fais concretement ? Voici trois agents que tu peux deployer des aujourd'hui pour ton business WordPress.

**[ÉCRAN - slide "Cas 1 : Agent Support Formateur"]**

**Le probleme** : tes etudiants posent les memes questions par email. Acces au cours, telecharger le certificat, probleme de paiement. Tu passes 2 heures par semaine a repondre manuellement.

**L'agent** :
- Trigger : email entrant (via Gmail ou formulaire)
- Outils : Google Sheets (FAQ), Gmail (envoyer reponse), TutorLMS (verifier inscription)
- Fonctionnement : l'agent lit la question, consulte la FAQ, verifie le statut de l'etudiant, redige une reponse personnalisee
- Human-in-the-Loop : actif les 2 premieres semaines, puis desactive sur les reponses FAQ simples

**Le resultat** : les questions FAQ sont traitees automatiquement. Tu n'interviens que sur les cas complexes. Tu recuperes 2 heures par semaine.

**[ÉCRAN - screencast rapide - structure de l'agent support]**

[Montre un agent configure avec : Gmail (lecture + envoi), Google Sheets (lecture FAQ), Human-in-the-Loop actif]
[Montre un exemple de conversation test]

Voici a quoi ressemble l'agent dans OttoKit. Les outils, les permissions, le prompt. Tout ce qu'on a vu dans les lecons precedentes, assemble pour un cas reel.

**[ÉCRAN - slide "Cas 2 : Agent Contenu"]**

**Le probleme** : tu veux publier regulierement sur ton blog, mais la creation de contenu prend du temps. Brief, redaction, mise en forme, publication.

**L'agent** :
- Trigger : Schedule App (chaque lundi a 9h) ou declenchement manuel
- Outils : API OpenAI (generer le contenu), WordPress (creer le brouillon), Google Sheets (journal de publication)
- Fonctionnement : l'agent recoit un sujet (depuis un sheet ou un prompt), genere un article, le publie en brouillon, et log l'action dans le sheet
- Human-in-the-Loop : toujours actif (tu relis avant publication)

**Le resultat** : chaque lundi, un brouillon d'article t'attend dans WordPress. Tu relis, tu ajustes, tu publies. Le temps de creation passe de 3 heures a 30 minutes.

**[ÉCRAN - slide "Cas 3 : Agent SEO"]**

**Le probleme** : tu ne sais pas quels articles optimiser en priorite. Tu voudrais un assistant qui analyse tes contenus et te dise ou agir.

**L'agent** :
- Trigger : mensuel (Schedule App, le 1er du mois)
- Outils : Google Sheets (liste d'articles + metriques), API Google Search Console (via webhook), Gmail (rapport)
- Fonctionnement : l'agent recupere les donnees de performance, identifie les articles qui perdent du trafic, et t'envoie un rapport avec les priorites d'optimisation
- Human-in-the-Loop : non (c'est un rapport, pas une action)

**Le resultat** : chaque mois, tu recois un rapport clair avec les 5 articles a optimiser. Tu sais exactement ou concentrer tes efforts.

**[ÉCRAN - slide "Quel agent pour toi ?"]**

| Ton besoin | L'agent recommande |
|---|---|
| Tu reponds aux memes questions | Agent Support |
| Tu publies regulierement du contenu | Agent Contenu |
| Tu veux suivre tes performances SEO | Agent SEO |
| Tu combines les trois | Les trois, avec des triggers differents |

Commence par un seul agent. Celui qui resout ton plus gros probleme de temps. Ajoute les autres quand le premier est stable.

**[TRANSITION - face caméra]**

Trois agents, trois problemes resolus. Mais attention : un agent n'est pas toujours la bonne solution. Dans la prochaine lecon, on voit quand utiliser un agent et quand un simple workflow suffit.

---

**Points cles**
- Agent Support : repond aux FAQ etudiants automatiquement (Gmail + Sheets + LMS)
- Agent Contenu : genere des brouillons d'articles chaque semaine (OpenAI + WordPress)
- Agent SEO : analyse les performances et envoie un rapport mensuel (GSC + Sheets + Gmail)
- Commence par un seul agent, celui qui economise le plus de temps

**Mots-cles SEO**
- OttoKit AI Agent cas d'usage
- agent support WordPress OttoKit
- agent contenu automatique WordPress
- agent SEO OttoKit automatisation

---

## Leçon 11.8 - Agent vs workflow : quand utiliser lequel

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides arbre de decision

---

**[INTRO - face caméra]**

Les AI Agents sont puissants. Mais ils ne remplacent pas les workflows. Chaque outil a son domaine. Utiliser un agent la ou un workflow suffit, c'est gaspiller des tasks et ajouter de l'imprevisibilite. Utiliser un workflow la ou un agent est necessaire, c'est passer des heures a gerer des cas particuliers. On va clarifier ca.

**[ÉCRAN - slide "L'arbre de decision"]**

Pose-toi ces trois questions :

**Question 1 : Le processus est-il toujours le meme ?**
- Oui → Workflow
- Non → Continue

**Question 2 : Les inputs sont-ils previsibles ?**
- Oui → Workflow
- Non → Continue

**Question 3 : La reponse necessite-t-elle du raisonnement ?**
- Oui → Agent
- Non → Workflow avec conditions

Trois questions, une reponse claire.

**[ÉCRAN - slide "Exemples - Workflow"]**

Ces cas ne necessitent pas d'agent :

| Scenario | Pourquoi un workflow suffit |
|---|---|
| Nouvelle commande → email de confirmation | Toujours le meme processus, memes donnees |
| Nouvel article publie → partage sur les reseaux | Action fixe, pas de decision |
| Formulaire soumis → ajouter dans un Google Sheet | Transfert de donnees direct |
| Paiement recu → inscrire a la formation | Etapes predefinies, conditions binaires |
| Chaque lundi → envoyer un rapport | Planification simple |

Le point commun : les etapes sont connues a l'avance. Le resultat est previsible.

**[ÉCRAN - slide "Exemples - Agent"]**

Ces cas necessitent un agent :

| Scenario | Pourquoi un agent est necessaire |
|---|---|
| Repondre a un email de support | Le contenu de l'email est imprevisible |
| Analyser un article et suggerer des ameliorations | L'analyse depend du contenu |
| Decider quel article prioriser pour le SEO | Le choix depend de multiples criteres |
| Traiter une reclamation client | Chaque reclamation est differente |
| Resumer un document et l'envoyer au bon destinataire | Le destinataire depend du contenu |

Le point commun : les inputs varient, et la bonne action depend du contexte.

**[ÉCRAN - slide "Le cout en tasks"]**

Un detail financier important :

- **Workflow** : 1 task par étape executee. Un workflow de 5 etapes = 5 tasks.
- **Agent** : 1 task par action de l'agent, mais l'agent peut faire plusieurs tentatives, consulter plusieurs outils. Un agent qui repond a un email peut consommer 3 a 10 tasks.

Sur un plan avec 1 000 tasks par mois :
- 200 executions de workflow a 5 etapes = 1 000 tasks
- 200 executions d'agent a 5-10 actions = 1 000 a 2 000 tasks

Les agents consomment plus. Utilise-les quand la valeur ajoutee le justifie.

**[ÉCRAN - slide "La regle des 80/20"]**

En pratique, pour la plupart des business WordPress :

- **80% des automations** sont des workflows classiques (transfert de donnees, notifications, actions repetitives)
- **20% des automations** beneficient d'un agent (support client, analyse de contenu, decisions contextuelles)

Commence par automatiser les 80% avec des workflows. Puis identifie les 20% ou un agent apporte une vraie valeur.

**[ÉCRAN - slide "Checklist de decision"]**

Avant de creer un agent, verifie :

- [ ] Un workflow avec des conditions ne suffit-il pas ?
- [ ] Les inputs sont-ils vraiment imprevisibles ?
- [ ] Le cout en tasks supplementaire est-il justifie ?
- [ ] Le Human-in-the-Loop est-il configure pour les actions sensibles ?
- [ ] Tu as un plan B si l'agent repond mal ?

Si tu reponds "oui" a tout, cree l'agent. Sinon, reste sur un workflow.

**[TRANSITION - face caméra]**

Le Module 11 est termine. Tu sais creer des agents, leur donner des outils, garder le controle avec le Human-in-the-Loop, configurer MCP, et surtout choisir le bon outil au bon moment. Passe au quiz pour valider tout ca.

---

**Points cles**
- Workflow = processus fixe et previsible. Agent = inputs variables et raisonnement contextuel.
- Les agents consomment 2 a 4 fois plus de tasks que les workflows classiques
- 80% des automations sont des workflows, 20% beneficient d'un agent
- Toujours se demander si un workflow conditionnel ne suffit pas avant de creer un agent

**Mots-cles SEO**
- OttoKit agent vs workflow
- quand utiliser AI Agent OttoKit
- cout tasks agent OttoKit
- choisir workflow ou agent WordPress

---

## Notes de production - Module 11

### Captures a preparer
- Slide comparaison workflow vs agent (tableau)
- Screencast OttoKit : section AI Agents dans le dashboard
- Screencast OttoKit : creation d'un agent (formulaire complet)
- Screencast OttoKit : interface de test / chat agent
- Screencast OttoKit : ajout d'outils (Gmail, Google Sheets) a un agent
- Screencast OttoKit : activation Human-in-the-Loop + notification
- Screencast OttoKit : approbation d'une action dans le dashboard
- Screencast OttoKit : activation Developer Mode + section MCP
- Screencast OttoKit : creation serveur MCP + copie URL
- Screencast Claude Desktop : configuration MCP + liste des outils
- Screencast Claude Desktop : commande "Cree un brouillon" + resultat
- Screencast WordPress admin : brouillon cree via MCP
- Slide architecture MCP (schema LLM → serveur MCP → OttoKit → apps)
- Slides cas d'usage (support, contenu, SEO)
- Slide arbre de decision agent vs workflow
- Slide comparaison cout en tasks

### Environnement de demo
- Compte OttoKit (plan premium - necessaire pour AI Agents et MCP)
- Cle API OpenAI ou Anthropic (pour le modele de l'agent)
- Google Sheet "FAQ Support" avec colonnes : Question, Reponse, Categorie (10+ lignes)
- Compte Gmail connecte a OttoKit
- Site WordPress schoolsWP avec TutorLMS (au moins 1 cours et 1 etudiant)
- Claude Desktop installé avec support MCP
- Fichier de configuration MCP local (`.claude/mcp.json` ou équivalent)

### Durée estimée par leçon (hors quiz)
| Leçon | Durée vidéo |
|-------|-------------|
| 11.1 | 6 min |
| 11.2 | 8 min |
| 11.3 | 7 min |
| 11.4 | 7 min |
| 11.5 | 7 min |
| 11.6 | 7 min |
| 11.7 | 7 min |
| 11.8 | 6 min |
| **Total M11** | **55 min** |
