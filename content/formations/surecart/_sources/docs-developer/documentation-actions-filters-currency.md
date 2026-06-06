---
source_url: https://developer.surecart.com/documentation/actions-filters/currency
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/currency#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These filters allow you to customize how currency amounts are formatted and displayed throughout SureCart.

## [​](https://developer.surecart.com/documentation/actions-filters/currency#surecart/currency/format) `surecart/currency/format`

Filter the formatted currency string. This is the final output that users see.

Parameters: `$formatted` (string) — The formatted currency string (e.g., "$19.99"). `$amount`(int) — The amount in cents.`$currency_code` (string) — The currency code (e.g., 'USD', 'EUR').

```
add_filter( 'surecart/currency/format', function( $formatted, $amount, $currency_code ) {
    // Add custom prefix
    return 'Price: ' . $formatted;
}, 10, 3 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/currency#surecart/currency/locale) `surecart/currency/locale`

Filter the locale used for currency formatting.

```
add_filter( 'surecart/currency/locale', function( $locale ) {
    return get_locale();
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/currency#surecart/currency/max_cents) `surecart/currency/max_cents`

Filter the maximum number of decimal places shown.

```
add_filter( 'surecart/currency/max_cents', function( $decimals, $amount, $converted ) {
    // Always show 2 decimal places
    return 2;
}, 10, 3 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/currency#surecart/currency/filter_url) `surecart/currency/filter_url`

Disable URL-based currency switching (for full-page caching compatibility).

```
add_filter( 'surecart/currency/filter_url', '__return_false' );
```

## [​](https://developer.surecart.com/documentation/actions-filters/currency#surecart/display_amount/free) `surecart/display_amount/free`

Filter the text displayed for $0 prices.

```
add_filter( 'surecart/display_amount/free', function( $text ) {
    return 'No Cost';
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/currency#surecart/currency_switcher/label) `surecart/currency_switcher/label`

Filter the currency switcher label text.

```
add_filter( 'surecart/currency_switcher/label', function( $label ) {
    return strtolower( $label );
} );
```
