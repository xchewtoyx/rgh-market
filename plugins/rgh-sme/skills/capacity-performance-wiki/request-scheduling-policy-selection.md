---
type: concept
title: Request Scheduling Policy Selection
description: Whenever multiple requests contend for one resource, some scheduling policy decides serving order — the choice trades off latency, fairness, and predictability, and no single policy optimizes all of them at once.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Len Bass, Paul Clements, Rick Kazman), ch. 9"
---

Any time work queues for a contended resource, something decides which queued item runs next. This decision has two parts — assigning each request a priority, and dispatching among priorities — and the choice of policy directly shapes latency distribution and predictability under load, independent of the resource's raw capacity. Competing goals a scheduler might optimize for (optimal resource use, honoring request importance, minimizing latency, maximizing throughput, preventing starvation) are often mutually exclusive, so picking a policy is a genuine [trade-off](throughput-vs-latency-tradeoff.md), not a search for a universally-best answer.

## Common Policies

*   **FIFO** — serve requests in arrival order, treating all requests as equal priority. Simple, but a single slow request blocks every equally-important request behind it; only appropriate when requests genuinely carry equal priority and similar cost.
*   **Fixed-priority scheduling** — assign each request source a static priority. Gives strong service to high-priority work, but a continuous stream of high-priority requests can starve a lower-priority (but still important) request indefinitely. Three ways to derive the static priority: **semantic importance** (priority set from a domain characteristic, e.g. [priority tiers](request-priority-shedding.md)); **deadline monotonic** (shorter-deadline request streams get higher priority — used for mixed-priority real-time streams); **rate monotonic** (a deadline-monotonic special case for periodic streams: shorter period implies higher priority; the form most operating system schedulers support directly).
*   **Dynamic priority scheduling** — priority is recomputed as conditions change rather than fixed upfront: **round-robin** (cycle through requests in order, giving each a bounded turn); **earliest-deadline-first** (serve whichever pending request has the nearest deadline); **least-slack-first** (serve whichever request has the least slack, where slack = time remaining until deadline minus remaining work). On a single processor with preemptible work, earliest-deadline-first and least-slack-first are both provably *optimal*: if any ordering exists that meets every deadline, one of these two will find it.
*   **Static scheduling** — a cyclic-executive style schedule fixes preemption points and dispatch order entirely offline. Eliminates runtime scheduling overhead but only works when the workload is known and stable enough to schedule in advance.

## Applying This to Capacity Work

The scheduling policy is a lever independent of raw resource capacity: it doesn't change how much work a resource can do, only which requests get served first when demand exceeds supply. This makes it a capacity-planning decision, not just an implementation detail — for example:

*   FIFO under sustained overload produces the queueing latency blow-up described by the [M/M/1 queue model](mm1-queue-model.md) uniformly across all requests; fixed or dynamic priority scheduling instead concentrates that latency onto the requests deliberately chosen to absorb it.
*   [LIFO vs. FIFO queueing under overload](lifo-vs-fifo-queueing-under-overload.md) is itself a specific instance of this same dispatching choice, evaluated for the case where discarding old requests is preferable to serving them late.
*   [Request priority shedding](request-priority-shedding.md) is fixed-priority scheduling pushed to its extreme: instead of merely deprioritizing low-tier requests, it rejects them outright once resource pressure crosses a threshold.
