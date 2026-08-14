---
type: concept
title: Unreliable Networks
description: >
  Asynchronous packet networks give no delivery or latency guarantees; a
  sender that gets no response cannot tell what failed, or whether the request
  was actually processed.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 8"
---

# Unreliable Networks

Distributed systems are shared-nothing machines connected by asynchronous
packet-switched networks (Ethernet/IP). The network makes **no guarantees**
about delivery or timing. When a sender gets no response, at least six
scenarios are indistinguishable:

1. The request was lost in transit.
2. The request is waiting in a queue at the destination.
3. The remote node crashed.
4. The remote node is [paused](process-pauses.md) (e.g. GC) and will resume.
5. The remote node processed the request but the response was lost.
6. The response is merely delayed and will arrive later.

The critical corollary: **absence of a response tells you nothing about
whether the request was processed.** Any retry may therefore duplicate the
effect, which is why [retries require idempotency](idempotency.md), and any
failure declaration is a guess made via
[timeouts](timeouts-and-failure-detection.md).

## Why delays are unbounded

Circuit-switched networks (traditional telephony) reserve fixed bandwidth per
connection, making queueing impossible and latency bounded. Packet-switched
networks deliberately share wire capacity dynamically to exploit bursty
traffic, so delay arises from queueing at every hop: switch queues, the
receiving OS's buffers, CPU scheduling, and (in virtualized environments) the
hypervisor. Under load these queues grow without bound; packets are dropped
when queues fill, requiring retransmission. Latency guarantees would require
reserving capacity — a trade of utilization (cost) for predictability that
current datacenter technology doesn't offer.

Network partitions — one part of the network cut off from another — are just
the extreme of this, and handling them is not optional: software must respond
to faults deliberately (even if the response is "show an error"), and the
response must be tested by inducing faults, not assumed.
