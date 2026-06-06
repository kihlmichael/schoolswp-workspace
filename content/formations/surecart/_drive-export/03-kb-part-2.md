# SureCart - Base de connaissances (partie 2 sur 4)


===== SOURCE: customers-access-dashboard.md =====

---
source_url: https://surecart.com/docs/customers-access-dashboard
source: surecart-kb
scraped: true
---

# How Can Customers Access the Dashboard - SureCart

## Overview

SureCart automatically generates a customer dashboard page when you activate the plugin. This "my account" page allows customers to manage orders, downloads, plans, account information, payment methods, and passwords.

## Access Methods

### During Purchase

After completing a purchase, customers see a **"Manage Orders" button** on the thank you page that directs them to their dashboard.

Customers also receive an order notification email containing a "View Order Details" button that redirects them to the dashboard.

**First-time access:** New customers receive a prompt to set up a password for future logins (unless a password field was included in checkout).

### Via Header Menu

The dashboard page is automatically created with a front-end URL when SureCart installs.

**To add dashboard access to your menu:**

1. Navigate to **Appearance > Menus**
2. In the Pages section, click **View All**
3. Select **Dashboard** and click **Add to Menu**
4. Click **Save Menu**

This makes the dashboard link accessible from your site's main navigation, requiring customers to log in when they click it.

## Dashboard Features

Customers can view recent orders, manage subscriptions, update account details, modify payment methods, and download receipts or invoices from their dashboard.


===== SOURCE: customers-change-password.md =====

---
source_url: https://surecart.com/docs/customers-change-password
source: surecart-kb
scraped: true
---

# How Can Customers Change Their Password

## What is a Customer Dashboard?

The customer dashboard is an automatically generated page in SureCart functioning as an account page. It allows customers to access recent orders, downloads, plans, and account information. Customers can update passwords, review billing details, manage payment methods, add or delete payment options, and select default payment methods.

## How Can Customers Change Their Passwords?

Customers access the dashboard at their domain followed by "/customer-dashboard" (e.g., example.com/customer-dashboard).

**Steps to change password:**

1. Log in with credentials to the customer dashboard
2. Once logged in, click the avatar in the bottom left corner next to their name
3. Select "Account" from the menu options
4. Locate the "Update Password" section
5. Enter the new password and confirm it in the corresponding fields
6. Click the "Update Password" button to save changes

## What if Customers Forget Their Password?

If customers forget their passwords, they can regain access by:

1. Visiting the Customer Dashboard
2. Entering their email address
3. Clicking "Send a login code"
4. Opening their email and copying the confirmation code
5. Returning to the dashboard and pasting the confirmation code
6. Using the steps above to reset their password

Customers can then use their new password for future logins.


===== SOURCE: customers-update-account.md =====

---
source_url: https://surecart.com/docs/customers-update-account
source: surecart-kb
scraped: true
---

# How Can Customers Update Their Account Details

## What is Customer Dashboard?

The customer dashboard is an automatically generated page in SureCart functioning as a "my account" area. It allows customers to view recent orders, downloads, subscription plans, and account information. Customers can also manage passwords, billing details, and payment methods from this location.

## How Can Customers Update Their Account Details?

The default dashboard URL follows the pattern: yourdomain.com/customer-dashboard

### Step-by-Step Instructions

1. **Log In**: Customers enter their login credentials to access the dashboard.

2. **Access Account Menu**: Locate the avatar displaying the customer's name in the bottom left corner and click it.

3. **Select Account Option**: Choose "Account" from the menu that appears.

4. **Modify Fields**: In the "Update Account Details" section, customers can change:
   - Account Email
   - First Name
   - Last Name
   - Display Name

5. **Save Changes**: Click the "Save" button to apply modifications.

The display name updates immediately upon saving. All changes persist across the dashboard after confirmation.


===== SOURCE: customers-update-payment.md =====

