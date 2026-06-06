---
source_url: https://surecart.com/docs/fathom-analytics-integration
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/Fathom Analytics Integration Guide

# Fathom Analytics Integration Guide

You can integrate SureCart purchases with Fathom Analytics. To do this, you need to add some custom code to your site.

The easiest way to add custom code is to use a [free code snippets plugin](https://wordpress.org/plugins/insert-headers-and-footers/), though you can do this in your theme editor as well.

You can also use the official [Fathom Analytics WP](https://wordpress.org/plugins/fathom-analytics/) plugin to display analytics data directly within your WordPress dashboard.

### Integrating Fathom Analytics Using Embed Code

- Log into [Fathom](https://app.usefathom.com/).
- Click on the **Settings**.

- If you create a new site, add your site name and click on **Create Site**.

- After your site is created, you'll see this screen. Copy the embed code provided and paste it into the head section of your website.

- If you need the embed code for an existing site, click on the site name, then copy your embed code and paste it into the head section of your site.

You can use code snippet plugins such as [WPCode](https://wordpress.org/plugins/insert-headers-and-footers/) to insert this code into your website's head section.

### Using Fathom Analytics WP Plugin For Integration

- Install and activate [Fathom Analytics For WP Plugin](https://wordpress.org/plugins/fathom-analytics/) from your WordPress dashboard.
- Click on the plugin settings.

- Here, enter your **Site ID** from your Fathom dashboard.

- If you have enabled [Site Sharing](https://usefathom.com/docs/features/shared-dashboards) in Fathom, you need to enter your Fathom Analytics account password here. If not, you can leave it blank.

- Click on the **Save Changes** button.

Fathom will show all the analytics data from your site within your WordPress dashboard.

### Integrating SureCart Purchases With Fathom Analytics

[Events](https://usefathom.com/docs/features/events) in Fathom allows you to monitor specific actions taken by visitors on your website.

In our case, we want to track each time a customer purchases a product from your SureCart store. To do this,

- Add this snippet after your embed code. `YOUR-EVENT-ID` is the Site ID from your Fathom dashboard.

```
add_action(
    'wp_footer',
    function() {  ?>
        <script>
            document.addEventListener('scCheckoutCompleted', function(e) {
                const checkout = e.detail;
                if( checkout && checkout.amount_due ) {
                    fathom.trackEvent('YOUR-EVENT-ID', checkout.amount_due / 100 );
                }
            });
        </script>
        <?php
    }
);
```

Thats it! Your SureCart purchases are now officially synced with your Fathom analytics account.

Use this data to gain valuable insights from your customer purchases and improve your site's overall performance.

We hope this guide helped you. If you have any questions, please don't hesitate to reach out to our support team. We're here to help!
