---
type: concept
title: Request Deduplication and Idempotency Keys
description: >
  Wire mechanisms that let clients safely retry non-idempotent calls without
  duplicate side effects by supplying a unique client-generated token.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 26"
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 5"
---

After ambiguous network failure a client cannot tell whether the server never
received the request or processed it but lost the response. [Standard methods](standard-method-contract.md)
that are idempotent (get, list) retry freely; non-idempotent creates and deletes
need explicit deduplication.

## Request identifier

Add an optional **request id** field (for example `requestId?: string` on
`CreateChatRoomRequest`) on methods that need safe retry. Unlike
[resource identifiers](resource-identifier.md), request ids are **client-chosen**
and single-use — only the client knows whether a call is a retry.

- **Missing/blank id:** process normally — deduplication is opt-in, not inferred
  from the body hash (clients may legitimately submit identical bodies twice).
- **Invalid format:** reject with 400 — enforce the same format rules as resource
  ids because clients choose poorly.

## Response caching

On first processing with a request id: execute, cache the **full response** keyed
by id, return it. On duplicate: return cached response — not a bare "already handled"
error (create retries still need the created id).

Caching entire responses is pragmatic even for large payloads (batch create of
hundreds of rows) — RAM is cheaper than bespoke response reconstruction.

**Stale cache is correct:** if client A's update response is lost and retried while
client B updates the same resource, the retry returns A's original cached response,
not live state. The pattern guarantees **same outcome as if the first attempt had
succeeded**, not freshness. Do not keep the cache synchronized with live data.

## Collisions and fingerprints

Clients reuse ids by mistake. Store a [request fingerprint](request-fingerprint.md)
(hash of the request body) with each cache entry. On cache hit: matching hash →
return cached response; mismatch → **409 Conflict** (collision, not retry).

## Cache expiration

Expire entries after a short window (~five minutes is a reasonable start). Reset the
timer on each cache hit so further retries within the grace period still succeed.
Tune from observed traffic and cost.

## Rollout

Not every API needs deduplication everywhere. Add on sensitive methods first; make
`requestId` required when duplicate execution is unacceptable.

Prefer absolute updates ("set x to y") over incremental deltas under retry.
Document which standard methods are idempotent and which require keys.

Distinct from request-fingerprint **authentication** — same hash machinery, different
purpose.
