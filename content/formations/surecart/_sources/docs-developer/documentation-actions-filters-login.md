---
source_url: https://developer.surecart.com/documentation/actions-filters/login
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/login#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These filters allow you to customize the login and authentication experience.

## [​](https://developer.surecart.com/documentation/actions-filters/login#sc_login_redirect_url) `sc_login_redirect_url`

Filter the redirect URL after login.

```
add_filter( 'sc_login_redirect_url', function( $url ) {
    // Redirect to custom dashboard
    return home_url( '/my-account/' );
} );

// Or redirect based on user role
add_filter( 'sc_login_redirect_url', function( $url ) {
    $user = wp_get_current_user();

    if ( in_array( 'subscriber', $user->roles ) ) {
        return home_url( '/member-dashboard/' );
    }

    return $url;
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/login#disable-password-nag) Disable Password Nag

Control whether new users see the password change nag after their account is created with a random, temporary password.

```
add_filter( 'get_user_metadata', function( $value, $object_id, $meta_key, $single ) {
    if ( 'default_password_nag' === $meta_key ) {
        return ''; // Return empty to prevent password nag from showing
    }
    return $value;
}, 10, 4 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/login#use-cases) Use Cases

### Role-Based Redirects

```
add_filter( 'sc_login_redirect_url', function( $url ) {
    $user = wp_get_current_user();

    if ( in_array( 'administrator', $user->roles ) ) {
        return admin_url();
    }

    if ( in_array( 'sc_member', $user->roles ) ) {
        return home_url( '/members/' );
    }

    return home_url( '/my-account/' );
} );
```
