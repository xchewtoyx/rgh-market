---
type: concept
title: Memory Overcommit
description: How operating system memory overcommit policies permit the over-allocation of virtual memory, creating capacity risks that can trigger the Out-Of-Memory (OOM) killer.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 7"
---

**Memory overcommit** is an operating system memory management policy that permits applications to allocate more virtual memory than the system has physical memory (RAM + swap) to back. While it increases resource density, overcommit introduces severe capacity risks that can lead to sudden process termination.

## The Overcommit Mechanism

When an application requests memory (e.g., via `malloc()` or `mmap()`), the OS kernel grants the allocation in virtual memory (inflating the process's **Virtual Size (VSZ)**) without immediately allocating physical RAM. Physical page frames are only mapped when the application actually writes to the memory, triggering a minor page fault.

This design assumes that applications rarely use 100% of their allocated virtual memory simultaneously.

## Linux Overcommit Modes

The kernel's allocation behavior is configured via the `/proc/sys/vm/overcommit_memory` sysctl:

### Mode 0: Heuristic Overcommit (Default)
The kernel uses an internal heuristic to estimate if there is "enough" memory. It allows reasonable overcommit but rejects obvious over-allocations (e.g., a process requesting 1 TB of virtual memory on a 16 GB RAM host).

### Mode 1: Always Overcommit
The kernel always approves all virtual memory allocation requests, bypassing checks. 
*   **Capacity Risk:** Highly volatile. Applications can allocate infinite virtual memory, but writing to it will crash the system if physical memory is exhausted.

### Mode 2: Strict Non-Overcommit (Disable Overcommit)
The kernel strictly enforces a memory **Commit Limit**, rejecting allocation requests if they would push total committed memory past this threshold:

$$\text{Commit Limit} = \text{Swap Space} + \left( \text{Physical RAM} \times \frac{\text{vm.overcommit\_ratio}}{100} \right)$$

*   **Behavior:** When the limit is reached, allocation system calls return `ENOMEM` (Out of Memory). This allows applications to handle memory exhaustion gracefully (e.g., returning an error, closing idle connections, or flushing cache) rather than crashing.

## The Out-Of-Memory (OOM) Killer

When overcommit is enabled (Modes 0 or 1), the system can run out of physical RAM and swap space while processing page faults for already-granted allocations. To prevent a kernel panic, the kernel invokes the **OOM Killer**.

1.  **Process Selection:** The OOM killer computes an `oom_score` for every process, reflecting the percentage of physical RAM and swap it is consuming.
2.  **Termination:** The process with the highest score is abruptly terminated (`SIGKILL`) to free up physical memory.

### Protecting Critical Processes

In production environments, critical master processes (e.g., databases, system daemons, container runtimes) can be protected from OOM termination by tuning their `oom_score_adj` in `/proc/[pid]/oom_score_adj` (ranging from `-1000` to `1000`):
*   Setting `oom_score_adj` to `-1000` completely exempts the process from the OOM killer.

## Swapping vs. the OOM Killer for Latency-Sensitive Services

Allowing swap gives an overcommitted system a way to survive memory pressure without killing a process, but for latency-sensitive stateful services (databases in particular) this trade is often not worth taking: swapping a working set out to disk turns in-memory-speed operations into disk-latency operations, potentially degrading *every* request for as long as the swapped pages are needed back, whereas an OOM-killed process fails fast and, given proper redundancy and failover (see [N+M redundancy](n-plus-m-redundancy.md)), can be replaced by a healthy replica quickly. For this class of workload, disabling swap entirely and letting `oom_score_adj` tuning protect the critical process — rather than letting it degrade slowly under swap — is often the better latency trade-off, provided failover is actually solid enough to make fast failure survivable.
