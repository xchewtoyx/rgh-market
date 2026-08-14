---
type: concept
title: A Single Trace Can't See Cross-Request Contention
description: Distributed tracing is effective at showing which part of a system a request was slow in, but a request can be slow purely because other, unrelated requests were queued or contending for the same resource ahead of it — an effect invisible from that request's own trace alone.
sources:
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §7"
---

[Distributed tracing](distributed-tracing-for-troubleshooting.md) is good at answering "which service or RPC in the call chain was slow" — but that's a different question from "why was it slow," and tracing alone doesn't always answer the second one. A request's own trace only shows *its* path through the system; if it was slow because other, unrelated requests were queued ahead of it for the same resource (a lock, a thread pool, a downstream service at capacity), that contention doesn't show up anywhere in the slow request's own spans — every span it touched can look individually correct while the request as a whole was still slow, purely from waiting its turn.

Two mitigations, neither of which is automatic from tracing infrastructure alone:

- **Application-level annotations of contention state** — have the contended component explicitly record queue depth, in-flight request count, or an "overloaded" flag as an annotation on spans passing through it, turning an otherwise-invisible systemic condition into a queryable field.
- **Paired/comparative sampling** — sample two time-overlapping requests through the same system and compare their relative latencies stage by stage, rather than examining either trace in isolation (the general technique behind ProfileMe-style paired sampling). Divergence between two requests that should have taken similar paths at similar times is itself evidence of contention, even without a component ever nameable as "the cause."

This is a specific, mechanism-level instance of the broader debugging trap in [emergent failure vs. broken-component hunting](emergent-failure-vs-broken-component-hunting.md): the "problem" here is an interaction between requests, not a defect in any single one of them, so a debugging approach that only inspects one request's trace at a time is structurally unable to find it no matter how carefully that one trace is read.
