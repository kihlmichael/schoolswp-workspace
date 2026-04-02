# Pinterest Strategy System — schoolsWP

> Système de pilotage complet pour le compte Pinterest de schoolsWP.
> Auteur : Michaël KIHL | Date : avril 2026
> Langue : français | Ton : direct, pédagogique, chaleureux, structuré, authentique

---

## 1. Vue d'ensemble du système

Ce système de pilotage Pinterest couvre l'intégralité du cycle de vie du compte schoolsWP : de la création du profil à l'analyse mensuelle des performances, en passant par la production de pins, le calendrier éditorial et le suivi SEO Pinterest.

Il s'articule autour de 7 tableaux Google Sheets centralisés dans un dossier Google Drive dédié (ID : `1D10mjPHE_PEab5ajRUq7spoY4gleTSEY`). Chaque tableau a un rôle précis et des liens logiques avec les autres : le tableau SEO alimente les descriptions de boards et de pins, le calendrier éditorial pilote la cadence de publication, et le tableau de performances permet d'ajuster la stratégie chaque mois.

La logique est simple : **planifier > produire > publier > mesurer > ajuster**. Le système est conçu pour être maintenu par une seule personne, avec une charge hebdomadaire d'environ 2 heures.

---

## 2. Arborescence Google Drive

```
Pinterest/
  00 - Stratégie/
  01 - Boards/
  02 - Pins/
  03 - Visuels/
      WordPress/
      SEO/
      LMS/
      CRM/
      Automatisation/
      Plugins/
      Ecommerce/
      Freelance/
      Stratégie-contenu/
      Coulisses/
  04 - SEO & Mots-clés/
  05 - Calendrier éditorial/
  06 - Performances & KPI/
  07 - Archives/
      Visuels/
          2026/
          2027/
      Pins/
      Boards/
```

### Détail des dossiers

| Dossier                      | Utilité                                   | Contenu concret                                                           |
| ---------------------------- | ----------------------------------------- | ------------------------------------------------------------------------- |
| `00 - Stratégie/`            | Cadrage stratégique du compte Pinterest   | Fiche profil, positionnement, objectifs, notes de réflexion stratégique   |
| `01 - Boards/`               | Documentation des boards                  | Fichier de suivi des boards, descriptions SEO, catégories                 |
| `02 - Pins/`                 | Suivi opérationnel des pins               | Fichier de suivi des pins, briefs de création, notes d'optimisation       |
| `03 - Visuels/`              | Stockage des visuels produits             | Images, infographies, templates Canva, organisés par pilier de contenu    |
| `04 - SEO & Mots-clés/`      | Recherche et suivi de mots-clés Pinterest | Fichier de mots-clés, exports Pinterest Trends, analyses concurrentielles |
| `05 - Calendrier éditorial/` | Planification de la publication           | Calendrier semaine par semaine, 4-8 semaines à l'avance                   |
| `06 - Performances & KPI/`   | Analyse et reporting                      | Suivi mensuel des KPI globaux, par board et par pin                       |
| `07 - Archives/`             | Archivage du contenu obsolète             | Visuels anciens, pins archivés, boards désactivés, classés par année      |

---

## 3. Liste des tableaux à créer

| #   | Tableau                      | Objectif                                                  | Fréquence MAJ                   |
| --- | ---------------------------- | --------------------------------------------------------- | ------------------------------- |
| A   | Profil & Positionnement      | Fiche identitaire du compte Pinterest                     | Trimestrielle                   |
| B   | Suivi des Boards             | Piloter les boards, leurs descriptions SEO et leur statut | Mensuelle                       |
| C   | Suivi des Pins               | Suivre chaque pin du brief à la performance               | Continue (à chaque publication) |
| D   | Calendrier éditorial         | Planifier les publications 4-8 semaines à l'avance        | Hebdomadaire                    |
| E   | SEO & Mots-clés Pinterest    | Centraliser la recherche de mots-clés Pinterest           | Mensuelle                       |
| F   | Suivi des performances / KPI | Mesurer les résultats globaux et par contenu              | Mensuelle                       |
| G   | Backlog d'idées              | Stocker et prioriser les idées de pins                    | Continue                        |

---

## 4. Détail complet de chaque tableau

### A. Profil & Positionnement du compte

