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
