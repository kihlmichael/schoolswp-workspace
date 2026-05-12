# Séquence FluentCRM : Accueil du lead qui a téléchargé le PDF

> Attention : séquence que vit **le lead après inscription**. À ne pas confondre avec la séquence *contenue dans* le PDF.

---

## Email 1 : T+0 (immédiat) · Livraison

**Objet** : Ton template est juste ici
**Pré-header** : Clique pour télécharger la séquence welcome FluentCRM
**Tag appliqué** : `template_welcome_delivered`

```
Salut [prenom|"toi"],

Voilà ton template : [📄 Télécharger la séquence welcome FluentCRM](lien_pdf)

(Le lien reste actif, tu peux y revenir quand tu veux.)

Comment l'utiliser en 3 étapes :

1. Ouvre FluentCRM → Automations → New Funnel
2. Colle les 4 objets + délais du tableau page 1 du PDF
3. Crée les 4 tags et câble la bascule finale (expliquée section 3)

En 45 minutes, le compte de ton client a sa première vraie séquence qui tourne.

Demain je t'envoie pourquoi j'ai créé ce template précis
(et pas un générique comme ceux qu'on trouve partout).

Michaël
schoolsWP
```

---

## Email 2 : T+1 jour · Contexte

**Objet** : Pourquoi j'ai créé ce template
**Pré-header** : L'histoire de 40 comptes clients vides
**Tag appliqué** : `story_delivered`

```
Salut [prenom|"toi"],

Il y a 2 ans, j'installais FluentCRM chez un client formateur WordPress.
3 mois plus tard, je repasse voir le compte.

Liste : 340 inscrits. Automations actives : 0. Emails envoyés : 0.

Le client avait payé la licence, j'avais bien configuré SMTP, tout fonctionnait.
Mais personne n'avait jamais écrit la première séquence.

C'est devenu ma règle : je ne livre plus un FluentCRM sans une séquence welcome.
Et pour ne pas repartir de zéro à chaque client, j'ai créé ce template.

Celui que tu as téléchargé hier.

Dis-moi : tu installes FluentCRM pour combien de clients par an ?
(Réponds directement à cet email, je lis tout.)

Michaël
```

---

## Email 3 : T+3 jours · Valeur additionnelle

**Objet** : L'astuce que j'ajoute à chaque compte client
**Pré-header** : Goal tracking sur l'email 3 = +30 % de conversions
**Tag appliqué** : `tip_delivered`

```
Salut [prenom|"toi"],

L'astuce : sur l'email 3 du template, ajoute un Goal.

FluentCRM → Funnel → Block "Benchmark" → Goal "Clicked Link"
→ action "Apply Tag: engaged_lead"

Résultat chez mes clients : ~30 % des inscrits déclenchent ce goal.
Ça donne une liste ultra-segmentée, prête pour une offre ciblée.

J'ai écrit un article complet sur les automations FluentCRM
que j'installe en priorité : [FluentCRM : les 4 automations indispensables](https://schoolswp.com/fluentcrm-automations-indispensables/)

Tu peux tester FluentCRM Pro ici si tu ne l'as pas encore :
[FluentCRM Pro](https://fluentcrm.com/) (affilié, ça soutient le travail)

Michaël
```

---

## Email 4 : T+7 jours · Transition

**Objet** : Ce que tu vas recevoir ensuite
**Pré-header** : La suite côté FluentCRM
**Tag appliqué** : `welcome_completed`
**Bascule** : move to list `affiliate_fluentcrm_sequence`

```
Salut [prenom|"toi"],

Récap de la semaine :
- J+0 : template welcome FluentCRM livré
- J+1 : pourquoi il existe
- J+3 : l'astuce goal tracking email 3

La suite : je t'envoie sur 3 semaines une série pratique sur FluentCRM
(les automations que j'installe en priorité, les pièges à éviter,
la façon dont je justifie la licence chez mes clients).

Une seule question avant de démarrer :
qu'est-ce que tu essaies de résoudre en priorité côté FluentCRM ?
(Automation ? Délivrabilité ? Revente ? Quelque chose d'autre ?)

Réponds-moi en une ligne. Ça oriente ce que je t'envoie ensuite.

Michaël
schoolsWP
```

---

## Planning FluentCRM (paramétrage funnel)

- **Funnel name** : `Welcome - LM Welcome Template FluentCRM`
- **Trigger** : Form submission → `lead-magnet-welcome-template-fluentcrm`
- **Starting action** : Apply tag `source_lm_fluentcrm` + Add to list `lead_magnet_welcome_template`
- **Action 1** : Send Email 1 (T+0, immédiat) + Apply tag `template_welcome_delivered`
- **Wait** : 1 day
- **Action 2** : Send Email 2 + Apply tag `story_delivered`
- **Wait** : 2 days
- **Action 3** : Send Email 3 + Apply tag `tip_delivered`
- **Wait** : 4 days
- **Action 4** : Send Email 4 + Apply tag `welcome_completed`
- **Action 5** : Move to list `affiliate_fluentcrm_sequence`

## Conditions de sortie

- **Unsubscribe** → sortie immédiate (natif FluentCRM)
- **Clic sur CTA commercial** email 3 → Apply tag `engaged_buyer` (ne sort pas, continue)
- **Pas d'ouverture sur 7 jours** → maintien, pas de re-send auto

## Tags FluentCRM à créer

`source_lm_fluentcrm` · `template_welcome_delivered` · `story_delivered` · `tip_delivered` · `welcome_completed` · `engaged_buyer`

---

## KPIs à suivre

1. **Taux de conversion landing** (visiteurs → inscrits) · cible **25-40 %**
2. **Taux d'ouverture email 1** · cible **> 60 %**
3. **Taux de clic email 1** (téléchargement PDF) · cible **> 40 %**
4. **Taux de réponse email 2** · cible **> 2 %**
5. **Taux de bascule vers `affiliate_fluentcrm_sequence`** · cible **> 70 %** des arrivés à email 4
6. **Taux de désinscription cumulé 7 jours** · cible **< 3 %**
7. **Taux de clic affilié email 3** (FluentCRM Pro) · cible **> 8 %**