---
source_url: https://surecart.com/docs/customers-update-payment
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Customer Dashboard](https://surecart.com/docs-category/customer-dashboard/)/How Can Customers Update Their Payment Methods?

# How Can Customers Update Their Payment Methods?

This document explains how to add, update, and set a default payment method from the SureCart Customer Dashboard. The steps below are written from the customer's perspective and can be shared directly with customers who need to manage their payment methods.

For a general overview of the Customer Dashboard and its sections, refer to [Customer Dashboard Overview](https://surecart.com/docs/overview-customer-dashboard/).

## **Requirements**

- An existing customer account on the store
- Access to the email address associated with the customer account
- A payment method to add (such as a credit or debit card)

## **Accessing the Customer Dashboard**

The Customer Dashboard is available at the store domain followed by the customer-dashboard slug. For example, if the store domain is example.com, the dashboard is located at example.com/customer-dashboard.

- Open the Customer Dashboard URL in a web browser.
- Enter the email address used during checkout, then click **Next**.
- Enter the password, then click **Login**.

For more detail on signing in, refer to [How Customers Access the Dashboard](https://surecart.com/docs/customers-access-dashboard/).

## **Adding a Payment Method**

- After signing in, click the avatar in the bottom-left corner, next to the account name.
- Select **Billing** from the menu.
- Click **Add** in the top-right corner of the Billing section.
- Enter the card information in the form.
- Click **Save Payment Method**.

**Expected outcome:** The new payment method is added to the account and appears in the list of saved payment methods in the Billing section.

## **Setting a Default Payment Method**

The default payment method is used for future payments and subscription renewals.

- In the Billing section, click the three-dot menu next to the payment method to set as default.
- Select **Make Default**. A confirmation popup appears.
- To apply this payment method to all active subscriptions, toggle on **Update All Subscriptions**.
- Click **Make Default** to confirm.

**Expected outcome:** The selected payment method becomes the default for future payments. When **Update All Subscriptions** is enabled, all active subscriptions are also switched to the new default payment method.

## **Notes and Limitations**

- Payment method data is processed and stored securely by the connected payment processor (such as Stripe). SureCart and the store owner do not store full card numbers.
- Setting a payment method as default without enabling **Update All Subscriptions** applies the default only to future one-time payments and to new subscriptions. Existing subscriptions continue to use their previously assigned payment method.
- The available payment method types depend on the payment processors connected to the store. If a processor only supports cards, only cards can be added.
- Removing a payment method that is currently assigned to an active subscription may cause the next renewal to fail. Assigning a different payment method to the subscription before removing the old one is recommended.

## **Related Documentation**

- [Customer Dashboard Overview](https://surecart.com/docs/overview-customer-dashboard/)
- [How Customers Access the Dashboard](https://surecart.com/docs/customers-access-dashboard/)
- [How Customers Update Account Details](https://surecart.com/docs/customers-update-account/)
- [How Customers Change Their Password](https://surecart.com/docs/customers-change-password/)
- [Managing Subscriptions in the Customer Dashboard](https://surecart.com/docs/subcription-in-customer-dashboard/)

## **FAQ**

**Does adding a new payment method automatically update active subscriptions?**

No. Adding a payment method only saves it to the account. To use it for active subscriptions, it must be set as the default with the **Update All Subscriptions** option enabled, or assigned individually to each subscription.

**What happens to existing subscriptions when a new default is set without enabling Update All Subscriptions?**

Existing subscriptions keep their currently assigned payment method. The new default applies only to future one-time payments and to subscriptions created afterward.

**Can more than one payment method be saved at the same time?**

Yes. Multiple payment methods can be saved in the Billing section. One of them is marked as the default, and the others remain available to be assigned to specific subscriptions or set as the default later.

**How is a payment method removed?**

In the Billing section, click the three-dot menu next to the payment method and select the remove option. If the payment method is assigned to an active subscription, assigning a different payment method to that subscription first is recommended to avoid a failed renewal.

**What types of payment methods can be added?**

The available types depend on the payment processors connected to the store. Card payments are supported when a card-capable processor (such as Stripe) is connected. Other methods may be available depending on the processor configuration.

**What happens if a saved card expires or is declined?**

If the default card expires or a payment is declined, the associated payment may fail. Adding a new valid payment method and setting it as the default resolves this. For subscriptions, the renewal can be retried after a valid payment method is in place.


===== SOURCE: customers-upgrade-downgrade-subscription.md =====

---
source_url: https://surecart.com/docs/customers-upgrade-downgrade-subscription
source: surecart-kb
scraped: true
---

# How Customers Can Upgrade/Downgrade a Subscription

## Overview

Customers can independently manage their subscription plans through the SureCart customer dashboard without needing to contact merchant support. The process allows upgrading to higher-tier plans or downgrading to lower-tier plans.

## Step-by-Step Process

**Step 1: Access the Dashboard**
Customers must log into their SureCart customer dashboard.

**Step 2: Navigate to Plans**
Select the "Plans" tab and choose the product they wish to modify.

**Step 3: Select New Plan**
Under "Update Plan," customers can choose either a higher plan (upgrade) or lower plan (downgrade).

**Step 4: Proceed**
Click the "Next" button to continue.

**Step 5: Review Timing Notification**
The system displays how the change will be processed based on merchant settings:

- **Immediate renewal**: Subscription changes take effect right away
- **Next billing cycle**: Changes apply at the end of the current billing period

**Step 6: Confirm**
Click "Confirm" to finalize the plan change.

## Billing Outcomes

When downgrading immediately (for example, from yearly to monthly), the current payment balance becomes $0, and remaining credits apply to future monthly charges.

## Post-Change

SureCart automatically generates a prorated invoice and sends it to the customer's registered email address.


===== SOURCE: customize-email-templates.md =====

---
source_url: https://surecart.com/docs/customize-email-templates
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Email](https://surecart.com/docs-category/email/)/How to Customize Email Templates

# How to Customize Email Templates

SureCart allows you to personalize emails for your customers. You can adjust notification settings, edit content, and add a personal touch to the subject and body.

To customize any email that SureCart sends to customers, please follow the steps below:

### Choosing the Email to Edit

Navigate to SureCart **Settings** > **Notifications**.

You can see the name of the email, the description, and a button to edit. Click on the **Edit** button to customize it.

For example, here we are editing the email message which is sent to customers upon subscription cancellation.

### Overview of Email Editing

Upon clicking on the Edit button, you will be redirected to the [SureCart platform](http://app.surecart.com/) where you will find more of these email templates under the **Email > Customer Emails** section.

You can easily change the Email Subject. The Email Body might look a little daunting for some users but fear not, we are going to make it easy for you.

The **Liquid Variables** are the ones that allow us to output data for this specific template. Most of the work will be in the Email Body, so let's break it down.

### Editing Email Subject

Edit the Email Subject text to your liking. You can use the same example below for testing purposes.

Notice that we used a Liquid Variable called {{ subscription.name }}. We will cover that later.

### Previewing Email to See Changes

Click on the **Save** button to save your changes. You can preview the email by clicking on the **Preview Email** button.

You can see that your new Email Subject has been updated, and the Liquid Variable has been successfully replaced by the Product Name.

If you wish, you can send a test email by clicking on the **Send Test Email** button.

If you make a mistake, you can always revert to the default template by clicking on the **Revert to Default** button.

### Editing Email Body

Let's now change the h3 heading. Replace the text on line 2 from "**Your subscription was canceled**" to "**Your subscription just ended. Please renew!**".

Once you finish your customization, Click on the **Save** button, and then click on the **Preview Email** button to see a preview.

### Liquid Variables

Liquid variables, like {{ subscription.name }}, insert dynamic content in the email templates.

For example, here's how the Liquid Variables for this **Order Confirmation** email template are displayed:

```
   "store": {
    "brand": {
      "address": "Logoipsum\n2200 Tinker Loop\nAlamogordo New York 88310\nUnited States of America",
      "email": "suport@storename.com",
      "logo_url": "https://media.surecart.com/4zqjol8ny24sf7zibtkbop7vqmqw",
      "phone": "(575) 479-4701",
      "website": "https://storename.com"
    },
    "name": "Store Name",
    "url": "https://storename.com"
  }
```

Here is how we extract it to be used as a variable in our email body.

- `{{ store.brand.address }}`: This variable will output the store's brand address.
- `{{ store.brand.email }}`: This variable will output the store's brand email address.
- `{{ store.brand.logo_url }}`: This variable will output the store's brand logo URL.
- `{{ store.brand.phone }}`: This variable will output the store's brand phone number.
- `{{ store.brand.website }}`: This variable will output the store's brand website.
- `{{ store.name }}`: This variable will output the store's name.
- `{{ store.url }}`: This variable will output the store's URL.

You can follow the same idea to extract the variable and modify your email to best suit your company's needs.

### Filters

Let's see just a few filters that will help you personalize your email templates.

#### Capitalize Letters

Suppose the customer typed their name all in small caps, like "**adrian l. derossett**" and you want the email to capitalize. So here's how you can do it in the email body:

```
{{ "adrian l. derosset" | capitalize }}
```

The result will be: "**Adrian L. Derosset**".

#### Prepend and Append

Going one step further we can also append or prepend some text to it, see an example here of prepend:

```
{{ "adrian l. derosset" | capitalize | prepend: "Hello " }}
```

The result will be: "**Hello** **Adrian L.** **Derosset**".

#### Splitting the Name

Now, suppose you want only the first name – some people have big names, and it would be odd to add to an email a big name. So one way you can accomplish it is this:

```
{{ "adrian l. derossett" | split: " " | first | capitalize | prepend: "Hello "}}
```

The result will be: "**Hello Adrian**".

#### Finding More Filters

We covered just a few filters, but you can see all filters available [here](https://shopify.github.io/liquid/basics/introduction/).

That's it with this guide. If you have any more questions or come across any issues, please feel free to reach out to our support team. We're always here to help!


===== SOURCE: customize-text-in-order-confirmation-popup.md =====

---
source_url: https://surecart.com/docs/customize-text-in-order-confirmation-popup
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/Customize text in order confirmation popup

# Customize text in order confirmation popup

After an order is placed, your buyer will see an order confirmation popup.

You may want to change the text in this popup to match your brand and style.

You can easily accomplish this for each custom checkout form you create.

- Navigate to the checkout form editor, and click on the top bar as shown in the image. This will reveal the checkout form settings in the right panel.

- Click on **Success Text** to reveal the text placeholders that you can edit which include the title, description, and button text.

- Save your form by clicking on the **Update** button.

You can edit this text according to your brand and preferences. Personalizing it will help align the content with your unique style and communication preferences.

We hope this guide helped you. If you have any questions, please don't hesitate to contact our support team. We're here to help!


===== SOURCE: dashboard-not-working.md =====

---
source_url: https://surecart.com/docs/dashboard-not-working
source: surecart-kb
scraped: true
---

# Help! My Customer Dashboard Is Not Working

## What is the Customer Dashboard

The customer dashboard is a dedicated page automatically generated when you activate SureCart. It functions as an account page where customers can access recent orders, downloads, subscription plans, and account information. Customers can also update passwords, review billing details, and manage payment methods including adding, deleting, and selecting default payment options.

## Troubleshooting Guide

### Customer Dashboard Leads to a 404 Page

#### Case 1 - Page in Draft or Pending Review

If the dashboard works for you but not for customers:

1. Navigate to WordPress > Pages
2. Locate the Dashboard page or custom Thank You page
3. If the page status is Draft or Pending Review, change it to Published
4. Test by opening the page in an incognito window where you are not logged in

#### Case 2 - Page Trashed

If the dashboard is missing from your pages list:

1. Go to WordPress > Pages > All Pages
2. Check the Trash folder for the Dashboard page
3. Click the "Restore" button if found
4. Confirm the page is published

#### Case 3 - Page Deleted

If the Customer Dashboard does not appear in your pages or trash:

1. Go to Plugins
2. Deactivate SureCart (your data remains safe)
3. Activate SureCart again
4. Navigate to WordPress > Pages > All Pages

The dashboard will be automatically recreated and restored to working condition.

## Need Further Help

If you encounter different issues or need additional assistance, contact SureCart support for personalized help.


===== SOURCE: default-country-for-address.md =====

---
source_url: https://surecart.com/docs/default-country-for-address
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/How to Set Default Country Code in Address Block

# How to Set Default Country Code in Address Block

This document explains how to set the default country in the Address block of your checkout form.

## Requirements

- WordPress admin access
- SureCart installed and activated
- A checkout form already created

## Step-by-Step Instructions

1. Go to **WordPress Dashboard → SureCart → Custom Forms**.
2. Click to edit your checkout form.

## Add the Address Block (If Needed)

If the Address block is not present:

1. Click the **+ Add Block** button in the form editor.
2. Search for **Address**.
3. Select the block to add it to your form.
4. Click **Save**.

## Set the Default Country

1. Click the **Address** block.
2. In the right-hand settings panel, scroll to find the **Default Country** option.
3. Select your preferred default country.
4. Click **Save**.

## Expected Outcome

The selected country will be pre-selected for customers in the Address section during checkout.

## Notes and Limitations

- The Address block can be used for both physical and digital products.
- If you are selling digital products only, the block label can be renamed.
- Changes apply immediately after updating the form.

## FAQ

**Why don't I see the Shipping Address block in my checkout form?**

The Shipping Address section is part of the Address block. If your product requires shipping or tax calculation, SureCart may automatically require address information during checkout.

**Can I remove the Address block from my checkout form?**

Yes, but if the products require shipping or tax calculation, SureCart may still require address information during checkout.


===== SOURCE: delete-business-and-user-account.md =====

---
source_url: https://surecart.com/docs/delete-business-and-user-account
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Settings](https://surecart.com/docs-category/settings/)/How to Permanently Delete Your Business and User Account

# How to Permanently Delete Your Business and User Account

If you want to permanently delete a business from your SureCart account, or delete your SureCart user, here is how.

When you first setup SureCart, you did 3 things:

1. Installed the [SureCart plugin](https://surecart.com/) on your website
2. Created a SureCart account
3. Created a business that is linked to your SureCart account

Follow these steps to delete both business and user accounts from your website.

### Removing the SureCart Plugin

Removing the SureCart plugin is very simple, it's the same process as removing any plugin on your website where you deactivate it and then delete it.

- You can find your plugin at **Plugins** > **Installed Plugins**.

This will delete the plugin from your WordPress dashboard.

### Deleting Your SureCart Store

For this step, you will need to log into the [SureCart platform](https://app.surecart.com/) with the username and password you used.

Once inside your account:

- Navigate to the **General** section under **Settings**.

- Scroll down and click on the **Delete Store** button.

This will permanently delete your SureCart store.

### Deleting Your SureCart User Account.

For this step, you'll need to stay logged into the same SureCart platform.

- Click on the toggle to the right of your name in the top right corner of the screen, then click on the **Profile** icon.

- A slide-out panel will appear on the right, click on **Delete User**.

- A new prompt will pop up that'll urge you to type CONFIRM in a text box.
- Just type it and click on the **Confirm** button to finally delete your user account.

This will permanently delete your user account.

Be very careful while following these steps as it will result in the permanent deletion of your SureCart store as well as all the data associated with it.

That's it! We hope this guide helped you. If you have any more questions, please feel free to reach out to our support team. We're here to assist you!


===== SOURCE: delete-customer.md =====

---
source_url: https://surecart.com/docs/delete-customer
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Online Store](https://surecart.com/docs-category/online-store/)/Can I Delete a SureCart Customer?

# Can I Delete a SureCart Customer?

You might be wondering how to delete a SureCart customer.

You **cannot delete a customer who made a purchase** and has a checkout because we want to preserve the integrity of your data and avoid any inconsistencies.

For example, if you delete a customer who has a checkout, you will end up with a checkout record in SureCart with no associated customer. This can cause problems with your reports, analytics, and refunds.

But If you manually added a customer from the Customers tab in SureCart, you can delete them. However, you can only do so if they have not made any purchases yet.

If you don't want to keep customers on your website anymore, you can delete them. Remember, even if you remove them from the website, their information is still saved in the SureCart database, [which can be exported.](https://surecart.com/docs/export-order-data)

You also have the option to delete customers for whom you've processed test payments in test mode. You can learn more about this [here](https://surecart.com/docs/clear-test-data/).

### How to Delete the User from Your Website

If you need to remove a user created, with the SureCart customer role, on your WordPress website during a customer's purchase, here's how you can do it:

You can go to the Users tab in WordPress, find the customer you want to delete, and delete them from there. This will remove them from your WordPress site.

1. Go to the **Users** tab from your WordPress website.

2. Hover over the user and click on delete.

3. Confirm Deletion.

The user will be deleted from your website, but their information will stay in the [SureCart database](https://app.surecart.com/).

If you remove a user from your WordPress site and they come back later to purchase with the same email address, don't worry. Their information will still be connected to SureCart. This means you'll be able to see all the past orders they made.

In a nutshell: So, if a SureCart customer bought something, you can't delete it. But if you added them and they bought nothing, you can.

**Can I delete customer data from my SureCart account?**

No, you cannot delete a SureCart customer if they have made any purchases. You can only delete them if you manually add them and they haven't bought anything.


===== SOURCE: delete-surecart-forms.md =====

---
source_url: https://surecart.com/docs/delete-surecart-forms
source: surecart-kb
scraped: true
---

# How to Delete SureCart Custom Forms

To delete any SureCart custom forms, go to your website, find SureCart, and click on Forms. By hovering over the custom checkout form with your mouse, you can click on the Trash button.

Once you've put your form in the trash, it will be deleted.

**Note:** Please don't remove the default SureCart form & page named "Checkout – Store Checkout". If someone tries to buy a product, they need this page. If it's gone, they can't buy anything from your website.

If you deleted the default checkout form, you can bring it back by deactivating and re-activating the SureCart plugin.


===== SOURCE: developer-docs.md =====

---
source_url: https://surecart.com/docs/developer-docs
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Developer Docs](https://surecart.com/docs-category/developer-docs/)/Developer Docs

# Developer Docs

SureCart is fully extendable with hooks and filters along with our open API.

[Developer Documentation](https://developer.surecart.com/docs/)

[API Documentation](https://api-docs.surecart.com/)


===== SOURCE: disable-checkout-item-removal.md =====

---
source_url: https://surecart.com/docs/disable-checkout-item-removal
source: surecart-kb
scraped: true
---

# How to Disable Item Removal in Your Checkout Form

In SureCart, every checkout form comes with the option to remove items that customers may decide against purchasing. It's as simple as clicking on the cancel icon within the order summary.

In this guide, we'll walk you through the steps to disable the removal of items from your checkout form, giving your users the flexibility they need.

## **How To Disable This Option?**

By default, this option is enabled in SureCart. To disable it, just follow these steps:

- Navigate to the **SureCart** dashboard and select **Custom Forms** to access your checkout form.
- Begin by selecting the **Order Summary** block in the editor and open the **List View** by clicking on this icon.

This action shows where the order summary items are located in the list view, specifically under **Totals**.

- Expand the **Totals** option. You'll find removable checkout items under **Line Items**. Select it.
- To disable the removable items, toggle off the **Removable** button on the right-hand side.
- Click on the **Update** button to apply these changes on your checkout form.

Thats it! Now, if you check it out – the option to remove items from the order summary is no longer visible.


===== SOURCE: disable-editing-quantities.md =====

---
source_url: https://surecart.com/docs/disable-editing-quantities
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/How to Disable Editing Quantities in Your Checkout Form

# How to Disable Editing Quantities in Your Checkout Form

This document explains how to disable quantity editing in a SureCart checkout form, preventing customers from increasing or decreasing product quantities during checkout.

### **Requirements**

- WordPress admin access
- SureCart installed and activated
- An existing checkout form

### **Quantity Editing Overview**

By default, SureCart allows customers to adjust product quantities directly in the order summary during checkout.

When quantity editing is disabled:

- The **+** and **−** controls are hidden
- Customers cannot change product quantities from the checkout form

### **Disable Quantity Editing in the Checkout Form**

Follow the steps below to disable quantity editing.

However, if you prefer to restrict this feature for your customers, SureCart also provides you an option to disable it.

If you disable this feature, the above **'+'** and **'-'** icons won't show up for your customers. In this article, we'll show you exactly how you can do it.

- Go to **WordPress Dashboard → SureCart → Checkout**.
- Open the checkout form you want to edit.
- Select the **Order Summary** block.
- Open the **List View** to locate the block structure.
- Expand **Totals**.
- Select **Line Items**.
- In the settings panel on the right, disable the **Editable** option.
- Click **Update** to save the changes.

### **Expected Outcome**

After completing these steps, customers will no longer see quantity controls in the order summary and will not be able to change product quantities during checkout.

### **Notes and Limitations**

- Existing orders are not affected by this change.
- Disabling quantity editing applies only to the checkout form being edited.
- Customers can still modify quantities before reaching checkout, depending on your store flow.

### **FAQ**

**Does disabling quantity editing remove products from the checkout?**

No. It only prevents customers from changing quantities in the order summary.

**Can I re-enable quantity editing later?**

Yes. You can re-enable the **Editable** option at any time.

**Does this affect all checkout forms?**

No. Quantity editing is configured per checkout form.


===== SOURCE: disable-payment-processor.md =====

---
source_url: https://surecart.com/docs/disable-payment-processor
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Online Store](https://surecart.com/docs-category/online-store/)/How to Disable a Payment Processor

# How to Disable a Payment Processor

In this article, we'll guide you through the process of turning off a payment processor, using Stripe as an example.

However, these steps can be applied to other payment processors as well. So, whether you want to disable Stripe or any other payment processor, this guide will help you do just that.

Let's begin with the process!

### **Disabling a Payment Processor**

In this section, we will quickly learn how to access the necessary settings in SureCart to disable any payment processor.

1. In the SureCart menu, click on "Settings."

2. In the SureCart settings menu, click on "Payment Processors."

3. Click on the payment processor you want to disable. In our case, we will select Stripe.

4. Choose the payment processor you want to disable. Here, we only have "Stripe" enabled in test mode.

5. Select the Stripe account that you want to disable here.

6. Turn the toggle off to deactivate this payment processor.

7. Click on the "Save" button to save your changes.

8. Your payment processor has been successfully disabled. It will not be shown to your customers on the checkout pages!

To remove this account from your connected list of stripe accounts, access the "More" dropdown menu and click the "Disconnect Processor" button.

Similarly, you can disable any payment processor you want!

### Important Note:

- Before making changes, inform your customers of the potential impact on their subscriptions.
- Ensure you understand the implications of disabling or switching processors, especially if you have active subscriptions.
- For customers with Subscriptions/Installments paid via Paypal, disabling this processor will **NOT** stop payments from being charged by this processor. This will continue to be charged via PayPal. Please refer to this guide on how to [cancel or pause a user subscription](https://surecart.com/docs/how-to-cancel-the-subscriptions-in-surecart/), alternatively, once you've activated another payment processor, please advise the customer to update their payment method from the Customer Area.

The process is same for all the payment processors but if you get stuck anywhere, you can reach out to us and we'll be more than happy to assist!


===== SOURCE: display-company-customer-tax-on-invoice.md =====

---
source_url: https://surecart.com/docs/display-company-customer-tax-on-invoice
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Tax](https://surecart.com/docs-category/tax/)/How to Display My Company's or My Customer's Tax ID/VAT on an Invoice

# How to Display My Company's or My Customer's Tax ID/VAT on an Invoice

To display your own tax ID/VAT number on an invoice, you need to add it to your Tax Settings page.

- You can find this under **SureCart > Settings > Taxes.** Enable the **Tax Collection** option and fill in the address details.

- Scroll down a bit and navigate to the applicable **Tax Regions** where you are collecting tax. For this example, we will use the **European Union**.

- Turn on **Collect EU VAT** and enter your VAT number.

The company information will now automatically appear on invoices downloaded by your customers.

To display your customer's tax ID/VAT number on an invoice, please refer to the [How to collect Tax or VAT numbers from your customer](https://surecart.com/docs/how-to-collect-tax-or-vat-numbers-from-your-customers/) doc.

If you face any issues, please reach out to our support team. We're always here to help!


===== SOURCE: download-invoice.md =====

---
source_url: https://surecart.com/docs/download-invoice
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Online Store](https://surecart.com/docs-category/online-store/)/How to Download SureCart Purchase Invoice

# How to Download SureCart Purchase Invoice

If you've purchased a SureCart paid plan and need to download your invoice, follow these steps:

1. Go to [https://app.surecart.com](https://app.surecart.com), select your store from the left panel dropdown, then click the gear icon at the top-right corner and choose **Plan & Billing**.
2. On the left-hand side, click on **Plan Portal**.
3. At the bottom of the page, you will see **Order History**.
4. Select the order for which you need an invoice, then click it to view the order details.
5. Click the **View Invoice** button.
6. You will be able to download or print your invoice.


===== SOURCE: download-invoices.md =====

---
source_url: https://surecart.com/docs/download-invoices
source: surecart-kb
scraped: true
---

# How to Download Receipts/Invoices in SureCart

## Overview

SureCart enables merchants to download receipts and invoices for customer orders. Saving receipts or invoices is important for record-keeping and tax purposes.

## Steps to Download

1. **Access Orders**: Navigate to SureCart's Orders section from your website dashboard
2. **Select Order**: Choose the specific order for which you need the invoice
3. **Locate Download Button**: Scroll to the "Paid Section" and click "Download Receipt / Invoice"
4. **Choose Format**: A new tab opens allowing you to either download as PDF or print directly

Once downloaded, the invoice file becomes available on your computer for storage and reference purposes.


===== SOURCE: dynamic-pricing.md =====

---
source_url: https://surecart.com/docs/dynamic-pricing
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Revenue Boosters](https://surecart.com/docs-category/revenue-booster/)/Dynamic Pricing

# Dynamic Pricing

This document explains what Dynamic Pricing is, how it works, and how to configure pricing rules using real-world examples.

Dynamic Pricing enables you to automatically apply discounts or fees during checkout based on specific conditions, such as cart value, product attributes, customer data, or shipping details.

## Requirements

- WordPress admin access
- SureCart installed and activated
- At least one published product
- Access to **SureCart → Promotions → Dynamic Pricing**

## Creating a Rule

Dynamic Pricing works through **rules**. Each rule defines:

- Where the pricing applies (Checkout, Line Item, or Shipping)
- When it applies in the purchase lifecycle (initial checkout, renewals, or both)
- Under which conditions it applies
- What adjustment is applied (discount or fee)

**Step-by-step:**

1. Go to **Promotions > Dynamic Pricing** and click **Add New**.
2. Enter a **Name** (internal reference) and **Display Name** (visible to customers).

## Using a Template Rule

SureCart provides pre-built templates for common use cases (e.g., Free Shipping Minimum, Subscription renewal discount).

When you create a rule using a template, the **When to Apply** option is automatically pre-selected based on the intended use case.

## When to Apply

This setting is **required** for all Dynamic Pricing rules.

- **All Transactions** — Applies to both initial checkout and future renewals/plan changes.
- **Initial checkout** — Applies only to the customer's first purchase.
- **Renewals & plan changes** — Applies to subscription renewals, upgrades, and downgrades.

## Adding Conditions

Conditions use logical AND/OR logic. Available attributes depend on the rule target (Line Item, Checkout, or Shipping).

**Line Item Schema attributes** include: Quantity, Subtotal Amount, SKU (Product/Variant), Product Name, Product Collection, WordPress User Role, Customer Order Count, Price Type, and more.

**Checkout Schema attributes** include: Subtotal Amount, Line Item Quantity, Order Type, Email, Shipping Amount, Selected Shipping Method Name, WordPress User Role, Customer Order Count, and more.

## Global Settings

Global Settings define how multiple discounts or fees are applied when more than one rule matches.

Available strategies:

- **All** — All matching rules apply
- **First** — Only the first matching rule applies
- **Smallest** — Only the smallest matching discount applies
- **Largest** — Only the largest matching discount applies

You can define different strategies for Checkout, Line items, and Shipping.

## FAQs

**Do Dynamic Pricing rules affect subscription renewals?**

It depends on the **When to Apply** setting. Choose Initial checkout, Renewals & plan changes, or All Transactions explicitly.

**What happens if multiple rules match?**

All matching rules are evaluated. The final behavior depends on your Global Settings configuration.

**Do Dynamic Pricing rules replace coupons?**

No. Dynamic Pricing applies automatically. Coupons require customer input and are managed separately.

**Can I schedule when a Dynamic Pricing rule is active?**

Yes. Each rule can have a start and end date.


===== SOURCE: edit-checkout-form.md =====

---
source_url: https://surecart.com/docs/edit-checkout-form
source: surecart-kb
scraped: true
---

# How to Edit & Customize a Form in Surecart

In the SureCart checkout form, there are several blocks available to help you customize your form with elements like email fields, phone number fields, and more.

### How to Edit and Customize Your Checkout Form

If you already have a checkout form created and you want to make some changes to it:

- On your website, go to SureCart and click on Forms, then click the Edit button below the form where you want to make the changes.
- Click on the block that you want to edit. You will see the settings panel open on the right side of your screen and you can make the desired changes.
- When you're satisfied with the changes, you can update the checkout form from the Update button.

Your checkout form has been updated as per the changes you made.

### How to Add Other Blocks to the Checkout Form

You can add any block on your checkout form as per your requirement to show different things on your checkout form.

For example, to add a Terms and Conditions checkbox field:

- Click the plus sign below any block you already have, search for the Checkbox, and then click it.
- Select the Checkbox text and change it by writing Terms and Conditions.
- Select the Terms and Conditions, click on the link button, and insert the URL of the Terms and Conditions page.
- Toggle on the switch to make it Required and Checked by default.

The newly added blocks will now appear on your checkout page.


===== SOURCE: edit-customer-details-on-invoice.md =====

---
source_url: https://surecart.com/docs/edit-customer-details-on-invoice
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Online Store](https://surecart.com/docs-category/online-store/)/How to Edit Customer Details on an Invoice

# How to Edit Customer Details on an Invoice

SureCart lets you adjust customer details on their invoice after a purchase.

This article guides you on how to do it, and when you might not be able to make changes.

## Invoices With Taxes

If tax was collected for an invoice, you will not be able to adjust the customer details. Since tax is calculated at the time the invoice is paid the customer's address and tax ID/VAT information is locked at this point in time.

You can determine if tax was calculated for an invoice if there is a **Tax** column on the invoice.

## Invoices Without Taxes

If tax was not calculated for an invoice, you can update the customer details.

This can be done by [editing the customers record](https://surecart.com/docs/overview-of-customers-section/) from your WordPress dashboard.

Another way to do this is to have your customer edit their own details from the [customer dashboard](https://surecart.com/docs/overview-customer-dashboard/).

Hope this helped. If you have any more questions or face any issues, please do reach out to our support team. We're always here to help!


===== SOURCE: enable-additional-payment-options.md =====

---
source_url: https://surecart.com/docs/enable-additional-payment-options
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Payments](https://surecart.com/docs-category/payments/)/How to Enable Bank Transfer, Klarna, Clearpay, and More On Your SureCart Store

# How to Enable Bank Transfer, Klarna, Clearpay, and More On Your SureCart Store

Stripe not only supports credit card payments but also various other payment options. This includes popular options like ACH, Klarna, Clearpay, iDEAL, and much more.

The best part? Many times, these alternative payment options mean lower fees for merchants.

In this guide, we'll show you how to easily add these options to your SureCart checkout forms.

## **Enable Payment Options in Stripe**

To use these payment options, we need to enable them both in Stripe as well as in your SureCart account. Let's start with the Stripe steps.

- Login to your [Stripe account](https://dashboard.stripe.com/dashboard), the one connected to your SureCart store.

- Here, click on **Settings**, and then select **Payment methods** on the following screen.

- You'll find various payment options here, including wallets, links, bank debits, and more.

- You can enable any payment option by clicking the **Turn On** button next to its name.

- Let's use the "ACH Direct Debit" option as an example for this guide. As you can see, it's already **Active** on our Stripe dashboard.

Webhooks are typically pre-configured when you are using SureCart. So, simply click **Turn On Anyway** if prompted.

That's it! You have successfully enabled ACH Direct Debit in your SureCart checkout forms. Customers based in the US also have an extra option to pay using their frequently used payment method.

Now, when customers go to the checkout form, they'll see this extra payment option "US bank account" available for them.

**Note**: Stripe will display ACH Direct Debit only when you present pricing in a supported currency and use a [supported payment flow](https://stripe.com/docs/payments/payment-methods/integration-options).

You can try out and enable multiple payment options for your customers and see what works best for you!

That's everything. We hope this guide helped you. Please free to reach out to our support team if you have any more questions.


===== SOURCE: enable-manage-license-addon.md =====

---
source_url: https://surecart.com/docs/enable-manage-license-addon
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Licensing](https://surecart.com/docs-category/licensing/)/How Licenses Work in SureCart

# How Licenses Work in SureCart

SureCart can help you automatically generate licenses for your customers upon product purchase.

It's a really simple setup that requires you to use the SureCart License Addon with SureCart.

This document will help you understand what licenses are, how they work with SureCart, and how you can set up licensing in SureCart.

Let's start with the basics.

### What is the SureCart Licensing and How Does it Work

The SureCart Licensing feature lets you create and manage license keys for any digital items you sell.

Now, let's understand how licensing works in SureCart!

Let's imagine that you sell WordPress plugins. You can enable licensing for your products, and when someone buys your WordPress, they get a unique key in their email after purchase.

Now, when your customers use that license, you can use SureCart's APIs and SDKs to check if the license was created by SureCart or not after a valid purchase.

All plans include access to the licensing feature, but the level of access may vary depending on the specific plan.

So, if you need help setting up product licensing, we're here to walk you through the process.

#### How to Enable Licensing of Products from Your Website

Setting up licensing in SureCart can be done directly from the product page, we just need to enable the license for the products needing a license, Let's take a closer look at this process.

- Open the product page and scroll down to the Licensing section. Toggle on the switch to enable license creation.

- Limit the licenses by entering any desired number in the Activation Limit field. Leave it blank for infinite activations.

- Then click on the Add Downloads button and add your plugins or themes.

- Once you add more files to the Downloads section, you will be able to select the next version from the Current Release dropdown select field.

Once the customer has purchased, they can access the license keys by selecting the purchased product in the Downloads Tab.

### How to Access the Customers' Licenses

You will also have a "Licenses" page where you can view a complete list of all licenses that were generated for your customers after their purchase.

- Go to SureCart from your WordPress website and click on Licenses.

- For each customer you wish to see the license, click on its license key.

When viewing the details of a specific license, you will see a page like this with full activation details.

### How to Validate Licenses with SDK/APIs:

If you're a developer or product owner and you want to make sure your product only runs if a valid SureCart license key is used, you can check out our SDK guide or API docs.

These will show you how to validate SureCart-generated license keys within your product.

- [API Documentation](https://api-docs.surecart.com/reference/introduction) – There are public and private API endpoints for managing licenses and activations.

- [WordPress SDK](https://github.com/surecart/wordpress-sdk) – This SDK can be used to integrate SureCart licensing with your WordPress plugins and themes.

In a nutshell, the License Addon in SureCart basically helps you protect and manage your digital products like a pro.

It ensures only people who've bought your stuff can use it, thanks to unique license keys. It's a handy tool for anyone looking to sell digital goods without the headache of unauthorized sharing.

If you have any questions as you explore the Addon, please get in touch with support.


===== SOURCE: enable-spam-protection.md =====

---
source_url: https://surecart.com/docs/enable-spam-protection
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Settings](https://surecart.com/docs-category/settings/)/How to Enable Spam Protection and Security in SureCart

# How to Enable Spam Protection and Security in SureCart

Spam is definitely one of the most problematic things that we've come across on the internet whether it be on your email, your phone, or even on your online shop.

The good news is that SureCart comes with built-in spam prevention and other security options to help you feel at ease with running your online site.

### What is the Value of Maintaining Shop Security

There are many different types of exploits, hacks, or even simple annoyances that can happen if you don't beef up your store security:

1. Spam
2. Malware
3. Data Hacks
4. DOS Attacks
5. And much more...

A lot of these are very serious issues that could put you and your customers at risk. As the site owner, you hold the responsibility of making sure that you and everyone on your site are protected from any of these attacks and entities.

### What is Spam Protection

Spam is when you get unwanted, annoying messages or actions, often sent in large amounts, that can mess up websites, servers, or services for regular users.

To stop spam, people have come up with different methods. One common way is to add tests or actions that real users can pass but spammers can't.

### SureCart's Spam Protection & Security

You can find the spam protection settings by navigating to your **WordPress Dashboard > SureCart > Settings > Advanced**, from here, scroll down to "Spam Protection & Security."

#### Test Mode Restricted

The **Test Mode Restricted** setting gives you control over who can perform test orders on your site.

When this setting is **enabled** (default), only users with administrator roles can complete test orders that create actual order entries in your system. For non-administrative users, they can still simulate a test order and see a "Test checkout successful" confirmation popup; however, no order data will be saved or processed.

When this setting is **disabled**, anyone with access to the checkout form can perform test orders, and the test orders will create entries in the system.

By default, this setting is **enabled**, ensuring tighter control over test order functionality for enhanced security.

#### Honeypot

Honeypot is a tool that is used to add a field to your forms that are invisible to actual human users on a browser, but are visible to bots.

This is done in the hopes of tricking these bots into filling out the forms as they are programmed to do, and therefore identifying them as such.

In this case, they will be denied access to the site and to complete the form and purchase. As a result, we can prevent them from spamming the site and disallowing the spam transactions from pushing through.

This field is completely invisible to actual users since they are not displayed to people who visit your checkout form.

#### ReCaptcha v3

reCaptcha is probably something that you've seen before and are familiar with. Google was the first to develop this and it started out as a simple puzzle that you need to solve to prove that you are human.

In order to enable reCaptcha v3 in SureCart, you have to register your site and set it up on Google.

Here are the steps on how to register your site:

1. Sign in to your Google Account
2. Go to [Google reCaptcha site admin registration page](https://www.google.com/recaptcha/admin/create)
3. Add a Label, this can be anything but to avoid confusion, you may enter the name of your site in this field
4. Select the reCaptcha type, for this case, select "Score based (v3)"
5. Add the domain/s of your website
6. Agree to the terms of service
7. Click **Submit**

From the next page, you can see your **Site Key** and **Secret Key**. These are the keys that you need to enable your reCaptcha v3 on SureCart.

Back on SureCart, copy the keys and paste them into the corresponding fields from your "Advanced" Tab.

Once you click **Save**, you're all set. Google reCaptcha v3 has been successfully set up on your online shop.

#### Stripe Fraud Monitoring

The **Stripe Fraud Monitoring** setting helps protect your store from fraudulent transactions by utilizing Stripe's built-in fraud detection tools. When enabled, this setting loads **stripe.js** on every page, allowing Stripe to monitor and analyze user activity to identify potential fraud.

**Benefits of enabling Stripe Fraud Monitoring:**

- Prevents fraudulent transactions and chargebacks.
- Monitors user behavior to flag potentially risky activity.
- Seamlessly integrates with your existing Stripe payment gateway.

Enabling this setting is highly recommended for stores processing high transaction volumes or operating in regions with elevated fraud risks.

#### Strong Password Validation

With this option, your password fields, in the checkout form, gain an extra layer of security, ensuring that only strong, validated passwords are accepted.

These validations include requiring passwords to be more than 6 characters long and having a special character included in addition to the alphanumeric password.

With this enabled, you can be sure that you and your users adhere to these rules to help contain any potential for breaches in security related to weak and easily guessed passwords.

By following these guidelines, you can be rest assured that you may never have the problem of dealing with spam and security issues in your SureCart store.


===== SOURCE: enable-stripe-payment-methods.md =====

---
source_url: https://surecart.com/docs/enable-stripe-payment-methods
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Uncategorized](https://surecart.com/docs-category/uncategorized/)/How to Enable Stripe Payment Methods

# How to Enable Stripe Payment Methods

Did you know that when you have a Stripe account, you can accept more than just credit card payments? In fact, they support nearly 20 different payment methods, most of which you can use with SureCart.

To view the full list of payment methods that Stripe supports by country and currency, click [here](https://stripe.com/docs/payments/payment-methods/integration-options#country-currency-support).

See the full doc [here](https://surecart.com/docs/connect-stripe/).

If you are having issues, please check out our [troubleshooting doc](https://surecart.com/docs/connect-stripe/#verifying-the-surecart-configuration-in-stripe).


===== SOURCE: enable-upsell-funnels.md =====

---
source_url: https://surecart.com/docs/enable-upsell-funnels
source: surecart-kb
scraped: true
---

# How to Enable Upsell Funnels in SureCart

SureCart enables merchants to implement upsells to convince customers to purchase higher-tier product versions, increasing average order value.

## Upsells vs. Order Bumps

- **Upsells**: Offer pricier upgrades after checkout
- **Order Bumps**: Suggest product bundles during checkout

## Adding Upsell Funnels

1. Navigate to **SureCart > Products > Upsells**
2. Click **Add new** and name your upsell (internal name only, not visible to customers)

## Display Conditions

**Options:**
- Show after all product purchases
- Show after specific purchases only

**For Specific Purchases:**
- Click **Add A Condition**
- Select products by name or price from dropdown
- Add multiple conditions as needed

**Show Upsell Offer If** settings (for multiple cart items):
- **All of these are in the cart**: Upsell displays only if all selected products are present
- **Any of these items are in the cart**: Upsell displays if any selected item exists
- **None of these items are in the cart**: Upsell displays only if none are present

## Post Purchase Offer Section

Three components:

1. **Upsell Offer #1**: First upsell customers see after purchase
2. **Upsell Offer #2**: Secondary offer if customer accepts first upsell
3. **Downsell Offer**: Lower-priced alternative if customer rejects first upsell

## Customizing Upsell Offers

### Choose Upsell Title And Product

- Name the upsell (displays to customers at page top)
- Select product from dropdown or search bar

### Upsell Behavior

- **Skip if in order**: Don't show upsell if item already in customer's cart
- **Skip if purchased**: Don't display if customer previously purchased this item
- **Always show**: Display regardless of cart contents or purchase history

### Add To or Replace The Entire Order

**Add to the order:**
- Upsell adds on top of existing order; all previously selected products remain
- Example: T-shirt + hat upsell = cart contains T-shirt + hat

**Replace the entire order:**
- Upsell completely replaces customer's order; all existing cart items removed
- Example: Basic Plan replaced by Pro Plan upsell = cart contains only Pro Plan
- Note: Removes ALL items regardless of quantity

**When to use each:**
- Use **Add to order** to increase order value through product stacking
- Use **Replace entire order** for clear upgrades or alternatives (monthly to annual plan)

### Design The Upsell Offer

- Click **Edit** to customize default upsell template
- All elements are editable: countdown logo, CTA title, product media, typography
- Countdown Timer default: 30 minutes (adjustable)
- Click **Create Offer** to finalize

## Adjusting Upsell Priority

- Rating scale: 1 (lowest priority) to 5 (highest priority)
- When multiple upsells target same product, only highest priority displays

Click **Save Funnel** to apply all changes.

## Troubleshooting: Payment Method Compatibility with Mollie

**Issue:** iDEAL and Bancontact don't appear during checkout when upsell funnels are enabled.

**Reason:** Upsell funnels require payment methods supporting one-click/reusable payment intents. iDEAL and Bancontact support only one-time purchases.

**Solutions:**
- Business dependent on iDEAL/Bancontact: don't use upsell funnels for those products
- For recurring/upsell funnels: use reusable payment intent methods (credit cards, SEPA Direct Debit)

## Frequently Asked Questions

**Q: What happens to payment methods when upsell funnels are active?**
A: Only reusable payment methods display at checkout. SureCart automatically manages compatibility.

**Q: Why isn't my preferred payment method showing?**
A: Payment methods lacking reusable payment support won't appear in checkout containing active upsell funnels.


===== SOURCE: export-order-data.md =====

---
source_url: https://surecart.com/docs/export-order-data
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Settings](https://surecart.com/docs-category/settings/)/How to Export Your Data from SureCart

# How to Export Your Data from SureCart

Today, we're going to walk you through some important steps on how to export your store data from SureCart in a CSV file. This will enable you to uncover valuable insights and make the most of your SureCart store's data.

Whether your goal is to analyze sales trends, make your operations more efficient, or supercharge your marketing efforts, this guide will show you how to export your data effectively.

So, let's get started!

### Types of Data You Can Export from SureCart

Now, let's get to the heart of the matter – what data can you export from SureCart? The possibilities are rich and varied, and here's the impressive lineup:

1.  **Affiliates**: A list of all your affiliate customers and users including their emails and other details.
2.  **Charges:** Get information on all the charges that were processed in your store including information like the amount, payment processor, date, currency, etc.
3.  **Coupons:** Get a list of all the coupons created on your store, both active and inactive.

4.  **Customers:** All the details related to customers like their first name, last name, email, addresses, etc.
5.  **Line Items**: Information and layout of the checkout pages that you have created.
6.  **Orders:** The list of all the orders made on your account with all the associated information for the orders including addresses and payment methods.
7.  **Payouts**: Affiliate payout information.
8.  **Products/Prices:** A list of all the products and their individual pricing options in your store.

9.  **Promotions:** A list of all the promotions run, active and inactive, in your store.

10. **Refunds:** A list of all the refunds processed on your store including all the pertinent information for the refunds.

11. **Subscriptions:** A list of all the subscriptions active and inactive on the account.

By exporting these varieties of data, you can analyze and make data-driven decisions to grow your business.

Let's learn how to export data with SureCart.

### How to Export Each Data Type with SureCart

SureCart exports the data mentioned above in a CSV format.

You can find these settings by following:

1. Navigate to WordPress Dashboard > SureCart >Settings > Data Export.

2. From this screen, choose which data you want to export.

3. Click on the **Export CSV** button, and you will be redirected to your SureCart App Dashboard.

4. From here, you will be brought to the "Exports" tab.

5. In order to export your data, click on the **New Export**(+) button at the top right corner.

6. You will be presented with a popup to select the type of Data to export. Your export will include all records in a CSV format.

7. Enter the email address where you want to receive your data export file.

8. Click on the "**Create**" button.

9. Once done, you will be brought back to the SureCart App Dashboard and you will find the status of the file export.

10. You will get an email when the export is completed with a link to the file.

Similarly, you can follow the same steps to export other types of data. Once this is done, the exported file will contain all the necessary information based on the data type that you selected to export.

We hope this article was helpful. In case you still have questions, we're just a message away!


===== SOURCE: exporting-stripe-data.md =====

---
source_url: https://surecart.com/docs/exporting-stripe-data
source: surecart-kb
scraped: true
---

# How to Get Stripe Customer ID and Payment Method ID

If you're making the transition to SureCart from other billing platforms such as WooCommerce or Shopify, you'll be pleased to know that migrating is a seamless process that won't disrupt your customers' existing subscriptions, provided you're using Stripe for payment collection.

This means that if you start using SureCart to manage subscriptions instead of WooCommerce, your customers' subscriptions will not be affected. They'll simply be charged as they were before in exchange for your services.

To achieve this smooth transition, you'll need to import your customer data into SureCart using a CSV file. This file should include essential information such as the Stripe Customer ID and Payment Method ID.

In this guide, we'll walk you through the steps to get both the Customer ID and Payment Method ID from your Stripe account.

### **How to Export Customer Data with Customer ID & Payment Method ID from Stripe**

You need to have a proper user role in the Stripe account in order to export the data. If you have the necessary access, follow the steps below to export the data:

1. Log in to your Stripe account.
2. Choose the store where you have customer details, then click on the "Customer" tab.
3. Click on the "Export" button.
4. Choose the desired date range in which your customers were added to Stripe.
5. Change the columns to custom and select ID, Email, and Card ID.
6. Click on the "Export" button.

Once you click the "Export" button, your file will be downloaded to your computer, and you're now ready to proceed to the next steps.

### **How to Import New Customers' Data in SureCart**

Now, you need to import your CSV file into SureCart to add or update customer information in your SureCart store. You can do this from the SureCart platform.

If your customers are already registered in SureCart and you simply need to update their payment method ID, you can easily achieve this by importing a CSV file containing the customer ID, Card ID/Payment Method ID, and Customer Email.

SureCart will automatically match the customer using the provided email and update their payment method ID and Customer ID accordingly.

However, if your CSV file includes additional information such as first name and last name, in addition to customer ID, Card ID/Payment Method ID, and Customer email, importing it will not only update the payment method but also update other customer details.

For instance, if a customer named John with the email john@example.com exists in your store, and your CSV lists the first name as Darrel for john@example.com, the customer's name will change to Darrel after the update.

On the other hand, if you do not have any existing customers associated with the email addresses in your SureCart store, importing the CSV file will result in the creation of new customers with only the email address, Stripe Customer ID, and Payment Method ID.

After importing the file, SureCart will automatically match the emails and update the other fields, which in this case are "Stripe Customer Id" and "Stripe Payment Method Id." All the heavy lifting is done for you.

You will notice that the fields "Stripe Customer Id" and "Stripe Payment Method Id" have been successfully updated for the customers that were in your CSV file, while the others remain unchanged.

You can now go and check some customers. You'll notice that they now have a payment method associated with their user accounts.


===== SOURCE: express-payment-wallet-buttons-not-appearing.md =====

---
source_url: https://surecart.com/docs/express-payment-wallet-buttons-not-appearing
source: surecart-kb
scraped: true
---

# Express Payment (Wallet) Buttons Not Appearing

## Overview

Express payments in SureCart offer quick and secure payment options like Apple Pay and Google Pay, enabling users to complete transactions with minimal steps using stored information.

## Enabling the Express Payment Block

The Express Payment block has been removed from SureCart's standard block list as it is now deprecated. To add it manually, use a PHP snippet via your theme's functions.php or a code snippets plugin that registers the block with the inserter enabled.

**Note:** Since this is deprecated, usage occurs at your own discretion without active support.

## Adding the Express Payment Block

1. Navigate to **Custom Forms** in your WordPress dashboard
2. Select the form where you want to enable express payments
3. Click the **+** icon to add a block
4. Search for and select **Express Payment**
5. Users will now see wallet buttons compatible with their browser

## Why Buttons Are Not Appearing

These buttons only appear on their supported browsers and devices. If wallet buttons are not visible, the issue likely stems from browser compatibility:

- **Apple Pay** appears in Safari
- **Google Pay** appears in Chrome
- Other wallets depend on specific browser support

Ensure you are using a supported browser for the specific wallet button you expect to see.

For additional assistance, contact SureCart support.


===== SOURCE: facebook-pixel-integration.md =====

---
source_url: https://surecart.com/docs/facebook-pixel-integration
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/Facebook Pixel Integration

# Facebook Pixel Integration

SureCart will automatically track Facebook Pixel events for you. To enable this, you only need to install the [Facebook Pixel plugin](https://wordpress.org/plugins/official-facebook-pixel/) on your site.

It must be installed directly, not [through Google Tag Manager](https://surecart.com/docs/track-events-with-fbpixels/) or another 3rd party script manager.

Here's how you can install and set up this plugin on your WordPress site.

## Install Meta Pixels for WordPress

- Install and Activate the Meta Pixels plugin on your WordPress dashboard.

- Navigate to **Settings** > **Meta** and click on **Get Started** to connect your Facebook business account to your site.

This will guide you through the process of connecting your Facebook account with the WordPress site. Make sure you have your [Facebook Business account set up](https://www.facebook.com/business/help/1710077379203657?id=180505742745347) properly before proceeding.

- After the integration is complete, confirm the connection to complete the process.

## Events to Track

Here are the events that are sent to Facebook Pixel.

- **Add To Cart**: Sent when a product is added to the cart.
- **InitiateCheckout**: Sent when the checkout is initiated.
- **Purchase**: Sent when a purchase is made or checkout is completed.
- **Start Trial**: Sent when a trial is started, either paid or free.
- **Subscribe**: Sent when a subscription is started.
- **AddPaymentInfo**: Sent when payment info is added to the checkout form.
- **Search**: When a search is performed on the product shop page. The search string is also tracked.
- **ViewContent**: When a specific page product is viewed.

That's it with this guide. If you need assistance with anything else, please contact our support team. We're always here to help!


===== SOURCE: failed-payments-purchase-behavior.md =====

---
source_url: https://surecart.com/docs/failed-payments-purchase-behavior
source: surecart-kb
scraped: true
---

# How to Set Up Failed Payment and Purchase Behavior for Subscriptions

## Overview

SureCart enables you to configure what happens when subscription payments fail. These settings are found in **SureCart > Settings > Subscriptions** and consist of two main components: failed payment handling and purchase behavior options.

## Failed Payments Setup

When a customer's subscription payment fails, their subscription status changes to "Past Due." SureCart's intelligent retry system attempts another payment within a specified timeframe.

**Configuration Options:**

You can select from a dropdown menu to specify how long a subscription remains active after failed payments:

- One week
- Two weeks
- Three weeks

After the selected duration expires without successful payment, the subscription is automatically canceled. This feature gives customers time to update payment methods while protecting your revenue.

## Purchase Behavior Setup

This premium feature (requires account upgrade) provides three configurable options:

### 1. Require Upfront Payment Method

Enables "no credit card required" free trials, allowing customers to access trial periods without providing payment information upfront.

### 2. Prevent Duplicate Trials

When enabled, this prevents customers from receiving multiple trial periods for the same product. Returning customers are charged full price instead of receiving another trial.

### 3. Purchase Revoke Behavior

Specifies when to cancel a user's purchase, offering two choices:

- Immediate cancellation
- Cancellation after all payment methods have been retried

## Access Location

All settings are configurable at **SureCart > Settings > Subscriptions**

**Note:** These features require a premium SureCart account upgrade.


===== SOURCE: fathom-analytics-integration.md =====

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


===== SOURCE: filter-and-display-featured-products.md =====

---
source_url: https://surecart.com/docs/filter-and-display-featured-products
source: surecart-kb
scraped: true
---

# How to Filter and Display Featured Products - SureCart

## Overview

This guide demonstrates how to use Bricks Builder to filter and display only featured SureCart products through query loop configuration.

## Steps

### 1. Enable Query Loop

In the Bricks Builder editor, toggle on the "Query loop" feature to allow dynamic filtering of product posts.

### 2. Select Post Type

Set "Post Type" to "SureCart Product" to ensure the loop retrieves SureCart products rather than standard WordPress posts.

### 3. Add Meta Query

- Locate "Meta Query" under the "Posts" query settings
- Click "+ Add Meta Query" to add a new filtering condition

### 4. Configure Meta Query Settings

Enter the following configuration to filter featured products:
- **Meta key:** featured
- **Meta value:** 1
- **Compare:** Equal
- **Type:** CHAR (or auto-detect if available)

### 5. Save and Test

- Save your changes in the editor
- Preview or check the live page to confirm only products marked as featured display correctly

## Result

The query loop will now display exclusively products with featured metadata set to 1, allowing you to highlight specific items in your store.

## Additional Resources

- Dynamic Data documentation for Bricks Builder
- SureCart Custom Fields customization options


===== SOURCE: fix-surecart-store-disconnected.md =====

---
source_url: https://surecart.com/docs/fix-surecart-store-disconnected
source: surecart-kb
scraped: true
---

# Fix – SureCart store disconnected

There are some situations when the SureCart store is often disconnected from the website. This can happen if you have a plugin that is regenerating WordPress salts – we use this salt to securely store the API token in the database (so it's not in clear text). However, regenerating WordPress salts will cause a disconnection. Often this is caused by security plugins.

The fix is to add a line to your wp-config.php file that will hard-code your api token there. Can you add this:

```
define( 'SURECART_API_TOKEN', 'your_api_token' );
```

Make sure it's above this line:

```
/* That's all, stop editing! Happy publishing. */
```


===== SOURCE: fixing-product-cant-be-blank-error.md =====

---
source_url: https://surecart.com/docs/fixing-product-cant-be-blank-error
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Troubleshooting](https://surecart.com/docs-category/troubleshooting/)/Fixing "Product Can't Be Blank" Error

# Fixing "Product Can't Be Blank" Error

Have you encountered a "Product Can't Be Blank" error during your checkout process? This issue can arise due to a couple of reasons:

1. **Deleted or Archived Product/Price**: If the product or price on your form has been removed or archived, this error may appear. To address this, please ensure you update your form or the purchase button to reference a product or price that's currently available.
2. **Page Caching**: If this page is cached extensively, it might occasionally serve outdated data, which could include archived prices. It's recommended to review and, if necessary, reduce caching settings. You can check our [Caching Guide](https://surecart.com/docs/caching/) to make sure that all your settings are aligned to allow SureCart to function properly.

If you continue to experience difficulties, please contact our support team for further assistance.


===== SOURCE: getting-started.md =====

---
source_url: https://surecart.com/docs/getting-started
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Getting Started](https://surecart.com/docs-category/getting-started/)/Getting Started with SureCart

# Getting Started with SureCart

This document explains how to install SureCart, complete the initial setup, connect a SureCart account, and create the first product.

## **Requirements**

- WordPress admin access
- A WordPress site (self-hosted or cloud-hosted)
- A valid email address for store notifications

## **Installing the SureCart Plugin**

1. Go to **WordPress Dashboard → Plugins → Add New**.
2. Search for **SureCart** in the plugin search field.
3. Click **Install Now**, then click **Activate**.

**Expected outcome:** Once activated, the SureCart menu becomes available in the WordPress sidebar.

## **Completing the Setup Wizard**

### **Step 1: Open the Setup Wizard**

- In the WordPress sidebar, hover over the **SureCart** menu.
- Click **Get Started**.
- On the welcome screen, click **Create New Store**.

### **Step 2: Configure Store Details**

- **Brand Color:** Select the primary color used across store design elements.
- **Store Currency:** Select the currency used to process all transactions.
- Click **Continue** to proceed.

### **Step 3: Select a Starting Point**

- **Start From Scratch:** Creates an empty store with no products.
- **Start With Demo Products:** Creates the store with sample products preloaded.

### **Step 4: Confirm the Notification Email**

- Enter a valid email address in the **Email Address** field.
- Click **Continue** to proceed.

### **Step 5: Finish the Wizard**

Click **View My Products** to access the WordPress dashboard.

## **Connecting the SureCart Account**

After the wizard is finished, the store must be claimed by connecting it to a SureCart account. Without this step, the store may be deleted.

1. In the WordPress dashboard, click **Complete Setup** in the green banner.
2. Sign up or sign in to a SureCart account.
3. Verify the email address via the confirmation email.

**Expected outcome:** The orange notification bar disappears and account setup is complete.

## **Creating the First Product**

1. Go to **WordPress Dashboard → SureCart → Products**.
2. Click **Add New**.
3. Configure the product name, description, price, product type, and images.

**Expected outcome:** Once saved, the product appears in the Products list.

## **Notes and Limitations**

- The brand color and notification email configured during the wizard can be changed later.
- The store must be claimed via the Complete Setup step. Unclaimed stores may be deleted.
- Email verification is required to activate all account features.

## **Related Documentation**

- [How to Install the SureCart Plugin](https://surecart.com/docs/installing-surecart/)
- [Creating a Product in SureCart](https://surecart.com/docs/create-product/)
- [Next Steps After Getting Started with SureCart](https://surecart.com/docs/second-steps/)


===== SOURCE: guest-checkout.md =====

---
source_url: https://surecart.com/docs/guest-checkout
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Settings](https://surecart.com/docs-category/settings/)/Guest checkout

# Guest checkout

## Guest checkouts

Guest checkout is especially convenient for first-time customers who wish to avoid leaving a digital footprint, receiving promotional notifications, or committing to an account for a one-time purchase. Requiring account creation in such scenarios can negatively impact conversion rates. Furthermore, guest checkout provides a faster and more streamlined purchasing experience compared to creating an account.

Although guest checkout may seem appealing to first-time customers, it poses significant drawbacks for merchants. With guest checkout, you can only notify customers about shipping updates. It restricts opportunities for marketing, abandoned cart recovery, sharing promotional materials, sending newsletters, or even requesting product feedback.

## Customer accounts

Registered accounts offer customers a more interactive and personalized shopping experience with the store and its merchants. This connection provides businesses with a valuable marketing opportunity to deliver targeted recommendations and promotional materials. Meanwhile, users gain access to exclusive discounts, stay updated on the latest products, and can leave reviews for items they've purchased.

Another key advantage is the tailored account page, where users can log in to view their purchase history, payment details, and billing information. They can easily manage their account by upgrading or downgrading services, as well as opting in or out of newsletters or other marketing communications.

Additionally, the checkout process for registered users is seamless and efficient. With saved billing information, addresses, and tax details, completing a purchase requires just a single click on the checkout button. This convenience enhances the overall shopping experience for customers.

## How does it work in SureCart?

SureCart currently does not offer a direct "guest checkout" option, as we believe account creation benefits merchants and users. An account is automatically created using the provided email address whenever a user completes a purchase.


===== SOURCE: hide-invoice-button-on-customer-dashboard.md =====

---
source_url: https://surecart.com/docs/hide-invoice-button-on-customer-dashboard
source: surecart-kb
scraped: true
---

# How to Hide/Change the Download Invoice Button on Your Customer Dashboard

## Overview

SureCart displays a download invoice button on the customer dashboard by default. For specific use cases, you may want to hide this button or replace it with custom invoicing solutions.

## Implementation Steps

### Using Code Snippets Plugin

1. Copy the PHP filter code that hooks into `surecart/order/set_attribute` and returns an empty string for the `statement_url` attribute (see source_url for exact code)

2. Navigate to your WordPress dashboard and go to **Snippets > All Snippets > Functions (PHP)**

3. Click "Add New" to create a new code snippet

4. Paste the code into the editor and optionally add a title and description

5. Click "Save Changes and Activate" to enable the snippet

### Alternative Methods

You can implement this code through:

- Your theme's functions.php file directly
- Any code snippets plugin of your choice

## Customization

The invoice URL can be modified according to your specific requirements rather than simply returning an empty string.

## Verification

After activation, visit your customer dashboard to confirm the download button has been removed or modified as intended.

## Support

If issues persist or implementation assistance is needed, contact SureCart's support team.


===== SOURCE: how-to-cancel-the-subscriptions-in-surecart.md =====

---
source_url: https://surecart.com/docs/how-to-cancel-the-subscriptions-in-surecart
source: surecart-kb
scraped: true
---

# How to Cancel Subscriptions in SureCart

## Overview

Canceling a subscription in SureCart is a quick and straightforward process that can be completed in just a few clicks.

## Step-by-Step Instructions

1. **Navigate to Subscriptions**: Go to WordPress dashboard > SureCart > Subscriptions

2. **Select the Subscription**: Click the edit button adjacent to the subscription you wish to cancel

3. **Access Cancel Option**: Click the "Action" button dropdown in the top right corner and select "Cancel Subscription"

4. **Confirm Cancellation**: A confirmation popup will appear where you can choose between:
   - Immediate cancellation
   - Cancellation at the end of the current billing period

   Then click to confirm the cancellation.


===== SOURCE: how-to-create-coupons.md =====

---
source_url: https://surecart.com/docs/how-to-create-coupons
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Revenue Boosters](https://surecart.com/docs-category/revenue-booster/)/How to Create Coupons

# How to Create Coupons

SureCart makes it easy for you to create discount coupons or special offers for your customers. Simply generate coupon codes that customers can apply during checkout for specific purchases in your store.

It's a great way to attract new customers and provide a delightful experience to your existing customer base.

Check out this [article](https://surecart.com/docs/create-coupons/) to learn how you can also create and use these coupons for your store.


===== SOURCE: how-to-create-shipping-profiles.md =====

---
source_url: https://surecart.com/docs/how-to-create-shipping-profiles
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Online Store](https://surecart.com/docs-category/online-store/)/How to Create Shipping Profiles

# How to Create Shipping Profiles

SureCart has an important feature called "Shipping." It allows you to charge customers for shipping based on where they want their orders delivered.

To make this work for your products, you need to create "shipping profiles" and this article will show you how to create a new shipping profile.

Let's get started!

### **What is a Shipping Profile?**

SureCart includes a default profile called "General." But you might be wondering, "Why would I need an extra profile in the first place?

Well, think of a shipping profile as a way to organize where you ship your products and how much you charge for shipping.

When you set up a shipping profile, you can specify the products you want to include, the shipping zones you want to cover, and the shipping methods you want to offer for those products.

By default, SureCart provides a General profile, but you might have specific shipping requirements or want to offer different methods for certain products. That's where creating additional profiles comes in handy.

### **Why would you need an additional profile?**

If SureCart comes with a default profile, why should you need another one?

The answer is that in most cases you don't. But an additional shipping profile would be useful when you want to offer different shipping options for specific products or deliver to specific regions.

Let's say a store sells both lightweight items and heavy furniture. To handle shipping differently for these product types, the store owner can create a custom shipping profile for heavy furniture products.

This allows them to set up separate shipping methods, rates, and zones tailored to the specific needs of these items.

Moreover, if the store owner wants to offer special shipping options to customers in certain regions or countries, they can create a custom shipping profile for those regions.

By having additional shipping profiles, you can precisely define shipping options based on various product types and geographical locations.

### **How to set up a new profile**

In this step-by-step guide, we will walk you through the process of configuring a shipping profile.

1. To begin, from your SureCart dashboard, click on the "Settings" menu.

2. Next, select the "Shipping" menu from the options.

3. To create a new profile, simply click on the "Add New Profile" button.

4. Enter the desired name for your profile, for example, "Heavy Items", and then click on the "Add New" button to save it.

5. Click on the "Add Product" button to add the products that you will be shipping under this profile.

6. In the dropdown menu, you'll find a list of all your products. You can search for a specific product or scroll through the list to find it. Once you locate the product, click on it to select it.

7. Click on the "Create Zone" button to specify where you want to ship this product.

8. Enter the desired name for the zone as you prefer. For example – North America.

9. Choose the countries from the drop-down menu where you want to ship this product, and then click the "Next" button to continue.

10. Choose one of the available shipping methods from the list or create a new one.

11. Enter the price you want to charge for the shipping.

12. Select how you want to charge the shipping fee for these products. In our case, we will select "Based on item weight" but if you can choose the shipping fee based on your needs.

It will open two options where you can set the minimal weight and the maximum weight.

13. Click on the dropdown menu to select the unit of mass you want to work with. In this case, we selected "Kg" from the dropdown menu. But you can choose the unit that you prefer.

14. Set the minimum weight of the product for this shipping to be applied.

15. Now, set the maximum weight of the product for this shipping to be applied, and then click on the "Add" button to save your changes.

Congratulations! You have set up your shipping profile for your heavy items.

Now, when your customers buy the products that come under the heavy item profile, they will see the shipping price for the product.

A shipping profile is a way to organize where and how much you charge for shipping. While a default profile is available, creating additional profiles is beneficial when you want to offer different shipping options for specific products or regions.

But if you still have questions, don't hesitate to reach out to us! We'll be more than happy to assist.

### **Frequently Asked Questions**

**Can I add more than one shipping profile to one product?**

No. A product needs to be only in one profile.


===== SOURCE: how-to-delete-your-store.md =====

---
source_url: https://surecart.com/docs/how-to-delete-your-store
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Settings](https://surecart.com/docs-category/settings/)/How to Delete Your SureCart Store

# How to Delete Your SureCart Store

Want to delete your SureCart store? We understand, and we're here to guide you through the process.

- Navigate to the **General** section under **Settings**.

- Scroll down to the Danger Zone. Here, click on the **Delete Store** option to delete your SureCart store. Confirm your intent, as this step cannot be undone.

- You will get a confirmation message of the store being deleted.

This will delete your SureCart store permanently.

We hope this guide helped you. If you have any questions, please don't hesitate to contact our support team. We're here to help!


===== SOURCE: how-to-hide-the-quantity-option.md =====

---
source_url: https://surecart.com/docs/how-to-hide-the-quantity-option
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/How to hide the quantity option

# How to hide the quantity option

Each component in the cart and checkout has extensive options to make it very easy to customize it.

Simply click on a component and the options will appear on the right.

Learn [how to disable editing quantities](https://surecart.com/docs/disable-editing-quantities/) in your checkout form with our detailed documentation.


===== SOURCE: how-to-import-reviews-in-surecart.md =====

---
source_url: https://surecart.com/docs/how-to-import-reviews-in-surecart
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Migrating](https://surecart.com/docs-category/migrating/)/How to Import Reviews in SureCart

# How to Import Reviews in SureCart

This document explains how to import product reviews into SureCart using a CSV file.

## **Requirements**

- Access to the SureCart App
- WordPress admin access
- SureCart installed and activated
- Products already created in SureCart
- Review data exported from the source platform
- A spreadsheet app or CSV editor

## **Where Reviews Are Imported**

Reviews are imported from the SureCart App.

Navigation path: **SureCart App → Settings → Imports → New Import → Reviews**

## **Import Reviews Into SureCart**

### Step 1: Open the Reviews Import Screen

1. Log in to the SureCart App.
2. Go to **Settings → Imports**.
3. Click **New Import**.
4. Select **Reviews**.

### Step 2: Download the Template CSV File

1. In the **Reviews Import** window, click the **template CSV file** link.
2. Save the template file to your computer.

Do not rename, remove, or change the column headers. The uploaded file must include the header row with column names matching the template.

### **Step 3: Add Review Data to the CSV File**

Add the review data to the template, one row per review.

| Column               | Description                                                     |
| -------------------- | --------------------------------------------------------------- |
| **Customer Email\*** | The email address of the customer who submitted the review.     |
| **Created At**       | The date and time when the review was created.                  |
| **Product Id\***     | The SureCart product ID for the product this review belongs to. |
| **Title\***          | The title or headline of the review.                            |
| **Body**             | The main review content.                                        |
| **Stars\***          | The review rating: 1, 2, 3, 4, or 5.                            |
| **Status**           | The review status, such as `published`.                         |

Fields marked with \* are required.

### **Step 4: Add the Correct Product ID**

Each imported review must be connected to an existing SureCart product. Add the correct product ID in the **Product Id** column for each review.

### **Step 5: Save the File as CSV**

Save or export the file in `.csv` format. Do not upload `.xlsx`, `.numbers`, or other non-CSV formats.

### **Step 6: Upload the Completed CSV File**

1. Return to the **Reviews Import** window in the SureCart App.
2. Upload the completed CSV file.
3. Click **Import**.

### **Step 7: Check the Import Status**

| Status     | Meaning                            |
| ---------- | ---------------------------------- |
| Processing | SureCart is importing the reviews. |
| Completed  | The import has finished.           |
| Failed     | The import could not be completed. |

### **Step 8: Review the Imported Reviews**

After the import is completed, go to **WordPress Dashboard → SureCart → Products → Reviews** to verify the imported reviews.

## **Notes and Limitations**

- Always use the SureCart review import template before importing reviews.
- Products should already exist in SureCart before importing reviews.
- The file must be uploaded in `.csv` format.
- Test the import with a small CSV file before importing a large number of reviews.

## **Related Documentation**

- [How to Enable and Configure Product Reviews](https://surecart.com/docs/product-reviews/)
- [How to Display Product Reviews Using Shortcodes](https://surecart.com/docs/product-reviews-shortcodes/)


===== SOURCE: how-to-make-test-payments.md =====

---
source_url: https://surecart.com/docs/how-to-make-test-payments
source: surecart-kb
scraped: true
---

# How to Make Test Payments

SureCart's test payments feature lets you practice transactions without spending real money, ensuring your payment processes work accurately and reliably.

### Using SureCart's Built-In Test Processor

By default, SureCart's own test processor will be active on your store. When in use, you'll see a test payment option at checkout.

Please note that this test payment option is not intended for real transactions and should not be used in a live environment.

Since it's not a real payment option, you don't need to input any payment information when making a test purchase.

To disable it, head to SureCart **Settings** > **Payment Processors**, and click on any of the available processors. Access the **Test Processor** tab and click the "Disable" button on the top-right.

### Activating Test Mode for Payment Processors

SureCart allows you to activate test mode for multiple payment processors such as Stripe, PayPal, Paystack, and Mollie.

**Important Note**: The **Test Mode Restricted** setting allows you to control who can perform test orders. When enabled, only administrators can finalize test orders that create actual test order entries in your store.

To manage this setting: Go to **SureCart Settings** > **Advanced** tab > **Spam Protection & Security** > locate **Test Mode Restricted**.

Here's how you can enable the test mode:

- Navigate to the **Settings** section under **SureCart**.
- Navigate to the **Payment Processors** section.
- Select your preferred payment processor (e.g., Stripe).
- Access the "Connect" dropdown menu and select **Test Mode**.
- You can **skip this form** in test mode and avoid entering payment information.

### Activating Test Mode In Your Checkout

After activating test mode in your SureCart settings, proceed to enable it in your form:

- Navigate to the **Custom Forms** section under **SureCart**.
- Select the checkout form.
- Select the **Test** option from the dropdown.
- Click on the **Update** button in the top-right corner to apply these changes.

### **Activate Test Mode via Checkout Page Admin Bar**

To enable or disable test mode easily, access the admin bar on the checkout page while logged into your WordPress dashboard.

- Select any product, proceed to its checkout page, then access the dropdown menu and select **Test Mode**.

### **Previewing Test Mode On Your Checkout**

- Navigate to the shop page on your website and buy any product item.
- Proceed to checkout and fill in the test Stripe information. Since the payment is in test mode, you don't need to fill in real payment details.

If you are using the Stripe integration, use Stripe's test cards to test the transaction.

### **Clearing Test Data (Optional)**

- Navigate to SureCart **Settings**, then proceed to **Payment Processors**. Choose the previously used payment processor.
- Select **General** under Settings.
- Scroll down and click on the **Clear Test Data** button.

A new prompt will appear, instructing you to type the **CONFIRM** text message. Your test data will be automatically deleted in a few minutes.

This action is irreversible, so please be sure you are not deleting any real data.


===== SOURCE: how-to-remove-surecart-user-roles.md =====

---
source_url: https://surecart.com/docs/how-to-remove-surecart-user-roles
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Settings](https://surecart.com/docs-category/settings/)/How to Remove SureCart User Roles

# How to Remove SureCart User Roles

SureCart adds four user roles after installation, which are SureCart Customer, SureCart Shop Manager, SureCart Shop Accountant, and SureCart Shop Worker. If you would like to remove any of these user roles, you can simply follow the steps mentioned in this article. Let's get started.

In order to remove the default SureCart roles, you can either use a plugin called [User Role Editor](https://wordpress.org/plugins/user-role-editor/) or a custom code. For more information on how this plugin works, please visit the documentation page of the plugin from [here](http://shinephp.com/user-role-editor-wordpress-plugin/).

To use a custom code on your website, we highly recommend using a child theme. If you are not familiar with the child theme, here is an [article](https://wpastra.com/guides-and-tutorials/wordpress-create-child-theme/) that will guide you through the process.

**Step 1:** Navigate to the WordPress dashboard and click on Appearance > Theme File Editor

**Step 2**: Choose the child theme from the drop-down in the top-right corner and click on the select button to get it selected.

**Step 3**: Once the child theme is selected, click on the function.php file to add the custom code.

**Step 4**: Scroll down to the bottom of the page, copy the below code, and paste it at the bottom of the existing code. If you'd like to remove only one or some of them, you can remove the line that represents the user role you'd like to keep. For example, if you would like to keep the SureCart shop manager role, please remove the line of code that says "remove_role( 'sc_shop_manager');.

```
function wps_remove_role() {
remove_role( 'sc_customer' );
remove_role( 'sc_shop_manager' );
remove_role( 'sc_shop_accountant' );
remove_role( 'sc_shop_worker' );
}
add_action( 'init', 'wps_remove_role' );
```

**Step 5:** Click on the update button at the bottom and this code will remove the SureCart user roles from your website. You can remove the code once the user roles are removed later.

In conclusion, removing SureCart user roles from your WordPress website is a straightforward process that can be done through either a plugin or custom code. By following the steps outlined in this article, you can remove the default SureCart roles, including SureCart Customer, SureCart Shop Manager, SureCart Shop Accountant, and SureCart Shop Worker.

Alternatively, you can also run this code using a custom code plugin such as [Code Snippet](https://wordpress.org/plugins/code-snippets/).

Note: We strongly recommend that you take a backup of your site before editing the code of your website.


===== SOURCE: how-to-use-surecart-3-0-with-avada-builder.md =====

---
source_url: https://surecart.com/docs/how-to-use-surecart-3-0-with-avada-builder
source: surecart-kb
scraped: true
---

# How to Use SureCart 3.0 with Avada Builder

## Overview

SureCart 3.0 requires additional configuration steps to maintain compatibility with the Avada Builder. Ensure you have installed Avada Builder before proceeding.

## Setting Up the Shop Page

1. Navigate to your Pages list and locate your Shop Page, or access it from the SureCart Sidebar
2. In the Page Attributes section on the right side, select "SureCart" as the template
3. Remove the `[sc_product_list]` block from the editor
4. Re-add the element using a Code Block instead
5. To ensure proper product image display, insert this CSS:

[code snippet omitted — see source_url]

6. Save and verify the shop page displays correctly on the frontend

## Configuring Product Detail Pages

1. When editing a product, select "SureCart Layout" as the template layout
2. Save the product
3. Add the following script via WP-Code or another header-footer script injection plugin:

[code snippet omitted — see source_url]

## Fixing Missing Product Thumbnails in Cart

If product thumbnails don't appear in the cart:

1. Go to **Avada > Performance** in your WordPress dashboard
2. Click the **Optimization** tab
3. Increase the **WordPress Big Image Size Threshold** setting (suggest 2500 or higher)
4. Change **Image Lazy Loading** from "Avada" to "WordPress"

These adjustments should restore proper thumbnail display in your cart.


===== SOURCE: ideal-checkout-troubleshooting.md =====

---
source_url: https://surecart.com/docs/ideal-checkout-troubleshooting
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Troubleshooting](https://surecart.com/docs-category/troubleshooting/)/Why iDEAL Might Not Appear in Your Checkout

# Why iDEAL Might Not Appear in Your Checkout

If you don't see iDEAL as a payment option in SureCart, especially when offering subscriptions or recurring payments, don't worry.

This is a common issue and it's related to how Stripe handles certain payment methods.

Here's a simple explanation and how you can fix it.

## **Why iDEAL Doesn't Show for Subscriptions**

When you're offering subscriptions, Stripe only shows payment methods that can handle recurring payments.

Unfortunately, iDEAL doesn't support recurring payments directly. Instead, Stripe uses SEPA Direct Debit to manage these.

So, iDEAL won't show up when your customers check out for subscriptions. Instead, SEPA will be visible, and iDEAL options will only show up after your customers click on SEPA.

## **How to Get iDEAL to Show Up At Checkout For Subscriptions**

If iDEAL isn't showing for purchases, here are some steps to check:

1. When you are enabling Payment Methods on your Stripe Dashboard, make sure that SureCart is the profile you are modifying.

   To do that:
   - Go to **Settings** > **Payments**.
   - Go to **Payment methods** and select SureCart as the default profile here.

2. Double-check that iDEAL is enabled in both test mode and live mode. To do it:
   - Enable the **Test Mode** button, scroll down to iDEAL, and turn it on.
   - When enabling, turn on the **Recurring payments** button and click "Request access".
   - Switch back to the live mode and follow the same steps.

3. Enable SEPA and ensure your Stripe account is approved for SEPA Direct Debit.

## **Why SEPA Appears Instead of iDEAL for Recurring Payments**

For subscriptions, Stripe uses SEPA to handle recurring payments. That's why you see SEPA instead of iDEAL at checkout.

While it may look different, your customers should see the iDEAL options after clicking on SEPA.

If you've tried all the steps above and iDEAL still isn't showing, don't worry. Contact Stripe support or your payment provider for further assistance.

And if you have any questions about SureCart, we're always here to help!


===== SOURCE: import-customers-in-bulk.md =====

---
source_url: https://surecart.com/docs/import-customers-in-bulk
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Migrating](https://surecart.com/docs-category/migrating/)/How to Import Customers in Bulk With SureCart

# How to Import Customers in Bulk With SureCart

In this article, we'll guide you through the process of importing customers in bulk into SureCart. This method involves uploading customer data using a CSV file.

By following these steps, you can import multiple customers at once into your SureCart store.

Let's dive into the process of bulk customer imports with SureCart.

###### Important Note

Migrating an eCommerce platform is a technical process and may require developer expertise, especially when dealing with custom setups or non-standard configurations. The following points apply to all migrations:

- **Effort and expertise required.** Migration involves transferring data accurately while keeping the store operational. Consulting a qualified developer is recommended for store owners who are not familiar with technical processes such as CSV preparation, database migration, or payment processor data transfer.
- **Scope of support.** SureCart support can assist with questions about documentation and product functionality. Hands-on migration work, including data preparation and platform-specific exports, is the responsibility of the store owner or their developer.
- **Realistic expectations.** Migration requires careful planning and execution. Time and complexity vary depending on the size of the store, the source platform, and the data being transferred.

For questions during the migration process, [contact SureCart support](https://surecart.com/support/open-a-ticket/).

### **Preparing Your CSV File**

To import your customers through a CSV file, you need to prepare a CSV file with the information required to create a customer in SureCart.

Here's a template CSV file that you can refer to and create your file with real customer information.

[CSV File Sample](https://app.surecart.com/imports/customers/template.csv)

In the template file, you will find all the fields you need to have in order to import the customer's data.

You have two options to start with your customer data.

**Option one**: You can use your own file that has all the customer information. Just make sure to change the headers in your file to match the headers of our template.

**Option two**: If it's easier for you, just copy the information from your file and paste it into our template. The most important thing is to make sure the first row with the column headers matches correctly.

**Please note**: The field with an asterisk (\*) next to the header is required. In this case, it's the Email field. You must fill in the Email field because without it the importing process won't work properly.

#### **List of all fields**

| **Field**                | **Use**                                                                           |
| ------------------------ | --------------------------------------------------------------------------------- |
| Email                    | The email address of the customer                                                 |
| First Name               | The given or personal name of the customer                                        |
| Last Name                | The family or surname of the customer                                             |
| Name                     | A combination of first and last name, or an additional name used for the customer |
| Phone                    | The contact number of the customer                                                |
| Billing Line 1           | The first line of the billing address                                             |
| Billing Line 2           | The second line of the billing address                                            |
| Billing City             | The city or locality of the billing address                                       |
| Billing State            | The state or province of the billing address                                      |
| Billing Postal Code      | The postal or ZIP code of the billing address                                     |
| Billing Country          | The country of the billing address (two-letter code format, e.g., "US")           |
| Shipping Line 1          | The first line of the shipping address                                            |
| Shipping Line 2          | The second line of the shipping address                                           |
| Shipping City            | The city or locality of the shipping address                                      |
| Shipping State           | The state or province of the shipping address                                     |
| Shipping Postal Code     | The postal or ZIP code of the shipping address                                    |
| Shipping Country         | The country of the shipping address (two-letter code format)                      |
| Stripe Customer Id       | A unique identifier assigned by Stripe to identify the customer                   |
| Stripe Payment Method Id | A unique identifier assigned by Stripe for the customer's payment method          |

**Please note:** You can retrieve the "Stripe Customer Id" and "Stripe Payment Method Id" from your Stripe account. Refer to the article "[How to Get Stripe Customer ID and Payment Method ID](https://surecart.com/docs/exporting-stripe-data/)" if you are importing active subscriptions through Stripe.

### **How to Import Customers?**

Once you have your CSV file ready, you can follow the instructions below to import the customers into SureCart.

1. Login to the SureCart platform and navigate to **Imports**. Click on the **New Import** button.

2. Select **Customers** from the dropdown menu.

3. Download the sample template CSV file that we've created for you. You can fill this out or create your own CSV file.

4. Click on the **Upload** button or simply drag and drop your CSV file into the upload area.

5. Once you've uploaded your file, it will appear in the upload field.

**Note**: Only CSV files are accepted. Avoid uploading .numbers files from Apple devices, as they won't import your customers.

6. Click on the toggle to enable the Live Mode. If the toggle is turned off, the data will be imported in test mode. Then, click on the Import button to begin the importing process.

7. Once submitted, you will notice that the status will be **Pending**.

8. You can click on the status to check if it's ready. The importing process can vary, but for small data (less than 1000 rows), it usually takes less than a minute. You'll also receive an email notification once the process is complete.

9. The status will change to **Completed** once the importing is finished.

10. Click on a row to view more detailed information about it.

There you have it! All the information related to your customers will be displayed on a specific row. This is also a great way to check if your data was successfully imported.

### **Checking The Imported Customers on Your WordPress Site**

Once the customers are imported, you'll be able to see them in your customer list in SureCart. To see these newly created customers, go to the **Customers** section.

Great job! Your customer data has been successfully imported to SureCart.

Please take note that your customers are not yet associated with WordPress users at this stage. But don't worry, we have an article titled "[Manually Sync Your WordPress Users With SureCart](https://surecart.com/docs/sync-users-with-surecart)" that explains this process step by step.

### **Conclusion**

We've detailed the step-by-step process, including accessing the import screen, downloading the template file, uploading the data, and verifying the results.

By following these instructions, you can effectively manage your customer data and complete the transition to SureCart.

If you need help importing additional components to SureCart, check out these articles:

- [How to Import Subscriptions in Bulk With SureCart](https://surecart.com/docs/import-subscriptions-in-bulk/)
- [How to Import Products in Bulk With SureCart](https://surecart.com/docs/import-products-in-bulk/)

If you encounter any issues or have questions during the importing process, don't hesitate to seek assistance from our support team. We are always ready to help and provide further guidance.


===== SOURCE: import-from-woocommerce.md =====

---
source_url: https://surecart.com/docs/import-from-woocommerce
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Migrating](https://surecart.com/docs-category/migrating/)/How to Import Products from WooCommerce into SureCart

# How to Import Products from WooCommerce into SureCart

This document explains how to import existing WooCommerce products into SureCart. Two paths are available: a guided setup for new SureCart users and a manual import for stores that already have SureCart installed.

## **Requirements**

- WordPress admin access
- SureCart version 4.3.0 or higher, installed and activated
- WooCommerce installed and activated on the same WordPress site
- At least one product available in the WooCommerce store

## **Supported Product Types**

The following SureCart product types are supported during import:

- **One time** products
- **Installment** products
- **Subscription** products

Subscription product imports have been tested with the **WooCommerce Subscriptions** extension. Other product types in WooCommerce are skipped during the import.

## **Path 1: Import During SureCart Setup (New Users)**

1. Go to **WordPress Dashboard → Plugins → Installed Plugins**.
2. Locate **SureCart** and click **Get Started**.
3. On the welcome screen, click **Create New Store**.
4. On the **Confirm Store Details** screen, set the **Brand Color** and **Store Currency**, then click **Continue**.
5. On the **Confirm Email for Store Notifications** screen, enter the email address, then click **Continue**.
6. On the **Select A Starting Point** screen, choose **Import Products from Woo**.
7. Complete the remaining setup steps to finalize the store.

**Expected Outcome:** The import runs in the background once setup is complete. After it finishes, the imported products appear under **WordPress Dashboard → SureCart → Products**, and a confirmation notice is shown: _"SureCart: WooCommerce products import complete."_

## **Path 2: Import on an Existing SureCart Store**

1. Ensure **WooCommerce** is installed and activated.
2. Go to **WordPress Dashboard → SureCart → Settings**.
3. Open the **Advanced** tab.
4. Scroll to the **Syncing** section.
5. On the **WooCommerce Products** row, click **Import**.
6. In the dialog, review the number of products detected.
7. Click **Import Products** to start the import.

**Expected Outcome:** A confirmation message appears: _"WooCommerce import started in the background."_ Once finished, the imported products appear under **WordPress Dashboard → SureCart → Products**.

## **Notes and Limitations**

- The import runs in the background and may take a few minutes.
- Only One time, Installment, and Subscription product types are imported. Other WooCommerce product types are skipped.
- Products that have already been imported are automatically skipped on subsequent runs.
- WooCommerce customers and orders are not included in this import. Only products are imported.

## **FAQ**

**Are WooCommerce customers and orders imported along with the products?**

No. Only products are imported.

**Can the import be run more than once?**

Yes. Only new or previously unimported products are added.

**What happens to products that already exist in SureCart?**

Products already imported are detected and skipped. The import does not create duplicates.


===== SOURCE: import-products-in-bulk.md =====

---
source_url: https://surecart.com/docs/import-products-in-bulk
source: surecart-kb
scraped: true
---

# How to Import Products in Bulk With SureCart

## Overview

This guide walks you through importing products in bulk into SureCart using a CSV file. The process involves preparing your data file and uploading it through the SureCart platform.

## Important Notes

Migrating an eCommerce platform is a technical process and may require developer expertise, especially when dealing with custom setups or non-standard configurations.

SureCart support assists with documentation and product functionality questions. Hands-on migration work remains the responsibility of store owners or their developers.

## Preparing Your CSV File

### Download Template

Access the sample CSV file at: `https://app.surecart.com/imports/products/template.csv`

### Required Fields

The following fields are mandatory:

- **Slug** - unique identifier for URLs
- **Name** - product title
- **Currency** - ISO code (USD, EUR, etc.)
- **Amount** - price in minor units (e.g., $9.90 = 990)

### Field Reference Table

| Field               | Type     | Example      | Notes                               |
| ------------------- | -------- | ------------ | ----------------------------------- |
| Slug                | Text     | product-name | Lowercase, hyphens/underscores only |
| Name                | Text     | My Product   | Product title                       |
| Currency            | ISO Text | USD          | Currency code                       |
| Amount              | Integer  | 990          | Minor units (cents)                 |
| Description         | Text     | Brief text   | Supports basic formatting           |
| Status              | Text     | published    | Current product state               |
| Recurring Interval  | Text     | month        | Subscription frequency              |
| Trial Duration Days | Integer  | 14           | Days for trial period               |
| Shipping Enabled    | Boolean  | true/false   | Physical product shipping           |
| Tax Enabled         | Boolean  | true/false   | Apply taxes                         |
| metadata.tag        | Text     | summer-sale  | Custom tags, comma-separated        |

### CSV Preparation Tips

- Match your data column headers to template headers exactly
- Use lowercase letters, numbers, hyphens, and underscores only
- Avoid special characters in slug and metadata fields
- Place all product information in appropriate columns

## Import Process

### Step-by-Step Instructions

1. **Access Imports Menu** - Log into SureCart platform and click Imports
2. **Create New Import** - Click "New Import" button
3. **Select Products** - Choose "Products" from dropdown
4. **Download Template** - Click template CSV file link (optional reference)
5. **Upload File** - Drag and drop CSV or browse to select file
6. **Start Import** - Click Import button
7. **Monitor Status** - Status displays as "Pending" then "Completed"
8. **Verify Results** - Click status or rows to view detailed import information
9. **Access Products** - Find imported items in Products menu dashboard
10. **Enhance Data** - Add images, adjust status, and make final edits

### Processing Time

For small data sets with less than 1000 rows, it usually takes less than a minute. Email notification confirms when import completes.

## Post-Import Tasks

After successful import, enhance your products by:

- Adding product images
- Adjusting product status
- Creating product descriptions (rich formatting)
- Setting up variants and pricing options
- Configuring shipping and tax settings

## Metadata Import Feature

Custom metadata attributes can be imported using column headers with the `metadata.` prefix.

**Example columns:**

- `metadata.tag`
- `metadata.color`
- `metadata.collection`

Multiple tags can be assigned in a single field separated by commas.

## FAQ

**Q: What is the metadata import feature?**
Metadata allows importing custom attributes alongside products via CSV columns using the `metadata.` naming convention.

**Q: How do I add metadata fields?**
Add columns using format: `metadata.FieldName`. Each column becomes a custom attribute on the product.

**Q: Can I include multiple tags?**
Yes. Multiple tags in metadata.tag can be separated by commas within a single cell.


===== SOURCE: import-purchases-in-bulk-surecart.md =====

---
source_url: https://surecart.com/docs/import-purchases-in-bulk-surecart
source: surecart-kb
scraped: true
---

# How to Import Your Purchases in Bulk With SureCart

SureCart allows merchants to import historical purchases in bulk. This tool is particularly useful for migrating data such as licenses or customer purchases from another platform.

However, it's important to note that importing purchases is not the same as importing past orders. Purchases imported through this process are not linked to any specific order ID, and no new orders will be created during the import.

**Important Note**: Migrating an eCommerce platform is a technical process and may require developer expertise. SureCart support can assist with questions about documentation and product functionality. Hands-on migration work is the responsibility of the store owner or their developer.

## **Preparing Your CSV File**

To get started, you'll need to prepare a CSV file with all your purchase information. A template CSV file is available at: https://app.surecart.com/imports/purchases/template.csv

**Required fields** (marked with \*): Customer Email, Price ID, and Quantity.

**Reminder**: When inputting the **Revoke at** date, choose a future date. If the date is earlier than the current time, the import process will fail.

### **List Of Fields In Your CSV File**

| Field            | Use                                                                    |
| ---------------- | ---------------------------------------------------------------------- |
| Customer Email\* | The email address of the customer associated with the purchases.       |
| License Key      | This is the license key usually associated with a digital product.     |
| Price Id\*       | The unique identifier or reference specific to the purchase.           |
| Revoke At        | The date at which the product access will be revoked for the customer. |
| Quantity\*       | Number of purchases made by the customer.                              |
| Variant Id       | Unique identifier of the product variant.                              |

## **Where to Get Your Price ID, Variant ID, & License Key From SureCart?**

You can get both the Price ID and the Variant ID by going to the individual product and clicking on the **Copy Link** button.

To copy a specific variant's ID, select the variant from the dropdown and click on the **Copy** button.

Filling in License Keys is not mandatory. But if you want a license key, you can find them under the **Licenses** section.

**Note**: Please ensure that the enable **license creation** option is activated under the individual digital product.

## **How to Import Purchases?**

Once you have your CSV file ready:

- Navigate to **Settings** > **Imports** and click on the **New Import** button.
- Select **Purchases** from the dropdown.
- Drag and drop the CSV file directly into the upload area or click to browse.
- Enable the switch if you want to import purchases in **Live Mode**. If not, the purchases will be imported in test mode.
- Click on the **Import** button.

The importing process usually takes less than a minute for small data (less than 100). You'll also receive an email notification once the process is complete.

After the import process is done, you'll see the status change to **Completed**.


===== SOURCE: import-subscriptions-in-bulk.md =====

---
source_url: https://surecart.com/docs/import-subscriptions-in-bulk
source: surecart-kb
scraped: true
---

# How to Import Subscriptions in Bulk With SureCart

In this article, we'll guide you through the process of importing multiple subscriptions at once using SureCart. Whether you're transitioning from another platform or looking to manage your subscriptions more efficiently, this guide provides the necessary steps to help you get started.

Before diving in, make sure to review the articles on importing customers and importing products in bulk. These steps are essential for ensuring a proper migration to SureCart.

Importing subscriptions is an essential task, especially if you manage a large number of subscriptions. Instead of manually entering each one, the bulk import feature allows you to handle the process more efficiently, helping to save time and reduce manual work.

If you're switching from another platform to SureCart, importing subscriptions also ensures that your customer data remains intact, and your subscribers continue receiving uninterrupted service.

**Important Note**: Migrating an eCommerce platform is a technical process and may require developer expertise. SureCart support can assist with questions about documentation and product functionality. Hands-on migration work is the responsibility of the store owner or their developer.

### **Preparing Your CSV File**

Importing subscriptions through a CSV file requires careful preparation. Ensure you have a CSV file ready with all the necessary information to create the subscriptions in SureCart.

A template CSV file is available at: https://app.surecart.com/imports/subscriptions/template.csv

**Required fields** (marked with \*): Customer Email, Price ID, and First SC Period Start At.

**Important**: When entering the First SC Period Start At date, it's important to choose a future date. If the date is earlier than the current time, the importing process will fail.

#### **List of all fields**

| Field                    | Use                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------ |
| Customer Email           | The email address of the customer associated with the subscription.                                          |
| Price Id                 | The unique identifier or reference to the specific product being subscribed to.                              |
| First SC Period Start At | The date and time when the first billing period handled by SureCart for the subscription will start.         |
| Ad Hoc Amount            | The amount charged for any ad-hoc (one-time) purchases made within the subscription.                         |
| Coupon Id                | The unique identifier or reference to a coupon applied to the subscription for discounts or promotions.      |
| Promotion Code           | The code associated with a promotion or special offer applied to the subscription.                           |
| Quantity                 | The number of units or items included in the subscription, particularly relevant for quantity-based pricing. |
| Tax Enabled              | Indicates whether taxes are applied to the subscription.                                                     |
| Trial End At             | The date and time when any trial period for the subscription will end.                                       |

### **Where To Get The Price ID?**

1. Click on the **Products** option from your WordPress dashboard.
2. Click on the product you want. This will take you to the product's details page.
3. Click on the **Copy Links** button to find all the prices associated with that product.
4. You'll find the Price ID at the bottom of the pop-up.

### **How to Import Subscriptions?**

Once you have your CSV file ready:

1. Click on the **Imports** menu in the SureCart platform.
2. Click on the **New Import** button.
3. Choose **Subscriptions** from the dropdown menu.
4. Click on **this Template CSV file** button to get a sample CSV file.
5. Drag and drop the CSV file into the upload area, or click to browse and choose the file.
6. If you want to import the subscription in Live Mode, enable the switch. Otherwise, subscriptions will be imported in test mode.
7. Click on the **Import** button.

The importing process usually takes less than a minute for small data (less than 100). You'll also receive an email notification once the process is complete.

After the import process is done, you'll see the status change to **Completed**.

**IMPORTANT**: Even though your subscription is active, your customers may not have any payment information associated with their account. If you've added the Stripe Customer ID and Payment Method ID, be aware that your customer could be **double-charged** if you don't deactivate the billing on the platform you are migrating from.

Customers need to add a valid credit card to their account to ensure their subscriptions work smoothly.


===== SOURCE: individual-collections.md =====

---
source_url: https://surecart.com/docs/individual-collections
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Bricks Builder](https://surecart.com/docs-category/bricks-builder/)/How to Customize Layouts for Individual Collections

# How to Customize Layouts for Individual Collections

How to Customize Layouts for Individual Collections

In this guide, we'll show you how to create a custom layout for each collection with just a few simple steps.

By using template conditions, you can assign unique layouts to individual collection pages, giving each collection its own distinct design.

Let's get started!

### **Creating a Custom Layout for Each Collection**

If you already have a collection template, follow the steps below. If not, make sure to create one first. We have detailed documentation on how to create a collection template here.

- Open the Collection Template.
- Click on the **Settings** icon (1) in the top navigation bar.

- In the settings panel, navigate to **Template Settings**.

- Click on **Conditions**.

- Click the **ADD CONDITION** button to define when this template should be applied.

- In the new condition, click to open the dropdown menu (1).
- Select the **Terms** option from the list (2).

- Click the **Select Terms** dropdown (1).
- Now you just need to choose the specific collection(s) to which you want to apply this layout (2).

That's it!

You've successfully created a custom layout for the selected collection(s). Each collection can now have its own unique design, giving you greater flexibility and control over your site's appearance.


===== SOURCE: initial-troubleshooting.md =====

---
source_url: https://surecart.com/docs/initial-troubleshooting
source: surecart-kb
scraped: true
---

# SureCart Troubleshooting Guide: Resolve Common Issues Quickly and Easily

While we're always ready to help you with anything that you need help with by opening a ticket, before reaching out for support, try these quick troubleshooting steps to resolve common SureCart issues.

These simple steps can solve up to 80% of common problems, saving you time and getting you back to using SureCart smoothly.

These steps can help with issues related to:

- **Display and layout:** How SureCart appears on your WordPress site.
- **Browser errors:** Issues specific to your web browser.
- **Functionality:** Any problem with how SureCart functions on your site.

## Initial Troubleshooting Steps:

1. **Check Troubleshooting Guides:** We have identified the most common issues our customers face. You can see them on the **Troubleshooting** category.
2. **Update SureCart:** Ensure you're using the latest version for optimal performance.
3. **Clear Cache:** Clear your browser cache, cookies, and WordPress site cache to eliminate temporary data causing conflicts.
4. **Clear SureCart Account Cache:** You can try to clear your SureCart account cache by going to SureCart > Settings and clicking on the "Clear Account Cache" in the top-right corner.
5. **Try a different browser/device:** Rule out browser-specific issues.
6. **Disable caching on SureCart pages (if applicable):** If you use caching plugins, exclude SureCart pages and sections to prevent conflicts.
7. **Check for plugin conflicts:** Temporarily disable other plugins one by one to identify potential conflicts with SureCart. Do the same with your theme if necessary.
8. **Verify required pages:** Ensure essential pages like Shop, Checkout, Customer Dashboard, and Cart are not deleted or trashed. Restore them if needed.
9. **Recreate products/forms (if issue is specific):** If only one product or form has issues, try recreating it instead of duplicating.
10. **Customize CSS (optional):** Refer to SureCart's guide for proper CSS customization using ShadowDOM.
11. **Address translation issues:** Use the LocoTranslate plugin and follow SureCart's translation guide.
12. **Review settings:** Check related settings in SureCart and other plugins for potential conflicts.

**Remember**: Try steps one at a time, checking if the issue persists after each step to isolate the problem. Make minimal changes to your site to avoid causing further issues.

## Payment Issues and External Connections:

### **Refresh or Reconnect Payment Processors:**

- Go to your **SureCart App Dashboard** > **Settings** > **Payments**.
- Choose to **refresh** or **disconnect and reconnect** your payment processors if you're experiencing checkout issues.

### **Try Different Payment Processors:**

- Connect a different payment processor to see if the problem persists. This helps determine if the issue is specific to a processor or SureCart.

### **Verify Payment Processor Account:**

- Double-check that you've connected the **correct account** within your payment processor platform. Some platforms allow switching accounts, so ensure you're using the intended one.

### **Verify Connected SureCart Shop:**

- Ensure you've connected the **correct SureCart Shop** from the dashboard to your WordPress site.
- If you suspect an incorrect connection, simply **reconnect the Secret Token** on your WordPress site.

## Troubleshooting Advanced Issues

For issues related to webhooks, API, and other advanced functionalities:

**Resync Webhooks (for webhook failures):**

- Go to your **WordPress site** > **SureCart** > **Settings** > **Connection** > **Advanced Options**.
- Click on "**Resync Webhooks**".
- Return to your **SureCart Dashboard** and **retry the webhooks** to see if the issue persists.


===== SOURCE: installing-surecart.md =====

---
source_url: https://surecart.com/docs/installing-surecart
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Getting Started](https://surecart.com/docs-category/getting-started/)/How to Install SureCart Plugin

# How to Install SureCart Plugin

In this tutorial, you will learn how to install the SureCart plugin and connect it to the SureCart platform.

So if you do not know this, [SureCart Platform](https://app.surecart.com/) is like a storage unit that stores all data, customer orders, products, and store configurations instead of your WordPress site.

And that helps us keep your WordPress site from slowing down while you use SureCart.

That's why you need to connect the SureCart plugin on your WordPress site to the SureCart Platform.

### Install the SureCart Plugin from the WordPress Repository

To connect SureCart with your WordPress site, you have to install and activate SureCart plugin on your site.

So you can search for SureCart on the WordPress repository and install & activate it on your site as you would normally install and activate any WordPress plugin.

Next, let's connect the SureCart plugin to your new store from your WordPress account!


===== SOURCE: instant-checkout-pages.md =====

---
source_url: https://surecart.com/docs/instant-checkout-pages
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Instant Checkout](https://surecart.com/docs-category/instant-checkout/)/How to Set Up Instant Checkout Pages

# How to Set Up Instant Checkout Pages

SureCart's Instant Checkout feature lets you create a unique checkout link for a specific product.

You get a special link that you can share on social media, email, or your website. This link lets customers skip the usual website navigation and go straight to checkout.

This makes buying stuff quicker and easier, and it usually leads to more sales. If you're wondering how to do it, just follow these steps:

1. Go to SureCart from your website and click on **Products**.

2. Select any product.

3. On the right side of the product, you will find the **Instant Checkout** button; click on it.

4. By clicking on it, a new dropdown will open up. Toggle on **Published** to make the Instant checkout page accessible to your users/customers.

5. The next option is **Test Mode**. Click on it if you want to make a test purchase using the instant checkout page. Later, you can turn it off.

6. Below the Test Mode, you can toggle on or off additional product information such as the product image, product description, coupon field, and terms and conditions.

7. **Save Product** to apply changes before you can copy the link.

8. Copy the link URL so you can share it with your customers and users, or view it in a new window by clicking the **View** button.

So, setting up an Instant Checkout Page in SureCart is simple, right?

It's all about clicking the right buttons and toggling your desired options. You can quickly create a unique checkout link for any product, simplifying your customers' buying process.

Hope this helps. If you have any more questions, please feel free to reach out to our support team. We are happy to answer any questions you may have!


