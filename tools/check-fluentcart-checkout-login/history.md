# Historique des changements - PineDigitalCo/fluentcart-checkout-login

> Append-only. Une entree par changement detecte par check.ps1. Ne pas reecrire les entrees passees.

## 2026-06-02 - Baseline initiale - risque nul - reco surveiller

- Mise en place du watcher. Etat fige comme reference.
- Repo cree le 2026-05-28, 6 commits (tous du 28/05), 0 release, 0 tag, 0 issue/PR.
- 2 fichiers traces : fluent-cart-checkout-login.zip (5899 o) et readme.txt (1000 o). Aucune source hors ZIP.
- Version readme (Stable tag) : 1.0.1. Version header PHP dans le ZIP : 1.0.3 (incoherence notee).
- Deep scan v1.0.3 : 0 fonction dangereuse, 0 URL externe en dur, echappement PHP propre (14 appels), couplage FluentCart confirme (window.fluentcart_checkout_info, handle fct-checkout, endpoint /user/login, header X-WP-Nonce).
- Decision : staging oui, production non sans audit, interet editorial oui.
