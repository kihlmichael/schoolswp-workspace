# Plan de correction FR — post 2969996 (à appliquer dès fin de maintenance)

> Méthode : remplacements chirurgicaux in-place via Novamira (str_replace ciblés pour le texte, remplacement de bloc pour la table), sauvegarde en préservant l'échappement des blocs Kadence (slash). Aucune réécriture complète. Bloqué le 2026-06-03 par maintenance planifiée EasyHoster (503).

## Sources des données factuelles (prix/note)

- Prix annuels (PAA Google via booknetic.com) : Basic 45 $/an, Standard 99 $/an, Premium 199 $/an, Elite 299 $/an (add-ons inclus : 0 / 8 / 19 / 50+). Licence à vie Basic environ 99 $ (blogvault).
- Note : 4,93/5 sur 444 avis CodeCanyon (booknetic.com, 2026-05) ; Capterra 4,5/103 ; Trustpilot 3,2/22.
- A revérifier sur la page officielle au moment de publier (les prix bougent).

## B1 + I5 — Tutoiement + voix « mon avis »

| Avant                                                  | Après                                                |
| ------------------------------------------------------ | ---------------------------------------------------- |
| pour voir si votre portefeuille valide                 | pour voir si ton portefeuille valide                 |
| correspond-il vraiment à votre quotidien professionnel | correspond-il vraiment à ton quotidien professionnel |
| Vous ne manipulez pas un simple calendrier             | Tu ne manipules pas un simple calendrier             |
| Votre image de marque gagne en crédibilité             | Ton image de marque gagne en crédibilité             |
| gage de sérieux immédiat pour vos clients              | gage de sérieux immédiat pour tes clients            |
| Si vous gérez un seul service basique                  | Si tu gères un seul service basique                  |
| transforme votre taux de conversion                    | transforme ton taux de conversion                    |
| Résumé de notre avis sur Booknetic (note 4,5/5)        | Résumé de mon avis sur Booknetic (note 4,93/5)       |

## B2 — FAQ en français

| Avant                                                         | Après                                                         |
| ------------------------------------------------------------- | ------------------------------------------------------------- |
| Questions? We Have Answers.                                   | Des questions ? Voici les réponses.                           |
| Get answers to a list of the most Frequently Asked Questions. | Les réponses aux questions les plus fréquentes sur Booknetic. |

## B4 + I1 — Prix réels + table native (bloc HTML brut remplacé par un bloc tableau Gutenberg natif)

Nouvelle table (4 colonnes : Formule, Prix annuel, Add-ons inclus, Idéal pour) :

| Formule  | Prix annuel | Add-ons inclus | Idéal pour                |
| -------- | ----------- | -------------- | ------------------------- |
| Basic    | 45 $/an     | 0              | Tester l'outil, 1 service |
| Standard | 99 $/an     | 8              | Indépendant, TPE          |
| Premium  | 199 $/an    | 19             | Multi-services            |
| Elite    | 299 $/an    | 50+            | Agences, multi-sites      |

Légende : « Tarifs annuels Booknetic. Licence à vie Basic disponible autour de 99 $. »

Mentions inline du prix :

| Avant                                                                                                                      | Après                                                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| licence à vie dès 79 $ sur CodeCanyon                                                                                      | licence à vie dès 99 $ sur CodeCanyon                                                                                                                                                                                                                        |
| licence à vie à 79 $ sur CodeCanyon                                                                                        | licence à vie à 99 $ sur CodeCanyon                                                                                                                                                                                                                          |
| FAQ : « ...plan Basic à vie, mais je te recommande de regarder le plan Standard à 229 $ qui inclut plus de 45 modules... » | « Les formules annuelles vont de 45 $ (Basic) à 299 $ (Elite) selon le nombre d'add-ons inclus, et une licence à vie Basic est disponible autour de 99 $. Pour la plupart des indépendants, le plan Standard (99 $/an, 8 add-ons) couvre déjà l'essentiel. » |

## B5 + A6 — Note unifiée + nettoyage markup

| Avant                                              | Après                                                            |
| -------------------------------------------------- | ---------------------------------------------------------------- |
| 4,91/5 (2 occurrences)                             | 4,93/5                                                           |
| La note de 4.5/5 souligne une satisfaction réelle. | La note de 4,93/5 sur 444 avis souligne une satisfaction réelle. |
| balises meta charset parasites dans les accordéons | supprimées                                                       |

## I2 — Lien interne incohérent (ancre « plugin de tableau » pointant vers /design-wordpress/)

Avant : « Pour comparer avec un autre [meilleur plugin de tableau](/design-wordpress/) bien noté, la fiabilité reste l'argument numéro un des utilisateurs satisfaits. »

Après : « Comme pour tout plugin sérieux, la fiabilité reste l'argument numéro un des utilisateurs satisfaits. » (lien hors-sujet retiré)

## I3 — URL Masteriyo (paramètre de tracking + rel manquant)

Avant : lien vers `/masteriyo-lms-avis/` avec un paramètre `?srsltid=...` et `target` blank sans `rel`.

Après : `/masteriyo-lms-avis/` propre, `target` blank + `rel` noreferrer noopener.

## I6 — Mot interdit « sans effort »

Avant : « ...réduisent drastiquement les oublis de tes clients sans effort de ta part. Le système travaille en arrière-plan... »

Après : « ...réduisent drastiquement les oublis de tes clients, et le système travaille en arrière-plan... »

## I4 — Meta Rank Math

- Focus keyword : avis booknetic
- Meta description : « Avis Booknetic 2026 : prix réels, fonctionnalités, avis clients et alternatives. Mon test honnête du plugin de réservation WordPress pour décider en 5 minutes. »

## B3 — CTA / lien affilié (EN ATTENTE)

L'article n'a AUCUN lien d'achat. Il faut un bouton CTA (template Kadence mémorisé) vers Booknetic. URL affiliée/cloak à fournir par Michaël ; à défaut lien officiel booknetic.com (à remplacer). Non appliqué tant que l'URL n'est pas confirmée.

## Statut

- 4 bloquants sur 5 + tous les « importants » prêts à appliquer en un passage.
- B3 (CTA affilié) en attente de l'URL.
- Exécution dès que schoolswp.com sort de maintenance.
