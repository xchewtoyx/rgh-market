---
type: concept
title: Ephemeral Port Exhaustion
description: A capacity bottleneck where a system exhausts its pool of temporary source ports due to high rates of short-lived connections accumulating in the TIME_WAIT state.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 10"
---

**Ephemeral port exhaustion** is a common network capacity bottleneck that occurs when a client system initiates outbound connections at a rate faster than the operating system can reclaim closed ports. This prevents the system from opening new outbound connections, causing application errors.

## The TCP 4-Tuple Constraint

A TCP connection is uniquely identified by a 4-tuple:

$$\text{Connection ID} = (\text{Source IP}, \text{Source Port}, \text{Destination IP}, \text{Destination Port})$$

When an application initiates an outbound connection, the operating system assigns a temporary source port from its **ephemeral port range** (configured via `/proc/sys/net/ipv4/ip_local_port_range`). 

If a client makes connections to a single target server (fixed Destination IP and Destination Port) from a single Source IP, the maximum number of concurrent connections is bounded by the number of available ephemeral ports.

## The TIME_WAIT Bottleneck

When a TCP connection is actively closed (typically by the client), the socket transitions to the **`TIME_WAIT`** state.
*   **Purpose:** The socket remains in `TIME_WAIT` for 2 Maximum Segment Lifetimes (2 MSL, which is hardcoded to $60 \text{ seconds}$ in the Linux kernel). This guarantees that any delayed or out-of-order packets belonging to the closed connection expire in transit, preventing them from corrupting subsequent connections.
*   **The Problem:** While a socket is in `TIME_WAIT`, its source port is locked and cannot be reused for a connection to the same destination.

### The Exhaustion Math
If a client application establishes and closes $500 \text{ connections/second}$ to a single backend database:
*   In $60 \text{ seconds}$ (the duration of the `TIME_WAIT` lock), the client will accumulate:
    $$500 \text{ conn/s} \times 60 \text{ s} = 30,000 \text{ sockets in } TIME\_WAIT$$
*   If the system's ephemeral port range is set to the Linux default (`32768` to `60999`, yielding $28,232$ ports), the client will exhaust all available ports.
*   Subsequent connection attempts fail immediately with the error **`Cannot assign requested address` (`EADDRNOTAVAIL`)**.

## Diagnosis

*   **Count Sockets (`ss`):** Run `ss -s` to view a summary of socket states. A high count of `timewait` sockets (e.g., $>20,000$) indicates potential exhaustion.
*   **Identify Errors:** Monitor application logs for connection errors containing `EADDRNOTAVAIL` or "Cannot assign requested address".

## Mitigations

1.  **Connection Pooling (Recommended):** Configure the application to use persistent connections (HTTP Keep-Alive, [database connection pools](connection-pool-saturation.md)). Reusing existing sockets eliminates the need to continuously open and close connections, bypassing ephemeral port allocation entirely.
2.  **Enable TCP Time-Wait Reuse:** Enable the `net.ipv4.tcp_tw_reuse` sysctl:
    ```bash
    sysctl -w net.ipv4.tcp_tw_reuse=1
    ```
    This allows the Linux kernel to safely recycle a socket in `TIME_WAIT` for a new outgoing connection if the connection uses TCP Timestamps (`net.ipv4.tcp_timestamps = 1`) and the timestamp of the incoming packet is greater than the last recorded timestamp.
3.  **Expand the Ephemeral Port Range:** Increase the pool of available source ports:
    ```bash
    sysctl -w net.ipv4.ip_local_port_range="1024 65535"
    ```
    This increases the maximum ephemeral pool from $28,232$ to $64,511$ ports.
4.  **Use Multiple IPs:** Bind the client or destination services to multiple IP addresses, multiplying the unique 4-tuples available.
