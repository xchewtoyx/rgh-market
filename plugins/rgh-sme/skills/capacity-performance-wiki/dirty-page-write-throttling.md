---
type: concept
title: Dirty Page Write Throttling
description: A kernel write-throttling mechanism that blocks application write operations synchronously when dirty pages in the page cache exceed memory thresholds.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 8"
---

In Linux, standard file writes (`write()`) are asynchronous by default: they write to the file system page cache, mark the memory pages as **dirty**, and return immediately. However, if the rate of writes exceeds the physical storage device's write throughput, the kernel triggers **dirty page write throttling**, blocking application writes synchronously.

## The Flushing and Throttling Thresholds

The kernel controls dirty page management using two system-wide memory thresholds (configured via `sysctl`):

### 1. Background Writeback Threshold
Configured by `vm.dirty_background_ratio` (percentage of total memory) or `vm.dirty_background_bytes`.
*   **Behavior:** When dirty pages in the page cache reach this threshold, the kernel wakes up background writeback threads (e.g., `kworker` or `flush` daemons) to write dirty pages to disk asynchronously.
*   **Impact:** Zero latency impact on applications; writes continue to return immediately.

### 2. Synchronous Throttling Threshold
Configured by `vm.dirty_ratio` (percentage of total memory) or `vm.dirty_bytes`.
*   **Behavior:** If the write rate continues to outpace background disk write throughput, dirty pages will accumulate until they hit this threshold. At this point, the kernel enters an emergency throttling state.
*   **Impact:** Any thread attempting a write system call is suspended and forced to synchronously flush dirty pages to disk before the system call can return. 

```
Dirty Page Ratio (Memory %)
|   
|   [100%]
|   
|==== [vm.dirty_ratio] ====> SYNCHRONOUS THROTTLING (Writers Block)
|   
|==== [vm.dirty_background_ratio] ====> Asynchronous Background Writeback Starts
|   
+----------------------------> Time
```

## Performance and Capacity Consequences

*   **Latency Spikes:** Direct throttling turns a sub-microsecond in-memory write operation into a multi-millisecond disk write operation, creating sudden write latency spikes that disrupt databases, logs, and queue consumers.
*   **I/O serialization storms:** If a system has a large amount of RAM (e.g., 256 GB) and `vm.dirty_ratio` is set to the default 20%, the system can accumulate 50 GB of dirty pages before throttling. When it finally hits the limit, the database may freeze for tens of seconds while the storage controller attempts to flush 50 GB of data to disk.

## Diagnostic Action

*   Verify current dirty page levels in `/proc/meminfo` (specifically `Dirty` and `Writeback` values).
*   Monitor page cache operations using the BCC/bpftrace `cachestat` tool to observe dirty page creation and writeback rates.

## Mitigations and Tuning

For write-heavy database or messaging systems:

*   **Lower `vm.dirty_background_ratio`:** Set this to a low value (e.g., `5` or `3`, or use `vm.dirty_background_bytes` to set it to a fixed small size like `104857600` [100 MB]). This starts background flushing immediately, smoothing out I/O demand on the storage controller.
*   **Cap `vm.dirty_ratio`:** Set this to a conservative value (e.g., `10` or `15`, or use `vm.dirty_bytes` to set a fixed cap like `524288000` [500 MB]). Sizing this cap prevents the system from accumulating a massive backlog of dirty pages, avoiding long freeze times when throttling occurs.
*   **Application-Level Syncing:** Use asynchronous writes paired with deliberate, periodic `fsync()` or `fdatasync()` calls in the application layer to control *when* data is committed, rather than allowing the kernel to hit thresholds and throttle randomly.
