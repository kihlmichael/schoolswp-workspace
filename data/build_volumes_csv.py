import sys, csv
sys.stdout.reconfigure(encoding='utf-8')

volumes = {
    '5euros': 2400, 'flyingpress': 590, 'mailerpress': 90, 'suretriggers': 40, 'tastewp': 110,
    '5euros com': 6600, 'chatseo': 590, 'suremembers': 210, '5euros.com avis': 320,
    'wp rocket vs flying press': 10, 'taste wp': 30, 'flyingpress vs wp rocket': 260,
    'frank houbre': 50, '5 euros': 4400, '5euros.com': 6600, '5 euros.com': 390,
    'latepoint': 210, '5euro.com': 390, 'canva wordpress': 170, 'flying press vs wp rocket': 10,
    'thot seo': 1300, 'local by flywheel': 390, 'metricool gratuit': 390, 'fluent crm': 390,
    'befreelancr': 480, 'localwp vs xampp': 10, 'wp rocket vs flyingpress': 140,
    'learndash': 590, 'thruuu': 320, 'buddyboss': 480, 'divi pixel': 480, 'tutor lms': 720,
    'amelia wp': 140, 'link whisper wordpress plugin': 10, 'fluentcrm': 390,
    'amelia booking': 320, 'skoatch': 390, 'tutorlms': 720, 'divi machine': 170,
    'elementskit': 320, 'armember': 30, 'latepoint plugin': 10, 'playground wordpress': 40,
    'instawp alternative': 10, 'tutor lms reviews': 10, 'funnelkit': 140,
    'elementor vs divi': 260, 'linkfinder': 880, 'espace membre wordpress': 50,
    'alidropship': 210, 'droip': 40500, 'amelia wordpress francais': 10, 'wp rocket test': 10,
    'crocoblock lifetime deal': 10, 'theme kadence': 40, 'restrict content pro': 70,
    'wplingua': 40, 'barn2': 20, 'amelia reservation': 140, 'slug seo': 110,
    'traducteur wordpress': 260, 'launchflows vs cartflows': 140, 'cartflows': 210,
    'o2switch avis': 590, 'wordpress referencement': 880, 'tunnel de vente wordpress': 170,
    'theme divi': 50, 'zipwp': 0, '5 euro.com': 390, '5euros.com site': 320,
    'pierre eliott lallemant': 30, 'wpboutik': 0, 'skeall': 140, 'o2switch': 33100,
    'zip wp': 0, 'clickwhale': 0, 'kadence': 720, 'localwp': 1600, 'fluent smtp': 40,
    'amelia booking plugin': 10, '5euros com avis': 320, 'zip wp wordpress': 0,
    'divi bodycommerce': 10, 'flyingpress plugin': 10, 'surecart wordpress': 10,
    'suremembers plugin': 10, 'flyingpress vs wprocket': 0, 'fluentcart': 0,
    'fluentbooking': 0, 'thruuu website text extractor': 0, 'tutor lms review': 10,
    'linksclub': 260, 'instawp': 320, '5 euros com': 390,
    'link whisper premium wordpress plugin': 10, 'bit flows': 0,
    'cinq euros.com': 50, 'wp zip': 170, 'fluentcommunity avis': 0, '5 euros microservice': 170,
    'prix metricool': 0, 'wishlist member wordpress': 10, 'fluentcrm coupon': 0,
    'wordpress canva': 140, 'fluentbooking wordpress': 0, 'frank houbre avis': 10,
    'logiciel local': 20, 'suretriggers wordpress plugin': 0, 'suretriggers plugin': 0,
    'metricool pricing euro': 0, 'wordpress kadence blocks': 10, 'comparateur de serp': 0,
    'buddyboss vs buddypress': 10, 'wp ninja tables': 140, 'fluent form woocommerce': 10,
    'surecart vs fluentcart': 0, 'skoatch avis': 0, 'slug seo wordpress': 10,
    'metricool starter plan price': 0, 'thotseo': 0, 'metricool': 18100, 'seo wordpress': 720,
    'avis chatseo': 0, 'linkuma': 3600, 'outil seo tout-en-un': 40,
    'amelia wordpress booking plugin pricing': 0, 'link whisper': 590,
    'maintenance site wordpress': 590, 'wordpress academy': 10, 'ameliawp': 140,
    'wishlist member': 390, 'solid affiliate': 10, 'learndash review': 10,
    'avis skoatch': 0, 'wordpress multisite': 320, 'perfmatters': 170, 'fluent forms': 390,
    'wordpress sur mesure': 0, 'metricool free plan features': 0, 'kadence theme wordpress': 70,
    'linkuma tarif': 0, 'linkuma avis': 1600, 'is metricool free': 10, 'lms wordpress': 90,
    'launchflows review': 0, 'kadence theme': 140, 'linksgarden avis': 30,
    'systeme.io pricing 2026': 0, 'localwp review': 10, 'latepoint wordpress': 30,
    'amelia vs bookly': 140, 'cloudflare apo vs wp rocket': 10, 'seo slug': 10,
    'amelia pricing': 10, 'wordpress multilingual plugins': 50, 'multi sites wordpress': 320,
    'best wordpress plugin for internal linking': 0, 'metricool pricing plans': 0,
    'nettoyage wordpress': 20, 'xampp vs localwp': 0, 'local wordpress': 720,
    'fluentcart vs woocommerce': 0, 'local flywheel': 70, 'zipwp alternative': 0,
    'metricool free trial': 10, 'metricool pricing free plan': 0, 'thruuu seo': 10,
    'wp rocket': 2900, 'traduction plugin wordpress': 30,
    'meilleur plugin de traduction wordpress': 20, 'suretriggers vs zapier': 0,
    'crocoblock membership': 10, 'crocoblock lifetime': 10, 'wordpress translation plugin': 110,
    'wordpress kadence': 40, 'elementskit lite': 30, 'metricool free plan limitations': 0,
    'referencement wordpress': 480, 'wp seo ninja review': 0, 'plugin wordpress divi': 170,
    'mise a jour wordpress': 20, 'theme divi wp': 480, 'gutenberg wordpress': 590,
    'seo wp': 10, 'multisite wordpress': 320, 'evidencewp': 0, 'fluent form': 390,
    'plugin langue wordpress': 30, 'aio seo': 70, 'wp seo': 30, 'local wp avis': 0,
    'wishlist members': 390, 'link whisper wordpress internal linking plugin': 0,
    'buddyboss review': 10, 'outil seo tout en un': 40, 'wp seo ninja reviews': 0,
    'avis copilhost': 0, 'plugin de traduction wordpress': 30, 'suremembers review': 10,
    'pretty links alternative': 10, 'traduction site wordpress': 170,
    'maintenance corrective wordpress': 10, 'latepoint review': 0, 'learn dash': 590,
    'seo free wordpress': 10, 'affiliatewp review': 10, 'wp theme divi': 480,
    'frank houbre formation': 10, 'wp rocket alternative': 10, 'crocoblock pricing': 10,
    'thruuu pricing': 10, 'learndash pricing': 10, 'learndash price': 10, 'learndash cost': 0,
    'all in one seo for wordpress': 140, 'all in one seo woocommerce': 10, 'wordpress 6.9': 260,
    'all in one seo pack': 30, 'wordpress lms reviews': 0, 'wordpress gutenberg': 390,
    'rank math seo': 880, 'seo for wordpress': 720, 'wordpress language translation': 10,
    'wp auto translate': 0, 'creer une plateforme de formation en ligne': 0,
    'affiliatewp reviews': 10, 'multi site wordpress': 320, 'plugin traduction': 320,
    'maintenance preventive wordpress': 0, 'wp rocket avis': 20, 'divi pixels': 480,
    'amelia booking plugin pricing 2026': 0, 'easyhoster': 320, 'fluent smtp vs wp mail smtp': 10,
    'alidropship premium store': 10, 'wordpress outils seo': 0, 'cartflows alternatives': 10,
    'maintenance site wordpress professionnel': 0, 'prestoplayer': 10,
    'link whisper wordpress internal linking plugin features': 0, 'localwp deutsch': 0,
    'buddyboss wordpress': 10, 'creer plateforme formation wordpress': 0,
    'what is crocoblock': 10, 'what is wordpress playground': 0, 'alidropship plugin reviews': 0,
    'wordpress 6.9 field guide': 0, 'wordpress all in one seo': 140, 'wp rocket vs': 10,
    'freelance netlinking': 0, 'wordpress clean database': 20, 'instawp.com': 10,
    'rapyd cloud': 0, 'tarif metricool': 0, 'thot seo prix': 0, 'seokey wordpress': 0,
    '5euro.com site': 110, 'chatseo avis': 0, 'fluent support': 0, 'kadence wordpress': 110,
    'copilhost': 0, 'tutor lms wordpress': 20, 'zipwp avis': 0, 'academy lms': 30,
    'pulse browser avis': 0, 'cinq euros': 320, 'link whisper wordpress': 10,
    'microthemer': 110, 'fluent cart': 0, 'metricool app': 10, 'suretrigger': 10,
    'mailerpress pro': 0, 'woocommerce alternative': 10, 'sure triggers': 10,
    'avis flyingpress': 0, 'flyingpress free version': 0, 'amelia plugin': 170,
    'netlinking platform': 0, 'metricool pricing 2024': 0, 'metricool review': 10,
    'metricool free plan': 10, 'wordpress translation plugins': 110, 'wp amelia': 90,
    'sureforms': 70, 'tastewp.com': 10, 'slug wordpress': 110, 'optimisation seo wordpress': 390,
    'latepoint alternatives': 0, 'fluent booking': 0, 'espace membres wordpress': 50,
    'o2switch price': 0, 'meilleur plugin traduction wordpress': 20, 'metricool pricing': 40,
    'avis thot seo': 0, 'perfmatters review': 10, 'rapyd cloud discount code': 0,
    'outils seo wordpress': 10, 'divipixel': 480, 'launchflows': 10,
    'securite maintenance wordpress': 0, 'nettoyage site wordpress': 0,
    'clean wordpress database': 10, 'divi theme wp': 480, 'wordpress maintenance': 1300,
    'sureform': 70, 'crocoblock discount': 10, 'alo seo': 10, 'learndash lms wordpress': 10,
    'learndash avis': 10, 'thot seo avis': 0, 'social ninja': 140, 'seo slugs': 10,
    'amelia booking wordpress pricing': 0, 'amelia plugin wordpress': 30, 'plugin divi': 320,
    'pourquoi utiliser wordpress multisite': 0, 'wp social ninja pricing': 0,
    'tastewp login': 0, 'sure cart': 10, 'amelia packages': 10, 'all in one seo plugin': 10,
    'woofunnels vs cartflows': 10, 'clean up database wordpress': 20, 'metricool rating': 0,
    'academy lms pro': 0, 'lms tutor': 10, 'seo for all': 170, 'wordpress espace membre': 50,
    'avis lws': 590, 'surecart review': 10, 'seo gratuit wordpress': 10,
    'clean up wordpress database': 20, 'seo in wordpress': 720, 'what are slugs in wordpress': 10,
    'amelia': 9900, 'getresponse email automatisation': 0, 'wordpress amelia': 30,
    'alidropship plugin review': 0, 'prix divi wordpress': 10, 'wordpress divi': 210,
    'amelia vs bookly comparison': 0, 'theme wp': 880, 'barn2 plugins': 10,
    'wordpress 6.9 review': 0, 'seo wordpress site': 50, 'aioseo': 170, 'seokey': 590,
    'wordpress mitgliederverwaltung': 0,
    # French accented variants
    'amelia wordpress francais': 10,
    'amelia reservation': 140,
    'amelia wordpress \u00e9': 10,
}

