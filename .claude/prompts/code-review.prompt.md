# Code Review

Revue de code pour le projet schoolsWP.

## Cible
Fichier(s) : $ARGUMENTS

## Checklist
- [ ] Sécurité : path traversal, injection, secrets exposés
- [ ] Conventions : PEP 8, kebab-case fichiers, line-length 120
- [ ] Architecture : héritage BaseContentAgent, signature async run()
- [ ] Tests : couverture des cas limites
- [ ] Performance : appels API inutiles, boucles non optimisées

## Format de sortie
Pour chaque issue trouvée :
- **Fichier:ligne** — Description du problème
- **Sévérité** : Critical / High / Medium / Low
- **Fix suggéré** : code ou explication

Résumé final : nombre d'issues par sévérité, score qualité /10.
