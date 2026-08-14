---
type: concept
title: Backup and Restore Integrity
description: >
  Backups need the same integrity protection as primary storage, restores
  must validate it, and compartmentalized data plus routinely exercised
  partial restores determine real recovery time.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 9"
---

# Backup and Restore Integrity

"No one cares about backups; they only care about restores." For
persistent data, [recovery](design-for-recovery.md) has security
dimensions beyond the classic reliability ones:

- **Protect backups like primary storage.** A malicious
  [insider](insider-risk.md) can corrupt your backups and then force a
  restore from them. Cryptographic signatures over backups are useless if
  restore tooling doesn't *validate them during restore*, or if access
  controls don't restrict who can manually create signatures.
- **Compartmentalize the data.** Isolate detected corruption to the
  smallest practical subset and validate/restore just that: restoring
  0.01% of the data is fast only if you can identify and integrity-check
  that subset without reading the other 99.99%. Chunk size trades storage
  and compute overhead against MTTR; good large-system design tends to
  compartmentalize naturally
  ([compartmentalization](compartmentalization.md)).
- **Exercise restores through migrations.** A data migration is
  essentially a low-priority partial restore; sharing infrastructure
  between migrations and restores means every routine migration builds
  evidence and confidence in the recovery path
  ([continuous validation](continuous-validation.md)).
- **Don't resurrect deleted data.** Deletion is often legally required;
  recovery systems must not quietly restore data assumed destroyed. Mind
  the distinction between deleting encrypted data and deleting its
  encryption keys — key destruction is an efficient deletion mechanism
  *only* if keys are compartmentalized per data type compatibly with
  granular deletion requirements. [Soft deletion](soft-deletion-recovery-window.md)
  is the deliberate exception to "don't resurrect": a defined, bounded
  window where a delete is reversible on purpose, before the same
  irreversibility takes over.
