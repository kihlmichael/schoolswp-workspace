# Troubleshooting — Yoast/RankMath Issue (Broken Dashboard)

> Source : https://docs.themeum.com/tutor-lms/troubleshooting/yoast-rankmath-compatibility/

## Yoast/RankMath Issue (Broken Dashboard)

For some users, who are using Yoast/Rank Math on their site and an overridden main/child theme file, the Tutor LMS dashboard gets broken in some instances. This doc aims to provide to fix this.

- First check if the theme you are using is overriding the **Tutor LMS** plugin or not.
- Then, check if your theme has a child theme or not. You will need to override the theme with a child theme. Go to the Tutor folder from that theme and find the **dashboard.php** file.
- You will need to override this file. Access the folder from the website server and navigate to the file that you need to override. Open the file with an editor.
- Now, on the top and bottom of that, you can see this function called **get_header()** and **get_footer()**.

To fix the broken dashboard issue replace the `get_header()` function with:

```php
$is_by_short_code = isset($is_shortcode) && $is_shortcode===true;
if(!$is_by_short_code && !defined( 'OTLMS_VERSION' ))  {
    get_header();
}
```

and replace the `get_footer()` function with:

```php
if(!$is_by_short_code && !defined( 'OTLMS_VERSION' )) {
    get_footer();
}
```

**Note:** The overall issue is, you can't directly use the get_header() and get_footer() functions without the above condition.
