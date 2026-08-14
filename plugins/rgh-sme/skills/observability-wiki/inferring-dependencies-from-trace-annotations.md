---
type: concept
title: Infer Service Dependencies From Trace Annotations, Not Static Config
description: In a large system, which services and shared infrastructure a job actually depends on changes dynamically enough that static configuration can't be trusted as ground truth — but mining accumulated trace annotations for what a job's requests actually touched can derive an accurate, current dependency graph automatically.
sources:
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §6.3"
---

In a large computing cluster with thousands of logical jobs, dependencies between jobs — and on shared infrastructure those jobs both rely on — change dynamically enough that static configuration can't be trusted as an accurate map of what actually depends on what. That's a problem when accurate dependency information is exactly what's needed to identify bottlenecks or safely plan a service move.

The fix is to derive the dependency graph from observed behavior instead of declared configuration: mine [trace annotations](trace-anatomy-and-spans.md) accumulated across many requests for which resources a job's calls actually touched, and build the graph from that. A concrete example: tagging every storage operation with the name of the specific table or resource it affected, then aggregating across a large volume of traces, is enough to automatically infer both job-to-job dependencies and job-to-shared-infrastructure dependencies at whatever granularity the annotations support — without anyone having declared those dependencies anywhere.

This is the same underlying move behind [distributed tracing for troubleshooting](distributed-tracing-for-troubleshooting.md) generally: treat accumulated, per-event telemetry as ground truth about actual runtime behavior, and treat configuration or documentation describing intended behavior as a hypothesis to be checked against it rather than assumed correct.
