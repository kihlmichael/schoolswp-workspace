import json, html, csv, io

ART_TITLE = "FluentCart vs WooCommerce : lequel choisir ?"

# ---------- NINJA TABLES DATA ----------
t1 = {
    "title": ART_TITLE,
    "desc": "FluentCart vs WooCommerce : le résumé en 30 secondes",
    "columns": [{"name": "Critère", "key": "critere"}, {"name": "FluentCart", "key": "fluentcart"}, {"name": "WooCommerce", "key": "woocommerce"}],
    "rows": [
        {"critere": "Lancement", "fluentcart": "Fin 2025 (récent)", "woocommerce": "2011 (mature)"},
        {"critere": "Architecture", "fluentcart": "SPA moderne (React + API REST)", "woocommerce": "Monolithique WordPress"},
        {"critere": "Abonnements / licences", "fluentcart": "Inclus nativement", "woocommerce": "Extensions payantes"},
        {"critere": "Frais de transaction", "fluentcart": "0 %", "woocommerce": "0 % (cœur)"},
        {"critere": "Écosystème d'extensions", "fluentcart": "Naissant", "woocommerce": "Immense"},
        {"critere": "Produits physiques + logistique", "fluentcart": "Correct", "woocommerce": "Référence"},
        {"critere": "Courbe d'apprentissage", "fluentcart": "Douce", "woocommerce": "Raide"},
        {"critere": "Idéal pour", "fluentcart": "Numérique, formations, abonnements", "woocommerce": "Boutiques physiques, gros catalogues"},
    ],
}
t2 = {
    "title": ART_TITLE,
    "desc": "Tout est inclus dans le cœur du plugin",
    "columns": [{"name": "Fonctionnalité", "key": "fonctionnalite"}, {"name": "FluentCart", "key": "fluentcart"}, {"name": "WooCommerce", "key": "woocommerce"}],
    "rows": [
        {"fonctionnalite": "Abonnements / paiements récurrents", "fluentcart": "Inclus", "woocommerce": "Extension payante"},
        {"fonctionnalite": "Gestion de licences logicielles", "fluentcart": "Inclus", "woocommerce": "Extension payante"},
        {"fonctionnalite": "Tunnels de vente / order bumps", "fluentcart": "Inclus", "woocommerce": "Extension payante"},
        {"fonctionnalite": "Rapports avancés", "fluentcart": "Inclus", "woocommerce": "Extension payante"},
        {"fonctionnalite": "Intégration CRM native", "fluentcart": "Inclus (FluentCRM)", "woocommerce": "Via connecteur"},
    ],
}
json.dump({"tables": [t1, t2]}, open(".tmp-ninja-data.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

def write_csv(path, t):
    buf = io.StringIO()
    w = csv.writer(buf)
    keys = [c["key"] for c in t["columns"]]
    w.writerow([c["name"] for c in t["columns"]])
    for r in t["rows"]:
        w.writerow([r[k] for k in keys])
    open(path, "w", encoding="utf-8", newline="").write(buf.getvalue())

write_csv("content/articles/fluentcart-vs-woocommerce/table-1-resume.csv", t1)
write_csv("content/articles/fluentcart-vs-woocommerce/table-2-inclus.csv", t2)

# ---------- FAQ KADENCE BLOCK ----------
ACC_ATTRS = '"startCollapsed":true,"linkPaneCollapse":false,"contentBgColor":"#ffffff","contentBorderStyle":[{"top":["","",0],"right":["","",0],"bottom":["","",0],"left":["","",0],"unit":"px"}],"titleStyles":[{"size":["md","",""],"sizeType":"em","lineHeight":[1.2,"",""],"lineType":"","letterSpacing":"","family":"","google":"","style":"","weight":"","variant":"","subset":"","loadGoogle":true,"padding":[14,16,14,16],"marginTop":10,"color":"palette3","background":"palette7","border":["","","",""],"borderRadius":["","","",""],"borderWidth":["","","",""],"colorHover":"palette9","backgroundHover":"palette1","borderHover":["","","",""],"colorActive":"palette9","backgroundActive":"palette1","borderActive":["","","",""],"textTransform":""}],"titleBorder":[{"top":[null,"",""],"right":[null,"",""],"bottom":[null,"",""],"left":[null,"",""],"unit":"px"}],"titleBorderHover":[{"top":[null,"",""],"right":[null,"",""],"bottom":[null,"",""],"left":[null,"",""],"unit":"px"}],"titleBorderActive":[{"top":["#444444","",""],"right":["#444444","",""],"bottom":["#444444","",""],"left":["#444444","",""],"unit":"px"}],"titleBorderRadius":[5,5,5,5],"iconStyle":"arrow","iconSide":"left"'

qa = [
    ("Pourquoi FluentCart est-il plus rapide que WooCommerce ?",
     "Grâce à son architecture en Single Page Application et à l'API REST. Là où WooCommerce recharge tout WordPress à chaque action, FluentCart ne traite que les données nécessaires, ce qui réduit le temps d'exécution PHP et la charge serveur. En front-end, il charge aussi beaucoup moins de CSS et de JavaScript sur les pages produits, ce qui garde la navigation fluide même sur un hébergement mutualisé modeste."),
    ("Quelle solution pour vendre des formations et des produits numériques ?",
     "FluentCart, sans hésiter. Il gère nativement les licences, la livraison de fichiers et les abonnements, et il s'intègre à FluentCRM pour automatiser ton marketing après-vente. WooCommerce reste possible si tu veux une personnalisation visuelle extrême du checkout, mais il demandera plus de maintenance pour atteindre la même fluidité."),
    ("WooCommerce garde-t-il un avantage pour les boutiques physiques ?",
     "Oui, et un net. Pour la gestion de stocks multi-entrepôts, les catalogues de milliers de références, les calculs de taxes complexes ou l'intégration avec une caisse physique (POS), sa maturité et son écosystème font la différence. C'est l'outil de la robustesse pour les e-commerçants établis."),
    ("Peut-on gérer des abonnements sans extension payante ?",
     "Oui, c'est l'un des gros avantages de FluentCart : les paiements récurrents sont inclus d'origine. Tu évites une dépense comme WooCommerce Subscriptions, et tout se configure depuis une interface unique, ce qui réduit aussi les risques de conflits entre plugins."),
    ("Combien coûtent vraiment ces deux solutions sur le long terme ?",
     "FluentCart fonctionne sur une licence tout-inclus : tu connais ton coût fixe dès le départ, rapports et tunnels compris. WooCommerce est gratuit au départ, mais son coût total grimpe avec l'accumulation d'extensions payantes (logistique, abonnements, tunnels) et, parfois, un hébergement plus cher pour absorber sa gourmandise. Sur la durée, FluentCart est généralement plus prévisible."),
    ("Peut-on migrer de WooCommerce vers FluentCart facilement ?",
     "Pour une boutique numérique, oui : la bascule est raisonnable et le gain immédiat. Pour une grosse boutique physique avec des intégrations logistiques imbriquées, sois prudent, certaines extensions n'ont pas encore d'équivalent côté FluentCart. Teste d'abord la version gratuite en parallèle avant de migrer."),
]

pane_ids = ["2967212_bacbe3-1b", "2967212_d1a0d9-a2", "2967212_0c31f9-77", "2967212_271143-6e", "2967212_c7c195-fa", "2967212_9a3f12-mg"]

def pane(idx, qid, q, a):
    attr = '{"uniqueID":"%s"}' % qid if idx == 1 else '{"id":%d,"uniqueID":"%s"}' % (idx, qid)
    return ('<!-- wp:kadence/pane %s -->\n'
            '<div class="wp-block-kadence-pane kt-accordion-pane kt-accordion-pane-%d kt-pane%s"><div class="kt-accordion-header-wrap">'
            '<button class="kt-blocks-accordion-header kt-acccordion-button-label-show" type="button">'
            '<span class="kt-blocks-accordion-title-wrap"><span class="kt-blocks-accordion-title">%s</span></span>'
            '<span class="kt-blocks-accordion-icon-trigger"></span></button></div>'
            '<div class="kt-accordion-panel"><div class="kt-accordion-panel-inner"><!-- wp:paragraph -->\n'
            '<p>%s</p>\n<!-- /wp:paragraph --></div></div></div>\n'
            '<!-- /wp:kadence/pane -->') % (attr, idx, qid, q, a)

def accordion(accid, panes):
    inner = "\n\n".join(panes)
    return ('<!-- wp:kadence/accordion {"uniqueID":"%s","paneCount":3,%s} -->\n'
            '<div class="wp-block-kadence-accordion alignnone"><div class="kt-accordion-wrap kt-accordion-id%s kt-accordion-has-3-panes kt-active-pane-0 kt-accordion-block kt-pane-header-alignment-left kt-accodion-icon-style-arrow kt-accodion-icon-side-left" style="max-width:none">'
            '<div class="kt-accordion-inner-wrap" data-allow-multiple-open="true" data-start-open="none">%s</div></div></div>\n'
            '<!-- /wp:kadence/accordion -->') % (accid, ACC_ATTRS, accid, inner)

acc1 = accordion("2967212_5f8743-f6", [pane(i + 1, pane_ids[i], html.escape(qa[i][0]), html.escape(qa[i][1])) for i in range(3)])
acc2 = accordion("2967212_c20c6b-d7", [pane(i + 1, pane_ids[i + 3], html.escape(qa[i + 3][0]), html.escape(qa[i + 3][1])) for i in range(3)])

col1 = ('<!-- wp:kadence/column {"borderWidth":["","","",""],"uniqueID":"2967212_89d7d1-8f","kbVersion":2,"className":"inner-column-1"} -->\n'
        '<div class="wp-block-kadence-column kadence-column2967212_89d7d1-8f inner-column-1"><div class="kt-inside-inner-col">%s</div></div>\n'
        '<!-- /wp:kadence/column -->') % acc1
col2 = ('<!-- wp:kadence/column {"id":2,"borderWidth":["","","",""],"uniqueID":"2967212_86e59a-24","kbVersion":2,"className":"inner-column-2"} -->\n'
        '<div class="wp-block-kadence-column kadence-column2967212_86e59a-24 inner-column-2"><div class="kt-inside-inner-col">%s</div></div>\n'
        '<!-- /wp:kadence/column -->') % acc2

h2 = ('<!-- wp:kadence/advancedheading {"uniqueID":"2967212_f02e79-dc","sizeType":"rem","fontWeight":"800","margin":["","","xxs",""],"fontSize":["xl","",null],"fontHeight":[1.2,"",""]} -->\n'
      '<h2 class="kt-adv-heading2967212_f02e79-dc wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading2967212_f02e79-dc">Questions fréquentes</h2>\n'
      '<!-- /wp:kadence/advancedheading -->')
sub = ('<!-- wp:kadence/advancedheading {"uniqueID":"2967212_10d620-7f","margin":["","","md",""],"marginType":"em","htmlTag":"p","fontSize":["md","",""]} -->\n'
       '<p class="kt-adv-heading2967212_10d620-7f wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading2967212_10d620-7f">Les réponses aux questions que tu te poses avant de choisir.</p>\n'
       '<!-- /wp:kadence/advancedheading -->')
row = ('<!-- wp:kadence/rowlayout {"uniqueID":"2967212_1c1fbe-93","collapseGutter":"custom","customRowGutter":[10,"",""],"colLayout":"equal","padding":[0,"",0,""],"kbVersion":2} -->\n'
       '%s\n\n%s\n'
       '<!-- /wp:kadence/rowlayout -->') % (col1, col2)
faq = "\n\n".join([h2, sub, row])
open(".tmp-faq-kadence.html", "w", encoding="utf-8").write(faq)

print("CSV1 rows:", len(t1["rows"]), "| CSV2 rows:", len(t2["rows"]))
print("FAQ chars:", len(faq), "| panes:", faq.count("wp:kadence/pane") // 2, "| accordions:", faq.count("wp:kadence/accordion") // 2)
print("FAQ wp open/close:", faq.count("<!-- wp:"), faq.count("<!-- /wp:"))
