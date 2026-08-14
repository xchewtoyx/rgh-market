---
type: concept
title: Data Minimization at Ingestion
description: >
  Dropping or tokenizing sensitive fields before they enter the pipeline,
  since data that was never collected can't leak later.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 7"
---

The first question worth asking when someone proposes encrypting a sensitive
field isn't how to encrypt it — it's whether the pipeline needs to collect
that field at all. "Data cannot leak if it is never collected." Dropping
unnecessary sensitive fields at ingestion, rather than defaulting to
forwarding everything downstream and cleaning it up later, removes the risk
at its cheapest possible point: before it exists anywhere in the pipeline to
be governed, secured, or retained.

Where identity tracking is genuinely required, apply tokenization or hashing
at ingestion time rather than downstream, so raw identifiers never propagate
further than the point where they're first replaced. Two caveats worth
carrying forward: encryption and hashing are not automatic "privacy magic
bullets" — most managed storage already encrypts at rest and in transit by
default, so the real residual risk is usually
[*access control*](data-access-policy-enforcement.md), not a
missing-encryption gap, and naive unsalted hashing can be trivially reversed
by anyone who can test a plausible input (a known customer email) against
the hash.

For the rare case where engineers genuinely need to work against live
sensitive production data (a bug that only reproduces there), the safer
default is **touchless production** — develop and test against simulated or
cleansed data, with fully automated deployment so no one routinely touches
live sensitive data — with a **broken-glass process** (two-person approval,
scoped and time-limited access tied to a specific issue) as the explicit,
audited exception path rather than an implicit standing privilege.
