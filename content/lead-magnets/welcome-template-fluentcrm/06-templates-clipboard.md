# Clipboard : 9 templates FluentCRM prêts à coller

Fichier optimisé pour la création UI des 9 modèles d'e-mail. Pour chaque bloc :

1. FluentCRM → E-mails → Modèles d'e-mail → `Créer un nouveau modèle`
2. Coller le **titre template**, le **sujet**, puis passer l'éditeur en mode HTML et coller le **corps**
3. Enregistrer → Suivant

Smartcode prénom utilisé : `{{contact.first_name}}` (natif FluentCRM, le fallback se gère via `{{contact.first_name||"toi"}}` si tu préfères).

Lien PDF : remplacer `#REMPLACER_PAR_LIEN_PDF#` dans l'email 1 par l'URL réelle après upload média WP.

---

## Template 1 · Welcome E1 · Livraison

**Titre template**

```
LM Welcome Template FluentCRM · E1 · Livraison
```

**Sujet**

```
Ton template est juste ici
```

**Pré-header**

```
Clique pour télécharger la séquence welcome FluentCRM
```

**Corps (HTML)**

```html
<p>Salut {{contact.first_name}},</p>

<p>Voilà ton template : <a href="#REMPLACER_PAR_LIEN_PDF#" target="_blank" rel="noopener">📄 Télécharger la séquence welcome FluentCRM</a></p>

<p><em>(Le lien reste actif, tu peux y revenir quand tu veux.)</em></p>

<p><strong>Comment l'utiliser en 3 étapes :</strong></p>

<ol>
  <li>Ouvre FluentCRM → Automations → New Funnel</li>
  <li>Colle les 4 objets + délais du tableau page 1 du PDF</li>
  <li>Crée les 4 tags et câble la bascule finale (expliquée section 3)</li>
</ol>

<p>En 45 minutes, le compte de ton client a sa première vraie séquence qui tourne.</p>

<p>Demain je t'envoie pourquoi j'ai créé ce template précis (et pas un générique comme ceux qu'on trouve partout).</p>

<p>Michaël<br>schoolsWP</p>
```

---

## Template 2 · Welcome E2 · Contexte

**Titre template**

```
LM Welcome Template FluentCRM · E2 · Contexte
```

**Sujet**

```
Pourquoi j'ai créé ce template
```

**Pré-header**

```
L'histoire de 40 comptes clients vides
```

**Corps (HTML)**

```html
<p>Salut {{contact.first_name}},</p>

<p>Il y a 2 ans, j'installais FluentCRM chez un client formateur WordPress. 3 mois plus tard, je repasse voir le compte.</p>

<p>Liste : 340 inscrits. Automations actives : 0. Emails envoyés : 0.</p>

<p>Le client avait payé la licence, j'avais bien configuré SMTP, tout fonctionnait. Mais personne n'avait jamais écrit la première séquence.</p>

<p>C'est devenu ma règle : je ne livre plus un FluentCRM sans une séquence welcome. Et pour ne pas repartir de zéro à chaque client, j'ai créé ce template.</p>

<p>Celui que tu as téléchargé hier.</p>

<p>Dis-moi : tu installes FluentCRM pour combien de clients par an ?<br>
<em>(Réponds directement à cet email, je lis tout.)</em></p>

<p>Michaël</p>
```

---

## Template 3 · Welcome E3 · Astuce

**Titre template**

```
LM Welcome Template FluentCRM · E3 · Astuce
```

**Sujet**

```
L'astuce que j'ajoute à chaque compte client
```

**Pré-header**

```
Goal tracking sur l'email 3 = +30 % de conversions
```

**Corps (HTML)**

```html
<p>Salut {{contact.first_name}},</p>

<p><strong>L'astuce :</strong> sur l'email 3 du template, ajoute un Goal.</p>

<p>FluentCRM → Funnel → Block "Benchmark" → Goal "Clicked Link"<br>
→ action "Apply Tag: engaged_lead"</p>

<p>Résultat chez mes clients : ~30 % des inscrits déclenchent ce goal. Ça donne une liste ultra-segmentée, prête pour une offre ciblée.</p>

<p>Tu peux tester FluentCRM Pro ici si tu ne l'as pas encore : <a href="https://fluentcrm.com/" target="_blank" rel="noopener">FluentCRM Pro</a> <em>(affilié, ça soutient le travail)</em></p>

<p>Michaël</p>
```

---

## Template 4 · Welcome E4 · Transition

**Titre template**

```
LM Welcome Template FluentCRM · E4 · Transition
```

**Sujet**

```
Ce que tu vas recevoir ensuite
```

**Pré-header**

```
La suite côté FluentCRM
```

**Corps (HTML)**

