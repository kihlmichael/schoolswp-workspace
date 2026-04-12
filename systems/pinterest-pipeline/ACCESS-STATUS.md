# Access Status — Pinterest Pipeline schoolsWP

> Derniere verification : 2026-04-03

## Canva MCP

| Test | Resultat | Details |
| --- | --- | --- |
| Connexion MCP | OK | Canva MCP operationnel |
| search-designs | OK | Designs Pinterest trouves (pins master 348 pages, boards covers 18 pages) |
| get-design | OK | Metadata complete (owner, title, URLs, thumbnail, page_count) |
| get-export-formats | OK | PNG, JPG, PDF, PPTX, MP4 disponibles |
| generate-design | DISPONIBLE | `pinterest_pin` supporte comme design_type natif |
| generate-design-structured | NON ADAPTE | Reserve aux presentations (outline review flow) |
| export-design | A TESTER | Disponible, URL expire 24h, qualite depend du plan |

### Designs Canva existants

| Design | ID | Pages | Usage |
| --- | --- | --- | --- |
| Epingles Pinterest 1000x1500 | `DAFU6F7oeGo` | 348 | Design principal — pins articles |
| Tableaux Pinterest 1000x1000 | `DAFcKw0FSZ0` | 18 | Couvertures de boards |
| Pinterest Pin 1000x1500 | `DAD3565Mpro` | 2 | Ancien template |
| Template 10 epingles | `DAEdt83WHWw` | 11 | Templates referencs |
| Epingles classiques ORIGINAL | `DAFSkDM-VmM` | 71 | Templates originaux |

### Workflow Canva recommande (Chemin B — sans Enterprise)

1. `generate-design` avec `design_type: "pinterest_pin"` + prompt detaille (specs brand)
2. Ou : utiliser le design master (`DAFU6F7oeGo`) comme base et ajouter des pages
3. `export-design` en PNG pour recuperer l'image
4. Telecharger avant expiration 24h

## Pinterest API

| Test | Resultat | Details |
| --- | --- | --- |
| App Pinterest | A CREER | Pas encore d'app dans le Developer Portal |
| OAuth 2.0 | A CONFIGURER | Authorization code flow a mettre en place |
| Access token | MANQUANT | `PINTEREST_ACCESS_TOKEN` absent du `.env` |
| Sandbox | A ACTIVER | Disponible apres creation de l'app |

### Prochaines etapes Pinterest

1. Creer une app sur https://developers.pinterest.com/
2. Configurer OAuth 2.0 (redirect URI)
3. Generer access token + refresh token
4. Stocker dans `.env` (jamais versionne)
5. Tester en sandbox : `POST /pins` avec un pin de test
6. Creer les 10 boards et recuperer les `board_id`

## Resume

| Composant | Statut | Action requise |
| --- | --- | --- |
| Canva MCP | OPERATIONNEL | Aucune — pret a utiliser |
| Canva generate-design | PRET | Utiliser `pinterest_pin` comme design_type |
| Canva export | PRET | Tester un export reel |
| Pinterest API | A CONFIGURER | Creer app + OAuth + tokens |
| Claude Code orchestration | PRET | SOP + skill + scripts en place |

**Verdict : Canva est pret. Pinterest API necessite la creation de l'app et la config OAuth.**
