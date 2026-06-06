# Analyse produit : NovaMira vu dans la vidéo de Darrel Wilson (2026)

> **Source** : https://www.youtube.com/watch?v=El484PgSHEk - Darrel Wilson (509 k abonnés, 36 k vues au 05/06/2026)
> **Méthode reproductible associée** : [2026-06-05_methode-wordpress-claude-darrel-wilson.md](2026-06-05_methode-wordpress-claude-darrel-wilson.md)
> **Objet** : ce que la vidéo montre de NovaMira (positionnement, workflow MCP réel, frictions visibles à l'écran) et les pistes produit qui en découlent.
> **Périmètre** : analyse de ce qui est montré dans la vidéo. Les "bugs" listés sont des symptômes observés à l'écran, à corréler avec le code du repo `novamira/` avant correction.

---

## 1. Positionnement perçu (comment un YouTubeur à 509 k abonnés vend NovaMira)

NovaMira n'est jamais "présenté" via une fiche : Darrel l'introduit comme "le dernier plugin de la liste", en insistant uniquement sur sa fonction de **pont**. Verbatim :

- _"the last plugin that we're going to install is not available in the WordPress repository."_
- _"this plugin will essentially bridge the gap. So, it'll connect WordPress with Claude (...) and it imports the website."_
- _"it is a free website, free plugin, does not cost you anything whatsoever. You can upgrade, but what this does here is that this connects your website with Claude and it also teaches the AI about Elementor to make sure you have a really smooth transition."_
- _"Now, Nova Mira not only connects your website, but it also teaches Claude about the elements to help it utilize the elements on your websites."_

**3 promesses produit retenues par l'audience** :

1. Pont MCP WordPress <-> Claude.
2. Import du design (HTML -> Elementor natif).
3. "Enseigne" à Claude comment utiliser les éléments Elementor (la valeur différenciante).

**Point notoriété / marque** : le nom est **massacré phonétiquement** par les sous-titres et probablement à l'oral : "Novamira", "Novamirror", "Nova Mira", "Nova Mir". Jamais écrit "NovaMira" en un mot. Risque SEO/branding : les gens chercheront "nova mirror wordpress", "nova mira plugin". Piste : sécuriser ces variantes (redirections, page qui ranke sur les fautes courantes, prononciation explicite dans la doc).

---

## 2. Workflow MCP réel montré à l'écran

Séquence exacte (timestamps approx.) :

1. **Pré-requis** : Claude **Desktop** obligatoire, pas le navigateur (~01:26) : _"we need the desktop version in order to connect an MCP (...) the browser version will not work."_
2. **Install** (~18:36) : download zip (hors repo WP.org) -> Add plugin -> Upload plugin -> Install now -> Activate.
3. **Menu** : sous-menu **"Configuration"** dans l'admin (transcrit "Novamirror").
4. **Activer les abilities** (~21:37) : case **"turn on AI abilities for this sites"** -> "save settings" -> OK.
5. **Generate application password** (~21:46) : bouton dédié.
6. **Encart "Connect your client"** (~21:53) -> **contourné** (voir friction #1).
7. **"Need adjacent configuration"** (~22:03) : lien en bas -> choisir **"Claude desktop"** -> un bloc de **code** s'affiche -> **Copy**.
8. **Coté Claude** (~22:23) : profil -> Settings -> Developer -> **Edit config** -> ouvre `claude_desktop_config.json` -> tout supprimer -> coller -> **Save** (jamais "Save as").
9. **Restart** Claude (Quit + réouverture).
10. **Vérif** (~24:12) : Settings -> Developer -> _"the MCP is running. So it is now officially connected to our WordPress websites."_

**À noter pour le produit** : Darrel ne lit jamais le contenu du bloc de code (il ne mentionne ni l'endpoint `/wp-json/mcp/...`, ni un token, ni le format JSON). Pour l'utilisateur lambda c'est une boîte noire "copy/paste" - ce qui est rassurant, mais rend tout échec opaque (pas de quoi diagnostiquer si le MCP ne démarre pas).

---

## 3. Frictions observées -> pistes produit (priorisées)

| #      | Friction montrée à l'écran                                                                                                          | Verbatim                                                                                                                                                    | Impact                                                                                                                | Piste produit                                                                                                                                                                                                                                                  |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **F1** | **Le flux "Connect your client" ne marche pas avec Claude** : il faut le contourner manuellement par "Need adjacent configuration". | _"I've been using this plugin for a while, and this typically doesn't work well with Claude. So, we're just going to (...) do it directly through Claude."_ | **Élevé** - dit publiquement à 509 k personnes, juste avant l'étape de connexion. C'est LE point noir UX de la vidéo. | Réparer ou retirer le bouton "Connect your client", ou le renommer en "Auto-connect (beta)". Faire du flux manuel (config JSON) le chemin par défaut/recommandé. À corréler avec le code.                                                                      |
| **F2** | **Claude "oublie" que NovaMira aide** (~1 fois/10) : hésite, demande "which one should we pick?".                                   | _"sometimes Claude doesn't understand that Nova Mira can teach the AI (...) just (...) repeat the prompt, and (...) tell it to use the Nova Mira plugin."_  | **Moyen-élevé** - casse la promesse "teaches the AI".                                                                 | Renforcer les **descriptions des tools/abilities MCP** (champ description de chaque ability) pour qu'elles s'auto-sélectionnent : ex. "Use this to convert HTML designs into native Elementor elements." Ajouter un tool d'amorçage type "elementor_guidance". |
| **F3** | **Images servies depuis une URL externe, pas dans la médiathèque.**                                                                 | _"these images (...) are not stored in your library (...) being pulled from a URL. So you probably have to update your images."_                            | **Moyen** - travail manuel post-import, fragile (lien mort = image cassée).                                           | **Sideload automatique** des images vers la médiathèque WP lors de l'import (download_url + media_handle_sideload). Gros gain de qualité perçue.                                                                                                               |
| **F4** | **Widgets HTML résiduels** quand Claude ne sait pas mapper un design.                                                               | _"if Claude doesn't know how to (...) implement the elements, it's just going to create its own HTML widget (...) you'll just (...) delete these."_         | **Moyen** - dette visuelle, l'utilisateur doit remplacer à la main.                                                   | Élargir le "teaching" à plus de widgets (testimonials, profil, pricing, accordéon...). Documenter la liste des éléments Elementor que NovaMira sait mapper.                                                                                                    |
| **F5** | **Header/footer créés en "draft" / non publiés** via Xpro.                                                                          | _"sometimes it doesn't apply it. Sometimes (...) it may put it as draft. It really depends on the AI."_                                                     | **Moyen** - "very common problem" selon lui.                                                                          | Si NovaMira pilote la création header/footer : forcer `post_status=publish` + assignation "Entire website". Sinon, ajouter une ability "publish_template".                                                                                                     |
| **F6** | **Bug "post meta"** sur l'affichage header/footer (Claude doit débugger).                                                           | _"Now I see the real problem. It doesn't post because of post meta (...) they find the bug and fix things."_                                                | **Moyen** - rattrapé par l'auto-correction de Claude, mais ça allonge la session.                                     | Vérifier la gestion des post meta de templates Xpro côté abilities NovaMira (conditions d'affichage).                                                                                                                                                          |
| **F7** | **Wrap/flexbox mal géré** par Claude (récurrent).                                                                                   | _"Claude doesn't know how to properly wrap elements (...) it's literally one option in the flexbox setting (...) you're going to see this a lot."_          | **Faible-moyen** - pas spécifique NovaMira (limite Claude/Elementor), mais récurrent.                                 | Ajouter une consigne "wrap: no-wrap par défaut" dans le guidance injecté, ou un tool de normalisation flexbox post-import.                                                                                                                                     |
| **F8** | **Conversion lente (~12 min)** pour 5 pages.                                                                                        | _"waited about a solid 12 minutes (...) it now finished."_                                                                                                  | **Faible** - acceptable, mais perçu.                                                                                  | Mesurer/optimiser le nombre d'appels MCP par page ; envisager un mode batch.                                                                                                                                                                                   |
| **F9** | **Boîte noire en cas d'échec** : l'utilisateur copie un code qu'il ne comprend pas ; aucun diagnostic si le MCP ne démarre pas.     | (Darrel : _"Don't worry. Don't panic."_)                                                                                                                    | **Faible** - tant que ça marche.                                                                                      | Ajouter un bouton "Test connection" côté plugin + un health-check qui dit "MCP joignable / token valide / abilities ON".                                                                                                                                       |

**Note** : l'intitulé entendu _"turn on AI abilities for this sites"_ est une **mauvaise transcription** des sous-titres. Le vrai libellé du plugin est **"Enable AI Abilities"** (vérifié dans le code, voir §6.3).

---

## 4. Ce qui marche bien (à préserver / capitaliser)

- **Le pont MCP fonctionne** et la vérif "MCP running" est claire et rassurante.
- Claude reconnaît **"full access"** une fois connecté : _"Claude also acknowledged that Nova Mira is installed with full access (...) now they can understand our website better."_
- **Auto-correction** : quand un bug survient (post meta), Claude le diagnostique et le corrige seul -> _"That's the beauty of using Claude."_ NovaMira expose assez de surface pour que Claude itère.
- **Gratuit + upgrade** : modèle bien reçu (_"does not cost you anything whatsoever"_).
- **Positionnement final** : Darrel qualifie le combo Claude + NovaMira de méthode _"the most optimal and quickest"_ parmi _"several ways to integrate Claude"_, et annonce **d'autres tutos à venir**. Bon signal de relation influenceur à entretenir.

---

## 5. Recommandations actionnables (synthèse)

**Quick wins UX (forte visibilité)**

1. **F1** : régler le flux "Connect your client" (ou le déprioriser visuellement) - c'est le reproche public n°1.
2. **F9** : bouton "Test connection / health-check" dans Configuration.
3. Corriger l'intitulé "for this sites" si confirmé.

**Cœur de la promesse "teaches the AI"** 4. **F2** : durcir les descriptions des abilities MCP pour auto-sélection (réduire le bug 1/10). 5. **F4** : élargir la couverture de widgets mappés + doc publique de la liste.

**Qualité du rendu importé** 6. **F3** : sideload auto des images (gros gain perçu). 7. **F5/F6** : fiabiliser publication + conditions d'affichage des templates header/footer. 8. **F7** : injecter une consigne flexbox "no-wrap".

**Marque / acquisition** 9. Sécuriser les variantes de nom ("nova mirror", "nova mira") en SEO. 10. Entretenir la relation Darrel Wilson (il promet d'autres tutos) : lui fournir une version testée du flux corrigé, un code promo, ou une co-promo.

---

## 6. Corrélation avec le code réel (repo `novamira/`, v1.0.1 - vérifié le 05/06/2026)

J'ai lu le code source du plugin. Plusieurs affirmations de la vidéo sont **contredites par le code**. C'est le point le plus important de cette analyse.

### 6.1 Ce que NovaMira EST vraiment (vs ce que la vidéo laisse croire)

NovaMira est un **serveur MCP générique d'accès WordPress**, pas un constructeur de site Elementor. Il expose **8 abilities** via l'**Abilities API de WordPress 6.9** + le **MCP Adapter d'Automattic** (bundlé) - aucun protocole MCP custom ([readme.txt:30](../../../novamira/readme.txt), [admin-page.php:206-247](../../../novamira/includes/admin-page.php#L206-L247)) :

`execute-php`, `read-file`, `write-file`, `edit-file`, `delete-file`, `disable-file`, `enable-file`, `list-directory`. Toutes exigent `manage_options` (admin).

- **Transport** : HTTP via le proxy npx `@automattic/mcp-wordpress-remote` -> endpoint `wp-json/mcp/mcp-adapter-default-server`, auth par application password ([connect-page.php:240-247, 636-637](../../../novamira/includes/connect-page.php#L636-L637)). STDIO via WP-CLI en option.
- **Positionnement officiel** : _"For development and staging environments only. Do not use on production sites."_ ([readme.txt:11,15](../../../novamira/readme.txt)). Sécurité soignée : sandbox PHP (`wp-content/novamira-sandbox/`), safe mode + crash recovery, domain-locking, limite 30 s, répertoires critiques protégés, avertissements rouges répétés dans l'UI.
- Éditeur : **Ovation S.r.l. / dynamicooo / dev@novamira.ai** (licence AGPL-3.0).

### 6.2 Les 3 affirmations de Darrel que le code contredit

1. **"It teaches the AI about Elementor"** -> **FAUX dans le code.** Recherche exhaustive : **zéro occurrence d'`elementor`, `media_handle`, `sideload`, `wp_insert_post`** dans le code du plugin (les seuls matches sont dans `node_modules`). NovaMira ne "connaît" pas Elementor : il donne à Claude `execute-php` + filesystem, et **c'est Claude seul** qui fabrique l'Elementor (en écrivant le post meta `_elementor_data` via PHP). La promesse "teaches the AI" est du **marketing de Darrel**, pas une réalité produit. -> **C'est la cause racine de F2** : aucune description d'ability ne mentionne Elementor, donc Claude ne peut pas "deviner" que ces primitives servent à un import Elementor.

2. **Node.js "parce que Claude génère parfois du React"** -> **imprécis.** La vraie raison : le proxy MCP **tourne via `npx`** (donc Node requis pour la connexion elle-même). Le code le dit noir sur blanc : _"Requires Node.js (provides npm/npx)"_ ([connect-page.php:501-503](../../../novamira/includes/connect-page.php#L501-L503)).

3. **Outil "pour tout le monde / site live"** -> **en contradiction avec le readme** : dev/staging only, jamais la prod. Darrel pousse à des débutants un plugin qui donne `execute-php` + `delete-file` en accès admin sur un **site de production**. C'est l'**écart le plus risqué** : SAV potentiel, faille de sécurité si l'app password fuite, site cassable par une PHP générée. À arbitrer côté marque.

### 6.3 Statut réel de chaque friction (après lecture du code)

| Friction                               | Verdict code                                    | Détail                                                                                                                                                                                                                                                                                                     |
| -------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **F1** "Connect your client" cassé     | **À nuancer / probablement version antérieure** | La v1.0.1 n'a **pas** de bouton "auto-connect" : la page "Configuration" fournit directement le bloc de config dans 14 onglets clients (dont Claude Desktop) à copier/coller. Soit Darrel a filmé une build plus ancienne, soit il a mal nommé un onglet. **Pas de bug auto-connect dans le code actuel.** |
| **F2** Claude oublie Elementor         | **Confirmé, cause identifiée**                  | Aucune guidance Elementor exposée. Fix léger : enrichir les **MCP server instructions** (déjà injectées à l'init avec locale + plugins actifs, cf. CHANGELOG v1.0.0-rc4/v1.0.1) d'un bloc "si Elementor actif, écris dans `_elementor_data`, utilise les widgets natifs...".                               |
| **F3** images en URL                   | **Confirmé absent (par design)**                | Pas de logique média. Un sideload auto supposerait une ability orientée import - hors ADN "MCP dev tool". À trancher selon la stratégie produit (cf. 6.4).                                                                                                                                                 |
| **F4** widgets HTML résiduels          | **Confirmé absent**                             | Même logique que F2/F3 : dépend entièrement de Claude.                                                                                                                                                                                                                                                     |
| **F5/F6** templates draft / post meta  | **Confirmé absent**                             | NovaMira ne pilote ni Xpro ni les templates : c'est Claude via execute-php.                                                                                                                                                                                                                                |
| **F7** wrap/flexbox                    | **Hors périmètre plugin**                       | Limite Claude/Elementor pure.                                                                                                                                                                                                                                                                              |
| **F9** boîte noire / pas de diagnostic | **Confirmé, vraie opportunité**                 | Il existe une alerte "AI Abilities not enabled" ([connect-page.php:704-718](../../../novamira/includes/connect-page.php#L704-L718)) mais **aucun "Test connection"** qui pingue réellement l'endpoint MCP.                                                                                                 |
| Libellé "for this sites"               | **Corrigé : mauvaise transcription**            | Le vrai libellé est **"Enable AI Abilities"** ([admin-page.php:263](../../../novamira/includes/admin-page.php#L263)). Pas de faute de pluriel à corriger.                                                                                                                                                  |
| Nit doc                                | **Réel**                                        | `readme.txt` affiche `Stable tag: 0.1.0` alors que le CHANGELOG/zip sont en **1.0.1** -> stable tag pas synchronisé.                                                                                                                                                                                       |

### 6.4 La vraie question stratégique pour toi

Il y a un **mismatch de récit** :

- **Ce que le plugin EST** : un MCP générique dev/staging (execute-php + filesystem), public développeur, agnostique du page builder.
- **Ce que Darrel VEND** : un constructeur de site IA grand public, Elementor, en production.

Deux trajectoires possibles, à choisir consciemment :

- **A. Assumer le récit "build your AI website"** : alors il faut une **couche Elementor** (server instructions enrichies + éventuellement 1-2 abilities orientées page-building/média) et un **mode "guidé" plus sûr** pour le cas prod (au minimum un gros disclaimer + un mode lecture/écriture restreint). Cela règle F2/F3/F4 et aligne le produit sur sa promo la plus virale.
- **B. Rester un outil de dev pur** : alors le décalage avec la promo de Darrel doit être cadré (page "ce que NovaMira fait / ne fait pas", recommandation staging, pas de promesse Elementor) pour éviter les attentes déçues et le risque sécurité.

Quick wins indépendants de ce choix : **bouton "Test connection"** (F9), **server instructions enrichies** (F2, fix le plus rentable), **sync du `Stable tag`**, **SEO sur les variantes de nom** ("nova mirror", "nova mira").

> Note : analyse fondée sur la v1.0.1 présente dans `novamira/`. La build filmée par Darrel peut différer (F1). À confirmer en regardant la version montrée à l'écran dans la vidéo si besoin.
