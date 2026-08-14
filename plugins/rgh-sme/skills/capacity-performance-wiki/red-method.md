---
type: concept
title: The RED Method
description: A workload-centric performance methodology focused on monitoring request rates, error rates, and request duration for service endpoints.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 2"
---

The **RED Method** is a workload-centric, top-down performance methodology designed specifically for monitoring microservices, distributed applications, and API endpoints. Unlike resource-focused approaches, it measures system health based on the client request flow.

## The Core Metrics

For **every service or endpoint**, monitor three key metrics:

1.  **Requests:** The rate of incoming requests to the service (e.g., requests per second). This measures the workload volume.
2.  **Errors:** The rate or percentage of requests that fail (e.g., HTTP 5xx responses, failed RPCs, database errors).
3.  **Duration:** The distribution of time taken for requests to complete (latency). Rather than simple averages, this is typically analyzed using [percentiles](latency-percentiles-vs-mean.md) (e.g., p95, p99) to capture tail latency behavior.

## Application and Contrast

The RED Method aligns with the [workload perspective](resource-vs-workload-perspectives.md) of performance analysis, measuring the direct user experience of a service (how fast is it and is it failing?). 

It contrasts with the [USE Method](use-method.md), which is resource-oriented:
*   **USE Method** is best for hardware and OS infrastructure (e.g., "Is CPU saturated?").
*   **RED Method** is best for application layer APIs and microservices (e.g., "Are users getting slow database queries?").

A robust capacity and performance strategy uses both: RED for high-level monitoring and alerting on client-facing issues, and USE for lower-level diagnostics to find the resource limitations causing those issues.
