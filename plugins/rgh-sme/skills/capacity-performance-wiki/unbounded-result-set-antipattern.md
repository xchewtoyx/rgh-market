---
type: concept
title: Unbounded Result Set Antipattern
description: A query or API call with no explicit limit on how many rows or records it can return works fine on a small dataset and becomes a resource-exhaustion risk once production data grows past what the caller silently assumed.
sources:
  - title: "Release It!, 2nd Edition"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Michael T. Nygard), ch. 4"
---

A query like `SELECT * FROM orders WHERE customer_id = ?` or an API endpoint that returns "all matching records" with no pagination or `LIMIT` clause behaves identically to a bounded query for as long as the matching set stays small. Nothing about the code changes as the underlying data grows — the failure is entirely a function of data volume the caller never accounted for, which is exactly why it tends to surface long after the code was written and reviewed, once a customer, a batch job, or organic growth finally produces a match count nobody tested against.

## Why It's a Capacity Problem, Not Just a Correctness One

An unbounded result set that grows large enough causes damage on both sides of the call:

*   **On the database side**, materializing and transmitting an unexpectedly large row set consumes memory, I/O, and network bandwidth proportional to the match count rather than to any request-level budget — a single query can degrade a shared database for every other concurrent query.
*   **On the caller side**, deserializing a much-larger-than-expected response can trigger long garbage-collection pauses or an out-of-memory condition, turning one oversized query into a caller-side [slow response](rpc-deadlines-and-resource-holding.md) or crash that then propagates its own load-shedding and retry effects onto everything else the caller was serving.

## Mitigation

*   **Always cap result sets explicitly** — a `LIMIT`/`TOP` clause, or a hard maximum enforced by the query layer, so an unexpectedly large match count is truncated rather than fully materialized.
*   **Design for pagination from the start** on any query or endpoint whose result size is a function of data the caller doesn't control (a customer's order history, a search result set) rather than retrofitting it once a production incident forces the issue.
*   **Treat an unbounded query as untested load, not just untested logic.** The same discipline that requires characterizing [load parameters](load-parameters.md) before capacity planning applies here at the level of an individual query: the maximum realistic match count is itself a load parameter that needs an explicit bound, not an assumption.
