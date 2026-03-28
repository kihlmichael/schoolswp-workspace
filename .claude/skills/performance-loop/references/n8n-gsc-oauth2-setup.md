# Google OAuth2 — Setup n8n pour Search Console API

---

## Étape 1 — Google Cloud Console

1. Créer un projet : `schoolswp-seo-ops`
2. APIs & Services → Bibliothèque → activer **Search Console API**
3. Écran de consentement OAuth :
   - Type : External
   - Ajouter ton email testeur si demandé
4. Identifiants → Créer → **ID client OAuth 2.0** → type **Web application**
5. Récupérer : `Client ID` + `Client Secret`

---

## Étape 2 — Callback URL (n8n d'abord)

Dans n8n → Credentials → New → Google OAuth2 API → copier le champ **OAuth Redirect URL** affiché.

Coller cette URL dans Google Cloud → Authorized redirect URIs.

Format attendu : `https://schoolswp-n8n.wp1.host/rest/oauth2-credential/callback`

> Prendre l'URL affichée par n8n, pas une valeur devinée.

---

## Étape 3 — Credential n8n

Type : **Google OAuth2 API** (generic)

| Champ             | Valeur                                                |
| ----------------- | ----------------------------------------------------- |
| Grant Type        | Authorization Code                                    |
| Authorization URL | `https://accounts.google.com/o/oauth2/v2/auth`        |
| Access Token URL  | `https://oauth2.googleapis.com/token`                 |
| Client ID         | [depuis Google Cloud]                                 |
| Client Secret     | [depuis Google Cloud]                                 |
| Scope             | `https://www.googleapis.com/auth/webmasters.readonly` |
| Ignore SSL Issues | false                                                 |

Si n8n propose **"Set up for use in HTTP Request node"** → activer.

→ Cliquer **Connect** → connecter le compte Google qui a accès à la propriété GSC `schoolswp.com`.

---

## Étape 4 — Test 1 : lister les sites (valider l'auth)

```
Method : GET
URL    : https://www.googleapis.com/webmasters/v3/sites
Auth   : Predefined Credential Type → ton credential Google OAuth2
```

Résultat attendu : liste des propriétés GSC du compte.
Si `schoolswp.com` n'apparaît pas → mauvais compte connecté ou propriété non partagée.

---

## Étape 5 — Test 2 : première vraie requête GSC

```
Method : POST
URL    : https://www.googleapis.com/webmasters/v3/sites/sc-domain:schoolswp.com/searchAnalytics/query
Auth   : Predefined Credential Type → ton credential Google OAuth2
Body JSON :
```

```json
{
  "startDate": "2026-02-14",
  "endDate": "2026-03-13",
  "dimensions": ["page"],
  "rowLimit": 10,
  "startRow": 0,
  "dataState": "final"
}
```

---

## Erreurs fréquentes

| Erreur                        | Cause                                                       | Fix                                                          |
| ----------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ |
| `redirect_uri_mismatch`       | URL de callback n8n non copiée exactement dans Google Cloud | Reprendre l'URL affichée par n8n, la recoller                |
| `access_denied`               | Écran de consentement mal configuré ou email non autorisé   | Ajouter l'email comme testeur dans Google Cloud              |
| `403 insufficientPermissions` | Mauvais scope ou compte sans accès GSC                      | Vérifier scope + compte connecté                             |
| `404 site not found`          | Mauvais `siteUrl` dans l'endpoint                           | Tester `sc-domain:schoolswp.com` vs `https://schoolswp.com/` |

---

## Ordre de test recommandé

```
1. GET /webmasters/v3/sites               → valider auth
2. POST searchAnalytics/query (page)      → valider données
3. POST searchAnalytics/query (page+query)→ valider topic discovery
```

---

## Résumé ultra court

**Google Cloud :**

- Search Console API activée
- OAuth Client ID (Web app)
- Callback URL n8n dans Authorized redirect URIs

**n8n Credential :**

- Authorization URL : `https://accounts.google.com/o/oauth2/v2/auth`
- Token URL : `https://oauth2.googleapis.com/token`
- Scope : `https://www.googleapis.com/auth/webmasters.readonly`

**HTTP Request node :**

- Auth : Predefined Credential Type → Google OAuth2
- Method : POST
- URL : `/webmasters/v3/sites/sc-domain:schoolswp.com/searchAnalytics/query`