**Objectif** : centraliser toutes les informations identitaires du compte Pinterest schoolsWP.
**Rôle dans le système** : référence pour les descriptions de boards, le ton des pins et les mots-clés de profil. À consulter avant toute mise à jour du compte.
**Fréquence de MAJ** : trimestrielle ou lors d'un changement stratégique.
**Conseil pratique** : imprime cette fiche et garde-la visible quand tu rédiges des descriptions de boards ou de pins.

**Format : une ligne par champ (fiche, pas tableau multi-lignes)**

| Champ                 | Type  | Description                          | Valeur schoolsWP                                                                                                                   |
| --------------------- | ----- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| Nom du compte         | Texte | Nom affiché sur Pinterest            | schoolsWP                                                                                                                          |
| Bio                   | Texte | Description du profil (160 car. max) | WordPress. Clair. Structuré. Utile. Guides, tutoriels et stratégies WordPress pour créateurs de contenu, freelances et formateurs. |
| URL du site           | URL   | Lien vers le site principal          | https://schoolswp.com                                                                                                              |
| Piliers de contenu    | Texte | Liste des piliers éditoriaux         | LMS, CRM, SEO, automatisation, ecommerce, freelance, formation                                                                     |
| Audience cible        | Texte | Profils visés                        | Créateurs de contenu, freelances WordPress, formateurs, petites entreprises                                                        |
| Objectif Pinterest    | Texte | Objectif principal                   | Trafic qualifié vers les articles + notoriété de marque                                                                            |
| Mots-clés de profil   | Texte | 5-8 mots-clés pour le SEO du profil  | WordPress, SEO WordPress, LMS WordPress, CRM WordPress, automatisation WordPress, formation WordPress, WooCommerce                 |
| Catégorie Pinterest   | Texte | Catégorie principale du compte       | Éducation / Technologie                                                                                                            |
| Date création         | Date  | Date de création du compte           | Avril 2026                                                                                                                         |
| Dernière optimisation | Date  | Date de la dernière revue du profil  | --                                                                                                                                 |
| Notes                 | Texte | Remarques libres                     | Compte en lancement, phase de construction                                                                                         |

---

### B. Suivi des Boards

**Objectif** : piloter l'ensemble des boards Pinterest, leurs descriptions SEO, leur statut et leur performance globale.
**Rôle dans le système** : alimente le calendrier éditorial (chaque pin est associé à un board) et le tableau de performances.
**Fréquence de MAJ** : mensuelle (revue des descriptions, ajout de nouveaux boards).
**Conseil pratique** : vérifie chaque mois que chaque board a au moins 15 pins. Un board vide nuit au compte.

| Colonne               | Type             | Description                                    | Exemple                                                                              |
| --------------------- | ---------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------ |
| Nom du board          | Texte            | Nom affiché sur Pinterest                      | SEO WordPress : guides et optimisation                                               |
| Thématique / Pilier   | Liste déroulante | Pilier de contenu associé                      | SEO                                                                                  |
| Audience visée        | Texte            | Profil cible pour ce board                     | Blogueurs WordPress, freelances SEO                                                  |
| Mot-clé principal     | Texte            | Mot-clé SEO principal du board                 | SEO WordPress                                                                        |
| Mots-clés secondaires | Texte            | 3-5 mots-clés complémentaires                  | Rank Math, optimisation WordPress, référencement naturel WordPress, maillage interne |
| Description SEO       | Texte            | Description optimisée (300-500 car.)           | (voir section descriptions ci-dessous)                                               |
| Catégorie Pinterest   | Liste déroulante | Catégorie officielle Pinterest                 | Éducation / Technologie                                                              |
| URL cible             | URL              | Page principale vers laquelle le board renvoie | https://schoolswp.com/seo/                                                           |
| Nombre de pins        | Nombre           | Pins actuellement dans le board                | 0                                                                                    |
| Statut                | Liste déroulante | Actif / En pause / À optimiser / Archivé       | Actif                                                                                |
| Priorité              | Liste déroulante | P1 / P2 / P3                                   | P1                                                                                   |
| Date de création      | Date             | Date de création du board                      | 2026-04-15                                                                           |
| Dernière optimisation | Date             | Date de la dernière revue                      | --                                                                                   |
| Notes                 | Texte            | Remarques libres                               | Board de lancement, remplir avec 15 pins minimum                                     |

#### Descriptions SEO des 10 boards schoolsWP

