---
source_url: https://developer.surecart.com/documentation/actions-filters/media
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/media#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These filters allow you to customize how media elements like videos and image galleries are displayed throughout SureCart.

## [​](https://developer.surecart.com/documentation/actions-filters/media#video-filters) Video Filters

### [​](https://developer.surecart.com/documentation/actions-filters/media#surecart/product-video-poster/size) `surecart/product-video-poster/size`

```
add_filter( 'surecart/product-video-poster/size', function( $size ) {
    return 'full';
} );
```

### [​](https://developer.surecart.com/documentation/actions-filters/media#surecart_video_html) `surecart_video_html`

Filter the video HTML output for complete customization.

Parameters: `$html` (string), `$video` (array — src, poster, dimensions), `$media` (object), `$metadata` (array — duration, codec, etc.)

```
add_filter( 'surecart_video_html', function( $html, $video, $media, $metadata ) {
    return sprintf(
        '<div class="custom-video-player" data-src="%s" data-poster="%s"></div>',
        esc_url( $video['src'] ),
        esc_url( $video['poster'] ?? '' )
    );
}, 10, 4 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/media#image-gallery-filters) Image Gallery Filters

### [​](https://developer.surecart.com/documentation/actions-filters/media#surecart/image-slider/active-breakpoint) `surecart/image-slider/active-breakpoint`

```
add_filter( 'surecart/image-slider/active-breakpoint', function( $breakpoint ) {
    return 768;
} );
```

## Use Cases

### Custom Video Player Integration

```
add_filter( 'surecart_video_html', function( $html, $video, $media, $metadata ) {
    wp_enqueue_script( 'plyr' );
    wp_enqueue_style( 'plyr' );

    return sprintf(
        '<video class="plyr" playsinline controls data-poster="%s">
            <source src="%s" type="video/mp4" />
        </video>',
        esc_url( $video['poster'] ?? '' ),
        esc_url( $video['src'] )
    );
}, 10, 4 );
```