```html
<p>Salut {{contact.first_name}},</p>

<p><strong>Récap de la semaine :</strong></p>

<ul>
  <li>J+0 : template welcome FluentCRM livré</li>
  <li>J+1 : pourquoi il existe</li>
  <li>J+3 : l'astuce goal tracking email 3</li>
</ul>

<p>La suite : je t'envoie sur 3 semaines une série pratique sur FluentCRM (les automations que j'installe en priorité, les pièges à éviter, la façon dont je justifie la licence chez mes clients).</p>

<p>Une seule question avant de démarrer :<br>
qu'est-ce que tu essaies de résoudre en priorité côté FluentCRM ?<br>
<em>(Automation ? Délivrabilité ? Revente ? Quelque chose d'autre ?)</em></p>

<p>Réponds-moi en une ligne. Ça oriente ce que je t'envoie ensuite.</p>

<p>Michaël<br>schoolsWP</p>
```

---

## Template 5 · Affiliation E1 · Le coût

**Titre template**

```
SEQ FluentCRM Pro · E1 · Le coût
```

**Sujet**

```
Combien tu paies Mailchimp ce mois-ci ?
```

**Sujet alternatif (A/B)**

```
Le coût caché de ton email marketing
```

**Corps (HTML)**

```html
<p>{{contact.first_name}},</p>

<p>Tu as téléchargé la séquence welcome FluentCRM il y a quelques jours.</p>

<p>Une question directe : si tu installes FluentCRM chez tes clients mais que toi tu utilises encore Mailchimp, Brevo ou ActiveCampaign, tu paies combien par mois pour envoyer tes propres emails ?</p>

<ul>
  <li>30 €/mois si tu as 2 000 contacts sur Brevo.</li>
  <li>45 $/mois à 2 000 contacts sur Mailchimp.</li>
  <li>49 $/mois sur ActiveCampaign Lite.</li>
</ul>

<p>500 à 600 € par an pour faire exactement ce que FluentCRM fait.<br>
Sur ton propre WordPress. Avec tes contacts chez toi.<br>
Pas chez un tiers.</p>

<p>Demain je t'envoie ce que FluentCRM voit que les autres ne voient pas.</p>

<p>Michaël</p>

<p><strong>P.S.</strong> : Je ne te pousse pas à résilier quoi que ce soit aujourd'hui. Je te pose juste la question que personne ne te pose.</p>
```

---

## Template 6 · Affiliation E2 · La découverte

**Titre template**

```
SEQ FluentCRM Pro · E2 · La découverte
```

**Sujet**

```
Ce que tes contacts font vraiment dans WordPress
```

**Sujet alternatif (A/B)**

```
FluentCRM voit ce que Brevo ne verra jamais
```

**Corps (HTML)**

```html
<p>{{contact.first_name}},</p>

<p>Hier je te parlais du coût.<br>
Aujourd'hui je te parle de ce que tu rates côté données.</p>

<p><strong>Mailchimp, Brevo, ActiveCampaign savent :</strong></p>
<ul>
  <li>Si tes contacts ouvrent tes emails</li>
  <li>S'ils cliquent sur tes liens</li>
</ul>

<p><strong>FluentCRM sait ça, plus :</strong></p>
<ul>
  <li>Quels articles WordPress ils lisent</li>
  <li>Quels formulaires ils remplissent (Fluent Forms, WPForms, Gravity)</li>
  <li>Quels produits WooCommerce ils achètent (et ceux qu'ils abandonnent)</li>
  <li>Quelles formations LMS ils suivent (LearnDash, TutorLMS, LifterLMS)</li>
</ul>

<p>Parce que FluentCRM tourne DANS ton WordPress.<br>
Pas à côté.</p>

<p>Ça change tout : tu segmentes sur des comportements réels, pas juste sur des clics email.</p>

<p>Michaël</p>

<p><strong>P.S.</strong> : La version gratuite suffit pour tester tout ça.</p>
```

---

## Template 7 · Affiliation E3 · La preuve

**Titre template**

```
SEQ FluentCRM Pro · E3 · La preuve
```

**Sujet**

```
3 ans avec FluentCRM chez mes clients
```

**Sujet alternatif (A/B)**

```
Ce que j'ai arrêté de faire grâce à FluentCRM
```

**Corps (HTML)**

```html
<p>{{contact.first_name}},</p>

<p>Ça fait 3 ans que j'installe FluentCRM chez mes clients.</p>

<p><strong>Ce que j'ai arrêté de faire :</strong></p>
<ul>
  <li>Exporter un CSV Brevo pour croiser avec WooCommerce</li>
  <li>Facturer 2 heures de "debug SMTP Mailchimp" par mois</li>
  <li>Expliquer au client pourquoi il paie 2 outils qui font la moitié du travail</li>
</ul>

<p><strong>Ce que j'ai commencé à faire :</strong></p>
<ul>
  <li>Livrer une automation welcome dès l'installation (avec le template que tu as)</li>
  <li>Segmenter sur l'achat WooCommerce sans exporter quoi que ce soit</li>
  <li>Facturer la config FluentCRM comme un package, c'est plus clair pour le client</li>
</ul>

<p>Un exemple concret : sur un client formateur, la séquence "acheteur formation débutant" vs "acheteur formation avancée" a doublé le taux d'upsell sur 90 jours. Zéro export, zéro Zapier.</p>

<p>Tu peux installer FluentCRM gratuitement ici : <a href="https://wordpress.org/plugins/fluent-crm/" target="_blank" rel="noopener">FluentCRM (version gratuite WordPress)</a></p>

<p>Michaël</p>

<p><strong>P.S.</strong> : Une limite honnête, l'UI des funnels demande 20 min d'adaptation si tu viens d'ActiveCampaign. Après, tu ne veux plus revenir en arrière.</p>
```

