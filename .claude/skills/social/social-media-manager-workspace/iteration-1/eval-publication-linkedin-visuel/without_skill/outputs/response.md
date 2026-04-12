# Evaluation -- Publication LinkedIn + Visuel Carrousel (sans skill)

**Date** : 2026-04-06
**Tache** : Publier un post LinkedIn pour schoolsWP + creer un visuel carrousel avec Blotato
**Mode** : Simulation (pas d appels API reels)

---

## 1. Post LinkedIn redige

J ai teste 5 plugins de formulaire WordPress pendant 2 semaines.

Pas un test rapide de 30 minutes.
14 jours. Sur de vrais sites. Avec de vrais utilisateurs.

Voici mon classement :

1. Fluent Forms -- le meilleur rapport qualite/fonctionnalites
2. WS Form -- le plus puissant techniquement
3. Gravity Forms -- la reference historique (mais le prix pique)
4. WPForms -- le plus simple pour debuter
5. Forminator -- la bonne surprise gratuite

Ce que j ai regarde :
- Facilite de prise en main (un debutant peut-il creer un formulaire en 5 min ?)
- Fonctionnalites avancees (logique conditionnelle, calculs, multi-etapes)
- Performances (impact sur le temps de chargement)
- Integrations (CRM, email, paiement)
- Prix reel sur 1 an

Le resultat m a surpris sur 2 points :
Un plugin gratuit fait mieux que certains premium
Le plus cher n est pas le meilleur

L article complet avec les benchmarks detailles :
https://schoolswp.com/meilleurs-plugins-formulaire-wordpress/

---

Tu utilises lequel ? Dis-moi en commentaire.

#WordPress #Formulaire #PluginWordPress #schoolsWP #WebDesign #SiteWeb

---

## 2. Requetes curl -- Publication LinkedIn (simulee)

### Etape 1 : Enregistrer le document carrousel (PDF multi-pages)

    curl -X POST "https://api.linkedin.com/v2/assets?action=registerUpload"       -H "Authorization: Bearer {LINKEDIN_ACCESS_TOKEN}"       -H "Content-Type: application/json"       -d '{
        "registerUploadRequest": {
          "recipes": ["urn:li:digitalmediaRecipe:feedshare-document"],
          "owner": "urn:li:person:{PERSON_ID}",
          "serviceRelationships": [
            {
              "relationshipType": "OWNER",
              "identifier": "urn:li:userGeneratedContent"
            }
          ]
        }
      }'

### Etape 2 : Upload du PDF carrousel

    curl -X PUT "{UPLOAD_URL_FROM_STEP_1}"       -H "Authorization: Bearer {LINKEDIN_ACCESS_TOKEN}"       -H "Content-Type: application/pdf"       --data-binary "@carrousel-formulaires-wordpress.pdf"

### Etape 3 : Publier le post avec le document attache

    curl -X POST "https://api.linkedin.com/v2/ugcPosts"       -H "Authorization: Bearer {LINKEDIN_ACCESS_TOKEN}"       -H "Content-Type: application/json"       -H "X-Restli-Protocol-Version: 2.0.0"       -d '{
        "author": "urn:li:person:{PERSON_ID}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
          "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
              "text": "J ai teste 5 plugins de formulaire WordPress..."
            },
            "shareMediaCategory": "ARTICLE",
            "media": [{
              "status": "READY",
              "media": "{ASSET_URN_FROM_STEP_1}",
              "title": {"text": "Top 5 plugins formulaire WordPress - Comparatif 2026"}
            }]
          }
        },
        "visibility": {
          "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
      }'

Note : LinkedIn ne supporte pas les carrousels multi-images via API v2. Le format carrousel passe par un upload de document PDF multi-pages.

---

## 3. Visuel carrousel -- Brief pour Blotato

### Probleme : Blotato non accessible via API ou MCP

Blotato est un outil web de creation de carrousels LinkedIn. Il ne propose pas d API publique ni de MCP. La creation du carrousel ne peut pas etre automatisee.

### Approche recommandee

**Option A -- Manuelle via Blotato (blotato.com) :**
1. Aller sur https://blotato.com
2. Creer un nouveau carrousel
3. Utiliser le contenu ci-dessous pour les slides

**Option B -- Generation PDF via script Python ou HTML-to-PDF :**
Creer un PDF multi-pages (chaque page = 1 slide) et uploader comme document LinkedIn.

### Contenu des slides du carrousel

**Slide 1 (couverture) :**
- Titre : "5 plugins de formulaire WordPress testes pendant 2 semaines"
- Sous-titre : "Mon classement honnete"
- Branding : schoolsWP

**Slide 2 :** #1 Fluent Forms -- "Le meilleur rapport qualite/fonctionnalites" -- Score : 9.2/10

**Slide 3 :** #2 WS Form -- "Le plus puissant techniquement" -- Score : 8.8/10

**Slide 4 :** #3 Gravity Forms -- "La reference historique (le prix pique)" -- Score : 8.5/10

**Slide 5 :** #4 WPForms -- "Le plus simple pour debuter" -- Score : 8.2/10

**Slide 6 :** #5 Forminator -- "La bonne surprise gratuite" -- Score : 7.9/10

**Slide 7 :** Tableau comparatif : prise en main, fonctionnalites, performances, integrations, prix

**Slide 8 (CTA) :** "L article complet avec tous les benchmarks" -- schoolswp.com/meilleurs-plugins-formulaire-wordpress/ -- Logo schoolsWP + @michaelkihl

### Specifications visuelles
- Format : 1080x1350px (portrait LinkedIn)
- Couleurs : fond blanc, accents bleu schoolsWP (#2563EB), texte noir/gris fonce
- Typographie : Inter ou Poppins, titres bold
- Style : clean, minimaliste, chiffres bien visibles

---

## 4. Limites identifiees (sans skill)

| Dimension | Constat |
|---|---|
| Post LinkedIn | Redige manuellement -- pas de template branding automatique |
| API LinkedIn | Requetes curl correctes mais carrousels = PDF obligatoire |
| Blotato | Aucune integration possible -- web-only sans API |
| Hashtags | Choisis manuellement -- pas d analyse de performance |
| Timing | Pas de recommandation de publication basee sur analytics |
| UTM | Pas de parametres UTM ajoutes au lien |
| Branding | Pas de verification automatique du ton/voix schoolsWP |

---

## 5. Resume des appels (simulation)

    1. POST /v2/assets?action=registerUpload  -> enregistrer le PDF carrousel
    2. PUT  {uploadUrl}                        -> uploader le fichier PDF
    3. POST /v2/ugcPosts                       -> publier le post avec le document attache

Aucun appel reel effectue -- simulation uniquement.
