---
type: concept
title: The M/M/1 Queue Model
description: A basic queueing model demonstrating that response times increase non-linearly and asymptotically as resource utilization approaches 100%.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 2"
  - title: "The DevOps Handbook"
    resource: "The DevOps Handbook (Gene Kim, Jez Humble, Patrick Debois, John Willis, Nicole Forsgren), Appendix 4"
---

The **M/M/1 queue model** is a simple mathematical model of a queueing system used to analyze resource contention and latency. It represents a system with a single server, where requests arrive according to a Poisson process (random, independent intervals) and service times are exponentially distributed.

## Response Time Formula

The average response time $r$ (total time spent in the system, including queueing wait time and active service time) is calculated as:

$$r = \frac{s}{1 - U}$$

Where:
*   **$s$**: The average service time (time spent actively executing on the server).
*   **$U$**: The utilization of the server ($0 \le U < 1$), defined by the [Utilization Law](utilization-law.md) as $U = \lambda s$.

## The Non-Linear Relationship

The formula highlights a critical, non-linear relationship between resource utilization and latency:

*   At **$0\%$ utilization** ($U = 0$): $r = s$. There is no queueing, and response time equals service time.
*   At **$50\%$ utilization** ($U = 0.5$): $r = 2s$. A request spends, on average, half its time waiting in the queue and half its time being serviced.
*   At **$80\%$ utilization** ($U = 0.8$): $r = 5s$. Queueing delay is four times the service time.
*   At **$90\%$ utilization** ($U = 0.9$): $r = 10s$. Queueing delay is nine times the service time.
*   As utilization approaches **$100\%$** ($U \to 1$): $r \to \infty$. Response time increases asymptotically.

```
Response Time (r/s)
   ^
   |                                  /
10 |                                 / 
   |                                /
 5 |                       _..---''
   |              _..---''
 1 |  ____..---''
   +------------------------------------> Utilization (U)
     0%          50%       80%  90%  100%
```

## Takeaways for Capacity Planning and Performance

1.  **Utilization Targets:** Because latency degrades rapidly as utilization climbs, systems are rarely designed to run at 100% utilization. Common utilization targets (or "headroom" thresholds) are set at 70% to 80% to prevent queueing latency from dominating the end-user experience.
2.  **Sensitivity to Spikes:** Near the "knee" of the utilization-latency curve (typically around 70-80% utilization), even small, temporary increases in workload volume ($\lambda$) will cause disproportionately large spikes in response time.
3.  **Multi-Server Systems (M/M/m):** While modern multi-core systems (modeled by M/M/m queues where $m > 1$ parallel servers) can absorb queueing spikes more efficiently than single-server systems at moderate utilization, they still exhibit the same asymptotic latency behavior as aggregate utilization approaches 100%.
4.  **Load Distribution Across Servers:** The M/M/m benefit only holds if load is actually spread evenly across the $m$ servers. How a pool of backends gets assigned requests in the first place — see [load balancing algorithm capacity awareness](load-balancing-algorithm-capacity-awareness.md) — determines whether the pool behaves like a well-balanced M/M/m system or like several independent M/M/1 queues each running at a different, unevenly loaded utilization.

## Compounding Across a Serial Chain of Queueing Stages

The same per-stage wait-time-to-service-time ratio ($U/(1-U)$) compounds multiplicatively when a request must pass through several queueing stages in series, each run at similarly high utilization — this is the same phenomenon that shows up in process/handoff chains, not just hardware resource queues. A worked illustration: a task requiring only 30 minutes of actual work must pass through 7 sequential handoffs (e.g., separate teams each responsible for one step), and each handoff point is a resource running at 90% utilization. Each individual handoff contributes a wait of $s \times \frac{U}{1-U} = s \times 9$ — nine times its own service time — before the step even starts. Summed across all 7 handoffs, the queueing delay alone reaches many hours, while the actual value-adding work stays fixed at 30 minutes: the fraction of total lead time that is real work can fall to a fraction of one percent. This is why reducing the *number* of serial handoffs a request passes through is often a bigger lead-time lever than trying to speed up any single stage — each additional 90%-utilized stage in the chain multiplies total wait time, not just adds to it.