---

## Template 8 · Affiliation E4 · Gratuit vs Pro

**Titre template**

```
SEQ FluentCRM Pro · E4 · Gratuit vs Pro
```

**Sujet**

```
Gratuit vs Pro : quand ça vaut vraiment le coup
```

**Sujet alternatif (A/B)**

```
La seule raison de passer Pro
```

**Corps (HTML)**

```html
<p>{{contact.first_name}},</p>

<p>FluentCRM gratuit est déjà solide.<br>
Tu as les campagnes, les automations, les tags, les formulaires.</p>

<p><strong>Alors quand passer Pro ?</strong></p>

<p>Pas pour "avoir plus de fonctionnalités".<br>
Pour un cas d'usage précis :</p>

<p>→ Si tu automatises au-delà de "envoie 3 emails à la suite"<br>
<em>(conditions, branches, goals, split A/B sur les funnels)</em></p>

<p>→ Si tu fais du WooCommerce ou du LMS<br>
<em>(les deep data Pro débloquent l'automation sur le comportement d'achat)</em></p>

<p>→ Si tu revends FluentCRM à tes clients<br>
<em>(la licence Agency te couvre plusieurs installations)</em></p>

<p>Si tu es juste sur "envoyer une newsletter hebdo" : la version gratuite suffit.<br>
Si tu veux vraiment passer en mode automation : le Pro se paie tout seul.</p>

<p>Demain je t'envoie le lien direct et je te laisse décider.</p>

<p>Michaël</p>

<p><strong>P.S.</strong> : Tu n'es pas obligé d'acheter maintenant. Tu peux tester la version gratuite pendant un mois avant de voir si le Pro t'apporterait quelque chose.</p>
```

---

## Template 9 · Affiliation E5 · La décision

**Titre template**

```
SEQ FluentCRM Pro · E5 · La décision
```

**Sujet**

```
Dernière chose sur FluentCRM
```

**Sujet alternatif (A/B)**

```
Je te laisse décider
```

**Corps (HTML)**

```html
<p>{{contact.first_name}},</p>

<p>Je ne vais pas te relancer 15 fois.</p>

<p>Mais voici la question directe : tu livres des sites WordPress avec une stratégie email à tes clients, oui ou non ?</p>

<p>Si oui, tu as besoin d'un outil qui tient dans WordPress. Pas d'un abonnement Mailchimp facturé en $ avec une interface qui ne sait rien de ton WooCommerce.</p>

<p>FluentCRM est celui que j'utilise sur schoolsWP et chez tous mes clients. Pas parce que c'est parfait. Parce que c'est simple, efficace, natif WordPress, et que tes contacts restent chez toi.</p>

<p>Version gratuite → <a href="https://wordpress.org/plugins/fluent-crm/" target="_blank" rel="noopener">wordpress.org/plugins/fluent-crm</a><br>
Version Pro → <a href="https://fluentcrm.com/" target="_blank" rel="noopener">fluentcrm.com</a> <em>(lien affilié)</em></p>

<p>Michaël</p>

<p><strong>P.S.</strong> : Si tu as une question sur la config ou le choix de la licence, réponds à cet email. Je te file un coup de main.</p>
```

---

## Checklist de création

- [ ] Template 1 : LM Welcome Template FluentCRM · E1 · Livraison
- [ ] Template 2 : LM Welcome Template FluentCRM · E2 · Contexte
- [ ] Template 3 : LM Welcome Template FluentCRM · E3 · Astuce
- [ ] Template 4 : LM Welcome Template FluentCRM · E4 · Transition
- [ ] Template 5 : SEQ FluentCRM Pro · E1 · Le coût
- [ ] Template 6 : SEQ FluentCRM Pro · E2 · La découverte
- [ ] Template 7 : SEQ FluentCRM Pro · E3 · La preuve
- [ ] Template 8 : SEQ FluentCRM Pro · E4 · Gratuit vs Pro
- [ ] Template 9 : SEQ FluentCRM Pro · E5 · La décision

Une fois les 9 templates créés, reviens à [05-manual-setup-fluentcrm.md](05-manual-setup-fluentcrm.md) étape 2 (formulaire Fluent Forms).
