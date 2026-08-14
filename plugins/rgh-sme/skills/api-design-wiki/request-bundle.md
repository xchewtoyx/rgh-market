---
type: concept
title: Request Bundle
description: >
  A single API operation that accepts multiple sub-requests or incident records
  in one message to amortize round-trip cost.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 5, ch. 7"
---

A **request bundle** combines multiple independent sub-requests in one message —
structured as [parameter forests](parameter-forest.md) or [parameter trees](parameter-tree.md)
with per-element [id elements](id-element.md) and counters. Reduces chatty integrations;
increases payload complexity and partial-failure handling.

**Response options:**

1. **Single bundled response** mirroring request structure (for example comma-separated
   ids in path returning one array).
2. **Multiple responses** as sub-results complete (protocol-dependent streaming).

Document **atomicity**: all-or-nothing vs per-item [error report shape](error-report-shape.md).
Elements may execute **concurrently** — do not assume order unless explicitly guaranteed
(and document the cost of ordering). Clients wait for the whole bundle, improving total
time versus many sequential calls but raising latency to first byte.

**Risks:** uneven access control across elements forces partial failures and retry
logic; provider may need stateful coordination — harmful for horizontally scaled
[processing resources](processing-resource.md). Best when the protocol lacks native
multiplexing and every element shares compatible authorization.

Combines with [conditional request](conditional-request.md), [wish list](wish-list.md),
and [wish template](wish-template.md) — combining three such patterns rarely pays off.
Distinct from [batch operations](batch-operations.md) (same-type atomic CRUD on a
collection) though both reduce round trips.

Positively affects invocation-count [rate limit](rate-limit.md) accounting; clarify
billing in [pricing plan as contract](pricing-plan-as-contract.md).

Version bundled sub-requests under one [version identifier](version-identifier.md)
when wire shape must stay coherent.
