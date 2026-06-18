---
source_url: https://surecart.com/docs/related-products
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Products](https://surecart.com/docs-category/products/)/Related Products

# Related Products

This guide will explore the settings for related products in the block editor (Bricks users can create these using query loops) and how to leverage them to achieve your desired design.

To begin you will want to [edit the product template](https://surecart.com/docs/product-pages-guide/). Once there, click on **Document Overview** (1), then click on **the arrows** (2) to expand and reveal all components. This step helps you navigate the document structure and access specific elements for editing.

Click on the Related Products block to edit the related product settings.

This allows you to customize attributes such as **default sorting**, **taxonomy**, and the number of products per page. You can also configure fallback options in case no related products are available.

### Settings

You can adjust the sorting, taxonomy, pagination, and fallback settings for related products from the related products block. Let's take a look at each setting in detail.

#### **Default Sorting**

This setting uses the same sorting options from the [product list block](https://surecart.com/docs/product-list-guide-shop-page/). It determines the default order in which your products will be displayed.

However, for this block, we've added a new **Random** option, which displays products in a randomized order. Each time a user refreshes the page, the products appear in a different sequence.

Keep in mind, selecting **Random** order means:

- Pagination cannot be used (since it would just display random items paging back and forth)
- If you are caching this page, each user won't get a random order, but it will change whenever cache is purged.

#### **Taxonomy**

You can display products based on a specific taxonomy. By default, the store includes only the **collection taxonomy**, but you can add your own taxonomy and display products accordingly.

For example, if you create a taxonomy called "**Style**" and assign styles to your products, you can use this setting to display only products that share the same style taxonomy terms. This gives you control over filtering and organizing the products shown.

Related products will display any products that have **any** of matching terms in the same taxonomy.

#### **Products Per Page**

This setting allows you to limit the number of products displayed at the same time without pagination. For example, if you set this value to 3, only three products will appear on the carousel at once, providing a clean and organized layout for your users. Adjusting this setting ensures a user-friendly experience by preventing overcrowding.

#### **Max Pages to Show**

If you have a large number of related products, multiple paginations will be generated based on your settings. This option allows you to limit the number of pages shown in the pagination system.

For example, setting this value to 2 restricts the display to two pages, even if more products are available. This helps control how much content users can browse through at one time while keeping the design clean and user-friendly.

#### **All Products Fallback**

If a product has no related items, you can enable this setting to display non-related products from your store instead.

This option ensures that your carousel always features products, even when there are no direct matches, providing users with a continuous shopping experience and maximizing the visibility of your inventory.

#### **Layout**

To control how many columns of products are displayed, click on the **Template Element** (1) and adjust the **layout settings** (2). From here you can drag and drop blocks, reorder, or style any of the elements in related posts. You can also set the number of columns in two ways:

##### **Manual**

This option displays the exact number of columns you set. For example, if you select **3**, you will see 3 products per row on Desktop devices (mobile devices will always display stacked).

##### **Auto**

This option adjusts the number of columns based on the column width and the page's dimensions. You can set a minimum column width, and the number of products shown per row will dynamically adjust (showing fewer or more) depending on the screen size. This provides more responsive control.

That's it! If you have any suggestions or feedback, feel free to let us know [here](https://surecart.com/support/open-a-ticket/).
