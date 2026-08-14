---
type: concept
title: Developer–Operator Telemetry Mismatch
description: Pre-defined metrics and logs reflect what developers chose to expose at build time, which often fails to match what operators need to diagnose unpredictable production issues — and recording everything upfront has real performance and signal-to-noise costs.
sources:
  - title: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems"
    resource: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems (Mace, Roelke, Fonseca), §2.3"
---

Distributed-system problems are complex, varied, and unpredictable; the information required to diagnose a specific issue may not be reported in system logs or pre-defined metrics, because there is a structural mismatch between **developer expectations and incentives** and **operator and user needs**. Developers instrument what they anticipate debugging; operators encounter failures nobody anticipated. Log messages often contain too little information for diagnosis; issue trackers fill with requests for new metrics, changed aggregation methods, and new breakdowns of existing metrics — frequently unresolved due to developer pushback or inertia.

Recording more information upfront does not solve the mismatch — it trades one problem for two others:

- **Performance cost paid by everyone** — HBase's `SchemaMetrics`, introduced to aid developers, imposes a ~10% performance overhead on *all* HBase users whether or not they use it; enabling too many metrics can overwhelm a Ganglia server's processing capacity.
- **Needle-in-a-haystack retrieval** — even when data exists, extracting the relevant subset requires deep system familiarity. Mesos exposes cluster state via a single JSON endpoint that can become massive when a client wants only a subset.

Dynamic instrumentation frameworks (Fay, DTrace, SystemTap) address the mismatch by allowing near-arbitrary probes to be installed at runtime, proven useful for diagnosing complex, subtle problems. Their side-effect-free design limits how much probes can share information: Fay probes in the same address space can share state; DTrace's scope is limited to a single OS instance. [Pivot Tracing](pivot-tracing.md) extends dynamic instrumentation with [causal metadata propagation](context-propagation.md) across process and tier boundaries, so runtime-defined queries can correlate probes that prior dynamic tools could not link.

Production [distributed tracing](trace-anatomy-and-spans.md) systems (Dapper, HTrace, Zipkin) help navigate [cross-tier observability gaps](cross-tier-observability-gaps.md), but most record traces for offline analysis — what gets recorded is still defined a priori, reproducing this challenge for anything not included in the trace schema. The corrective posture is the same as [closing telemetry gaps from past incidents](closing-telemetry-gaps-from-past-incidents.md) and the [streetlight effect in instrumentation priorities](streetlight-effect-in-instrumentation-priorities.md): treat "we didn't instrument this because nobody asked" as a gap to close, not as evidence the path doesn't matter.
