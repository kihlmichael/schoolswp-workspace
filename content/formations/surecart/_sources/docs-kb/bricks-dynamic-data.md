---
source_url: https://surecart.com/docs/bricks-dynamic-data
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Bricks Builder](https://surecart.com/docs-category/bricks-builder/)/Dynamic Data for Bricks Builder

# Dynamic Data for Bricks Builder

In this documentation, we will explore and explain all the dynamic data available for use within the Bricks Builder.

For more detailed information about Bricks Builder's dynamic data, be sure to consult the [official documentation](https://academy.bricksbuilder.io/article/dynamic-data/) on their website.

### **Understanding Dynamic Data**

Dynamic data refers to the data fields that can change based on the product or context. By utilizing dynamic data in Bricks Builder, you can efficiently display product-specific information that automatically updates, allowing for a highly customizable and personalized user experience.

### **List of All Available Dynamic Data**

| **Dynamic Data**                             | **Description**                                                            | **Example**                             |
| -------------------------------------------- | -------------------------------------------------------------------------- | --------------------------------------- |
| {sc_product_price}                           | The default or first price of a product.                                   | $39                                     |
| {sc_product_selected_price}                  | The price currently selected in the Price Selector element.                | $30                                     |
| {sc_product_scratch_price}                   | The price before any discounts are applied (crossed-out price).            | $29                                     |
| {sc_product_selected_scratch_price}          | The original price for the currently selected pricing option.              | $24                                     |
| {sc_product_price_range}                     | For products with variable prices, the range from lowest to highest.       | $24 - $39                               |
| {sc_product_description}                     | The description of the product.                                            | Offer your customers the flexibility... |
| {sc_product_stock}                           | The current stock level of the product.                                    | 33                                      |
| {sc_product_sku}                             | The SKU (Stock Keeping Unit), a unique identifier for your product.        | ABC12345                                |
| {sc_product_on_sale}                         | Whether or not the product is on sale (1 = true, 0 = false).               | 1                                       |
| {sc_product_trial}                           | If the product includes a trial period, the length or start date.          | Starting in 15 days                     |
| {sc_product_selected_price_trial}            | The trial info for the currently selected pricing option.                  | Starting in 15 days                     |
| {sc_product_billing_interval}                | How frequently the customer will be billed.                                | Every month                             |
| {sc_product_selected_price_billing_interval} | The billing interval for the selected pricing option.                      | Every year                              |
| {sc_product_setup_fee}                       | The setup fee associated with the product's first price.                   | $9 Setup Fee                            |
| {sc_product_selected_price_setup_fee}        | The setup fee for the selected price in the Price Selector.                | $9 Setup Fee                            |
| {sc_price_name}                              | The name of the price or pricing option (within the Price Choice element). | Subscribe & Save                        |
| {sc_price_amount}                            | The actual price amount for the selected Price Choice element option.      | $24 / month                             |
| {sc_price_trial}                             | The trial period for the selected Price Choice element.                    | Starting in 7 days                      |
| {sc_price_setup_fee}                         | The setup fee for the selected price in the Price Choice element.          | $9 Setup Fee                            |

### **How to Use This Data in Bricks Builder**

To ensure dynamic data works correctly with SureCart in Bricks Builder, there are a few important conditions you must meet. Dynamic data must be used either:

1. Inside a **Query Loop** where the **SureCart Product** is set as the post type, or
2. Within a **Bricks Template** part for:
   - **SureCart - Single Product**, or
   - **SureCart - Collection Archive**.

Additionally, dynamic data should be placed inside **Product Form** or **Product Card** elements to ensure it pulls the correct product information.

If these conditions are not met, the dynamic data fields won't pull in the correct product information.

#### **Steps to Insert Dynamic Data:**

1. Navigate to the relevant page or template in Bricks Builder: For dynamic product displays, use a **Query Loop** with **SureCart Product** as the post type, or use the SureCart Single Product or Collection Archive template parts.
2. Enable the **Query Loop** if applicable, and set the post type to **SureCart Product**.
3. Ensure that the dynamic data is placed inside **Product Form** or **Product Card** elements.
4. Select the element where you want to display dynamic data (e.g., a text block, pricing table, etc.).
5. Choose the relevant dynamic data field from the available options within the Bricks interface.
6. Preview your page to ensure that the correct product data is dynamically displayed.

By adhering to these steps and using the right template structure or query settings, you can effectively create pages that dynamically pull in and display product information in real time.
