---
type: concept
title: Latency Percentiles vs. Mean
description: Why the arithmetic mean of a response-time distribution hides the outlier behavior that matters for user experience and SLAs, and why percentiles are used instead.
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 1"
---

The **arithmetic mean** of a set of response times is a poor summary statistic for latency, because it is dominated by the bulk of fast requests and masks how bad the slow outliers are. Two systems can have identical mean latency while one has a much worse experience for a meaningful fraction of users.

## Percentiles

Latency is instead described using **percentiles**, which state the response-time threshold below which a given fraction of requests complete:

*   **Median (p50):** half of all requests are faster than this value, half slower. Represents the "typical" request.
*   **Tail percentiles (p95, p99, p999):** the response-time threshold for the slowest 5%, 1%, and 0.1% of requests, respectively.

Tail percentiles matter disproportionately because the users who hit them are often not random: a user with an unusually large amount of data, or making an unusually complex query, tends to land in the slow tail on *every* request — meaning the "outlier" experience is actually a consistent, repeated experience for a specific (sometimes especially valuable) subset of users.

## Why the Tail Is Worth Optimizing

Optimizing tail latency has a direct, measurable business cost trade-off: pushing further into the tail (e.g., from p99 to p999) typically costs disproportionately more engineering and infrastructure effort per unit of latency improvement, because the causes of extreme outliers are increasingly rare and varied. Organizations therefore pick a percentile target that reflects where the marginal cost of further optimization stops being justified by the marginal benefit, rather than chasing p100.

## Consequences for Engineering Practice

*   **SLAs and SLOs should be defined on percentiles, not means** — a mean-based target can be met while a meaningful fraction of requests are unacceptably slow.
*   **Percentiles cannot be averaged.** Combining latency measurements from multiple servers, or multiple time windows, by averaging their percentiles produces a statistically meaningless number. See [percentile aggregation across nodes](percentile-aggregation-across-nodes.md) for the correct approach.
*   **Percentiles need enough samples to mean anything.** A high percentile computed from a low-traffic window is statistically unstable — see [percentile sample size requirement](percentile-sample-size-requirement.md).
*   **Fan-out amplifies the tail.** A request that depends on several backend calls in parallel is only as fast as the slowest one — see [tail latency amplification](tail-latency-amplification.md).
*   **Load tests must measure the tail correctly.** A generator that waits for each response before issuing the next request systematically undercounts the tail — see [coordinated omission](coordinated-omission.md).
