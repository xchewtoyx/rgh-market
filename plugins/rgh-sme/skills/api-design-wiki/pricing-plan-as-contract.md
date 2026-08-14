---
type: concept
title: Pricing Plan as Contract
description: >
  Published billing tiers and metering rules that fund API operations and define
  mutual provider–client obligations alongside rate limits and SLAs.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 9"
---

An API is a product whose development and operations must be funded. A **pricing
plan** (rate plan) in the [API description](api-description.md) defines how
consumption is metered and billed — subscription, usage-based, market-based, or
combinations (for example flat monthly base plus overage). It pairs with
[rate limit](rate-limit.md) tiers, [service level agreement as contract](service-level-agreement-as-contract.md),
and client identification via [API key as message element](api-key-as-message-element.md)
or equivalent auth.

## Variants

- **Subscription** — recurring fee largely independent of volume, often with a
  fair-use [rate limit](rate-limit.md); multiple billing levels with upgrade paths
  when allowance is exceeded (or downgrade/block if not).
- **Usage-based** — bill on calls, data transferred, or operation type (reads
  cheaper than creates); periodic invoicing or prepaid credit packages.
- **Market-based** — bid/max price; service while market price is at or below bid.
- **Freemium** — free tier or trial, payment above threshold; can combine with any
  variant above.

A one-off sign-up fee alone often misprices hobbyists versus high-volume
enterprise users.

## Design tensions

**Accuracy versus cost** — clients expect pay-for-what-you-use and spending caps;
deep per-call accounting can hurt performance. **Granularity** — real-time versus
daily aggregates; metering outages mean lost revenue unless the API stops or
service is free until metering recovers.

**Security and privacy** — tie charges to the correct tenant; prevent key
impersonation. In multitenant APIs, [error report shape](error-report-shape.md)
and metering responses must not leak other tenants' existence or usage (competitors,
NDA partners).

Product owners and engineers jointly balance implementation effort: subscription
pricing is simpler; usage-based needs monitoring, reporting, and dispute-resistant
detail. Starting subscription-only and adding usage-based later is viable.

## Cost control for clients

When pricing includes data volume, [wish list](wish-list.md) and
[wish template](wish-template.md) help clients limit transferred fields and
control bills.

Changing tiers, limits, or meter granularity may require a
[version identifier](version-identifier.md) bump and updated commercial terms.
[Aggressive obsolescence](aggressive-obsolescence.md) of features may force plan
adjustments.
