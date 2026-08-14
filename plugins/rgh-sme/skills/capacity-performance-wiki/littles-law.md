---
type: concept
title: Little's Law
description: A fundamental queueing theory law relating the average number of items in a system to the arrival rate and average time spent in the system.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 2"
---

**Little's Law** is a foundational theorem in queueing theory that describes the relationship between concurrency, throughput, and response time in a stable queueing system.

## The Equation

$$L = \lambda W$$

Where:
*   **$L$**: The average number of items (requests, processes, network packets) inside the system.
*   **$\lambda$**: The average arrival rate of items (which equals the throughput of the system when it is in a steady state).
*   **$W$**: The average time an item spends in the system (also known as residence time, latency, or response time).

## Key Characteristics and Assumptions

*   **Generality:** Little's Law is remarkably general. It is independent of the probability distribution of arrivals (e.g., Poisson or bursty), the distribution of service times (e.g., exponential or constant), and the scheduling/queueing discipline (e.g., First-In-First-Out, Last-In-First-Out, or Processor Sharing).
*   **System Boundary:** The system can be defined as any arbitrary boundary (e.g., a single queue, an entire application server, a database instance, or a network switch). The law holds as long as the system is stable (i.e., the arrival rate equals the departure rate over the long run, and the queue does not grow to infinity).

## Application in Capacity and Performance Engineering

1.  **Estimating Concurrency Requirements:**
    If an application server processes $1,000 \text{ requests/sec}$ ($\lambda$) and has an average response time of $100 \text{ ms}$ ($W = 0.1 \text{ s}$), the average number of concurrent requests being processed is:
    $$L = 1000 \times 0.1 = 100 \text{ concurrent requests}$$
    This calculation dictates resource provisioning, such as the required size of thread pools, database connection pools, and memory capacity (to hold the request context for 100 concurrent requests).

2.  **Validating Load Test Harnesses:**
    During performance testing, if a load generator is configured with a concurrency limit of 50 clients ($L = 50$) and the server achieves a throughput of 200 requests/second ($\lambda = 200$), the average latency *must* be:
    $$W = \frac{L}{\lambda} = \frac{50}{200} = 250 \text{ ms}$$
    If the monitored server-side latency is vastly different, it indicates a bottleneck in the network, queueing in the client, or a measurement error.

3.  **Detecting Saturation:**
    If server latency ($W$) spikes while the arrival rate ($\lambda$) remains constant, the number of items in the system ($L$) must increase proportionately, indicating that requests are accumulating in queues (saturation).

4.  **Catching a Throttled Load Generator Masquerading as a Server Limit:**
    A load test can show response time apparently flattening out to a constant value as configured client concurrency ($N_{init}$) keeps increasing — which looks like it violates Little's Law, since a stable system's response time shouldn't become independent of load like that. The real explanation is usually that the *client's* own thread pool is throttling: not every "initiated" client thread is actually active and generating load at any given moment. Cross-checking with Little's Law exposes this: compute $N_{active} = X \cdot R$ from the *measured* throughput and response time at each configured concurrency level, then compare it to $N_{init}$. If $N_{active}$ stops growing well before $N_{init}$ does, the gap ($N_{idle} = N_{init} - N_{active}$) is threads sitting idle in the client's pool rather than actually loading the server — the apparent plateau is an artifact of the test harness, not a property of the system under test. Treating load-test output as inherently trustworthy just because the rig was expensive or complex is a common mistake; a Little's Law cross-check like this is a cheap way to catch it before the result reaches a capacity plan.

5.  **Deliberately Bounding Concurrency:**
    Because $L$, $\lambda$, and $W$ are locked together, capping the concurrency $L$ a resource is allowed to work on at once is a direct lever on the system's queueing behavior — see [concurrency limiting as admission control](concurrency-limiting-as-admission-control.md) for why holding excess concurrency in a queue in front of a resource can raise that resource's own effective throughput compared to letting all offered concurrency reach it directly.
