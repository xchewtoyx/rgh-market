---
type: concept
title: Correlate Independent Telemetry Systems via a Shared Trace ID
description: Exporting a simple, stable trace/span ID as metadata lets otherwise-unrelated telemetry systems — exception trackers, network dashboards, ad hoc query logs — link back into the full distributed trace context, without needing to be part of one unified pipeline.
sources:
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §6.1.1, §6.2, §6.4"
---

A tracing system doesn't have to be the single source of truth for every telemetry signal to be valuable — it can act as a connective layer other, independently-built systems join against, as long as it exports a simple, stable identifier (a [trace/span id](trace-anatomy-and-spans.md)) those systems can attach as their own metadata. This is a much lower integration cost than merging systems into one pipeline, and Google saw it pay off in several unrelated ways:

- **Exception monitoring** — when an exception occurs inside a sampled trace, the exception-reporting service tags the report with that trace's id, and its own UI links directly from a specific exception report out to the full distributed trace it happened in. An [exception slug](exception-slug-for-error-attribution.md) tells you *which* code path threw; the linked trace tells you the full forensic context — what request, what upstream calls, what state — surrounding the moment it threw.
- **Ad hoc log correlation** — a team investigating tail latency pulled a sample of real user queries from a separate, secure log repository that had nothing to do with the tracing system, and joined them against the trace repository purely on the shared trace id, building example-query lists per subsystem without either system needing to know about the other in advance.
- **Attribution for a system the tracing tool wasn't designed for** — a network-usage dashboard used trace ids to point from an expensive inter-cluster network flow back to its **causal trace root** (the application-level request that ultimately caused the traffic), turning "these two machines exchanged a lot of data" into "this specific endpoint's requests caused this load" — something the network layer alone can't see, since it only ever sees two peer machines in isolation. The dashboard built on top of these APIs took under two weeks.

The general lesson: designing a tracing/telemetry system's public interface around a simple, exportable unique id (rather than requiring every consumer to integrate deeply) is what lets a much wider ecosystem of unplanned tools correlate against it later — see [self-service telemetry access](self-service-telemetry-access.md) for the parallel argument about API-driven adoption more broadly.
