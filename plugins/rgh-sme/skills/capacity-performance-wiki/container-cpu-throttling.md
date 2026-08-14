---
type: concept
title: Container CPU Throttling
description: How standard OS container CPU limit quotas (CFS quotas) throttle multi-threaded applications, causing severe latency spikes even when average CPU utilization remains low.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 6"
---

In containerized environments (such as Kubernetes or Docker), CPU limits are enforced by the Linux kernel using the Completely Fair Scheduler (CFS) quota mechanism. While intended to prevent resource hogging, this quota mechanism often introduces severe **container CPU throttling**, leading to unexpected latency spikes for multi-threaded applications.

## How CFS Quota Works

CFS quota throttling operates over a fixed time window, defined by two kernel control group (`cgroup`) parameters:

*   **`cpu.cfs_period_us`:** The period window, typically set to $100,000 \mu\text{s}$ ($100 \text{ ms}$).
*   **`cpu.cfs_quota_us`:** The total allowed CPU execution time (across all threads) within that period.

For example, if a container is assigned a Kubernetes CPU limit of `2.0`, the kernel sets `cpu.cfs_quota_us = 200,000` ($200 \text{ ms}$) and `cpu.cfs_period_us = 100,000` ($100 \text{ ms}$).

## The Multi-Threaded Throttling Failure Mode

If an application is multi-threaded, its threads run concurrently. The kernel sums the runtime of *all* threads against the quota.

1.  **Workload Burst:** A multi-threaded web server running 10 threads receives a batch of concurrent requests at the start of a $100 \text{ ms}$ period.
2.  **Rapid Quota Exhaustion:** All 10 threads run in parallel. In just $20 \text{ ms}$ of real-world time, they consume a total of $200 \text{ ms}$ of CPU quota ($10 \text{ threads} \times 20 \text{ ms} = 200 \text{ ms}$).
3.  **Throttling Phase:** Having exhausted the quota, the kernel scheduler immediately suspends (throttles) the container's processes for the remaining $80 \text{ ms}$ of the period.
4.  **Latency Spikes:** During this $80 \text{ ms}$ freeze, the application cannot process I/O, respond to health checks, or handle requests, causing severe latency spikes (tail latency).

### The Monitoring Illusion
Because traditional metrics tools (like Prometheus `node_exporter` or `kubectl top`) sample CPU utilization over long windows (e.g., 10 seconds or 1 minute), they average out this behavior. The system might report a comfortable 20% average CPU utilization, hiding the fact that the application was completely frozen for 80% of every 100 ms interval.

```
Time (100ms period)
|==== Run (20ms) ====|XXXXXXXXXXXXXXXX Throttled (80ms) XXXXXXXXXXXXXXXX|
^                     ^
Quota Exhausted       Period Resets (Quota Refilled)
```

## Mitigation and Tuning Strategies

*   **Size Thread Pools to CPU Limits:** Configure application thread pools to match the assigned CPU limit (e.g., if CPU limit is 2, set thread pools to 2 workers). This prevents the application from executing more parallel work than its quota can sustain over a short window.
*   **Use CFS Bandwidth Burst:** Modern Linux kernels (5.14+) support CFS burst (`cpu.cfs_burst_us`). This allows containers to accumulate unused CPU quota from quiet periods and use it to absorb spikes in active periods without triggering throttling.
*   **Remove Limits (Use CPU Requests Only):** In Kubernetes, configure containers with CPU *requests* (which map to `cpu.shares` and guarantee CPU cycles during contention) but omit CPU *limits*. This allows containers to burst onto idle host CPU cycles without being artificially throttled.
*   **Monitor Throttling Directly:** Monitor the cgroup metrics directly rather than raw CPU utilization. Track `/sys/fs/cgroup/cpu/cpu.stat` (specifically `nr_throttled` and `throttled_time`) to detect the volume of throttled cycles.
