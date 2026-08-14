---
type: concept
title: Direct Reclaim Stalls
description: A virtual memory failure mode where allocating threads block synchronously to free physical memory pages, causing severe latency spikes.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 7"
---

In Linux memory management, **direct reclaim** is a synchronous process where a thread requesting memory is forced to halt its execution and personally free up physical RAM pages before its allocation request can be satisfied. This introduces significant latency spikes into application execution.

## The Memory Watermark Mechanism

The Linux kernel manages physical memory allocation and reclamation using three watermarks: `min`, `low`, and `high` (configured dynamically based on the `/proc/sys/vm/min_free_kbytes` sysctl).

```
Physical Memory
+-----------------------+  (Total RAM)
|                       |
|   Free Pages          |
|                       |
+-----------------------+  high watermark  (kswapd stops)
|                       |
+-----------------------+  low watermark   (kswapd wakes up)
|   Emergency Pages     |
+-----------------------+  min watermark   (Direct Reclaim begins)
|   Reserved for Kernel |
+-----------------------+  0
```

1.  **Background Reclaim (`kswapd`):** When free memory drops below the `low` watermark, the background kernel daemon `kswapd` wakes up. It asynchronously reclaims memory (evicting clean, file-backed page cache pages and writing dirty anonymous pages to swap) until free memory rises back to the `high` watermark. This background process does not block application threads.
2.  **Direct Reclaim:** If the rate of memory allocation by applications exceeds `kswapd`'s reclamation throughput, or if free memory drops below the `min` watermark, the kernel enters an emergency state. Any thread attempting to allocate memory is suspended and forced to perform **direct reclaim**—synchronously searching for, freeing, or swapping out pages to service its own allocation request.

## Performance and Latency Impact

Direct reclaim stalls can turn a sub-microsecond memory allocation (`malloc`, `new`, or a minor page fault) into a multi-millisecond blocking operation. The thread must wait for file system synchronization, memory compaction, or slow disk writes (if swapping anonymous memory), causing substantial latency jitter.

## Diagnosis

*   **`sar -B`:** Monitor paging statistics. Check the `pgscand/s` metric (pages scanned directly) and `pgscank/s` (pages scanned by `kswapd`). If `pgscand/s` is greater than 0, the system is actively undergoing direct reclaim.
*   **BCC/bpftrace `drsnoop`:** Traces direct reclaim events in real-time, recording the duration of the reclaim stall and the name of the process that was blocked.

## Mitigation and Tuning

*   **Increase `vm.min_free_kbytes`:** Raising this value increases the distance between the watermarks, giving `kswapd` more headroom to begin reclaiming memory before the system hits the absolute threshold for direct reclaim. (Note: setting this value too high, e.g., $>10\%$ of system memory, can trigger early Out-of-Memory conditions).
*   **Reduce Memory Fragmentation:** Fragmentation prevents the allocation of contiguous pages (required for high-order allocations). Periodic memory compaction or pre-allocating static huge pages can reduce fragmentation-driven direct reclaim.
*   **Tune `vm.swappiness`:** Lowering swappiness (e.g., to `10`) tells the kernel to prefer reclaiming clean page cache pages rather than swapping out anonymous memory, reducing the likelihood of blocking I/O during reclaim.
