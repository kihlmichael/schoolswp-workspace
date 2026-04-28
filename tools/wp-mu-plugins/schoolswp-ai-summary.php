<?php
/**
 * Plugin Name: schoolsWP - Boutons resumer avec IA
 * Description: Affiche une rangee de boutons (ChatGPT, Perplexity, Claude, Mistral, Grok) qui ouvrent l'IA choisie avec un prompt pre-rempli demandant un resume de l'article courant. Multilingue Polylang (FR + EN). Zero appel API, zero stockage. Shortcode [swp_ai_summary]. Auto-injection scoped FR active par defaut.
 * Author: schoolsWP
 * Version: 2.1.0
 * License: GPL-2.0-or-later
 */

if (!defined('ABSPATH')) {
    exit;
}

define('SWP_AI_SUMMARY_VERSION', '2.1.0');

/**
 * Detecte la langue du post via Polylang. Fallback sur la locale du site.
 * Retourne un code 2 lettres en lowercase (fr, en, ...).
 */
function swp_ai_summary_get_lang($post_id)
{
    if (function_exists('pll_get_post_language')) {
        $lang = pll_get_post_language((int) $post_id);
        if ($lang) {
            return strtolower((string) $lang);
        }
    }
    return strtolower(substr((string) get_locale(), 0, 2));
}

/**
 * Strings UI + prompt par langue. Filtrable via `swp_ai_summary_strings`
 * pour ajouter ES/IT/PT/etc. sans toucher au mu-plugin.
 *
 * @param string $lang Code 2 lettres.
 * @return array{title_q:string, title_c:string, aria_aside:string, aria_pill:string, prompt:string}
 */
function swp_ai_summary_strings($lang = 'fr')
{
    $strings = array(
        'fr' => array(
            'title_q'    => 'Pas le temps&#8201;?',
            'title_c'    => 'Faites-le r&eacute;sumer par l\'IA',
            'aria_aside' => 'Resumer cet article avec une IA',
            'aria_pill'  => 'Resumer cet article avec %s',
            'prompt'     => 'Lis cet article schoolsWP intitule "%1$s" puis donne-moi un resume clair en 5 points cles, en francais : %2$s',
        ),
        'en' => array(
            'title_q'    => 'No time?',
            'title_c'    => 'Get an AI summary',
            'aria_aside' => 'Summarize this article with AI',
            'aria_pill'  => 'Summarize this article with %s',
            'prompt'     => 'Read this schoolsWP article titled "%1$s" and give me a clear summary in 5 key points, in English: %2$s',
        ),
    );

    $filtered = apply_filters('swp_ai_summary_strings', $strings);
    if (!is_array($filtered)) {
        $filtered = $strings;
    }
    $lang = is_string($lang) ? strtolower($lang) : 'fr';

    if (isset($filtered[$lang])) {
        return $filtered[$lang];
    }
    return $filtered['fr'];
}

/**
 * Liste des LLMs supportes : nom, host, URL pattern (avec %s) et icone SVG.
 * Filtrable via `swp_ai_summary_llms`.
 *
 * @return array<int, array{name:string, host:string, url_pattern:string, icon:string}>
 */
