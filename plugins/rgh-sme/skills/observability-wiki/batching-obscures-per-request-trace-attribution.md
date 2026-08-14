---
type: concept
title: Batching Obscures Per-Request Trace Attribution
description: Distributed tracing implicitly assumes a subsystem does work for one traced request at a time; when a subsystem instead batches several requests' work together for efficiency (e.g. coalesced disk writes), the trace can misattribute the whole batch's cost to a single request, or hide the other requests in the batch entirely.
sources:
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §7"
---

The [trace/span model](trace-anatomy-and-spans.md) implicitly assumes each unit of traced work is handled independently — one request in, one span out. Many systems intentionally violate that assumption for efficiency: buffering several requests and then operating on the whole group at once (e.g. coalescing multiple disk writes into one), because doing so is cheaper per-unit than handling each request in isolation.

This breaks trace attribution two ways. First, whichever request happens to trigger the batched operation gets "blamed" for the full duration of the whole batch's work, not just its own share — a single traced request can appear deceptively slow or expensive when the real cost was shared across many. Second, because a trace relies on a single trace id per traced unit of work, only one request in a coalesced batch ends up associated with the resulting span at all — the others' contribution to that same span is invisible in the trace data, even though they experienced the same latency.

There's no complete fix within the standard trace model; the practical mitigation is for the batching subsystem itself to log enough information (e.g. how many requests were coalesced into this operation, or an approximate cost-share) as an annotation on the span, so an investigator reading a suspiciously expensive span for a "simple" request knows to check whether it was actually paying for other work bundled in alongside it. Look for this failure mode specifically whenever a traced span's duration seems disproportionate to what its own request should require — it's a good candidate explanation before assuming the instrumentation itself is wrong.
