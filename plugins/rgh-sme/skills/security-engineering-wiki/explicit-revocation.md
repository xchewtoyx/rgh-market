---
type: concept
title: Explicit Revocation Mechanisms
description: >
  Revoking compromised credentials via centrally managed, distributed
  revocation lists — designed so the revocation system itself can't be
  weaponized to deny service or fail open under attack.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 9"
---

# Explicit Revocation Mechanisms

When an attacker holds valid credentials (say, an SSH key pair with login
access to a server cluster), a revocation system lets you cut that access
and recover control. But a revocation system is itself a high-value
mechanism whose accidental or malicious use has consequences — design for
that from the start.

- **Central validity service, careful with fail-open.** A centralized
  certificate-validity database prioritizes security but becomes a
  dependency: if it's down, everything is down, and the temptation to
  fail open is strong. Failing open circumvents the very protection —
  even *partial* fail-open is exploitable: if the validity database
  accepts all properly signed credentials whenever its time/epoch service
  is unreachable, then a simple DoS on the time service resurrects every
  old revoked credential for the attack's duration. Instead, distribute
  known-good revocation lists that nodes cache locally and act on until
  better data arrives — best-understanding beats time-out-and-allow. See
  [fail safe versus fail secure](fail-safe-vs-fail-secure.md).
- **Don't smear ground truth across the fleet.** Directly editing
  `authorized_keys`/`known_hosts` on servers scales poorly and makes "is
  this key gone everywhere?" unanswerable. Centrally manage keys and
  certificates and distribute state as a revocation list, using your
  usual file-update, monitoring, and rate-limiting machinery — recovery
  becomes "push a file," a process you already trust. This also
  [removes wall-clock dependence](avoid-wall-clock-dependencies.md) from
  certificate validation: pushed root-key and revocation files are things
  you directly control, unlike time distribution, and incorrect time
  otherwise re-validates old certs (letting attackers in) or fails valid
  ones (outage).
- **Safeguard revocation at scale against abuse.** A partially
  compromised attacker may try to revoke *your* credentials — potentially
  every valid credential in the infrastructure. Blindly replacing a Key
  Revocation List invites a one-push total outage; instead, have each
  server evaluate a new KRL and refuse any update that revokes its own
  credentials. A KRL revoking all hosts is then ignored by all hosts, and
  the attacker's best move (revoke half) leaves half your fleet running —
  recovering half is vastly easier than all.
- **No special emergency paths, no exempt accounts.** A dedicated
  rarely-used "emergency revocation list" won't work when needed; shard
  the regular list so emergency updates touch only a subset, using the
  same mechanism in normal and emergency operation (same logic as
  [emergency-push-is-normal-push](decouple-rollout-speed-from-policy.md)).
  And never create "special" accounts (e.g. senior-executive direct
  access) that bypass revocation — one successful attack on such an
  account defeats the entire mechanism.
