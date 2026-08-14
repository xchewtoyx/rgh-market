---
type: concept
title: Reverse ETL
description: >
  Feeding processed pipeline output back into source systems or SaaS
  platforms, and why it's now treated as a legitimate serving pattern rather
  than an antipattern.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 2"
---

Reverse ETL takes data that a pipeline has already processed and pushes it
back into the operational systems it originally came from, or into SaaS
platforms — for example, pushing computed ad bids from a warehouse into
Google Ads, or pushing derived customer metrics into a CRM.

It was long treated as an unspoken antipattern (data is supposed to flow
*into* the warehouse, not back out to operational systems), but commercial
tooling (Hightouch, Census) has emerged specifically to support it, and it's
now treated as a legitimate, likely-permanent serving pattern rather than
something to design around. The term itself is still settling — some argue
the same need could be met by event-stream-based transformations sent
directly back to source systems instead of a dedicated reverse-ETL hop — but
the underlying requirement (get transformed data back to the systems that
need to act on it, with [lineage](data-lineage.md) intact) persists
regardless of what it's called.

As a pipeline design concern, reverse ETL adds a delivery-guarantee question
that forward ingestion doesn't usually have to answer as sharply: pushing a
wrong or duplicate value into an external CRM or ad platform has an external,
sometimes costly, effect, not just an internal reporting error — so
idempotency and reconciliation matter more, not less, at this hop.

A related but distinct case is **data propagation to non-negotiable external
targets**: extracting from the presentation layer to share with business
partners, submit to a government/regulatory recipient, or feed a packaged
analytics or data-mining tool that can't query the warehouse directly. This
is structurally the same extract-transform-load work as any other pipeline,
using the same tooling — the difference is that the target's format and
delivery requirements are fixed by an outside party, not negotiable the way
an internal consumer's needs usually are.

**Runaway feedback loops**: because reverse ETL writes back into the same
kind of system that feeds the pipeline's own ingestion, it can create a
closed loop that amplifies itself if left unmonitored — download ad
performance data, compute new bids from a model, push the new bids back into
the ad platform, then ingest the results of *those* bids on the next cycle.
A bug that trends the model's bids upward can spiral through repeated cycles
of this loop and waste a large amount of spend before anyone notices, since
each individual write looks reasonable in isolation. Any reverse ETL loop
needs its own monitoring and guardrails (a sanity-check bound on how much an
output value can move per cycle, for instance) precisely because the loop
being closed removes the human checkpoint that would normally catch runaway
behavior.
