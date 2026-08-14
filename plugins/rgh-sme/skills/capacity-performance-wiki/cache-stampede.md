---
type: concept
title: Cache Stampede
description: A performance failure mode where the expiration of a highly popular cached item causes concurrent requests to saturate backend databases simultaneously.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 5"
---

A **cache stampede** (also known as a **cache miss storm**, and sometimes loosely as a "thundering herd") is a critical system failure mode that occurs when a highly popular cached item expires or is invalidated under high-concurrency workloads. It is caused by cache key expiration specifically; for the client-side retry-driven variant of "thundering herd," see [synchronized retry storm](synchronized-retry-storm.md).

## The Failure Mechanism

1.  **High Traffic:** A specific cached key (e.g., homepage configuration, product details) is requested thousands of times per second.
2.  **Expiration:** The key's Time-To-Live (TTL) expires, or the key is manually invalidated.
3.  **Simultaneous Cache Misses:** Because the key is no longer in the cache, all concurrent requests arriving at that instant result in a cache miss.
4.  **Backend Saturation:** Hundreds or thousands of application threads simultaneously query the underlying database or microservice to fetch the raw data and rebuild the cache.
5.  **Cascading Failure:** The database experiences a massive spike in CPU utilization, disk read latency, and connection exhaustion, leading to slow response times or service outages.

```
[Clients] ----(1000 req/sec)----> [App Servers] ----(Cache Miss)----> [Database]
                                       |                                (Saturates!)
                                       +----(Lock/Rebuild)----> [Cache]
```

## Mitigation Strategies

To protect backend capacity from cache stampedes, systems use several architectural patterns:

### 1. Mutual Exclusion (Locking)
When a cache miss occurs, the application thread must acquire a lock (a local mutex or a distributed lock like Redis Redlock) before querying the backend database.
*   **Behavior:** Only the first thread acquires the lock and queries the database. All other threads wait for the lock to be released or poll the cache until the value is re-populated by the winning thread.
*   **Trade-Off:** Introduces slight latency overhead for waiting threads during a miss, but completely insulates the backend from traffic spikes.

### 2. Probabilistic Early Expiration (XFetch)
This algorithm probabilistically triggers a cache refresh *before* the key's TTL expires. The probability of early refresh increases as the key approaches its expiration time and is proportional to the database query computation time and the request rate.
*   **Formula:** A refresh is triggered if:
    $$-\beta \cdot \delta \cdot \ln(\text{rand}()) > \text{TTL}$$
    Where $\delta$ is the time taken to compute the value, $\beta$ is a tuning constant ($>0$), and $\text{rand}()$ is a uniform random number between 0 and 1.
*   **Behavior:** Popular keys are refreshed asynchronously by a request thread just before they expire, ensuring subsequent requests never experience a hard cache miss.

### 3. Background Refresh
The application never allows keys to expire naturally from client-facing requests. Instead, a background cron job or message queue consumer periodically recalculates the data and updates the cache.
*   **Behavior:** Client requests always hit the cache, resulting in $O(1)$ constant latency.

### 4. Soft Expiration (Stale-While-Revalidate)
The cache maintains a "soft" expiration time and a "hard" expiration time.
*   **Behavior:** When the soft TTL expires, the cache immediately serves the stale (old) cached value to the client, but triggers an asynchronous background thread to fetch the fresh data from the database and rebuild the cache.
