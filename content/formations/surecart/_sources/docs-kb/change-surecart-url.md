---
source_url: https://surecart.com/docs/change-surecart-url
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Migrating](https://surecart.com/docs-category/migrating/)/How to Change the Store URL in SureCart

# How to Change the Store URL in SureCart

This document explains how to update the store URL when the domain or address of an existing SureCart store changes (for example, from store.example.com to shop.example.com). The procedure updates how the store URL is displayed in customer-facing locations such as invoices, receipts, and email notifications.

## **Requirements**

- WordPress admin access
- SureCart installed, activated, and connected
- The new domain configured at the hosting and DNS level, pointing to the WordPress installation

## **Updating the Store URL**

The fields that reference the store URL are located on the **Store Settings** page. The page contains three sections, each with its own **Save** button. The store URL appears in two of these sections, and both must be updated.

### **Step 1: Update the Store Details Section**

1. Go to **WordPress Dashboard → SureCart → Settings → Store Settings**.
2. Locate the **Store URL** field. Replace the existing URL with the new domain.
3. Locate the **Terms Page** field. Update the URL to use the new domain.
4. Locate the **Privacy Policy Page** field. Update the URL to use the new domain.
5. Click **Save** at the bottom of the Store Details section.

### **Step 2: Update the Contact Information Section**

6. On the same **Store Settings** page, scroll down to the **Contact Information** section.
7. Locate the **Website** field.
8. Update the URL to match the new domain.
9. Click **Save** at the bottom of the Contact Information section.

**Expected outcome:** After saving both sections, all new invoices, receipts, and email notifications display the updated URL.

## **Notes and Limitations**

- The **Store Settings** page contains three sections (Store Details, Notification Settings, Contact Information), and each is saved independently.
- Existing invoices and emails already sent to customers are not updated retroactively.
- The WordPress Site Address must already point to the new domain before updating the SureCart settings.

## **Related Documentation**

- [How to Update Store Details](https://surecart.com/docs/update-store-details/)
- [Migrating to Another WordPress Install](https://surecart.com/docs/migrate-to-another-wordpress-install/)
- [How to Transfer Store Ownership](https://surecart.com/docs/transfer-store-ownership/)
