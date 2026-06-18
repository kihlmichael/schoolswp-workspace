---
source_url: https://surecart.com/docs/password-field-checkout
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/How to Set Up a Password Field During the Checkout Process

# How to Set Up a Password Field During the Checkout Process

This document explains how to add a password field to a SureCart checkout form, allowing customers to create their customer dashboard password during checkout.

### **Requirements**

- WordPress admin access
- SureCart installed and activated
- An existing checkout form

### **Customer Dashboard Access Overview**

SureCart provides customers with a dashboard where they can access order history, subscriptions, and account details.

Customers can access this dashboard in two ways:

- **Email link** – Customers receive a login link by email after completing a purchase and can set a password from the dashboard.
- **Checkout password field** – Customers create their password directly during checkout using a password field.

This guide focuses on configuring the password field during checkout.

### **Add a Password Field to the Checkout Form**

Follow the steps below to add a password field to a checkout form.

- Go to **WordPress Dashboard → SureCart → Checkout**.
- Open the **Store Checkout** form.
- Click the **+** button to add a new block.
- Navigate to the **SureCart** block section.
- Drag and drop the **Password** block into the checkout form where customers should enter their password.

### **Configure Password Field Settings**

After adding the password block, configure its settings as needed.

- Select the **Password** block.
- Enable **Required** to require customers to create a password during checkout.
- Enable **Password Confirmation** to require customers to confirm their password.
- Click **Update** to save the changes.

### **Expected Outcome**

After completing these steps, customers will be prompted to create a password during checkout. They can then use their email address and password to log in directly to their customer dashboard.

### **Notes and Limitations**

- The password field applies only to checkout forms where it is added.
- Customers who do not create a password during checkout can still access the dashboard using the email login link.
- Existing customers are not affected by adding the password field.

### **FAQ**

**Is the password field required for all customers?**

No. The password field is optional unless the **Required** option is enabled in the block settings.

**Can customers still log in without setting a password during checkout?**

Yes. Customers can use the email-based login link to access their dashboard if no password is created during checkout.

**Does adding a password field affect existing orders?**

No. This setting applies only to new checkouts.
