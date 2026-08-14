---
type: concept
title: Cache Hit Ratio Economics
description: Whether a cache is worth adding is a measurable question, not an assumption — a formula relating hit ratio to lookup times decides if it helps at all, and its cost must still be weighed against the capacity it actually saves.
sources:
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 5"
---

A cache is only a net win if the arithmetic actually works out — adding one is not automatically an improvement, and its benefit is directly computable before committing resources to it.

## When a Cache Actually Helps

Let $L$ be the uncached lookup time, $H$ the cache-hit time, $M$ the cache-miss time (which is usually slightly *worse* than $L$, since a miss pays for the cache check plus the full original lookup), and $R$ the hit ratio (hits over total lookups). A cache is a net win exactly when:

$$H \cdot R + M \cdot (1-R) < L$$

When cache-access cost is small enough to treat as negligible, this simplifies to an intuitive rule of thumb: expected improvement is approximately proportional to the hit ratio itself — a cache with a 33% hit ratio on a 6-second lookup gives, at best, roughly a 4-second average, with real-world gains typically landing somewhat below that ideal because cache-access overhead isn't actually free. Whether a given cache tier is even fast enough to be worth checking depends on the underlying latency gap being cached across — a disk-based cache is a clear win against a lookup that would otherwise cross a continent, but the same disk-based cache adds nothing (or actively hurts) against a lookup that's already same-datacenter.

## Cost-Effectiveness Is a Separate Question From Raw Performance

A cache that measurably improves latency can still be the wrong investment if its cost exceeds what it saves. If a cache lets 15 replicas do the work that would otherwise need 20, it's worth adding only if the cache's own cost (RAM, complexity, operational burden) is less than the 5 replicas it displaces — compare against [asynchronous offload](asynchronous-offload-for-capacity.md) and other capacity-relief techniques on the same cost basis, not in isolation. Where faster response time itself has a measurable revenue or conversion effect, that effect belongs in the comparison too, not just infrastructure cost.

## Sizing a Cache Before or After Building It

*   **Before building one:** sample historical request logs over a representative window and count how often the *same* key would have been requested again, assuming a hypothetical infinite, non-expiring cache. If even that best case shows a low duplicate rate, caching won't help regardless of size; if it does, the cumulative size of those duplicate responses estimates how large a real cache would need to be to capture them.
*   **After building one:** run a deliberately oversized cache and watch where usage naturally plateaus given normal entry expiry, or inspect the age distribution of cached entries directly — a distribution where the bulk of entries were touched recently but a long tail sits much older typically marks the boundary between the working set that's actually earning its keep and the excess that isn't.
*   **Ongoing:** monitor the real hit ratio continuously in production and re-tune size as traffic patterns shift — a size that was correct at launch is not guaranteed to stay correct as the workload's access pattern changes.

Cache correctness under concurrent misses (avoiding a [cache stampede](cache-stampede.md)) and entry replacement policy (see [cache replacement algorithms](cache-replacement-algorithms.md)) are separate concerns from sizing — a correctly-sized cache with the wrong invalidation strategy, or the wrong replacement policy for its access pattern, can still perform poorly.
