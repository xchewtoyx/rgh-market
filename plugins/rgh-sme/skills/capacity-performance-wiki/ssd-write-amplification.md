---
type: concept
title: SSD Write Amplification
description: An undesirable phenomenon in NAND flash storage (SSDs) where the physical volume of data written to flash memory is a multiple of the logical writes requested by the host.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 9"
---

**SSD write amplification** is a critical storage performance and longevity concern in solid-state drives (SSDs). It occurs when the amount of data physically written by the drive controller to the NAND flash memory is greater than the amount of data written by the host operating system.

## The Physical Cause: Page vs. Block Architecture

NAND flash memory exhibits a structural asymmetry in how data is read, written, and erased:
*   **Reads and Writes:** Performed at the **Page** level (typically $4\text{--}16 \text{ KB}$).
*   **Erases:** Can only be performed at the **Block** level (typically $128\text{--}512 \text{ Pages}$, or $2\text{--}8 \text{ MB}$).

Because flash cells must be erased before they can be rewritten, overwriting a single page of data is not simple. The SSD controller's **Flash Translation Layer (FTL)** must execute a read-modify-write cycle:
1.  Read the entire block containing the target page into controller RAM.
2.  Modify the target page in memory.
3.  Erase the entire physical block on flash.
4.  Write the entire modified block back to flash.

## Write Amplification Factor (WAF)

The **Write Amplification Factor (WAF)** measures this overhead:

$$\text{WAF} = \frac{\text{Physical Bytes Written to NAND Flash}}{\text{Logical Bytes Written by Host}}$$

*   **Ideal WAF = 1.0:** Physical writes match host writes. This is achieved through large, sequential write workloads.
*   **High WAF (WAF $> 3.0$):** Common in workloads featuring small, random writes (such as transactional database updates). Writing 1 KB of data might force the FTL to physically write 32 KB, resulting in a WAF of 32.

```
Host Writes (10 GB) ====> [ SSD Controller / FTL ] ====> NAND Flash Writes (30 GB)
                                                          (WAF = 3.0)
```

## Capacity, Performance, and Lifespan Impacts

1.  **Performance Degradation (Garbage Collection Stalls):** When the SSD runs out of clean blocks, the controller must perform background garbage collection (consolidating partially filled blocks and erasing them) while simultaneously handling host I/O. This resource contention causes write latency to spike, creating severe tail latency.
2.  **Hardware Wear-Out:** Flash memory cells have a finite lifespan, measured in Program/Erase (P/E) cycles. A high WAF accelerates the consumption of these cycles, causing the drive to reach its write endurance limit prematurely.

## Mitigation and Tuning

*   **Sequential I/O Patterns:** Design applications (such as Log-Structured Merge-tree databases like RocksDB) to write data in large, sequential batches to match physical block boundaries. Note that the LSM-tree storage engine itself has a separate, engine-level write amplification from its own background compaction — see [LSM-tree write amplification](lsm-tree-write-amplification.md) — which compounds with, rather than replaces, the SSD's own WAF.
*   **Enable TRIM:** Ensure the operating system mounts SSD filesystems with TRIM support (or schedules `fstrim` regularly). TRIM informs the FTL which blocks contain deleted file data, allowing the controller to skip copying those stale pages during garbage collection, lowering WAF.
*   **Over-Provisioning:** Reserve a percentage of the SSD's capacity (e.g., 10% to 20%) as unallocated space. Over-provisioning gives the FTL more temporary blocks to perform garbage collection, reducing write amplification and maintaining consistent write performance under heavy loads.