# Read the raw CSV
with open('d:/VS Code/CLAUDE CODE/projects/schoolswp/data/requetes_raw.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = list(reader.fieldnames)

print(f'Rows: {len(rows)}')
print(f'Columns: {fieldnames}')

# Build output
out_rows = []
matched = 0
for row in rows:
    kw_orig = row.get('Requetes les plus frequentes', row.get('Requ\u00eates les plus fr\u00e9quentes', '')).strip()
    # Try both column names
    for col in fieldnames:
        if 'Requ' in col:
            kw_orig = row[col].strip()
            break
    kw = kw_orig.lower()
    # normalize accents for lookup
    import unicodedata
    kw_norm = ''.join(c for c in unicodedata.normalize('NFD', kw) if unicodedata.category(c) != 'Mn')
    vol = volumes.get(kw, volumes.get(kw_norm, 0))
    if vol > 0:
        matched += 1
    row['Volume de recherche'] = vol
    out_rows.append(row)

print(f'Matched with volume > 0: {matched} / {len(rows)}')

# Write output
out_fields = fieldnames + ['Volume de recherche']
with open('d:/VS Code/CLAUDE CODE/projects/schoolswp/data/requetes_avec_volumes.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=out_fields)
    writer.writeheader()
    writer.writerows(out_rows)

print('Done! Saved to data/requetes_avec_volumes.csv')
print('\nTop 10 by volume:')
sorted_rows = sorted(out_rows, key=lambda r: int(r['Volume de recherche']), reverse=True)
for r in sorted_rows[:10]:
    for col in fieldnames:
        if 'Requ' in col:
            print(f"  {r[col]}: {r['Volume de recherche']}")
            break
