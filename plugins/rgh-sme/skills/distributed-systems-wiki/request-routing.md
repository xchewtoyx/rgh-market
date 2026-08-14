---
type: concept
title: Request Routing to Partitions
description: >
  How a client's request finds the node currently owning a key's partition —
  forwarding between nodes, a routing tier, or partition-aware clients, with
  placement metadata agreed via a coordination service.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 6"
  - title: "Dynamo: Amazon's Highly Available Key-value Store"
    resource: "Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al.), §3.3, §6.4"
---

# Request Routing to Partitions

[Partition](partitioning.md) placement changes over time
([rebalancing](rebalancing-partitions.md), failover), so "which node do I ask
for key X?" is a moving target — an instance of service discovery. Three
placements for the routing knowledge:

1. **Any node forwards.** Client contacts any node (round-robin); if that
   node doesn't own the partition, it forwards the request and relays the
   reply. No dedicated infrastructure; nodes share placement via gossip
   (Cassandra, Riak).
2. **Routing tier.** A partition-aware proxy in front of the cluster routes
   each request (mongos in MongoDB, Moxi in Couchbase); the proxy is itself
   infrastructure to scale and keep current.
3. **Partition-aware clients.** Clients hold the partition-to-node map and
   connect directly — fastest path, thickest client.

Dynamo measured the concrete cost of *not* choosing option 3: routing every
request through a generic load balancer (server-driven coordination) versus
having the client library poll a random node every 10 seconds for the
current membership view and route directly (client-driven) — a pull-based
refresh chosen over push specifically because it scales to large client
populations without the server tracking per-client state, at the cost of up
to 10 seconds of staleness that a client self-corrects by refreshing
immediately once it notices unreachable members. In production this cut
average latency by 3–4ms and **99.9th-percentile** latency by over 30ms,
simply by removing the load balancer hop and the extra network hop it can
add — a concrete instance of why [tail-latency-conscious
systems](tail-latency-amplification.md) favor thick, routing-aware clients
once the operational cost of keeping their view fresh is worth paying.

Whichever layer routes, it must **agree on current placement** — a routed
request hitting a node that no longer owns the partition means errors or, in
subtle cases, stale answers. Many systems delegate the authoritative mapping
to a [coordination service](coordination-services.md): ZooKeeper holds
partition-to-node metadata, nodes register themselves, and routing tiers and
clients subscribe to change notifications (HBase, SolrCloud, Kafka). Gossip
protocols distribute the same knowledge without the external dependency, at
the cost of eventual agreement.

## Metadata indirection for bulk transfers

For large payloads, routing through data rather than around it turns the
router into a bandwidth bottleneck: proxying every byte of a multi-gigabyte
read through a routing tier or forwarding node saturates that node's network
capacity long before it saturates any single storage node's. The fix
separates the two questions — a metadata server answers only "which node(s)
hold this data" and returns that location list, and the client then fetches
the bulk payload directly from the data-holding node(s), never routing the
payload itself through the metadata layer. Distributed file systems built
around a master/chunkserver split use exactly this pattern (the master holds
a directory-to-chunk-location mapping, analogous to a filesystem's inode
table, while chunkservers hold the actual data blocks) — it is the same
[control-plane-versus-data-plane](control-plane-vs-data-plane.md) separation
applied at the storage layer: the metadata server is control plane, the
direct client-to-chunkserver transfer is data plane, and keeping them
separate is what keeps the control plane cheap to run at scale. Returning
locations is only half the story — [read replica
selection](read-replica-selection.md) determines which returned replica
actually serves the read, and ordering bugs there can create [hot
spots](hot-spots-and-skew.md) even when placement is fair.

## Hop count is a latency design choice, not just a topology detail

Structured peer-to-peer overlays (Chord, Pastry) route a request through a
chain of intermediate peers — typically O(log N) hops for an N-node overlay —
each peer forwarding to whichever neighbor is topologically closer to the
key. This bounds routing table size per node at the cost of turning every
request into a multi-hop chain, and each hop is an independent chance to hit
the network's tail — exactly the compounding effect [tail latency
amplification](tail-latency-amplification.md) describes for fan-out, applied
serially instead of in parallel. Dynamo rejected this trade for a
latency-sensitive workload with a tight percentile SLA (99.9% within a few
hundred milliseconds): instead it keeps every node aware of enough routing
information to reach the right node in a single hop — a **"zero-hop
DHT"** — accepting a larger per-node membership table (see the scaling limit
this creates under [membership services](membership-services.md)) in
exchange for removing hop count from the latency budget entirely.
