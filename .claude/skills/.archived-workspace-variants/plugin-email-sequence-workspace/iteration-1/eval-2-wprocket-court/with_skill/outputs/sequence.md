# SEQ — WP Rocket Discovery (3 emails)

---

## 1. Recapitulatif

| Email | Jour | Objet principal | Objet alternatif | Angle | Role |
|---|---|---|---|---|---|
| 1 | J0 | Ton site WordPress est lent (et tu perds des visiteurs) | 3 secondes : c'est tout ce que Google te laisse | Probleme + decouverte | Prise de conscience + presentation de l'outil |
| 2 | J3 | Mon site charge 2x plus vite depuis 10 minutes | Le test de vitesse qui m'a fait changer d'avis | Preuve + approfondissement | Cas concret + gratuit vs Pro |
| 3 | J7 | WP Rocket : ma reponse honnete | Un plugin de cache, oui ou non ? | Decision | Convertir sans pression |

---

## 2. Emails

### Email 1 — J0 : Probleme + decouverte

```
Objet : Ton site WordPress est lent (et tu perds des visiteurs)
Objet alternatif : 3 secondes : c'est tout ce que Google te laisse

[Prenom],

Tu as deja teste la vitesse de ton site WordPress ?

Si la reponse est non, fais-le maintenant. Un test PageSpeed, 30 secondes.

Si la reponse est oui, tu sais probablement deja que :
- Chaque seconde de chargement en plus = des visiteurs qui partent
- Google penalise les sites lents dans ses resultats
- Un plugin WordPress mal configure peut doubler ton temps de chargement

Le probleme, c'est que la plupart des solutions de cache WordPress sont soit
trop complexes a configurer, soit inefficaces sans reglages manuels.

J'utilise WP Rocket depuis plusieurs mois. C'est un plugin de cache qui fait
trois choses bien : cache de page, lazy loading des images, et minification
CSS/JS.

Pas besoin de toucher au code. Pas besoin de comprendre ce qu'est un cache.

Dans mon prochain email, je te montre exactement ce que ca a change sur mon
site — chiffres a l'appui.

Michael

P.S. : WP Rocket a une version gratuite avec les fonctions de base. Tu peux
tester sans rien payer.
```

---

### Email 2 — J3 : Preuve + approfondissement

```
Objet : Mon site charge 2x plus vite depuis 10 minutes
Objet alternatif : Le test de vitesse qui m'a fait changer d'avis

[Prenom],

10 minutes. C'est le temps qu'il m'a fallu pour installer et configurer
WP Rocket.

Le resultat : mon temps de chargement divise par 2.

Pas en optimisant 15 parametres. Pas en lisant 3 tutoriels. Juste en
installant le plugin et en activant les reglages recommandes.

Ce que fait la version gratuite :
- Cache de page (le plus gros gain de vitesse)
- Lazy loading (les images se chargent quand on scrolle)
- Minification CSS/JS (fichiers plus legers)

Ce que la version Pro ajoute (49 euros/an) :
- CDN integre (tes fichiers servis depuis des serveurs proches du visiteur)
- Preloading (le cache se genere automatiquement, pas au premier visiteur)
- Optimisation de la base de donnees (nettoyage des revisions, transients...)

Mon avis : la version gratuite suffit pour un site classique. Le Pro devient
utile quand tu as du trafic ou beaucoup de contenu.

Une limite honnete : WP Rocket ne corrige pas un mauvais hebergeur. Si ton
hebergement est lent a la base, le cache ameliore les choses mais ne fait
pas de miracles.

Tu veux tester ? Commence par la version gratuite :
-> Installe WP Rocket et lance un test PageSpeed avant/apres.

Michael

P.S. : Si tu as deja un plugin de cache installe (W3 Total Cache, LiteSpeed
Cache...), desactive-le avant d'installer WP Rocket. Deux plugins de cache
en meme temps = conflit garanti.
```

---

### Email 3 — J7 : Decision

```
Objet : WP Rocket : ma reponse honnete
Objet alternatif : Un plugin de cache, oui ou non ?

[Prenom],

Je ne vais pas te relancer 15 fois sur WP Rocket.

Mais voici la question simple : ton site est-il aussi rapide qu'il pourrait
l'etre ?

Si tu n'as pas de plugin de cache, la reponse est non.

WP Rocket est celui que j'utilise sur schoolsWP. Pas parce que c'est le seul.
Parce que c'est celui qui m'a donne des resultats concrets en 10 minutes,
sans configuration technique.

Version gratuite -> deja efficace pour un site standard.
Version Pro (49 euros/an) -> CDN, preloading, optimisation BDD. Utile si tu
veux aller plus loin.

-> Decouvrir WP Rocket : schoolswp.com/recommande/wp-rocket (lien affilie)

Je recommande WP Rocket parce que je l'utilise et que les resultats sont la.
Si tu choisis un autre outil de cache, aucun probleme — l'important, c'est
que ton site soit rapide.

Michael

P.S. : Si tu as des questions sur la configuration ou un doute entre gratuit
et Pro, reponds a cet email. Je te donne mon avis.
```

