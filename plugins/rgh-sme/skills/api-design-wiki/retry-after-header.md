---
type: concept
title: Retry-After Header
description: >
  Server-authoritative retry delay in seconds, preferred over absolute timestamps,
  when the provider knows when a retried request may succeed.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 29"
---

When the server knows **when** a retry may succeed — especially [rate limit](rate-limit.md)
window reset — communicate via the **`Retry-After`** HTTP header (RFC 7231) instead
of forcing blind [exponential backoff](exponential-backoff-with-jitter.md).

Format: **duration in seconds** (preferred) or absolute HTTP-date. Prefer
duration — clock skew between server and client makes timestamps unreliable
(client at "1:00 p.m." may retry immediately when server meant "wait until
1:00 p.m.").

Clients: if `Retry-After` is present on a retriable response, use
`Number(header) * 1000` ms for that wait; otherwise fall back to jittered
backoff.

The server cannot enforce client compliance — document alongside
[client retry eligibility](client-retry-eligibility.md).
