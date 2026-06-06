# knowledge/

Dossier de data propriétaire pour le pipeline `thruuu-writer`.

Dépose ici les informations à injecter dans la rédaction d'un article :

- retours d'expérience réels (tests, captures, mesures)
- citations vérifiées et leur source
- chiffres et données confirmés
- notes internes, extraits de documentation, ressources

## Fonctionnement

À l'étape 6 du pipeline `thruuu-writer` (« Construire la base de connaissances »), tous
les fichiers `.md` et `.txt` de ce dossier sont lus automatiquement. Cette base prime
comme source de vérité sur les sources web fetchées.

Dossier vide = aucune erreur, le pipeline continue normalement.

## Format

Un fichier par sujet ou par source. Markdown ou texte brut. Nomme les fichiers de façon
explicite, par exemple `fluentcrm-tests-2026.md` ou `citation-tutor-lms.txt`.

## À ne pas faire

Ne stocke ici aucun secret, aucune clé API, aucune donnée sensible : ce dossier est lu
et son contenu peut se retrouver dans un draft d'article.
