---
type: concept
title: Hash Partitioning
description: >
  Assigning keys to partitions by hash to spread load uniformly — at the cost
  of destroying key-order locality and range queries.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 6"
---

# Hash Partitioning

Run each key through a non-cryptographic hash function (MD5, FNV — it only
needs uniformity, not security) and assign each [partition](partitioning.md) a
range of *hash values*. Skewed, clustered keys come out uniformly scattered,
eliminating the [hot spots](hot-spots-and-skew.md) that key order causes under
[key-range partitioning](key-range-partitioning.md).

The price: **key-order locality is destroyed.** Keys that were adjacent are
scattered across all partitions, so range queries on the key either aren't
supported (Riak, Couchbase, Voldemort) or must be sent to
[all partitions](partitioned-secondary-indexes.md) (MongoDB with hashed
sharding).

**Compound-key compromise (Cassandra):** hash only the *first* column of a
compound primary key to pick the partition; the remaining columns sort rows
within it. `(user_id, update_timestamp)` spreads users uniformly while
keeping each user's updates contiguous and range-scannable — an effective
pattern for one-to-many data. Note also that hashing fixes load imbalance
from *key distribution*, not from *request distribution*: a single extremely
hot key still hashes to a single partition (see
[hot spots and skew](hot-spots-and-skew.md)).

Language warning: "consistent hashing" as defined in the literature
(random-boundary rehashing rings) is rarely what databases actually do —
partition assignment usually follows one of the
[rebalancing strategies](rebalancing-partitions.md) instead, and `hash(key)
mod N` in particular is a trap fixed by decoupling logical partition count
from node count — see [fixed partitions](fixed-partitions.md).
