---
name: linkbuilding-outreach
description: |
  Analyse des prospects backlinks, qualification d'opportunites et redaction d'emails d'outreach
  hyper-personnalises pour schoolsWP. Utilise ce skill des que l'utilisateur veut obtenir des backlinks,
  analyser un prospect pour du link building, rediger un email d'outreach, qualifier une opportunite
  de lien, traiter un lot de prospects CSV/Google Sheets, ou parle de "backlink", "outreach",
  "link building", "netlinking", "prospect backlink", "email de demande de lien", "guest post",
  "digital PR", meme s'il ne mentionne pas explicitement "outreach" ou "link building".
  Ne pas utiliser pour : SEO on-page, audit technique, redaction d'articles, maillage interne.
allowed-tools:
  - mcp__firecrawl__firecrawl_scrape
  - Bash
  - Read
  - Write
  - Agent
---

# Link Building Outreach — schoolsWP

Transforme des opportunites de backlinks en recommandations d'outreach actionnables pour schoolsWP.

Le principe fondamental : **la pertinence editoriale prime sur la quantite**. Un email d'outreach ne
vaut la peine d'etre envoye que si le lien propose apporte une vraie valeur au lecteur du prospect.
Si le fit est artificiel, mieux vaut ne pas envoyer et le dire franchement.

---

## Entrees attendues

L'utilisateur fournit au minimum :
- **URL prospect** : la page ou le site a analyser comme cible de backlink
- **URL a promouvoir** : la page schoolsWP qu'on souhaite faire lier

Optionnellement :
- **Contexte** : precision sur l'angle, la raison du ciblage, une relation existante
- **Google Sheet** : un lot de prospects (lu via `gws` CLI)
- **CSV/fichier** : un lot de prospects en fichier local

## Pipeline d'execution

### 1. Collecte du contenu

Scrape les deux URLs avec Firecrawl pour obtenir le contenu reel :

```
firecrawl_scrape({ url: "<url>", formats: ["markdown"] })
```

Si Firecrawl echoue ou retourne un contenu trop pauvre, signale-le explicitement dans le rapport
(`Statut d'acces : partiel` ou `inaccessible`). Ne jamais extrapoler au-dela du contenu reellement
obtenu.

**Mode batch (Google Sheet)** : lire le Sheet via `gws` CLI, detecter automatiquement les colonnes
pertinentes (url_prospect, url, lien, target, page, contexte, langue, priorite...), puis boucler
sur chaque ligne. Chaque prospect recoit une analyse individualisee — zero copier-coller generique.

### 2. Analyse du prospect

Identifie a partir du contenu scrape :
- Sujet principal, angle editorial, ton, niveau de profondeur
- Public probable
- **Points d'accroche precis** : passages, exemples, ressources, formulations ou idees
  qu'on peut citer dans l'email pour prouver qu'on a lu la page
- Themes connexes ou recents visibles

**Signaux de prudence** (disqualifiants ou degradants) :
- Page trop pauvre, trop commerciale, trop affiliee
- Absence de coherence editoriale, page obsolete, hors sujet
- Listicle trop large sans angle precis
- Pas d'auteur visible, pas de logique editoriale
- Page qui ne semble pas accueillir de ressources externes

### 3. Analyse de la page a promouvoir

Evalue honnetement :
- Sujet exact, promesse, valeur ajoutee reelle
- Ce qu'elle apporte de complementaire, plus clair, plus pratique ou plus actuel
- Interet reel pour le prospect et son audience

Pour une page schoolsWP, evaluer specifiquement : niveau pedagogique, clarte de structure,
utilite concrete, presence d'exemples/comparatifs/FAQ/retours de tests, coherence avec
l'audience du prospect.

**Regle d'honnetete** : si la page schoolsWP n'apporte rien de substantiellement utile au
prospect, dis-le clairement. Ne jamais forcer un fit qui n'existe pas.

### 4. Qualification

Classe l'opportunite dans une seule categorie :

| Niveau | Criteres |
|---|---|
| **Tres pertinente** | Forte coherence editoriale + forte utilite + accroche credible + email legitime |
| **Pertinente** | Bonne coherence globale + angle valable + outreach possible |
| **Faible** | Fit partiel, peu de valeur ajoutee, personnalisation trop legere |
| **A eviter** | Fit artificiel, contenu inaccessible, manque de valeur, outreach non credible |

Si "Faible" ou "A eviter" : recommander explicitement de ne pas envoyer.

### 5. Email d'outreach (uniquement si Tres pertinente ou Pertinente)

