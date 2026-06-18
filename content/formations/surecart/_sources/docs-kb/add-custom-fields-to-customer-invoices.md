---
source_url: https://surecart.com/docs/add-custom-fields-to-customer-invoices
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Uncategorized](https://surecart.com/docs-category/uncategorized/)/How to Add Custom Fields to Customer Invoices

# How to Add Custom Fields to Customer Invoices

This guide will help you add custom fields, such as a company registration number or tax number, to your customer invoices in SureCart. Follow these steps to capture the data at checkout and display it on future invoices.

### **How Can You Add Custom Fields at Checkout?**

To add custom fields, follow these steps:

1. **Edit the Checkout Form**:

- Go to your checkout form in SureCart and add a Conditional block.
- Insert a TextField or other suitable fields for the additional information you need to capture from customers.
- These will be displayed during checkout for customers to fill in.

**2. Store Data as Metadata:**

- The custom fields will be stored as metadata on the checkout object. For example, with keys like `invoice_column_1` and `invoice_column_2`.

### **How Can You Display Custom Fields on Invoices?**

1. **Access the Invoice Template**:
   - Navigate to the invoice template editor at [SureCart Invoice Template](https://app.surecart.com/order_statement_template/edit).

2. **Use Metadata in the Template**:
   - To display the metadata, include the following pattern where you'd like the custom fields to appear, using `checkout.metadata.your_key_name` syntax.

   - This will display the values entered by the customer at checkout on their invoice.

**Important Notes:**

- **Placeholder Keys**: The provided keys are placeholders used for demonstration purposes. You must replace these with the actual keys corresponding to the custom fields you've configured in your setup.
- **Custom Field Setup**: Ensure that the custom fields you want to display are properly set up and added to the invoice metadata.
- **Validation**: Test the output on your invoices to confirm that the correct data appears in the desired format.

### **What About Existing Subscriptions?**

For customers who already have active subscriptions and did not fill in these custom fields, here are your options:

- **Manual Update**: You can manually update the customer information using SureCart's API. Head to [SureCart API Reference](https://developer.surecart.com/reference/update_checkout) to update the metadata for existing customers.
- **Customer Dashboard**: You could also allow customers to update their information directly through their dashboard. This feature may require custom development, as there's no UI for metadata updates at this time.

### **How Can You Manually Add Data via API?**

If you need to update customer metadata manually, follow these steps:

1. **Get Authorization**: Include your secret token in the Authorization field.
2. **Provide Checkout ID**: Add the appropriate checkout ID for the customer.
3. **Add Metadata**: In the request body, include the metadata fields that need updating.
4. **Submit**: Hit "Try it" in the API console to save your changes.

For more details, check the SureCart API documentation [here](https://developer.surecart.com/reference/update_checkout).

We hope this guide helps you add custom fields to your invoices and manage customer data seamlessly. If you run into any issues, feel free to leave a comment below, and we'll be happy to assist you further!
