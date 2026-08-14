---
type: concept
title: Continuous Integrity Auditing
description: Treating verification as an ongoing background process rather than a one-time check, since silent corruption can occur after a fact was first confirmed true.
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 12"
---

# Continuous Integrity Auditing

Verifying a claim or a stored fact once is not the same as it staying true. Data (and by extension, previously-verified claims about that data) can be silently corrupted after verification — by hardware bit-flips, storage degradation, or an unnoticed edit — with no visible signal that anything changed. **Continuous integrity auditing** is the practice of re-checking previously-verified state on an ongoing basis against an independent reference, rather than treating verification as a single pass/fail event that stays valid indefinitely.

## Timeliness vs. Integrity — Why This Matters More Than It Looks
Two distinct ways a verified claim can go wrong later:
- **Timeliness violations**: the claim was true when checked but is now stale (the underlying fact changed through a normal, visible process). This is recoverable once someone re-checks it, but — as with any [stale evidence](stale-evidence-maintenance.md) — it does not self-correct without a maintenance process that actually triggers that re-check.
- **Integrity violations**: the claim or its supporting record has been silently corrupted, lost, or falsified with no visible trace. Unlike staleness, nothing in the ordinary flow of information will surface this on its own — the record just looks confirmed and correct until someone checks it again.

Integrity violations are the more dangerous failure mode precisely because they are invisible by default: a reviewer who verified a fact once has no natural signal telling them to verify it again.

## Verification Action
- Don't treat "verified" as a permanent stamp on a claim, dataset, or document — especially for records that are read/relied-upon far more often than they are re-examined, since corruption there can compound silently for a long time (see [ephemeral source preservation](ephemeral-source-preservation.md) for a related failure of trusting a source will remain unchanged).
- Where a record's correctness matters over time (a source archive, a dataset a chain of claims depends on, a compliance record), build in periodic re-verification against an independent check — a checksum, a hash comparison against a known-good copy, or cross-referencing an immutable log of how the record arrived at its current state — rather than relying solely on the verification performed at creation time.
- Favor recording claims and their supporting evidence in an append-only, tamper-evident form (an immutable log or history) over overwriting records in place: an append-only record preserves the provenance trail needed to reconstruct how a claim came to be believed true, which is what makes later re-auditing possible at all. This complements — but doesn't replace — the audit-trail discipline in [verification accounting](verification-accounting.md).
