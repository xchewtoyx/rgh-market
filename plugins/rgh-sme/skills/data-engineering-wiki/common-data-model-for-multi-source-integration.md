---
type: concept
title: Common Data Model for Multi-Source Integration
description: >
  Standardizing on one canonical schema that every source system's data gets
  mapped into, instead of picking one source's own format as the target or
  building bespoke per-pair mappings.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (Serra), ch. 8"
---

A **common data model (CDM)** is a standardized target schema that every
source feeding a warehouse or integration layer gets mapped into, rather
than the pipeline adopting one source system's own format as the de facto
standard. The canonical case: several CRM products from different vendors,
each with its own table and field naming, need to feed one warehouse.
Picking any single vendor's schema as the target either privileges that
vendor's modeling quirks over the others' or breaks the moment that vendor's
schema changes; a CDM instead defines a schema independent of any one
source, and every source — including that first vendor's — maps into it the
same way.

This is [conformance](warehouse-layering-source-staging-presentation.md)
applied one layer earlier than a warehouse's own conformed dimensions: a CDM
is the multi-*system* integration target that a pipeline's extraction and
mapping logic normalizes toward, before the data even reaches the point
where warehouse-internal conformance (identical column names and meaning
for the same concept across warehouse tables) applies.

**Build vs. buy** is the practical decision a data engineer actually faces:
building a CDM from scratch is substantial modeling work, but several cloud
platforms and vendors publish prebuilt, industry-specific CDMs (banking,
healthcare, retail) that can be adopted and customized instead of designed
from zero — trading some modeling effort for the constraint of fitting the
organization's actual data into a schema someone else already opinionated
about. Adopting a prebuilt CDM is usually worth it when the organization's
data genuinely resembles the industry-standard shape the CDM assumes;
building a bespoke one is worth it once source data diverges enough from any
available template that forcing the fit would cost more mapping-logic
complexity than a from-scratch model would.

Once a CDM exists, every source's [extraction and mapping](extraction-transfer-method.md)
pipeline has one fixed target to transform toward regardless of how many
sources feed it — adding a new source system later means writing one new
source-to-CDM mapping, not renegotiating the target schema against every
mapping that already exists.
