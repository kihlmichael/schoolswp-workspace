# Leçon 6.5 - IA intégrée (OpenAI / OpenRouter) : à quoi ça sert

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 6 - Intégrations et fonctions avancées
- **Durée cible** : 7 min (~980 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Comprendre ce que fait le résumé d'avis par IA, récupérer une clé API chez OpenAI ou OpenRouter, connecter le service dans les réglages avancés, puis activer et personnaliser le résumé dans un template d'avis.
- **Prérequis** : Module 3 vu (Business Reviews), au moins une plateforme d'avis connectée avec des avis récupérés.

---

## Script narration

**[INTRO - face camera]**

Quand tu accumules des dizaines, voire des centaines d'avis sur Google, Facebook ou Yelp, c'est une bonne nouvelle. Mais pour un visiteur, lire tout ça est décourageant. C'est là qu'intervient l'IA intégrée à WP Social Ninja.

Son rôle est précis : elle lit tous tes avis et en génère un résumé court et bien tourné, le genre "Les clients apprécient la livraison rapide et le service au top". Ce résumé s'affiche en tête de ton mur d'avis. Dans cette leçon, on voit à quoi ça sert exactement, comment obtenir une clé API chez OpenAI ou OpenRouter, comment la connecter, et comment activer le résumé. C'est parti.

---

**[SECTION 1 - Ce que fait, et ne fait pas, cette intégration]**

**[FACE CAMERA]**

Avant tout, clarifions ce que l'IA fait ici, parce qu'il y a un malentendu fréquent.

L'IA ne modifie pas tes avis. Elle ne réécrit pas, ne corrige pas, ne supprime pas les avis individuels. Chaque avis reste tel que le client l'a écrit, authentique.

Ce qu'elle fait, c'est analyser l'ensemble des avis récupérés sur une plateforme et produire un seul résumé, une synthèse qui capte les sentiments clés. Ce résumé s'affiche dans le template d'avis que tu choisis, en haut, comme un "en un coup d'œil" qui aide le visiteur à comprendre vite ce que pensent tes clients.

Deux fournisseurs sont possibles : OpenAI et OpenRouter. La logique de connexion est quasiment identique pour les deux. Tu choisis celui pour lequel tu as déjà un compte. On va voir les deux.

---

**[SECTION 2 - Obtenir ta clé API OpenAI]**

**[ECRAN - platform.openai.com, page API Keys]**

Commençons par OpenAI. Tu vas sur le site d'OpenAI, dans la section dédiée aux clés API, et tu te connectes, ou tu crées un compte si tu n'en as pas.

Dans le menu de gauche, tu cliques sur API Keys, puis sur Create new secret key pour générer une nouvelle clé. Une fenêtre te demande de nommer ta clé : choisis un nom qui t'aidera à la reconnaître plus tard.

**[ECRAN - clé affichée, bouton de copie]**

Ta nouvelle clé s'affiche. Tu la copies et tu la conserves en lieu sûr, tu en auras besoin tout de suite. Petit réflexe de prudence : une clé API, ça se traite comme un mot de passe. Tu ne la partages pas et tu ne la laisses pas traîner.

---

**[SECTION 3 - Obtenir ta clé API OpenRouter]**

**[ECRAN - openrouter.ai, profil → Keys]**

La deuxième option, c'est OpenRouter. La démarche est la même dans l'esprit. Tu vas sur le site d'OpenRouter, tu t'inscris ou tu te connectes.

Tu cliques sur l'icône de profil, tu choisis Keys, ce qui t'amène sur la page des clés API. Tu cliques sur Create API Key. Une fenêtre apparaît : tu nommes ta clé, tu valides avec Create.

**[ECRAN - clé OpenRouter affichée]**

Ta clé s'affiche, tu la copies pour la suite. Même prudence que pour OpenAI : on garde la clé en sécurité. Quel que soit le fournisseur que tu as choisi, tu as maintenant ta clé en main. Passons à la connexion.

---

**[SECTION 4 - Connecter le service dans WP Social Ninja]**

**[ECRAN - WP Social Ninja → Settings → Advanced Settings]**

La connexion se fait au même endroit pour les deux fournisseurs. Tu vas dans WP Social Ninja, Settings, puis l'onglet Advanced Settings. Tu descends jusqu'à la section AI Review Summarizer Credentials.

Là, tu configures trois champs. AI Platform : tu sélectionnes OpenAI ou OpenRouter, selon la clé que tu as. Model : tu choisis le modèle d'IA que tu préfères dans la liste, par exemple un modèle gpt si tu es chez OpenAI. API Key : tu colles la clé que tu viens de copier.

Tu cliques sur Save Settings pour appliquer. Le service est connecté.

---

**[SECTION 5 - Activer et personnaliser le résumé]**

**[ECRAN - template d'avis, sidebar, toggle Display AI Summary]**

Le branchement est fait, reste à décider où afficher le résumé. Tu ouvres le template d'avis où tu veux le voir apparaître. Dans la barre latérale de droite, tu actives le toggle Display AI Summary.

Une fois activé, tu débloques plusieurs réglages pour soigner le rendu. Summary Style : tu choisis l'affichage en Text ou en List. Display Read More : ajoute un lien "Lire plus" pour les résumés longs. Text Typing Animation : ajoute un effet de frappe au clavier, plus dynamique. Et Regenerate AI Summary : rafraîchit le résumé en tenant compte des avis récemment collectés.

Ce dernier bouton est utile à connaître : quand tu reçois de nouveaux avis, le résumé ne se met pas à jour tout seul à l'infini. Tu cliques sur Regenerate pour le rafraîchir quand tu juges que ça vaut le coup.

**[FACE CAMERA]**

Une remarque honnête pour finir : l'IA ici reste un outil de confort. Elle résume, elle ne remplace pas tes vrais avis, qui restent ta meilleure preuve sociale. Et garde en tête que ces services peuvent avoir un coût selon le modèle et le volume. À toi de voir si le résumé apporte assez à ton visiteur pour justifier la mise en place.

---

**[OUTRO - face camera]**

Tu sais maintenant à quoi sert le résumé d'avis par IA, comment obtenir une clé chez OpenAI ou OpenRouter, comment la connecter dans les réglages avancés, et comment activer le résumé dans ton template. Dans la dernière leçon de ce module, on couvre l'import et l'export de tes contenus, et les réglages de performance pour garder un site rapide. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- OpenAI : page API Keys, Create new secret key, fenêtre de nommage, clé affichée (section 2)
- OpenRouter : profil → Keys, Create API Key, clé affichée (section 3)
- WP Social Ninja → Settings → Advanced Settings → AI Review Summarizer Credentials avec AI Platform / Model / API Key (section 4)
- Template d'avis : sidebar de droite, toggle Display AI Summary (section 5)
- Options de personnalisation : Summary Style (Text/List), Display Read More, Text Typing Animation, Regenerate AI Summary (section 5)
- Aperçu d'un résumé "At a Glance" affiché en tête d'un mur d'avis (section 1)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Section 1 : face camera ou slide, insister visuellement sur "l'IA ne réécrit pas les avis"
- Sections 2 et 3 : screencast réel chez OpenAI puis OpenRouter, flouter ou masquer les clés réelles à l'écran
- Section 4 : screencast WP Social Ninja, montrer que la connexion est identique pour les deux fournisseurs
- Section 5 : screencast sur le template, puis retour face camera pour la remarque "outil de confort + coût possible"
- Outro : face camera, CTA visuel vers la leçon 6.6

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:40 |
| Section 1 - Ce que ça fait | 1:15 |
| Section 2 - Clé OpenAI | 1:10 |
| Section 3 - Clé OpenRouter | 1:00 |
| Section 4 - Connecter le service | 1:15 |
| Section 5 - Activer et personnaliser | 1:25 |
| Outro | 0:15 |
| **Total** | **~7:00** |

### Sources

- Doc : `sources/docs/guide__ai-integration__openai-integration-for-review.md`
- Doc : `sources/docs/guide__ai-integration__openrouter-integration-for-review.md`
- Doc : `sources/docs/guide__integrations__integrations-overview.md` (résumé "At a Glance" en tête du mur d'avis)
