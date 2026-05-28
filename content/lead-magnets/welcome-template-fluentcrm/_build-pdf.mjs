#!/usr/bin/env node
// Build du PDF lead magnet "Séquence welcome FluentCRM" : multi-pages A4, design brand schoolsWP.
// Fusionne le contenu complet (v3, 11 pages) dans le système visuel schoolsWP.
// Rendu via Playwright (Chromium headless). QR code embarqué en data URI.
import { readFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';

const __dirname = dirname(fileURLToPath(import.meta.url));
// playwright est installé dans tools/html-to-png/node_modules (pas à la racine).
const toolsBase = resolve(__dirname, '..', '..', '..', 'tools', 'html-to-png', 'md-to-pdf.mjs');
const requireFromTools = createRequire(pathToFileURL(toolsBase));
const { chromium } = requireFromTools('playwright');

const qrPath = resolve(__dirname, '_qr-schoolswp.png');
const outputPath = resolve(__dirname, process.env.PDF_OUT || 'Template-Welcome-FluentCRM-schoolsWP.pdf');
const qrDataUri = `data:image/png;base64,${readFileSync(qrPath).toString('base64')}`;

const css = `
  @page {
    size: A4;
    margin: 17mm 15mm 16mm 15mm;
    @bottom-center {
      content: "schoolsWP  ·  schoolswp.com  ·  page " counter(page) " / " counter(pages);
      font-family: 'Inter', sans-serif; font-size: 7.5pt; color: #9ca3af; letter-spacing: 0.03em;
    }
  }
  @page :first { margin: 0 15mm 16mm 15mm; }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body {
    font-family: 'Inter', -apple-system, system-ui, sans-serif;
    color: #0F1419; background: #fff;
    -webkit-print-color-adjust: exact; print-color-adjust: exact;
    font-size: 10.5px; line-height: 1.5;
  }
  /* Cover */
  .cover { padding-top: 0; }
  .cover .topbar { height: 7px; background: linear-gradient(90deg, #00D400 0%, #00A300 100%); margin: 0 -15mm 16px -15mm; }
  .cover-head { display: flex; align-items: center; justify-content: space-between; margin-bottom: 26px; }
  .wordmark { font-size: 20px; font-weight: 800; letter-spacing: -0.02em; color: #0F1419; }
  .wordmark .wp { color: #00D400; }
  .badge {
    display: inline-flex; align-items: center; gap: 7px;
    background: #0F1419; color: #fff; padding: 6px 13px; border-radius: 999px;
    font-size: 10px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase;
  }
  .badge .dot { width: 7px; height: 7px; background: #00D400; border-radius: 50%; }
  .cover h1 { font-size: 34px; font-weight: 800; line-height: 1.08; letter-spacing: -0.02em; margin-bottom: 12px; }
  .cover h1 .g { color: #00D400; }
  .cover .lede { font-size: 14px; font-weight: 600; color: #00A300; margin-bottom: 28px; }
  /* Sections */
  .section { break-before: page; }
  h2 {
    font-size: 20px; font-weight: 800; color: #0F1419; letter-spacing: -0.01em;
    padding-bottom: 8px; margin-bottom: 14px; border-bottom: 2px solid #00D400;
  }
  h2 .n { color: #00D400; }
  h3 {
    font-size: 13px; font-weight: 700; color: #0F1419;
    display: flex; align-items: center; gap: 8px; margin: 16px 0 7px 0;
  }
  h3 .bar { width: 18px; height: 4px; background: #00D400; border-radius: 2px; flex: 0 0 auto; }
  p { margin-bottom: 9px; }
  .lead { font-size: 11px; line-height: 1.55; color: #374151; margin-bottom: 12px; }
  .muted { font-size: 9.5px; color: #6b7280; line-height: 1.5; }
  strong { font-weight: 700; color: #0F1419; }
  code {
    font-family: 'Consolas', 'Monaco', monospace; font-size: 9px;
    background: #ecfdf3; color: #027a48; padding: 1px 4px; border-radius: 3px;
  }
  /* Tables */
  table { border-collapse: collapse; width: 100%; margin: 8px 0 12px 0; font-size: 9.3px; break-inside: avoid; }
  th, td { border: 1px solid #e5e7eb; padding: 7px 9px; text-align: left; vertical-align: top; line-height: 1.35; }
  thead th { background: #0F1419; color: #fff; font-weight: 600; font-size: 8.7px; letter-spacing: 0.02em; text-transform: uppercase; }
  tbody tr:nth-child(even) { background: #F4F5F7; }
  td .num { color: #00A300; font-weight: 700; }
  /* Two columns */
  .twocol { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 6px 0 12px 0; break-inside: avoid; }
  .box { border: 1px solid #e5e7eb; border-radius: 10px; padding: 15px 17px; background: #F9FAFB; }
  .box.pos { background: #ecfdf3; border: 1px solid #abefc6; border-left: 4px solid #00D400; }
  .box.neg { background: #faf9f7; border-left: 4px solid #9ca3af; }
  .box h4 { font-size: 12px; font-weight: 800; margin-bottom: 10px; letter-spacing: 0.02em; }
  .box.pos h4 { color: #027a48; }
  .box.neg h4 { color: #6b7280; }
  .box ul { list-style: none; display: flex; flex-direction: column; gap: 6px; }
  .box li { font-size: 9.8px; line-height: 1.4; color: #374151; padding-left: 18px; position: relative; }
  .box.pos li::before { content: "\\2713"; position: absolute; left: 0; color: #00A300; font-weight: 800; }
  .box.neg li::before { content: "\\2022"; position: absolute; left: 2px; color: #9ca3af; font-weight: 800; }
  /* Rules / callouts */
  .rules { display: flex; flex-direction: column; gap: 6px; margin: 6px 0 10px 0; }
  .rule { font-size: 10px; line-height: 1.45; color: #374151; display: flex; gap: 8px; }
  .rule .arr { color: #00D400; font-weight: 800; flex: 0 0 auto; }
  /* Steps */
  .steps { counter-reset: step; display: flex; flex-direction: column; gap: 11px; margin: 6px 0 12px 0; }
  .step { display: flex; gap: 12px; font-size: 10.5px; line-height: 1.5; color: #374151; align-items: flex-start; break-inside: avoid; }
  .step .n {
    counter-increment: step; flex: 0 0 auto; width: 23px; height: 23px; border-radius: 50%;
    background: #00D400; color: #fff; font-weight: 700; font-size: 11px;
    display: flex; align-items: center; justify-content: center;
  }
  .step .n::before { content: counter(step); }
  .step .t strong { display: block; margin-bottom: 1px; }
  /* Checklist */
  .check { display: flex; flex-direction: column; gap: 7px; margin: 6px 0 10px 0; }
  .check .item { font-size: 10px; line-height: 1.4; color: #374151; display: flex; gap: 9px; break-inside: avoid; }
  .check .bx { flex: 0 0 auto; width: 13px; height: 13px; border: 1.5px solid #00A300; border-radius: 3px; margin-top: 1px; }
  .check .item strong { display: block; }
  /* Email cards */
  .email { border: 1px solid #e5e7eb; border-radius: 10px; padding: 0; margin: 0 0 14px 0; overflow: hidden; break-inside: avoid; }
  .email .head { background: #F4F5F7; padding: 9px 15px; border-bottom: 1px solid #e5e7eb; }
  .email .tag-when { font-size: 9px; font-weight: 700; color: #00A300; text-transform: uppercase; letter-spacing: 0.05em; }
  .email .subj { font-size: 12px; font-weight: 700; color: #0F1419; margin-top: 3px; }
  .email .pre { font-size: 9.3px; color: #6b7280; margin-top: 2px; }
  .email .body { padding: 12px 15px; font-size: 9.8px; line-height: 1.5; color: #374151; }
  .email .body p { margin-bottom: 7px; }
  .email .body .sig { color: #0F1419; font-weight: 600; }
  .email .foot { padding: 8px 15px; border-top: 1px dashed #e5e7eb; font-size: 9px; color: #6b7280; }
  /* CTA */
  .cta {
    display: flex; gap: 12px; align-items: flex-start; margin: 14px 0 0 0;
    background: #ecfdf3; border: 1px solid #abefc6; border-left: 4px solid #00D400;
    border-radius: 10px; padding: 16px 18px;
  }
  .cta .arr { color: #00A300; font-weight: 800; font-size: 16px; flex: 0 0 auto; }
  .cta .big { font-size: 12px; font-weight: 700; color: #054f31; margin-bottom: 4px; }
  .cta .small { font-size: 10px; color: #047857; line-height: 1.5; }
  .cta a, .lead a, .email a { color: #00A300; font-weight: 600; text-decoration: none; border-bottom: 1px solid rgba(0,161,0,0.35); }
  /* Cover footer */
  .cover-foot { display: flex; align-items: flex-end; justify-content: space-between; margin-top: 26px; padding-top: 16px; border-top: 1px solid #e5e7eb; }
  .cover-foot .tagline { font-size: 11px; font-weight: 700; }
  .cover-foot .tagline .wp { color: #00D400; }
  .cover-foot .url { font-size: 10px; font-weight: 600; color: #00A300; margin-top: 2px; }
  .cover-foot .author { font-size: 9px; color: #9ca3af; margin-top: 2px; }
  .qr { display: flex; flex-direction: column; align-items: center; gap: 4px; }
  .qr img { width: 84px; height: 84px; }
  .qr span { font-size: 7.5px; color: #9ca3af; }
  .toc { display: flex; flex-direction: column; gap: 5px; margin: 4px 0 8px 0; }
  .toc .ti { font-size: 10px; color: #374151; display: flex; gap: 8px; }
  .toc .ti .d { color: #00A300; font-weight: 700; flex: 0 0 auto; }
`;

const html = `<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Séquence welcome FluentCRM - schoolsWP</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>${css}</style>
</head>
<body>

<!-- COVER -->
<section class="cover">
  <div class="topbar"></div>
  <div class="cover-head">
    <div class="wordmark">schools<span class="wp">WP</span></div>
    <span class="badge"><span class="dot"></span> Ressource gratuite &middot; FluentCRM</span>
  </div>
  <h1>Séquence welcome <span class="g">FluentCRM</span></h1>
  <div class="lede">Template prêt à copier &middot; 4 emails &middot; 7 jours</div>

  <h3><span class="bar"></span> Pour qui</h3>
  <p class="lead">Pour les freelances WordPress qui installent FluentCRM chez leurs clients, mais qui veulent livrer plus qu'un outil : un vrai système d'emailing prêt à tourner. Réutilisable à l'identique sur n'importe quel compte. Pas de générique : un template forgé sur le terrain.</p>

  <h3><span class="bar"></span> Ce que tu trouves dans ce PDF</h3>
  <div class="toc">
    <div class="ti"><span class="d">1.</span><span>Une page Avant / Après pour visualiser le gain concret pour ton client.</span></div>
    <div class="ti"><span class="d">2.</span><span>Le schéma complet du funnel FluentCRM : trigger, délais, tags, conditions.</span></div>
    <div class="ti"><span class="d">3.</span><span>Les 4 emails complets prêts à copier : objet, pré-header, corps, CTA.</span></div>
    <div class="ti"><span class="d">4.</span><span>La checklist d'installation technique + une checklist livraison client.</span></div>
    <div class="ti"><span class="d">5.</span><span>Les variantes par type de client : formateur (cours) vs e-commerce (boutique).</span></div>
    <div class="ti"><span class="d">6.</span><span>Les 5 erreurs à éviter quand tu installes ce funnel chez un client.</span></div>
  </div>

  <h3><span class="bar"></span> Promesse en une ligne</h3>
  <p class="lead">En 45 minutes, le compte FluentCRM de ton client a une séquence welcome qui tourne, qui qualifie les leads et qui bascule proprement vers la newsletter régulière. Tu colles, tu adaptes la signature, c'est en place.</p>
  <p class="muted">Note : tout fonctionne sur la version gratuite de FluentCRM. La version Pro apporte uniquement le goal tracking avancé (optionnel et pédagogique).</p>

  <div class="cover-foot">
    <div>
      <div class="tagline">schools<span class="wp">WP</span> : WordPress. Clair. Structuré. Utile.</div>
      <div class="url">schoolswp.com</div>
      <div class="author">Par Michaël KIHL &middot; v3</div>
    </div>
    <div class="qr"><img src="${qrDataUri}" alt="QR vers schoolswp.com"><span>schoolswp.com</span></div>
  </div>
</section>

<!-- AVANT / APRES -->
<section class="section">
  <h2>Avant / Après : ce que ton client gagne</h2>
  <p class="lead">Avant que tu installes ce template, voilà l'état typique d'un compte FluentCRM livré par un freelance (ou par le client lui-même après un tuto YouTube). Après l'installation, voilà ce que ton client constate dès la première semaine.</p>
  <div class="twocol">
    <div class="box neg">
      <h4>AVANT</h4>
      <ul>
        <li>FluentCRM installé, SMTP configuré</li>
        <li>Aucune séquence active</li>
        <li>Liste qui dort, contacts inactifs</li>
        <li>Aucun email parti depuis 3 mois</li>
        <li>Aucun retour visible pour le client</li>
        <li>Le client se demande pourquoi il a payé la licence</li>
      </ul>
    </div>
    <div class="box pos">
      <h4>APRÈS (en 45 min)</h4>
      <ul>
        <li>Séquence welcome 4 emails active</li>
        <li>Liste qui chauffe dès le J+0</li>
        <li>Contacts segmentés par engagement (tags)</li>
        <li>Bascule propre vers la newsletter régulière</li>
        <li>Reporting visible : ouverture / clic / désinscription</li>
        <li>Base prête pour vendre une offre, une formation</li>
      </ul>
    </div>
  </div>
  <h3><span class="bar"></span> Ce que ça change dans ta prestation</h3>
  <p class="lead">Tu ne livres plus une configuration, tu livres un système. C'est l'écart entre "j'ai installé FluentCRM" et "j'ai mis en place une automation marketing". Le second se vend 3 à 5 fois plus cher, et le client le perçoit immédiatement parce qu'il voit la séquence tourner.</p>
</section>

<!-- SCHEMA FUNNEL -->
<section class="section">
  <h2><span class="n">1.</span> Schéma du funnel FluentCRM</h2>
  <p class="lead">Trigger : un nouveau contact rejoint la liste cible (ou reçoit le tag de démarrage). La séquence s'exécute ensuite de manière linéaire avec une seule sortie automatique : la désinscription.</p>
  <table>
    <thead><tr><th>#</th><th>Délai</th><th>Action FluentCRM</th><th>Tag appliqué APRÈS envoi</th><th>Condition</th></tr></thead>
    <tbody>
      <tr><td><span class="num">1</span></td><td>T+0</td><td>Send Email 1 - Livraison</td><td><code>welcome_e1_sent</code></td><td>aucune</td></tr>
      <tr><td><span class="num">2</span></td><td>T+1j</td><td>Send Email 2 - Contexte</td><td><code>welcome_e2_sent</code></td><td>non désinscrit</td></tr>
      <tr><td><span class="num">3</span></td><td>T+3j</td><td>Send Email 3 - Astuce</td><td><code>welcome_e3_sent</code></td><td>non désinscrit</td></tr>
      <tr><td><span class="num">4</span></td><td>T+7j</td><td>Send Email 4 - Transition</td><td><code>welcome_completed</code></td><td>non désinscrit</td></tr>
    </tbody>
  </table>
  <div class="rules">
    <div class="rule"><span class="arr">&rarr;</span><span><strong>Bascule finale</strong> : après l'email 4, applique le tag de ta séquence suivante, puis Remove from list + Add to list <code>newsletter_active</code>.</span></div>
    <div class="rule"><span class="arr">&rarr;</span><span><strong>Sortie automatique</strong> : désinscription = arrêt immédiat (géré nativement par FluentCRM, rien à configurer).</span></div>
  </div>

  <h3><span class="bar"></span> FluentCRM gratuit vs Pro : quand passer Pro</h3>
  <p class="lead">Tout ce template fonctionne sur la version gratuite. La version Pro devient utile quand tu veux industrialiser et justifier une prestation plus complète chez ton client.</p>
  <div class="twocol">
    <div class="box neg">
      <h4>GRATUIT suffit si...</h4>
      <ul>
        <li>Tu veux envoyer les 4 emails</li>
        <li>Tu veux taguer les contacts (après envoi)</li>
        <li>Tu veux basculer vers une liste newsletter</li>
        <li>Tu veux suivre les ouvertures et clics de base</li>
        <li>Tu n'as pas besoin de scénarios conditionnels avancés</li>
      </ul>
    </div>
    <div class="box pos">
      <h4>PRO devient utile si...</h4>
      <ul>
        <li>Tu veux qualifier les leads engagés (goal tracking)</li>
        <li>Tu veux des branches conditionnelles complexes</li>
        <li>Tu veux une intégration WooCommerce / SureCart avancée</li>
        <li>Tu veux des automations récurrentes (date-based)</li>
        <li>Tu veux justifier une prestation 3-5x plus chère</li>
      </ul>
    </div>
  </div>
  <p class="muted">Lien partenaire FluentCRM Pro : <a href="https://fluentcrm.com/?ref=723">fluentcrm.com</a> (je touche une commission si tu passes par ce lien, ça soutient le travail).</p>
</section>

<!-- LES 4 EMAILS -->
<section class="section">
  <h2><span class="n">2.</span> Les 4 emails prêts à copier</h2>
  <p class="lead">Tous les emails utilisent le smartcode FluentCRM <code>{{contact.first_name|"toi"}}</code> pour personnaliser le prénom (avec fallback sur "toi" si vide). Adapte la signature à toi ou à ton client.</p>

  <div class="email">
    <div class="head"><div class="tag-when">Email 1 &middot; T+0 (immédiat) &middot; Livraison</div><div class="subj">Ton template est juste ici</div><div class="pre">Pré-header : Clique pour télécharger la séquence welcome FluentCRM</div></div>
    <div class="body">
      <p>Salut {{contact.first_name|"toi"}},</p>
      <p>Voilà ton template : <a href="LIEN_PDF">Télécharger la séquence welcome FluentCRM</a> (le lien reste actif, tu peux y revenir quand tu veux).</p>
      <p>Comment l'utiliser en 3 étapes :<br>1. Ouvre FluentCRM puis Automations puis New Funnel<br>2. Colle les 4 objets et délais du tableau du funnel<br>3. Crée les 4 tags et câble la bascule finale</p>
      <p>En 45 minutes, le compte de ton client a sa première vraie séquence qui tourne.</p>
      <p>Demain je t'envoie pourquoi j'ai créé ce template précis (et pas un générique comme ceux qu'on trouve partout).</p>
      <p class="sig">Michaël &middot; schoolsWP</p>
    </div>
    <div class="foot">Tag après l'envoi : <code>welcome_e1_sent</code></div>
  </div>

  <div class="email">
    <div class="head"><div class="tag-when">Email 2 &middot; T+1 jour &middot; Contexte</div><div class="subj">Pourquoi j'ai créé ce template</div><div class="pre">Pré-header : L'histoire de 40 comptes clients vides</div></div>
    <div class="body">
      <p>Salut {{contact.first_name|"toi"}},</p>
      <p>Il y a 2 ans, j'installais FluentCRM chez un client formateur WordPress. 3 mois plus tard, je repasse voir le compte.</p>
      <p>Liste : 340 inscrits. Automations actives : 0. Emails envoyés : 0.</p>
      <p>Le client avait payé la licence, j'avais bien configuré SMTP, tout fonctionnait. Mais personne n'avait jamais écrit la première séquence.</p>
      <p>C'est devenu ma règle : je ne livre plus un FluentCRM sans une séquence welcome. Et pour ne pas repartir de zéro à chaque client, j'ai créé ce template. Celui que tu as téléchargé hier.</p>
      <p>Dis-moi : tu installes FluentCRM pour combien de clients par an ? (Réponds directement à cet email, je lis tout.)</p>
      <p class="sig">Michaël</p>
    </div>
    <div class="foot">Tag après l'envoi : <code>welcome_e2_sent</code></div>
  </div>

  <div class="email">
    <div class="head"><div class="tag-when">Email 3 &middot; T+3 jours &middot; Astuce</div><div class="subj">L'astuce que j'ajoute à chaque compte client</div><div class="pre">Pré-header : Goal tracking sur l'email 3 = +30% de conversions qualifiées</div></div>
    <div class="body">
      <p>Salut {{contact.first_name|"toi"}},</p>
      <p>L'astuce : sur l'email 3 du template, ajoute un Goal. FluentCRM puis Funnel puis Block "Benchmark" puis Goal "Clicked Link" puis action "Apply Tag: engaged_lead".</p>
      <p>Résultat chez mes clients : environ 30% des inscrits déclenchent ce goal. Ça donne une liste ultra-segmentée, prête pour une offre ciblée.</p>
      <p>J'ai écrit un article complet sur les automations FluentCRM que j'installe en priorité : <a href="https://schoolswp.com/fluentcrm-automations-indispensables/">FluentCRM : les 4 automations indispensables</a>.</p>
      <p>Tu peux tester FluentCRM Pro ici si tu ne l'as pas encore : <a href="https://fluentcrm.com/?ref=723">FluentCRM Pro</a> (lien partenaire, ça soutient le travail).</p>
      <p class="sig">Michaël</p>
    </div>
    <div class="foot">Tag après l'envoi : <code>welcome_e3_sent</code></div>
  </div>

  <div class="email">
    <div class="head"><div class="tag-when">Email 4 &middot; T+7 jours &middot; Transition</div><div class="subj">Ce que tu vas recevoir ensuite</div><div class="pre">Pré-header : La suite côté FluentCRM</div></div>
    <div class="body">
      <p>Salut {{contact.first_name|"toi"}},</p>
      <p>Récap de la semaine :<br>- J+0 : template welcome FluentCRM livré<br>- J+1 : pourquoi il existe<br>- J+3 : l'astuce goal tracking email 3</p>
      <p>La suite : je t'envoie sur 3 semaines une série pratique sur FluentCRM (les automations que j'installe en priorité, les pièges à éviter, la façon dont je justifie la licence chez mes clients).</p>
      <p>Une seule question avant de démarrer : qu'est-ce que tu essaies de résoudre en priorité côté FluentCRM ? (Automation ? Délivrabilité ? Revente cliente ? Quelque chose d'autre ?) Réponds-moi en une ligne. Ça oriente ce que je t'envoie ensuite.</p>
      <p class="sig">Michaël &middot; schoolsWP</p>
    </div>
    <div class="foot">Tag après l'envoi : <code>welcome_completed</code> (déclenche la bascule newsletter)</div>
  </div>
</section>

<!-- INSTALLATION -->
<section class="section">
  <h2><span class="n">3.</span> Installation dans FluentCRM en 6 étapes</h2>
  <p class="lead">Suis ces 6 étapes dans l'ordre. Compte ~45 minutes la première fois, ~15 minutes à partir du 2e client.</p>
  <div class="steps">
    <div class="step"><span class="n"></span><span class="t"><strong>Créer les 4 tags</strong>FluentCRM puis Contacts puis Tags puis New Tag. Crée : <code>welcome_e1_sent</code>, <code>welcome_e2_sent</code>, <code>welcome_e3_sent</code>, <code>welcome_completed</code>. Bonus : <code>engaged_lead</code> (branche goal optionnelle).</span></div>
    <div class="step"><span class="n"></span><span class="t"><strong>Créer les 4 modèles d'email</strong>FluentCRM puis Emails puis Email Templates puis Create New. Colle les 4 corps de la section 2. Pour chaque modèle : sujet, pré-header, corps HTML (mode Source si tu colles depuis ce PDF).</span></div>
    <div class="step"><span class="n"></span><span class="t"><strong>Créer le funnel</strong>FluentCRM puis Automations puis New Funnel puis Trigger "Contact Added to Tag" (ou "Form Submission" selon ta source). Nom : Welcome - Séquence FluentCRM.</span></div>
    <div class="step"><span class="n"></span><span class="t"><strong>Câbler les 4 envois + tags</strong>Pour chaque email : Send Email puis Apply Tag (APRÈS l'envoi, pas avant). Avec les délais : 0, 1 jour, 3 jours, 7 jours.</span></div>
    <div class="step"><span class="n"></span><span class="t"><strong>Câbler la bascule finale</strong>Après l'email 4 : Apply Tag (séquence suivante) puis Remove from list (liste lead magnet) puis Add to list <code>newsletter_active</code>.</span></div>
    <div class="step"><span class="n"></span><span class="t"><strong>Tester avec un contact réel</strong>Crée un contact test avec ton email perso. Applique le tag de démarrage manuellement. Vérifie l'email 1 dans les 5 min. Réduis temporairement les délais à 1 minute pour valider le flux, puis réactive les vrais délais.</span></div>
  </div>
  <h3><span class="bar"></span> Checklist technique avant activation</h3>
  <div class="check">
    <div class="item"><span class="bx"></span><span>4 tags créés</span></div>
    <div class="item"><span class="bx"></span><span>4 modèles d'email rédigés (section 2)</span></div>
    <div class="item"><span class="bx"></span><span>Funnel créé avec le bon trigger</span></div>
    <div class="item"><span class="bx"></span><span>Tags appliqués APRÈS chaque Send Email</span></div>
    <div class="item"><span class="bx"></span><span>Délais 0 / 1 / 3 / 7 jours configurés</span></div>
    <div class="item"><span class="bx"></span><span>Bascule finale câblée (tag + remove/add list)</span></div>
    <div class="item"><span class="bx"></span><span>Test réel passé avec un contact perso</span></div>
    <div class="item"><span class="bx"></span><span>Liens de désinscription vérifiés</span></div>
    <div class="item"><span class="bx"></span><span>Funnel publié</span></div>
  </div>
</section>

<!-- CHECKLIST LIVRAISON CLIENT -->
<section class="section">
  <h2><span class="n">4.</span> Checklist livraison client</h2>
  <p class="lead">À la fin de l'installation, fais cette démo de 10 minutes à ton client (visio ou présentiel). Tu coches chaque ligne devant lui. C'est l'outil de prestation qui transforme ton install technique en livrable perçu. Il sert aussi de procès-verbal de fin de mission.</p>
  <div class="check">
    <div class="item"><span class="bx"></span><span><strong>La séquence est active</strong>Ouvrir FluentCRM puis Automations, vérifier le statut "Published" du funnel Welcome.</span></div>
    <div class="item"><span class="bx"></span><span><strong>L'email 1 part bien</strong>Envoyer un test sur l'adresse du client pour qu'il voie l'email arriver dans sa boîte.</span></div>
    <div class="item"><span class="bx"></span><span><strong>Les tags sont appliqués après l'envoi</strong>Ouvrir un contact, vérifier l'onglet Tags : <code>welcome_e1_sent</code> visible.</span></div>
    <div class="item"><span class="bx"></span><span><strong>La liste newsletter reçoit les bons contacts</strong>Après l'email 4, le contact bascule dans <code>newsletter_active</code>.</span></div>
    <div class="item"><span class="bx"></span><span><strong>Le lien de désinscription fonctionne</strong>Cliquer "Unsubscribe" dans un email reçu et vérifier la page de désabonnement.</span></div>
    <div class="item"><span class="bx"></span><span><strong>Le reporting de base est vérifiable</strong>FluentCRM puis Emails puis Reports : ouverture / clic / désinscription visibles.</span></div>
    <div class="item"><span class="bx"></span><span><strong>Les emails sont aux coordonnées du client</strong>Signature : nom, site et réseaux du client (pas la signature schoolsWP).</span></div>
    <div class="item"><span class="bx"></span><span><strong>Le client a un accès FluentCRM (si besoin)</strong>Rôle admin OU rôle custom Email Manager.</span></div>
  </div>
  <p class="muted">Conseil : envoie cette checklist par email à ton client à la fin de la mission. C'est un excellent ancrage de valeur, il garde la trace écrite de ce qu'il a reçu.</p>
</section>

<!-- VARIANTES -->
<section class="section">
  <h2><span class="n">5.</span> Variantes par type de client</h2>
  <p class="lead">La structure (4 emails, délais, tags, conditions) reste identique. Seuls les objets et la première phrase de chaque email changent selon le contexte du client.</p>
  <h3><span class="bar"></span> Variante A - Client formateur (cours, formations)</h3>
  <table>
    <thead><tr><th>#</th><th>Objet adapté</th></tr></thead>
    <tbody>
      <tr><td><span class="num">1</span></td><td>Ta première leçon arrive maintenant</td></tr>
      <tr><td><span class="num">2</span></td><td>Pourquoi je forme depuis 5 ans</td></tr>
      <tr><td><span class="num">3</span></td><td>L'erreur que font 90% des débutants</td></tr>
      <tr><td><span class="num">4</span></td><td>Voilà ce qu'on couvre ensemble ensuite</td></tr>
    </tbody>
  </table>
  <h3><span class="bar"></span> Variante B - Client e-commerce (boutique, abonnements)</h3>
  <table>
    <thead><tr><th>#</th><th>Objet adapté</th></tr></thead>
    <tbody>
      <tr><td><span class="num">1</span></td><td>Bienvenue, voici ton bon de bienvenue</td></tr>
      <tr><td><span class="num">2</span></td><td>L'histoire derrière [marque]</td></tr>
      <tr><td><span class="num">3</span></td><td>Le produit le plus sous-coté du catalogue</td></tr>
      <tr><td><span class="num">4</span></td><td>Ce que les habitués commandent en 2e fois</td></tr>
    </tbody>
  </table>
</section>

<!-- 5 ERREURS -->
<section class="section">
  <h2><span class="n">6.</span> Les 5 erreurs à éviter</h2>
  <p class="lead">Ces 5 erreurs sont celles que je vois le plus souvent quand un freelance installe sa première séquence. Elles cassent ou dégradent le funnel sans que tu t'en rendes compte avant que ton client ne te le signale. Une lecture rapide avant publication te les évite toutes.</p>
  <h3><span class="bar"></span> Erreur 1 - Créer les tags avant d'avoir défini la logique</h3>
  <p class="lead">Tu crées 12 tags "au cas où", puis tu te perds. La règle : ne crée un tag que si tu sais exactement quelle action y est attachée. Pour ce template : 4 tags (un par email envoyé) + 1 bonus (<code>engaged_lead</code>). C'est tout.</p>
  <h3><span class="bar"></span> Erreur 2 - Taguer avant l'envoi (et pas après)</h3>
  <p class="lead">Si tu mets Apply Tag puis Send Email, le tag est appliqué même si l'envoi échoue (SMTP down, rebond, contact bloqué). Ton tag ment alors sur l'état réel. Toujours : Send Email puis Apply Tag.</p>
  <h3><span class="bar"></span> Erreur 3 - Oublier le test réel avec un contact</h3>
  <p class="lead">Lancer la séquence sans test préalable, c'est le meilleur moyen de découvrir un email cassé via le client. Crée un contact test, lance le funnel, baisse les délais à 1 minute, valide tout le flux, puis remets les vrais délais.</p>
  <h3><span class="bar"></span> Erreur 4 - Ne pas vérifier le lien de désinscription</h3>
  <p class="lead">FluentCRM ajoute le lien de désinscription par défaut, mais selon le template HTML il peut être invisible (même couleur que le fond, taille trop petite). Clique-le toi-même avant de publier. RGPD oblige.</p>
  <h3><span class="bar"></span> Erreur 5 - Laisser les contacts dans la mauvaise liste</h3>
  <p class="lead">À la fin du funnel, fais Remove from list (liste lead magnet) puis Add to list <code>newsletter_active</code>. Sinon le contact reste éternellement dans la liste lead magnet et reçoit des doublons quand tu pousses la prochaine séquence.</p>
</section>

<!-- ET APRES -->
<section class="section">
  <h2>Et après ?</h2>
  <p class="lead">Tu as maintenant tout ce qu'il faut pour installer la séquence chez ton premier client (ou pour ton propre site). 45 minutes de boulot, et tu transformes une licence FluentCRM dormante en système actif.</p>
  <h3><span class="bar"></span> Prochaine étape recommandée</h3>
  <div class="steps">
    <div class="step"><span class="n"></span><span class="t">Installe la séquence chez un premier client (ou sur ton propre site) en suivant les 6 étapes de la section 3.</span></div>
    <div class="step"><span class="n"></span><span class="t">Teste avec un contact réel comme décrit dans la checklist livraison client.</span></div>
    <div class="step"><span class="n"></span><span class="t">Une fois la séquence welcome rodée, passe à l'automation suivante : la séquence d'autorité FluentCRM (découverte progressive de la version Pro). Je t'envoie les détails par email dans les 7 prochains jours, automatiquement.</span></div>
  </div>
  <div class="cta">
    <span class="arr">&rarr;</span>
    <div>
      <div class="big">Besoin d'un système FluentCRM complet pour ton site ou celui de tes clients ?</div>
      <div class="small">Retrouve tous les guides, templates et scénarios FluentCRM testés sur le terrain sur <strong>schoolswp.com</strong> : articles, comparatifs, automations recettées, guides d'intégration WooCommerce / TutorLMS / FluentBoards.</div>
    </div>
  </div>
</section>

</body>
</html>`;

const browser = await chromium.launch();
const page = await browser.newContext().then((c) => c.newPage());
await page.setContent(html, { waitUntil: 'networkidle' });
await page.pdf({ path: outputPath, format: 'A4', printBackground: true, preferCSSPageSize: true });
await page.setViewportSize({ width: 794, height: 1123 });
await page.screenshot({ path: resolve(__dirname, '_preview.png'), fullPage: true });
await browser.close();
console.log(outputPath);