**1. WordPress : guides et bonnes pratiques**

> WordPress est le CMS le plus utilisé au monde, mais la plupart des utilisateurs n'exploitent pas son vrai potentiel. Tu trouveras ici des guides pratiques, des tutoriels pas à pas et des bonnes pratiques pour construire un site WordPress performant, organisé et durable. Chaque pin t'amène vers un contenu clair et structuré sur schoolsWP, conçu pour les créateurs de contenu et les freelances qui veulent maîtriser WordPress sans jargon inutile.

**2. SEO WordPress : guides et optimisation**

> Améliorer ton référencement naturel WordPress avec des guides concrets, des tutoriels Rank Math et des stratégies de maillage interne. Ce board couvre tout le SEO on-page et technique pour WordPress : structure de contenu, optimisation des balises, sitemap, vitesse de chargement et stratégie de mots-clés. Des contenus testés et documentés sur schoolsWP pour gagner en visibilité sans devenir expert technique.

**3. LMS WordPress : créer et vendre des formations en ligne**

> Construire une plateforme de formation en ligne avec WordPress et TutorLMS. Ce board rassemble des guides pour créer tes cours, structurer ton catalogue, gérer tes apprenants et monétiser tes formations. Que tu sois formateur indépendant ou organisme de formation, tu trouveras des tutoriels clairs et des retours d'expérience concrets publiés sur schoolsWP pour lancer ton LMS sans usine à gaz.

**4. CRM et email marketing WordPress**

> Gérer tes contacts, segmenter ton audience et automatiser tes séquences email directement depuis WordPress avec FluentCRM. Ce board réunit des guides pratiques pour mettre en place un CRM efficace sans outil externe coûteux : formulaires, tags, séquences, segmentation et reporting. Des stratégies testées sur schoolsWP pour transformer tes visiteurs en audience fidèle.

**5. Automatisation WordPress : workflows et gain de temps**

> Automatiser les tâches répétitives de ton site WordPress avec n8n et les bons outils. Ce board présente des workflows concrets, des tutoriels d'automatisation et des stratégies pour gagner du temps sur la gestion de contenu, les notifications, les sauvegardes et la synchronisation de données. Des guides pratiques publiés sur schoolsWP pour les créateurs qui veulent travailler plus intelligemment.

**6. Plugins WordPress : tests, avis et comparatifs**

> Choisir les bons plugins WordPress parmi les milliers disponibles. Ce board rassemble des tests détaillés, des comparatifs honnêtes et des avis argumentés sur les plugins essentiels : SEO, sécurité, performance, formulaires, ecommerce et LMS. Des évaluations basées sur des tests réels documentés sur schoolsWP, sans sponsoring caché ni promesse exagérée.

**7. E-commerce WordPress : WooCommerce et vente en ligne**

> Vendre en ligne avec WordPress et WooCommerce sans complexité inutile. Ce board couvre la mise en place d'une boutique en ligne, la configuration des paiements, la gestion du catalogue produit, l'optimisation des fiches et les stratégies de conversion. Des guides structurés et des retours d'expérience concrets pour les entrepreneurs qui choisissent WordPress comme plateforme de vente.

**8. Freelance et business WordPress**

> Vivre de WordPress en tant que freelance ou entrepreneur. Ce board aborde le positionnement, la gestion de projet, la relation client, la tarification et les outils pour développer une activité WordPress durable. Des conseils pratiques et des retours d'expérience authentiques publiés sur schoolsWP pour celles et ceux qui construisent leur activité autour de WordPress.

**9. Stratégie de contenu WordPress : calendrier éditorial et clusters SEO**

> Planifier et structurer ta stratégie de contenu WordPress pour maximiser ton autorité thématique. Ce board couvre le calendrier éditorial, les clusters SEO, le maillage interne, la priorisation des sujets et l'organisation de la production de contenu. Des méthodes éprouvées et documentées sur schoolsWP pour publier avec régularité et cohérence.

**10. schoolsWP Coulisses : behind the scenes**

> Découvrir les coulisses de schoolsWP : choix techniques, processus de création, outils utilisés, résultats obtenus et leçons apprises. Ce board montre en toute transparence comment schoolsWP est construit et optimisé au quotidien. Des retours honnêtes sur ce qui fonctionne et ce qui ne fonctionne pas, pour inspirer les créateurs WordPress qui veulent progresser en toute authenticité.

