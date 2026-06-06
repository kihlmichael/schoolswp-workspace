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
