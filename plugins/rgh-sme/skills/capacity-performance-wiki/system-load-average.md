---
type: concept
title: System Load Average
description: A system metric representing the average number of runnable and uninterruptible tasks, which serves as a coarse measure of system demand.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 3"
---

The **system load average** is a standard system metric representing the average demand for CPU and disk resources over time. On Unix-like systems, it is traditionally displayed as three values representing the 1-minute, 5-minute, and 15-minute moving averages.

## Calculation and Linux Specifics

In classic Unix systems, the load average is the average number of threads in the scheduler run queue (tasks in the `TASK_RUNNING` state, either executing on a CPU or waiting for CPU time).

However, **Linux implements a unique modification**:
$$\text{Linux Load Average} = \text{Average of } (\text{Tasks in } TASK\_RUNNING + \text{Tasks in } TASK\_UNINTERRUPTIBLE)$$

*   `TASK_RUNNING`: Threads actively running or waiting in a CPU run queue.
*   `TASK_UNINTERRUPTIBLE`: Threads sleeping in kernel space, typically waiting for disk/block I/O (e.g., waiting for page cache read/write, page fault resolution) or kernel locks.

## Crucial Interpretation Pitfalls

1.  **Disk I/O Inflation:** Because Linux includes `TASK_UNINTERRUPTIBLE` tasks, the load average can spike due to disk I/O bottlenecks or storage saturation even if overall CPU utilization is very low. For example, a system with a single CPU and a stalled storage array can show a load average of 50 while CPU utilization remains near 0%.
2.  **Relative to Core Count:** A load average of "10" has completely different meanings depending on hardware capacity.
    *   On a **2-core** machine, a load of 10 indicates severe saturation (5x the CPU capacity).
    *   On a **64-core** machine, a load of 10 represents a largely idle system (only ~15% utilization).
3.  **Exponential Decay Lag:** The three load average values are exponentially decaying averages. They do not show instantaneous spikes or drop-offs. If a massive workload burst occurs and terminates quickly, the 1-minute load average will remain elevated for several minutes, lagging behind the actual system state.
4.  **No Saturation Details:** The load average is a coarse summary metric. It does not differentiate between CPU queueing, disk queueing, or lock contention, nor does it identify which specific processes are driving the load.

## Diagnostic Action

When load average is high, engineers must perform a secondary check using tools like `vmstat`, `iostat`, or `top` to determine the true driver of the load:
*   If **CPU utilization** is high, the load is driven by computation.
*   If **iowait** (CPU time spent waiting for I/O) is high or disk utilization (`%util`) is near 100%, the load is driven by storage device saturation.
