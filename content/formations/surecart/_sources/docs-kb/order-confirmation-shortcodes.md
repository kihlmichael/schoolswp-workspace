---
source_url: https://surecart.com/docs/order-confirmation-shortcodes
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Developer Docs](https://surecart.com/docs-category/developer-docs/)/Order Confirmation Shortcodes

# Order Confirmation Shortcodes

While SureCart offers highly customizable WordPress blocks for the customer dashboard and order confirmation, some users still prefer to do everything in their page builder of choice.

For example, the order confirmation block. While we do offer a dedicated block for order confirmation, we completely understand if you prefer achieving this using page builders.

To make this possible, we have introduced the order confirmation shortcodes that you can add to your page builder.

## Order Confirmation Shortcode

This is for making custom thank you pages and will allow you to display the order data anywhere on the page.

Everything must be wrapped inside a **`sc_order_confirmation`** shortcode.

```
[sc_order_confirmation]

Please check your inbox for more instructions.
[sc_order_confirmation_line_items]
[sc_customer_dashboard_button]Go To Dashboard[/sc_customer_dashboard_button]

[/sc_order_confirmation]
```

This component passes the purchased order data from the checkout page into the individual components. We'll show you how it works in a bit.

## Adding Order Confirmation Shortcode To Your Website

To use this shortcode, you need to create a new custom thank you page and link it to your checkout form.

- Navigate to **Pages** > **All Pages** in your WordPress dashboard and click **Add New Page** to create a new page.
- Name this page as you like, you can give it any name.
- Click on the toggle block inserter icon and add a new **Shortcode** element to your page.
- Paste the above shortcode here.
- Navigate to your checkout and connect this page to it. Follow this [article](https://surecart.com/docs/custom-thank-you-page/) for more details.

Now, when a customer purchases from your store, they will be redirected to this thank you page with details of the purchased product.

You can easily customize this shortcode to display only the elements you want your customers to see.

That's it! We hope this helped you. If you have any questions, feel free to reach out to our support team. We're always here to help!
