---
type: concept
title: Replication Is Not a Backup
description: Database replication protects against hardware failure and localized downtime but does not protect against data corruption or user-error deletions, which propagate instantly to all replicas.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 26"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 2"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 18"
---

A common systems engineering error is conflating database replication with backup strategies. While both involve maintaining copies of data, they protect against completely different failure modes.

## The Core Difference

*   **Replication** is the real-time copying of data across multiple database nodes or geographic sites. Its primary purpose is to ensure high availability (minimal downtime) and load distribution.
*   **Backups** are periodic, immutable, point-in-time snapshots of the database stored in isolated environments. Their primary purpose is to preserve data history and ensure [durability as an SLI](durability-as-sli.md).

## Why Replication Fails to Protect Data Integrity

Replication does not protect against logical corruption or operator error:
1.  **Instantaneous Propagation of Errors**: If a software bug, runaway script, or human operator executes a destructive query (e.g., `DROP TABLE` or a malformed `DELETE`), that instruction is immediately propagated to all replica nodes.
2.  **Lack of Historical Recovery**: Once the corrupted state is written to the primary, the previous correct state is lost across all replicas.

## Mitigation Architecture for Data Integrity

To defend against logical data loss, reliability engineering employs a multi-layered approach:
*   **Soft Deletion (Trash Bin Pattern)**: Design systems where deletion requests mark records as "deleted" but do not immediately purge them from disk, allowing recovery within a buffer window (e.g., 30 days).
*   **Point-in-Time Recovery (PITR)**: Utilize database transaction logs and snapshot histories to restore the system state to the exact millisecond before the corruption or error occurred.
*   **Off-site Immutable Backups**: Maintain off-line or write-once-read-many (WORM) storage copies of snapshots that are physically and logically isolated from the production network to prevent ransomware or compromised administrator accounts from destroying backup history.
*   **Data Integrity Verification**: Establish procedures to verify restored data against cryptographic signatures or known good states. When recovering from prolonged corruption or compromises, ensure the recovery point is old enough to avoid reintroducing corrupted/malicious states, and be prepared for custom data splicing to reconcile valid transactions with historical backups.
