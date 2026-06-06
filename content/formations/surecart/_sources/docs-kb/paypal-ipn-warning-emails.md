---
source_url: https://surecart.com/docs/paypal-ipn-warning-emails
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Troubleshooting](https://surecart.com/docs-category/troubleshooting/)/PayPal IPN Warning Emails

# PayPal IPN Warning Emails

This document explains PayPal Instant Payment Notification (IPN) warning emails that some SureCart users may receive.

## Introduction

Some users may receive warning emails from PayPal regarding Instant Payment Notification (IPN) failures at `https://app.surecart.com/`. These emails can be safely ignored and do not indicate a problem with SureCart transactions or account security.

## Understanding the Issue

SureCart does not use PayPal's IPN system. These warning emails are sent in error by PayPal and do not reflect an actual issue with SureCart or the connected PayPal account.

## What to Do

No action is required. These emails can be safely ignored.

PayPal may send multiple warning emails over time. This does not indicate a problem and will not affect payment processing or transaction functionality.

## Notes

- SureCart does not rely on PayPal's IPN system for transaction notifications.
- PayPal may continue to send these warning emails intermittently. This is expected behavior due to the error on PayPal's side.
- No configuration changes are needed in SureCart or PayPal to resolve this issue.

## FAQ

**Will ignoring these emails affect my payments or transactions?**

No. SureCart does not use IPNs, so these warning emails have no impact on payment processing or transaction functionality.

**Why is PayPal sending these emails if SureCart doesn't use IPNs?**

This is an error on PayPal's side. PayPal is incorrectly attempting to send IPNs to SureCart and generating warning emails when the notifications are not received.

**Should I disable IPN settings in my PayPal account?**

No action is needed. IPN settings do not need to be modified.
