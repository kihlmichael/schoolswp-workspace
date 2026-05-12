# tools/skoatch/payloads

Payloads JSON pour les sous-commandes Skoatch.

## Convention nommage

    test-NNN-<site-short>-<keyword-slug>.json

- test-NNN : numero monotone (lisibilite des runs)
- site-short : michaelkihl ou autre
- keyword-slug : kebab-case du mot-cle

## Regles d'or

- **site_id obligatoire**. 503 pour michaelkihl.fr. **Jamais 742 (schoolswp.com)**.
- is_auto_generated: true lance la generation. Sans ce flag (ou avec false), l'article est cree mais reste en attente.
- is_auto_published: false empeche le push WP automatique apres generation. Toujours false pour les tests.
- is_publish_to_draft: true configure le push (via /publish manuel) en mode brouillon. Filet de securite si la publication finit par etre declenchee.
- additional_instructions est la SEULE voie de controle du ton tant que les content_prompts Skoatch sont vides.

## Variantes locales

Tout fichier nomme *.local.json est gitignore - utile pour itererer sans commiter chaque version intermediaire.

## Cycle d'un test (5 etapes)

1. Verifier le solde de credits :

       .venv/Scripts/python -m tools.skoatch.cli credits

2. Lancer avec polling jusqu'au terminal :

       .venv/Scripts/python -m tools.skoatch.cli create --payload tools/skoatch/payloads/test-NNN-...json --wait > tools/skoatch/runs/test-NNN-result.json

3. Inspecter dans le resultat : data.content (HTML), data.title, data.pictures (featured image), data.site, data.job_status_id (doit etre 20).

4. Si OK et qu'on veut le push WP draft :

       .venv/Scripts/python -m tools.skoatch.cli publish --id <id>

5. Sinon, nettoyer cote Skoatch :

       .venv/Scripts/python -m tools.skoatch.cli delete --id <id>
