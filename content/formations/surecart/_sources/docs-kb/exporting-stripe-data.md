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
