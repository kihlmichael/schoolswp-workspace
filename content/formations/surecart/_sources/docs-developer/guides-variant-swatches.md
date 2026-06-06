---
source_url: https://developer.surecart.com/guides/variant-swatches
source: surecart-developer-docs
scraped: true
---

# Variant Swatches

Guide: transform variant option pills into visual image swatches using variant images assigned to each variant.

Prerequisite: assign images to your variants first (see Variant Images documentation in the SureCart docs).

## How it works

The code hooks into render_block to intercept the surecart/product-variant-pill block. It replaces the text pill with a thumbnail from the variant's assigned image. Clicking a swatch updates the product gallery image.

## Implementation summary

Add to functions.php or a custom plugin. Set the variable at the top to your variant option name (default: "color").

Key steps in the implementation:

1. Hook into render_block with priority 10 and 3 arguments
2. Check blockName equals surecart/product-variant-pill and the block context name matches the target option
3. Call sc_get_product() to retrieve the current product
4. Filter product->gallery to find images whose variant_option metadata matches the pill value
5. Use WP_HTML_Tag_Processor to set a CSS background-image style on the pill div (56px x 56px by default)
6. Add CSS classes: sc-variant-color-swatch, plus data-wp-class attributes for selected and disabled states
7. Wrap in a flex column div (sc-variant-color-wrapper)

Full source code available at: https://developer.surecart.com/guides/variant-swatches

## Customization options

- Change variant option name: set the variable to "size", "material", etc.
- Show variant labels: uncomment the name div below each swatch
- Adjust swatch size: modify width and height in the inline style (default 56px)

## CSS for selected and disabled states

Selected swatch: add border-color and box-shadow using the brand green (#00824c).

Disabled/unavailable swatch: set opacity to 0.4 and cursor to not-allowed.

Target class names: sc-variant-color-swatch--selected and sc-variant-color-swatch--disabled.