function swp_ai_summary_llms()
{
    $llms = array(
        array(
            'name'        => 'ChatGPT',
            'host'        => 'chatgpt.com',
            'url_pattern' => 'https://chatgpt.com/?q=%s',
            'icon'        => '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21.55 10.04a5.42 5.42 0 0 0-.47-4.45 5.48 5.48 0 0 0-5.9-2.63 5.5 5.5 0 0 0-9.41 1.97 5.42 5.42 0 0 0-3.62 2.63 5.48 5.48 0 0 0 .67 6.43 5.42 5.42 0 0 0 .46 4.45 5.48 5.48 0 0 0 5.91 2.63 5.5 5.5 0 0 0 9.41-1.97 5.42 5.42 0 0 0 3.62-2.63 5.48 5.48 0 0 0-.67-6.43Zm-8.18 11.42a4.06 4.06 0 0 1-2.6-.95l.13-.07 4.33-2.5a.7.7 0 0 0 .36-.62v-6.1l1.83 1.06a.06.06 0 0 1 .03.05v5.06a4.08 4.08 0 0 1-4.08 4.07Zm-8.76-3.74a4.05 4.05 0 0 1-.48-2.73l.12.08 4.33 2.5a.7.7 0 0 0 .71 0l5.3-3.05v2.11a.07.07 0 0 1-.03.06l-4.38 2.52a4.07 4.07 0 0 1-5.57-1.49Zm-1.14-9.43a4.07 4.07 0 0 1 2.14-1.79V11.5a.7.7 0 0 0 .35.61l5.27 3.04-1.84 1.06a.07.07 0 0 1-.06 0l-4.38-2.53a4.08 4.08 0 0 1-1.48-5.39Zm15.04 3.5-5.3-3.07 1.84-1.06a.07.07 0 0 1 .06 0l4.38 2.53a4.07 4.07 0 0 1-.61 7.34v-5.14a.72.72 0 0 0-.37-.61Zm1.83-2.74-.13-.07-4.33-2.52a.7.7 0 0 0-.71 0l-5.3 3.05V7.4a.06.06 0 0 1 .03-.06l4.38-2.52a4.08 4.08 0 0 1 6.06 4.22Zm-11.45 3.74-1.83-1.05a.07.07 0 0 1-.04-.05V6.62a4.08 4.08 0 0 1 6.69-3.13l-.13.07-4.33 2.5a.7.7 0 0 0-.36.62Z"/></svg>',
        ),
        array(
            'name'        => 'Perplexity',
            'host'        => 'perplexity.ai',
            'url_pattern' => 'https://www.perplexity.ai/search?q=%s',
            'icon'        => '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 1.5 13.6 9 19.5 4.7 16.2 10.5 22.5 12 16.2 13.5 19.5 19.3 13.6 15 12 22.5 10.4 15 4.5 19.3 7.8 13.5 1.5 12 7.8 10.5 4.5 4.7 10.4 9Z"/></svg>',
        ),
        array(
            'name'        => 'Claude',
            'host'        => 'claude.ai',
            'url_pattern' => 'https://claude.ai/new?q=%s',
            'icon'        => '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2c-.5 0-1 1.7-1.5 4.7-1-2.3-2-3.6-2.8-3.2-.7.4 0 2.5 1.4 4.8C6.6 7.5 4.5 7.2 4 7.9c-.4.6 1.4 1.7 4 2.4-2.6.7-4.4 1.8-4 2.4.5.7 2.6.4 5.1-.3-1.4 2.3-2.1 4.4-1.4 4.8.8.4 1.8-.9 2.8-3.2.5 3 1 4.7 1.5 4.7s1-1.7 1.5-4.7c1 2.3 2 3.6 2.8 3.2.7-.4 0-2.5-1.4-4.8 2.5.7 4.6 1 5.1.3.4-.6-1.4-1.7-4-2.4 2.6-.7 4.4-1.8 4-2.4-.5-.7-2.6-.4-5.1.3 1.4-2.3 2.1-4.4 1.4-4.8-.8-.4-1.8.9-2.8 3.2C13 3.7 12.5 2 12 2Z"/></svg>',
        ),
        array(
            'name'        => 'Mistral',
            'host'        => 'mistral.ai',
            'url_pattern' => 'https://chat.mistral.ai/chat?q=%s',
            'icon'        => '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="8" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/><rect x="13" y="13" width="8" height="8" rx="1"/></svg>',
        ),
        array(
            'name'        => 'Grok',
            'host'        => 'grok.com',
            'url_pattern' => 'https://grok.com/?q=%s',
            'icon'        => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M5 5 L19 19 M19 5 L5 19"/></svg>',
        ),
    );

    $filtered = apply_filters('swp_ai_summary_llms', $llms);
    return is_array($filtered) ? $filtered : $llms;
}

/**
 * Construit le prompt envoye au LLM, dans la langue du post. Filtrable via `swp_ai_summary_prompt`.
 */
function swp_ai_summary_build_prompt($post_id)
{
    $url     = get_permalink($post_id);
    $title   = get_the_title($post_id);
    $lang    = swp_ai_summary_get_lang($post_id);
    $strings = swp_ai_summary_strings($lang);

    $default = sprintf(
        $strings['prompt'],
        wp_strip_all_tags((string) $title),
        (string) $url
    );

    $prompt = apply_filters('swp_ai_summary_prompt', $default, $post_id, $url, $title, $lang);
    return rawurlencode((string) $prompt);
}

