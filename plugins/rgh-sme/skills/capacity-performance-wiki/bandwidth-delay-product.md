---
type: concept
title: Bandwidth-Delay Product (BDP)
description: A fundamental networking metric representing the volume of data in flight over a network link, which determines the socket buffer sizes required to achieve maximum throughput.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 10"
---

The **Bandwidth-Delay Product (BDP)** is a core capacity planning metric in networking. It defines the volume of data that can be "in flight" (sent but not yet acknowledged) over a network path at any given instant. 

## The Formula

$$\text{BDP} = \text{Bandwidth} \times \text{RTT}$$

Where:
*   **Bandwidth:** The transmission rate of the network link (e.g., in bits per second or bytes per second).
*   **RTT (Round-Trip Time):** The time required for a packet to travel from sender to receiver and back again (in seconds).

## Impact on TCP Throughput

Under the TCP protocol, the volume of unacknowledged data in flight is restricted by the sender's congestion window (`cwnd`) and the receiver's advertised receive window (`rwnd`).

If the maximum size of these windows is smaller than the path's BDP, the sender will exhaust the window and be forced to idle, waiting for ACKs to return before transmitting more data. This limits the maximum achievable throughput of a single TCP connection:

$$\text{Max Throughput} \le \frac{\text{TCP Window Size}}{\text{RTT}}$$

To achieve $100\%$ utilization of the link's bandwidth, the TCP window size (which is backed by the socket's send and receive buffers) must be sized at least as large as the BDP:

$$\text{Required Socket Buffer Size} \ge \text{BDP}$$

## Sizing Worked Example

An application server in Virginia transfers data to an object store in Oregon over a dedicated $10 \text{ Gbps}$ network link.
*   **Bandwidth:** $10 \text{ Gbps} = 1.25 \text{ GB/s} = 1,250,000,000 \text{ bytes/s}$
*   **RTT:** $80 \text{ ms} = 0.08 \text{ s}$

### 1. Calculate the BDP
$$\text{BDP} = 1.25 \text{ GB/s} \times 0.08 \text{ s} = 100 \text{ MB}$$

This means that to keep the network link fully saturated, there must be $100 \text{ MB}$ of data in transit across the country at any point.

### 2. Sizing Bottleneck
If the Linux kernel's default maximum socket buffer size is capped at $4 \text{ MB}$ (`net.ipv4.tcp_rmem` max value), the maximum throughput a single TCP stream can sustain is:

$$\text{Max Throughput} = \frac{4 \text{ MB}}{0.08 \text{ s}} = 50 \text{ MB/s} = 400 \text{ Mbps}$$

The single TCP connection is throttled to only **$4\%$** of the physical network capacity due to buffer sizing, despite the network link being completely clear.

## Mitigations and Tuning

*   **Configure TCP Window Auto-Tuning:** Ensure Linux TCP auto-tuning is enabled (default on modern kernels) and increase the maximum buffer limit in sysctl:
    *   `net.ipv4.tcp_rmem = 4096 87380 134217728` (allows receive window to autotune up to 128 MB).
    *   `net.ipv4.tcp_wmem = 4096 65536 134217728` (allows send window to autotune up to 128 MB).
    *   `net.core.rmem_max = 134217728` (sets system-wide max socket receive buffer).
    *   `net.core.wmem_max = 134217728` (sets system-wide max socket send buffer).
*   **Utilize BBR Congestion Control:** Loss-based congestion control algorithms (like Cubic) often under-fill the BDP on links with packet loss. BBR models the BDP dynamically, maintaining the optimal window size to maximize throughput while minimizing queueing delay.

At the application layer, the same round-trip-bound ceiling can be worked around without touching kernel buffers at all, by keeping more than one request outstanding on a connection at once — see [request pipelining and the in-flight request limit](request-pipelining-in-flight-limit.md).

In cloud deployments specifically, RTT (and therefore this whole calculation) is itself a placement decision — see [cloud network topology and egress cost planning](cloud-network-topology-capacity-planning.md) for how zone/region placement trades off against bandwidth, latency, and cost.
