# Script video - Module 1, Lecon 5 : Anti-spam

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 1 - Fondations
**Lecon** : 5/6 - Anti-spam
**Duree** : 6 min (~900 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast configuration anti-spam
**Objectif** : Proteger ses formulaires contre le spam sans degrader l'experience utilisateur

---

**[INTRO - face camera]**

Tu as configure tes notifications, ton formulaire est pret. Et puis un matin, tu ouvres ta boite mail : 47 soumissions de bots. Des liens suspects, du texte en cyrillique, des adresses email generees aleatoirement.

Le spam sur les formulaires WordPress, c'est un probleme reel. FluentForms a plusieurs couches de protection. On les configure ensemble.

**[ECRAN - screencast "Honeypot"]**

Premiere couche : le Honeypot. C'est la protection invisible.

Le Honeypot ajoute un champ cache dans le formulaire. Le visiteur humain ne le voit pas et ne le remplit pas. Un bot, lui, remplit tous les champs - y compris le champ cache. FluentForms detecte la soumission du bot et la rejette silencieusement.

Dans FluentForms, le Honeypot est actif par defaut. Tu n'as rien a configurer. Va dans Form Settings → Misc pour verifier qu'il est bien active.

C'est une premiere barriere efficace contre les bots basiques. Mais contre les bots plus sophistiques, il faut aller plus loin.

**[ECRAN - screencast "reCAPTCHA v2 et v3"]**

Deuxieme couche : Google reCAPTCHA.

reCAPTCHA v2, c'est la case "Je ne suis pas un robot" que tout le monde connait. Parfois avec les images de feux tricolores et de bus. Ca fonctionne, mais ca degrade l'experience.

reCAPTCHA v3 est invisible. Il analyse le comportement du visiteur - mouvements de souris, vitesse de saisie, parcours sur la page - et attribue un score de 0 a 1. Au-dessus du seuil, la soumission passe. En dessous, elle est bloquee. Le visiteur ne voit rien.

Pour configurer : va dans Fluent Forms → Settings → reCAPTCHA. Tu as besoin de cles API Google. Va sur google.com/recaptcha, cree un projet, choisis v2 ou v3, recupere la cle du site et la cle secrete. Colle-les dans FluentForms. Ensuite, dans chaque formulaire, ajoute le champ reCAPTCHA depuis la sidebar.

Mon avis sur reCAPTCHA : v3 est acceptable, v2 est a eviter. Demander a tes visiteurs de cliquer sur des voitures, c'est mauvais pour le taux de conversion.

**[ECRAN - screencast "hCaptcha"]**

Troisieme option : hCaptcha. C'est l'alternative orientee vie privee.

hCaptcha fonctionne comme reCAPTCHA mais ne collecte pas les donnees de tes visiteurs pour les revendre a Google. Si tu es sensible au RGPD ou que tes visiteurs le sont, c'est un bon choix.

La configuration est identique : cles API depuis le site hCaptcha, coller dans FluentForms, ajouter le champ dans le formulaire.

**[ECRAN - screencast "Cloudflare Turnstile"]**

Quatrieme option - et c'est celle que je recommande : Cloudflare Turnstile.

Turnstile est gratuit, invisible, et ne demande jamais au visiteur de resoudre un puzzle. Pas de cases a cocher, pas d'images a identifier. Le visiteur ne sait meme pas qu'il est en train d'etre verifie.

Il utilise des signaux navigateur et des challenges cryptographiques pour determiner si le visiteur est humain. Le taux de faux positifs est tres faible.

Configuration : cree un compte Cloudflare si tu n'en as pas deja un, va dans Turnstile dans le dashboard, cree un widget, recupere les cles. Dans FluentForms → Settings → Turnstile, colle les cles. Ajoute le champ Turnstile dans le formulaire.

Pourquoi je le recommande : gratuit, invisible, pas de degradation de l'UX, respectueux de la vie privee, et efficace. C'est le meilleur compromis en 2026.

**[ECRAN - screencast "Protections supplementaires"]**

Au-dela des captchas, FluentForms offre deux protections supplementaires.

Planification de formulaire : tu definis une date de debut et une date de fin. En dehors de cette periode, le formulaire est desactive. Utile pour les inscriptions a un evenement ou les promotions temporaires - et ca elimine les soumissions spam hors periode.

Limitation par IP : tu definis un nombre maximum de soumissions par adresse IP sur une periode donnee. Par exemple, 3 soumissions par IP par jour. Ca bloque les bots qui pilonnent le meme formulaire.

Ces deux options se trouvent dans Form Settings → Restrictions & Scheduling.

**[OUTRO - face camera]**

En resume : active le Honeypot (c'est deja fait par defaut), ajoute Cloudflare Turnstile, et configure une limitation par IP si tu as du trafic eleve. Oublie reCAPTCHA v2 avec ses puzzles d'images - tes visiteurs meritent mieux.

Prochaine lecon : la migration. Si tu es actuellement sur Contact Form 7, WPForms ou Gravity Forms, je te montre comment tout migrer en un clic. On se retrouve tout de suite.

---

**Points cles** :
- Honeypot : actif par defaut, invisible, bloque les bots basiques
- reCAPTCHA v3 : invisible, score comportemental - v2 a eviter (UX degradee)
- hCaptcha : alternative respectueuse de la vie privee
- Cloudflare Turnstile : recommande (gratuit, invisible, efficace)
- Protections supplementaires : planification de formulaire, limitation par IP

**Mots cles SEO** : FluentForms anti-spam, FluentForms Cloudflare Turnstile, FluentForms reCAPTCHA, proteger formulaire WordPress spam

---

**Notes de production** :
- Face camera : intro (15 sec) + outro (15 sec)
- Screencast : configuration de chaque solution anti-spam
- Montrer le dashboard Cloudflare Turnstile (creation widget)
- Ton : direct, recommandation claire pour Turnstile