---

## 3. Automation FluentCRM

### Tags a creer

| Tag | Role | Applique quand |
|---|---|---|
| `wp-rocket-sequence` | Marque l'entree dans la sequence | Debut de la sequence |
| `wp-rocket-converti` | Marque la conversion | Clic sur le lien affilie (email 3) |
| `wp-rocket-termine` | Marque la fin naturelle | Email 3 envoye, pas converti |

### Nommage de l'automation

`SEQ — WP Rocket Discovery`

### Schema de l'automation

```
[TRIGGER] Tag "wp-rocket-sequence" applique
    |
[CONDITION] Tag "wp-rocket-converti" OU "wp-rocket-termine" present ?
    | Non                         | Oui
    |                          [FIN — anti-doublon]
    |
[ENVOYER] Email 1 (J0 — Probleme + decouverte)
    |
[ATTENTE] 3 jours
    |
[CONDITION] Tag "wp-rocket-converti" ?
    | Non                         | Oui
[ENVOYER] Email 2              [FIN — sortie propre]
(J3 — Preuve + approfondissement)
    |
[ATTENTE] 4 jours
    |
[CONDITION] Tag "wp-rocket-converti" ?
    | Non                         | Oui
[ENVOYER] Email 3              [FIN — sortie propre]
(J7 — Decision)
    |
[APPLIQUER TAG] wp-rocket-termine
[RETIRER TAG] wp-rocket-sequence
    |
[FIN]
```

### Condition anti-doublon (entree)

Avant d'entrer dans la sequence, verifier :
- Le contact n'a PAS le tag `wp-rocket-termine` (deja passe)
- Le contact n'a PAS le tag `wp-rocket-converti` (deja converti)
- Le contact est en statut "Abonne" dans FluentCRM

### Tracking de conversion

**Option A — FluentCRM Pro (natif)**
- Trigger : clic sur le lien `schoolswp.com/recommande/wp-rocket` dans l'email 3
- Action : appliquer le tag `wp-rocket-converti`

**Option B — Page de redirection + webhook (version gratuite)**
- Page WordPress `/recommande/wp-rocket` avec redirection vers le lien affilie
- Webhook FluentCRM via OttoKit pour appliquer le tag `wp-rocket-converti` au passage

Recommandation : utiliser l'option B si tu es sur FluentCRM gratuit. Elle fonctionne sans extension Pro.

### Strategie post-sequence

Les contacts tagues `wp-rocket-termine` (non convertis) :

1. **Relance douce (J+30)** — Un seul email "WP Rocket vient de sortir une mise a jour" si mise a jour recente — tag temporaire `wp-rocket-relance-30`
2. **Inclusion dans une sequence thematique** — Si tu as un cluster "performance WordPress" ou "outils essentiels", inclure le contact dans cette sequence
3. **Ne rien faire** — Parfois le meilleur choix. Ne pas harceler.

---

## 4. Checklist pre-lancement

- [ ] Les 3 tags sont crees dans FluentCRM (`wp-rocket-sequence`, `wp-rocket-converti`, `wp-rocket-termine`)
- [ ] L'automation `SEQ — WP Rocket Discovery` est configuree et en mode "brouillon"
- [ ] Chaque email a ete relu (aucune fonctionnalite inventee)
- [ ] Les liens (affilie et articles) sont testes et fonctionnels
- [ ] La page `/recommande/wp-rocket` redirige correctement (si option B)
- [ ] Un contact test a recu la sequence complete (3 emails sur 7 jours)
- [ ] Le statut du contact test passe bien de `wp-rocket-sequence` a `wp-rocket-termine`
- [ ] Le clic sur le lien affilie applique bien `wp-rocket-converti`

---

## 5. KPI de suivi

| KPI | Seuil acceptable | Seuil bon | Action si en dessous |
|---|---|---|---|
| Taux d'ouverture moyen | > 25% | > 40% | Revoir les objets (tester les variantes A/B) |
| Taux de clic Email 2 (lien installation) | > 3% | > 6% | Revoir le CTA ou l'angle de preuve |
| Taux de clic Email 3 (lien affilie) | > 2% | > 5% | Revoir l'urgence ou la proposition de valeur |
| Taux de conversion sequence | > 1% | > 3% | Revoir l'alignement audience/outil |
| Taux de desabonnement | < 2% | < 0.5% | Revoir la frequence ou la pertinence |
