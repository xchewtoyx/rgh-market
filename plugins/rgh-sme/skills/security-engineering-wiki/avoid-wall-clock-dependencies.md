---
type: concept
title: Avoid Wall-Clock Dependencies
description: >
  Wall-clock time is state you can't control; recovery and certificate
  validity should rest on rates, epochs, version numbers, or validity
  lists instead.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 9"
---

# Avoid Wall-Clock Dependencies

Time of day is a form of state you generally cannot alter, so anywhere a
system incorporates wall-clock time threatens
[recovery](design-for-recovery.md): replaying signed transactions fails if
certificates have expired since; databases expecting monotonic time
recover badly from corruption; inaccurate clocks make cross-system log
correlation error-prone. External time you don't control is worse still —
Y2K/epoch rollovers, certificates with far-future expiry ("not my problem
anymore"), unauthenticated NTP under attacker-controlled networks. A fixed
date or offset in code is a time-bomb smell.

**Alternatives to tying events to wall-clock time**:

- **Rates** — a backstop rate limit works even without knowing the time
  of day; where waiting is genuinely wanted, measure *elapsed* time, not
  absolute time.
- **Manually advanced progress**: epoch or version numbers — an integer
  the whole system coordinates on for "valid vs. expired," stored in a
  lock service or ratcheted forward locally. You can advance rapidly to
  release fast, or *halt advancement* during trouble to debug — which
  removes the temptation to disable certificate verification wholesale
  when things age out mid-incident. Guard against adversarial
  acceleration/rollover: a large (64-bit) value plus a hardcoded backstop
  rate (e.g. one increment per second gives billions of years).
  [Fencing tokens](fencing-tokens.md) are the same idea applied to
  revoking a stale actor's authority instead of a credential's validity
  window.
- **Validity lists** — Google's ALTS certificates carry no expiration
  time at all; an actively pushed revocation list defines valid vs.
  revoked serial ranges. Periodic pushes create time compartments;
  emergency pushes revoke suspect keys; pausing pushes enables forensics.
  See [explicit revocation](explicit-revocation.md).

Deliberately time-bounded access (e.g. daily reauthentication) is the
legitimate exception — but the repair path for the system must not itself
rely on wall-clock time. Better to omit expiry from an SSH key pair than
to be forced to *skip validity checking* during recovery; the cure of
disabled verification is worse than the disease of aging certificates.
