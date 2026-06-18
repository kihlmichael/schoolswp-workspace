---
source_url: https://developer.surecart.com/documentation/custom-loops
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/custom-loops#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

Querying products utilizes the "WordPress Loop". Specify the `sc_product` post type in the query.

## [​](https://developer.surecart.com/documentation/custom-loops#simple-query-example) Simple Query Example

```
$products = new WP_Query(
  array(
    'post_type'      => 'sc_product',
    'posts_per_page' => 10,
  )
);
```

## [​](https://developer.surecart.com/documentation/custom-loops#getting-product-data-from-the-post) Getting Product Data From The Post

### In the loop

Use `sc_get_product()` after calling `$products->the_post()`:

```
$products = new WP_Query(
  array(
    'post_type'      => 'sc_product',
    'posts_per_page' => 10,
  )
);

if ( $products->have_posts() ) :
  while ( $products->have_posts() ) :
    $products->the_post();

    $product = sc_get_product();

    echo esc_html( $product->display_amount );

    if ( $product->is_out_of_stock ) {
      echo 'Out of stock!';
    }

    if ( $product->is_low_stock ) {
      echo 'Only ' . (int) $product->available_stock . ' left!';
    }
  endwhile;
endif;
```

### Outside the loop

```
$posts = get_posts(
  array(
    'post_type'      => 'sc_product',
    'posts_per_page' => 10,
  )
);

foreach($posts as $post) {
  $product = sc_get_product( $post );
  echo esc_html( $product->display_amount );
}
```

## [​](https://developer.surecart.com/documentation/custom-loops#querying-variant-options) Querying Variant Options

### Single variant option

```
$products = new WP_Query(
  [
    'post_type'      => 'sc_product',
    'posts_per_page' => 10,
    'variant_options' => [
      [
        'name' => 'Color',
        'values' => 'Orange'
      ]
    ]
  ]
);
```

### Multiple variant options (AND)

```
$products = new WP_Query(
  [
    'post_type'      => 'sc_product',
    'posts_per_page' => 10,
    'variant_options' => [
      'relation' => 'AND',
      [ 'name' => 'Color', 'values' => 'Orange' ],
      [ 'name' => 'Size', 'values' => 'Small' ]
    ]
  ]
);
```

### Multiple variant options (OR)

```
$products = new WP_Query(
  [
    'post_type'      => 'sc_product',
    'posts_per_page' => 10,
    'variant_options' => [
      'relation' => 'OR',
      [ 'name' => 'Color', 'values' => 'Orange' ],
      [ 'name' => 'Size', 'values' => ['Small', 'Medium'] ]
    ]
  ]
);
```
