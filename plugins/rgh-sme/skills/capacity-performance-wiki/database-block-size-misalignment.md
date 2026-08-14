---
type: concept
title: Database Block Size Misalignment
description: A database's page/block size is the smallest unit of I/O it performs, so a small logical read or write still costs a full block, and misalignment between that block size and the underlying filesystem or RAID stripe size wastes I/O beyond what the database's own block size already costs.
sources:
  - title: "Database Reliability Engineering"
    resource: "Database Reliability Engineering (Laine Campbell, Charity Majors), ch. 10"
---

A database stores rows inside fixed-size **blocks** (or pages — typically 8 KB or 16 KB), and the block, not the row, is the smallest unit the storage engine reads or writes. A 1 KB row living on a 16 KB block still costs a full 16 KB read to fetch — the database cannot read a fraction of a block. This is the same granularity mismatch that underlies [file system vs. disk latency](file-system-vs-disk-latency.md) analysis, one layer down: it applies even before the request reaches the OS page cache or block device.

## Compounding Misalignment: Database Block vs. Storage Stripe

A second, independent alignment problem sits between the database's block size and the filesystem or RAID array's own block/stripe size beneath it. If a database block boundary doesn't line up with the underlying storage's block or stripe boundary, a single logical database block can straddle two physical storage blocks — turning what should be one physical I/O into two. This is a distinct cost from the [RAID write penalty](raid-write-penalty.md) (which comes from parity/mirroring mechanics) and from the database's own block size (which comes from not being able to read less than one block): misalignment adds a *third*, avoidable multiplier on top of both, purely from the two layers' block boundaries not agreeing with each other.

## Practical Implications

*   **Match block sizes deliberately** across the database, filesystem, and RAID/storage layer where the platform allows it, rather than accepting each layer's independent default.
*   **SSDs are more sensitive to block-size tuning than HDDs**: larger block sizes can impose a 30-40% latency penalty on SSDs relative to HDDs, so the cost of getting block-size tuning wrong is higher on flash-backed storage than it might have been on spinning disks.
*   **Aggregate I/O demand scales with block size, not row size**: a capacity model that sizes disk IOPS or bandwidth requirements from row-level query volume without accounting for the block size those rows are read/written in will systematically underestimate physical I/O demand — see [RAID write penalty](raid-write-penalty.md) for the equivalent translation from logical to physical IOPS on the write-penalty side of this same problem.