/**
 * Rend le bloc HTML : titre + 5 pills LLM cliquables, dans la langue du post.
 */
function swp_ai_summary_render($post_id = null)
{
    $post_id = $post_id ? (int) $post_id : (int) get_the_ID();
    if (!$post_id) {
        return '';
    }
    $url = get_permalink($post_id);
    if (!$url) {
        return '';
    }

    $lang    = swp_ai_summary_get_lang($post_id);
    $strings = swp_ai_summary_strings($lang);
    $encoded = swp_ai_summary_build_prompt($post_id);
    $llms    = swp_ai_summary_llms();
    if (empty($llms)) {
        return '';
    }

    ob_start();
    ?>
    <aside class="swp-ai-summary" data-swp-ai-summary lang="<?php echo esc_attr($lang); ?>" aria-label="<?php echo esc_attr($strings['aria_aside']); ?>">
        <p class="swp-ai-summary__title">
            <span class="swp-ai-summary__title-q"><?php echo $strings['title_q']; // Entites HTML controlees dev. ?></span>
            <span class="swp-ai-summary__title-c"><?php echo $strings['title_c']; ?></span>
        </p>
        <ul class="swp-ai-summary__pills">
            <?php foreach ($llms as $llm) :
                if (empty($llm['name']) || empty($llm['url_pattern']) || empty($llm['icon'])) {
                    continue;
                }
                $href = sprintf($llm['url_pattern'], $encoded);
                $slug = sanitize_title($llm['name']);
                ?>
                <li class="swp-ai-summary__item">
                    <a class="swp-ai-summary__pill"
                       href="<?php echo esc_url($href); ?>"
                       target="_blank"
                       rel="noopener noreferrer nofollow"
                       data-llm="<?php echo esc_attr($slug); ?>"
                       aria-label="<?php echo esc_attr(sprintf($strings['aria_pill'], $llm['name'])); ?>">
                        <span class="swp-ai-summary__pill-icon" aria-hidden="true"><?php echo $llm['icon']; // SVG hardcode. ?></span>
                        <span class="swp-ai-summary__pill-name"><?php echo esc_html($llm['name']); ?></span>
                    </a>
                </li>
            <?php endforeach; ?>
        </ul>
    </aside>
    <?php
    return (string) ob_get_clean();
}

/**
 * Shortcode [swp_ai_summary id="123"]. Sans argument, utilise le post courant.
 */
function swp_ai_summary_shortcode($atts)
{
    $atts = shortcode_atts(array('id' => 0), $atts, 'swp_ai_summary');
    return swp_ai_summary_render((int) $atts['id']);
}
add_shortcode('swp_ai_summary', 'swp_ai_summary_shortcode');

/**
 * CSS inline (~1.5 Ko, footer, imprime une fois).
 */
