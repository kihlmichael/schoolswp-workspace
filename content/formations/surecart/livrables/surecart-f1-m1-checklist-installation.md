---
title: SureCart - Checklist d'installation (Module 1)
version: 1.0
last_updated: 2026-06-05
---

# Checklist d'installation SureCart

Garde cette fiche à côté de toi pendant le Module 1. Coche chaque ligne quand elle est faite : à la fin, ta base technique est propre et prête à encaisser. Chaque point renvoie à la leçon qui le couvre.

## Les 10 points à valider

- [ ] **1. Plugin installé et activé** : Extensions, Ajouter, rechercher SureCart, Installer, Activer. Le menu SureCart apparaît dans la barre latérale. _(Leçon 1.1)_
- [ ] **2. Boutique rattachée à ton compte** : tu as cliqué sur Complete Setup dans le bandeau vert, créé ou connecté ton compte SureCart, et validé ton email. Une boutique non rattachée peut être supprimée. _(Leçon 1.1)_
- [ ] **3. Jeton API connecté** : statut Connected dans SureCart, Settings, Connection. Jeton collé via l'interface, ou défini dans wp-config.php si tu utilises un plugin de sécurité costaud. _(Leçon 1.2)_
- [ ] **4. Stripe connecté** : pastille verte dans Settings, Payment Processors, onglet Stripe, en Live Mode. _(Leçon 1.3)_
- [ ] **5. Apple Pay validé (ou écarté en connaissance de cause)** : activé côté Stripe, domaine exact ajouté et vérifié via le dossier .well-known. Badge Enabled affiché. _(Leçon 1.3)_
- [ ] **6. PayPal connecté ou écarté volontairement** : si tu le proposes, onglet PayPal, Connect, Live Mode, compte connecté. Sinon, c'est un choix assumé, pas un oubli. _(Leçon 1.4)_
- [ ] **7. Devise vérifiée** : la devise choisie dans l'assistant est la bonne. Tu la fixes maintenant, pendant que c'est encore sans risque. _(Leçon 1.5)_
- [ ] **8. Branding clair et sombre posé** : couleur et logo réglés pour Light Mode ET Dark Mode dans Settings, Design & Branding. _(Leçon 1.5)_
- [ ] **9. Interface et emails en français** : interface traduite via Loco Translate (emplacement Custom), langue des emails et factures réglée dans Store Settings, Store Language. _(Leçon 1.6)_
- [ ] **10. Cache configuré et paiement test réussi** : pages dynamiques et API REST exclues du cache, combinaison JS désactivée. Un paiement test passe de bout en bout (modal Thank you, reçu, commande dans l'espace client). _(Leçons 1.7 et 1.8)_

## Mémo technique

### Le jeton API dans wp-config.php (méthode robuste)

À ajouter juste au-dessus de la ligne `/* That's all, stop editing! Happy publishing. */`. Sauvegarde une copie du fichier avant de l'éditer : une faute de frappe ici peut empêcher ton site de se charger.

```
define( 'SURECART_API_TOKEN', 'st_ta_cle_secrete_ici' );
```

Cette méthode survit aux migrations et aux régénérations de salts. Utile si un plugin de sécurité déconnecte ta boutique toute seule. Si tu n'es pas à l'aise avec l'édition de fichiers, reste sur la méthode par l'interface : elle fonctionne très bien.

### Apple Pay : 3 conditions pour tester

- Uniquement dans le navigateur Safari.
- Une vraie carte enregistrée dans le portefeuille Apple Pay de l'appareil.
- Un pays où Apple Pay est disponible.

En mode test Stripe, ta vraie carte est transformée en carte de test : tu peux essayer sans débit réel.

### Les 5 règles de cache qui évitent les bugs

1. Exclure du cache les pages connexion, inscription, paiement et espace client.
2. Exclure les requêtes de l'API REST.
3. Ne pas différer le chargement des scripts de base de WordPress.
4. Désactiver la combinaison des scripts JavaScript (elle peut casser le checkout).
5. Limiter le cache navigateur sur les données de boutique.

> Règle d'or : après chaque réglage de cache, teste ton tunnel de paiement en navigation privée. Si quelque chose casse, c'est presque toujours le cache. Tu reviens sur tes exclusions.

## Si ton paiement test bloque

Reprends ces trois points dans l'ordre. Dans neuf cas sur dix, le problème est là.

1. **Connexion à la plateforme** : statut Connected dans Settings, Connection.
2. **Processeur connecté** : pastille verte sur Stripe (ou ton processeur).
3. **Cache** : les exclusions ci-dessus sont bien appliquées.

## Avant de passer en live

- [ ] Données de test effacées via Settings, Advanced, Clear Test Data (taper CONFIRM, action irréversible : ne vérifie que tu n'effaces que des données de test).
- [ ] Mode test désactivé sur tes produits, sinon tu ne peux pas encaisser pour de vrai.
