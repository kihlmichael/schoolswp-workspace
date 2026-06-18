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
