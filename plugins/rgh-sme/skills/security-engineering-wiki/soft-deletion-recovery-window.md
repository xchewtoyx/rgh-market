---
type: concept
title: Soft Deletion as a Recovery Window
description: >
  Route deletions through a delayed-purge holding state instead of an
  immediate hard delete, so an accidental or malicious deletion stays
  recoverable for a defined window instead of being instantly permanent.
sources:
  - title: Site Reliability Engineering
    resource:
      "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 26,
      Data Integrity"
---

# Soft Deletion as a Recovery Window

An immediate, unrecoverable delete has exactly the same shape whether it
was triggered by a legitimate user, an operator's mistake, a bug, or a
malicious [insider](insider-risk.md) — the system can't distinguish
intent, and once the data is actually gone, intent stops mattering. Soft
deletion breaks that: a delete request moves the data into a "deleted but
retained" state rather than unlinking it immediately, and only a
separate, delayed purge step (commonly on the order of weeks) actually
destroys it. For that window, the deletion is fully reversible.

This turns data destruction — normally instantaneous and total — into
something with the same recoverability properties as any other change:
detectable and undoable within a bounded period. It complements rather
than replaces [backup and restore integrity](backup-and-restore-integrity.md):
a backup protects against losing data nobody meant to delete, while soft
deletion protects specifically against a delete action itself, whether
that action was legitimate, mistaken, or malicious, by giving the system
(or a human) time to notice and reverse it before the purge runs.

The purge window is a deliberate tradeoff, not a free extension of safety:
holding deleted data longer costs storage and keeps sensitive data alive
longer than a user who asked for deletion might expect, which cuts
against [data minimization](data-minimization.md) and any legal deletion
obligation. Where deletion must be provably permanent (compliance
requirements, a user's right-to-erasure request), soft deletion needs a
hard boundary — the purge must actually run, and running it should be
verifiable, not merely scheduled. This is the same trust question
[backup and restore integrity](backup-and-restore-integrity.md) raises
about key destruction as a deletion mechanism: a recoverability window and
a genuine deletion guarantee are in tension, and a system should be
explicit about which one it's promising for which class of data — see
[access classification by risk](access-classification-by-risk.md) for
deciding that per data class rather than picking one policy for
everything.
