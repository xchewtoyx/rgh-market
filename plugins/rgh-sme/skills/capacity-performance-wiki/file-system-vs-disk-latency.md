---
type: concept
title: File System vs. Disk Latency
description: The distinction between latency experienced at the application file system layer (VFS) and latency at the physical block device, decoupled by the page cache.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 8"
---

A fundamental distinction in systems performance analysis is the difference between latency measured at the file system interface and latency measured at the underlying physical block device.

## Defining the Latencies

*   **File System Latency:** The time elapsed from when an application thread invokes a VFS file system call (e.g., `read()`, `write()`, `stat()`, `fsync()`) to when the system call returns. This represents the direct performance experienced by the application code.
*   **Disk Latency (Block I/O Latency):** The time elapsed from when the operating system block device driver dispatches an I/O request to the physical storage controller to when the hardware confirms completion. This represents physical hardware performance.

## The Decoupling Effect of the Page Cache

File system latency and disk latency are decoupled by the operating system's file page cache. 

If the **Page Cache Hit Ratio** is high:
*   An application's read request finds the data in RAM.
*   The VFS returns immediately.
*   **Result:** Average file system latency is measured in **microseconds**, even if the underlying physical disk is highly saturated or slow (e.g., executing writes at **10 milliseconds**).

If the **Page Cache Hit Ratio** drops (e.g., due to memory pressure or random access patterns):
*   Read requests miss the cache and fall through to physical disk reads.
*   The application thread is put into a blocked state (`TASK_UNINTERRUPTIBLE`) waiting for the hardware.
*   **Result:** Average file system latency rises toward physical disk latency (milliseconds), degrading application throughput.

```
[Application]
      |
  VFS Read/Write  <=== FILE SYSTEM LATENCY (Microseconds on Cache Hit)
      v
+------------+       Cache Hit (99%)
| Page Cache |-----------------------> Return Data
+------------+
      |
  Cache Miss (1%)
      v
+------------------+
| Block Device /   |<=== DISK I/O LATENCY (Milliseconds)
| Physical Disk    |
+------------------+
```

## Diagnostic Workflow

Relying solely on disk I/O metrics (like `%util` or average wait time from `iostat`) is a common pitfall. A disk can show 100% utilization, but if the application's active working set fits entirely in the page cache, the application will experience zero performance impact.

To diagnose storage-related performance issues systematically:

1.  **Measure File System Latency First:** Use tools like `ext4dist` or `xfsdist` (BCC/bpftrace) to check if the application's file system calls are actually slow.
2.  **Measure Cache Hit Ratios:** Use `cachestat` to check if a low page cache hit ratio is forcing requests down to the disk.
3.  **Measure Block Device Latency:** Use `biolatency` or `iostat -xz` to determine if the storage hardware itself is saturated or malfunctioning.

A layer above this diagnostic chain, a database's own block size introduces the same granularity effect one level higher — see [database block size misalignment](database-block-size-misalignment.md) for how a small logical row read still costs a full block, and how misalignment against the filesystem/RAID stripe size beneath it adds further avoidable I/O.
