# PDF : Template Séquence Welcome FluentCRM

**Format** : 1 page A4 stricte - Inter 11pt min - vert `#00D400` sur titres et flèches - logo schoolsWP top-left - QR code bas-droite vers schoolswp.fr

---

## Titre principal

Ta première séquence welcome FluentCRM prête à copier

## Sous-titre

Pour freelances WordPress : 4 emails, 7 jours, tags et conditions inclus, installable chez n'importe quel client en 45 min

---

## Section 1 : Le contexte

Tes clients installent FluentCRM et le compte reste vide. Zéro automation, zéro email, zéro ROI. Voici la séquence que tu colles dans chaque compte pour que leur liste chauffe dès J+0 sans repartir d'une page blanche.

---

## Section 2 : Le cœur actionnable

| # | Délai | Objet | Pré-header | Tag FluentCRM | Condition |
| --- | --- | --- | --- | --- | --- |
| 1 | T+0 | Merci + voici ce que tu attendais | On démarre fort | `welcome_sent` | aucune |
| 2 | T+2j | Pourquoi [entreprise] fait ça | L'histoire derrière | `story_sent` | non désinscrit |
| 3 | T+4j | Le piège qu'on voit le plus souvent | Et comment l'éviter | `value_sent` | a cliqué email 1 ou 2 |
| 4 | T+7j | Voilà ce qui arrive maintenant | Newsletter-style | `welcome_completed` | non désinscrit |

**Bascule finale** : tag `welcome_completed` → déplacer vers liste `newsletter_active`.
**Sortie anticipée** : désinscription = stop complet du funnel.
**Goal** : clic sur CTA commercial = move to liste `engaged_buyer`.

---

## Section 3 : Comment l'utiliser en 3 étapes

1. FluentCRM → Automations → New Funnel → Trigger **"New Contact Added"** avec filtre sur la liste cible.
2. Ajouter **4 actions "Send Email"** avec délais `0 / 2 / 4 / 7 jours`, une action **"Apply Tag"** avant chaque envoi.
3. Créer les **4 tags** dans FluentCRM → Tags, puis câbler la **bascule finale** via action "Remove from list" + "Add to list".

---

## Footer

schoolsWP - WordPress. Clair. Structuré. Utile.
schoolswp.fr