Redige un email qui respecte ces principes :
- Court, clair, humain, credible — semble ecrit a la main
- Mentionne un element precis reellement observe sur la page prospect
- Transition naturelle vers la ressource schoolsWP
- Proposition de lien non forcee

**Detection de langue** : si le prospect est francophone, rediger en francais. Si anglophone,
en anglais. S'adapter au contexte le plus naturel pour le destinataire.

#### Ton schoolsWP obligatoire

Direct, pedagogique, chaleureux, structure, authentique.
Phrases courtes. Concret. Aucune flatterie vide. Aucune formule cliche. Aucun ton spammy.

Formulations compatibles :
- "dans mon cas", "sur schoolsWP", "d'apres mes tests"
- "j'ai documente", "j'ai remarque"
- "ca peut completer ce passage", "ca peut etre utile a tes lecteurs"
- "si tu estimes que ca apporte quelque chose"

**Interdits absolus** :
- "Je me permets de vous contacter car..."
- "J'ai adore votre excellent article..."
- "Nous avons une ressource qui pourrait interesser vos lecteurs..."
- "Cela serait benefique pour votre SEO..."
- Tout compliment non prouve, toute demande insistante, toute phrase template

#### Si opportunite Faible ou A eviter

Ne pas ecrire de faux bon email. Proposer des alternatives non intrusives si pertinentes :
- Suivre le prospect, commenter un contenu
- Creer une meilleure ressource, chercher une autre page plus coherente
- Ameliorer la page schoolsWP avant outreach

### 6. Variantes et suivi (uniquement si outreach recommande)

Generer :
- **5 objets d'email** : 2 sobres, 2 curiosite, 1 tres direct
- **2 relances** : 1 courte et simple, 1 plus contextualisee
- **5 anchor texts** : naturels, editoriaux, non suroptimises — des formulations qu'un editeur
  integrerait reellement, pas des mots-cles SEO bruts

### 7. Sauvegarde

Sauvegarder le rapport complet en `.md` dans `content/outreach/` avec le format de nom :
`YYYY-MM-DD_prospect-domain.md` (ex: `2026-04-06_wpmarmite.md`).

Pour le mode batch : un fichier par prospect, plus un fichier recapitulatif
`YYYY-MM-DD_batch-summary.md` avec le tableau des qualifications.

---

## Format de sortie

Chaque prospect produit exactement cette structure :

```markdown
# Prospect
- URL prospect :
- URL a promouvoir :
- Contexte eventuel :
- Statut d'acces au contenu : accessible / partiel / inaccessible
- Langue probable de contact :
- Identifiant CSV si present :

# Analyse du prospect
- Sujet principal :
- Angle editorial :
- Ton :
- Niveau de profondeur :
- Public probable :
- Points precis reperes :
- Themes connexes ou recents visibles :
- Signaux de prudence :
- Limites d'analyse :

# Analyse de la page a promouvoir
- Sujet :
- Promesse :
- Valeur ajoutee :
- Interet potentiel pour le prospect :
- Cette ressource merite-t-elle d'etre proposee ? oui / non / incertain
- Pourquoi :

# Qualification de l'opportunite
- Niveau :
- Justification :
- Recommandation : envoyer / ne pas envoyer

# Email principal
Objet :
Email :

# Variantes d'objet
1.
2.
3.
4.
5.

# Relance 1
Objet :
Email :

# Relance 2
Objet :
Email :

# Suggestions d'anchor text
1.
2.
3.
4.
5.

# Note strategique
- Pourquoi cet outreach a une chance de fonctionner :
- Risque principal :
- Amelioration possible avant envoi :
- Alternative si non-envoi :
```

---

## Heuristiques de fit schoolsWP

**Prospects prioritaires** — ceux qui publient sur :
WordPress, plugins WP, SEO WordPress, automatisation, CRM/email marketing WP, LMS/formation
en ligne, comparatifs d'outils, guides pour freelances/createurs/formateurs/independants,
performance, maintenance, conversion, acquisition, contenus IA dans un contexte WordPress.

**Prospects souvent non prioritaires** :
Annuaires sans ligne editoriale, fermes a liens, pages ultra-commerciales sans contenu,
sites sans coherence thematique, contenus trop eloignes du perimetre schoolsWP.

---

## Regles critiques

1. Ne jamais inventer un detail non observe dans le contenu scrape
2. Ne jamais inventer une personnalisation non verifiable
3. Ne jamais ecrire un email generique si les elements observables sont trop faibles
4. Ne jamais forcer une opportunite de lien faible
5. Signaler clairement toutes les limites d'analyse
6. Si l'opportunite est mauvaise, le dire franchement — la credibilite de schoolsWP en depend
