---
source_url: https://surecart.com/docs/product-list-guide-shop-page
source: surecart-kb
scraped: true
---

# Product List Guide – Shop Page

### **What is Product List**?

SureCart offers a flexible product list block to showcase a grid of your products in your store.

When you set up your store in SureCart, a default shop page named **Shop — Sample Page** is automatically created for you. This page contains some sample product items, displaying them based on the chosen theme. You can find this page under the **Pages** section in your WordPress dashboard.

### **Product List Customization Features**

#### **Sidebar**

You can configure the default state of the Sidebar, either open or closed, by selecting the Sidebar component and enabling or disabling the "Open by default" toggle. You can also adjust the position of the block to either Default (fixed) or Sticky.

#### **Products per Page**

You can choose how many products are displayed per page to suit your layout preferences.

#### **Auto Fixed Columns**

You can choose a fixed number of columns to display or set a minimum column width to automatically adjust to your page size.

#### **Pagination Options**

If you have a large number of products, you can enable the **Paginate** option to organize them across multiple pages. This feature adds **Next** and **Previous** buttons, allowing users to easily navigate between pages. You can also customize the pagination font size.

#### **Sort and Filter**

Sorting and filtering options help your customers navigate your products more easily. Customers can sort products by their latest additions, oldest items, price (low to high) and price (high to low). You can also set the default sorting option.

#### **Taxonomy Filtering**

SureCart allows you to assign custom taxonomies to products and filter them within the product list block. To add a filter, duplicate an existing filter block, and in the settings panel on the right, select the desired taxonomy under the **Taxonomy** dropdown.

#### **Search Products**

Your customers have the ability to search for specific products within your list. In case you don't want to show the search, you can simply remove this block.

#### **Choose the Products You Want to Display**

Select which products you want to display on your product list. You can either show all, featured, or hand-picked products based on your preference.

#### **Edit Products**

SureCart allows you to edit each product card individually, giving you complete control over how your products are displayed. In the editor, you can:

- Change the text size and font of product titles
- Update product image like aspect ratio, border, margin etc
- Set custom price ranges
- Adjust the padding between product items

### **Integrating ShortCodes**

For those who prefer shortcodes, SureCart provides the flexibility to configure your product list.

```
[sc_product_list] - Display a list of products in a grid.
   "columns": It sets the number of columns, defaulting to 4.
   "limit": It sets the maximum limit, defaulting to 15.
   "pagination_enabled": It enables or disables pagination, defaulting to enabled (true).
   "ajax_pagination": It activates or deactivates AJAX pagination, defaulting to enabled (true).
   "pagination_auto_scroll": It turns on or off automatic scrolling when new results are loaded, defaulting to on (true).
   "search_enabled": It allows or disallows the use of a search function, defaulting to allowed (true).
   "sort_enabled": It permits or prohibits sorting functionality, defaulting to permitted (true).
   "ids": The product ids you want to show here, separated by a comma.
   type="custom": This is useful if you do not wish to display all of the products from the shop page on a page but only custom ones.
```

Example shortcode for a page builder:

```
[sc_product_list columns="3" limit="9" ids="049627ac-f5e0-4157-a530-c4b2dbef82bb,c960b061-d321-43e3-a151-8c40b35f0c22,a114295c-198a-4e33-aa47-ab7d07172193" search_enabled="true" sort_enabled="true" type="custom"]
```
