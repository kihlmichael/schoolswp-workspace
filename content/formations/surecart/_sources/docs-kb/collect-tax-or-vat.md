---
source_url: https://surecart.com/docs/collect-tax-or-vat
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Tax](https://surecart.com/docs-category/tax/)/How to Collect Tax ID/VAT Numbers from Your Customers

# How to Collect Tax ID/VAT Numbers from Your Customers

To collect your customers' tax ID/VAT number, navigate to **SureCart > Forms** and select the form you wish to edit.

Then, add a "VAT or Tax ID Input" field to your form. You can control where you want this form field to appear.

### Changing VAT behavior

To change VAT behavior navigate to **SureCart > Settings > Tax**. Be sure that "Tax Collection" is turned on. Please enable any necessary settings:

**Require VAT Number**: This will require the VAT field to be required on all forms. It will also automatically add a VAT field to your form if you have not already added one.

**Local Reverse Charge**: By default, reverse charges will not apply when customers are in your home country. However, enabling this setting enables you to apply a reverse charge when a customer is in your home country.

**VAT Number Verification Failure**: By default, SureCart will validate an EU VAT number EU VAT Number Validation API, which takes data from VIES. If it matches, a VAT exemption is done automatically.

If it fails to validate, the user sees an error. Sometimes a user can have a valid VAT number in their home country, but not registered through VIES. This will also make validation fail. You can change this behavior:

- Reject the order and show an error
- Accept the order but don't apply reverse charge (don't remove VAT)
- Accept the order and remove VAT as normal (remove VAT)

### Invoices

If a customer properly configures their tax ID/VAT number during checkout, it automatically appears on the invoice.

We hope this guide helped you. If you have any questions, please don't hesitate to contact our support team. We're here to help!
