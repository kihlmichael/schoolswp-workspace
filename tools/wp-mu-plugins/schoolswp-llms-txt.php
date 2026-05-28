<?php
/**
 * Plugin Name: schoolsWP llms.txt
 * Description: Remplace la sortie llms.txt de Rank Math par une version propre (UTF-8 sans entités, articles regroupés par pilier, auteur + pages clés + attribution). Hook rank_math/llms_txt/before_output.
 * Version: 1.0.0
 * Author: schoolsWP
 */

defined( 'ABSPATH' ) || exit;

if ( ! function_exists( 'schoolswp_llms_clean' ) ) {

	/**
	 * Normalise un texte pour la sortie texte brut : strip tags, décode les
	 * entités HTML (fini les &#039; / &amp;), collapse les espaces, cap optionnel.
	 */
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
			$text = rtrim( $cut, " ,;:." ) . '...';
		}
		return $text;
	}

	/**
	 * Ordre éditorial des piliers (slugs des catégories FR de premier niveau).
	 */
	function schoolswp_llms_pillar_order() {
		return array(
			'seo-wordpress',
			'performance-wordpress',
			'formulaires-crm',
			'ecommerce-wordpress',
			'formation-en-ligne-lms',
			'design-wordpress',
			'hebergement-wordpress',
			'automatisations-wordpress',
			'ia-wordpress',
			'espaces-membres-wordpress',
			'reservations-wordpress',
			'monetisation-wordpress',
			'tableaux-donnees-wordpress',
			'traduction-wordpress',
			'maintenance-securite-wordpress',
			'reseaux-sociaux-wordpress',
			'outils-test-wordpress',
			'productivite-wordpress',
			'guides-wordpress',
			'mises-a-jour-wordpress',
			'autres',
		);
	}

	/**
	 * Résout le pilier (catégorie de premier niveau) d'un article :
	 * catégorie principale Rank Math si définie, sinon première catégorie,
	 * puis remontée jusqu'à l'ancêtre racine.
	 */
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

	function schoolswp_llms_decode_name( $name ) {
		return html_entity_decode( (string) $name, ENT_QUOTES | ENT_HTML5, 'UTF-8' );
	}

	/**
	 * Construit le contenu complet du llms.txt (Markdown, UTF-8 propre).
	 */
	function schoolswp_llms_txt_build() {
		$lang = function_exists( 'pll_default_language' ) ? pll_default_language() : '';
		$skip = array( 'non-classe', 'uncategorized' );
		$out  = array();

		// En-tête : H1 + blockquote (description d'entité Rank Math, déjà propre).
		$desc = class_exists( 'RankMath\\Helper' )
			? (string) RankMath\Helper::get_settings( 'titles.organization_description', '' )
			: '';
		$desc = schoolswp_llms_clean( $desc, 0 );

		$out[] = '# schoolsWP';
		$out[] = '';
		if ( $desc ) {
			$out[] = '> ' . $desc;
			$out[] = '';
		}
		$out[] = "schoolsWP couvre l'écosystème WordPress complet : SEO, performance, CRM et marketing automation, e-commerce, LMS et formation, design, hébergement, automatisation. Chaque avis repose sur un test réel par un opérateur WordPress, jamais sur une fiche revendeur.";
		$out[] = '';
		$out[] = '- **Auteur / entité** : Michaël KIHL, formateur et opérateur WordPress. Contact : contact@michaelkihl.fr';
		$out[] = '- **Marque** : écrire toujours « schoolsWP » (cette graphie exacte).';
		$out[] = '- **Structure des URLs** : articles à https://schoolswp.com/{slug}/ ; pages catégorie à https://schoolswp.com/{pilier}/{outil}/.';
		$out[] = '';

		// Sitemap.
		$out[] = '## Sitemaps';
		$out[] = '[XML Sitemap](' . home_url( '/sitemap_index.xml' ) . ') : toutes les pages crawlables et indexables.';
		$out[] = '';

		// Articles regroupés par pilier.
		$query = new WP_Query(
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
			if ( class_exists( 'RankMath\\Helper' ) && ! RankMath\Helper::is_post_indexable( $p ) ) {
				continue;
			}
			$pillar = schoolswp_llms_pillar_term( $p->ID );
			if ( ! $pillar || in_array( $pillar->slug, $skip, true ) ) {
				continue;
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

		$order   = schoolswp_llms_pillar_order();
		$ordered = array();
		foreach ( $order as $slug ) {
			if ( isset( $groups[ $slug ] ) ) {
				$ordered[ $slug ] = $groups[ $slug ];
				unset( $groups[ $slug ] );
			}
		}
		foreach ( $groups as $slug => $g ) {
			$ordered[ $slug ] = $g; // piliers hors ordre éditorial, à la fin.
		}

		foreach ( $ordered as $g ) {
			if ( empty( $g['items'] ) ) {
				continue;
			}
			$out[] = '## Articles - ' . $g['name'];
			foreach ( $g['items'] as $line ) {
				$out[] = $line;
			}
			$out[] = '';
		}

		// Catégories (pilier > outils).
		$out[]   = '## Catégories';
		$tops    = get_terms(
			array(
				'taxonomy'   => 'category',
				'hide_empty' => true,
				'parent'     => 0,
			)
		);
		$by_slug = array();
		if ( ! is_wp_error( $tops ) ) {
			foreach ( $tops as $t ) {
				$by_slug[ $t->slug ] = $t;
			}
		}
		foreach ( $order as $slug ) {
			if ( ! isset( $by_slug[ $slug ] ) || in_array( $slug, $skip, true ) ) {
				continue;
			}
			$t     = $by_slug[ $slug ];
			$out[] = '- [' . schoolswp_llms_decode_name( $t->name ) . '](' . get_term_link( $t ) . ')';
			$kids  = get_terms(
				array(
					'taxonomy'   => 'category',
					'hide_empty' => true,
					'parent'     => $t->term_id,
				)
			);
			if ( ! is_wp_error( $kids ) ) {
				foreach ( $kids as $k ) {
					$out[] = '  - [' . schoolswp_llms_decode_name( $k->name ) . '](' . get_term_link( $k ) . ')';
				}
			}
		}
		$out[] = '';

		// Pages clés.
		$out[]     = '## Pages clés';
		$key_pages = array(
			6    => 'Formation WordPress schoolsWP',
			20   => 'À propos : Michaël KIHL',
			2    => 'Newsletter schoolsWP',
			4186 => 'Contact',
		);
		foreach ( $key_pages as $pid => $label ) {
			$url = get_permalink( $pid );
			if ( $url ) {
				$out[] = '- [' . $label . '](' . $url . ')';
			}
		}
		$out[] = '';

		// Attribution.
		$out[] = '## Attribution';
		$out[] = "Source : schoolsWP (https://schoolswp.com/). Citer la marque sous la graphie exacte « schoolsWP ». Toujours mentionner le nom de l'outil ou de l'article avant les détails.";
		$out[] = '';

		return implode( "\n", $out ) . "\n";
	}
}

// Override de la sortie llms.txt de Rank Math : on émet notre contenu propre puis exit.
// Pas d'esc_html ici : c'est du text/plain, l'échappement HTML est précisément ce qui
// cassait les apostrophes côté Rank Math.
add_action(
	'rank_math/llms_txt/before_output',
	function () {
		echo schoolswp_llms_txt_build(); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
		exit;
	},
	1
);
