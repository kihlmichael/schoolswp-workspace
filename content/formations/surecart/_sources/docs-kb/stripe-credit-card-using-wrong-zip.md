---
source_url: https://surecart.com/docs/stripe-credit-card-using-wrong-zip
source: surecart-kb
scraped: true
---

# Stripe Credit Card Field Is Using The Wrong Zip Code - SureCart

## Summary

When testing purchases in SureCart, users may encounter issues inputting non-U.S. zip codes. Stripe determines the billing address country using the card number and validates postal code formats accordingly.

## Key Points

**The Core Issue:**
Many test cards default to U.S. billing addresses, which only accept five-digit numeric codes (like 12345). This limitation isn't a SureCart bug but rather Stripe's validation based on the card's country origin.

**Solution:**
- Use proper five-digit U.S. ZIP codes when testing with American test cards
- Switch to international test card numbers from Stripe's testing documentation to validate different postal code formats (alphanumeric for UK cards, etc.)

**Why This Happens:**
Different countries have different postal code requirements: some require numeric-only formats, others allow alphanumeric characters, and some may not require them at all. Stripe enforces these rules based on the card's detected country.

Users experiencing ongoing issues are encouraged to contact SureCart's support team for additional assistance.