---

### C. Suivi des Pins

**Objectif** : suivre chaque pin de l'idée à la publication et mesurer sa performance individuelle.
**Rôle dans le système** : tableau opérationnel central. Alimenté par le backlog et le calendrier. Reçoit les données de performance.
**Fréquence de MAJ** : continue (à chaque création ou publication de pin).
**Conseil pratique** : ne publie jamais un pin sans l'avoir d'abord enregistré ici. C'est ta source de vérité.

| Colonne               | Type             | Description                                                                        | Exemple                                                                                                                                                                        |
| --------------------- | ---------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ID pin                | Texte            | Identifiant unique                                                                 | PIN-SEO-001                                                                                                                                                                    |
| Titre SEO             | Texte            | Titre optimisé (40-100 car.)                                                       | Rank Math : guide complet pour optimiser ton SEO WordPress                                                                                                                     |
| Board associé         | Liste déroulante | Board de destination                                                               | SEO WordPress : guides et optimisation                                                                                                                                         |
| Pilier                | Liste déroulante | Pilier de contenu                                                                  | SEO                                                                                                                                                                            |
| URL de destination    | URL              | Lien vers l'article cible                                                          | https://schoolswp.com/rank-math-guide/                                                                                                                                         |
| Mot-clé principal     | Texte            | Mot-clé SEO principal                                                              | Rank Math WordPress                                                                                                                                                            |
| Mots-clés secondaires | Texte            | 2-4 mots-clés complémentaires                                                      | plugin SEO WordPress, optimiser SEO WordPress                                                                                                                                  |
| Description SEO       | Texte            | Description optimisée (150-300 car.)                                               | Rank Math est le plugin SEO le plus complet pour WordPress. Découvre comment le configurer pas à pas pour améliorer ton référencement naturel. Guide complet sur schoolsWP.com |
| Type de visuel        | Liste déroulante | Image statique / Infographie / Carrousel / Vidéo                                   | Image statique                                                                                                                                                                 |
| Format                | Liste déroulante | 1000x1500 / 1080x1080 / Autre                                                      | 1000x1500                                                                                                                                                                      |
| Angle du contenu      | Texte            | Angle éditorial du pin                                                             | Tutoriel pas à pas                                                                                                                                                             |
| CTA                   | Texte            | Appel à l'action                                                                   | Découvre le guide complet sur schoolsWP.com                                                                                                                                    |
| Statut                | Liste déroulante | Idée / Brief / En création / À valider / Planifié / Publié / À optimiser / Archivé | Idée                                                                                                                                                                           |
| Date prévue           | Date             | Date de publication prévue                                                         | 2026-04-20                                                                                                                                                                     |
| Date publiée          | Date             | Date de publication effective                                                      | --                                                                                                                                                                             |
| Impressions           | Nombre           | Nombre d'impressions                                                               | 0                                                                                                                                                                              |
| Clics                 | Nombre           | Clics sortants                                                                     | 0                                                                                                                                                                              |
| Sauvegardes           | Nombre           | Nombre de sauvegardes                                                              | 0                                                                                                                                                                              |
| Taux engagement       | Formule          | (clics + sauvegardes) / impressions × 100                                          | 0%                                                                                                                                                                             |
| Note d'optimisation   | Texte            | Remarques pour ré-optimisation                                                     | --                                                                                                                                                                             |

---

### D. Calendrier éditorial

**Objectif** : planifier les publications 4-8 semaines à l'avance avec un équilibre entre piliers et formats.
**Rôle dans le système** : pilote la cadence de publication. S'alimente depuis le backlog d'idées et le tableau de suivi des pins.
**Fréquence de MAJ** : hebdomadaire (chaque dimanche ou lundi).
**Conseil pratique** : commence par 3-5 pins par semaine. Augmente progressivement à 7-10 quand tu as du stock de visuels.

