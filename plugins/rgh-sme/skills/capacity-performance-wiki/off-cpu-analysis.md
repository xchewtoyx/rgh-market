---
type: concept
title: Off-CPU Analysis
description: A performance analysis methodology that measures the duration and stack traces of threads when they are blocked and not executing on a CPU.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 2"
---

**Off-CPU Analysis** is a performance analysis methodology focused on measuring the time threads spend in a blocked, waiting, or sleeping state, rather than actively executing on a CPU core.

## The Core Concept

A thread's elapsed execution or response time can be split into two mutually exclusive states:

$$\text{Total Elapsed Time} = \text{On-CPU Time} + \text{Off-CPU Time}$$

*   **On-CPU Time:** The time a thread is scheduled on a CPU core executing instructions. This is what traditional CPU profilers (like `perf`, Java profilers, or CPU flame graphs) measure.
*   **Off-CPU Time:** The time a thread is blocked, waiting for an event (such as disk I/O, network packets, lock acquisition, or page faults), or waiting in the scheduler's run queue to be run.

## Why Off-CPU Analysis is Crucial

If a system or application is exhibiting high latency or low throughput, but CPU utilization is low, traditional CPU profiling will fail to expose the bottleneck. This is because the threads are spent waiting off-CPU. Relying solely on CPU profiling in this scenario is a classic example of the **Streetlight Anti-Methodology** (looking only where the tools are familiar).

Common causes of high Off-CPU time include:
1.  **I/O Latency:** Waiting for synchronous read/write operations to complete on storage devices.
2.  **Network Wait:** Waiting for responses from database queries, remote RPC calls, or cache lookups.
3.  **Lock Contention:** Threads blocking while waiting to acquire a mutex, semaphore, or database lock.
4.  **Scheduler Latency:** A thread is runnable but must wait in the scheduler's run queue because all CPU cores are busy (this is a form of CPU saturation).

## Methodology: How to Measure Off-CPU Time

Off-CPU analysis is typically performed using [dynamic tracing tools](instrumentation-overhead-and-observer-effect.md) (such as ftrace, BCC, or `bpftrace` on Linux) to instrument scheduler state transitions:

1.  **Trace Scheduler Switches:** Instrument the scheduler's context switch event (e.g., `sched_switch`).
2.  **Record Timestamp and Stack:** When a thread transitions from a running state to a blocked state, record the current timestamp and its stack trace.
3.  **Calculate Duration:** When the thread is scheduled back onto a CPU, calculate the elapsed time since it was blocked.
4.  **Visualize with Flame Graphs:** Aggregate these stack traces and durations to generate an **Off-CPU Flame Graph**, where the width of the bars represents the total blocked duration rather than CPU cycles consumed. This directly reveals which code paths are responsible for the application's waiting time.
