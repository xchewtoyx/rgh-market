---
type: concept
title: The Four Golden Signals and System Instrumentation Methods
description: Latency, traffic, errors, and saturation are the four signal categories that provide a minimal sufficient picture of service health, analyzed via workload-centric (RED) and resource-centric (USE) methodologies across system and database layers.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 6"
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 2"
  - title: "Database Reliability Engineering"
    resource: "Database Reliability Engineering (Laine Campbell & Charity Majors), ch. 4"
---

A minimal, active set of signals to instrument and visualize for any service:

1. **Latency** — The time taken to service a request. Telemetry must distinguish successful-request latency from failed-request latency (an immediate HTTP 500 error might return in 2ms and skew averages downwards). See [latency percentiles, not averages](latency-percentiles-not-averages.md).
2. **Traffic** — The demand placed on the system (e.g., HTTP requests/sec, network I/O bits/sec, database transactions/sec).
3. **Errors** — The rate of requests that fail, including explicit errors (HTTP 5xx), implicit errors (HTTP 200 with wrong/empty payload), and policy violations.
4. **Saturation** — How "full" the service or resource is, representing the queueing or wait time before work can be processed. Saturation is a leading indicator of performance degradation that warns of impending bottlenecks before resource exhaustion occurs.

These four signals are a starting point for [operational dashboards](purposes-of-monitoring.md) and pair with [symptom-based alerting](symptom-based-vs-cause-based-alerting.md).

## Workload vs. Resource: The RED and USE Methods

To systematically gather and display these signals, operators use two complementary instrumentation methodologies:

* **The RED Method (Workload-Centric)**: Focuses on **Requests** (rate), **Errors** (rate), and **Duration** (latency) for *every service endpoint*. Optimized for microservices, user journeys, and API layer health.
* **The USE Method (Resource-Centric)**: Focuses on **Utilization** (% time busy or capacity used), **Saturation** (work queue length or wait times), and **Errors** (hardware or software error rates) for *every physical and logical resource* (CPU, memory, storage disks, network interfaces, lock structures).

## Database Saturation and Instrumentation Layers

Because databases are highly stateful and bottleneck-prone, monitoring database health requires layering the USE and RED methods across distinct tiers:

1. **Application Connection Layer**: Focuses on connection pool utilization (active connections vs. maximum limits) and saturation (connection queue backlog, thread/connection timeouts). *Tip: Watch for connection pool overhead; for instance, disabling database client autocommit can inject unnecessary BEGIN/COMMIT round-trips for read-only queries, saturating connection pools.*
2. **Internal Database Visibility**:
   * *Throughput and Latency*: Track reads, writes, and DDL operations. SQL comments containing the calling application logic file/line help map slow database transactions back to the source code.
   * *Replication Health*: Monitor for replication **lag** (time behind primary), replication **broken** status (stopped thread), and replication **drift** (silent desync, detected via periodic range-checksum comparisons).
   * *Concurrency and Locking*: Track lock wait times, mutex/semaphore contention, and rollback/deadlock rates as saturation and correctness signals.
   * *Compaction/Flush Queues*: Monitor journal write latency and background task queues (compaction, page flushing) as flush-induced bottlenecks degrade frontend latency.
3. **Server and Operating System Layer**: Apply the USE method to monitor OS resources (CPU, memory swap, disk I/O, file descriptor allocation). In virtualized environments, check CPU **steal time** (>10% indicates a noisy neighbor that requires server termination/relaunch).

## Granularity and Sampling Resolution

High-[cardinality](cardinality.md), highly variable metrics require high-resolution (typically $\le 1$-second) sampling. Standard 1-minute averaging windows are lossy and can hide transient spikes (e.g., brief lock contention, microsecond disk queue spikes, or CPU thrashing from Transparent Huge Pages defragmentation), leading to delayed alerts and missed root causes. 