| Colonne           | Type             | Description                                      | Exemple                                                    |
| ----------------- | ---------------- | ------------------------------------------------ | ---------------------------------------------------------- |
| Semaine           | Texte            | Numéro de semaine                                | S16                                                        |
| Jour              | Liste déroulante | Lundi / Mardi / ... / Dimanche                   | Mardi                                                      |
| Date              | Date             | Date précise                                     | 2026-04-15                                                 |
| Pin prévu (titre) | Texte            | Titre du pin planifié                            | Rank Math : guide complet pour optimiser ton SEO WordPress |
| Board cible       | Liste déroulante | Board de destination                             | SEO WordPress : guides et optimisation                     |
| Pilier            | Liste déroulante | Pilier de contenu                                | SEO                                                        |
| Format            | Liste déroulante | Image statique / Infographie / Carrousel / Vidéo | Image statique                                             |
| Statut            | Liste déroulante | Planifié / Publié / Reporté / Annulé             | Planifié                                                   |
| Lien vers visuel  | URL              | Lien Google Drive du visuel                      | https://drive.google.com/...                               |
| Notes             | Texte            | Remarques                                        | Premier pin du board SEO                                   |

---

### E. SEO & Mots-clés Pinterest

**Objectif** : centraliser la recherche de mots-clés Pinterest pour alimenter les descriptions de boards, pins et le backlog.
**Rôle dans le système** : source de mots-clés pour tous les autres tableaux. Les mots-clés alimentent les descriptions SEO.
**Fréquence de MAJ** : mensuelle (ajouter de nouveaux mots-clés, vérifier les tendances).
**Conseil pratique** : utilise la barre de recherche Pinterest et Pinterest Trends comme sources principales. Les suggestions automatiques sont de l'or.

| Colonne                    | Type             | Description                                  | Exemple                                                 |
| -------------------------- | ---------------- | -------------------------------------------- | ------------------------------------------------------- |
| Mot-clé                    | Texte            | Mot-clé ou expression                        | WordPress LMS                                           |
| Volume estimatif           | Liste déroulante | Fort / Moyen / Faible                        | Moyen                                                   |
| Intention                  | Liste déroulante | Découverte / Inspiration / Décision / Action | Décision                                                |
| Pilier associé             | Liste déroulante | Pilier de contenu lié                        | LMS                                                     |
| Boards concernés           | Texte            | Boards utilisant ce mot-clé                  | LMS WordPress : créer et vendre des formations en ligne |
| Pins utilisant ce mot-clé  | Nombre           | Nombre de pins existants                     | 0                                                       |
| Tendance                   | Liste déroulante | Stable / Montant / Saisonnier                | Montant                                                 |
| Date dernière vérification | Date             | Date de la dernière vérification             | 2026-04-01                                              |
| Notes                      | Texte            | Remarques                                    | Vérifier en septembre (rentrée = pic LMS)               |

---

### F. Suivi des performances / KPI

**Objectif** : mesurer les résultats du compte Pinterest globalement et identifier les contenus les plus performants.
**Rôle dans le système** : alimente les décisions stratégiques mensuelles (quels piliers renforcer, quels boards optimiser).
**Fréquence de MAJ** : mensuelle (première semaine du mois pour le mois précédent).
**Conseil pratique** : remplis ce tableau le 1er de chaque mois. 15 minutes suffisent avec Pinterest Analytics ouvert.

| Colonne                | Type    | Description                               | Exemple    |
| ---------------------- | ------- | ----------------------------------------- | ---------- |
| Mois                   | Texte   | Mois concerné                             | Avril 2026 |
| Impressions totales    | Nombre  | Impressions globales du mois              | 0          |
| Clics sortants         | Nombre  | Clics vers le site                        | 0          |
| Sauvegardes totales    | Nombre  | Nombre de sauvegardes                     | 0          |
| Taux engagement global | Formule | (clics + sauvegardes) / impressions × 100 | 0%         |
| Abonnés                | Nombre  | Nombre d'abonnés en fin de mois           | 0          |
| Nouveaux abonnés       | Nombre  | Abonnés gagnés ce mois                    | 0          |
| Vues profil            | Nombre  | Vues du profil                            | 0          |
| Pins publiés ce mois   | Nombre  | Nombre de pins publiés                    | 0          |
| Top pin du mois        | Texte   | Titre du pin le plus performant           | --         |
| Top board du mois      | Texte   | Board le plus performant                  | --         |
| Top pilier du mois     | Texte   | Pilier avec le plus d'engagement          | --         |
| Observations           | Texte   | Analyse et enseignements                  | --         |

---

### G. Backlog d'idées

