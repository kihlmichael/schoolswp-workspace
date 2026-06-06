---
source_url: https://surecart.com/docs/setup-custom-email
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Email](https://surecart.com/docs-category/email/)/How to Set Up a Custom Email Address For Your Store?

# How to Set Up a Custom Email Address For Your Store?

By default, all email notifications sent to buyers have the email address set to **notifications@surecart.com**.

But there may be cases where you want everything white-labeled, meaning you want to edit the email sender to be an email address of your choice.

We have added this option to all premium plans and you can easily set this email address when you log into the SureCart platform and go into the Email settings.

Visit [app.surecart.com](http://app.surecart.com/) and log in to your account.

- Click on **Settings** and select **Email**.

- Click on the **Setup Custom Email Address** button.

- Enter the email address that you want here and click on the **Next Step:Verification** button.

To complete this process, you need to perform the following verification steps:

- **Verify your email address**: By now, you should have received an email on the entered email address. Please check your inbox and verify it.

If you did not receive any email, please click on the **Resend Verification Email** button.

- **Configure DKIM DNS**: Adding DKIM DNS is important because it verifies that emails come from genuine senders and haven't been tampered with, reducing the risk of fraud and spam.

To do this, you would typically need to access the DNS settings for your domain through your domain registrar's website or control panel.

Look for the option to manage DNS records or edit DNS settings. Then, paste the following TXT record with the provided Hostname and TXT Value.

Click on both the **Check DNS Records** buttons after adding these values to your domain.

**Note:** Checking DKIM is only necessary if you're using a new domain which wasn't connected to SureCart previously.

That's it! Once all verifications are complete, your new email address will be used for sending notifications to customers.

You can also remove this email address anytime by clicking on the **Remove Email Address** button at the top.

We hope this helped you. If you have any questions or face any issues with configuring DKIM DNS settings, reach out to our support team for assistance. We're here to help!