function swp_ai_summary_assets()
{
    if (is_admin()) {
        return;
    }
    static $printed = false;
    if ($printed) {
        return;
    }
    $printed = true;
    ?>
    <style id="swp-ai-summary-css">
    .swp-ai-summary{margin:1.6em 0;padding:1.2em 1.3em;border-radius:14px;background:linear-gradient(135deg,#1e293b,#12111F);color:#f8fafc;box-shadow:0 8px 24px -12px rgba(15,23,42,.35);position:relative;overflow:hidden}
    .swp-ai-summary::before{content:"";position:absolute;inset:auto -50px -70px auto;width:220px;height:220px;background:radial-gradient(circle,rgba(0,212,0,.18) 0%,rgba(0,212,0,0) 65%);pointer-events:none;z-index:0}
    .swp-ai-summary__title{margin:0 0 .9em;font-size:.78em;letter-spacing:.08em;text-transform:uppercase;font-weight:700;line-height:1.4;position:relative;z-index:1}
    .swp-ai-summary__title-q{color:#8F8DA5}
    .swp-ai-summary__title-c{color:#00D400;margin-left:.4em}
    .swp-ai-summary__pills{display:flex;flex-wrap:wrap;gap:.55em;list-style:none;margin:0;padding:0;position:relative;z-index:1}
    .swp-ai-summary__item{margin:0;padding:0}
    .swp-ai-summary__pill{display:inline-flex;align-items:center;gap:.55em;padding:.5em 1em .5em .5em;border-radius:999px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);color:#f8fafc;text-decoration:none;font-size:.92em;font-weight:600;line-height:1;transition:transform .15s ease,background .15s ease,border-color .15s ease,box-shadow .15s ease}
    .swp-ai-summary__pill:hover{background:rgba(0,212,0,.12);border-color:rgba(0,212,0,.55);color:#fff;transform:translateY(-1px);box-shadow:0 4px 14px -4px rgba(0,212,0,.45)}
    .swp-ai-summary__pill:focus-visible{outline:2px solid #00D400;outline-offset:2px}
    .swp-ai-summary__pill-icon{display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;width:1.7em;height:1.7em;border-radius:50%;background:rgba(255,255,255,.1);color:#fff;transition:background .15s ease,color .15s ease}
    .swp-ai-summary__pill-icon svg{width:1em;height:1em;display:block}
    .swp-ai-summary__pill:hover .swp-ai-summary__pill-icon{background:linear-gradient(135deg,#00D400,#00A100);color:#12111F}
    @media (max-width:560px){
        .swp-ai-summary{padding:1em 1.1em}
        .swp-ai-summary__title{font-size:.72em}
        .swp-ai-summary__pill{font-size:.88em;padding:.45em .85em .45em .45em}
        .swp-ai-summary__pill-icon{width:1.55em;height:1.55em}
    }
    @media (prefers-reduced-motion:reduce){
        .swp-ai-summary__pill,.swp-ai-summary__pill-icon{transition:none}
        .swp-ai-summary__pill:hover{transform:none}
    }
    </style>
    <?php
}
add_action('wp_footer', 'swp_ai_summary_assets');

/**
 * Langues acceptees par l'auto-injection. Defaut : FR uniquement.
 * Pour activer EN : add_filter('swp_ai_summary_auto_inject_langs', fn() => ['fr', 'en']);
 * Pour desactiver totalement : add_filter('swp_ai_summary_auto_inject_langs', '__return_empty_array');
 */
function swp_ai_summary_auto_inject_langs()
{
    return apply_filters('swp_ai_summary_auto_inject_langs', array('fr'));
}

/**
 * Auto-injection sur single posts :
 * - Filtree par langue Polylang (defaut FR).
 * - Skip si le shortcode est deja place manuellement (placement custom prioritaire).
 * - Insertion juste avant le premier H2 (block Gutenberg ou tag), prepend au top sinon.
 * - Pour exclure une categorie : has_category(['slug'], get_the_ID()) dans le filtre swp_ai_summary_skip.
 */
add_filter('the_content', 'swp_ai_summary_auto_inject', 5);
function swp_ai_summary_auto_inject($content)
{
    if (!is_singular('post') || !is_main_query() || !in_the_loop()) {
        return $content;
    }

    $post_id = (int) get_the_ID();
    if (!$post_id) {
        return $content;
    }

    // Echappatoire utilisateur (filtre booleen)
    if (apply_filters('swp_ai_summary_skip', false, $post_id)) {
        return $content;
    }

    // Scope langue (Polylang ou locale fallback)
    $allowed = swp_ai_summary_auto_inject_langs();
    if (!empty($allowed) && is_array($allowed)) {
        $lang = swp_ai_summary_get_lang($post_id);
        if (!in_array($lang, $allowed, true)) {
            return $content;
        }
    } elseif (is_array($allowed) && empty($allowed)) {
        // Tableau vide explicite : auto-injection desactivee
        return $content;
    }

    // Dedupe : shortcode deja place manuellement
    if (strpos($content, '[swp_ai_summary]') !== false) {
        return $content;
    }

    $block = swp_ai_summary_render($post_id);
    if ($block === '') {
        return $content;
    }

    // Insertion avant le premier H2 (Gutenberg block, sinon tag direct, sinon top)
    $pos = strpos($content, '<!-- wp:heading');
    if ($pos === false) {
        $pos = stripos($content, '<h2');
    }
    if ($pos === false) {
        return $block . $content;
    }
    return substr($content, 0, $pos) . $block . substr($content, $pos);
}
