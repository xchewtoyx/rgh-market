---
type: concept
title: Location Separation
description: >
  Confine the impact of a compromise to the location where it happens —
  via per-location roles, trust roots, and key trees — while never letting
  physical location itself confer trust.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 8"
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 2"
---

# Location Separation

Location separation limits an attacker's reach along the *where*
dimension: physically compromising one datacenter shouldn't let them read
data in the others, and even your most powerful administrators can have
region-limited access to mitigate [insider risk](insider-risk.md).
Physical location is a natural [compartment](compartmentalization.md)
border because many adverse events are location-bound — natural disasters,
fiber cuts, power outages, fires, and any attack requiring physical
presence (few adversaries below state level can be in many places at
once).

Mechanisms:

- **Run the same microservice as different roles per location**
  (datacenter/region), protecting instances from each other with normal
  access controls — [role separation](role-separation.md) along a second
  axis.
- **Trust isolation.** Default-deny cross-location communication; allow
  only expected flows, with per-API granularity (user-facing APIs are
  often global, control-plane APIs constrained), and give teams tooling to
  measure, define, and enforce per-API location limits. Identities carry
  location metadata: each location runs its *own* job-control system that
  certifies jobs with that location's metadata, and machines accept jobs
  only from their local one — a single central authority would itself be a
  high-value target. A per-location root of trust, with the trusted-root
  list distributed fleet-wide, lets every machine detect cross-location
  spoofing and lets you revoke an entire location's identity.
- **Confidentiality isolation.** Per-location key trees: root keys placed
  only in their location, key access gated by trust isolation, so
  exfiltrated ciphertext from one branch can't be decrypted with another
  branch's keys. Transitioning from a global tree is gradual — a leaf is
  isolated only once every key above it is local.
- **Align physical and logical boundaries.** Segment networks on both
  network-level and physical risk: corporate vs. production in separate
  buildings; high-visitor-traffic areas subdivided. Compartmentalize
  secrets/keys/credentials to physical servers — e.g. a certificate per
  datacenter rather than one shared across all servers, so a physical
  compromise means draining and revoking *that* datacenter's cert while
  the rest keep serving. Ensure multi-region services have no critical
  dependency single-homed in one datacenter.

**The limitation — location must not imply trust.** Under zero trust
([BeyondCorp](zero-trust-networking.md)), a workstation is trusted by
machine certificate and configuration assertions; an untrusted device on
an office port lands in a guest VLAN. Google doesn't even trust
datacenter interiors: a red team once planted a wireless implant on a rack
— and a helpful technician, assuming legitimacy, zip-tied its cabling
neatly. Production trust is rooted in per-machine credentials, so an
unauthorized implant is simply not trusted. Location separation confines
*your* compromised assets; presence in a location must never authenticate
anyone.

**Location cuts the other way too: the administrator's location can itself
be the violation**, independent of where the data sits or any breach
occurring. A routine, fully approved change made by an in-jurisdiction
engineer against data governed by a foreign data-protection regime (e.g. a
non-EU administrator touching EU-resident data under the EU's regime) can
be a compliance violation purely because of *who* reached across the
boundary, not because anything was mishandled. Access-control design for
globally distributed teams needs to encode administrator jurisdiction as
its own dimension, separate from data location and separate from the
attacker-containment reasoning above.
