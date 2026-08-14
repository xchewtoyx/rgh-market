---
type: concept
title: Digital Forensics
description: >
  Reconstructing an attacker's steps via imaging, log and malware
  analysis, and a forensic timeline — expanding through pivot points and
  sharded forensics/reversing/hunting teams until leads dry up.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 17"
---

# Digital Forensics

Investigating a compromise means backtracking through each phase of the
attack to reconstruct the attacker's steps, identifying everything they
touched. Core techniques:

- **Forensic imaging** — secure read-only copy (with checksum) of
  storage, preserving state without damaging originals (courts want the
  images).
- **Memory imaging** — process trees, running executables, even
  passwords to files the attacker encrypted.
- **File carving** — recovering "deleted" files (e.g. logs the attacker
  wiped) from unlinked-but-not-zeroed disk regions.
- **Log analysis** — the system's own logs plus network and neighboring
  systems' logs (see [security log design](security-log-design.md)).
- **Malware analysis** — reversing attacker tools for capabilities and
  indicators of compromise (IOCs), fed back to forensics and detection.

Relationships between events matter as much as events: build a
**forensic timeline** — a chronologically ordered event list that
establishes correlation and causation of attacker activity.

**Pivot points drive scope.** Start hands-off (per
[incident OpSec](incident-operational-security.md) — no account
lockouts on first instinct) with the initial questions: how did the
backdoor arrive, what can it do, where else does it exist, what did the
attacker do here? Each answer spawns new questions — the file share the
attacker reached becomes its own forensic subject with the same question
set.

**Shard when staffed**: a *Forensics* group investigating touched
systems, a *Reversing* group extracting IOC fingerprints from binaries,
and a *Hunting* group sweeping all systems for those fingerprints,
feeding hits back to Forensics — with the operations lead keeping the
loop between them tight.

**When to stop**: the popcorn rule. When the interval between new
discoveries noticeably lengthens, you likely know enough to remove the
attacker and protect the target data — move to remediation before the
bag burns. You will not have learned everything; that's expected. The
[remediation lead's plan](security-crisis-management.md) should already
be waiting.
