# Lecon 3.3 — Domaine personnalise : DNS, SSL, configuration

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 3 — De la demo au site en production
- **Lecon** : 3/7
- **Duree cible** : 8 min
- **Objectif pedagogique** : Configurer un nom de domaine personnalise sur un site ZipWP ou exporte, gerer les DNS et le certificat SSL.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

Ton site fonctionne. Mais il est encore accessible via une URL provisoire — quelque chose comme ton-projet.zipwp.site. Pour un site professionnel, ca ne passe pas. Tu as besoin de ton propre nom de domaine.

Dans cette lecon, on configure tout : le domaine, les DNS, et le certificat SSL. Que tu sois reste chez ZipWP ou que tu aies exporte vers un hebergeur tiers.

---

[SECTION 1 — Configurer un domaine chez ZipWP]

Si tu es heberge chez ZipWP, la procedure est directe.

Va dans le dashboard ZipWP. Selectionne ton site. Va dans Settings, puis Custom Domain. Saisis ton nom de domaine — par exemple mon-site.fr.

ZipWP te donne alors des enregistrements DNS a configurer chez ton registrar. Un registrar, c'est l'endroit ou tu as achete ton nom de domaine — Netim, OVH, Gandi, Namecheap.

Connecte-toi a l'interface de ton registrar. Va dans la zone DNS de ton domaine. Tu vas ajouter ou modifier deux types d'enregistrements.

L'enregistrement A : il pointe ton domaine vers l'adresse IP du serveur ZipWP. Copie l'IP fournie par ZipWP et colle-la dans le champ "Valeur" de l'enregistrement A. Le champ "Nom" reste vide ou contient "@" — ca designe la racine du domaine.

L'enregistrement CNAME pour www : il pointe www.mon-site.fr vers mon-site.fr. Le champ "Nom" contient "www", le champ "Valeur" contient ton domaine racine.

Enregistre. C'est tout cote DNS.

---

[SECTION 2 — Configurer un domaine apres export]

Si tu as exporte ton site vers un hebergeur comme o2switch ou Infomaniak, la methode est differente.

Option 1 — pointer les nameservers : tu remplaces les nameservers de ton registrar par ceux de ton hebergeur. Chez o2switch, les nameservers sont ns1.o2switch.net et ns2.o2switch.net. Chez Infomaniak, idem — tu trouves les nameservers dans la console d'administration. Cette methode donne le controle DNS complet a ton hebergeur. C'est la methode la plus propre.

Option 2 — pointer un enregistrement A : tu gardes les nameservers de ton registrar et tu pointes uniquement l'enregistrement A vers l'IP de ton serveur. Cette methode est utile si tu geres d'autres services sur le meme domaine — emails, sous-domaines pour d'autres projets.

Dans les deux cas, cote hebergeur, tu dois ajouter le domaine dans ton panel d'administration. Chez o2switch, c'est dans cPanel → Domaines complementaires ou Domaines alias. Chez Infomaniak, c'est dans la gestion des sites.

---

[SECTION 3 — Le certificat SSL]

Le SSL, c'est ce qui fait apparaitre le cadenas et le "https" dans la barre d'adresse. Sans SSL, les navigateurs affichent "Non securise" — et tes visiteurs partent.

Chez ZipWP : le SSL est automatique. Des que ton domaine est configure et que les DNS ont propage, ZipWP active le certificat. Tu n'as rien a faire.

Chez un hebergeur FR : la plupart proposent Let's Encrypt gratuitement. Chez o2switch, va dans cPanel → SSL/TLS Status et active le certificat pour ton domaine. Chez Infomaniak, c'est automatique a l'ajout du domaine. Chez OVH, active Let's Encrypt dans l'espace client.

Une fois le SSL actif, force le HTTPS dans WordPress. Va dans Reglages → General. Change l'adresse WordPress et l'adresse du site en remplacant http par https. Enregistre.

Derniere etape : installe un plugin comme Really Simple SSL ou configure une redirection dans le .htaccess pour que toutes les requetes HTTP soient automatiquement redirigees vers HTTPS.

---

[SECTION 4 — Propagation DNS : patience]

Tu as configure tes DNS. Tu as clique sur "Enregistrer". Et... ton domaine ne fonctionne pas encore.

C'est normal. La propagation DNS prend entre 15 minutes et 24 heures. En pratique, c'est souvent 1 a 2 heures. Mais ca peut prendre plus longtemps selon le registrar et le TTL configure.

Comment verifier : utilise un outil comme whatsmydns.com. Saisis ton domaine et verifie que les enregistrements A pointent bien vers la bonne IP dans toutes les regions.

En attendant la propagation, ne touche a rien. Ne change pas les DNS en te disant que ca n'a pas marche. Attends. Verifie. Et si apres 24 heures ca ne fonctionne toujours pas, contacte ton registrar.

Astuce : vide le cache DNS de ton ordinateur. Sur Windows, ouvre un terminal et tape ipconfig /flushdns. Ca peut debloquer la resolution locale.

---

[OUTRO]

Ton domaine est configure, ton SSL est actif, tes visiteurs voient un site professionnel avec un cadenas vert. Plus d'URL provisoire.

Prochaine lecon : le SEO. Parce que ZipWP genere un site fonctionnel, mais le referencement reste basique. On va installer Rank Math et configurer tout ce qu'il faut pour que Google te trouve.

---

## Notes de production

### Captures d'ecran suggerees

1. **ZipWP Custom Domain** — Interface de configuration du domaine dans le dashboard
2. **Zone DNS registrar** — Exemple chez Netim ou OVH avec les champs A et CNAME
3. **Nameservers** — Ecran de configuration des nameservers chez un registrar
4. **SSL/TLS cPanel** — Activation Let's Encrypt chez o2switch
5. **WordPress Reglages** — Champs adresse WordPress avec https
6. **whatsmydns.com** — Verification de la propagation DNS

### Transitions

- Intro → Section 1 : zoom sur le dashboard ZipWP, section Custom Domain
- Section 1 → Section 2 : transition vers interface registrar
- Section 2 → Section 3 : apparition du cadenas SSL
- Section 3 → Section 4 : carte du monde avec propagation DNS
- Section 4 → Outro : retour avatar

### Notes HeyGen / ElevenLabs

- Ton technique mais accessible — les DNS effraient beaucoup de debutants
- Articuler clairement : "A record", "CNAME", "nameservers", "SSL"
- Section 4 : ton rassurant — "c'est normal, attends"
- Eviter le jargon inutile, expliquer chaque terme a la premiere utilisation
