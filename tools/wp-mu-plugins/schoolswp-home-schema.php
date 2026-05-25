<?php
/**
 * Plugin Name: schoolsWP Home Schema
 * Description: Injecte un JSON-LD enrichi sur la home (FR + EN + DE) : Organization, WebSite avec SearchAction, BreadcrumbList, FAQPage. Complémentaire au mu-plugin schoolswp-person-schema (qui couvre Michaël KIHL en tant que personne).
 * Version: 1.0.2
 * Author: Michaël KIHL
 * License: GPLv2 or later
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Détecte si on est sur une home (FR, EN ou DE) Polylang.
 */
function schoolswp_home_schema_is_home_page() {
    if (is_front_page() && is_home()) {
        return true;
    }
    // Polylang : /en/ et /de/ ont leurs propres front pages
    if (function_exists('pll_current_language')) {
        global $wp;
        $current_url = home_url($wp->request);
        $home_urls = [
            home_url('/'),
            home_url('/en/'),
            home_url('/de/'),
        ];
        foreach ($home_urls as $home) {
            if (rtrim($current_url, '/') === rtrim($home, '/')) {
                return true;
            }
        }
    }
    return is_front_page();
}

/**
 * FAQ par langue. Filtrable via `schoolswp_home_schema_faq`.
 * Format : array<['question' => string, 'answer' => string]>
 *
 * Ces FAQs alimentent le bloc FAQPage du JSON-LD. Elles doivent rester pixel-perfect
 * cohérentes avec ce qui est visible dans la home (accordion Kadence), sinon Google
 * pénalise le rich snippet et n'affiche pas le résultat enrichi.
 */
function schoolswp_home_schema_faq($lang = 'fr') {
    $faq = [
        'fr' => [
            [
                'question' => 'Qu’est-ce que schoolsWP ?',
                'answer'   => 'schoolsWP est une plateforme de formations WordPress concrètes pour freelances, créateurs et solopreneurs. Michaël KIHL y partage des tutoriels, audits et méthodes pour créer des sites WordPress performants, automatisés et rentables.',
            ],
            [
                'question' => 'À qui s’adressent les formations schoolsWP ?',
                'answer'   => 'Aux freelances qui veulent vivre du web, aux solopreneurs qui automatisent leur business WordPress, et aux créateurs de contenu qui cherchent une stack pro sans tomber dans la dette technique.',
            ],
            [
                'question' => 'Quels piliers WordPress couvre schoolsWP ?',
                'answer'   => 'Six piliers : automatisation (Fluent stack, n8n, SureTriggers), SEO et GEO/AIO, performance et UX, monétisation (FluentCart, affiliations), formations en ligne (TutorLMS), sécurité et hébergement.',
            ],
            [
                'question' => 'Les formations schoolsWP sont-elles gratuites ?',
                'answer'   => 'Les articles, tutoriels et la newsletter sont gratuits. Les formations approfondies (modules vidéo, accompagnement, certifications) sont payantes via FluentCart et TutorLMS.',
            ],
            [
                'question' => 'Comment contacter Michaël KIHL ?',
                'answer'   => 'Par email à contact@michaelkihl.fr, sur LinkedIn (linkedin.com/in/michaelkihl/) ou via les boutons sociaux en bas de chaque article.',
            ],
            [
                'question' => 'Comment recevoir les nouveaux contenus schoolsWP ?',
                'answer'   => 'En t’abonnant à la newsletter via le bouton présent sur la home : tu reçois chaque semaine les nouveaux articles, audits et méthodes testées sur WordPress.',
            ],
        ],
        'en' => [
            [
                'question' => 'What is schoolsWP?',
                'answer'   => 'schoolsWP is a practical WordPress training platform for freelancers, creators and solopreneurs. Michaël KIHL shares tutorials, audits and methods to build WordPress sites that are fast, automated and profitable.',
            ],
            [
                'question' => 'Who are schoolsWP trainings for?',
                'answer'   => 'For freelancers who want to make a living from the web, solopreneurs automating their WordPress business, and content creators looking for a pro stack without falling into technical debt.',
            ],
            [
                'question' => 'Which WordPress pillars does schoolsWP cover?',
                'answer'   => 'Six pillars: automation (Fluent stack, n8n, SureTriggers), SEO and GEO/AIO, performance and UX, monetization (FluentCart, affiliates), online training (TutorLMS), security and hosting.',
            ],
            [
                'question' => 'Are schoolsWP trainings free?',
                'answer'   => 'Articles, tutorials and the newsletter are free. In-depth trainings (video modules, coaching, certifications) are paid via FluentCart and TutorLMS.',
            ],
            [
                'question' => 'How to contact Michaël KIHL?',
                'answer'   => 'By email at contact@michaelkihl.fr, on LinkedIn (linkedin.com/in/michaelkihl/) or via the social buttons at the bottom of each article.',
            ],
            [
                'question' => 'How to receive new schoolsWP content?',
                'answer'   => 'By subscribing to the newsletter via the button on the home page: you receive each week the new articles, audits and tested methods on WordPress.',
            ],
        ],
        'de' => [
            [
                'question' => 'Was ist schoolsWP?',
                'answer'   => 'schoolsWP ist eine praktische WordPress-Trainingsplattform für Freelancer, Kreative und Solopreneure. Michaël KIHL teilt Tutorials, Audits und Methoden, um schnelle, automatisierte und profitable WordPress-Seiten zu erstellen.',
            ],
            [
                'question' => 'Für wen sind die schoolsWP-Trainings gedacht?',
                'answer'   => 'Für Freelancer, die vom Web leben möchten, Solopreneure, die ihr WordPress-Geschäft automatisieren, und Content-Ersteller, die einen professionellen Stack ohne technische Schulden suchen.',
            ],
            [
                'question' => 'Welche WordPress-Säulen deckt schoolsWP ab?',
                'answer'   => 'Sechs Säulen: Automatisierung (Fluent stack, n8n, SureTriggers), SEO und GEO/AIO, Performance und UX, Monetarisierung (FluentCart, Affiliates), Online-Training (TutorLMS), Sicherheit und Hosting.',
            ],
            [
                'question' => 'Sind die schoolsWP-Trainings kostenlos?',
                'answer'   => 'Artikel, Tutorials und der Newsletter sind kostenlos. Tiefgehende Trainings (Video-Module, Coaching, Zertifizierungen) sind kostenpflichtig über FluentCart und TutorLMS.',
            ],
            [
                'question' => 'Wie kann man Michaël KIHL kontaktieren?',
                'answer'   => 'Per E-Mail an contact@michaelkihl.fr, auf LinkedIn (linkedin.com/in/michaelkihl/) oder über die Social-Buttons am Ende jedes Artikels.',
            ],
            [
                'question' => 'Wie erhält man neue schoolsWP-Inhalte?',
                'answer'   => 'Durch Abonnieren des Newsletters über den Button auf der Startseite: Du erhältst wöchentlich die neuen Artikel, Audits und getesteten Methoden zu WordPress.',
            ],
        ],
    ];

    $filtered = apply_filters('schoolswp_home_schema_faq', $faq);
    if (!is_array($filtered) || !isset($filtered[$lang])) {
        return $faq['fr'];
    }
    return $filtered[$lang];
}

