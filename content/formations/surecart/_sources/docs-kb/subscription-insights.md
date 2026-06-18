---
source_url: https://surecart.com/docs/subscription-insights
source: surecart-kb
scraped: true
---

# Understanding Subscription Insights - SureCart

## Subscription Metrics Terms

**Total Subscription**: The total number of active subscriptions your business currently has. Includes both new and existing subscriptions.

**New Subscription**: Count of newly created subscriptions during a specific period.

**New Trials**: The number of subscriptions in a trial period within a selected time frame.

**MRR (Monthly Recurring Revenue)**: The total revenue your business generates from subscription fees on a monthly basis.

**MRR Lost**: Revenue lost due to cancellations, downgrades, or churn.

**Outstanding Installments**: Total value of unpaid installment payments.

## How MRR is Calculated

The calculation method varies by subscription type:

- **Monthly subscriptions**: MRR = SUM(active subscriptions x monthly cost)
- **Annual subscriptions**: MRR = SUM(active subscriptions / 12)
- **Daily subscriptions**: MRR = SUM(active subscriptions x 30.436875)
- **Weekly subscriptions**: MRR = SUM(active subscriptions x 4.348125)

The multipliers 30.436875 and 4.348125 represent the average number of days and weeks in a month, taking into account a time span of 100 years, including leap years.

### Example Calculation

A sample with 3 monthly ($30/month), 2 annual ($120/year), and 5 daily ($2/day) subscriptions yields: MRR = $231.75/month

## Live Mode and Test Mode

Analytics metrics can be toggled between Live Mode (default) and Test Mode with a single click.

## Quick Filter

Date range filters are available for common periods like current week.

## Subscriptions Table

A table displays all subscriptions with filters for: All, Active, Trialing, Past Due, and Canceled statuses.

## FAQ

**Q: How are metrics calculated for annual subscriptions?**
Divided by 12 monthly; a $300 annual subscription shows as $25 MRR.

**Q: Are installments included in Total Subscriptions and MRR?**
No, installments are tracked separately under "Outstanding Installments."

**Q: How can MRR Lost data help businesses?**
Understanding revenue loss helps identify causes and implement improvements to reduce churn.

**Q: What subscription warning signs should businesses monitor?**
High churn rates, stagnant MRR, and unexpected fluctuations.
