---
type: concept
title: Emergency Access
description: >
  A minimal, low-dependency, still-access-controlled path to core
  administrative interfaces and responder communications for when normal
  access is completely broken.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 9"
---

# Emergency Access

All [recovery](design-for-recovery.md) depends on responders being able to
reach the system. When normal access methods are completely broken, there
are no further layers to absorb failure — emergency access must be both
maximally reliable and still secure. It comprises the minimum set of
technologies needed to reach core administrative interfaces (root on
network devices and machine OSs, application admin consoles) and to
communicate with other responders, while preserving access control as far
as possible. Google's approach: self-contained critical services on
geographically distributed racks, so during a global outage each reachable
rack anchors local recovery that expands radially — accepting the risks
of missing context and regional divergence for meaningfully faster
recovery.

**Access control.** The access-control service must not be a single point
of failure for all remote access. Alternatives should avoid the same
dependencies with *equally strong* policies, accepting worse convenience
and features. Emergency credentials can't derive from dynamic
infrastructure (SSO, federated identity) unless those have low-dependency
replacements — Google provisions offline alternate credentials and
alternate authentication/authorization algorithms, restricted to the few
responders who must move first while everyone else waits. Credential
lifetime is a hard tradeoff: short-lived credentials become a time bomb
if the outage outlasts them, and proactively issued ones may expire just
as the outage starts. Network-level authorization has parallel risks —
dynamic protocols (SDN) may need static alternatives, with monitoring
good enough to tell network-access failure from higher-layer failure.

**Communications.** Decide in advance what responders use when chat is
down — or compromised and eavesdropped
([incident opsec](incident-operational-security.md)). Prefer the fewest
dependencies adequate for team size; outsourced tools must be reachable
when layers outside your control are broken; phone bridges increasingly
ride IP telephony; self-hosted IRC is reliable and self-contained but
weak on authentication/confidentiality.

**Responder habits decide whether any of it works.** Unique emergency
tools plus stress plus rarely used processes obstruct access — humans,
not technology, are what render [breakglass](breakglass.md) tools
ineffective. Minimize the distinction between normal and emergency
process so habit carries responders (Google folded emergency mode into
the same Chrome-based access platform used daily). Enforce a minimum
practice cadence for emergency credentials and procedures (waivable for
those who exercise equivalents routinely), and keep policies, how-tos,
and architecture diagrams available — rarely used detail is forgotten,
and documentation relieves pressure and dependence on subject-matter
experts. Automation must never be allowed to disable these services (see
[graceful degradation](graceful-degradation.md)).

You're only as available as the sum of your dependencies: failures in
layers you don't control aren't actionable, so find cost-effective
redundancy where you can, and know where you'll simply have to wait.
