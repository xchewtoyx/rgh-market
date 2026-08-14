---
type: concept
title: I/O Scheduler Selection
description: The Linux block-layer I/O scheduler should match the underlying storage's access characteristics — a scheduler optimizing for seek time actively hurts performance on media that has none.
sources:
  - title: "Database Reliability Engineering"
    resource: "Database Reliability Engineering (Laine Campbell, Charity Majors), ch. 5"
---

The Linux kernel's block-layer I/O scheduler decides the order in which queued I/O requests are dispatched to a storage device. Different schedulers optimize for different physical access characteristics, so the right choice depends on the underlying media, not on a single "best" default.

## Matching Scheduler to Media

*   **`noop` (or `none`) for SSD/NVMe arrays:** solid-state storage has no mechanical seek penalty and typically has its own internal, controller-level request reordering and wear-leveling optimization. A host-side scheduler trying to reorder requests for seek-time locality is solving a problem the device doesn't have, and only adds CPU overhead and latency to the I/O path. Treating all requests as equally costly (`noop`'s behavior) is closer to correct for this media, since it lets the device's own controller do the optimization it's actually positioned to do well.
*   **`deadline` for concurrent, multithreaded database workloads on other media:** the `deadline` scheduler bounds how long any single request can be starved by reordering, which matters when many threads are issuing I/O concurrently and no single request should be able to wait indefinitely behind reordering optimizations for other requests.

## Why This Is a Capacity-Relevant Choice

Picking the wrong scheduler for the media doesn't show up as an outright failure — it shows up as unexplained extra latency or reduced achievable IOPS on storage that should be capable of much more, the same class of hidden capacity loss that motivates [active benchmarking](benchmarking-pitfalls.md): the scheduler's overhead is invisible in a benchmark that only reports throughput/latency without checking whether the storage subsystem is doing unnecessary reordering work.
