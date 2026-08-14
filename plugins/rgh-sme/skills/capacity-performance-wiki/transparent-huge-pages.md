---
type: concept
title: Transparent Huge Pages (THP)
description: How dynamic kernel allocation of 2MB memory pages (THP) can introduce severe latency jitter due to memory compaction and page allocation stalls.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 7"
---

**Transparent Huge Pages (THP)** is a Linux kernel feature that automatically and dynamically aggregates standard $4 \text{ KB}$ virtual memory pages into $2 \text{ MB}$ (or larger) **huge pages**. While designed to improve memory efficiency, THP frequently introduces severe tail latency spikes in database and runtime workloads.

## The Problem: TLB Misses vs. Compaction Stalls

Modern processors translate virtual to physical addresses using a hardware cache called the **Translation Lookaside Buffer (TLB)**. 
*   **TLB Miss Cost:** If an application (like a database or JVM heap) manages $128 \text{ GB}$ of RAM using standard $4 \text{ KB}$ pages, the page table contains over 33 million entries. This exhausts the TLB cache, causing frequent TLB misses that force the CPU to perform slow page table walks in DRAM.
*   **Huge Pages Solution:** Using $2 \text{ MB}$ huge pages reduces the number of page table entries by a factor of 500, drastically increasing TLB hit rates and improving CPU instruction efficiency.

### Why THP Fails Latency-Sensitive Systems

Unlike static huge pages, which are pre-allocated at boot time, THP attempts to allocate and collapse pages dynamically in the background via the kernel thread `khugepaged`. 

As system uptime increases, physical memory becomes fragmented. When an application requests memory, or when `khugepaged` attempts to promote pages:

1.  **Allocation Failure:** The kernel cannot find a contiguous $2 \text{ MB}$ block of physical RAM.
2.  **Memory Compaction:** The kernel must execute a synchronous compaction routine, migrating allocated $4 \text{ KB}$ pages around in physical RAM to consolidate free space into a contiguous $2 \text{ MB}$ block.
3.  **Compaction Stalls:** If memory is under pressure or heavily fragmented, the allocating thread blocks (stalls) waiting for compaction to complete. This turns a sub-microsecond memory write into a multi-millisecond delay, causing severe jitter in the p99 and p999 latencies of the application.

## The Upside: Fewer Minor Faults and TLB Misses When It Works

When huge pages *are* allocated without hitting compaction, THP delivers a genuine CPU efficiency win, not just a latency risk. Standard 4 KB pages under a growing heap trigger frequent minor page faults as new pages are mapped in, and each mapping consumes a TLB entry; a large heap can exhaust the TLB and force costly page table walks. Because a single 2 MB huge page replaces roughly 500 standard pages, heap growth under THP can eliminate the large majority of those minor page faults and the TLB pressure that comes with them — measurable directly as a drop in the [Instructions Per Cycle](instructions-per-cycle.md) instruction count for the same workload, since fewer faults and walks means fewer instructions retired to do the same work. This is the mechanism behind [explaining](explain-unexpected-performance-changes.md) an unexpectedly lower CPU utilization after a change that shifts allocations onto huge-page boundaries (e.g., a compiler or allocator upgrade) — a real efficiency gain, distinct from the compaction-stall risk above, and the reason THP is not a straightforward "always disable" decision: it trades allocation-time latency risk for steady-state CPU efficiency.

## Diagnostic Action

Look for high memory compaction activity or [direct reclaim stalls](direct-reclaim-stalls.md) in `/proc/vmstat`:
*   `compact_stall`: Number of times page allocation had to stall for compaction.
*   `compact_fail` / `compact_success`: Success rate of compaction attempts.

## Mitigations and Tuning

For high-throughput, low-latency applications (e.g., PostgreSQL, MySQL, MongoDB, Redis, Elasticsearch, Java Cassandra nodes), THP should be disabled:

### 1. Disable THP
Disable dynamic huge page allocation and defragmentation at boot time by adding the following to the kernel boot command line, or in a startup script:
```bash
echo never > /sys/kernel/mm/transparent_hugepage/enabled
echo never > /sys/kernel/mm/transparent_hugepage/defrag
```
*   `enabled=never`: Prevents new transparent huge pages from being allocated.
*   `defrag=never`: Prevents threads from blocking on compaction stalls during allocation.

### 2. Use Static HugePages (HugeTLB)
If the workload benefits from huge pages, use static huge pages instead of THP. Static huge pages are reserved at boot time (e.g., by setting `vm.nr_hugepages` in `/etc/sysctl.conf`).
*   **Advantage:** Guarantees contiguous memory blocks are immediately available, bypassing the need for dynamic compaction and eliminating compaction stalls entirely.
*   **Disadvantage:** Memory reserved for static huge pages is locked and cannot be used for standard system allocations or file system page cache, requiring precise capacity sizing.
