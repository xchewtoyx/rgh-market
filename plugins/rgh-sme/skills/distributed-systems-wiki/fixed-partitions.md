---
type: concept
title: Fixed Partitions
description: >
  Decoupling a key's logical partition from its physical node by fixing the
  partition count independently of cluster size, so adding nodes rebalances
  ownership without reshuffling every key's assignment.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 19, Fixed Partitions"
  - title: "Dynamo: Amazon's Highly Available Key-value Store"
    resource: "Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al.), §4.2, §6.2"
---

# Fixed Partitions

Naive `hash(key) % num_nodes` satisfies the two basic requirements of
[partitioning](partitioning.md) — even distribution, and locating a key's
owner without asking every node — but breaks the moment the cluster resizes:
going from 3 nodes to 5 reshuffles almost every key's assignment, forcing a
large, disruptive data migration just to add a couple of nodes. This is the
concrete failure mode behind [hash partitioning](hash-partitioning.md)'s
warning that `hash(key) mod N` is a trap.

The fix is a level of indirection: introduce a **fixed number of logical
partitions**, chosen once at cluster creation and never changed regardless
of how the cluster resizes, and separately maintain a logical-partition →
physical-node mapping that *does* change on resize. A key's logical
partition is `hash(key) % partition_count` and never moves; only which node
currently hosts that partition changes. Rebalancing therefore reassigns
whole partitions between nodes instead of individual keys, and — for systems
like Kafka that need per-partition ordering — a partition's contents never
cross into a different logical partition, so per-partition order survives
every rebalance.

Guidance on sizing: pick a partition count with headroom for growth, well
above the expected node count (Akka recommends roughly 10x node count in
shards; Apache Ignite defaults to 1024; Hazelcast defaults to 271 for
clusters under 100 nodes). The hash function itself has to be
platform-independent — a JVM's built-in object hash varies by runtime and is
unsuitable — so real implementations use MD5 or Murmur hash instead.
Partition counts are also commonly chosen as a power of 2, since `hash mod
2^n` reduces to masking the low n bits of the hash instead of a general
modulo operation — cheap enough to matter at the request rates these lookups
run at.

Decoupling logical partition count from node count also solves a second
problem beyond rebalancing cost: heterogeneous hardware. Choosing many more
partitions than nodes (e.g. a few thousand) and assigning a *variable*
number of them per node, sized to that node's actual capacity, lets a node
twice as powerful as its peers simply hold twice as many partitions — the
same lever vnodes (below) use for even distribution, generalized here to
uneven hardware rather than uniform nodes.

## Assigning partitions to nodes

Partition-to-node assignment is itself a piece of small, critical,
frequently-read metadata, so it's typically delegated to a [coordination
service](coordination-services.md) or a dedicated [consistent
core](coordination-services.md) that tracks live membership (via
[heartbeat](heartbeat.md)-based [lease](distributed-locks.md) expiry) and
persists the mapping through a [replicated log](replicated-log.md) —
YugabyteDB's master cluster and Kafka's KIP-631 controller both work this
way. Peer-to-peer systems without a dedicated core instead elect an
[emergent leader](emergent-leader.md) (Akka, Hazelcast) to do the same
coordinating job. Either way, membership changes (a node joining, a node
declared failed) are themselves committed through the log rather than kept
as purely local state, so every node's view of "who owns what" stays
consistent even across a coordinator failover.

A practical scaling trap: if every client fetches the partition table
directly from a single coordinator on every request, that coordinator
becomes a read bottleneck under enough clients — both Kafka (originally
polling ZooKeeper directly for metadata) and YugabyteDB hit this in
production. The fix is to replicate or cache the partition table across all
cluster nodes, so a client can refresh it from whichever node it's already
talking to.

## The alternative: partitions proportional to node count

Cassandra popularized the opposite approach — classic consistent hashing,
where each *node* (rather than the cluster as a whole) owns one or more
randomly placed hash tokens on a ring, and a key maps to the node owning the
next-higher token. This needs a search over sorted tokens rather than fixed
partitioning's O(1) modulo lookup, and has been shown to produce more data
imbalance — which is why most systems prefer fixed partitions instead. A
single token per node also has a sharper flaw: adding one node dumps the
entire burden of splitting a range onto exactly one existing neighbor.
Cassandra's fix is to give each node many random tokens ("vnodes," 256 by
default) so a new node pulls smaller slices from many existing nodes at
once instead of overloading one.

This is a different rebalancing story from [key-range
partitioning](key-range-partitioning.md), where the partition-to-key mapping
is expected to change over time as ranges split — fixed partitions keep that
mapping frozen and rebalance ownership instead.

### Origin: Dynamo's ring, and why it moved to fixed partitions

This token-per-node scheme is Dynamo's original design, and Dynamo's own
production history is a worked demonstration of why most systems eventually
move away from it. The mechanics: a key hashes (MD5, in Dynamo's case) to a
position on the ring; walking clockwise from that position to the first
node position found is that key's owner; each node holds several random
**token** positions (virtual nodes) rather than one, so a node's failure or
departure spreads its load evenly across the rest of the ring instead of
dumping it all on one neighbor, and a joining node picks up a roughly equal
slice from many existing nodes instead of stealing one giant contiguous
range from a single one.

In production this "random tokens per node" strategy hit three concrete
costs as cluster size grew: **bootstrapping was slow**, because a joining
node's key ranges are scattered and unpredictable, forcing existing nodes to
scan their entire local store to find what to hand off — measured at nearly
a full day during a busy season on nodes serving millions of requests/day;
**[anti-entropy](read-repair-and-anti-entropy.md) got expensive**, because
every membership change reshuffles many nodes' key ranges and invalidates
their [Merkle trees](read-repair-and-anti-entropy.md), forcing expensive
recomputation; and **archival was impractical**, since there was no
contiguous way to snapshot the whole key space — it had to be pulled node
by node. Dynamo's fix was exactly the fixed-partitions move described
above: decouple a fixed number of equal-sized partitions from token
placement, and go further by giving each node a *fixed* count of `Q/S`
partitions (Q = total partitions, S = node count) rather than random
per-node tokens, so partitions can be relocated as whole files instead of
scattered key-by-key transfers. Measured in production, this change
improved load-balancing efficiency **and** cut the per-node membership
metadata Dynamo had to gossip by three orders of magnitude — random tokens
require every node to track every other node's token positions, while fixed
partitions only require tracking the (much smaller, fixed-size) partition
table. (Replicating a key across several *distinct physical* nodes despite
virtual-node ring positions is a related concern of the replica-selection
layer above partitioning — see [leaderless replication's preference
lists](leaderless-replication.md).)
