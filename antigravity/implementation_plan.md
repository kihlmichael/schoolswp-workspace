# Plan d'Alignement Branding schoolsWP - CRM Local

Ce document détaille la stratégie et les étapes pour réécrire et polir le brouillon de l'article "Pourquoi installer un CRM local sur WordPress ?" afin de respecter à la lettre la charte éditoriale et la typographie de schoolsWP.

---

## 1. Diagnostic de l'existant & Écarts Branding

Nous avons audité le fichier [pourquoi_crm_local_wordpress.md](file:///d:/ANTIGRAVITY/outputs/pourquoi_crm_local_wordpress.md) par rapport aux fichiers officiels [BRAND_RULES.md](file:///D:/VS%20Code/CLAUDE%20CODE/projects/schoolswp/content/docs/BRAND_RULES.md) et [BRAND_CHECKLIST.md](file:///D:/VS%20Code/CLAUDE%20CODE/projects/schoolswp/content/docs/BRAND_CHECKLIST.md) extraits du projet principal. 

Voici les écarts majeurs identifiés :
* **Longueur des phrases :** Plusieurs phrases dépassent largement la limite stricte de 20 mots (certaines atteignent 34 mots). La charte exige 8 à 15 mots en moyenne.
* **Typographie :** Aucun nom d'outil n'est formaté en italique. La charte impose l'italique pour tous les logiciels et extensions (*FluentCRM*, *Fluent Forms*, *Fluent Support*, *FluentBoards*, *WordPress*, *HubSpot*, *ActiveCampaign*, *Zapier*, *Make*, *Salesforce*).
* **Naming "schoolsWP" :** Le nom de la marque `schoolsWP` n'est mentionné nulle part. Nous devons l'ancrer en y ajoutant des retours d'expérience personnels ("sur schoolsWP", "d'après mes tests").
* **Mots "borderline" ou interdits :** Présence de termes comme "simplement" (dans un contexte flou) et manque de rythme direct sujet-verbe-complément.
* **Manque de sources obligatoires :** La règle 33 impose une section finale `## Sources & ressources` (H2) avec les liens/outils cités.
* **Manque du bloc QA :** Le bloc de signature `**Brand QA** - schoolsWP` avec les scores de validation est absent.

---

## 2. Plan de Réécriture Chirurgicale

Nous allons procéder à une réécriture section par section en appliquant les consignes suivantes :

### A. Formatage et Structure :
1. **Longueur maximale :** 20 mots par phrase. 8-15 mots en moyenne. Raccourcir en coupant les phrases longues avec un point "." ou des deux-points " : ".
2. **Italiques systématiques :** *FluentCRM*, *Fluent Forms*, *Fluent Support*, *FluentBoards*, *WordPress*, *HubSpot*, *ActiveCampaign*, *Zapier*, *Make*, *Salesforce*.
3. **Paragraphes aérés :** 2 à 4 phrases par paragraphe, séparés par un saut de ligne double.
4. **Zéro tiret interdit :** Aucun tiret em-dash "-" ou en-dash "–". Remplacer par des tirets courts espacés " - " ou des deux-points " : ".
5. **Gras ciblé :** Seulement sur les termes clés essentiels, sans surcharge.
6. **Maximum 1 émoji par section**, aucun émoji en cascade.

### B. Intégration de l'Expérience schoolsWP (Michael) :
* Remplacer les déclarations impersonnelles par des ancrages concrets : *"Dans mon cas, j'utilise FluentCRM..."*, *"Sur schoolsWP, j'ai fait le choix de..."*, *"Depuis 2021..."*.

### C. Ajout des sections requises :
* **Sources & ressources (H2)** : Liste formatée avec les outils cités et leur année.
* **Brand QA Footer** :
  ```markdown
  **Brand QA** - schoolsWP
  Ton : 5/5 | Clarté : 5/5 | Valeurs : 5/5 | Interdits : 5/5 | Vocabulaire : 5/5
  ```

---

## 3. Validation de l'utilisateur

> [!IMPORTANT]
> Pour respecter la règle 2 (Data Safety) et la règle 4 de `gemini.md` :
> **Es-tu d'accord avec cette grille de réécriture et l'analyse des écarts ?**
> Une fois ton feu vert reçu, je lancerai la réécriture pour reconstruire l'article final.
