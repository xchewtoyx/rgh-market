---
type: concept
title: Yield and Harvest
description: >
  A finer availability frame than up/down: yield is the chance of getting an
  answer at all; harvest is how complete that answer is when parts of the
  system are down.
sources:
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 11"
---

# Yield and Harvest

When part of a distributed system is down, "is the service available?" is
too coarse. Split it:

- **Yield:** the probability a request gets *an* answer.
- **Harvest:** the *completeness* of the answer — what fraction of the full
  data contributed to it.

A [partitioned](partitioning.md) search service with 25% of its nodes down
can either fail every query (harvest 100%, yield down) or answer every query
from the surviving 75% of the data (yield 100%, harvest 75%). Neither is
"correct" — it's a product decision that should be made *deliberately, in
advance*, per data type: search results and recommendations usually tolerate
reduced harvest; account balances do not, and preserving their harvest means
paying for more replicas and zones.

This is the same trade-off [CAP](cap-theorem.md) states in the extreme, made
operational: [scatter/gather reads](partitioned-secondary-indexes.md) are the
classic place it bites (return partial results, or fail because one
partition timed out?). Decomposing a system into independently failing
pieces (functional partitioning, service decomposition) is harvest
management: it shrinks how much harvest any single failure removes,
preserving overall yield.
