---
type: concept
title: Cascading Failure
description: A positive feedback loop of failures that propagates through a system, often triggered by resource exhaustion, load shifts, or thundering herds.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 22"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 10"
  - title: Release It!
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 2, ch. 3, ch. 4"
---

A cascading failure is a failure mode where a small localized issue triggers a feedback loop of failures that propagates across system boundaries, ultimately collapsing the entire service. It is the [fault-error-failure chain](fault-error-failure-chain.md) allowed to cross component and service boundaries unchecked. Systems with high interactive complexity and tight coupling make this kind of propagation a statistically expected occurrence rather than a rare anomaly — see [normal accident theory](normal-accident-theory.md).

## Mechanics of Propagation

Cascading failures are driven by positive feedback loops. Common triggers and propagation pathways include:
1.  **Load Shifting**: In a cluster of redundant servers, if one node fails, its traffic is distributed among the remaining healthy nodes. If the system is operating near capacity, this additional load can overload and crash another node, initiating a domino effect.
2.  **Resource Exhaustion**: An increase in latency or errors in a downstream dependency can cause upstream threads, database connections, or network sockets to block. This resource starvation quickly starves the upstream service, propagating the failure.
3.  **Retry Storms**: When calls to a downstream dependency fail, client libraries often retry automatically. Without coordinate mitigation, these retries multiply and act as a denial-of-service attack on the already struggling dependency.

### A Worked Example of Resource-Exhaustion Propagation

A fleet-grounding airline outage shows resource exhaustion propagating concretely. An uncaught runtime exception in a minor internal admin tool (triggered by a missing lookup-table entry for a rare discount code) caused the container to discard the bean instance without releasing its database connection or thread back to their pools. Because that admin tool shared its application server clusters, containers, and connection pool with the passenger-facing check-in and booking systems, the exhausted pool starved those critical-path systems too — thread starvation propagated from the admin app server to the shared database and core transactional app servers until the entire system went down over what began as a routine change to a non-critical tool.

## Structural Mitigation in Reliability Engineering

Preventing cascading failures is a core objective of designing for [dependency reliability composition](dependency-reliability-composition.md). Key structural mitigations include:
*   **Decoupling Dependencies**: Designing critical user paths with [hard vs soft dependency](hard-vs-soft-dependency.md) distinctions. Downstream issues should be isolated so soft dependencies fail gracefully rather than locking resources upstream.
*   **Circuit Breakers**: Wrapping dependency calls in [circuit breakers](circuit-breaker-pattern.md) to immediately fail fast locally when error thresholds are crossed, preventing local thread/socket exhaustion.
*   **Exponential Backoff with Jitter**: Adding randomized backoff delays to retry attempts to prevent synchronized thundering herd spikes.
*   **Load Shedding**: Rejecting low-priority requests via [load shedding](load-shedding.md) at the server boundary under overload to preserve capacity for critical traffic.
*   **Bulkheads**: Partitioning shared resources (thread pools, connection pools, server clusters) per function via the [bulkhead pattern](bulkhead-pattern.md), so resource exhaustion in a low-priority function cannot starve a critical one.
*   **Canary Requests**: In fan-out architectures, testing a query against one or two backends via the [canary request pattern](canary-request-pattern.md) before dispatching it fleet-wide, so a single malformed or malicious query can't crash every backend at once.
*   **Failure Domain Alignment**: Sizing and auditing [failure domains](failure-domain.md) so a local failure's blast radius matches its intended scope instead of silently spanning more of the system than assumed.
