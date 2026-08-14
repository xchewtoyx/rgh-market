---
type: concept
title: Conditional Request
description: >
  Client-supplied version metadata that skips full response bodies when server
  data is unchanged, saving bandwidth on rarely mutating resources.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 3, ch. 7"
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), conditional retrieval"
---

A **conditional request** carries [metadata elements](metadata-element.md) — in
headers or the message — stating the client's cached version. The provider
evaluates the condition; if data is unchanged, return a short **not modified**
status instead of the full body; the client reuses its cache.

Variants:

- **Time-based:** last-modified timestamp; respond only if newer than the client's
  copy (`If-Modified-Since` / `304 Not Modified`). Needs reasonable clock alignment
  when accuracy matters.
- **Fingerprint-based:** entity tag or hash of the representation (`ETag` /
  `If-None-Match` / `304`). Works when content, not wall time, defines sameness.

Implementation may compute the full response then discard it if unchanged — saving
bandwidth but not server CPU unless paired with server-side caching.

## Trade-offs

Clients avoid reprocessing unchanged payloads without the server tracking per-client
freshness — the client reminds the server what it already holds. Combines with
[wish list](wish-list.md) or [wish template](wish-template.md) to specify which
subset to resend when the condition fails. With [pagination](pagination.md), evaluate
conditions including metadata changes (new pages added while a page's rows are
unchanged).

Providers should define interaction with [rate limit](rate-limit.md) and
[pricing plan as contract](pricing-plan-as-contract.md) — conditional hits may still
incur cost if computation runs before the 304.

Distinct from [request deduplication and idempotency keys](request-deduplication-and-idempotency-keys.md)
(retry safety) and from [resource revision](resource-revision.md) (optimistic write
concurrency).
