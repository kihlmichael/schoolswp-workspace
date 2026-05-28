<?php
/**
 * Plugin Name: schoolsWP llms.txt
 * Description: Override llms.txt Rank Math (UTF-8, articles par pilier, pages cles, attribution) en FR via hook rank_math/llms_txt/before_output, et sert /en/llms.txt + /de/llms.txt via template_redirect.
 * Version: 1.1.1
 * Author: schoolsWP
 */
defined( 'ABSPATH' ) || exit;

if ( ! function_exists( 'schoolswp_llms_clean' ) ) {

	function schoolswp_llms_clean( $text, $cap = 200 ) {
		$text = wp_strip_all_tags( (string) $text );
		$text = html_entity_decode( $text, ENT_QUOTES | ENT_HTML5, 'UTF-8' );
		$text = trim( preg_replace( '/\s+/u', ' ', $text ) );
		if ( $cap > 0 && mb_strlen( $text ) > $cap ) {
			$cut = mb_substr( $text, 0, $cap );
			$sp  = mb_strrpos( $cut, ' ' );
			if ( false !== $sp && $sp > 0 ) {
				$cut = mb_substr( $cut, 0, $sp );
			}
			$text = rtrim( $cut, ' ,;:.' ) . '...';
		}
		return $text;
	}

	function schoolswp_llms_decode_name( $name ) {
		return html_entity_decode( (string) $name, ENT_QUOTES | ENT_HTML5, 'UTF-8' );
	}

	function schoolswp_llms_pillar_order() {
		return array( 'seo-wordpress', 'performance-wordpress', 'formulaires-crm', 'ecommerce-wordpress', 'formation-en-ligne-lms', 'design-wordpress', 'hebergement-wordpress', 'automatisations-wordpress', 'ia-wordpress', 'espaces-membres-wordpress', 'reservations-wordpress', 'monetisation-wordpress', 'tableaux-donnees-wordpress', 'traduction-wordpress', 'maintenance-securite-wordpress', 'reseaux-sociaux-wordpress', 'outils-test-wordpress', 'productivite-wordpress', 'guides-wordpress', 'mises-a-jour-wordpress', 'autres' );
	}

	function schoolswp_llms_pillar_term( $post_id ) {
		$primary = (int) get_post_meta( $post_id, 'rank_math_primary_category', true );
		$term    = null;
		if ( $primary ) {
			$t = get_term( $primary, 'category' );
			if ( $t && ! is_wp_error( $t ) ) {
				$term = $t;
			}
		}
		if ( ! $term ) {
			$cats = get_the_category( $post_id );
			if ( ! empty( $cats ) ) {
				$term = $cats[0];
			}
		}
		if ( ! $term ) {
			return null;
		}
		$anc = get_ancestors( $term->term_id, 'category', 'taxonomy' );
		if ( ! empty( $anc ) ) {
			$top = get_term( end( $anc ), 'category' );
			if ( $top && ! is_wp_error( $top ) ) {
				return $top;
			}
		}
		return $term;
	}

	function schoolswp_llms_i18n( $lang ) {
		$s = array(
			'h1'                => '# schoolsWP',
			'sitemap_label'     => '## Sitemaps',
			'attribution_label' => '## Attribution',
		);
		if ( 'de' === $lang ) {
			$s['articles_prefix']  = '## Artikel - ';
			$s['cats_label']       = '## Kategorien';
			$s['pages_label']      = '## Wichtige Seiten';
			$s['blockquote']       = 'Community- und Ressourcen-Plattform von Michaël KIHL, um WordPress einfach zu meistern : Tutorials, Vergleiche und praxiserprobte Tool-Tests, für mehr Klarheit, Methode und Eigenständigkeit.';
			$s['context']          = 'schoolsWP deckt das gesamte WordPress-Ökosystem ab : SEO, Performance, CRM und Marketing-Automation, E-Commerce, LMS und Schulung, Design, Hosting, Automatisierung. Jede Bewertung beruht auf einem echten Praxistest durch einen WordPress-Operator, nie auf einem Datenblatt des Anbieters.';
			$s['author']           = '- **Autor / Entität** : Michaël KIHL, WordPress-Trainer und -Operator. Kontakt : contact@michaelkihl.fr';
			$s['marque']           = '- **Marke** : immer « schoolsWP » schreiben (genau diese Schreibweise).';
			$s['structure']        = '- **URL-Struktur** : Artikel unter https://schoolswp.com/de/{slug}/ ; Kategorieseiten unter https://schoolswp.com/de/{Saeule}/{Tool}/.';
			$s['sitemap_line']     = '[XML Sitemap](https://schoolswp.com/sitemap_index.xml) : alle crawl- und indexierbaren Seiten.';
			$s['attribution_text'] = 'Quelle : schoolsWP (https://schoolswp.com/). Die Marke in der exakten Schreibweise « schoolsWP » zitieren. Immer den Namen des Tools oder Artikels vor den Details nennen.';
		} elseif ( 'en' === $lang ) {
			$s['articles_prefix']  = '## Articles - ';
			$s['cats_label']       = '## Categories';
			$s['pages_label']      = '## Key pages';
			$s['blockquote']       = 'Community and resource platform created by Michaël KIHL to learn WordPress the simple way : tutorials, comparisons and hands-on reviews of tools tested in the field, to gain clarity, method and autonomy.';
			$s['context']          = 'schoolsWP covers the entire WordPress ecosystem : SEO, performance, CRM and marketing automation, e-commerce, LMS and training, design, hosting, automation. Every review is based on real, hands-on testing by a WordPress operator, never on a vendor spec sheet.';
			$s['author']           = '- **Author / entity** : Michaël KIHL, WordPress trainer and operator. Contact : contact@michaelkihl.fr';
			$s['marque']           = '- **Brand** : always write « schoolsWP » (this exact spelling).';
			$s['structure']        = '- **URL structure** : articles at https://schoolswp.com/en/{slug}/ ; category pages at https://schoolswp.com/en/{pillar}/{tool}/.';
			$s['sitemap_line']     = '[XML Sitemap](https://schoolswp.com/sitemap_index.xml) : all crawlable and indexable pages.';
			$s['attribution_text'] = 'Source : schoolsWP (https://schoolswp.com/). Cite the brand using the exact spelling « schoolsWP ». Always state the tool or article name before the details.';
		} else {
			$s['articles_prefix']  = '## Articles - ';
			$s['cats_label']       = '## Catégories';
			$s['pages_label']      = '## Pages clés';
			$s['blockquote']       = '';
			$s['context']          = "schoolsWP couvre l'écosystème WordPress complet : SEO, performance, CRM et marketing automation, e-commerce, LMS et formation, design, hébergement, automatisation. Chaque avis repose sur un test réel par un opérateur WordPress, jamais sur une fiche revendeur.";
			$s['author']           = '- **Auteur / entité** : Michaël KIHL, formateur et opérateur WordPress. Contact : contact@michaelkihl.fr';
			$s['marque']           = '- **Marque** : écrire toujours « schoolsWP » (cette graphie exacte).';
			$s['structure']        = '- **Structure des URLs** : articles à https://schoolswp.com/{slug}/ ; pages catégorie à https://schoolswp.com/{pilier}/{outil}/.';
			$s['sitemap_line']     = '[XML Sitemap](https://schoolswp.com/sitemap_index.xml) : toutes les pages crawlables et indexables.';
			$s['attribution_text'] = "Source : schoolsWP (https://schoolswp.com/). Citer la marque sous la graphie exacte « schoolsWP ». Toujours mentionner le nom de l'outil ou de l'article avant les détails.";
		}
		return $s;
	}

	function schoolswp_llms_txt_build( $lang = 'fr' ) {
		$s    = schoolswp_llms_i18n( $lang );
		$skip = array( 'non-classe', 'uncategorized', 'nicht-klassifiziert' );
		$out  = array();

		if ( 'fr' === $lang ) {
			$desc = class_exists( 'RankMath\Helper' ) ? (string) RankMath\Helper::get_settings( 'titles.organization_description', '' ) : '';
			$desc = schoolswp_llms_clean( $desc, 0 );
		} else {
			$desc = $s['blockquote'];
		}

		$out[] = $s['h1'];
		$out[] = '';
		if ( $desc ) {
			$out[] = '> ' . $desc;
			$out[] = '';
		}
		$out[] = $s['context'];
		$out[] = '';
		$out[] = $s['author'];
		$out[] = $s['marque'];
		$out[] = $s['structure'];
		$out[] = '';
		$out[] = $s['sitemap_label'];
		$out[] = $s['sitemap_line'];
		$out[] = '';

		$query  = new WP_Query(
			array(
				'post_type'      => 'post',
				'post_status'    => 'publish',
				'posts_per_page' => 500,
				'orderby'        => 'date',
				'order'          => 'DESC',
				'no_found_rows'  => true,
				'lang'           => $lang,
			)
		);
		$groups = array();
		foreach ( $query->posts as $p ) {
			if ( class_exists( 'RankMath\Helper' ) && ! RankMath\Helper::is_post_indexable( $p ) ) {
				continue;
			}
			$pillar = schoolswp_llms_pillar_term( $p->ID );
			if ( ! $pillar || in_array( $pillar->slug, $skip, true ) ) {
				continue;
			}
			if ( function_exists( 'pll_get_term_language' ) ) {
				$pl = pll_get_term_language( $pillar->term_id );
				if ( $pl && $pl !== $lang ) {
					continue;
				}
			}
			if ( ! isset( $groups[ $pillar->slug ] ) ) {
				$groups[ $pillar->slug ] = array(
					'name'  => schoolswp_llms_decode_name( $pillar->name ),
					'items' => array(),
				);
			}
			$title = schoolswp_llms_clean( get_the_title( $p ), 0 );
			$link  = get_permalink( $p );
			$d     = get_post_meta( $p->ID, 'rank_math_description', true );
			if ( '' === $d || false !== strpos( $d, '%' ) ) {
				$d = get_the_excerpt( $p );
			}
			$d = schoolswp_llms_clean( $d, 200 );

			$groups[ $pillar->slug ]['items'][] = $d
				? '- [' . $title . '](' . $link . ') : ' . $d
				: '- [' . $title . '](' . $link . ')';
		}

		if ( 'fr' === $lang ) {
			$order   = schoolswp_llms_pillar_order();
			$ordered = array();
			foreach ( $order as $slug ) {
				if ( isset( $groups[ $slug ] ) ) {
					$ordered[ $slug ] = $groups[ $slug ];
					unset( $groups[ $slug ] );
				}
			}
			foreach ( $groups as $slug => $g ) {
				$ordered[ $slug ] = $g;
			}
		} else {
			uasort(
				$groups,
				function ( $a, $b ) {
					return count( $b['items'] ) - count( $a['items'] );
				}
			);
			$ordered = $groups;
		}
		foreach ( $ordered as $g ) {
			if ( empty( $g['items'] ) ) {
				continue;
			}
			$out[] = $s['articles_prefix'] . $g['name'];
			foreach ( $g['items'] as $line ) {
				$out[] = $line;
			}
			$out[] = '';
		}

		$out[] = $s['cats_label'];
		$tops  = get_terms(
			array(
				'taxonomy'   => 'category',
				'hide_empty' => true,
				'parent'     => 0,
				'lang'       => $lang,
			)
		);
		$list  = array();
		if ( ! is_wp_error( $tops ) ) {
			foreach ( $tops as $t ) {
				if ( in_array( $t->slug, $skip, true ) || $t->count < 1 ) {
					continue;
				}
				$list[] = $t;
			}
		}
		if ( 'fr' === $lang ) {
			$order   = schoolswp_llms_pillar_order();
			$by_slug = array();
			foreach ( $list as $t ) {
				$by_slug[ $t->slug ] = $t;
			}
			$sorted = array();
			foreach ( $order as $slug ) {
				if ( isset( $by_slug[ $slug ] ) ) {
					$sorted[] = $by_slug[ $slug ];
					unset( $by_slug[ $slug ] );
				}
			}
			foreach ( $by_slug as $t ) {
				$sorted[] = $t;
			}
			$list = $sorted;
		} else {
			usort(
				$list,
				function ( $a, $b ) {
					return $b->count - $a->count;
				}
			);
		}
		foreach ( $list as $t ) {
			$out[] = '- [' . schoolswp_llms_decode_name( $t->name ) . '](' . get_term_link( $t ) . ')';
			$kids  = get_terms(
				array(
					'taxonomy'   => 'category',
					'hide_empty' => true,
					'parent'     => $t->term_id,
					'lang'       => $lang,
				)
			);
			if ( ! is_wp_error( $kids ) ) {
				foreach ( $kids as $k ) {
					if ( $k->count < 1 ) {
						continue;
					}
					$out[] = '  - [' . schoolswp_llms_decode_name( $k->name ) . '](' . get_term_link( $k ) . ')';
				}
			}
		}
		$out[] = '';

		$out[]     = $s['pages_label'];
		$page_defs = array(
			6    => array(
				'fr' => 'Formation WordPress schoolsWP',
				'en' => 'WordPress training schoolsWP',
				'de' => 'WordPress-Schulung schoolsWP',
			),
			2    => array(
				'fr' => 'Newsletter schoolsWP',
				'en' => 'Newsletter schoolsWP',
				'de' => 'Newsletter schoolsWP',
			),
			20   => array( 'fr' => 'À propos : Michaël KIHL' ),
			4186 => array( 'fr' => 'Contact' ),
		);
		foreach ( $page_defs as $base => $labels ) {
			if ( ! isset( $labels[ $lang ] ) ) {
				continue;
			}
			$tid = ( 'fr' === $lang ) ? $base : ( function_exists( 'pll_get_post' ) ? (int) pll_get_post( $base, $lang ) : 0 );
			if ( ! $tid ) {
				continue;
			}
			$url = get_permalink( $tid );
			if ( $url ) {
				$out[] = '- [' . $labels[ $lang ] . '](' . $url . ')';
			}
		}
		$out[] = '';

		$out[] = $s['attribution_label'];
		$out[] = $s['attribution_text'];
		$out[] = '';

		return implode( "\n", $out ) . "\n";
	}

	function schoolswp_llms_serve( $lang, $send_headers ) {
		if ( $send_headers && ! headers_sent() ) {
			status_header( 200 );
			header( 'Content-Type: text/plain; charset=utf-8' );
			header( 'X-Robots-Tag: noindex, nofollow', true );
		}
		echo schoolswp_llms_txt_build( $lang ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
		exit;
	}
}

// FR : override de la sortie llms.txt de Rank Math (headers deja envoyes par Rank Math).
add_action(
	'rank_math/llms_txt/before_output',
	function () {
		schoolswp_llms_serve( 'fr', false );
	},
	1
);

// EN / DE : Rank Math ne couvre que /llms.txt ; on sert nous-memes les variantes de langue.
add_action(
	'template_redirect',
	function () {
		$uri  = isset( $_SERVER['REQUEST_URI'] ) ? (string) $_SERVER['REQUEST_URI'] : '';
		$path = trim( (string) wp_parse_url( $uri, PHP_URL_PATH ), '/' );
		if ( 'en/llms.txt' === $path ) {
			schoolswp_llms_serve( 'en', true );
		}
		if ( 'de/llms.txt' === $path ) {
			schoolswp_llms_serve( 'de', true );
		}
	},
	0
);
