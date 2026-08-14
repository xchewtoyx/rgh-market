---
type: concept
title: Compartmentalization and Blast Radius
description: >
  Deliberately creating small operational units with restricted access
  between them, so a breach or failure in one compartment does not
  jeopardize the rest of the system.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), chs. 1, 8"
  - title: Software Architecture in Practice, 4th Edition
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), chs. 11, 16"
---

# Compartmentalization and Blast Radius

Compartmentalization creates small individual operational units and limits
access to and from each one — like a ship's compartments keeping one
breach from sinking the vessel. On a single flat network, one compromised
credential can reach every device; segmented (e.g. VLANs with network
ACLs, per-segment access for specific classes of users and services), a
breach or overload in one compartment stays there. A **DMZ** is the
canonical instance at the network-perimeter level: a zone between the
internet and the internal network, bounded by a firewall on each side, so
externally reachable services sit in a compartment whose own reach into
the intranet is separately filtered and minimized rather than trusted by
default. Compartment barriers
should constrain attackers *and* accidental failures alike — this is the
structural expression of limiting blast radius, and a core layer of
[defense in depth](defense-in-depth.md). It also limits an adversary's
ability to use a compromised host or stolen credential to move laterally
or escalate privilege; scoping credentials (e.g. to a geographic region)
is one direct implementation.

**Boundaries need enforceable identity.** A compartment must permit some
access but not unrestricted access, which requires recognizing endpoints
and confirming identity: mutually authenticated RPCs certify both parties
and can carry extra metadata (e.g. location) for decisions like rejecting
nonlocal requests.

**Granularity is a tradeoff.** Per-RPC-method compartments align with
logical application boundaries and scale linearly with features — a good
balance. Constraining acceptable *parameter values* per method is tighter
but scales with number of clients and compounds coordination cost;
compartments wrapping a whole server are cheap but weak. Consult incident
management and operations teams when choosing — they are the ones who will
seal compartments during a response. Even imperfect compartments help: an
attacker probing edge cases may slip and alert you, and escape time is
response time. Per-customer isolation is the same tradeoff at product
level: shared instances risk cross-tenant leaks via the virtualization
layer; dedicated hardware eliminates that at a utilization premium. The
leak vector isn't only concurrent tenants sharing hardware — it's also
*sequential* tenants: a hypervisor or container runtime must actively
scrub memory, disk, and reused network identifiers (MAC/IP addresses)
between one tenant's use of a physical resource and the next's, or a later
tenant inherits an earlier one's residue.

**Operational payoffs during incidents**:

- Responses proportional to the incident — disable parts, not the whole
  system.
- Quarantine without sacrificing evidence: freeze some compartments for
  forensics while recovering others.
- Natural boundaries for replacement and repair — jettison a compartment
  to save the rest.

**Separation dimensions** (Google compartmentalizes on all three):
[role](role-separation.md), [location](location-separation.md), and time
(see [credential rotation](credential-rotation.md)). For redundancy-based
functional isolation on top of these, see
[failure domains](failure-domains.md).

Compartments only add resilience while the separation *holds*: validate
continuously that operations prohibited across boundaries actually fail,
and flag unexpected successes in logs
([continuous validation](continuous-validation.md)).
