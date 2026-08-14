---
type: concept
title: Load Generator Bottlenecks
description: A performance testing pitfall where the test harness itself becomes saturated, limiting test throughput and masking target system regressions.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 1"
---

During load testing or benchmarking, a **load generator bottleneck** (or test harness bottleneck) occurs when the client machine or software generating the synthetic workload reaches a performance limit. This caps the maximum achievable throughput, regardless of the target system's actual capacity.

## Common Causes

1.  **Single-Threaded Client Execution:** The load generator client is single-threaded and saturates a single CPU core on the generator machine, capping request rates.
2.  **Synchronous Blocking:** The generator thread blocks waiting for a response before sending the next request. In this scenario, the maximum throughput $T$ is limited by the server's latency $L$ and the thread count $N$:
    $$T \le \frac{N}{L}$$
    If the server's latency increases, the test throughput will drop even if the server has idle resources. This same closed-loop behavior also corrupts the *latency* results the test reports, not just its throughput — see [coordinated omission](coordinated-omission.md).
3.  **Client-Side Resource Exhaustion:** The load generator machine runs out of CPU, memory, ephemeral network ports, or bandwidth.

## Consequences

*   **Masked Regressions:** A performance regression in a new software release may go unnoticed if the throughput in both tests is capped by the same load generator limit.
*   **Artificially Low CPU Utilization:** The server under test may show low utilization (e.g., 20% CPU), giving a false impression of headroom, because the load generator cannot push enough traffic to saturate it.

## Mitigation Strategies

*   **Monitor the Load Generator:** Run resource monitoring (CPU, network, memory) on the load generation machines to verify they are not saturated.
*   **Scale Horizontally:** Launch multiple parallel generator processes across separate client machines to distribute the load generation work.
*   **Use Asynchronous Clients:** Employ non-blocking, asynchronous load testing tools (e.g., `wrk`, `vegeta`) that can generate high concurrency without requiring one thread per connection.
*   **Validate Scale:** Verify that doubling the number of load generator instances roughly doubles the throughput (until the target system itself starts to saturate).
