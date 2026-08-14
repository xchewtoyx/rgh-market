---
type: concept
title: Intended State
description: >
  Recovery means returning to a known good state, which requires
  thoroughly encoding the intended state at every layer — host, firmware,
  global services — and continuously comparing deployed state against it.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 9"
---

# Intended State

[Recovery](design-for-recovery.md) from any error class means returning
to a known good state — which requires *knowing* the intended state and
being able to *read* the deployed state. Not knowing is a common root
problem. Even "stateless" services have state (code version, ports,
startup behavior); the more thoroughly you encode intended state and
reduce mutable state per layer, the easier it is to recognize you're back
to good. This encoding is the foundation of automation, intrusion
detection, and recovery alike.

**Host layer.** Google machines continuously checksum every file on their
local filesystem; a central service compares these maps against each
machine's assigned package set and records deviations, which are repaired.
One mechanism catches everything: cosmic-ray bit corruption, a rollout for
one component accidentally touching another's file, and out-of-band local
modification — accidental *or malicious*. In-memory state is covered by
idempotent `post_install`/`pre_rm` commands per package (e.g. restart
sshd when its config file is repaired). Security payoffs: every deviation
can be inspected for malice; an attacker who plants shellcode without
reverse-engineering the repair system finds their changes reverted *and
logged*, making track-covering much harder. At this abstraction all state
changes are equal — a failed-canary rollback and an emergency bash update
are routine changes through one rate-limited, auditable pipeline.
(Reimaging the machine on any deviation is the cruder, more disruptive
alternative.)

**Firmware layer.** Track at least each device's firmware version;
ideally all its settings. Packages carry an *activation check* — a
script with hardware-specific knowledge that periodically verifies
correct installation and reports deviations, keeping hardware complexity
out of the generic monitoring daemon and putting remediation with subject
experts. Why it matters: timekeeping cards with two firmware chips and
leap-second bugs decide whether the fleet can serve accurate time at all;
BIOS boot order (SATA before USB) blocks a datacenter intruder's USB
boot; the database of keys allowed to sign BIOS updates needs tracking
against tampering. Crucially, manage the state of *inactive* fallback
images and secondary devices too — recovery is a bad time to discover
what bugs live in the image you've never run.

**Global services.** The most persistent layers — storage, naming,
identity — are the hardest to recover. Support multiple instances from
the very first deployment, even for intended singletons: beyond
backup/restore, you may need to rebuild the entire system. Capture how
the service is created (declarative config, turnup automation) — like
test-driven development for infrastructure. Hermetic containers capture
much by default, but don't be lulled: restoring from scratch exercises
the full dependency chain and surfaces capacity shortfalls, quota limits,
and organically grown circular dependencies. Disaster-test it under
controlled conditions.

For the data itself, see
[backup and restore integrity](backup-and-restore-integrity.md).
