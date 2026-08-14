---
type: concept
title: Disk Failure Rate Planning
description: Provisioning spare storage capacity and redundancy based on empirical drive failure rates over a device's lifetime, rather than treating disk failure as a rare edge case.
sources:
  - title: "Database Reliability Engineering"
    resource: "Database Reliability Engineering (Laine Campbell, Charity Majors), ch. 5"
---

Storage capacity planning has to account for **disk failure as a routine, expected event**, not a rare edge case, because empirical failure rates are high enough to matter at any real fleet size. A widely cited large-scale study of drive failures (Google, 2007) found roughly 3 in 100 drives fail within their first three months of service, and roughly 1 in 50 fail between six and twelve months — meaning a fleet of any meaningful size will experience ongoing drive failures continuously, not occasionally.

## Capacity Implications

*   **Spare/replacement capacity must be budgeted, not improvised.** Given predictable failure rates, the number of drives likely to fail in a given period is a forecastable quantity, not a surprise — replacement stock and rebuild capacity should be sized against that forecast the same way any other demand is sized.
*   **Redundancy sizing should assume failures happen in the normal operating window, not just at the tail.** A drive failure rate this common is not a rare-catastrophe scenario for [N+M redundancy](n-plus-m-redundancy.md) purposes — $M$ needs to comfortably cover the expected concurrent-failure count at the fleet's actual size, not just a single worst-case unit loss.

## Failure Isolation Shapes the Blast Radius, Not Just the Rate

How disks are grouped changes what a failure costs, independent of how often failures happen:

*   **RAID arrays** (see [RAID write penalty](raid-write-penalty.md)) pool multiple physical disks into one logical volume — a single disk failure is absorbed transparently (RAID 1/10) or via parity reconstruction (RAID 5/6), but the array as a whole represents one unit of correlated risk if redundancy within it is exhausted (e.g., a second failure during a RAID 5 rebuild window).
*   **JBOD (Just a Bunch of Disks)** keeps disks independent rather than pooled: individual disk failures are more frequently *visible* as discrete events (no RAID controller masks them), but each failure's blast radius is limited to that one disk's data — the rest of the JBOD set keeps serving unaffected. This is a capacity/availability trade-off, not a strictly worse option: JBOD trades higher visible failure frequency for smaller per-failure impact, while RAID trades lower visible failure frequency for a larger correlated-risk unit when its redundancy budget is exhausted.

Which shape is right depends on whether the system's higher-level redundancy (e.g., database replication across independent hosts) already provides durability, making per-disk RAID redundancy partially redundant with it, or whether the disk layer is the primary durability boundary.
