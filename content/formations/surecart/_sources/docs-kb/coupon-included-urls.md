---
source_url: https://surecart.com/docs/coupon-included-urls
source: surecart-kb
scraped: true
---

# How to Include Coupons to Product URLs and Share With Users

Want to send customers product page links with coupons already applied? SureCart offers a straightforward solution to this.

You can simply do this by adding coupon codes at the end of the product page URLs.

Incorporating coupons directly into product URLs can offer significant advantages.

**For businesses:** it can increase sales conversions, make tracking of marketing campaigns simpler, enhance customer satisfaction, and provide seamless promotional opportunities. It allows for direct and personalized promotions, improving the page's visibility on search engines.

**For customers:** it offers convenience, immediate savings, and a smoother, more transparent shopping experience.

### How to Share a Product with Prefilled Parameters

Sharing a product link with an already-filled coupon code can make the purchasing journey smoother and more user-friendly. Here's a step-by-step guide to accomplish this:

- Navigate to your WordPress dashboard and select Products under SureCart.
- Identify and select the product you wish to share.
- Under the Pricing section, click on the 'Copy Links' button.
- Find the "Buy Link" field and click the 'Copy' button to obtain the URL.
- Paste the copied URL into your browser.

Example URL:

```
https://example.com/checkout/?line_items%5B0%5D%5Bprice_id%5D=1a830bba-ede0-4640-88ff-c1d5a94fe993&line_items%5B0%5D%5Bquantity%5D=1
```

### How to Insert Coupon Into the Product URL

- From SureCart, navigate to Coupons, select coupons, and copy the coupon code.

To embed the coupon code into the URL, append the parameter "**&coupon=YOUR_COUPON_CODE**" to the end of the product page's URL. For instance, if your coupon code is "**20-OFF-SECRET**", the appended portion would be "**&coupon=20-OFF-SECRET**".

Final URL:

```
https://example.com/checkout/?line_items%5B0%5D%5Bprice_id%5D=1a830bba-ede0-4640-88ff-c1d5a94fe993&line_items%5B0%5D%5Bquantity%5D=1&coupon=20-OFF-SECRET
```

Once the customer clicks on the shared link, they will be redirected to a checkout page with the coupon code pre-applied, making the purchasing process seamless and efficient.
