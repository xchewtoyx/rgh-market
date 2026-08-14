---
type: concept
title: The USE Method
description: A resource-centric performance methodology that checks utilization, saturation, and errors for every hardware and system resource.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 2"
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 9"
---

The **USE Method** (Utilization, Saturation, and Errors) is a resource-centric, bottom-up methodology designed for the rapid triage of system bottlenecks and performance issues. It is applied early in an investigation to systematically identify or rule out hardware and software resource limits.

Locating a resource-level bottleneck this way is the first half of the [measure before optimizing](measure-before-optimizing.md) discipline — the USE Method finds *where* to look; a change should still be measured before and after to confirm it actually helped.

## The Core Rule

For **every physical and logical resource** in the system, check three metrics:

1.  **Utilization:** The proportion of time the resource was busy executing work, or the proportion of total capacity consumed over a specified interval.
2.  **Saturation:** The degree to which extra requested work cannot be serviced immediately and is queued waiting for execution.
3.  **Errors:** The rate of error events occurring on the resource.

## Resource Directory

A resource can be a physical component (e.g., CPU, RAM, storage, network interface) or a logical component (e.g., kernel locks, file descriptors, [connection pools](connection-pool-saturation.md)).

### Common Examples of USE Metrics

| Resource | Utilization Metric | Saturation Metric | Errors Metric |
| :--- | :--- | :--- | :--- |
| **CPU** | % CPU busy time | Scheduler run queue length or wait time | CPU-specific hardware errors (e.g., machine check exceptions) |
| **Memory** | % Physical memory used | Page scan rate, swap-in/out rate, OOM killer invocations | ECC memory faults |
| **Storage Disk** | % Time disk is busy (e.g., `%util` in `iostat`) | Disk queue length or average wait time | I/O errors, controller resets |
| **Network Interface** | % Bandwidth used relative to interface speed | Dropped packets, buffer queue drops | Transmission/receive errors, collision rate |
| **Logical Locks** | % Time lock is held | Threads waiting for lock acquisition | Lock acquisition timeouts, deadlock detections |

## Context and Flow

The USE Method is a **resource-oriented** approach. It is highly effective for identifying the physical bottlenecks that constrain application performance. However, because it does not measure application request rates or end-user latency, it should be paired with a workload-oriented methodology like the [RED Method](red-method.md) to understand overall system health from a [workload perspective](resource-vs-workload-perspectives.md).

## Applying USE on Linux: Tooling Reference

Turning the three USE questions into a checklist requires knowing which command exposes each metric for each resource. On Linux:

| Resource | Utilization | Saturation | Errors |
| :--- | :--- | :--- | :--- |
| CPU (system) | `mpstat -P ALL 1` (%usr, %sys) | `vmstat 1` (`r` column vs. [system load average](system-load-average.md)) | `dmesg` (machine check exceptions) |
| Memory | `free -m` ([free vs. available](free-vs-available-memory.md)) | `sar -B 1` (majflt/s), `sar -W 1` (si/so swap activity), [direct reclaim stalls](direct-reclaim-stalls.md) | `dmesg` (ECC corrections, OOM killer) |
| Storage device I/O | `iostat -xz 1` (`%util`) | `iostat -xz 1` (`aqu-sz` queue depth) | `/sys/block/*/stat`, `dmesg` |
| Storage capacity | `df -h` (bytes used) | `df -i` ([inode exhaustion](inode-exhaustion.md)) | file system errors in `dmesg` |
| Network interface | `sar -n DEV 1` (throughput vs. link speed) | `netstat -s`, `ethtool -S` (buffer/queue drops) | interface error and drop counters |
| [NUMA interconnect](non-uniform-memory-access.md) | `numactl --hardware` | interconnect stall/bandwidth counters | hardware bus error counters |

Each row is a starting point, not a full diagnosis — follow the linked notes above for how to interpret saturation once a candidate resource is flagged.

The same saturation pattern recurs one layer up the stack, inside application-level resources the OS-level tools above don't see directly: a query engine's per-operator memory allocation is itself a resource with a utilization/saturation story, and exceeding it produces [query execution spilling](query-execution-spilling.md) rather than an OS-visible signal.

## Utilization Can Mislead for Concurrent Devices

The USE Method's Utilization check assumes a resource that does one thing at a time, so "100% busy" cleanly implies no spare capacity. This assumption breaks for resources with **internal concurrency** — notably storage devices. A RAID controller or SSD reporting `%util` (percent of time the device had at least one outstanding request) at 100% may still have room to accept more concurrent requests, because the metric only tracks whether the device was busy, not how many operations it was processing in parallel.

For these devices, `%util` alone cannot confirm saturation. Cross-check against queue depth (`aqu-sz` in `iostat -xz`) or a request-latency histogram (`biolatency`): a rising queue depth or a widening latency tail under a constant `%util` of 100% is the real saturation signal, not `%util` itself. See [RAID write penalty](raid-write-penalty.md) for how physical I/O concurrency is shaped by RAID level, and [file system vs. disk latency](file-system-vs-disk-latency.md) for why disk-layer metrics alone can also miss application-visible latency.

## Utilization Can Mislead for Variable-Efficiency Resources

A second, distinct way utilization misleads applies even to resources with *no* internal-concurrency confound — a single processor that genuinely was doing something in every sampled interval. Tools like `nvidia-smi`'s "GPU utilization" report the percentage of time the device was *actively processing something at all*, not how efficiently. A processor capable of 100 operations/second doing just 1 operation/second the entire time still reports 100% utilization under this time-based definition — it was never idle, but it was nowhere near its achievable throughput.

The fix is a [*throughput-based* utilization measure](utilization-vs-efficiency.md): achieved rate of work divided by the resource's theoretical peak rate, rather than percentage of time busy. In accelerator workloads this shows up as **MFU (Model FLOP/s Utilization)** — observed compute throughput over theoretical peak FLOP/s — and **MBU (Model Bandwidth Utilization)** — observed memory-bandwidth consumption over theoretical peak bandwidth. Both can be low even while the time-based utilization metric reads 100%, and which one is the relevant one to watch depends on whether the workload is [compute-bound or memory-bandwidth-bound](compute-bound-vs-memory-bandwidth-bound.md) — the same underlying lesson [instructions per cycle](instructions-per-cycle.md) applies one level down, at CPU clock-cycle granularity, to reveal whether "busy" cycles are doing useful compute or stalled waiting on memory.

As with any utilization number, the goal is never to maximize it for its own sake — a higher throughput-based utilization means nothing if it's bought at higher cost or higher latency than the workload actually needs. Its value is in tracking efficiency trends on the same hardware and workload over time, and in catching a workload that's much further from its hardware's real ceiling than a time-based "100% busy" reading would suggest.
