---
type: concept
title: Inode Exhaustion
description: A capacity planning bottleneck where a file system runs out of available metadata index nodes (inodes) and fails to write new files, despite having free disk space.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 8"
---

**Inode exhaustion** is a critical capacity planning failure mode where a file system is unable to create new files or directories because it has consumed all available metadata slots (inodes), even though abundant physical storage space (bytes) remains on the device.

## What is an Inode?

An **inode** (index node) is a kernel data structure that stores metadata about a specific file or directory on a file system, including:
*   File type, permissions, and owner.
*   File size in bytes.
*   Timestamps (creation, modification, access).
*   Pointers to the physical data blocks on disk where the file's contents are stored.

An inode does *not* store the file name (which is cached in a [directory entry or dentry](file-system-vs-disk-latency.md)) or the actual file data.

## The Exhaustion Bottleneck

On many traditional Unix-like file systems (such as Linux ext3 and ext4), **the total number of inodes is fixed when the file system is formatted.** The kernel reserves a set percentage of disk space for the inode table, creating a strict upper limit on the total number of files and directories the partition can hold.

### Failure Symptoms
When an application creates millions of small files (such as web session files, cache fragments, email spools, or microscopic log files):

1.  The fixed inode table is completely filled.
2.  Any subsequent attempt to write a new file, create a directory, or append data that requires new metadata blocks will fail.
3.  The operating system returns a **"No space left on device" (`ENOSPC`)** error, even if a command like `df -h` shows that only 10% of physical disk bytes are used.

## Sizing and Diagnosis

*   **`df -h` vs. `df -i`:** Standard monitoring tools checking only block capacity (`df -h`) will miss this issue. SREs must monitor inode utilization using **`df -i`** to view the total, used, and free inode counts and percentages.
*   **Atypical Inode Density:** By default, ext4 allocates one inode for every 16 KB of block space. If the average file size on a volume is much smaller than 16 KB, the system will run out of inodes before running out of bytes.

## Mitigations

*   **Cleanup and Pruning:** Use automated cron scripts to delete or archive old session files, temporary files, and cache entries.
*   **Metadata-Efficient Storage:** Consolidate small files into single archive files (e.g., `.tar` or `.zip` files) or migrate them to object storage services (like AWS S3) which do not rely on local file system inodes.
*   **Format Tuning:** If a partition is designated for small-file storage, format it with a higher inode density by reducing the bytes-per-inode ratio (e.g., `mkfs.ext4 -i 4096` to allocate one inode per 4 KB block).
*   **Dynamic Inode File Systems:** Use modern file systems like **XFS** or **ZFS** which allocate inodes dynamically as needed, removing the fixed partition-time limit.
