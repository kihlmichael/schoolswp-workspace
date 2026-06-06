# Fiche de repo : FluentCart Checkout Login

> Fiche de surveillance d'un plugin communautaire tiers. Source de verite : le repo GitHub. Cette fiche est un instantane ancre sur l'etat reel au 2026-06-02 (deep scan du code v1.0.3). Le watcher check.ps1 met a jour la baseline et l'historique a chaque evolution.

## Identite

| Champ         | Valeur                                                                                                           |
| ------------- | ---------------------------------------------------------------------------------------------------------------- |
| Repo          | https://github.com/PineDigitalCo/fluentcart-checkout-login                                                       |
| Auteur        | Pine Digital (pinedigital) / header PHP : "My Listing Pro"                                                       |
| Cree le       | 2026-05-28                                                                                                       |
| Dernier push  | 2026-05-28 (6 commits, tous le meme jour)                                                                        |
| Visibilite    | public                                                                                                           |
| Licence       | GPLv2 (annoncee dans readme.txt) mais AUCUN fichier LICENSE dans le repo                                         |
| Stars / forks | 1 / 0                                                                                                            |
| Description   | Permet a un invite de se connecter depuis le checkout FluentCart et d'y rester (reuse du login REST FluentCart). |

## Scorecard (reference Michael + lecture audit)

| Axe                         | Estimation Michael | Lecture deep scan v1.0.3                                                                                                                                                               |
| --------------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Potentiel                   | 7/10               | Confirme. Comble un manque reel de FluentCart (login invite sur checkout).                                                                                                             |
| Maturite                    | 3/10               | Confirme. Pas de release, pas de tag, pas de tests, pas de CI, pas de changelog, licence absente, version incoherente.                                                                 |
| Risque securite apparent    | 4/10               | Legerement meilleur sur le code lui-meme (0 fonction dangereuse, echappement propre), mais "vibe-coded non revu" plus form de login expose sur page publique maintiennent la prudence. |
| Risque maintenance          | 7/10               | Confirme, voire sous-estime. Couplage fort aux internes FluentCart (3 points de rupture silencieuse).                                                                                  |
| Utilisable en production    | NON sans audit     | Confirme.                                                                                                                                                                              |
| Utilisable en staging       | OUI pour test      | Confirme.                                                                                                                                                                              |
| Interet editorial schoolsWP | OUI                | Confirme.                                                                                                                                                                              |

## Contenu actuel du repo

Le repo ne contient que 2 fichiers traces :

- fluent-cart-checkout-login.zip (5899 o) : le binaire distribue.
- readme.txt (1000 o) : en-tete plugin facon WordPress.org.

Aucune source n'est exposee hors du ZIP. Le README.md initial a ete supprime au profit de readme.txt.

Contenu interne du ZIP (3 fichiers) :

- fluent-cart-checkout-login.php (6111 o) : enregistre les hooks, enqueue les assets, rend le panneau de login.
- assets/checkout-login.js (5256 o) : soumet le formulaire au login REST de FluentCart.
- assets/checkout-login.css (4005 o) : mise en page du panneau.

## Incoherence de version (a surveiller)

- readme.txt annonce Stable tag 1.0.1.
- Le header PHP dans le ZIP declare Version 1.0.3 (et la constante FCL_CHK_LOGIN_VERSION vaut 1.0.3).

Le ZIP est en avance sur le readme. Hygiene de release faible. Le watcher tracke la version du readme (cheap) et relit le header en deep scan.

## Checklist technique (deep scan v1.0.3)

