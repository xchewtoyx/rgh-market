---
type: concept
title: Pivot Tracing
description: Pivot Tracing is a dynamic causal monitoring system that lets operators define ad hoc queries over a tracepoint vocabulary, compiles them to advice installed at runtime, and uses baggage propagation to correlate measurements across process and tier boundaries.
sources:
  - title: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems"
    resource: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems (Mace, Roelke, Fonseca), §2.2"
  - title: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems"
    resource: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems (Mace, Roelke, Fonseca), §1"
---

Pivot Tracing targets a gap that neither pre-defined metrics nor offline [distributed tracing](trace-anatomy-and-spans.md) fully closes. Monitoring distributed systems is hard — hardware/software failures, misconfiguration, hot spots, aggressive tenants — and the tools commonly used (logs, counters, metrics) share two fundamental limitations:

1. **What gets recorded is defined a priori**, at development or deployment time ([developer–operator telemetry mismatch](developer-operator-telemetry-mismatch.md)).
2. **Information is recorded component- or machine-centrically**, making it extremely hard to correlate events that cross those boundaries ([cross-tier observability gaps](cross-tier-observability-gaps.md)).

Dynamic instrumentation (Fay, DTrace) enables diagnosing unanticipated problems at runtime but cannot propagate monitoring context across address-space or OS-instance boundaries. Pivot Tracing combines dynamic instrumentation with causal tracing so operators can obtain an arbitrary metric at one point while selecting, filtering, and grouping by events meaningful at *other* parts of the system — even across component or machine boundaries.

The name derives from spreadsheet pivot tables: dynamically selecting values, functions, and grouping dimensions from an underlying dataset. Intended for both one-off interactive debugging and standing long-running monitoring queries.

Three design goals drive the architecture:

1. **Dynamic runtime configuration** — install and change monitoring without recompiling or redeploying target systems.
2. **Low overhead** — enable "always on" monitoring rather than probe-only diagnostics.
3. **Cross-process causality** — capture causal relationships between events from multiple processes and applications.

Two mechanisms combine to meet these goals:

- **Dynamic code injection** — queries compile to an intermediate representation called **advice** ([pivot-tracing-advice.md](pivot-tracing-advice.md)), which Pivot Tracing agents install at the relevant [tracepoints](pivot-tracing-tracepoints.md) without recompiling or redeploying the system.
- **Causal metadata propagation** — [baggage](pivot-tracing-baggage.md) carries values captured at one tracepoint to advice executing at a later tracepoint along the same causal chain, enabling [happened-before joins](happened-before-join.md) in queries.

High-level flow: an operator defines a [query](pivot-tracing-query-language.md) over the tracepoint vocabulary; the query compiles to advice; agents install that advice dynamically; each time execution reaches an instrumented tracepoint, the installed advice runs. Advice at some tracepoints emits tuples, which are aggregated locally and streamed to the client over a message bus. A query optimizer decides where to install instrumentation and when propagation is required — simple aggregations at a single tracepoint (e.g. summing bytes read per host) need no propagation; cross-tier attribution queries do.

Production tracing systems like Dapper, HTrace, Zipkin, and Cloudtrace obtain richer per-execution information than component-centric logs or metrics alone, but most record or reconstruct traces of execution for **offline** analysis — what gets recorded is still defined [a priori](developer-operator-telemetry-mismatch.md), leaving the same "one size does not fit all" problem Pivot Tracing addresses. See [attributing shared-service load back to individual callers](attributing-shared-service-load-to-callers.md) for the worked HDFS disk-bandwidth example, [end-to-end latency diagnosis](pivot-tracing-end-to-end-latency-diagnosis.md) for per-component latency decomposition, and [instrumentation overhead](pivot-tracing-instrumentation-overhead.md) for measured cost.

Pivot Tracing is not meant to replace all functions of logs — security auditing, forensics, and general debugging still have their place. Dynamic instrumentation is not strictly required: a system could hard-code predefined tracepoints, at the cost of restricting users to those locations and tying new ones to the system's dev/build cycle; inactive hard-coded tracepoints would then cost at least a conditional check rather than Pivot Tracing's true zero cost for unused tracepoints. A system without [baggage propagation](context-propagation.md) can still use Pivot Tracing's other mechanisms, in which case it resembles DTrace or Fay. The mechanism generalizes beyond Java — queries can span systems in different languages given a platform-independent baggage format.
