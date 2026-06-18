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
