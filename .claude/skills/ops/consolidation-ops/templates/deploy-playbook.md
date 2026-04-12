# Playbook de déploiement — schoolsWP vers WordPress

## Prérequis

- [ ] Accès SSH ou FTP au serveur WordPress
- [ ] Python 3.11+ installé sur le serveur (si agents)
- [ ] Backup de la base de données effectué
- [ ] Tag de version créé sur le dépôt

## Variables d'environnement

| Variable | Description | Obligatoire |
|----------|-------------|-------------|
| `WP_HOST` | URL du site WordPress | Oui |
| `WP_USER` | Utilisateur SSH/FTP | Oui |
| `WP_PATH` | Chemin du site sur le serveur | Oui |
| `DB_BACKUP_PATH` | Chemin des backups DB | Oui |

## Étapes de déploiement

### 1. Vérifications pré-déploiement

```bash
# Vérifier que tous les tests passent
pytest tests/ -v

# Vérifier que le workspace est propre
bash scripts/verify-consolidation.sh

# Vérifier le tag de version
git describe --tags --abbrev=0
```

### 2. Backup

```bash
# Backup de la base de données
wp db export $DB_BACKUP_PATH/backup-$(date +%Y%m%d-%H%M%S).sql

# Backup des fichiers
tar -czf $DB_BACKUP_PATH/files-$(date +%Y%m%d-%H%M%S).tar.gz $WP_PATH
```

### 3. Déploiement

```bash
# Synchroniser les fichiers
rsync -avz --delete \
  --exclude='.git' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  --exclude='.env' \
  ./ $WP_USER@$WP_HOST:$WP_PATH/

# Redémarrer les services si nécessaire
ssh $WP_USER@$WP_HOST "cd $WP_PATH && systemctl restart schoolswp-agents"
```

### 4. Vérifications post-déploiement

- [ ] Le site est accessible
- [ ] Les agents répondent (vérifier le dashboard santé)
- [ ] Les formulaires fonctionnent
- [ ] Les emails automatiques partent (tester avec FluentCRM)
- [ ] Pas d'erreurs dans les logs : `tail -100 /var/log/schoolswp/agents.log`

## Rollback

Si quelque chose ne va pas :

```bash
# Restaurer les fichiers
tar -xzf $DB_BACKUP_PATH/files-[TIMESTAMP].tar.gz -C /

# Restaurer la base de données
wp db import $DB_BACKUP_PATH/backup-[TIMESTAMP].sql

# Redémarrer
ssh $WP_USER@$WP_HOST "systemctl restart schoolswp-agents"
```

## Checklist finale

- [ ] Tests passés avant déploiement
- [ ] Backup effectué
- [ ] Déploiement réussi
- [ ] Vérifications post-déploiement OK
- [ ] CHANGELOG mis à jour
- [ ] Entrée dans lessons.md si incident
