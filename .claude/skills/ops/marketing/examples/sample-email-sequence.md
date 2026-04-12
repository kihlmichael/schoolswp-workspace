# Exemple — Sequence email nurture schoolsWP (3 emails)

**Objectif** : accueillir un nouvel inscrit et l'amener vers la formation gratuite Tutor LMS
**Outil** : FluentCRM
**Tag d'entree** : `lead-tutor-lms`
**Tutoiement** : oui (emails = tu)

---

## Email 1 — Bienvenue + valeur immediate

**Objet** : Ton site WordPress peut devenir une plateforme de formation
**Preview text** : Sans SaaS, sans commission, sans budget technique.

---

Salut,

Tu viens de rejoindre la communaute schoolsWP. Merci.

Pas de long discours de bienvenue — juste ce qui va t'etre utile.

Si tu es ici, c'est probablement parce que tu veux vendre des formations depuis ton propre site WordPress. Bonne nouvelle : c'est plus simple et moins cher que ce que la plupart des gens pensent.

Voici le point de depart que je recommande :

**La formation gratuite "Creer ta premiere formation avec Tutor LMS"** — 3 modules, 45 minutes au total. A la fin, tu auras un cours en ligne fonctionnel sur ton site.

[Acceder a la formation gratuite]

A demain pour un conseil concret sur le choix du bon LMS.

Michael

---

**Delai avant email 2** : 24h
**Condition** : envoye dans tous les cas

---

## Email 2 — Contenu educatif

**Objet** : Les 3 erreurs qui tuent une formation en ligne WordPress
**Preview text** : J'ai fait la premiere pendant 6 mois.

---

Salut,

Avant de lancer ta premiere formation, laisse-moi te faire gagner du temps avec 3 erreurs que je vois tout le temps :

**Erreur 1 — Choisir un LMS trop complexe pour ses besoins.**
Si tu debutes, tu n'as pas besoin de 47 fonctions. Un LMS simple avec quiz + certificat + paiement couvre 90 % des cas. Tutor LMS et LearnDash font le travail. Tout le reste est du bruit.

**Erreur 2 — Ne pas structurer ses modules avant de rediger.**
Le plan de formation vient avant le contenu. Pas l'inverse. 5 modules de 3 lecons valent mieux que 20 lecons en vrac.

**Erreur 3 — Ignorer la page de vente.**
Ton cours peut etre excellent — si la page qui le presente ne donne pas envie, personne ne cliquera. La page de vente est aussi importante que le contenu.

J'ai detaille chaque erreur avec des solutions concretes dans cet article :
[3 erreurs qui tuent une formation WordPress]

Demain, je te partage la methode que j'utilise pour structurer une formation en une apres-midi.

Michael

---

**Delai avant email 3** : 24h
**Condition** : envoye dans tous les cas

---

## Email 3 — Conversion douce

**Objet** : Ta formation en ligne, structuree en 2 heures
**Preview text** : La methode que j'utilise pour chaque nouveau cours.

---

Salut,

Hier je t'ai parle des erreurs classiques. Aujourd'hui, la solution.

J'utilise une methode en 4 etapes pour structurer n'importe quelle formation :

1. **Definir la transformation** — qu'est-ce que ton eleve saura faire a la fin ?
2. **Decouper en modules** — 4 a 6 modules, chacun = une etape vers la transformation
3. **Ecrire les lecons** — une lecon = un concept + un exercice
4. **Creer la page de vente** — promesse + contenu + preuve + prix

Cette methode est au coeur de la formation gratuite que je t'ai partagee lundi. Si tu ne l'as pas encore commencee, c'est le bon moment :

[Commencer la formation gratuite Tutor LMS]

Et si tu veux aller plus loin — structure avancee, automatisation des inscriptions, monetisation — la formation complete schoolsWP couvre tout ca en detail.

[Decouvrir la formation complete]

A bientot,

Michael

---

## Logique FluentCRM

```
Declencheur : tag "lead-tutor-lms" ajoute
  → Email 1 (immediat)
  → Attendre 24h
  → Email 2
  → Attendre 24h
  → Email 3
  → Si clic sur "formation complete" → tag "interested-tutor-premium"
  → Si pas d'ouverture email 2 + 3 → tag "cold-lead" + sequence re-engagement
```
