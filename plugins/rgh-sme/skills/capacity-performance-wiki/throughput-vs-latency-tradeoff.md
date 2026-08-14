---
type: concept
title: Throughput vs. Latency Trade-Off
description: The fundamental systems engineering trade-off where optimizing for throughput (rate of work) often increases latency (individual response time) and vice versa.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 2"
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 9"
---

The **throughput vs. latency trade-off** is a fundamental constraint in systems design and capacity engineering. Optimizing a system to maximize the total volume of work processed per unit of time (throughput) typically increases the response time of individual operations (latency), and vice versa.

## Understanding the Trade-Off

*   **Throughput-Optimized Systems:** Focus on [efficiency, resource utilization](utilization-vs-efficiency.md), and amortization of overhead. This is often achieved through **batching**, where multiple tasks are grouped and executed together (see [request batching for throughput](request-batching-for-throughput.md) for the mechanics of size/time-triggered batching over a network call). Batching reduces overhead (e.g., system calls, network headers, context switches, disk seeks), but it forces individual tasks to wait in queues while the batch is accumulated or processed, increasing latency.
*   **Latency-Optimized Systems:** Focus on responsiveness and immediate execution. This requires processing tasks as soon as they arrive, which limits queueing and waiting. However, executing tasks individually increases overhead and reduces overall efficiency, lowering the system's maximum sustainable throughput.

## Concrete Examples

| Subsystem | Throughput Optimization (High Latency) | Latency Optimization (Low Throughput) |
| :--- | :--- | :--- |
| **Networking** | **Nagle's Algorithm / TCP Buffering:** Wait to accumulate a full MSS of packet payload before sending, reducing TCP/IP header overhead. | **TCP_NODELAY:** Send packets immediately, even if they contain only a few bytes. Increases packet count and header overhead. |
| **Storage / DB** | **Group Commits / Delayed Flushing:** Batch write logs in memory and flush them to disk periodically to maximize sequential disk write throughput. | **Synchronous Writes:** Flush every write transaction immediately to disk for persistence and immediate completion confirmation. |
| **CPU Scheduling** | **Large Time Slices:** Allow threads to run longer before preemption, minimizing context-switching overhead. | **Small Time Slices / Real-time Scheduling:** Preempt running threads frequently to ensure new work is scheduled with minimal delay. |
| **JVM Garbage Collection** | **Parallel GC:** Pause application execution ("stop-the-world") to clean heap memory with maximum efficiency and high throughput. | **Concurrent/Low-Latency GC (e.g., ZGC):** Perform GC tasks concurrently with application threads, incurring CPU overhead but avoiding long pause times. |
| **Inference/Compute Serving** | **Batch APIs:** accumulate requests over a long window (hours) to run them at full hardware efficiency; commonly offered at roughly half the per-request cost of the equivalent online API, at the price of hours- rather than seconds-scale turnaround. | **Online APIs:** process each request as soon as it arrives to minimize response latency, at higher per-request compute cost since the hardware can't be packed as efficiently. |

## Capacity Planning Takeaways

When planning capacity, it is vital to define whether the primary constraint is a throughput target or a [latency budget](latency-first-unit-vs-per-unit-rate.md) — and, once a latency budget is chosen, whether raw throughput or [goodput](goodput-vs-throughput.md) (throughput that actually meets it) is the number being optimized:
1.  **Utilization Headroom:** As demonstrated by the [M/M/1 Queue Model](mm1-queue-model.md), keeping resource utilization low guarantees low latency but requires overprovisioning (lower throughput relative to hardware capacity).
2.  **SLA/SLO Alignment:** System tuning parameters (e.g., batch sizes, queue depths, buffer limits) must be calibrated to strike the correct balance dictated by the service level objectives.
