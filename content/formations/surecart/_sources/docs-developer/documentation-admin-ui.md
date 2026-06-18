---
source_url: https://developer.surecart.com/documentation/admin-ui
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/admin-ui#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

If you want to add custom UI elements to admin pages of SureCart like Order, Product, Customer, Affiliate pages etc. you can use this API to add either in the Main or the Sidebar area.

# [​](https://developer.surecart.com/documentation/admin-ui#page-metaboxes) Page Metaboxes

To add metaboxes to individual pages, you will need to register an addon, client-side using react.

### Registering an Addon

Call the `registerAddon` function from the global `window.surecart` object. Parameters: `name` (string, required), `settings` (object, required — `render` (HTML/React component), `scope` ("main" or "sidebar"), `title` (string)).

```
import SidebarComponent from "./SidebarComponent";

window.surecart.registerAddon("custom-sidebar", {
  render: () => <SidebarComponent />,
  scope: "sidebar",
  title: "Custom Sidebar Box",
});
```

### Getting Page Data

SureCart uses [WordPress Core Data](https://developer.wordpress.org/block-editor/reference-guides/data/data-core/) (WordPress' flavor of Redux).

#### Get The Current Page ID

```
const id = window.surecart.getCurrentPageId();
```

#### Querying an Order

```
import { useSelect } from "@wordpress/data";
import { store } from "@wordpress/core-data";

const order = useSelect(
  (select) =>
    select(store).getEntityRecord("surecart", "order", id, {
      expand: ["checkout"],
    }),
  [id]
);
```

#### Querying A Product

```
import { useSelect } from "@wordpress/data";
import { store } from "@wordpress/core-data";

const product = useSelect(
  (select) =>
    select(store).getEntityRecord("surecart", "product", id, {
      expand: ["prices", "variants"],
    }),
  [id]
);
```

# [​](https://developer.surecart.com/documentation/admin-ui#admin-list-tables) Admin List Tables

Add custom columns to list table views in its admin pages (Orders, Products, Invoices, etc.) using WordPress's `manage_{$post_type}_posts_columns` functions.

### Step 1 — Add the column

```
add_filter( 'manage_sc-products_columns', 'my_custom_column' );

function my_custom_column( $columns ) {
    $columns['metabox'] = 'Metabox';
    return $columns;
}
```

### Step 2 — Add the column content

`$data` is the model object for the current row.

```
add_action( 'manage_sc-products_custom_column', 'my_custom_column_content', 10, 2 );

function my_custom_column_content( $column_name, $data ) {
    if ( 'metabox' === $column_name ) {
        echo esc_html( $data->id );
    }
}
```

Pages available: `sc-orders`, `sc-products`, etc. (found in the URL `page` parameter).
