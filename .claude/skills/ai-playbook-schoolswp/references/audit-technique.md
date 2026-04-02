# Checklist Audit Technique WordPress — schoolsWP

Utiliser cette checklist pour tout audit de site WordPress. Cocher chaque point vérifié.

---

## 1. Performance

- [ ] Temps de chargement < 3 secondes (GTmetrix ou PageSpeed Insights)
- [ ] Score Core Web Vitals vert (LCP, FID/INP, CLS)
- [ ] Cache navigateur configuré
- [ ] Cache serveur actif (plugin cache ou hébergeur)
- [ ] CDN configuré si trafic international
- [ ] Images compressées et en format moderne (WebP)
- [ ] Lazy loading actif sur les images
- [ ] CSS/JS minifiés
- [ ] Pas de plugins lourds inutilisés
- [ ] Base de données optimisée (révisions, transients nettoyés)

## 2. Sécurité

- [ ] WordPress à jour (dernière version stable)
- [ ] Thème à jour
- [ ] Tous les plugins à jour
- [ ] Certificat SSL actif et valide
- [ ] Connexion admin sécurisée (mot de passe fort, 2FA si possible)
- [ ] Préfixe de table modifié (pas wp_ par défaut)
- [ ] Édition de fichiers désactivée dans wp-config.php
- [ ] Sauvegardes automatiques configurées (quotidiennes minimum)
- [ ] Plugin de sécurité actif (Wordfence, Sucuri, ou équivalent)
- [ ] Permissions fichiers correctes (644 pour fichiers, 755 pour dossiers)

## 3. SEO technique

- [ ] Sitemap XML généré et soumis à Google Search Console
- [ ] robots.txt correctement configuré
- [ ] Pas de pages importantes bloquées par noindex
- [ ] Redirections 301 en place pour les anciennes URLs
- [ ] Pas d'erreurs 404 non traitées
- [ ] Canonical tags corrects
- [ ] Données structurées (Schema.org) si pertinent
- [ ] Vitesse mobile satisfaisante

## 4. Plugins

- [ ] Chaque plugin actif a une raison d'être documentée
- [ ] Pas de plugins désactivés traînant dans l'installation
- [ ] Pas de conflits connus entre plugins
- [ ] Alternatives plus légères évaluées pour les plugins lourds
- [ ] Plugins premium avec licences valides

## 5. Contenu et structure

- [ ] Page d'accueil configurée (pas la page par défaut WordPress)
- [ ] Permaliens en "nom de l'article"
- [ ] Pages légales présentes (mentions légales, politique de confidentialité, CGV si e-commerce)
- [ ] Page 404 personnalisée
- [ ] Menu de navigation clair et fonctionnel
- [ ] Formulaire de contact fonctionnel

## 6. Hébergement

- [ ] Version PHP récente (8.1+ recommandé)
- [ ] Limites mémoire suffisantes (256 MB minimum)
- [ ] Certificat SSL auto-renouvelé
- [ ] Sauvegardes côté hébergeur en plus des sauvegardes plugin
- [ ] Support réactif en cas de problème
