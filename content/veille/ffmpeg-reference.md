# FFmpeg — Document de référence & suivi d'intégration schoolsWP

> **Statut** : Veille active  
> **Créé** : 2026-05-26  
> **Dernière mise à jour** : 2026-05-26  
> **Objectif** : Surveiller l'évolution du projet FFmpeg et préparer son intégration dans le flux de travail schoolsWP

---

## 1. Nature du projet

FFmpeg est une infrastructure multimédia open-source bas niveau. Ce n'est pas une application web — c'est un socle C utilisable en CLI ou comme bibliothèque embarquée dans d'autres logiciels.

### Bibliothèques principales

| Composant | Rôle |
|---|---|
| `libavcodec` | Encodage / décodage audio-vidéo |
| `libavformat` | Formats conteneurs, muxing/demuxing |
| `libavfilter` | Graphes de filtres audio/vidéo |
| `libavutil` | Primitives utilitaires communes |
| `libavdevice` | Périphériques d'entrée/sortie |
| `libswresample` | Rééchantillonnage audio |
| `libswscale` | Conversion / redimensionnement d'images |

### Outils CLI exposés

- `ffmpeg` — transcodage, conversion, traitement
- `ffplay` — lecture média
- `ffprobe` — analyse et inspection de fichiers

---

## 2. État du dépôt GitHub (snapshot 2026-05-21)

- **Repo** : https://github.com/FFmpeg/FFmpeg
- **Statut** : miroir — la source officielle est sur Forgejo + mailing list `ffmpeg-devel`
- **Stars** : ~60 352 | **Forks** : ~13 834
- **Langage** : C (principal) + assembleur SIMD/DSP
- **Branche par défaut** : `master`
- **Issues / PR GitHub** : désactivés — contribution via patches uniquement
- **Dernier push** : 21 mai 2026

> ⚠️ GitHub est utile pour lire et cloner, pas pour contribuer ni suivre les discussions.

---

## 3. Architecture technique

```
Frontends CLI
    └── ffmpeg / ffplay / ffprobe

Bibliothèques cœur
    ├── libavcodec   (codecs)
    ├── libavformat  (formats)
    ├── libavfilter  (filtres)
    ├── libavutil    (utilitaires)
    ├── libavdevice  (devices)
    ├── libswresample (audio resampling)
    └── libswscale   (image scaling)

Documentation & exemples
    └── doc/ / doc/examples/

Tests & validation
    └── FATE (suite de régression)
```

Modèle d'usage : outil CLI **ou** bibliothèque embarquée. Les deux sont pertinents pour schoolsWP selon le contexte.

---

## 4. Build & dépendances

```bash
./configure
make
make install
```

- `./configure --help` expose toutes les options
- Les dépendances externes sont **désactivées par défaut** (licences, redistribution)
- Écrit en **ISO C11**, headers publics compatibles C99
- Interdit : VLA, nombres complexes
- Performance : assembleur SIMD/DSP avec sélection runtime + tests `checkasm`

---

## 5. Règles qualité & contraintes

- Pas de crash, pas de fuite mémoire, pas de data race
- Pas de comportement indéfini
- Thread-safe / library-safe
- Flux entrants traités comme **non fiables** (sécurité critique)
- Allocation mémoire : `av_malloc` (jamais `malloc` direct)
- Journalisation : `av_log` (jamais `printf`/`stdio`)

---

## 6. Tests — FATE

FATE est la suite de régression officielle, avec agrégation serveur. Elle couvre :
- Plusieurs architectures CPU
- Plusieurs OS et configurations
- Formats, codecs, options de compilation
- Régressions comportementales

---

## 7. Licences

| Mode | Licence |
|---|---|
| Par défaut | LGPL v2.1+ |
| Avec `--enable-gpl` | GPL v2+ |
| Avec `--enable-nonfree` | Non redistribuable |

> ⚠️ **Point critique pour schoolsWP** : toute intégration dans un produit, SaaS, extension ou distribution serveur nécessite un audit de licence avant mise en production.

