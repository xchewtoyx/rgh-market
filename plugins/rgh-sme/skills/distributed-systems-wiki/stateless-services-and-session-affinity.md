---
type: concept
title: Stateless Services and Session Affinity
description: >
  Keeping per-request history out of service instances makes any instance
  interchangeable; when statefulness can't be avoided, pinning a client to
  one instance trades that interchangeability for simplicity.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman), ch. 17"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 27"
---

# Stateless Services and Session Affinity

**State**, here, is data whose current value depends on request history and
affects how future requests are handled. It has to live somewhere: inside
each service instance (a **stateful** service), inside each client, or in
an external database — the latter two are both called "stateless" because
the *service* instance itself retains no history between requests.

The default worth defaulting to is **stateless services**. A stateful
instance loses its history on failure and is hard to recover, and it
blocks the thing that makes horizontal scaling and failover cheap: spinning
up a fresh, interchangeable instance that can transparently take over from
any other. A [load balancer](l4-vs-l7-load-balancing.md) in front of
stateless instances can route any request to any instance, evict a failing
one, and add capacity, all without coordinating who "owns" a given client's
state.

When statefulness genuinely can't be avoided — an in-memory cache warmed
per-client, a long-lived connection, a partially-built session — two
workarounds pin a client's request series to one instance instead of
paying to replicate that state everywhere:

- **Direct sessions.** The load balancer routes only the client's first
  request; the client learns that instance's address and talks to it
  directly afterward, bypassing the balancer for the rest of the session.
- **Sticky sessions (session affinity).** The load balancer itself keeps
  routing a given client's subsequent requests to the same instance
  (typically via a cookie at [L7](l4-vs-l7-load-balancing.md)), so the
  client never needs to know which instance it's pinned to.

Both should be used sparingly: they reintroduce exactly the failure mode
statelessness avoids. If the pinned instance dies, the client's session
dies with it — there's no other instance to transparently fail over to —
and a popular sticky client can overload its one instance while siblings
sit idle, defeating the balancer's job.

Small amounts of state that must be visible to *every* instance at once
(configuration, a load balancer's own address, partition ownership) are a
different problem — that's what a [coordination
service](coordination-services.md) is for, not per-client pinning.

## Transient local state on ephemeral workers

On [ephemeral compute instances](ephemeral-compute-instances.md), anything
in-process or on local disk is lost whenever the scheduler replaces the
worker (and local disk is lost if the job moves machines). Legitimate uses
still exist, but each accepts bounded loss:

- **Caching** — trades a small durability risk for latency; see [caching
  tiers](caching-tiers.md) for provisioning the uncached path for full load.
- **Warm-up pulls** — copy data from external storage at startup to cut
  serving latency.
- **Batched writes** — metrics or batch outputs where losing a fraction is
  acceptable, or where work can be recomputed; long jobs can
  **checkpoint** to persistent storage periodically to cap loss the same way
  [dynamic work assignment](dynamic-work-assignment.md) caps it per chunk.

If all local state is immutable, failure resistance is comparatively painless;
mutable local state pushes you toward pet semantics unless you replicate or
externalize it.

