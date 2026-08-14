---
type: concept
title: Benchmarking Pitfalls
description: Common methodology errors in performance benchmarking that produce invalid results, mask bottlenecks, or distort system capacity estimates.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 12"
  - title: "Database Reliability Engineering"
    resource: "Database Reliability Engineering (Laine Campbell, Charity Majors), ch. 10"
---

Benchmarking is the practice of measuring a system's throughput, latency, or capacity limits under controlled, reproducible workloads. However, benchmarking is prone to methodological errors that produce deceptive results.

The pitfalls below concern benchmarking a whole system (or a realistic subsystem) under representative load. For cheaply and repeatably timing a single small operation in isolation — a different, complementary need — see [micro-benchmark framework investment](micro-benchmark-framework-investment.md).

## Primary Benchmarking Pitfalls

### 1. Benchmarking Cache Instead of Storage
*   **The Error:** Testing storage devices (SSDs/HDDs) using a dataset (working set) that is smaller than the host's physical RAM. The operating system buffers the read requests in the [file system page cache](file-system-vs-disk-latency.md), meaning the benchmark measures memory transfer speeds ($>10 \text{ GB/s}$) rather than actual disk performance ($500 \text{ MB/s}$ to $3 \text{ GB/s}$).
*   **Prevention:** Ensure the benchmark working set size is at least twice the physical RAM capacity of the system under test, or use the [`O_DIRECT`](o-direct-io.md) flag to bypass the page cache completely.

### 2. Ignoring Warm-Up Periods
*   **The Error:** Collecting performance metrics immediately upon launching the system. At startup, the system is "cold" (empty page caches, empty database buffer pools, uncompiled JIT execution caches). Measuring performance during this phase reflects startup overhead rather than steady-state capacity.
*   **Prevention:** Run the benchmark for a designated "warm-up" period (e.g., 5 to 15 minutes) before beginning to record performance metrics.

### 3. Relying on Mean (Average) Latency
*   **The Error:** Summarizing request response times using the arithmetic mean. Averages hide tail latencies. For example, a system with a 10 ms average latency could have a 99th percentile (p99) latency of 5,000 ms, meaning 1 in 100 users experiences a 5-second freeze.
*   **Prevention:** Always record and report latency distributions using [percentiles](latency-percentiles-vs-mean.md) (p50, p90, p99, p99.9) and histograms.

### 4. Ignoring Error Rates
*   **The Error:** Reporting high request throughput without verifying request success. An application server might show a massive throughput of $10,000 \text{ requests/second}$ because it is instantly returning lightweight "HTTP 500 Internal Server Error" or "Connection Refused" responses due to database saturation.
*   **Prevention:** Track request error rates alongside throughput. A benchmark result is only valid if the error rate remains below an acceptable threshold (e.g., $<0.1\%$).

### 5. Unrepresentative Workloads
*   **The Error:** Generating synthetic traffic that does not mirror real-world access patterns (e.g., querying record IDs sequentially or using a perfectly uniform random distribution). In production, data access typically follows a **power-law distribution** (e.g., Zipfian or Pareto 80/20 distributions), where a small subset of "hot keys" are queried repeatedly while the rest are rarely accessed.
*   **Prevention:** Configure load generators (like YCSB or custom scripts) to use Zipfian or Pareto access distributions to accurately test cache hit ratios and lock contention. The same representativeness concern applies to the environment itself, not just the traffic pattern — see [scaled capacity test environments](scaled-capacity-test-environment.md).

### 6. Thermal and Frequency Scaling Variance
*   **The Error:** Running short tests where the CPU operates at maximum Turbo Boost frequency, but failing to test long-term sustained load where CPU clock rates drop due to thermal throttling or frequency scaling governors (`cpufreq`).
*   **Prevention:** Ensure benchmarks run long enough (soak testing) for system temperatures to stabilize, and lock the CPU governor to `performance` mode.

### 7. Benchmarking a Greenfield (Freshly Created) Dataset
*   **The Error:** Running a benchmark against a newly created, empty-then-loaded database. A freshly built B-tree index has its pages laid out contiguously in the order data was inserted, so early reads and writes benefit from artificially good sequential I/O locality — a benchmark run at this stage measures best-case, not steady-state, performance.
*   **Why It Diverges From Production:** As a real dataset ages, ordinary inserts, updates, and deletes trigger page splits and fragmentation, scattering what was once contiguous data across the disk and introducing the random I/O pattern that dominates a mature database's actual access pattern. A benchmark that never lets this fragmentation accumulate systematically overstates the system's real-world capacity.
*   **Prevention:** Benchmark against a dataset that has been aged through a realistic volume of inserts, updates, and deletes — not just loaded once and immediately queried — so index fragmentation and page-split overhead are represented in the result.

## Vendor Benchmark Marketing Tactics

The pitfalls above apply to benchmarks you run yourself; vendor-published benchmarks comparing their product favorably to competitors add a further layer of risk, since the vendor controls every variable and has an incentive to flatter their own system. Recurring tactics worth watching for when evaluating a vendor's published numbers, rather than treating them as a substitute for your own testing:

*   **Undersized "big data" datasets** — a system marketed for petabyte scale gets benchmarked against a dataset small enough to fit entirely in RAM or SSD cache, producing unrealistically fast repeat-query numbers that say nothing about the system's behavior at the scale it's actually being sold for.
*   **Mismatched billing-model cost comparisons** — comparing an always-on cluster's cost to a per-query or per-second dynamic-compute system on a naive per-second basis, ignoring that the two pricing models charge for fundamentally different things (idle-but-provisioned time vs. only-when-queried time).
*   **Asymmetric optimization** — running a workload shape that favors the vendor's own architecture (e.g., a join-heavy query on highly normalized data against a row store, compared against a columnar system with no equivalent schema tuning applied), then layering additional vendor-specific optimizations onto only one side of the comparison.
*   **Contractual gag clauses** — historically, some vendor contracts (informally called "DeWitt clauses") prohibited customers from publishing independent benchmark results at all, insulating unfavorable comparisons from ever surfacing publicly.

The only reliable defense is the same one that applies to your own benchmarking: run the vendor's system against your own representative data volume and query/access patterns (see the Unrepresentative Workloads pitfall above) rather than trusting a vendor's published comparison, however credible its methodology section reads.

## Active Benchmarking Rule

Never run a benchmark passively. Running a load generator and looking only at the reported throughput and latency is a blind methodology. **Always run host-level system observability tools (`iostat`, `vmstat`, `mpstat`, `sar`) during the test.** 

This allows you to verify *why* the benchmark reached a limit—by identifying which resource (CPU cores, memory capacity, block storage IOPS, network interface bandwidth, or kernel locks) reached 100% utilization or saturation first.
