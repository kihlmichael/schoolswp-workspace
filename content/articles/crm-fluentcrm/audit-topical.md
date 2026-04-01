# Audit SEO — Autorité Thématique schoolsWP

## Score Autorité : 74/100

---

## Détail :

**Couverture : 15/20**
**Connexions : 16/20**
**Cohérence : 17/20**
**Positionnement : 15/20**
**Potentiel cluster : 11/20**

---

## Manques identifiés :

- **[CRITIQUE] Absence totale de traitement de la délivrabilité email** — Le SMTP est mentionné comme prérequis technique mais le sujet de la délivrabilité (réputation de domaine, warm-up, taux d'ouverture, SPF/DKIM/DMARC) n'est pas abordé. C'est pourtant un angle décisionnel majeur pour un solopreneur qui migre depuis Mailchimp : il veut savoir si ses emails vont atterrir en boîte de réception, pas juste si le plugin envoie.

- **[CRITIQUE] Aucun retour chiffré ou test terrain propriétaire** — L'article mentionne "dans mon cas, sur schoolsWP, j'ai observé…" mais ne livre aucune donnée concrète : taux d'ouverture observé, volume de contacts testé, temps de mise en place réel, comparaison avant/après fragmentation. La promesse terrain est posée mais jamais tenue. C'est le principal écart entre l'angle affiché et ce que le lecteur reçoit réellement.

- **[SECONDAIRE] Le module pipeline/suivi commercial est évacué trop rapidement** — L'article dit que FluentCRM n'est pas HubSpot, mais ne montre pas ce que FluentCRM fait réellement côté suivi deal/opportunité. Pour une intention décisionnelle, l'acheteur veut savoir jusqu'où va le CRM : y a-t-il une vue contact enrichie, un historique d'activité, une notion de "deal stage" ? Ce gap laisse une zone floue pour le lecteur qui hésite entre FluentCRM et un outil commercial léger.

- **[SECONDAIRE] Absence de mention de Groundhogg** — Concurrent direct natif WordPress, souvent cité dans les comparatifs SERP sur ce mot-clé. Son absence dans le comparatif affaiblit la crédibilité exhaustive de l'article sur une intention décisionnelle.

- **[SECONDAIRE] Pas de section sur les limites réelles de FluentCRM** — Les limites citées ("gros volumes", "équipe commerciale") sont des cas de non-usage évidents. Les vraies limites terrain — bugs connus, support réactif ou non, contraintes de la base de données WordPress sous charge, absence de fonctions A/B testing sur les séquences — ne sont pas abordées. Un article décisionnel honnête les traite.

---

## Opportunités de cluster :

- **Article satellite 1 : "Comment configurer FluentSMTP avec Amazon SES pour envoyer 10 000 emails sans toucher ta délivrabilité" | Angle technique-terrain avec mise en place pas-à-pas et coût réel (SES = ~0,10$/1000 emails) | Lien logique direct : l'article pilier cite explicitement ce besoin SMTP mais ne le résout pas — satellite naturel à fort potentiel de trafic long tail**

- **Article satellite 2 : "FluentCRM + LearnDash : construire une séquence d'onboarding qui réduit l'abandon de formation" | Angle cas d'usage complet pour formateurs (le profil cible schoolsWP par excellence) avec automatisation réelle documentée étape par étape | Lien logique : l'article pilier identifie ce profil comme idéal mais ne lui donne aucun système concret — ce satellite transforme l'intention en exécution**

- **Article satellite 3 : "FluentCRM vs ActiveCampaign : le test côte à côte pour un freelance WordPress à moins de 5 000 contacts" | Angle comparatif décisionnel approfondi avec critères pondérés, captures d'écran, et verdict tranché par profil | Lien logique : le tableau comparatif de l'article pilier est trop synthétique pour clore la décision — ce satellite capte les requêtes "fluentcrm vs activecampaign" avec une profondeur que le pilier ne peut pas offrir sans se diluer**

- **Article satellite 4 : "Structurer ses listes et tags FluentCRM : la méthode pour ne jamais repartir de zéro" | Angle méthodologique sur l'architecture CRM (étape 3 de l'article pilier développée en standalone) | Lien logique : c'est l'étape que l'article qualifie lui-même de "stratégique que beaucoup sautent" — signal fort qu'elle mérite sa propre profondeur**

---

## Recommandation stratégique : Satellite fort → À renforcer avant publication

**Justification :** L'article a la structure et le positionnement d'un bon pilier CRM, mais il manque la substance terrain qui justifie ce statut sur une intention décisionnelle compétitive. En l'état, il surpasse un article généraliste SERP sur la forme, mais pas encore sur la preuve — le lecteur qui arrive avec une décision à prendre repart sans les éléments différenciants que seul schoolsWP peut apporter (données réelles, limites honnêtes, système complet). Deux ajouts critiques suffiraient à changer la donne : un bloc "retour terrain chiffré" et une section délivrabilité traitée sérieusement.