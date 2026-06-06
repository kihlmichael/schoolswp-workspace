---
source_url: https://surecart.com/docs/cart-menu-icon-shortcode
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Developer Docs](https://surecart.com/docs-category/developer-docs/)/The Cart Menu Icon Shortcode

# The Cart Menu Icon Shortcode

Sometimes you will want to add the cart menu icon outside of your WordPress menus, or perhaps you are using a page builder that does not pull in default WordPress menus.

If you are not using the block editor, you can use the `sc_cart_menu_icon` shortcode to achieve this.

```
[sc_cart_menu_icon cart_icon="shopping-bag" cart_menu_always_shown=1]
```

This shortcode uses the following parameters:

- **cart_icon** - Either "shopping-bag" or "shopping-cart". Shows the specific cart icon of your choice.
- **cart_menu_always_shown** - Either 1 or 0. If you choose 0, the icon won't show up unless you have added something to your cart.

Find more of such helpful shortcodes in our [list of shortcodes](https://surecart.com/docs/all-shortcodes/).
