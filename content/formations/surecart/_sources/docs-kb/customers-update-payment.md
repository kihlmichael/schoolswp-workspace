---
source_url: https://surecart.com/docs/customers-update-payment
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Customer Dashboard](https://surecart.com/docs-category/customer-dashboard/)/How Can Customers Update Their Payment Methods?

# How Can Customers Update Their Payment Methods?

This document explains how to add, update, and set a default payment method from the SureCart Customer Dashboard. The steps below are written from the customer's perspective and can be shared directly with customers who need to manage their payment methods.

For a general overview of the Customer Dashboard and its sections, refer to [Customer Dashboard Overview](https://surecart.com/docs/overview-customer-dashboard/).

## **Requirements**

- An existing customer account on the store
- Access to the email address associated with the customer account
- A payment method to add (such as a credit or debit card)

## **Accessing the Customer Dashboard**

The Customer Dashboard is available at the store domain followed by the customer-dashboard slug. For example, if the store domain is example.com, the dashboard is located at example.com/customer-dashboard.

- Open the Customer Dashboard URL in a web browser.
- Enter the email address used during checkout, then click **Next**.
- Enter the password, then click **Login**.

For more detail on signing in, refer to [How Customers Access the Dashboard](https://surecart.com/docs/customers-access-dashboard/).

## **Adding a Payment Method**

- After signing in, click the avatar in the bottom-left corner, next to the account name.
- Select **Billing** from the menu.
- Click **Add** in the top-right corner of the Billing section.
- Enter the card information in the form.
- Click **Save Payment Method**.

**Expected outcome:** The new payment method is added to the account and appears in the list of saved payment methods in the Billing section.

## **Setting a Default Payment Method**

The default payment method is used for future payments and subscription renewals.

- In the Billing section, click the three-dot menu next to the payment method to set as default.
- Select **Make Default**. A confirmation popup appears.
- To apply this payment method to all active subscriptions, toggle on **Update All Subscriptions**.
- Click **Make Default** to confirm.

**Expected outcome:** The selected payment method becomes the default for future payments. When **Update All Subscriptions** is enabled, all active subscriptions are also switched to the new default payment method.

## **Notes and Limitations**

- Payment method data is processed and stored securely by the connected payment processor (such as Stripe). SureCart and the store owner do not store full card numbers.
- Setting a payment method as default without enabling **Update All Subscriptions** applies the default only to future one-time payments and to new subscriptions. Existing subscriptions continue to use their previously assigned payment method.
- The available payment method types depend on the payment processors connected to the store. If a processor only supports cards, only cards can be added.
- Removing a payment method that is currently assigned to an active subscription may cause the next renewal to fail. Assigning a different payment method to the subscription before removing the old one is recommended.

## **Related Documentation**

- [Customer Dashboard Overview](https://surecart.com/docs/overview-customer-dashboard/)
- [How Customers Access the Dashboard](https://surecart.com/docs/customers-access-dashboard/)
- [How Customers Update Account Details](https://surecart.com/docs/customers-update-account/)
- [How Customers Change Their Password](https://surecart.com/docs/customers-change-password/)
- [Managing Subscriptions in the Customer Dashboard](https://surecart.com/docs/subcription-in-customer-dashboard/)

## **FAQ**

**Does adding a new payment method automatically update active subscriptions?**

No. Adding a payment method only saves it to the account. To use it for active subscriptions, it must be set as the default with the **Update All Subscriptions** option enabled, or assigned individually to each subscription.

**What happens to existing subscriptions when a new default is set without enabling Update All Subscriptions?**

Existing subscriptions keep their currently assigned payment method. The new default applies only to future one-time payments and to subscriptions created afterward.

**Can more than one payment method be saved at the same time?**

Yes. Multiple payment methods can be saved in the Billing section. One of them is marked as the default, and the others remain available to be assigned to specific subscriptions or set as the default later.

**How is a payment method removed?**

In the Billing section, click the three-dot menu next to the payment method and select the remove option. If the payment method is assigned to an active subscription, assigning a different payment method to that subscription first is recommended to avoid a failed renewal.

**What types of payment methods can be added?**

The available types depend on the payment processors connected to the store. Card payments are supported when a card-capable processor (such as Stripe) is connected. Other methods may be available depending on the processor configuration.

**What happens if a saved card expires or is declined?**

If the default card expires or a payment is declined, the associated payment may fail. Adding a new valid payment method and setting it as the default resolves this. For subscriptions, the renewal can be retried after a valid payment method is in place.