---

## 8. Contribution (workflow non-GitHub)

- Patches via **Forgejo** ou mailing list **ffmpeg-devel**
- Outils : `git format-patch` / `git send-email`
- Les PR GitHub sont ignorées
- Maintenance distribuée par zones (voir fichier `MAINTAINERS`)

---

## 9. Forces & points de vigilance

### ✅ Forces

- Profondeur fonctionnelle exceptionnelle (codecs, formats, filtres)
- Performance : optimisations SIMD/DSP par architecture
- Portabilité : Linux, macOS, Windows, ARM, etc.
- Stabilité historique et large adoption industrielle
- Utilisable CLI ou bibliothèque embarquée

### ⚠️ Points de vigilance

- Barrière d'entrée élevée (C, compilation native, sécurité mémoire)
- Traite des fichiers potentiellement hostiles → robustesse critique
- Workflow contribution mailing list déroutant pour les habitués GitHub
- Audit de licence obligatoire avant distribution

---

## 10. Pattern d'intégration schoolsWP

> Ne pas embarquer FFmpeg directement dans PHP. Le bon pattern est découplé :

```
WordPress (upload / déclencheur)
    ↓
File d'attente (n8n / BullMQ / Redis)
    ↓
Worker serveur (Node.js / Python)
    ↓
FFmpeg CLI (transcodage, compression, extraction)
    ↓
Stockage média (S3 / local / CDN)
    ↓
Retour WordPress (mise à jour post, métadonnées, miniature)
```

### Cas d'usage potentiels pour schoolsWP

| Besoin | Commande FFmpeg |
|---|---|
| Compression vidéo article | `ffmpeg -i input.mp4 -crf 23 -preset fast output.mp4` |
| Extraction miniature | `ffmpeg -i video.mp4 -ss 00:00:05 -vframes 1 thumbnail.jpg` |
| Conversion audio | `ffmpeg -i input.wav -codec:a libmp3lame output.mp3` |
| Normalisation audio | `ffmpeg -i input.mp3 -filter:a loudnorm output.mp3` |
| Génération sous-titres | Via `ffprobe` + analyse flux |
| Redimensionnement vidéo | `ffmpeg -i input.mp4 -vf scale=1280:720 output.mp4` |

### Règles de sécurité pour le worker

- Exécutions **sandboxées** (Docker recommandé)
- Validation stricte des fichiers entrants (MIME, extension, taille)
- Limites CPU / RAM / temps d'exécution
- Whitelist des commandes FFmpeg autorisées
- Logs systématiques
- Séparation uploads utilisateurs / traitement système

---

## 11. Suivi des évolutions

> Mettre à jour cette section à chaque veille significative.

| Date | Version / Événement | Impact potentiel schoolsWP | Source |
|---|---|---|---|
| 2026-05-21 | Dernier push connu (miroir GitHub) | — | GitHub mirror |
| — | — | — | — |

### Sources de veille recommandées

- **Changelog officiel** : https://git.ffmpeg.org/ffmpeg.git (Forgejo)
- **Mailing list résumés** : https://ffmpeg.org/pipermail/ffmpeg-devel/
- **Release notes** : https://ffmpeg.org/download.html
- **Security advisories** : https://ffmpeg.org/security.html

---

## 12. Prochaines étapes

- [ ] Choisir un worker pour le pattern d'intégration : **n8n** (déjà en place) ou worker dédié Python/Node
- [ ] Tester FFmpeg CLI en local sur Windows (disponible dans `_archive/ffmpeg/` du workspace)
- [ ] Définir les 3 premiers cas d'usage prioritaires (compression, miniature, audio)
- [ ] Auditer la licence selon le mode de déploiement envisagé (LGPL ou GPL)
- [ ] Évaluer la pertinence d'un conteneur Docker dédié sur le serveur schoolsWP

---

*Document maintenu dans `content/veille/ffmpeg-reference.md` — à mettre à jour lors de chaque session de veille.*
