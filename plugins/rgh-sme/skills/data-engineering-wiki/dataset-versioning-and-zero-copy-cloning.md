---
type: concept
title: Dataset Versioning and Zero-Copy Cloning
description: >
  Keeping prior versions of a dataset addressable for recovery and history
  tracking, and the low-cost virtual-copy technique object storage makes
  possible.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 6"
---

Versioning a dataset in object storage — keeping old versions addressable
instead of discarding them on overwrite — serves two pipeline concerns:
recovering from a corrupting process failure (roll back to the last known
good version rather than trying to hand-repair bad output), and tracking a
dataset's history well enough to diagnose why a downstream model's
performance changed, the data equivalent of using code version control to
find the commit that introduced a bug.

**Zero-copy cloning** is a specific technique this enables: an
object-storage-based platform can create a new virtual copy of a table by
pointing new references at the existing underlying files, without
physically duplicating any data — a "shallow copy" in the same sense
Python uses the term. Future writes to either the original or the clone
diverge independently from that point on, without needing to copy anything
up front. The real risk is that deleting the *original* object's underlying
files can also destroy a clone that still points at them — a pipeline
engineer needs to know exactly how a given platform's shallow copy behaves
before deleting raw files, since fully managed platforms typically hide this
mechanic while lower-level lake tooling exposes it directly (a capability
that's genuinely useful and genuinely dangerous in the same breath). Where
that risk isn't acceptable, some platforms also support **deep copying** —
physically duplicating all underlying files — at higher storage cost but
without the shared-file exposure.

A related managed-platform feature is **time travel**: the ability to query
or clone a table as it existed at a previous point in time, without the
pipeline having explicitly snapshotted that version itself. This turns an
accidental bad write or a dropped table into a recoverable event (query the
prior state, or clone it back) rather than a permanent loss, and it's built
on the same underlying versioned-storage mechanics as zero-copy cloning —
old data isn't actually deleted on write, just no longer referenced by the
table's current pointer, until it ages out of the configured retention
window. Retention duration is a direct cost/recoverability trade-off, the
same one [data temperature tiering](data-temperature-tiering.md) describes
for any other retained-but-rarely-accessed data.
