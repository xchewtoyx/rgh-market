---
type: concept
title: RAID Write Penalty
description: The ratio of physical block device write operations required to service a single logical write request, which determines storage performance and capacity sizing.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 9"
---

The **RAID write penalty** is a fundamental storage performance concept representing the number of physical disk I/O operations required to execute a single logical write request. The penalty varies significantly by RAID configuration, impacting both write throughput and the capacity sizing of storage arrays.

## Penalty by RAID Level

| RAID Level | Description | Write Penalty | Physical I/O Mechanics per Logical Write |
| :--- | :--- | :--- | :--- |
| **RAID 0** | Striping | **1** | The logical write is written directly to the target striped disk. |
| **RAID 1** | Mirroring | **2** | The logical write must be written to both the primary and mirror disk. |
| **RAID 10** | Striped Mirrors | **2** | The logical write is written to both disks in the mirrored pair. |
| **RAID 5** | Distributed Parity | **4** | To update a single block, the controller must: <br>1. Read old data<br>2. Read old parity<br>3. Compute new parity<br>4. Write new data<br>5. Write new parity |
| **RAID 6** | Dual Parity | **6** | To update a single block, the controller must:<br>1. Read old data<br>2. Read old $P$ and $Q$ parity blocks<br>3. Compute new parities<br>4. Write new data<br>5. Write new $P$ and $Q$ parity blocks |

## Sizing and Capacity Planning Formulas

To size a storage array for a target workload, capacity engineers must translate application-level (logical) IOPS requirements into hardware-level (physical) IOPS capacity.

### Calculating Physical IOPS Required

$$\text{Physical IOPS} = (\text{Logical Reads}) + (\text{Logical Writes} \times \text{Write Penalty})$$

### Worked Example
An application requires a database volume to support $2,000$ logical IOPS with a workload profile of $60\%$ reads and $40\%$ writes. This translates to:
*   Logical Reads = $1,200 \text{ IOPS}$
*   Logical Writes = $800 \text{ IOPS}$

Calculating the physical IOPS required from the underlying disks:
*   **For RAID 10 (Write Penalty = 2):**
    $$\text{Physical IOPS} = 1,200 + (800 \times 2) = 2,800 \text{ IOPS}$$
*   **For RAID 5 (Write Penalty = 4):**
    $$\text{Physical IOPS} = 1,200 + (800 \times 4) = 4,400 \text{ IOPS}$$
*   **For RAID 6 (Write Penalty = 6):**
    $$\text{Physical IOPS} = 1,200 + (800 \times 6) = 6,000 \text{ IOPS}$$

## Capacity Planning Takeaways

1.  **Workload Profile Sensitivity:** Write-heavy workloads (e.g., transactional databases, message queues, write-ahead logs) are highly sensitive to write penalties. For these workloads, RAID 10 is preferred over RAID 5 or 6, as it minimizes the physical IOPS overhead on the drive array.
2.  **I/O Saturation:** Failing to account for the RAID write penalty during hardware sizing will lead to unexpected storage saturation, where physical disks reach 100% utilization (`%util`) despite logical metrics showing the volume is operating well below its rated limits.

The write penalty above assumes the logical I/O itself is already well-formed. A separate multiplier applies before that if the database's own block size doesn't line up with the RAID stripe boundary beneath it — see [database block size misalignment](database-block-size-misalignment.md).
