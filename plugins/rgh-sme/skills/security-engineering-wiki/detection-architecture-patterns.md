---
type: concept
title: Detection Architecture Patterns
description: >
  Two ways to centralize attack detection in the architecture itself —
  validating individual messages at a boundary versus watching aggregate
  usage patterns — so detection logic isn't scattered and reinvented.
sources:
  - title: Software Architecture in Practice, 4th Edition
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 11"
---

# Detection Architecture Patterns

Two recurring architectural shapes concentrate attack detection into one
place instead of scattering ad hoc checks across every component:

**Intercepting validator.** A wrapper component sits between a message
source — especially valuable when that source is external — and its
destination, and every message passes through it before delivery. Its
core job is verifying message integrity (checksums, hashes against
tampering), but the same choke point is a natural place to also fold in
intrusion detection, denial-of-service detection, and delivery-anomaly
detection (abnormal timing or connection patterns that suggest a
man-in-the-middle), because they all need to inspect traffic at the same
boundary. The tradeoff is a permanent latency cost on every message, and
that intrusion signatures drift — the validator needs the same ongoing
maintenance as any other component that encodes a signature database.

**Intrusion prevention system (IPS).** Rather than validating individual
messages, an IPS is a standalone element that profiles *aggregate usage
patterns* over time, allowing traffic that looks normal and blocking (and
reporting) traffic that doesn't. Because it reasons over patterns rather
than single messages, one IPS deployment can cover most of both the
detection and reaction tactics at once. The tradeoffs mirror the
validator's: a continuously updated pattern database, a performance cost,
and — since IPS is commonly bought rather than built — a fit that may not
match your specific application's traffic shape as precisely as a
purpose-built check would.

Both patterns are instances of the same underlying architectural move as
[safe proxies](safe-proxies.md) and
[secure-by-construction frameworks](secure-by-construction-frameworks.md):
put a security property behind one enforced boundary that every relevant
interaction is forced through, rather than trusting every caller or every
component to implement it correctly on its own. Findings from either
pattern feed the same [audit log](audit-log-design.md) and
[security log](security-log-design.md) machinery used for investigation
and [digital forensics](digital-forensics.md).
