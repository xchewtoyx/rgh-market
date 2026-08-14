---
type: concept
title: Non-Uniform Memory Access (NUMA)
description: A multi-socket processor architecture where physical memory is partitioned into local nodes, making memory access times dependent on the physical distance between the CPU core and the RAM.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 6"
---

**Non-Uniform Memory Access (NUMA)** is a memory design used in multi-socket (multiprocessor) systems. Under NUMA, physical memory is partitioned into distinct **NUMA nodes**, each wired directly to a specific CPU socket. 

## Local vs. Remote Memory Access

A CPU core's memory access time varies depending on which physical memory module it is accessing:

*   **Local Memory Access:** The CPU core accesses RAM attached directly to its own socket. This is the lowest-latency, highest-bandwidth connection.
*   **Remote Memory Access:** The CPU core accesses RAM attached to a different CPU socket. This request must traverse high-speed interconnect buses (e.g., Intel Ultra Path Interconnect (UPI), AMD Infinity Fabric). 

### Performance and Capacity Impact

Remote memory access introduces a **30% to 100% latency penalty** relative to local access. It also consumes interconnect bus bandwidth, which can become a system-wide bottleneck under memory-intensive workloads. 

If a multi-threaded application (such as a database) is scheduled across multiple sockets but its memory is allocated on only one socket, it will suffer from severe remote-access latency, limiting the benefit of [vertical scaling](horizontal-vs-vertical-scaling.md) (adding sockets).

```
NUMA Node 0                      NUMA Node 1
+------------+                   +------------+
| Socket 0   |<== Interconnect==>| Socket 1   |
| (Local)    |   (QPI/UPI/IF)    | (Remote)   |
+------------+                   +------------+
      ||                               ||
+------------+                   +------------+
| Memory 0   |                   | Memory 1   |
+------------+                   +------------+
```

## Mitigation and Tuning Strategies

To minimize remote memory overhead in high-performance or low-latency systems:

### 1. NUMA Pinning and Affinity
Use tools like `numactl` or control groups (`cgroups`) to bind application processes and their memory allocation to the same NUMA node:
*   `numactl --membind=0 --physcpubind=0-15 ./my_app` (restricts the application to CPU cores 0–15 and forces it to allocate memory only from NUMA Node 0).

### 2. Memory Allocation Policies
*   **Bind (`MPOL_BIND`):** Strict allocation from specified nodes. Fails if memory on those nodes is exhausted.
*   **Preferred (`MPOL_PREFERRED`):** Attempts to allocate locally, falling back to remote nodes if local memory is full.
*   **Interleave (`MPOL_INTERLEAVE`):** Round-robins page allocations across all nodes. This is highly effective for large, shared-memory architectures (e.g., Memcached, large databases) where maximizing memory bandwidth across sockets is more important than raw latency.

### 3. Automatic Kernel NUMA Balancing
The Linux kernel includes an automatic NUMA balancing feature (`sysctl kernel.numa_balancing=1`). It periodically scans process pages, marks them unmapped, and triggers minor page faults when threads access them to determine where the accessing threads reside. It then migrates the pages to the local NUMA node of the accessing thread.
*   **Trade-Off:** Page migration consumes CPU cycles and memory bandwidth. It should be disabled if static pinning is already configured.
