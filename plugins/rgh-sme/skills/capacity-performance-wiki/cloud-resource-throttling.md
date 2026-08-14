---
type: concept
title: Cloud Resource Throttling
description: How cloud providers enforce capacity limits on storage I/O and network bandwidth using token bucket credit models, leading to sudden performance drops.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 11"
---

In cloud environments, resource capacity is virtualized and metered. Cloud providers strictly enforce limits on storage I/O (IOPS and throughput) and network bandwidth using a **token bucket** (or credit-based) algorithm. Failing to plan for these limits leads to sudden, severe performance degradation once burst reserves are exhausted.

## The Token Bucket Mechanism

To balance cost and performance, cloud providers allocate resource capacities using two tiers:

1.  **Baseline Rate:** The continuous, guaranteed performance level of the resource (e.g., $100 \text{ MB/s}$ network throughput or $3,000 \text{ IOPS}$ storage volume).
2.  **Burst Rate:** A temporary, higher performance level (e.g., $300 \text{ MB/s}$ or $6,000 \text{ IOPS}$) that the resource can sustain for short periods.

This is managed via a token bucket credit model:
*   **Token Accumulation:** When resource utilization is below the baseline rate, the system accumulates "credits" (tokens) in a virtual bucket, up to a maximum bucket capacity.
*   **Token Consumption:** During workload spikes, the application can burst above the baseline rate, consuming tokens from the bucket to sustain higher throughput.
*   **Exhaustion and Throttling:** If the workload remains elevated and consumes tokens faster than the baseline fill rate, the bucket eventually runs empty. Once depleted, the cloud provider **abruptly throttles** the resource down to its strict baseline rate.

```
Workload Demand (MB/s)
  ^
  |        /---- Burst (Consuming Credits)
  |       / 
  +------/================== [Baseline Limit]
  |                         \___ Throttled (Credits Exhausted)
  |   
  +-------------------------------------> Time
```

## Capacity Planning Risks

*   **The "Delayed Failure" Trap:** A common sizing pitfall occurs during short-term [load testing](capacity-test-types.md) rather than a longer soak run. An engineer runs a 30-minute load test, and the storage system performs perfectly because it is supported by a full bucket of burst credits. However, once deployed to production under sustained load, the credits run out after a few hours, the volume throttles, queueing latency spikes, and the application collapses.
*   **Write Latency Spikes:** Storage throttling (e.g., AWS EBS throttling) forces block I/O requests to queue, causing average disk read/write response times (`r_await`/`w_await` in `iostat`) to jump from microseconds to hundreds of milliseconds.

## Mitigation and Sizing Strategies

*   **Size for Sustained Load:** Do not size production storage or network capacity based on burst limits. Ensure the *baseline* provisioned capacity (e.g., provisioned IOPS on AWS gp3/io2 volumes or instance-level network limits) matches or exceeds the sustained peak demand of the application.
*   **Monitor Credit Balances:** Track cloud provider-specific metrics (such as AWS CloudWatch `BurstBalance` for gp2 volumes, or `CPUCreditBalance` for burstable EC2 instances). Configure automated alerts to trigger when the credit balance drops below 20%.
*   **Implement Application Rate Limiting:** If workloads are bursty, use application-level rate limiters or message queue consumer concurrency limits to smooth out execution spikes, preventing rapid token depletion.
