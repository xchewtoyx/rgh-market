---
type: concept
title: Design for Recovery
description: >
  Prepare at design time to return a failed or compromised system to a
  known good state, with change mechanisms fast enough for emergencies and
  guarded by policy.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 9"
---

# Design for Recovery

Even the most secure and [resilient](design-for-resilience.md) systems
eventually need humans to intervene and recover them. Recovery is complex
in unanticipated ways: rolling back an unstable release may reintroduce
patched vulnerabilities; rolling forward a security patch may introduce
instability; fast deployment wins the race against attackers but limits
testing. These tradeoffs must be designed for in advance — mid-incident is
the wrong time to discover them.

**What you recover from** — four classes, and the advice is not to
over-classify edge cases but to be ready for all of them:

- *Random errors*: hardware fails, bit flips silently, disasters strike.
- *Accidental errors*: humans with good intent err, more as task
  complexity rises; a meaningful fraction of Google outages traced to a
  unilateral human action with no engineering or procedural safety check.
- *Software errors*: bugs — delayed accidental errors — which can mimic
  or magnify the others.
- *Malicious actions*: [insiders](insider-risk.md) or attackers with
  stolen credentials; mitigation design is the same for both.

**Core principles**, each its own note:

- Build change mechanisms to go
  [as fast as you'll ever need, guarded by policy](decouple-rollout-speed-from-policy.md)
  — the emergency push system should be the normal push system at maximum.
- [Limit dependencies on wall-clock time](avoid-wall-clock-dependencies.md)
  — time is state you can't control.
- Manage the [rollback/security tradeoff](rollback-security-tradeoff.md):
  roll back freely for reliability, but stop attackers from rolling you
  back into known vulnerabilities.
- Use an [explicit revocation mechanism](explicit-revocation.md) that
  can't be turned into a weapon against you.
- [Know your intended state, down to the bytes](intended-state-recovery.md)
  — you can only return to a known good state if you know what "good" is;
  for persistent data, see
  [backup and restore integrity](backup-and-restore-integrity.md).
- Maintain [emergency access](emergency-access.md) for when normal access
  is completely broken.

Recovery processes do unusual tasks under unfamiliar conditions — test
them ([continuous validation](continuous-validation.md)), including
whether recovery instructions are readable and whether a second instance
of a "singleton" service can actually be created. Design core recovery
logic to be portable and unit-testable with faked hardware interfaces, so
failure modes you can't realistically reproduce end-to-end are still
exercised.

Side benefits sell the investment: machines engineered for authenticated
firmware update, rollback, and attestation can be automatically cleaned
and repurposed, and reduce supply-chain security burden — first-touch
provisioning simply *is* the recovery procedure, which also means recovery
gets exercised routinely.