**Objectif** : stocker et prioriser toutes les idées de pins avant qu'elles n'entrent dans le calendrier éditorial.
**Rôle dans le système** : réservoir d'idées. Les idées validées passent dans le calendrier éditorial puis dans le suivi des pins.
**Fréquence de MAJ** : continue (ajouter des idées dès qu'elles apparaissent).
**Conseil pratique** : ne filtre pas à l'entrée. Ajoute toute idée, même vague. Le tri se fait après, pas avant.

| Colonne       | Type             | Description                                      | Exemple                                                  |
| ------------- | ---------------- | ------------------------------------------------ | -------------------------------------------------------- |
| Idée          | Texte            | Description courte de l'idée                     | Infographie : 5 erreurs SEO WordPress les plus courantes |
| Pilier        | Liste déroulante | Pilier de contenu                                | SEO                                                      |
| Type de pin   | Liste déroulante | Image statique / Infographie / Carrousel / Vidéo | Infographie                                              |
| Angle         | Texte            | Angle éditorial                                  | Erreurs à éviter                                         |
| Mot-clé cible | Texte            | Mot-clé visé                                     | erreurs SEO WordPress                                    |
| Priorité      | Liste déroulante | P1 / P2 / P3                                     | P2                                                       |
| Statut        | Liste déroulante | Idée / Validé / En production / Publié           | Idée                                                     |
| Date d'ajout  | Date             | Date d'ajout dans le backlog                     | 2026-04-01                                               |
| Notes         | Texte            | Remarques                                        | Peut être décliné en carrousel                           |

---

## 5. Statuts, conventions de nommage et règles de pilotage

### Statuts de workflow (pins)

```
Idée → Brief → En création → À valider → Planifié → Publié → À optimiser → Archivé
```

- **Idée** : dans le backlog, pas encore validée
- **Brief** : idée validée, brief rédigé (titre, mot-clé, angle, board cible)
- **En création** : visuel en cours de production
- **À valider** : visuel et texte prêts, en attente de validation
- **Planifié** : validé, date de publication fixée dans le calendrier
- **Publié** : en ligne sur Pinterest
- **À optimiser** : publié mais sous-performant, à retravailler
- **Archivé** : retiré ou obsolète

### Statuts de boards

```
Actif → En pause → À optimiser → Archivé
```

- **Actif** : board alimenté régulièrement, au moins 1 pin/mois
- **En pause** : temporairement inactif, pas de nouveaux pins
- **À optimiser** : description ou contenu à revoir
- **Archivé** : board désactivé, contenu obsolète

### Priorités

| Niveau | Signification                          | Délai                            |
| ------ | -------------------------------------- | -------------------------------- |
| P1     | Impact fort sur le trafic ou la marque | À traiter cette semaine          |
| P2     | Important pour la croissance           | À planifier sous 2 semaines      |
| P3     | Nice-to-have                           | Backlog, à placer quand possible |

### Conventions de nommage

| Élément           | Convention                                                     | Exemple                                                      |
| ----------------- | -------------------------------------------------------------- | ------------------------------------------------------------ |
| Fichier visuel    | `PIN-[pilier]-[sujet]-[format]-[date]`                         | `PIN-SEO-rank-math-1000x1500-20260415`                       |
| Board             | Nom lisible + mot-clé principal                                | `SEO WordPress : guides et optimisation`                     |
| Pin (titre)       | Mot-clé principal en début, 40-100 caractères                  | `Rank Math : guide complet pour optimiser ton SEO WordPress` |
| Description pin   | Mot-clé en première phrase, 150-300 car., CTA en fin           | (voir tableau C)                                             |
| Description board | 2-3 phrases, mots-clés naturels, 300-500 car., pas de hashtags | (voir section B)                                             |
| ID pin            | `PIN-[PILIER]-[numéro séquentiel]`                             | `PIN-SEO-001`, `PIN-LMS-012`                                 |

### Cadence de suivi

| Fréquence    | Actions                                                                   |
| ------------ | ------------------------------------------------------------------------- |
| Quotidien    | Publier les pins planifiés pour le jour                                   |
| Hebdomadaire | Revue du calendrier, alimentation du backlog, check performances rapides  |
| Mensuel      | Analyse KPI complète, ajustements stratégie, archivage, planification M+1 |

### Logique d'archivage

- **Pin sans engagement après 90 jours** : analyser le titre, la description et le visuel. Ré-optimiser ou archiver.
- **Board inactif depuis 60 jours** : évaluer la pertinence. Fusionner avec un autre board ou archiver.
- **Visuels anciens** : déplacer dans `07 - Archives/Visuels/[année]/`
- **Archivage = jamais de suppression** : tout est conservé dans le dossier Archives.

---

## 6. Checklist de mise en place initiale

- [ ] Créer un compte Pinterest Business (ou convertir un compte personnel)
- [ ] Choisir le nom d'affichage : schoolsWP
- [ ] Rédiger la bio du profil avec les mots-clés principaux (160 car. max)
- [ ] Ajouter l'URL du site (https://schoolswp.com) et la revendiquer
- [ ] Choisir la catégorie du compte (Éducation / Technologie)
- [ ] Ajouter le logo schoolsWP comme photo de profil
- [ ] Créer l'arborescence Google Drive (dossier Pinterest + 8 sous-dossiers)
- [ ] Créer les 7 tableaux Google Sheets avec les colonnes détaillées ci-dessus
- [ ] Remplir le tableau A (Profil & Positionnement)
- [ ] Créer les 10 boards avec leurs descriptions SEO (copier depuis la section 4.B)
- [ ] Faire une première session de recherche de mots-clés Pinterest (20-30 mots-clés)
- [ ] Remplir le tableau E (SEO & Mots-clés) avec les mots-clés trouvés
- [ ] Préparer 15-20 premiers pins (visuels + titres + descriptions)
- [ ] Planifier les 4 premières semaines dans le calendrier éditorial (3-5 pins/semaine)
- [ ] Installer le tag Pinterest sur schoolswp.com (vérification + suivi conversions)
- [ ] Activer Pinterest Analytics et vérifier qu'il remonte les données
- [ ] Publier les 3-5 premiers pins pour initialiser les boards prioritaires
- [ ] Vérifier l'affichage du profil sur mobile et desktop

---

## 7. Checklist hebdomadaire

À faire chaque semaine (idéalement le lundi matin, 30-45 min) :

- [ ] Publier les pins planifiés pour la semaine (ou les programmer via Pinterest)
- [ ] Vérifier que chaque pin publié a bien le bon lien, titre et description
- [ ] Mettre à jour le statut des pins dans le tableau C (Planifié → Publié)
- [ ] Consulter Pinterest Analytics : impressions et clics des 7 derniers jours
- [ ] Identifier le pin le plus performant de la semaine et noter pourquoi
- [ ] Ajouter 3-5 nouvelles idées dans le backlog (tableau G)
- [ ] Planifier la semaine suivante dans le calendrier éditorial (tableau D)
- [ ] Ré-épingler 1-2 pins performants des semaines précédentes dans d'autres boards pertinents
- [ ] Vérifier les tendances Pinterest sur tes piliers (barre de recherche + Pinterest Trends)
- [ ] S'assurer que tous les piliers sont représentés sur les 2 prochaines semaines

---

## 8. Checklist mensuelle

À faire le 1er de chaque mois (1h-1h30) :

- [ ] Remplir le tableau F (KPI) avec les données Pinterest Analytics du mois écoulé
- [ ] Identifier le Top 5 des pins les plus performants (impressions + clics + sauvegardes)
- [ ] Identifier le Flop 5 des pins les moins performants et analyser pourquoi
- [ ] Passer les pins sous-performants en statut "À optimiser" (nouveau visuel, titre ou description)
- [ ] Vérifier et mettre à jour les descriptions des boards si nécessaire
- [ ] Réordonner les pins dans chaque board (les plus performants en premier)
- [ ] Ajouter 5-10 nouveaux mots-clés dans le tableau E (SEO & Mots-clés)
- [ ] Archiver les pins sans engagement depuis 90+ jours
- [ ] Évaluer l'équilibre entre les piliers : chaque pilier a-t-il eu au moins 2 pins ce mois ?
- [ ] Planifier le mois suivant : 4 semaines dans le calendrier éditorial
- [ ] Vérifier le profil : bio, photo, URL, catégorie — tout est à jour ?

---

## 9. Erreurs à éviter

### 1. Boards trop génériques

"WordPress" ou "Inspiration" ne servent à rien. Un board doit avoir un angle précis et un mot-clé cible : "SEO WordPress : guides et optimisation" est trouvé par Pinterest, "WordPress" ne l'est pas.

### 2. Descriptions vides ou sans mots-clés

Pinterest est un moteur de recherche. Une description vide = un pin invisible. Chaque board et chaque pin doit avoir une description rédigée avec des mots-clés naturels.

### 3. Pins sans URL de destination

Un pin sans lien est une impasse. Chaque pin schoolsWP doit pointer vers un article du blog. C'est l'objectif numéro un : générer du trafic qualifié.

### 4. Publier en rafale puis disparaître

Pinterest récompense la régularité, pas les pics. Mieux vaut 3 pins par semaine pendant 12 mois que 50 pins la première semaine puis plus rien.

### 5. Ignorer Pinterest Analytics

Les données sont là pour piloter. Si tu ne regardes pas tes performances, tu ne sais pas ce qui fonctionne. 15 minutes par semaine suffisent.

### 6. Ne jamais ré-optimiser les anciens pins

Un pin publié il y a 3 mois peut être ré-optimisé : nouveau titre, nouvelle description, nouveau visuel. Pinterest redistribue du reach aux pins mis à jour.

### 7. Utiliser des hashtags

Les hashtags ne servent plus à rien sur Pinterest depuis 2023. Ils n'améliorent pas la découverte et prennent de la place dans tes descriptions. À supprimer.

### 8. Copier les descriptions entre pins

Chaque pin doit avoir une description unique. Pinterest pénalise le contenu dupliqué, y compris les descriptions identiques sur des pins différents.

### 9. Négliger le format 1000x1500

Le format vertical 2:3 (1000x1500 px) est le format natif de Pinterest. Les images carrées ou horizontales sont désavantagées dans le flux. Utilise le bon format.

### 10. Créer trop de boards dès le départ

Commence avec 8-10 boards bien remplis (15+ pins chacun) plutôt que 25 boards à 2 pins. Un board vide fait amateur et n'est pas poussé par l'algorithme.

### 11. Oublier le CTA dans les descriptions de pins

La description doit guider l'utilisateur. Termine toujours par un CTA clair : "Découvre le guide complet sur schoolsWP.com" ou "Lis l'article sur schoolsWP.com".

### 12. Mélanger les thématiques dans un même board

Un board = un sujet. Ne mets pas un pin sur WooCommerce dans le board SEO. La cohérence thématique est un signal fort pour l'algorithme Pinterest.

---

## 10. Conseils finaux de pilotage

### 1. Traite Pinterest comme un moteur de recherche, pas un réseau social

Pinterest fonctionne par mots-clés et intention de recherche, pas par likes et commentaires. Investis ton temps dans les descriptions SEO, pas dans l'engagement social.

### 2. La régularité vaut plus que le volume

3-5 pins par semaine publiés régulièrement pendant 6 mois produiront plus de résultats que 100 pins publiés en une semaine. Programme tes publications à l'avance.

### 3. Chaque pin est un investissement long terme

Un pin a une durée de vie de 3-6 mois (contre quelques heures sur les réseaux sociaux). Chaque pin bien optimisé continue de générer du trafic des mois après sa publication.

### 4. Mesure ce qui compte : les clics sortants

Les impressions flattent l'ego, mais l'objectif schoolsWP est le trafic vers le blog. Concentre ton analyse sur les clics sortants et le taux de clic.

### 5. Réutilise tes meilleurs contenus

Un article performant sur le blog peut générer 3-5 pins différents (angles différents, visuels différents). Ne te limite pas à un pin par article.

### 6. Fais évoluer le système, pas le complexifier

Ce système de pilotage doit rester simple. Si un tableau devient trop lourd, simplifie-le. Si une colonne n'est jamais remplie, supprime-la. L'outil doit servir la stratégie, pas l'inverse.

### 7. Revois ta stratégie tous les 3 mois

Tous les trimestres, prends 1 heure pour revoir les performances globales, ajuster les piliers de contenu et identifier de nouvelles opportunités de mots-clés. Le système doit s'adapter, pas se figer.

### 8. Documente tes apprentissages

Utilise la colonne "Notes" de chaque tableau pour consigner ce que tu apprends. Dans 6 mois, ces notes vaudront plus que n'importe quel cours Pinterest.

---

_Document généré le 1er avril 2026 dans le cadre du système de pilotage Pinterest schoolsWP._
_Dossier Google Drive : `1D10mjPHE_PEab5ajRUq7spoY4gleTSEY`_
