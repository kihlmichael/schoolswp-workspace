---
source_url: https://developer.surecart.com/documentation/actions-filters/requests
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/requests#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These filters allow you to intercept and modify data before it's sent to the SureCart API, and transform responses as they come back.

## [​](https://developer.surecart.com/documentation/actions-filters/requests#surecart/request/model) `surecart/request/model`

Filter the model instance before an API request is made.

Parameters: `$model` (Model instance being sent to the API), `$request` (WP_REST_Request).

```
// Add metadata to every checkout
add_filter( 'surecart/request/model', function( $model, $request ) {
    if ( ! $model instanceof \SureCart\Models\Checkout ) {
        return $model;
    }

    $model['metadata'] = array_merge(
        (array) ( $model['metadata'] ?? [] ),
        [
            'source'       => 'wordpress',
            'utm_source'   => $_GET['utm_source'] ?? null,
            'utm_medium'   => $_GET['utm_medium'] ?? null,
            'utm_campaign' => $_GET['utm_campaign'] ?? null,
        ]
    );

    return $model;
}, 10, 2 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/requests#surecart/request/response) `surecart/request/response`

Filter the API response after it's received.

Parameters: `$response` (mixed), `$args` (array — HTTP request arguments), `$endpoint` (string).

```
add_filter( 'surecart/request/response', function( $response, $args, $endpoint ) {
    if ( strpos( $endpoint, 'customers' ) === false ) {
        return $response;
    }

    if ( is_object( $response ) && ! empty( $response->email ) ) {
        $wp_user = get_user_by( 'email', $response->email );
        if ( $wp_user ) {
            $response->wp_user_id = $wp_user->ID;
            $response->wp_roles = $wp_user->roles;
        }
    }

    return $response;
}, 10, 3 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/requests#surecart/request/args) `surecart/request/args`

Filter the HTTP request arguments before sending.

```
add_filter( 'surecart/request/args', function( $args, $endpoint ) {
    if ( strpos( $endpoint, 'exports' ) !== false ) {
        $args['timeout'] = 120;
    }
    return $args;
}, 10, 2 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/requests#surecart/request/endpoint) `surecart/request/endpoint`

Filter the API endpoint URL before the request is made.

```
add_filter( 'surecart/request/endpoint', function( $endpoint, $args ) {
    if ( defined( 'WP_DEBUG' ) && WP_DEBUG ) {
        error_log( 'SureCart API: ' . $endpoint );
    }
    return $endpoint;
}, 10, 2 );
```
