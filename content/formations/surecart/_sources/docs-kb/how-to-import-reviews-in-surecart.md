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