| Point verifie                                                                              | Resultat                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Dependance window.fluentcart_checkout_info                                                 | OUI. getInfo() lit ce global, en extrait rest.url et rest.nonce. Rupture silencieuse si FluentCart le renomme.                                                                                                                                         |
| Handle JS fct-checkout                                                                     | OUI. Le script est enqueue avec fct-checkout en dependance. Si FluentCart renomme ce handle, le script ne se charge plus correctement.                                                                                                                 |
| Endpoint REST FluentCart utilise                                                           | {rest.url}/user/login, POST form-urlencoded, header X-WP-Nonce egal rest.nonce.                                                                                                                                                                        |
| Comportement apres login                                                                   | window.location.reload() en cas de succes. Reste sur l'URL du checkout.                                                                                                                                                                                |
| Conservation du panier                                                                     | NON gere par le plugin. Le reload s'appuie sur la persistance panier de FluentCart. A tester en staging.                                                                                                                                               |
| Recuperation des donnees client                                                            | NON gere par le plugin. Apres reload, c'est FluentCart qui repeuple les donnees de facturation.                                                                                                                                                        |
| Absence d'erreurs console                                                                  | A verifier en staging. Bug latent repere : ligne 174 du JS, payload.message lu alors que payload peut etre null apres un JSON.parse rate (reponse d'erreur non-JSON), donc TypeError possible.                                                         |
| Absence de conflit avec le checkout                                                        | Bien gere. Rendu via l'action fluent*cart/before_checkout_page_start, HORS du root data-fluent-cart-checkout-page, sans classes fct*\*. Isolation DOM volontaire.                                                                                      |
| Securite du formulaire                                                                     | Reutilise le nonce REST de FluentCart (X-WP-Nonce), pas de nonce propre. action egale # plus preventDefault (pas de fallback sans JS). Form de login expose sur une page publique : surface d'attaque legerement elargie, pas de rate-limiting propre. |
| Echappement HTML cote PHP                                                                  | Propre. 14 appels esc_html, esc_attr, esc_url. Redirection passee dans wp_sanitize_redirect puis wp_validate_redirect. Aucun echo de donnee utilisateur brute.                                                                                         |
| Fonctions dangereuses (eval, decodage base64, exec shell, ecriture fichier, appel externe) | AUCUNE, ni en PHP ni en JS. Pas d'URL externe en dur. Le JS utilise textContent (pas innerHTML).                                                                                                                                                       |

## Risques identifies

1. **Maintenance / couplage** (principal) : 3 points de rupture silencieuse aux internes FluentCart (le global window.fluentcart_checkout_info, le handle fct-checkout, les actions fluent_cart/\*). Un refactor FluentCart casse le plugin sans erreur visible (juste un toast "Checkout data is unavailable").
2. **Gouvernance** : vibe-coded, code non revu (auto-declare), pas de tests/CI, pas de release versionnee, licence absente du repo, version incoherente. Aucune garantie de suivi.
3. **Bug JS latent** : TypeError possible sur reponse d'erreur non-JSON (cf. checklist).
4. **Surface d'attaque** : un formulaire de login sur la page de checkout publique est une cible potentielle de credential stuffing. Le plugin n'ajoute pas de protection propre, il delegue a FluentCart.

Points rassurants : echappement PHP correct, aucune fonction dangereuse, isolation DOM reflechie, gestion d'erreur defensive cote JS.

## Decision actuelle

- **Production** : NON, jamais sans audit prealable.
- **Staging** : OUI, pour tester le parcours (login invite, conservation panier, repopulation donnees, erreurs console).
- **Editorial schoolsWP** : OUI, sujet pertinent (combler un manque FluentCart) si et quand le plugin gagne en fiabilite.
- **Re-evaluation declenchee par** : sortie d'une release, exposition des sources hors ZIP, apparition de tests/CI, commit securite, ou contribution communautaire (issues/PR).

## Surveillance

- Watcher : check.ps1 (ce dossier). Voir README.md pour usage, cron et stockage du webhook.
- Baseline : .baseline.json (etat fige, compare a chaque run).
- Historique : history.md (append-only, une entree par changement detecte).
- Rapports : reports/ (rapport Markdown 6 sections a chaque changement significatif).
- Alerte : Discord (webhook schoolsWP-Routines, channel #alerts) via env var DISCORD_SCHOOLSWP_ROUTINES_URL.
