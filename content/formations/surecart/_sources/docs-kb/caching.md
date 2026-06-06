---
source_url: https://surecart.com/docs/caching
source: surecart-kb
scraped: true
---

# Caching Configuration for SureCart

## Overview

This guide provides guidance on configuring caching plugins to work properly with SureCart. It identifies potential conflicts and offers solutions.

## Key Configuration Requirements

**REST API Protection**: Exclude all REST API requests from being cached to prevent stale customer data, cart information, and checkout problems.

**Core Script Handling**: WordPress foundational scripts (wp-api-fetch, wp-a11y, wp-i18n, wp-url-js, dom-ready-js, hooks-js) must load synchronously and should not be deferred.

**JavaScript Optimization**: Disable script combining since HTTP/2 enables parallel resource loading, making file combination unnecessary and potentially harmful.

**Dynamic Page Exclusion**: Login, registration, checkout, and customer dashboard pages require exclusion from caching due to their user-specific, real-time nature.

**Browser Caching**: Aggressive browser caching for eCommerce data should be disabled to prevent displaying outdated cart contents or order information that cannot be remotely refreshed.

## Implementation Approach

Test thoroughly after adjusting caching settings. Contact SureCart support for additional assistance with implementation challenges.
