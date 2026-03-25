# Sequence email WP Rocket — 3 emails

**Plugin** : WP Rocket (cache WordPress)
**Modele** : Freemium — gratuit limite / Pro a 49 EUR/an
**Lien affilie** : schoolswp.com/recommande/wp-rocket
**Objectif** : conversion vers WP Rocket Pro via le lien affilie

---

## Logique d'automation

```
Declencheur : inscription liste OU tag "performance-wp" applique

Jour 0 → Email 1 : Le probleme (site lent = visiteurs perdus)
  ├─ Si clic lien WP Rocket → tag "wp-rocket-interesse"
  │    └─ Attendre 2 jours → Email 3 (offre directe)
  └─ Si pas de clic → Attendre 3 jours → Email 2

Jour 3 → Email 2 : Le tutoriel (comment j'ai divise mon temps de chargement par 2)
  ├─ Si clic lien WP Rocket → tag "wp-rocket-interesse"
  │    └─ Attendre 2 jours → Email 3 (offre directe)
  └─ Si pas de clic → Attendre 3 jours → Email 3

Jour 6 → Email 3 : La decision (gratuit vs Pro, pourquoi Pro vaut le coup)
  └─ Fin de sequence → tag "wp-rocket-sequence-terminee"
```

**Tags utilises** :
- `performance-wp` — declencheur d'entree
- `wp-rocket-interesse` — a clique sur le lien au moins une fois
- `wp-rocket-sequence-terminee` — sequence complete

**Conditions de sortie** :
- Achat detecte (si webhook disponible) → retirer de la sequence
- Desabonnement → retirer de la sequence

---

## Email 1 — Le probleme

**Objet** : Ton site WordPress met plus de 3 secondes a charger ?

**Pre-header** : Chaque seconde en trop te coute des visiteurs (et du chiffre d'affaires).

---

Salut {prenom},

Je vais etre direct : si ton site WordPress met plus de 3 secondes a s'afficher, tu perds des visiteurs. Pas un ou deux. Des dizaines. Chaque jour.

Google le confirme : **53 % des visiteurs mobiles quittent une page qui met plus de 3 secondes a charger.**

Et ce n'est pas juste une question de confort. Un site lent, c'est :
- un taux de rebond qui explose
- un SEO qui recule (Google penalise la lenteur)
- des conversions qui chutent — personne n'attend pour acheter

Le pire ? La plupart des sites WordPress sont lents par defaut. Themes lourds, plugins mal optimises, pas de cache... le cocktail classique.

La bonne nouvelle : ca se corrige. Et pas en une semaine de config serveur.

**En 10 minutes, j'ai divise le temps de chargement de mon site par 2.** Avec un seul plugin.

Je t'en parle dans mon prochain email.

A tres vite,
{signature}

P.S. — Si tu veux deja jeter un oeil, c'est [WP Rocket](https://schoolswp.com/recommande/wp-rocket). Version gratuite disponible pour tester.

---

## Email 2 — Le tutoriel

**Objet** : Comment j'ai divise mon temps de chargement par 2 (en 10 min)

**Pre-header** : Pas de code, pas de serveur a configurer. Juste un plugin et 4 reglages.

---

Salut {prenom},

Dans mon dernier email, je te parlais de la lenteur des sites WordPress. Aujourd'hui, je te montre comment j'ai regle le probleme.

**Le plugin : WP Rocket.**

Voici ce que j'ai fait, etape par etape :

### 1. Installation (2 minutes)
J'ai installe WP Rocket comme n'importe quel plugin. Des l'activation, le cache de page est actif. Mon site chargeait deja plus vite sans toucher un seul reglage.

### 2. Lazy loading des images (1 minute)
Un toggle a activer. Les images ne se chargent que quand le visiteur scrolle jusqu'a elles. Resultat : la page initiale s'affiche bien plus vite.

### 3. Minification CSS et JavaScript (2 minutes)
WP Rocket compresse automatiquement les fichiers CSS et JS. Moins de poids = chargement plus rapide.

### 4. Passage en Pro pour le CDN (5 minutes)
C'est la que la difference s'est vraiment sentie. Le CDN integre distribue les fichiers statiques sur des serveurs partout dans le monde. Mes visiteurs internationaux ont vu une amelioration nette.

**Resultat : temps de chargement divise par 2.** De 4,2 secondes a 1,9 seconde. Mesure avec GTmetrix, pas au feeling.

En bonus avec la version Pro :
- **Preloading** : WP Rocket genere le cache avant meme que les visiteurs arrivent
- **Optimisation de la base de donnees** : nettoyage des revisions, transients, commentaires spam

Le tout pour 49 EUR par an. Moins que ce que coute un visiteur perdu par jour.

Tu peux commencer avec la version gratuite pour voir la difference, puis passer en Pro quand tu es convaincu : [Tester WP Rocket](https://schoolswp.com/recommande/wp-rocket)

A bientot,
{signature}

---

## Email 3 — La decision

**Objet** : WP Rocket gratuit ou Pro — voici ce que je te recommande

**Pre-header** : La version gratuite fait le job. La version Pro change la donne.

---

Salut {prenom},

Tu te demandes peut-etre si la version gratuite de WP Rocket suffit. Reponse honnete : ca depend de ton site.

Voici le comparatif clair :

| Fonctionnalite | Gratuit | Pro (49 EUR/an) |
|---|---|---|
| Cache de page | Oui | Oui |
| Lazy loading images | Oui | Oui |
| Minification CSS/JS | Oui | Oui |
| CDN integre | Non | **Oui** |
| Preloading du cache | Non | **Oui** |
| Optimisation base de donnees | Non | **Oui** |
| Support prioritaire | Non | **Oui** |

**Mon avis :**

Si ton site a peu de trafic et un hebergement correct, la version gratuite t'apporte deja une belle amelioration. Cache + lazy loading + minification, c'est le trio de base qui fait la difference.

**Mais si tu veux vraiment optimiser** — surtout avec du trafic international, un site WooCommerce, ou un hebergement mutualise — le Pro vaut largement ses 49 EUR par an.

Le CDN seul justifie le prix. Et l'optimisation de la base de donnees evite que ton site ralentisse au fil du temps (revisions d'articles, transients expires, commentaires spam... ca s'accumule).

Pour te donner une idee : 49 EUR/an, c'est **4 EUR par mois**. Moins cher qu'un cafe par semaine. Pour un site qui charge deux fois plus vite.

**Ma recommandation** : commence par la version gratuite. Mesure la difference. Puis passe en Pro pour aller au bout de l'optimisation.

[Essayer WP Rocket maintenant](https://schoolswp.com/recommande/wp-rocket)

A tres vite,
{signature}

P.S. — Si tu as des questions sur la configuration, reponds a cet email. Je t'aide avec plaisir.

---

## Resume de la sequence

| Email | Jour | Objet | Objectif |
|---|---|---|---|
| 1 | J+0 | Ton site WordPress met plus de 3 secondes a charger ? | Sensibilisation au probleme + premier clic |
| 2 | J+3 | Comment j'ai divise mon temps de chargement par 2 (en 10 min) | Preuve sociale + tutoriel concret |
| 3 | J+6 | WP Rocket gratuit ou Pro — voici ce que je te recommande | Comparatif + decision d'achat |

**KPIs a suivre** :
- Taux d'ouverture par email (cible : > 35 %)
- Taux de clic sur le lien affilie (cible : > 5 %)
- Conversions trackees via le lien affilie
- Taux de desabonnement (alerte si > 1 % par email)
