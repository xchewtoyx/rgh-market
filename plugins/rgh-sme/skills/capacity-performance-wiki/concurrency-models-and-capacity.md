---
type: concept
title: Concurrency Models and Capacity Trade-Offs
description: How different application concurrency models (multi-process, multi-threaded, and event-driven asynchronous) influence resource consumption, context-switching overhead, and scaling limits.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 5"
---

The concurrency model of an application determines how it handles multiple simultaneous operations (e.g., client requests). Each model places a unique set of constraints on system resource capacity—specifically memory footprint, CPU scheduling overhead, and connection limits.

## The Three Primary Concurrency Models

### 1. Multi-Process Model
In this model, the application spawns or forks a dedicated operating system process for each active connection or task (e.g., PostgreSQL, Apache prefork, PHP-FPM).

*   **Capacity & Resource Impact:**
    *   **Memory-Bound Scaling:** Each process has its own virtual memory space. Although Linux utilizes Copy-on-Write (CoW) to share read-only memory segments, each process still requires separate page tables, thread structures, and file descriptor tables. This creates a high memory baseline (typically tens of megabytes per process).
    *   **High Context-Switching Cost:** Context switching between processes requires invalidating the CPU's Translation Lookaside Buffer (TLB) and swapping process page tables, which adds substantial CPU overhead under high concurrency.
    *   **Bottleneck:** Memory capacity usually limits the maximum number of concurrent workers (e.g., maxing out at hundreds of concurrent processes).

### 2. Multi-Threaded Model
In this model, a single process spawns multiple execution threads that share the same virtual address space (e.g., Java JVM, MySQL, Apache worker). Modern Linux utilizes a 1:1 thread model via NPTL, mapping each user-space thread directly to a kernel task.

*   **Capacity & Resource Impact:**
    *   **Moderate Memory Footprint:** Threads share the process heap, but each thread requires its own stack space (typically $512 \text{ KB to } 8 \text{ MB}$).
    *   **Scheduler Saturation:** Spawning thousands of threads to handle high connection concurrency leads to CPU scheduler bottlenecks. The CPU spends excessive time performing thread context switches (saving/restoring registers) rather than executing application code.
    *   **[Lock Contention](lock-contention-overhead.md):** Shared memory requires synchronization primitives (locks, mutexes). Under high concurrency, threads spend significant time blocked off-CPU waiting for lock acquisition.
    *   **Bottleneck:** CPU scheduler overhead and lock contention typically limit scalability (e.g., maxing out at thousands of threads).

### 3. Event-Driven Asynchronous Model
This model uses a small, fixed number of threads (often one per CPU core) running an event loop (`epoll` on Linux) to manage all connections (e.g., Nginx, Node.js, Redis, Envoy). File descriptors are configured in non-blocking mode, and the event loop invokes callbacks as I/O events occur.

*   **Capacity & Resource Impact:**
    *   **Extremely Low Memory Footprint:** Eliminates thread stack overhead and process duplication. A single worker thread can manage tens of thousands of concurrent TCP connections with minimal memory.
    *   **High Connection Density:** Avoids OS-level context switching and thread scheduling overhead, permitting extreme horizontal connection scalability.
    *   **CPU Blocking Vulnerability:** Because a single thread handles thousands of connections, any synchronous CPU-bound task (e.g., cryptographic operations, JSON parsing of massive payloads, infinite loops) blocks the entire event loop. While blocked, the server cannot accept new connections or process I/O for existing connections, causing a rapid spike in latency across all clients.
    *   **Bottleneck:** CPU-bound processing latency and event loop blocking.

## Sizing and Capacity Planning Guide

The "Scaling Dimension" column below reflects [horizontal vs. vertical scaling](horizontal-vs-vertical-scaling.md) trade-offs at the per-process level; the same choice recurs at the whole-system level once a single node's concurrency model is maxed out.

| Model | Primary Bottleneck | Scaling Dimension | Best Use Case |
| :--- | :--- | :--- | :--- |
| **Multi-Process** | Physical RAM (Page Tables) | Scale-up (Add Memory) or Scale-out | Heavy, isolated tasks (databases) |
| **Multi-Threaded** | CPU Scheduler / Lock Contention | Scale-up (Add CPU cores) | Mix of CPU and I/O tasks |
| **Event-Driven** | Single-threaded CPU blocking | Scale-out (Process per core) | High-concurrency, I/O-bound (gateways, proxies) |
