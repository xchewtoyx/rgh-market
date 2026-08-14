---
type: concept
title: Resource vs. Workload Perspectives
description: Two complementary analytical approaches in systems performance that focus either on system components (resources) or client requests (workloads).
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 1"
---

Performance analysis can be approached from two distinct perspectives: bottom-up (focusing on system resources) and top-down (focusing on the workload).

## Resource Perspective
The **resource perspective** focuses on the hardware and software components of the system, such as CPUs, memory, storage devices, network interfaces, and kernel lock structures.

*   **Primary Question:** "Is a specific resource bottlenecked, saturated, or failing?"
*   **Key Metrics:**
    *   **Utilization:** The percentage of time a resource is busy, or the fraction of its total capacity in use.
    *   **Saturation:** The degree to which a resource has queued work or waiting processes (e.g., CPU run queue length, disk queue depth).
    *   **Errors:** The rate of physical or logical error events (e.g., network packet drops, disk read retries).
    *   **Throughput:** The rate of operations performed by the resource (e.g., disk I/O operations per second, network bytes per second).

## Workload Perspective
The **workload perspective** focuses on the requests or operations submitted to the system by clients or applications, such as HTTP requests, SQL database queries, RPC calls, or background batch transactions.

*   **Primary Question:** "How fast are client requests being processed, and where is the time being spent?"
*   **Key Metrics:**
    *   **Throughput (Request Rate):** The rate of requests processed by the application (e.g., requests per second, transactions per second).
    *   **Latency (Response Time):** The duration from request submission to completion, including queueing and service time.
    *   **Error Rate:** The percentage or count of requests that failed to complete successfully (e.g., HTTP 5xx responses).

## Complementary Nature
While workload metrics (especially latency) directly reflect end-user experience, resource metrics are essential for identifying the underlying bottlenecks that cause performance degradation. For example, a workload-perspective analysis might reveal high query latency, but a resource-perspective analysis is needed to identify that the delay is caused by storage volume saturation.
