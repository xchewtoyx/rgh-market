---
type: concept
title: The Utilization Law
description: A fundamental queueing theory law relating resource utilization to throughput and service time.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 2"
---

The **Utilization Law** is a fundamental relationship in queueing theory and capacity planning that defines how resource utilization relates to request throughput and the service time of individual requests.

## The Equation

$$U = \lambda B$$

Where:
*   **$U$**: The utilization of the resource (expressed as a fraction $0 \le U \le 1$ or a percentage $0\% \le U \le 100\%$).
*   **$\lambda$**: The system throughput (the rate at which requests are processed by the resource, equal to arrival rate in a stable system).
*   **$B$**: The average service time of a request at that resource (the time the resource is actively processing the request, *excluding* any queueing or wait time).

## Key Distinction: Service Time vs. Response Time

It is critical to distinguish between service time ($B$) and overall response/residence time ($W$):
*   **Service Time ($B$):** Time spent actively using the resource.
*   **Response Time ($W$):** Total elapsed time from request arrival to completion, encompassing wait time in a queue plus service time ($W = \text{Wait Time} + B$).

The Utilization Law uses *service time* ($B$), not response time ($W$).

## Application in Capacity Planning

1.  **Calculating Theoretical Maximum Throughput:**
    The absolute maximum throughput $\lambda_{max}$ a single resource can sustain occurs when its utilization reaches $100\%$ ($U = 1$):
    $$\lambda_{max} = \frac{1}{B}$$
    For example, if a single-threaded CPU task takes $2.5 \text{ ms}$ of CPU service time ($B = 0.0025 \text{ s}$) to process a database query, the maximum throughput that CPU core can support is:
    $$\lambda_{max} = \frac{1}{0.0025} = 400 \text{ queries/sec}$$

2.  **Sizing Resource Needs:**
    If a system must support a target throughput of $\lambda = 600 \text{ requests/sec}$ and each request requires $1.5 \text{ ms}$ of service time ($B = 0.0015 \text{ s}$), the total required capacity (in terms of number of parallel resource units, such as CPU cores, $m$) to keep average utilization at a target $U_{target} = 60\%$ can be calculated:
    $$\text{Total Utilization } U_{total} = \lambda B = 600 \times 0.0015 = 0.9 \text{ (90% of a single core)}$$
    $$\text{Cores Needed } m = \frac{U_{total}}{U_{target}} = \frac{0.9}{0.6} = 1.5 \text{ cores}$$
    Thus, a minimum of 2 cores is required.

3.  **Backing Out an Otherwise-Unmeasurable Service Time:**
    Per-request service time is often the hardest quantity in this law to measure directly — many systems expose utilization and throughput (both easy to sample: `vmstat`-style utilization counters, request-rate counters) but have no built-in way to time a single request's actual resource-holding time in isolation. Since the law only has three variables, the two easy-to-measure ones pin down the third: $B = U/\lambda$. For example, an HTTP server showing 40% CPU utilization while serving 200 requests/sec implies an average per-request CPU service time of $B = 0.40/200 = 2\text{ ms}$, without ever having instrumented an individual request's CPU time directly.

    This derived service time is exactly the input [fitting the Universal Scalability Law to data](fitting-universal-scalability-law-to-data.md) and other queueing-theoretic capacity models need, and it doubles as a sanity check: if a derived $B$ swings wildly between otherwise-similar measurement windows, that's a signal the utilization or throughput measurement itself is unreliable, not that per-request service time is actually volatile.
