# Lecon 3.5 — Securite : mises a jour, backups, protection login

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 3 — De la demo au site en production
- **Lecon** : 5/7
- **Duree cible** : 8 min
- **Objectif pedagogique** : Securiser un site WordPress post-ZipWP avec les mises a jour, les backups automatiques et la protection de l'acces admin.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

Un site WordPress non securise, c'est une question de temps avant le probleme. Un plugin obsolete, un mot de passe faible, pas de backup — et un matin tu ouvres ton site et tu vois une page en chinois ou un message de rancongiciel.

Ca arrive. Pas qu'aux gros sites. Ca arrive surtout aux petits sites laisses sans maintenance. Alors on va verrouiller tout ca en quelques etapes.

---

[SECTION 1 — Les mises a jour : la base absolue]

WordPress, ton theme et tes plugins recoivent regulierement des mises a jour. Certaines ajoutent des fonctionnalites, mais la plupart corrigent des failles de securite. Un plugin pas a jour, c'est une porte ouverte.

Regle : mets a jour WordPress core, ton theme Astra, et tous tes plugins au moins une fois par semaine. Va dans le tableau de bord → Mises a jour. Tu vois la liste de tout ce qui doit etre mis a jour. Un clic.

Avant chaque mise a jour, fais un backup. Pas apres — avant. Si une mise a jour casse quelque chose, tu peux restaurer en deux minutes.

Option automatique : WordPress permet d'activer les mises a jour automatiques pour les plugins et les themes. Va dans Extensions → Extensions installees, et active "Mises a jour automatiques" pour chaque plugin. C'est pratique si tu ne veux pas y penser. Mais surveille quand meme — une mise a jour auto qui casse un truc, ca arrive.

---

[SECTION 2 — Les backups : ton assurance vie]

Si tu es heberge chez ZipWP, les backups sont automatiques. Tu n'as rien a configurer. ZipWP gere les sauvegardes et la restauration directement depuis le dashboard.

Si tu es heberge ailleurs, installe UpdraftPlus. C'est le plugin de backup le plus fiable pour WordPress. Version gratuite suffisante.

Configure UpdraftPlus : va dans Reglages → UpdraftPlus Backups. Configure une sauvegarde automatique hebdomadaire. Choisis un stockage externe — Google Drive, Dropbox, ou un serveur FTP. Ne stocke jamais tes backups uniquement sur le meme serveur que ton site. Si le serveur tombe, tes backups tombent avec.

Retiens : base de donnees + fichiers. UpdraftPlus sauvegarde les deux separement. Tu as besoin des deux pour restaurer completement.

Teste la restauration au moins une fois. Fais un backup, casse quelque chose volontairement sur un site de test, et restaure. Mieux vaut decouvrir un probleme de restauration sur un test que sur ton site en production un samedi soir.

---

[SECTION 3 — Protection du login]

La page de connexion WordPress est a wp-admin ou wp-login.php. Tout le monde le sait — y compris les bots qui tentent des milliers de combinaisons login/mot de passe par jour.

Premiere protection : un mot de passe fort. Pas "MonSite2024". Un vrai mot de passe — 16 caracteres minimum, lettres, chiffres, caracteres speciaux. Utilise un gestionnaire de mots de passe — Bitwarden, 1Password, ou le gestionnaire integre de ton navigateur.

Deuxieme protection : limite les tentatives de connexion. Installe Limit Login Attempts Reloaded. Ce plugin bloque une adresse IP apres un certain nombre de tentatives echouees. Configure : 3 tentatives avant blocage, 20 minutes de verrouillage, blocage 24h apres 3 verrouillages.

Troisieme protection : change l'URL de connexion. Installe WPS Hide Login. Ce plugin remplace wp-login.php par une URL personnalisee de ton choix — par exemple mon-site.fr/acces-admin. Les bots qui ciblent wp-login.php ne trouveront plus rien.

Optionnel mais recommande : active l'authentification a deux facteurs. Rank Math ou un plugin dedie comme WP 2FA. A chaque connexion, tu saisis ton mot de passe plus un code genere par ton telephone. C'est la protection la plus efficace contre les acces non autorises.

---

[SECTION 4 — Mesures complementaires]

Quelques actions supplementaires qui prennent cinq minutes :

Supprime le compte "admin". Si ton identifiant de connexion est "admin", cree un nouveau compte administrateur avec un nom different, connecte-toi avec ce nouveau compte, et supprime le compte "admin". C'est le premier identifiant que les bots essaient.

Desactive l'edition de fichiers dans WordPress. Ajoute cette ligne dans ton fichier wp-config.php : define('DISALLOW_FILE_EDIT', true). Ca empeche quiconque de modifier les fichiers PHP depuis l'admin WordPress — meme un admin compromis.

Verifie les utilisateurs. Va dans Utilisateurs et verifie qu'il n'y a pas de comptes inconnus. Si tu vois un utilisateur que tu n'as pas cree, supprime-le immediatement et change tous tes mots de passe.

---

[OUTRO]

Ton site est maintenant securise. Mises a jour regulieres, backups automatiques vers un stockage externe, login protege avec des tentatives limitees et une URL cachee.

Ce n'est pas du paranoia. C'est de la bonne hygiene. 15 minutes de configuration aujourd'hui, et tu n'as plus a t'en soucier.

Prochaine lecon : l'AI Troubleshooter de ZipWP. Un outil de diagnostic integre qui detecte et corrige les problemes WordPress automatiquement.

---

## Notes de production

### Captures d'ecran suggerees

1. **Mises a jour WordPress** — Tableau de bord avec la liste des mises a jour disponibles
2. **UpdraftPlus** — Ecran de configuration avec planification et stockage externe
3. **Limit Login Attempts** — Ecran de configuration (nombre de tentatives, duree de blocage)
4. **WPS Hide Login** — Configuration de l'URL personnalisee
5. **wp-config.php** — Ligne DISALLOW_FILE_EDIT mise en surbrillance
6. **Utilisateurs** — Liste des utilisateurs dans l'admin WordPress

### Transitions

- Intro → Section 1 : animation cadenas qui se ferme
- Section 1 → Section 2 : transition vers logo UpdraftPlus
- Section 2 → Section 3 : animation ecran de login avec tentatives bloquees
- Section 3 → Section 4 : checklist visuelle des mesures
- Section 4 → Outro : retour avatar, ton rassurant

### Notes HeyGen / ElevenLabs

- Ton serieux mais pas alarmiste — informer, pas effrayer
- Phrase cle : "Un site non securise, c'est une question de temps avant le probleme"
- Section 3 : rythme structure, chaque protection numerotee
- Articuler les noms de plugins : "UpdraftPlus", "Limit Login Attempts Reloaded", "WPS Hide Login"
