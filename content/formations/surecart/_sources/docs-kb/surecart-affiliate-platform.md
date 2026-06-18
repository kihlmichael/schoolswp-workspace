---
source_url: https://surecart.com/docs/surecart-affiliate-platform
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Affiliate Platform (for merchants)](https://surecart.com/docs-category/affiliates-for-merchants/)/SureCart Affiliate Platform

# SureCart Affiliate Platform

In this article, we will guide you through the Affiliate Platform. This platform empowers users to join as affiliates, promoting your products and earning rewards for each successful sale.

We'll walk you through each feature, step by step, revealing simple yet impactful ways to maximize your affiliate experience and boost your earnings.

## **What is an Affiliate Platform?**

An affiliate platform is like a meeting place. It connects sellers who want to sell more with people who want to help sell their stuff.

These helpers, called affiliates, earn rewards when they bring in customers or make sales. The platform gives affiliates special links to track their work, making sure they get paid for what they do.

It helps sellers reach more people without spending lots of money upfront. They team up with affiliates who use different online ways to show the seller's stuff to more folks.

Overall, it's a win-win: sellers sell more, and affiliates earn rewards for helping them out.

## **Merchant Settings**

Before anything else, you need to configure your affiliate settings where you will define the Affiliate Signups, Referral Tracking, and Commissions and payouts.

Let's get started.

- To begin, log in to your WordPress dashboard using your credentials.
- Then, navigate to **SureCart** > **Settings**, and **Affiliates**.

### **Affiliate Signups**

This is where you set up how affiliates sign up and get approved to promote products in your store.

- To enable new affiliate signups, toggle the **Allow New Affiliate** Signups switch.

- Complete the Program Description field. This is where you usually specify how the affiliate program works or how much commission you will provide to your affiliates.

- If you wish to automatically approve new affiliates, simply enable the **Auto Approve New Affiliates** toggle.

- Click on the **Save** button in the top right corner of your screen to save your changes.

The Signup URL is where your affiliates will sign up for the affiliate program. To **modify** it, follow the steps below.

- Login at [app.surecart.com](http://app.surecart.com/) and select your store. Then, go to the "Store".
- Change the **Store ID / Subdomain**, ensuring it contains only letters, numbers, and dashes. Click the **Save** button to apply these changes.

- Return to the Affiliates menu, and you'll notice that your Signup URL has been changed.

- The **Signup Question** field asks the affiliates questions during the signup process. If you leave it blank, the default question "How will you promote this store?" will be used.

- You can enter the URL to your Terms & Conditions page here. This page will be shown to affiliates after signing up.

- The payout email is where affiliates get their commission payments. If enabled, this will include a separate payout email field on the signup form itself.

### **Referral Tracking**

This is where you'll set up how clicks are tracked and how affiliates get credit for referrals.

Before we start, let's clarify some terms.

**Referrer Type**: This determines which affiliate should get credit for a sale if a customer has clicked multiple affiliate links. The first referrer means the first affiliate link to be clicked will get credit, and the last referrer means the last affiliate link to be clicked will get credit.

**Tracking Length**: Also known as the "cookie duration", this is how long a special code (called a cookie) stays on someone's device after they click an affiliate link. It's like a small marker that remembers they came from an affiliate's link.

This time matters because if someone clicks an affiliate link and buys something within that time, the affiliate still gets recognized for the sale.

For instance, if the tracking length is 30 days, it means that if someone clicks an affiliate link and buys something from that store within the next 30 days, the affiliate will receive a commission for that sale.

**Tracking Script**: The tracking script is a small snippet of code that helps an affiliate platform keep track of who sends customers to a store's website. The tracking script must be present on all sites where affiliate links should be tracked.

If a store uses SureCart V.2.10.0 or later, they don't need to worry about setting up this tracking code. It's handled automatically by the system through a single toggle that can enable or disable it.

Now that you understand how it works, let's set them up:

- Enable "Tracking" to add a tracking script to this site.

- In the Referrer type, choose **which** referrer should receive credit. If you prefer the default option, which is Last, there's no need to make changes. However, if you want the referrer who initiated the first interaction to get credit, click on the dropdown menu and select First.

- Set the Tracking Length in days for when you want to credit the referrer.

- In the **Affiliate Referral URL** field, enter the address where you want your affiliates to direct traffic.

- Decide whether you want to approve new referrals automatically or not.

### **Commissions & Payouts**

This is where you set up how affiliates earn commissions and receive their payments.

**Commission**: A commission is like a "thank you" reward. When someone helps to sell things for a store by bringing in customers or making sales happen, the store gives them a part of the money earned as a way of saying thank you.

**Subscription Commissions**: A subscription commission is like a repeating thank-you bonus for affiliates. If they bring in customers who sign up for services that people pay for regularly (like every month), the affiliate keeps getting a bonus each time those customers pay.

**Lifetime Commissions**: Lifetime commissions mean an affiliate keeps getting bonuses for all the shopping a customer does in the future, not just the first time they buy something.

Now that you understand the basics of how it functions, let's configure the settings.

- Enter the commission amount you wish to pay your affiliates, and then select whether it's a percentage or a flat rate.

- To reward affiliates for renewal subscriptions, switch on the **Subscription Commissions** toggle.

- If you wish to limit the time that subscription commissions are awarded, you can set this in the designated field for the number of days. For example, setting the field to 365 would mean that affiliates are only awarded commissions for 1 year after the subscription starts.
- If you don't wish to limit the time a subscription commission is awarded, you can leave the field blank.

- To reward affiliates for future purchases, switch on the **Lifetime Commissions** toggle.

- If you prefer to award commissions to the affiliate for a specific period after a customer's purchase, you can set this duration in the number of days.
- If you wish to provide commissions indefinitely, you can leave the field blank.

- Finally, write a Payout Instruction so that your affiliates understand your terms and conditions for receiving their payments.

That's it! Hope this article was helpful. If you need more information, please feel free to reach out to us.

### **Frequently Asked Questions**

**The user is approved on the Requests tabs but is not becoming an affiliate, why?**

To transition from the Requests tab to the Affiliate tab, a user needs to complete the affiliate setup process.

Upon approval, whether automatically or manually, the affiliate receives an email prompting them to finalize their affiliate setup by registering. Once this step is completed, they officially become an affiliate.

**The user is also a SureCart store owner. Can they become an affiliate of another store?**

Absolutely! Any store owner has an affiliate platform and can also become an affiliate of any SureCart affiliate store.

For a seamless experience, this store owner needs to use the same email address they used for their store.

**Why my test purchases are not being tracked**?

Currently, the affiliate platform is only tracking live purchases.

We are considering making this feature available in the test mode in the future!

**How to make a payout**?

Right now, the platform lists payouts for merchants to handle manually. Soon, will be able to make things easier by creating CSV files. We're also planning to automate this process to make it smoother.
