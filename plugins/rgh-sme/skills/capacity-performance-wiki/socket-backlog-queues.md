---
type: concept
title: Socket Backlog Queues
description: The kernel-level queues that manage incoming TCP connections during and after the three-way handshake before they are accepted by the application.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 10"
---

When an application socket listens on a port (using the `listen()` system call), the operating system kernel maintains two distinct backlog queues to manage incoming TCP connection requests. Under heavy traffic or application blockage, these queues can saturate, leading to dropped connections.

## The Two Backlog Queues

```
Client                   Kernel Backlog Queues                 Application
  |                               |                                 |
  |--- SYN ---------------------->| (SYN Backlog Queue)             |
  |<-- SYN-ACK -------------------| [Half-open connections]         |
  |                               |                                 |
  |--- ACK ---------------------->| (Accept Queue)                  |
  |   (Handshake Complete)        | [Established connections]       |
  |                               |                                 |
  |                               | <--- accept() ------------------|
  |                               |  (Connection Removed)           |
```

### 1. The SYN Backlog Queue (Half-Open Queue)
This queue holds TCP connections that are in the middle of the three-way handshake. The server has received a `SYN` packet and sent a `SYN-ACK`, and is waiting for the client's final `ACK` to complete the handshake.

*   **Tuning Parameter:** `net.ipv4.tcp_max_syn_backlog` (system-wide sysctl).
*   **Saturation Consequence:** If this queue overflows (due to a sudden traffic burst or a SYN flood denial-of-service attack), the kernel will drop incoming `SYN` packets, preventing new clients from connecting. If `net.ipv4.tcp_syncookies = 1` is enabled, the kernel will fall back to using SYN cookies, allowing connections to proceed without consuming backlog queue slots.

### 2. The Accept Queue (Established Queue)
This queue holds fully established TCP connections (the three-way handshake is complete) that are waiting to be picked up by the application process via the `accept()` system call.

*   **Sizing Rule:** The size of the Accept queue is determined by the minimum of:
    *   The backlog parameter passed to the application's `listen(fd, backlog)` call.
    *   The system-wide kernel parameter `net.core.somaxconn`.
*   **Saturation Consequence:** If the application thread or event loop blocks (e.g., due to CPU-bound processing, lock contention, or slow garbage collection) and stops calling `accept()`, the Accept queue will overflow. 
    *   When this occurs, the kernel drops incoming client `ACK` packets (or sends a `RST` reset packet, depending on `net.ipv4.tcp_abort_on_overflow`). 
    *   From the client's perspective, the connection is initiated but times out or fails during transmission.

## Diagnosis and Sizing

*   **Inspect Queue Depths (`ss`):** Run `ss -lnt` to inspect the state of listening sockets.
    *   **`Send-Q` (Send Queue):** The maximum capacity of the Accept queue.
    *   **`Recv-Q` (Receive Queue):** The number of established connections currently waiting in the Accept queue. If `Recv-Q` is equal to or near `Send-Q`, the application is failing to accept connections fast enough.
*   **Identify Drops (`nstat`):** Run `nstat -az | grep -E "ListenDrop|ListenOverflow"` to inspect cumulative protocol counters. Non-zero counts for `TcpExtListenDrops` and `TcpExtListenOverflows` indicate that connections have been discarded due to backlog queue saturation.

## Mitigation

*   **Increase `net.core.somaxconn`:** Raise this limit to `2048` or `4096` on high-concurrency servers to accommodate larger application-level backlog limits.
*   **Increase Application Backlog:** Configure the web server, proxy, or database runtime (e.g., Nginx's `backlog` setting) to use a higher backlog count matching `somaxconn`.
*   **Optimize Event Loop Responsiveness:** Ensure the application thread calling `accept()` is not blocked by long-running computations or synchronous I/O.