/**
 * Détecte la langue de la page courante (Polylang).
 */
function schoolswp_home_schema_get_lang() {
    if (function_exists('pll_current_language')) {
        $lang = pll_current_language();
        if ($lang && in_array($lang, ['fr', 'en', 'de'], true)) {
            return $lang;
        }
    }
    return 'fr';
}

/**
 * Construit le JSON-LD complet : Organization + WebSite + BreadcrumbList + FAQPage.
 * Wrappe dans @graph pour Rank Math compatibility.
 */
function schoolswp_home_schema_build() {
    $lang = schoolswp_home_schema_get_lang();
    $home_url = home_url('/');
    $brand_name = 'schoolsWP';
    $logo_url = 'https://schoolswp.com/wp-content/uploads/2022/06/favicon-schoolswp.com-michaelkihl-50x50.png';

    // Localised home URL per language
    $localised_home = ($lang === 'fr') ? home_url('/') : home_url('/' . $lang . '/');

    $organization = [
        '@type'    => 'Organization',
        '@id'      => $home_url . '#organization',
        'name'     => $brand_name,
        'url'      => $home_url,
        'logo'     => [
            '@type' => 'ImageObject',
            'url'   => $logo_url,
        ],
        'sameAs'   => [
            'https://www.linkedin.com/in/michaelkihl/',
            'https://x.com/MichaelKihl',
            'https://www.youtube.com/@MichaelKihl',
            'https://www.facebook.com/KIHLMichael',
        ],
        'founder'  => [
            '@type' => 'Person',
            '@id'   => $home_url . '#person-michaelkihl',
            'name'  => 'Michaël KIHL',
        ],
        'contactPoint' => [
            '@type'       => 'ContactPoint',
            'email'       => 'contact@michaelkihl.fr',
            'contactType' => 'customer support',
            'areaServed'  => ['FR', 'BE', 'CH', 'CA', 'LU'],
            'availableLanguage' => ['French', 'English', 'German'],
        ],
    ];

    $website = [
        '@type'    => 'WebSite',
        '@id'      => $home_url . '#website',
        'url'      => $home_url,
        'name'     => $brand_name,
        'inLanguage' => $lang,
        'publisher' => ['@id' => $home_url . '#organization'],
        'potentialAction' => [
            '@type'  => 'SearchAction',
            'target' => [
                '@type'       => 'EntryPoint',
                'urlTemplate' => $home_url . '?s={search_term_string}',
            ],
            'query-input' => 'required name=search_term_string',
        ],
    ];

    $breadcrumb = [
        '@type' => 'BreadcrumbList',
        '@id'   => $localised_home . '#breadcrumb',
        'itemListElement' => [
            [
                '@type'    => 'ListItem',
                'position' => 1,
                'name'     => ($lang === 'fr') ? 'Accueil' : (($lang === 'de') ? 'Startseite' : 'Home'),
                'item'     => $localised_home,
            ],
        ],
    ];

    $faq_items = [];
    foreach (schoolswp_home_schema_faq($lang) as $idx => $qa) {
        $faq_items[] = [
            '@type'          => 'Question',
            'name'           => $qa['question'],
            'acceptedAnswer' => [
                '@type' => 'Answer',
                'text'  => $qa['answer'],
            ],
        ];
    }

    $faqpage = [
        '@type'      => 'FAQPage',
        '@id'        => $localised_home . '#faqpage',
        'mainEntity' => $faq_items,
    ];

    $graph = [
        '@context' => 'https://schema.org',
        '@graph'   => [$organization, $website, $breadcrumb, $faqpage],
    ];

    return apply_filters('schoolswp_home_schema_graph', $graph, $lang);
}

/**
 * Inject le JSON-LD dans le head sur les pages home uniquement.
 */
add_action('wp_head', 'schoolswp_home_schema_inject', 25);
function schoolswp_home_schema_inject() {
    if (!schoolswp_home_schema_is_home_page()) {
        return;
    }
    $graph = schoolswp_home_schema_build();
    echo "\n<script type=\"application/ld+json\" id=\"schoolswp-home-schema\">\n";
    echo wp_json_encode($graph, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
    echo "\n</script>\n";
}
