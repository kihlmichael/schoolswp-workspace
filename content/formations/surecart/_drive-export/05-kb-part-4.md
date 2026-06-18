# SureCart - Base de connaissances (partie 4 sur 4)


===== SOURCE: quick-view-bricks.md =====

---
source_url: https://surecart.com/docs/quick-view-bricks
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Bricks Builder](https://surecart.com/docs-category/bricks-builder/)/How to Create a Quick View in Bricks Builder

# How to Create a Quick View in Bricks Builder

In this guide, we will explore how to create a quick view effect for SureCart in Bricks Builder without the need for any external plugins, leveraging only Bricks and SureCart's native elements.

Let's get started.

### **Create the Pop-Up Template**

The first element we need to design is the pop-up itself because it needs to be selected within the page where we want the quick view effect. So, let's create our pop-up in Bricks Builder.

- Go to the **Bricks** menu, then select **Templates**, and click the **Add New Template** button.

- Give your template a name (1), such as "Quick View."
- Select the template type as **Popup** (2).
- Click the **Publish** button to save your changes.
- Finally, click the **Edit with Bricks** button (3) to start customizing the template.

- Click on the **plus (+) icon** to add a new section to your design.

- Add the **Product Form** element (1).
- Click on the **Save** button (2) to save your changes.
- Exit the pop-up editing page.

- Add the **Template** element to the page where you want the pop-up to open. The specific location of this element on the page is not important.

- After adding the **Template** element, click on it to open its settings and select the **Quick View** pop-up template you created earlier.

### **Triggering the Popup Template**

To display the popup template, we will use Bricks' native Interactions. To learn more about Bricks Interactions, check out this [documentation](https://academy.bricksbuilder.io/article/interactions/).

- On the element that you want to function as a button to open the popup (in this example, we used a text link), go to the **Interactions** tab (1) and configure the following settings (2):
  - **Trigger**: Click
  - **Action**: Show element
  - **Target**: Popup
  - **Popup**: Select "Quick View" (or the name you assigned).

- Save the page and preview it on the frontend.

That's it!

You can now enhance your popup by adding a close button and styling it to your preference.


===== SOURCE: reactivate-subscriptions-using-customer-dashboard.md =====

---
source_url: https://surecart.com/docs/reactivate-subscriptions-using-customer-dashboard
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Customer Dashboard](https://surecart.com/docs-category/customer-dashboard/)/How to Reactivate Cancelled Subscriptions Using Customer Dashboard

# How to Reactivate Cancelled Subscriptions Using Customer Dashboard

SureCart makes it super easy to bring back your canceled subscription. Situations come up, and sometimes you might decide to cancel your subscriptions.

That's where SureCart's reactivation feature helps you. With it, you can easily reactivate your subscription, making the whole process of coming back to SureCart simple.

## **Reactivating Subscriptions From Your Customer Dashboard**

The easiest way to reactivate these subscriptions is by going to your [customer dashboard](https://surecart.com/docs/overview-customer-dashboard/). The process is quite simple, you just have to follow these steps.

- Navigate to your customer dashboard. If you're not sure how to get there, just follow the steps given [here](https://surecart.com/docs/customers-access-dashboard/).

- Here, you can find the recently canceled subscription on the **Dashboard** section itself. Click on your canceled plan.

- You'll be automatically navigated to the **Plans** section. Here, click on the **Resubscribe** option.

- Simply click on the **Yes, Reactivate** button to reactivate your subscription.

Congratulations! Your subscription has been successfully reactivated. You can now see your previously canceled plan active again on your customer dashboard.

That's it! We hope this guide proves helpful. If you face any issues or can't find your customer dashboard for reactivation, please feel free to reach out to our support team.


===== SOURCE: refund-an-order.md =====

---
source_url: https://surecart.com/docs/refund-an-order
source: surecart-kb
scraped: true
---

# How to Refund an Order - SureCart

## Overview

SureCart enables merchants to process refunds for customer orders. The system handles refunds for all product types, including subscriptions.

## Step-by-Step Refund Process

1. Navigate to the Orders section within SureCart from your website dashboard

2. Select the specific order requiring a refund

3. Scroll to the Charge Section, click the three-dot menu, and select "Refund"

4. In the slide-out panel, review the "Refund Item(s)" section. Select items to refund and choose whether to:
   - Restock the item
   - Revoke Purchase (this removes product access and cancels subscriptions)

5. Select an appropriate reason from the "Reason for refund" dropdown menu, which will appear in your payment processor records

6. Enter your desired refund amount in the "Refund Amount" field under "Summary." You can adjust this up to the total available amount

7. Review all details and click the "Refund" button to complete the transaction

## Post-Refund Outcomes

Following refund initiation:
- Customers receive email notification with refund details
- Access to linked products (LMS courses, etc.) is revoked
- Download file access becomes unavailable
- Refunds can take 5-10 days to appear on a customer's statement. Processor fees are typically not returned.


===== SOURCE: related-products.md =====

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


===== SOURCE: remove-coupon-from-checkout.md =====

---
source_url: https://surecart.com/docs/remove-coupon-from-checkout
source: surecart-kb
scraped: true
---

# How to Remove Coupon Field From the Checkout Form

With SureCart, you have the flexibility to tailor your customer's checkout experience by customizing the checkout page as per your needs.

By default, SureCart displays a coupon code field on the checkout form. If you decide that offering a direct coupon field isn't suitable for your checkout form, you can effortlessly remove it.

Follow the next steps to remove the coupon code from the checkout form:

- Log into your WordPress dashboard, navigate to SureCart, and select Forms.
- Choose the desired form and click on Edit.
- Click on the List View.
- Expand the form, search for the coupon field, and click on the three dots next to it.
- Choose Delete from the dropdown menu.
- Confirm and finalize your changes by hitting the Update button.

That's it; your checkout form no longer has a coupon code.

Remember that coupons can still be used via URL parameters, but there will no longer be a coupon option on the checkout form.


===== SOURCE: remove-plugin-data.md =====

---
source_url: https://surecart.com/docs/remove-plugin-data
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Settings](https://surecart.com/docs-category/settings/)/How to Remove SureCart Plugin Data from Your Website

# How to Remove SureCart Plugin Data from Your Website

When you disable and delete the SureCart plugin, the plugin's data isn't automatically removed. This means if you reinstall the plugin, it'll still remember your prior settings, like its connection to app.surecart.com.

Now, keep in mind, that removing the plugin data doesn't mean you're [wiping out all your store's data](https://surecart.com/docs/how-to-permanently-delete-your-business-and-user-account/). Your customers, orders, products, and all the settings tailored for your SureCart store remain intact.

Should you decide to reinstall the SureCart plugin later on, it's a breeze! Just reconnect it to your store via app.surecart.com [using the API key](https://surecart.com/docs/how-to-find-your-surecart-api-token/), and everything – your products, customers, and orders – will all come right back.

This guide will teach you how to remove SureCart plugin data like SureCart customer roles, pages, shop, posts, checkout forms, and others when you uninstall the SureCart plugin from your website. You can simply follow the steps below to remove your data from SureCart.

1. Go to SureCart from your website and click Settings.

2. Click on the Advanced tab and scroll to the bottom of the page to find Uninstall.

3. Toggle on the Remove Plugin Data and Click Save.

If you proceed with this action, you'll entirely erase your website's plugin data associated with the SureCart Plugin.

However, as I pointed out earlier, you can always reconnect to app.surecart.com using the API keys.

In case you're thinking of deleting all this data permanently, along with your user account, you can simply follow the steps outlined in this guide: [How to Permanently Delete Your Business and User Account.](https://surecart.com/docs/how-to-permanently-delete-your-business-and-user-account/)

Got questions? We're all ears, so reach out anytime.


===== SOURCE: remove-surecart-logo-from-emails.md =====

---
source_url: https://surecart.com/docs/remove-surecart-logo-from-emails
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Email](https://surecart.com/docs-category/email/)/How to Remove SureCart Logo from the Automatic Email Notification?

# How to Remove SureCart Logo from the Automatic Email Notification?

By default, automatic email notifications sent by SureCart contain the SureCart logo. This is a premium feature — you will need to upgrade your account to one of the premium subscriptions to access it.

## Steps to Remove the SureCart Logo

1. From your WordPress dashboard, navigate to **Settings** under **SureCart**.
2. Access the **Design and Branding** section.
3. Toggle the button next to **Remove SureCart Branding**.
4. Click on the **Save** button.

This will remove the SureCart logo from all emails that customers receive.


===== SOURCE: restrict-purchases-to-specific-countries.md =====

---
source_url: https://surecart.com/docs/restrict-purchases-to-specific-countries
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/How to Restrict Purchases to Specific Countries

# How to Restrict Purchases to Specific Countries

To restrict purchases to specific countries, please check out our developer docs:

[View Developer Docs](https://developer.surecart.com/documentation/actions-filters/checkout#address-countries)


===== SOURCE: sales-tax-eu-vat.md =====

---
source_url: https://surecart.com/docs/sales-tax-eu-vat
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Tax](https://surecart.com/docs-category/tax/)/How to Set Up EU VAT Taxes in SureCart

# How to Set Up EU VAT Taxes in SureCart

In this article, we will show you how to set up EU VAT taxes in SureCart.

### **What is EU VAT**

If you sell products to customers in the European Union (EU) or EU collection obligation, you may need to comply with EU VAT regulations.

VAT stands for Value Added Tax, and it's a consumption tax applied to goods and services in the EU.

### **How EU VAT Works in SureCart**

EU VAT Settings will become visible only after you've [enabled the Tax Collection](https://surecart.com/docs/configure-tax-settings-in-surecart/) option from the Store Tax Settings section.

Here, you can manage how your store handles EU VAT collection and validation.

Within this section, there are three important settings to note:

**Require VAT number**: Businesses or legal entities registered for VAT use this unique identifier number. Enabling this option will show customers a field to enter an EU VAT number when they're purchasing through a checkout form.

**Local reverse charge**: Local reverse charge is when the customer, not the supplier, pays the VAT on a transaction. Enabling this option allows you to apply reverse charges when customers add valid VAT numbers, even if customers are in their home country.

**VAT Number Verification Failure**: In this setting, you can choose the behavior your checkout will display when VAT verification fails. You have three options:

- Reject the order and show an error.
- Accept the order but don't apply the reverse charge.
- Accept the order and apply the reverse charge.

We hope this helped you. If you have any questions, please don't hesitate to contact our support team. We're here to help!

> **Note:** Please note, this article isn't intended to provide tax advice. We're simply here to explain the available features and guide you on how to best use them for your SureCart-powered eCommerce store. For any specific tax obligations you may have, we strongly recommend consulting a tax expert.


===== SOURCE: second-steps.md =====

---
source_url: https://surecart.com/docs/second-steps
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Getting Started](https://surecart.com/docs-category/getting-started/)/Steps After Getting Started with SureCart

# Steps After Getting Started with SureCart

This document explains how to customize the three main pages of a SureCart store: the Shop Page, the Product Page, and the Checkout Page.

## **Requirements**

- WordPress admin access
- SureCart plugin installed and activated
- At least one product created in SureCart

## **Choosing an Editor for Store Pages**

SureCart integrates with the WordPress Block Editor (Gutenberg) by default.

For advanced design control, SureCart also integrates with:

- Elementor (and Elementor Pro)
- Bricks Builder

**Important:** The Cart and Checkout Pages can only be customized using the Block Editor.

## **The Shop Page**

The Shop Page displays the list of products available in the store. It is powered by the **Product List Block**.

### **Accessing the Shop Page**

1. Go to **SureCart menu**.
2. Locate the menu named **Shop**.
3. Click **Edit** to open it in the Block Editor.

### **Available Customization Options**

- Number of products displayed per page
- Number of products per row (columns)
- Filters such as Sort By, Collections, or Custom Post Types
- Pagination (enable or disable)
- Aspect ratio of product images
- Product details displayed (title, price, add-to-cart button)
- Typography and spacing

## **The Product Page**

The Product Page displays detailed information about an individual product.

### **Editing the Product Page Template**

1. Go to **WordPress Dashboard → SureCart → Products**.
2. Select the product to edit.
3. In the right sidebar, locate the **Template** section.
4. Click **Edit Product Template** to open the template in the Block Editor.

### **Available Customization Options**

- Image display style: **Gallery View** or **Slideshow View**
- Position of elements such as title, description, price, and buttons
- Typography, colors, and spacing
- Adding or removing blocks

## **The Checkout Page**

### **Available Checkout Layouts**

SureCart provides the following starting layouts: Default, Full Page, Simple, Sections, Two Column, Donation, Invoice.

### **Accessing the Checkout Page**

1. Go to **SureCart menu**.
2. Locate the page named **Checkout**.
3. Click **Edit** to open it in the Block Editor.

### **Available Customization Options**

- Switch between **Test Mode** and **Live Mode**
- Reposition form fields, product selections, and order details
- Control which payment processors are displayed
- Configure conditional logic to show or hide elements
- Customize the order summary
- Add custom fields
- Set a custom thank-you page

## **Notes and Limitations**

- The Cart and Checkout Pages cannot be edited with Elementor or Bricks Builder.
- Changes to a product template apply to all products assigned to that template.

## **Related Documentation**

- [Getting Started with SureCart](https://surecart.com/docs/getting-started)
- [Product List Guide – Shop Page](https://surecart.com/docs/product-list-guide-shop-page/)
- [Product Pages Guide](https://surecart.com/docs/product-pages-guide/)
- [Edit Checkout Form](https://surecart.com/docs/add-checkout-form/)


===== SOURCE: see-abandoned-orders.md =====

---
source_url: https://surecart.com/docs/see-abandoned-orders
source: surecart-kb
scraped: true
---

# How to See Abandoned Orders - SureCart

## Overview

Abandoned orders occur when people add items to their cart but leave the website without finishing their purchase.

## Accessing Abandoned Orders

1. Navigate to **SureCart > Orders** in the WordPress Dashboard
2. Click the **"Abandoned"** submenu option under Orders

## Dashboard Sections

### Abandoned Checkout Stats

This section displays key metrics including:
- Recoverable Checkouts
- Recoverable Revenue
- Recovered Checkouts
- Recovered Revenue
- Checkout Recovery Rate
- Revenue Recovery Rate

These statistics are available across various time periods for performance analysis.

### Abandoned Checkout List

A detailed table showing all abandoned checkouts. Click "View Checkout" to access individual order details.

## Order Details Available

When viewing a specific abandoned order, you can access:

- **Cart Recovery Link**: A shareable link customers can use to return to their incomplete purchases
- **Checkout Details**: Product names, applied coupons, and total cart value
- **Customer Information**: View the customer's full profile by selecting "View Customer"

## Recovery Options

SureCart enables both manual recovery (sharing links directly) and automated processes through the Abandoned Checkout feature for systematic cart recovery campaigns.


===== SOURCE: set-dark-mode.md =====

---
source_url: https://surecart.com/docs/set-dark-mode
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Online Store](https://surecart.com/docs-category/online-store/)/How to Set Theme Styles for Dark Mode

# How to Set Theme Styles for Dark Mode

When your website has a predominantly dark background, it can be hard to get everything looking right.

To make it easy for SureCart users, we have created a dark mode theme that will automatically adjust your styles. The process to enable this option is quite simple. Just follow these steps.

- Navigate to the SureCart **Settings**.

- Head to the **Design & Branding** section and select **Dark** from this dropdown to apply dark mode to your website.

- Click on the **Save** button just below to apply these changes.

This will apply the dark mode to your website. We recommend using Dark mode only if your website has a dark background. Using dark mode on a website with a light background is not a good practice.

That's it! We hope this guide helps you. If you have any more questions or face any issues, feel free to reach out to our support team.


===== SOURCE: set-reply-to-email.md =====

---
source_url: https://surecart.com/docs/set-reply-to-email
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Email](https://surecart.com/docs-category/email/)/How to Set Reply To Email for Your Store

# How to Set Reply To Email for Your Store

SureCart lets you choose the sender name and reply-to email address for all store notifications sent from your store.

## Steps

1. Navigate to **SureCart → Settings → Notifications**.
2. Set your sender name and the email address that will be used as the reply-to email.
3. Click the **Save** button.

Every email your customers receive from your store will use this email address and sender name.


===== SOURCE: set-up-fee-on-trials.md =====

---
source_url: https://surecart.com/docs/set-up-fee-on-trials
source: surecart-kb
scraped: true
---

# How to Charge Set Up Fee on Trials

Here are the simple steps below to understand how to charge a setup fee on free trial plans.

- Let's create a new price. You can select installment or subscription. In this example, we'll choose a subscription.
- Activate the free trial.
- Activate the Setup Fee, you can also charge a Setup Fee alone without the need of a Free trial.
- Now, click to activate the "Charge setup fee during free trial". Once you're finished, click the "Create Price" button.

By following these simple steps, you've successfully added a free trial and incorporated the setup fee during the trial period for your product.

Now, to understand how this will appear for the customer, navigate to the checkout page and choose the pricing option accordingly.

You'll observe a message in the pricing selector indicating that the subscription will begin in 15 days, when the trial ends. You will also see the amount of setup fee on the checkout page.

Additionally, the total price will reflect the value of the setup fee.

After making the purchase, your customers can log in to their SureCart dashboard and see the purchase details.

In the Plans section, they will see a label indicating that the plan is under trial, along with the start date of their subscription.

Additionally, in the Order History section, they will observe a charge of $10 associated with the setup fee.

That's how easy it is to collect a setup fee and offer a free trial in SureCart.


===== SOURCE: set-up-your-branding.md =====

---
source_url: https://surecart.com/docs/set-up-your-branding
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Getting Started](https://surecart.com/docs-category/getting-started/)/How to Set Up Branding in SureCart

# How to Set Up Branding in SureCart

This document explains where SureCart applies brand colors and logos across the store, how to configure these settings, and how to remove the "Powered by SureCart" label from emails and invoices.

## **Requirements**

- WordPress admin access
- SureCart installed and activated
- A brand logo file (light and dark versions recommended)

## **Where Branding Appears**

Brand colors and logos configured in SureCart are applied across all customer-facing areas of the store:

- **Customer Dashboard** — login screen and dashboard interface
- **Checkout Pages** — hosted checkout and embedded checkout forms
- **Email Notifications** — order confirmations, receipts, subscription notifications
- **Invoices** — brand logo in the header

## **Configuring Brand Colors and Logo**

Brand colors and logos are configured in the Design & Branding settings. SureCart supports separate logo and color configurations for light mode and dark mode.

For complete instructions, refer to [How to Configure Email Logos for Light and Dark Mode](https://surecart.com/docs/light-and-dark-logo/).

## **Removing the "Powered by SureCart" Label**

1. Go to **WordPress Dashboard → SureCart → Settings**.
2. Open the **Design & Branding** tab.
3. Locate the option to remove SureCart branding.
4. Toggle the option on.
5. Click **Save**.

**Expected outcome:** After saving, the "Powered by SureCart" label no longer appears in the footer of new emails and invoices.

## **Notes and Limitations**

- Brand color and logo changes apply to new emails and invoices generated after saving. Previously sent emails and existing invoices are not updated retroactively.
- Dark mode support varies between email clients.

## **Related Documentation**

- [How to Configure Email Logos for Light and Dark Mode](https://surecart.com/docs/light-and-dark-logo/)
- [Customize Email Templates](https://surecart.com/docs/customize-email-templates/)
- [How to Set Reply To Email for Your Store](https://surecart.com/docs/set-reply-to-email/)


===== SOURCE: setup-custom-email.md =====

---
source_url: https://surecart.com/docs/setup-custom-email
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Email](https://surecart.com/docs-category/email/)/How to Set Up a Custom Email Address For Your Store?

# How to Set Up a Custom Email Address For Your Store?

By default, all email notifications sent to buyers have the email address set to **notifications@surecart.com**.

But there may be cases where you want everything white-labeled, meaning you want to edit the email sender to be an email address of your choice.

We have added this option to all premium plans and you can easily set this email address when you log into the SureCart platform and go into the Email settings.

Visit [app.surecart.com](http://app.surecart.com/) and log in to your account.

- Click on **Settings** and select **Email**.

- Click on the **Setup Custom Email Address** button.

- Enter the email address that you want here and click on the **Next Step:Verification** button.

To complete this process, you need to perform the following verification steps:

- **Verify your email address**: By now, you should have received an email on the entered email address. Please check your inbox and verify it.

If you did not receive any email, please click on the **Resend Verification Email** button.

- **Configure DKIM DNS**: Adding DKIM DNS is important because it verifies that emails come from genuine senders and haven't been tampered with, reducing the risk of fraud and spam.

To do this, you would typically need to access the DNS settings for your domain through your domain registrar's website or control panel.

Look for the option to manage DNS records or edit DNS settings. Then, paste the following TXT record with the provided Hostname and TXT Value.

Click on both the **Check DNS Records** buttons after adding these values to your domain.

**Note:** Checking DKIM is only necessary if you're using a new domain which wasn't connected to SureCart previously.

That's it! Once all verifications are complete, your new email address will be used for sending notifications to customers.

You can also remove this email address anytime by clicking on the **Remove Email Address** button at the top.

We hope this helped you. If you have any questions or face any issues with configuring DKIM DNS settings, reach out to our support team for assistance. We're here to help!


===== SOURCE: setup-donations-with-surecart.md =====

---
source_url: https://surecart.com/docs/setup-donations-with-surecart
source: surecart-kb
scraped: true
---

# How to Set Up a Donation/Pay What You Want in SureCart

SureCart has a few options for how to set up prices for your products or even collect donations for your fundraisers. This option is called the Pay What You Want option.

### **What is Donation/Pay What You Want**

Pay What You Want (PWYW) or Donation pricing is a flexible pricing strategy where customers have the freedom to determine the price they are willing to pay for a product or service.

Instead of a fixed or predetermined price, PWYW allows customers to choose the amount they believe the product or service is worth to them.

This approach is also sometimes referred to as "Pay What You Can" or "Donation."

### How to Set Up Donation in SureCart

SureCart allows the creation of a product form that provides multiple donation amounts from which the user can select an amount or enter a custom amount.

You will be able to allow donors to choose the amount they contribute, with a minimum amount.

- Log in to your WordPress dashboard and navigate to SureCart and Products. Click on the "Add New" button to create a new product.
- Add the name of the product and click on the create button. Once the product is created, click on the "Add a Price" button to add a price to your product.
- Let the Payment Type be One Time, now set a price and enable the button that says "Allow Customer to pay anything they want". This will ensure that the customer can donate any amount of their choice.

You can also select the minimum amount and maximum amount of the donation. If you would like to include the tax with the donation amount, enable the tax included button.

- Click on the "Create Price" button to complete the process.

That's it, you have successfully created the Donation/Pay What You Want Pricing in SureCart.

Next, you can set up a Donation Form and select the above-created product to create a donation form that you can share with your customers to collect payments for this product.


===== SOURCE: setup-installment-payment-type.md =====

---
source_url: https://surecart.com/docs/setup-installment-payment-type
source: surecart-kb
scraped: true
---

# How to Set Up Installment Payment Type in SureCart

SureCart has a few options for how to set prices for your products or services. One of them is called "Installment Payment Type."

### **What is Installment Payment Type**

Imagine you're selling a fancy phone worth $600 in your store. Normally, you can set up a one-time payment type to collect the complete amount for this phone at once.

Or you can create pricing with Installment Payment Type so your customers can pay the total amount of $600 in equal installments over a set period of time, like 6 monthly payments of $100.

This type of payment is called an "Installment Payment Type."

### **How to Setup Installment Payment Type in SureCart**

To set up the Installment payment type for your products:

- Go to the "Products" section. Click on "Add New" for the product you want to add.
- Enter your product details like Name, Description, and Images, and then under the Pricing section, click the "Add a Price" button.
- Enter the pricing name and choose the Payment Type as **Installment** for the product.
- Set up a price and add the repeat interval for the installments. Select how many installments to be charged for the product.
- Toggle the **Setup fee** option, if you want to collect any additional one-time fee from your customers when they make a purchase.
- Once you've made all the settings, review your prices and click the "Create Price" button.

Once you've created the pricing, you will notice the **Copy Links** option beside it. This option provides:

- Buy Link
- Add to Cart Button shortcode
- Buy Button Shortcode
- Price ID (for use with the SureCart API)

You can use these links and shortcodes on your block editor or even Elementor, Beaver Builder or other page builders to display this product to people on your website.


===== SOURCE: setup-one-time-payment-type.md =====

---
source_url: https://surecart.com/docs/setup-one-time-payment-type
source: surecart-kb
scraped: true
---

# How to Set Up One Time Payment Type in SureCart

SureCart has a few options for how to set prices for your products or services. One of them is called "One Time Payment Type."

### **What is One Time Payment Type**

Let's say you have a product to sell in your store where people can purchase the product by paying the complete amount at once, like a T-shirt. So this type of payment is called "One Time Payment Type".

### How to Set Up One Time Payment Type in SureCart

To set up one-time payment type for your products:

- Go to the "Products" section. Click on "Add New" for the product you want to add.
- Enter your product details like Name, Description, and Images, and then under the Pricing section, click the "Add a Price" button.
- Enter the pricing name and choose the Payment Type as **One Time** for the product.
- If you want to collect donations or want to set the price as "Pay What You Want", you can enable the "Allow customers to pay what they want" option.
- Review your prices and click the "Create Price" button.

Once you've created the pricing, you will notice the **Copy Links** option beside it. This option provides:

- Buy Link
- Add to Cart Button shortcode
- Buy Button Shortcode
- Price ID (for use with the SureCart API)

You can use these links and shortcodes on your block editor or even Elementor, Beaver Builder, or other page builders to display this product to people on your website.


===== SOURCE: setup-subscription-payment-type.md =====

---
source_url: https://surecart.com/docs/setup-subscription-payment-type
source: surecart-kb
scraped: true
---

# How to Set Up Subscription Payment Type in SureCart

SureCart has a few options for how to set prices for your products or services. One of them is called "Subscription Payment Type."

### **What is Subscription Payment Type**

Subscription payment type is a way to collect recurring payments from customers at a fixed interval of time.

For example, if you have a fitness app that costs $15 per month, you can set up a subscription payment type so that customers are automatically charged $15 every month.

### **How to Setup Subscription Payment Type in SureCart**

If you want to add a subscription payment type for an existing product, you can access the product from the Products page, then go to the Pricing section and click on "Add Another Price."

Or else if you are setting up a Subscription payment type for your new products, follow the steps below:

- Go to the "Products" section. Click on "Add New" for the product you want to add.
- Enter your product details like Name, Description, and Images, and then under the Pricing section, click the "Add a Price" button.
- Enter the pricing name and choose the Payment Type as **Subscription** for the product. Enter a price and select the repeat interval for the payment.
- If you want some flexibility for the price and set the price as "Pay What You Want", you can enable the "Allow customers to pay what they want" option.
- Toggle the **Setup Fee** option to collect any additional fee to set up an account for the users.
- Next, you have the option to provide free trials in this payment type. You can select days for which the free trials are made available with an option to charge the setup fee during this time period.
- Review your prices and click the "Create Price" button.

Once you've created the pricing, you will notice the **Copy Links** option beside it. This option provides:

- Buy Link
- Add to Cart Button shortcode
- Buy Button Shortcode
- Price ID (for use with the SureCart API)

You can use these links and shortcodes on your block editor or even Elementor, Beaver Builder, or other page builders to display this product to people on your website.


===== SOURCE: shipping-zone-methods-rates.md =====

---
source_url: https://surecart.com/docs/shipping-zone-methods-rates
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Online Store](https://surecart.com/docs-category/online-store/)/Managing Shipping Zone, Methods & Rates in SureCart

# Managing Shipping Zone, Methods & Rates in SureCart

SureCart offers versatile options for setting up shipping methods and rates to cater to different business requirements.

### **What is Shipping in SureCart?**

Shipping is a vital feature in SureCart that allows you to collect shipping charges from customers based on their desired delivery location.

With SureCart, you can provide multiple shipping methods to your customers, such as Expedited, Express, same-day delivery, and more.

You have the flexibility to set custom rates to meet various shipping requirements, including options based on item weight, flat rates, and order pricing.

### **How does Shipping work?**

SureCart offers three default shipping methods, each associated with different shipping speeds or classes that you can provide to your customers.

Within each zone, you have the flexibility to set a combination of shipping methods and their corresponding prices, giving you the ability to customize the shipping options for different geographic areas.

You can easily link your products with specific shipping profiles, and by default, all your products are assigned to the General profile.

Once customers make a purchase, they will be presented with the option to select their preferred shipping method during the checkout process, ensuring a smooth and tailored shopping experience for them.

### **What are Shipping Zones?**

Shipping zones are specific geographical locations where you can ship your products. Currently, the zones are determined based on countries.

### **What are Shipping Methods?**

Shipping methods are the speeds or classes of shipping your store offers. A shipping method refers to the process or way by which goods or products are transported from one location to another.

SureCart comes with three default shipping methods, but you can easily customize and change them according to your preferences.

### **What are Shipping Rates?**

Shipping rates are the prices you charge for shipping your products, and they are based on different pricing models such as Flat Rate, Based on item weight, and Based on order price.

### **How to Set up Shipping in SureCart**?

This step-by-step guide will walk you through the process of configuring shipping methods and rates using SureCart's intuitive interface.

Let's get started!

- To begin, from your SureCart dashboard, click on the "Settings" menu.

- Next, select the "Shipping" menu from the options.

- By default, the shipping profile will be set to "General." If you wish to create a custom profile, you can do so by upgrading your account to one of our premium plans. For now, click on the "General" menu to set your shipping methods and rates.

- You have the option to change the name of your shipping profile, but for now, let's keep it as it is.

By default, all your products will be listed under this profile, and any new products you add to your shop will automatically be added here.

**Important to note**: If you want to use a different profile for specific products, you can create a custom profile and add those products to it. For instance, if you have heavy items like a table, you can create a separate profile and assign that heavy product to it. Then, you can set a different shipping zone, method, and rate for that specific profile.

This way, you can have different shipping options for different types of products in your shop.

- To create our first zone, click on the "Create Zone" button.

Shipping zones are different areas where you deliver your products to customers, and you can set up different shipping rates for each zone.

- Type the zone name you want. For this, since we want the shipping to the United States, we will type "United States" in the Zone name field.

- In the "Select Countries" dropdown, start typing the country in which you want to provide shipping, and select it from the menu. Once you are done, click on the "Next" button.

When you start using SureCart, you'll find three default shipping methods available: Express, Standard, and Economy.

- In the "Shipping Method" dropdown, select one of the available options. Alternatively, you can create a new Shipping Method by clicking on the "Add New" button.

- Select how you want to charge the customers. We currently have three options: Flat Rate, Based on item weight, or Based on order price.

- Enter the price for the shipping rate, and once you are done, click on the "Add" button to save your changes.

- Now, let's go back and make our changes available in the frontend. To do this, click on the back arrow.

- Click on the Enable Shipping Rates toggle to activate it, and then click on the "Save" button to save your changes.

That's it! When your customers are checking out, they will see an option to select the shipping method if their address matches your shipping profile.

### **Conclusion**

SureCart's shipping module empowers you to create and customize shipping methods and rates tailored to your business needs. By following this step-by-step guide, you can efficiently configure your shipping options, ensuring accurate rates and a smooth checkout experience for your customers. Regularly review and update your shipping settings to adapt to changes in your business and customer demands.


===== SOURCE: slide-out-cart.md =====

---
source_url: https://surecart.com/docs/slide-out-cart
source: surecart-kb
scraped: true
---

# How to Enable & Disable Slide-out Cart

## Overview

The Slide-out Cart in SureCart functions as a shopping companion that appears when customers add products to their cart. This feature displays all items in the cart and allows customers to proceed with their order.

## For Non-FSE Themes

### Steps to Enable/Disable

1. **Access Settings**: Navigate to SureCart and click on Settings
2. **Select Design & Branding**: Click the Design & Branding option
3. **Locate Cart Section**: Scroll down to find the Cart section
4. **Toggle Enable Cart**: Turn the option on or off as needed

### Cart Icon Display Options

The Cart Icon Type dropdown offers three configurations:

- **Floating Icon Only**: Displays as a floating icon when items are added to cart
- **Menu Icon Only**: Shows the cart icon in the header menu; select specific menus where it should appear
- **Both**: Displays both floating icon and menu header icon simultaneously

### Additional Settings

- **Position for Cart**: Choose whether the cart displays right or left of the menu
- **Always Show Cart (Menu Only)**: Toggle to display the cart menu icon even when empty
- **Save Changes**: Click Save to apply all modifications

## For FSE (Full Site Editing) Themes

### Steps to Add Cart Menu Icon

1. **Access Customize**: Go to WordPress Appearance > Customize
2. **Navigate to Template Parts**: Click Template Parts option
3. **Select Header**: Choose Header from available options
4. **Edit Header**: Click Edit button
5. **Add Block**: Insert a new block and search for "Cart Menu Icon"
6. **Insert Block**: Click the Cart Menu Icon block
7. **Save**: Click Save to apply changes

### Alternative Method

For themes where the Cart Menu Icon block does not function properly, utilize the Cart Menu Icon shortcode as an alternative solution.


===== SOURCE: stop-sending-woocommerce-notifications.md =====

---
source_url: https://surecart.com/docs/stop-sending-woocommerce-notifications
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Troubleshooting](https://surecart.com/docs-category/troubleshooting/)/How To Stop Sending WooCommerce Notifications via SureCart?

# How To Stop Sending WooCommerce Notifications via SureCart?

If you're using WooCommerce to power your e-commerce store along with SureCart, you may want to customize or disable certain notifications that are sent to your customers by SureCart.

These notifications can include order confirmation emails, refund notifications, and other messages related to their purchase.

In this document, we will explain how you can stop the notifications that are sent from SureCart.

- Log in to your WordPress dashboard and click on SureCart and select Settings.

- Click on the Notifications tab to access the notifications settings.

- Choose the emails that you would like to send to the customers via SureCart by clicking on the Radio Buttons next to each email settings.

Finally, click on the **Save** button and the respective SureCart notifications will be turned off.

We hope this guide helped you. If you have any questions, please don't hesitate to reach out to our support team. We're here to help!


===== SOURCE: store-transfer.md =====

---
source_url: https://surecart.com/docs/store-transfer
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Online Store](https://surecart.com/docs-category/online-store/)/How to transfer a store to a new organization and assign a license.

# How to transfer a store to a new organization and assign a license.

On the SureCart platform, you can transfer a store from one organization to another. In this documentation, we will guide you through this process and explain how to apply a license to the store.

Store to Transfer:

- Open the SureCart platform and select the store you want to transfer

- Navigate to the General tab and scroll down to the "Transfer Store" button.

- In the pop-up window, select the destination organization where the store will be transferred. and hit the Transfer button.

That it, your store is now transferred to another organization.

Now that your store has been transferred to another organization, we can proceed with applying one of the store licenses. Let's follow these steps.

- Click on Organization Settings to access organization setting of that store.

- Open the Plans & Billing of the organization

- Here you will see an option to apply license for your store.

- Use the **Assign Store** license button to open a popup with the options to apply your license to the stores.

On this popup, you will see all stores of this organization including one that we moved recently, use the **Assign** button to assign a license to that store.

That's it! Now you know how to transfer stores between organizations and assign licenses to them. If you have any further questions, feel free to reach out to us through the available support channels.


===== SOURCE: stripe-application-fee.md =====

---
source_url: https://surecart.com/docs/stripe-application-fee
source: surecart-kb
scraped: true
---

# What Is the "SureCart Application Fee," and Why It's Not an Extra Charge

When using Stripe with SureCart, you may notice a line item labeled **"SureCart Application Fee"** on subscription transactions.

- If you sell subscriptions with Stripe, there is always a subscription fee involved, no matter what tool you're using.
- With most platforms, that fee goes directly to Stripe.
- With SureCart, that fee appears as a **SureCart Application Fee**, because SureCart provides its own subscription management system.
- Your overall costs remain the same; you're simply paying SureCart instead of Stripe for this part of your subscription business.

### **Why That's Better for Your Reporting & Accounting**

- **No extra fees** – The SureCart Application Fee replaces the subscription fee you would otherwise pay directly to Stripe.
- **Transparency** – Your Stripe payment processing fees remain visible in Stripe, while the subscription fee is shown separately under SureCart.
- **Simplified bookkeeping** – You can clearly distinguish which fees go to Stripe (payment processing) and which go to SureCart (subscription management).
- **Supports ongoing innovation** – This model allows SureCart to keep building and supporting features that make running a subscription business easier.

### **Comparison Table**

| Transaction Type     | Stripe Processing Fee   | SureCart Application Fee                 |
| -------------------- | ----------------------- | ---------------------------------------- |
| One-Time Purchase    | Yes (charged by Stripe) | No                                       |
| Subscription Payment | Yes (charged by Stripe) | Yes (replaces Stripe's subscription fee) |

### **Detailed Breakdown**

#### **Stripe's Fee Structure**

Whenever you sell subscriptions using Stripe, there are two types of fees involved:

- A **standard processing fee** (e.g., 2.9% + 30¢ in the U.S.), and
- A **subscription-related fee** for managing recurring payments.

With most platforms, both of these fees are charged directly by Stripe.

#### **How SureCart Works Differently**

With SureCart:

- You still pay Stripe's **standard processing fees**, as usual.
- You do **not** pay Stripe's subscription fee because SureCart manages subscriptions directly.
- Instead, you'll see a **SureCart Application Fee** that reflects this same cost, just shown under SureCart rather than Stripe.

This means your total fees are the same, but the label is different.

### **Why SureCart Built Its Own Subscription System**

SureCart manages subscriptions inside its own platform so you can take advantage of Stripe's reliability while unlocking features that wouldn't otherwise be possible, such as:

- **Reactivate canceled subscriptions** – Bring a customer back without forcing them to start over.
- **Switch payment methods, even across processors** – For example, allow a customer to move from a credit card on Stripe to PayPal.
- **No manual syncing of products and prices** – With SureCart, everything lives in one place.
- **More flexibility for your business** – SureCart can keep improving with features like upgrades, downgrades, proration rules, and customer-friendly tools.

### **Summary**

The **"SureCart Application Fee"** is not an extra charge. It is simply the subscription fee you would always pay when selling subscriptions with Stripe, only shown under SureCart instead of Stripe.

You still:

- Pay Stripe for **payment processing**, and
- Pay SureCart the equivalent of Stripe's subscription fee, as the **SureCart Application Fee**.


===== SOURCE: stripe-credit-card-using-wrong-zip.md =====

---
source_url: https://surecart.com/docs/stripe-credit-card-using-wrong-zip
source: surecart-kb
scraped: true
---

# Stripe Credit Card Field Is Using The Wrong Zip Code - SureCart

## Summary

When testing purchases in SureCart, users may encounter issues inputting non-U.S. zip codes. Stripe determines the billing address country using the card number and validates postal code formats accordingly.

## Key Points

**The Core Issue:**
Many test cards default to U.S. billing addresses, which only accept five-digit numeric codes (like 12345). This limitation isn't a SureCart bug but rather Stripe's validation based on the card's country origin.

**Solution:**
- Use proper five-digit U.S. ZIP codes when testing with American test cards
- Switch to international test card numbers from Stripe's testing documentation to validate different postal code formats (alphanumeric for UK cards, etc.)

**Why This Happens:**
Different countries have different postal code requirements: some require numeric-only formats, others allow alphanumeric characters, and some may not require them at all. Stripe enforces these rules based on the card's detected country.

Users experiencing ongoing issues are encouraged to contact SureCart's support team for additional assistance.


===== SOURCE: subcription-in-customer-dashboard.md =====

---
source_url: https://surecart.com/docs/subcription-in-customer-dashboard
source: surecart-kb
scraped: true
---

# How to Allow Customers to Manage Their Subscription Plans

## Overview

SureCart enables store owners to grant customers control over their subscription management directly from their customer dashboard. This eliminates the need for customers to contact support for routine subscription modifications.

## Enabling Subscription Management

To allow customers to manage their subscriptions:

1. Navigate to **SureCart**
2. Access the **Settings** section
3. Select **Subscription**

## Available Subscription Management Options

### Allow Subscription Changes

This setting permits customers to switch pricing plans directly from their customer portal. When enabled, subscribers can upgrade or downgrade between different subscription tiers without merchant intervention.

### Allow Subscription Quantity Changes

When activated, this feature allows customers to directly modify the number of subscriptions they have through their customer portal. This eliminates the need for repurchasing plans when adjusting quantities.

### Allow Subscription Cancellations

Enabling this option lets customers cancel their subscriptions from their customer portal. Subscribers can independently terminate their plans using a dedicated cancellation button in their dashboard.

## Customer Experience

Once these settings are enabled, customers access all subscription management functions through their personal dashboard. The process is streamlined and user-friendly, requiring no merchant assistance for standard subscription modifications like upgrades, downgrades, quantity adjustments, or cancellations.


===== SOURCE: subscription-insights.md =====

---
source_url: https://surecart.com/docs/subscription-insights
source: surecart-kb
scraped: true
---

# Understanding Subscription Insights - SureCart

## Subscription Metrics Terms

**Total Subscription**: The total number of active subscriptions your business currently has. Includes both new and existing subscriptions.

**New Subscription**: Count of newly created subscriptions during a specific period.

**New Trials**: The number of subscriptions in a trial period within a selected time frame.

**MRR (Monthly Recurring Revenue)**: The total revenue your business generates from subscription fees on a monthly basis.

**MRR Lost**: Revenue lost due to cancellations, downgrades, or churn.

**Outstanding Installments**: Total value of unpaid installment payments.

## How MRR is Calculated

The calculation method varies by subscription type:

- **Monthly subscriptions**: MRR = SUM(active subscriptions x monthly cost)
- **Annual subscriptions**: MRR = SUM(active subscriptions / 12)
- **Daily subscriptions**: MRR = SUM(active subscriptions x 30.436875)
- **Weekly subscriptions**: MRR = SUM(active subscriptions x 4.348125)

The multipliers 30.436875 and 4.348125 represent the average number of days and weeks in a month, taking into account a time span of 100 years, including leap years.

### Example Calculation

A sample with 3 monthly ($30/month), 2 annual ($120/year), and 5 daily ($2/day) subscriptions yields: MRR = $231.75/month

## Live Mode and Test Mode

Analytics metrics can be toggled between Live Mode (default) and Test Mode with a single click.

## Quick Filter

Date range filters are available for common periods like current week.

## Subscriptions Table

A table displays all subscriptions with filters for: All, Active, Trialing, Past Due, and Canceled statuses.

## FAQ

**Q: How are metrics calculated for annual subscriptions?**
Divided by 12 monthly; a $300 annual subscription shows as $25 MRR.

**Q: Are installments included in Total Subscriptions and MRR?**
No, installments are tracked separately under "Outstanding Installments."

**Q: How can MRR Lost data help businesses?**
Understanding revenue loss helps identify causes and implement improvements to reduce churn.

**Q: What subscription warning signs should businesses monitor?**
High churn rates, stagnant MRR, and unexpected fluctuations.


===== SOURCE: subscription-saver.md =====

---
source_url: https://surecart.com/docs/subscription-saver
source: surecart-kb
scraped: true
---

# How to Set Up Subscription Saver - SureCart

## Overview

SureCart's Subscription Saver is a retention tool that engages customers during the cancellation process. When customers attempt to cancel, they encounter a feedback form explaining their reasons, potentially leading to discount offers that encourage them to remain subscribed.

## Enabling Subscription Saver

1. Navigate to WordPress Dashboard > SureCart > Settings > Subscription Saver
2. Enable "Subscription Saver & Cancelation Insight"
3. Click Save

## Configuring the Cancellation Survey

### Survey Answer Options

Customize the cancellation reasons customers see by:

- Using pre-populated default options or modifying them
- Clicking "Add New" to create custom reasons
- For each reason, specify:
  - **Label**: Customer-facing text
  - **Offer Discount**: Toggle to present discount upon selection
  - **Request Comments**: Enable additional feedback with customizable prompt text

### Survey Form Settings

Personalize the modal popup with:

- **Title**: Main heading text
- **Description**: Brief explanatory text
- **Skip Link**: Text for skipping the survey

Use the Preview button to review appearance before saving.

## Renewal Discount Configuration

Set up incentive offers with these parameters:

- **Discount Type**: Percentage or fixed amount
- **Duration**: Forever, once only, or multiple months
- **Usage Limit**: Per-customer usage restrictions (blank = unlimited)
- **Modal Text**: Customizable title, description, button, and cancellation link

## Results and Insights

After implementation, survey data appears in the SureCart Dashboard under Subscriptions > Cancellation section, providing valuable retention metrics.


===== SOURCE: surecart-abilities.md =====

---
source_url: https://surecart.com/docs/surecart-abilities
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/How to Get the Most Out of SureCart Abilities

# How to Get the Most Out of SureCart Abilities

This document explains how to use SureCart Abilities effectively to manage a store through AI assistants like Claude, ChatGPT, Cursor, and others. With Abilities enabled, common store operations can be completed in a single conversational request.

## **Quick Setup Reminder**

Before using Abilities, the MCP Adapter must be installed and an AI client connected. The full setup is available at WordPress Dashboard → SureCart → Settings → MCP.

## **Why Use Abilities**

Many routine store tasks involve repetitive UI navigation. With Abilities, these same tasks can be completed by describing the goal in plain language to an AI assistant.

The biggest gains come from tasks that require:

- Multiple steps across different sections of the admin
- Searching or filtering through long lists
- Performing the same action on several records
- Combining data from different parts of the store

## **Practical Use Cases**

### **Use Case 1: Extending a Subscription Renewal Date**

```
Find the active subscription for customer@example.com and extend the renewal date by 7 days.
```

### **Use Case 2: Creating an Invoice for a Custom Order**

```
Create an invoice for John Doe (johndoe@example.com) for the
"Premium Course" product, due on 2026-06-15, and send it to him.
```

### **Use Case 3: Reviewing Recent Store Performance**

```
Show me my store performance for the last 30 days.
Include total revenue, active subscriptions, and the top 5 products by sales.
```

### **Use Case 4: Bulk Coupon Creation for a Campaign**

```
Create three Black Friday coupons:
- BF10 for 10% off, valid Nov 24-28, max 500 uses
- BF20 for 20% off, valid Nov 25-27, max 200 uses
- BF30 for 30% off, valid Nov 26 only, max 50 uses
```

### **Use Case 5: Issuing a Partial Refund**

```
Issue a 50% refund on the most recent order for customer@example.com
with the reason "partial product issue".
```

## **Tips for Better Results**

- **Be Specific with Identifiers** — use customer email, full product name, dates in YYYY-MM-DD format
- **State the Goal, Not the Steps** — describe the desired outcome rather than each step
- **Specify Variants** — for products with multiple variants, include the variant name
- **Confirm Before Destructive Actions** — add "and confirm before applying" for deletions/refunds

## **Permissions and Safety**

The MCP settings page includes three permission toggles:

- **Enable Abilities** — Master switch for all AI access
- **Enable Edit Abilities** — Allows creating and modifying data
- **Enable Delete Abilities** — Allows permanent deletion of data

## **Notes and Limitations**

- AI assistants follow the permissions configured in MCP settings.
- Multi-variant products require the variant to be specified in the prompt.
- Destructive actions (deletions, refunds, cancellations) typically prompt for confirmation before execution.


===== SOURCE: surecart-affiliate-platform.md =====

---
source_url: https://surecart.com/docs/surecart-affiliate-platform
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Affiliate Platform (for merchants)](https://surecart.com/docs-category/affiliates-for-merchants/)/SureCart Affiliate Platform

# SureCart Affiliate Platform

In this article, we will guide you through the Affiliate Platform. This platform empowers users to join as affiliates, promoting your products and earning rewards for each successful sale.

We'll walk you through each feature, step by step, revealing simple yet impactful ways to maximize your affiliate experience and boost your earnings.

## **What is an Affiliate Platform?**

An affiliate platform is like a meeting place. It connects sellers who want to sell more with people who want to help sell their stuff.

These helpers, called affiliates, earn rewards when they bring in customers or make sales. The platform gives affiliates special links to track their work, making sure they get paid for what they do.

It helps sellers reach more people without spending lots of money upfront. They team up with affiliates who use different online ways to show the seller's stuff to more folks.

Overall, it's a win-win: sellers sell more, and affiliates earn rewards for helping them out.

## **Merchant Settings**

Before anything else, you need to configure your affiliate settings where you will define the Affiliate Signups, Referral Tracking, and Commissions and payouts.

Let's get started.

- To begin, log in to your WordPress dashboard using your credentials.
- Then, navigate to **SureCart** > **Settings**, and **Affiliates**.

### **Affiliate Signups**

This is where you set up how affiliates sign up and get approved to promote products in your store.

- To enable new affiliate signups, toggle the **Allow New Affiliate** Signups switch.

- Complete the Program Description field. This is where you usually specify how the affiliate program works or how much commission you will provide to your affiliates.

- If you wish to automatically approve new affiliates, simply enable the **Auto Approve New Affiliates** toggle.

- Click on the **Save** button in the top right corner of your screen to save your changes.

The Signup URL is where your affiliates will sign up for the affiliate program. To **modify** it, follow the steps below.

- Login at [app.surecart.com](http://app.surecart.com/) and select your store. Then, go to the "Store".
- Change the **Store ID / Subdomain**, ensuring it contains only letters, numbers, and dashes. Click the **Save** button to apply these changes.

- Return to the Affiliates menu, and you'll notice that your Signup URL has been changed.

- The **Signup Question** field asks the affiliates questions during the signup process. If you leave it blank, the default question "How will you promote this store?" will be used.

- You can enter the URL to your Terms & Conditions page here. This page will be shown to affiliates after signing up.

- The payout email is where affiliates get their commission payments. If enabled, this will include a separate payout email field on the signup form itself.

### **Referral Tracking**

This is where you'll set up how clicks are tracked and how affiliates get credit for referrals.

Before we start, let's clarify some terms.

**Referrer Type**: This determines which affiliate should get credit for a sale if a customer has clicked multiple affiliate links. The first referrer means the first affiliate link to be clicked will get credit, and the last referrer means the last affiliate link to be clicked will get credit.

**Tracking Length**: Also known as the "cookie duration", this is how long a special code (called a cookie) stays on someone's device after they click an affiliate link. It's like a small marker that remembers they came from an affiliate's link.

This time matters because if someone clicks an affiliate link and buys something within that time, the affiliate still gets recognized for the sale.

For instance, if the tracking length is 30 days, it means that if someone clicks an affiliate link and buys something from that store within the next 30 days, the affiliate will receive a commission for that sale.

**Tracking Script**: The tracking script is a small snippet of code that helps an affiliate platform keep track of who sends customers to a store's website. The tracking script must be present on all sites where affiliate links should be tracked.

If a store uses SureCart V.2.10.0 or later, they don't need to worry about setting up this tracking code. It's handled automatically by the system through a single toggle that can enable or disable it.

Now that you understand how it works, let's set them up:

- Enable "Tracking" to add a tracking script to this site.

- In the Referrer type, choose **which** referrer should receive credit. If you prefer the default option, which is Last, there's no need to make changes. However, if you want the referrer who initiated the first interaction to get credit, click on the dropdown menu and select First.

- Set the Tracking Length in days for when you want to credit the referrer.

- In the **Affiliate Referral URL** field, enter the address where you want your affiliates to direct traffic.

- Decide whether you want to approve new referrals automatically or not.

### **Commissions & Payouts**

This is where you set up how affiliates earn commissions and receive their payments.

**Commission**: A commission is like a "thank you" reward. When someone helps to sell things for a store by bringing in customers or making sales happen, the store gives them a part of the money earned as a way of saying thank you.

**Subscription Commissions**: A subscription commission is like a repeating thank-you bonus for affiliates. If they bring in customers who sign up for services that people pay for regularly (like every month), the affiliate keeps getting a bonus each time those customers pay.

**Lifetime Commissions**: Lifetime commissions mean an affiliate keeps getting bonuses for all the shopping a customer does in the future, not just the first time they buy something.

Now that you understand the basics of how it functions, let's configure the settings.

- Enter the commission amount you wish to pay your affiliates, and then select whether it's a percentage or a flat rate.

- To reward affiliates for renewal subscriptions, switch on the **Subscription Commissions** toggle.

- If you wish to limit the time that subscription commissions are awarded, you can set this in the designated field for the number of days. For example, setting the field to 365 would mean that affiliates are only awarded commissions for 1 year after the subscription starts.
- If you don't wish to limit the time a subscription commission is awarded, you can leave the field blank.

- To reward affiliates for future purchases, switch on the **Lifetime Commissions** toggle.

- If you prefer to award commissions to the affiliate for a specific period after a customer's purchase, you can set this duration in the number of days.
- If you wish to provide commissions indefinitely, you can leave the field blank.

- Finally, write a Payout Instruction so that your affiliates understand your terms and conditions for receiving their payments.

That's it! Hope this article was helpful. If you need more information, please feel free to reach out to us.

### **Frequently Asked Questions**

**The user is approved on the Requests tabs but is not becoming an affiliate, why?**

To transition from the Requests tab to the Affiliate tab, a user needs to complete the affiliate setup process.

Upon approval, whether automatically or manually, the affiliate receives an email prompting them to finalize their affiliate setup by registering. Once this step is completed, they officially become an affiliate.

**The user is also a SureCart store owner. Can they become an affiliate of another store?**

Absolutely! Any store owner has an affiliate platform and can also become an affiliate of any SureCart affiliate store.

For a seamless experience, this store owner needs to use the same email address they used for their store.

**Why my test purchases are not being tracked**?

Currently, the affiliate platform is only tracking live purchases.

We are considering making this feature available in the test mode in the future!

**How to make a payout**?

Right now, the platform lists payouts for merchants to handle manually. Soon, will be able to make things easier by creating CSV files. We're also planning to automate this process to make it smoother.


===== SOURCE: surecart-glossary.md =====

---
source_url: https://surecart.com/docs/surecart-glossary
source: surecart-kb
scraped: true
---

# SureCart Glossary

Common terms and definitions used in SureCart.

## Terms Related to Store Settings

### Store Name

Your store's identity. The name that customers see when visiting your online store, and what appears in notifications or messages they receive.

### Store URL

A unique web link that takes customers to your online storefront. Added to email notifications, invoices, and various messages. Won't change or affect your main website address.

### Default Currency

The starting point when setting new prices for products in SureCart. All products created in SureCart will have prices set in the default currency by default.

### Store Language

The language used for all messages, notifications, invoices, and communications sent from your store to customers.

## Terms Related to Design and Branding

### Brand Color

Your store's signature hue. SureCart uses this color for main buttons, links, and various parts of the user interface.

### Select Theme

The style and mood of your checkout forms. Choose between dark and light themes to match your website's design.

### Floating Cart

A virtual shopping basket that appears on the side of the screen when items are added. Provides a smooth shopping experience.

### Cart Menu Icon

The shopping cart symbol placed anywhere on your website (widgets, menus, headers, footers). Shows customers what they've added to their cart.

## Terms Related to SureCart Blocks

### Cart Toggle Icon

Adds a cart icon to your checkout page showing the number of items in the cart. The icon can be a shopping cart or shopping bag.

### Store Logo

Allows adding a store logo to your page. Displayed at the top by default; customizable.

### Buy Button

Redirects the customer to another product's checkout page with that product added to the cart automatically. Can link multiple products.

### Add To Cart Button

Customers can click to directly buy a different product on the same checkout page (unlike the Buy button which takes customers to a different checkout).

### Logout Button

A button for customers to sign out of their account.

### Order Confirmation

Displays a confirmation message to customers after they buy your product.

### Customer Dashboard Button

Adds a button that leads your customer to their customer dashboard account.

### Cart Blocks

Adds cart-related items such as cart coupons, cart subtotal, display messages. Sub-blocks are only available after adding this Cart block item first.

### SureCart Columns

Lets you organize and design your page better by adding columns (50/50, 70/30, etc.).

### Product List

Lets you design and display the products your store has.

## Terms Related to Orders and Receipts

### Order Number Prefix

A unique label for your orders. Set this prefix to help organize and identify them in invoices, order history, and listings.

### Order Numbers Counter

The numbering system for orders (e.g., 001, 002, 003 or custom alphanumeric patterns).

## Terms Related to Abandoned Checkout

### GDPR

The General Data Protection Regulation — an EU Regulation. SureCart provides GDPR compliance settings that show confirmation text below the email on checkout forms.

### Discount Duration

How long a special offer or discount coupon is valid for a particular user:
1. **Once**: The discount applies one time only
2. **Forever**: The discount is available indefinitely
3. **Repeating**: The discount renews for a specific number of months

### Discount Expires

The countdown clock for a special offer — the time limit for how long a discount can be used before it becomes invalid.

### Grace Period

A period of time (in days) that kicks in after a customer makes a purchase. Gives customers a moment before sending abandoned checkout notifications, preventing accidental abandoned cart triggers right after a purchase.

## Terms Related to Subscriptions

### Customer Portal

A personal space for customers within your online store where they can:
- View order history
- View active plans
- Update personal information and address
- Manage passwords
- Manage payment information

### Subscription Saver

A customer retention feature that activates when a customer wants to cancel their subscription. It asks why they want to cancel and may offer a renewal discount or incentive to keep their subscription active.

## Terms Related to Shipping

### Shipping Profile

A set of rules and instructions for getting products shipped to customers. Organizes destinations and shipping fees for different locations.

### Shipping Method

The transportation options your store provides for delivery. SureCart provides three default shipping methods that can be customized.

## Terms Related to Payment Processors

### Payment Processor

The financial bridge connecting your online store to customers' payment methods. Checks that payment details are valid, sufficient funds exist, and processes the transaction.

### Manual Payment Methods

Offline or non-digital payment methods (e.g., cash on delivery). Payments are made outside the online checkout process and require manual processing by the store owner.

## Terms Related to Connection

### API Token

A secret key that lets SureCart and WordPress communicate safely and securely with each other.

## Advanced Settings Terms

### Stripe Payment Element

An embeddable form for securely collecting payment details. Simplifies payment collection, boosts security, and provides flexibility for customers.

### Sync Customers

Connecting SureCart and WordPress so they share information. Required for integration with third-party apps like LearnDash, LifterLMS, TutorLMS, and more. Ensures customers have appropriate WordPress user roles.

### Clear Test Data

Removes all test users, fake orders, and trial subscriptions from your store in one click. Provides a clean slate before going live.

## Terms Related to Forms

### Checkout Form

The digital equivalent of a cashier's counter. A customizable online form where customers enter shipping address, payment details, and contact information. Also displays product pricing, allows quantity adjustment, product removal, and coupon application.

### Instant Checkout

A dedicated page for one specific product. Customers go straight to this page to buy that item without browsing the entire store.

## Terms Related to Orders

### Manual Order

A feature that lets store owners place orders on behalf of customers, selecting products and then sending the bill to the customer.

### Fulfillment

The complete process from when a customer clicks "buy" to delivery:
- Order management and verification
- Tracking code assignment
- Fulfillment status updates (Not Shipped, Shipped, Delivered)

## Terms Related to the SureCart Platform

### SureCart Platform

The backend infrastructure of your online store. Handles:
- Data hosting (products, orders, customer information)
- Logic and processing (prices, inventory, order processing)
- Request handling for a smooth shopping experience


===== SOURCE: surecart-multisite.md =====

---
source_url: https://surecart.com/docs/surecart-multisite
source: surecart-kb
scraped: true
---

# Using SureCart on a WordPress Multisite

Setting up SureCart on a WordPress Multisite can be a little different compared to a normal WordPress site. To make sure it works perfectly, you'll need to follow a few key steps.

### Recommended Setup

The first thing to know is that SureCart works best with a **subdomain-based Multisite setup**. This means your sites will look like "store.example.com", not "example.com/store".

SureCart is designed to run independently on each subsite. If you try using a subfolder-based multisite or activate the plugin across the entire network, it can lead to conflicts or unexpected issues.

You should also **avoid network activating SureCart**. Instead, only activate the plugin on the specific subsite where you plan to run your store.

### What to Do If You're Using a Subfolder-Based Multisite or Already Activated SureCart on the Network

If you've already set up your multisite using subfolders (e.g., "example.com/store") or activated SureCart network-wide, follow these steps:

- **Switch to a Subdomain Setup**: First, you must convert your Multisite setup from subfolders to subdomains. WordPress has plenty of guides to help you make the switch.
- **Deactivate SureCart from the Network**: Once you've updated to a subdomain-based setup, log in to the Network Admin area and deactivate SureCart from the entire network.
- **Clean Up Unnecessary Pages**: SureCart might have created pages like the **Customer Dashboard** and **Checkout page** on the main site or other subsites. You should delete these to prevent any leftover configuration issues.
- **Reactivate SureCart Only Where Needed**: Go to the specific subsite where you want the store and activate SureCart there only.

### Why Does All This Matter?

SureCart is built to work in a specific way for Multisites. When you stick to a subdomain setup and activate the plugin only on the store subsite, you'll avoid configuration problems, plugin conflicts, and unexpected errors.

If you don't follow these steps, you might notice issues like pages not working correctly, features behaving oddly, or even the store not loading as expected.


===== SOURCE: surecart-product-types.md =====

---
source_url: https://surecart.com/docs/surecart-product-types
source: surecart-kb
scraped: true
---

# What Types of Products Can I Create in SureCart?

SureCart allows you to collect payments for any product you want to sell, ranging from physical products to digital products and services. Here's a quick rundown of the kinds of products you can sell with SureCart:

- **Digital Products** – Ideal for online courses, learning management systems, or access groups.
- **Downloadable Products** – Perfect for any type of downloadable files, such as ebooks, PDFs, audio, or video files.
- **Physical Products** – From straightforward physical items to variable products, SureCart seamlessly handles a wide range.
- **Subscription Products** – Designed for selling subscription-based products, allowing you to set up recurring billing effortlessly.
- **Licensed Products** – Tailored for those selling licensed products like applications, themes, plugins, or any software type.
- **Affiliate Products** – A newly added feature in SureCart that supports the affiliate platform, empowering you to boost sales through affiliate marketing.

### **Physical Products**

For the average E-commerce store, the most commonly used product type is the Physical product.

SureCart is great for selling physical products as it comes with all the features you might need:

- **Inventory Management** – Product inventory, in brief, is the number of items ready for sale. In SureCart, you can monitor the quantity and attach a SKU (Stock Keeping Unit) to your products.
- **Variations** – A product variant is essentially a distinct version of a product (e.g., Shoes available in different colors and sizes).
- **Cash on delivery/Manual Payment Modes** – Manual payment methods are important in e-commerce, especially when online payments aren't possible.

### **Digital Products**

SureCart can also help you sell digital products like e-books, music files, or online courses easily.

Key features:

- **Integrations with learning platforms** – Direct integration with learning platforms like LearnDash, TutorLMS, and more.
- **Integrations with membership groups** – Manage content restrictions by integrating with content restriction plugins.
- **Easy way to manage downloadable products** – Attach downloadable files directly to the product; after purchase they are immediately available for download.
- **Send licenses with purchase** – If you are selling products that require licensing, SureCart provides an all-in-one licensing solution.

### **Downloadable Products**

Downloadable products come in various file types that you can easily download from the internet, such as a PDF document, an image, or a software program.

A downloadable product can be either virtual or physical. Creating a downloadable product in SureCart is simple:

- Start by creating a new product
- Fill in the necessary information including title, description, price
- In the middle part of the product creation page, add your downloadable files

SureCart supports various file types, including images, PDFs, and more. You can store downloads in your secure SureCart store, or in your preferred file storage (Google Drive, Dropbox, etc.).

### **Subscription Products**

One effective way to ensure steady revenue for your store over a long period is by accepting recurring payments.

For example, if you have a fitness app that costs $15 per month, you can set up a subscription payment type so that customers are automatically charged $15 every month.

Key subscription features:

- **Offer trials** – Add a trial period so customers can try out your stuff before they subscribe.
- **Subscription Saver** – When a customer decides to cancel their subscription, it gives them a feedback form and offers immediate discounts.
- **Pay what you want** – Allow customers to pay what they want instead of a predefined price.
- **Track useful subscription metrics** – Monitor key business metrics.
- **Upgrades and downgrades** – Easy options for upgrading, downgrading, or canceling subscriptions.
- **Subscription management** – Manually create new subscriptions for users, pause, cancel, and resume subscriptions.

### **Licensed Products**

With SureCart Business and Pro plans, you can get an add-on for the software licensing platform. This allows you to sell any software that needs licensing.

After a customer makes a purchase, they will receive a unique key via email. You can utilize SureCart's APIs and SDKs to verify if the license was generated by SureCart.

Benefits of Using SureCart License feature:

- **Automate license creation**: SureCart automatically generates unique license keys for each customer purchase.
- **Offload update checks and downloads**: SureCart handles resource-intensive tasks like update checks and downloads.
- **Seamless integration**: The License Addon integrates seamlessly with the SureCart plugin.
- **Simple setup**: Get started quickly with the provided WordPress SDK.


===== SOURCE: switching-payment-processors.md =====

---
source_url: https://surecart.com/docs/switching-payment-processors
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Payments](https://surecart.com/docs-category/payments/)/Switching Payment Processors

# Switching Payment Processors

When switching payment processors or connecting new accounts in SureCart, it's important to understand how subscriptions and payment methods will be impacted. This guide will walk you through the key points to consider and how to manage existing and new payment methods.

#### Key Concepts:

- **Active Mode (Test/Live):** While you can connect multiple Stripe accounts, you cannot have more than one mode (Test or Live) active at the same time. For example, you can have Live mode from one account active while Test mode is active on another.

- **inactive Processor**: A processor can be disabled while still connected to SureCart. In this state, it will not accept new payment methods, but existing subscriptions linked to that processor will continue to renew normally.

### Managing Existing Subscriptions

- **New Payment Methods**: When a new processor is activated, all new payment methods and subscriptions will be linked to that processor. However, existing subscriptions will continue using the payment method stored with the previous processor.
- **Existing Subscriptions**: Even if a processor is disabled, existing payment methods connected to it will still be charged. This ensures a smooth transition for ongoing subscriptions without service disruption.

### How to Change Processors in SureCart:

1. Go to the **Processors** page in your SureCart dashboard.

1. You can enable or disable processors as needed. When a processor is disabled, it will still handle renewals for existing subscriptions, but new payment methods will not be associated with it.
1. If you want all new payment methods to go to a new processor, ensure the new processor is **active** and the previous one is **disabled**. Remember, only one **mode** (Test or Live) can be active at a time.

For further assistance with migrating or managing payment processors, contact SureCart support.


===== SOURCE: switching-store-currency.md =====

---
source_url: https://surecart.com/docs/switching-store-currency
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Settings](https://surecart.com/docs-category/settings/)/Switching Store Currency

# Switching Store Currency

Your store currency determines the currency used for all transactions, pricing, and reporting in SureCart. While it is possible to change your store currency, doing so has significant implications you should understand before proceeding.

## What happens when you switch currency?

1. **Future Orders** — All new orders will be processed in the new currency.
2. **Prices Missing** — Prices are **not** automatically converted to the new currency. After switching, you will need to manually update all product prices. Until you do, products may not have valid prices and will be unavailable for purchase.
3. **Reporting Incorrect** — Reports are displayed in the current store currency only. Orders placed in a previous currency will **not** appear in your reports.
4. **Affiliate Referrals/Payouts Change** — New affiliate referrals and payouts created after the switch will use the new currency.
5. **Existing Subscription Renewal Errors** — Active subscriptions created in the old currency **may fail to renew** after the switch.

## Who should (and shouldn't) switch currency?

| Scenario                        | Recommendation  |
| ------------------------------- | --------------- |
| New store with no transactions  | Safe to switch  |
| Test store during setup         | Safe to switch  |
| Live store with order history   | Not recommended |
| Store with active subscriptions | Not recommended |

## Changed by mistake?

If your store currency was changed in error, you can switch it back to the original currency. Once reverted, your previous orders, reports, and subscriptions will function as they did before.


===== SOURCE: sync-users-with-surecart.md =====

---
source_url: https://surecart.com/docs/sync-users-with-surecart
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Settings](https://surecart.com/docs-category/settings/)/Manually Sync Your WordPress Users With SureCart

# Manually Sync Your WordPress Users With SureCart

In this guide, we'll show you how to sync your SureCart customers to WordPress.

This step is pretty important, especially if you're switching from another platform or doing things in a more complex manner.

If you've recently imported [customers](https://surecart.com/docs/import-customers-in-bulk) or [subscriptions](https://surecart.com/docs/import-subscriptions-in-bulk) (via CSV) to your SureCart account and want them to be synced to your WordPress site, then you can simply follow the steps in this doc.

Let's dive in!

### **Why Do You Need to Sync The Customers?**

SureCart is a headless e-commerce platform, which means that customer information and all other SureCart data aren't stored within WordPress, but rather in the [SureCart platform](https://app.surecart.com/).

This has major advantages:

- Your WordPress site remains unaffected by e-commerce functionality, ensuring there's no slowdown.
- When we save your data in the SureCart cloud instead of your WordPress database, your checkout pages, product pages, and other parts of your website will load faster.
- You don't need to worry about backups of your e-commerce data.
- Migrating from one WordPress install to another is much easier and faster.
- There's no requirement to upscale your server or invest in a pricier hosting plan.

Since the data resides in the SureCart database, we need to establish a connection between SureCart and your WordPress site.

This allows us to execute certain actions, such as integrating with third-party apps like LearnDash, LifterLMS, TutorLMS, and others.

To achieve this, you need to make sure that your customers in the SureCart cloud are registered as users on your WordPress site with appropriate user roles.

**Please note**: To synchronize purchases, importing a subscription is necessary. Currently, we don't import past orders. This association is needed for third-party apps like the ones we mentioned above.

For instance, consider a scenario: You possess a customer from a different platform, such as WooCommerce, and you've successfully imported them into SureCart. This particular customer has acquired a subscription for a course in LearnDash.

Now, to ensure that the user's experience remains seamless, following the migration to SureCart, you must execute the synchronization process. This synchronization activates their access to the course, enabling uninterrupted learning.

### **How To Manually Sync SureCart Customers as WordPress**

Make sure that you already imported the customers and subscriptions before following our step-by-step instructions below.

Just to check, go to one of the imported customers and look in the WordPress User section. You will see there are no users connected to this SureCart customer. But by syncing customers with WordPress users, you can assign a user role to multiple customers at once.

1. Go to Settings then Advanced menu, In the advanced screen, look for the Syncing section and click on the Sync Customers button.

2. In the Customers Sync Popup, you can sync WordPress users and/or run purchase action. You can check the toggle that applies to your scenario. After that, click on the Start Sync button.

3. A notice will inform you that the sync process will start in the background.

Congratulations!

You just synced all your SureCart customers with WordPress. You can go back to the same customer and check that now you have a WordPress User linked with the SureCart Customer.

Syncing SureCart customers with WordPress is vital to connect the two SureCart cloud and your WordPress site smoothly. SureCart stores data in the cloud, and syncing links this data with your WordPress site.

By following our guide, you can easily link SureCart and WordPress, benefiting both you and your customers.


===== SOURCE: third-steps.md =====

---
source_url: https://surecart.com/docs/third-steps
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Getting Started](https://surecart.com/docs-category/getting-started/)/Making a First Sale with SureCart

# Making a First Sale with SureCart

This document explains how to test the checkout flow using Test Mode and how to enable live payments to begin processing real orders.

## **Requirements**

- WordPress admin access
- SureCart plugin installed and activated
- At least one product created in SureCart
- A SureCart account connected to the store

## **Testing the Checkout in Test Mode**

### **Step 1: Open the Product**

- Go to **WordPress Dashboard → SureCart → Products**.
- Click the product name or the **Edit** link.

### **Step 2: Enable Test Mode**

- On the product editing page, locate the **Instant Checkout** dropdown menu in the top-right corner.
- Toggle the **Test Mode** option to activate it.
- Click **Save Product**.

**Note:** When Test Mode is enabled, the Instant Checkout displays a **Test Mode** badge and uses a test payment processor. Real payment methods are not available in this mode.

### **Step 3: Open the Instant Checkout Preview**

- Open the **Instant Checkout** dropdown menu again.
- Click **View** (or Preview if not published).

### **Step 4: Complete the Test Order**

- Enter a value in the **Name** field.
- Fill in the **Shipping Address** fields.
- Click **Purchase** to submit the test order.

**Expected outcome:** A **Thank you** confirmation modal appears. A test receipt is sent to the email address used in the order.

### **Step 5: Review the Test Order in the Customer Dashboard**

Click **Continue** in the confirmation modal to open the Customer Dashboard. The Customer Dashboard displays the test order under **Order History**.

### **Disabling Test Mode**

1. Open the product in **WordPress Dashboard → SureCart → Products**.
2. Open the **Instant Checkout** dropdown menu.
3. Toggle the **Test Mode** option off.
4. Click **Save Product**.

## **Enabling Live Payments**

To process real transactions, a payment processor must be connected: Stripe, PayPal, or Mollie.

## **Notes and Limitations**

- Test Mode transactions do not process real payments and do not generate live orders.
- Test Mode is configured per product.
- A receipt email is sent for both test and live orders.

## **Related Documentation**

- [Getting Started with SureCart](https://surecart.com/docs/getting-started/)
- [Next Steps After Getting Started with SureCart](https://surecart.com/docs/second-steps/)
- [How to Connect Stripe Payment Processor](https://surecart.com/docs/connect-stripe)


===== SOURCE: track-events-with-fbpixels.md =====

---
source_url: https://surecart.com/docs/track-events-with-fbpixels
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/How to Track SureCart Events with Facebook Pixel

# How to Track SureCart Events with Facebook Pixel

If you want to track SureCart events, like purchase events or add-to-cart events, through Facebook pixel, we got you covered.

In this article, we are going to show you how to send tracking information to Facebook through Google Tag Manager (GTM) and also through custom code.

Let's get started.

### **Creating Custom Events Trigger in GTM & Facebook Pixel Tag**

In this section, we will guide you through the process of setting up Google Tag Manager (GTM) to track various events on your website.

To illustrate, let's consider the example of a "view product event" that should be triggered when a visitor views a specific product on your SureCart store.

The same steps can be applied to track other events such as Search, Initiate Checkout, Start Trial, and so on.

For example, if you have a specific event on your website that you want to track, like the View Product event, you can do it in two simple steps.

1. Create a Custom Event Trigger in Google Tag Manager.
2. Associate the Trigger with Your Facebook Pixel Tag.

We've described both the steps further.

#### Step 1: Create a Custom Event Trigger:

- In your GTM container, go to **Triggers**.
- Click the **New** button to create a new trigger.
- Give your trigger a descriptive name, like "Event - View Product".
- In the **Trigger Configuration** section, choose **Custom Event** as the trigger type.
- Enter the event name in the Event name field exactly as it appears in your dataLayer push. For example, if it's "scProductViewed," type "scProductViewed."
- Under **This trigger fires on**, select **All Custom Events**.
- Click on the **Save Button** to save your changes.

Now that we have the trigger, we need to create the tags for Facebook.

#### Step 2: Creating Facebook Pixel Tag in Google Tag Manager

Now, we are going to cover the steps to create a Facebook Tag using Google Tag Manager. Please follow the steps below to create a Facebook Pixel Tag.

- In your GTM container, go to **Tags**.
- Click the **New** button to create a new tag.
- Give your tag a descriptive name, like "Facebook - View Product".
- In the **Tag Configuration** section, select **Custom HTML** as the tag type.
- In the HTML field, paste the Facebook Pixel code that you get from Facebook.
- In the **Triggering** section, click to add a trigger.
- Choose the same custom event trigger you used for the Google Analytics tag (For example, "Event - View Product").
- Click **Save** to save your Facebook Pixel Tag.
- After creating the tag and associating it with the trigger, click the **Submit** or **Publish** button in the upper-right corner of GTM to publish your changes live.

By following these steps, you'll have set up the Facebook Pixel Tag in Google Tag Manager, and it will fire when the View Product event occurs on your website.

Now you just need to replicate the same steps for all the events you want to track.

### **Facebook Pixel Integration Through Custom Code**

You can track Facebook pixel events without Google Tag Manager if you prefer. To do this, you should add a bit of custom code to your site.

The easiest way to do this is to use a [free code snippets plugin](https://wordpress.org/plugins/code-snippets/), though you can do this in your theme or with a separate plugin too.

Our checkout component emits an event called scOrderPaid, which happens when a checkout is paid. This lets you listen for the event, and look at the checkout data to send to Facebook pixel.

So if you want to choose this method, you can simply add the custom code to your site's footer, listening for the `scCheckoutCompleted` event and calling `fbq('track', 'Purchase', {...})` with the checkout data.

In this quick reference article, we've covered the essentials of tracking SureCart events in Facebook Pixel using Google Tag Manager (GTM) and also straight with a custom code.

We hope this was helpful. If you run into any problems or have questions, reach out to our support team. We are always ready to help and provide further guidance.


===== SOURCE: track-events-with-ga.md =====

---
source_url: https://surecart.com/docs/track-events-with-ga
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/How to Track Add to Cart and Purchase Events with Google Analytics

# How to Track Add to Cart and Purchase Events with Google Analytics

Using Google Analytics, you can track the "Add to Cart" and "Purchase" events on your SureCart store.

This means that when someone adds a product to their cart or makes a purchase in your store, you can monitor and analyze these actions through Google Analytics.

This functionality is valuable for easily tracking customer behavior within your store so you can make data-driven decisions.

In this article, we'll see two ways to connect your SureCart to Google Analytics for tracking Add to Cart and Purchase events.

These methods are

- Using Google Site Kit plugin on your website.
- Using Google Tag Manager.

We are going to cover both in this article.

Regardless of the method, you need to have Google Analytics on your website, and the simplest way is by using the [Google Site Kit plugin](https://wordpress.org/plugins/google-site-kit/).

## Automatically Track the Events Using Site Kit Plugin

To automatically track the Add To Cart and Purchase events, Install and activate the Google Site Kit plugin on your website.

This plugin will display Google Analytics stats in your WordPress Admin area.

This method works effortlessly, without any complications. We recommend it only if you need to track Add To Cart and/or Purchase events due to its simplicity.

With this approach, whenever someone adds a product to their cart or makes a purchase, you can easily view this information in your Google Analytics statistics.

Now if you want to track additional events, you can connect your SureCart store with [Google Tag Manager](https://tagmanager.google.com/).

Consider this analogy: When you use SureCart with Google Analytics directly, it's like a phone that automatically dials your friend's number when you make a purchase.

However, if you're using Tag Manager, it's similar to having an intermediary that forwards your call to your friend after you've made a purchase. We'll assist you in setting up that call forwarding.

## Tracking the Custom Events Using Google Tag Manager

In this section, we'll walk you through the process of tracking different Google Analytics events in your SureCart store using Google Tag Manager.

If you haven't already, be sure to check out our article on [How to Track Events With Google Tag Manager](https://surecart.com/docs/custom-events-with-gtm/) so you can easily follow this guide.

Let's get started.

### **Setting Up Google Tag Manager (GTM) for Multi-Event Tracking with a Custom Trigger**

In this section, we are going to cover how to set up Google Tag Manager (GTM) to track the View Product event.

You can use the same steps to add other events like Search, Initiate Checkout, Start Trial, etc.

You can use the same trigger in Google Tag Manager (GTM) to track the events for Google Analytics, Facebook Pixel, or other platforms.

In GTM, [triggers](https://support.google.com/tagmanager/answer/7679316?hl=en) are used to determine when tags should fire based on certain conditions or events.

If you have an event on your website that you want to track, like View Product, you can create one custom event trigger for that event and then associate it with your Google Analytics tag.

Here's how you can do it:

**Step 1: Create your Google Tag Manager Account:**

Create a Google Tag Manager account and link it to your WordPress website. This is a straightforward process, just paste the provided GTM code snippet into your site header.

You can do this directly or utilize plugins like [HFCM](https://wordpress.org/plugins/header-footer-code-manager/) for assistance.

**Step 2: Create a Custom Event Trigger:**

- In your GTM container, go to **Triggers**.
- Click on the **New** button to create a new trigger.
- Provide a descriptive name for your trigger, such as "Event – View Product."

- Click on the **Trigger Configuration** section, then select **Custom Event** as the trigger type.

- Enter the event name in the **Event name** field exactly as it appears in your dataLayer push. For example, if it's "scProductViewed," type "scProductViewed."
- Under **This trigger fires on**, select **All Custom Events**.
- Click on the **Save Button** to save your changes.

Now that we have the trigger, we need to create the tags for Google Analytics.

### **Creating a Google Analytics Tag in Google Tag Manager for Event Tracking**

Now we are going to cover the steps to create the Google Analytics Tag using Google Tag Manager:

**Step 1: Create a New Tag and configure it:**

- In your GTM container, go to **Tags**
- Click the **New** button to create a new tag.
- Give your tag a descriptive name, like "GA4 – View Product"
- In the **Tag Configuration** section, select **Google Analytics → Analytics: GA4 Event** as the tag type.

**Step 2: Configure Google Analytics Settings:**

- Enter your GA4 **Measurement ID** and **Event Name** in their respective fields. To find your Measurement ID in your Google Analytics account, follow [these](https://support.google.com/analytics/answer/12270356?hl=en#:~:text=Find%20your%20measurement%20ID,row%20of%20the%20stream%20details.) steps.
- In the **Triggering** section, click to add a trigger.
- Choose the custom event trigger you created earlier (For example, "Event – View Product").

**Step 3: Save Your Tag and Publish Your Changes:**

- Click **Save** to save your Google Analytics Tag.
- After creating the tag and associating it with the trigger, click the **Submit**/ **Publish** button in the upper-right corner to publish your changes live.

By following these steps, you'll have set up the Google Analytics Tag in Google Tag Manager. GTM will fire when the **View Product** event occurs on your website.

Now you just need to replicate the same steps for all the events you want to track.

In this quick reference article, we've covered the essentials of tracking SureCart events in Google Analytics using Google Tag Manager (GTM).

If you encounter any issues or have questions during the importing process, don't hesitate to seek assistance from our support team. We are always ready to help and provide further guidance.


===== SOURCE: transfer-store-ownership.md =====

---
source_url: https://surecart.com/docs/transfer-store-ownership
source: surecart-kb
scraped: true
---

# How to Transfer Store Ownership in SureCart

Transferring store ownership in SureCart lets you give someone else full control of your store.

This is helpful if you sell your business, stop managing the store, or want to make someone else the owner. For example, if you sell your online store, you can quickly transfer everything to the new owner.

In this article, we'll show you how to add the new owner as a team member and then transfer the store to them in a few easy steps.

## **Add new Organization**

Before you can transfer the store to the new account we need to create an organization and move our store in the organization, In the end we will move the organization with the store not only the store.

- Go to the SureCart platform, select the store and click Switch organization
- Click on the **New Organization** button
- Name the organization and click the **Create New Organization** button

That it, now we have created new organization and we can move the Store into this organization

## **Move store into the organization**

- Open the SureCart platform and select the store you want to transfer
- Navigate to the General tab and scroll down to the "Transfer Store" button.
- In the pop-up window, select the destination organization where the store will be transferred. and hit the Transfer button.

That is, your store is now transferred to another organization, in the next step we will add new member to the organization.

## **Add the New Owner as a Team Member**

Before you can transfer ownership, you need to invite the person as a team member in the same organization

- Go to the SureCart platform and select the desired store.
- Go to Organization settings and open the Members from the left sidebar.
- Go to **Invites** top right and click on the "Invite Member" button.
- Enter the person's name, and email address, and assign them the necessary roles, such as Admin or Developer. In this case, we need to select Admin
- Click the "Send Invite" button.

Once you send the invitation, the new owner will receive an email. They need to accept the invite and join the store as a team member.

## **Transfer Store Ownership**

After the person has accepted the team member invite, you can transfer the store ownership to them. To do this:

- Go to the Organization setting and from the general tab click on the **Transfer Ownership** button
- Click on their name and click the "Transfer Store" button here.
- Next, you need to confirm the transfer in the dialog box that appears.

**Note**: Once you transfer ownership, you'll no longer have control over the store unless the new owner permits you again.

Your store ownership has now been successfully transferred to the new team member.


===== SOURCE: translating-surecart.md =====

---
source_url: https://surecart.com/docs/translating-surecart
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Localization](https://surecart.com/docs-category/localization/)/How to Translate SureCart in Your Own Language

# How to Translate SureCart in Your Own Language

SureCart is 100% translation-ready and comes with .po / .mo files and also can be translated to any language that you want using software such as LocoTranslate or Poedit.

You can translate the words you see in the SureCart plugin on two sides of your store:

- The parts that you see as a customer on the Customer Dashboard or the Checkout page.
- The parts that are only seen by you as store owner on the Product Page, Subscriptions, and Settings.

So let's say you are looking to translate the texts on the checkout page to a different language from English, you can do that using any of the two methods mentioned in the article.

Let's understand both these methods!

### **Method 1: Using Loco Translate**

SureCart allows translating almost every text/string without much of an effort.

Let's see how LocoTranslate can help us with the process.

- Firstly, you need to install the Loco Translate plugin from the Plugins page > Add New.

- Upon installation, visit the Loco Translate Plugins and choose the SureCart option from the list to translate.

- Now, under the Overview tab, click on New Language.

- Here, select the language you want and set the location to **Custom**. Click on the "Start translating" button once you've made these changes.

- Now, you will be taken to the editor page. Loco Translate will fetch all the words and phrases that you can be translated and you can set the translation manually.

- Save the Translations, and view the text/string on the Instant Checkout page to see how your translation looks.

- Once the strings are translated, please make sure you clear the cache on your website and check the updated text/string on the front end.

That's it!

We were able to translate a text on the SureCart checkout form using the Loco Translate plugin.

### Method 2: Using The .pot File

The SureCart plugin provides a platform for String Translation for our users.

Our developers pull in all the validated translations once they reach above 80% on the platform during every plugin update.

If you are interested in helping us translate SureCart in any of your desired languages, please feel free to write to our [support team](https://surecart.com/support/open-a-ticket/).

Now, coming to the translation of strings using the .pot file, please follow these steps:

- Download the [SureCart plugin](https://wordpress.org/plugins/surecart/) on your computer. Next, double-click on the plugin zip file to extract it.
- Click on the plugin folder and look for the Languages folder.

- Under the Languages folder, you will find the surecart.pot file at the top of the folder. We will need this .pot file after installing the Poedit plugin on your system.

- Now, you will be required to install the [**Poedit app**](https://poedit.net/download) on your computer, you can find a free version for Windows and Mac.
- Upon installation, you will notice the application's home screen. Click on the **Create New** button.

- Here you will be redirected to the computer's file manager. Select the .pot file of the SureCart plugin which we found under the Languages folder.

- Choose the language you want to translate to from the dropdown menu. Click on the Ok button.

Now, Poedit will display all the text/strings as Source Text available for translation.

- Click or search using Ctrl+F for the string you want to translate and provide the Translation text in the Translation field.

- Once you are done translating the texts/strings, you can save the file using the Save button under the File menu at the top-left of the screen.

Here, it is important to note that, you have to save your file after the language name and country code.

Be sure to prefix the text domain before the [language code](https://wpastra.com/docs/complete-list-wordpress-locale-codes/). Also, capitalize the file name correctly as it is important here.

For language codes, please [refer to](https://wpastra.com/docs/complete-list-wordpress-locale-codes/) this list. And text domain can be found in the style.css file of the theme, or the main PHP file of the plugin.

Examples of file names for the SureCart plugin:

- For German: "surecart-de_DE.po" & "surecart-de_DE.mo"
- For French: "surecart-fr_FR.po" & "surecart-fr_FR.mo"

Note, that Poedit will save your files as .po and .mo files.

- Next, we simply need to place these files in the **/wp-content/languages/** directory. As we do not want to lose all the translations and edits we have done, we will upload the file in the above-mentioned folder on your computer.

By following the above steps, you will be able to successfully translate the strings/text in the SureCart.

We ensure all the texts in SureCart are made translatable, if you notice any of the texts are missing, please feel free to drop us a message using the below support.

If you still have any questions, please feel free to write to us via our [Support form](https://surecart.com/support/open-a-ticket/).


===== SOURCE: trial-subscription.md =====

---
source_url: https://surecart.com/docs/trial-subscription
source: surecart-kb
scraped: true
---

# How to Set Up Subscription Plans with Trials in SureCart

SureCart makes selling stuff online super easy and helps you take care of your customers significantly.

One remarkable thing you can do with SureCart is make subscription plans for the stuff you're selling. You can even add a trial period. This means customers can try out your stuff before they subscribe, which could help you sell more.

### How Do Trial Subscriptions Work in SureCart?

Here's how a trial subscription works:

1. People choose your product and go to checkout. They have to enter their payment details, but they won't be charged anything yet.
2. After checking out, their trial starts. They can use and enjoy your product without having to pay.
3. Once the trial is over, that's when they start paying. The money is taken from the payment details they entered during checkout, which marks their subscription's start.
4. Then, the subscription just keeps going like normal. This is the subscription cycle.

### **How to add a subscription payment type**

- Inside your product, scroll down to the Pricing section.
- Click the 'Add Another Price' button.
- Insert a name for the Subscription in the `Name` field.
- In the `Price` field, insert the amount you want to charge your customer.
- In the `Repeat Payment Every` field, choose how often you want this payment to be repeated. Choose from the dropdown: Day, Week, Month, or Year.
- Add a "Compare at Price" option to highlight the value of the current offer for the customer.

### **How to Add a Free Trial to The Subscription Payment Type**

SureCart offers the ability to set a trial period for your subscription plans. This trial allows you to offer customers the opportunity to trial the product for a customizable number of days.

- Toggle the `Free Trial` option and specify how many days you would like the free trial to last in the following field.
- In the final step, click the Create Price button.

There will be a reminder notification sent three days before the trial ends.

### Preventing Free Trial Abuse for Subscriptions

Customers repeatedly signing up for free trials can be a concern. SureCart allows you to restrict customers from purchasing multiple free trials.

To enable this:

- Go to SureCart **Settings** > **Subscriptions**.
- Scroll down to "Purchase Behavior" and enable **Prevent Duplicate Trials**.

Now, customers can no longer claim multiple free trials for the same product. If someone has previously used a free trial for the product, they will be charged the full price instead of receiving another trial.


===== SOURCE: unable-to-sign-in.md =====

---
source_url: https://surecart.com/docs/unable-to-sign-in
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Troubleshooting](https://surecart.com/docs-category/troubleshooting/)/Unable to Sign In To SureCart Dashboard Due To Sign-In Loop

# Unable to Sign In To SureCart Dashboard Due To Sign-In Loop

## What Triggers the Sign-In Loop Issue in SureCart?

The sign-in loop issue occurs when users are unable to sign in to the SureCart dashboard due to a continuous loop of the sign-in page. Causes include:

- Browser cache and cookies
- Incorrect login credentials
- Third-party plugins or extensions

## How To Resolve The Sign-In Loop Issue?

### Clearing the Browser Cache and Cookies

In Google Chrome: Click the three-dot icon on the top right, select **Clear browsing data** (or press **Ctrl + Shift + Del**), set Time range to **All time**, and clear cached images, cookies, and other site data.

Alternatively, try signing in using incognito mode to use a fresh session without stored cache or cookies.

### Login Credentials

Verify that the login credentials entered are correct. If you have forgotten your password, go to the sign-in page and click the **Forgot your Password** option. Enter your email address and follow the instructions to reset your password.

### Third-Party Plugins Or Extensions

Third-party browser plugins or extensions can sometimes interfere with the sign-in process. Disable any that may be causing issues. In Chrome, navigate to **Manage Extensions** in the browser settings and disable or remove suspect plugins.


===== SOURCE: understanding-ecommerce-fees.md =====

---
source_url: https://surecart.com/docs/understanding-ecommerce-fees
source: surecart-kb
scraped: true
---

# Understanding eCommerce Fees

The doc is here to explain the fees associated with processing ecommerce transactions. SureCart offers multiple payment processors and each charges different fees.

## Processor Fees

**SureCart does not charge these fees**, these are incurred from using a payment processor. It's important to be aware of the processor fees charged by payment services like Stripe, PayPal, Mollie etc. Charging fees is standard across the eCommerce industry and vary depending on the processor.

These fees are charged to cover operational costs like payment processing, security, and fraud prevention.

### Stripe

The standard fee they charge is 2.9% + 30¢ per successful transaction. But there are other Stripe fees that may apply to your transaction depending on the payment method used by the buyer, where the buyer is located, if the product is a subscription. The two that are most common extra fees are 1.5% for international cards and + 1% if currency conversion is required.

**Stripe Standard Fee Example**

| Description                                    | Amount |
| ---------------------------------------------- | ------ |
| Product Price                                  | $30.00 |
| Tax (20% VAT)                                  | $6.00  |
| Total                                          | $36.00 |
| Stripe Standard Fee 2.9% + 30¢                 | $1.17  |
| Net Profit (total – tax – Stripe standard fee) | $28.83 |

### PayPal

The standard fee they charge is 3.49% + fixed fee per successful transaction. The fixed fee is different per currency. For example, all USD transactions have a 49¢ fixed fee per transaction. The most common extra fee is 1.5% for international cards.

**PayPal Standard Fee Example**

| Description                                    | Amount |
| ---------------------------------------------- | ------ |
| Product Price                                  | $30.00 |
| Tax (20% VAT)                                  | $6.00  |
| Total                                          | $36.00 |
| PayPal Standard Fee 3.49% + 49¢                | $1.54  |
| Net Profit (total – tax – PayPal standard fee) | $28.46 |

### International Payment Processors

You can use Mollie to process payments alongside Stripe and PayPal. Mollie charges a percentage of the transaction plus a fixed fee, similar to the others.

## **Transaction Fee**

For merchants on our Launch plan, a small fee of 1.9% is added per transaction, supporting the services provided under this plan, which includes all of our features and customer support. Other WordPress ecommerce products such as Easy Digital Downloads 3%, GiveWP 2%, The Events Calendar 2%, Paid Members Pro 2%, and others, charge higher transaction fees yet don't give you full access to all features.

The SureCart Launch plan has lower transaction fees, and we give you access to the entire SureCart feature set. **Upgrading to a pro plan eliminates this transaction fee.**

**Transaction Launch Plan Example**

| Description                    | Amount |
| ------------------------------ | ------ |
| Product Price                  | $30.00 |
| Tax (20% VAT)                  | $6.00  |
| Total                          | $36.00 |
| Stripe Standard Fee 2.9% + 30¢ | $1.17  |
| Transaction Fee 1.9%           | $0.57  |
| Net Profit                     | $28.26 |

Because we want to make sure merchants are aware, if your store is on the Launch plan, we add a notice in the SureCart platform.

Upgrading to a pro plan eliminates this transaction fee. Our pro plans do not have transaction fees.


===== SOURCE: update-customers-details.md =====

---
source_url: https://surecart.com/docs/update-customers-details
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Online Store](https://surecart.com/docs-category/online-store/)/How to Update Customer's Details?

# How to Update Customer's Details?

Wondering how you can update customer details on SureCart? It's simple.

Imagine a customer buys your product but mistypes their email. Using the wrong email address will prevent users from receiving information about product purchases, invoices, and password resets.

No worries! They reach out to you, and you can quickly set things right from your end. Cool, right?

Now, let's see how you can update customer details!

- Navigate to SureCart and click on the Customers tab.

- Click on the customer name.

There's a section labeled Customer Details. That's your spot to make edits.

Remember: every purchase on your site means there's an account on WordPress for that customer.

If they made a mistake with their email, it'll be wrong on WordPress too. This means they might miss out on important emails.

- Select the field where you want to make the changes.

- Give the page a quick refresh. You'll see the WordPress User email now matches up with what's in Customer Details.

And that's it! Simple, right?

By following the steps above, you can make changes to your customer details based on your needs.

Got more questions? You can reach out to us anytime.


===== SOURCE: update-store-details.md =====

---
source_url: https://surecart.com/docs/update-store-details
source: surecart-kb
scraped: true
---

# How to Update Store Details

## Overview

SureCart streamlines the process of configuring your store's essential information through a single, user-friendly settings page. These details appear across multiple touchpoints including email notifications, invoices, and the customer dashboard, making accurate configuration crucial for professional presentation.

## Steps to Fill Store Details

1. **Navigate to Settings**
   Access the WordPress dashboard and select SureCart > Settings.

2. **Store Name**
   Enter your store name, which appears in notifications, invoices, and throughout your website.

3. **Store URL**
   Provide your live store URL — this is where customers will be directed when accessing your store.

4. **Default Currency**
   Select your store's currency, which displays across your shop, product pages, and checkout.

5. **Timezone**
   Define your store's timezone to ensure accurate timing for checkouts, invoices, and other features.

6. **Language**
   Set your preferred language. This applies to your store regardless of WordPress language settings.

7. **Terms Page URL**
   Add the URL to your terms page, primarily used during checkout.

8. **Privacy Policy URL**
   Include your privacy policy page URL.

9. **Save Changes**
   Click the Save button to preserve all updates. Changes apply immediately to your store.

## Key Information

Store details are essential for professional operations and customer trust. All configured information propagates across customer-facing and internal systems automatically upon saving.


===== SOURCE: update-upsell-countdown-timer.md =====

---
source_url: https://surecart.com/docs/update-upsell-countdown-timer
source: surecart-kb
scraped: true
---

# How to Update Your Upsell Countdown Timer in SureCart

## Overview

The countdown timer displayed at the top of upsell pages shows remaining time for an offer. By default, it's configured for 30 minutes, but this duration can be customized.

## Steps to Update the Timer

1. **Access Settings**: Navigate to SureCart **Settings** > **Orders & Invoices**
2. **Locate Upsells Section**: Scroll down to find the **Upsells** section
3. **Adjust Duration**: Change the time limit to your preferred duration (measured in minutes)
4. **Save Changes**: Click the **Save** button to apply your modifications

## Result

Once saved, the updated countdown timer will display on your upsell page with the newly configured duration.

## Additional Resources

For more comprehensive information about upsell functionality, see the article on enabling upsell funnels. Support is available through the contact page if issues arise.


===== SOURCE: upgrade-downgrade-plan.md =====

---
source_url: https://surecart.com/docs/upgrade-downgrade-plan
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Payments](https://surecart.com/docs-category/payments/)/How to Switch Your Plans on SureCart Store

# How to Switch Your Plans on SureCart Store

This guide explains how to switch your plans (either downgrade or upgrade) in the SureCart store.

For instance, if you're currently on the 5 Stores Yearly Pro Plan and want to switch to the 1 Store Yearly Pro Plan, you can do it yourself. Go to your SureCart dashboard and follow simple steps to change your current plan.

In the top-left corner, click on the **Store** dropdown menu.

In the modal that appears, click **Organization Settings**.

Click **Plan & Billing** from the menu.

In the top-right corner, click the **Manage Billing** dropdown, then select **Manage Subscription**.

A list of subscriptions will be displayed. Select the subscription you want to switch to.

In the **Change Subscription** section, select the plan you want to switch to (1), and then click the **Preview Change** button (2).

After reviewing the details, click the **Confirm Change** button to finalize the plan update.

That's it! You have successfully switched your plan.

And in case, you still have any questions, please feel free to reach out to us through our [Support Portal](https://surecart.com/contact-us/) and select Account & Billing. We would be more than happy to help!


===== SOURCE: upgrade-groups.md =====

---
source_url: https://surecart.com/docs/upgrade-groups
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Revenue Boosters](https://surecart.com/docs-category/revenue-booster/)/What are Upgrade Groups in SureCart?

# What are Upgrade Groups in SureCart?

The Upgrade Group in SureCart refers to a collection of related products or services that are offered as upgrades to the base product. These upgrades are designed to provide additional features, enhanced functionality, or improved performance compared to the standard version.

By bundling these upgrades together, you can create enticing upgrade packages that encourage your customers to choose a higher-tier option.

SureCart's Upgrade Groups feature empowers merchants to present upgrade options to their customers, thereby maximizing revenue and customer loyalty.

### Understanding Upgrade Groups

When a customer views a product on a SureCart-powered website, they are presented with an option to explore upgrade possibilities. By selecting this option, they can view the available upgrade groups related to the base product.

For instance, imagine you have implemented three subscription options on your website: Basic, Gold, and Platinum. The Basic plan is available for free, while the Gold plan costs $10 and the Platinum plan costs $20. The Upgrade Group feature provides users with the ability to upgrade from the Basic plan to either the Gold or Platinum plans.

### How Does an Upgrade Group Work?

Imagine a customer who has subscribed to the basic plan, which is free of charge, and now wishes to upgrade to the Gold membership plan. With SureCart's Upgrade Group functionality, the process is straightforward.

Now, let's consider a scenario where a customer is already a Gold member and decides to upgrade further to the Platinum plan on the same day they subscribed to the Gold membership. The customer will only be required to pay the difference amount between the Gold membership ($10) and the Platinum membership ($20).

### How to create the upgrade group?

Before you can create an upgrade group, you will need to create the products that you would like to add to the upgrade group.

Once you have added the products, please follow the steps below to create an upgrade group.

**Step 1:** Navigate to the **Products** > **Upgrade Groups**.

**Step 2:** Click on the **Add New** button to add a new upgrade group.

**Step 3:** Enter a name for your upgrade group. Please note that the name that you will enter here will not be visible to the customers and is for internal reference only. Click on the Create button to save the group name.

**Step 4:** On the next page, you will need to enter the product details that you would like to include in this upgrade group. Click on the **Add Product** button to start adding the products.

**Step 5:** You will get a pop-up on the screen with a drop-down to select the products. Select the product that you would like to add to this upgrade group and click on the Add Product button to add it to the list. Repeat this process until you have added all the products.

**Step 6:** Once you have added all the products, click the **Save Group** option in the top right corner to save the group.

That's it. Your upgrade group is selected and is live. Customers now can switch between the memberships by either upgrading or downgrading.

### Benefits of Upgrade Group

- **Increased Revenue**: By offering upgrade options, you can upsell to customers, resulting in higher average order values and increased revenue.
- **Enhanced Customer Experience**: Upgrade groups enable customers to personalize their purchases, leading to a more tailored and satisfying shopping experience.
- **Improved Customer Loyalty**: By presenting customers with relevant upgrade options, you can strengthen customer loyalty and encourage repeat purchases.
- **Streamlined Shopping Process**: Upgrade groups simplify the decision-making process for customers.
- **Competitive Advantage**: By incorporating the Upgrade Group feature, you can differentiate yourself from the competitors.

### FAQ

**Can I create multiple upgrade groups for a single product?** Yes, you can create multiple upgrade groups for a single product.

**Are upgrade groups customizable?** Yes, upgrade groups are customizable.

**If a customer chooses to downgrade, how will the refund be calculated?** The refund is calculated on prorated basis meaning they will be charged for the period of time they have used the subscription.

**Is the Upgrade Group feature available in all SureCart plans?** No, upgrade group is a premium feature.

**Do the Upgrade Groups handle proration as well?** Yes, Upgrade Groups are designed to handle proration seamlessly.

### Conclusion

The Upgrade Group feature in SureCart empowers you to offer product upgrades, enhancing the overall shopping experience for customers. By bundling related upgrades together, you can present enticing options that cater to customers' needs and preferences.


===== SOURCE: upgrading-downgrading-cancellation-of-subscriptions.md =====

---
source_url: https://surecart.com/docs/upgrading-downgrading-cancellation-of-subscriptions
source: surecart-kb
scraped: true
---

# How Does Upgrading, Downgrading, and Subscription Cancellation Work in SureCart?

## Overview

SureCart enables merchants to manage subscription modifications through flexible timing options. You can upgrade, downgrade, or cancel the subscriptions from the next billing cycle or immediately.

## Configuration Steps

Navigate to **SureCart > Settings > Subscriptions** in your WordPress dashboard.

## Three Main Options

### Upgrade

The platform recommends selecting immediate upgrades so customers gain access right away after payment. When upgrades process immediately, a prorated invoice will be generated and paid.

### Downgrade

You can schedule downgrades for either immediate or next billing cycle.
- **Immediate downgrades**: Customers receive credits for unused time they've prepaid
- **Next billing cycle downgrades**: They keep access through their paid period with no credits applied

### Cancellation

- **Immediate cancellations**: End subscriptions right away with potential credits for unused prepaid time
- **Next billing cycle cancellations**: Allow continued access until the current period ends

## Failed Payment Handling

The system automatically marks unpaid subscriptions as "Past Due" and implements smart retry logic. You can configure how long to retain subscriptions after payment failures: one, two, or three weeks.

## Premium Feature: Behavior Settings

Trial periods without payment requirements are available on upgraded SureCart accounts, allowing you to set minimum upfront payment amounts if desired.


===== SOURCE: upgrading-to-surecart-v3.md =====

---
source_url: https://surecart.com/docs/upgrading-to-surecart-v3
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Migrating](https://surecart.com/docs-category/migrating/)/Upgrading to SureCart V3

# Upgrading to SureCart V3

Upgrading to SureCart V3 introduces powerful new features and enhanced functionality. However, due to significant structural changes, it's essential to carefully review your site afterward to ensure all elements look and function as expected.

This documentation provides a complete roadmap for upgrading to SureCart V3, including **essential steps to take before upgrading**, an **overview of new features and improvements**, and a **post-upgrade checklist** to help you verify key pages, resolve any style or layout issues, and identify potential conflicts with themes or plugins.

###### Important Note

SureCart V3 has undergone extensive testing, including a multi-month beta period where we tested the new version on over 100 stores. While we don't anticipate any major problems, **this is a significant update, so it's possible that some visual elements may appear different**.

Additionally, **caching** can sometimes interfere with updates, potentially causing display or functionality issues. To ensure that all changes are properly reflected, please **clear your site's cache post-upgrade**. For detailed guidance on managing caching, see our [SureCart Caching Documentation](https://surecart.com/docs/caching/).

### **Things to Do Before Upgrading:**

#### 1. Back Up Your Full Site

**Why is this important?** Backing up your entire site is essential before upgrading to prevent any potential data loss or issues during the process.

**How to do it?** Use a trusted WordPress backup plugin or your hosting provider's built-in backup tools to create a complete backup of your site.

**Helpful Resource:** You may also want to consult the [Migrating SureCart to Another WordPress Install](https://surecart.com/docs/migrate-to-another-wordpress-install/) guide, which provides detailed instructions on backing up and migrating your site safely.

#### 2. Test In A Staging Environment

Before applying the upgrade to your live site, test it in a staging environment. This helps you identify any issues with custom templates, plugins, or third-party integrations before affecting your customers.

### **Post-Upgrade Checklist**

After upgrading, use the following steps to verify your site and ensure everything is functioning as intended.

#### 1. Check The Shop Page

- **Why:** Changes to SureCart's structure and the removal of certain DOM elements may impact the display of the shop page.
- **What to Look For:** Inspect for any missing margins, spacing inconsistencies, or misaligned elements.
- **How to Fix:** Edit the shop page and review your layout settings. Remove any unnecessary **group blocks** that could be causing layout issues.

#### 2. Check Collection Archive Pages

- **Why:** Collection pages may be affected by layout changes in SureCart V3, especially if you're using custom styling or theme integrations.
- **What to Look For:** Check for consistent spacing, alignment, and that all collection items display correctly.

#### 3. Check Product Pages

- **Why:** Product pages may need adjustments due to changes in SureCart's DOM structure and functionality enhancements.
- **What to Look For:** Verify that all elements—such as product images, descriptions, prices, and variant selectors—are displayed and working correctly.

#### 4. Check Slide Out Cart

- **Why:** The cart experience is critical, and V3 changes could potentially impact the display or interaction of the cart.
- **What to Look For:** Add products to the cart and open the slide-out cart to ensure all items are visible, prices are correct, and buttons are working as expected.

#### 5. Check Add To Cart and Buy Buttons

- **Why:** These buttons were reworked to use your theme's styles for the **default WordPress button block**.
- **What to Look For:** Ensure your add to cart and buy buttons are styled to your liking. They may have changed in terms of color, size or width depending on your theme's styles.

### **New Features and Functionality in V3**

#### **WordPress Interactivity API Integration**

The Cart, Shop Page, and Product Page have been moved to the WordPress Interactivity API, providing a more dynamic user experience such as more block styling, easier CSS customizations, and more.

#### **SureCart Products as Custom Post Types**

SureCart products are now handled as Custom Post Types, offering benefits such as improved speed, greater customization options, compatibility with SEO plugins, and more. Includes Advanced Custom Fields and Metabox integration, post meta box integration, and improved usage in page builders and query loops.

#### **Product Images in WordPress Gallery**

All product images are now managed through the WordPress gallery, making it easier to organize and manage media.

#### **Flexible Product List Design**

The product list (shop page) is now composed of smaller blocks, giving you more flexibility in design and customization.

#### **Product List Patterns**

You can choose from **pre-made patterns (templates)** for your product list layout.

#### **New Product Filters**

Two additional filters have been introduced: Show products by taxonomy (SureCart Collection) and show products by keywords.

#### **New Default Sorting**

You can now set the default sorting order for your shop.

#### **New Sale Badge**

A sale badge has been added to products, providing a visual cue for discounted items.

#### **Automatic Layout Grid**

The new auto layout mode adjusts your product grid to fit different screen sizes, offering a responsive design without manual adjustments.

#### Native Bricks Builder Integration

- **Templates** for Bricks Builder: SureCart - Single Product and SureCart - Collection Archive.
- Compatibility with **ACSS** (Automatic CSS)
- Product loop
- About **20 dynamic data points** have been added for Bricks Builder integration.
- **12 native Bricks elements** were introduced, including: Product Form, Product Card, Add to Cart, Collection Tags, Product Media, Price Selector, Price Data, Product Data, Quantity, Sale Badge, Custom Amount, Product Variant Pills.

**IMPORTANT:** For SureCart elements (such as Add To Cart, Collection Tags, Product Media, etc.) to function properly, they must be placed within the Product Form or Product Card block wrappers.

### **Additional Considerations**

**Manual Checks:** After upgrading, manually review each key page on the frontend to confirm everything appears and works as expected.

**Caching Issues:** Caching can sometimes cause problems by serving outdated content or styles. After upgrading, be sure to clear your site's cache.

### **FAQ**

**What happens if I revert back to SureCart V2 after upgrading to V3?**

If you revert back to V2, the cart, shop page, and product page may break. This can be easily fixed by re-adding blocks or resetting the templates, but it's important to prepare for this in advance.

**Why aren't my Add to Cart, Collection Tags, Product Media, and other elements working correctly?**

For SureCart elements to work properly, they must be placed within the Product Form or Product Card block wrappers.

**Why does my store look or function incorrectly after upgrading to SureCart V3?**

Caching can sometimes cause display or functionality issues by serving outdated content after an update. If you notice any unexpected visuals or behaviors after upgrading, try clearing your site's cache.


===== SOURCE: user-roles-and-permissions.md =====

---
source_url: https://surecart.com/docs/user-roles-and-permissions
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Settings](https://surecart.com/docs-category/settings/)/A Guide to SureCart User Roles and Permissions

# A Guide to SureCart User Roles and Permissions

### **Introduction**

User roles in WordPress are like predefined job descriptions. They decide what a person can do on a website. This is important for keeping the site safe and organized.

These roles make sure people only have the right abilities based on their job.

So, think of it like this: in WordPress, you have different "jobs" with different "tasks," and these roles make sure every user has access to the necessary sections of the website.

For example, administrator role can access every part of your website but an editor may only see limited settings.

In the same way, WordPress and different WordPress plugins offer various user roles, each with different permissions.

In this guide, we'll delve into SureCart User Roles and Permissions, exploring each role's abilities and essential details.

Let's begin!

### **What are User Roles in SureCart**

Think of SureCart user roles like job titles in an eCommerce platform. They determine who can do what, ensuring smooth store operations.

Following are the user roles and their capabilities that are available when you install SureCart on your website:

**SureCart Customer**: Regular shoppers. They can browse products, add items to their cart, and buy stuff. They're the heart of the business because they're the ones making purchases.

**SureCart Shop Worker**: Store employees who help with various tasks in the store. They might be in charge of handling orders, packaging products, and assisting customers. And they have the capability to view all Products, Orders, Subscriptions, Customers, Coupons, Licenses in SureCart.

They have a bit more access than customers, but they can't make big changes like modify and fulfil orders.

**SureCart Accountant**: Just like in real life, an accountant is the money expert. They can look at the financial side of things, checking order history, and subscriptions. They can't modify products or alter the website's appearance.

**SureCart Shop Manager**: Shop Managers have full control of the SureCart store. They can add or remove products, manage shop workers, and even make changes to the orders directly. They're responsible for keeping the store running smoothly.

So, user roles are like assigning specific jobs to different people on the eCommerce platform. It helps keep everything organized and secure, making sure the right people have the right responsibilities.

Only the Site Administrator can access and manage the Account Settings in SureCart, including Store, Clearing Test Data settings, assign user roles in the store, etc.

### **Access Levels and Restrictions for Each User Role**

#### **SureCart Customer Role**

People who make purchases from your store are assigned this role. They can:

- Access the [Customer Dashboard](https://surecart.com/docs/customers-update-account/).

- View Payment History and Billing Details, making modifications.

- Update personal data, add credit card details, and review/modify payment methods.

#### **SureCart Shop Worker Role**

This role is assigned by website admins to people who will be managing and fulfilling orders. They can:

- Handle orders, packaging, and shipping.
- Update order fulfillment details.
- Create Promotions.
- Review Balance or Credit Transactions.
- Upload files while creating products.

#### **SureCart Accountant Role**

This role is for employees who will review financial reports and profits. They can:

- For reviewing reports and profits via the Dashboard
- Check the sales and profits in the dashboard, making sure everything adds up
- Cannot modify the website's look and feel or edit the products

#### **SureCart Shop Manager Role**

They do what Shop Workers do, plus:

- Viewing Reports and Sensitive Shop Data like customer details.
- Exporting Shop Reports and adjusting related Settings like name, timezone, notifications, etc.
- Assign user roles to your store.
- Manage orders, refunds, products, pricing, and forms.

#### **Site Administrator Role**

This is the general WordPress Admin role that manages Account and Test Data settings, distinct from Shop Managers.

Site administrators can control every part of your website, including every setting within SureCart.

### **Best Practices for User Permissions**

Provide access to users only when they really need it. Avoid giving extra permissions if they're not necessary. This keeps your website safe and stops users from making bad changes or deleting things.

Not many users need the Admin role on the website. To keep your site safe, you can limit this. Most users can do their jobs well with fewer abilities on your store.

If you want more control over what users can do on your website, think about using a free tool called [User Role Editor](https://wordpress.org/plugins/user-role-editor/). It helps you pick what each user can do.

Further, there might be a scenario where you do not require SureCart roles on your store. In that scenario, you can simply [remove SureCart roles](https://surecart.com/docs/how-to-remove-surecart-user-roles/) that you do not need.

### **Conclusion**

In conclusion, user roles play a big role on a WordPress website, especially when many people are in charge. This is true for eCommerce stores made with SureCart too.

As you are dealing with sensitive data from customers, it is of high importance to only let certain users see what they need to. You should only give certain powers to users who really need them.

If you have any questions about the SureCart Roles, you can reach out to us and we are happy to help.


===== SOURCE: variant-images.md =====

---
source_url: https://surecart.com/docs/variant-images
source: surecart-kb
scraped: true
---

# How to Link Images to Product Variants in SureCart

In SureCart, you can link images to specific product variants to ensure the correct image is displayed when a customer selects a variant option (e.g., color, size) on the product page. This guide will walk you through the steps to link an image to a variant using SureCart settings and the WordPress Media Library.

### **Set Up Variants in SureCart**

Before linking an image to a variant, ensure that your product has variants set up correctly. For more detailed instructions on creating and managing product variants, check out our Creating and Managing Variants guide.

You can do this in the SureCart product settings:

- **Option Name:** This is the category of the variant (e.g., Color, Size).
- **Option Values:** These are the specific variants under each category (e.g., White, Black, Light Green for Color).

**Example**:

Option Name: _Color_

Option Values: _White, Black, Light Green_

### **Link Media to a Variant**

You can easily link images or videos to specific product variants in SureCart. This allows customers to see the correct media when they select a particular option (e.g., color, size, style).

1. In your **Product Images/Media** gallery, hover over the image or video you want to link to a variant.
   - Click the **pencil (edit)** icon to open the media details.
2. In the **Edit Media** panel, scroll down to the **Variation** section.
3. From the **Option** dropdown, select the exact variant option that should display this media.
   - Example: _Color — Green_
   - If you want the media to display for all variants, leave it set to **(All Variations)**.
4. Click **Done** to save your changes.

### Working with Videos

SureCart also supports linking videos to product variants. This is useful for showing product demos, promotional clips, or tutorials.

When editing a video, you have the following options:

- **Poster**: Choose a poster image that will display before the video plays. You can select an image from the library or generate a thumbnail from the video.
- **Aspect Ratio**: Define how the video should be displayed (e.g., 1:1, 16:9).
- **Variation**: Just like with images, you can assign the video to a specific variant option. Example: _Size — Large_. Or keep it as **(All Variations)** so the video shows for every variant.

### **Verify the Link**

To ensure that the image is correctly linked to the variant:

1. Go back to your product page in SureCart.
2. Select the variant option on the product page (e.g., choose "Light Green" from the color options).
3. The image you linked should now appear when the variant is selected.

## **Frequent Asked Questions**

**Can I use videos as variant media?**

Yes, videos can be linked to specific variants just like images. In the **Edit Media** panel for the video, you can select a **Poster** image, choose the **Aspect Ratio**, and set the **Variation > Option** to link the video to a specific variant (or leave as **(All Variations)**).

**What happens if I leave the variation set to "(All Variations)"?**

The media (image or video) will be visible regardless of which variant option is selected. Use this when you want a universal image or video to show for every variant.

**How do I verify the media link is working?**

On your product page, select the variant (e.g. "Green" or "Large"). The linked image or video should appear when that variant is active.


===== SOURCE: vault-plan.md =====

---
source_url: https://surecart.com/docs/vault-plan
source: surecart-kb
scraped: true
---

# Vault – Redeem & Manage Your SureCart Pro Plan

The Vault provides access to premium plugins and tools from Brainstorm Force, including the SureCart Pro plan. Once purchased, users can redeem and manage their Vault benefits directly within their SureCart account.

## Redeeming a Vault Plan

### Step 1: Locate Your Purchase ID

After clicking **Redeem** in your Vault Dashboard, a unique Purchase ID is generated for your SureCart Pro plan. This code is not displayed in the dashboard; instead, it's sent via email.

Look for an email with the subject: **"Access your SureCart Pro plan"**

The Purchase ID resembles: `3f21b502-e8ba-42cc-9ef9-086809516e31`

### Step 2: Sign In or Create Your SureCart Account

Visit [https://app.surecart.com](https://app.surecart.com)

You can either log into an existing account or create a new one. Note that your SureCart login is separate from your Vault login—password changes in one don't affect the other.

### Step 3: Redeem Your Purchase ID

1. Open **Settings** (gear icon)
2. Navigate to **Plan & Billing**
3. Click **"Click here to claim it."**
4. Paste your Purchase ID
5. Click the **Claim** button

Your SureCart Pro plan activates immediately for your organization.

## Managing a Vault Plan

### Update Your Vault Subscription

Your Vault subscription is billed and managed through the Vault store.

1. Visit [https://vault.brainstormforce.com/customer-dashboard/](https://vault.brainstormforce.com/customer-dashboard/)
2. Sign in using your purchase email

From your account dashboard, you can:

- View billing details
- Update payment information
- Renew or cancel your subscription
- Access invoices

Changes automatically reflect in your SureCart organization once your subscription status updates.

### Remove the Plan from Your Current Organization

To use your Vault plan with a different SureCart organization:

1. Log into **app.surecart.com**
2. Select the organization with the current Vault plan
3. Click the **gear icon**
4. Choose **Plan & Billing**
5. Click **Remove Vault Plan**
6. Confirm the removal

The organization reverts to the default plan and no longer uses Vault benefits.

### Activate the Plan in a Different Organization

After removal, apply the plan to a new organization:

1. Switch to the new organization
2. Go to **Plan & Billing**
3. Click **"Click here to claim it."**
4. Enter your Purchase ID
5. Click **Claim**

Your Vault plan becomes active for the new organization.

## Support

For assistance with redeeming your plan:

- Email: **support@surecart.com**
- Contact Vault support through your customer dashboard


===== SOURCE: view-your-order-button-in-emails-not-working.md =====

---
source_url: https://surecart.com/docs/view-your-order-button-in-emails-not-working
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Troubleshooting](https://surecart.com/docs-category/troubleshooting/)/View your order button in emails not working

# View your order button in emails not working

When you setup your SureCart store, certain important pieces of data need to be filled out.

Most important is the support email address and the store website address.

These are used in the emails that go to your buyers. Without these, the reply to email will not go to you and the "View your order" button in the emails also will lead to nowhere.

The good news is it will just take you a minute to fill these out!

## How to add your store details

To make sure the "View your order" button in your buyer's email functions properly, you need to add store details and contact information. Otherwise, the view your order button won't lead them anywhere.

- Navigate to **Settings** in SureCart, then click on **Store Settings**.

- Before moving forward, please complete the **Store Details** section if you haven't already.

- Scroll down slightly and add your **Contact Information** in the Store Settings.

The "View your order" button in buyer emails should now function correctly.

We hope this guide was helpful. If you have questions or if the solution above doesn't work for you, please contact our support team. We're here to assist you!


