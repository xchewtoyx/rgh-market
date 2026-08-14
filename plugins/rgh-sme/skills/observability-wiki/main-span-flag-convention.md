---
type: concept
title: The Main-Span Flag Convention
description: Tagging one designated span per request or job as the primary unit of work (e.g. main = true) lets queries isolate it from noisy child spans, which is essential for correct error-rate and latency calculations that would otherwise double-count status codes from downstream sub-requests.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 6"
---

A request or job typically produces one root [span](trace-anatomy-and-spans.md) representing the overall unit of work, plus any number of child spans for its sub-operations. Without a way to distinguish the two, a query computing an aggregate like "error rate" or "p99 latency" across all spans will double-count: a single failed request that made three downstream calls, one of which also failed, would otherwise count as two errors instead of one, or mix child-span durations into a metric meant to describe the whole request.

The fix is a simple tagging convention: mark the one span per request/job that represents the primary unit of work with an attribute like `main = true`. Queries computing request-level aggregates then filter to `main = true` first, cleanly separating "how is the overall request doing" from "how are its sub-operations doing." This convention pairs naturally with [recording sub-operation timings as attributes rather than child spans](timings-as-attributes-not-child-spans.md) — both exist to keep request-level aggregation simple and correct.
