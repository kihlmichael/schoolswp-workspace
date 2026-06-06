---
source_url: https://developer.surecart.com/api-reference/rate-limiting
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/api-reference/rate-limiting#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

The SureCart API uses a number of safeguards against bursts of incoming traffic to help maximize its stability. If you send many requests in quick succession, you might see error responses with status code 429.

### [​](https://developer.surecart.com/api-reference/rate-limiting#api-limiters) API Limiters

We have several limiters in the API, including a rate limiter and a concurrency limiter. Treat the limits as maximums, and don't generate unnecessary load. To prevent abuse, we might reduce the limits.You can request a limit increase to enable a high-traffic application by contacting SureCart Support.

### [​](https://developer.surecart.com/api-reference/rate-limiting#rate-limits) Rate Limits

The basic rate limiter restricts the number of API requests as follows:Default Limit: 150 operations / 10 secondsSensitive Endpoints: 10 operations / 1 minutePublic Endpoints: 60 operations / 1 minuteSensitive endpoints include those that may trigger notifications or call third-party services. In general, these are endpoints that should not be called frequently.Public endpoints are those that are accessible with a public API key. For example, our license check endpoint.
