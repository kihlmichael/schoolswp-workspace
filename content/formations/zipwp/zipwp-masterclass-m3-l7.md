# Lecon 3.7 - Maintenance hebdomadaire

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 3 - De la demo au site en production
- **Lecon** : 7/7
- **Duree cible** : 6 min
- **Objectif pedagogique** : Mettre en place une routine de maintenance hebdomadaire (15 min) et une checklist mensuelle pour garder un site WordPress sain.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

Un site WordPress, ca ne se "lance" pas et ca s'oublie. Un site qui n'est pas maintenu, c'est un site qui ralentit, qui se fait hacker, ou qui perd des prospects parce qu'un formulaire est casse depuis trois semaines et personne ne s'en est rendu compte.

La bonne nouvelle : 15 minutes par semaine suffisent. Pas une heure, pas une demi-journee. 15 minutes le lundi matin. C'est tout ce qu'il faut pour garder ton site sain.

---

[SECTION 1 - Routine hebdomadaire : les 5 verifications]

Bloque un creneau de 15 minutes chaque lundi matin. Mets un rappel. Et fais ces cinq choses dans l'ordre.

Verification numero 1 : les mises a jour. Connecte-toi a l'admin WordPress. Va dans le tableau de bord → Mises a jour. Mets a jour WordPress core, le theme Astra, et tous les plugins. Si tu as active les mises a jour automatiques, verifie quand meme que tout s'est bien passe - un echec silencieux, ca arrive.

Verification numero 2 : le formulaire de contact. Ouvre ton site, va sur la page contact, et envoie un message test. Verifie que tu recois l'email dans ta boite. Si tu ne recois rien, le formulaire est casse - et ca veut dire que les prospects qui t'ecrivent depuis une semaine n'ont pas recu de reponse.

Verification numero 3 : les backups. Si tu utilises UpdraftPlus, va dans les reglages et verifie que le dernier backup s'est termine avec succes. Verifie la date. Si le backup a plus d'une semaine, il y a un probleme de planification. Si tu es chez ZipWP, verifie dans le dashboard que les backups automatiques sont actifs.

Verification numero 4 : les commentaires spam. Si tu as un blog, va dans Commentaires et supprime les spams. Akismet en filtre la majorite, mais il en passe toujours quelques-uns. Un site avec des commentaires spam visible, ca nuit a la credibilite.

Verification numero 5 : la vitesse. Lance un test rapide sur PageSpeed Insights - pagespeed.web.dev. Rentre ton URL et regarde le score mobile. Si le score a chute significativement par rapport a la semaine derniere, quelque chose a change - un plugin, une image trop lourde, un script qui bloque.

5 verifications, 15 minutes. C'est fait.

---

[SECTION 2 - Checklist mensuelle]

Une fois par mois, prends 30 minutes supplementaires pour trois verifications plus approfondies.

Premiere : les liens casses. Installe le plugin Broken Link Checker, ou utilise un service en ligne comme deadlinkchecker.com. Lance un scan. Les liens casses nuisent au SEO et a l'experience utilisateur. Corrige ou supprime les liens morts.

Deuxieme : relis tes textes principaux. Ouvre la page d'accueil, la page services, la page a propos. Lis comme si tu decouvras le site pour la premiere fois. Les informations sont-elles toujours a jour ? Les prix ont-ils change ? Le numero de telephone est-il correct ? Les temoignages sont-ils encore pertinents ?

Troisieme : verifie le certificat SSL. Va sur ton site et verifie que le cadenas est present dans la barre d'adresse. Clique dessus et verifie la date d'expiration du certificat. Let's Encrypt renouvelle automatiquement, mais des fois ca echoue - et tu ne t'en rends compte que quand les visiteurs voient l'avertissement "Non securise".

---

[SECTION 3 - Automatiser ce qui peut l'etre]

Tu peux reduire ces 15 minutes en automatisant certaines taches.

Mises a jour automatiques : on en a parle dans la lecon securite. Active-les pour les plugins et le theme. Ca elimine la verification numero 1.

Monitoring uptime : utilise un service gratuit comme UptimeRobot. Il verifie toutes les 5 minutes que ton site est en ligne et t'envoie un SMS ou un email s'il tombe. Tu n'as plus besoin de verifier manuellement.

Rapports PageSpeed automatises : configure un rapport hebdomadaire via Google Search Console ou un outil tiers. Tu recois un email avec les metriques de performance - sans te connecter.

Meme avec ces automatisations, garde le test du formulaire en manuel. Envoie un vrai message. Lis un vrai email de confirmation. C'est la seule facon de verifier que la chaine complete fonctionne.

---

[OUTRO]

15 minutes le lundi matin. 30 minutes supplementaires une fois par mois. C'est tout ce qu'il faut pour garder ton site en bonne sante.

Ce n'est pas de la maintenance lourde. C'est de l'hygiene basique. Comme te brosser les dents - ca prend peu de temps, et tu le regrettes tres vite si tu arretes.

Tu viens de terminer le Module 3. Ton site est en production, securise, optimise pour le SEO, et tu as une routine de maintenance en place. Dans le Module 4, on passe au niveau superieur : les Blueprints et le workflow professionnel. Tu vas apprendre a transformer ton site en template reutilisable et a livrer des sites clients en une journee.

---

## Notes de production

### Captures d'ecran suggerees

1. **Mises a jour WordPress** - Tableau de bord avec notifications de mise a jour
2. **Formulaire contact** - Test d'envoi avec champs remplis
3. **UpdraftPlus** - Statut du dernier backup avec date et heure
4. **PageSpeed Insights** - Score mobile avec les metriques principales
5. **UptimeRobot** - Dashboard avec statut uptime du site
6. **Checklist visuelle** - Resume graphique : 5 checks hebdo + 3 checks mensuels

### Transitions

- Intro → Section 1 : apparition d'un calendrier avec "Lundi 9h - Maintenance"
- Section 1 → Section 2 : transition vers calendrier mensuel
- Section 2 → Section 3 : animation "automatisation" avec engrenages
- Section 3 → Outro : retour avatar, ton de synthese motivant

### Notes HeyGen / ElevenLabs

- Ton energique et motivant - la maintenance ne doit pas sembler penible
- Phrase cle a appuyer : "15 minutes le lundi matin. C'est tout."
- Section 1 : rythme checklist, chaque point numerote et separe
- Section 3 : ton pragmatique, on gagne du temps
- Outro : ton satisfait, transition vers le Module 4
